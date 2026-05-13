# BRIEF-CC-S2.2-Lot-E — Fix bug wikilinks + rejeu eval 30q + RAPPORT + PR finale

**Émetteur :** Cowork Hub IA Plateforme
**Destinataire mixte (D-030)** :
- **Claude Code Plateforme** (session web) : Lots E.1 et E.3 (refactor code + tests + RAPPORT + PR)
- **Claude Code Desktop** (local) : Lot E.2 (rejeu eval 30q après fix wikilinks)
- **Blaise** : coordination + sync ascendante + merge PR finale
**Garant transverse :** Blaise Cavalli
**Sprint :** S2.2 Lot E (clôture définitive S2.2)
**Statut :** v1, à transmettre

---

## 1. Métadonnées

- **Repo cible :** `hub-ia`, branche `claude/execute-pilot-batches-mBSIp` (post-commits Lots A+B+C+D)
- **Sprint précédent :** S2.2 Lot D (Desktop) — eval partiel q-016 → q-030, 9/15 sources retrouvées, bug d'extraction wikilinks identifié, RAPPORT à finaliser
- **Nature de l'itération :** fix critique du bug d'extraction wikilinks dans `query.py` + rejeu eval 30q + RAPPORT consolidé + PR finale S2.2 vers main
- **Coût API attendu** : Plateforme 0 $ (refactor + tests mockés), Desktop ~0,75 $ Anthropic + ~0,001 $ OpenAI (rejeu eval 30q)

---

## 2. Contexte court — le bug structurant à fixer

Le Lot D (Desktop) a livré un eval partiel sur 15 questions (q-016 → q-030) et a découvert un **bug structurant** : `query.py` ne capte pas les wikilinks Obsidian de forme `[[code#ancre]]` dans le champ `cited_codes`.

**Évidence concrète** (du RAPPORT Desktop) :
- **q-016** : la réponse contient `[[chiffres-macro-2026#18-h-jour-mckinsey-2025]]` (wikilink avec ancre) mais `cited_codes=['cu-008', 'cu-001']` — chiffres-macro-2026 absent
- **q-021** : la réponse contient `[[dep-02#cycle-stitch-evaluate-iterate]]` mais `cited_codes=[]` — dep-02 absent
- **q-027** : pattern identique sur chiffres-macro-2026

**Impact estimé** : sans ce bug, score subset q-016 → q-030 estimé ~12/15 sources (vs 9/15 mesuré). Cible adaptée 12/15 (80 %) atteinte après fix.

**Cause probable** : la fonction `extract_cited_codes(answer: str)` dans `rag/code/backend/query.py` (ligne 270) utilise une regex qui tronque sur `#` ou ne gère pas le pattern complet `[[code#ancre]]`. À investiguer en début de Lot E.1.

---

## 3. Préalable obligatoire (lectures avant exécution)

À lire dans cet ordre :

1. **Rapport Lot D côté Desktop** : `rag-prep/JOURNAL-POC-RAG.md` entrée « 2026-05-13 (S2.2 Lot D) » — diagnostic complet du bug + résultats partiels
2. **Rapport eval Lot D** : `rag/eval/eval-report-s2.2.md` + `rag/eval/eval-report-s2.2.json` (sera **écrasé** au Lot E.2 par le rejeu final — préserver les résultats partiels dans le RAPPORT-CC-S2.2 Lot E.3)
3. **Brief S2.2 source** : `rag-prep/briefs/BRIEF-CC-S2.2.md` (contexte original des 5 lots A→E)
4. **Code à patcher** : `rag/code/backend/query.py` ligne 270 (`extract_cited_codes`)
5. **Décisions et SPEC à respecter** : `rag-prep/_instructions-rag.md`, `rag-prep/DECISIONS-RAG.md` (30 décisions actées dont D-022 spécialisation rôles, D-024 architecture circulation, D-030 hybride), `rag-prep/SPEC-MD-POUR-RAG.md` v1.4
6. **STATUS** : `rag-prep/STATUS-RAG.md` — L1.26e marqué « Prêt pour Claude Code Plateforme »

**Audit de départ obligatoire** (D-018) : `git fetch && git status`, basculer sur la branche `claude/execute-pilot-batches-mBSIp` et `git pull`. Le tip de branche doit inclure le commit Desktop `f5e8e9b` (MAJ JOURNAL + STATUS post-Lot D).

---

## 4. Méthode — 3 sous-lots E.1, E.2, E.3

### Lot E.1 — Fix regex extract_cited_codes (Claude Code Plateforme web)

**Livrable** : refactor de `extract_cited_codes()` dans `rag/code/backend/query.py` pour reconnaître **tous les patterns** de citation présents dans les réponses Claude :

1. **Crochets simples** : `[cu-008]`, `[CU-008]`, `[pr-07]` (déjà géré dans v1)
2. **Wikilinks Obsidian sans ancre** : `[[cu-008]]`, `[[pattern-llm-wiki]]` (à vérifier — peut-être déjà géré)
3. **Wikilinks Obsidian avec ancre** : `[[chiffres-macro-2026#18-h-jour-mckinsey-2025]]`, `[[dep-02#cycle-stitch-evaluate-iterate]]` (**non géré actuellement, à ajouter**) — extraire le code avant `#`
4. **Wikilinks avec alias** : `[[cu-008|Knowledge base RAG]]`, `[[chiffres-macro-2026#...|95 % MIT NANDA]]` (à vérifier) — extraire le code avant `|` ou `#`

**Regex unifiée suggérée** (à valider en TDD) :
```python
# Crochets simples : [code]
PATTERN_BRACKETS = re.compile(r'\[([a-z0-9-]+(?:-\d+)?)\]', re.IGNORECASE)
# Wikilinks Obsidian : [[code]], [[code#ancre]], [[code|alias]], [[code#ancre|alias]]
PATTERN_WIKILINK = re.compile(r'\[\[([a-z0-9-]+(?:-\d+)?)(?:[#|][^\]]*)?\]\]', re.IGNORECASE)
```

Filtrer les matches selon une liste de codes valides (présents dans le vault) pour éviter les faux positifs sur du texte arbitraire entre crochets.

**Tests** : étendre `rag/code/backend/test_query.py` avec fixtures couvrant les 4 patterns + cas limites (code inexistant entre crochets ignoré, texte arbitraire ignoré, mixte crochets+wikilinks dans même réponse). Cibler ~5-8 nouveaux tests.

**Critères de succès** :
- 159 tests existants + 5-8 nouveaux verts
- Sanity check sur les 3 cas évoqués (q-016 / q-021 / q-027) : le fix doit extraire `chiffres-macro-2026` et `dep-02` quand le wikilink avec ancre est présent

**Commit attendu** : `fix(rag-backend): extract_cited_codes gère wikilinks Obsidian avec ancre et alias (s2.2 lot e.1)`

---

### Lot E.2 — Rejeu eval complet 30 questions (Claude Code Desktop)

**Préalable** : Blaise pull la branche en local après le push du Lot E.1, puis invoque Claude Code Desktop (qui doit relire le briefing inaugural si nouvelle session).

**Livrable Desktop** : rejeu complet de l'eval sur les 30 questions avec le `query.py` patché :

```bash
cd "/Users/quest/Cowork/Startup manager at Quai Alpha/Canaux/Hub-IA/repo-current"
source rag/code/.venv/bin/activate
git pull
python3 rag/code/eval/run_eval.py --questions rag/eval/questions.yaml --report rag/eval/eval-report-s2.2.md --json rag/eval/eval-report-s2.2.json
cat rag/eval/eval-report-s2.2.md
```

**Note importante** : le fichier `rag/eval/eval-report-s2.2.md` du Lot D **sera écrasé** par ce rejeu. C'est intentionnel — le rapport final S2.2 doit refléter l'évaluation post-fix. Les résultats partiels Lot D sont déjà consignés dans le JOURNAL (entrée 13 mai Desktop), pas besoin de les préserver dans un fichier dédié.

**Critères de succès Lot E.2** :
- **≥ 24/30 sources retrouvées** (cible brief initial atteinte, soit 80 %)
- **≥ 50 %** concepts attendus couverts par question
- Coût total Lot E.2 : ~0,75 $ Anthropic + ~0,001 $ OpenAI (re-indexation incrémentale = quasi-nulle vu que le vault n'a pas changé depuis Lot D ; les 30 queries Sonnet 4.6 consomment ~0,75 $)
- **Latence acceptée** : 12-18 sec/question (recalibrage explicite vs cible brief initial 5 sec — irréaliste pour Sonnet 4.6 sur ces volumes 3500 tokens in / 900 tokens out, observation Lot D)
- Push des artefacts sur la branche : `feat(rag-eval): S2.2 Lot E.2 rejeu eval 30q post-fix wikilinks`

**Si la cible 24/30 n'est PAS atteinte** : signalement à Blaise pour investigation. Le RAPPORT Lot E.3 doit alors analyser question par question.

---

### Lot E.3 — RAPPORT-CC-S2.2 consolidé + PR finale (Claude Code Plateforme)

**Livrable A** : `rag-prep/briefs/RAPPORT-CC-S2.2.md` (~2000-2500 mots, structure 8 sections) consolidant **toutes les étapes S2.2 du Lot A au Lot E** :

1. **Synthèse exécutive** : 5 lots traités (A+B Cowork + C Plateforme + D+E.2 Desktop + E.1+E.3 Plateforme), 4 commits + le tien + le rejeu, score eval final X/30
2. **Détail par lot** :
   - Lot A : pattern-llm-wiki + refactor cu-008/dep-02
   - Lot B : extension golden set 30q + **crash YAML int values** (commit `00d80e8` Desktop exception D-022)
   - Lot C : métriques coût (`_cost.py`), pre-commit hook, system prompt enrichi (commit `127de86`)
   - Lot D : eval partiel q-016 → q-030 (commit `fa8fc88`), 9/15 sources, **bug wikilinks identifié**
   - Lot E.1 : fix `extract_cited_codes` (ton commit)
   - Lot E.2 : rejeu eval 30q complet (commit Desktop)
3. **Résultats finaux eval 30q** : X/30 sources retrouvées, Y/30 concepts ≥ 50 %, latence moyenne, coût exact
4. **Coût API total cumulé S1+S2.1+S2.2** : ~0,30 $ (S1c.2) + ~0 $ (S2.1) + ~0,76 $ (S2.2 Lot D crash + Lot E.2 rejeu) ≈ **~1,06 $** sur ~8 $ crédits initiaux
5. **Écarts résiduels signalés à Blaise** :
   - Dépassement cap durci S2.2 Lot D (0,71 $ vs 0,50 $ Anthropic) — accepté ex-ante
   - Latence Sonnet 4.6 ~16 sec/question vs cible brief 5 sec — cible irréaliste pour ces volumes
   - Identité Git par défaut `Quest <quest@MacBook-Air-de-Quest.local>` — à arbitrer si configuration `user.name`/`user.email` souhaitée
6. **Propositions d'amendement SPEC v1.5** (à arbitrer Cowork) :
   - **AP-5 (anti-pattern golden set)** : « valeurs numériques dans `expected_concepts` du golden set doivent être quotées en YAML » — issue blocker Desktop q-016/q-019/q-027
   - **Recalibrage cible latence** dans les futurs briefs : 12-18 sec/question pour Sonnet 4.6 sur volumes ~3500 in / 900 out
   - Mention explicite du pattern wikilink `[[code#ancre]]` et `[[code|alias]]` à reconnaître par les regex d'extraction de citations
7. **Recommandations pour Sprint S2.3** :
   - Cible latence recalibrée
   - AP-5 ajouté à SPEC v1.5
   - Allocation D-030 : pattern Plateforme→Desktop pour eval (validé en S2.2) à appliquer en S2.3
8. **Liste complète des commits S2.2** + bilan global S1 + S2.1 + S2.2

**Livrable B** : Ouverture PR vers main :
- **Titre PR** : `feat(rag): Sprint S2.2 - pattern-llm-wiki + extension golden set 30q + métriques + pre-commit + eval extended`
- **Description PR** : pointer vers RAPPORT-CC-S2.2, lister les 7 commits (B7C7F96 + 127DE86 + 00D80E8 + FA8FC88 + F5E8E9B + commit Lot E.1 + commit Lot E.2), mentionner les évolutions structurantes (pattern-llm-wiki extrait, golden set 30q, métriques coût, pre-commit hook, fix wikilinks)
- **Pas de merge automatique** : Blaise valide manuellement.

**Commit attendu** : `docs(rag): rapport mission S2.2 + ouverture PR finale`

---

## 5. Estimation effort consolidée

| Sous-lot | Acteur | Effort estimé | Coût |
|---|---|---|---|
| E.1 — Fix regex wikilinks + tests | Claude Code Plateforme | 1-2 h | 0 $ |
| E.2 — Rejeu eval 30q | Claude Code Desktop | 30 min | ~0,75 $ |
| E.3 — RAPPORT + PR | Claude Code Plateforme | 1-2 h | 0 $ |
| **Total** | — | **~2,5-4,5 h split** | **~0,75 $** |

Coût total estimé S2.2 (Lot D + Lot E.2) : ~1,46 $ sur ~2,70 $ Anthropic restants. Cap mensuel 50 $ très loin.

---

## 6. Règles de prudence

1. **Pas de modification des MD du vault** (D-022). Le fix concerne uniquement `rag/code/backend/query.py`.
2. **Pas de modification de `questions.yaml`** : déjà corrigé par Desktop en Lot D (commit `00d80e8`).
3. **Plafonds Lot E.2** : alerte > **0,80 $ Anthropic** + > **0,15 $ OpenAI**. Si Sonnet 4.6 dépasse 25 sec/question en moyenne, signaler à Blaise.
4. **Pas de re-ingestion** : le vault est inchangé depuis Lot D. ChromaDB local contient déjà 121 chunks. Si le rejeu lance une re-indexation, il faut comprendre pourquoi (probable : config par défaut de `ingest.py` au démarrage de `run_eval.py`).
5. **Régression check** : après le fix wikilinks, vérifier que les 10 questions du golden set initial (q-001 à q-010) restent à 10/10 sources comme en S1c.2.
6. **Coordination Plateforme ↔ Desktop** : Blaise déclenche Desktop après push Plateforme Lot E.1. Pas d'auto-déclenchement.

---

## 7. Décisions explicites de NE PAS faire

1. ❌ Pas de modification de `questions.yaml` (déjà fixé Lot D Desktop)
2. ❌ Pas de modification du code de l'audit-md-rag (hors scope S2.2)
3. ❌ Pas de portage TypeScript / Cloudflare Worker (livrable S3)
4. ❌ Pas de configuration Git `user.name`/`user.email` côté Mac de Blaise (signaler dans RAPPORT, c'est sa décision)
5. ❌ Pas d'extension du golden set au-delà des 30 questions (livrable S2.3 ou S3 si pertinent)
6. ❌ Pas de merge automatique de la PR S2.2 (Blaise valide manuellement)

---

## 8. Validation finale avant clôture S2.2

**Lot E.1 (Plateforme)** :
- [ ] `extract_cited_codes` reconnaît `[code]`, `[[code]]`, `[[code#ancre]]`, `[[code|alias]]`
- [ ] 159 tests existants + ~5-8 nouveaux verts (~167 tests total)
- [ ] Sanity check : test des 3 cas q-016, q-021, q-027 passe (les codes attendus sont extraits)
- [ ] Pas de régression sur les 10 questions originales (10/10 maintenu post-fix)

**Lot E.2 (Desktop)** :
- [ ] 30 questions évaluées sans crash
- [ ] ≥ 24/30 sources retrouvées (cible 80 %)
- [ ] ≥ 50 % concepts attendus couverts par question
- [ ] Coût total Lot E.2 < 0,80 $ Anthropic
- [ ] Latence moyenne dans la fourchette 12-18 sec/question (acceptée)

**Lot E.3 (Plateforme)** :
- [ ] `RAPPORT-CC-S2.2.md` produit en 8 sections (~2000-2500 mots)
- [ ] PR ouverte avec titre conforme + description listant les 7 commits
- [ ] `JOURNAL-POC-RAG.md` mis à jour (append S2.2 Lot E)
- [ ] `STATUS-RAG.md` mis à jour : L1.26e ✅ Fait, sprint S2.2 ✅ clôturé, S2.3 prêt

---

## 9. Fichiers de référence

**Référentiels du couple 2** (clone Git) :
- `_instructions-rag.md` v1
- `DECISIONS-RAG.md` (30 décisions actées)
- `SPEC-MD-POUR-RAG.md` v1.4
- `STATUS-RAG.md`, `JOURNAL-POC-RAG.md`, `cartographie-rag.md`, `SYNC-INTER-CANAUX.md`, `whitelist-wikilinks-futurs.md`
- `briefs/BRIEF-CC-S2.2.md` (brief source S2.2)
- `briefs/RAPPORT-CC-S1.md` + `RAPPORT-CC-S1bis.md` + `RAPPORT-CC-S1ter.md` + `RAPPORT-CC-S2.1.md`

**Code à patcher** :
- `rag/code/backend/query.py` ligne 270 (`extract_cited_codes`)
- `rag/code/backend/test_query.py` (tests à étendre)

**Contact** : Blaise Cavalli (garant transverse). Toute question, blocker, écart → signaler.

---

*Brief Lot E produit le 13 mai 2026. Cible D-021 : ~2400 mots (légèrement au-dessus de 2000 vu le split en 3 sous-lots). Allocation D-030 hybride : Plateforme E.1 + E.3, Desktop E.2 — coordination Blaise entre les deux.*
