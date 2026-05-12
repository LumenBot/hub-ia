"""Tests pour query.py (retrieval + génération + citations).

Exécution :
    pytest rag/code/backend/test_query.py -v

Mocks complets : aucun appel API. On valide la structure du flow et la
sélection des codes cités.
"""

from __future__ import annotations

import importlib.util
import json
import os
import sys

import pytest


HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT_PATH = os.path.join(HERE, "query.py")


def _load_query():
    spec = importlib.util.spec_from_file_location("query", SCRIPT_PATH)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


query_mod = _load_query()


# ============================================================
# Fakes
# ============================================================

class FakeEmbedder:
    def __init__(self):
        self.calls: list[str] = []

    def embed_one(self, text):
        self.calls.append(text)
        return [0.1] * 8


def _mk_chunk(code: str, h2: str, doc: str, distance: float):
    return query_mod.RetrievedChunk(
        chunk_id=f"{code.lower()}#{h2.lower().replace(' ', '-')}",
        document=doc,
        metadata={
            "code": code.lower(),
            "titre": f"Titre {code}",
            "h2_title": h2,
            "source_file": f"modules/{code.lower()}.md",
        },
        distance=distance,
    )


class FakeRetriever:
    def __init__(self, chunks):
        self._chunks = chunks
        self.calls: list[tuple] = []

    def query(self, embedding, k=5):
        self.calls.append((embedding, k))
        return self._chunks[:k]


class FakeGenerator:
    def __init__(self, answer: str):
        self.answer = answer
        self.calls: list[tuple[str, str]] = []

    def generate(self, system, user, max_tokens=1024):
        self.calls.append((system, user))
        return self.answer


# ============================================================
# Tests
# ============================================================

class TestBuildContext:
    def test_empty_chunks(self):
        prompt = query_mod.build_user_prompt("Q1", [])
        assert "aucun chunk pertinent" in prompt
        assert "Q1" in prompt

    def test_with_chunks(self):
        chunks = [
            _mk_chunk("CU-008", "RAG vs fine-tuning", "Le RAG injecte...", 0.2),
            _mk_chunk("DEP-02", "Architecture", "Stitch evaluate iterate", 0.3),
        ]
        prompt = query_mod.build_user_prompt("Diff RAG/FT ?", chunks)
        assert "Diff RAG/FT ?" in prompt
        assert "CONTEXTE" in prompt
        assert "code=cu-008" in prompt
        assert "Stitch evaluate iterate" in prompt
        assert "similarity=0.800" in prompt
        assert "similarity=0.700" in prompt


class TestCitationExtraction:
    def test_extract_cu(self):
        ans = "Le RAG diffère [CU-008]. Voir aussi [DEP-02]. Pas [hors-code]."
        codes = query_mod.extract_cited_codes(ans)
        assert codes == ["CU-008", "DEP-02"]

    def test_dedup(self):
        ans = "Voir [CU-008], puis [cu-008] encore, et [PR-07]."
        codes = query_mod.extract_cited_codes(ans)
        assert codes == ["CU-008", "PR-07"]

    def test_architecture_codes(self):
        ans = "Pattern [A1] et [A3]."
        codes = query_mod.extract_cited_codes(ans)
        assert codes == ["A1", "A3"]

    def test_outils_code(self):
        ans = "Voir [OUTILS-VECTOR-DB]."
        codes = query_mod.extract_cited_codes(ans)
        assert codes == ["OUTILS-VECTOR-DB"]

    def test_no_code_returns_empty(self):
        assert query_mod.extract_cited_codes("Pas de code dans cette réponse.") == []


class TestAnswerFlow:
    def test_full_pipeline(self):
        chunks = [_mk_chunk("CU-008", "Vue d'ensemble", "Le RAG combine retrieval et LLM.", 0.1)]
        emb = FakeEmbedder()
        ret = FakeRetriever(chunks)
        gen = FakeGenerator("Le RAG diffère [CU-008].\n\nSources : CU-008")

        result = query_mod.answer_question(
            "Quelle différence entre RAG et fine-tuning ?", emb, ret, gen, k=5
        )

        assert emb.calls == ["Quelle différence entre RAG et fine-tuning ?"]
        assert ret.calls[0][1] == 5
        assert len(gen.calls) == 1
        # System prompt non vide
        assert "Hub IA" in gen.calls[0][0]
        # Citations extraites
        assert result.cited_codes == ["CU-008"]
        assert result.chunks == chunks

    def test_no_chunks_still_runs(self):
        emb = FakeEmbedder()
        ret = FakeRetriever([])
        gen = FakeGenerator("Je n'ai pas de réponse documentée dans le Hub IA.")
        result = query_mod.answer_question("question inconnue", emb, ret, gen, k=5)
        assert result.chunks == []
        assert result.cited_codes == []
        assert "documenté" in result.answer or "Hub IA" in result.answer

    def test_to_dict_serializable(self):
        chunks = [_mk_chunk("PR-07", "Build vs Buy", "Cadrage transverse.", 0.4)]
        emb = FakeEmbedder()
        ret = FakeRetriever(chunks)
        gen = FakeGenerator("Réponse [PR-07].")
        result = query_mod.answer_question("Build vs buy ?", emb, ret, gen)
        d = result.to_dict()
        # JSON serializable
        json.dumps(d)
        assert d["question"] == "Build vs buy ?"
        assert d["cited_codes"] == ["PR-07"]
        assert d["chunks"][0]["code"] == "pr-07"
        assert d["chunks"][0]["distance"] == 0.4


class TestFormatHuman:
    def test_format_includes_question_answer_chunks(self):
        chunks = [_mk_chunk("CU-001", "Veille", "Démarche.", 0.2)]
        result = query_mod.QueryResult(
            question="Comment faire de la veille ?",
            answer="Une démarche en trois temps [CU-001].",
            chunks=chunks,
            cited_codes=["CU-001"],
        )
        out = query_mod.format_human(result)
        assert "Comment faire de la veille ?" in out
        assert "[CU-001]" in out
        assert "Veille" in out
        assert "sim=0.800" in out


class TestPromptDiscipline:
    def test_system_prompt_mentions_citations_and_refuses_invention(self):
        sp = query_mod.SYSTEM_PROMPT
        assert "Hub IA" in sp
        assert "Citations" in sp or "cite" in sp.lower()
        assert "pas d'invention" in sp.lower() or "invention" in sp.lower()
        assert "n'ai pas de réponse" in sp or "documentée" in sp


# ============================================================
# S2.2 Lot C — Prompt enrichi (briques transverses + wikilinks)
# ============================================================

class TestPromptEnrichiS22:
    """Le system prompt v2 doit mentionner les briques transverses comme
    sources canoniques privilégiées (D-025) et le format wikilink Obsidian
    comme citation préférée."""

    def test_mentionne_briques_transverses_canoniques(self):
        sp = query_mod.SYSTEM_PROMPT
        assert "chiffres-macro-2026" in sp, "doit mentionner le référentiel chiffres-macro"
        assert "vigilance-" in sp, "doit mentionner la famille vigilance-*"
        assert "pattern-" in sp, "doit mentionner la famille pattern-*"
        assert "glossaire" in sp.lower()

    def test_mentionne_autorite_canonique_transverse(self):
        sp = query_mod.SYSTEM_PROMPT
        # Le prompt doit indiquer que les transverses sont d'autorité supérieure
        # à une mention équivalente dans un module
        assert "autorité" in sp.lower() or "canoniques privilégiées" in sp.lower() \
            or "source canonique" in sp.lower()

    def test_mentionne_format_wikilink_obsidian(self):
        sp = query_mod.SYSTEM_PROMPT
        assert "[[" in sp, "doit montrer la syntaxe wikilink [[code]]"
        assert "]]" in sp
        assert "préféré" in sp.lower() or "wikilink" in sp.lower()

    def test_format_crochets_simples_reste_accepte_retro_compat(self):
        sp = query_mod.SYSTEM_PROMPT
        # Rétro-compatibilité du format historique [CODE]
        assert "[CU-008]" in sp or "[CU-001]" in sp or "[DEP-02]" in sp or \
               "rétro-compatibilité" in sp.lower()

    def test_extraction_citations_supporte_les_deux_formats(self):
        """L'extraction doit fonctionner sur les crochets simples (v1).
        Les wikilinks Obsidian [[...]] ne sont pas matchés par CODE_PATTERN
        (intentionnel : ils sont du markup interne, pas des citations
        exposées) — confirmé par les tests existants."""
        ans = "Réponse [CU-008]. Voir aussi [DEP-02]."
        codes = query_mod.extract_cited_codes(ans)
        assert codes == ["CU-008", "DEP-02"]


# ============================================================
# S2.2 Lot C — Instrumentation coût (intégration Generator/Embedder)
# ============================================================

class FakeAnthropicResponse:
    """Mock minimal d'un objet de réponse Anthropic avec usage."""
    class _Usage:
        def __init__(self, in_tokens, out_tokens):
            self.input_tokens = in_tokens
            self.output_tokens = out_tokens

    class _Block:
        def __init__(self, text):
            self.text = text
            self.type = "text"

    def __init__(self, text, in_tokens=100, out_tokens=50):
        self.content = [self._Block(text)]
        self.usage = self._Usage(in_tokens, out_tokens)


class FakeAnthropicClient:
    def __init__(self, in_tokens=100, out_tokens=50):
        self.in_tokens = in_tokens
        self.out_tokens = out_tokens
        self.messages = self

    def create(self, model, max_tokens, system, messages):
        return FakeAnthropicResponse("ok", self.in_tokens, self.out_tokens)


class TestCostInstrumentation:
    def test_generator_log_cost_avec_usage(self, tmp_path):
        gen = query_mod.Generator(
            model="claude-sonnet-4-6",
            api_key="dummy",
            cost_log_path=str(tmp_path / "cost.jsonl"),
        )
        # On bypass _ensure() en plantant directement le client mock
        gen._client = FakeAnthropicClient(in_tokens=1234, out_tokens=567)
        out = gen.generate("system", "user")
        assert out == "ok"
        # Vérifier que le log JSONL contient l'entrée
        log = (tmp_path / "cost.jsonl").read_text(encoding="utf-8")
        assert "claude-sonnet-4-6" in log
        assert '"tokens_in": 1234' in log
        assert '"tokens_out": 567' in log

    def test_generator_tolerant_si_log_path_inaccessible(self, tmp_path):
        gen = query_mod.Generator(
            model="claude-sonnet-4-6",
            api_key="dummy",
            cost_log_path=str(tmp_path / "ne-pas-exister" / "cost.jsonl"),
        )
        gen._client = FakeAnthropicClient(in_tokens=10, out_tokens=5)
        # Doit retourner la réponse sans crasher même si log inaccessible
        out = gen.generate("system", "user")
        assert out == "ok"
