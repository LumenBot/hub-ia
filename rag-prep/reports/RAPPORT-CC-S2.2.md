# RAPPORT-CC-S2.2 — Brique pattern-llm-wiki + golden set 30q + métriques + pre-commit + eval extended

**Émetteur :** Claude Code Hub IA Plateforme (Lot E.3)
**Destinataire :** Cowork Hub IA Plateforme + Blaise Cavalli (garant transverse)
**Sprint :** S2.2 (clôture définitive)
**Briefs sources :** `rag-prep/briefs/BRIEF-CC-S2.2.md` + `rag-prep/briefs/BRIEF-CC-S2.2-Lot-E.md`
**Branche développement :** `claude/execute-pilot-batches-mBSIp` (conservée — D-027)
**Date :** 13 mai 2026
**Allocation D-030 :** hybride Cowork (Lots A, B) + Claude Code Plateforme (Lots C, E.1, E.3) + Claude Code Desktop (Lots D, E.2)

---

## 1. Objectifs S2.2

Le sprint S2.2 préparait la production de la vague 3 (CU-026, CU-027, DEP-08) en consolidant trois axes structurels :

1. **Extraire la première brique transverse** `pattern-llm-wiki.md` (D-025) — le recouvrement cu-008 ↔ dep-02 sur le pattern LLM Wiki Karpathy était confirmé en revue I-003 (~30-40 lignes dupliquées). Sans extraction préalable, la vague 3 (cu-014 et cu-025 référenceront aussi LLM Wiki) aurait amplifié la dette éditoriale.

2. **Étendre le golden set de 10 à 30 questions** — couverture suffisante pour valider la robustesse du pipeline sur un vault élargi à 10 fichiers MD (3 modules CU + 1 PR + 1 DEP + 4 transverses + 1 fiche outils).

3. **Renforcer les garde-fous opérationnels** — métriques de coût instrumentées dans tous les scripts API, pre-commit hook audit-md-rag, system prompt enrichi mentionnant les briques transverses comme sources canoniques privilégiées.

**Cible eval initiale** : ≥ 24/30 sources retrouvées (≥ 80 %), ≥ 50 % concepts attendus couverts, coût total Lot D < 0,65 $ (cap durci). **Cible atteinte et dépassée** après fix wikilinks (Lot E.1) : **30/30 sources, 30/30 score global**.

---

## 2. Livrables par lot

| Lot | Acteur | Commit | Livrable |
|---|---|---|---|
| **A** — Production MD transverse + refactor modules | Cowork | `b7c7f96` | `rag/content/transverses/pattern-llm-wiki.md` v3.8.6 (~120 lignes : pattern Karpathy + 5 patterns post-Karpathy + tableau de décision par volume corpus). Refactor `cu-008.md` v3.8.6 et `dep-02.md` v3.8.6 (sections LLM Wiki remplacées par renvoi `[[pattern-llm-wiki]]`). Refactor `cu-001.md` aussi. Chiffres canonisés v3.8.5/6 (22 chiffres dans `chiffres-macro-2026.md`). Mention « troisième voie SLM » dans `pr-07.md`. `cartographie-rag.md` enrichie + `whitelist-wikilinks-futurs.md` mise à jour. |
| **B** — Extension golden set | Cowork | `b7c7f96` | 20 nouvelles questions ajoutées à `rag/eval/questions.yaml` (q-011 → q-030). Répartition : 3 cu-001 + 3 cu-008 + 3 pr-07 + 3 dep-02 + 2 outils-vector-db + 4 transverses (1 par brique) + 2 cross-modules (q-029 cross-llm-wiki-dep02, q-030 cross-pr07-vigilance). |
| **C** — Métriques + pre-commit + prompt | Claude Code Plateforme | `127de86` | Module `rag/code/_cost.py` centralisé (`estimate_cost`, `log_cost`, `read_cost_log`, `summarize_cost`, `format_cost_summary`) + intégration dans `ingest.py` / `query.py` / `run_eval.py` (`resp.usage.*tokens` exposés). `rag/code/.cost-log.jsonl` gitignored. `.githooks/pre-commit` bash + `.githooks/README.md` (activation `git config core.hooksPath .githooks`). `SYSTEM_PROMPT` enrichi (D-025 : briques transverses canoniques, format wikilink Obsidian préféré + rétro-compat crochets). **159/159 tests verts** (134 cumulés + 25 nouveaux). |
| **D bis** — Fix YAML int values | Claude Code Desktop | `00d80e8` | Correction ciblée de 3 entrées du golden set (q-016, q-019, q-027) où `1,8`/`95`/`21` étaient parsées comme `int` par PyYAML, faisant crasher `evaluate_one` sur `int.lower()`. **Exception D-022** auto-correction Desktop validée ex-ante par Blaise pour rapidité (vs circuit Cowork). |
| **D** — Eval extended (1er run partiel) | Claude Code Desktop | `fa8fc88` | Eval sur 15 questions q-016 → q-030 (le 1er run a crashé à q-016 sur le bug YAML, rerun ciblé après fix). 9/15 sources retrouvées ≥ 1, **15/15 concepts ≥ 50 %**. **Bug d'extraction wikilinks identifié** par observation 3 réponses (q-016, q-021, q-027) contenant des wikilinks `[[code#ancre]]` non extraits. Coût : **0,71 $ Anthropic + 0,0005 $ OpenAI** (cap durci 0,50 $ Anthropic dépassé — accepté ex-ante par Blaise). |
| **E.1** — Fix `extract_cited_codes` | Claude Code Plateforme | `34496cb` (PR #47 mergée) | Refactor de `extract_cited_codes()` dans `rag/code/backend/query.py`. Deux patterns : `WIKILINK_CITATION_PATTERN` (formes `[[code]]`, `[[code#ancre]]`, `[[code\|alias]]`, `[[code#ancre\|alias]]`) + `BRACKET_CITATION_PATTERN` (rétro-compat `[CODE]` avec lookbehind/lookahead évitant la double-capture). Sortie normalisée en lowercase, ordre d'apparition préservé, dédup case-insensitive. **+12 tests** `TestWikilinkExtraction` + adaptations historiques. **171/171 tests verts**. |
| **E.2** — Rejeu eval complet 30q | Claude Code Desktop | `af18810` | Rerun complet 30 questions post-fix E.1 sur le vault enrichi (10 fichiers, 121 chunks). **Résultats finaux** : 30/30 sources retrouvées, 25/30 concepts pleinement couverts, **30/30 concepts ≥ 50 %**, **30/30 score global**. Latence moyenne **16,4 s/question**. Coût ~0,70 $ Anthropic (estimé). Artefacts : `rag/eval/eval-report-s2.2-final.md` + `rag/eval/eval-report-s2.2-final.json`. |
| **E.3** — RAPPORT + PR finale | Claude Code Plateforme | *(ce commit)* | Présent rapport + ouverture PR finale S2.2. |

---

## 3. Métriques quantitatives

### Eval golden set 30 questions — avant vs après fix wikilinks

| Indicateur | Lot D (1er run, partiel) | Lot E.2 (final, complet) | Δ |
|---|---|---|---|
| Questions évaluées | 15 (q-016 → q-030) | 30 (q-001 → q-030) | +15 |
| **Sources retrouvées** | 9/15 (60 %) | **30/30 (100 %)** | +21 |
| Concepts ≥ 50 % couverts | 15/15 (100 %) | 30/30 (100 %) | maintenu |
| Concepts pleinement couverts | n/a | 25/30 (83 %) | — |
| **Score global** | 9/15 | **30/30** | +21 |
| Cible brief (≥ 24/30 = 80 %) | n/a sur sous-set | **✅ largement atteinte** | — |

**Impact du fix Lot E.1** : sur les 15 questions du sous-set Lot D, 6 questions supplémentaires sont retrouvées une fois les wikilinks `[[code#ancre]]` extraits — notamment q-016 et q-027 sur `chiffres-macro-2026`, q-021 sur `dep-02`. Le fix permet aussi de capter sereinement les wikilinks dans toutes les autres questions où Claude les utilise sans crochets simples.

### Régression check (10 questions originales S1)

Les 10 questions pilotes S1 (q-001 → q-010) restent à **10/10 sources retrouvées** post-fix (vérifié dans `eval-report-s2.2-final.md`). Aucune régression.

### Latence Sonnet 4.6

| Statistique | Valeur |
|---|---|
| Latence moyenne | **16,4 s/question** |
| Min (Lot D) | 9 s |
| Max (Lot D) | 22 s |
| Cible initiale brief S1 §4 | 5 s (irréaliste) |

Cible 5 s/question (brief S1 puis reportée en S2.2) n'est **pas tenue et ne peut pas l'être** pour Sonnet 4.6 sur ces volumes (~3500 tokens in / ~900 tokens out par question). Recalibrage proposé en §6.

### Volume du vector store

| Snapshot | Chunks | Re-indexation |
|---|---|---|
| Post-S1c.2 (vault 9 fichiers) | 107 | initiale |
| Post-S2.2 Lot A (vault 10 fichiers, refactor) | **121** | +15 (pattern-llm-wiki), 52 updates (cu-008/dep-02), 1 suppression |
| Coût ingestion incrémentale | — | **0,000474 $** (23 719 tokens in × text-embedding-3-small) |

---

## 4. Anomalies & fixes

### Anomalie #1 — YAML int values (Lot D blocker)

**Symptôme** : `evaluate_one()` crashe sur `AttributeError: 'int' object has no attribute 'lower'` lors du 1er run de l'eval extended. Crash systématique à q-016.

**Cause racine** : trois entrées du golden set Lot B contiennent des valeurs numériques **non quotées** dans `expected_concepts` :
- q-016 : `[1,8, heures, McKinsey]` → PyYAML parse `1,8` comme float
- q-019 : `[95, ROI, gouvernance, redesign]` → `95` parsé comme `int`
- q-027 : `[21, McKinsey, workflow]` → `21` parsé comme `int`

**Fix** (commit `00d80e8` — Claude Code Desktop, auto-correction validée ex-ante par Blaise) : quotation strictement formelle des 3 valeurs concernées :
- `[1,8, heures, McKinsey]` → `["1,8 heures", McKinsey]`
- `[95, ROI, ...]` → `["95 %", ROI, ...]`
- `[21, McKinsey, workflow]` → `["21 %", McKinsey, workflow]`

**Périmètre d'exception D-022** : limité aux 3 valeurs numériques non quotées, sans toucher au sens éditorial. Tracé dans le JOURNAL avec rationale (rapidité vs circuit Cowork classique).

### Anomalie #2 — `extract_cited_codes` ne capte pas les wikilinks Obsidian (Lot D → Lot E.1)

**Symptôme** : Lot D mesure 9/15 sources retrouvées alors que les réponses Claude contiennent les wikilinks vers les bonnes sources. Cas reproductibles :
- q-016 : réponse contient `[[chiffres-macro-2026#18-h-jour-mckinsey-2025]]` → non extrait
- q-021 : réponse contient `[[dep-02#cycle-stitch-evaluate-iterate]]` → non extrait
- q-027 : pattern identique sur `chiffres-macro-2026`

**Cause racine** : `extract_cited_codes()` v1 utilisait un seul `CODE_PATTERN` regex pour matcher uniquement le format historique `[CODE]` à crochets simples. Le system prompt enrichi du Lot C demande pourtant explicitement à Claude de produire des wikilinks Obsidian `[[code]]` (D-025). Les wikilinks étaient donc systématiquement perdus à l'extraction.

**Fix** (commit `34496cb` — Lot E.1, PR #47 mergée) : refactor en deux patterns indépendants :

```python
WIKILINK_CITATION_PATTERN = re.compile(
    r"\[\[([a-zA-Z][a-zA-Z0-9-]*)(?:#[^\]\|]*)?(?:\|[^\]]*)?\]\]"
)
BRACKET_CITATION_PATTERN = re.compile(
    r"(?<!\[)\[(CU-\d+|PR-\d+|DEP-\d+|A\d+|OUTILS-[A-Z0-9-]+|TRANSVERSE-[A-Z0-9-]+)\](?!\])",
    re.IGNORECASE,
)
```

Le `(?<!\[)` et `(?!\])` du second pattern empêchent la double-capture à l'intérieur d'un wikilink `[[...]]`. Sortie normalisée en lowercase, ordre d'apparition préservé via tri par position, dédup case-insensitive.

**Couverture tests** : 12 nouveaux tests dédiés (`TestWikilinkExtraction`) couvrant wikilink simple, avec ancre, avec alias, ancre+alias combinés, briques transverses, dédup, mix wikilinks/crochets, lookbehind/lookahead, ordre d'apparition, outils-*, ignore non-codes.

### Effet combiné des deux fixes

Sans Anomalie #1 résolue : 0 question évaluable au-delà de q-015 (crash systématique).
Sans Anomalie #2 résolue : score sources retrouvées ~60 % au lieu de 100 %.

Le sprint S2.2 a donc validé empiriquement la valeur d'une **boucle eval réelle avec mesures quantitatives** — ces deux anomalies n'auraient pas été détectées par tests unitaires mockés seuls (D-007 leçon, anti-pattern à inscrire dans SPEC v1.5).

---

## 5. Décisions structurantes prises pendant le sprint

Aucune nouvelle décision actée **en propre** dans S2.2 (D-001 à D-030 toutes pré-existantes). Mais le sprint a généré **3 décisions opérationnelles ponctuelles** documentées dans le JOURNAL, candidates à formalisation en SPEC v1.5 :

1. **Exception D-022 ciblée pour fix YAML** (Lot D blocker) : auto-correction Desktop validée ex-ante par Blaise pour 3 valeurs numériques non quotées du golden set. Le sens éditorial est préservé, l'exception est strictement formelle. Pattern : « si un blocker bloque l'eval et la correction est strictement formelle, Desktop peut auto-corriger sans circuit Cowork » — à codifier comme délégation D-022 conditionnelle.

2. **Dépassement de cap durci budgétaire accepté ex-ante** (Lot D) : 0,71 $ Anthropic mesuré vs cap durci 0,50 $ du brief (et cap mensuel global 50 $ très loin). Décision : accepter le dépassement plutôt que tronquer l'eval. Pattern : « les caps durcis brief sont des alertes opérationnelles, pas des hard-stops absolus, tant que le cap mensuel D-013 est respecté ».

3. **Allocation D-030 hybride validée empiriquement** : pattern Plateforme (refactor + tests sans coût API) → Desktop (eval avec coût API) → Plateforme (RAPPORT + PR) testé en S2.2 sur 7 itérations. Pattern fonctionnel, à reconduire en S2.3.

---

## 6. Recommandations SPEC v1.5

À arbitrer par Cowork lors de la prochaine itération SPEC :

### Proposition 1 — AP-5 : YAML int values dans golden set (anti-pattern)

**Contexte** : Anomalie #1 du Lot D (3 entrées du golden set crashent `evaluate_one`).

**Suggestion d'ajout à SPEC §Anti-patterns** :
> **AP-5 — Valeurs numériques non quotées dans `expected_concepts`** : toute valeur commençant par un chiffre dans le champ `expected_concepts` d'une entrée golden set doit être quotée explicitement (`"95 %"`, `"1,8 heures"`, `"21 %"`). PyYAML parse sinon les nombres en `int`/`float` et l'évaluation crashe sur `int.lower()`. À vérifier au commit côté Cowork (pre-commit golden set futur) ou à intercepter défensivement côté `evaluate_one` (`str(c).lower()` au lieu de `c.lower()`).

### Proposition 2 — Formalisation du pattern d'extraction wikilink (SPEC §R9 ou §Extraction citations)

**Contexte** : le pattern wikilink Obsidian `[[code]]`, `[[code#ancre]]`, `[[code|alias]]` est désormais codifié dans le system prompt v2 (Lot C) et dans `extract_cited_codes()` v2 (Lot E.1), mais pas encore reflété dans SPEC.

**Suggestion d'ajout à SPEC §R9 ou nouvelle section §Extraction citations** :
> Les réponses produites par le pipeline RAG citent les sources selon deux formats :
> - **Préféré** : wikilink Obsidian `[[code]]` (avec ancre/alias optionnels).
> - **Accepté (rétro-compat)** : crochets simples `[CODE]` pour les familles canoniques (CU, PR, DEP, A, OUTILS, TRANSVERSE).
>
> `extract_cited_codes()` doit reconnaître les deux formats, normaliser la sortie en lowercase, préserver l'ordre d'apparition, dédupliquer case-insensitive.

### Proposition 3 — Recalibrage de la cible latence (briefs S2.3+)

**Contexte** : la cible 5 s/question des briefs S1 et S2.2 est irréaliste pour Sonnet 4.6 sur volumes ~3500 tokens in / 900 tokens out. Mesure empirique : 16,4 s/question en moyenne (9–22 s).

**Suggestion** : adopter en SPEC §Performances ou directement dans les briefs futurs :
> **Cible latence Sonnet 4.6 (volumes ~3-5 k tokens in / ~0,5-1,5 k tokens out)** : 12–18 s/question acceptables. Cible < 5 s/question serait techniquement atteignable avec Haiku 4.5 (~3× plus rapide) mais au prix d'une dégradation qualitative (à mesurer en S3 si optimisation latence prioritaire).

### Proposition 4 — Boucle eval réelle comme garde-fou structurel

**Contexte** : les deux anomalies du sprint (YAML int + bug wikilinks) ont été détectées par eval réelle, pas par tests unitaires mockés.

**Suggestion** : ajouter à SPEC §Validation ou §Tests :
> Toute évolution du pipeline (prompt, regex d'extraction, modèles, embeddings) doit déclencher un **rejeu eval golden set** sur le vault courant avant clôture du sprint, en complément des tests unitaires mockés. Les mocks valident le contrat ; l'eval réelle valide l'effet observé sur les vrais corpus.

---

## 7. Pistes investigation S2.3 — matching exact vs sémantique pour concepts

Les **5 concepts attendus non « pleinement » couverts** (mais score ≥ 50 % maintenu) révèlent une limite structurelle du matching `expected_concepts` actuel (sous-chaîne exacte case-insensitive) :

| Question | Concept attendu | Forme dans la réponse | Diagnostic |
|---|---|---|---|
| q-001 | `méthode` | `méthodologie` | Dérivé lexical (substantif → substantif dérivé) |
| q-012 | `vérification` | `vérifier` | Forme verbale du concept nominal attendu |
| q-016 | `1,8 heures` | `1,8 heure` (singulier) | Variation morphologique (pluriel vs singulier) |
| q-028 | `persistant` | `persistance` | Adjectif → substantif (même racine) |
| q-029 | `économie` | `gain` / `économies` | Synonyme + variation morphologique |

**Cause** : `c in answer_text` (sous-chaîne) ne tolère ni stemming ni synonymes. Le contenu est bien présent éditorialement, le score est juste défaillant sur la métrique.

**Pistes pour S2.3** (à arbitrer en début de sprint) :

1. **Stemming léger** côté `evaluate_one` (par exemple `unicodedata` + tronquer aux 5-7 premiers caractères pour les mots > 7 chars). Risque : faux positifs (« source » vs « sourcing »).
2. **Liste de synonymes par concept** : enrichir `expected_concepts` avec `[concept_principal, synonyme_1, synonyme_2]` côté Cowork. Coût Cowork : ~15-30 min pour les 30 questions.
3. **LLM-as-judge** (D-007 DEP-02) : remplacer le matching textuel par un appel Claude Haiku 4.5 qui juge si la réponse couvre le concept. Coût : ~0,001 $/concept × 30 = négligeable, mais introduit une dépendance API supplémentaire.
4. **Composer** stemming + synonymes (1+2) en premier passage, LLM-as-judge en repli sur les concepts non matchés. Compromis recommandé pour S2.3 ou S3.

**Recommandation S2.3** : commencer par option 2 (liste synonymes par concept) — minimal effort, maximal contrôle éditorial, pas de dépendance API supplémentaire. Si insuffisant après une vague de production MD, évaluer option 4.

---

## 8. Coûts cumulés

### Détail S2.2

| Phase | Modèle | Tokens in | Tokens out | Coût $ |
|---|---|---|---|---|
| Lot A — Cowork (production MD) | — | — | — | 0,00 |
| Lot B — Cowork (extension golden set) | — | — | — | 0,00 |
| Lot C — Plateforme (refactor + tests) | — | — | — | 0,00 |
| Lot D bis — Desktop (fix YAML) | — | — | — | 0,00 |
| Lot D ingestion incrémentale | text-embedding-3-small | 23 719 | 0 | 0,000474 |
| Lot D 1er run (16 q jusqu'à crash q-016) | claude-sonnet-4-6 | ~55 000 | ~14 000 | 0,3749 |
| Lot D rerun ciblé (q-016 → q-030, 15 q) | claude-sonnet-4-6 | ~52 500 | ~13 500 | ~0,34 |
| Lot E.1 — Plateforme (refactor + tests) | — | — | — | 0,00 |
| Lot E.2 — Desktop (rerun complet 30 q) | claude-sonnet-4-6 | ~105 000 | ~27 000 | ~0,70 |
| Lot E.3 — Plateforme (ce rapport + PR) | — | — | — | 0,00 |
| **Total S2.2 (estimé)** | — | — | — | **~1,41 $ (Lot D large) + ~0,001 $ OpenAI** |

**Synthèse fournie par Blaise** : ~1,41 $ Anthropic + 0,001 $ OpenAI = ~1,41 $ pour l'ensemble Lot D + reruns (incluant Lot E.2). **Cumul S2.2 estimé : ~2,50 $** (incluant overhead opérationnel + variance d'estimation).

### Cumul historique S1 + S2.1 + S2.2

| Sprint | Coût $ |
|---|---|
| S1 (S1c.2 local Blaise — ingest + 10 queries) | ~0,30 |
| S1bis | 0,00 (mocks) |
| S1ter Lot C.1 python-dotenv | 0,00 |
| S2.1 (audit v2 refactor) | 0,00 |
| **S2.2 (cumul)** | **~2,50** |
| **Total cumulé S1 + S2.1 + S2.2** | **~2,80 $** |

### Budget restant

Crédits initiaux : ~3 $ Anthropic + ~5 $ OpenAI sans renouvellement automatique (cf. brief S1ter §1).

| Provider | Initial | Consommé S1-S2.2 | **Restant** |
|---|---|---|---|
| Anthropic | ~3,00 $ | ~2,80 $ | **~0,20 $** ⚠ |
| OpenAI | ~5,00 $ | ~0,003 $ | **~4,997 $** |

⚠ **Alerte budgétaire structurelle pour S2.3** : les crédits Anthropic ne suffiront pas pour un nouveau rejeu eval complet de 30 questions (~0,70 $ requis). Trois options pour S2.3 :
1. Recharger les crédits Anthropic (côté Blaise).
2. Basculer en `claude-haiku-4-5` pour l'eval (coût ~5× inférieur — 0,15 $ par rejeu 30q estimé), avec perte qualitative à mesurer.
3. Eval ciblée sous-ensemble (10 questions critiques) pour réduire le volume.

Plafonds D-013 (50 $/mois Anthropic, 10 $/mois OpenAI) restent **très largement préservés** au niveau mensuel.

---

## Liste des commits S2.2

| SHA | Acteur | Lot | Message |
|---|---|---|---|
| `b7c7f96` | Cowork | A + B | `feat S2.2 Lots A et B - pattern-llm-wiki + refactor cu-008 dep-02 + golden set 30q` |
| `127de86` | Plateforme | C | `feat(rag): métriques coût + pre-commit hook + system prompt enrichi (s2.2 lot C)` |
| `00d80e8` | Desktop | D bis | `fix(rag-eval): quote int values in q-016/019/027 (s2.2 lot D blocker)` |
| `fa8fc88` | Desktop | D | `feat(rag-eval): S2.2 Lot D eval q-016 → q-030 sur vault enrichi (partiel)` |
| `f5e8e9b` | Desktop | D | `chore(rag-prep): MAJ JOURNAL + STATUS post-S2.2 Lot D (Claude Code Desktop)` |
| `8f2a60f` | Cowork | E | `docs(rag-prep): brief S2.2 Lot E (fix wikilinks + eval full + rapport)` |
| `34496cb` | Plateforme | E.1 | `fix(rag-backend): extract_cited_codes capte les wikilinks Obsidian (s2.2 lot E.1)` *(PR #47 mergée sur main)* |
| `4298da0` | Plateforme | — | `Merge remote-tracking branch 'origin/main' into claude/execute-pilot-batches-mBSIp` |
| `af18810` | Desktop | E.2 | `feat(rag-eval): S2.2 Lot D rerun complet 30 questions post-Lot E.1 (final)` |
| `125310a` | Desktop | E.2 | `chore(rag-prep): MAJ JOURNAL + STATUS post-rerun final 30q (Lot D définitif)` |
| *(ce commit)* | Plateforme | E.3 | `docs(rag): rapport mission S2.2 + ouverture PR finale` |

**Suite tests cumulée S1 + S2.1 + S2.2** : 171/171 verts (134 + 25 nouveaux S2.2 Lot C + 12 nouveaux S2.2 Lot E.1).

---

*Rapport produit le 13 mai 2026 par Claude Code Hub IA Plateforme (Lot E.3). Format conforme brief CC-S2.2 Lot E §4 (8 sections) + déposé dans `rag-prep/reports/` selon consigne Blaise. Sprint S2.2 définitivement clôturé après merge de la PR finale.*
