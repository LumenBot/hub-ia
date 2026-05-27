#!/usr/bin/env bash
# check-links.sh — vérification des liens internes morts (Markdown) du repo strategie-ia
#
# Auteur          : Cowork Hub IA Plateforme (Claude Code)
# Date            : 2026-05-27
# Owner           : 07-tech-et-architecture
# Confidentialité : public
# Statut          : validé
#
# Détecte :
#   - les liens Markdown relatifs `[texte](./chemin)` ou `[texte](../chemin)` pointant
#     vers un fichier inexistant
#   - les wikilinks Obsidian `[[cible]]` sans correspondance dans le repo
#
# Limites volontaires :
#   - les liens externes (https://...) ne sont PAS vérifiés (réseau, lent, faux positifs)
#   - les ancres (`#section`) ne sont pas résolues à la profondeur de la section
#     (on vérifie seulement que le fichier cible existe)
#
# Usage :
#   ./check-links.sh                 # audit complet du repo (CWD = racine)
#   ./check-links.sh --staged        # diff Git seulement (CI/pre-commit)
#
# Exit codes : 0 OK | 1 lien mort détecté | 2 erreur d'exécution

set -euo pipefail

STAGED=0
[[ "${1:-}" == "--staged" ]] && STAGED=1

ROOT="$(pwd)"

# Liste des fichiers MD à scanner.
if [[ "${STAGED}" -eq 1 ]]; then
  if ! git rev-parse --git-dir >/dev/null 2>&1; then
    echo "[erreur] --staged hors d'un repo Git" >&2
    exit 2
  fi
  MD_FILES=$(git diff --name-only --diff-filter=ACMR HEAD -- '*.md' 2>/dev/null || true)
else
  MD_FILES=$(find . -name "*.md" -not -path "*/_archives/*" -not -path "*/.git/*" -not -path "*/node_modules/*" 2>/dev/null)
fi

if [[ -z "${MD_FILES}" ]]; then
  echo "[check-links] aucun fichier MD à scanner."
  exit 0
fi

ERRORS=0
TOTAL_LINKS=0

# Construction de l'index des chemins existants (insensible à la casse pour wikilinks).
declare -A EXISTING_PATHS
declare -A EXISTING_BASENAMES
while IFS= read -r f; do
  rel="${f#./}"
  EXISTING_PATHS["${rel}"]=1
  base=$(basename "${rel}" .md)
  EXISTING_BASENAMES["${base,,}"]="${rel}"
done < <(find . -type f -not -path "*/.git/*" -not -path "*/node_modules/*" 2>/dev/null)

check_relative_link() {
  local source_file="$1"
  local target="$2"
  local source_dir
  source_dir=$(dirname "${source_file}")
  # Strip ancre (#section) et query (?param).
  local clean_target="${target%%#*}"
  clean_target="${clean_target%%\?*}"
  [[ -z "${clean_target}" ]] && return 0  # ancre interne pure
  # Résolution relative.
  local resolved
  resolved=$(cd "${source_dir}" 2>/dev/null && readlink -m "${clean_target}" 2>/dev/null || echo "")
  if [[ -z "${resolved}" ]]; then
    return 0
  fi
  # Strip le prefix ROOT.
  resolved="${resolved#${ROOT}/}"
  resolved="${resolved#./}"
  if [[ -n "${EXISTING_PATHS[${resolved}]:-}" ]] || [[ -e "${ROOT}/${resolved}" ]]; then
    return 0
  fi
  echo "  ✗ lien mort : [...](${target}) → cible inexistante (${resolved})"
  return 1
}

check_wikilink() {
  local source_file="$1"
  local target="$2"
  # Wikilinks toléreront `cible`, `cible#ancre`, `cible|alias`.
  local clean_target="${target%%#*}"
  clean_target="${clean_target%%|*}"
  clean_target=$(echo "${clean_target}" | tr -d '[:space:]')
  [[ -z "${clean_target}" ]] && return 0
  local target_lower="${clean_target,,}"
  if [[ -n "${EXISTING_BASENAMES[${target_lower}]:-}" ]]; then
    return 0
  fi
  echo "  ✗ wikilink mort : [[${target}]] → aucun fichier MD correspondant"
  return 1
}

for source_file in ${MD_FILES}; do
  [[ ! -f "${source_file}" ]] && continue

  file_errors=0
  # Liens Markdown relatifs : [texte](./xxx) ou [texte](../xxx).
  while IFS= read -r match; do
    [[ -z "${match}" ]] && continue
    TOTAL_LINKS=$((TOTAL_LINKS + 1))
    target=$(echo "${match}" | sed -E 's/.*\]\((\.[^\)]+)\).*/\1/')
    if ! check_relative_link "${source_file}" "${target}"; then
      file_errors=$((file_errors + 1))
    fi
  done < <(grep -oE '\]\(\.\.?\/[^)]+\)' "${source_file}" 2>/dev/null || true)

  # Wikilinks Obsidian : [[cible]] (limité au pattern simple).
  while IFS= read -r match; do
    [[ -z "${match}" ]] && continue
    TOTAL_LINKS=$((TOTAL_LINKS + 1))
    target=$(echo "${match}" | sed -E 's/\[\[([^]]+)\]\]/\1/')
    if ! check_wikilink "${source_file}" "${target}"; then
      file_errors=$((file_errors + 1))
    fi
  done < <(grep -oE '\[\[[^]]+\]\]' "${source_file}" 2>/dev/null || true)

  if [[ "${file_errors}" -gt 0 ]]; then
    echo "${source_file} — ${file_errors} lien(s) mort(s)"
    ERRORS=$((ERRORS + file_errors))
  fi
done

echo "---"
echo "[check-links] ${TOTAL_LINKS} liens internes scannés, ${ERRORS} mort(s)."

if [[ "${ERRORS}" -gt 0 ]]; then
  exit 1
fi
exit 0
