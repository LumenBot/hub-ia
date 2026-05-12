"""Tests pour audit-md-rag.py (5 règles v1).

Exécution : pytest rag/code/audit/test_audit_md_rag.py -v
"""

from __future__ import annotations

import importlib.util
import os
import sys
import textwrap
from datetime import date

import pytest


HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT_PATH = os.path.join(HERE, "audit-md-rag.py")


def _load_module():
    spec = importlib.util.spec_from_file_location("audit_md_rag", SCRIPT_PATH)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


audit_md_rag = _load_module()


# ============================================================
# Fixtures : un MD conforme + plusieurs MD non conformes
# ============================================================

CONFORME = textwrap.dedent("""\
---
code: cu-001
titre: "Recherche & veille"
type: module-cu
axe: B
niveau: 1
tags: [veille, recherche]
version: 3.8.2
last_updated: 2026-05-11
glosaire_termes: [veille, rag]
derives: ["[[cu-008]]"]
public_cible: [dirigeant, ops]
---

# Recherche & veille

## Vue d'ensemble

Module pédagogique simple. 95 % des projets GenAI échouent (Source : MIT Sloan / NANDA, août 2025, [URL](https://example.com)).

Voir aussi [[cu-008|Knowledge base RAG]].

## Méthodologie

Démarche en trois temps. Section autonome lisible isolément.
""")


def write_md(tmp_path, name: str, content: str) -> str:
    from pathlib import Path
    fp = Path(str(tmp_path)) / name
    fp.write_text(content, encoding="utf-8")
    return str(fp)


@pytest.fixture
def vault_conforme(tmp_path):
    write_md(tmp_path, "cu-001.md", CONFORME)
    cu008 = CONFORME.replace("code: cu-001", "code: cu-008").replace("# Recherche & veille", "# Knowledge base RAG").replace('titre: "Recherche & veille"', 'titre: "Knowledge base RAG"').replace("[[cu-008|Knowledge base RAG]]", "[[cu-001]]")
    write_md(tmp_path, "cu-008.md", cu008)
    return str(tmp_path)


# ============================================================
# Tests par règle
# ============================================================

class TestR1Frontmatter:
    def test_conforme_zero_hit(self, vault_conforme):
        files = audit_md_rag.list_md_files(vault_conforme)
        codes = audit_md_rag.vault_codes(files)
        result = audit_md_rag.audit_file(files[0], vault_conforme, codes)
        r1_hits = [h for h in result["hits"] if h.startswith("R1")]
        assert r1_hits == [], f"R1 hits inattendus: {r1_hits}"

    def test_absent(self, tmp_path):
        fp = write_md(tmp_path, "bad.md", "# Sans frontmatter\n\nContenu.")
        files = [fp]
        codes = audit_md_rag.vault_codes(files)
        result = audit_md_rag.audit_file(fp, str(tmp_path), codes)
        assert any("R1" in h and ("absent" in h or "invalide" in h) for h in result["hits"])

    def test_champ_manquant(self, tmp_path):
        md = CONFORME.replace("public_cible: [dirigeant, ops]\n", "")
        fp = write_md(tmp_path, "bad.md", md)
        codes = audit_md_rag.vault_codes([fp])
        result = audit_md_rag.audit_file(fp, str(tmp_path), codes)
        assert any("public_cible" in h and "R1" in h for h in result["hits"])

    def test_champ_vide(self, tmp_path):
        md = CONFORME.replace("tags: [veille, recherche]", "tags: []")
        fp = write_md(tmp_path, "bad.md", md)
        codes = audit_md_rag.vault_codes([fp])
        result = audit_md_rag.audit_file(fp, str(tmp_path), codes)
        assert any("R1" in h and "tags" in h for h in result["hits"])

    def test_type_invalide(self, tmp_path):
        md = CONFORME.replace("type: module-cu", "type: bogus")
        fp = write_md(tmp_path, "bad.md", md)
        codes = audit_md_rag.vault_codes([fp])
        result = audit_md_rag.audit_file(fp, str(tmp_path), codes)
        assert any("R1" in h and "bogus" in h for h in result["hits"])


class TestR2H1:
    def test_conforme(self, vault_conforme):
        files = audit_md_rag.list_md_files(vault_conforme)
        codes = audit_md_rag.vault_codes(files)
        result = audit_md_rag.audit_file(files[0], vault_conforme, codes)
        assert [h for h in result["hits"] if h.startswith("R2")] == []

    def test_aucun_h1(self, tmp_path):
        md = CONFORME.replace("# Recherche & veille\n", "")
        fp = write_md(tmp_path, "bad.md", md)
        codes = audit_md_rag.vault_codes([fp])
        result = audit_md_rag.audit_file(fp, str(tmp_path), codes)
        assert any("R2" in h and "aucun H1" in h for h in result["hits"])

    def test_h1_multiple(self, tmp_path):
        md = CONFORME + "\n# Deuxième H1\n\nBoom.\n"
        fp = write_md(tmp_path, "bad.md", md)
        codes = audit_md_rag.vault_codes([fp])
        result = audit_md_rag.audit_file(fp, str(tmp_path), codes)
        assert any("R2" in h and "2 H1" in h for h in result["hits"])

    def test_h1_mismatch_titre(self, tmp_path):
        md = CONFORME.replace("# Recherche & veille", "# Autre chose")
        fp = write_md(tmp_path, "bad.md", md)
        codes = audit_md_rag.vault_codes([fp])
        result = audit_md_rag.audit_file(fp, str(tmp_path), codes)
        assert any("R2" in h and "!=" in h for h in result["hits"])


class TestR3Chunking:
    def test_section_courte_ok(self, vault_conforme):
        files = audit_md_rag.list_md_files(vault_conforme)
        codes = audit_md_rag.vault_codes(files)
        result = audit_md_rag.audit_file(files[0], vault_conforme, codes)
        assert [h for h in result["hits"] if h.startswith("R3")] == []

    def test_section_h2_trop_longue(self, tmp_path):
        long_text = ("mot " * 700).strip()
        md = CONFORME.replace(
            "Démarche en trois temps. Section autonome lisible isolément.",
            long_text,
        )
        fp = write_md(tmp_path, "bad.md", md)
        codes = audit_md_rag.vault_codes([fp])
        result = audit_md_rag.audit_file(fp, str(tmp_path), codes)
        assert any("R3" in h and "subdiviser" in h for h in result["hits"])

    def test_h2_long_avec_h3_courts_ok(self, tmp_path):
        body = CONFORME + textwrap.dedent("""

        ## Grande section

        ### Sous-section A

        Contenu court A.

        ### Sous-section B

        Contenu court B.
        """)
        fp = write_md(tmp_path, "ok.md", body)
        codes = audit_md_rag.vault_codes([fp])
        result = audit_md_rag.audit_file(fp, str(tmp_path), codes)
        assert [h for h in result["hits"] if h.startswith("R3")] == []


class TestR4Wikilinks:
    def test_cible_existante_ok(self, vault_conforme):
        files = audit_md_rag.list_md_files(vault_conforme)
        codes = audit_md_rag.vault_codes(files)
        result = audit_md_rag.audit_file(files[0], vault_conforme, codes)
        assert [h for h in result["hits"] if h.startswith("R4")] == []

    def test_cible_inexistante(self, tmp_path):
        md = CONFORME.replace("[[cu-008|Knowledge base RAG]]", "[[cu-999]]")
        fp = write_md(tmp_path, "bad.md", md)
        codes = audit_md_rag.vault_codes([fp])
        result = audit_md_rag.audit_file(fp, str(tmp_path), codes)
        assert any("R4" in h and "cu-999" in h for h in result["hits"])

    def test_lien_vers_glossaire_ok(self, tmp_path):
        md = CONFORME.replace("[[cu-008|Knowledge base RAG]]", "[[glossaire#rag]]")
        fp = write_md(tmp_path, "ok.md", md)
        codes = audit_md_rag.vault_codes([fp])
        result = audit_md_rag.audit_file(fp, str(tmp_path), codes)
        assert [h for h in result["hits"] if h.startswith("R4")] == []


class TestR6ChiffresSources:
    def test_chiffre_source_ok(self, vault_conforme):
        files = audit_md_rag.list_md_files(vault_conforme)
        codes = audit_md_rag.vault_codes(files)
        result = audit_md_rag.audit_file(files[0], vault_conforme, codes)
        assert [h for h in result["hits"] if h.startswith("R6")] == []

    def test_chiffre_orphelin(self, tmp_path):
        md = CONFORME.replace(
            "95 % des projets GenAI échouent (Source : MIT Sloan / NANDA, août 2025, [URL](https://example.com)).",
            "95 % des projets GenAI échouent, ce qui est notable.",
        )
        fp = write_md(tmp_path, "bad.md", md)
        codes = audit_md_rag.vault_codes([fp])
        result = audit_md_rag.audit_file(fp, str(tmp_path), codes)
        assert any("R6" in h and "95" in h for h in result["hits"])

    def test_chiffre_avec_lien_markdown_ok(self, tmp_path):
        md = CONFORME.replace(
            "95 % des projets GenAI échouent (Source : MIT Sloan / NANDA, août 2025, [URL](https://example.com)).",
            "70 % des dirigeants attendent l'IA [étude Gartner](https://gartner.com).",
        )
        fp = write_md(tmp_path, "ok.md", md)
        codes = audit_md_rag.vault_codes([fp])
        result = audit_md_rag.audit_file(fp, str(tmp_path), codes)
        assert [h for h in result["hits"] if h.startswith("R6")] == []


# ============================================================
# Tests d'intégration : main() + exit code
# ============================================================

class TestMainExitCode:
    def test_exit_zero_si_clean(self, vault_conforme, capsys):
        rc = audit_md_rag.main(["--vault", vault_conforme])
        assert rc == 0
        out = capsys.readouterr().out
        assert "CLEAN" in out

    def test_exit_one_si_hits(self, tmp_path, capsys):
        write_md(tmp_path, "broken.md", "# Sans frontmatter\n\nVide.")
        rc = audit_md_rag.main(["--vault", str(tmp_path)])
        assert rc == 1
        out = capsys.readouterr().out
        assert "broken.md" in out

    def test_rapport_fichier(self, vault_conforme, tmp_path):
        report_path = tmp_path / "report.txt"
        rc = audit_md_rag.main(["--vault", vault_conforme, "--report", str(report_path)])
        assert rc == 0
        assert "CLEAN" in report_path.read_text(encoding="utf-8")

    def test_vault_vide_sans_md(self, tmp_path, capsys):
        rc = audit_md_rag.main(["--vault", str(tmp_path)])
        assert rc == 0


# ============================================================
# Tests unitaires des helpers
# ============================================================

class TestHelpers:
    def test_split_frontmatter_present(self):
        fm, body = audit_md_rag.split_frontmatter(CONFORME)
        assert fm is not None
        assert fm["code"] == "cu-001"
        assert body.startswith("# Recherche")

    def test_split_frontmatter_absent(self):
        fm, body = audit_md_rag.split_frontmatter("# Pas de frontmatter\n\nContent")
        assert fm is None

    def test_estimate_tokens(self):
        assert audit_md_rag.estimate_tokens("un deux trois quatre cinq") == 6

    def test_split_sections(self):
        body = "# H1\n\nIntro.\n\n## A\n\nTexte A.\n\n## B\n\n### B1\n\nTexte B1.\n"
        sections = audit_md_rag.split_sections(body)
        levels = [s[0] for s in sections]
        assert levels == ["h1", "h2", "h2", "h3"]


# ============================================================
# Bloc A (S2.1) — D-028 exception R1 + D-029 whitelist R4
# ============================================================

GLOSSAIRE_RACINE = textwrap.dedent("""\
---
code: glossaire
titre: "Glossaire canonique du Hub IA"
type: transverse
axe: transverse
niveau: 1
tags: [glossaire, definitions]
version: 3.8.4
last_updated: 2026-05-11
glosaire_termes: []
derives: []
public_cible: [dirigeant, ops, r&d, tech, transverse]
---

# Glossaire canonique du Hub IA

## RAG

Définition.
""")

CHIFFRES_MACRO_RACINE = textwrap.dedent("""\
---
code: chiffres-macro-2026
titre: "Chiffres macro IA — référentiel canonique 2026"
type: transverse
axe: transverse
niveau: 2
tags: [chiffres]
version: 3.8.4
last_updated: 2026-05-12
glosaire_termes: []
derives: []
public_cible: [dirigeant, ops, r&d, tech, transverse]
---

# Chiffres macro IA — référentiel canonique 2026

## 95 % — projets GenAI sans ROI (MIT NANDA 2025)

**95 % des projets GenAI** (Source : MIT NANDA 2025).
""")


class TestD028ExceptionR1:
    """D-028 : glosaire_termes et derives peuvent être vides pour les fichiers
    racines transverses (glossaire.md, chiffres-macro-*.md)."""

    def test_glossaire_avec_champs_vides_ne_genere_pas_erreur_r1(self, tmp_path):
        fp = write_md(tmp_path, "glossaire.md", GLOSSAIRE_RACINE)
        codes = audit_md_rag.vault_codes([fp])
        ctx = audit_md_rag.AuditContext(vault_codes=codes)
        result = audit_md_rag.audit_file(fp, str(tmp_path), ctx)
        r1_glosaire_errors = [
            h for h in result["errors"]
            if h.startswith("R1") and ("glosaire_termes" in h or "derives" in h)
        ]
        assert r1_glosaire_errors == [], f"R1 ne devrait pas signaler les champs vides : {r1_glosaire_errors}"

    def test_chiffres_macro_avec_champs_vides_ne_genere_pas_erreur_r1(self, tmp_path):
        fp = write_md(tmp_path / "transverses" if False else tmp_path, "chiffres-macro-2026.md", CHIFFRES_MACRO_RACINE)
        codes = audit_md_rag.vault_codes([fp])
        ctx = audit_md_rag.AuditContext(vault_codes=codes)
        result = audit_md_rag.audit_file(fp, str(tmp_path), ctx)
        r1_glosaire_errors = [
            h for h in result["errors"]
            if h.startswith("R1") and ("glosaire_termes" in h or "derives" in h)
        ]
        assert r1_glosaire_errors == []

    def test_module_ordinaire_avec_champs_vides_garde_erreur_r1(self, tmp_path):
        """L'exception D-028 NE doit PAS s'appliquer aux modules ordinaires."""
        md = CONFORME.replace("derives: [\"[[cu-008]]\"]", "derives: []")
        fp = write_md(tmp_path, "cu-001.md", md)
        codes = audit_md_rag.vault_codes([fp])
        ctx = audit_md_rag.AuditContext(vault_codes=codes)
        result = audit_md_rag.audit_file(fp, str(tmp_path), ctx)
        assert any(h.startswith("R1") and "derives" in h for h in result["errors"])

    def test_transverse_non_racine_garde_erreur_r1(self, tmp_path):
        """Un transverse ordinaire (vigilance-..., pattern-...) ne bénéficie pas de l'exception."""
        md = CONFORME.replace("code: cu-001", "code: vigilance-test")\
                     .replace("type: module-cu", "type: transverse")\
                     .replace("axe: B", "axe: transverse")\
                     .replace("derives: [\"[[cu-008]]\"]", "derives: []")
        fp = write_md(tmp_path, "vigilance-test.md", md)
        codes = audit_md_rag.vault_codes([fp])
        ctx = audit_md_rag.AuditContext(vault_codes=codes)
        result = audit_md_rag.audit_file(fp, str(tmp_path), ctx)
        assert any(h.startswith("R1") and "derives" in h for h in result["errors"])

    def test_helper_is_r1_exception_glossaire(self):
        fm = {"code": "glossaire", "type": "transverse"}
        assert audit_md_rag._is_r1_exception(fm, "glosaire_termes") is True
        assert audit_md_rag._is_r1_exception(fm, "derives") is True
        assert audit_md_rag._is_r1_exception(fm, "tags") is False

    def test_helper_is_r1_exception_chiffres_macro(self):
        fm = {"code": "chiffres-macro-2026", "type": "transverse"}
        assert audit_md_rag._is_r1_exception(fm, "derives") is True
        # variantes d'année autorisées par préfixe
        fm2 = {"code": "chiffres-macro-2027", "type": "transverse"}
        assert audit_md_rag._is_r1_exception(fm2, "derives") is True


class TestD029WhitelistR4:
    """D-029 : wikilinks vers MD planifiés (whitelisted) génèrent un warning
    plutôt qu'une erreur."""

    @pytest.fixture
    def whitelist_path(self, tmp_path_factory):
        # whitelist hors du vault pour éviter qu'elle soit auditée
        wl = tmp_path_factory.mktemp("wl") / "whitelist.md"
        wl.write_text(textwrap.dedent("""\
            # whitelist

            | Code | Titre | Vague |
            |---|---|---|
            | `cu-002` | Assistant rédactionnel | 3 |
            | `cu-014` | Multi-agents | 3 |
            | `pr-04` | Marché IA | 3 |
        """), encoding="utf-8")
        return str(wl)

    def test_load_whitelist_parse_codes(self, whitelist_path):
        codes = audit_md_rag.load_whitelist(whitelist_path)
        assert codes == {"cu-002", "cu-014", "pr-04"}

    def test_load_whitelist_fichier_absent_retourne_set_vide(self, tmp_path):
        codes = audit_md_rag.load_whitelist(str(tmp_path / "introuvable.md"))
        assert codes == set()

    def test_wikilink_whitelisted_genere_warning_pas_erreur(self, tmp_path, whitelist_path):
        # MD qui pointe vers cu-014 (whitelisted), pas dans le vault
        md = CONFORME.replace("[[cu-008]]", "[[cu-014]]").replace("[[cu-008|Knowledge base RAG]]", "[[cu-014|Multi-agents]]")
        fp = write_md(tmp_path, "cu-001.md", md)
        codes = audit_md_rag.vault_codes([fp])
        ctx = audit_md_rag.AuditContext(
            vault_codes=codes,
            whitelist_codes=audit_md_rag.load_whitelist(whitelist_path),
        )
        result = audit_md_rag.audit_file(fp, str(tmp_path), ctx)
        r4_errors = [h for h in result["errors"] if h.startswith("R4")]
        r4_warnings = [h for h in result["warnings"] if h.startswith("R4")]
        assert r4_errors == [], f"cu-014 whitelisted ne doit pas être en erreur : {r4_errors}"
        assert any("cu-014" in w for w in r4_warnings)

    def test_wikilink_inconnu_reste_erreur(self, tmp_path, whitelist_path):
        md = CONFORME.replace("[[cu-008]]", "[[cu-999]]").replace("[[cu-008|Knowledge base RAG]]", "[[cu-999]]")
        fp = write_md(tmp_path, "cu-001.md", md)
        codes = audit_md_rag.vault_codes([fp])
        ctx = audit_md_rag.AuditContext(
            vault_codes=codes,
            whitelist_codes=audit_md_rag.load_whitelist(whitelist_path),
        )
        result = audit_md_rag.audit_file(fp, str(tmp_path), ctx)
        assert any("cu-999" in h for h in result["errors"])

    def test_strict_future_transforme_warning_en_erreur(self, tmp_path, whitelist_path):
        md = CONFORME.replace("[[cu-008]]", "[[cu-014]]").replace("[[cu-008|Knowledge base RAG]]", "[[cu-014]]")
        fp = write_md(tmp_path, "cu-001.md", md)
        codes = audit_md_rag.vault_codes([fp])
        ctx = audit_md_rag.AuditContext(
            vault_codes=codes,
            whitelist_codes=audit_md_rag.load_whitelist(whitelist_path),
            strict_future=True,
        )
        result = audit_md_rag.audit_file(fp, str(tmp_path), ctx)
        r4_errors = [h for h in result["errors"] if "cu-014" in h]
        r4_warnings = [h for h in result["warnings"] if "cu-014" in h]
        assert r4_errors  # erreur en mode strict
        assert "strict-future" in r4_errors[0]
        assert r4_warnings == []

    def test_main_strict_future_flag_active_durcissement(self, tmp_path, whitelist_path, capsys):
        md = CONFORME.replace("[[cu-008]]", "[[cu-014]]").replace("[[cu-008|Knowledge base RAG]]", "[[cu-014]]")
        write_md(tmp_path, "cu-001.md", md)
        rc = audit_md_rag.main([
            "--vault", str(tmp_path),
            "--whitelist", whitelist_path,
            "--strict-future",
        ])
        assert rc == 1
        out = capsys.readouterr().out
        assert "cu-014" in out

    def test_main_sans_strict_future_warning_non_bloquant(self, tmp_path, whitelist_path, capsys):
        md = CONFORME.replace("[[cu-008]]", "[[cu-014]]").replace("[[cu-008|Knowledge base RAG]]", "[[cu-014]]")
        write_md(tmp_path, "cu-001.md", md)
        rc = audit_md_rag.main([
            "--vault", str(tmp_path),
            "--whitelist", whitelist_path,
        ])
        # 0 erreur (warning seulement) ⇒ exit code 0
        assert rc == 0
        out = capsys.readouterr().out
        assert "warning" in out.lower() or "⚠" in out


# ============================================================
# Bloc B (S2.1) — R5 glossaire + R7 nommage + R8 versioning git
# ============================================================

GLOSSAIRE_AVEC_TERMES = textwrap.dedent("""\
---
code: glossaire
titre: "Glossaire canonique du Hub IA"
type: transverse
axe: transverse
niveau: 1
tags: [glossaire]
version: 3.8.4
last_updated: 2026-05-11
glosaire_termes: []
derives: []
public_cible: [dirigeant, ops, r&d, tech, transverse]
---

# Glossaire canonique du Hub IA

## RAG

Retrieval-Augmented Generation.

## Fine-tuning

Modification des poids du modèle.

## Embeddings

Représentation vectorielle.
""")


class TestR5Glossaire:
    """R5 — terme du glossaire utilisé en clair → warning (déduplication)."""

    @pytest.fixture
    def vault_avec_glossaire(self, tmp_path):
        write_md(tmp_path, "glossaire.md", GLOSSAIRE_AVEC_TERMES)
        return str(tmp_path)

    def _ctx(self, vault):
        files = audit_md_rag.list_md_files(vault)
        return audit_md_rag.AuditContext(
            vault_codes=audit_md_rag.vault_codes(files),
            glossaire_terms=audit_md_rag.load_glossaire_terms(vault),
        )

    def test_load_glossaire_terms_extrait_h2(self, vault_avec_glossaire):
        terms = audit_md_rag.load_glossaire_terms(vault_avec_glossaire)
        assert "rag" in terms
        assert "fine-tuning" in terms
        assert "embeddings" in terms

    def test_terme_en_clair_genere_warning(self, vault_avec_glossaire):
        md = CONFORME.replace(
            "Démarche en trois temps.",
            "Démarche en trois temps. On parle ici de Fine-tuning et d'embeddings.",
        )
        fp = write_md(vault_avec_glossaire, "cu-001.md", md)
        ctx = self._ctx(vault_avec_glossaire)
        result = audit_md_rag.audit_file(fp, vault_avec_glossaire, ctx)
        r5_warnings = [w for w in result["warnings"] if w.startswith("R5")]
        terms_signaled = {w for w in r5_warnings if "fine-tuning" in w.lower() or "embeddings" in w.lower()}
        assert len(terms_signaled) == 2  # dédupliqué par terme

    def test_terme_via_wikilink_pas_warning(self, vault_avec_glossaire):
        md = CONFORME.replace(
            "Démarche en trois temps.",
            "Démarche citant [[glossaire#fine-tuning]] et [[glossaire#embeddings]].",
        )
        fp = write_md(vault_avec_glossaire, "cu-001.md", md)
        ctx = self._ctx(vault_avec_glossaire)
        result = audit_md_rag.audit_file(fp, vault_avec_glossaire, ctx)
        r5_warnings = [
            w for w in result["warnings"]
            if w.startswith("R5") and ("fine-tuning" in w.lower() or "embeddings" in w.lower())
        ]
        assert r5_warnings == []

    def test_r5_n_est_pas_appliquee_au_glossaire_lui_meme(self, vault_avec_glossaire):
        fp = os.path.join(vault_avec_glossaire, "glossaire.md")
        ctx = self._ctx(vault_avec_glossaire)
        result = audit_md_rag.audit_file(fp, vault_avec_glossaire, ctx)
        r5_warnings = [w for w in result["warnings"] if w.startswith("R5")]
        assert r5_warnings == []

    def test_r5_warnings_pas_erreurs(self, vault_avec_glossaire):
        """R5 produit des warnings, jamais des erreurs (première itération SPEC §10)."""
        md = CONFORME.replace(
            "Démarche en trois temps.",
            "Démarche, et Fine-tuning sont mentionnés.",
        )
        fp = write_md(vault_avec_glossaire, "cu-001.md", md)
        ctx = self._ctx(vault_avec_glossaire)
        result = audit_md_rag.audit_file(fp, vault_avec_glossaire, ctx)
        r5_errors = [h for h in result["errors"] if h.startswith("R5")]
        assert r5_errors == []


class TestR7Nommage:
    """R7 — conformité du nom de fichier."""

    @pytest.mark.parametrize("name", [
        "cu-001.md", "cu-008.md", "pr-07.md", "dep-02.md", "a1.md",
        "outils-vector-db.md", "outils-llm-gateway.md",
        "glossaire.md",
        "transverse-test.md", "vigilance-hallucinations.md",
        "pattern-llm-wiki.md", "chiffres-macro-2026.md",
        "methodologie-prompt-engineering.md", "cadrage-ai-act.md",
    ])
    def test_noms_conformes(self, tmp_path, name):
        fp = write_md(tmp_path, name, CONFORME)
        result = audit_md_rag.check_r7_nommage(fp)
        assert result.errors == [], f"{name} devrait être valide"

    @pytest.mark.parametrize("name", [
        "Module_001.md",        # underscore + casse
        "MaFiche.md",
        "cu_001.md",            # underscore
        "test.md",               # pas de famille
        "cu-001.markdown",       # mauvaise extension
        "outils.md",             # outils sans catégorie
    ])
    def test_noms_non_conformes(self, tmp_path, name):
        fp = write_md(tmp_path, name, CONFORME)
        result = audit_md_rag.check_r7_nommage(fp)
        assert any("R7" in e for e in result.errors), f"{name} devrait déclencher R7"


class TestR8Versioning:
    """R8 — last_updated vs git mtime, tolérance 7 jours."""

    def test_parse_last_updated_iso_string(self):
        d = audit_md_rag._parse_last_updated("2026-05-12")
        assert d == date(2026, 5, 12)

    def test_parse_last_updated_date_object(self):
        d = audit_md_rag._parse_last_updated(date(2026, 5, 12))
        assert d == date(2026, 5, 12)

    def test_parse_last_updated_invalide(self):
        assert audit_md_rag._parse_last_updated("pas une date") is None
        assert audit_md_rag._parse_last_updated(None) is None

    def test_skip_si_git_indisponible(self, tmp_path):
        fp = write_md(tmp_path, "cu-001.md", CONFORME)
        fm, _ = audit_md_rag.split_frontmatter(CONFORME)
        ctx = audit_md_rag.AuditContext()
        result = audit_md_rag.check_r8_versioning(
            fp, fm, ctx,
            git_mtime_func=lambda fp, repo_root: None,
        )
        assert result.errors == []

    def test_ecart_acceptable_pas_erreur(self, tmp_path):
        fp = write_md(tmp_path, "cu-001.md", CONFORME)
        fm, _ = audit_md_rag.split_frontmatter(CONFORME)
        ctx = audit_md_rag.AuditContext()
        # last_updated du CONFORME = 2026-05-11 ; git = 2026-05-12 → 1 jour
        result = audit_md_rag.check_r8_versioning(
            fp, fm, ctx,
            git_mtime_func=lambda fp, repo_root: date(2026, 5, 12),
        )
        assert result.errors == []

    def test_ecart_excessif_erreur(self, tmp_path):
        fp = write_md(tmp_path, "cu-001.md", CONFORME)
        fm, _ = audit_md_rag.split_frontmatter(CONFORME)
        ctx = audit_md_rag.AuditContext()
        # last_updated = 2026-05-11 ; git = 2026-06-15 → 35 jours
        result = audit_md_rag.check_r8_versioning(
            fp, fm, ctx,
            git_mtime_func=lambda fp, repo_root: date(2026, 6, 15),
        )
        assert any("R8" in e and "35 jours" in e for e in result.errors)

    def test_last_updated_invalide_erreur(self, tmp_path):
        md = CONFORME.replace("last_updated: 2026-05-11", "last_updated: invalid-date")
        fp = write_md(tmp_path, "cu-001.md", md)
        fm, _ = audit_md_rag.split_frontmatter(md)
        ctx = audit_md_rag.AuditContext()
        result = audit_md_rag.check_r8_versioning(fp, fm, ctx)
        assert any("R8" in e and "non parseable" in e for e in result.errors)


# ============================================================
# Bloc C (S2.1) — R6 étendu + R9 chiffres macro canoniques
# ============================================================

CHIFFRES_MACRO_FULL = textwrap.dedent("""\
---
code: chiffres-macro-2026
titre: "Chiffres macro IA — référentiel canonique 2026"
type: transverse
axe: transverse
niveau: 2
tags: [chiffres]
version: 3.8.4
last_updated: 2026-05-12
glosaire_termes: []
derives: []
public_cible: [dirigeant, ops, r&d, tech, transverse]
---

# Chiffres macro IA — référentiel canonique 2026

## 95 % — projets GenAI sans ROI (MIT NANDA 2025)

Source : MIT NANDA 2025.

## 67 % — dirigeants PME/TPE (Bpifrance 2025)

Source : Bpifrance Le Lab 2025.

## 21 % — organisations IA ayant redesigné leurs workflows (McKinsey 2025)

Source : McKinsey 2025.
""")


class TestR6Etendu:
    """R6 — wikilink vers chiffres-macro-* reconnu comme source canonique."""

    def test_chiffre_sourcé_par_wikilink_transverse_ok(self, tmp_path):
        md = CONFORME.replace(
            "95 % des projets GenAI échouent (Source : MIT Sloan / NANDA, août 2025, [URL](https://example.com)).",
            "[[chiffres-macro-2026#95-pourcent-mit-nanda|95 % des projets GenAI sans ROI]] (MIT NANDA 2025).",
        )
        fp = write_md(tmp_path, "cu-001.md", md)
        ctx = audit_md_rag.AuditContext(vault_codes=audit_md_rag.vault_codes([fp]))
        result = audit_md_rag.audit_file(fp, str(tmp_path), ctx)
        r6_errors = [e for e in result["errors"] if e.startswith("R6")]
        assert r6_errors == [], f"Le wikilink chiffres-macro devrait suffire comme source : {r6_errors}"

    def test_chiffre_orphelin_sans_wikilink_garde_erreur_r6(self, tmp_path):
        md = CONFORME.replace(
            "95 % des projets GenAI échouent (Source : MIT Sloan / NANDA, août 2025, [URL](https://example.com)).",
            "95 % des projets GenAI échouent sans la moindre référence.",
        )
        fp = write_md(tmp_path, "cu-001.md", md)
        ctx = audit_md_rag.AuditContext(vault_codes=audit_md_rag.vault_codes([fp]))
        result = audit_md_rag.audit_file(fp, str(tmp_path), ctx)
        assert any(e.startswith("R6") for e in result["errors"])


class TestR9ChiffresMacro:
    """R9 — chiffre canonique du Hub cité en clair → warning."""

    @pytest.fixture
    def vault_avec_chiffres(self, tmp_path):
        transverses = tmp_path / "transverses"
        transverses.mkdir()
        (transverses / "chiffres-macro-2026.md").write_text(CHIFFRES_MACRO_FULL, encoding="utf-8")
        return str(tmp_path)

    def _ctx(self, vault):
        files = audit_md_rag.list_md_files(vault)
        return audit_md_rag.AuditContext(
            vault_codes=audit_md_rag.vault_codes(files),
            canonical_chiffres=audit_md_rag.load_canonical_chiffres(
                os.path.join(vault, "transverses", "chiffres-macro-2026.md")
            ),
        )

    def test_load_canonical_chiffres(self, vault_avec_chiffres):
        chiffres = audit_md_rag.load_canonical_chiffres(
            os.path.join(vault_avec_chiffres, "transverses", "chiffres-macro-2026.md")
        )
        values = [c["value"] for c in chiffres]
        assert "95 %" in values or "95 %" in [c["value"] for c in chiffres]
        assert "67 %" in values
        assert "21 %" in values

    def test_chiffre_macro_en_clair_warning(self, vault_avec_chiffres):
        md = CONFORME.replace(
            "Démarche en trois temps.",
            "On observe que 67 % des PME/TPE peinent à démarrer. Démarche en trois temps.",
        )
        fp = write_md(vault_avec_chiffres, "cu-001.md", md)
        ctx = self._ctx(vault_avec_chiffres)
        result = audit_md_rag.audit_file(fp, vault_avec_chiffres, ctx)
        r9_warnings = [w for w in result["warnings"] if w.startswith("R9") and "67" in w]
        assert r9_warnings, f"R9 devrait signaler 67 % en clair : {result['warnings']}"

    def test_chiffre_macro_wikilinké_pas_warning(self, vault_avec_chiffres):
        md = CONFORME.replace(
            "Démarche en trois temps.",
            "Comme [[chiffres-macro-2026#67-pourcent-bpifrance|67 % des PME]] l'illustrent.",
        )
        fp = write_md(vault_avec_chiffres, "cu-001.md", md)
        ctx = self._ctx(vault_avec_chiffres)
        result = audit_md_rag.audit_file(fp, vault_avec_chiffres, ctx)
        r9_warnings = [w for w in result["warnings"] if w.startswith("R9") and "67 %" in w]
        assert r9_warnings == [], f"Le wikilink devrait suffire : {r9_warnings}"

    def test_r9_skip_sur_chiffres_macro_lui_meme(self, vault_avec_chiffres):
        """Le fichier chiffres-macro-2026.md lui-même contient les chiffres en clair :
        c'est la source canonique, R9 doit le skip."""
        fp = os.path.join(vault_avec_chiffres, "transverses", "chiffres-macro-2026.md")
        ctx = self._ctx(vault_avec_chiffres)
        result = audit_md_rag.audit_file(fp, vault_avec_chiffres, ctx)
        r9_warnings = [w for w in result["warnings"] if w.startswith("R9")]
        assert r9_warnings == []

    def test_r9_skip_sur_glossaire(self, vault_avec_chiffres):
        """Le glossaire est aussi exempté de R9 pour éviter le bruit
        si une définition contient un chiffre macro."""
        glossaire_md = GLOSSAIRE_AVEC_TERMES.replace(
            "Retrieval-Augmented Generation.",
            "Retrieval-Augmented Generation. 95 % des cas PME couverts.",
        )
        glossaire_fp = write_md(vault_avec_chiffres, "glossaire.md", glossaire_md)
        ctx = self._ctx(vault_avec_chiffres)
        result = audit_md_rag.audit_file(glossaire_fp, vault_avec_chiffres, ctx)
        r9_warnings = [w for w in result["warnings"] if w.startswith("R9")]
        assert r9_warnings == []

    def test_r9_deduplication_par_chiffre(self, vault_avec_chiffres):
        """Plusieurs occurrences du même chiffre → 1 seul warning."""
        md = CONFORME.replace(
            "Démarche en trois temps.",
            "Pour 67 % des PME, c'est un défi. Et 67 % le confirment encore. Et toujours 67 %.",
        )
        fp = write_md(vault_avec_chiffres, "cu-001.md", md)
        ctx = self._ctx(vault_avec_chiffres)
        result = audit_md_rag.audit_file(fp, vault_avec_chiffres, ctx)
        r9_warnings = [w for w in result["warnings"] if w.startswith("R9") and "67" in w]
        assert len(r9_warnings) == 1

    def test_r9_pas_d_erreurs_seulement_warnings(self, vault_avec_chiffres):
        md = CONFORME.replace(
            "Démarche en trois temps.",
            "Selon nous, 21 % des organisations ont redesigné. Démarche.",
        )
        fp = write_md(vault_avec_chiffres, "cu-001.md", md)
        ctx = self._ctx(vault_avec_chiffres)
        result = audit_md_rag.audit_file(fp, vault_avec_chiffres, ctx)
        r9_errors = [e for e in result["errors"] if e.startswith("R9")]
        assert r9_errors == []

    def test_r9_contexte_sans_chiffres_canoniques_skip(self, tmp_path):
        """Si chiffres-macro-2026.md n'existe pas, R9 ne fait rien."""
        fp = write_md(tmp_path, "cu-001.md", CONFORME)
        ctx = audit_md_rag.AuditContext(canonical_chiffres=[])
        result = audit_md_rag.audit_file(fp, str(tmp_path), ctx)
        r9 = [w for w in result["warnings"] if w.startswith("R9")]
        assert r9 == []
