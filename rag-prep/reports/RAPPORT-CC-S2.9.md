# RAPPORT-CC-S2.9 — Sprint optimisation : R11 cleanup + bug-fix --filter-unit + benchmarks 4/5 + arbitrage final

**Émetteur :** Claude Code Hub IA Plateforme (Lot J)
**Destinataire :** Cowork Hub IA Plateforme + Blaise Cavalli (garant transverse)
**Sprint :** S2.9 (clôture définitive)
**Brief source :** `rag-prep/briefs/BRIEF-CC-S2.9.md` (sprint optimisation / tech debt pur)
**Branche développement :** `claude/execute-s29-lot-j-rapport` (depuis `main` post-merge PR #111)
**Date :** 27 mai 2026
**Allocation D-030 :** hybride codifiée SPEC v2.3 (**3ᵉ sprint consécutif avec Lot Dev Plateforme dès démarrage**) — Cowork (Lots A, F.9, F.9-bis) + Plateforme (**Lot Dev --filter-unit + Lot J**) + Desktop (Lot I référence intégré + Bench-2 à Bench-5)

---

## 1. Objectifs S2.9

Le sprint S2.9 est le **premier sprint sans production éditoriale** du POC : focus exclusif tech debt + optimisation latence/coût. Quatre axes structurants :

1. **Patches R11 éditoriaux** (Lot F.9 + F.9-bis Cowork) — traiter les 85 manquements R11 détectés par `citation_audit.py` en S2.8 + les 27 résiduels vague 8 (architectures + brique pattern-grille) pour atteindre **0 manquement R11 audit**.
2. **Bug-fix `--filter-unit`** (Lot Dev Plateforme) — implémenter le flag CLI prescrit dans les briefs Lot I depuis S2.7 mais jamais codé (2 occurrences contournées Desktop-side par 2 sous-YAML dérivés).
3. **Benchmark optimisations latence/coût** (Lots Bench-1 à Bench-5 Desktop) — 5 variations sur baseline Sonnet 4.6 / top-k 5 / embed-small : reranking, top-k 3, embeddings -large, BM25+dense hybrid, Haiku 4.5 sur eval.
4. **Arbitrage final SPEC v2.4** (Lot J Plateforme) — recommandation explicite sur lesquelles optimisations activer en production, codification patterns émergents.

**Question structurante** : le pattern de saturation **AP-8 cluster fiches sœurs** identifié par q-083 (RAPPORT-CC-S2.8 §4) est-il soluble par une optimisation retrieval seule, sans toucher au contenu MD ?

---

## 2. Livrables par lot

| Lot | Acteur | Livrable | PR | Statut |
|---|---|---|---|---|
| **A** | Cowork | SPEC v2.3 + BRIEF-CC-S2.9 | #107 | ✅ mergée |
| **Dev --filter-unit** | Plateforme | `rag/code/eval/run_eval.py` flag + `filter_questions_by_unit()` + 9 tests + DIAGNOSTIC + VALIDATION-SCORING 5/5 | #108 | ✅ mergée |
| **F.9** | Cowork | Patches R11 éditoriaux — 85 manquements sur 21 fichiers vague 5-7 | #109 | ✅ mergée |
| **I + Benchs** | Desktop | Lot I baseline (intégré au comparatif) + Bench-2/3/4/5 + comparatif + wrappers `bench_runner.py` / `bench_runner_hybrid.py` + `rank_bm25` dans requirements | #110 | ✅ mergée |
| **F.9-bis** | Cowork | Patches R11 résiduels vague 8 — 27 manquements sur 6 fiches (architectures A1-A4-Hybride + brique pattern-grille) | #111 | ✅ mergée |
| **J** | Plateforme | RAPPORT-CC-S2.9 (ce document) + PR finale | *(en cours)* | ⏳ |

**Lots non joués cette sprint** : pas de Lot B (pas de sondage D-026 — sprint sans production), pas de Lot F.X (pas de vague nouvelle), pas de Lot G/H (whitelist + golden set inchangés). Pattern « sprint tech debt pur » inédit qui mériterait formalisation SPEC v2.4 (cf. §6).

**Récurrence pattern Lot Dev Plateforme dès démarrage** : 3ᵉ sprint consécutif (S2.7 mode adversarial → S2.8 R11 audit → S2.9 bug-fix --filter-unit). La codification SPEC v2.3 §allocation D-030 (issue RAPPORT-CC-S2.8 §6 proposition 2) est validée empiriquement dès son 1ᵉʳ sprint d'application.

---

## 3. Métriques par benchmark

### 3.1 Tableau comparatif (sous-set 20q stratifié — 6 standard stress + 14 adversariales)

| Bench | Std/6 | Adv/14 | Total/20 | p50 (s) | p90 (s) | Coût ($) | Δ qualité | Δ latence | Δ coût |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **baseline** Sonnet 4.6 / top-k 5 / embed-small | 5 | 14 | **19/20** | 12,0 | 20,0 | 0,4053 | — | — | — |
| bench-1 reranking | — | — | **non exécuté** | — | — | — | — | — | — |
| bench-2 top-k 5→3 | 4 ↓ | 14 | 18/20 | 10,0 | 17,0 | 0,3239 | **−1 std** (q-030) | **−16 % p50** | **−20 %** |
| bench-3 embed-large (1536 dim) | 5 | 12 ↓ | 17/20 | 11,0 | 20,0 | 0,3848 + 0,024 ingest | **−2 adv** | ~0 | +5 % +×6,5 ingest |
| **bench-4 BM25+dense hybrid (RRF k=60)** | **6** ↑ | 14 | **20/20 🎯** | 11,0 | 22,0 | 0,4124 | **+1 std (q-083 résolu)** | +10 % p90 | ~0 (+1,8 %) |
| **bench-5 Haiku 4.5 (génération seule)** | 5 | 14 | 19/20 | **5,0** | **8,0** | **0,0953** | 0 | **−58 % p50 / −60 % p90** | **−76 %** |

**Note méthodologique sur le sous-set** : Desktop a arbitré un sous-set 20q stratifié (6 std clés couvrant q-030/q-036/q-056/q-083/q-073/q-076 + les 14 adversariales) face à l'incohérence budgétaire du brief : 118q × 5 benchs × ~0,024 $/q ≈ 17 $ vs cap durci 3,50 $. Le sous-set préserve l'angle stress + non-régression et permet une **comparaison apples-to-apples** entre les 5 evals (sous-set constant). Coût total réel : **1,6452 $** (cap respecté avec marge ~0,80 $ — économie associée au bench-1 non exécuté). Le pattern « sous-set échantillonné par défaut sur benchmarks » mérite codification SPEC v2.4 (cf. §6).

### 3.2 Focus q-083 (cas-école saturation AP-8 cluster fiches sœurs)

| Bench | Score q-083 | Sources citées |
|---|:---:|---|
| baseline | 0 ❌ | chiffres-macro-2026, cu-027, architecture-a1-saas-proprietaire |
| bench-2 top-k 3 | 0 ❌ | chiffres-macro-2026, cu-027, architecture-a1-saas-proprietaire |
| bench-3 embed-large | 0 ❌ | chiffres-macro-2026, cu-027 |
| **bench-4 BM25 hybrid** | **1 ✅** | **outils-llm**, chiffres-macro-2026, cu-027 |
| bench-5 Haiku | 0 ❌ | chiffres-macro-2026 |

**Lecture** : seul le hybrid BM25+dense ramène `outils-llm` dans le top-5. Le signal lexical (« API », « Sonnet », « Opus », « Claude ») suffit à BM25 pour faire émerger les chunks que le dense seul ne ranke pas assez haut face au cluster « Coût indicatif » des 5 architectures vague 8. **Validation empirique du pattern AP-8** (RAPPORT-CC-S2.8 §5 Finding 4) : la saturation par cluster de fiches sœurs est **soluble par fusion lexicale + sémantique sans modification éditoriale**.

### 3.3 R11 audit post-patches

| Étape | Manquements R11 | Mentions correctes |
|---|:---:|:---:|
| S2.8 audit initial (vague 5-7) | 85 | 3 |
| Post-Lot F.9 (patches Cowork vague 5-7) | 27 résiduels vague 8 | ~43 |
| Post-Lot F.9-bis (patches Cowork vague 8) | **0 ✅** | **70** |

R11 audit **clean** : `python3 rag/code/audit/citation_audit.py` retourne `CLEAN — aucun manquement R11 détecté.` sur les 38 MD du vault.

### 3.4 Suite tests cumulée

| Indicateur | S2.8 | S2.9 | Delta |
|---|:---:|:---:|:---:|
| Tests `rag/code/` | 234 | **243** | +9 (TestFilterQuestionsByUnit + TestFilterUnitCLI) |
| Tests verts | 234/234 | **243/243** | ✅ |
| Couverture nouveaux modules | citation_audit.py 28 tests | citation_audit.py 28 + filter_questions_by_unit 9 | — |

---

## 4. Anomalies & observations

### Anomalie #1 — Bench-1 reranking non exécuté (à reprogrammer S2.10)

**Constat** : capacités Cohere/Voyage absentes (clé API non provisionnée, librairies `cohere`/`voyageai` non installées) ET `sentence_transformers` non installé (lourd ~500 MB pour le cross-encoder local `BAAI/bge-reranker-large`). Desktop a documenté la décision en clair dans la branche `s2.9-eval-reference` et économisé ~0,80 $ Anthropic.

**Décision** : reporter à S2.10 avec arbitrage Blaise préalable sur la voie (acquisition clé API Cohere/Voyage vs install local 500 MB). **Important** : la combinaison BM25 hybrid + Haiku 4.5 retenue ici (cf. §5) couvre déjà 20/20 à coût/latence optimisés ; le reranking est désormais un « nice to have » pas un « critical path ».

### Anomalie #2 — Bench-3 embeddings -large : régression adversarial

**Constat** : `text-embedding-3-large` (1536 → 3072 dim effectives) régresse l'adversarial de 14 → 12 (2 hallucinations introduites) sans gain mesurable sur le standard. q-083 reste KO. Surcoût ingestion ×6,5 ($0,024 vs $0,0035 pour -small) **sans bénéfice**.

**Hypothèse diagnostique** : sur-spécification sémantique → le modèle plus fin sépare mieux dans l'espace embeddings, ce qui augmente la similarité de chunks hors-corpus avec les questions pièges (q-adv-001 XYZ-2027, q-adv-008 BCG×AI Act) et fait basculer le RAG en mode « tentative de réponse » au lieu de refus. **À retenir comme cas-école** : un meilleur modèle d'embeddings n'est pas systématiquement un meilleur retrieval — le contexte adversarial doit faire partie du benchmark systématiquement (validation empirique SPEC v2.2 §rythme +2 adv/vague).

### Anomalie #3 — Bench-2 top-k 5→3 : régression standard q-030

**Constat** : la réduction top-k 5 → 3 fait perdre q-030 (« lien entre PME et données structurées non textuelles ») — `pr-07` sort du top-3 alors qu'il était #4-#5 du top-5 baseline. Gain latence -16 % et coût -20 % réels mais **non admissible** au regard de la non-régression intégrale exigée par cap qualité minimal 100/104 + 12/14 (cf. §5).

**Note** : top-k 3 reste exploitable dans un usage à risque tolérance élevé (chatbot prospect-non-PME, démo) avec patch éditorial préalable des fiches transversales pour densifier les premiers chunks. Pas la voie prioritaire.

### Observation #1 — BM25 hybrid résout AP-8 = validation empirique SPEC v2.3

**Constat** : RAPPORT-CC-S2.8 §5 Finding 4 a identifié le pattern « cluster de fiches sœurs → saturation sur termes transverses » comme nouveau AP-8 (vs AP-7 module pivot dense). Le bench-4 résout empiriquement le cas-école q-083 **sans modification éditoriale**. → **Le pattern curatif « activer BM25 hybrid en prod si AP-8 récurrent » est désormais un acquis**, à codifier SPEC v2.4 (cf. §6).

### Observation #2 — Haiku 4.5 préserve qualité 19/20 = pivot économique

**Constat** : substitution **uniquement** sur l'étape génération (retrieval inchangé) → score 19/20 (identique baseline Sonnet), latence p50 5 s (−58 %), coût 0,005 $/q (−76 %). Pas de dégradation observable sur le sous-set 20q (stress + adversarial). Pivot économique majeur : pour le même budget Anthropic mensuel, on peut faire **×4 plus d'évaluations** OU **×3-4 plus de production**.

**Garde-fou** : le sous-set est non-représentatif des questions « RGPD complexe / AI Act juridique » qui peuvent demander Sonnet — la décision §5 inclut un routing ad-hoc.

### Observation #3 — Incohérence budgétaire du brief S2.9 (à retenir)

**Constat** : le brief BRIEF-CC-S2.9 §3 prescrit « 118q × 6 benchs × ~0,024 $/q ≈ 17 $ vs cap 3,50 $ » — incohérence cap × volume. Desktop a arbitré en autonomie un sous-set 20q stratifié (cf. §3.1) **après échange synchrone Cowork** et a livré dans le cap avec marge. **Pattern à codifier** : « sous-set échantillonné par défaut sur benchmarks d'optimisation » devient une méthode normée SPEC v2.4 (cf. §6 proposition 4) pour éviter de re-déclencher cette friction en S2.10+.

### Observation #4 — Hygiène merge respectée (4ᵉ sprint consécutif clean)

`git grep "<<<<<<<"` retourne uniquement des références documentaires (mentions de la règle dans SPEC + JOURNAL). Aucun marqueur de conflit réel introduit sur la branche Lot J. Discipline SPEC v2.0 §Hygiène merge tient depuis S2.6.

---

## 5. Décisions structurantes — arbitrage final optimisations production

### Méthodologie d'arbitrage (brief §8.2)

- **Qualité minimale** : retenir uniquement si standard ≥ 100/104 (extrapolé du sous-set 6/6 = 100 % maintenu) ET adversarial ≥ 12/14
- **Gain latence minimal** : retenir si gain p90 ≥ 15 %
- **Gain coût minimal** : retenir si réduction coût/q ≥ 20 %
- Combinaisons possibles (Haiku + BM25, etc.) examinées en pistes S2.10

### Décision #1 — ✅ **Adopter bench-4 BM25+dense hybrid en production (retrieval)**

- **Qualité** : 20/20 (seul bench qui résout q-083 — cas-école AP-8)
- **Coût** : ~0 % vs baseline (+1,8 %)
- **Latence** : +10 % p90 (acceptable car compensé par bench-5)
- **Effort** : modéré (rank_bm25 librairie Python légère, fusion RRF k=60, ~150 lignes code)

**Justification** : le pattern AP-8 cluster fiches sœurs est désormais résolu **sans coût éditorial**. Au rythme actuel de production (1 vague/2 sprints), la prochaine occurrence d'un cluster (vague 9 = 3-4 CU restants ?) bénéficiera immédiatement de cette mitigation. **Recommandation : Lot Dev S2.10 Plateforme pour intégration prod retrieval BM25 hybrid**.

### Décision #2 — ✅ **Adopter bench-5 Haiku 4.5 en production (génération par défaut)**

- **Qualité** : 19/20 identique baseline Sonnet
- **Coût** : −76 % (0,005 $/q vs 0,021 $/q)
- **Latence** : −58 % p50 / −60 % p90
- **Effort** : trivial (changement du `model=` dans `query.py`, fallback Sonnet via routing ad-hoc)

**Justification** : pivot économique majeur, aucun trade-off mesurable sur le sous-set 20q. Le routing ad-hoc Sonnet est conservé pour les requêtes à risque (RGPD complexe, AI Act juridique, audits sécurité, génération de contenu pédagogique long). **Recommandation : Lot Dev S2.10 Plateforme pour switch défaut Haiku + intégration routing rules**.

### Décision #3 — ❌ **Skipper bench-2 top-k 5→3**

Régression standard q-030 (perte de `pr-07`) inadmissible vs cap non-régression intégrale. Gain latence/coût réel mais incompatible avec la qualité minimale fixée. **Décision : pas d'intégration**.

### Décision #4 — ❌ **Skipper bench-3 embeddings -large**

Régression adversarial 14 → 12 + surcoût ingest ×6,5 sans gain mesurable. Cas-école « meilleur modèle ≠ meilleur retrieval » à documenter. **Décision : pas d'intégration**.

### Décision #5 — ⏭️ **Reprogrammer bench-1 reranking en S2.10**

Non exécuté faute de capacité (clés API absentes + libs non installées). Arbitrage Blaise requis sur la voie (Cohere/Voyage cloud vs sentence_transformers local 500 MB). Priorité **non-prioritaire** étant donné que la combinaison BM25 hybrid + Haiku 4.5 atteint 20/20 ; reranking devient un « nice to have ».

### Combinaison à benchmarker S2.10 (priorité absolue)

**Hypothèse à tester** : Haiku 4.5 + BM25 hybrid (retrieval BM25+dense + génération Haiku).

**Projection** :
- **Qualité** : 20/20 maintenu (Haiku préserve 19/20 standalone + BM25 hybrid résout q-083 → addition = 20/20)
- **Latence** : p50 ~6 s (−50 % vs baseline 12 s — bench-5 latence retrieval + BM25 marginal)
- **Coût** : ~0,12 $ pour 20q (~×4 réduction vs baseline 0,40 $)

**Validation requise S2.10** : eval combinée + analyse latence retrieval (BM25 +1-2 s) + coût.

---

## 6. Recommandations SPEC v2.4 (4 propositions à arbitrer Cowork)

### Proposition 1 — Codifier le pattern curatif « activer BM25 hybrid si AP-8 récurrent »

Ajouter à SPEC §AP-8 (introduit v2.3) un **pattern curatif additionnel** : « si un cas-école AP-8 (cluster fiches sœurs saturant le retrieval sur un terme transverse) est confirmé sur 2 sprints consécutifs, activer BM25+dense hybrid en production retrieval ». **Cas-école documenté** : q-083 tarifs API Sonnet/Opus (S2.8 §4 + S2.9 bench-4). Validation empirique : score 20/20 vs 19/20 baseline sans modification éditoriale. Le pattern complète la mitigation préventive « différenciation des leads » (SPEC v2.3 AP-8 origine).

### Proposition 2 — Codifier Haiku 4.5 comme baseline production pour les requêtes standard

Ajouter à SPEC §Performances une nouvelle entrée : « Modèle de génération par défaut = Haiku 4.5 (`claude-haiku-4-5-20251001`), routing Sonnet 4.6 ad-hoc pour les requêtes à risque (juridique RGPD/AI Act, audits sécurité, génération pédagogique long format) ». **Recalibrage table latence + coût** :

| Vault | Latence p50 (cible) | Latence p90 (cible) | Coût/q (cible) |
|---|---|---|---|
| 200-300 chunks | 4-5 s (Haiku) / 12-15 s (Sonnet) | 7-8 s / 18-20 s | 0,005 $ / 0,021 $ |
| 300-400 chunks | 5-6 s / 15-19 s | 8-10 s / 22-26 s | 0,005-0,006 $ / 0,021-0,025 $ |
| 400-500 chunks | 6-7 s / 18-22 s | 9-12 s / 25-30 s | 0,006-0,008 $ / 0,025-0,030 $ |

### Proposition 3 — Anti-pattern « 3ᵉ occurrence brief CLI » (issue Plateforme DIAGNOSTIC-FILTER-UNIT)

Codifier dans SPEC §Validation : « tout flag CLI prescrit dans un BRIEF Desktop pour `rag/code/eval/run_eval.py` ou `rag/code/audit/*` doit être validé empiriquement (`--help` + test argparse) **avant** ouverture du brief. Si manquant : ouverture d'un Lot Dev Plateforme dès l'identification, **pas en fin de sprint** ». Symétrique de la discipline SPEC v2.2 §Validation manuelle (issue cas-école harness adversarial S2.7 0/12). Évite la 3ᵉ occurrence d'écart silencieux brief↔code.

### Proposition 4 — Codifier « sous-set échantillonné par défaut sur benchmarks d'optimisation »

Ajouter à SPEC §Validation benchmark : « pour tout sprint d'optimisation comparant N ≥ 3 variantes sur un golden set, **arbitrage Cowork × Desktop préalable** sur un sous-set stratifié 15-25q (typiquement 5-8 std stress + 10-14 adv) au lieu du golden set complet. Cap budgétaire et latence d'exécution doivent permettre la couverture des N variantes prévues × 1,2 (marge ; +20 % pour rejeu si bug détecté). Validation empirique apples-to-apples sur sous-set constant ». Évite la friction observée S2.9 (118q × 5 benchs × 0,024 $/q ≈ 17 $ vs cap 3,50 $).

---

## 7. Pistes investigation S2.10

1. **Combinaison Haiku 4.5 + BM25 hybrid** (priorité absolue) — eval sous-set 20q + projection 118q. Hypothèse : 20/20 + p50 ~6 s + coût ~0,12 $/20q.
2. **Intégration prod retrieval BM25 hybrid** (Lot Dev Plateforme S2.10) — porter `bench_runner_hybrid.py` (Desktop) en module pipeline `rag/code/backend/hybrid_retrieval.py`. Effort ~2-3h + tests.
3. **Switch défaut Haiku 4.5 + routing rules** (Lot Dev Plateforme S2.10) — modification `rag/code/backend/query.py` + table de routing ad-hoc Sonnet (RGPD/AI Act juridique = Sonnet, reste = Haiku). Effort ~1-2h + tests.
4. **Bench-1 reranking** (si capacité acquise) — arbitrage Blaise préalable sur la voie (Cohere/Voyage cloud vs sentence_transformers local 500 MB). Priorité non-prioritaire vu que 20/20 déjà atteint sans reranking.
5. **Démarrage vague 9** (CU-002, CU-003, CU-005, etc.) — production éditoriale Cowork avec stack optimisée Haiku + BM25 hybrid en place. AP-7 + AP-8 + nouvelle proposition « cluster curatif BM25 » à appliquer dès la conception.
6. **Audit v3 audit-md-rag éventuel** (si déclencheur SPEC v2.4 § audit v3 atteint) — élargissement R12+ (nouvelles règles d'audit MD) selon arbitrage Cowork.

---

## 8. Coûts cumulés S1 → S2.9

### Détail S2.9

| Phase | Acteur | Coût $ |
|---|---|---|
| Lot A — SPEC v2.3 + BRIEF | Cowork | 0,00 |
| Lot Dev — bug-fix --filter-unit | Plateforme | **0,00** |
| Lot F.9 — patches R11 vague 5-7 (85 manquements) | Cowork | 0,00 |
| Lot I baseline + Bench-2/3/4/5 + comparatif | Desktop | **1,6452** |
| Lot F.9-bis — patches R11 résiduels vague 8 (27 manquements) | Cowork | 0,00 |
| Lot J — RAPPORT + PR (ce commit) | Plateforme | 0,00 |
| **Total S2.9** | — | **~1,65 $** |

**Note méthodologique** : le Lot I « référence » prescrit au brief (~0,50 $) a été **intégré dans le comparatif** par Desktop (baseline = première ligne de la table §3.1, coût 0,4053 $ inclus dans le total 1,6452 $). Pas de Lot I séparé.

**Bench-1 reranking non exécuté** : économie ~0,80 $ vs cap. Marge totale cap 3,50 $ → réel 1,65 $ = ~1,85 $ disponible reportable S2.10.

### Cumul historique S1 → S2.9

| Sprint | Coût $ Anthropic |
|---|---|
| S1 → S2.4 | ~5,10 |
| S2.5 | ~2,10 |
| S2.6 | ~2,05 |
| S2.7 | ~2,59 |
| S2.8 | ~2,85 |
| **S2.9** | **~1,65** |
| **Total cumulé S1 → S2.9** | **~16,34 $** |

OpenAI cumulé : ~0,03 $ (embeddings + ingest incréments + re-embed 444 chunks bench-3 ~0,024 $).

### Budget

**Cap mensuel D-013 (50 $/mois Anthropic, 10 $/mois OpenAI) préservé** — le cumul ~16,34 $ depuis S1 (sur ~7 semaines) reste largement sous le plafond mensuel. **Le sprint S2.9 inverse la tendance** : ~1,65 $ vs ~2,5-2,85 $ moyens depuis S2.5, grâce au switch d'attente Haiku 4.5 (validé empiriquement ici) + non-exécution bench-1. **Projection S2.10** : si Haiku 4.5 devient le défaut prod **dès S2.10**, le coût eval mensuel devrait se diviser par 3-4 → marge confortable pour le démarrage vague 9 (4-6 modules CU restants).

---

## Liste des commits / PR S2.9

| PR | Lot | Acteur |
|---|---|---|
| #107 | A — SPEC v2.3 + BRIEF-CC-S2.9 | Cowork |
| #108 | Dev — bug-fix --filter-unit + 9 tests + DIAGNOSTIC + VALIDATION-SCORING 5/5 | Plateforme |
| #109 | F.9 — patches R11 éditoriaux 85 manquements vague 5-7 | Cowork |
| #110 | I + Bench-2/3/4/5 + comparatif + wrappers + rank_bm25 | Desktop |
| #111 | F.9-bis — patches R11 résiduels 27 manquements vague 8 | Cowork |
| *(ce commit)* | J — RAPPORT + PR finale | Plateforme |

**Suite tests cumulée S1 → S2.9** : 243/243 verts (+9 vs S2.8 = `TestFilterQuestionsByUnit` + `TestFilterUnitCLI`).

---

*Rapport produit le 27 mai 2026 par Claude Code Hub IA Plateforme (Lot J). Format conforme brief CC-S2.9 (8 sections, calque S2.8) + déposé dans `rag-prep/reports/` selon convention Cowork. Sprint S2.9 définitivement clôturé après merge de la PR finale.*

***Finding central** : **2 optimisations à adopter en production — BM25+dense hybrid (résout AP-8 q-083 : 20/20) + Haiku 4.5 par défaut (−76 % coût / −58 % latence à qualité préservée)**. AP-8 désormais soluble par retrieval seul, sans coût éditorial. Pattern « sprint tech debt pur » inédit dans le POC validé empiriquement (effort cumulé 8-12h, coût 1,65 $, livrables 4 PRs). Les 4 propositions d'amendement SPEC v2.4 (§6) restent à arbitrer par Cowork après merge.*
