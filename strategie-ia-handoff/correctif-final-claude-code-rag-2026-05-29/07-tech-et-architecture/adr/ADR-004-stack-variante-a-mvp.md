---
id: ADR-004
statut: proposed
date_proposition: 2026-05-29
date_acceptation: ~
deciders: Cavalli, Hub Strat
consulted: Claude Code RAG, Claude Code Content, Hub RAG
informed: Claude Design, DEV IA Head
tags: [stack, mvp, vercel, supabase, anthropic, souverainete, variante-a]
supersedes: ~
superseded_by: ~
---

# ADR-004 — Stack Variante A (Vercel + Supabase EU regions) en MVP, migration variante B post-Étape 4

**Version** : v0.1 (draft skeleton — à finaliser PR 6 Vague B prévue J+15)
**Date de création** : 2026-05-29
**Dernière mise à jour** : 2026-05-29
**Statut** : draft (proposed)
**Auteur principal** : Cowork Hub IA Plateforme (Claude Code RAG)
**Owner fonctionnel** : 07-tech-et-architecture/adr
**Confidentialité** : public
**Tags** : adr, stack, mvp, vercel, supabase, hosting, souverainete

---

## Context

L'ouverture du produit `strategie-ia.pro` (MVP commercialisable post-Étape 1 POC RAG juin 2026 → Étape 2 MVP fin 2026 / janv 2027) nécessite un choix de stack technique pivot.

Deux variantes envisagées par Cowork Hub Strat :
- **Variante A — Stack US (mainstream)** : Vercel (hosting front + edge functions) + Supabase EU regions (DB + auth + storage) + Anthropic (LLM principal Haiku 4.5 / Sonnet 4.6 — cf. ADR-001) + Stripe (paiement) + Plausible/Matomo EU (analytics souverains)
- **Variante B — Stack souveraine pure EU** : OVHcloud / Scaleway (hosting) + PostgreSQL self-hosted ou Outscale managed + Mistral La Plateforme Enterprise (LLM souverain) + Stancer ou Lemon Way (paiement EU) + Matomo on-premise

Arbitrage Cavalli (cf. RETEX synthèse §3.2 + décision IP statut side project) : adopter Variante A en MVP, migration vers Variante B reportée post-Étape 4 (post-monétisation Pro tier stabilisée, post-signature convention QFC, post-validation product-market fit).

## Decision

**Stack Variante A retenue en MVP commercialisable (Étape 2)** :

| Composant | Fournisseur | Plan | Justification |
|-----------|-------------|------|---------------|
| Hosting front | **Vercel** | Pro (~20 $/mois) | Deploy preview, edge functions, CDN global, GitHub native |
| Database + auth + storage | **Supabase** | Pro (~25 $/mois) avec EU regions (Frankfurt ou Paris) | Postgres managed, auth turnkey, RGPD-compliant via EU regions |
| LLM principal | **Anthropic Haiku 4.5 + Sonnet 4.6** (cf. ADR-001) | Pay-as-you-go | Pivot économique S2.9 validé |
| LLM réserve souveraine | **Mistral La Plateforme Enterprise** (cf. ADR-001) | À activer par tenant | Souveraineté EU + Zero Data Retention |
| Paiement | **Stripe** | Standard (2,9 % + 0,30 €) | Maturité produit, intégration native Supabase |
| Analytics | **Plausible** ou **Matomo Cloud** (EU) | ~10 $/mois | Souverain FR/EU, RGPD-friendly |
| Monitoring runtime | **Sentry** | Team (~26 $/mois) | Error tracking + web vitals |
| Observabilité LLM | **Langfuse** (cf. `09/observability/`) | Self-hosted ou cloud EU | Traces RAG, eval, prompts |

**Engagement migration Variante B** : à instruire post-Étape 4 (2027+) sur la base d'un nouvel ADR avec critères objectifs de bascule (volume utilisateurs, sensibilité données, exigences clients ETI, statut convention QFC).

## Status

`proposed` — en attente d'arbitrage Cavalli (validation post-IP statut side project + accord avec Hub Strat sur la promesse commerciale souveraineté du Pro tier).

## Consequences

### Positives

- Time-to-market accéléré (Vercel + Supabase = setup MVP en 1-2 jours vs 1-2 semaines stack souveraine pure)
- Coût fixe MVP maîtrisé (~80-100 $/mois infra + variable LLM/Stripe)
- Surface RGPD acceptable (EU regions Supabase + Anthropic Zero Data Retention contractuel)
- Routing souverain Mistral activable par tenant (réponse à exigences entreprise spécifiques)
- Skill mainstream (Vercel + Supabase + Stripe) — embauche future facilitée si recrutement Étape 4+

### Négatives / risques

- **Promesse commerciale souveraineté à nuancer** : la stack mainstream n'est pas « 100 % souveraine », il faut éviter la communication ambiguë (cf. GLOSSAIRE v1.1 § termes 🟢 commerciaux validés)
- Vendor lock-in modéré (Vercel + Supabase APIs proprios)
- Coût Stripe variable peut grimper sur croissance Pro tier (à monitorer)
- Migration Variante B post-Étape 4 = chantier non négligeable — provisionner budget et fenêtre dédiée
- Conformité AI Act et règlements EU à instruire au cas par cas (cf. ADR connexe juridique à venir)

### À mesurer post-mise en production

- TCO mensuel réel infra (vs projection ~100 $/mois MVP)
- Taux de tenants demandant le routing souverain Mistral (signal pour bascule Variante B)
- Latence p50/p90 Vercel edge → Anthropic API (côte est US) + retour
- Incidents et MTTR Sentry sur la première cohorte utilisateurs

## Liens

- ADR connexe : [ADR-001 LLM par défaut Haiku/Sonnet/Mistral](../../09-rag-et-ia/adr/ADR-001-llm-haiku-baseline-sonnet-routing.md)
- ADR connexe : [ADR-005 Conventional Commits + branch protection](./ADR-005-conventional-commits-squash-branch-protection.md)
- ADR connexe : [ADR-002 BM25 hybrid retrieval](../../09-rag-et-ia/adr/ADR-002-bm25-hybrid-rrf-retrieval.md)
- Décision source : RETEX Hub Strat synthèse §3.2 « statut `06/site-strategie-ia-pro/` : dossier de spec + référence externe (déploiement Vercel séparé en variante A stack US) »

---

## Historique

| Date | Version | Modification |
|------|---------|--------------|
| 2026-05-29 | v0.1 | Création draft skeleton pré-shutdown — à finaliser PR 6 Vague B (cible J+15 = 2026-06-18). Sourcing décision Cavalli §3.2 RETEX Hub Strat. Arbitrage Cavalli requis avant `accepted` (cohérence promesse commerciale souveraineté + post-IP statut side project). |

---

*ADR-004 `07-tech-et-architecture/adr/` — Cowork Hub IA Plateforme (Claude Code RAG), 29 mai 2026. Draft skeleton pré-shutdown. Format Michael Nygard CONVENTIONS v1.1 §12.1.*
