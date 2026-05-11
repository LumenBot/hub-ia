#!/usr/bin/env python3
"""
Audit conformité MD du vault RAG — v1
=====================================

Script qui parcourt tous les fichiers .md de `rag/content/` et applique les
5 règles minimales définies en §10 de `SPEC-MD-POUR-RAG.md` v1.

À lancer avant tout commit qui modifie le vault :
    python3 rag/code/audit/audit-md-rag.py

Options :
    --vault PATH   chemin du vault (défaut : rag/content)
    --report PATH  chemin de sortie du rapport (défaut : stdout)
    --strict       exit code 1 dès la première erreur (CI)

Sortie :
    rapport texte structuré (un bloc par fichier détecté + total)
    code retour 0 si 0 hit, 1 si hits détectés

Couvre 5 règles minimales (v1 — D-016, D-023) :
    R1-frontmatter-complet : 10 champs canoniques présents et non vides
    R2-h1-unique           : un seul H1, identique au champ `titre`
    R3-chunking-respecte   : aucune section H2 > 800 tokens sans subdivision H3
    R4-wikilinks-valides   : toutes les cibles wikilink existent dans le vault
    R6-chiffres-sources    : chiffre statistique suivi d'une mention de source

Style aligné sur `site-web-prep/audit-global.py` (couple 1).

Réfs : D-016, D-023, SPEC-MD-POUR-RAG.md v1 §10.
"""

from __future__ import annotations

import argparse
import glob
import os
import re
import sys
from typing import Iterable

try:
    import yaml
except ImportError:
    print("[erreur] pyyaml requis : pip install pyyaml", file=sys.stderr)
    sys.exit(2)


ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DEFAULT_VAULT = os.path.join(ROOT, "content")

FRONTMATTER_FIELDS = [
    "code",
    "titre",
    "type",
    "axe",
    "niveau",
    "tags",
    "version",
    "last_updated",
    "glosaire_termes",
    "derives",
    "public_cible",
]

TYPE_ALLOWED = {"module-cu", "prealable-pr", "deploiement-dep", "architecture", "fiche-outil", "transverse"}
AXE_ALLOWED = {"A", "B", "C", "D", "E", "agentique", "transverse"}
NIVEAU_ALLOWED = {1, 2, 3, 4}
PUBLIC_ALLOWED = {"dirigeant", "ops", "r&d", "tech", "transverse"}

CHUNK_TOKEN_LIMIT = 800
TOKENS_PER_WORD = 1.3

NUMBER_PATTERNS = [
    re.compile(r"\b\d+\s?%"),
    re.compile(r"\b\d+(?:[.,]\d+)?\s?[x×]\b", re.IGNORECASE),
    re.compile(r"\b\d+(?:[.,]\d+)?\s?[kK]€"),
    re.compile(r"\b\d+(?:[.,]\d+)?\s?M€"),
]
SOURCE_MARKERS = re.compile(r"(Source\s*:|\[[^\]]+\]\([^)]+\)|URL)", re.IGNORECASE)
WIKILINK_PATTERN = re.compile(r"\[\[([^\]\|#]+)(?:#[^\]\|]+)?(?:\|[^\]]+)?\]\]")


# ============================================================
# Helpers
# ============================================================

def list_md_files(vault: str) -> list[str]:
    return sorted(glob.glob(os.path.join(vault, "**", "*.md"), recursive=True))


def rel(fp: str, vault: str) -> str:
    return os.path.relpath(fp, vault)


def read(fp: str) -> str:
    with open(fp, encoding="utf-8") as f:
        return f.read()


def split_frontmatter(text: str) -> tuple[dict | None, str]:
    """Retourne (frontmatter_dict, body). frontmatter_dict=None si absent."""
    if not text.startswith("---\n") and not text.startswith("---\r\n"):
        return None, text
    end = text.find("\n---", 4)
    if end == -1:
        return None, text
    fm_raw = text[4:end]
    body = text[end + 4:].lstrip("\n")
    try:
        data = yaml.safe_load(fm_raw) or {}
        if not isinstance(data, dict):
            return None, body
        return data, body
    except yaml.YAMLError:
        return None, body


def estimate_tokens(text: str) -> int:
    """Estimation grossière du nombre de tokens (~1.3 token/mot)."""
    words = len(text.split())
    return int(words * TOKENS_PER_WORD)


def split_sections(body: str) -> list[tuple[str, str, str]]:
    """Découpe le corps en sections (level, title, body).

    level ∈ {"h1", "h2", "h3"}. body inclut le titre.
    """
    lines = body.splitlines(keepends=True)
    sections: list[tuple[str, str, str]] = []
    current_level = None
    current_title = None
    current_buf: list[str] = []

    for line in lines:
        m = re.match(r"^(#{1,3})\s+(.+?)\s*$", line.rstrip("\n"))
        if m:
            if current_level is not None:
                sections.append((current_level, current_title or "", "".join(current_buf)))
            depth = len(m.group(1))
            current_level = f"h{depth}"
            current_title = m.group(2).strip()
            current_buf = [line]
        else:
            current_buf.append(line)

    if current_level is not None:
        sections.append((current_level, current_title or "", "".join(current_buf)))

    return sections


def vault_codes(files: Iterable[str]) -> set[str]:
    """Indexe les codes de fichiers du vault (basename sans .md + champ `code` du frontmatter)."""
    codes: set[str] = set()
    for fp in files:
        base = os.path.splitext(os.path.basename(fp))[0]
        codes.add(base.lower())
        try:
            text = read(fp)
            fm, _ = split_frontmatter(text)
            if fm and isinstance(fm.get("code"), str):
                codes.add(fm["code"].strip().lower())
        except Exception:
            pass
    codes.add("glossaire")
    return codes


# ============================================================
# Règle R1 — Frontmatter complet
# ============================================================

def check_r1_frontmatter(fp: str, fm: dict | None) -> list[str]:
    hits: list[str] = []
    if fm is None:
        hits.append("R1: frontmatter YAML absent ou invalide")
        return hits

    for field in FRONTMATTER_FIELDS:
        if field not in fm:
            hits.append(f"R1: champ frontmatter manquant `{field}`")
            continue
        value = fm[field]
        if value is None or value == "" or value == [] or value == {}:
            hits.append(f"R1: champ frontmatter vide `{field}`")

    if "type" in fm and fm["type"] not in TYPE_ALLOWED:
        hits.append(f"R1: type `{fm['type']}` hors valeurs autorisées {sorted(TYPE_ALLOWED)}")
    if "axe" in fm and fm["axe"] not in AXE_ALLOWED:
        hits.append(f"R1: axe `{fm['axe']}` hors valeurs autorisées {sorted(AXE_ALLOWED)}")
    if "niveau" in fm and fm["niveau"] not in NIVEAU_ALLOWED:
        hits.append(f"R1: niveau `{fm['niveau']}` hors {sorted(NIVEAU_ALLOWED)}")
    if "public_cible" in fm and isinstance(fm["public_cible"], list):
        bad = [p for p in fm["public_cible"] if p not in PUBLIC_ALLOWED]
        if bad:
            hits.append(f"R1: public_cible invalide {bad} (autorisés : {sorted(PUBLIC_ALLOWED)})")

    return hits


# ============================================================
# Règle R2 — H1 unique, identique au titre
# ============================================================

def check_r2_h1(fp: str, fm: dict | None, body: str) -> list[str]:
    hits: list[str] = []
    h1s = re.findall(r"^#\s+(.+?)\s*$", body, flags=re.MULTILINE)
    if len(h1s) == 0:
        hits.append("R2: aucun H1 détecté")
        return hits
    if len(h1s) > 1:
        hits.append(f"R2: {len(h1s)} H1 détectés (un seul autorisé)")

    if fm and "titre" in fm and isinstance(fm["titre"], str):
        titre = fm["titre"].strip().strip('"').strip("'")
        if h1s[0].strip() != titre:
            hits.append(f"R2: H1 `{h1s[0].strip()}` != frontmatter.titre `{titre}`")

    return hits


# ============================================================
# Règle R3 — Chunking : H2 > 800 tokens doit être subdivisé en H3
# ============================================================

def check_r3_chunking(fp: str, body: str) -> list[str]:
    hits: list[str] = []
    sections = split_sections(body)

    i = 0
    while i < len(sections):
        level, title, content = sections[i]
        if level != "h2":
            i += 1
            continue

        children: list[tuple[str, str, str]] = []
        j = i + 1
        while j < len(sections) and sections[j][0] == "h3":
            children.append(sections[j])
            j += 1

        if children:
            for ch_level, ch_title, ch_content in children:
                tokens = estimate_tokens(ch_content)
                if tokens > CHUNK_TOKEN_LIMIT:
                    hits.append(
                        f"R3: section H3 `{title} > {ch_title}` ≈ {tokens} tokens (> {CHUNK_TOKEN_LIMIT})"
                    )
        else:
            tokens = estimate_tokens(content)
            if tokens > CHUNK_TOKEN_LIMIT:
                hits.append(
                    f"R3: section H2 `{title}` ≈ {tokens} tokens (> {CHUNK_TOKEN_LIMIT}, à subdiviser en H3)"
                )

        i = j if children else i + 1

    return hits


# ============================================================
# Règle R4 — Wikilinks vers cibles existantes
# ============================================================

def check_r4_wikilinks(fp: str, body: str, known_codes: set[str]) -> list[str]:
    hits: list[str] = []
    for match in WIKILINK_PATTERN.finditer(body):
        target = match.group(1).strip().lower()
        if not target:
            hits.append("R4: wikilink vide `[[]]`")
            continue
        if target not in known_codes:
            hits.append(f"R4: wikilink `[[{target}]]` → cible inexistante dans le vault")
    return hits


# ============================================================
# Règle R6 — Chiffres sourcés
# ============================================================

def check_r6_chiffres(fp: str, body: str) -> list[str]:
    hits: list[str] = []
    for pat in NUMBER_PATTERNS:
        for m in pat.finditer(body):
            start = m.start()
            window = body[start:start + 200]
            if not SOURCE_MARKERS.search(window):
                snippet = body[max(0, start - 20):start + 40].replace("\n", " ").strip()
                hits.append(f"R6: chiffre `{m.group(0)}` sans source proche — contexte: «{snippet}»")
    return hits


# ============================================================
# Orchestration
# ============================================================

def audit_file(fp: str, vault: str, known_codes: set[str]) -> dict:
    text = read(fp)
    fm, body = split_frontmatter(text)
    hits: list[str] = []
    hits.extend(check_r1_frontmatter(fp, fm))
    hits.extend(check_r2_h1(fp, fm, body))
    hits.extend(check_r3_chunking(fp, body))
    hits.extend(check_r4_wikilinks(fp, body, known_codes))
    hits.extend(check_r6_chiffres(fp, body))
    return {"file": rel(fp, vault), "hits": hits}


def format_report(results: list[dict], vault: str) -> str:
    total_files = len(results)
    files_with_hits = [r for r in results if r["hits"]]
    total_hits = sum(len(r["hits"]) for r in results)

    lines: list[str] = []
    lines.append("=" * 70)
    lines.append("AUDIT MD-RAG v1 — rapport")
    lines.append("=" * 70)
    lines.append(f"Vault          : {vault}")
    lines.append(f"Fichiers audités: {total_files}")
    lines.append(f"Fichiers en erreur: {len(files_with_hits)}")
    lines.append(f"Total écarts   : {total_hits}")
    lines.append("")

    if not files_with_hits:
        lines.append("✅ CLEAN — aucun écart détecté.")
        return "\n".join(lines) + "\n"

    by_rule: dict[str, int] = {}
    for r in files_with_hits:
        for h in r["hits"]:
            rule = h.split(":", 1)[0]
            by_rule[rule] = by_rule.get(rule, 0) + 1

    lines.append("Répartition par règle :")
    for rule in sorted(by_rule):
        lines.append(f"  {rule}: {by_rule[rule]} écart(s)")
    lines.append("")

    for r in files_with_hits:
        lines.append("-" * 70)
        lines.append(f"📄 {r['file']} — {len(r['hits'])} écart(s)")
        for h in r["hits"]:
            lines.append(f"  • {h}")
    lines.append("")
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Audit conformité MD vault RAG (SPEC v1).")
    parser.add_argument("--vault", default=DEFAULT_VAULT, help="chemin du vault (défaut: rag/content)")
    parser.add_argument("--report", default=None, help="chemin de sortie (défaut: stdout)")
    parser.add_argument("--strict", action="store_true", help="exit 1 dès première erreur")
    args = parser.parse_args(argv)

    vault = os.path.abspath(args.vault)
    if not os.path.isdir(vault):
        print(f"[erreur] vault introuvable : {vault}", file=sys.stderr)
        return 2

    files = list_md_files(vault)
    if not files:
        report = f"⚠️  Aucun fichier .md trouvé dans {vault}\n"
        if args.report:
            with open(args.report, "w", encoding="utf-8") as f:
                f.write(report)
        else:
            print(report)
        return 0

    known_codes = vault_codes(files)
    results = [audit_file(fp, vault, known_codes) for fp in files]
    report = format_report(results, vault)

    if args.report:
        with open(args.report, "w", encoding="utf-8") as f:
            f.write(report)
    else:
        print(report)

    total_hits = sum(len(r["hits"]) for r in results)
    return 1 if total_hits > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
