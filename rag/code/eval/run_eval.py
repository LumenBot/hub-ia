#!/usr/bin/env python3
"""
Évaluation du golden set RAG — v1
=================================

Rejoue les 10 questions de `rag/eval/questions.yaml` via le backend `query.py`
et produit un rapport de matching :

  * `sources_match` : codes attendus retrouvés dans `cited_codes`
  * `concepts_match`: termes attendus présents (sous-chaîne case-insensitive)
                      dans la réponse
  * `score_global`  : 1 si sources_match ≥ 1 ET ≥ 50% des concepts couverts,
                      0 sinon

Critère de succès brief §9 : ≥ 8/10 sources attendues citées,
≥ 7/10 réponses jugées utiles au sondage manuel Blaise (note saisie a
posteriori dans golden-answers.yaml).

Usage :
    python3 rag/code/eval/run_eval.py
    python3 rag/code/eval/run_eval.py --questions PATH --report PATH

Réfs : brief §9, D-019, DEP-02 (Stitch → Evaluate → Iterate).
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import sys
from dataclasses import asdict, dataclass

try:
    import yaml
except ImportError:
    print("[erreur] pyyaml requis", file=sys.stderr)
    sys.exit(2)


ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DEFAULT_QUESTIONS = os.path.join(ROOT, "eval", "questions.yaml")
DEFAULT_GOLDEN = os.path.join(ROOT, "eval", "golden-answers.yaml")
QUERY_SCRIPT = os.path.join(ROOT, "code", "backend", "query.py")


def _load_query():
    spec = importlib.util.spec_from_file_location("query", QUERY_SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


# ============================================================
# Évaluation d'un item
# ============================================================

@dataclass
class EvalItem:
    id: str
    question: str
    expected_sources: list[str]
    expected_concepts: list[str]
    cited_codes: list[str]
    sources_match: list[str]
    sources_missing: list[str]
    concepts_match: list[str]
    concepts_missing: list[str]
    score_global: int
    answer_preview: str

    def to_dict(self) -> dict:
        return asdict(self)


def evaluate_one(question_entry: dict, result_dict: dict) -> EvalItem:
    expected_sources = [s.lower() for s in question_entry.get("expected_sources", [])]
    expected_concepts = [c.lower() for c in question_entry.get("expected_concepts", [])]
    cited = [c.lower() for c in result_dict.get("cited_codes", [])]
    answer_text = (result_dict.get("answer") or "").lower()

    sources_match = [s for s in expected_sources if s in cited]
    sources_missing = [s for s in expected_sources if s not in cited]
    concepts_match = [c for c in expected_concepts if c in answer_text]
    concepts_missing = [c for c in expected_concepts if c not in answer_text]

    has_source = bool(sources_match)
    concept_ratio = len(concepts_match) / max(1, len(expected_concepts))
    score = 1 if (has_source and concept_ratio >= 0.5) else 0

    return EvalItem(
        id=question_entry["id"],
        question=question_entry["question"],
        expected_sources=expected_sources,
        expected_concepts=expected_concepts,
        cited_codes=cited,
        sources_match=sources_match,
        sources_missing=sources_missing,
        concepts_match=concepts_match,
        concepts_missing=concepts_missing,
        score_global=score,
        answer_preview=(result_dict.get("answer") or "")[:240].replace("\n", " "),
    )


# ============================================================
# Orchestration
# ============================================================

def run_eval(questions: list[dict], runner) -> list[EvalItem]:
    items: list[EvalItem] = []
    for q in questions:
        result = runner(q["question"])
        items.append(evaluate_one(q, result))
    return items


def format_report(items: list[EvalItem]) -> str:
    total = len(items)
    sources_ok = sum(1 for i in items if i.sources_match)
    concepts_full = sum(1 for i in items if not i.concepts_missing)
    score_ok = sum(1 for i in items if i.score_global == 1)

    lines: list[str] = []
    lines.append("=" * 70)
    lines.append("ÉVAL GOLDEN SET — rapport")
    lines.append("=" * 70)
    lines.append(f"Questions : {total}")
    lines.append(f"Sources attendues retrouvées : {sources_ok}/{total}")
    lines.append(f"Concepts attendus pleinement couverts : {concepts_full}/{total}")
    lines.append(f"Score global (source + ≥50% concepts) : {score_ok}/{total}")
    lines.append("")

    for it in items:
        flag = "✅" if it.score_global else "❌"
        lines.append("-" * 70)
        lines.append(f"{flag} {it.id} — {it.question}")
        lines.append(f"   Sources attendues : {it.expected_sources}")
        lines.append(f"   Sources citées    : {it.cited_codes}")
        if it.sources_missing:
            lines.append(f"   ⚠ manquantes     : {it.sources_missing}")
        lines.append(f"   Concepts trouvés  : {it.concepts_match}")
        if it.concepts_missing:
            lines.append(f"   ⚠ concepts absents: {it.concepts_missing}")
        lines.append(f"   Extrait réponse   : {it.answer_preview[:200]}")
    lines.append("")
    target = "✅ cible atteinte" if sources_ok >= 8 else "⚠ cible (8/10 sources) non atteinte"
    lines.append(f"Critère brief §9 : {target}")
    return "\n".join(lines) + "\n"


# ============================================================
# Adapter : runner réel (CLI) ou mocké (tests)
# ============================================================

def make_real_runner():
    """Construit un runner qui appelle answer_question() avec le backend complet."""
    query_mod = _load_query()
    embedder = query_mod.Embedder()
    retriever = query_mod.Retriever()
    generator = query_mod.Generator()

    def runner(question: str) -> dict:
        return query_mod.answer_question(question, embedder, retriever, generator).to_dict()

    return runner


# ============================================================
# CLI
# ============================================================

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Évaluation golden set RAG.")
    parser.add_argument("--questions", default=DEFAULT_QUESTIONS)
    parser.add_argument("--report", default=None, help="chemin du rapport texte (défaut: stdout)")
    parser.add_argument("--json", default=None, help="dump JSON détaillé en plus du rapport")
    args = parser.parse_args(argv)

    if not os.path.exists(args.questions):
        print(f"[erreur] questions introuvables : {args.questions}", file=sys.stderr)
        return 2

    with open(args.questions, encoding="utf-8") as f:
        questions = yaml.safe_load(f) or []

    runner = make_real_runner()
    items = run_eval(questions, runner)

    report = format_report(items)
    if args.report:
        with open(args.report, "w", encoding="utf-8") as f:
            f.write(report)
    else:
        print(report)

    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump([i.to_dict() for i in items], f, ensure_ascii=False, indent=2)

    sources_ok = sum(1 for i in items if i.sources_match)
    return 0 if sources_ok >= 8 else 1


if __name__ == "__main__":
    sys.exit(main())
