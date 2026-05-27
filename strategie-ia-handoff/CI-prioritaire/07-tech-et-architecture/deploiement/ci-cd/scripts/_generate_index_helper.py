#!/usr/bin/env python3
"""Helper Python pour `generate-index.sh` — extraction métadonnées MD + render INDEX.md.

Auteur          : Cowork Hub IA Plateforme (Claude Code)
Date            : 2026-05-27
Owner           : 07-tech-et-architecture
Confidentialité : public
Statut          : validé

Préfixé `_` pour signaler qu'il s'agit d'un helper privé du script bash
`generate-index.sh`, pas d'un script à appeler directement (convention §11
exceptions techniques + clarté pour relecture humaine).

Usage interne :
    python3 _generate_index_helper.py --root /path/to/strategie-ia
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from datetime import date
from pathlib import Path

CATEGORIES = [
    "01-strategie",
    "02-finance",
    "03-recherche-et-analyse",
    "04-juridique",
    "05-marque-et-design",
    "06-produit-et-site",
    "07-tech-et-architecture",
    "08-contenu-editorial",
    "09-rag-et-ia",
    "10-commercial-et-marketing",
    "11-gouvernance",
    "12-orchestration-agents",
    "13-veille",
]

ROOT_GOVERNANCE = [
    "README.md", "INDEX.md", "CONVENTIONS.md", "GLOSSAIRE.md",
    "CONTRIBUTING.md", "CODEOWNERS", "ROADMAP.md", "CHANGELOG.md",
    "FRONTIERES.md",
]

EXCLUDED_PARTS = {"_archives", ".git", "node_modules", "__pycache__"}


def extract_meta(text: str) -> dict[str, str]:
    """Extrait Version / Date / Confidentialité / Statut / Owner depuis l'en-tête MD."""
    header = "\n".join(text.splitlines()[:60])
    fields: dict[str, str] = {}
    for name in ["Version", "Date de création", "Dernière mise à jour",
                 "Confidentialité", "Statut", "Owner fonctionnel", "Auteur principal"]:
        m = re.search(rf"\*\*{re.escape(name)}\*\*\s*:\s*([^\n*]+)", header)
        if m:
            fields[name] = m.group(1).strip().strip("`*")
    # Date la plus récente (fallback : ISO trouvée).
    if "Dernière mise à jour" in fields:
        iso = re.search(r"\d{4}-\d{2}-\d{2}", fields["Dernière mise à jour"])
        if iso:
            fields["_date_iso"] = iso.group(0)
    elif "Date de création" in fields:
        iso = re.search(r"\d{4}-\d{2}-\d{2}", fields["Date de création"])
        if iso:
            fields["_date_iso"] = iso.group(0)
    if "_date_iso" not in fields:
        iso = re.search(r"\d{4}-\d{2}-\d{2}", header)
        if iso:
            fields["_date_iso"] = iso.group(0)
    # Version simplifiée (extraire "v1.0" depuis "v1.0 — 27 mai 2026" éventuel).
    if "Version" in fields:
        vm = re.search(r"v?\d+(?:\.\d+)*", fields["Version"])
        if vm:
            fields["_version_short"] = vm.group(0)
    return fields


def category_owner(root: Path, cat: str) -> str:
    readme = root / cat / "README.md"
    if not readme.exists():
        return "—"
    text = readme.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"\*\*Owner fonctionnel\*\*\s*:\s*([^\n*]+)", text)
    if m:
        return m.group(1).strip().strip("`*")
    return "—"


def list_md_in_category(root: Path, cat: str) -> list[Path]:
    cat_dir = root / cat
    if not cat_dir.is_dir():
        return []
    out: list[Path] = []
    for p in cat_dir.rglob("*.md"):
        if any(part in EXCLUDED_PARTS for part in p.parts):
            continue
        out.append(p)
    return sorted(out)


def render_row(path: Path, root: Path) -> str:
    rel = str(path.relative_to(root)).replace(os.sep, "/")
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return f"| [`{path.name}`](./{rel}) | — | — | — | — |"
    meta = extract_meta(text)
    version = meta.get("_version_short", meta.get("Version", "—"))
    date_iso = meta.get("_date_iso", "—")
    conf = meta.get("Confidentialité", "—").lower()
    statut = meta.get("Statut", "—").lower()
    return f"| [`{path.name}`](./{rel}) | {version} | {date_iso} | {conf} | {statut} |"


def render_root_governance(root: Path) -> list[str]:
    lines = ["## Fichiers de gouvernance racine", ""]
    lines.append("| Document | Version | Date | Confidentialité | Statut |")
    lines.append("|----------|---------|------|-----------------|--------|")
    for name in ROOT_GOVERNANCE:
        path = root / name
        if not path.exists():
            continue
        if name == "CODEOWNERS":
            lines.append(f"| [`{name}`](./{name}) | — | — | public | validé |")
            continue
        lines.append(render_row(path, root))
    lines.append("")
    return lines


def category_display_title(root: Path, cat: str) -> str:
    """Extrait le H1 du README de catégorie si présent, sinon dérive du nom kebab."""
    readme = root / cat / "README.md"
    if readme.exists():
        text = readme.read_text(encoding="utf-8", errors="replace")
        m = re.search(r"^#\s+(.+?)\s*$", text, re.MULTILINE)
        if m:
            return m.group(1).strip()
    # Fallback : "01-strategie" → "01 — strategie"
    return re.sub(r"^(\d{2})-(.+)$", r"\1 — \2", cat).replace("-", " ")


def render_category(root: Path, cat: str) -> list[str]:
    cat_dir = root / cat
    if not cat_dir.is_dir():
        return []
    title = category_display_title(root, cat)
    owner = category_owner(root, cat)
    lines = [f"## {title}", "", f"**Owner fonctionnel** : {owner}", ""]
    files = list_md_in_category(root, cat)
    if not files:
        lines.append("*Aucun document publié à ce jour.*")
        lines.append("")
        return lines
    lines.append("| Document | Version | Date | Confidentialité | Statut |")
    lines.append("|----------|---------|------|-----------------|--------|")
    for path in files:
        lines.append(render_row(path, root))
    lines.append("")
    return lines


def render_transverses(root: Path) -> list[str]:
    lines = ["## Dossiers transverses", ""]
    for name, desc in [
        ("_archives", "versions antérieures déclassées (timestampées)"),
        ("_handoffs", "briefs entrants/sortants entre agents (matière en cours)"),
        (".config", "configuration repo : templates + scripts CI/CD"),
    ]:
        if (root / name).exists():
            lines.append(f"- [`{name}/`](./{name}/) — {desc}")
    lines.append("")
    return lines


def render(root: Path) -> str:
    today = date.today().isoformat()
    out: list[str] = [
        "# INDEX — repo `strategie-ia`",
        "",
        f"**Version** : généré automatiquement",
        f"**Dernière mise à jour** : {today}",
        f"**Statut** : généré",
        f"**Confidentialité** : public",
        "",
        "> ℹ️ Cet INDEX est régénéré automatiquement par "
        "`07-tech-et-architecture/deploiement/ci-cd/scripts/generate-index.sh`.",
        "> Ne pas éditer manuellement — les modifications seraient écrasées au prochain run.",
        "",
        "---",
        "",
    ]
    out.extend(render_root_governance(root))
    out.append("---")
    out.append("")
    for cat in CATEGORIES:
        if (root / cat).is_dir():
            out.extend(render_category(root, cat))
            out.append("---")
            out.append("")
    out.extend(render_transverses(root))
    out.append("---")
    out.append("")
    out.append(f"*Index généré le {today} via `generate-index.sh`.*")
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True)
    args = parser.parse_args(argv)
    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"[erreur] racine introuvable : {root}", file=sys.stderr)
        return 2
    print(render(root))
    return 0


if __name__ == "__main__":
    sys.exit(main())
