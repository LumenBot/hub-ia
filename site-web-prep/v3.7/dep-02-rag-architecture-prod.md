# DEP-02 — RAG en production : choisir son architecture

**Public cible :** dirigeant qui pilote un projet RAG + son interface technique

---

## Métadonnées (pour Claude Code)

- **Section** : Déploiement
- **Niveau** : ⭐⭐⭐ Avancé
- **Type** : Cadrage stratégique
- **Durée lecture** : 22 min
- **Emoji h1** : 🔎
- **Titre métier visible** : « RAG en production : choisir son architecture »
- **Sous-titre hero** : Le RAG hybride a triplé en Q1 2026 (10,3 % → 33,3 %). Le débat n'est plus « RAG ou pas » mais « quelle architecture selon mon volume et mes données ». Voici comment décider.
- **Card index promesse** : « Cadrage stratégique »

## Synthèse exécutive

### Pourquoi cette page ?

Tu as compris que le RAG (Retrieval-Augmented Generation : un agent IA qui consulte ta documentation interne avant de répondre) est la brique centrale pour exploiter ton patrimoine documentaire. Mais tu hésites entre 5 architectures et autant de vector databases. Cette fiche te donne **la grille de décision selon le volume de ta base, la nature de tes données, et ton budget**.

L'enjeu n'est plus technique : il est stratégique. Le mauvais choix d'architecture coûte 10x plus cher en production que le bon. Et les patrons d'architecture évoluent vite : **le RAG hybride a triplé son intention d'adoption en Q1 2026** (10,3 % → 33,3 % en un trimestre, VentureBeat) parce que le RAG dense pur plafonne sur les corpus métier réels.

### 4 takeaways

1. **Trois architectures cohabitent en 2026 selon ton volume.** Pour < 100K tokens → LLM Wiki Karpathy (95 % moins coûteux). Pour 100K-10M tokens → RAG hybride (dense + sparse + reranking). Au-delà → RAG hybride avec sharding et caching avancé. Le mauvais choix coûte 10x plus.

2. **Le vector DB n'est PAS la décision principale.** Beaucoup de PME se trompent en passant 80 % du temps sur le choix Pinecone vs Qdrant. **Le bon embedding model et le reranking pèsent 5-10x plus** sur la qualité finale.

3. **Une pipeline de retrieval bien faite réduit les hallucinations de 70 à 90 %.** Les chiffres de Techment 2026 sont reproductibles. Mais cela exige une discipline : chunking adapté, retrieval hybride, reranking obligatoire, eval pipeline pour mesurer.

4. **Le LLM Wiki Karpathy (avril 2026) change la donne pour les petits corpus.** Pour une base < 100K tokens stable (manuel produit, FAQ technique, documentation interne d'un domaine), une simple base markdown maintenue par un LLM peut surpasser un RAG vectoriel — et coûter 95 % moins en tokens.

### Stats (3-4)

- **+322 %** d'adoption du retrieval hybride en Q1 2026 (VentureBeat)
- **70-90 %** de réduction des hallucinations avec une pipeline de retrieval bien faite (Techment 2026)
- **95 %** de tokens en moins avec le LLM Wiki Karpathy vs RAG vectoriel pur sur bases < 100K tokens
- **+1 à 9 %** de recall amélioré avec retrieval hybride vs vectoriel pur (TiDB benchmarks)

### Quand cette page est utile

Tu envisages de déployer un RAG en production sur **ton patrimoine documentaire interne** (manuels, procédures, retours terrain, base de connaissance métier). Tu veux choisir entre LLM Wiki / RAG dense / RAG hybride. Tu cherches un référentiel pour benchmarker les vector DB sans te perdre dans les détails techniques. Tu as un budget mensuel à arbitrer.

## Section 1 — RAG en 2026 : pourquoi le débat a évolué

### 1.1 Ce qui a changé en 2025-2026

Trois ruptures structurent le marché aujourd'hui :

1. **Le RAG dense pur plafonne sur les corpus métier réels.** Quand le corpus contient des acronymes, des codes produits, des références techniques (numéros ATC, codes SKU, références ISO), l'embedding sémantique ne suffit plus. D'où la bascule massive vers le **retrieval hybride** (dense + sparse BM25 + reranking).

2. **Le LLM Wiki d'Andrej Karpathy** (gist GitHub avril 2026, 17 M de vues, 5 000 stars en quelques jours) propose une alternative radicale pour les petits corpus : pas de vector DB, pas de chunking, juste une base markdown maintenue par un LLM. **95 % moins coûteux en tokens** que le RAG vectoriel pour les bases < 100K tokens stables.

3. **Les vector DB se sont commoditisés.** Pinecone, Qdrant, Weaviate, Chroma, MongoDB Atlas Vector Search : 5+ acteurs solides, prix qui baissent, performances équivalentes sur la majorité des cas. Le débat n'est plus « lequel choisir » mais « comment l'utiliser correctement ».

### 1.2 La règle de décision en 30 secondes

Trois questions pour choisir l'architecture :

- **Volume du corpus** : < 100K tokens ? 100K-10M ? > 10M ?
- **Fréquence de mise à jour** : statique ? hebdomadaire ? continue ?
- **Nature des données** : texte narratif ? techniques avec acronymes/codes ? mixte ?

Le tableau de décision en section 4 te donne la réponse.

## Section 2 — Le LLM Wiki Karpathy — alternative crédible pour les petits corpus

### 2.1 Le pattern en deux phrases

Au lieu d'embedder ton corpus dans un vector DB et de retrieve des chunks à chaque requête, tu maintiens **une base markdown structurée par un LLM**. Quand tu ajoutes un document, le LLM met à jour les pages markdown affectées (synthèses, entités, contradictions). Quand un utilisateur pose une question, le LLM consulte directement les pages markdown pertinentes.

### 2.2 Quand c'est pertinent (les cas types)

- **Manuel produit stable** (ex : documentation technique d'une machine industrielle) : 30K-80K tokens, mises à jour trimestrielles
- **FAQ métier** : questions/réponses standardisées, < 50K tokens
- **Procédures internes RH** : règlement intérieur, processus de recrutement, etc.
- **Documentation projet** : un cahier des charges, un manuel d'intégration

### 2.3 Quand ce n'est PAS pertinent

- **Volume > 200K tokens** : le contexte LLM devient trop coûteux et lent
- **Mises à jour temps réel** : pas adapté
- **Corpus très hétérogène** : la maintenance markdown devient une charge

### 2.4 Coût-bénéfice mesuré

Pour une PME avec un corpus de 50K tokens :
- **RAG vectoriel** : ~150-300 €/mois (vector DB managed + embeddings + LLM)
- **LLM Wiki** : ~10-50 €/mois (juste le LLM, pas de vector DB)

→ Économie potentielle de 90 % sur les petits corpus.

## Section 3 — Le RAG hybride — le standard 2026 pour les corpus moyens et grands

### 3.1 Anatomie d'une pipeline RAG hybride

Sept étapes à connaître (ton prestataire doit te les réciter sans hésiter) :

1. **Chunking** : découpage du corpus en passages de 256-1024 tokens avec overlap de 100 tokens
2. **Embedding** : conversion de chaque chunk en vecteur (OpenAI text-embedding-3-small, Mistral embed, Cohere embed)
3. **Indexation** : stockage des vecteurs + métadonnées dans le vector DB
4. **Query rewriting** : reformulation de la requête utilisateur pour optimiser la recherche
5. **Retrieval hybride** : recherche dense (vector similarity) **+** recherche sparse (BM25) en parallèle
6. **Reranking** : un cross-encoder (Cohere Rerank, BGE-reranker) re-classe les top-K résultats par pertinence réelle
7. **Generation** : le LLM consulte les chunks pertinents et génère la réponse avec citations

### 3.2 Les choix techniques qui pèsent vraiment sur la qualité

Par ordre d'impact sur la qualité finale :

1. **Embedding model** : 30-40 % d'impact sur la pertinence
2. **Reranking** : +10-30 % de précision (sauter cette étape sacrifie 30 % de précision)
3. **Chunking** : sweet spot Q&A factuel = 256-512 tokens, tâches analytiques = 512-1024 tokens
4. **Choix vector DB** : 5-10 % d'impact (souvent surestimé en PME)

### 3.3 Eval pipeline obligatoire

**Sans eval pipeline, tu ne sais pas si une modif améliore ou dégrade.** Une eval pipeline = un dataset golden de 50-200 questions/réponses avec scoring automatique (BLEU, ROUGE, semantic similarity, jugement LLM). Mise en place : 1-2 semaines, mais c'est ce qui sépare le RAG amateur du RAG production.

## Section 4 — Tableau de décision RAG (à utiliser avec ton prestataire)

| Volume corpus | Nature données | Fréquence MAJ | Architecture recommandée | Coût mensuel typique |
|---|---|---|---|---|
| < 50K tokens | Texte narratif stable | Trimestrielle | **LLM Wiki Karpathy** | 10-50 € |
| 50K-100K tokens | Mixte | Mensuelle | **LLM Wiki** ou **RAG dense Chroma** | 50-150 € |
| 100K-1M tokens | Texte avec acronymes/codes | Hebdomadaire | **RAG hybride Qdrant** | 150-500 € |
| 1M-10M tokens | Mixte | Quotidienne | **RAG hybride Pinecone/Qdrant + cache** | 500-2000 € |
| > 10M tokens | Hétérogène | Continue | **RAG hybride sharded + LLM Wiki layer** | 2000-10K € |

**Important** : ce tableau est indicatif. Le vrai choix dépend aussi de ta latence cible, de ton SLA, et de ta contrainte de souveraineté (cf. [page Architectures](../architectures.html)).

## Section 5 — Choix vector DB : panorama 2026

### 5.1 Les 5 acteurs solides

| Vector DB | Profil | Quand le choisir |
|---|---|---|
| **Pinecone** | Managed serverless, premium | Enterprise sans équipe ops, pricing OK |
| **Qdrant** | Open-source, self-host possible, performant | Contrôle des coûts, souveraineté EU |
| **Weaviate** | Hybrid search natif, multi-tenant | Multi-clients, hybrid en standard |
| **Chroma** | Simple, local, gratuit | Prototypage, petits volumes |
| **MongoDB Atlas Vector Search** | Si déjà sur Mongo | Pas de nouvelle brique infra |

### 5.2 La question piège : « Quel vector DB choisir ? »

**Mauvaise question.** La bonne question est : « Quel embedding model + quelle pipeline de reranking ? ». Le vector DB n'est qu'un moteur de stockage. La qualité vient de l'embedding et du reranking.

Si tu n'as pas encore d'avis : **Qdrant self-hosted** pour démarrer (gratuit, contrôle, EU). Migration vers Pinecone managed si tu atteins les limites ops.

## Section 6 — Les 5 écueils typiques RAG en production

À éviter à tout prix.

1. **Mauvais chunking = mauvais résultats**, indépendamment du modèle. Sweet spot : 256-512 tokens Q&A, 512-1024 tokens analytique. Trop petit → perte de contexte. Trop grand → bruit dans le retrieval.
2. **Croire que le choix vector DB est central** : c'est l'embedding model qui pèse le plus sur la qualité.
3. **Oublier le reranking** : -30 % de précision en moyenne.
4. **RAG dense pur sur corpus métier avec acronymes/codes** : rate les références. Hybride obligatoire.
5. **Construire un RAG sans eval pipeline** : impossible de mesurer si une modif améliore ou dégrade.

## Section 7 — Plan d'action 60 jours pour un RAG production-ready

### Jours 1-15 — Cadrage
- Inventaire du corpus (volume, nature, fréquence MAJ)
- Décision architecture via tableau section 4
- Définition KPI (précision sur dataset golden, latence cible, coût/requête max)

### Jours 16-30 — Pilote
- Mise en œuvre de la pipeline (chunking + embedding + retrieval + reranking + generation)
- Construction du dataset golden (50-100 questions/réponses)
- Mesure des KPI sur le golden

### Jours 31-45 — Optimisation
- Itération sur chunking, embedding, reranking
- Mesure systématique sur le golden après chaque modification

### Jours 46-60 — Mise en production
- Déploiement sur 5-15 utilisateurs cibles
- Monitoring (latence, coût, satisfaction utilisateur)
- Décision Go/No-Go production large

## Section 8 — Pour aller plus loin (Schéma A)

### Callout d'aiguillage

> Pour le panorama complet des outils RAG, retrouve les fiches détaillées sur la [page Ressources du Hub](../ressources.html#bibliographie).

### 📰 Articles de fond
- [VentureBeat — Hybrid retrieval intent tripled (mars 2026)](https://venturebeat.com/data/the-retrieval-rebuild-why-hybrid-retrieval-intent-tripled-as-enterprise-rag-programs-hit-the-scale-wall) — La bascule Q1 2026 vers le retrieval hybride
- [MindStudio — LLM Wiki vs RAG comparison](https://www.mindstudio.ai/blog/llm-wiki-vs-rag-markdown-knowledge-base-comparison) — Analyse comparée patterns 2026
- [Techment — RAG in 2026](https://www.techment.com/blogs/rag-in-2026/) — État de l'art RAG production

### 🎓 Tutoriels & cas pratiques
- [Avi Chawla — Foundations of AI Engineering](https://blog.dailydoseofds.com/p/foundations-of-ai-engineering-and-0a6) — Série 8 piliers, RAG en pilier 2
- [LangChain RAG from scratch](https://github.com/langchain-ai/rag-from-scratch) — Vidéos pédagogiques fondamentales
- [Karpathy LLM Wiki Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — Le pattern original avril 2026

### 📚 Documentation officielle & études
- [arXiv 2511.17593 — Survey on enterprise RAG](https://arxiv.org/abs/2511.17593) — Synthèse académique architectures RAG 2026
- [Anthropic Engineering — Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — Référence sur l'organisation du contexte
- [NIST AI RMF (sect. RAG)](https://www.nist.gov/itl/ai-risk-management-framework) — Gouvernance gratuit

### 👥 Communautés & veille
- [Pinecone Community](https://community.pinecone.io/) — Communauté technique active
- [Qdrant Discord](https://qdrant.tech/community/) — Open-source EU

## Renvois internes pour Claude Code

- **Section 4** : lien `<a href="../architectures.html">page Architectures</a>` pour les contraintes de souveraineté
- **Section 8 (callout)** : lien `<a href="../ressources.html#bibliographie">page Ressources</a>`
- **Section corps** : si une fiche outil existe pour Pinecone/Qdrant/Weaviate dans ressources.html → lien `<a href="../ressources.html#pinecone">Pinecone</a>` etc. (à vérifier ancres existantes)

## Composants visuels suggérés

- **Section 3.1** : schéma SVG en 7 étapes de la pipeline RAG hybride (similaire à ceux déjà présents dans CU-008)
- **Section 4** : tableau de décision en composant `.tool-table` (déjà centralisé dans `module-v3.css`)
- **Section 5.1** : tableau panorama vector DB en `.tool-table`
- **Section 7** : timeline visuelle 60 jours en `.timeline-block`

## Note Cowork
Sources prioritaires : VentureBeat, Karpathy, Techment, Avi Chawla, NIST. Aucune mention d'éditeur SaaS spécifique en promotion. Référence [CU-008 Knowledge base RAG](../modules/cu-008-knowledge-base-rag.html) à enrichir en Batch B avec section LLM Wiki.
