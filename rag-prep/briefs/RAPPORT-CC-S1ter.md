# RAPPORT-CC-S1ter — Clôture définitive S1 (python-dotenv + validation end-to-end)

**Émetteur :** Claude Code Hub IA Plateforme
**Destinataire :** Cowork Hub IA Plateforme + Blaise Cavalli (garant transverse)
**Sprint :** S1ter (clôture définitive S1 + S1bis)
**Brief source :** `rag-prep/briefs/BRIEF-CC-S1ter-validation-end-to-end-avec-cles.md`
**Branche développement :** `claude/execute-pilot-batches-mBSIp` (conservée — D-027)
**Date :** 12 mai 2026

---

## 1. Synthèse exécutive

**Lot S1c.1 livré intégralement.** `python-dotenv` ajouté aux 3 scripts (ingest, query, eval) via un helper `_env.py` centralisé. 67/67 tests verts (62 originaux + 5 nouveaux pour `_env`). Critère brief §4 validé : les 3 modules s'importent désormais sans `export OPENAI_API_KEY` préalable.

**Lot S1c.2 différé à exécution locale par Blaise.** Le fichier `rag/code/.env` (gitignored par construction, D-013) n'est pas synchronisable vers la session Claude Code Plateforme web. Conformément au brief §3 (« Si `.env` absent → blocker, signaler à Blaise sans avancer ») et à la réponse de Blaise via `AskUserQuestion`, l'exécution réelle (`ingest.py` sur 9 MD + 10 queries via `query.py` + `run_eval.py`) sera réalisée par Blaise depuis son Mac local où le `.env` existe avec permissions `-rw-------`. Les artefacts attendus (`rag/eval/queries-s1ter-output.md` + `rag/eval/eval-report-s1ter.md`) seront pushés par Blaise après exécution.

**Lot S1c.3 livré partiellement :** ce rapport est produit, PR ouverte. Section §3, §4 et §5 marquées « exécution locale Blaise — résultats attendus » plutôt que valeurs mesurées. Le rapport sera complété par Blaise (ou par une session future Claude Code Plateforme S1quad) une fois les artefacts S1c.2 disponibles.

**Coût API consommé S1ter :** 0,00 $ (mocks + import sanity exclusivement). Plafonds durcis du brief §7 (alerte > 0,50 $ Anthropic / > 0,10 $ OpenAI) restent intacts.

**Discipline §7 brief respectée :** aucune modification des MD du vault, aucune modification des fichiers de gouvernance hors JOURNAL/STATUS/ce rapport.

---

## 2. Résultats Lot S1c.1 — python-dotenv

### Livré

| Fichier | Nature | Détail |
|---|---|---|
| `rag/code/_env.py` | nouveau | Helper `load_env(path=None)` qui lit `rag/code/.env` via python-dotenv. Tolérant : si fichier absent ou dépendance indisponible, fallback silencieux. `override=False` : ne touche pas aux vars d'env déjà définies (compatibilité CI / Docker). |
| `rag/code/ingestion/ingest.py` | modifié | `import _env` en tête, avant le bloc `try: import yaml`. Place du load avant tout import openai. |
| `rag/code/backend/query.py` | modifié | Idem, avant tout import anthropic / openai. |
| `rag/code/eval/run_eval.py` | modifié | Idem (le script lance des appels API via `make_real_runner`). |
| `rag/code/requirements.txt` | modifié | Ajout `python-dotenv>=1.0.0`. |
| `rag/code/.env.example` | modifié | Préambule explicite référençant `_env.py`, conserve les 6 vars existantes. |
| `rag/code/test_env.py` | nouveau | 5 tests dédiés. |

### Tests

```
$ python3 -m pytest rag/code/ -v
============================== 67 passed in 0.28s ==============================
```

| Suite | Tests | Statut |
|---|---|---|
| `test_env.py` (nouveau) | 5 | ✅ |
| `audit/test_audit_md_rag.py` | 26 | ✅ |
| `ingestion/test_ingest.py` | 14 | ✅ |
| `backend/test_query.py` | 12 | ✅ |
| `eval/test_run_eval.py` | 10 | ✅ |
| **Total** | **67** | **✅ 67/67** |

### Sanity check du critère brief

```
$ cd rag/code && python3 -c "
import sys; sys.path.insert(0, '.')
from ingestion import ingest
from backend import query
from eval import run_eval
print('OK')"
OK — 3 modules importés sans erreur, _env chargé.
```

Critère brief §4 « `python -c "from ingestion.ingest import …" ne lève pas d'erreur même sans `export OPENAI_API_KEY` préalable » : ✅ validé.

### Choix d'implémentation

**Helper centralisé `_env.py` plutôt que `from dotenv import load_dotenv; load_dotenv()` dupliqué dans chaque script** (variante littérale du brief §4) :
- DRY : un seul endroit où changer le chemin `.env`, le comportement de fallback ou la gestion d'erreur
- Tolérance silencieuse : si `python-dotenv` n'est pas installé (ex. CI minimaliste, environnement Docker prod), les scripts continuent de fonctionner avec les vars d'env directes
- `override=False` : aligné avec la convention python-dotenv standard. Les scripts qui sont lancés avec `OPENAI_API_KEY` déjà exporté (ex. CI GitHub Actions secrets) ne sont pas écrasés par le `.env` local
- Chemin absolu calculé une fois (`rag/code/.env`) — pas de dépendance au cwd

---

## 3. Résultats Lot S1c.2 — ingestion + retrieval (à exécuter localement)

**Non exécuté dans cette session web.** Procédure documentée pour exécution locale Blaise :

### Pré-requis local
```bash
cd ~/path/to/hub-ia
git pull origin claude/execute-pilot-batches-mBSIp    # récupérer Lot S1c.1
ls -la rag/code/.env                                   # doit être -rw-------
cd rag/code && pip install -r requirements.txt         # installe python-dotenv 1.0+
```

### Commandes attendues

```bash
# 1. Ingestion réelle (volume attendu : ~30-60 chunks, coût < 0,01 $ OpenAI)
python3 rag/code/ingestion/ingest.py --vault rag/content --store rag/code/vector_store

# 2. Re-indexation incrémentale
#    - Bumper le last_updated d'un MD (ex. cu-001.md)
#    - Re-lancer ingest.py
#    - Vérifier report.chunks_updated == nb chunks affectés par ce fichier seulement
python3 rag/code/ingestion/ingest.py --vault rag/content --store rag/code/vector_store

# 3. Query CLI sur les 10 questions du golden set
#    Boucle sur rag/eval/questions.yaml, sortie JSON pour pipeline d'eval
for id in q-001 q-002 ... q-010 ; do
  python3 rag/code/backend/query.py --json "<question>" > rag/eval/q-XXX.json
done

# 4. Eval automatique (rejoue les 10 questions + matching)
python3 rag/code/eval/run_eval.py \
  --questions rag/eval/questions.yaml \
  --report rag/eval/eval-report-s1ter.md \
  --json rag/eval/eval-report-s1ter.json
```

### Critères de succès (brief §4) à vérifier au runtime

- [ ] Ingestion sans erreur, **~30-60 chunks créés** en ChromaDB local
- [ ] Re-indexation incrémentale opérationnelle (1 fichier modifié → seuls ses chunks ré-indexés)
- [ ] 10 questions traitées en moins de 5 sec/question
- [ ] **≥ 8/10** questions ont les `expected_sources` citées
- [ ] **≥ 50 %** des concepts attendus par question présents
- [ ] Coût OpenAI < **0,10 $** + Anthropic < **0,50 $** (plafonds S1ter durcis)

### Artefacts attendus à pusher

| Fichier | Contenu |
|---|---|
| `rag/eval/queries-s1ter-output.md` | 10 réponses Claude + sources citées + latence par question |
| `rag/eval/eval-report-s1ter.md` | Rapport `run_eval.py` (matching `expected_sources` + `concepts_match`) |
| `rag/eval/eval-report-s1ter.json` | Version JSON pour analyse machine |

---

## 4. Résultats Lot S1c.2 — eval golden set (à exécuter localement)

**Non exécuté dans cette session web.** Mêmes raisons qu'en §3. Le rapport généré par `run_eval.py` aura la structure suivante :

```
======================================================================
ÉVAL GOLDEN SET — rapport
======================================================================
Questions : 10
Sources attendues retrouvées : X/10
Concepts attendus pleinement couverts : Y/10
Score global (source + ≥50% concepts) : Z/10

... (détail par question)

Critère brief §9 : ✅ cible atteinte | ⚠ cible (8/10 sources) non atteinte
```

**Exit code** : 0 si ≥ 8/10 sources retrouvées (codé en S1 Lot 6).

---

## 5. Coût API accumulé S1 + S1bis + S1ter

| Provider | S1 | S1bis | S1ter (cette session) | S1c.2 attendu local | Total cumulé |
|---|---|---|---|---|---|
| OpenAI | 0 | 0 | 0 | < 0,01 $ | **< 0,01 $** |
| Anthropic | 0 | 0 | 0 | ~0,20-0,30 $ (estim. 10 questions × 2-3k tokens × Sonnet 4.6) | **< 0,30 $** |
| **Total** | **0** | **0** | **0** | **< 0,30 $** | **< 0,30 $** |

Plafonds D-013 (50 $ / 10 $ mois) et plafonds durcis brief S1ter §7 (0,50 $ / 0,10 $) intacts dans toutes les configurations.

---

## 6. Apprentissages clés

### Bonnes surprises

1. **Helper `_env.py` centralisé** plus propre que la variante littérale du brief (load_dotenv dupliqué dans chaque script) : code DRY, fallback silencieux, chemin absolu robuste.
2. **`override=False` par défaut** : protège les déploiements CI où les secrets sont injectés en vars d'env directes (cas typique GitHub Actions). Le `.env` local reste source d'autorité uniquement quand les vars d'env sont absentes.
3. **Sanity check « import sans clés API ne casse pas »** trivial à valider sans coût. Permet de vérifier que `_env.py` est bien tolérant au fichier absent (cas attendu en CI / production Docker / sandbox web).

### Points de vigilance pour S1c.2 (à observer en local)

1. **Re-indexation incrémentale** : c'est le cas-test qui m'inquiète le plus. Si le `content_hash` SHA-256 inclut le header injecté du frontmatter (`[METADATA]…[CONTENT]…`), tout bump de `last_updated` invalide TOUS les chunks du fichier (pas seulement ceux modifiés en contenu). C'est le comportement actuel — à confirmer comme acceptable au runtime.
2. **Chunks dépassant 800 tokens non détectés par audit-md-rag v1** : si certains MD du vault ont des sections H2 réellement > 800 tokens (faux négatif R3 dû au calcul `tokens ≈ words × 1.3`), `ingest.py` les acceptera tels quels mais ils dégraderont la qualité du retrieval. À monitorer dans `eval-report-s1ter.md`.
3. **Wikilinks anticipant les vagues 3+** : `query.py` peut citer un wikilink `[[cu-026]]` dans sa réponse, mais ce code n'est pas dans `extract_cited_codes` (regex matche `[CU-026]` entre crochets simples, pas wikilink double-crochet). Comportement intentionnel — les wikilinks Obsidian sont du markup, pas des citations sources.
4. **Système prompt v1 (S1)** : très court, ne mentionne pas la whitelist wikilinks futurs ni les briques transverses. Peut produire des réponses qui citent des codes en clair (`[CU-XXX]`) au lieu de wikilinks Obsidian. À enrichir en S2.

### Gaps identifiés sur le vault (déjà documentés en S1bis)

1. **Audit v1 non aligné SPEC v1.2 / v1.3** : 150 écarts bruts dont ~141 faux positifs (R1 glossaire, R4 vault partiel, R6 chiffres wikilinkés). D-028 (exception R1) et D-029 (whitelist R4) actées par Cowork attendent l'implémentation audit v2.
2. **R9 et R10** non implémentées (roadmap S2).
3. **Latence d'embedding OpenAI** depuis EU : à mesurer en S1c.2 — si > 1 sec par question, vague 2+ devra envisager un cache local d'embeddings query.

---

## 7. Recommandations pour Sprint S2

(En complément des recommandations RAPPORT-CC-S1 §6 et RAPPORT-CC-S1bis §8 qui restent valides.)

1. **Prioriser audit-md-rag v2** dès le démarrage S2 :
   - Implémenter D-028 : exception R1 quand `code == "glossaire"` ou `type == "transverse"` racine
   - Implémenter D-029 : lecture de `rag-prep/whitelist-wikilinks-futurs.md` au démarrage, R4 produit `warning` (pas `error`) pour les codes whitelistés
   - Implémenter R9 : détecter les chiffres macro Hub en clair sans wikilink vers `chiffres-macro-2026.md` (16 chiffres canoniques actuels à parser)
   - Implémenter R5/R7/R8/R10
   - Effort estimé : 4-6 h Claude Code
2. **Compléter S1c.2 en local** (Blaise) puis pusher les artefacts `rag/eval/queries-s1ter-output.md` et `rag/eval/eval-report-s1ter.md`. Si cible 8/10 sources non atteinte → diagnostic des questions échouées (chunking ? prompt système ? coverage du vault ?) avant migration vague 3.
3. **Métriques de coût accumulées dans les scripts** : instrumenter `query.py` et `ingest.py` pour logger le coût estimé par appel (tokens × tarif modèle) dans `rag/code/.cost-log.jsonl` (gitignored). Premier garde-fou pour vague 3 (~50 MD vs 9 actuels).
4. **Pre-commit hook audit-md-rag** sur `rag/content/` (RAPPORT-CC-S1 §6 reco 5, RAPPORT-CC-S1bis §8 reco 3).
5. **Enrichir le system prompt** de `query.py` pour mentionner les briques transverses (D-025) et la whitelist (D-029) — discipline pour le retrieval Phase 2 LLM Wiki.
6. **Démarrage S3 backend Cloudflare Worker** : portage TypeScript de `query.py`, capture feedback Supabase, widget HTML/JS sur le Hub.

---

## 8. Liste complète des commits S1 + S1bis + S1ter

### Sprint S1 (Claude Code Plateforme — 12 mai matin)
- `9e81533` chore(rag): scaffold rag/ folder structure (couple 2 init)
- `614fea9` feat(rag): audit-md-rag.py v1 — 5 règles minimales + tests
- `9834187` feat(rag): ingestion pipeline ChromaDB + tests + re-indexation incrémentale
- `ee306af` feat(rag): backend query CLI — retrieval + génération Claude + citations
- `5912460` feat(rag): golden set évaluation initial (10 questions) + script run_eval
- `ca3983e` chore(rag-prep): rapport mission S1 + MAJ journal + status

### Dépôts Cowork (12 mai matin/après-midi)
- `668934e` feat(rag): dépôt vault initial — vague 1 + vague 2 + briques transverses (10 fichiers MD)
- `fd0df0b` chore(rag): sync rag-prep/ — SPEC v1.2 + 27 décisions + brief CC-S1bis

### Sprint S1bis (Claude Code Plateforme — 12 mai après-midi)
- `d8c0c20` chore(rag): audit-md-rag report on real vault content (s1bis lot 1)
- `36d07ca` docs(rag): rapport mission consolidé S1+S1bis + ouverture PR

### Merge PR #42 vers main (Blaise — 12 mai)
- `d48b61f` Merge pull request #42 from LumenBot/claude/execute-pilot-batches-mBSIp

### Intégration post-S1bis (Cowork — 12 mai soir)
- `094931c` feat(rag): post-S1bis intégration — SPEC v1.3 + D-028/D-029 + whitelist wikilinks futurs + 90 % canonisé + 9 vs 10 corrigé
- `ea3e262` Merge pull request #43 from LumenBot/feature/post-s1bis-spec-v1.3-d028-d029
- `83cea32` chore(rag-prep): BRIEF-CC-S1ter + JOURNAL/STATUS post-étape C

### Sprint S1ter (Claude Code Plateforme — 12 mai)
- `9f0b341` feat(rag): python-dotenv pour lecture automatique .env (s1ter lot 1)
- *(à venir)* `docs(rag): rapport mission S1ter + ouverture PR clôture S1`

**Suite tests cumulée :** 67/67 verts (62 originaux S1 + 5 nouveaux S1ter).

---

*Rapport produit le 12 mai 2026 par Claude Code Hub IA Plateforme. Format conforme §4 du brief CC-S1ter (8 sections). Lot S1c.2 explicitement marqué « exécution locale Blaise » en §3 et §4, conditionnel à la disponibilité du `.env` côté Mac de Blaise. La PR ouverte porte le titre canonique du brief malgré la non-exécution de S1c.2 — décision Blaise (réponse `AskUserQuestion`) : le sprint S1ter est livré côté code (python-dotenv) ; l'exécution end-to-end avec les vraies clés est différée en local pour respect de la consigne « secrets jamais dans le diff » et de la consigne brief §3 « blocker si .env absent ».*
