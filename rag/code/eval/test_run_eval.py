"""Tests pour run_eval.py (matching sources + concepts).

Exécution :
    pytest rag/code/eval/test_run_eval.py -v
"""

from __future__ import annotations

import importlib.util
import os
import sys

import pytest


HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT_PATH = os.path.join(HERE, "run_eval.py")


def _load_run_eval():
    spec = importlib.util.spec_from_file_location("run_eval", SCRIPT_PATH)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


run_eval = _load_run_eval()


# ============================================================
# Tests : evaluate_one
# ============================================================

class TestEvaluateOne:
    def test_all_match_score_1(self):
        q = {
            "id": "q-001",
            "question": "Q?",
            "expected_sources": ["cu-008"],
            "expected_concepts": ["retrieval", "fine-tuning"],
        }
        r = {
            "answer": "Le RAG fait du retrieval et est différent du fine-tuning [CU-008].",
            "cited_codes": ["CU-008"],
        }
        item = run_eval.evaluate_one(q, r)
        assert item.score_global == 1
        assert item.sources_match == ["cu-008"]
        assert item.sources_missing == []
        assert set(item.concepts_match) == {"retrieval", "fine-tuning"}

    def test_source_manque_score_0(self):
        q = {
            "id": "q-002",
            "question": "Q?",
            "expected_sources": ["cu-008"],
            "expected_concepts": ["retrieval"],
        }
        r = {"answer": "Réponse avec retrieval mais sans citation.", "cited_codes": []}
        item = run_eval.evaluate_one(q, r)
        assert item.score_global == 0
        assert item.sources_missing == ["cu-008"]

    def test_source_ok_mais_concepts_insuffisants(self):
        q = {
            "id": "q-003",
            "question": "Q?",
            "expected_sources": ["dep-02"],
            "expected_concepts": ["stitch", "evaluate", "iterate", "production"],
        }
        r = {"answer": "Mention de production [DEP-02].", "cited_codes": ["DEP-02"]}
        item = run_eval.evaluate_one(q, r)
        # 1 concept sur 4 = 25% < 50%
        assert item.score_global == 0
        assert "stitch" in item.concepts_missing

    def test_case_insensitive(self):
        q = {
            "id": "q-004",
            "question": "Q?",
            "expected_sources": ["CU-001"],
            "expected_concepts": ["Veille"],
        }
        r = {"answer": "La VEILLE est essentielle [cu-001].", "cited_codes": ["cu-001"]}
        item = run_eval.evaluate_one(q, r)
        assert item.score_global == 1

    def test_sources_match_partiel(self):
        q = {
            "id": "q-005",
            "question": "Q?",
            "expected_sources": ["cu-008", "dep-02"],
            "expected_concepts": ["retrieval"],
        }
        r = {"answer": "Retrieval [CU-008].", "cited_codes": ["CU-008"]}
        item = run_eval.evaluate_one(q, r)
        assert item.sources_match == ["cu-008"]
        assert item.sources_missing == ["dep-02"]
        # Au moins une source citée + concept retrouvé → score 1
        assert item.score_global == 1


# ============================================================
# Tests : run_eval orchestration
# ============================================================

class TestRunEval:
    def test_runner_called_once_per_question(self):
        questions = [
            {"id": "a", "question": "Q1", "expected_sources": ["cu-001"], "expected_concepts": ["v"]},
            {"id": "b", "question": "Q2", "expected_sources": ["cu-008"], "expected_concepts": ["r"]},
        ]
        calls: list[str] = []

        def runner(q: str) -> dict:
            calls.append(q)
            return {"answer": "v r [CU-001] [CU-008]", "cited_codes": ["CU-001", "CU-008"]}

        items = run_eval.run_eval(questions, runner)
        assert calls == ["Q1", "Q2"]
        assert len(items) == 2
        assert all(i.score_global == 1 for i in items)


# ============================================================
# Tests : format_report
# ============================================================

class TestFormatReport:
    def test_summary_and_per_item(self):
        item_ok = run_eval.EvalItem(
            id="q1", question="?", expected_sources=["cu-001"], expected_concepts=["veille"],
            cited_codes=["cu-001"], sources_match=["cu-001"], sources_missing=[],
            concepts_match=["veille"], concepts_missing=[], score_global=1,
            answer_preview="ok",
        )
        item_ko = run_eval.EvalItem(
            id="q2", question="?", expected_sources=["dep-02"], expected_concepts=["stitch"],
            cited_codes=[], sources_match=[], sources_missing=["dep-02"],
            concepts_match=[], concepts_missing=["stitch"], score_global=0,
            answer_preview="ko",
        )
        report = run_eval.format_report([item_ok, item_ko])
        assert "1/2" in report  # sources_ok
        assert "q1" in report and "q2" in report
        assert "non atteinte" in report  # 1/2 < 8/10


# ============================================================
# Test : questions.yaml structure conforme
# ============================================================

class TestQuestionsYaml:
    def test_golden_set_10_questions(self):
        import yaml
        questions_path = os.path.join(os.path.dirname(HERE), "..", "eval", "questions.yaml")
        with open(questions_path, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        # S2.2 Lot B : extension 10 → 30 questions (20 nouvelles couvrant
        # vague 3.5 + transverses + cross-modules).
        assert len(data) == 30
        for entry in data:
            assert "id" in entry
            assert "question" in entry
            assert "expected_sources" in entry and entry["expected_sources"]
            assert "expected_concepts" in entry and entry["expected_concepts"]
            assert "unit" in entry

    def test_golden_set_couvre_5_unites_pilotes_et_extensions_s22(self):
        """Les 5 unités pilotes S1 doivent rester couvertes, plus les
        extensions S2.2 (briques transverses + cross-modules)."""
        import yaml
        questions_path = os.path.join(os.path.dirname(HERE), "..", "eval", "questions.yaml")
        with open(questions_path, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        units = {q["unit"] for q in data}
        # Les 5 unités pilotes S1 restent toutes représentées
        pilotes = {"cu-001", "cu-008", "pr-07", "dep-02", "outils-vector-db"}
        assert pilotes.issubset(units), f"unités pilotes manquantes : {pilotes - units}"
        # Couverture S2.2 attendue : transverses + cross-modules
        assert "pattern-llm-wiki" in units
        assert any(u.startswith("cross-") for u in units), "au moins 1 cross-modules attendu"

    def test_golden_answers_sous_ensemble_des_questions(self):
        """golden-answers peut être un sous-ensemble des questions (les
        20 nouvelles questions S2.2 Lot B n'ont pas encore leur golden-
        answer canonique côté Cowork — production différée)."""
        import yaml
        q_path = os.path.join(os.path.dirname(HERE), "..", "eval", "questions.yaml")
        a_path = os.path.join(os.path.dirname(HERE), "..", "eval", "golden-answers.yaml")
        with open(q_path, encoding="utf-8") as f:
            qs = yaml.safe_load(f)
        with open(a_path, encoding="utf-8") as f:
            ans = yaml.safe_load(f)
        q_ids = {q["id"] for q in qs}
        a_ids = {a["id"] for a in ans}
        # Toute golden-answer doit pointer sur une question existante
        assert a_ids.issubset(q_ids), f"golden-answer orpheline : {a_ids - q_ids}"
        # Les 10 premières questions doivent garder leur golden-answer
        assert {f"q-{i:03d}" for i in range(1, 11)}.issubset(a_ids)
