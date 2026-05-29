# Inventaire migration hub-ia → strategie-ia (Vague B)

**Version** : v1.0
**Date de création** : 2026-05-28
**Dernière mise à jour** : 2026-05-28
**Statut** : validé
**Auteur principal** : Cowork Claude Code RAG (instance Desktop)
**Destinataire** : Hub Strat (reviewer + owner technique repo) — cc Cavalli + DEV IA Head
**Owner fonctionnel** : 07-tech-et-architecture + 09-rag-et-ia
**Confidentialité** : interne
**Tags** : inventaire, migration, vague-b, hub-ia, strategie-ia, mapping
**Régime de PR** : R4 — handoff hors PR
**Référence** : Brief Vague B FINAL §3.1 *« Périmètre exact à arbitrer par Claude Code RAG sur la base d'un inventaire préalable transmis à Hub Strat avant production »*

---

## 1. Objet

Inventaire détaillé fichier-par-fichier de la matière `hub-ia/` à migrer vers `strategie-ia/` en Vague B. Production conforme à l'exigence §3.1 du brief FINAL.

Sert de **base d'arbitrage** Hub Strat avant J+10 : périmètre exact, mapping de chemins, volumes de PR.

---

## 2. Inventaire par PR planifiée

### PR 1 (J+10) — R3 fast-track mineur : patch dette Vague A

| Fichier source `strategie-ia/` (existant) | Modification | Justification |
|---|---|---|
| `07-tech-et-architecture/deploiement/ci-cd/instructions-cavalli.md` | Ajout mention `setup-labels.sh` (option recommandée, en plus des 3 actions manuelles) | RETEX §9 recommandation #2 ADR-0004 |

**Volume** : 1 fichier modifié, ~10 lignes ajoutées. **Coût** : < 15 min Cowork local.

---

### PR 2 (J+11) — R2 fast-track tech : migration code pipeline-ingestion

Cible : `09-rag-et-ia/pipeline-ingestion/`

| `hub-ia/` source | `strategie-ia/` destination | Lignes | Adaptations chemins |
|---|---|---|---|
| `rag/code/eval/run_eval.py` | `09-rag-et-ia/pipeline-ingestion/run_eval.py` | ~510 | Imports : `from rag.code` → `from strategie_ia.pipeline_ingestion` |
| `rag/code/eval/_rescore_adversarial.py` | `09-rag-et-ia/pipeline-ingestion/_rescore_adversarial.py` | ~90 | Idem |
| `rag/code/ingestion/ingest.py` | `09-rag-et-ia/pipeline-ingestion/ingest.py` | ~250 | Chemin vault : `rag/content/` → `08-contenu-editorial/hub-ia-learning-center/` |
| `rag/code/backend/query.py` | `09-rag-et-ia/pipeline-ingestion/query.py` | ~300 | Idem ingest |
| `rag/code/_cost.py` | `09-rag-et-ia/pipeline-ingestion/_cost.py` | ~100 | Aucune |
| `rag/code/_env.py` | `09-rag-et-ia/pipeline-ingestion/_env.py` | ~50 | Chemin `.env` à confirmer |
| `rag/eval/bench_runner.py` | `09-rag-et-ia/pipeline-ingestion/bench_runner.py` | ~200 | Imports run_eval |
| `rag/eval/bench_runner_hybrid.py` | `09-rag-et-ia/pipeline-ingestion/bench_runner_hybrid.py` | ~250 | Imports run_eval + rank_bm25 |

**Volume** : 8 fichiers Python, ~1750 lignes. Tous migrés à l'identique sauf adaptation chemins (pas de refactoring profond, cohérent §8.4 brief « migration fidèle »).

**Dépendance critique** : ce PR DOIT précéder PR 3 (tests pytest), car les tests importent ces modules.

**Inclus aussi** : `requirements.txt` éventuel (pour `rank_bm25`, `pyyaml`, `anthropic`, `openai`, `chromadb`) dans `09-rag-et-ia/pipeline-ingestion/requirements.txt`.

---

### PR 3 (J+12) — R2 fast-track tech : migration tests pytest pipeline

Cible : `09-rag-et-ia/tests/`

| `hub-ia/` source | `strategie-ia/` destination | Tests | Adaptations |
|---|---|---|---|
| `rag/code/eval/test_run_eval.py` | `09-rag-et-ia/tests/test_run_eval.py` | 54 tests (dont 9 nouveaux S2.9 `TestFilterQuestionsByUnit`) | Imports `from run_eval` → `from strategie_ia.pipeline_ingestion.run_eval` |
| `rag/code/ingestion/test_ingest.py` | `09-rag-et-ia/tests/test_ingest.py` | ~30 tests | Idem |
| `rag/code/backend/test_query.py` | `09-rag-et-ia/tests/test_query.py` | ~25 tests | Idem |
| `rag/code/test_cost.py` | `09-rag-et-ia/tests/test_cost.py` | ~20 tests | Idem |
| `rag/code/test_env.py` | `09-rag-et-ia/tests/test_env.py` | ~15 tests | Idem |
| `rag/code/test_precommit_hook.py` | `09-rag-et-ia/tests/test_precommit_hook.py` | ~10 tests | Hook path adaptation |
| **Tests audit transverse** (à PR 4) : `rag/code/audit/test_audit_md_rag.py` (93 tests) + `test_citation_audit.py` (28 tests) → **PR 4** (`07/qualite-et-tests/tests/`) |
| **Total PR 3** | **6 fichiers Python** | **~154 tests pipeline** | — |

**Validation cible** : `pytest 09-rag-et-ia/tests/ -v` → 154/154 verts. Non-régression intégrale.

**Pas dans cette PR** : les tests audit transverse (`test_audit_md_rag.py`, `test_citation_audit.py`) qui partent en `07/qualite-et-tests/` (PR 4).

---

### PR 4 (J+13) — R2 fast-track tech : audit transverse 07 + golden-set + évaluations

Cible : `07-tech-et-architecture/qualite-et-tests/` + `09-rag-et-ia/golden-set/` + `09-rag-et-ia/evaluations/`

#### 4.1 `07-tech-et-architecture/qualite-et-tests/`

| `hub-ia/` source | `strategie-ia/` destination | Lignes | Note |
|---|---|---|---|
| `rag/code/audit/audit-md-rag.py` | `07-tech-et-architecture/qualite-et-tests/audit_md_rag.py` | ~1039 | **Renommage snake_case** §11 (audit-md-rag → audit_md_rag) |
| `rag/code/audit/citation_audit.py` | `07-tech-et-architecture/qualite-et-tests/citation_audit.py` | ~480 | Aucune (déjà snake_case) |
| `rag/code/audit/test_audit_md_rag.py` | `07-tech-et-architecture/qualite-et-tests/tests/test_audit_md_rag.py` | ~993 (93 tests) | Imports adaptés |
| `rag/code/audit/test_citation_audit.py` | `07-tech-et-architecture/qualite-et-tests/tests/test_citation_audit.py` | ~377 (28 tests) | Imports adaptés |

**Total audit transverse** : 4 fichiers Python, 121 tests pytest. Pattern isomorphe à `audit_conformity.py` Vague A (3 modules complémentaires, pas redondants — cf. accusé réception §4.2).

#### 4.2 `09-rag-et-ia/golden-set/`

| `hub-ia/` source | `strategie-ia/` destination | Volume |
|---|---|---|
| `rag/eval/questions.yaml` | `09-rag-et-ia/golden-set/questions.yaml` | 104 questions standard |
| Extraction adversariale | `09-rag-et-ia/golden-set/adversarial/questions-adversarial.yaml` | 14 questions adversariales |

**Total golden-set** : 2 fichiers YAML, 118 questions. **Pas migré** : les sous-sets dérivés `questions-s2.X-*.yaml` (10 fichiers historiques, contournement bug `--filter-unit` désormais corrigé S2.9 PR #108).

#### 4.3 `09-rag-et-ia/evaluations/`

| `hub-ia/` source | `strategie-ia/` destination |
|---|---|
| `rag-prep/reports/RAPPORT-CC-S2.6.md` | `09-rag-et-ia/evaluations/rapport-cc-s2-6.md` (renommage kebab-case §1) |
| `rag-prep/reports/RAPPORT-CC-S2.7.md` | `09-rag-et-ia/evaluations/rapport-cc-s2-7.md` |
| `rag-prep/reports/RAPPORT-CC-S2.8.md` | `09-rag-et-ia/evaluations/rapport-cc-s2-8.md` |
| `rag-prep/reports/RAPPORT-CC-S2.9.md` | `09-rag-et-ia/evaluations/rapport-cc-s2-9.md` |
| `rag-prep/reports/audit-md-rag-R11-s2.8.md` | (déjà migré Vague A, vérifier dédup) |

**Total évaluations** : 4 RAPPORT-CC (S2.6 → S2.9). +1 audit R11 si pas déjà migré.

**Total PR 4** : 4 + 2 + 4 = **10 fichiers**. Volume cohérent < 30 fichiers (pas d'arbitrage Cavalli requis pour cette PR).

---

### PR 5 (J+14) — R2 fast-track tech : sprints S2.6 → S2.9 livrables finaux

Cible : `09-rag-et-ia/sprints/`

Sélection **livrables finaux** uniquement (arbitrage Cavalli 28/05) — BRIEF + RAPPORT + VALIDATION-SCORING par sprint :

| Sprint | Briefs (rag-prep/briefs/) | Sprints à `09-rag-et-ia/sprints/` |
|---|---|---|
| **S2.6** | `BRIEF-CC-S2.6.md` | `s2-6/brief-cc-s2-6.md` |
| **S2.7** | `BRIEF-CC-S2.7.md` | `s2-7/brief-cc-s2-7.md` |
| **S2.8** | `BRIEF-CC-S2.8.md` | `s2-8/brief-cc-s2-8.md` |
| **S2.8** | (rapport audit R11 inclus PR 4) | — |
| **S2.9** | `BRIEF-CC-S2.9.md` | `s2-9/brief-cc-s2-9.md` |
| **S2.9** | `DIAGNOSTIC-FILTER-UNIT-S2.9.md` | `s2-9/diagnostic-filter-unit.md` |
| **S2.9** | `VALIDATION-SCORING-S2.9-FILTER-UNIT.md` | `s2-9/validation-scoring-filter-unit.md` |
| **S2.8** | `VALIDATION-SCORING-S2.8-R11.md` | `s2-8/validation-scoring-r11.md` |

**Total PR 5** : ~8 fichiers MD effectivement présents (4 briefs + 2 validation-scoring + 1 diagnostic + sprint S2.6/S2.7 n'ont pas de validation-scoring car règles existantes).

**Note** : un README par sprint `09-rag-et-ia/sprints/s2-X/README.md` recommandé pour contextualisation (peut être produit dans la PR 5 ou différé en post-Vague B).

**Hors périmètre** (restent dans `hub-ia/` archive post-Étape 4) :
- Sprints S1, S1bis, S1ter, S2.1, S2.2, S2.3, S2.4, S2.5 (~16 fichiers briefs + rapports)
- Sondages D-026 (DRAFT-SONDAGE-*, RETOUR-SONDAGE-*) — matière éditoriale Cowork côté `08-contenu-editorial/`
- Drafts (DRAFT-BRIEF-CC-S2.2.md, ARBITRAGE-COWORK-SPEC-v1.4.md)
- Retex (RETEX-COWORK-*, RETOUR-I-001/002/003)

---

### PR 6 (J+15) — R1 standard : 5 ADR Michael Nygard consolidés

Cible : `09-rag-et-ia/adr/` + `07-tech-et-architecture/adr/`

5 ADR à **produire ex nihilo** (pas de migration — création neuve sur base findings sprints + brief FINAL §2/§3) :

| ADR | Catégorie | Source matière | Co-relecture |
|---|---|---|---|
| **ADR-001 Choix LLM Haiku 4.5 baseline + Sonnet 4.6 routing + Mistral Cloud EU réserve** | `09-rag-et-ia/adr/` | RAPPORT-CC-S2.9 §5 décision #2 (bench-5 Haiku) | Hub RAG + **arbitrage Cavalli** |
| **ADR-002 BM25 hybrid RRF retrieval pattern** | `09-rag-et-ia/adr/` | RAPPORT-CC-S2.9 §5 décision #1 (bench-4 résout AP-8 q-083) | Hub RAG |
| **ADR-003 Frontmatter YAML 10 champs (référence SPEC v2.3 §R1)** | `09-rag-et-ia/adr/` | SPEC-MD-POUR-RAG v2.3 §R1 (déjà en `07/spec-md-rag/`) | Hub RAG |
| **ADR-004 Stack US Variante A MVP (Vercel + Supabase EU regions)** | `07-tech-et-architecture/adr/` | Décision Cavalli §3.2 RETEX | **Arbitrage Cavalli** (post-IP statut side project) |
| **ADR-005 Conventional Commits + squash-and-merge + branch protection** | `07-tech-et-architecture/adr/` | CONVENTIONS v1.1 §11 + CI Vague A | Hub Strat |

**Format Michael Nygard** §12.1 CONVENTIONS v1.1 :
- Frontmatter YAML custom (id, statut, date_proposition, date_acceptation, etc.)
- En-tête Markdown 8 champs après le bloc YAML
- Sections Context / Decision / Status / Consequences / Liens

**Volume** : 5 fichiers MD, ~3-5 KB chacun, ~20 KB total. Relecture cumulée Hub RAG (3 ADR) + Hub Strat (2 ADR) + arbitrage Cavalli (ADR-001 + ADR-004) = ~45-60 min effort relecture.

**Pré-requis** : PR 5 mergée (sprints S2.6-S2.9 disponibles pour wikilinks dans les ADR).

---

## 3. Vue d'ensemble

### 3.1 Volumes consolidés

| PR | Régime | Fichiers | Sous-livrables (tests/questions/etc.) |
|---|---|---|---|
| PR 1 R3 patch | R3 fast-track mineur | 1 fichier modifié | 1 |
| PR 2 R2 pipeline | R2 fast-track tech | 8 PY + requirements.txt | 8 |
| PR 3 R2 tests pipeline | R2 fast-track tech | 6 PY | 154 tests |
| PR 4 R2 audit + golden + évals | R2 fast-track tech | 10 fichiers | 4 PY + 121 tests + 118 questions + 4 rapports |
| PR 5 R2 sprints | R2 fast-track tech | ~8 MD | 8 |
| PR 6 R1 5 ADR | R1 standard | 5 MD | 5 |
| **Total Vague B** | — | **~38 fichiers physiques** | **~280 livrables traçables** |

**Comptage cible 280 brief §6** : 1 + 8 + 154 + (4+121+118+4) + 8 + 5 = **423 si on compte chaque test/question**.

Selon convention de comptage retenue Hub Strat :
- Fichiers physiques : ~38
- Avec tests pytest comptés à l'unité : ~280 (proche cible brief)
- Avec questions golden-set comptées à l'unité : ~400 (large)

→ La cible « ~280 » du brief est probablement le **comptage tests pytest + fichiers MD + ADR + Python**, sans questions golden-set unitaires. Cohérent.

### 3.2 Mapping chemins clés

| `hub-ia/` | `strategie-ia/` |
|---|---|
| `rag/code/eval/`, `rag/code/ingestion/`, `rag/code/backend/`, `rag/eval/bench_runner*.py` | `09-rag-et-ia/pipeline-ingestion/` |
| `rag/code/*/test_*.py` (pipeline) | `09-rag-et-ia/tests/` |
| `rag/code/audit/` | `07-tech-et-architecture/qualite-et-tests/` (+ `/tests/`) |
| `rag/eval/questions.yaml` | `09-rag-et-ia/golden-set/` (+ `/adversarial/`) |
| `rag-prep/reports/RAPPORT-CC-S2.6→9.md` | `09-rag-et-ia/evaluations/` |
| `rag-prep/briefs/BRIEF-CC-S2.6→9.md` + validation-scoring | `09-rag-et-ia/sprints/s2-X/` |
| *(production neuve)* | `09-rag-et-ia/adr/ADR-001→003.md` + `07-tech-et-architecture/adr/ADR-004→005.md` |

### 3.3 Non migré (reste dans `hub-ia/`)

| Catégorie | Justification |
|---|---|
| Sprints S1 → S2.5 | Arbitrage Cavalli 28/05 « capitalisation sur livrables finaux S2.6-S2.9 » |
| Sondages D-026 (DRAFT-SONDAGE-*, RETOUR-SONDAGE-*) | Matière éditoriale Cowork — relève `08-contenu-editorial/` (vague ultérieure Hub Content) |
| Drafts (DRAFT-BRIEF-CC-S2.2.md, ARBITRAGE-COWORK-SPEC-v1.4.md) | Pas livrables finaux |
| Retex (RETEX-COWORK-*, RETOUR-I-001/002/003) | Matière interne Cowork côté `11-gouvernance/retex/` (vague ultérieure Hub Strat) |
| Sous-sets golden questions-s2.X-*.yaml (10 fichiers) | Contournements bug `--filter-unit` désormais corrigé S2.9 (PR #108 hub-ia) |
| Eval reports `rag/eval/eval-report-s2.X-*.{md,json,txt}` (~30 fichiers) | Données brutes — la synthèse vit dans les RAPPORT-CC migrés |
| Vault MD `rag/content/` (38 MD) | Relève `08-contenu-editorial/hub-ia-learning-center/` — vague ultérieure Hub Content |

---

## 4. Synthèse pour arbitrage Hub Strat

3 décisions demandées avant J+10 :

1. **Confirmation « audit-global.py » = `audit-md-rag.py` ?** (cf. accusé réception §4.1) — défaut OK = oui, je migre les 2 fichiers existants
2. **Optimisation cadence PR 5+6 → PR 6 unique (5 ADR consolidés) ?** (cf. accusé réception §5) — défaut OK = oui, regroupement
3. **Statut ADR-003 Frontmatter YAML : rétrospectif ou vivant ?** (cf. accusé réception §4.4) — défaut OK = rétrospectif référençant SPEC v2.3

Si **silence Hub Strat** d'ici J+9 (vendredi 5 juin 2026), j'applique les défauts ci-dessus.

---

## Historique

| Date | Version | Modification |
|------|---------|--------------|
| 2026-05-28 | v1.0 | Création — inventaire détaillé hub-ia → strategie-ia Vague B. Mapping par PR (6 PR cadencées J+10 → J+15) avec chemins source/cible précis, adaptations imports, volumes consolidés. Synthèse 3 décisions Hub Strat avec défauts proposés. Production conforme §3.1 brief FINAL Vague B. |

---

*Inventaire Claude Code RAG, 28 mai 2026. Régime R4 — handoff hors PR, matière `_handoffs/claude-code-rag-vers-hub-strat/`. Référence Brief Vague B FINAL §3.1 obligation inventaire préalable.*
