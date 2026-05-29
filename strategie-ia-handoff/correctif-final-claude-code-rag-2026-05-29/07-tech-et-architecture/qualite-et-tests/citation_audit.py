#!/usr/bin/env python3
"""
Audit R11 — Wikilinks outils glossariés
========================================

Implémente la règle R11 inscrite SPEC v1.4 §audit v3 et activée S2.8 (BRIEF-CC-S2.8 §4) :

> R11 : tout outil ayant sa propre fiche `outils-*.md` dans le vault, lorsqu'il
> est mentionné dans un autre MD, doit être **wikilinké à sa première occurrence**
> dans ce MD (ex. première mention « Mistral » dans `pr-05.md` doit être
> `[[outils-llm#mistral]]` ou `[[outils-llm|Mistral]]` au moins une fois dans le
> fichier).

Activation conditionnée à 5+ fiches `outils-*.md` produites — seuil franchi en
S2.7 (6 fiches : outils-vector-db S1 + 5 fiches vague 7 : outils-llm,
outils-frameworks-rag, outils-knowledge-management, outils-observabilite-llm,
outils-workflow-automation).

Algorithme (BRIEF-CC-S2.8 §4.2) :

1. Parser tous les fichiers `rag/content/ressources/outils-*.md` → extraire la
   liste canonique des outils (par section H2 par outil).
2. Pour chaque autre MD du vault (modules/, prealables/, deploiement/,
   architectures/, transverses/), parcourir le texte en cherchant les mentions
   d'outils.
3. Pour la **première occurrence en clair** (hors wikilink) de chaque outil
   dans le MD : vérifier qu'un wikilink vers la fiche source apparaît au plus
   tard à cette position.
4. Reporter au format Markdown + JSON les MD avec mentions outils sans
   wikilink à la première occurrence.

Usage :

    python3 rag/code/audit/citation_audit.py \
        --report rag-prep/reports/audit-md-rag-R11-s2.8.md \
        --json rag-prep/reports/audit-md-rag-R11-s2.8.json

Options :
    --vault PATH      chemin du vault (défaut : rag/content)
    --report PATH     rapport Markdown (défaut : stdout)
    --json PATH       export JSON (optionnel)
    --strict          exit 1 si au moins 1 manquement détecté

Réfs : SPEC-MD-POUR-RAG.md v1.4 §audit v3 + v2.2 §Validation,
BRIEF-CC-S2.8 §4, D-022 (Plateforme code uniquement).
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys
import unicodedata
from dataclasses import dataclass, field

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DEFAULT_VAULT = os.path.join(ROOT, "content")
RESSOURCES_SUBDIR = "ressources"
OUTILS_FICHE_GLOB = "outils-*.md"

# H2 dont le titre ne représente pas un outil mais une section de méta-contenu
# de la fiche (intro, comparatif, recommandations, etc.). Casse-insensible,
# matché par préfixe du titre H2.
NON_TOOL_H2_PREFIXES = (
    "quand",
    "comparatif",
    "recommandations",
    "pour aller",
    "outils ",  # « Outils satellites à mentionner », « Outils hybrides ... »
)

# Wikilinks Obsidian (toutes formes : nu, ancre, alias).
WIKILINK_PATTERN = re.compile(r"\[\[([^\]\|#]+)(?:#[^\]\|]+)?(?:\|[^\]]+)?\]\]")
# Spans englobants `[[...]]` pour exclure les mentions à l'intérieur.
WIKILINK_SPAN_PATTERN = re.compile(r"\[\[[^\]]+\]\]")


# ============================================================
# Structures
# ============================================================

@dataclass(frozen=True)
class Tool:
    """Outil canonique extrait d'une fiche `outils-*.md`.

    - `display_name` : nom tel qu'affiché dans le H2 (« Mistral », « n8n », « Phoenix Arize »).
    - `aliases` : variantes acceptées comme mention en clair (split « / » du H2).
    - `source_fiche` : basename sans .md de la fiche source (« outils-llm »).
    - `anchor` : slug Obsidian de la section H2 d'origine (« mistral »).
    """

    display_name: str
    aliases: tuple[str, ...]
    source_fiche: str
    anchor: str


@dataclass
class Manquement:
    """Manquement R11 détecté pour un (fichier, outil) donné."""

    file: str           # chemin relatif au vault
    tool: str           # display_name de l'outil
    source_fiche: str   # « outils-llm »
    line: int           # ligne de la première occurrence en clair (1-indexed)
    snippet: str        # extrait de la ligne (max 120 chars)


@dataclass
class FileResult:
    """Résultat R11 par fichier."""

    file: str
    manquements: list[Manquement] = field(default_factory=list)
    ok_mentions: list[str] = field(default_factory=list)  # noms d'outils correctement wikilinkés


# ============================================================
# Helpers (alignés sur audit-md-rag.py)
# ============================================================

def list_md_files(vault: str) -> list[str]:
    return sorted(glob.glob(os.path.join(vault, "**", "*.md"), recursive=True))


def rel(fp: str, vault: str) -> str:
    return os.path.relpath(fp, vault)


def read(fp: str) -> str:
    with open(fp, encoding="utf-8") as f:
        return f.read()


def split_frontmatter(text: str) -> tuple[str, str]:
    """Retourne (frontmatter_raw, body). Sans dépendance YAML : on coupe juste
    sur les fences `---` pour pouvoir mesurer correctement les lignes du body.
    """
    if not text.startswith("---\n") and not text.startswith("---\r\n"):
        return "", text
    end = text.find("\n---", 4)
    if end == -1:
        return "", text
    fm_raw = text[:end + 4]
    body = text[end + 4:].lstrip("\n")
    return fm_raw, body


def split_sections(body: str) -> list[tuple[str, str]]:
    """Découpe le body en (h2_title, h2_block) — seuls les H2 nous intéressent
    pour extraire les outils. Les H1/H3 sont ignorés ici.
    """
    sections: list[tuple[str, str]] = []
    current_title: str | None = None
    buf: list[str] = []
    for line in body.splitlines(keepends=True):
        m = re.match(r"^##\s+(.+?)\s*$", line.rstrip("\n"))
        if m and not line.startswith("###"):
            if current_title is not None:
                sections.append((current_title, "".join(buf)))
            current_title = m.group(1).strip()
            buf = [line]
        else:
            if current_title is not None:
                buf.append(line)
    if current_title is not None:
        sections.append((current_title, "".join(buf)))
    return sections


def slugify(text: str) -> str:
    """Slug Obsidian-style (NFKD + alnum + tirets)."""
    s = unicodedata.normalize("NFKD", text)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower().strip()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-") or "section"


# ============================================================
# Étape 1 — Parsing des fiches outils-*.md
# ============================================================

def _is_non_tool_h2(title: str) -> bool:
    low = title.strip().lower()
    return any(low.startswith(p) for p in NON_TOOL_H2_PREFIXES)


def extract_tool_names(h2_title: str) -> list[str]:
    """Extrait la liste d'aliases d'un titre H2 d'outil.

    Heuristique :
    - On découpe sur le séparateur ` — ` (em-dash entouré d'espaces) pour
      isoler la partie « nom (vendeur) » à gauche.
    - On retire le suffixe parenthétique « (Vendeur) ».
    - On découpe sur ` / ` pour gérer les multi-noms (ex. « Kimi K2 / K2.6 »).

    Retourne `[]` si le H2 n'est pas reconnu comme un outil.
    """
    if _is_non_tool_h2(h2_title):
        return []
    head = h2_title.split(" — ")[0].strip()
    if not head or _is_non_tool_h2(head):
        return []
    head = re.sub(r"\s*\([^)]*\)\s*$", "", head).strip()
    if not head:
        return []
    parts = [p.strip() for p in head.split(" / ") if p.strip()]
    return parts


def parse_outils_fiches(vault: str) -> list[Tool]:
    """Parse toutes les fiches `outils-*.md` et retourne la liste canonique
    des outils (une entrée par outil, possiblement plusieurs aliases).
    """
    ressources_dir = os.path.join(vault, RESSOURCES_SUBDIR)
    tools: list[Tool] = []
    seen_aliases: set[str] = set()  # détection collisions inter-fiches
    for fp in sorted(glob.glob(os.path.join(ressources_dir, OUTILS_FICHE_GLOB))):
        fiche_code = os.path.splitext(os.path.basename(fp))[0]
        _, body = split_frontmatter(read(fp))
        for title, _ in split_sections(body):
            aliases = extract_tool_names(title)
            if not aliases:
                continue
            display = aliases[0]
            anchor = slugify(display)
            tools.append(Tool(
                display_name=display,
                aliases=tuple(aliases),
                source_fiche=fiche_code,
                anchor=anchor,
            ))
            for a in aliases:
                key = a.lower()
                if key in seen_aliases:
                    # Collision : un même alias pour deux fiches outils.
                    # On garde la première occurrence, sans erreur — ce cas
                    # devrait rester rare (à traiter Cowork-side si signalé).
                    pass
                seen_aliases.add(key)
    return tools


# ============================================================
# Étape 2 — Détection des mentions et des wikilinks
# ============================================================

def _wikilink_spans(text: str) -> list[tuple[int, int]]:
    return [(m.start(), m.end()) for m in WIKILINK_SPAN_PATTERN.finditer(text)]


def _is_inside_spans(pos: int, spans: list[tuple[int, int]]) -> bool:
    for s, e in spans:
        if s <= pos < e:
            return True
    return False


def find_wikilink_positions(body: str, target_fiche: str) -> list[int]:
    """Positions de début des wikilinks `[[target_fiche...]]` (toutes formes :
    nu, `#ancre`, `|alias`). Casse-insensible sur la cible.
    """
    positions: list[int] = []
    target_low = target_fiche.lower()
    for m in WIKILINK_PATTERN.finditer(body):
        if m.group(1).strip().lower() == target_low:
            positions.append(m.start())
    return positions


def find_first_naked_occurrence(body: str, aliases: tuple[str, ...]) -> tuple[int, int] | None:
    """Retourne (position, longueur) de la première mention en clair (hors
    wikilink) d'un des aliases. Comparaison **case-sensitive** sur les noms
    canoniques (les H2 sont déjà proprement capitalisés ; case-sensitive évite
    les faux positifs sur les mots anglais comme « Make », « Llama »).
    """
    spans = _wikilink_spans(body)
    best: tuple[int, int] | None = None
    for alias in aliases:
        pattern = re.compile(rf"(?<![\w-]){re.escape(alias)}(?![\w-])")
        for m in pattern.finditer(body):
            pos = m.start()
            if _is_inside_spans(pos, spans):
                continue
            if best is None or pos < best[0]:
                best = (pos, m.end() - m.start())
                break  # plus petite position pour cet alias trouvée
    return best


def line_of(body: str, pos: int) -> tuple[int, str]:
    """Retourne (numero_ligne_1indexed, ligne) pour la position `pos` dans `body`."""
    line_start = body.rfind("\n", 0, pos) + 1
    line_end = body.find("\n", pos)
    if line_end == -1:
        line_end = len(body)
    line_text = body[line_start:line_end]
    line_num = body.count("\n", 0, pos) + 1
    return line_num, line_text


# ============================================================
# Étape 3 — Application R11 par fichier
# ============================================================

def check_r11_for_file(fp: str, vault: str, tools: list[Tool]) -> FileResult:
    """Applique R11 à un fichier MD. Retourne `FileResult` listant les
    manquements détectés. Skip si `fp` est une fiche outils-*.md (R11 ne
    s'applique pas à la fiche d'origine elle-même).
    """
    rel_fp = rel(fp, vault)
    result = FileResult(file=rel_fp)

    # R11 ne s'applique pas aux fiches outils-*.md (auto-référence).
    fp_basename = os.path.splitext(os.path.basename(fp))[0]
    if fp_basename.startswith("outils-"):
        return result

    # On exclut le frontmatter (qui peut contenir des termes côté `tags`
    # ou `glosaire_termes` sans rapport avec une mention rédactionnelle)
    # mais on conserve l'offset de ligne pour pouvoir reporter une position
    # cohérente avec ce que l'éditeur affiche.
    text = read(fp)
    fm_raw, body = split_frontmatter(text)
    body_start = len(text) - len(body)
    fm_line_offset = text[:body_start].count("\n")

    for tool in tools:
        naked = find_first_naked_occurrence(body, tool.aliases)
        if naked is None:
            continue
        naked_pos = naked[0]
        wikilink_positions = find_wikilink_positions(body, tool.source_fiche)
        if wikilink_positions and min(wikilink_positions) <= naked_pos:
            result.ok_mentions.append(tool.display_name)
            continue

        line_in_body, line_text = line_of(body, naked_pos)
        line_num = line_in_body + fm_line_offset
        snippet = line_text.strip()
        if len(snippet) > 120:
            snippet = snippet[:117] + "..."
        result.manquements.append(Manquement(
            file=rel_fp,
            tool=tool.display_name,
            source_fiche=tool.source_fiche,
            line=line_num,
            snippet=snippet,
        ))
    return result


# ============================================================
# Étape 4 — Reporting
# ============================================================

def format_md_report(results: list[FileResult], tools: list[Tool], vault: str) -> str:
    total_files = len(results)
    files_with_manq = [r for r in results if r.manquements]
    total_manq = sum(len(r.manquements) for r in results)
    total_ok = sum(len(r.ok_mentions) for r in results)

    lines: list[str] = []
    lines.append("# R11 audit — wikilinks outils glossariés")
    lines.append("")
    lines.append(f"- **Vault** : `{vault}`")
    lines.append(f"- **Fiches outils parsées** : {len({t.source_fiche for t in tools})}")
    lines.append(f"- **Outils canoniques détectés** : {len(tools)}")
    lines.append(f"- **Fichiers MD audités** : {total_files}")
    lines.append(f"- **Fichiers avec manquements R11** : {len(files_with_manq)}")
    lines.append(f"- **Mentions outils correctes (wikilink présent)** : {total_ok}")
    lines.append(f"- **Manquements R11 totaux** : {total_manq}")
    lines.append("")

    if total_manq == 0:
        lines.append("CLEAN — aucun manquement R11 détecté.")
        return "\n".join(lines) + "\n"

    lines.append("## Détail des manquements")
    lines.append("")
    lines.append("| Fichier MD | Outil mentionné | Première occurrence (ligne) | Recommandation |")
    lines.append("|---|---|---|---|")
    for r in results:
        for m in r.manquements:
            reco = f"Ajouter `[[{m.source_fiche}|{m.tool}]]` à la première occurrence (L{m.line})"
            lines.append(f"| `{m.file}` | {m.tool} | L{m.line} : `{m.snippet}` | {reco} |")
    lines.append("")
    lines.append(f"**Total** : {total_manq} manquements détectés sur {len(files_with_manq)} fichier(s).")
    return "\n".join(lines) + "\n"


def to_json_payload(results: list[FileResult], tools: list[Tool], vault: str) -> dict:
    return {
        "rule": "R11",
        "spec_ref": "SPEC-MD-POUR-RAG.md v1.4 §audit v3 + BRIEF-CC-S2.8 §4",
        "vault": vault,
        "summary": {
            "fiches_parsed": len({t.source_fiche for t in tools}),
            "tools_canonical": len(tools),
            "files_audited": len(results),
            "files_with_manquements": sum(1 for r in results if r.manquements),
            "manquements_total": sum(len(r.manquements) for r in results),
            "ok_mentions_total": sum(len(r.ok_mentions) for r in results),
        },
        "tools_index": [
            {
                "display_name": t.display_name,
                "aliases": list(t.aliases),
                "source_fiche": t.source_fiche,
                "anchor": t.anchor,
            }
            for t in tools
        ],
        "manquements": [
            {
                "file": m.file,
                "tool": m.tool,
                "source_fiche": m.source_fiche,
                "line": m.line,
                "snippet": m.snippet,
                "recommendation": f"[[{m.source_fiche}|{m.tool}]]",
            }
            for r in results for m in r.manquements
        ],
    }


# ============================================================
# Orchestration
# ============================================================

def run_audit(vault: str) -> tuple[list[FileResult], list[Tool]]:
    tools = parse_outils_fiches(vault)
    files = list_md_files(vault)
    results = [check_r11_for_file(fp, vault, tools) for fp in files]
    return results, tools


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Audit R11 — wikilinks outils glossariés (SPEC v2.2 / BRIEF-CC-S2.8).")
    parser.add_argument("--vault", default=DEFAULT_VAULT, help="chemin du vault (défaut : rag/content)")
    parser.add_argument("--report", default=None, help="rapport Markdown (défaut : stdout)")
    parser.add_argument("--json", default=None, help="export JSON (optionnel)")
    parser.add_argument("--strict", action="store_true", help="exit 1 si au moins 1 manquement")
    args = parser.parse_args(argv)

    vault = os.path.abspath(args.vault)
    if not os.path.isdir(vault):
        print(f"[erreur] vault introuvable : {vault}", file=sys.stderr)
        return 2

    results, tools = run_audit(vault)
    report_md = format_md_report(results, tools, vault)

    if args.report:
        os.makedirs(os.path.dirname(os.path.abspath(args.report)) or ".", exist_ok=True)
        with open(args.report, "w", encoding="utf-8") as f:
            f.write(report_md)
    else:
        print(report_md)

    if args.json:
        os.makedirs(os.path.dirname(os.path.abspath(args.json)) or ".", exist_ok=True)
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(to_json_payload(results, tools, vault), f, ensure_ascii=False, indent=2)

    total_manq = sum(len(r.manquements) for r in results)
    if args.strict and total_manq > 0:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
