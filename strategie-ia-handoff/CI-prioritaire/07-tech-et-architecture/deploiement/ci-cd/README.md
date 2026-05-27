# `07-tech-et-architecture/deploiement/ci-cd/` — CI conformité

**Version** : v1.0
**Date de création** : 2026-05-27
**Dernière mise à jour** : 2026-05-27
**Statut** : validé
**Auteur principal** : Cowork Hub IA Plateforme (Claude Code)
**Owner fonctionnel** : 07-tech-et-architecture
**Confidentialité** : public
**Tags** : ci, github-actions, audit, conformité, qualité

---

## 1. Synthèse exécutive

Ce dossier contient la CI conformité du repo `strategie-ia` (priorité critique
J+3 à J+7 — cf. CdC Claude Code étape 2 §3.1). Quatre productions :

- `scripts/audit-conformity.sh` — point d'entrée bash, délègue au helper Python `audit_conformity.py`
- `scripts/check-links.sh` — vérification des liens internes morts (Markdown relatifs + wikilinks Obsidian)
- `scripts/generate-index.sh` — régénération automatique de `INDEX.md` à partir des en-têtes MD (helper Python `_generate_index_helper.py`)
- `.github/workflows/audit-conformity.yml` — workflow GitHub Actions qui orchestre les 3 scripts à chaque PR

Objectif : décharger Hub Strat de la dette de relecture conventions/liens/index
en automatisant les contrôles mécaniques. Sans cette CI, le rôle reviewer transverse
Hub Strat devient un goulot dès la vague A.

## 2. Contexte

Issue du **challenge étape 1 Claude Code** (§4 frictions anticipées : *« CI absente
au démarrage = goulot Hub Strat manuel »*) et de la **décision Cavalli §3.1 CdC v1.1**
(*« CI conformité prioritaire J+3 à J+7, en parallèle des contributions étape 3 »*).

Stack technique :
- **Bash** pour les points d'entrée (kebab-case `.sh`, §1 CONVENTIONS)
- **Python 3.11** pour le parsing robuste YAML/Markdown (snake_case `_*.py`, §11)
- **GitHub Actions** pour l'orchestration CI (déclenché à chaque PR)

Aucune dépendance Python externe — uniquement la stdlib (re, pathlib, subprocess,
argparse, unicodedata, dataclasses). Pas de `requirements.txt` à maintenir.

## 3. Conventions vérifiées

| Règle | Référence | Sévérité |
|-------|-----------|----------|
| Naming kebab-case (.md) | §1 CONVENTIONS | erreur |
| Naming snake_case (.py) | §11 CONVENTIONS | erreur |
| Pas d'accents / espaces / caractères spéciaux | §1 | erreur |
| En-tête métadonnées obligatoires (Version, Statut, Confidentialité) | §2 | erreur |
| En-tête métadonnées recommandées (Date, Auteur, Owner, Tags) | §2 | warning |
| Footer Historique présent | §2 | warning |
| Format dates ISO 8601 | §6 | erreur |
| Confidentialité valeur reconnue (public/interne/restreint) | §9 | erreur |
| Statut valeur reconnue (draft/revue-en-cours/validé/archivé) | §2 + v1.1 | warning |
| Docstring PEP 257 obligatoire (.py) | §11 | erreur |
| Métadonnées docstring (Auteur, Date, Owner, Confidentialité, Statut) | §11 | warning |
| Numérotation ADR `ADR-NNN-titre-court.md` | §12 | erreur |
| Statut ADR ∈ {proposed, accepted, deprecated, superseded} | §12 | erreur |
| Liens internes morts (Markdown relatifs + wikilinks) | — | erreur |
| Pas de marqueurs `<<<<<<<` non résolus | hub-ia SPEC v2.0 (importé) | erreur |
| INDEX.md à jour vs contenu réel du repo | — | erreur |

**Politique de blocage** : PR bloquée si **au moins 1 erreur**. Warnings autorisés
(régime R3 fast-track mineur — cf. `CONTRIBUTING.md` §2). Le flag `--strict`
permet de bloquer aussi sur warnings (usage local, pas CI).

## 4. Usage local (avant push)

Pour valider une contribution avant d'ouvrir la PR :

```bash
# Audit complet du repo
./07-tech-et-architecture/deploiement/ci-cd/scripts/audit-conformity.sh

# Audit du diff seulement (équivalent CI)
./07-tech-et-architecture/deploiement/ci-cd/scripts/audit-conformity.sh --staged

# Audit strict (échoue sur les warnings aussi)
./07-tech-et-architecture/deploiement/ci-cd/scripts/audit-conformity.sh --strict

# Vérification des liens
./07-tech-et-architecture/deploiement/ci-cd/scripts/check-links.sh

# Régénération de l'INDEX
./07-tech-et-architecture/deploiement/ci-cd/scripts/generate-index.sh

# Vérification que l'INDEX est à jour (sans le régénérer)
./07-tech-et-architecture/deploiement/ci-cd/scripts/generate-index.sh --check
```

**Pre-commit hook recommandé** (à installer manuellement par chaque contributeur) :

```bash
# .git/hooks/pre-commit
#!/usr/bin/env bash
./07-tech-et-architecture/deploiement/ci-cd/scripts/audit-conformity.sh --staged --strict || exit 1
```

## 5. Politique CI dans `audit-conformity.yml`

| Job | Déclenchement | Bloque merge ? |
|-----|---------------|----------------|
| `audit-conformity` | PR + push main | ✅ oui |
| `check-links` | PR + push main | ✅ oui |
| `check-index` | PR + push main | ✅ oui |
| `check-merge-markers` | PR + push main | ✅ oui |

Tous les jobs s'exécutent en parallèle. Un job rouge bloque le merge **si la branch
protection est active sur `main`** (cf. `INSTRUCTIONS-CAVALLI.md`).

## 6. Régénération de l'INDEX.md

L'INDEX est régénéré automatiquement par `generate-index.sh` à partir des
en-têtes MD de chaque fichier du repo. Le workflow CI vérifie en mode `--check`
que l'INDEX committé est synchrone avec le contenu réel ; si pas, la PR est
bloquée et le contributeur doit régénérer l'INDEX et le committer.

Workflow recommandé en cas de désynchronisation :

```bash
cd <racine-strategie-ia>
./07-tech-et-architecture/deploiement/ci-cd/scripts/generate-index.sh
git add INDEX.md
git commit -m "chore(07-tech): regenerate INDEX.md after content changes"
git push
```

## 7. Évolutions à prévoir (v1.1+)

- **`audit-conformity.sh --fix`** : auto-correction des cas simples (en-tête manquant
  → ajout via template, date manquante → date du jour). Effort estimé : ~3-4 h.
- **`check-links.sh` étendu** aux ancres `#section` (résolution réelle de la section
  dans le fichier cible). Effort : ~2 h.
- **Bot commentaire PR** : annoter les lignes problématiques directement dans la PR
  GitHub (`reviewdog` ou action custom). Effort : ~3 h.
- **Audit Glossaire** : détection des termes 🔴 bannis en façade externe dans les
  documents `confidentialité: public`. Effort : ~4 h (parsing glossaire + matching
  contextualisé).

## 8. Coordination

- **Hub RAG** (régime R2 fast-track tech sur 07/09) : peut consulter et proposer des
  PR sur ces scripts. La logique audit est volontairement isomorphe à `audit-md-rag.py`
  côté `hub-ia/rag/code/audit/` pour préserver le pattern dual repo pendant la transition.
- **Hub Strat** (reviewer transverse) : approuve les évolutions structurelles
  (ajout de règles, modification de la sévérité, exclusions nouvelles).
- **Cavalli** (owner décisionnel) : arbitre les ajustements de politique de blocage
  (durcissement/assouplissement de la branch protection).

## 9. Sources et références

- `CONVENTIONS.md` v1.1 §§1, 2, 6, 9, 11, 12 (règles vérifiées)
- `CONTRIBUTING.md` v1.1 §2 (régimes R1/R2/R3) + §4.bis (seuil d'alerte goulot Hub Strat)
- `FRONTIERES.md` v1.0 §2.1 (frontière 07↔09 — code audit transverse en 07)
- `CdC-claude-code.md` (étape 2) §3.1 (CI conformité prioritaire)
- `hub-ia/rag/code/audit/audit-md-rag.py` (pattern et style importés depuis hub-ia)

---

## Historique

| Date | Version | Modification |
|------|---------|--------------|
| 2026-05-27 | v1.0 | Création initiale — CI conformité prioritaire J+3 à J+7. 4 productions : audit-conformity, check-links, generate-index, workflow YAML. Style et patterns importés depuis `hub-ia/rag/code/audit/`. |

---

*CI conformité repo `strategie-ia` — Cowork Hub IA Plateforme (Claude Code), 27 mai 2026.*
