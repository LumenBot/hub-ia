# BRIEF-CC-S2.9 — Sprint optimisation / tech debt pur (patches R11 + bug-fix --filter-unit + benchmark optimisations latence) + SPEC v2.3

**Émetteur :** Cowork Hub IA Plateforme
**Destinataire :** Claude Code Plateforme (Lot Dev bug-fix + Lot J), Claude Code Desktop (Lots Bench + I eval), pas de Cowork Hub IA (pas de production from scratch)
**Garant transverse :** Blaise Cavalli
**Sprint :** S2.9 (post-clôture S2.8 — 103/104 std + 14/14 adv, **vault 444 chunks au-dessus seuil 400 SPEC v2.1**, coût cumulé S1→S2.8 ~14,67 $)
**Date de cadrage :** 26 mai 2026
**SPEC en vigueur :** **v2.3** (produite Cowork-side simultanément à ce brief, sync ascendante en début de sprint)
**Allocation D-030 :** hybride **Lot Dev Plateforme dès démarrage** (codifié SPEC v2.3) + Cowork (Lot A SPEC + Lot F.9 patches R11) + Claude Code Desktop (Lots Bench benchmark + I eval référence)
**Particularité S2.9** : **pas de production contenu, pas de sondage D-026 nécessaire** — sprint exclusivement tech debt + optimisation.

---

## 1. Décisions Blaise validées (26 mai 2026)

1. **SPEC v2.3** — 3 propositions Plateforme validées et produites Cowork-side : AP-8 saturation cluster fiches sœurs + officialisation Lot Dev Plateforme D-030 + tech debt code §Items S2.9.
2. **S2.9 sprint tech debt pur** — pas de production contenu, focus exclusif optimisations latence + tech debt code + patches R11.
3. **Pas de sondage D-026** — pas de production from scratch en S2.9, donc pas applicable.
4. **Benchmark optimisations latence** : 5 variations à tester (reranking, top-k 5→3, embeddings-large, BM25+dense, Haiku 4.5 sur eval). Arbitrage en fin de sprint sur lesquelles activer en production.

## 2. Objectifs S2.9

Quatre axes structurants :

1. **Patches R11 éditoriaux** (Lot F.9 Cowork) : traiter les 85 manquements R11 détectés audit S2.8 sur 21 fichiers existants. Application strictement mécanique (transformation `Outil` → `[[outils-X|Outil]]` à la première occurrence du fichier). Effort ~2-3h Cowork éditorial.

2. **Bug-fix `--filter-unit`** (Lot Dev Plateforme) : corriger le bug détecté pendant Lot I S2.8 sur le filtre `--filter-unit adversarial` de `rag/code/eval/run_eval.py`. Diagnostic + correctif + tests unitaires. Effort ~1-2h Plateforme dev.

3. **Benchmark optimisations latence** (Lot Bench Desktop) : 5 variations à benchmarker sur le golden set complet 118q (104 std + 14 adv) pour mesurer impact qualité retrieval + gain latence + impact coût. Effort ~2-3h Desktop, ~3,50 $ Anthropic cumulé.

4. **Arbitrage final SPEC v2.4** (Lot J Plateforme) : RAPPORT-CC-S2.9 avec recommandations explicites sur lesquelles optimisations activer en production + propositions SPEC v2.4 selon mesures empiriques.

**Cibles métriques S2.9** :
- **R11 audit post-patches** : 0 manquement (audit clean)
- **Tech debt --filter-unit** : 0 régression sur 234 tests + filtre adversarial fonctionnel
- **Benchmark optimisations** : 5 variations testées, minimum 1 retenue pour production avec gain mesurable (latence p50 ≤ 18 s ou p90 ≤ 22 s ou coût/q ≤ 0,020 $)
- **Eval référence post-patches R11** : non-régression 103+/104 std + 14/14 adv maintenue
- **Cap durci sprint S2.9** : ~3,50 $ Anthropic (5 benchmarks × ~0,60-0,80 $ + eval référence ~0,50 $)

## 3. Lots S2.9 — allocation hybride D-030

| Lot | Acteur | Périmètre | Dépendance | Effort |
|---|---|---|---|---|
| **A** | Cowork | SPEC v2.3 déjà produite + sync ascendante (commit Git par Blaise via Desktop) | — | 5 min (sync) |
| **Dev --filter-unit** | Plateforme | Diagnostic + bug-fix `rag/code/eval/run_eval.py --filter-unit adversarial` + tests unitaires + documentation | A clôturé | 1-2h dev + tests |
| **F.9** | Cowork | Patches R11 éditoriaux : traiter les 85 manquements selon rapport audit S2.8 sur 21 fichiers (`cu-008.md` 10, `dep-05.md` 7, `glossaire.md` 7, `pattern-souverainete-eu.md` 10, `dep-02.md` 5, etc.) | A clôturé | 2-3h Cowork éditorial |
| **Bench-1** | Desktop | Benchmark **Reranking** : ajout couche reranking (cross-encoder ou Cohere reranker) sur top-10 → top-5. Eval 118q + mesure latence + coût | Dev clôturé | ~30 min + 0,80 $ |
| **Bench-2** | Desktop | Benchmark **Top-k 5→3** : réduction top-k retrieval. Eval 118q + mesure latence + coût | Dev clôturé | ~30 min + 0,60 $ |
| **Bench-3** | Desktop | Benchmark **Embeddings -large** : passage à text-embedding-3-large (1536 dim vs 1024 small actuel). Re-ingestion ChromaDB + Eval 118q + mesure latence + coût | Dev clôturé | ~45 min + 0,60 $ |
| **Bench-4** | Desktop | Benchmark **BM25 + dense hybrid** : ajout BM25 (lexical) au retrieval dense. Eval 118q + mesure latence + coût | Dev clôturé | ~30 min + 0,60 $ |
| **Bench-5** | Desktop | Benchmark **Haiku 4.5 sur eval** : remplacement Sonnet 4.6 par Haiku 4.5 sur l'étape génération. Eval 118q + mesure latence + coût | Dev clôturé | ~30 min + 0,30 $ (Haiku ~3× moins cher) |
| **I (référence)** | Desktop | Eval référence post-patches R11 + bug-fix `--filter-unit` (sur baseline Sonnet 4.6 actuelle, sans optimisation) — confirmation non-régression 103+/104 std + 14/14 adv | F.9 + Dev clôturés | ~30 min + 0,50 $ |
| **J** | Plateforme | RAPPORT-CC-S2.9 (8 sections format S2.8) + analyse comparative des 5 benchmarks + recommandation arbitrage final SPEC v2.4 + PR finale S2.9 | I + Bench-1 à Bench-5 clôturés | 45 min - 1h |

**Cap durci sprint S2.9** : ~3,50 $ Anthropic (5 benchmarks ~3,00 $ + eval référence 0,50 $). Cohérent SPEC v2.1 §Performances vault > 400 chunks.

## 4. Spécification Lot F.9 — Patches R11 éditoriaux (Cowork)

### 4.1 Cible

0 manquement R11 après patches (validation par re-run `citation_audit.py` post-patches).

### 4.2 Méthode

Patches mécaniques selon rapport audit S2.8 (`rag-prep/reports/audit-md-rag-R11-s2.8.md`) :

1. Lire le rapport audit (85 lignes de manquements détaillées)
2. Pour chaque ligne : ouvrir le fichier MD source, repérer la première occurrence de l'outil mentionné, remplacer par le wikilink recommandé
3. **Discipline R10/R11 stricte** : la transformation est purement mécanique, ne pas modifier le sens du texte
4. **Discipline hygiène merge SPEC v2.0** : `git grep "<<<<<<<"` retourne vide post-stash pop avant `git add`
5. Re-exécuter `python -m rag.code.audit.citation_audit` post-patches : attendu 0 manquement

### 4.3 Répartition par fichier (du plus chargé au moins)

| Fichier MD | Manquements | Outils principaux concernés |
|---|---|---|
| `cu-008.md` | 10 | Claude, GPT, Mistral, NotebookLM, Lucie, Pleias-RAG, Qdrant, pgvector, Pinecone, ChromaDB, Dify, Flowise, LangChain |
| `pattern-souverainete-eu.md` | 10 | Claude, GPT, Mistral, Mixtral, Llama, Lucie, Pleias-RAG, LightOn, Langfuse, Qdrant, n8n |
| `dep-05.md` | 7 | Claude, LangChain, Langfuse, LangSmith, Comet Opik, Phoenix Arize, Helicone |
| `glossaire.md` | 7 | Claude, GPT, Mistral, Llama, Qdrant, pgvector, Pinecone, ChromaDB |
| `dep-02.md` | 5 | Claude, Mistral, Qdrant, Pinecone |
| `dep-07.md` | 5 | LangChain, Langfuse, LangSmith, Comet Opik, Phoenix Arize |
| `pr-07.md` | 4 | Claude, GPT, Mistral, n8n, Make |
| `dep-01.md` | 6 | Claude, GPT, Mistral, Qdrant, pgvector, ChromaDB |
| `pr-09.md` | 2 | Claude, Mistral |
| `vigilance-confidentialite.md` | 4 | Claude, Mistral, Llama, Qwen |
| `pattern-llm-wiki.md` | 3 | Claude, NotebookLM, Pinecone |
| Autres (~12 fichiers) | 22 | variés |

### 4.4 Exemple de patch type (cu-008.md ligne 63)

**Avant** :
> 2. **Modèle IA** (Claude, GPT, Mistral) qui consulte la base vectorielle pour récupérer les chunks pertinents.

**Après** :
> 2. **Modèle IA** ([[outils-llm|Claude]], [[outils-llm|GPT]], [[outils-llm|Mistral]]) qui consulte la base vectorielle pour récupérer les chunks pertinents.

**Note discipline** : à la première occurrence uniquement (R11). Les occurrences ultérieures dans le même fichier peuvent rester en clair (cohérent avec audit S2.8 qui ne signale que la première occurrence).

### 4.5 Effort estimé

2-3h Cowork éditorial. Travail mécanique mais volumineux. Possibilité de scripter en bash/sed pour accélérer (à arbitrer en cours de production selon patience).

## 5. Spécification Lot Dev --filter-unit (Plateforme)

### 5.1 Cible

Bug-fix de `rag/code/eval/run_eval.py --filter-unit adversarial` détecté pendant Lot I S2.8. Diagnostic précis + correctif + tests unitaires.

### 5.2 Diagnostic attendu

À documenter précisément dans `briefs/DIAGNOSTIC-FILTER-UNIT-S2.9.md` (Plateforme) :
- Comportement attendu : `--filter-unit adversarial` filtre uniquement les questions avec `unit: adversarial`
- Comportement constaté S2.8 : à diagnostiquer (filtrage incomplet ? confusion units ? off-by-one ?)
- Cause root identifiée

### 5.3 Correctif + tests

- Correctif minimal (pas de refactoring large)
- 3-5 tests unitaires couvrant : filtre standard / filtre adversarial / filtre invalide / filtre vide
- Non-régression 234 tests existants (audit + scoring + citation_audit + run_eval)

### 5.4 Effort estimé

1-2h dev + tests + documentation. Coût Anthropic = 0 $.

## 6. Spécification Lots Bench-1 à Bench-5 — Benchmark optimisations latence (Desktop)

### 6.1 Méthode commune

Chaque benchmark = 1 eval complet 118q (104 std + 14 adv) sur baseline avec une seule optimisation modifiée. Reporting standardisé pour comparabilité.

**Baseline référence S2.8** : Sonnet 4.6, top-k 5, text-embedding-3-small (1024 dim), retrieval dense only, pas de reranking, vault 444 chunks.

**Cibles métriques** par benchmark :
- **Qualité retrieval** : standard ≥ 96/104 (non-régression vs 103/104 S2.8), adversarial ≥ 12/14
- **Latence** : p50 et p90 standard + adversarial à mesurer
- **Coût** : coût total eval + coût par question

**Reporting** : `briefs/BENCHMARK-S2.9-{nom}.md` avec score détaillé + latence p50/p90 + coût + tableau comparatif vs baseline.

### 6.2 Bench-1 — Reranking

**Variation** : ajout d'une couche de reranking sur top-10 retrieval → top-5 réordonné. Options : cross-encoder (BAAI/bge-reranker-large) ou Cohere Reranker v3.

**Hypothèse à tester** : qualité retrieval meilleure (top-5 mieux ordonné) au prix d'une latence +50-200 ms.

**Coût estimé** : ~0,80 $ (1 eval 118q + appels reranker).

### 6.3 Bench-2 — Top-k 5→3

**Variation** : retrieval top-3 chunks au lieu de top-5.

**Hypothèse à tester** : gain latence ~20-30 % (moins de contexte Sonnet) au prix possible de qualité retrieval -5-10 %.

**Coût estimé** : ~0,60 $ (eval 118q avec contexte réduit, moins de tokens in Sonnet).

### 6.4 Bench-3 — Embeddings -large (1536 dim vs -small 1024 dim)

**Variation** : passage à text-embedding-3-large (1536 dim) lors de l'ingestion ChromaDB + retrieval. Re-ingestion complète requise.

**Hypothèse à tester** : qualité retrieval meilleure (séparation cosine plus fine) au prix d'un coût embedding ×2 + latence cosine légèrement supérieure.

**Coût estimé** : ~0,60 $ (eval 118q + re-ingestion 35 MD = ~444 chunks × ~0,00013 $/chunk ≈ 0,06 $ embedding + eval).

### 6.5 Bench-4 — BM25 + dense hybrid

**Variation** : retrieval hybride combinant BM25 (lexical, rapide) + dense (cosine). Fusion des scores avec poids ~0,4 BM25 / 0,6 dense.

**Hypothèse à tester** : qualité retrieval meilleure sur les questions exactes (acronymes, chiffres exacts, noms propres) au prix d'une complexité retrieval (2 indexes à maintenir).

**Coût estimé** : ~0,60 $ (eval 118q standard, BM25 quasi gratuit).

### 6.6 Bench-5 — Haiku 4.5 sur eval

**Variation** : remplacement Sonnet 4.6 par Haiku 4.5 (`claude-haiku-4-5-20251001`) sur l'étape génération de réponse uniquement (retrieval inchangé).

**Hypothèse à tester** : gain latence ×3 (Haiku ~5 s/q vs Sonnet 16-19 s/q) + gain coût ×3-4 (Haiku moins cher) au prix possible d'une qualité réponse -5-15 %.

**Cible qualité** : standard ≥ 90/104 (perte tolérable -13 pts), adversarial ≥ 12/14.

**Coût estimé** : ~0,30 $ (Haiku ~3× moins cher que Sonnet sur 118q).

## 7. Spécification Lot I référence (Desktop)

### 7.1 Cible

Confirmation non-régression baseline S2.8 post-patches R11 + bug-fix `--filter-unit`. Sans optimisation activée.

**Cibles** :
- Standard ≥ 103/104 maintenu (non-régression)
- Adversarial ≥ 14/14 maintenu
- Latence p50 ≤ 22 s / p90 ≤ 26 s (cible SPEC v2.1 vault 400-500 chunks projeté ~470 chunks post-patches R11 mineurs)
- Coût ≤ 0,50 $

### 7.2 Procédure

1. Pull main + créer branche `s2.9-eval-reference`
2. **Discipline hygiène merge SPEC v2.0** : `git grep "<<<<<<<"` vide avant `git add`
3. Re-ingestion incrémentale ChromaDB (patches R11 = modifications éditoriales mineures, à valider si re-ingestion nécessaire ou si delta négligeable)
4. **Eval référence** : `python -m rag.code.eval.run_eval --questions rag/eval/questions.yaml --report rag/eval/eval-report-s2.9-reference.md --json rag/eval/eval-report-s2.9-reference.json`
5. **Mesure latence p50/p90** sur les 2 modes (standard + adversarial filter-unit fonctionnel post-bug-fix)
6. Commit + push artefacts + MAJ JOURNAL + STATUS
7. Reporting Cowork : confirmation non-régression + baseline pour comparaison Bench-1 à Bench-5

## 8. Spécification Lot J — Analyse comparative + arbitrage SPEC v2.4

### 8.1 Structure RAPPORT-CC-S2.9 (8 sections format S2.8)

1. **Objectifs S2.9** (4 axes : patches R11 + bug-fix --filter-unit + benchmark optimisations + arbitrage final)
2. **Livrables par lot** (A → J avec acteurs + commits)
3. **Métriques par benchmark** : tableau comparatif Bench-1 à Bench-5 vs baseline (qualité standard, qualité adv, latence p50/p90, coût/q, coût total)
4. **Anomalies & observations** — focus bug-fix --filter-unit + patches R11 impact retrieval éventuel + observations qualitatives benchmark
5. **Décisions structurantes** : **arbitrage final optimisations à activer en production** (typiquement 1-2 retenues sur les 5)
6. **Recommandations SPEC v2.4** : codification des optimisations retenues + patterns architecturaux émergents éventuels
7. **Pistes investigation S2.10** : démarrage vague 9 (CU-002, CU-003, CU-005, etc.) avec stack optimisée + audit v3 audit-md-rag éventuel
8. **Coûts cumulés** (S1 → S2.9, estimation ~18,2 $)

### 8.2 Arbitrage attendu §5

Méthodologie d'arbitrage recommandée :

- **Qualité minimale** : optimisation rejetée si standard < 100/104 ou adversarial < 12/14
- **Gain latence minimal** : optimisation retenue si gain p90 ≥ 15 % vs baseline
- **Gain coût minimal** : optimisation retenue si réduction coût/q ≥ 20 %
- **Combinaisons possibles** : Haiku 4.5 + top-k 3, Haiku 4.5 + embeddings-large, etc. (à arbitrer si gains additifs significatifs)

L'arbitrage final est validé par Cowork via AskUserQuestion post-Lot J avant Lot M (Lot mise en production des optimisations retenues, en S2.10 ou en patch immédiat selon impact).

## 9. Points de discipline post-S2.8 à honorer

- **Discipline hygiène merge SPEC v2.0** : `git grep "<<<<<<<"` obligatoire post-stash pop sur tous les lots
- **VALIDATION-SCORING-S2.9 obligatoire** (SPEC v2.2) pour le bug-fix `--filter-unit` (impact potentiel sur le scoring adversarial)
- **AP-7 + AP-8 vigilance** : à honorer dans les futures productions vague 9+ (anti-patterns codifiés SPEC v2.3)
- **Pattern « production module pivot dense » SPEC v2.1** : pas applicable en S2.9 (pas de production contenu)
- **D-030 hybride avec Lot Dev Plateforme dès démarrage** (codifié SPEC v2.3) : appliqué S2.9 avec Lot Dev --filter-unit
- **Eval référence pré-clôture** : Lot I référence obligatoire avant Lots Bench (mesure baseline propre)
- **Coût Anthropic transparent** : reporting par benchmark dans le RAPPORT-CC-S2.9 §3

## 10. Synthèse opérationnelle

**Démarrage immédiat (sans dépendance)** :
- **Lot A — Sync SPEC v2.3** (5 min — Blaise via Desktop)
- **Lot Dev --filter-unit** (1-2h Plateforme, en parallèle des autres lots)
- **Lot F.9 — Patches R11** (2-3h Cowork éditorial, en parallèle de Lot Dev)

**Après Lot Dev + Lot F.9 mergés** :
- **Lot I référence** (~30 min Desktop, ~0,50 $)
- **Lots Bench-1 à Bench-5** (~2-3h Desktop cumulé, ~3,00 $)

**Clôture sprint** :
- **Lot J — RAPPORT-CC-S2.9 + analyse comparative + arbitrage** (45 min - 1h Plateforme)
- **AskUserQuestion arbitrage final** (Blaise valide les optimisations à activer en production)

**Effort total estimé** : ~8-12h cumulé sur ~3-5 jours.

## 11. Vault post-S2.9 — projection

| Avant S2.9 (post-clôture S2.8) | Après S2.9 (cible) | Delta |
|---|---|---|
| 35 fichiers MD | 35 fichiers MD (patches R11 mineurs) | 0 fichier nouveau |
| ~444 chunks ChromaDB | ~444-450 chunks (delta R11 négligeable) | ~0-6 chunks |
| 104 std + 14 adv | 104 std + 14 adv (inchangé) | 0 |
| 103/104 + 14/14 score | 103/104 + 14/14 maintenu | Stabilité confirmée |
| 0 optimisations activées | 1-2 optimisations en production | Gain latence / coût mesurable |

**Optimisation cible production S2.9** : 1-2 retenues parmi les 5 benchmarkés, selon trade-off qualité/latence/coût.

---

*Brief produit le 26 mai 2026 par Cowork Hub IA Plateforme post-clôture S2.8 (103/104 std + 14/14 adv = robustesse confirmée mais vault 444 chunks au-dessus seuil 400). SPEC v2.3 en vigueur (produite Cowork-side simultanément). À transmettre par Blaise via sync ascendante après revue.*
