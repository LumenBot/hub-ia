#!/usr/bin/env bash
# generate-index.sh — génération automatique de INDEX.md à partir des en-têtes MD
#
# Auteur          : Cowork Hub IA Plateforme (Claude Code)
# Date            : 2026-05-27
# Owner           : 07-tech-et-architecture
# Confidentialité : public
# Statut          : validé
#
# Walks tous les fichiers MD du repo, extrait les métadonnées (Version, Date,
# Confidentialité, Statut), et génère INDEX.md à la racine. Délègue à un helper
# Python pour le parsing robuste des en-têtes ; fallback bash minimal si Python absent.
#
# Usage :
#   ./generate-index.sh                  # génère INDEX.md à la racine (CWD = racine du repo)
#   ./generate-index.sh --check          # mode vérification : exit 1 si désynchronisation
#   ./generate-index.sh --output FILE    # destination alternative
#
# Exit codes : 0 OK | 1 désynchronisation détectée (--check) | 2 erreur d'exécution

set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PY_HELPER="${HERE}/_generate_index_helper.py"
ROOT="$(pwd)"
OUTPUT="${ROOT}/INDEX.md"
CHECK_MODE=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --check) CHECK_MODE=1; shift ;;
    --output) OUTPUT="$2"; shift 2 ;;
    -h|--help)
      sed -n '2,20p' "$0"
      exit 0
      ;;
    *) echo "[erreur] argument inconnu : $1" >&2; exit 2 ;;
  esac
done

if [[ ! -f "${PY_HELPER}" ]]; then
  echo "[erreur] helper Python introuvable : ${PY_HELPER}" >&2
  exit 2
fi
if ! command -v python3 >/dev/null 2>&1; then
  echo "[erreur] python3 requis (>= 3.9)" >&2
  exit 2
fi

GENERATED=$(python3 "${PY_HELPER}" --root "${ROOT}")

if [[ "${CHECK_MODE}" -eq 1 ]]; then
  if [[ ! -f "${OUTPUT}" ]]; then
    echo "[erreur] INDEX.md introuvable à ${OUTPUT} (mode --check)" >&2
    exit 1
  fi
  if ! diff -q <(echo "${GENERATED}") "${OUTPUT}" >/dev/null 2>&1; then
    echo "[generate-index] désynchronisation détectée — exécuter sans --check pour régénérer."
    exit 1
  fi
  echo "[generate-index] INDEX.md à jour."
  exit 0
fi

echo "${GENERATED}" > "${OUTPUT}"
echo "[generate-index] INDEX.md régénéré : ${OUTPUT}"
exit 0
