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

# Chargement automatique de rag/code/.env (S1ter Lot S1c.1)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import _env  # noqa: F401  # side-effect: load_env() au moment de l'import

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
    # S2.3 Lot D : format mixte (str | list[str]) pour supporter les
    # synonymes (option B). asdict() sérialise correctement les listes
    # imbriquées en JSON.
    expected_concepts: list
    cited_codes: list[str]
    sources_match: list[str]
    sources_missing: list[str]
    concepts_match: list
    concepts_missing: list
    score_global: int
    answer_preview: str

    def to_dict(self) -> dict:
        return asdict(self)


# ============================================================
# Matching sémantique des concepts attendus — S2.3 Lot D
# ============================================================

def concept_matched(concept_entry, answer_text_lower: str) -> bool:
    """Détecte si un `concept` attendu est présent dans la réponse.

    Format option B retenu en S2.3 (cf. BRIEF-CC-S2.3 §4) — un concept
    peut prendre deux formes dans `expected_concepts` :

    - **Scalaire (str, cas v1)** : match littéral sous-chaîne case-
      insensitive.
    - **Liste de synonymes (list[str])** : match dès qu'**au moins un**
      synonyme apparaît dans la réponse (rétro-compat des dérivés
      lexicaux : méthode/méthodologie, vérification/vérifier,
      « 1,8 heures »/« 1,8 heure », persistant/persistance, etc.).

    Cas dégénéré : liste vide → False + warning stderr (un concept liste
    sans synonymes ne peut jamais matcher — à signaler à Cowork pour
    enrichissement du golden set).

    Le paramètre s'appelle `answer_text_lower` pour rappeler le contrat
    d'appel (texte de réponse déjà lowercased par `evaluate_one()`).
    Pour la robustesse face à un usage direct hors-pipeline, la fonction
    re-applique défensivement `.lower()` à la réponse.
    """
    answer = answer_text_lower.lower() if answer_text_lower else ""
    if isinstance(concept_entry, list):
        if not concept_entry:
            print(
                "[warn] concept_matched: liste de synonymes vide — "
                "concept dégénéré, ne pourra jamais matcher",
                file=sys.stderr,
            )
            return False
        return any(str(syn).lower() in answer for syn in concept_entry)
    return str(concept_entry).lower() in answer


def evaluate_one(question_entry: dict, result_dict: dict) -> EvalItem:
    expected_sources = [s.lower() for s in question_entry.get("expected_sources", [])]
    # S2.3 Lot D : on préserve le format mixte (str | list[str]) sans
    # applatir en lowercase ici — concept_matched() gère les deux formes.
    expected_concepts = list(question_entry.get("expected_concepts", []))
    cited = [c.lower() for c in result_dict.get("cited_codes", [])]
    answer_text = (result_dict.get("answer") or "").lower()

    sources_match = [s for s in expected_sources if s in cited]
    sources_missing = [s for s in expected_sources if s not in cited]
    concepts_match = [c for c in expected_concepts if concept_matched(c, answer_text)]
    concepts_missing = [c for c in expected_concepts if not concept_matched(c, answer_text)]

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

    # S2.2 Lot C — affichage du cumul coût accumulé
    try:
        import _cost  # noqa: F401
        summary = _cost.summarize_cost()
        if summary["total_calls"] > 0:
            print(_cost.format_cost_summary(summary))
    except Exception:
        pass

    sources_ok = sum(1 for i in items if i.sources_match)
    return 0 if sources_ok >= 8 else 1


if __name__ == "__main__":
    sys.exit(main())
