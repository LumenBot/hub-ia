# BRIEF-CC-S1 — Pilote pipeline RAG + infrastructure couple 2

**Émetteur :** Cowork Hub IA Plateforme
**Destinataire :** Claude Code Hub IA Plateforme (premier brief — canal à créer par Blaise)
**Garant transverse :** Blaise Cavalli
**Sprint :** S1 (pilote)
**Statut :** v1 (à transmettre par Blaise)

---

## 1. Métadonnées

- **Repo cible :** `hub-ia` (branche `main`)
- **Auteur du brief :** Cowork Hub IA Plateforme
- **Sprint précédent :** S0 cadrage (consolidé dans `Canaux/Hub-IA-Plateforme/_instructions-rag.md` v1)
- **Nature de l'itération :** mise en place de l'infrastructure RAG (setup + audit + premier pipeline) en parallèle de la production des 5 fichiers MD pilotes côté Cowork

---

## 2. Contexte court

Le canal Cowork Hub IA Plateforme (en parallèle de toi) produit en S1 les 5 fichiers MD pilotes du vault RAG (CU-001, CU-008, PR-07, DEP-02, outils-vector-db). Tu interviens pour : **(a)** initialiser l'infrastructure technique du dossier `rag/` dans le repo `hub-ia`, **(b)** créer le script `audit-md-rag.py` qui valide la conformité des MD à `SPEC-MD-POUR-RAG.md` v1, **(c)** mettre en place le premier pipeline d'ingestion ChromaDB sur les 5 unités pilotes, **(d)** activer un retrieval + génération basique avec Claude Sonnet 4.6 pour valider l'architecture end-to-end.

À la fin de S1, le système doit pouvoir répondre à 5-10 questions types sur les 5 unités pilotes, avec citations sources. Pas de widget public à ce stade (livrable S3).

---

## 3. Préalable obligatoire (lectures avant code)

**Tous les fichiers de référence du couple 2 vivent dans le dossier `rag-prep/` à la racine du clone Git `hub-ia`**. Lecture obligatoire dans cet ordre :

1. `rag-prep/_instructions-rag.md` v1 — référentiel complet, notamment §8 sur l'architecture de circulation Cowork ↔ Git ↔ Claude Code (D-024)
2. `rag-prep/DECISIONS-RAG.md` — registre des décisions actées D-001 à D-024
3. `rag-prep/SPEC-MD-POUR-RAG.md` v1 — cahier des charges des fichiers MD que tu vas indexer
4. `rag-prep/STRATEGIE-MD-RAG.md` — méthodologie de retranscription (pour comprendre la nature des MD que tu reçois)
5. `rag-prep/STATUS-RAG.md` — état actuel
6. `rag-prep/cartographie-rag.md` — inventaire angles thématiques
7. `rag-prep/SYNC-INTER-CANAUX.md` — coordination couple 1 ↔ couple 2
8. `rag-prep/briefs/RETEX-COWORK-HUB-IA-vers-PLATEFORME.md` — RetEx du couple 1, source de plusieurs décisions du couple 2 (utile pour comprendre les invariants)

**Audit de départ obligatoire** : `git fetch && git status` sur `hub-ia` (procédure de resync D-018). Si désynchro → `git reset --hard origin/main` après confirmation Blaise.

**Convention de circulation à respecter (D-024)** : tu écris tes mises à jour des fichiers vivants (`JOURNAL-POC-RAG.md`, `STATUS-RAG.md`, `RAPPORT-CC-S1.md`) directement dans `rag-prep/` du clone Git, puis tu commits et tu pushes. Cowork ne modifie jamais ton clone Git. Pas de risque de conflit Git de ton côté tant que tu respectes cette discipline.

---

## 4. Méthode — 6 lots dans l'ordre

### Lot 1 — Initialisation infrastructure repo `rag/`

**Livrable** : structure de dossiers créée et committée :
```
rag/
├── content/                      ← vault Obsidian (les 5 MD pilotes y seront déposés par Cowork via rag-prep/, voir note ci-dessous)
│   ├── modules/
│   ├── prealables/
│   ├── deploiement/
│   ├── architectures/
│   ├── ressources/
│   ├── transverses/
│   └── (glossaire.md sera produit par Cowork)
├── code/
│   ├── ingestion/                ← script d'indexation ChromaDB
│   ├── backend/                  ← Cloudflare Worker (TS) + CLI Python S1
│   ├── audit/                    ← audit-md-rag.py
│   └── eval/                     ← script run_eval.py
├── eval/
│   ├── questions.yaml            ← golden set initial (10 questions)
│   └── golden-answers.yaml       ← réponses attendues
├── docs/                         ← documentation technique du code RAG (créée à ta main, contenu à ta discrétion)
└── README.md                     ← documentation interne brève
```

**Note sur `rag/docs/`** : ce dossier est créé par toi en Lot 1 et hébergera la documentation technique que tu juges utile à côté de ton code (README architecture, schéma de flux, dépendances Python, comment lancer en local). Il ne duplique pas les conventions de gouvernance qui vivent dans `rag-prep/` (source de vérité unique).

**Note sur le `.gitignore`** : à étendre dans le `.gitignore` racine du repo `hub-ia` (pas un nouveau fichier `.gitignore.rag`) pour exclure : `rag/code/.env`, `rag/code/**/__pycache__/`, `rag/code/**/.pytest_cache/`, `rag/code/vector_store/` (storage local ChromaDB), `rag/code/node_modules/`, `rag/code/.wrangler/` (cache Cloudflare Workers).

**Note sur la circulation des MD pilotes** (D-024) : les 5 MD pilotes seront produits par Cowork dans son dossier de travail Cowork-side, puis copiés par Blaise vers `rag-prep/content-drafts/` du clone Git, puis migrés par toi dans `rag/content/` (les MD validés vivent dans `rag/`, pas dans `rag-prep/`). À détailler dans le brief S1.5 ou directement dans ce lot une fois la première vague de MD pilotes prête.

**Critères de succès** : structure créée, `.gitignore` racine du repo `hub-ia` étendu.

**Commit attendu** : `chore(rag): scaffold rag/ folder structure (couple 2 init)`.

---

### Lot 2 — Configuration MCP Obsidian côté Claude Code

**Livrable** : MCP Obsidian configuré et fonctionnel pointant sur `rag/content/`. Vérification : tu peux lister les fichiers du vault, lire un fichier MD, en créer un de test (puis le supprimer).

**Critères de succès** : pas d'erreurs au démarrage MCP, opérations basiques de lecture/écriture validées.

**Pas de commit** sur ce lot (config locale Claude Code).

---

### Lot 3 — Script `audit-md-rag.py` v1 (5 règles)

**Livrable** : script Python dans `rag/code/audit/audit-md-rag.py` qui parcourt tous les fichiers `.md` du vault et applique les 5 règles minimales définies en §10 de `SPEC-MD-POUR-RAG.md` :
- R1-frontmatter-complet
- R2-h1-unique
- R3-chunking-respecte
- R4-wikilinks-valides
- R6-chiffres-sources

**Sortie** : rapport texte structuré (un fichier par défaut détecté + total). Format aligné sur le style `audit-global.py` du couple 1 (référence : `Canaux/Hub-IA/repo-current/site-web-prep/audit-global.py`). Exit code non-zéro si erreur détectée.

**Test associé** (D-022, tests automatisés) : `rag/code/audit/test_audit_md_rag.py` avec au moins 2 fixtures MD (un conforme + un non conforme) et assertions sur chaque règle.

**Commit attendu** : `feat(rag): audit-md-rag.py v1 — 5 règles minimales + tests`.

---

### Lot 4 — Pipeline d'ingestion ChromaDB

**Livrable** : script `rag/code/ingestion/ingest.py` qui :
1. Parcourt `rag/content/**/*.md`
2. Parse le frontmatter YAML
3. Découpe chaque fichier en chunks selon D-011 (section H2 = chunk, frontmatter injecté en tête, subdivision H3 si > 800 tokens)
4. Calcule les embeddings via OpenAI text-embedding-3-small (D-007)
5. Insère dans ChromaDB local (`rag/code/vector_store/`) avec métadonnées (code, type, axe, niveau, tags, version, public_cible, source_file, chunk_id)
6. Supporte re-indexation incrémentale (skip si chunk inchangé, basé sur hash du contenu + version frontmatter)

**Test associé** : `rag/code/ingestion/test_ingest.py` avec un mini-vault de 2 fichiers MD de test, vérifiant que les chunks sont correctement créés et que la re-indexation incrémentale détecte les modifications.

**Critère de succès** : ingestion des 5 unités pilotes produit ~25-40 chunks indexés sans erreur. Coût estimé < 0,05 $.

**Commit attendu** : `feat(rag): ingestion pipeline ChromaDB + tests + re-indexation incrémentale`.

---

### Lot 5 — Backend retrieval + génération (script CLI)

**Livrable** : script `rag/code/backend/query.py` (CLI Python pour S1, le portage Cloudflare Worker viendra en S3) qui :
1. Reçoit une question en CLI (`python query.py "Quelle différence entre RAG et fine-tuning ?"`)
2. Calcule l'embedding de la question (OpenAI)
3. Retrieval top-k=5 dans ChromaDB
4. Construction du contexte (chunks retrouvés + métadonnées)
5. Appel API Claude Sonnet 4.6 (D-005) avec system prompt structuré (à concevoir : pédagogique, citant les sources, respectant le ton Hub IA)
6. Retourne la réponse + les codes sources citées

**Test associé** : `rag/code/backend/test_query.py` qui mocke les appels API et valide la structure du flow.

**Critère de succès** : le script répond à 5-10 questions types avec citations sources, en moins de 5 secondes par question.

**Commit attendu** : `feat(rag): backend query CLI — retrieval + génération Claude + citations`.

---

### Lot 6 — Golden set d'évaluation initiale (10 questions)

**Livrable** : fichier `rag/eval/questions.yaml` avec 10 questions types pour les 5 unités pilotes (2 questions par unité environ). Format :
```yaml
- id: q-001
  question: "Quelle est la différence entre RAG et fine-tuning ?"
  expected_sources: [cu-008]
  expected_concepts: [retrieval, citation-sources, mise-a-jour]
- id: q-002
  ...
```

Fichier `rag/eval/golden-answers.yaml` avec les réponses attendues (texte ou critères qualitatifs).

Script `rag/code/eval/run_eval.py` qui rejoue les questions et produit un rapport de matching (sources citées correspondent aux `expected_sources` ? concepts attendus présents ?).

**Critère de succès** : 8/10 questions ont les sources attendues citées, au moins 7/10 ont une réponse jugée utile par sondage manuel de Blaise.

**Commit attendu** : `feat(rag): golden set évaluation initial (10 questions) + script run_eval`.

---

## 5. Estimation effort consolidée

| Lot | Effort estimé Claude Code |
|---|---|
| Lot 1 | 1 h |
| Lot 2 | 1 h (config + tests basiques) |
| Lot 3 | 3-4 h (script + tests + alignement style audit-global.py couple 1) |
| Lot 4 | 4-5 h (ingestion + chunking + incrémental + tests) |
| Lot 5 | 3-4 h (CLI + retrieval + prompt + tests) |
| Lot 6 | 2-3 h (golden set + script eval) |
| **Total** | **~15-19 h Claude Code** |

À étaler sur le sprint S1 (3 semaines). Pas de date d'échéance interne (D-020). Rythme selon disponibilité Blaise et limites d'usage modèle.

---

## 6. Workflow recommandé

1. **Branche dédiée** : `feature/rag-s1-pilote` créée depuis `main`
2. **Ordre des lots** : 1 → 2 → 3 → 4 → 5 → 6 (dépendances strictes : 4 dépend du vault rempli par Cowork — coordination via Blaise pour le timing ; 5 dépend de 4)
3. **Commits granulaires** par lot (pas un seul commit final)
4. **PR vers main** à la fin du Lot 6, avec rapport mission consolidé (voir §9)
5. **Audit-md-rag** : à exécuter sur le vault après chaque ajout de fichier MD par Cowork ; signaler tout écart à Blaise

---

## 7. Règles de prudence en exécution autonome

1. **Pas de manipulation des fichiers HTML du site Hub IA** sous quelque prétexte que ce soit (D-022, spécialisation des rôles). Si un besoin apparaît → blocker, signalement à Blaise.
2. **Pas de production de fichiers MD du vault `rag/content/`** : c'est le rôle de Cowork (D-022). Tu peux créer des fichiers MD de test pour `test_*.py`, jamais dans `content/`.
3. **Pas de modifications dans `Canaux/Hub-IA-Plateforme/`** (registres du couple 2) : tu peux les **lire** mais pas les éditer (sauf `JOURNAL-POC-RAG.md`, `STATUS-RAG.md`, et `briefs/RAPPORT-CC-S1.md` pour ton rapport mission).
4. **Plafonds API** : monitorer le coût accumulé. Si > 30 $ Anthropic ou > 5 $ OpenAI atteints → signalement immédiat à Blaise.
5. **Pas de déploiement public** en S1 : tout reste local sur ton environnement. Le backend Cloudflare Worker arrive en S3.

---

## 8. Décisions explicites de NE PAS faire dans ce sprint

1. ❌ Pas de widget HTML/JS embarqué dans le Hub (livrable S3)
2. ❌ Pas de backend Cloudflare Worker déployé (livrable S3, on reste en CLI Python en S1)
3. ❌ Pas de capture feedback Supabase (livrable S3)
4. ❌ Pas de portage TypeScript du backend (S3)
5. ❌ Pas de gestion d'utilisateurs / authentification
6. ❌ Pas d'optimisation prématurée des prompts ou du chunking — les apprentissages du pilote serviront à ajuster en S2 (boucle Stitch → Evaluate → Iterate)
7. ❌ Pas d'extension du golden set au-delà de 10 questions (extension en S2 vers 30 questions)

---

## 9. Validation finale avant PR

Checklist à exécuter avant ouverture de PR :

- [ ] `audit-md-rag.py` exécuté sur les 5 unités pilotes → 0 erreur
- [ ] Tous les tests automatisés passent (`pytest rag/code/`)
- [ ] Pipeline d'ingestion testé sur les 5 unités → ~25-40 chunks indexés
- [ ] Script `query.py` répond aux 10 questions du golden set
- [ ] `run_eval.py` produit un rapport ≥ 8/10 sources attendues citées
- [ ] Coût accumulé < 5 $ (Anthropic + OpenAI cumulés)
- [ ] Rapport mission `briefs/RAPPORT-CC-S1.md` produit (format §10)
- [ ] `JOURNAL-POC-RAG.md` mis à jour (append session(s) Claude Code S1)
- [ ] `STATUS-RAG.md` mis à jour (sprint S1 fait, sprint S2 prêt)
- [ ] Aucun secret (clé API) dans le diff

---

## 10. Format du rapport mission (référence canonique couple 1)

Fichier `rag-prep/briefs/RAPPORT-CC-S1.md` à produire dans le clone Git (qui sera commit + push à la fin du sprint), structure inspirée du modèle couple 1 (RetEx Q1) :

1. **Synthèse exécutive** : lots traités, principaux écarts résolus
2. **Détail par lot** (avec extraits commits, résultats audit, métriques)
3. **Anti-patterns évités** : grep final sur les règles de prudence §7
4. **Écarts résiduels signalés pour validation Blaise**
5. **Propositions d'amendement à `SPEC-MD-POUR-RAG.md` ou `_instructions-rag.md`** (apprentissages du pilote)
6. **Recommandations pour le sprint S2**
7. **Liste des commits** + coût API accumulé

---

## 11. Fichiers de référence et contact

**Référentiels du couple 2** (tous dans `rag-prep/` du clone Git `hub-ia`) :
- `rag-prep/_instructions-rag.md` v1 — référentiel complet
- `rag-prep/DECISIONS-RAG.md` — 24 décisions actées
- `rag-prep/STRATEGIE-MD-RAG.md` v1 — méthodologie
- `rag-prep/SPEC-MD-POUR-RAG.md` v1 — format MD (8 règles)
- `rag-prep/cartographie-rag.md` v0 — angles thématiques
- `rag-prep/STATUS-RAG.md` — état sprint
- `rag-prep/JOURNAL-POC-RAG.md` — journal continu
- `rag-prep/SYNC-INTER-CANAUX.md` — coordination inter-canaux
- `rag-prep/briefs/RETEX-COWORK-HUB-IA-vers-PLATEFORME.md` — RetEx couple 1

**Référentiel du couple 1 à connaître** (pour alignement éditorial sur les chunks que tu indexes) :
- `site-web-prep/RULES-IMPLEMENTATION-v1.6.md` dès que mergé (refonte simplifiée 13 règles en 11 dimensions A.1 à K.1, plus lisible). En transition, `site-web-prep/RULES-IMPLEMENTATION.md` v1.5.14 reste opposable jusqu'au merge de la branche `refactor/rules-v1.6-consolidation` côté couple 1.
- `site-web-prep/audit-global.py` (référence de style pour `rag/code/audit/audit-md-rag.py` — alignement structurel avec les 13 règles automatisées listées dans v1.6 §3)

**Contact** : Blaise Cavalli (garant transverse). Toute question, blocker, ou écart par rapport au brief remonte via lui.

---

*Brief produit le 11 mai 2026. Volume : ~1900 mots (dans la cible D-021 ~2000 mots).*
