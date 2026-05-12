# BRIEF-CC-S1ter — Validation end-to-end avec clés API (clôture définitive S1)

**Émetteur :** Cowork Hub IA Plateforme
**Destinataire :** Claude Code Hub IA Plateforme
**Garant transverse :** Blaise Cavalli
**Sprint :** S1ter (clôture définitive S1 + S1bis)
**Branche cible :** convention D-027 (nouvelle branche `claude/execute-…` créée automatiquement par l'outillage)
**Statut :** v1, à transmettre

---

## 1. Métadonnées

- **Repo cible :** `hub-ia` (partir de `main` post-merge des PR #42 et PR `feature/post-s1bis-spec-v1.3-d028-d029`)
- **Auteur du brief :** Cowork Hub IA Plateforme
- **Sprint précédent :** S1bis (Lot S1b.1 livré, Lots S1b.2 + S1b.3 en pause faute de clés API)
- **Nature de l'itération :** ajout `python-dotenv` au code + reprise S1b.2 (validation end-to-end réelle avec ingestion + retrieval + génération + eval)

---

## 2. Contexte court

S1bis a livré Lot S1b.1 (audit-md-rag sur vault réel : 150 écarts bruts, 0 violation éditoriale claire après classification). S1b.2 et S1b.3 ont été mis en pause faute de `OPENAI_API_KEY` et `ANTHROPIC_API_KEY` dans la session. RAPPORT-CC-S1bis produit en marquant explicitement S1b.2 non exécuté.

**Évolutions depuis :**
- Blaise a créé les clés API et les a positionnées dans `rag/code/.env` (gitignored)
- Crédits disponibles : ~3 $ Anthropic + ~5 $ OpenAI sans renouvellement automatique → **discipline budgétaire serrée**
- SPEC bumpée v1.2 → v1.3 (exception R1 glossaire + politique whitelist wikilinks futurs)
- 2 nouvelles décisions actées : **D-028** (exception R1 fichiers racines transverses), **D-029** (whitelist wikilinks futurs)
- `chiffres-macro-2026.md` étendu à 16 chiffres (ajout 4e canonisation : « 90 % cas PME où le RAG bat le fine-tuning »)
- `whitelist-wikilinks-futurs.md` produit (69 codes whitelistés couvrant vagues 3 à 5)
- `glossaire.md` v3.8.4 et `cu-008.md` v3.8.5 refactorés pour wikilinker le 90 %
- Item descendant **I-D-002** ouvert vers couple 1 (sources primaires manquantes sur heuristiques techniques DEP-02 HTML)

---

## 3. Préalable obligatoire (lectures avant exécution)

À lire dans cet ordre, intégralement :

1. **Tes 2 rapports mission précédents** : `rag-prep/briefs/RAPPORT-CC-S1.md` + `rag-prep/briefs/RAPPORT-CC-S1bis.md` (contexte de tes 7 commits + écarts signalés)
2. `rag-prep/_instructions-rag.md` v1 — référentiel complet (§8 architecture de circulation D-024)
3. `rag-prep/DECISIONS-RAG.md` — registre actualisé (29 décisions actées, dont D-028 et D-029 nouvelles)
4. `rag-prep/SPEC-MD-POUR-RAG.md` v1.3 — cahier des charges actualisé (exception R1 + politique whitelist)
5. `rag-prep/whitelist-wikilinks-futurs.md` — nouveau (69 codes whitelistés)
6. `rag-prep/STATUS-RAG.md` — état sprint actuel (L1.19 fait, L1.20-L1.23 anticipés)
7. `rag-prep/cartographie-rag.md` — 9 entrées de vault à jour
8. `rag/eval/audit-report-s1bis.md` — pour contexte sur les écarts à NE PAS corriger ici

**Audit de départ obligatoire** (D-018) : `git fetch && git status` sur `hub-ia`, partir d'un main à jour incluant les merges PR #42 + PR `feature/post-s1bis-…`.

**Vérification préalable des clés** : `ls -la rag/code/.env` doit retourner le fichier (permissions `-rw-------`). Si absent → blocker, signaler à Blaise sans avancer.

---

## 4. Méthode — 3 lots dans l'ordre

### Lot S1c.1 — Refactor python-dotenv (option propre actée par Blaise)

**Livrable** : ajout de `python-dotenv` au code pour lecture automatique du `.env` au démarrage des scripts.

**Détail** :
1. Ajouter `python-dotenv>=1.0.0` dans `rag/code/requirements.txt`
2. Modifier `rag/code/ingestion/ingest.py` : `from dotenv import load_dotenv; load_dotenv()` en tête de script (avant les imports openai/anthropic). Charge automatiquement `rag/code/.env` si présent.
3. Modifier `rag/code/backend/query.py` : idem.
4. Modifier `rag/code/eval/run_eval.py` : idem (si le script lance des appels API).
5. Mettre à jour les docstrings `OPENAI_API_KEY` / `ANTHROPIC_API_KEY` pour mentionner le `.env` comme source par défaut.
6. **Tests** : étendre `rag/code/ingestion/test_ingest.py` et `rag/code/backend/test_query.py` avec un test sanity « clés lues depuis .env sans variable d'environnement préalable ». Utiliser `tmp_path` et `monkeypatch` pour ne pas dépendre du `.env` réel.

**Critères de succès** :
- `python -c "from ingestion.ingest import OpenAIEmbeddingClient; print('OK')"` ne lève pas d'erreur même sans `export OPENAI_API_KEY` préalable
- Suite tests : tous les tests S1 (62/62) restent verts + nouveaux tests load_dotenv verts

**Commit attendu** : `feat(rag): python-dotenv pour lecture automatique .env (s1ter lot 1)`.

---

### Lot S1c.2 — Validation end-to-end réelle (le cœur du sprint)

**Livrable** : exécution complète de la pipeline sur le vault de 9 MD avec clés API désormais disponibles.

**Étapes** :

1. **Ingestion réelle** : `python3 rag/code/ingestion/ingest.py --vault rag/content --store rag/code/vector_store` sur le vault complet (9 fichiers).
   - Volume attendu : ~30-60 chunks indexés (estimation sur 9 fichiers de ~80-200 lignes chacun)
   - Coût attendu : < 0,01 $ OpenAI (corpus ~50 k tokens × 0,02 $/M = ~0,001 $)
2. **Re-indexation incrémentale** : modifier 1 fichier MD de test (bump `last_updated` du frontmatter d'un module), relancer `ingest.py`, vérifier que `report.chunks_updated` indique seuls les chunks affectés.
3. **Query CLI sur les 10 questions du golden set** : exécuter `python3 rag/code/backend/query.py "..."` pour chacune des 10 questions de `rag/eval/questions.yaml`. Sauvegarder les réponses + sources citées + latence dans `rag/eval/queries-s1ter-output.md`.
4. **Eval automatique** : `python3 rag/code/eval/run_eval.py` produit le rapport de matching (`sources_match` + `concepts_match`) dans `rag/eval/eval-report-s1ter.md`.

**Critères de succès** :
- Ingestion sans erreur, ~30-60 chunks créés en ChromaDB local
- Re-indexation incrémentale opérationnelle (1 fichier modifié → seuls ses chunks ré-indexés)
- 10 questions traitées en moins de 5 sec/question
- **≥ 8/10 questions** ont les `expected_sources` citées (cible D-021 maintenue)
- **≥ 50 %** des concepts attendus par question présents dans les réponses
- Coût accumulé OpenAI < **0,10 $** + Anthropic < **0,50 $** (durci par rapport au brief S1bis vu crédits réduits)

**Commit attendu** : `feat(rag): validation end-to-end sur vault 9 MD — ingest + 10 queries + eval (s1ter lot 2)`.

---

### Lot S1c.3 — Rapport mission consolidé + ouverture PR

**Livrable A — `rag-prep/briefs/RAPPORT-CC-S1ter.md`** (structure modèle, ~1500-2000 mots) :

1. **Synthèse exécutive** : lots S1c.1-S1c.3 traités, principaux succès, coût total
2. **Résultats Lot S1c.1** : ajout python-dotenv + extension tests (62 + N nouveaux tests verts)
3. **Résultats ingestion** : nombre de chunks créés, fichiers/sections couverts, performance re-indexation incrémentale, coût OpenAI exact
4. **Résultats query + eval** : matching `expected_sources` (X/10), distribution latence, observations qualitatives sur les réponses, coût Anthropic exact
5. **Coût API total accumulé S1 + S1bis + S1ter** (estimation)
6. **Apprentissages clés** : qualité du retrieval observée vs attendu, gaps identifiés sur le vault (manques de contenu, problèmes de chunking), suggestions pour S2
7. **Recommandations pour Sprint S2** : production widget public, déploiement Cloudflare Worker, capture feedback Supabase, audit-md-rag v2 (alignement SPEC v1.3 + R9/R10)
8. **Liste complète des commits S1 + S1bis + S1ter**

**Livrable B — Ouverture PR vers `main`** :
- **Titre PR** : `feat(rag): Sprint S1ter - validation end-to-end + python-dotenv + clôture définitive S1`
- **Description PR** : pointer vers RAPPORT-CC-S1ter.md, mentionner les améliorations vs PR #42 (Lot S1b.2 désormais exécuté), résultats eval ≥ 8/10, coût total < 1 $
- **Reviewers** : laisser vide (Blaise validera côté GitHub)

**Pas de merge automatique** : Blaise mergera après validation manuelle.

**Commit attendu** : `docs(rag): rapport mission S1ter + ouverture PR clôture S1`.

---

## 5. Estimation effort consolidée

| Lot | Effort estimé Claude Code |
|---|---|
| S1c.1 | 1 h (refactor + tests + validation) |
| S1c.2 | 1-2 h (ingest + 10 queries + eval + observation) |
| S1c.3 | 1 h (rédaction rapport + ouverture PR) |
| **Total** | **~3-4 h Claude Code** |

**Coût API estimé total** : ~0,30 $ (largement sous les crédits disponibles 3 $ + 5 $).

---

## 6. Workflow recommandé

1. Confirmer la lecture des préalables (« Sync state lue, je m'apprête à faire X »).
2. Vérifier la présence du `.env` et le chargement via python-dotenv (Lot S1c.1 valide le mécanisme).
3. Enchaîner les 3 lots dans l'ordre. Ne pas commencer S1c.2 si S1c.1 n'est pas validé (clés non chargées = échec garanti).
4. Commits granulaires par lot.
5. PR ouverte à la toute fin (Lot S1c.3).

---

## 7. Règles de prudence — plafonds API durcis pour S1ter

**Compte tenu des crédits limités (3 $ Anthropic + 5 $ OpenAI sans renouvellement)** :

1. **Alerte hard** : si > **0,50 $ Anthropic** ou > **0,10 $ OpenAI** atteints → arrêt immédiat + signalement à Blaise. Plus serré que les plafonds D-013 (50 $ / 10 $) qui étaient le cap absolu mensuel.
2. **Pas de re-ingestion répétée** : ingest les 9 fichiers UNE FOIS, garder le vector store, ne pas relancer en boucle pour debug. Si nécessaire de re-ingester pour tests, utiliser `--dry-run` (gratuit).
3. **Limiter les retries** : pas plus de 2 tentatives par question en cas d'erreur API. Au-delà, signaler à Blaise.
4. **Pas de modifications des MD du vault** sous quelque prétexte que ce soit (D-022). Si l'audit détecte une erreur → signaler à Blaise, ne pas corriger toi-même.
5. **Pas de modifications des fichiers de gouvernance** dans `rag-prep/` (sauf `JOURNAL-POC-RAG.md`, `STATUS-RAG.md`, et tes propres rapports `briefs/RAPPORT-CC-S1ter.md`).
6. **Pas de déploiement Cloudflare Worker** en S1ter : tout reste en CLI Python local. Le widget public est livrable S3.

---

## 8. Décisions explicites de NE PAS faire dans ce sprint

1. ❌ Pas d'audit-md-rag v2 (roadmap S2, hors scope S1ter)
2. ❌ Pas de portage TypeScript / Cloudflare Worker (livrable S3)
3. ❌ Pas de capture feedback Supabase (livrable S3)
4. ❌ Pas d'extension du golden set au-delà des 10 questions (extension S2)
5. ❌ Pas de production de fichiers MD du vault (rôle Cowork D-022)
6. ❌ Pas de merge automatique de la PR (Blaise valide manuellement côté GitHub)

---

## 9. Validation finale avant clôture S1ter

Checklist à exécuter avant d'ouvrir la PR :

- [ ] python-dotenv ajouté + load_dotenv() en tête des scripts d'ingestion, query et eval
- [ ] Nouveaux tests load_dotenv verts (62 + N tests verts au total)
- [ ] Pipeline d'ingestion testé sur 9 MD du vault → 30-60 chunks indexés
- [ ] Re-indexation incrémentale validée (1 fichier modifié → ses chunks re-indexés uniquement)
- [ ] 10 questions du golden set évaluées via query.py
- [ ] `run_eval.py` produit le rapport de matching
- [ ] ≥ 8/10 questions ont les sources attendues citées
- [ ] Coût accumulé S1ter < **0,60 $** total (Anthropic + OpenAI)
- [ ] `RAPPORT-CC-S1ter.md` produit en 8 sections
- [ ] PR ouverte avec titre + description conformes
- [ ] Aucun secret (clé API) dans le diff
- [ ] `JOURNAL-POC-RAG.md` mis à jour (append S1ter)
- [ ] `STATUS-RAG.md` mis à jour (S1 + S1bis + S1ter ✅ — sprint S1 définitivement clos, prêt pour S2)

---

## 10. Fichiers de référence et contact

**Référentiels du couple 2** (tous dans `rag-prep/` du clone Git) :
- `rag-prep/_instructions-rag.md` v1
- `rag-prep/DECISIONS-RAG.md` (29 décisions actées dont D-024 à D-029)
- `rag-prep/SPEC-MD-POUR-RAG.md` v1.3 (R1 à R10 + exception structurelle + politique whitelist)
- `rag-prep/STRATEGIE-MD-RAG.md` v1
- `rag-prep/cartographie-rag.md` (9 entrées vault à jour)
- `rag-prep/whitelist-wikilinks-futurs.md` (69 codes whitelistés)
- `rag-prep/STATUS-RAG.md`
- `rag-prep/JOURNAL-POC-RAG.md`
- `rag-prep/SYNC-INTER-CANAUX.md` (3 items archivés + 2 descendants ouverts I-D-001 et I-D-002)
- `rag-prep/briefs/RAPPORT-CC-S1.md` + `RAPPORT-CC-S1bis.md` (tes rapports précédents)

**Contact** : Blaise Cavalli (garant transverse). Toute question, blocker, ou écart par rapport au brief remonte via lui.

---

*Brief produit le 12 mai 2026. Volume : ~1800 mots (cible D-021 ~2000 mots respectée). Branche cible déterminée par convention D-027.*
