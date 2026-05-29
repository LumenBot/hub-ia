---
id: ADR-001
statut: proposed
date_proposition: 2026-05-29
date_acceptation: ~
deciders: Cavalli, Hub Strat, Hub RAG
consulted: Claude Code RAG
informed: Claude Code Content
tags: [llm, model-routing, cost-optimization, souverainete-eu]
supersedes: ~
superseded_by: ~
---

# ADR-001 — LLM par défaut : Haiku 4.5 baseline + Sonnet 4.6 routing premium + Mistral Cloud EU en réserve souveraine

**Version** : v0.1 (draft skeleton — à finaliser PR 6 Vague B prévue J+15)
**Date de création** : 2026-05-29
**Dernière mise à jour** : 2026-05-29
**Statut** : draft (proposed)
**Auteur principal** : Cowork Hub IA Plateforme (Claude Code RAG)
**Owner fonctionnel** : 09-rag-et-ia/adr
**Confidentialité** : public
**Tags** : adr, llm, haiku, sonnet, mistral, cost, latency, sprint-s2-9

---

## Context

Le sprint S2.9 (cf. `09-rag-et-ia/evaluations/rapport-cc-s2-9.md` §5 décision #2) a benchmarké empiriquement 5 variantes d'optimisation sur sous-set 20q stratifié (6 std stress + 14 adversariales).

Le bench-5 (Haiku 4.5 sur l'étape génération uniquement, retrieval inchangé) a livré :
- **Qualité préservée** : 19/20 identique baseline Sonnet 4.6
- **Latence** : p50 5 s (−58 % vs baseline 12 s), p90 8 s (−60 % vs 20 s)
- **Coût** : 0,0953 $ pour 20q (−76 % vs baseline 0,4053 $) — soit ~0,005 $/q

Aucune dégradation observable sur ce panel (qui inclut le bloc adversarial 14/14).

Côté souveraineté EU, Mistral La Plateforme Enterprise reste disponible comme fournisseur LLM souverain de référence, à activer en routing ad-hoc selon le profil utilisateur (cas RGPD complexe, AI Act juridique, données sensibles classified entreprise).

## Decision

**Modèle de génération par défaut** : `claude-haiku-4-5-20251001` (Haiku 4.5).

**Routing ad-hoc Sonnet 4.6** (`claude-sonnet-4-6`) déclenché si :
- Requête tagguée `juridique` (RGPD, AI Act, conformité)
- Requête tagguée `audit-securite` (audit applicatif, supply chain)
- Requête tagguée `pedagogique-long` (génération module éditorial > 1500 mots)
- Fallback automatique si Haiku retourne un score adversarial < seuil (à instrumenter post-Étape 2)

**Mistral La Plateforme Enterprise** en réserve souveraine activable par configuration tenant (organisation cliente avec exigence stricte hébergement EU + Zero Data Retention). Pas le défaut, mais slot natif dans le router.

## Status

`proposed` — en attente d'arbitrage Cavalli (validation post-IP statut side project + cohérence routing premium avec promesse commerciale Pro tier 29 €/mois) avant passage `accepted`.

## Consequences

### Positives

- Pivot économique majeur : pour le même budget Anthropic mensuel (cap D-013 50 $/mois), ×4 plus d'évaluations possibles OU ×3-4 plus de production de contenu
- Latence p50 ramenée à ~5 s — quasi-temps réel pour l'expérience utilisateur conversationnelle Pro tier
- Cohérence avec la promesse souveraineté EU (Mistral en réserve activable)
- Routing ad-hoc préserve la qualité sur les cas à risque sans surcoût systémique

### Négatives / risques

- Tests adversariaux validés sur **sous-set 20q** uniquement — extension recommandée à 50-100q post-Étape 2 pour confirmer robustesse statistique
- Routing rules à maintenir dans `09/pipeline-ingestion/query.py` ou couche dédiée (effort ~2-3h Plateforme Vague B suite ou S2.10)
- Sonnet 4.6 reste payé pour ~10-15 % du trafic estimé → coût marginal non nul mais maîtrisé
- Mistral La Plateforme Enterprise nécessite configuration tenant et test d'intégration avant production (Étape 2 MVP)

### À mesurer post-mise en production

- Taux de fallback automatique Haiku → Sonnet (cible < 5 %)
- Latence p99 (au-delà du p90 mesuré sur sous-set)
- Coût mensuel réel vs projection ~0,12 $/utilisateur Pro/mois

## Liens

- Source empirique : `09-rag-et-ia/evaluations/rapport-cc-s2-9.md` §3.1 tableau comparatif + §5 décision #2
- Bench détaillé : `09-rag-et-ia/evaluations/eval-report-s2-9-comparatif.md`
- Code bench : `09-rag-et-ia/pipeline-ingestion/bench_runner.py`
- ADR connexe : [ADR-002 BM25 hybrid RRF retrieval](./ADR-002-bm25-hybrid-rrf-retrieval.md) (autre optimisation S2.9 adoptée)
- ADR connexe : [ADR-004 Stack US Variante A MVP](../../07-tech-et-architecture/adr/ADR-004-stack-variante-a-mvp.md) (Vercel + Supabase + Anthropic)

---

## Historique

| Date | Version | Modification |
|------|---------|--------------|
| 2026-05-29 | v0.1 | Création draft skeleton pré-shutdown — à finaliser PR 6 Vague B (cible J+15 = 2026-06-18). Sourcing empirique RAPPORT-CC-S2.9 §5. Co-relecture Hub RAG par construction + arbitrage Cavalli. |

---

*ADR-001 `09-rag-et-ia/adr/` — Cowork Hub IA Plateforme (Claude Code RAG), 29 mai 2026. Draft skeleton pré-shutdown. Format Michael Nygard CONVENTIONS v1.1 §12.1.*
