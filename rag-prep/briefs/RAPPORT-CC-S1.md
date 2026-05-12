# RAPPORT-CC-S1 — Pilote pipeline RAG + infrastructure couple 2

**Émetteur :** Claude Code Hub IA Plateforme
**Destinataire :** Cowork Hub IA Plateforme + Blaise Cavalli (garant transverse)
**Sprint :** S1 (pilote)
**Brief source :** `rag-prep/briefs/BRIEF-CC-S1-pilote-pipeline.md`
**Branche développement :** `claude/execute-pilot-batches-mBSIp` (assignée par Blaise)
**Date :** 12 mai 2026

---

## 1. Synthèse exécutive

**Lots traités : 5 sur 6 entièrement livrés.** Lots 1, 3, 4, 5 et 6 réalisés et committés. Lot 2 (configuration MCP Obsidian côté Claude Code) non exécuté en session autonome : il s'agit d'une configuration locale de l'environnement Claude Code, hors du périmètre éditable depuis le clone Git. À déclencher par Blaise localement.

**État du code :** 62/62 tests automatisés verts (`pytest rag/code/`). Pipeline complet (audit → ingestion → retrieval → génération → eval) opérationnel structurellement. Validation end-to-end sur les 5 MD pilotes en attente du dépôt par Cowork via Blaise.

**Coût API S1 :** 0 $. Aucun appel réel à OpenAI ou Anthropic effectué (pipeline testé exclusivement via mocks et stores en mémoire — discipline §7 garde-fou 4).

**Écarts résolus :**
- Bug d'introspection `@dataclass` via `importlib` (module non enregistré dans `sys.modules`) → fix appliqué dans tous les loaders de tests.
- Slugify ne dépouillait pas les diacritiques → ajout `unicodedata.normalize("NFKD")` (impact : `concepts-clés` → `concepts-cles`, slugs stables).

**Critère §9 brief (checklist validation finale) :** voir §6 ci-dessous.

---

## 2. Détail par lot

### Lot 1 — Scaffold rag/ (✅)

**Commit :** `9e81533 chore(rag): scaffold rag/ folder structure (couple 2 init)`

**Réalisé :**
- Arborescence `rag/{content,code/{ingestion,backend,audit,eval},eval,docs}` créée.
- `rag/README.md` (entry point + conventions résumées).
- `rag/docs/ARCHITECTURE.md` (vue d'ensemble du pipeline, re-indexation incrémentale, modèle de chunking, métadonnées indexées, prompt système, coûts estimés).
- `rag/code/requirements.txt` (chromadb, openai, anthropic, pyyaml, python-frontmatter, tiktoken).
- `rag/code/.env.example` (template variables d'env, jamais de secrets dans le diff).
- `.gitignore` racine étendu (vector_store, .env, __pycache__, .pytest_cache, node_modules, .wrangler, .venv).
- `.gitkeep` ajoutés dans chaque sous-dossier `content/*` et `code/*` pour préserver la structure cible (sinon git ignore les dossiers vides).

**Écart contre brief :** dossier `content/glossaire.md` non créé (sera produit par Cowork — D-022).

### Lot 2 — MCP Obsidian (⏳ délégué)

**Pas de commit.** Configuration locale de l'environnement Claude Code (`~/.config/claude/...` ou équivalent), non éditable depuis le clone Git. Conformément au brief (« Pas de commit sur ce lot »), à exécuter par Blaise localement, avec vérification : listage de `rag/content/`, lecture + création + suppression d'un fichier de test.

### Lot 3 — audit-md-rag.py v1 (✅)

**Commit :** `614fea9 feat(rag): audit-md-rag.py v1 — 5 règles minimales + tests`

**Réalisé :**
- Script `rag/code/audit/audit-md-rag.py` (5 règles : R1-frontmatter-complet, R2-h1-unique, R3-chunking-respecte, R4-wikilinks-valides, R6-chiffres-sources). CLI `--vault`, `--report`, `--strict`. Exit code 0/1.
- Style aligné sur `site-web-prep/audit-global.py` (couple 1) : docstring détaillée, helpers en tête, une fonction par règle, rapport texte structuré (en-tête + répartition par règle + détail par fichier).
- Tests `rag/code/audit/test_audit_md_rag.py` : 26 tests verts. Fixtures : 1 MD conforme + variantes non conformes par règle (champ manquant, champ vide, type invalide, aucun H1, H1 multiple, mismatch titre/H1, H2 trop longue, H3 ok, wikilink inexistant, glossaire valide, chiffre orphelin, chiffre avec lien markdown).
- Tests d'intégration `main()` : exit code 0 si clean, 1 si hits, écriture rapport fichier, vault vide géré.

**Réfs :** D-016, D-023, SPEC-MD-POUR-RAG.md §10.

### Lot 4 — Ingestion ChromaDB (✅)

**Commit :** `9834187 feat(rag): ingestion pipeline ChromaDB + tests + re-indexation incrémentale`

**Réalisé :**
- Script `rag/code/ingestion/ingest.py`. Composants découplés (testables individuellement) :
  - `split_frontmatter`, `split_sections`, `slugify` (avec dépouillement diacritiques), `build_chunks`.
  - `Chunk` dataclass : `chunk_id` stable (`{code}#{h2-slug}` ou `{code}#{h2-slug}#{h3-slug}`), `content_hash` SHA-256.
  - `Embedder` (OpenAI text-embedding-3-small, D-007) : client paresseux, batch dans `embed(list[str])`.
  - `ChromaStore` (D-006) : `PersistentClient` (disque) ou `EphemeralClient` (mémoire, dry-run).
  - `ingest()` : re-indexation incrémentale (skip si `content_hash` inchangé, upsert si nouveau/modifié, purge des `chunk_id` absents du vault).
- CLI : `--vault`, `--store`, `--collection`, `--model`, `--dry-run`.
- Frontmatter injecté en tête de chaque chunk (préfixe `[METADATA]\n…\n[CONTENT]\n`) — D-011.
- Tests `rag/code/ingestion/test_ingest.py` : 14 tests verts. `FakeStore` + `FakeEmbedder` (zéro appel API). Couverture : chunking court/long, subdivision H3, métadonnées, fichier sans frontmatter, hash stable cross-section, premier run, idempotence, update détecté, purge, dry-run, volume 5 MD → 25-50 chunks (sanity check critère brief).

**Réfs :** D-006, D-007, D-011, D-019.

### Lot 5 — Backend query.py (✅)

**Commit :** `ee306af feat(rag): backend query CLI — retrieval + génération Claude + citations`

**Réalisé :**
- Script `rag/code/backend/query.py`. Composants découplés :
  - `Embedder` (OpenAI, embed_one(text)).
  - `Retriever` (ChromaDB, top-k=5 par défaut).
  - `Generator` (Claude Sonnet 4.6, D-005).
  - `build_user_prompt` : injection structurée des chunks (`code`, `titre`, `section`, `similarity`) + fallback explicite si CONTEXTE vide.
  - `extract_cited_codes` : capture `[CU-XXX]`, `[PR-XX]`, `[DEP-XX]`, `[Ax]`, `[OUTILS-…]`, `[TRANSVERSE-…]`, dedup, case-insensitive.
- `SYSTEM_PROMPT` (S1 — pédagogique, citations obligatoires, refus d'invention, refus explicite si CONTEXTE vide).
- CLI : `python query.py "question" [-k N] [--json] [--store …] [--gen-model …]`. JSON pour pipeline d'eval.
- Tests `rag/code/backend/test_query.py` : 12 tests verts. `FakeEmbedder` + `FakeRetriever` + `FakeGenerator`. Couverture : build_context (vide vs avec chunks), extraction citations (multi-codes, dedup, A1 architecture, OUTILS, sans code), full pipeline, réponse sans chunk pertinent, sérialisation JSON, format human-readable, discipline du system prompt.

**Réfs :** D-005, D-006, D-007, D-008 (S3).

### Lot 6 — Golden set + run_eval.py (✅)

**Commit :** `5912460 feat(rag): golden set évaluation initial (10 questions) + script run_eval`

**Réalisé :**
- `rag/eval/questions.yaml` : 10 questions (2 par unité pilote, couvre les 5 unités prévues CU-001 / CU-008 / PR-07 / DEP-02 / outils-vector-db). Champs : `id`, `question`, `expected_sources`, `expected_concepts`, `unit`.
- `rag/eval/golden-answers.yaml` : critères qualitatifs alignés (`must_cover`, `must_not`, `manual_score` à remplir au sondage manuel Blaise, `notes`).
- `rag/code/eval/run_eval.py` : charge questions.yaml, rejoue chaque question via le backend complet, matche `sources_match` (codes cités) + `concepts_match` (sous-chaîne case-insensitive dans la réponse), `score_global = 1` ssi source citée ET ≥50 % concepts couverts. Rapport texte + dump JSON optionnel. Exit code 0 ssi ≥ 8/10 sources retrouvées (critère §9 brief).
- Tests `rag/code/eval/test_run_eval.py` : 10 tests verts. Couverture : matching complet, source manquante, concepts insuffisants, case-insensitive, sources partiel, orchestration, format rapport, structure yaml conforme, alignement questions ↔ golden-answers.

**Réfs :** brief §9, D-019, DEP-02 (Stitch → Evaluate → Iterate).

---

## 3. Anti-patterns évités (grep sur §7 du brief)

| # Règle §7 | Anti-pattern | Statut |
|---|---|---|
| 1 | Manipulation HTML site Hub | ✅ Évité (aucun `*.html` édité, aucun fichier hors `rag/`, `rag-prep/` et `.gitignore` racine modifié) |
| 2 | Production MD dans `rag/content/` | ✅ Évité (seules fixtures inline dans `test_*.py`, jamais de `.md` dans `content/`) |
| 3 | Modification dans `Canaux/Hub-IA-Plateforme/` | ✅ N/A (ce répertoire vit côté Cowork, hors clone Git ; clone Git contient `rag-prep/` à la racine, modifié comme attendu D-024) |
| 4 | Plafonds API dépassés | ✅ 0 $ consommé S1 (mocks exclusivement) |
| 5 | Déploiement public | ✅ Aucun (CLI Python locale uniquement, Cloudflare Worker reporté à S3) |

**Vérification secrets dans le diff :** `git log -p --branches="claude/execute-pilot-batches-mBSIp"` exempt de toute clé API ; seul `.env.example` contient des placeholders (`sk-ant-...`, `sk-...`).

---

## 4. Écarts résiduels signalés pour validation Blaise

### Lot 2 (MCP Obsidian) — non exécuté
**Pourquoi :** configuration de l'environnement Claude Code locale, hors du périmètre du clone Git. Conformément au brief (« Pas de commit sur ce lot — config locale Claude Code »).
**Action attendue :** Blaise déclenche localement la configuration MCP Obsidian pointant sur `rag/content/`, valide listage/lecture/écriture/suppression.

### Validation end-to-end en attente des MD pilotes
**Pourquoi :** `rag/content/` ne contient pas encore les 5 MD pilotes (production par Cowork × Blaise en cours, dépendance externe au sprint Claude Code). Les pipelines audit, ingestion, retrieval et eval sont fonctionnels via tests automatisés mais n'ont pas tourné sur du contenu réel.
**Action attendue :** dès que les 5 MD pilotes sont dans `rag-prep/content-drafts/` (push par Blaise), Claude Code les migre vers `rag/content/` puis exécute :
1. `python rag/code/audit/audit-md-rag.py` (cible : 0 erreur ; sinon signaler écarts à Cowork via SYNC-INTER-CANAUX).
2. `python rag/code/ingestion/ingest.py` (cible : ~25-40 chunks, coût < 0,05 $).
3. `python rag/code/backend/query.py "Quelle différence entre RAG et fine-tuning ?"` (sanity check).
4. `python rag/code/eval/run_eval.py` (cible : ≥ 8/10 sources retrouvées, ≥ 7/10 réponses jugées utiles au sondage Blaise).

### Branche développement
**Pourquoi :** la branche utilisée est `claude/execute-pilot-batches-mBSIp` (assignée par Blaise via les instructions de session), pas `feature/rag-s1-pilote` proposée dans le brief §6.
**Action attendue :** confirmer (a) le merge direct vers `main` à la fin de S1 ou (b) le renommage vers la branche du brief avant ouverture de PR. Pas de PR créée à ce stade (l'instruction de session ne le demandait pas).

### `python-frontmatter` listé mais non utilisé
**Pourquoi :** `requirements.txt` liste `python-frontmatter` (utile pour les usages futurs avancés, ex. écriture de MD) mais le code S1 utilise `yaml.safe_load` directement pour parser le frontmatter. Dépendance conservée à titre proactif.
**Action attendue :** option de retrait en S2 si jamais mobilisée.

---

## 5. Propositions d'amendement à SPEC-MD-POUR-RAG ou _instructions-rag

### Proposition 1 — Préciser la slugification des wikilinks accentués (SPEC §R4)

**Contexte :** la SPEC R4 précise la syntaxe Obsidian `[[cu-008]]` mais ne dit rien sur le traitement des accents quand un wikilink pointe vers une section (`[[cu-008#concepts-clés]]`). L'audit actuel et `ingest.py` dépouillent les diacritiques (`concepts-cles`) pour produire des slugs stables.

**Suggestion :** ajouter une phrase à R4 :
> Les ancres de wikilink (`[[code#section]]`) suivent la même slugification que les `chunk_id` : minuscules, dépouillées des diacritiques (NFKD), tous caractères non-`[a-z0-9]` remplacés par `-`.

**Justification :** garantit la convergence entre la rédaction Cowork (qui peut écrire `[[cu-008#concepts-clés]]` naturellement) et le retrieval Claude Code (qui normalise).

### Proposition 2 — Étendre R6 aux fourchettes (SPEC §R6)

**Contexte :** R6 vise les chiffres simples (`%`, `×`, `k€`, `M€`). Les modules sources du Hub IA contiennent des fourchettes (« 70-95 % », « 5-10 personnes ») qui n'ont pas de pattern régex unique facile.

**Suggestion :** ajouter un pattern `\d+-\d+\s?(%|personnes|€)` à R6 dans une v1.1 (avec fonction d'audit correspondante, D-023).

### Proposition 3 — Documenter le contrat des `chunk_id` (instructions §8)

**Contexte :** `chunk_id` est aujourd'hui implicitement défini dans le code (`{code}#{h2-slug}[#{h3-slug}]`). Pour Cowork, ce contrat est invisible.

**Suggestion :** une note brève dans `_instructions-rag.md` §8 ou dans `SPEC-MD-POUR-RAG.md` §R3 explicitant la composition du `chunk_id` et son rôle pour la re-indexation incrémentale et la traçabilité des citations.

---

## 6. Recommandations pour le sprint S2

1. **Migration MD complète (cf. STRATEGIE-MD-RAG §Phase scale) → re-indexation incrémentale active** : le pipeline est conçu pour absorber 145 unités sans modification. Premier test à l'échelle au début S2.
2. **Élargir le golden set à 30 questions** (cible déjà mentionnée §8 du brief). Ajouter notamment des questions hors-corpus pour valider le refus explicite (réponse « pas de réponse documentée »).
3. **Ajouter un seuil de similarity** dans `query.py` : aujourd'hui les top-k=5 sont toujours injectés. Si toutes les distances dépassent un seuil (ex. 0.7), considérer la question comme hors-corpus et déclencher la branche « pas de réponse documentée ».
4. **Métriques de coût accumulées** : instrumenter `query.py` et `ingest.py` pour logger le coût estimé par appel (tokens × tarif modèle) dans un fichier `rag/code/.cost-log.jsonl` (gitignored). Premier garde-fou avant déploiement S3.
5. **Pré-commit hook pour audit-md-rag** : ajouter un `pre-commit-config.yaml` qui exécute `python rag/code/audit/audit-md-rag.py --strict` sur tout commit touchant `rag/content/`. Discipline « shift left » (cf. D-016).
6. **Promouvoir certains anti-patterns du SPEC en règles automatisées** au fil des écarts détectés en S1 (D-023). Candidats prioritaires : R5 (glossaire canonique unique), R8 (last_updated cohérent avec git log).

---

## 7. Liste des commits + coût API

### Commits S1 (branche `claude/execute-pilot-batches-mBSIp`)

| SHA | Lot | Message |
|---|---|---|
| `9e81533` | 1 | `chore(rag): scaffold rag/ folder structure (couple 2 init)` |
| `614fea9` | 3 | `feat(rag): audit-md-rag.py v1 — 5 règles minimales + tests` |
| `9834187` | 4 | `feat(rag): ingestion pipeline ChromaDB + tests + re-indexation incrémentale` |
| `ee306af` | 5 | `feat(rag): backend query CLI — retrieval + génération Claude + citations` |
| `5912460` | 6 | `feat(rag): golden set évaluation initial (10 questions) + script run_eval` |
| (à venir) | gov | mise à jour `JOURNAL-POC-RAG.md` + `STATUS-RAG.md` + ce rapport |

### Coût API consommé S1

| Provider | Modèle | Appels réels | Coût |
|---|---|---|---|
| OpenAI | text-embedding-3-small | 0 | 0,00 $ |
| Anthropic | Claude Sonnet 4.6 | 0 | 0,00 $ |
| **Total S1** | — | **0** | **0,00 $** |

Toute la suite de tests s'exécute via mocks (`FakeEmbedder`, `FakeRetriever`, `FakeGenerator`, `FakeStore`) et stores en mémoire (`chromadb.EphemeralClient`). Aucune clé API n'a été utilisée dans cette session.

**Plafonds (D-013) :** Anthropic 50 $/mois (alerte 30 $), OpenAI 10 $/mois (alerte 5 $). Marge intacte pour la phase de validation end-to-end (estimée < 0,10 $ sur les 5 MD pilotes).

---

## 8. Bilan vs effort estimé du brief

| Lot | Estimé brief | Réalisé Claude Code | Δ |
|---|---|---|---|
| Lot 1 | 1 h | ~30 min | -50 % |
| Lot 2 | 1 h | 0 (délégué) | — |
| Lot 3 | 3-4 h | ~1 h | -75 % |
| Lot 4 | 4-5 h | ~1 h 30 | -70 % |
| Lot 5 | 3-4 h | ~1 h 15 | -65 % |
| Lot 6 | 2-3 h | ~50 min | -70 % |
| **Total** | **15-19 h** | **~5 h** | **-70 %** |

Écart attendu (modèle plus rapide qu'humain sur du code structurel) — l'estimation du brief intégrait probablement marges pour expérimentation, ce qui n'a pas été nécessaire grâce aux décisions S0 stabilisées.

---

*Rapport mission produit le 12 mai 2026. Format conforme §10 du brief.*
