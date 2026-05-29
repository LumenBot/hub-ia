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
        assert "1/2" in report  # sources_ok (bloc standard)
        assert "q1" in report and "q2" in report
        assert "BLOC 1" in report  # S2.7 : reporting 2 blocs


# ============================================================
# Test : questions.yaml structure conforme
# ============================================================

class TestQuestionsYaml:
    def test_golden_set_volume_courant(self):
        import yaml
        questions_path = os.path.join(os.path.dirname(HERE), "..", "eval", "questions.yaml")
        with open(questions_path, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        # S2.3 Lot C v2 : golden set passé à 42 questions, puis enrichi
        # vagues 4/5/6 + questions adversariales (S2.7). Volume ≥ 30 tolérant.
        assert len(data) >= 30
        for entry in data:
            assert "id" in entry
            assert "question" in entry
            # S2.7 : deux types valides — standard (sources + concepts) ou
            # adversarial (expected_refusal true OU expected_sources vide).
            is_adv = entry.get("expected_refusal") is True or (
                "expected_sources" in entry and not entry["expected_sources"]
            )
            if is_adv:
                # Question adversariale : pas de sources/concepts attendus.
                assert entry.get("expected_refusal") is True or entry.get("expected_sources") == []
            else:
                assert "expected_sources" in entry and entry["expected_sources"]
                assert "expected_concepts" in entry and entry["expected_concepts"]

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


# ============================================================
# S2.3 Lot D — concept_matched() : matching scalaire + liste synonymes
# ============================================================

class TestConceptMatchedScalaire:
    """Cas v1 (rétro-compat) : un concept = une string, match littéral
    sous-chaîne case-insensitive."""

    def test_concept_scalaire_present(self):
        assert run_eval.concept_matched("veille", "la veille IA est essentielle") is True

    def test_concept_scalaire_absent(self):
        assert run_eval.concept_matched("RAG", "réponse sans le mot attendu") is False

    def test_concept_scalaire_case_insensible(self):
        assert run_eval.concept_matched("VEILLE", "La veille IA") is True
        assert run_eval.concept_matched("veille", "LA VEILLE IA") is True

    def test_concept_scalaire_ne_matche_pas_morphologie(self):
        """Justification du format option B : « méthode » n'est PAS une
        sous-chaîne de « méthodologie » (caractère 7 de « méthodologie »
        est « o », pas « e »). C'est le faux négatif S2.2 §7 qui motive
        l'introduction des listes de synonymes."""
        assert run_eval.concept_matched("méthode", "méthodologie de veille") is False
        # Pour matcher, il faut passer en format liste (cf. tests suivants)


class TestConceptMatchedListe:
    """S2.3 Lot D : un concept = liste de synonymes, match dès qu'au
    moins un synonyme apparaît."""

    def test_liste_un_synonyme_trouve(self):
        assert run_eval.concept_matched(
            ["méthode", "méthodologie", "approche"],
            "voici une méthodologie en trois temps",
        ) is True

    def test_liste_aucun_synonyme_trouve(self):
        assert run_eval.concept_matched(
            ["méthode", "méthodologie", "approche"],
            "réponse sans aucun synonyme attendu",
        ) is False

    def test_liste_premier_synonyme_match(self):
        assert run_eval.concept_matched(
            ["vérification", "vérifier"],
            "il faut vérification systématique",
        ) is True

    def test_liste_dernier_synonyme_match(self):
        assert run_eval.concept_matched(
            ["vérification", "vérifier", "valider"],
            "il faut valider chaque source",
        ) is True

    def test_liste_synonymes_case_insensible(self):
        # Synonymes en uppercase, réponse en lowercase → match
        assert run_eval.concept_matched(
            ["MÉTHODE", "MÉTHODOLOGIE"],
            "une méthode rigoureuse",
        ) is True
        # Inverse : synonymes lowercase, réponse uppercase
        assert run_eval.concept_matched(
            ["method", "methodology"],
            "METHOD IS GOOD",
        ) is True

    def test_liste_synonymes_avec_chiffres_quotes(self):
        """Cas issu de S2.2 §7 — variation morphologique sur les valeurs
        numériques quotées (singulier/pluriel)."""
        assert run_eval.concept_matched(
            ["1,8 heures", "1,8 heure"],
            "selon mckinsey, 1,8 heure par jour perdue",
        ) is True
        # Synonyme entier seulement, réponse contient le format singulier
        assert run_eval.concept_matched(
            ["1,8 heures"],
            "selon mckinsey, 1,8 heure par jour perdue",
        ) is False

    def test_liste_synonymes_morphologie_persistant(self):
        """q-028 S2.3 — persistant/persistance/persistent."""
        assert run_eval.concept_matched(
            ["persistant", "persistance", "persistent"],
            "le pattern offre une persistance native",
        ) is True

    def test_liste_synonymes_economie_gain(self):
        """q-029 S2.3 — économie/économies/gain/réduction."""
        assert run_eval.concept_matched(
            ["économie", "économies", "gain", "réduction"],
            "un gain mesuré de 95 % sur les tokens",
        ) is True


class TestConceptMatchedDegenere:
    """Cas dégénéré : liste vide → False + warning stderr."""

    def test_liste_vide_retourne_false(self, capsys):
        result = run_eval.concept_matched([], "n'importe quel texte")
        assert result is False

    def test_liste_vide_emet_warning_stderr(self, capsys):
        run_eval.concept_matched([], "texte")
        captured = capsys.readouterr()
        assert "vide" in captured.err.lower() or "warn" in captured.err.lower()


class TestEvaluateOneFormatMixte:
    """S2.3 Lot D — `expected_concepts` peut être un mix scalaires + listes
    dans la même entrée (cas réel observé dans questions.yaml q-001, q-039,
    q-042)."""

    def test_mix_scalaire_et_liste_tous_matches(self):
        q = {
            "id": "q-mix",
            "question": "?",
            "expected_sources": ["cu-001"],
            "expected_concepts": [
                "veille",                                      # scalaire
                ["méthode", "méthodologie", "approche"],       # liste synonymes
                "source",                                       # scalaire
            ],
        }
        r = {
            "answer": "La veille IA repose sur une méthodologie de source",
            "cited_codes": ["cu-001"],
        }
        item = run_eval.evaluate_one(q, r)
        assert item.score_global == 1
        # Les 3 concepts sont matchés (1 scalaire + 1 liste + 1 scalaire)
        assert len(item.concepts_match) == 3
        assert len(item.concepts_missing) == 0
        # expected_concepts préservé tel quel (format mixte sérialisable JSON)
        assert item.expected_concepts == q["expected_concepts"]

    def test_mix_scalaire_et_liste_partiel(self):
        q = {
            "id": "q-mix-partial",
            "question": "?",
            "expected_sources": ["cu-008"],
            "expected_concepts": [
                ["méthode", "méthodologie"],
                "absent_de_la_reponse",
                ["synonyme1", "synonyme2"],
            ],
        }
        r = {
            "answer": "méthodologie en trois temps, et synonyme1 mentionné",
            "cited_codes": ["cu-008"],
        }
        item = run_eval.evaluate_one(q, r)
        # 2 listes matchent, 1 scalaire ne matche pas
        assert len(item.concepts_match) == 2
        assert len(item.concepts_missing) == 1
        # 2/3 ≥ 50 % → score 1 (avec source citée)
        assert item.score_global == 1

    def test_evaluate_one_ne_crashe_pas_sur_format_mixte_reel(self):
        """Sanity check : ne crashe pas sur la structure réelle de
        questions.yaml v2 S2.3 (q-001 contient [str, str, list])."""
        q = {
            "id": "q-001",
            "question": "Qu'est-ce que la veille IA ?",
            "expected_sources": ["cu-001"],
            "expected_concepts": ["veille", "source", ["méthode", "méthodologie", "approche"]],
        }
        r = {"answer": "Veille IA et source [[cu-001]]", "cited_codes": ["cu-001"]}
        # Doit fonctionner sans AttributeError sur .lower() d'une liste
        item = run_eval.evaluate_one(q, r)
        assert item.id == "q-001"
        assert isinstance(item.expected_concepts, list)

    def test_evaluate_one_serialise_format_mixte_en_json(self):
        """to_dict() doit produire un dict sérialisable JSON, même avec
        listes imbriquées dans expected_concepts."""
        import json
        q = {
            "id": "q-json",
            "question": "?",
            "expected_sources": ["cu-001"],
            "expected_concepts": ["veille", ["méthode", "méthodologie"]],
        }
        r = {"answer": "veille avec méthodologie", "cited_codes": ["cu-001"]}
        item = run_eval.evaluate_one(q, r)
        # Sérialisation JSON ne lève pas d'exception
        s = json.dumps(item.to_dict(), ensure_ascii=False)
        assert "méthodologie" in s


class TestRetroCompatV1Inchangee:
    """Tous les tests v1 (concepts scalaires uniquement) doivent continuer
    à passer sans modification — preuve de rétro-compatibilité."""

    def test_evaluate_one_v1_format_scalaires_seuls(self):
        q = {
            "id": "q-v1",
            "question": "?",
            "expected_sources": ["cu-008"],
            "expected_concepts": ["retrieval", "fine-tuning"],
        }
        r = {
            "answer": "Le RAG fait du retrieval et est différent du fine-tuning [CU-008]",
            "cited_codes": ["cu-008"],
        }
        item = run_eval.evaluate_one(q, r)
        assert item.score_global == 1
        assert set(item.concepts_match) == {"retrieval", "fine-tuning"}


# ============================================================
# S2.7 Lot Dev — Mode adversarial (refus correct vs hallucination)
# ============================================================

class TestIsAdversarial:
    def test_expected_refusal_true(self):
        assert run_eval.is_adversarial({"id": "q", "expected_refusal": True}) is True

    def test_expected_sources_vide(self):
        assert run_eval.is_adversarial({"id": "q", "expected_sources": []}) is True

    def test_standard_non_adversarial(self):
        assert run_eval.is_adversarial({"id": "q", "expected_sources": ["cu-001"]}) is False

    def test_absence_champs_non_adversarial(self):
        # ni expected_refusal ni expected_sources vide → standard
        assert run_eval.is_adversarial({"id": "q", "expected_concepts": ["x"]}) is False


class TestRefusalDetected:
    def test_chaque_marqueur_canonique_detecte(self):
        for marker in run_eval.REFUSAL_MARKERS:
            assert run_eval.refusal_detected(f"Réponse : {marker} sur ce sujet.") is True

    def test_case_insensible(self):
        assert run_eval.refusal_detected("JE NE DISPOSE PAS de cette donnée") is True

    def test_aucun_marqueur(self):
        assert run_eval.refusal_detected("Voici une réponse détaillée et assurée.") is False


class TestEvaluateAdversarial:
    def test_refus_correct_score_1(self):
        """Cas 1 brief §4.5 : marqueur de refus + aucune source citée → score=1."""
        q = {"id": "q-adv-001", "question": "Seuil dispositif XYZ-2027 ?", "expected_refusal": True}
        r = {"answer": "Ce dispositif ne figure pas dans les documents du Hub IA.", "cited_codes": []}
        item = run_eval.evaluate_one(q, r)
        assert item.mode == "adversarial"
        assert item.adversarial_verdict == "refus_correct"
        assert item.score_global == 1

    def test_hallucination_score_0(self):
        """Cas 2 brief §4.5 : sources citées + réponse inventée (aucun marqueur) → score=0."""
        q = {"id": "q-adv-002", "question": "Seuil dispositif XYZ-2027 ?", "expected_sources": []}
        r = {
            "answer": "Le seuil d'éligibilité au dispositif XYZ-2027 est de 250 salariés [PR-08].",
            "cited_codes": ["pr-08"],
        }
        item = run_eval.evaluate_one(q, r)
        assert item.mode == "adversarial"
        assert item.adversarial_verdict == "hallucination"
        assert item.score_global == 0

    def test_refus_partiel_score_0(self):
        """Cas 3 brief §4.5 : marqueur de doute + tentative de réponse (sources citées)
        → refus partiel, défaut score=0."""
        q = {"id": "q-adv-003", "question": "Seuil dispositif XYZ-2027 ?", "expected_refusal": True}
        r = {
            "answer": "Je ne dispose pas de cette information précise, mais d'après [PR-08] "
                      "le seuil pourrait être autour de 250 salariés.",
            "cited_codes": ["pr-08"],
        }
        item = run_eval.evaluate_one(q, r)
        assert item.mode == "adversarial"
        assert item.adversarial_verdict == "refus_partiel"
        assert item.score_global == 0

    def test_dispatch_via_evaluate_one(self):
        """evaluate_one() doit router vers le scoring adversarial automatiquement."""
        q = {"id": "q-adv", "question": "?", "expected_sources": []}
        r = {"answer": "Aucune information dans le corpus.", "cited_codes": []}
        item = run_eval.evaluate_one(q, r)
        assert item.mode == "adversarial"

    def test_refus_franc_avec_citations_reste_correct(self):
        """S2.7 Lot I finding (calibration v2) : un refus FRANC (phrase
        canonique du system prompt) reste refus_correct MÊME si le RAG cite
        le contexte pour EXPLIQUER le manque. C'est le faux négatif corrigé
        (harness 0/12 → 12/12)."""
        q = {"id": "q-adv-001", "question": "Seuil dispositif XYZ-2027 ?", "expected_refusal": True}
        r = {
            "answer": "Je n'ai pas de réponse documentée dans le Hub IA pour cette question. "
                      "Le dispositif XYZ-2027 n'apparaît dans aucun des extraits du vault [PR-08].",
            "cited_codes": ["pr-08"],
        }
        item = run_eval.evaluate_one(q, r)
        assert item.adversarial_verdict == "refus_correct"
        assert item.score_global == 1

    def test_strong_marker_prime_sur_citations(self):
        """Chaque marqueur STRONG doit donner refus_correct même avec sources."""
        for marker in run_eval.STRONG_REFUSAL_MARKERS:
            q = {"id": "q", "question": "?", "expected_refusal": True}
            r = {"answer": f"Réponse : {marker} sur ce sujet.", "cited_codes": ["pr-08"]}
            item = run_eval.evaluate_adversarial(q, r)
            assert item.adversarial_verdict == "refus_correct", f"marker={marker}"
            assert item.score_global == 1

    def test_serialisation_json(self):
        import json
        q = {"id": "q-adv", "question": "?", "expected_refusal": True}
        r = {"answer": "hors scope du Hub IA", "cited_codes": []}
        item = run_eval.evaluate_one(q, r)
        s = json.dumps(item.to_dict(), ensure_ascii=False)
        assert "adversarial" in s
        assert "refus_correct" in s


class TestFormatReportAdversarial:
    def test_reporting_deux_blocs(self):
        std = run_eval.EvalItem(
            id="q-std", question="?", expected_sources=["cu-001"], expected_concepts=["veille"],
            cited_codes=["cu-001"], sources_match=["cu-001"], sources_missing=[],
            concepts_match=["veille"], concepts_missing=[], score_global=1,
            answer_preview="ok", mode="standard",
        )
        adv_ok = run_eval.EvalItem(
            id="q-adv-ok", question="?", expected_sources=[], expected_concepts=[],
            cited_codes=[], sources_match=[], sources_missing=[],
            concepts_match=[], concepts_missing=[], score_global=1,
            answer_preview="hors scope", mode="adversarial", adversarial_verdict="refus_correct",
        )
        adv_hallu = run_eval.EvalItem(
            id="q-adv-hallu", question="?", expected_sources=[], expected_concepts=[],
            cited_codes=["pr-08"], sources_match=[], sources_missing=[],
            concepts_match=[], concepts_missing=[], score_global=0,
            answer_preview="réponse inventée", mode="adversarial", adversarial_verdict="hallucination",
        )
        report = run_eval.format_report([std, adv_ok, adv_hallu])
        assert "BLOC 1" in report
        assert "BLOC 2" in report
        assert "ADVERSARIAL" in report.upper()
        assert "Refus corrects : 1/2" in report
        assert "Hallucinations détectées : 1/2" in report
        # La question hallucination doit être listée nommément
        assert "q-adv-hallu" in report

    def test_pas_de_bloc_adversarial_si_aucune(self):
        std = run_eval.EvalItem(
            id="q-std", question="?", expected_sources=["cu-001"], expected_concepts=["veille"],
            cited_codes=["cu-001"], sources_match=["cu-001"], sources_missing=[],
            concepts_match=["veille"], concepts_missing=[], score_global=1,
            answer_preview="ok",
        )
        report = run_eval.format_report([std])
        assert "BLOC 1" in report
        assert "BLOC 2" not in report


# ============================================================
# Tests S2.9 Lot Dev — filter_questions_by_unit
# ============================================================

class TestFilterQuestionsByUnit:
    """Couvre le bug-fix `--filter-unit` (S2.9 Lot Dev, 2e occurrence de
    l'écart procédure S2.7/S2.8). Documenté `briefs/DIAGNOSTIC-FILTER-UNIT-S2.9.md`.

    Stratégie de matching adversarial = union de 2 signaux pour robustesse :
    1. `unit: adversarial` explicite dans la YAML (convention Cowork)
    2. `is_adversarial()` sémantique (expected_refusal=true OU expected_sources=[])
    """

    QUESTIONS = [
        {"id": "q-001", "question": "?", "unit": "cu-001",
         "expected_sources": ["cu-001"], "expected_concepts": []},
        {"id": "q-002", "question": "?", "unit": "dep-05",
         "expected_sources": ["dep-05"], "expected_concepts": []},
        {"id": "q-adv-001", "question": "?", "unit": "adversarial",
         "expected_refusal": True},
        # Adversarial via signal sémantique seul (pas de champ `unit:` explicite)
        {"id": "q-adv-002", "question": "?", "expected_refusal": True},
        # Adversarial via expected_sources vide explicite (sans champ `unit:`)
        {"id": "q-adv-003", "question": "?", "expected_sources": []},
    ]

    def test_filter_none_keeps_all(self):
        out = run_eval.filter_questions_by_unit(self.QUESTIONS, None)
        assert [q["id"] for q in out] == ["q-001", "q-002", "q-adv-001", "q-adv-002", "q-adv-003"]

    def test_filter_all_keeps_all(self):
        out = run_eval.filter_questions_by_unit(self.QUESTIONS, "all")
        assert len(out) == 5

    def test_filter_adversarial_keeps_adversarial(self):
        out = run_eval.filter_questions_by_unit(self.QUESTIONS, "adversarial")
        assert [q["id"] for q in out] == ["q-adv-001", "q-adv-002", "q-adv-003"]

    def test_filter_standard_keeps_non_adversarial(self):
        out = run_eval.filter_questions_by_unit(self.QUESTIONS, "standard")
        assert [q["id"] for q in out] == ["q-001", "q-002"]

    def test_filter_unknown_value_raises(self):
        with pytest.raises(ValueError, match="filter-unit"):
            run_eval.filter_questions_by_unit(self.QUESTIONS, "azerty")

    def test_filter_does_not_mutate_input(self):
        before = list(self.QUESTIONS)
        run_eval.filter_questions_by_unit(self.QUESTIONS, "adversarial")
        assert self.QUESTIONS == before

    def test_filter_empty_input(self):
        assert run_eval.filter_questions_by_unit([], "adversarial") == []
        assert run_eval.filter_questions_by_unit([], "standard") == []
        assert run_eval.filter_questions_by_unit([], None) == []

    def test_filter_unit_case_sensitive_for_yaml_value(self):
        # La convention YAML est `unit: adversarial` lowercase. On tolère néanmoins
        # les variantes de casse côté valeur YAML (défense en profondeur).
        qs = [{"id": "q-x", "question": "?", "unit": "Adversarial",
               "expected_refusal": True}]
        out = run_eval.filter_questions_by_unit(qs, "adversarial")
        assert len(out) == 1


class TestFilterUnitCLI:
    """Smoke tests CLI : le flag `--filter-unit` est bien parsé par argparse."""

    def test_cli_choices_include_three_values(self):
        # Garantit que les 3 valeurs prévues par BRIEF-CC-S2.9 §5.3 sont supportées.
        assert set(run_eval.FILTER_UNIT_CHOICES) == {"standard", "adversarial", "all"}
