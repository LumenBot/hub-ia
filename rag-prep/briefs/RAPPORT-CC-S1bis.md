# RAPPORT-CC-S1bis — Validation end-to-end (clôture S1) + ouverture PR

**Émetteur :** Claude Code Hub IA Plateforme
**Destinataire :** Cowork Hub IA Plateforme + Blaise Cavalli (garant transverse)
**Sprint :** S1bis (clôture S1)
**Brief source :** `rag-prep/briefs/BRIEF-CC-S1bis-validation-end-to-end.md`
**Branche développement :** `claude/execute-pilot-batches-mBSIp` (conservée — D-027)
**Date :** 12 mai 2026

---

## 1. Synthèse exécutive

**Lot S1b.1 livré** (audit-md-rag sur vault réel). **Lots S1b.2 et S1b.3 partiellement livrés** : rapport et PR produits, mais la validation end-to-end (ingestion réelle + retrieval + génération + eval) **n'a pas pu être exécutée** car aucune clé `OPENAI_API_KEY` ni `ANTHROPIC_API_KEY` n'était exposée dans l'environnement de cette session. Arbitrage Blaise demandé via `AskUserQuestion` — option « Pause après S1b.1 puis ouverture PR sur l'existant » retenue.

**État du vault réel ingéré :** 9 fichiers MD (le brief et STATUS-RAG annonçaient 10 — écart §4 ci-dessous).

**Résultat audit (S1b.1) :** 150 écarts bruts, **0 violation éditoriale claire** de SPEC v1.2 après classification. Détail en §2.

**Coût API consommé S1bis :** 0 $ (S1b.2 non exécuté).

**Discipline §7 brief respectée :** aucune modification des MD du vault, aucune modification du code de l'audit (évolutions scope v2).

---

## 2. Résultats audit-md-rag sur vault réel

Commande : `python3 rag/code/audit/audit-md-rag.py --vault rag/content --report rag/eval/audit-report-s1bis-raw.txt`. Rapport analysé : `rag/eval/audit-report-s1bis.md`. Dump brut : `rag/eval/audit-report-s1bis-raw.txt`.

### Distribution brute

| Règle | Écarts détectés | Nature |
|---|---|---|
| R1 (frontmatter complet) | 2 | Faux positifs structurels |
| R2 (H1 unique) | 0 | — |
| R3 (chunking ≤ 800 tokens) | 0 | — |
| R4 (wikilinks valides) | 83 | Vault partiel (MD vagues 3+ à venir) |
| R6 (chiffres sourcés) | 65 | Majoritairement faux positifs R9 SPEC v1.2 |
| **Total** | **150** | |

### Classification qualifiée

| Cat | Nb | Détail | Action |
|---|---|---|---|
| A — faux positif structurel | 2 | `glossaire.md` : `glosaire_termes: []` et `derives: []` vides par construction (le glossaire est la racine du système) | Audit v2 : exception `code == "glossaire"` |
| B — vault partiel S1 | 83 | Wikilinks vers `cu-002`, `cu-011`, `pr-04`, `dep-07`, etc. — modules à produire en vagues 3+ | Attendu — résolu naturellement par les vagues suivantes |
| C — faux positif R9 | ~58 | Chiffres dans alias de wikilinks vers `chiffres-macro-2026.md`. L'audit R6 v1 ne reconnaît pas les wikilinks Obsidian comme « source proche » | Audit v2 : reconnaître `[[chiffres-macro-…]]` comme source valide |
| D — chiffres orphelins potentiels | ~7 | Chiffres sans wikilink visible dans la fenêtre 200 chars (glossaire, dep-02 impacts relatifs, outils-vector-db) | Arbitrage Blaise / Cowork |

**Lecture qualifiée du critère brief §4 « total errors = 0 » :** atteint sur la conformité éditoriale SPEC v1.2 ; non atteint sur le décompte brut tant que l'audit n'a pas été aligné v1.2 (objet naturel de v2, hors scope S1bis).

---

## 3. Résultats ingestion + re-indexation incrémentale

**Non exécuté.** Le Lot S1b.2 du brief CC-S1bis nécessite :
- `OPENAI_API_KEY` pour calculer les embeddings (`text-embedding-3-small`, D-007)
- `ANTHROPIC_API_KEY` pour la génération (`claude-sonnet-4-6`, D-005)

Aucune des deux variables d'environnement n'était définie dans la session Claude Code Plateforme. Avant toute tentative, j'ai posé la question à Blaise via `AskUserQuestion` (3 options : fournir les clés / mode dégradé mocké / pause après S1b.1). L'option **« Pause après S1b.1 »** a été retenue.

**Reste à exécuter (à reprendre dans une session future) :**

1. `python3 rag/code/ingestion/ingest.py` sur le vault (9 fichiers réels).
   - Volume attendu : ~30-60 chunks selon brief §4 (à valider).
   - Coût attendu : < 0,01 $ OpenAI (corpus ~50 k tokens).
2. Re-indexation incrémentale : modifier un `last_updated` d'un MD, relancer `ingest.py`, vérifier `report.chunks_updated == 1`.
3. Boucle d'eval : 10 questions golden set via `query.py` + `run_eval.py`.

**Sanity test offline (sans API)** que j'ai pu faire : `python3 rag/code/ingestion/ingest.py --vault rag/content --dry-run` aurait fonctionné (store en mémoire, aucune embedding) mais le brief demande l'ingestion réelle, et c'est le critère « ~30-60 chunks indexés » qui compte. Je n'ai pas exécuté le dry-run pour éviter de produire des artefacts trompeurs dans le rapport (un nombre de chunks issu d'un dry-run sans embedding ne valide pas la pipeline réelle).

---

## 4. Résultats eval golden set

**Non exécuté.** Cf. §3. Le golden set `rag/eval/questions.yaml` (10 questions, 2 par unité pilote) et `rag/eval/golden-answers.yaml` sont commités et prêts. Le script `run_eval.py` est testé sur mocks (10/10 tests verts en S1).

**Reste à mesurer (session future) :**
- `sources_match` (`expected_sources` ⊂ `cited_codes` ?) — cible brief §4 : ≥ 8/10
- `concepts_match` — cible : ≥ 50 % des concepts attendus par question
- Latence < 5 sec/question
- Sondage manuel Blaise pour la qualité éditoriale — cible : ≥ 7/10 réponses jugées utiles

---

## 5. Coût API accumulé

| Provider | Modèle | Appels | Coût |
|---|---|---|---|
| OpenAI | text-embedding-3-small | 0 | 0,00 $ |
| Anthropic | Claude Sonnet 4.6 | 0 | 0,00 $ |
| **Total S1 + S1bis** | — | **0** | **0,00 $** |

Plafonds D-013 (50 $/mois Anthropic, 10 $/mois OpenAI) intacts. Plafonds CC-S1bis §7 (> 1 $ Anthropic ou > 0,30 $ OpenAI) sans risque tant que S1b.2 n'aura pas tourné.

---

## 6. Écarts résiduels signalés à Blaise

### Écart 1 — Clés API absentes (bloquant S1b.2 + S1b.3 ingestion réelle)
**Action attendue :** définir `OPENAI_API_KEY` et `ANTHROPIC_API_KEY` dans une session future Claude Code Plateforme (variables d'environnement ou `rag/code/.env` gitignored), puis exécuter S1b.2 + extension du présent rapport en S1ter.

### Écart 2 — Inventaire vault 9 vs 10
**Constat :** 9 fichiers MD réellement présents dans `rag/content/` sur la branche, contre 10 annoncés dans le brief CC-S1bis §1 et dans STATUS-RAG §Vague 1+2.

Décompte effectif :
- 1 glossaire (`glossaire.md`)
- 1 fiche outils (`ressources/outils-vector-db.md`)
- 3 transverses (`chiffres-macro-2026.md`, `vigilance-hallucinations.md`, `vigilance-confidentialite.md`)
- **2** modules CU (`cu-001.md`, `cu-008.md`) — STATUS dit « 3 modules CU »
- 1 préalable (`pr-07.md`)
- 1 déploiement (`dep-02.md`)
- **Total : 9**

**Hypothèses non confirmées :** (a) un module CU supplémentaire prévu en pilote mais non transféré ; (b) une brique transverse type `pattern-llm-wiki.md` (cf. STATUS §Vague 3 anticipée) que STATUS comptait dans le décompte initial ; (c) simple coquille rédactionnelle.

**Action attendue :** confirmation de Blaise / Cowork. Pas bloquant pour la PR si on accepte « 9 fichiers déposés en S1 pilote ».

### Écart 3 — ~7 chiffres en catégorie D du rapport audit
**Action attendue :** arbitrage Cowork sur la nécessité de sourcer (« +11 % qualité reranker », « 99,99 % uptime », « 80 % entreprises ont déjà Postgres », « 90 % cas PME RAG suffit ») ou de les laisser en l'état (anti-pattern AP-3 partiel ou rédaction acceptable).

### Écart 4 — Audit-md-rag.py v1 non aligné SPEC v1.2
**Constat :** R9 (chiffres macro wikilinkés) et R10 (transposition fidèle) sont en roadmap audit v2. Tant qu'elles ne sont pas implémentées, l'audit v1 produit des faux positifs R6 massifs.

**Action attendue :** prioriser audit-md-rag v2 dans le sprint S2 (cf. §8 reco) — coût estimé ~3-4 h Claude Code.

### Écart 5 — Lot 2 du brief CC-S1 (MCP Obsidian)
**Statut :** non applicable (D-012-bis acte le report en Phase 2). Pour mémoire, déjà documenté dans RAPPORT-CC-S1 §4.

---

## 7. Propositions d'amendement à `SPEC-MD-POUR-RAG.md` ou autres référentiels

### Proposition 1 — Exception R1 pour `code: glossaire` (SPEC §R1)
**Contexte :** `glossaire.md` a `glosaire_termes: []` et `derives: []` vides par construction. R1 v1 les détecte à tort comme « champs vides » (anti-pattern paresse). Une exception explicite est nécessaire.

**Suggestion :** ajouter une note à R1 :
> Le fichier `glossaire.md` (`code: glossaire`, `type: transverse`) peut avoir `glosaire_termes: []` et `derives: []` vides par construction (le glossaire est la racine canonique du système de termes). Cette exception est codifiée dans audit-md-rag v2.

### Proposition 2 — Convergence R6 ↔ R9 dans audit v2 (SPEC §Validation)
**Contexte :** R6 reconnaît `Source :`, URL et liens markdown comme sources, mais pas les wikilinks `[[chiffres-macro-…]]`. R9 SPEC v1.2 demande explicitement de wikilinker les chiffres macro canoniques.

**Suggestion :** ajouter à la roadmap audit v2 (§Validation) :
> Audit v2 — règle R6 étendue : reconnaître `\[\[chiffres-macro-\d{4}#[^\]]+\]\]` (et plus généralement `\[\[transverses/…\]\]`) comme source canonique valide, en complément de `Source :`, URL et liens markdown. C'est la convergence opérationnelle entre R6 et R9.

### Proposition 3 — Codification du décompte vault dans STATUS-RAG
**Contexte :** écart 9 vs 10 entre STATUS et factuel. Cas typique d'incohérence inventaire.

**Suggestion :** ajouter une commande de comptage dans STATUS-RAG ou un script `rag/code/audit/inventory.py` qui produit un dump factuel du vault (fichier par catégorie). À rejouer à chaque sprint pour ancrer le décompte.

### Proposition 4 — Mode `--allow-future-links` pour R4 (audit v2)
**Contexte :** 83 R4 sur des wikilinks anticipant la production. R4 stricte n'a de sens que sur vault complet.

**Suggestion :** roadmap audit v2 : option `--allow-future-links` ou fichier `rag/content/.expected-codes.yaml` qui distingue « cible inexistante (erreur) » de « cible non encore produite (warning) ».

---

## 8. Recommandations pour Sprint S2

1. **Prioriser audit-md-rag v2** dès le démarrage S2 (R1 exception glossaire, R6 reconnaissance wikilinks canoniques, R5 glossaire, R7 nommage, R8 versioning git, R9 chiffres macro, R10 tableaux numériques fidèles, R4 mode permissif). Effort estimé : 3-4 h Claude Code. Avant toute production MD massive vague 3+.
2. **Exécuter S1b.2 + S1b.3** dès clés API disponibles (session « S1ter »). Effort : ~1 h.
3. **Pipeline d'eval automatisé en CI** : ajouter un workflow GitHub Actions qui rejoue `audit-md-rag.py --strict` à chaque PR touchant `rag/content/` (cf. RAPPORT-CC-S1 §6 reco 5, encore valable).
4. **Métriques de coût accumulées dans `query.py` et `ingest.py`** (cf. RAPPORT-CC-S1 §6 reco 4).
5. **Migration MD vague 3** : appliquer D-026 (co-production légère sondage Cowork Hub IA avant production sur 2-3 passages sensibles des modules N3/N4).
6. **Démarrage S3 backend Cloudflare Worker** : portage de `query.py` en TypeScript sur Cloudflare Workers (D-008), capture feedback Supabase, widget HTML/JS sur le Hub.

---

## 9. Liste complète des commits S1 + S1bis

### Sprint S1 (livré 12 mai matin)

| SHA | Lot | Message |
|---|---|---|
| `9e81533` | 1 | `chore(rag): scaffold rag/ folder structure (couple 2 init)` |
| `614fea9` | 3 | `feat(rag): audit-md-rag.py v1 — 5 règles minimales + tests` |
| `9834187` | 4 | `feat(rag): ingestion pipeline ChromaDB + tests + re-indexation incrémentale` |
| `ee306af` | 5 | `feat(rag): backend query CLI — retrieval + génération Claude + citations` |
| `5912460` | 6 | `feat(rag): golden set évaluation initial (10 questions) + script run_eval` |
| `ca3983e` | gov | `chore(rag-prep): rapport mission S1 + MAJ journal + status` |

**Suite tests S1 :** 62/62 verts (audit 26 + ingestion 14 + backend 12 + eval 10).

### Dépôts Cowork (commits Quest)

| SHA | Message |
|---|---|
| `668934e` | `feat(rag): dépôt vault initial — vague 1 + vague 2 + briques transverses (10 fichiers MD)` (9 effectivement présents — cf. §6 écart 2) |
| `fd0df0b` | `chore(rag): sync rag-prep/ — SPEC v1.2 + 27 décisions + brief CC-S1bis` |

### Sprint S1bis (livré 12 mai après-midi)

| SHA | Lot | Message |
|---|---|---|
| `d8c0c20` | S1b.1 | `chore(rag): audit-md-rag report on real vault content (s1bis lot 1)` |
| *(à venir)* | S1b.3 | `docs(rag): rapport mission consolidé S1+S1bis + ouverture PR` |

**Suite tests S1 + S1bis :** inchangée (62/62 verts — pas de nouveau code de production en S1bis, seulement exécution + analyse).

---

*Rapport mission produit le 12 mai 2026 par Claude Code Hub IA Plateforme. Format conforme §4 du brief CC-S1bis (9 sections). S1b.2 marqué non exécuté en §3 et §4, conditionnel à la fourniture des clés API en session future.*
