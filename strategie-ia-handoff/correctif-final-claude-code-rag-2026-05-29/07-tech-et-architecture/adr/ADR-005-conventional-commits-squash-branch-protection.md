---
id: ADR-005
statut: proposed
date_proposition: 2026-05-29
date_acceptation: ~
deciders: Hub Strat, Cavalli
consulted: Claude Code RAG, Claude Code Content, Hub RAG, DEV IA Head
informed: Claude Design, Hub Content
tags: [git, conventional-commits, squash-merge, branch-protection, ci, repo-discipline]
supersedes: ~
superseded_by: ~
---

# ADR-005 — Conventional Commits + squash-and-merge sur `main` + branch protection

**Version** : v0.1 (draft skeleton — à finaliser PR 6 Vague B prévue J+15)
**Date de création** : 2026-05-29
**Dernière mise à jour** : 2026-05-29
**Statut** : draft (proposed — partiellement effectif Vague A)
**Auteur principal** : Cowork Hub IA Plateforme (Claude Code RAG)
**Owner fonctionnel** : 07-tech-et-architecture/adr
**Confidentialité** : public
**Tags** : adr, git, commits, merge-strategy, branch-protection, ci, discipline

---

## Context

Le repo `LumenBot/strategie-ia` est alimenté par 6 agents IA pairs + Cavalli, avec 5 régimes de PR différenciés (R1 standard / R2 fast-track tech / R3 fast-track mineur / R4 hors PR / R5 exploratoires — cf. `CONTRIBUTING.md` v1.1 §2).

Sans discipline Git stricte, le risque est élevé :
- Historique illisible (commits descriptifs hétérogènes par agent)
- Marqueurs de conflit `<<<<<<<` non résolus committés par mégarde (cas-école hub-ia SPEC v2.0 §Hygiène merge, 3 occurrences PR #84/#86/#88)
- Merges directs sur `main` sans review (perte de traçabilité)
- Branches obsolètes accumulées

La Vague A `audit-conformity.yml` (cf. `.github/workflows/`) instrumente déjà 4 jobs CI bloquants. Cet ADR formalise les disciplines complémentaires côté Git workflow.

## Decision

**1. Conventional Commits format obligatoire**

Tous les commits suivent le format `type(scope): description courte`, où :

- **types autorisés** : `feat` / `fix` / `docs` / `style` / `refactor` / `test` / `chore` / `perf` / `ci`
- **scope** : catégorie repo (`01-strategie`, `02-finance`, ..., `13-veille`, ou transverses `handoff`, `ci`, `gov`)
- **description** : impératif présent, ≤ 72 caractères, pas de point final

Exemples :
- `feat(09-rag): BM25 hybrid RRF retrieval (S2.9 décision)`
- `fix(07-tech): audit-conformity exclut _handoffs/ matière éphémère`
- `docs(11-gouvernance): ADR-001 LLM Haiku baseline acté`
- `chore(handoff): coordination append-only v1.2 (+3 entries RAG)`

**2. Squash-and-merge obligatoire sur `main`**

- Toute PR mergée sur `main` produit **1 seul commit** (squash de tous les commits intermédiaires)
- Le message de commit final est dérivé du titre de la PR (lui-même au format Conventional Commits)
- Pas de merge commit, pas de rebase-and-merge — cohérent avec linear history requise par branch protection

**3. Branch protection sur `main`**

Règles activées (cf. `instructions-cavalli.md` du bundle Vague A) :
- ☑ Require pull request before merging (1 approve minimum)
- ☑ Require status checks to pass (4 jobs CI : audit-conformity / check-links / check-index / check-merge-markers)
- ☑ Require branches to be up to date before merging
- ☑ Require conversation resolution
- ☑ Require linear history
- ☑ Do not allow bypassing settings (incluant admins)
- ☑ Restrict pushes (Cavalli + Hub Strat uniquement, pour cas exceptionnels)

**Durcissement Étape 2 MVP** : 2 approves requis pour catégories sensibles (`04-juridique/`, `02-finance/`, `_internal/`) via CODEOWNERS multi-reviewer ou règle dédiée par path.

**4. Hygiène merge automatisée**

Job CI `check-merge-markers` bloque toute PR contenant des marqueurs `<<<<<<<` / `=======` / `>>>>>>>` non résolus dans le code source (exclusion `_archives/` pour éviter faux positifs sur historique).

Discipline héritée hub-ia SPEC v2.0 § Hygiène merge — `git grep "<<<<<<<"` vide avant `git add`, désormais automatisée côté CI.

## Status

`proposed` — partiellement effectif depuis Vague A (CI active, branch protection à activer par Cavalli côté GitHub Settings cf. `instructions-cavalli.md`). Devient `accepted` au merge PR 6 Vague B + confirmation branch protection active.

## Consequences

### Positives

- Historique `main` lisible (1 commit par PR, format normé) → changelog automatisable
- Traçabilité décisionnelle (Conventional Commits + ADR cross-references)
- Hygiène merge automatique (pas d'occurrence `<<<<<<<` possible)
- Branch protection bloque merges accidentels et permet la délégation reviewer croisé R2 sans risque
- Linear history compatible avec outils de blame, bisect, revert

### Négatives / risques

- Discipline Conventional Commits = courbe d'apprentissage pour les agents non habitués (mitigé par template + CI hint éventuel)
- Squash-and-merge perd l'historique fin des commits intermédiaires (compensé par description PR détaillée)
- Branch protection 1 approve peut créer un goulot reviewer si Hub Strat indisponible (mitigé par M2 délégation reviewer croisé tech CONTRIBUTING.md §4.bis + M3 backup Cavalli/DEV IA Head)
- Durcissement 2 approves Étape 2 MVP nécessite anticipation côté CODEOWNERS

### À mesurer post-mise en production

- Taux de conformité Conventional Commits à 30/60/90 jours
- Temps moyen review-to-merge par régime PR (R1/R2/R3)
- Nombre de PR bloquées par `check-merge-markers` (devrait tomber à 0 rapidement)

## Liens

- CI Vague A : `.github/workflows/audit-conformity.yml`
- Instructions activation Cavalli : `_handoffs/claude-code-rag-vers-hub-strat/instructions-cavalli-vague-a.md`
- CONTRIBUTING.md v1.1 §2 (régimes R1/R2/R3/R4/R5) + §4.bis (seuil d'alerte goulot)
- CONVENTIONS.md v1.1 §11 (Conventional Commits codifié)
- Discipline source : hub-ia SPEC v2.0 § Hygiène merge (héritée RAPPORT-CC-S2.5 §6 proposition 1)

---

## Historique

| Date | Version | Modification |
|------|---------|--------------|
| 2026-05-29 | v0.1 | Création draft skeleton pré-shutdown — à finaliser PR 6 Vague B (cible J+15 = 2026-06-18). Codifie la décision déjà partiellement effective Vague A (CI 4 jobs actifs, branch protection à activer Cavalli). Sourcing CONVENTIONS v1.1 §11 + CONTRIBUTING v1.1 §2. |

---

*ADR-005 `07-tech-et-architecture/adr/` — Cowork Hub IA Plateforme (Claude Code RAG), 29 mai 2026. Draft skeleton pré-shutdown. Format Michael Nygard CONVENTIONS v1.1 §12.1.*
