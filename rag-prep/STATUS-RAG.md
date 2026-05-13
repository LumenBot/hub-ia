# STATUS-RAG.md — État synthétique du sprint courant

**Dernière mise à jour :** 13 mai 2026 (S2.3 Lot F livré — RAPPORT + PR finale, sprint clôturé côté Plateforme)
**Sprint en cours :** **S2.3 clôturé côté Claude Code Plateforme** — tous les lots livrés (A Cowork Hub IA, B+C Cowork Plateforme, D Plateforme `78d0fa7`, E Desktop `a8e8977`+`08c5892`, F Plateforme = rapport + PR finale). **Cibles brief §7 dépassées** (41/42 score global, latence 16,6 s/q). `rag-prep/reports/RAPPORT-CC-S2.3.md` produit en 8 sections. PR finale ouverte vers main depuis branche `claude/execute-s23-lot-f-rapport`. En attente merge manuel Blaise + arbitrage Cowork des 4 propositions SPEC v1.6.
**Période S2.3 :** 13 mai → début juin 2026
**Acteurs mobilisés :** Cowork Hub IA Plateforme + Cowork Hub IA (canal sondage parallèle) + Blaise + Claude Code Plateforme + Claude Code Desktop

---

## Objectif du sprint S0

Acter l'ensemble des décisions structurantes nécessaires au démarrage opérationnel du POC RAG : architecture finale, conventions, stratégie de retranscription HTML → MD, sync inter-couples. Aucun code produit en S0. Aucun fichier MD du vault produit en S0. Préparation rigoureuse → confiance totale en exécution à partir de S1.

---

## Livrables S0

| # | Livrable | Statut | Acteur |
|---|---|---|---|
| L0.1 | 4 fichiers de référence + dossier `briefs/` initialisés | ✅ Fait | Cowork |
| L0.2 | `BRIEF-RETEX-COWORK-HUB-IA.md` rédigé | ✅ Fait | Cowork |
| L0.3 | RetEx couple 1 reçu et intégré (D-016 à D-022 actées) | ✅ Fait | Cowork + Blaise |
| L0.4 | Décisions techniques D-005 à D-014 et D-017 actées dans `DECISIONS-RAG.md` | ✅ Fait | Cowork + Blaise |
| L0.5 | `_instructions-rag.md` consolidé en v1 (intégrant RetEx + décisions techniques) | ✅ Fait | Cowork |
| L0.6 | `STRATEGIE-MD-RAG.md` (méthodologie de retranscription) | ✅ Fait | Cowork |
| L0.7 | `SPEC-MD-POUR-RAG.md` v1 (cahier des charges format MD) | ✅ Fait | Cowork |
| L0.8 | `cartographie-rag.md` initialisé (à enrichir au fil des productions MD) | ✅ Fait | Cowork |
| L0.9 | `SYNC-INTER-CANAUX.md` initialisé (avec item I-001 refonte RULES couple 1) | ✅ Fait | Cowork |
| L0.10 | `BRIEF-CC-S1.md` rédigé pour le canal Claude Code Plateforme | ✅ Fait | Cowork |
| L0.11 | Migration vers `rag-prep/` + D-024 actée (architecture de circulation Cowork ↔ Git ↔ Claude Code) | ✅ Fait | Cowork |
| L0.12 | Push initial de `rag-prep/` sur le repo Git | ⏳ En attente | Blaise |
| L0.13 | Création du canal Claude Code Hub IA Plateforme | ✅ Fait | Blaise |
| L0.14 | Vague 1 MD pilotes produite (glossaire + outils-vector-db + cu-001) | ✅ Fait | Cowork |
| L0.15 | Brief revue vague 1 + I-002 inscrit (sortie de S0, transition pré-vague 2) | ✅ Fait | Cowork |

---

| L0.16 | Transmission `BRIEF-COWORK-HUB-IA-REVUE-VAGUE-1.md` au couple 1 | ✅ Fait | Blaise |
| L0.17 | Réception `RETOUR-I-002-REVUE-VAGUE-1.md` (3100 mots, 7 réponses) | ✅ Fait | Couple 1 |
| L0.18 | Intégration retour I-002 : SPEC v1.1, D-025, 3 briques transverses, corrections cu-001, glossaire, archivage I-002 | ✅ Fait | Cowork |
| L1.1 | Vague 2 — Enrichissement glossaire (eval-set, LLM-as-judge, reranker, retrieval-hybride, MTEB) | ✅ Fait | Cowork |
| L1.2 | Vague 2 — Production cu-008.md (référence canonique D-017, 11 sections H2) | ✅ Fait | Cowork |
| L1.3 | Vague 2 — Production pr-07.md (10 sections H2) | ✅ Fait | Cowork |
| L1.4 | Vague 2 — Production dep-02.md (12 sections H2) | ✅ Fait | Cowork |
| L1.5 | Vague 2 — Mise à jour cartographie-rag (3 nouvelles entrées détaillées) | ✅ Fait | Cowork |
| L1.6 | Brief revue vague 2 + inscription I-003 | ✅ Fait | Cowork |
| L1.7 | Transmission BRIEF-COWORK-HUB-IA-REVUE-VAGUE-2 au couple 1 | ⏳ En attente | Blaise |
| L1.8 | Réception RETOUR-I-003-REVUE-VAGUE-2 (~2600 mots, 5 réponses structurées) | ✅ Fait | Couple 1 |
| L1.9 | Intégration retour I-003 : SPEC v1.2 (R10), D-026, chiffres-macro étendu, matrice PR-07 alignée, wikilinks transverses, archivage I-003 | ✅ Fait | Cowork |
| L1.10 | Inscription I-D-001 (descendant) : harmonisation matrice PR-07 HTML 6 vs 8 critères, à traiter par couple 1 | ✅ Fait | Cowork (inscription) — couple 1 (traitement) |
| L1.11 | Sprint S1 Claude Code Plateforme — 6 lots livrés, 62/62 tests verts | ✅ Fait | Claude Code Plateforme |
| L1.12 | D-012-bis (MCP Obsidian reporté Phase 2) + D-027 (convention branches Claude Code) actées | ✅ Fait | Cowork |
| L1.13 | Brief CC-S1bis produit (validation end-to-end + PR) | ✅ Fait | Cowork |
| L1.14 | Transfert des 9 MD du vault Cowork-side vers branche Git (initialement annoncé « 10 » par erreur de comptage Cowork — correction post-S1bis) | ✅ Fait | Blaise |
| L1.15 | Transmission brief CC-S1bis à Claude Code Plateforme | ✅ Fait | Blaise |
| L1.16a | S1bis Lot S1b.1 — audit-md-rag sur vault réel + rapport classifié | ✅ Fait (150 écarts bruts, 0 violation éditoriale réelle après classification) | Claude Code Plateforme |
| L1.16b | S1bis Lot S1b.2 — validation end-to-end (ingest + retrieval + génération + eval) | ⏸ En pause (clés API absentes dans session) | Claude Code Plateforme |
| L1.16c | S1bis Lot S1b.3 — RAPPORT-CC-S1bis + ouverture PR | ✅ Partiel (RAPPORT + PR livrés sans S1b.2 — §3/§4 marqués non exécutés) | Claude Code Plateforme |
| L1.17 | Merge PR par Blaise après validation manuelle | ⏳ En attente | Blaise |
| L1.18 | S1ter — exécution S1b.2 différée (ingest + queries + eval) dès clés API | ⏳ Reporté session future | Claude Code Plateforme |
| L1.19 | Étape B (arbitrage catégorie D) + Étape C (SPEC v1.3 + D-028/D-029 + whitelist + 4e canonisation chiffres-macro 90 % + refactor wikilinks + I-D-002 + correctifs 9 vs 10) | ✅ Fait | Cowork |
| L1.20 | Sync rag-prep côté Git (push de SPEC v1.3, whitelist, DECISIONS étendu, JOURNAL/STATUS/cartographie/SYNC, chiffres-macro v3.8.4, glossaire v3.8.4, cu-008 v3.8.5) | ✅ Fait (commit `094931c` + `83cea32`) | Blaise |
| L1.21 | Création `.env` local avec ANTHROPIC_API_KEY et OPENAI_API_KEY dans `rag/code/.env` (gitignored) | ✅ Fait (côté Mac Blaise) | Blaise |
| L1.22 | Brief CC-S1ter produit (3 lots S1c.1 python-dotenv + S1c.2 validation end-to-end + S1c.3 RAPPORT + PR) | ✅ Fait | Cowork |
| L1.23 | Transmission `BRIEF-CC-S1ter-validation-end-to-end-avec-cles.md` à Claude Code Plateforme | ✅ Fait | Blaise |
| L1.24a | S1ter Lot S1c.1 — python-dotenv + tests + sanity check | ✅ Fait (67/67 tests verts, commit `9f0b341`) | Claude Code Plateforme |
| L1.24b | S1ter Lot S1c.2 — validation end-to-end (ingest réel + 10 queries + eval) | ⏸ Différé exécution locale Blaise (`.env` jamais synchronisé vers session web — par construction D-013) | Blaise (exécution) + Claude Code (analyse post-push si besoin) |
| L1.24c | S1ter Lot S1c.3 — RAPPORT-CC-S1ter + ouverture PR | ✅ Partiel (RAPPORT + PR livrés, §3/§4/§5 marqués « exécution locale Blaise ») | Claude Code Plateforme |
| L1.24d | **S1c.2 exécution locale Blaise** — ingest réel + 10 queries + run_eval | ✅ Fait (10/10 sources retrouvées, 9/10 concepts couverts, 107 chunks créés, coût ~0,30 $) | Blaise |
| L1.25 | Merge final PR #44 par Blaise — **clôture définitive sprint S1** | ✅ Fait (commit `9bef8c4` sur main) | Blaise |
| L1.26a | S2.2 Lot A — `pattern-llm-wiki.md` v3.8.6 + refactor cu-008/dep-02 | ✅ Fait (`b7c7f96`) | Cowork |
| L1.26b | S2.2 Lot B — Extension golden set 10 → 30 questions | ✅ Fait (`b7c7f96`) | Cowork |
| L1.26c | S2.2 Lot C — Métriques coût + pre-commit hook + system prompt enrichi | ✅ Fait (`127de86`, 159/159 tests) | Claude Code Plateforme |
| L1.26d-bis | S2.2 Lot D blocker — fix YAML int values q-016/019/027 | ✅ Fait (`00d80e8`, auto-correction Desktop exception D-022 validée par Blaise) | Claude Code Desktop |
| L1.26d | S2.2 Lot D — Eval extended sur vault enrichi (1er run, partiel) | ✅ Partiel (`fa8fc88` : 15/30 questions q-016 → q-030 ; 9/15 sources, 15/15 concepts ≥ 50 % ; coût 0,71 $ — bug extraction wikilinks identifié) | Claude Code Desktop |
| L1.26e.1 | S2.2 Lot E.1 — Fix `extract_cited_codes` wikilinks Obsidian dans `query.py` | ✅ Fait (`34496cb`, mergé via PR #47 → main) | Claude Code Plateforme |
| L1.26d.2 | S2.2 Lot D rerun final — Eval complet 30q post-fix wikilinks | ✅ Fait (`af18810` : **30/30 sources, 30/30 concepts ≥ 50 %, 30/30 score global** ; cible brief 24/30 largement atteinte ; coût cumulé Lot D 1,41 $ ; latence moy. 16,4 s/q) | Claude Code Desktop |
| L1.26e.2 | S2.2 Lot E.3 — RAPPORT-CC-S2.2 + PR finale | ✅ Fait (`rag-prep/reports/RAPPORT-CC-S2.2.md` en 8 sections + PR #48 ouverte) | Claude Code Plateforme |
| L1.27 | **S2.3 ouverture** — SPEC v1.5 (4 props validées) + BRIEF-CC-S2.3 produit | ✅ Fait Cowork (13 mai 2026) — sync ascendante à effectuer par Blaise | Cowork |
| L1.27a | S2.3 Lot A — transmission sondage à Cowork Hub IA + attente RETOUR-SONDAGE | ✅ Fait (RETOUR-SONDAGE reçu 13 mai, D-026 validé empiriquement, 4 dérives sémantiques évitées) | Cowork (transmission) + Cowork Hub IA (canal parallèle) |
| L1.27b | S2.3 Lot B — production cu-026 + cu-027 + dep-08 selon RETOUR-SONDAGE | ✅ Fait Cowork (3 MD ~4700 mots + patch chiffres-macro I-D-005 + whitelist v2, 4 dérives évitées, 3 passages bonus intégrés, 0,00 $) — sync ascendante à effectuer par Blaise | Cowork |
| L1.27c | S2.3 Lot C — enrichissement synonymes 30 q existantes + ajout vague 3 | ✅ Fait Cowork v2 ajusté post-RETOUR (`questions-v2-s2.3.yaml` : **42 questions** — 30 enrichies + 9 vague 3 corrigées + 3 bonus ; AP-5 ✅ ; 0,00 $) — sync ascendante à effectuer par Blaise | Cowork |
| L1.27d | S2.3 Lot D — adapt `evaluate_one()` synonymes liste-de-listes + tests + (R11 optionnel) | ✅ Fait Plateforme (`78d0fa7`, PR #53 mergée) : `concept_matched()` + 19 nouveaux tests sur 5 classes, 190/190 verts, 0,00 $ ; R11 wikilink audit reporté (charge non bloquante) | Claude Code Plateforme |
| L1.27e | S2.3 Lot E — eval extended 42q post-vault enrichi | ✅ Fait (`a8e8977` branche `claude/execute-s23-lot-e-eval-42q` : **41/42 sources retrouvées, 41/42 concepts ≥ 50 %, 41/42 score global**, latence moy. 16,6 s/q ; **5 faux négatifs S2.2 résolus** via option B synonymes ; vague 3 retrieval 11/12 ✅, **1 échec q-038** dep-08 concepts détaillés ; **coût Lot E 1,02 $ Anthropic** — cap durci 0,90 $ dépassé +13 %, acceptable) | Claude Code Desktop |
| L1.27f | S2.3 Lot F — RAPPORT-CC-S2.3 + PR finale S2.3 | ✅ Fait (`rag-prep/reports/RAPPORT-CC-S2.3.md` 8 sections + PR finale ouverte depuis `claude/execute-s23-lot-f-rapport`) | Claude Code Plateforme |

---

## Vague 1 + Vague 2 — bilan production MD (corrigé post-S1bis)

**Vault `content/`** :
- 1 glossaire canonique (`glossaire.md`, 23 termes après vague 2)
- 1 fiche outils (`ressources/outils-vector-db.md`)
- 3 briques transverses (`transverses/chiffres-macro-2026.md`, `vigilance-hallucinations.md`, `vigilance-confidentialite.md`)
- 2 modules CU (`modules/cu-001.md`, `modules/cu-008.md` ← référence canonique D-017)
- 1 préalable PR (`prealables/pr-07.md`)
- 1 fiche déploiement DEP (`deploiement/dep-02.md`)

**Total : 9 fichiers MD du vault** (correction post-S1bis : Claude Code Plateforme a relevé un écart 9 vs 10 — mes décomptes précédents annonçaient 10 par erreur de comptage Cowork ; le nombre réel est 9). ~1100 lignes de contenu MD production.

---

## Blockers actifs

**Pause sprint S2 actée** en attente de fin d'itération couple 1 (signal I-D-003). Aucun blocker côté couple 2.

**Reprise attendue** : à la notification Blaise de fin d'itération couple 1 (Cowork Hub IA + Claude Code Hub IA livrent leur PR éditoriale sur main du repo `hub-ia`).

## Sprint S2 — découpé en 3 sous-sprints (S2.1, S2.2, S2.3) — séquencement acté

**D-030 actée** : architecture Claude Code hybride. Allocation au cas par cas dans chaque brief.

| Sous-sprint | Périmètre | Allocation D-030 | Statut |
|---|---|---|---|
| **S2.1** | Audit-md-rag v2 (D-028, D-029, R5-R10) | Claude Code Plateforme seul | ✅ **Mergé PR #45** (134/134 tests verts, vault audit 0 erreur + 183 warnings catégorisés) |
| **S2.2** | Brique `pattern-llm-wiki.md` + extension golden set 30 questions + métriques coût + pre-commit hook | Cowork + Plateforme + Desktop pour eval | 🟢 **Lots A+B+C+D livrés**. Lot D partiel q-016 → q-030 (15/30), crash bloquant sur q-016 (golden set int non-quoté) corrigé par auto-correction Desktop (commit `00d80e8`). Eval partiel `fa8fc88`. Bug extraction wikilinks identifié → Lot E. |
| **S2.3** | Vague 3 modules denses (cu-026, cu-027, dep-08) en co-production avec Cowork Hub IA (D-026) + matching sémantique synonymes + golden set 42q | Cowork + Cowork Hub IA + Plateforme + Desktop | 🟢 **Lots A→E livrés**. Eval Lot E 41/42 score global, cibles dépassées. Reste Lot F (RAPPORT + PR finale). |
| **S2.5** (nouvelle — issue v3.9) | **Vague 3.5** modules patchés v3.9 : `dep-03.md`, `dep-04.md`, `dep-05.md`, `pr-04.md` | Cowork + Cowork Hub IA (sondage co-produit DEP-05 §8) + Desktop pour eval | 🟡 **À cadrer post-S2.3** — les 4 modules n'existent pas encore dans le vault, production intégrale (pas refactor) |

## Reprise sprint S2 — post-itération couple 1 v3.9 — étapes A-I livrées

**Cause de reprise** : itération couple 1 v3.9 terminée et mergée (PR #46). Message de passation reçu. Sprint S2 reprend avec intégration intégrale du périmètre v3.9.

**Bilan étapes A-I (production Cowork 12 mai post-passation v3.9)** :

| Étape | Livrable | Statut |
|---|---|---|
| A | Rebaseline JOURNAL/STATUS/SYNC depuis Git post-v3.9 | ✅ Fait |
| B | Clôture I-D-004 dans SYNC-INTER-CANAUX | ✅ Fait |
| C | Canonisation 6 chiffres macro 2026 dans `chiffres-macro-2026.md` v3.8.5 (I-D-003 traité) | ✅ Fait |
| D | Refactor `pr-07.md` v3.8.5 — intégration encart « troisième voie 2026 — fine-tuning SLM » | ✅ Fait |
| E | Arbitrage règle « outil glossarié wikilinké » → reporté audit v3 (R11 roadmap) | ✅ Fait |
| F | Décision scope : **Scénario 2** — Vague 3 inchangée (CU-026/CU-027/DEP-08) + nouvelle **Vague 3.5** (DEP-03/DEP-04/DEP-05/PR-04) | ✅ Fait |
| G | Acceptation proposition couple 1 — sondage co-produit DEP-05 §8 (à activer vague 3.5) | ✅ Fait |
| H | Production SPEC v1.4 (3 arbitrages + roadmap audit v3 enrichie) | ✅ Fait |
| I | Update STATUS + JOURNAL + cartographie-rag | 🟡 En cours (this commit) |

**Plan d'action documenté à la reprise** (4 étapes) :

1. **Synchronisation avec couple 1** : réception notification fin d'itération via Blaise (liste des fichiers HTML créés/modifiés). Identification des impacts sur la couche MD (nouvelle vague à produire ? refactor existants ? évolution RULES ?). Mise à jour `whitelist-wikilinks-futurs.md` si nouveaux codes apparaissent.
2. **SPEC v1.4** : production des 3 arbitrages Cowork préparés dans `rag-prep/briefs/ARBITRAGE-COWORK-SPEC-v1.4.md` (P1 codifier R6 warning par défaut ✅, P2 R5 v3 reporté audit v3 ✅, P3 documenter options strict ✅). Effort 30-45 min.
3. **Sprint S2.2** : finalisation `DRAFT-BRIEF-CC-S2.2.md` (§6/§7/§8 prudence + checklist + fichiers de référence) → transmission Claude Code Plateforme. 4 lots A→E, ~7-10 h split entre Cowork/Plateforme/Desktop.
4. **Sprint S2.3** : transmission `DRAFT-SONDAGE-COWORK-HUB-IA-S2.3-PRE-PRODUCTION.md` au couple 1 (9 passages sensibles cu-026/cu-027/dep-08). Production des 3 modules denses après réception sondage. Eval post-production sur vault élargi (12-13 fichiers).

**Livrables Sprint S2 anticipés (à valider via brief CC-S2)** :

| # | Livrable | Acteur principal | Priorité |
|---|---|---|---|
| L2.1 | Audit-md-rag v2 (implémenter D-028 exception R1 + D-029 whitelist + R6 reconnaît wikilinks canoniques + R5/R7/R8/R9/R10) | Claude Code Plateforme | 🔴 Haute (avant production vague 3) |
| L2.2 | Brique transverse `pattern-llm-wiki.md` (urgent — recouvrement cu-008 ↔ dep-02 confirmé) | Cowork + co-production Cowork Hub IA (D-026) | 🔴 Haute |
| L2.3 | Vague 3 modules denses : `cu-026.md` (Gouvernance agents IA), `cu-027.md` (Faire développer une appli), `dep-08.md` (Sécurité agents et MCP) | Cowork + co-production Cowork Hub IA (D-026 sondage préalable) | 🟡 Moyenne |
| L2.4 | Brique transverse `pattern-eval-set-golden.md` (couplée avec dep-07 à produire) | Cowork | 🟡 Moyenne |
| L2.5 | Extension golden set 10 → 30 questions | Cowork + Claude Code Plateforme | 🟡 Moyenne |
| L2.6 | Métriques de coût instrumentées dans `query.py` et `ingest.py` | Claude Code Plateforme | 🟢 Basse |
| L2.7 | Pre-commit hook audit-md-rag sur `rag/content/` | Claude Code Plateforme | 🟢 Basse |
| L2.8 | Enrichissement system prompt query.py (briques transverses + whitelist) | Claude Code Plateforme | 🟢 Basse |

**Question ouverte avant cadrage S2** : D-030 — adoption Claude Code Desktop pour exécutions locales ?

## Bilan global Sprint S1 (clôturé)

- **Vault** : 9 fichiers MD, 107 chunks indexés, ~1100 lignes contenu
- **Code** : pipeline RAG complète (audit + ingestion + backend + eval), 67/67 tests verts
- **Eval** : 10/10 sources retrouvées, 9/10 concepts couverts sur golden set initial
- **Référentiel** : 29 décisions actées, SPEC v1.3 (10 règles + 9 anti-patterns), whitelist 69 codes
- **Coordination** : 3 items inter-canaux archivés, 2 descendants ouverts vers couple 1
- **Coût total** : ~0,30 $ API consommés sur 8 $ de crédits disponibles
- **Hackathon de septembre** : trajectoire respectée, S2 peut démarrer immédiatement
- **Arbitrage Cowork des 7 chiffres orphelins catégorie D résolu** : 1 canonisation (90 %), 1 item descendant I-D-002 inscrit pour le couple 1, 5 chiffres conservés tel quel (acceptables ou faux positifs R6).
- **Vague 3 à venir** (CU-026, CU-027, DEP-08) avec application D-026 (sondage Cowork Hub IA préalable sur 2-3 passages sensibles). Voir aussi production prioritaire de `pattern-llm-wiki.md` (recouvrement cu-008 ↔ dep-02 confirmé).

## Vague 3 anticipée — modules N3/N4 à produire

Trois briques transverses prioritaires à extraire AVANT ou EN PARALLÈLE de la vague 3 (recommandation Q4 du retour I-003) :

| Brique transverse | Urgence | Modules concernés | Effort estimé |
|---|---|---|---|
| `pattern-llm-wiki.md` | 🔴 Haute (recouvrement déjà confirmé cu-008/dep-02) | cu-008, dep-02, cu-025, cu-014 | 1-2 h (distillation + refactor) |
| `pattern-eval-set-golden.md` | 🟡 Moyenne (à coupler avec dep-07) | dep-02, dep-07, cu-026, cu-008 | 1-2 h avec dep-07 |
| `pattern-build-vs-buy.md` | 🟢 Basse (à coupler avec module suivant qui s'y réfère) | pr-07, cu-024, cu-027, cu-014 | 1-2 h avec module appelant |

## Sprint suivant — S1 (pilote)

**Objectif** : 5 unités MD pilotes produites + infrastructure RAG opérationnelle (audit, ingestion, retrieval, génération, eval initial).

**Livrables S1 anticipés (en partie côté Cowork, en partie côté Claude Code Plateforme) :**

| # | Livrable | Acteur |
|---|---|---|
| L1.1 | 5 fichiers MD pilotes produits (CU-001, CU-008, PR-07, DEP-02, outils-vector-db) | Cowork (avec assistance couple 1 sur CU-008, PR-07, DEP-02) |
| L1.2 | `glossaire.md` v1 initial (termes utilisés dans les 5 pilotes) | Cowork |
| L1.3 | Infrastructure `rag/` dans repo `hub-ia` | Claude Code Plateforme (Lot 1 brief S1) |
| L1.4 | `audit-md-rag.py` v1 + tests | Claude Code Plateforme (Lot 3 brief S1) |
| L1.5 | Pipeline ingestion ChromaDB | Claude Code Plateforme (Lot 4 brief S1) |
| L1.6 | Backend CLI retrieval + génération Claude Sonnet 4.6 | Claude Code Plateforme (Lot 5 brief S1) |
| L1.7 | Golden set 10 questions + script eval | Claude Code Plateforme (Lot 6 brief S1) |
| L1.8 | Rapport mission S1 par Claude Code + ajustements `SPEC-MD-POUR-RAG.md` v2 par Cowork | Les deux |

---

## Plan d'action global (rappel)

| Sprint | Période | Livrable principal |
|---|---|---|
| **S0** | mi-mai → début juin (3 sem.) | Cadrage : RetEx, conventions, specs, décisions techniques |
| **S1** | juin (3 sem.) | Pilote retranscription 5 unités + setup canal Claude Code Plateforme + premier pipeline ChromaDB |
| **S2** | juin-juillet (5 sem.) | Migration MD complète (145 unités) + pipeline RAG backend opérationnel |
| **S3** | juillet-août (3 sem.) | Widget public sur le Hub + capture feedback |
| **S4** | août (3 sem.) | Eval + récit hackathon |
| **Hackathon** | septembre 2026 | Démonstration |

---

## Métriques de progression (à activer post-S0)

- Nombre de fichiers MD produits / 145
- Nombre de questions du golden set évaluées
- Qualité moyenne des réponses (notation manuelle 1-5)
- Coût mensuel API
- Latence moyenne des réponses

---

## Prochaine session prévue

À la réception du RetEx couple 1, démarrage de la consolidation `_instructions-rag.md` v1 et production de `STRATEGIE-MD-RAG.md`.
