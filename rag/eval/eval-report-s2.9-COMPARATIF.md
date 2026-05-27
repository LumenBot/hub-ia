# S2.9 Lot I + Benchmarks — analyse comparative 5 evals

**Sous-set** : 20 questions = 6 standard stress/non-régression (q-030/q-036/q-056/q-083/q-073/q-076) + 14 adversariales (q-adv-001 à q-adv-014).

> ⚠️ Le sous-set est **constant** entre les 5 evals (comparaison apples-to-apples). Par construction (70 % adv, plus rapide), les p50/p90 ici **ne sont pas directement comparables** au full 118q ; ils mesurent l'impact relatif des variantes.

## Tableau comparatif

| Variante | Std/6 | Adv/14 | Total/20 | p50 (s) | p90 (s) | moy (s) | Coût gén ($) | Δ qualité vs baseline | Δ latence vs baseline | Δ coût vs baseline |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| baseline (Sonnet, k=5, embed -small) | 5 | 14 | **19/20** | 12,0 | 20,0 | 13,1 | 0,4053 | — | — | — |
| bench-2 top_k=3 | 4 | 14 | 18/20 | 10,0 | 17,0 | 11,0 | 0,3239 | **−1 std** | **−16 % p50** | **−20 %** |
| bench-3 embed -large | 5 | **12** | 17/20 | 11,0 | 20,0 | 13,1 | 0,3848 + 0,024 re-embed | **−2 adv** | ~0 | +5 % (+ surcoût ingest ×6,5) |
| **bench-4 BM25 + dense (RRF)** | **6** | 14 | **20/20 🎯** | 11,0 | 22,0 | 16,8 | 0,4124 | **+1 std (q-083 résolu)** | +28 % moy / +10 % p90 | ~0 |
| **bench-5 Haiku 4.5 (gen seulement)** | 5 | 14 | 19/20 | **5,0** | **8,0** | **5,2** | **0,0953** | 0 | **−58 % p50 / −60 % p90** | **−76 %** |

## Verdicts par bench

### Bench-1 — Reranking : NON EXÉCUTÉ ⏭️
Capacités requises absentes du venv (`cohere`, `voyageai`, `sentence_transformers`) et aucune clé API Cohere/Voyage. À reporter au S2.10 avec décision préalable (installer `sentence-transformers` lourd pour cross-encoder local, ou ajouter clé Cohere/Voyage pour API).

### Bench-2 — top_k 5 → 3 : ⚠️ trade-off mitigé
- Latence p50 12 → 10 s (−16 %), coût −20 %.
- **Régression qualité** : -1 std (3/6 → q-030 perd `pr-07`). q-083 inchangé (KO).
- **Recommandation** : ne pas adopter en prod sans patch éditorial. La réduction du contexte pénalise les questions transversales (multi-sources).

### Bench-3 — Embeddings text-embedding-3-large : ⚠️ régression
- Latence et qualité standard inchangées.
- **Régression adversarial** : 14 → 12 refus corrects (2 hallucinations introduites). q-083 toujours KO.
- Surcoût ingestion ×6,5 ($0,024 vs $0,0035 pour -small) sans gain mesuré.
- **Recommandation** : **pas adopter**. Le gain de dimension (1536 vs 1536, en fait 3072 vs 1536) n'apporte rien sur ce vault et dégrade la précision sémantique sur les questions adversariales (probable sur-spécification).

### Bench-4 — BM25 + dense hybrid (RRF) : ✅ **À ADOPTER POUR PROD**
- **Score parfait 20/20** — seul bench qui résout **q-083** (outils-llm cité).
- Coût ≈ baseline (+1,8 %), latence p90 +10 % (acceptable), moy +28 %.
- **Pattern saturation vague 8** (acronymes/pricing comme « tarif API Sonnet/Opus ») résolu par la fusion lexicale + sémantique.
- **Recommandation forte** : intégrer en production. Effort modéré (rank_bm25 léger pur Python, ~150 lignes de code, fusion RRF k=60 retient les chunks ayant un signal soit dense soit lexical).

### Bench-5 — Haiku 4.5 (génération seulement) : 🚀 **PIVOT ÉCONOMIQUE MAJEUR**
- **Qualité préservée** : 19/20 (identique à baseline). Aucune dégradation observable sur ce panel.
- **Latence p50 5 s (−58 %), p90 8 s (−60 %)** — quasi-temps réel.
- **Coût −76 %** (0,095 $ vs 0,405 $ pour 20q ; soit ~0,005 $/q).
- **Recommandation** : adopter Haiku pour les requêtes standard sur le Hub IA. Pour scénarios à risque (RGPD complexe, AI Act juridique), Sonnet 4.6 reste justifiable mais peut être déclenché ad-hoc.

## Reco combinée pour S2.10+

**Combinaison à benchmarker** : **Haiku 4.5 gen + BM25 hybrid retrieval**. Hypothèse : devrait combiner les bénéfices (qualité 20/20 + latence ~6 s + coût ~0,12 $/eval 20q). Si confirmé, c'est la nouvelle baseline production candidate. Effort : trivial (combiner les 2 wrappers).

## Cas q-083 (cas-école saturation vague 8)

| Bench | Score | Sources citées |
|---|:---:|---|
| baseline | 0 | chiffres-macro-2026, cu-027, architecture-a1-saas-proprietaire |
| bench-2 top_k=3 | 0 | chiffres-macro-2026, cu-027, architecture-a1-saas-proprietaire |
| bench-3 embed -large | 0 | chiffres-macro-2026, cu-027 |
| **bench-4 BM25 hybrid** | **1 ✅** | **outils-llm**, chiffres-macro-2026, cu-027 |
| bench-5 Haiku | 0 | chiffres-macro-2026 |

Le **hybrid BM25+dense est le seul mécanisme qui ramène outils-llm dans le top-5** pour cette question. Le signal lexical (« API », « Sonnet », « Opus », « Claude ») suffit à BM25 pour faire émerger les chunks d'outils-llm que le dense seul ne ranke pas assez haut.

## Coût total S2.9 Lot I + benchs

| Étape | Coût |
|---|---|
| Baseline (Sonnet, 20q) | 0,4053 $ |
| Bench-2 top_k=3 (Sonnet, 20q) | 0,3239 $ |
| Bench-3 embed -large (Sonnet 20q + re-embed 444 chunks) | 0,4083 $ |
| Bench-4 BM25 hybrid (Sonnet, 20q) | 0,4124 $ |
| Bench-5 Haiku (Haiku, 20q) | 0,0953 $ |
| **Total** | **1,6452 $** |

Sous le cap S2.9 de 3,50 $. Bench-1 reranking : non exécuté (capacité absente), économie ~0,80 $.
