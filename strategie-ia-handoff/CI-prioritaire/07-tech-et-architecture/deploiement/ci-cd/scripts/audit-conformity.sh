#!/usr/bin/env bash
# audit-conformity.sh — point d'entrée bash de l'audit de conformité repo strategie-ia
#
# Délègue à audit_conformity.py (Python pour parsing YAML/Markdown robuste).
# Conformément à §11 CONVENTIONS : wrapper bash en kebab-case, helper Python en snake_case.
#
# Usage :
#   ./audit-conformity.sh                  # audit complet du repo (CWD = racine)
#   ./audit-conformity.sh --staged         # audit du diff Git seulement (CI/pre-commit)
#   ./audit-conformity.sh --strict         # exit 1 si au moins 1 warning
#   ./audit-conformity.sh --files a.md b.py
#
# Exit codes : 0 conforme | 1 écart détecté | 2 erreur d'exécution

set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PY_SCRIPT="${HERE}/audit_conformity.py"

if [[ ! -f "${PY_SCRIPT}" ]]; then
  echo "[erreur] audit_conformity.py introuvable : ${PY_SCRIPT}" >&2
  exit 2
fi

if ! command -v python3 >/dev/null 2>&1; then
  echo "[erreur] python3 requis (>= 3.9)" >&2
  exit 2
fi

# Hygiène merge SPEC v2.0 (héritée hub-ia) : vérification préalable des marqueurs de conflit.
# Bloque l'audit si des marqueurs `<<<<<<<` apparaissent dans le code (pas dans la doc).
if git rev-parse --git-dir >/dev/null 2>&1; then
  if git grep -l '^<<<<<<< ' -- '*.py' '*.sh' '*.yml' '*.yaml' '*.ts' '*.tsx' 2>/dev/null | head -1 | grep -q .; then
    echo "[erreur] marqueurs de conflit `<<<<<<<` détectés dans le code source — résoudre avant audit." >&2
    git grep -l '^<<<<<<< ' -- '*.py' '*.sh' '*.yml' '*.yaml' '*.ts' '*.tsx' 2>/dev/null | sed 's/^/  /' >&2
    exit 1
  fi
fi

exec python3 "${PY_SCRIPT}" "$@"
