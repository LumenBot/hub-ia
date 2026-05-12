# cartographie-rag.md — Cartographie d'ancrage du vault RAG

**Statut :** v0 (initial, à enrichir au fil des productions MD)
**Dernière mise à jour :** 11 mai 2026
**Maintainer :** Cowork Hub IA Plateforme

> **Rôle :** inventorier, par fichier MD du vault `rag/content/`, les 3-5 **angles thématiques principaux** qu'il couvre. Lu par Cowork avant chaque nouvelle production MD pour éviter les doublons d'indexation (D-019, RetEx couple 1 Q3 §4).

> **Différence avec `veille/cartographie-hub-ia.md` du couple 1** : ce fichier-ci porte sur les **chunks RAG indexés**, pas sur les unités éditoriales du site. Granularité plus fine, focus angles thématiques.

---

## Structure d'une entrée

Pour chaque fichier MD produit, on consigne :

```
### `{nom-fichier}.md` ({type})

**Titre** : ...
**Version** : ...
**Date d'ajout au vault** : YYYY-MM-DD
**Angles thématiques principaux** (3-5 angles) :
1. Angle 1 — courte description
2. Angle 2 — ...
...

**Mots-clés sémantiques** : ...

**Recouvrements connus avec d'autres fichiers** :
- `xxx.md` (angle commun : ...)
- ...
```

---

## Inventaire des fichiers MD du vault

### `glossaire.md` (transverse)

**Titre** : Glossaire canonique du Hub IA
**Version** : 3.8.2
**Date d'ajout au vault** : 2026-05-11
**Angles thématiques principaux** :
1. Vocabulaire technique RAG (RAG, vector store, embeddings, chunk, HNSW)
2. Vocabulaire d'architecture (API, SaaS, open-source, self-hosting, cloud souverain, souveraineté)
3. Vocabulaire LLM et usage (LLM, prompt, token, fine-tuning, hallucination)
4. Vocabulaire de stade projet (POC, MVP)

**Mots-clés sémantiques** : définitions, glossaire, vocabulaire, terminologie, RAG, LLM

**Recouvrements connus avec d'autres fichiers** :
- Référencé par TOUS les autres fichiers MD du vault via wikilinks `[[glossaire#terme]]`. Source unique de vérité, ne fait pas doublon.

---

### `outils-vector-db.md` (fiche-outil)

**Titre** : Outils — Vector stores
**Version** : 3.8.2
**Date d'ajout au vault** : 2026-05-11
**Angles thématiques principaux** :
1. Panorama des 4 vector stores du marché 2026 (Qdrant, pgvector, Pinecone, ChromaDB)
2. Critères de choix d'un vector store selon volume, souveraineté, ops
3. Modèles économiques comparés (open-source self-hosted vs SaaS managé)
4. Cas d'usage Hub par outil (cross-references cu-008, cu-013, cu-019)

**Mots-clés sémantiques** : vector store, vector database, base vectorielle, Pinecone, Qdrant, ChromaDB, pgvector, RAG, embeddings, self-hosting, souveraineté

**Recouvrements connus avec d'autres fichiers** :
- `cu-008.md` (à produire) : recouvre le panorama vector DB et le choix d'architecture RAG ; la fiche outils-vector-db.md reste la **source canonique du détail technique des outils**, cu-008.md la référencera plutôt que dupliquer.
- `dep-02.md` (à produire) : même logique — référence vers outils-vector-db.md pour le détail des outils, focus dep-02 sur les décisions d'architecture.

---

### `transverses/chiffres-macro-2026.md` (transverse — référentiel chiffres canoniques)

**Titre** : Chiffres macro IA — référentiel canonique 2026
**Version** : 3.8.4 (post-S1bis)
**Date d'ajout au vault** : 2026-05-11 (extensions 2026-05-12)
**Angles thématiques principaux** :
1. Référentiel canonique de **16 chiffres macro** du Hub IA (sources datées + formulation exacte)
2. Discipline anti-dérive : tout module qui cite un de ces chiffres wikilinke ici plutôt que de reformuler
3. Couverture adoption IA (55 % usage GenAI, 26 % usage intégré, 67 % manque de méthode…)
4. Couverture risque/ROI (95 % MIT NANDA sans ROI, 80-95 % causes organisationnelles, +270 % Microsoft)
5. Couverture marché travail (×5 productivité PwC, 77k offres, 3,7× IDC Copilot)
6. Couverture RAG : **1,8 h/jour McKinsey** + **90 % cas PME RAG bat fine-tuning** (ajout S1bis)
7. Couverture transformation : **21 % organisations IA workflows redesignés** McKinsey (ajout S1bis)

**Mots-clés sémantiques** : chiffres, statistiques, sources, Bpifrance, France Num, MIT NANDA, Microsoft, PwC, IDC, McKinsey, RAG, fine-tuning

**Recouvrements connus** : SOURCE UNIQUE pour ces chiffres. Tous les modules qui les mentionneront feront référence ici par wikilink. Élimine la dérive AP-1 identifiée en revue I-002 et formalise R9 SPEC v1.2.

---

### `transverses/vigilance-hallucinations.md` (transverse — vigilance commune)

**Titre** : Vigilance — hallucinations des LLM
**Version** : 3.8.2
**Date d'ajout au vault** : 2026-05-11
**Angles thématiques principaux** :
1. 3 types d'hallucinations (factuelles, sources, inférences)
2. Discipline en 3 règles (vérifier sources, ne pas prendre la synthèse pour acquise, faire diverger les sources)
3. Mitigations techniques (RAG + citations, prompt engineering, garde-fous, eval continue)
4. Cas d'application par module (CU-001, CU-002, CU-008, CU-011, CU-012, CU-020, CU-025)
5. Anti-patterns observés (confiance par défaut, citation non vérifiée, délégation du fact-checking)

**Mots-clés sémantiques** : hallucination, vérification, sourcing, fact-checking, qualité IA

**Recouvrements connus** : référencée par ~10 modules (CU-001 déjà, CU-002, CU-008, CU-009, CU-011, CU-012, CU-020, CU-025, PR-05, PR-06, DEP-07 à venir). Évite la duplication d'un même contenu de vigilance dans chaque module.

---

### `transverses/vigilance-confidentialite.md` (transverse — vigilance commune)

**Titre** : Vigilance — confidentialité des données dans les outils IA
**Version** : 3.8.2
**Date d'ajout au vault** : 2026-05-11
**Angles thématiques principaux** :
1. Le risque structurel des chatbots grand public (Cloud Act, entraînement, rétention)
2. 4 catégories de données à ne JAMAIS coller dans un chatbot grand public (personnelles, contractuelles, stratégiques, régulées)
3. 3 options pour traiter les données sensibles (Pro/Enterprise, EU souverain, self-hosted/on-premise)
4. Discipline en 4 règles (catégoriser, politique IA interne, anonymisation source, certifications éditeur)
5. Cas d'application par module + anti-patterns observés

**Mots-clés sémantiques** : confidentialité, RGPD, AI Act, souveraineté EU, données sensibles, ISO 27001, SOC 2, SecNumCloud

**Recouvrements connus** : référencée par ~8 modules (CU-001 déjà, CU-002, CU-005, CU-007, CU-008, CU-020, CU-024, PR-05). Évite la duplication des règles de confidentialité dans chaque module.

---

### `cu-008.md` (module-cu — RÉFÉRENCE CANONIQUE D-017)

**Titre** : Knowledge base interne (RAG)
**Version** : 3.8.3
**Date d'ajout au vault** : 2026-05-11
**Angles thématiques principaux** :
1. RAG vs Fine-tuning — quand choisir lequel (« 90 % des cas PME = RAG »)
2. Pipeline RAG en deux temps (ingestion + interrogation)
3. RAG classique vs LLM Wiki Karpathy (avril 2026) — comparatif architectural
4. Patterns LLM Wiki post-Karpathy (persistent memory, self-maintaining KB, contradiction detection, multi-agent vaults, sleep consolidation)
5. Stack et outils en 3 voies (no-code NotebookLM, open-source EU Dify/Flowise, enterprise Vectara/Glean)
6. Plan de déploiement en 4 paliers + 5 pièges à éviter
7. Architectures recommandées selon sensibilité corpus (A1/A3/A4)
8. RetEx Conseil aviation 25 personnes (gain 60 % temps recherche, coût récurrent 150 €/mois)

**Mots-clés sémantiques** : RAG, knowledge base, vector store, embeddings, LLM Wiki, Karpathy, fine-tuning, AMETRA, Pleias-RAG, garbage in garbage out

**Recouvrements connus avec d'autres fichiers** :
- `dep-02.md` (RAG en production) : recouvre LLM Wiki + RAG hybride + choix vector DB. `cu-008` reste orienté décideur, `dep-02` orienté technique.
- `outils-vector-db.md` : référencé pour le détail technique des outils.
- `vigilance-hallucinations.md` et `vigilance-confidentialite.md` : wikilinkés pour les vigilances.
- `chiffres-macro-2026.md` : 1,8 h/jour McKinsey est un chiffre spécifique CU-008, pas dans le référentiel macro (mais à ajouter si recouvrement détecté).

---

### `pr-07.md` (prealable-pr)

**Titre** : Build vs Buy à l'ère de l'IA
**Version** : 3.8.3
**Date d'ajout au vault** : 2026-05-11
**Angles thématiques principaux** :
1. 3 tendances qui changent l'arbitrage 2026 (compression dev IA-assisté, banalisation IA dans SaaS, pression réglementaire)
2. Le scaling gap — 95 % MIT NANDA sans ROI, 21 % redesigné workflows, 67 % vs 33 % Buy/Build
3. 6 situations « BUY reste le bon choix »
4. 5 situations « BUILD redevient pertinent »
5. Pattern hybride dominant 2026 (SaaS commodity + build léger métier + couches de composition)
6. Matrice de décision 6 critères (différenciation, volume, évolutivité, budget, compétences, délai)
7. 7 écueils à éviter (workflow non redesigné, dette maintenance, POC vs MVP, gouvernance, lock-in, conformité, dogme)

**Mots-clés sémantiques** : build vs buy, SaaS, MVP, POC, MIT NANDA, McKinsey, Retool, scaling gap, hybride, compression dev, AI Act 2026, facturation électronique

**Recouvrements connus avec d'autres fichiers** :
- `chiffres-macro-2026.md` : 95 % MIT NANDA et 67 % vs 33 % MIT NANDA wikilinkés (canoniques).
- `cu-008.md`, `cu-027.md`, `cu-024.md` : référencés comme cas d'usage build.
- `pr-01.md` (Maturité organisationnelle) : recouvre le scaling gap, à articuler proprement quand pr-01 sera produit.
- `dep-06.md` (Inférence et coûts) : référencé pour le détail SaaS vs self-hosted.

---

### `dep-02.md` (deploiement-dep)

**Titre** : RAG en production : choisir son architecture
**Version** : 3.8.3
**Date d'ajout au vault** : 2026-05-11
**Angles thématiques principaux** :
1. 3 ruptures 2025-2026 (RAG dense plafonne, LLM Wiki Karpathy, vector DB commoditisés)
2. Règle de décision en 30 secondes (volume / fréquence MAJ / nature)
3. LLM Wiki — coût-bénéfice mesuré (économie 90 % petits corpus)
4. RAG hybride — anatomie 7 étapes (chunking, embedding, indexation, query rewriting, retrieval hybride, reranking, generation)
5. Choix techniques par ordre d'impact (embedding 30-40 %, reranking +10-30 %, chunking, vector DB 5-10 %)
6. Tableau de décision RAG par volume + Choix vector DB top 5
7. 5 écueils RAG production
8. Cycle Stitch → Evaluate → Iterate + RetEx embedding #130 MTEB qui bat OpenAI
9. Plan d'action 60 jours pour un RAG production-ready

**Mots-clés sémantiques** : RAG production, retrieval hybride, reranking, chunking, eval set, LLM-as-judge, MTEB, dense + sparse, BM25, golden set

**Recouvrements connus avec d'autres fichiers** :
- `cu-008.md` : recouvre LLM Wiki et stack/outils. `dep-02` reste orienté technique production.
- `outils-vector-db.md` : référencé pour panorama vector DB détaillé.
- `dep-07.md` (Évaluation continue) : à produire, recouvrera l'eval pipeline et le LLM-as-judge calibré.
- `vigilance-hallucinations.md` : wikilinké pour la réduction 70-90 % des hallucinations.

---

### `cu-001.md` (module-cu)

**Titre** : Recherche & veille augmentée
**Version** : 3.8.2
**Date d'ajout au vault** : 2026-05-11
**Angles thématiques principaux** :
1. Premier usage IA en organisation (porte d'entrée la plus rentable, 0 € de coût d'entrée)
2. Panorama 3 outils pour 3 usages (Perplexity web, Le Chat Pro souverain, NotebookLM corpus)
3. Méthode d'utilisation en 4 étapes (question contextualisée, vérification sources, itération, capitalisation)
4. Vigilances structurantes (hallucinations, confidentialité, paresse intellectuelle)
5. Cas d'usage type — préparation comité de direction

**Mots-clés sémantiques** : recherche augmentée, veille, Perplexity, Mistral, NotebookLM, hallucination, confidentialité, prompt, sources

**Recouvrements connus avec d'autres fichiers** :
- `cu-002.md` (Assistant rédactionnel) : couvre la production écrite IA — recouvrement faible, complémentarité.
- `cu-011.md` (Veille concurrentielle) : approfondit le pattern veille — recouvrement modéré (cu-001 = démarrage / cu-011 = veille soutenue), à articuler explicitement à la production de cu-011.
- `pr-05.md` (Sécurité IA) : reprend la vigilance confidentialité de façon transverse — wikilink explicite dans cu-001.
- Stat Bpifrance « 67 % dirigeants n'ont pas commencé » : à confronter avec celle de [[pr-04]] (Marché IA & emploi) lors de sa production pour éviter le doublon.

---

## Sujets à fort recouvrement attendu (vigilance prioritaire)

D'après la cartographie d'ancrage du couple 1 (`Canaux/Hub-IA/veille/cartographie-hub-ia.md`), les sujets suivants apparaissent dans plusieurs modules sources et nécessitent une vigilance particulière à l'indexation RAG pour éviter les doublons :

1. **RAG vs Fine-tuning** : traité dans CU-008 (orienté décideur) et DEP-02 (orienté technique) — angles complémentaires à préserver
2. **LLM Wiki Karpathy** : CU-008 (présentation) + DEP-02 (comparatif avec RAG hybride) + transverse possible Phase 2
3. **Architectures (4 patterns A1-A4 + hybride)** : page Architectures + nombreux modules CU qui y renvoient
4. **AI Act / RGPD** : CU-020 (module dédié) + encarts dans CU-002, CU-009, CU-010, CU-019, CU-024
5. **Gouvernance des agents** : CU-014 (multi-agents) + CU-026 (gouvernance dédiée) + DEP-05 (observabilité agents)
6. **Build vs Buy** : PR-07 (cadrage transverse) + CU-027 (appli métier)
7. **Compression coûts dev IA-assisté** : CU-027 + PR-07
8. **Chiffres macro** (95 % MIT NANDA, 76 % France Num, 70-95 % Gartner/McKinsey/Deloitte) : présents dans plusieurs modules — gérer par référence unique au glossaire ou à un fichier transverse plutôt que duplication

**Stratégie pour ces sujets à recouvrement** : créer des fichiers `transverse-{slug}.md` qui portent canoniquement l'angle, et faire référencer ces fichiers via wikilinks depuis les modules concernés au lieu de réindexer le même contenu.

---

## Historique des versions

| Version | Date | Modification |
|---|---|---|
| v0 | 11 mai 2026 | Initialisation, structure définie, premiers sujets à recouvrement identifiés |
