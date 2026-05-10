# Enrichissement CU-008 — LLM Wiki Karpathy (alternative au RAG basique)

**Module cible** : `modules/cu-008-knowledge-base-rag.html`
**Type** : Patch éditorial (ajout de section)
**Volume** : ~400 mots à intégrer

---

## Position de l'enrichissement

Ajouter une **nouvelle section** entre la section actuelle « Architecture RAG » et « Choix vector DB ». Titre suggéré : **« Au-delà du RAG : l'approche LLM Wiki (Karpathy, 2026) »**.

## Contenu à intégrer

### 1. La rupture conceptuelle d'avril 2026

En avril 2026, Andrej Karpathy a publié sur GitHub un gist intitulé **« LLM Wiki »** qui a fait 17 millions de vues, 5 000 stars et 4 282 forks en quelques jours. Le gist propose une **alternative architecturale au RAG classique** pour les bases de connaissance de petite à moyenne taille.

L'idée fondamentale : **arrêter de retrieve, commencer à synthétiser**.

### 2. RAG classique vs LLM Wiki — la différence en deux phrases

- **RAG classique** : à chaque requête, on cherche dans le vector store → on récupère des chunks → on injecte dans le prompt → on génère une réponse → **on oublie tout**. Stateless. Pas de mémoire de synthèse.

- **LLM Wiki** : on maintient une **base markdown structurée** par un LLM. Quand on ajoute un document, le LLM met à jour les pages markdown affectées (synthèses, entités, contradictions). Quand un utilisateur pose une question, le LLM consulte directement les pages markdown pertinentes.

Le shift conceptuel : **synthesis persistante** au lieu de **retrieval éphémère**.

### 3. Quand le LLM Wiki bat le RAG vectoriel

Selon les benchmarks publiés et les retours communautaires (mai 2026) :

| Volume corpus | Stabilité | Recommandation |
|---|---|---|
| < 50K tokens | Stable (MAJ trimestrielle) | **LLM Wiki** (95 % moins cher en tokens vs RAG vectoriel) |
| 50K-100K tokens | Stable | **LLM Wiki** ou RAG dense léger (Chroma) |
| 100K-1M tokens | Mixte | **RAG hybride** (cf. [DEP-02](../deploiement/dep-02-rag-architecture-prod.html)) |
| > 1M tokens | Quelconque | **RAG hybride avec sharding** |
| Mises à jour temps réel | — | **RAG vectoriel** (LLM Wiki ne convient pas) |

### 4. Cas types où le LLM Wiki est pertinent en PME

- **Manuel produit stable** (documentation technique d'une machine, manuel d'intégration, procédure qualité)
- **FAQ métier** structurée (< 50K tokens)
- **Procédures internes RH** (règlement intérieur, parcours d'onboarding)
- **Documentation de projet** (cahier des charges, spécifications fonctionnelles)

### 5. Cas où ça ne convient PAS

- Volume > 200K tokens (le contexte LLM devient trop coûteux et lent)
- Mises à jour temps réel (réindexation continue impossible)
- Corpus très hétérogène (la maintenance markdown devient une charge)
- Besoin de réponses ultra-précises avec citations multiples (le RAG hybride reste meilleur)

### 6. Implication pour les PME qui démarrent un RAG

**Ne pas sauter directement sur Pinecone + embeddings + reranking** si ton corpus est petit et stable. Tester d'abord l'approche LLM Wiki — souvent suffisante, beaucoup moins coûteuse, beaucoup plus simple à maintenir.

## Sources à ajouter dans la section finale (Schéma A)

À insérer dans la sous-rubrique « 📰 Articles de fond » :
- [Karpathy LLM Wiki Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — Le pattern original (avril 2026)
- [MindStudio — LLM Wiki vs RAG comparison](https://www.mindstudio.ai/blog/llm-wiki-vs-rag-markdown-knowledge-base-comparison) — Analyse comparée
- [Suryansh Tiwari (X) — RAG doesn't learn](https://x.com/Suryanshti777) — Critique conceptuelle du RAG classique

## Renvois internes à ajouter

- Vers [DEP-02 RAG en production : choisir son architecture](../deploiement/dep-02-rag-architecture-prod.html) (panorama complet RAG hybride)
- Vers [CU-025 Knowledge management IA-augmenté](cu-025-knowledge-management-dirigeant.html) (application personnelle dirigeant)

## Note Cowork
Cet enrichissement positionne CU-008 comme **module d'introduction au RAG** + **pointeur vers les patterns avancés** (LLM Wiki, RAG hybride). Préserve la valeur du module existant tout en l'actualisant avec la veille 2026.
