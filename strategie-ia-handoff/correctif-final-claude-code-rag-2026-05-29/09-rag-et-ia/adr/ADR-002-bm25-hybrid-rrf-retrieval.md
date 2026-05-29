---
id: ADR-002
statut: proposed
date_proposition: 2026-05-29
date_acceptation: ~
deciders: Cavalli, Hub Strat, Hub RAG
consulted: Claude Code RAG
informed: Claude Code Content
tags: [retrieval, bm25, hybrid, rrf, ap-8, sprint-s2-8, sprint-s2-9]
supersedes: ~
superseded_by: ~
---

# ADR-002 — BM25 + dense hybrid (RRF) en retrieval production

**Version** : v0.1 (draft skeleton — à finaliser PR 6 Vague B prévue J+15)
**Date de création** : 2026-05-29
**Dernière mise à jour** : 2026-05-29
**Statut** : draft (proposed)
**Auteur principal** : Cowork Hub IA Plateforme (Claude Code RAG)
**Owner fonctionnel** : 09-rag-et-ia/adr
**Confidentialité** : public
**Tags** : adr, retrieval, bm25, hybrid, rrf, anti-pattern, ap-8

---

## Context

Le sprint S2.8 (cf. `09-rag-et-ia/evaluations/rapport-cc-s2-8.md` §4 + §5 Finding 4) a identifié le pattern **AP-8 « cluster de fiches sœurs »** : quand plusieurs fiches partagent une même structure H2 (ex. les 5 architectures vague 8 avec leur section H2 « Coût indicatif »), la similarité sémantique cosine sature le top-5 sur les questions transverses au cluster — au détriment des fiches cibles légitimes.

Cas-école empirique : q-083 « Tarif API Claude Sonnet/Opus » échoue sur baseline car `outils-llm` ressort rang #6 (sim -0,067), étouffé par les 5 chunks « Coût indicatif » des architectures A1-A4-Hybride + `chiffres-macro-2026`.

Le sprint S2.9 a benchmarké le pattern hybrid BM25 + dense avec fusion RRF (Reciprocal Rank Fusion, k=60) en bench-4 :
- **Score 20/20** — seul bench parmi 5 qui résout q-083 (cf. `09-rag-et-ia/evaluations/eval-report-s2-9-comparatif.md` §3.2)
- **Coût** : ~0 % vs baseline (+1,8 %, 0,4124 $ vs 0,4053 $)
- **Latence** : p90 +10 % (acceptable, compensé par adoption Haiku 4.5 cf. ADR-001)
- **Implémentation** : `09-rag-et-ia/pipeline-ingestion/bench_runner_hybrid.py` (rank_bm25 librairie Python pure, ~150 lignes ajoutées)

## Decision

**Activer BM25 + dense hybrid (RRF k=60) en retrieval production** sur le pipeline RAG `strategie-ia.pro`.

Le signal lexical BM25 fait émerger les chunks contenant des **termes exacts** (acronymes, noms propres, prix unitaires, références numériques) que le dense embedding seul ne ranke pas assez haut quand un cluster sémantique concurrent sature le voisinage cosine.

**Configuration de référence** :
- Index BM25 : construit en parallèle de l'index dense ChromaDB, sur le même corpus de chunks
- Fusion : RRF avec `k=60` (paramètre standard, équilibre lexical/sémantique)
- Top-k retrieval : maintenu à 5 (pas de réduction à 3 — voir ADR-???? skipped)
- Pas de reranking post-fusion en MVP (bench-1 reranking reporté S2.10+ — cf. RAPPORT-CC-S2.9 §5 décision #5)

## Status

`proposed` — en attente de Lot Dev S2.10 Plateforme pour porter `bench_runner_hybrid.py` en module production `09-rag-et-ia/pipeline-ingestion/hybrid_retrieval.py` (ou wrapping `query.py`). Effort estimé 2-3h dev + tests.

## Consequences

### Positives

- **AP-8 résolu sans coût éditorial** : le pattern « cluster de fiches sœurs » n'oblige plus à différencier mécaniquement les leads des sections récurrentes (cf. proposition mitigation préventive SPEC v2.3 AP-8). La fusion lexicale + sémantique compense au niveau retrieval.
- Robustesse accrue sur les questions à terminologie précise (prix, sigles, noms propres) — typiquement les requêtes commerciales/juridiques du Pro tier
- Coût et latence quasi-neutres vs baseline

### Négatives / risques

- Maintenance de deux index (BM25 + dense) sur tous les changements de corpus — discipline d'ingestion à respecter
- Pondération RRF k=60 fixée empiriquement S2.9 — pourrait nécessiter ajustement post-Étape 2 sur trafic réel
- Pas de mécanisme de fallback explicite si BM25 défaillit (par ex. corpus monolingue inadapté à un terme étranger)
- Empêche temporairement l'adoption de `text-embedding-3-large` (skipped S2.9 bench-3 régression adv) — décision orthogonale à revisiter S2.10+

### À mesurer post-mise en production

- Distribution des sources contribuées par BM25 vs dense seul (pourcentage de questions où BM25 fait la différence)
- Latence retrieval p50/p90 sur trafic réel (vs ~11 s p50 mesuré sub-set 20q)
- Évolution de l'AP-8 sur les vagues 9+ (modules CU restants) — si la mitigation tient toujours

## Liens

- Cas-école : `09-rag-et-ia/evaluations/rapport-cc-s2-8.md` §4 (identification AP-8 q-083) + `09-rag-et-ia/evaluations/rapport-cc-s2-9.md` §3.2 (validation empirique)
- Code bench : `09-rag-et-ia/pipeline-ingestion/bench_runner_hybrid.py`
- Spec AP-8 : `07-tech-et-architecture/spec-md-rag/spec-md-pour-rag-v2-3.md` §Anti-patterns AP-8 (proposition S2.8 §6 + amendement curatif S2.9 §6)
- ADR connexe : [ADR-001 LLM Haiku baseline](./ADR-001-llm-haiku-baseline-sonnet-routing.md) (autre optimisation S2.9 adoptée)

---

## Historique

| Date | Version | Modification |
|------|---------|--------------|
| 2026-05-29 | v0.1 | Création draft skeleton pré-shutdown — à finaliser PR 6 Vague B (cible J+15 = 2026-06-18). Sourcing empirique RAPPORT-CC-S2.8 §5 Finding 4 + RAPPORT-CC-S2.9 §3.2 + §5 décision #1. Co-relecture Hub RAG par construction. |

---

*ADR-002 `09-rag-et-ia/adr/` — Cowork Hub IA Plateforme (Claude Code RAG), 29 mai 2026. Draft skeleton pré-shutdown. Format Michael Nygard CONVENTIONS v1.1 §12.1.*
