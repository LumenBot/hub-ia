---
id: ADR-003
statut: proposed
date_proposition: 2026-05-29
date_acceptation: ~
deciders: Cavalli, Hub Strat, Hub Content
consulted: Claude Code RAG, Hub RAG
informed: Claude Code Content
tags: [frontmatter, yaml, spec-r1, vault, ingestion, retrospectif]
supersedes: ~
superseded_by: ~
---

# ADR-003 — Frontmatter YAML 10 champs canoniques pour le vault RAG (rétrospectif)

**Version** : v0.1 (draft skeleton — à finaliser PR 6 Vague B prévue J+15)
**Date de création** : 2026-05-29
**Dernière mise à jour** : 2026-05-29
**Statut** : draft (proposed — rétrospectif, décision effective depuis S1)
**Auteur principal** : Cowork Hub IA Plateforme (Claude Code RAG)
**Owner fonctionnel** : 09-rag-et-ia/adr
**Confidentialité** : public
**Tags** : adr, frontmatter, yaml, spec, vault, retrospective

---

## Context

ADR rétrospectif. La décision est **effective depuis S1** (sprint pilote, mai 2026) et codifiée dans `SPEC-MD-POUR-RAG.md` §R1 (déjà migrée en `07-tech-et-architecture/spec-md-rag/spec-md-pour-rag-v2-3.md`). Cet ADR formalise la décision dans le format Michael Nygard pour traçabilité.

Le vault RAG `strategie-ia/08-contenu-editorial/hub-ia-learning-center/` ingéré par le pipeline RAG nécessite des métadonnées structurées pour :
- Routing du chunking (type de fichier détermine la stratégie H2 vs H3)
- Filtrage retrieval (axe, niveau, public_cible)
- Validation R1 par l'audit `audit_md_rag.py` (cf. `07-tech-et-architecture/qualite-et-tests/`)
- Cohérence inter-fichiers (wikilinks, derives, glosaire_termes)

## Decision

Tout fichier MD ingéré par le pipeline RAG (catégorie `08-contenu-editorial/hub-ia-learning-center/`) doit comporter un frontmatter YAML avec exactement **10 champs canoniques** :

| # | Champ | Type | Valeurs | Obligatoire |
|---|-------|------|---------|-------------|
| 1 | `code` | string | identifiant unique kebab-case (ex. `cu-008`, `outils-llm`) | oui |
| 2 | `titre` | string | titre éditorial (correspond au H1 unique du document) | oui |
| 3 | `type` | enum | `module-cu` / `prealable-pr` / `deploiement-dep` / `architecture` / `fiche-outil` / `transverse` | oui |
| 4 | `axe` | enum | `A` / `B` / `C` / `D` / `E` / `agentique` / `transverse` | oui |
| 5 | `niveau` | int | 1 / 2 / 3 / 4 | oui |
| 6 | `tags` | list[string] | mots-clés thématiques | oui |
| 7 | `version` | string | semver (`3.12.0`) | oui |
| 8 | `last_updated` | date | ISO 8601 (`2026-05-29`) | oui |
| 9 | `glosaire_termes` | list[string] | termes du glossaire utilisés | oui (D-028 exception racines) |
| 10 | `derives` | list[string] | wikilinks vers documents dérivés | oui (D-028 exception racines) |
| 11 | `public_cible` | list[enum] | `dirigeant` / `ops` / `r&d` / `tech` / `transverse` | oui |

**Exception D-028** : pour les fichiers racines transverses (`glossaire.md`, `chiffres-macro-*.md`), les champs `glosaire_termes` et `derives` peuvent être vides par construction.

## Status

`proposed` (rétrospectif) — codifié SPEC v1.0+ depuis S1, formalisé en ADR ici pour traçabilité pré-shutdown. Devient `accepted` au merge PR 6 Vague B.

## Consequences

### Positives

- Vault audité de manière déterministe par R1 (`audit_md_rag.py` — 121/121 tests sur hub-ia)
- Chunking déterministe par type (H2 autonome pour module-cu, H3 pour transverse, etc.)
- Filtrage retrieval par métadonnée (axe, niveau, public_cible) possible si activé en post-Étape 2
- Cohérence inter-fichiers vérifiable (wikilinks, derives)

### Négatives / risques

- Discipline éditoriale stricte requise — toute production éditoriale doit respecter le frontmatter
- Évolution des champs canoniques nécessite migration de TOUT le vault (eviter)
- Pas de versioning du schéma frontmatter lui-même (v1, v2) — à inscrire en SPEC v2.4+ si évolution

### À mesurer post-mise en production

- Taux de conformité R1 sur vault production (cible 100 %)
- Fréquence des wikilinks cassés détectés par l'audit (en baisse — cf. SPEC v2.3 codification R11 wikilinks outils)

## Liens

- SPEC source : `07-tech-et-architecture/spec-md-rag/spec-md-pour-rag-v2-3.md` §R1 « Frontmatter complet »
- Audit R1 : `07-tech-et-architecture/qualite-et-tests/audit_md_rag.py` `check_r1_frontmatter`
- Tests R1 : `07-tech-et-architecture/qualite-et-tests/tests/test_audit_md_rag.py` `TestR1Frontmatter`
- ADR connexe : ADR-???? Vault content `08/hub-ia-learning-center/` (production éditoriale Hub Content)

---

## Historique

| Date | Version | Modification |
|------|---------|--------------|
| 2026-05-29 | v0.1 | Création draft skeleton pré-shutdown — ADR rétrospectif (décision effective depuis S1, codifiée SPEC v1.0+). Formalisation Michael Nygard pour traçabilité. À finaliser PR 6 Vague B (cible J+15). |

---

*ADR-003 `09-rag-et-ia/adr/` — Cowork Hub IA Plateforme (Claude Code RAG), 29 mai 2026. Draft skeleton pré-shutdown rétrospectif. Format Michael Nygard CONVENTIONS v1.1 §12.1.*
