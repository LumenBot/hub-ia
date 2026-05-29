"""Tests pour `_cost.py` (S2.2 Lot C).

Couvre : calcul coût par modèle, append JSONL, lecture, cumul, format
human-readable, tolérance modèle inconnu.

Exécution : `pytest rag/code/test_cost.py -v`.
"""

from __future__ import annotations

import importlib.util
import json
import os
import sys


HERE = os.path.dirname(os.path.abspath(__file__))
MODULE_PATH = os.path.join(HERE, "_cost.py")


def _load_cost():
    sys.modules.pop("_cost", None)
    spec = importlib.util.spec_from_file_location("_cost", MODULE_PATH)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules["_cost"] = mod
    spec.loader.exec_module(mod)
    return mod


cost = _load_cost()


# ============================================================
# Calcul coût
# ============================================================

class TestEstimateCost:
    def test_openai_embedding_small(self):
        # 0,02 $ / 1M tokens × 1M tokens = 0,02 $
        assert cost.estimate_cost("text-embedding-3-small", 1_000_000) == 0.02

    def test_openai_embedding_small_small_volume(self):
        # 1000 tokens × 0,02 / 1M = 0,00002 $
        assert abs(cost.estimate_cost("text-embedding-3-small", 1000) - 0.00002) < 1e-9

    def test_claude_sonnet_4_6(self):
        # Sonnet 4.6 : 3 $/M input + 15 $/M output
        c = cost.estimate_cost("claude-sonnet-4-6", 1000, 500)
        expected = 1000 * 3.0 / 1_000_000 + 500 * 15.0 / 1_000_000
        assert abs(c - expected) < 1e-9

    def test_claude_haiku_4_5(self):
        c = cost.estimate_cost("claude-haiku-4-5", 1000, 1000)
        expected = 1000 * 0.80 / 1_000_000 + 1000 * 4.0 / 1_000_000
        assert abs(c - expected) < 1e-9

    def test_modele_inconnu_retourne_zero(self):
        assert cost.estimate_cost("modele-imaginaire-x9", 1000, 500) == 0.0

    def test_modele_versionne_resout_par_alias(self):
        """Les IDs versionnés (claude-sonnet-4-6-YYYYMMDD) sont catalogués
        séparément pour absorber les noms long form que renvoie l'API."""
        c = cost.estimate_cost("claude-sonnet-4-6-20260101", 1000, 100)
        assert c > 0


# ============================================================
# Log JSONL + lecture + cumul
# ============================================================

class TestLogCost:
    def test_log_append_jsonl(self, tmp_path):
        log_path = str(tmp_path / "cost.jsonl")
        entry = cost.log_cost("ingest.py", "text-embedding-3-small", 1000, 0, log_path=log_path)
        assert entry.model == "text-embedding-3-small"
        assert entry.tokens_in == 1000
        # Le fichier doit exister + contenir une ligne JSON
        with open(log_path, encoding="utf-8") as f:
            lines = f.readlines()
        assert len(lines) == 1
        parsed = json.loads(lines[0])
        assert parsed["model"] == "text-embedding-3-small"
        assert parsed["tokens_in"] == 1000
        assert "timestamp" in parsed

    def test_log_append_plusieurs_entrees(self, tmp_path):
        log_path = str(tmp_path / "cost.jsonl")
        cost.log_cost("query.py", "claude-sonnet-4-6", 1000, 500, log_path=log_path)
        cost.log_cost("query.py", "claude-sonnet-4-6", 2000, 800, log_path=log_path)
        cost.log_cost("ingest.py", "text-embedding-3-small", 5000, 0, log_path=log_path)
        with open(log_path, encoding="utf-8") as f:
            lines = f.readlines()
        assert len(lines) == 3

    def test_log_tolerant_filesystem_indisponible(self, tmp_path):
        # Chemin sans répertoire parent existant → l'écriture échoue, mais
        # l'appelant ne doit pas crasher (try/except dans log_cost)
        bad = str(tmp_path / "ne-pas-exister" / "cost.jsonl")
        # Ne lève pas d'exception même si l'écriture échoue
        entry = cost.log_cost("query.py", "claude-sonnet-4-6", 100, 50, log_path=bad)
        assert entry.cost_usd > 0


class TestReadCostLog:
    def test_read_jsonl(self, tmp_path):
        log_path = str(tmp_path / "cost.jsonl")
        cost.log_cost("query.py", "claude-sonnet-4-6", 1000, 500, log_path=log_path)
        cost.log_cost("ingest.py", "text-embedding-3-small", 2000, 0, log_path=log_path)
        entries = cost.read_cost_log(log_path)
        assert len(entries) == 2

    def test_read_jsonl_absent(self, tmp_path):
        assert cost.read_cost_log(str(tmp_path / "introuvable.jsonl")) == []

    def test_read_jsonl_tolerant_lignes_corrompues(self, tmp_path):
        log_path = tmp_path / "cost.jsonl"
        log_path.write_text(
            '{"timestamp": "x", "model": "m", "tokens_in": 1, "tokens_out": 0, "cost_usd": 0.0}\n'
            'ligne corrompue\n'
            '{"timestamp": "y", "model": "m", "tokens_in": 2, "tokens_out": 0, "cost_usd": 0.0}\n',
            encoding="utf-8",
        )
        entries = cost.read_cost_log(str(log_path))
        assert len(entries) == 2  # la ligne corrompue est silencieusement ignorée


class TestSummarizeCost:
    def test_summary_cumul_par_modele(self, tmp_path):
        log_path = str(tmp_path / "cost.jsonl")
        cost.log_cost("query.py", "claude-sonnet-4-6", 1000, 500, log_path=log_path)
        cost.log_cost("query.py", "claude-sonnet-4-6", 2000, 800, log_path=log_path)
        cost.log_cost("ingest.py", "text-embedding-3-small", 5000, 0, log_path=log_path)
        summary = cost.summarize_cost(log_path=log_path)
        assert summary["total_calls"] == 3
        assert "claude-sonnet-4-6" in summary["by_model"]
        assert summary["by_model"]["claude-sonnet-4-6"]["calls"] == 2
        assert summary["by_model"]["claude-sonnet-4-6"]["tokens_in"] == 3000
        assert summary["by_model"]["text-embedding-3-small"]["calls"] == 1
        assert summary["total_tokens_in"] == 8000

    def test_summary_log_vide_retourne_zero(self, tmp_path):
        log_path = str(tmp_path / "empty.jsonl")
        summary = cost.summarize_cost(log_path=log_path)
        assert summary["total_calls"] == 0
        assert summary["total_cost_usd"] == 0


class TestFormatCostSummary:
    def test_format_lisible(self, tmp_path):
        log_path = str(tmp_path / "cost.jsonl")
        cost.log_cost("query.py", "claude-sonnet-4-6", 1000, 500, log_path=log_path)
        summary = cost.summarize_cost(log_path=log_path)
        out = cost.format_cost_summary(summary)
        assert "claude-sonnet-4-6" in out
        assert "Total" in out
        assert "$" in out
