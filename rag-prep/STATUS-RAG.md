# STATUS-RAG.md — État synthétique du sprint courant

**Dernière mise à jour :** 12 mai 2026
**Sprint en cours :** S1 — Pilote (côté Claude Code Plateforme : Lots 1, 3, 4, 5, 6 livrés ; Lot 2 délégué à Blaise ; côté Cowork : production des 5 MD pilotes en cours)
**Période :** juin 2026 (3 semaines)
**Acteurs mobilisés :** Claude Code Hub IA Plateforme + Cowork Hub IA Plateforme + Blaise

---

## Avancement S1 (couple 2)

| # | Livrable | Statut | Acteur |
|---|---|---|---|
| L1.1 | 5 MD pilotes (CU-001, CU-008, PR-07, DEP-02, outils-vector-db) | ⏳ En cours | Cowork |
| L1.2 | `glossaire.md` v1 | ⏳ En cours | Cowork |
| L1.3 | Infrastructure `rag/` | ✅ Fait (Lot 1) | Claude Code |
| L1.4 | `audit-md-rag.py` v1 + tests | ✅ Fait (Lot 3, 26 tests verts) | Claude Code |
| L1.5 | Pipeline ingestion ChromaDB + tests + incrémental | ✅ Fait (Lot 4, 14 tests verts) | Claude Code |
| L1.6 | Backend CLI retrieval + Claude Sonnet 4.6 + tests | ✅ Fait (Lot 5, 12 tests verts) | Claude Code |
| L1.7 | Golden set 10 questions + run_eval.py + tests | ✅ Fait (Lot 6, 10 tests verts) | Claude Code |
| L1.8 | Rapport mission S1 | ✅ Fait (`briefs/RAPPORT-CC-S1.md`) | Claude Code |
| Lot 2 | Config MCP Obsidian côté Claude Code | ⏳ Local (Blaise) | Blaise |

**Suite tests `rag/code/` :** 62/62 verts.

**Branche développement :** `claude/execute-pilot-batches-mBSIp` (assignée par Blaise — substitue `feature/rag-s1-pilote` proposée dans le brief).

---

## Sprint précédent — S0 (clôturé)

**Sprint S0 (cadrage) :** terminé. Décisions D-001 à D-024 actées. 6 fichiers de gouvernance + briefs livrés. Push initial de `rag-prep/` effectué par Blaise (commit `ba7ff99`).

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
| L0.13 | Création du canal Claude Code Hub IA Plateforme | ⏳ En attente | Blaise |

---

## Blockers actifs

- **L0.12** : push initial de `rag-prep/` vers le clone Git puis le repo distant, par Blaise.
- **L0.13** : création du canal Claude Code Hub IA Plateforme, transmission du brief S1 à ce nouveau canal.

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
