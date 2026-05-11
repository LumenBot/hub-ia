# STRATEGIE-MD-RAG.md — Méthodologie de retranscription HTML → MD optimisé RAG

**Statut :** v1 (initiale)
**Dernière mise à jour :** 11 mai 2026
**Maintainer :** Cowork Hub IA Plateforme

> **Rôle :** définir **comment** transposer le contenu HTML du Hub IA en fichiers MD optimisés RAG. Ce fichier traite de la **stratégie d'analyse, sélection et production**. Pour le format technique des MD (frontmatter, chunking, naming), voir `SPEC-MD-POUR-RAG.md`.

---

## Principe directeur

Un fichier MD pour RAG n'est **pas** une réécriture exhaustive du HTML. C'est une **distillation orientée fonction**. Le critère unique est : *« est-ce que ce contenu, isolé dans un chunk de 400-700 tokens, peut servir une réponse utile à une question typique de visiteur Hub IA ? »*. Si non → on élimine. Si oui → on conserve, mais on reformule pour autonomie sémantique.

Les fichiers MD du vault et les fichiers HTML du site sont **deux œuvres parallèles non équivalentes**, optimisées pour deux publics radicalement différents (LLM vs humain).

---

## Démarche d'analyse — 5 questions à appliquer à chaque module HTML

Avant toute production MD, le module HTML source est passé au crible de ces 5 questions :

1. **Quelles sont les unités de connaissance autonomes contenues dans cette page ?** (Une définition, un cas d'usage, une comparaison, une procédure, un panorama d'outils, un RetEx anonymisé…)
2. **Quels chiffres, sources, citations sont indispensables et doivent être préservés exactement ?** (Pour traçabilité et conformité RULES 1.1)
3. **Quels concepts sont définis pour la première fois ici et méritent une entrée dans le glossaire canonique ?** (Pour cohérence cross-modules)
4. **Quels liens cross-modules sont implicites dans le texte et doivent devenir des wikilinks explicites ?** (Pour navigation Phase 2 LLM Wiki)
5. **Que dirait Cowork Hub IA si je lui demandais "qu'est-ce qu'il ne faut absolument pas perdre dans ce module" ?** → identifie ce qui mérite assistance contextuelle du couple 1.

---

## Ce qu'on conserve systématiquement

1. **Texte pédagogique structuré du corps des sections** (h2, h3 et contenu en prose, listes, exemples)
2. **Tableaux de décision** (RAG vs Fine-tuning, niveaux de maturité, etc.) — chunks à très haut intérêt RAG
3. **Listes structurées** (pièges à éviter, prérequis, étapes, critères) — chacune devient un chunk autonome
4. **Définitions et gloses** — extractibles en glossaire canonique partagé
5. **Chiffres sourcés** (« 95 % MIT Sloan / NANDA 2025 ») — citables par le RAG avec sourcing
6. **Exemples concrets et RetEx anonymisés** — réponses à valeur ajoutée
7. **Cas d'usage par profil** (« ce module est pour toi si… ») — utilisés pour filtrer par profil utilisateur
8. **Liens entre modules** — transposés en wikilinks `[[cu-008]]`

---

## Ce qu'on élimine

1. **Chrome navigationnel** : nav, footer, breadcrumb, boutons retour, reading progress, sticky TOC — zéro valeur sémantique
2. **Éléments visuels purs** : badges colorés, gradients, callouts décoratifs sans contenu nouveau, encadrés rhétoriques
3. **Composants interactifs** : auto-diagnostics, quiz, scripts — leur valeur dépend du JS, illisible en MD pur
4. **Executive summaries dans leur forme actuelle** : on conserve la **substance** (4 takeaways + stats + « pour toi si… ») mais reformulée en chunks sémantiquement autonomes, pas en bloc gradient bleu marine
5. **Redondances pédagogiques** : phrases d'introduction destinées à humaniser la lecture (« Comme on l'a vu plus haut… », « Imagine que tu es… ») — bruit pour le RAG

---

## Méthode de migration progressive

Plutôt que de figer la spec en théorie puis migrer 145 unités d'un coup, on opère en **boucle d'apprentissage** :

### Phase pilote (Sprint S1)

5 unités choisies pour leur diversité :
- 1 CU simple (proposition : **CU-001 Recherche & veille**, ⭐)
- 1 CU dense méta-récursif (référence canonique : **CU-008 Knowledge base RAG**, ⭐⭐⭐) — devient la référence canonique D-017
- 1 préalable PR (proposition : **PR-07 Build vs Buy**, transverse)
- 1 fiche déploiement DEP (proposition : **DEP-02 RAG en production**, méta-récursivité côté technique)
- 1 catégorie de fiches outils (proposition : **outils-vector-db.md** regroupant Pinecone, Qdrant, Weaviate, ChromaDB)

Pour chaque unité :
1. Application des 5 questions d'analyse
2. Production MD selon `SPEC-MD-POUR-RAG.md`
3. Validation manuelle par Blaise (sondage qualité)
4. Test d'indexation ChromaDB
5. Test sur 5-10 questions types
6. Identification des ratés (chunks qui ne servent pas, formulations trop liées au HTML, manques)

À l'issue du pilote : **ajustement de `SPEC-MD-POUR-RAG.md` en v2** sur la base des apprentissages. Discipline alignée sur le cycle **Stitch → Evaluate → Iterate** (DEP-02).

### Phase scale (Sprint S2)

Migration des 145 unités par lots successifs, dans cet ordre :
1. **Lot CU-simples** : CU-001 → CU-007 + CU-019 + CU-023 (⭐ à ⭐⭐)
2. **Lot CU-denses** : CU-008 (déjà fait), CU-010 → CU-014, CU-020 → CU-027 (⭐⭐ à ⭐⭐⭐⭐) — assistance Cowork Hub IA obligatoire
3. **Lot CU-agentiques** : CU-015, CU-016, CU-017, CU-018 (⭐⭐⭐⭐) — assistance Cowork Hub IA obligatoire
4. **Lot Préalables PR** : PR-01 → PR-07 — assistance Cowork Hub IA systématique (cadrages transverses denses en chiffres et RetEx)
5. **Lot Déploiement DEP** : DEP-01 → DEP-08 (le DEP-02 déjà fait en pilote)
6. **Lot Architectures** : A1, A2, A3, A4, hybride
7. **Lot Fiches outils** : ~15 fichiers MD par catégorie (de `outils-llm.md` à `outils-knowledge-management.md`)

À la fin de chaque lot : validation qualité par sondage + mise à jour `cartographie-rag.md`.

---

## Co-production avec Cowork Hub IA (couple 1)

Conformément à D-022 (spécialisation des rôles) et au RetEx Q2 §4, Cowork Hub IA Plateforme produit les MD seul **uniquement** sur les unités simples. Pour les unités denses, **co-production systématique** :

| Unité | Mode | Justification |
|---|---|---|
| CU-001 à CU-007, CU-019, CU-023 (⭐ à ⭐⭐) | Cowork seul, validation sondage Blaise | Pédagogie linéaire, peu de subtilités éditoriales |
| CU-008 à CU-018, CU-020 à CU-027 (⭐⭐⭐ à ⭐⭐⭐⭐) | Co-production avec Cowork Hub IA | Densité, nuances éditoriales, RetEx à préserver |
| PR-01 à PR-07 | Co-production systématique | Cadrages transverses chargés en chiffres sourcés et arbitrages éditoriaux |
| DEP-01 à DEP-08 | Co-production sur DEP-04 à DEP-08 (techniques avancées), Cowork seul sur DEP-01 à DEP-03 | DEP-04+ nécessitent maîtrise technique fine |
| Architectures | Cowork seul | Contenu structuré, peu d'ambiguïté |
| Fiches outils | Cowork seul après template validé par couple 1 sur 1 catégorie pilote | Structure très répétitive |

**Modalité de co-production** : Cowork Hub IA Plateforme produit le squelette MD (frontmatter, structure, wikilinks, métadonnées). Cowork Hub IA relit et corrige la prose, valide les nuances éditoriales, signale les pertes de sens. Coordination via `SYNC-INTER-CANAUX.md`.

**Charge cognitive estimée Cowork Hub IA** : ~30-50 min par module dense, soit ~15-20 h total sur les ~25 modules denses. Lissé sur S2 (5 semaines), c'est ~3-4 h/semaine — gérable sans dégrader la production éditoriale propre du couple 1.

---

## Convention pour les nouveaux contenus à venir (post-S0)

À partir de la spec MD-pour-RAG figée (fin S0), chaque nouvelle itération éditoriale du couple 1 (v3.9, v4.0…) déclenche une production MD associée par le couple 2 :

1. Le couple 1 ajoute dans son rapport de fin d'itération une mention : *« contenu produit, à reprendre par couple 2 pour MD RAG : [liste fichiers HTML créés/modifiés] »*
2. Le couple 2 consomme cette mention via `SYNC-INTER-CANAUX.md`
3. Production MD selon démarche standard → commit dans `rag/content/`
4. Pipeline RAG re-indexe automatiquement (incrémental, D-019)

Blaise reste l'aiguilleur de cette coordination (rôle de garant transverse).

---

## Critères de succès du sprint S1 (pilote)

Le sprint pilote est réussi si, à son issue :

1. **5 fichiers MD produits** conformes à `SPEC-MD-POUR-RAG.md` v1
2. **Audit-md-rag.py** valide les 5 fichiers sans erreur
3. **Pipeline d'ingestion ChromaDB** opérationnel sur le vault pilote
4. **Premier set de 5-10 questions types** évalué → réponses notées manuellement (≥ 7/10 cible)
5. **`SPEC-MD-POUR-RAG.md` v2** rédigée intégrant les apprentissages du pilote
6. **`cartographie-rag.md`** enrichi des 5 unités pilotes

---

## Anti-patterns à éviter (issus du RetEx couple 1)

1. **Démarrer avec un cahier des charges exhaustif** → on démarre minimaliste (5-10 règles), on enrichit au fil des écarts détectés
2. **Cowork qui produit du code à l'aveugle** → si une production MD doit être validée par exécution (test d'ingestion, test de retrieval), c'est Claude Code qui exécute, pas Cowork
3. **Pas de discipline de validation** → chaque fichier MD produit passe par audit-md-rag.py avant d'être considéré comme livré
4. **Référence canonique implicite** → cu-008.md est explicitement la référence à copier (D-017)

---

## Historique des versions

| Version | Date | Modification |
|---|---|---|
| v1 | 11 mai 2026 | Version initiale post-RetEx couple 1 |
