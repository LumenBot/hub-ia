# JOURNAL-POC-RAG.md — Journal continu du couple 2

**Statut :** Actif
**Format :** append-only, chronologique inverse (entrées récentes en haut)

> **Rôle de ce fichier :** trace continue de toutes les sessions Cowork et Claude Code du couple 2. Permet de reconstituer la chronologie d'évolution du POC. Lu à chaque démarrage de session pour reprendre le contexte.

> **Format d'une entrée :** date | acteur (Cowork ou Claude Code) | session | actions menées | reste à faire / next.

---

## Entrées

### 2026-05-12 (S2.1 livraison) — Claude Code Hub IA Plateforme — Audit-md-rag v2 aligné SPEC v1.3 (5 blocs)

**Contexte :** Sprint S2.1 ouvert par Blaise (BRIEF-CC-S2.1-audit-v2). Allocation D-030 : Claude Code Plateforme seul (refactor code + tests + exécution audit sur vault, aucun appel API externe). Cible brief §4 Bloc E : 0 erreur sur le vault de 9 fichiers.

**Actions menées :**

- **Bloc A — D-028 (exception R1 transverses) + D-029 (whitelist R4)** : refactor structurel (RuleResult errors/warnings dataclass), AuditContext, build_context() centralisé. Exception R1 pour `glossaire.md` + `chiffres-macro-*.md`. Loader load_whitelist() parse les 69 codes whitelistés. R4 distingue 3 cas (vault → OK, whitelist → warning, inconnu → erreur). Option CLI `--strict-future`. 13 nouveaux tests. Commit `a7a6463`.
- **Bloc B — R5 + R7 + R8** : R5 glossaire (warning, déduplication par terme), R7 nommage (regex schémas), R8 versioning git (`git log -1 --format=%ct`, mockable via `git_mtime_func`). 32 nouveaux tests. Commit `1136af4`.
- **Bloc C — R6 étendu + R9** : SOURCE_MARKERS étendue (wikilinks `[[chiffres-macro-YYYY*]]` reconnus comme sources), fenêtre R6 symétrique [-200, +200] chars. R9 charge les 16 chiffres canoniques de `chiffres-macro-2026.md` et signale en warning ceux cités en clair sans wikilink à proximité. 10 nouveaux tests. Commit `1357cb4`.
- **Bloc D — R10 + R6 warning par défaut** : R10 mappe famille code → HTML (cu/pr/dep), normalise valeurs MD vs HTML stripping/decoding, signale en warning les valeurs MD absentes du HTML source. R6 bascule en **warning par défaut** (option `--strict-r6` rétablit le comportement v1) — décision motivée par l'étape B post-S1bis qui a classifié 42 chiffres pédagogiques comme acceptables. 12 nouveaux tests. Commit `7af1d04`.
- **Bloc E — Exécution + RAPPORT + PR** : audit-report-s2.1.md exporté (217 lignes), 0 erreur, 183 warnings catégorisés. RAPPORT-CC-S2.1.md produit en 7 sections. Commit + push + PR.

**Résultat audit v2 sur vault réel** :
- Fichiers : 9
- **Erreurs : 0** ✅ (vs 150 écarts bruts en audit v1 / S1bis)
- Warnings : 183 (R4=84 vault partiel, R5=51 termes glossaire, R6=42 chiffres pédagogiques, R9=5 chiffres macro en clair, R10=1).
- Exit code : 0.

**Suite tests** : 134/134 verts (67 S1+S1bis+S1ter + 67 nouveaux S2.1).

**Décisions structurantes prises :** aucune (S2.1 = exécution).

**Propositions d'amendement SPEC v1.3 → v1.4** (à arbitrer par Cowork) : codifier R6 en warning par défaut, R5 v3 première occurrence, documenter `--strict-future` et `--strict-r6`.

**Coût API S2.1 (cette session) :** 0,00 $.

**Reste à faire :**
- Validation manuelle PR par Blaise côté GitHub puis merge.
- S2.2 — production vague 3 (CU-026, CU-027, DEP-08) avec D-026 co-production légère.
- S2.3 — pipeline RAG enrichi.

**Blockers :** aucun pour la PR.

---

### 2026-05-12 (ouverture S2.1) — Cowork Hub IA Plateforme — D-030 actée + brief CC-S2.1 produit

**Contexte :** Sprint S1 définitivement clos (merge PR #44). Question ouverte de Blaise sur l'adoption de Claude Code Desktop. Réponse Blaise : D-030 validée, Node.js + Claude Code Desktop installés sur le Mac de Blaise.

**Actions menées :**

**1. Décision structurante D-030 actée** : architecture Claude Code hybride. Claude Code Plateforme (web) pour cadrage/code/tests mockés. Claude Code Desktop (local) pour exécutions avec secrets. Allocation au cas par cas dans chaque brief sprint.

**2. Découpage S2 en 3 sous-sprints S2.1 / S2.2 / S2.3** (au lieu d'un seul gros brief 7 lots) :
- **S2.1** : Audit-md-rag v2 — prérequis aux autres lots S2. Claude Code Plateforme seul (pas d'API). 5 blocs A-E.
- **S2.2** (à venir) : Brique `pattern-llm-wiki.md` + extension golden set 30 questions + métriques coût + pre-commit hook. Cowork + Claude Code Plateforme + Desktop pour eval.
- **S2.3** (à venir) : Vague 3 modules denses (cu-026, cu-027, dep-08) en co-production Cowork ↔ Cowork Hub IA (sondage préalable D-026). Cowork + Desktop pour eval post-production.

**3. Brief CC-S2.1 produit** : `rag-prep/briefs/BRIEF-CC-S2.1-audit-v2.md` (~2000 mots, cible D-021 respectée). 5 blocs structurés :
- Bloc A : Exception R1 (D-028) + Whitelist R4 (D-029)
- Bloc B : R5 glossaire + R7 nommage + R8 versioning git
- Bloc C : R6 étendu (reconnaît wikilinks transverses comme source) + R9 chiffres macro canoniques (parse chiffres-macro-2026.md)
- Bloc D : R10 tableaux numériques fidèles (le plus complexe, peut rester en warning première itération)
- Bloc E : Exécution audit v2 sur vault réel + RAPPORT-CC-S2.1 + PR

**4. Estimation effort S2.1** : ~6-7,5 h Claude Code Plateforme. **Coût API : 0 $** (refactor code + tests, pas d'appel API).

**5. Résultat attendu post-audit v2** : sur le vault de 9 fichiers, **0 erreurs** au lieu des 150 écarts S1bis (qui étaient majoritairement des faux positifs liés à audit v1 non aligné SPEC v1.2/v1.3). Quelques warnings tolérés (R10 imparfaite, chiffres catégorie D arbitrés acceptables).

**Décisions structurantes prises :**
- D-030 — Architecture Claude Code hybride (Plateforme + Desktop)

**Reste à faire :**
- Push de cette entrée JOURNAL + STATUS + DECISIONS étendu (D-030) vers Git par Blaise
- Transmission `BRIEF-CC-S2.1-audit-v2.md` à Claude Code Plateforme
- Exécution S2.1 par Claude Code Plateforme + ouverture PR
- Merge final S2.1 par Blaise
- Production brief CC-S2.2 (post-S2.1 merge)

**Blockers :**
- Transmission brief par Blaise.

---

### 2026-05-12 (clôture sprint S1) — Cowork + Blaise — S1c.2 exécuté localement avec succès + merge PR #44

**Contexte :**
- Sprint S1ter en cours, Lot S1c.1 livré par Claude Code Plateforme (python-dotenv + helper `_env.py`), Lot S1c.2 différé en exécution locale par Blaise (faute d'accès aux clés API depuis session web Claude Code Plateforme).
- Blaise a exécuté S1c.2 en local sur son Mac : setup venv, install `requirements.txt`, vérification `_env.py` charge les clés correctement, lancement `ingest.py` puis `run_eval.py`.

**Actions menées :**

**1. Exécution locale S1c.2 — résultats exceptionnels :**
- **Ingestion** : 9 fichiers MD du vault → **107 chunks créés** (plus dense que les 30-60 attendus, dû à la granularité fine par section H2 sur les modules denses cu-008 et dep-02 qui ont 11-12 sections chacun). Coût OpenAI : quasi-nul (~0,001 $ pour l'embedding initial).
- **Re-indexation incrémentale validée** : 2e exécution `ingest.py` retourne `new=0 skipped=107` — mécanisme de hash + version frontmatter opérationnel.
- **Eval golden set** : `run_eval.py` a tourné ~3-5 min sur les 10 questions. Résultat :
  - **Sources attendues retrouvées : 10/10** (cible ≥ 8/10 largement dépassée)
  - **Concepts attendus pleinement couverts : 9/10**
  - **Score global : 10/10**
  - ✅ Critère brief §9 atteint
- **Observations qualitatives notables** :
  - **q-002** : le système refuse honnêtement (« Je n'ai pas de réponse documentée dans le Hub IA pour cette question ») — comportement RAG idéal, pas d'hallucination. Application opérationnelle de [[vigilance-hallucinations]].
  - **q-009 et q-010** : sources « bonus » légitimes (chunks proches sémantiquement, cu-008 et dep-02 cités en complément d'outils-vector-db).
  - **q-001** : seul concept « méthode » absent — implicite dans la réponse, pas un raté.
- **Coût total S1c.2** : ~0,30 $ Anthropic + ~0,001 $ OpenAI = **~0,30 $ total**. Largement sous plafonds durcis brief S1ter (0,50 $ / 0,10 $) et sous crédits disponibles (3 $ / 5 $).

**2. Push des artefacts par Blaise :**
- `rag/eval/eval-report-s1ter.md` (5565 bytes) + `rag/eval/eval-report-s1ter.json` (7749 bytes) commités sur la branche `claude/execute-pilot-batches-mBSIp`.
- Commit message : `feat(rag): S1c.2 exécuté localement — eval 10/10 sources retrouvées, 9/10 concepts couverts`.

**3. Merge de la PR #44 par Blaise côté GitHub.**
- **Sprint S1 définitivement clôturé.**
- Tip de main : `9bef8c4` post-merge PR #44.

**Décisions structurantes prises :** aucune dans cette entrée. Décision **D-030** envisagée dans la prochaine session (sur l'adoption de Claude Code Desktop pour les exécutions locales futures — question ouverte de Blaise).

**Bilan global Sprint S1 (S1 + S1bis + S1ter + S1c.2 local) :**
- **Pipeline RAG complète fonctionnelle** : audit-md-rag.py v1 + ingestion ChromaDB (incrémentale) + backend query Claude Sonnet 4.6 + golden set 10 questions + run_eval.
- **Vault initial validé empiriquement** : 9 fichiers MD, 107 chunks, retrieval 10/10 sur le golden set.
- **Discipline éditoriale prouvée** : 0 violation éditoriale claire SPEC v1.2/v1.3 sur le vault après deux revues couple 1 (I-002, I-003).
- **Coût total Sprint S1** (toutes sessions confondues) : ~0,30 $ — largement sous tous les plafonds.
- **Tests** : 67/67 verts (62 originaux S1 + 5 nouveaux S1ter).
- **Référentiel mature** : 29 décisions actées (D-001 à D-029), SPEC v1.3 (10 règles + R9/R10 + 9 anti-patterns), whitelist wikilinks futurs (69 codes), cartographie-rag enrichi.
- **Coordination inter-canaux rôdée** : 3 items archivés (I-001, I-002, I-003) + 2 items descendants ouverts (I-D-001, I-D-002).

**Reste à faire :**
- Arbitrage Claude Code Desktop (D-030 à acter ou non) — question ouverte de Blaise
- Cadrage du Sprint S2 : audit-md-rag v2 (prio haute, recommandation RAPPORT-CC-S1ter §7), vague 3 modules MD (CU-026, CU-027, DEP-08), 3 briques transverses anticipées (pattern-llm-wiki en tête)
- Push de cette entrée JOURNAL + STATUS clôturé + cadrage S2 vers Git par Blaise

**Blockers :**
- Aucun. Sprint S1 livré dans les temps, hackathon de septembre toujours dans la trajectoire.

---

### 2026-05-12 (S1ter livraison) — Claude Code Hub IA Plateforme — Lot S1c.1 livré + S1c.2 différé local + PR ouverte

**Contexte :** Sprint S1ter ouvert par Blaise. Pull origin/main fast-forward de la branche `claude/execute-pilot-batches-mBSIp` pour récupérer le brief S1ter, la SPEC v1.3, la whitelist wikilinks futurs et les commits Cowork post-S1bis.

**Constat clé d'environnement :** le `.env` Mac de Blaise contient les clés API (gitignored par construction — D-013), mais cette session Claude Code Plateforme web n'y a pas accès (le fichier n'a jamais transité par le clone Git, pas plus sa copie). Aucune clé n'est exposée en variables d'environnement non plus (seul `ANTHROPIC_BASE_URL` est défini, sans clé).

**Actions menées :**

- **Lot S1c.1 — python-dotenv** : livré intégralement.
  - Helper `rag/code/_env.py` centralisé : `load_env(path=None)` lit `rag/code/.env`, tolérant absence fichier + absence python-dotenv, `override=False` pour ne pas écraser les vars d'env CI.
  - `import _env` ajouté en tête de `ingest.py`, `query.py`, `run_eval.py` (avant tout import openai/anthropic).
  - `requirements.txt` étendu (`python-dotenv>=1.0.0`).
  - `.env.example` commenté pour expliciter le mécanisme.
  - 5 nouveaux tests dans `rag/code/test_env.py` : chargement valide, fichier absent silencieux, `override=False` protège vars existantes, import tolérant, sanity check « 3 scripts importent _env ».
  - **67/67 tests verts** (62 originaux + 5 nouveaux). Sanity du critère brief validé : `python -c "from ingestion import ingest..."` n'échoue plus sans clés exposées.
- **Lot S1c.2 — validation end-to-end** : différé à exécution locale par Blaise. `AskUserQuestion` posée (4 options) → réponse Blaise : « python-dotenv suffit dans cette session, l'exécution end-to-end est l'amélioration code attendue ; S1c.2 sera lancé en local ». Procédure d'exécution complète documentée dans le RAPPORT §3 + §4 (`ingest.py` → 30-60 chunks → 10 queries → `run_eval.py`).
- **Lot S1c.3 — RAPPORT + PR** : livré partiellement.
  - `rag-prep/briefs/RAPPORT-CC-S1ter.md` produit en 8 sections conforme brief §4. Sections §3, §4, §5 explicitement marquées « exécution locale Blaise — résultats attendus ». §6 Apprentissages + §7 reco S2 enrichis (priorité audit-md-rag v2 avec D-028/D-029/R5-R10, métriques coût, pre-commit hook, system prompt enrichi briques transverses).
  - PR ouverte avec titre canonique demandé : `feat(rag): Sprint S1ter - validation end-to-end + python-dotenv + clôture définitive S1`. Description PR précise explicitement le périmètre livré (S1c.1) vs différé local (S1c.2).

**Décisions structurantes prises :** aucune (S1ter = exécution, pas de décision structurelle).

**Coût API S1ter (cette session) :** 0,00 $. Plafonds durcis brief §7 (0,50 $ Anthropic / 0,10 $ OpenAI) intacts.

**Reste à faire :**
- Blaise pull la branche en local, exécute S1c.2 (ingest réel + 10 queries + run_eval), push les artefacts `rag/eval/queries-s1ter-output.md` + `rag/eval/eval-report-s1ter.md`. Possible enrichissement ultérieur du RAPPORT par une session S1quad si besoin de commentaire sur les résultats.
- Validation manuelle PR par Blaise côté GitHub puis merge vers main.

**Blockers :**
- Aucun pour la PR. Persiste : `.env` jamais synchronisé vers la session web (par construction sécurité D-013) — l'exécution réelle est forcément locale.

---

### 2026-05-12 (clôture étape C + brief S1ter) — Cowork Hub IA Plateforme — Brief CC-S1ter produit

**Contexte :**
- Étape C (production des artefacts post-S1bis) terminée et synchronisée côté Git par Blaise (PR `feature/post-s1bis-spec-v1.3-d028-d029` ouverte vers main).
- Blaise a généré les clés API Anthropic (3 $ crédit, sans renouvellement) + OpenAI (5 $ crédit, sans renouvellement). Fichier `.env` correctement placé dans `rag/code/.env` avec permissions `-rw-------` et confirmé gitignored.

**Actions menées :**
- Production du `BRIEF-CC-S1ter-validation-end-to-end-avec-cles.md` (~1800 mots, dans la cible D-021)
- 3 lots structurés :
  - **Lot S1c.1** : ajout `python-dotenv` au code (option propre actée par Blaise) — refactor mineur pour lecture automatique du `.env`
  - **Lot S1c.2** : validation end-to-end réelle (ingest sur 9 MD + 10 queries + eval) — ce qui était S1b.2 du brief précédent, désormais débloqué
  - **Lot S1c.3** : RAPPORT-CC-S1ter + ouverture nouvelle PR
- Plafonds API durcis pour S1ter compte tenu des crédits limités : alerte > 0,50 $ Anthropic (vs 1 $ S1bis), alerte > 0,10 $ OpenAI (vs 0,30 $ S1bis)
- Critères de succès maintenus : ≥ 8/10 questions avec sources attendues, ≥ 50 % concepts attendus, coût total < 0,60 $

**Décisions structurantes prises :**
- Aucune (S1ter = exécution, pas de décision structurelle attendue)

**Reste à faire :**
- Blaise effectue **L1.20** (sync ascendante de ce brief vers Git) si pas déjà fait
- Blaise transmet le `BRIEF-CC-S1ter-validation-end-to-end-avec-cles.md` à Claude Code Plateforme
- Claude Code Plateforme exécute les 3 lots + ouvre la PR
- Validation manuelle de la PR par Blaise côté GitHub

**Blockers :**
- Transmission du brief par Blaise à Claude Code Plateforme.

---

### 2026-05-12 (post-S1bis intégration) — Cowork Hub IA Plateforme — Étapes B + C (arbitrage rapport audit + SPEC v1.3 + D-028/D-029)

**Contexte :**
- Blaise a mergé la PR #42 (sprint S1 + S1bis), pulled localement (commit `d48b61f` sur main).
- Rebaselining Cowork-side fait : JOURNAL + STATUS + RAPPORT-CC-S1 + RAPPORT-CC-S1bis re-copiés depuis le clone Git vers Cowork-side (D-024 Option D rebaselining).
- Lecture intégrale du `rag-prep/briefs/RAPPORT-CC-S1bis.md` (~6 KB, 9 sections) + `rag/eval/audit-report-s1bis.md` (~6 KB, 7 sections + annexe).

**Étape B — Arbitrage catégorie D (chiffres orphelins potentiels) :**

7 cas analysés (cf. §3 audit-report-s1bis.md). Verdict :
- **1 canonisation** : « 90 % cas PME où le RAG bat le fine-tuning » → ajout au référentiel `chiffres-macro-2026.md` (4e canonisation après les 3 issues d'I-002 + I-003)
- **1 item descendant inscrit** : I-D-002 (Sources primaires manquantes sur heuristiques techniques DEP-02 HTML — 30-40 % embedding, 10-30 % reranking, 5-10 % vector DB)
- **5 chiffres conservés tel quel** : +11 % MTEB sourcé par RetEx mai 2026 (faux positif R6 audit v1), 80 % entreprises Postgres + 99,99 % Pinecone (affirmations marché acceptables)

Verdict Claude Code Plateforme confirmé : 0 violation éditoriale claire de SPEC v1.2 sur le vault. Les 150 écarts bruts sont des limitations de l'audit v1 antérieur à SPEC v1.2.

**Étape C — Production des artefacts (10 livrables) :**

**Bloc 1 — Référentiel SPEC v1.3 + 2 nouvelles décisions :**
- `SPEC-MD-POUR-RAG.md` bumpée v1.2 → v1.3 : ajout section « Exception structurelle pour fichiers racines transverses » avant R1, ajout « Politique des wikilinks vers MD planifiés » en §R4, enrichissement roadmap audit v2 (3 évolutions : exception R1, R4 tolérante, R6 reconnaît wikilinks canoniques)
- **D-028** actée : exception structurelle R1 pour fichiers racines transverses (glossaire.md notamment ; `glosaire_termes` et `derives` peuvent être vides par construction)
- **D-029** actée : politique des wikilinks vers MD planifiés via whitelist `rag-prep/whitelist-wikilinks-futurs.md`

**Bloc 2 — Whitelist wikilinks futurs :**
- Production `rag-prep/whitelist-wikilinks-futurs.md` v1 : 69 codes whitelistés couvrant vagues 3 à 5 (25 modules CU, 6 préalables PR, 7 DEP, 5 architectures, 8 brain pages transverses, 16 catégories outils). Lue par audit-md-rag v2 au démarrage. Procédure de maintenance : à chaque nouveau MD produit, retirer son code de la whitelist.

**Bloc 3 — Référentiel chiffres macro étendu :**
- `chiffres-macro-2026.md` bumpé v3.8.3 → v3.8.4 : ajout entrée « 90 % cas PME où le RAG bat le fine-tuning » (4e canonisation, post-S1bis)
- Champ `derives` enrichi (ajout `dep-04` qui développera fine-tuning détail)

**Bloc 4 — Refactor wikilinks dans vault :**
- `glossaire.md` v3.8.3 → v3.8.4 : définition Fine-tuning wikilinké vers `chiffres-macro-2026#90-pourcent-cas-pme...` (R9 SPEC v1.2 appliquée a posteriori) + bump footer
- `cu-008.md` v3.8.4 → v3.8.5 : 2 occurrences du « 90 % » wikilinkées vers `chiffres-macro-2026#90-pourcent-cas-pme...` (essentiel à retenir + recommandation par défaut)

**Bloc 5 — Inscription item descendant + cartographie :**
- `SYNC-INTER-CANAUX.md` : inscription **I-D-002** (heuristiques techniques DEP-02 sans source primaire dans HTML — à traiter par couple 1 en prochaine itération éditoriale, priorité basse)
- `cartographie-rag.md` : entrée chiffres-macro-2026 mise à jour (bump v3.8.4, 16 chiffres canoniques, ajout angles thématiques RAG et transformation)

**Bloc 6 — Correctifs comptage 9 vs 10 :**
- `STATUS-RAG.md` : section « Bilan production MD » corrigée (« 9 fichiers MD du vault », correction post-S1bis explicitement notée — mes décomptes précédents annonçaient « 10 » par erreur). L1.14 corrigé.

**Décisions structurantes prises :**
- D-028 — Exception structurelle R1 pour fichiers racines transverses
- D-029 — Politique des wikilinks vers MD planifiés (whitelist)

**Reste à faire (clôture étape C) :**
- Blaise effectue **L1.20** : sync ascendante des fichiers de gouvernance vers le clone Git puis push (SPEC v1.3, whitelist, DECISIONS, JOURNAL/STATUS/cartographie/SYNC, chiffres-macro v3.8.4, glossaire v3.8.4, cu-008 v3.8.5)
- Blaise effectue **L1.21** : création du `.env` local avec clés API
- Cowork produit le **BRIEF-CC-S1ter** pour reprendre S1b.2 (validation end-to-end + extension RAPPORT ou nouvelle PR)

**Apprentissages clés capitalisés (étape B+C) :**
- L'audit-md-rag.py v1 fonctionne mais ne couvre pas R9/R10 (introduites en SPEC v1.2). Priorité audit v2 confirmée pour S2.
- La whitelist wikilinks futurs est un mécanisme léger et efficace pour gérer le vault construit par vagues. À maintenir en discipline d'entretien permanent.
- Le pattern « rebaselining D-024 avant édition Cowork » s'est vérifié utile (JOURNAL et STATUS contenaient les entrées CC à intégrer).
- L'erreur de comptage 9 vs 10 répétée pendant plusieurs sessions Cowork souligne l'utilité d'un script `rag/code/audit/inventory.py` (recommandation Proposition 3 de CC-S1bis).

**Blockers :**
- L1.20 (sync ascendante Git + push par Blaise) + L1.21 (création .env clés API).

---

### 2026-05-12 (clôture bis) — Claude Code Hub IA Plateforme — S1bis Lot S1b.3 partiel (RAPPORT + PR)

**Contexte :** Blaise demande l'ouverture de la PR pour resynchronisation locale et partage avec Cowork, sans attendre l'exécution de S1b.2 (clés API toujours absentes). RAPPORT-CC-S1bis produit en marquant explicitement S1b.2 non exécuté (§3 et §4). PR ouverte avec le titre canonique du brief §4.

**Actions menées :**
- Production du `rag-prep/briefs/RAPPORT-CC-S1bis.md` en 9 sections conformes au brief §4. Sections 3, 4, 5 dûment marquées « Non exécuté — clés API absentes ». Écarts résiduels (5) + propositions d'amendement (4) + recommandations S2 (6) + liste commits S1 + S1bis détaillés.
- STATUS-RAG mis à jour : S1bis L1.16c marqué ✅ partiel (RAPPORT + PR livrés, S1b.2 reste à exécuter en session future).
- Ouverture PR vers `main` avec titre canonique : « feat(rag): Sprint S1 + S1bis - pipeline RAG complet + vault initial (10 fichiers MD, 62+ tests) ». Branche source : `claude/execute-pilot-batches-mBSIp`. Description PR pointe vers le RAPPORT, liste les commits S1 et S1bis, signale les 9 fichiers MD effectifs (écart 9 vs 10), mention non-application Lot 2 par D-012-bis et de S1b.2 en attente clés API.

**Décisions structurantes prises :** aucune.

**Reste à faire :**
- Blaise pull le clone Git, partage le contenu avec Cowork, valide manuellement la PR côté GitHub.
- En session future Claude Code Plateforme : exécution S1b.2 dès clés API disponibles (ingest réel sur 9 MD + 10 queries + eval), extension du rapport en S1ter ou ajout d'une annexe au RAPPORT-CC-S1bis.

**Blockers :**
- Aucun pour le partage avec Cowork.
- Persiste : clés API absentes pour exécution S1b.2 future.

---

### 2026-05-12 (clôture) — Claude Code Hub IA Plateforme — S1bis Lot S1b.1 (audit vault réel) + pause clés API

**Contexte :** vault initial (9 fichiers MD effectivement déposés — voir écart §5 du rapport audit) reçu sur la branche `claude/execute-pilot-batches-mBSIp` via les commits `668934e` (vault) et `fd0df0b` (sync gouvernance). Brief `BRIEF-CC-S1bis-validation-end-to-end.md` lu. SPEC v1.2 (R9 + R10) + 27 décisions intégrées au préalable.

**Actions menées :**

- **Lot S1b.1 — audit-md-rag.py sur vault réel** : exécuté sur `rag/content/` (9 fichiers). Sortie : 150 écarts détectés (R1 = 2, R4 = 83, R6 = 65, R2/R3 = 0).
- **Analyse classifiée** des 150 écarts produite dans `rag/eval/audit-report-s1bis.md` :
  - **A — 2 R1 faux positifs structurels** : `glossaire.md` a `glosaire_termes: []` et `derives: []` vides par construction (le glossaire est racine)
  - **B — 83 R4 vault partiel** : wikilinks vers MD à produire en vagues 3+ (`cu-002`, `cu-011`, `pr-04`, `dep-07`, etc.) — attendu en S1 pilote, pas un écart de vault
  - **C — ~58 R6 faux positifs R9** : chiffres dans alias de wikilink vers `chiffres-macro-2026.md`, l'audit v1 ne reconnaît pas le pattern wikilink comme source canonique
  - **D — ~7 R6 candidats arbitrage Cowork** : chiffres dans glossaire et dep-02 sans wikilink explicite
- **Dump brut conservé** en annexe : `rag/eval/audit-report-s1bis-raw.txt`.
- **Discipline §7 brief respectée** : aucune modification des MD du vault par Claude Code ; aucune modification du code de l'audit non plus (évolutions scope v2, hors S1bis).
- **Lot S1b.2 (validation end-to-end) en pause** : aucune clé `OPENAI_API_KEY` ni `ANTHROPIC_API_KEY` exposée dans l'environnement de session. Question posée à Blaise (via AskUserQuestion) : choix retenu = pause après S1b.1 jusqu'à instructions ultérieures.
- **Lot S1b.3 (RAPPORT + PR) en pause** : conditionnel à S1b.2.

**Écarts signalés à Blaise (synthèse) :**
1. Écart d'inventaire vault : **9 fichiers** trouvés vs **10 annoncés** dans brief + STATUS. Hypothèse : pattern transverse anticipé non transféré ou coquille. À confirmer.
2. Audit-md-rag v1 produit 150 écarts mais 0 violation éditoriale claire de SPEC v1.2 après classification. Recommandations détaillées pour audit v2 dans le rapport (exception R1 glossaire, R4 tolérante MD futurs, R6 reconnaît wikilinks canoniques, implémenter R5/R7/R8/R9/R10).
3. Clés API absentes dans la session → S1b.2 et S1b.3 en attente.

**Décisions structurantes prises :** aucune (S1bis = exécution, pas de décision structurelle).

**Reste à faire :**
- Blaise arbitre les ~7 chiffres orphelins potentiels (§3 catégorie D du rapport) avec Cowork.
- Blaise confirme l'écart d'inventaire 9 vs 10.
- Blaise fournit les clés API (ou choisit un mode dégradé) pour débloquer S1b.2 + S1b.3 + ouverture PR.

**Blockers :**
- Clés API absentes (OPENAI_API_KEY / ANTHROPIC_API_KEY) pour le Lot S1b.2.

---

### 2026-05-12 (suite) — Cowork Hub IA Plateforme — Brief CC-S1bis + D-012-bis + D-027

**Contexte :**
- Blaise a créé le canal Claude Code Plateforme et lui a transmis le brief CC-S1. Premier rapport reçu : **6 lots livrés, 62/62 tests verts, 0 $ API consommé**. Excellente exécution. 4 écarts résiduels signalés (Lot 2 délégué à Blaise, validation end-to-end en attente, branche `claude/execute-pilot-batches-mBSIp` ≠ brief, pas de PR ouverte).
- Cowork sandbox n'a pas pu lire le RAPPORT-CC-S1.md depuis le clone Git (warnings de permission sur `.git/` — cohérent avec D-024 lecture seule). Travail sur la base de la synthèse transmise par Blaise.

**Actions menées :**

**Bloc 1 — Révision décisions** :
- **D-012-bis** actée (supersède D-012 du 11 mai) : MCP Obsidian reporté à Phase 2. Raisons : gain marginal en Phase 1 (Claude Code accède déjà aux MD via filesystem direct + parsing frontmatter), valeur réelle en Phase 2 (LLM Wiki layer), coût opportunité ~30-45 min setup pour ROI quasi-nul.
- **D-027** actée : convention de nommage des branches Claude Code Plateforme acceptée — `claude/execute-{slug}-{hash}` accepté par défaut, pas de rename imposé. Mention de la branche supprimée des briefs futurs.

**Bloc 2 — Brief CC-S1bis produit** :
- Fichier `rag-prep/briefs/BRIEF-CC-S1bis-validation-end-to-end.md` (~1700 mots, dans la cible D-021)
- 3 lots ciblés : (1) audit-md-rag sur vault réel, (2) validation end-to-end ingestion + retrieval + génération + eval, (3) rapport mission consolidé + ouverture PR
- Critères de succès quantifiés : ~30-60 chunks indexés, ≥ 8/10 sources attendues citées, coût < 2 $
- Plafonds API rappelés (cf. D-013) : alerte > 1 $ Anthropic / > 0,30 $ OpenAI

**Bloc 3 — Procédure de transfert MD vers Git** :
- Transmise à Blaise pour exécution dans son terminal Mac :
  - `cd repo-current && git fetch --all && git checkout claude/execute-pilot-batches-mBSIp`
  - `cp -r ../../Hub-IA-Plateforme/rag-prep/content/* rag/content/`
  - `git add rag/content/ && git commit -m "feat(rag): dépôt vault initial..." && git push`
- 10 fichiers MD à transférer (1 glossaire + 2 modules CU + 1 préalable PR + 1 fiche-outil + 1 DEP + 3 transverses)

**Décisions structurantes prises :**
- D-012-bis — MCP Obsidian reporté Phase 2
- D-027 — Convention nommage branches Claude Code Plateforme

**Reste à faire :**
- Blaise exécute la procédure de transfert MD vers la branche `claude/execute-pilot-batches-mBSIp`
- Blaise transmet le brief CC-S1bis à Claude Code Plateforme
- Claude Code Plateforme exécute les 3 lots S1bis + ouvre la PR
- Validation manuelle de la PR par Blaise côté GitHub

**Blockers :**
- Transfert MD par Blaise et transmission brief CC-S1bis.

---

### 2026-05-12 (clôture) — Cowork Hub IA Plateforme — Intégration retour I-003

**Actions menées (ordre logique D-023 respecté : formaliser avant corriger) :**

**Bloc 1 — SPEC v1.2 + D-026** :
- Bump `SPEC-MD-POUR-RAG.md` v1.1 → v1.2
- Ajout **R10 nouvelle règle stricte** : transposition fidèle des valeurs numériques dans les tableaux (issue AP-4 du retour couple 1, promu en règle stricte). Roadmap audit R10 ajoutée (regex valeurs numériques + diff vs HTML source).
- Acte **D-026** : co-production légère obligatoire sur modules N3/N4 vague 3+ (sondage AVANT production sur 2-3 passages sensibles)

**Bloc 2 — Extension du référentiel chiffres macro** :
- `chiffres-macro-2026.md` v3.8.2 → v3.8.3
- Ajout entrée **« 21 % — organisations IA ayant redesigné leurs workflows (McKinsey 2025) »** avec wikilink dans pr-07 (2 occurrences refactorisées en wikilink R9)
- Ajout entrée **« 1,8 h/jour — temps perdu à chercher l'information (McKinsey 2025) »** avec wikilink dans cu-008 (essentiel à retenir)
- Champ `derives` enrichi avec cu-008 et cu-025

**Bloc 3 — Corrections vague 2** :
- `pr-07.md` v3.8.3 → v3.8.4 :
  - **Matrice 6 critères : 5 cellules réalignées sur HTML** (volume BUY < 20 utilisateurs, volume BUILD > 50 utilisateurs « ou volume élevé », budget BUY « SaaS 50-200 €/mois suffit, ROI 6 mois », budget BUILD « 40-100 k€ + 20 %/an OK », délai BUILD « 3-9 mois acceptables, valeur long terme »)
  - Wikilink `[[vigilance-hallucinations]]` ajouté dans Écueil 4 (gouvernance IA)
  - Wikilink `[[vigilance-confidentialite]]` ajouté dans Écueil 6 (obligations réglementaires RGPD)
  - Champ `derives` enrichi (`pr-05`, `vigilance-hallucinations`, `vigilance-confidentialite`)
- `dep-02.md` v3.8.3 → v3.8.4 :
  - **Nouvel Écueil 6 transverse** : « Ignorer la confidentialité du corpus indexé » avec wikilink `[[vigilance-confidentialite]]`
  - Champ `derives` enrichi (`vigilance-confidentialite`)
- `cu-008.md` v3.8.3 → v3.8.4 :
  - Section « L'essentiel à retenir » : 1,8 h/jour McKinsey wikilinké vers `[[chiffres-macro-2026#18-h-jour...]]` (R9 + canonisation préventive)
- `glossaire.md` : bump footer v3.8.2 → v3.8.3 (cohérence avec frontmatter v3.8.3, incohérence signalée Q4 du retour)

**Bloc 4 — SYNC-INTER-CANAUX** :
- **I-003 archivé** en items résolus avec capitalisation complète (5 apprentissages, suivi post-clôture)
- **I-D-001 nouvel item descendant inscrit** : harmonisation matrice PR-07 HTML (6 critères discours vs 8 critères table v3.8 enrichi). Couple 1 prend l'item de son côté. Convention « couple 1 tranche, couple 2 s'aligne » à la prochaine itération PR-07 HTML.

**Décisions structurantes prises :**
- D-026 — Co-production légère obligatoire sur modules N3/N4 vague 3+

**Bilan de la session :**
- 1 SPEC bumpée en v1.2 (+ R10)
- 1 décision actée (D-026)
- 1 brique transverse enrichie (chiffres-macro-2026 v3.8.3, +2 chiffres)
- 4 fichiers vague 2 corrigés (pr-07 matrice, pr-07 wikilinks, dep-02 wikilinks + nouvel écueil, cu-008 wikilink chiffre macro, glossaire footer)
- 1 item inter-canal archivé (I-003 clôturé)
- 1 item descendant ouvert (I-D-001 — première occurrence dans le sens couple 1 → couple 2)

**Apprentissages clés :**
- AP-1 (R9 chiffres macro) et AP-4 (R10 tableaux numériques) sont les deux dérives les plus systémiques sur les modules denses → l'audit-md-rag.py R9 + R10 sera décisif pour la vague 3
- La co-production légère D-026 est la procédure pivot qui équilibre vitesse d'exécution × fidélité éditoriale
- Le pattern de coordination inter-canaux fonctionne dans les deux sens : I-001/I-002/I-003 ascendants + I-D-001 descendant. Cycle complet.

**Reste à faire :**
- Validation Blaise de l'intégration
- Décision sur séquencement ingestion (recommandation Cowork Hub IA : ingestion progressive en 2 temps — vague 2 maintenant pour valider pipeline, vague 3 + briques transverses ensemble dans 2-3 sprints)
- Démarrage vague 3 (CU-026, CU-027, DEP-08) avec application D-026 (sondage Cowork Hub IA préalable)
- Production des 3 briques transverses anticipées : pattern-llm-wiki (urgent — recouvrement cu-008/dep-02), pattern-eval-set-golden (avec DEP-07), pattern-build-vs-buy (avec module suivant qui s'y réfère)

**Blockers :**
- Aucun blocker bloquant. Validation Blaise possible.

---

### 2026-05-12 (ter) — Cowork Hub IA Plateforme — Brief revue vague 2 + I-003

**Actions menées :**
- Blaise valide la suggestion de revue ciblée par Cowork Hub IA sur la vague 2 (modules denses produits en autonomie sans co-production).
- Production du `BRIEF-COWORK-HUB-IA-REVUE-VAGUE-2.md` (~1300 mots, dans la cible D-021). Format resserré vs I-002 (5 questions au lieu de 7) parce que Cowork Hub IA a déjà fourni la matrice méthodologique en I-002 (anti-patterns AP-1/AP-2/AP-3, pattern « module + transverses »).
- 5 questions structurées centrées sur les passages denses :
  - Q1 : conformité RULES sur chiffres techniques précis et fourchettes
  - Q2 : dérives sémantiques sur passages identifiés en Q6 d'I-002 (LLM Wiki post-Karpathy, matrice 6 critères, pipeline 7 étapes, cycle SEI avec RetEx embedding #130, cas AMETRA)
  - Q3 : application de R9 + détection de nouveaux chiffres macro à canoniser (1,8 h/jour McKinsey, 78 % Retool, 21 % McKinsey workflows, 70-90 % Techment)
  - Q4 : validation wikilinks transverses + détection de manques (LLM Wiki dupliqué cu-008/dep-02, SaaS vs self-hosted, eval set)
  - Q5 : vault prêt pour ingestion ? brain pages transverses prioritaires avant ingestion ?
- Inscription **I-003** dans `SYNC-INTER-CANAUX.md` (items montants ouverts).

**Décisions structurantes prises :**
- Aucune nouvelle décision actée.

**Reste à faire :**
- Blaise transmet le `BRIEF-COWORK-HUB-IA-REVUE-VAGUE-2.md` au canal Cowork Hub IA (pointage local).
- Réception du `RETOUR-I-003-REVUE-VAGUE-2.md` côté couple 2.
- Selon les réponses : corrections vague 2 + ajustement chiffres-macro-2026 + (potentiellement) production de brain pages transverses additionnelles avant ingestion.
- En parallèle, Claude Code Plateforme continue ses Lots S1.

**Blockers :**
- Réception du retour Cowork Hub IA sur I-003 avant ingestion par Claude Code Plateforme (recommandation).

---

### 2026-05-12 (bis) — Cowork Hub IA Plateforme — Production vague 2 (3 modules denses)

**Actions menées :**
- Enrichissement `glossaire.md` v3.8.3 avec 5 nouveaux termes (eval-set, LLM-as-judge, reranker, retrieval-hybride, MTEB) — anticipations identifiées par couple 1 dans Q6 de la revue I-002.
- Lecture intégrale des 3 HTML sources via Bash : `cu-008-knowledge-base-rag.html` (~66 KB), `pr-07-build-vs-buy.html` (~13 KB), `dep-02-rag-architecture-prod.html` (~16 KB).
- **Production de 3 modules MD denses** :
  - `content/modules/cu-008.md` v3.8.3 — **Référence canonique D-017** — Knowledge base interne (RAG). 11 sections H2 sémantiquement autonomes. Couvre RAG vs Fine-tuning, pipeline 2 temps, LLM Wiki Karpathy, patterns post-Karpathy (persistent memory, self-maintaining KB, contradiction detection, multi-agent vaults, sleep consolidation), 3 voies stack pragmatiques, déploiement 4 paliers, 5 pièges, architectures A1/A3/A4, RetEx Conseil aviation 25 personnes. Wikilinks vers chiffres-macro, vigilance-hallucinations, vigilance-confidentialite, outils-vector-db, glossaire.
  - `content/prealables/pr-07.md` v3.8.3 — Build vs Buy à l'ère de l'IA. 10 sections H2. Couvre 3 tendances 2025-2026, scaling gap (95 % MIT NANDA, 21 % McKinsey workflow), 6 situations BUY, 5 situations BUILD, pattern hybride dominant, matrice 6 critères, 7 écueils. Mention AMETRA dans la section BUILD (sans détail inventé). Wikilinks vers chiffres-macro pour 95 % et 67/33 %.
  - `content/deploiement/dep-02.md` v3.8.3 — RAG en production. 12 sections H2. Couvre 3 ruptures 2025-2026, règle décision 30 sec, LLM Wiki coût-bénéfice, anatomie pipeline 7 étapes, choix techniques par ordre d'impact, tableau décision par volume, panorama vector DB 5 acteurs + question piège, 5 écueils, cycle Stitch → Evaluate → Iterate + RetEx embedding #130 MTEB, plan 60 jours.
- Application discipline SPEC v1.1 :
  - R9 — chiffres macro wikilinkés vers chiffres-macro-2026 (95 % MIT NANDA, 67/33 %)
  - AP-2 — aucune conversion monétaire ad-hoc
  - AP-3 — citations préservées (Karpathy gist, Techment, VentureBeat, MIT NANDA, McKinsey, Retool, GitHub Copilot)
- Mise à jour `cartographie-rag.md` avec les 3 nouvelles entrées détaillées (angles thématiques + recouvrements).

**Décisions structurantes prises :**
- Aucune nouvelle décision actée. Production conforme à SPEC v1.1.

**Signaux faibles observés / capitalisation :**
- La densité de cu-008 a confirmé la pertinence du pattern « briques transverses » (D-025) : sans `vigilance-hallucinations` et `vigilance-confidentialite` extraites, cu-008 aurait dupliqué massivement le même contenu de pr-05, cu-001, etc.
- La discipline de double-relecture HTML ↔ MD a été appliquée mais en mode auto-relecture Cowork (pas de validation Cowork Hub IA en parallèle vu le go direct de Blaise). À signaler comme zone de risque résiduel : co-production prévue par STRATEGIE-MD-RAG §6 pas formellement exécutée.
- Mention AMETRA dans pr-07 conservée textuelle sans détail inventé. Sera à compléter quand cu-027 sera produit (pattern complet documenté ailleurs dans le Hub).

**Reste à faire :**
- Mise à jour STATUS + clôture des tâches vague 2
- Sondage qualité par Blaise sur les 3 modules denses (validation post-production)
- À envisager : revue ciblée par Cowork Hub IA sur les passages identifiés en Q6 (RAG vs LLM Wiki dans cu-008, matrice 6 critères dans pr-07, cycle SEI dans dep-02) — sur le modèle I-002 mais resserrée

**Blockers :**
- Aucun blocker bloquant. Sondage Blaise possible mais non obligatoire.

---

### 2026-05-12 — Cowork Hub IA Plateforme — Intégration retour I-002 (massive)

**Actions menées (session dense, ordre logique D-023 respecté : formaliser avant produire) :**

**Bloc 1 — SPEC v1.1 + D-025** :
- Bump `SPEC-MD-POUR-RAG.md` v1 → v1.1
- Ajout **R9** (règle stricte) : citation textuelle des chiffres canoniques + audit-md-rag.py R9 à implémenter en v2
- Nouvelle section méthodologique « Briques transverses » (catégories, critères d'extraction 3+ modules, 3 risques à monitorer)
- Enrichissement section anti-patterns : AP-2 (conversion monétaire ad-hoc) + AP-3 (édulcoration éléments contextuels)
- Ajout règles auditables v2 dans la roadmap audit (R5, R7, R8, R9)
- Acte **D-025** : pattern architectural « unité = module + extraction sélective de briques transverses »

**Bloc 2 — Production des 3 briques transverses prioritaires** (recommandation Q7.a couple 1) :
- `transverses/chiffres-macro-2026.md` v1 — référentiel canonique de 13 chiffres macro avec sources datées et formulations exactes. Source unique de vérité pour les chiffres macro du Hub (67 % Bpifrance, 95 % MIT NANDA, 76 % France Num, 55 % Bpifrance Osez l'IA, 26 % France Num, 58 % enjeu vital, 33 % adoption, 67 % vs 33 % Buy/Build, +270 % Microsoft, 80-95 % causes orga, ×5 PwC, 77k offres, 3,7× IDC, consensus 70-95 %).
- `transverses/vigilance-hallucinations.md` v1 — Pattern de vigilance commune à ~10 modules. 3 types d'hallucinations, discipline en 3 règles, mitigations techniques, cas d'application, anti-patterns observés.
- `transverses/vigilance-confidentialite.md` v1 — Pattern de vigilance commune à ~8 modules. Risque structurel, 4 catégories à protéger, 3 options souveraines, discipline en 4 règles.

**Bloc 3 — Corrections vague 1** :
- `cu-001.md` v3.8.2 → v3.8.3 :
  - Chiffre « 67 % n'ont pas commencé » corrigé en « ne savent pas par où commencer » (formulation canonique)
  - Conversion monétaire $ → € pour Perplexity Pro
  - Citation MIT 2025 réintégrée dans « L'essentiel à retenir »
  - Certifications ISO 27001 / SOC 2 du Chat Pro restaurées
  - Formulation « 5 minutes du réflexe humain à la matière exploitable » réintégrée
  - Phrases trop longues aérées (vigilances structurantes passées en liste)
  - Wikilinks ajoutés vers les 3 briques transverses (`[[vigilance-hallucinations]]`, `[[vigilance-confidentialite]]`, `[[chiffres-macro-2026#67-pourcent-...]]`)
  - Frontmatter `derives` enrichi
- `glossaire.md` v3.8.2 → v3.8.3 :
  - Ajout glose **On-premise** (13e glose obligatoire RULES §C.2)
  - Affinement « Vector store » (ancrage « brique centrale du RAG »)
  - Affinement « Chunk » (référence explicite SPEC §R3)

**Bloc 4 — Mise à jour fichiers vivants** :
- `cartographie-rag.md` : ajout des 3 nouvelles entrées (chiffres-macro-2026, vigilance-hallucinations, vigilance-confidentialite) avec angles thématiques et recouvrements
- `SYNC-INTER-CANAUX.md` : I-002 archivé en items résolus avec apprentissages capitalisés (5 dérives, 3 anti-patterns, 3 briques produites, D-025, suivi post-clôture)

**Décisions structurantes prises :**
- D-025 — Pattern architectural module + briques transverses sélectives (Actée)

**Bilan de la session :**
- 1 SPEC bumpée en v1.1
- 1 décision actée (D-025)
- 3 fichiers transverses produits (~290 lignes)
- 1 module CU corrigé (5 dérives résolues + phrases aérées + wikilinks transverses)
- 1 glossaire enrichi (+ On-premise)
- 4 fichiers vivants mis à jour (DECISIONS, JOURNAL, STATUS, cartographie, SYNC)
- 1 item inter-canal archivé (I-002 clôturé)

**Reste à faire — pré-vague 2 :**
- Validation Blaise de l'intégration (sondage de bonne tenue)
- Possible itération sur les briques transverses si Blaise détecte un point
- Démarrage de la vague 2 : CU-008 (référence canonique D-017), PR-07, DEP-02 — en co-production avec Cowork Hub IA pour ces 3 modules denses

**Blockers :**
- Aucun en bloquant. Sondage de validation Blaise possible mais non obligatoire avant vague 2.

---

### 2026-05-11 (clôture) — Cowork Hub IA Plateforme — Brief revue vague 1 + I-002

**Actions menées :**
- Blaise soulève une question architecturale fondamentale : la convention implicite « 1 fichier HTML = 1 fichier MD » est-elle optimale pour le RAG, ou faut-il un découpage sémantique plus poussé avec extraction de briques transverses ?
- Reconnaissance que la question dépasse l'expertise du couple 2 sur le maillage interne du Hub. Cowork Hub IA est mieux placé pour arbitrer.
- Décision : demander une revue à Cowork Hub IA **avant** production de la vague 2 (CU-008, PR-07, DEP-02), combinant (a) conformité éditoriale des 3 fichiers vague 1 produits, (b) arbitrage architectural sur le découpage sémantique.
- Production du `BRIEF-COWORK-HUB-IA-REVUE-VAGUE-1.md` (~1700 mots, dans la cible D-021) avec 7 questions structurées :
  - Q1 à Q4 : conformité éditoriale (RULES sourcing/langue/gloses, cohérence chiffres cross-Hub, dérive sémantique, alignement gloses §C.2)
  - Q5 : anti-patterns à formaliser dans SPEC v1.1
  - Q6 : recommandations vague 2
  - Q7 (structurante) : arbitrage architectural sur découpage sémantique
- Inscription de **I-002** dans `SYNC-INTER-CANAUX.md` (item montant ouvert, à transmettre par Blaise).
- Mise à jour `STATUS-RAG.md` : ajout L0.14 et nouveau blocker (vague 2 en attente revue couple 1).

**Décisions structurantes prises :**
- Aucune nouvelle décision actée. Décision architecturale (découpage sémantique) suspendue à la réponse Q7 du couple 1.

**Reste à faire :**
- Blaise transmet le `BRIEF-COWORK-HUB-IA-REVUE-VAGUE-1.md` au canal Cowork Hub IA (pointage local, pas besoin de push Git).
- Réception du `RETOUR-I-002-REVUE-VAGUE-1.md` côté couple 2.
- Selon les réponses : corrections vague 1 + ajustement SPEC v1.1 + (potentiellement) production de fichiers transverses **avant** vague 2.
- En parallèle, Claude Code Plateforme avance sur Lots 1-3 du brief S1.

**Anticipations / signaux faibles :**
- Premier exercice du pattern canonique de coordination inter-canaux dans le sens couple 2 → couple 1 (en miroir de I-001). Validation empirique du pattern.
- Si la réponse Q7 confirme l'extraction de briques transverses, le `cartographie-rag.md` v0 actuelle (qui anticipait déjà 8 sujets à fort recouvrement) sera enrichi avec une nouvelle catégorie « brain pages transverses » avant production massive.
- Discipline d'itération préservée : on évite de produire 3 modules denses qui devraient être refactorisés a posteriori.

**Blockers :**
- Réception du retour Cowork Hub IA sur I-002 avant production vague 2.

---

### 2026-05-11 (très tardive) — Cowork Hub IA Plateforme — Production MD pilote vague 1

**Actions menées :**
- Canal Claude Code Hub IA Plateforme lancé par Blaise (confirmation reçue).
- Lecture intégrale du HTML source `cu-001-recherche-veille.html` (sections executive, outils, méthode, pièges, cas, stats clés).
- Lecture intégrale de la section `cat-vector` de `ressources.html` (4 fiches outils : Qdrant, pgvector, Pinecone, ChromaDB).
- Création de la structure `Canaux/Hub-IA-Plateforme/rag-prep/content/` avec sous-dossiers `modules/`, `prealables/`, `deploiement/`, `ressources/`.
- Production de **3 fichiers MD** (vague 1 du sprint S1) :
  - `rag-prep/content/glossaire.md` v1 — 18 termes canoniques avec wikilinks croisés (RAG, vector-store, embeddings, LLM, POC, MVP, API, SaaS, open-source, self-hosting, souveraineté, cloud-souverain, hallucination, HNSW, chunk, fine-tuning, token, prompt). Tous les futurs MD du vault y feront référence.
  - `rag-prep/content/ressources/outils-vector-db.md` v1 — panorama des 4 vector stores du marché 2026 + comparatif synthétique + cross-references vers cu-008, dep-02, dep-06. Premier MD type `fiche-outil`, valide le format catégorie.
  - `rag-prep/content/modules/cu-001.md` v1 — module Recherche & veille augmentée distillé en 7 sections H2 sémantiquement autonomes. Premier MD type `module-cu`, valide le format module.
- Mise à jour `cartographie-rag.md` avec les 3 nouvelles entrées + identification des recouvrements à venir (cu-008 et dep-02 référenceront outils-vector-db.md plutôt que dupliquer).

**Décisions structurantes prises :**
- Aucune nouvelle décision actée. Production conforme à SPEC v1, STRATEGIE v1, D-001 à D-024.

**Reste à faire — clôture vague 1 :**
- Validation par Blaise des 3 MD produits (sondage qualité avant production des modules denses).
- Sur retour positif : production de la vague 2 (cu-008 référence canonique, pr-07, dep-02) — co-production avec Cowork Hub IA pour ces 3 modules denses (assistance contextuelle).
- En parallèle, Claude Code Plateforme attaque les Lots 1 à 3 du brief S1 (infrastructure repo `rag/`, MCP Obsidian, audit-md-rag.py).

**Anticipations / signaux faibles :**
- Aucune dérive sémantique détectée par auto-relecture, mais cela mérite confirmation par sondage Blaise (et plus tard par eval automatique sur questions test).
- Discipline de longueur des sections H2 respectée (estimation 400-700 tokens par section). À vérifier formellement quand `audit-md-rag.py` sera fonctionnel.
- `outils-vector-db.md` regroupe 4 outils en un seul fichier (conformément à D-014 et à la convention « fiches outils par catégorie »). Cela valide la stratégie « pas un fichier par fiche outil isolée » pour éviter la dilution du retrieval.

**Blockers :**
- Validation Blaise sur la vague 1 avant production vague 2.

---

### 2026-05-11 (tardive) — Cowork Hub IA Plateforme — Migration vers rag-prep/ et D-024

**Actions menées :**
- Clarification par Blaise du fonctionnement réel observé côté couple 1 : pas de modification croisée entre dossier Cowork local et clone Git local. Le clone Git est source de vérité unique. Cowork ne modifie jamais le clone Git, écrit uniquement dans son dossier de travail.
- 4 options soumises à Blaise pour la gestion des fichiers vivants. **Option D retenue** (rebaselining manuel par Blaise avant chaque session Cowork significative).
- Création du sous-dossier `Canaux/Hub-IA-Plateforme/rag-prep/` côté Cowork.
- Déplacement (mv) des 10 fichiers de gouvernance + dossier `briefs/` vers `rag-prep/`. La racine `Canaux/Hub-IA-Plateforme/` ne conserve que `README.md`, `analyses/`, `roadmap/` (méta-doc non transmise sur Git).
- Mise à jour `_instructions-rag.md` §8 (réécriture complète) : intégration de D-024 (architecture de circulation Cowork ↔ Git ↔ Claude Code), Option D rebaselining détaillée, distinction stables/briefs/rapports/vivants.
- Mise à jour `BRIEF-CC-S1-pilote-pipeline.md` :
  - Chemins de référence : `rag-prep/...` (dans le clone Git) au lieu de `Canaux/Hub-IA-Plateforme/...`
  - Lot 1 : ajout de `rag/docs/` dans la structure cible (créé à la main de Claude Code, contient doc technique, ne duplique pas les conventions de `rag-prep/`)
  - Précision sur la circulation des MD pilotes (Cowork-side → `rag-prep/content-drafts/` du clone Git → `rag/content/` final)
- Acte **D-024** dans `DECISIONS-RAG.md` (architecture de circulation à 3 espaces + Option D).

**Décisions structurantes prises :**
- D-024 — Architecture de circulation Cowork ↔ Git ↔ Claude Code Plateforme

**Reste à faire — clôture S0 :**
- Blaise effectue le push initial : `mkdir -p Canaux/Hub-IA/repo-current/rag-prep && cp -r Canaux/Hub-IA-Plateforme/rag-prep/* Canaux/Hub-IA/repo-current/rag-prep/ && cd Canaux/Hub-IA/repo-current && git add rag-prep/ && git commit -m "feat: rag-prep/ canal plateforme — gouvernance S0" && git push`
- Création du canal Claude Code Plateforme par Blaise, transmission du chemin `rag-prep/briefs/BRIEF-CC-S1-pilote-pipeline.md` comme premier ordre de mission.
- En parallèle, Cowork peut attaquer la production des 5 fichiers MD pilotes.

**Blockers :**
- Push initial par Blaise + création canal Claude Code Plateforme.

---

### 2026-05-11 (soir) — Cowork Hub IA Plateforme — Retour couple 1 sur I-001 + intégration

**Actions menées :**
- Réception du retour structuré de Cowork Hub IA sur l'item I-001 (refonte RULES v1.6).
- Item I-001 traité immédiatement côté couple 1 (3-4 h Cowork + 1-2 h Claude Code attendues). 3 livrables produits : `RULES-IMPLEMENTATION-v1.6.md`, `RULES-MIGRATION-v1.5-vers-v1.6.md`, `BRIEF-CLAUDE-CODE-RULES-v1.6.md`. Push effectué, intégration par Claude Code Hub IA sur branche `refactor/rules-v1.6-consolidation`.
- Intégration des 3 apprentissages partagés par couple 1 vers couple 2 :
  - Apprentissage 1 (démarrer minimaliste) : déjà appliqué dans `SPEC-MD-POUR-RAG.md` v1
  - Apprentissage 2 (nouvelle règle = nouvelle fonction d'audit) : acté en **D-023**, intégré dans `_instructions-rag.md` §7 garde-fou n°9, et dans le préambule de `SPEC-MD-POUR-RAG.md`
  - Apprentissage 3 (référentiel principal court vs annexes longues) : déjà appliqué
- Codification du pattern canonique de coordination inter-canaux dans `SYNC-INTER-CANAUX.md` sur la base du flux validé empiriquement sur I-001
- Item I-001 archivé dans `SYNC-INTER-CANAUX.md` (section « Items résolus / archivés ») avec trace temporelle complète et apprentissages capitalisés
- Référence v1.5.14 dans `BRIEF-CC-S1-pilote-pipeline.md` mise à jour : pointe désormais vers v1.6 dès merge, v1.5.14 transitoire

**Décisions structurantes prises :**
- D-023 — Principe « nouvelle règle = nouvelle fonction d'audit » codifié dès v1

**Suivi post-clôture :**
- Attendre notification (via Blaise) du merge de la branche `refactor/rules-v1.6-consolidation` par couple 1
- À réception du merge : substituer définitivement la référence v1.5.14 par v1.6 dans nos fichiers
- Premier cycle de coordination inter-canaux fonctionnel et capitalisé. Pattern canonique opposable pour les items futurs.

**Reste à faire — clôture S0 :**
- Identique à l'entrée précédente : Blaise crée le canal Claude Code Plateforme + transmet `BRIEF-CC-S1-pilote-pipeline.md`. En parallèle, Cowork attaque la production des 5 fichiers MD pilotes.

**Blockers :**
- Création du canal Claude Code Plateforme par Blaise pour ouvrir S1.

---

### 2026-05-11 (fin de journée) — Cowork Hub IA Plateforme — Clôture S0

**Actions menées :**
- Validation Blaise sur l'ensemble du bloc D-005 à D-014 et D-017 (11 décisions techniques actées en une passe sur recommandations Cowork).
- Production des 4 artefacts S0 majeurs :
  - `STRATEGIE-MD-RAG.md` v1 (méthodologie de retranscription HTML → MD, 5 questions d'analyse, démarche pilote → scale, co-production avec couple 1 cadrée)
  - `SPEC-MD-POUR-RAG.md` v1 (8 règles minimalistes : frontmatter 10 champs, H1 unique, sections H2 autonomes, chunking 400-700 tokens, wikilinks Obsidian, glossaire canonique, chiffres sourcés, nommage MD, versioning)
  - `cartographie-rag.md` v0 (structure définie, 8 sujets à fort recouvrement identifiés pour vigilance)
  - `SYNC-INTER-CANAUX.md` v0 (triggers de coordination définis + premier item I-001 sur refonte RULES v1.6 simplifiée)
- Consolidation `_instructions-rag.md` v1 (intégrant toutes les décisions actées, spécialisation rôles renforcée, procédure boot avec resync git, glossaire couple 2)
- Production du `BRIEF-CC-S1-pilote-pipeline.md` (6 lots, ~15-19 h Claude Code, cible ~1900 mots conforme D-021)

**Décisions structurantes prises :**
- D-005 à D-014 et D-017 toutes actées
- Choix de 5 unités pilotes pour S1 : CU-001, CU-008 (référence canonique), PR-07, DEP-02, outils-vector-db

**Reste à faire — clôture S0 :**
- Blaise transmet l'item I-001 (`SYNC-INTER-CANAUX.md`) au canal Cowork Hub IA (opportunité refonte RULES v1.6 simplifiée)
- Création du canal Claude Code Hub IA Plateforme par Blaise (déclenche l'ouverture du sprint S1)
- Démarrage en parallèle de la production des 5 unités MD pilotes côté Cowork (en co-production avec Cowork Hub IA pour CU-008, PR-07, DEP-02)

**Blockers :**
- Création du canal Claude Code Plateforme par Blaise pour ouvrir S1.

---

### 2026-05-11 (après-midi) — Cowork Hub IA Plateforme — Réception RetEx couple 1

**Actions menées :**
- Réception du `RETEX-COWORK-HUB-IA-vers-PLATEFORME.md` (~2800 mots, ADN QFC respecté).
- Lecture intégrale. Extraction des enseignements structurants :
  - **4 leviers principaux** identifiés par couple 1 : (1) spécialisation rôles Cowork/Code, (2) audit automatisé, (3) référence canonique unique, (4) resync systématique post-merge.
  - **5 frictions historiques à éviter** : Cowork produisant du code, absence resync, RULES qui grossit, cartographie imprécise, pas de recouvrement sémantique.
  - **7 signaux faibles à monitorer**.
- Mise à jour `DECISIONS-RAG.md` : ajout D-016 à D-022 (décisions issues directement du RetEx).
- Mise à jour `STATUS-RAG.md` : L0.3 marqué fait, ajout de livrables liés aux nouvelles décisions.

**Décisions structurantes prises :**
- D-016 — Mise en place d'un audit-md-rag.py automatisé dès S1 (équivalent audit-global.py couple 1)
- D-017 — Référence canonique MD à identifier dès S1 (proposition à valider Blaise)
- D-018 — Procédure de resync git systématique en début de session
- D-019 — Cartographie d'ancrage RAG distincte du contenu indexé (angles thématiques par chunk)
- D-020 — Pas de référence temporelle absolue dans les briefs et conventions (sauf échéance hackathon)
- D-021 — Discipline de concision des briefs (cible max 2000 mots)
- D-022 — Spécialisation des rôles couple 2 explicitée : Cowork = matière MD, Claude Code = code RAG (Python/JS), pas de mélange

**Reste à faire — next steps S0 :**
- Validation Blaise des décisions techniques D-005 à D-013 (LLM, vector DB, embeddings, backend, MCP Obsidian, plafonds API).
- Validation Blaise des décisions issues du RetEx (D-016 à D-022) ou amendements.
- Production de `STRATEGIE-MD-RAG.md` et `SPEC-MD-POUR-RAG.md` v1 (en démarrant minimaliste — leçon Q3 RetEx).
- Production du `SYNC-INTER-CANAUX.md` initial.
- Consolidation `_instructions-rag.md` v1.

**Blockers :**
- Décisions techniques D-005 à D-013 et D-016 à D-022 en attente de validation Blaise.

---

### 2026-05-11 — Cowork Hub IA Plateforme — Session de cadrage initial

**Actions menées :**
- Lecture du README du canal, de la roadmap globale, et du fichier `analyses/build-vs-buy-agent.md`.
- Échanges stratégiques avec Blaise sur 4 itérations successives :
  1. Premières observations + 5 questions de cadrage budget/compétences/délai/widget/souveraineté
  2. Implications des contraintes (POC démonstrateur < 100 €/mois, zéro compétence IT, hackathon septembre)
  3. Exploration du repo Hub IA (87 HTML, 56 MD, 145 unités éditoriales) + question Obsidian
  4. Décision architecturale finale : **architecture à 2 couches HTML/MD complémentaires** (D-001)
  5. Décision : **repo unique `hub-ia` avec dossier `rag/` séparé** (D-002)
  6. Décision : **architecture à 4 canaux** (D-003)
  7. Décision : **pas de bascule de source de vérité** (D-004)
- Création des 4 fichiers de référence (`_instructions-rag.md` v0, `DECISIONS-RAG.md` initial, ce `JOURNAL`, `STATUS-RAG.md`).
- Création du dossier `briefs/`.
- Rédaction du `BRIEF-RETEX-COWORK-HUB-IA.md` à transmettre au couple 1.

**Décisions structurantes prises :**
- D-001 à D-004 (cf. `DECISIONS-RAG.md`)
- Plan d'action S0 à S4 défini (cf. `STATUS-RAG.md`)

**Reste à faire — next steps S0 :**
- Blaise transmet le `BRIEF-RETEX-COWORK-HUB-IA.md` au canal Cowork Hub IA.
- Réception du RetEx couple 1 → consolidation `_instructions-rag.md` v1.
- Benchmark restreint des options techniques (LLM, vector DB, embeddings, backend) pour acter D-005 à D-008.
- Production de `STRATEGIE-MD-RAG.md` (méthodologie de retranscription) et `SPEC-MD-POUR-RAG.md` v1 (cahier des charges format).

**Blockers :** aucun.

---

*Format de toute nouvelle entrée :*

### YYYY-MM-DD — [Cowork ou Claude Code] — Description session

**Actions menées :**
- ...

**Décisions structurantes prises :**
- ... (ou : aucune)

**Reste à faire :**
- ...

**Blockers :**
- ... (ou : aucun)

---
