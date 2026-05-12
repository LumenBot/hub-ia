# STATUS-RAG.md — État synthétique du sprint courant

**Dernière mise à jour :** 11 mai 2026
**Sprint en cours :** S0 — Cadrage
**Période :** mi-mai → début juin 2026 (3 semaines)
**Acteurs mobilisés :** Cowork Hub IA Plateforme + Blaise + interaction couple 1 (via RetEx)

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
| L1.14 | Transfert des 10 MD du vault Cowork-side vers branche Git | ⏳ En attente | Blaise |
| L1.15 | Transmission brief CC-S1bis à Claude Code Plateforme | ⏳ En attente | Blaise |
| L1.16 | Exécution S1bis (audit-md-rag réel + validation end-to-end + RAPPORT + PR) | ⏳ En attente | Claude Code Plateforme |
| L1.17 | Merge PR par Blaise après validation manuelle | ⏳ En attente | Blaise |

---

## Vague 1 + Vague 2 — bilan production MD

**Vault `content/`** :
- 1 glossaire canonique (`glossaire.md`, 23 termes après vague 2)
- 1 fiche outils (`ressources/outils-vector-db.md`)
- 3 briques transverses (`transverses/chiffres-macro-2026.md`, `vigilance-hallucinations.md`, `vigilance-confidentialite.md`)
- 3 modules CU (`modules/cu-001.md`, `modules/cu-008.md` ← référence canonique D-017)
- 1 préalable PR (`prealables/pr-07.md`)
- 1 fiche déploiement DEP (`deploiement/dep-02.md`)

**Total : 10 fichiers MD du vault**, ~1000 lignes de contenu MD production.

---

## Blockers actifs

- **L1.14** : transfert des 10 MD du vault Cowork-side vers la branche Git `claude/execute-pilot-batches-mBSIp` par Blaise. Procédure documentée.
- **L1.15** : transmission du `BRIEF-CC-S1bis-validation-end-to-end.md` à Claude Code Plateforme par Blaise.
- Puis exécution autonome de S1bis par Claude Code Plateforme + PR ouverte + merge manuel par Blaise.
- **Vague 3 à venir** (CU-026, CU-027, DEP-08) avec application D-026 (sondage Cowork Hub IA préalable sur 2-3 passages sensibles).

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
