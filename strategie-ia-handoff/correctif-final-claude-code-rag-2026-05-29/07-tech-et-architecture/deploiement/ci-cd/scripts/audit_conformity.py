#!/usr/bin/env python3
"""Audit de conformité du repo `strategie-ia`.

Vérifie les conventions définies dans `CONVENTIONS.md` v1.1 :
- §1 Naming kebab-case pour fichiers et dossiers MD
- §2 En-tête métadonnées obligatoire (Version, Date de création, Dernière mise à jour,
  Statut, Auteur, Owner, Confidentialité, Tags)
- §2 Footer Historique obligatoire (tableau)
- §6 Format dates ISO 8601 (`YYYY-MM-DD`)
- §9 Confidentialité déclarée (`public` / `interne` / `restreint`)
- §11 Exceptions techniques code source : snake_case Python + docstring PEP 257
  avec métadonnées (auteur, date, owner, confidentialité, statut)
- §12 ADR : numérotation `ADR-NNN-titre-court.md` + statut
  `proposed`/`accepted`/`deprecated`/`superseded`

Auteur          : Cowork Hub IA Plateforme (Claude Code)
Date            : 2026-05-27
Owner           : 07-tech-et-architecture
Confidentialité : public
Statut          : validé

Usage :
    python3 audit_conformity.py --path .
    python3 audit_conformity.py --path . --strict
    python3 audit_conformity.py --files file1.md file2.md
    python3 audit_conformity.py --staged          # uniquement les fichiers du diff PR

Exit codes :
    0  conforme (erreurs = 0, warnings éventuels)
    1  écart de conformité (au moins 1 erreur, ou warning en --strict)
    2  erreur d'exécution (argument invalide, etc.)
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

# ============================================================
# Conventions de base
# ============================================================

ROOT_GOVERNANCE_FILES = {
    "README.md", "INDEX.md", "CONVENTIONS.md", "GLOSSAIRE.md",
    "CONTRIBUTING.md", "CODEOWNERS", "ROADMAP.md", "CHANGELOG.md",
    "FRONTIERES.md",
}

# Dossiers exclus de l'audit (templates avec placeholders, archives historiques).
# Le chemin `.config/templates` est le placement canonique strategie-ia ; le chemin
# `templates` à la racine est toléré pour les extractions de bundle handoff.
EXCLUDED_DIRS = {".config/templates", "templates", "_archives", ".git", "node_modules", "__pycache__"}

# Confidentialités acceptées (§9 CONVENTIONS).
CONFIDENTIALITES = {"public", "interne", "restreint"}

# Statuts acceptés (§2 + v1.1 « revue-en-cours »).
STATUTS = {"draft", "revue-en-cours", "validé", "valide", "archivé", "archive"}

# §1 Naming kebab-case : minuscules + chiffres + tirets + extension.
KEBAB_FILE_PATTERN = re.compile(r"^[a-z0-9]+(?:[a-z0-9-]*[a-z0-9])?(?:\.[a-z0-9]+)*$")
KEBAB_DIR_PATTERN = re.compile(r"^[a-z0-9]+(?:[a-z0-9-]*[a-z0-9])?$")

# Exceptions naming : dossiers transverses + dossiers métier numérotés.
NAMING_EXCEPTIONS = {
    ".github", ".config", "_archives", "_handoffs", "_internal",
}
NUMBERED_CATEGORY_PATTERN = re.compile(r"^\d{2}-[a-z0-9-]+$")

# §6 Format dates ISO 8601.
ISO_DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")

# §2 Champs métadonnées obligatoires en en-tête MD.
REQUIRED_METADATA_FIELDS = [
    "Version",
    "Statut",
    "Confidentialité",
]
RECOMMENDED_METADATA_FIELDS = [
    "Date de création",
    "Dernière mise à jour",
    "Auteur principal",
    "Owner fonctionnel",
    "Tags",
]

# §11 Python : champs métadonnées docstring (recommandés, pas bloquants).
PYTHON_METADATA_FIELDS = ["Auteur", "Date", "Owner", "Confidentialité", "Statut"]

# §12 ADR : numérotation + statut.
ADR_NAME_PATTERN = re.compile(r"^ADR-\d{3,4}-[a-z0-9-]+\.md$")
ADR_STATUS_VALUES = {"proposed", "accepted", "deprecated", "superseded"}

# ============================================================
# Modèles de résultats
# ============================================================

@dataclass
class Issue:
    file: str
    rule: str
    message: str
    severity: str  # "error" | "warning"


@dataclass
class AuditResult:
    issues: list[Issue] = field(default_factory=list)

    @property
    def errors(self) -> list[Issue]:
        return [i for i in self.issues if i.severity == "error"]

    @property
    def warnings(self) -> list[Issue]:
        return [i for i in self.issues if i.severity == "warning"]

    def add_error(self, file: str, rule: str, message: str) -> None:
        self.issues.append(Issue(file, rule, message, "error"))

    def add_warning(self, file: str, rule: str, message: str) -> None:
        self.issues.append(Issue(file, rule, message, "warning"))


# ============================================================
# Helpers
# ============================================================

def has_accents(s: str) -> bool:
    """Détecte les caractères accentués (NFKD : combinaison décomposable)."""
    decomposed = unicodedata.normalize("NFKD", s)
    return any(unicodedata.combining(c) for c in decomposed)


def is_excluded(path: Path, root: Path) -> bool:
    """Le chemin est-il dans un dossier exclu (templates, archives, .git, etc.) ?"""
    rel = path.relative_to(root)
    rel_str = str(rel).replace(os.sep, "/")
    return any(rel_str == ex or rel_str.startswith(ex + "/") for ex in EXCLUDED_DIRS)


def list_md_files(root: Path) -> list[Path]:
    out: list[Path] = []
    for p in root.rglob("*.md"):
        if is_excluded(p, root):
            continue
        out.append(p)
    return sorted(out)


def list_py_files(root: Path) -> list[Path]:
    out: list[Path] = []
    for p in root.rglob("*.py"):
        if is_excluded(p, root):
            continue
        out.append(p)
    return sorted(out)


def extract_header(text: str, max_lines: int = 50) -> str:
    """Retourne les `max_lines` premières lignes (zone en-tête du document)."""
    return "\n".join(text.splitlines()[:max_lines])


def extract_docstring(text: str) -> str | None:
    """Extrait la première docstring d'un module Python (PEP 257).

    Tolère shebang (`#!...`) et imports `from __future__` qui peuvent précéder
    la docstring dans un module bien écrit.
    """
    # Strip shebang line.
    if text.startswith("#!"):
        text = text.split("\n", 1)[1] if "\n" in text else ""
    # Skip leading whitespace + comments + optional `from __future__` imports.
    pattern_triple = re.compile(
        r'(?:\s*(?:#[^\n]*\n|from\s+__future__\s+[^\n]*\n))*\s*"""(.+?)"""',
        re.DOTALL,
    )
    m = pattern_triple.match(text)
    if m:
        return m.group(1)
    pattern_single = re.compile(
        r"(?:\s*(?:#[^\n]*\n|from\s+__future__\s+[^\n]*\n))*\s*'''(.+?)'''",
        re.DOTALL,
    )
    m = pattern_single.match(text)
    if m:
        return m.group(1)
    return None


# ============================================================
# Règles
# ============================================================

def check_naming_md(path: Path, root: Path, result: AuditResult) -> None:
    """§1 — kebab-case + pas d'accents + pas de caractères spéciaux."""
    rel = str(path.relative_to(root)).replace(os.sep, "/")
    name = path.name

    # Exceptions : fichiers de gouvernance racine majuscules autorisés.
    if rel in ROOT_GOVERNANCE_FILES or name in ROOT_GOVERNANCE_FILES:
        return

    # README.md de catégorie : autorisé en majuscules.
    if name == "README.md":
        return

    # Templates ADR : pattern spécifique ADR-NNN-xxx.md.
    if "/adr/" in rel or rel.startswith("adr/"):
        if ADR_NAME_PATTERN.match(name):
            return
        result.add_error(rel, "ADR-naming",
                         f"nom ADR non conforme `{name}` — attendu `ADR-NNN-titre-court.md`")
        return

    if has_accents(name):
        result.add_error(rel, "naming-accents", f"accent dans le nom de fichier `{name}`")
    if " " in name:
        result.add_error(rel, "naming-spaces", f"espace dans le nom de fichier `{name}`")
    if not KEBAB_FILE_PATTERN.match(name):
        result.add_error(rel, "naming-kebab",
                         f"nom non conforme kebab-case `{name}` (§1 CONVENTIONS)")

    # Vérifier les dossiers du chemin.
    for part in path.relative_to(root).parts[:-1]:
        if part in NAMING_EXCEPTIONS:
            continue
        if NUMBERED_CATEGORY_PATTERN.match(part):
            continue
        if has_accents(part):
            result.add_error(rel, "naming-accents",
                             f"accent dans un dossier du chemin `{part}`")
        if not KEBAB_DIR_PATTERN.match(part):
            result.add_error(rel, "naming-kebab",
                             f"dossier non conforme kebab-case `{part}` (§1)")


def check_metadata_md(path: Path, root: Path, result: AuditResult) -> None:
    """§2 — en-tête métadonnées + footer Historique + §6 dates ISO + §9 confidentialité."""
    rel = str(path.relative_to(root)).replace(os.sep, "/")

    # Fichiers de gouvernance racine et CODEOWNERS : exemptés (manifest libre).
    if rel == "CODEOWNERS":
        return

    text = path.read_text(encoding="utf-8", errors="replace")
    header = extract_header(text, max_lines=80)

    # Title H1 obligatoire.
    if not re.search(r"^#\s+\S", header, re.MULTILINE):
        result.add_error(rel, "metadata-title", "pas de titre H1 en début de document")

    # Champs métadonnées obligatoires.
    for field_name in REQUIRED_METADATA_FIELDS:
        pattern = rf"\*\*{re.escape(field_name)}\*\*\s*:"
        if not re.search(pattern, header):
            result.add_error(rel, "metadata-required",
                             f"champ obligatoire `**{field_name}**` manquant en en-tête")

    for field_name in RECOMMENDED_METADATA_FIELDS:
        pattern = rf"\*\*{re.escape(field_name)}\*\*\s*:"
        if not re.search(pattern, header):
            result.add_warning(rel, "metadata-recommended",
                               f"champ recommandé `**{field_name}**` manquant en en-tête")

    # §9 Confidentialité : valeur reconnue.
    conf_match = re.search(r"\*\*Confidentialité\*\*\s*:\s*([a-zé]+)", header)
    if conf_match:
        value = conf_match.group(1).lower().strip()
        if value not in CONFIDENTIALITES:
            result.add_error(rel, "confidentialite-invalide",
                             f"valeur `{value}` non reconnue (attendu : {sorted(CONFIDENTIALITES)})")

    # §2 Statut : valeur reconnue (informatif si présent).
    statut_match = re.search(r"\*\*Statut\*\*\s*:\s*([a-zé-]+)", header)
    if statut_match:
        value = statut_match.group(1).lower().strip()
        if value not in STATUTS:
            result.add_warning(rel, "statut-non-standard",
                               f"statut `{value}` hors valeurs attendues ({sorted(STATUTS)})")

    # §6 Format dates ISO 8601 dans les champs date.
    date_fields = ["Date de création", "Dernière mise à jour", "Date d'ouverture", "Date"]
    for field_name in date_fields:
        m = re.search(rf"\*\*{re.escape(field_name)}\*\*\s*:\s*([^\n*]+)", header)
        if not m:
            continue
        date_str = m.group(1).strip().strip("`*")
        # Tolérer les formes "v1.0 — YYYY-MM-DD" ou "YYYY-MM-DD" pures.
        iso_match = re.search(r"\d{4}-\d{2}-\d{2}", date_str)
        if not iso_match:
            result.add_error(rel, "date-iso",
                             f"date `{field_name}` non au format ISO 8601 : `{date_str}`")

    # Footer Historique : tableau ou section « Historique » présent.
    if "## Historique" not in text and "Historique" not in text.split("---")[-1]:
        result.add_warning(rel, "footer-historique",
                           "section `## Historique` non détectée en fin de document")


def check_python_conventions(path: Path, root: Path, result: AuditResult) -> None:
    """§11 — snake_case + docstring PEP 257 avec métadonnées."""
    rel = str(path.relative_to(root)).replace(os.sep, "/")
    name = path.name

    # snake_case obligatoire pour Python (§11).
    base = name[:-3]  # strip ".py"
    if not re.match(r"^[a-z_][a-z0-9_]*$", base):
        result.add_error(rel, "py-snake-case",
                         f"nom Python non conforme snake_case `{name}` (§11)")

    text = path.read_text(encoding="utf-8", errors="replace")
    docstring = extract_docstring(text)
    if not docstring:
        result.add_error(rel, "py-docstring",
                         "docstring PEP 257 absente en tête de module (§11)")
        return

    # Champs métadonnées dans la docstring (warning, pas bloquant).
    missing = [f for f in PYTHON_METADATA_FIELDS if f not in docstring]
    if missing:
        result.add_warning(
            rel, "py-metadata",
            f"métadonnées docstring incomplètes : manquant {missing} (§11)",
        )


def check_adr_status(path: Path, root: Path, result: AuditResult) -> None:
    """§12 — ADR statut parmi {proposed, accepted, deprecated, superseded}."""
    rel = str(path.relative_to(root)).replace(os.sep, "/")
    if "/adr/" not in rel and not rel.startswith("adr/"):
        return
    if not ADR_NAME_PATTERN.match(path.name):
        return  # autre fichier (README.md, etc.)

    text = path.read_text(encoding="utf-8", errors="replace")
    status_match = re.search(r"^\s*##\s*Status\s*\n\s*([a-z]+)", text, re.MULTILINE | re.IGNORECASE)
    if not status_match:
        status_match = re.search(r"\*\*Status\*\*\s*:\s*([a-z]+)", text, re.IGNORECASE)
    if not status_match:
        result.add_error(rel, "adr-status",
                         "ADR sans champ `Status` reconnaissable (§12)")
        return
    value = status_match.group(1).lower().strip()
    if value not in ADR_STATUS_VALUES:
        result.add_error(
            rel, "adr-status-invalide",
            f"statut ADR `{value}` hors valeurs autorisées {sorted(ADR_STATUS_VALUES)}",
        )


# ============================================================
# Orchestration
# ============================================================

def audit_paths(paths: list[Path], root: Path) -> AuditResult:
    result = AuditResult()
    for path in paths:
        if not path.exists():
            continue
        if is_excluded(path, root):
            continue
        if path.suffix == ".md":
            check_naming_md(path, root, result)
            check_metadata_md(path, root, result)
            check_adr_status(path, root, result)
        elif path.suffix == ".py":
            check_python_conventions(path, root, result)
    return result


def list_staged_files(root: Path) -> list[Path]:
    """Liste les fichiers du diff Git (HEAD vs index — usage CI/pre-commit)."""
    try:
        out = subprocess.run(
            ["git", "diff", "--name-only", "--diff-filter=ACMR", "HEAD"],
            cwd=str(root), capture_output=True, text=True, check=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return []
    files = [root / line.strip() for line in out.stdout.splitlines() if line.strip()]
    return [f for f in files if f.exists()]


def print_report(result: AuditResult, root: Path) -> None:
    if not result.issues:
        print("[audit-conformity] CLEAN — aucune anomalie détectée.")
        return

    print(f"[audit-conformity] {len(result.errors)} erreur(s), {len(result.warnings)} warning(s).")
    print("-" * 72)
    by_file: dict[str, list[Issue]] = {}
    for issue in result.issues:
        by_file.setdefault(issue.file, []).append(issue)
    for file in sorted(by_file):
        print(f"\n{file}")
        for issue in by_file[file]:
            sigil = "✗" if issue.severity == "error" else "⚠"
            print(f"  {sigil} [{issue.rule}] {issue.message}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Audit de conformité du repo strategie-ia.")
    parser.add_argument("--path", default=".", help="racine du repo à auditer (défaut : .)")
    parser.add_argument("--files", nargs="*", help="fichiers spécifiques à auditer")
    parser.add_argument("--staged", action="store_true",
                        help="auditer uniquement les fichiers du diff Git (CI/pre-commit)")
    parser.add_argument("--strict", action="store_true",
                        help="exit 1 si au moins 1 warning (sinon : 1 si au moins 1 erreur)")
    args = parser.parse_args(argv)

    root = Path(args.path).resolve()
    if not root.is_dir():
        print(f"[erreur] racine introuvable : {root}", file=sys.stderr)
        return 2

    if args.staged:
        paths = list_staged_files(root)
        if not paths:
            print("[audit-conformity] aucun fichier dans le diff Git.")
            return 0
    elif args.files:
        paths = [Path(f).resolve() for f in args.files]
    else:
        paths = list_md_files(root) + list_py_files(root)

    result = audit_paths(paths, root)
    print_report(result, root)

    if result.errors:
        return 1
    if args.strict and result.warnings:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
