# BRIEF-CC-S1bis — Validation end-to-end + ouverture PR

**Émetteur :** Cowork Hub IA Plateforme
**Destinataire :** Claude Code Hub IA Plateforme
**Garant transverse :** Blaise Cavalli
**Sprint :** S1 (clôture) — suite directe du `BRIEF-CC-S1-pilote-pipeline.md`
**Branche cible :** `claude/execute-pilot-batches-mBSIp` (conservée — convention D-027)
**Statut :** v1, à transmettre

---

## 1. Métadonnées

- **Repo cible :** `hub-ia` (branche `claude/execute-pilot-batches-mBSIp`)
- **Auteur du brief :** Cowork Hub IA Plateforme
- **Sprint précédent :** S1 (6 lots terminés, 62/62 tests verts, 0 $ API consommé, livrable RAPPORT-CC-S1.md)
- **Nature de l'itération :** validation end-to-end de la pipeline RAG sur le contenu réel du vault (10 fichiers MD déposés par Blaise) + ouverture PR vers main

---

## 2. Contexte court

Le sprint S1 a livré la pipeline RAG complète (audit-md-rag.py v1, ingestion ChromaDB, query CLI, run_eval.py) testée sur mocks et fixtures (62 tests). Le contenu réel du vault (vague 1 + vague 2 du couple 2) vient d'être déposé par Blaise dans `rag/content/` sur ta branche. Il s'agit maintenant de **valider la pipeline end-to-end sur ce contenu réel** et d'**ouvrir la PR**.

**Évolutions structurantes depuis le brief CC-S1** :
- **SPEC-MD-POUR-RAG v1.2** publiée (ajout R9 chiffres canoniques + R10 tableaux numériques fidèles)
- **3 nouvelles décisions** : D-024 (architecture circulation), D-025 (briques transverses), D-026 (co-production légère N3/N4)
- **D-012-bis (révision)** : MCP Obsidian reporté à Phase 2 — **Lot 2 du brief CC-S1 reclassé non applicable Phase 1**
- **D-027** : convention de nommage des branches Claude Code Plateforme — la branche actuelle `claude/execute-pilot-batches-mBSIp` est conservée
- **2 nouveaux items SYNC-INTER-CANAUX** traités (I-002, I-003 archivés)

---

## 3. Préalable obligatoire (lectures avant exécution)

À lire dans cet ordre, intégralement :

1. **Ton propre rapport mission précédent** : `rag-prep/briefs/RAPPORT-CC-S1.md` (contexte de tes 6 commits + écarts signalés)
2. `rag-prep/_instructions-rag.md` v1 — référentiel complet (notamment §8 architecture de circulation D-024)
3. `rag-prep/DECISIONS-RAG.md` — registre actualisé (27 décisions actées, dont D-024 à D-027)
4. `rag-prep/SPEC-MD-POUR-RAG.md` v1.2 — cahier des charges actualisé (R9 + R10 nouvelles règles strictes)
5. `rag-prep/STATUS-RAG.md` — état sprint actuel
6. `rag-prep/cartographie-rag.md` — inventaire des 10 fichiers MD désormais dans le vault avec angles thématiques et recouvrements

**Audit de départ obligatoire** : `git fetch && git status` sur `hub-ia` (procédure de resync D-018). Vérifier que ta branche `claude/execute-pilot-batches-mBSIp` contient bien les 10 fichiers MD déposés dans `rag/content/`.

---

## 4. Méthode — 3 lots dans l'ordre

### Lot S1b.1 — Audit-md-rag sur le contenu réel

**Livrable** : exécution de `audit-md-rag.py` sur l'ensemble du vault `rag/content/**/*.md` (10 fichiers attendus). Rapport texte structuré exporté en `rag/eval/audit-report-s1bis.md`.

**Critères de succès** :
- 10 fichiers MD parcourus
- Application des 5 règles R1 à R4 + R6 (R5, R7, R8, R9, R10 en roadmap v2 pas encore implémentées)
- Total errors **= 0** attendu (le vault a été produit conformément à SPEC v1.2 et passé en revue I-003)
- Si erreurs détectées → signaler à Blaise sans corriger soi-même (les MD du vault sont produits par Cowork — discipline D-022)

**Commit attendu** : `chore(rag): audit-md-rag report on real vault content (s1bis lot 1)`.

---

### Lot S1b.2 — Validation end-to-end (ingestion + retrieval + génération + eval)

**Livrable** : exécution complète de la pipeline sur le vault réel :

1. **Ingestion** : `python rag/code/ingestion/ingest.py` sur le vault `rag/content/`. Sortie attendue : ~30-60 chunks indexés dans ChromaDB (volume estimé sur 10 fichiers MD de ~80-200 lignes chacun).
2. **Re-indexation incrémentale** : modifier 1 fichier MD test (bump du `last_updated` du frontmatter), relancer `ingest.py`, vérifier que seuls les chunks affectés sont ré-indexés.
3. **Query CLI** : exécuter les 10 questions du golden set `rag/eval/questions.yaml` via `python rag/code/backend/query.py "..."` pour chacune. Sauvegarder les réponses + sources citées + latence en `rag/eval/queries-s1bis-output.md`.
4. **Eval** : `python rag/code/eval/run_eval.py` produit le rapport de matching (sources citées vs `expected_sources` + concepts attendus vs présents).

**Critères de succès** :
- Ingestion sans erreur, ~30-60 chunks créés
- Re-indexation incrémentale opérationnelle (un seul chunk re-indexé sur le fichier modifié)
- 10 questions traitées en moins de 5 sec/question
- **≥ 8/10 questions ont les `expected_sources` citées** (cible brief original maintenue)
- **≥ 7/10 réponses jugées utiles** par sondage manuel de Blaise (validation qualitative)
- Coût API accumulé Anthropic + OpenAI **< 2 $** (plafonds D-013 largement respectés)

**Commit attendu** : `feat(rag): end-to-end validation on real vault content (10 MD, eval set 10 questions)`.

---

### Lot S1b.3 — Rapport mission consolidé + ouverture PR

**Livrable A — `rag-prep/briefs/RAPPORT-CC-S1bis.md`** (structure modèle couple 1) :

1. **Synthèse exécutive** : lots S1b.1-S1b.3 traités, principaux écarts ou succès
2. **Résultats audit-md-rag sur vault réel** : nombre d'erreurs détectées par règle (R1-R4, R6), distribution
3. **Résultats ingestion** : nombre de chunks créés, fichiers/sections couverts, performance re-indexation incrémentale
4. **Résultats eval** : matching `expected_sources` (X/10), distribution latence, observations qualitatives sur les réponses
5. **Coût API accumulé** Anthropic + OpenAI (estimation)
6. **Écarts résiduels signalés à Blaise** (R5, R7, R8, R9, R10 non automatisés v1 ; recommandations pour audit-md-rag v2)
7. **Propositions d'amendement à `SPEC-MD-POUR-RAG.md` ou autres référentiels** issues des apprentissages
8. **Recommandations pour Sprint S2** (production widget public, déploiement Cloudflare Worker, capture feedback Supabase)
9. **Liste complète des commits des sprints S1 et S1bis**

**Livrable B — Ouverture PR vers `main`** :
- **Titre PR** : `feat(rag): Sprint S1 + S1bis - pipeline RAG complet + vault initial (10 fichiers MD, 62+ tests)`
- **Description PR** : pointer vers le RAPPORT-CC-S1bis.md, lister les commits par sprint, signaler les 10 fichiers MD du vault déposés par Cowork, mention de la non-application de Lot 2 (MCP Obsidian reporté Phase 2 par D-012-bis)
- **Labels** : `feat`, `rag`, `sprint-s1`, `documentation`
- **Reviewers** : laisser vide (Blaise validera côté GitHub)

**Pas de merge automatique** : c'est Blaise qui mergera après validation manuelle.

**Commit attendu** : `docs(rag): rapport mission consolidé S1+S1bis + ouverture PR`.

---

## 5. Estimation effort consolidée

| Lot | Effort estimé Claude Code |
|---|---|
| S1b.1 | 30 min (audit + rapport) |
| S1b.2 | 2-3 h (ingestion + 10 queries + eval + observation) |
| S1b.3 | 1-2 h (rédaction rapport + ouverture PR) |
| **Total** | **~4-6 h Claude Code** |

Coût API estimé : ~0,50-2 $ (10 questions × ~2-3k tokens chacune × Claude Sonnet 4.6 + embedding initial ingestion).

---

## 6. Workflow recommandé

1. Confirmer la lecture des préalables (« Sync state lue, je m'apprête à faire X »).
2. Vérifier la présence des 10 fichiers MD dans `rag/content/` (issus du dépôt par Blaise sur la branche actuelle).
3. Enchaîner les 3 lots dans l'ordre. Ne pas commencer S1b.2 si S1b.1 détecte des erreurs.
4. Commits granulaires par lot.
5. PR ouverte à la toute fin (Lot S1b.3).

---

## 7. Règles de prudence en exécution autonome

1. **Pas de modification des fichiers MD du vault** sous quelque prétexte que ce soit (D-022, spécialisation des rôles). Si l'audit détecte une erreur → signaler à Blaise, ne pas corriger toi-même.
2. **Pas de modification des fichiers de gouvernance du couple 2** dans `rag-prep/` (sauf `JOURNAL-POC-RAG.md`, `STATUS-RAG.md`, et tes propres rapports `briefs/RAPPORT-CC-S1bis.md`).
3. **Plafonds API** : si > 1 $ Anthropic ou > 0,30 $ OpenAI atteints → signalement immédiat à Blaise.
4. **Pas de déploiement Cloudflare Worker** en S1bis : tout reste en CLI Python local. Le widget public est livrable S3.
5. **Pas d'extension du golden set** au-delà des 10 questions (extension S2).

---

## 8. Décisions explicites de NE PAS faire dans ce sprint

1. ❌ Pas de setup MCP Obsidian (Lot 2 du brief original reclassé non applicable par D-012-bis)
2. ❌ Pas de portage TypeScript / Cloudflare Worker (livrable S3)
3. ❌ Pas de capture feedback Supabase (livrable S3)
4. ❌ Pas de production de fichiers MD du vault (rôle Cowork D-022)
5. ❌ Pas de modification de la branche en rename (D-027 conserve `claude/execute-pilot-batches-mBSIp`)
6. ❌ Pas de merge automatique de la PR (Blaise valide manuellement côté GitHub)

---

## 9. Validation finale avant clôture S1bis

Checklist à exécuter avant d'ouvrir la PR :

- [ ] `audit-md-rag.py` exécuté sur 10 MD du vault → 0 erreur (ou erreurs signalées à Blaise)
- [ ] Pipeline d'ingestion testé sur 10 MD → 30-60 chunks indexés
- [ ] Re-indexation incrémentale validée (1 fichier modifié → 1 chunk re-indexé)
- [ ] 10 questions du golden set évaluées via query.py
- [ ] `run_eval.py` produit le rapport de matching
- [ ] ≥ 8/10 questions ont les sources attendues citées
- [ ] Coût accumulé < 2 $ (Anthropic + OpenAI)
- [ ] `RAPPORT-CC-S1bis.md` produit en 9 sections
- [ ] PR ouverte avec titre + description + labels conformes
- [ ] Aucun secret (clé API) dans le diff
- [ ] `JOURNAL-POC-RAG.md` mis à jour (append S1bis)
- [ ] `STATUS-RAG.md` mis à jour (S1 + S1bis ✅, prêt pour S2)

---

## 10. Fichiers de référence et contact

**Référentiels du couple 2** (tous dans `rag-prep/` du clone Git) — lectures préalables :
- `rag-prep/_instructions-rag.md` v1 (§8 architecture de circulation D-024)
- `rag-prep/DECISIONS-RAG.md` (27 décisions actées dont D-024, D-025, D-026, D-027, D-012-bis)
- `rag-prep/SPEC-MD-POUR-RAG.md` v1.2 (10 règles, R9 et R10 nouvelles)
- `rag-prep/STRATEGIE-MD-RAG.md` v1
- `rag-prep/cartographie-rag.md` (10 entrées de vault)
- `rag-prep/STATUS-RAG.md`
- `rag-prep/JOURNAL-POC-RAG.md`
- `rag-prep/SYNC-INTER-CANAUX.md`
- `rag-prep/briefs/RAPPORT-CC-S1.md` (ton rapport précédent)

**Contact** : Blaise Cavalli (garant transverse). Toute question, blocker, ou écart par rapport au brief remonte via lui.

---

*Brief produit le 12 mai 2026. Volume : ~1700 mots (dans la cible D-021 ~2000 mots). Branche conservée selon D-027.*
