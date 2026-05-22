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

### `transverses/pattern-llm-wiki.md` (transverse — pattern architectural)

**Titre** : Pattern LLM Wiki — alternative architecturale au RAG classique
**Version** : 3.8.6
**Date d'ajout au vault** : 2026-05-12 (S2.2 Lot A)
**Angles thématiques principaux** :
1. RAG classique stateless vs LLM Wiki synthèse persistante (différence en deux phrases)
2. Tableau de décision par volume corpus (< 50K, 50K-100K, 100K-1M, > 1M, MAJ temps réel)
3. Cas types pertinents PME (manuel produit, FAQ, procédures RH, doc projet)
4. Coût-bénéfice mesuré (~95 % économie sur petits corpus, ~10-50 €/mois vs 150-300 €)
5. 5 patterns post-Karpathy : persistent memory, self-maintaining KB, contradiction detection, multi-agent vaults, sleep consolidation
6. 3 questions à se poser avant de choisir LLM Wiki vs RAG classique

**Mots-clés sémantiques** : LLM Wiki, Karpathy, RAG, synthèse persistante, base markdown, persistent memory, self-maintaining KB, contradiction detection, multi-agent vaults, sleep consolidation

**Recouvrements connus avec d'autres fichiers** :
- `cu-008.md` (Knowledge base RAG) : sections « Au-delà du RAG classique » + « Patterns LLM Wiki post-Karpathy » remplacées par renvoi `[[pattern-llm-wiki]]` + résumé court (refactor S2.2 Lot A — élimine la duplication ~30-40 lignes confirmée en revue I-003).
- `dep-02.md` (RAG en production) : section « LLM Wiki Karpathy — alternative crédible pour les petits corpus » remplacée par renvoi `[[pattern-llm-wiki]]` + résumé technique court.
- À référencer aux futures productions : `cu-014` (Multi-agents — synergie pattern multi-agent vaults), `cu-025` (Knowledge management dirigeant — pattern proche).

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

## Vague 4 — ajouts S2.4 Phase 2 (mai 2026, post-v3.10 + v3.11 HTML)

### `pattern-persistent-memory.md` (transverse)

**Titre** : Pattern Persistent memory pour agents IA (4 signaux convergents)
**Version** : 3.11.0
**Date d'ajout au vault** : 2026-05-13
**Angles thématiques principaux** :
1. 4 signaux convergents mai 2026 (Long context SubQ / LLM Wiki post-Karpathy / Persistent memory Vargas / agentmemory infrastructure)
2. Benchmarks agentmemory (95,2 % r@5 vs 86,2 % BM25 + coût token ÷ 100+)
3. Écosystème hooks 6 outils (Claude Code, Hermes Agent, OpenClaw, Codex CLI, Cursor, Gemini CLI)
4. Distinction conceptuelle vs LLM Wiki (synthèse stable vs mémoire stateful)
5. Préfiguration pattern A5 « Agents fédérés / persistent memory »

**Mots-clés sémantiques** : persistent memory, agentmemory, hooks multi-agents, mémoire conversationnelle, SQLite + FAISS, stateful, Jean Vargas

**Recouvrements connus** :
- `pattern-llm-wiki.md` : 2 patterns distincts mais convergents (table comparative incluse dans pattern-persistent-memory.md §Distinction conceptuelle)
- `cu-008.md` : encart H2 dédié « Persistent memory pour agents IA — 4 signaux convergents » avec renvoi pattern-persistent-memory
- `dep-02.md` : encart H2 dédié « Implication opérationnelle — architecture pour agent avec mémoire conversationnelle » avec mini-tableau profils workload distinct du tableau §4

### `pr-08.md` (préalable-pr) — nouveau préalable

**Titre** : Financer son projet IA en 2026
**Version** : 3.11.0
**Date d'ajout au vault** : 2026-05-13
**Angles thématiques principaux** :
1. 3 ruptures structurelles 2026 (CII-IA nouveau, France 2030 phase diffusion, convergence Bpifrance + DGE + Hub France IA)
2. Tableau 7 dispositifs fiscaux (CIR, CII, CII-IA, JEI, JEII, CICO, C3IV) + 5 profils PME
3. France 2030 — Plan « Osez l'IA » + 2 deadlines juin 2026 (AMI 5 juin + AAP 9 juin)
4. 4 leviers Bpifrance (diagnostics 40 %, formation 9 403 dirigeants, prêts, capital 240 M€ ×14)
5. Méthode — règle des 5 étapes + 5 pièges à éviter + plan d'action 30 jours

**Mots-clés sémantiques** : financement IA, CIR, CII, CII-IA, JEI, JEII, France 2030, IA Booster, Bpifrance, AMI, AAP, fiscalité innovation

**Recouvrements connus** :
- `pr-04.md` (Marché IA & emploi) : callout-info §1 référence explicite (à produire en S2.5)
- `dep-04.md` (Fine-tuning PME) : callout-info §2 référence explicite (à produire en S2.5)
- `cu-027.md` : mention discrète CII-IA pour dépenses calcul intensif GPU/CPU (stack ECC)
- `chiffres-macro-2026.md` v3.9.0 : wikilink direct vers 240 M€ Bpifrance (canonisé I-D-006)
- **PAS de wikilink vers PR-07** (rectification RETOUR-SONDAGE-S2.4 §1.3 — « couple 1 tranche, couple 2 s'aligne »)

### `cu-008.md` (refactor S2.4 — v3.8.6 → v3.11.0)

**Modification structurelle** : ajout section H2 « Persistent memory pour agents IA — 4 signaux convergents (mai 2026) » entre LLM Wiki et Stack outils. Lead bridge enrichi pattern Lot D-ter validé. Articulation explicite « 2 patterns distincts mais convergents » avec pattern-llm-wiki.

### `dep-02.md` (refactor S2.4 — v3.8.6 → v3.11.0)

**Modification structurelle** : ajout section H2 « Implication opérationnelle — architecture pour agent avec mémoire conversationnelle » entre LLM Wiki et RAG hybride. **Tableau §4 « Tableau de décision RAG » strictement intact** (rectification critique RETOUR-SONDAGE-S2.4 §3.4 — les 2 tableaux coexistent). Mini-tableau profils workload distinct.

### `cu-026.md` (patch S2.4 — v3.8.7 → v3.11.0)

**Modification structurelle** : ajout section H2 dédiée « 4 patterns Microsoft Frontier Firms — typologie de collaboration humain-agent IA (2026) » entre Framework 7 dimensions et Cadre réglementaire. Ordre canonique Author / Editor / Director / Orchestrator (progression croissante d'autonomie). **Distinction explicite « 4 patterns ≠ 7 dimensions »** préservée.

### `cu-027.md` (patch S2.4 — v3.8.7 → v3.11.0)

**Modification structurelle** : ajout « Point 4 — Benchmarks Stanford 2026 » dans section H2 « Rupture économique 2026 » (SWE-bench 60→100 %, productivité 14-26 %, emploi devs juniors -20 %). Wikilinks vers chiffres-macro-2026 v3.9.0 sections canonisées.

### `dep-08.md` (patch S2.4 — v3.8.7 → v3.11.0)

**Modification structurelle** : ajout section H2 dédiée « SBOM IA et supply chain — sécuriser la chaîne de dépendances agents (ANSSI / G7, 2026) » entre AgentShield specs opérationnelles et Sécuriser CLAUDE.md. Chiffre canonique 362 incidents IA Stanford intégré. 4 disciplines SBOM IA.

### `chiffres-macro-2026.md` (bump éditorial v3.8.6 → v3.9.0, S2.4.1 Lot B)

**Modification structurelle** : canonisation 20 nouveaux chiffres (1 enrichissement + 19 nouvelles sections H2) issus de I-D-006 (8 chiffres v3.10 Bpifrance/Microsoft/McKinsey) + I-D-007 (12 chiffres v3.11 Stanford/McKinsey). 27 → 46 sections H2. `derives` enrichi avec cu-014, pr-05, pr-08, dep-07, dep-08.

---

## Vague 5 — ajouts S2.5 Phase 2 (mai 2026, post-v3.10/v3.11 + signal v3.12 anticipé)

### `dep-01.md` (deploiement-dep) — nouveau

**Titre** : Cadrer un projet IA pour la mise en production
**Version** : 3.11.0
**Date d'ajout** : 2026-05-22
**Angles thématiques principaux** :
1. Heuristique anti-hype 2026 — single LLM call d'abord
2. Arbre de décision technique en 6 niveaux (Single LLM call → Long context → RAG → Fine-tuning → Single agent → Multi-agent)
3. Concept Jagged Frontier Stanford (IMO médaille d'or vs horloge analogique 50,1 % + OSWorld 12 → 66 %)
4. 4 stades projet : démo → POC → pilote → production

**Mots-clés sémantiques** : cadrage technique, arbre décision, heuristique anti-hype, Jagged Frontier, Single LLM call

**Recouvrements** :
- `pr-09.md` (vague 6) traitera le cadrage projet **stratégique** (distinct du cadrage technique). PAS de wikilink prématuré.
- Étapes 3-6 wikilinkent vers dep-02, dep-04, dep-05, cu-014, cu-026
- Pattern transverse pattern-llm-wiki + pattern-persistent-memory cités dès le niveau 2-3

### `dep-07.md` (deploiement-dep) — nouveau

**Titre** : Évaluation continue et qualité IA
**Version** : 3.11.0
**Date d'ajout** : 2026-05-22
**Angles thématiques principaux** :
1. Heuristique « eval first » Anthropic Engineering 2026
2. 3 types d'evals complémentaires (LLM-as-judge / offline référence / online utilisateurs)
3. Définitions canoniques Anthropic (eval / harness / multi-turn / state-modifying)
4. Méthode variance N runs pour agents long-running
5. Intégration CI/CD + gates de blocage

**Recouvrements** :
- Distinction nette évaluation (avant déploiement) vs observabilité (après) — wikilink vers `dep-05.md`
- Cycle Stitch → Evaluate → Iterate spécifique RAG dans `dep-02.md`, pas dupliqué
- §8.2 gates TOML cohérent avec `dep-05.md` §8.2 (wikilink, pas duplication)

### `dep-05.md` (deploiement-dep) — nouveau (le plus dense vague 5)

**Titre** : Agents en production : observabilité et garde-fous
**Version** : 3.11.0
**Date d'ajout** : 2026-05-22
**Angles thématiques principaux** :
1. Architecture observabilité 5 layers (logs / traces / métriques / événements / prompts-réponses)
2. 4 patterns industriels production 2026 (9-layer + gates TOML + Code Execution MCP + Agent Skills)
3. §8.5 Failure receipts et ownership (4 éléments anti-overclaimed completion)
4. §8.5bis Two-agent harness Anthropic (Initializer + Coding, mémoire externalisée)
5. KPI canoniques (containment rate / escalation accuracy / cost per interaction)

**Recouvrements** :
- Distinction explicitement préservée avec dep-07 (eval) + dep-08 (sécurité MCP) + cu-026 (gouvernance)
- Two-agent harness Anthropic distinct de Fat Skills / Thin Harness Garry Tan (cu-027) — pattern à ne pas confondre
- pattern-persistent-memory mémoire stateful vs mémoire externalisée artefacts versionnés (deux patterns complémentaires)

### `pr-01.md` (prealable-pr) — nouveau

**Titre** : Maturité organisationnelle face à l'IA
**Version** : 3.11.0
**Date d'ajout** : 2026-05-22
**Angles thématiques principaux** :
1. Typologie 4 profils dirigeants Bpifrance Le Lab (Sceptiques 27 % / Bloqués 26 % / Expérimentateurs 19 % / Innovateurs 28 %)
2. Encart McKinsey AI high performers (6 % + 3,6× transformation + 3× redesign + citation textuelle « intentional redesigning of workflows »)
3. Nuance d'échelle préservée (28 % Innovateurs ≠ 6 % high performers, échelles différentes)
4. Grille 4 paliers maturité (expérimentation isolée → stratégie cadrée → workflows redesignés → industrialisation)
5. Auto-évaluation 10 questions + 3 causes structurelles de blocage

**Recouvrements** :
- Frontière éditoriale claire avec pr-04 (PR-01 = posture dirigeant + organisation, PR-04 = marché + emploi)
- Wikilinks transverses vers chiffres-macro-2026

### `pr-04.md` (prealable-pr) — nouveau

**Titre** : Marché IA & emploi en 2026
**Version** : 3.11.0
**Date d'ajout** : 2026-05-22
**Angles thématiques principaux** :
1. §2bis 4 séries de chiffres convergents (Bpifrance + Microsoft + McKinsey + Stanford) — ordre canonique préservé
2. §2ter Maturité agentique (23 % scaling + 39 % expérimentation = 62 % engagés)
3. Paradoxe MIT NANDA 95 % sans ROI
4. Section 5 Transformation Paradox Microsoft 2026 (« le frein principal n'est ni la techno ni les collaborateurs, mais la culture »)
5. Prime salariale IA + asymétrie senior/junior + spécificité française

**Recouvrements** :
- Chiffres canoniques tous wikilinkés vers chiffres-macro-2026 (pas dupliqué)
- « -20 % emploi devs juniors US » reste local à cu-027 (cf. RETOUR-SONDAGE §7.3)
- Frontière éditoriale claire avec pr-01

### `pr-05.md` (prealable-pr) — nouveau

**Titre** : Sécurité IA — cadrage stratégique pour PME
**Version** : 3.11.0
**Date d'ajout** : 2026-05-22
**Angles thématiques principaux** :
1. Cybersécurité agentique distincte du LLM classique (McKinsey « Securing the agentic enterprise » mai 2026)
2. RAI maturité moyenne 2026 : 2,3/5 (vs 2,0 en 2025, ~1/3 à maturité ≥ 3, 2/3 à risque)
3. NIST CAISI 6 thèmes prioritaires + AI Agent Interoperability Profile Q4 2026
4. Encart 362 incidents Stanford symétrique avec dep-08 (formulation similaire, angles distincts)
5. Pas de cas-école PME nommé (module cartographique méthodologique)

**Recouvrements** :
- Pattern « 4 modules sécurité IA complémentaires » : PR-05 (stratégique) + DEP-05 (technique runtime) + DEP-08 (technique infrastructure) + CU-026 (gouvernance managériale)
- 362 incidents canonisé une seule fois dans chiffres-macro-2026, wikilinké depuis PR-05 + DEP-05 + DEP-08

### `cu-020.md` (module-cu) — nouveau

**Titre** : Conformité RGPD / AI Act pour l'IA en PME
**Version** : 3.11.0
**Date d'ajout** : 2026-05-22
**Angles thématiques principaux** :
1. 4 articles structurants (RGPD art. 22 + AI Act art. 4, 14, 50)
2. Typologie 4 niveaux de risque AI Act (interdit / haut risque / risque limité / risque minimal)
3. Sanctions chiffrées : 7 % CA mondial / 35 M€
4. Date pivot 2 août 2026 + Draft Guidelines Article 50 (3 juin / 2 août / 2 décembre 2026)
5. 3 fiches CNIL finales + guide HAS-CNIL santé mars 2026

**Recouvrements** :
- Wikilink vers cu-014 (transparence cascadée art. 50)
- Pas de wikilink artificiel vers pr-05 (non présent côté HTML — « couple 1 tranche, couple 2 s'aligne »)
- Article 14 + Moffatt v. Air Canada détaillés dans cu-026 (wikilinké, pas dupliqué)
- Pas de cas-école PME nommé (cohérent avec cu-024, pr-05, dep-08)

### `cu-024.md` (module-cu) — nouveau

**Titre** : Order-to-cash automation IA
**Version** : 3.11.0
**Date d'ajout** : 2026-05-22
**Angles thématiques principaux** :
1. Workflow O2C en 6 étapes canoniques (devis → bon de commande → facturation → relance → encaissement → lettrage)
2. Valeur IA différenciée par étape (forte : étapes 4 et 6 ; modérée : 1, 3 ; faible : 2, 5)
3. Chiffres canoniques : relance 30-40 % DSO en moins + 35-50 % productivité, lettrage 60-80 % automatique
4. Rectification critique acronymes : PA = Plateforme Agréée (LF 2026 art. 27) ≠ PPF = Portail Public de Facturation DGFiP
5. Calendrier réglementaire : 125 PA immatriculées au 5 mai 2026, 1er sept 2026 (réception obligatoire + émission grandes/ETI), 1er sept 2027 (PME/TPE)

**Recouvrements** :
- Module cartographique méthodologique (pas de cas-école PME nommé)
- Outils : Pennylane, Sellsy, Axonaut, Esker, Sidetrade, Aston AI (catégorie outils-compta-facturation-fr whitelistée)
- Wikilinks vers cu-008, pr-04, pr-07, pr-08, chiffres-macro-2026

### Patches Lot S2.5.0 + bis + ter (correctifs retrieval)

**3 modules patchés** côté leads (pas refactor structurel) :

- **`cu-001.md` v3.8.3 → v3.11.1** : lead « L'essentiel à retenir » enrichi vocabulaire question canonique q-002 (sources fiables actualité IA + veille IA générative + PME 2026)
- **`pr-07.md` v3.8.5 → v3.11.3** (3 patches successifs) : (1) Lot S2.5.0 — lead enrichi vocabulaire q-030 ; (2) Lot S2.5.0-bis — nouvelle H2 dédiée « Obligations réglementaires IA » concurrente aux chunks pr-08 ; (3) Lot S2.5.0-ter — densification chirurgicale lead H2 (titre verbatim « à anticiper », mode question + 4 ancrages, répétition contrôlée). Pattern empirique « 3 niveaux d'intervention retrieval » validé sur cette cible (q-030 rang #13 → #6 → #3 sim 0,3635).
- **`pr-08.md` v3.11.0 → v3.11.1** : lead restreint au scope strict financement (dispositifs fiscaux + Bpifrance + France 2030) — application AP-7 SPEC v1.8 inverse Lot D-ter.

---

## Récap inventaire post-S2.5 Phase 2

**Vault à 23 fichiers MD** :
- **6 modules CU** : cu-001, cu-008, **cu-020 (nouveau)**, **cu-024 (nouveau)**, cu-026, cu-027
- **5 préalables PR** : **pr-01 (nouveau)**, **pr-04 (nouveau)**, **pr-05 (nouveau)**, pr-07, pr-08
- **5 déploiement DEP** : **dep-01 (nouveau)**, dep-02, **dep-05 (nouveau)**, **dep-07 (nouveau)**, dep-08
- **5 transverses** : glossaire, chiffres-macro-2026, pattern-llm-wiki, pattern-persistent-memory, vigilance-hallucinations, vigilance-confidentialite
- **1 ressources** : outils-vector-db

**Reste pour vague 6 (S2.6 dédié)** : PR-09 + PR-10 + PR-11 (3 nouveaux préalables v3.12, sondage D-026 obligatoire sur PR-10 et PR-11).

---

## Historique des versions

| Version | Date | Modification |
|---|---|---|
| v0 | 11 mai 2026 | Initialisation, structure définie, premiers sujets à recouvrement identifiés |
| v1 | 19 mai 2026 | Section « Vague 4 — ajouts S2.4 Phase 2 » : pattern-persistent-memory, pr-08, refactor cu-008/dep-02, patches cu-026/cu-027/dep-08, bump chiffres-macro-2026 v3.9.0. Vault passe de 13 à 15 fichiers MD. |
| v3 | 22 mai 2026 | Section « Vague 5 — ajouts S2.5 Phase 2 » : 8 nouveaux modules (dep-01, dep-05, dep-07, pr-01, pr-04, pr-05, cu-020, cu-024) + 3 patches leads correctifs retrieval (cu-001 v3.11.1, pr-07 v3.11.3 avec 3 itérations Lot S2.5.0+bis+ter, pr-08 v3.11.1). Pattern « 3 niveaux d'intervention retrieval » validé empiriquement sur cible q-030 (rang #13 → #6 → #3). Vault passe de 15 à 23 fichiers MD. |
