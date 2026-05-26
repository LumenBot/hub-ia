"""Tests pour citation_audit.py — règle R11 (wikilinks outils glossariés).

Exécution : pytest rag/code/audit/test_citation_audit.py -v

Couverture :
- parse_outils_fiches : extraction des outils depuis 1 ou plusieurs fiches
- extract_tool_names : heuristique de découpe des H2
- find_first_naked_occurrence : ignore wikilinks, case-sensitive
- check_r11_for_file : positifs (OK) et négatifs (manquement détecté)
- Numéros de ligne globaux (frontmatter compris)
- Auto-exclusion des fiches outils-*.md
"""

from __future__ import annotations

import importlib.util
import os
import sys
import textwrap
from pathlib import Path

import pytest

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT_PATH = os.path.join(HERE, "citation_audit.py")


def _load_module():
    spec = importlib.util.spec_from_file_location("citation_audit", SCRIPT_PATH)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


citation_audit = _load_module()


# ============================================================
# Fixtures
# ============================================================

OUTILS_LLM = textwrap.dedent("""\
---
code: outils-llm
titre: "Fiche outils — LLM"
type: fiche-outil
---

# Fiche outils — LLM

## Quand utiliser un modèle LLM

Section méta — pas un outil.

## Claude (Anthropic) — référence raisonnement

Description Claude.

## Mistral — référence souveraine EU

Description Mistral.

## Kimi K2 / K2.6 (Moonshot AI) — long contexte

Description Kimi.

## Make (ex-Integromat) — note ambigüe

Volontairement placé ici pour test heuristique « Make » alias.

## Comparatif synthétique

Section méta — pas un outil.
""")


OUTILS_VECTOR_DB = textwrap.dedent("""\
---
code: outils-vector-db
titre: "Fiche outils — vector DB"
type: fiche-outil
---

# Fiche outils — vector DB

## Quand utiliser un vector store

Section méta.

## Qdrant — référence open-source

Description Qdrant.

## pgvector — extension Postgres

Description pgvector.
""")


@pytest.fixture
def vault(tmp_path: Path) -> Path:
    ressources = tmp_path / "ressources"
    ressources.mkdir()
    (ressources / "outils-llm.md").write_text(OUTILS_LLM, encoding="utf-8")
    (ressources / "outils-vector-db.md").write_text(OUTILS_VECTOR_DB, encoding="utf-8")
    return tmp_path


def _write(vault: Path, rel_path: str, content: str) -> Path:
    fp = vault / rel_path
    fp.parent.mkdir(parents=True, exist_ok=True)
    fp.write_text(content, encoding="utf-8")
    return fp


# ============================================================
# extract_tool_names
# ============================================================

class TestExtractToolNames:
    def test_simple_em_dash(self):
        assert citation_audit.extract_tool_names("Mistral — référence souveraine EU") == ["Mistral"]

    def test_vendor_parens(self):
        assert citation_audit.extract_tool_names("Claude (Anthropic) — référence raisonnement") == ["Claude"]

    def test_aliases_slash(self):
        out = citation_audit.extract_tool_names("Kimi K2 / K2.6 (Moonshot AI) — long contexte premium")
        assert out == ["Kimi K2", "K2.6"]

    def test_meta_section_quand(self):
        assert citation_audit.extract_tool_names("Quand utiliser un modèle LLM") == []

    def test_meta_section_comparatif(self):
        assert citation_audit.extract_tool_names("Comparatif synthétique") == []

    def test_meta_section_outils_satellites(self):
        assert citation_audit.extract_tool_names("Outils satellites à mentionner") == []

    def test_make_vendor_strip(self):
        assert citation_audit.extract_tool_names("Make (ex-Integromat) — référence SaaS no-code") == ["Make"]

    def test_pour_aller_plus_loin(self):
        assert citation_audit.extract_tool_names("Pour aller plus loin") == []


# ============================================================
# parse_outils_fiches
# ============================================================

class TestParseOutilsFiches:
    def test_count_and_fiches(self, vault):
        tools = citation_audit.parse_outils_fiches(str(vault))
        names = sorted({t.display_name for t in tools})
        assert "Claude" in names
        assert "Mistral" in names
        assert "Qdrant" in names
        assert "pgvector" in names
        assert "Kimi K2" in names
        # 2 fiches : outils-llm + outils-vector-db
        assert len({t.source_fiche for t in tools}) == 2

    def test_anchor_is_slug(self, vault):
        tools = citation_audit.parse_outils_fiches(str(vault))
        claude = next(t for t in tools if t.display_name == "Claude")
        assert claude.anchor == "claude"
        assert claude.source_fiche == "outils-llm"

    def test_alias_preserved(self, vault):
        tools = citation_audit.parse_outils_fiches(str(vault))
        kimi = next(t for t in tools if t.display_name == "Kimi K2")
        assert "K2.6" in kimi.aliases


# ============================================================
# find_first_naked_occurrence
# ============================================================

class TestNakedOccurrence:
    def test_finds_naked_mention(self):
        body = "Mistral est un LLM."
        out = citation_audit.find_first_naked_occurrence(body, ("Mistral",))
        assert out is not None and out[0] == 0

    def test_ignores_inside_wikilink(self):
        body = "[[outils-llm|Mistral]] est un LLM."
        out = citation_audit.find_first_naked_occurrence(body, ("Mistral",))
        assert out is None

    def test_finds_after_wikilink(self):
        body = "[[outils-llm|Mistral]] est un LLM. Plus tard on reparle de Mistral."
        out = citation_audit.find_first_naked_occurrence(body, ("Mistral",))
        # La 2e mention nue doit être trouvée (en dehors du wikilink).
        assert out is not None
        assert body[out[0]:out[0] + out[1]] == "Mistral"

    def test_case_sensitive(self):
        # Volontairement case-sensitive pour éviter faux positifs sur mots anglais
        # comme « make ». Le H2 source utilise « Make » → ne matche pas « make ».
        body = "Pour faire ce truc, il faut make un appel HTTP."
        out = citation_audit.find_first_naked_occurrence(body, ("Make",))
        assert out is None

    def test_word_boundary_chatgpt(self):
        # \bGPT\b ne doit pas matcher l'intérieur de « ChatGPT »
        body = "ChatGPT est très populaire."
        out = citation_audit.find_first_naked_occurrence(body, ("GPT",))
        assert out is None

    def test_word_boundary_hyphen(self):
        # « Pleias-RAG » avec tiret : ne doit matcher que la chaîne complète.
        body = "Mention de Pleias-RAG dans le texte."
        out = citation_audit.find_first_naked_occurrence(body, ("Pleias-RAG",))
        assert out is not None

    def test_multiple_aliases(self):
        body = "On utilise K2.6 directement."
        out = citation_audit.find_first_naked_occurrence(body, ("Kimi K2", "K2.6"))
        assert out is not None
        # « K2.6 » doit matcher
        assert "K2.6" in body[out[0]:out[0] + out[1] + 5]


# ============================================================
# check_r11_for_file — cas positifs (OK)
# ============================================================

MD_FRONTMATTER = textwrap.dedent("""\
---
code: pr-test
titre: "Test"
type: prealable-pr
---

# Test
""")


class TestCheckPositive:
    def test_wikilink_before_mention(self, vault):
        """Cas positif : wikilink AVANT la mention en clair → OK."""
        content = MD_FRONTMATTER + textwrap.dedent("""
        ## Section

        Voir [[outils-llm]] pour démarrer. Plus tard, on évoque Mistral comme exemple.
        """)
        fp = _write(vault, "prealables/pr-test.md", content)
        tools = citation_audit.parse_outils_fiches(str(vault))
        result = citation_audit.check_r11_for_file(str(fp), str(vault), tools)
        assert not [m for m in result.manquements if m.tool == "Mistral"]
        assert "Mistral" in result.ok_mentions

    def test_wikilink_alias_inline(self, vault):
        """Cas positif : la mention EST le wikilink (forme alias)."""
        content = MD_FRONTMATTER + textwrap.dedent("""
        ## Section

        Le LLM [[outils-llm|Mistral]] est souverain EU.
        """)
        fp = _write(vault, "prealables/pr-test.md", content)
        tools = citation_audit.parse_outils_fiches(str(vault))
        result = citation_audit.check_r11_for_file(str(fp), str(vault), tools)
        # Aucune mention nue → aucun manquement Mistral
        assert not [m for m in result.manquements if m.tool == "Mistral"]

    def test_tool_not_mentioned(self, vault):
        """Cas positif : outil non mentionné du tout → pas de manquement."""
        content = MD_FRONTMATTER + "\n## Section\n\nTexte sans mention.\n"
        fp = _write(vault, "prealables/pr-test.md", content)
        tools = citation_audit.parse_outils_fiches(str(vault))
        result = citation_audit.check_r11_for_file(str(fp), str(vault), tools)
        assert result.manquements == []


# ============================================================
# check_r11_for_file — cas négatifs (manquement attendu)
# ============================================================

class TestCheckNegative:
    def test_naked_mention_no_wikilink(self, vault):
        """Cas négatif : Mistral en clair sans wikilink → manquement signalé."""
        content = MD_FRONTMATTER + textwrap.dedent("""
        ## Section

        Le modèle Mistral est intéressant pour la souveraineté.
        """)
        fp = _write(vault, "prealables/pr-test.md", content)
        tools = citation_audit.parse_outils_fiches(str(vault))
        result = citation_audit.check_r11_for_file(str(fp), str(vault), tools)
        manq = [m for m in result.manquements if m.tool == "Mistral"]
        assert len(manq) == 1
        assert manq[0].source_fiche == "outils-llm"

    def test_wikilink_after_first_mention(self, vault):
        """Cas négatif : mention en clair AVANT le wikilink → manquement."""
        content = MD_FRONTMATTER + textwrap.dedent("""
        ## Section

        Le modèle Mistral est intéressant. On en reparle dans [[outils-llm]].
        """)
        fp = _write(vault, "prealables/pr-test.md", content)
        tools = citation_audit.parse_outils_fiches(str(vault))
        result = citation_audit.check_r11_for_file(str(fp), str(vault), tools)
        assert [m for m in result.manquements if m.tool == "Mistral"]


# ============================================================
# Auto-exclusion des fiches outils-*.md (la fiche source ne s'audite pas)
# ============================================================

class TestAutoExclusion:
    def test_outils_fiche_self_excluded(self, vault):
        tools = citation_audit.parse_outils_fiches(str(vault))
        fp = str(vault / "ressources" / "outils-llm.md")
        result = citation_audit.check_r11_for_file(fp, str(vault), tools)
        assert result.manquements == []
        assert result.ok_mentions == []


# ============================================================
# Numéros de ligne (frontmatter compris)
# ============================================================

class TestLineNumbering:
    def test_line_number_includes_frontmatter(self, vault):
        """Le numéro de ligne reporté doit correspondre au fichier complet
        (frontmatter compris), pour pouvoir naviguer dans l'éditeur.
        """
        content = MD_FRONTMATTER + textwrap.dedent("""
        ## Section

        Le modèle Mistral est intéressant.
        """)
        fp = _write(vault, "prealables/pr-test.md", content)
        tools = citation_audit.parse_outils_fiches(str(vault))
        result = citation_audit.check_r11_for_file(str(fp), str(vault), tools)
        m = next(x for x in result.manquements if x.tool == "Mistral")
        # MD_FRONTMATTER = 7 lignes (--- + 4 champs + --- + \n) + # Test + lignes du body
        # On vérifie juste que la ligne est > 5 (donc bien décalée par le frontmatter)
        # et que le snippet contient « Mistral ».
        assert m.line > 5
        assert "Mistral" in m.snippet


# ============================================================
# Reporting (smoke)
# ============================================================

class TestReportingSmoke:
    def test_md_report_clean(self, vault):
        # Pas de fichiers à auditer en dehors des fiches outils-* → clean
        tools = citation_audit.parse_outils_fiches(str(vault))
        results = [citation_audit.check_r11_for_file(
            str(vault / "ressources" / "outils-llm.md"), str(vault), tools)]
        report = citation_audit.format_md_report(results, tools, str(vault))
        assert "CLEAN" in report

    def test_md_report_with_manquements(self, vault):
        content = MD_FRONTMATTER + "\n## Section\n\nMention Mistral en clair.\n"
        fp = _write(vault, "prealables/pr-test.md", content)
        tools = citation_audit.parse_outils_fiches(str(vault))
        result = citation_audit.check_r11_for_file(str(fp), str(vault), tools)
        report = citation_audit.format_md_report([result], tools, str(vault))
        assert "Mistral" in report
        assert "Manquements R11" in report

    def test_json_payload_structure(self, vault):
        content = MD_FRONTMATTER + "\n## Section\n\nMention Mistral en clair.\n"
        fp = _write(vault, "prealables/pr-test.md", content)
        tools = citation_audit.parse_outils_fiches(str(vault))
        result = citation_audit.check_r11_for_file(str(fp), str(vault), tools)
        payload = citation_audit.to_json_payload([result], tools, str(vault))
        assert payload["rule"] == "R11"
        assert payload["summary"]["manquements_total"] >= 1
        assert any(m["tool"] == "Mistral" for m in payload["manquements"])
