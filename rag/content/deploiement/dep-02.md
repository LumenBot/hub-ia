---
code: dep-02
titre: "RAG en production : choisir son architecture"
type: deploiement-dep
axe: B
niveau: 3
tags: [rag, production, architecture, llm-wiki, hybride, embeddings, reranking, eval-set, chunking]
version: 3.8.4
last_updated: 2026-05-12
glosaire_termes: [rag, vector-store, embeddings, chunk, llm, llm-wiki, hnsw, reranker, retrieval-hybride, eval-set, llm-as-judge, mteb]
derives: ["[[cu-008]]", "[[pr-07]]", "[[dep-01]]", "[[dep-03]]", "[[dep-04]]", "[[dep-06]]", "[[dep-07]]", "[[outils-vector-db]]", "[[vigilance-hallucinations]]", "[[vigilance-confidentialite]]"]
public_cible: [ops, r&d, tech]
---

# RAG en production : choisir son architecture

## L'essentiel à retenir

**Trois architectures cohabitent en 2026 selon le volume de corpus.** Pour < 100K tokens → [[glossaire#llm-wiki]] Karpathy (95 % moins coûteux). Pour 100K-10M tokens → [[glossaire#retrieval-hybride]] (dense + sparse + [[glossaire#reranker|reranking]]). Au-delà → RAG hybride avec sharding et caching avancé. **Le mauvais choix coûte 10× plus.**

**Le [[glossaire#vector-store]] n'est PAS la décision principale.** Beaucoup de PME se trompent en passant 80 % du temps sur le choix Pinecone vs Qdrant. Le bon modèle d'[[glossaire#embeddings]] et le reranking pèsent 5 à 10 fois plus sur la qualité finale.

**Une pipeline de retrieval bien faite réduit les [[vigilance-hallucinations|hallucinations]] de 70 à 90 %** (Source : Techment 2026, reproductible). Mais cela exige une discipline : chunking adapté, retrieval hybride, reranking obligatoire, eval pipeline pour mesurer.

**Le LLM Wiki Karpathy (avril 2026) change la donne pour les petits corpus.** Pour une base < 100K tokens stable (manuel produit, FAQ technique, documentation interne d'un domaine), une simple base markdown maintenue par un LLM peut surpasser un RAG vectoriel — et coûter 95 % moins en tokens.

**Stats clés** :
- +322 % d'adoption du retrieval hybride au Q1 2026 (Source : VentureBeat)
- 70-90 % de réduction des hallucinations avec pipeline propre (Source : Techment)
- 95 % de tokens en moins avec LLM Wiki sur petits corpus
- +1 à 9 % de recall hybride vs vectoriel pur (Source : TiDB)

## À qui cette page est utile

Tu envisages de déployer un [[glossaire#rag]] en production sur ton patrimoine documentaire interne. Tu veux choisir entre LLM Wiki, RAG dense, RAG hybride. Tu cherches un référentiel pour benchmarker les vector DB sans te perdre dans les détails techniques. Tu as un budget mensuel à arbitrer pour ta pipeline RAG.

Niveau ⭐⭐⭐ Avancé. Public cible : DSI, lead tech, prestataire IA-natif, responsable produit IA en PME / ETI.

**Pré-requis pédagogiques** : maîtrise du concept de RAG (cf. [[cu-008]]) et arbitrage Build vs Buy posé (cf. [[pr-07]]).

## Ce qui a changé en 2025-2026 — trois ruptures structurantes

**Rupture 1 — Le RAG dense pur plafonne sur les corpus métier réels.** Quand le corpus contient des acronymes, des codes produits, des références techniques (numéros ATC, codes SKU, références ISO), l'[[glossaire#embeddings|embedding sémantique]] ne suffit plus. D'où la bascule massive vers le [[glossaire#retrieval-hybride]] (dense + sparse BM25 + reranking).

**Rupture 2 — Le [[glossaire#llm-wiki]] d'Andrej Karpathy** (gist GitHub avril 2026, 17 M de vues, 5 000 stars en quelques jours) propose une alternative radicale pour les petits corpus : pas de vector DB, pas de chunking, juste une base markdown maintenue par un LLM. 95 % moins coûteux en tokens que le RAG vectoriel pour les bases < 100K tokens stables.

**Rupture 3 — Les [[glossaire#vector-store|vector DB]] se sont commoditisés.** Pinecone, Qdrant, Weaviate, Chroma, MongoDB Atlas Vector Search — 5 acteurs solides, prix qui baissent, performances équivalentes sur la majorité des cas. Le débat n'est plus « lequel choisir » mais « comment l'utiliser correctement ». Détail des outils dans [[outils-vector-db]].

**Règle de décision en 30 secondes** : trois questions à se poser.
1. Volume du corpus : < 100K tokens ? 100K-10M ? > 10M ?
2. Fréquence de mise à jour : statique ? hebdomadaire ? continue ?
3. Nature des données : texte narratif ? techniques avec acronymes/codes ? mixte ?

Le tableau de décision plus bas donne la réponse architecturale.

## LLM Wiki Karpathy — alternative crédible pour les petits corpus

**Le pattern en deux phrases.** Au lieu d'embedder ton corpus dans un vector DB et de retrieve des [[glossaire#chunk]]s à chaque requête, tu maintiens une base markdown structurée par un LLM. Quand tu ajoutes un document, le LLM met à jour les pages markdown affectées (synthèses, entités, contradictions). Quand un utilisateur pose une question, le LLM consulte directement les pages markdown pertinentes.

**Quand c'est pertinent** : manuel produit stable (documentation technique d'une machine industrielle) de 30K-80K tokens avec mises à jour trimestrielles ; FAQ métier (questions/réponses standardisées, < 50K tokens) ; procédures internes RH (règlement intérieur, processus de recrutement) ; documentation projet (cahier des charges, manuel d'intégration).

**Quand ce n'est PAS pertinent** : volume > 200K tokens (le contexte LLM devient trop coûteux et lent) ; mises à jour temps réel (pas adapté) ; corpus très hétérogène (la maintenance markdown devient une charge).

**Coût-bénéfice mesuré** pour une PME avec corpus de 50K tokens :
- RAG vectoriel : ~150-300 €/mois (vector DB managé + embeddings + LLM)
- LLM Wiki : ~10-50 €/mois (juste le LLM, pas de vector DB)
- → Économie potentielle de 90 % sur les petits corpus.

## RAG hybride — anatomie d'une pipeline production

Sept étapes à connaître (ton prestataire doit te les réciter sans hésiter) :

1. **Chunking** : découpage du corpus en passages de 256-1024 tokens avec overlap de 100 tokens
2. **Embedding** : conversion de chaque chunk en vecteur (OpenAI text-embedding-3-small, Mistral Embed, Cohere Embed)
3. **Indexation** : stockage des vecteurs + métadonnées dans le [[glossaire#vector-store]]
4. **Query rewriting** : reformulation de la requête utilisateur pour optimiser la recherche
5. **[[glossaire#retrieval-hybride|Retrieval hybride]]** : recherche dense (vector similarity) + recherche sparse (BM25) en parallèle
6. **[[glossaire#reranker|Reranking]]** : un cross-encoder (Cohere Rerank, BGE-reranker) re-classe les top-K résultats par pertinence réelle
7. **Generation** : le LLM consulte les chunks pertinents et génère la réponse avec citations

C'est l'architecture standard 2026 pour les corpus moyens et grands.

## Les choix techniques qui pèsent vraiment + eval pipeline obligatoire

**Par ordre d'impact sur la qualité finale** :
- **Modèle d'embedding** : 30-40 % d'impact sur la pertinence
- **Reranking** : +10-30 % de précision (sauter cette étape sacrifie 30 % de précision)
- **Chunking** : sweet spot Q&A factuel = 256-512 tokens, tâches analytiques = 512-1024 tokens
- **Choix vector DB** : 5-10 % d'impact (souvent surestimé en PME)

**Eval pipeline obligatoire.** Sans eval pipeline, tu ne sais pas si une modification améliore ou dégrade ton système. Une eval pipeline = un [[glossaire#eval-set|golden set]] de 50-200 questions/réponses avec scoring automatique. Mise en place : 1-2 semaines, mais c'est ce qui sépare le RAG amateur du RAG production. Détail méthodologique dans [[dep-07]] (Évaluation continue et qualité IA).

## Tableau de décision RAG (à utiliser avec ton prestataire)

| Volume corpus | Nature données | Fréquence MAJ | Architecture recommandée | Coût mensuel typique |
|---|---|---|---|---|
| < 50K tokens | Texte narratif stable | Trimestrielle | LLM Wiki Karpathy | 10-50 € |
| 50K-100K tokens | Mixte | Mensuelle | LLM Wiki ou RAG dense Chroma | 50-150 € |
| 100K-1M tokens | Texte avec acronymes/codes | Hebdomadaire | RAG hybride Qdrant | 150-500 € |
| 1M-10M tokens | Mixte | Quotidienne | RAG hybride Pinecone/Qdrant + cache | 500-2 000 € |
| > 10M tokens | Hétérogène | Continue | RAG hybride sharded + LLM Wiki layer | 2 000-10 000 € |

Ce tableau est indicatif. Le vrai choix dépend aussi de la latence cible, du SLA visé, et de la contrainte de [[glossaire#souverainete]] (voir page Architectures du Hub).

## Choix vector DB — panorama 2026 et question piège

**Les 5 acteurs solides** :

| Vector DB | Profil | Quand le choisir |
|---|---|---|
| Pinecone | Managed serverless, premium | Enterprise sans équipe ops, pricing OK |
| Qdrant | Open-source, self-host possible, performant | Contrôle des coûts, souveraineté EU |
| Weaviate | Hybrid search natif, multi-tenant | Multi-clients, hybrid en standard |
| Chroma | Simple, local, gratuit | Prototypage, petits volumes |
| MongoDB Atlas Vector Search | Si déjà sur Mongo | Pas de nouvelle brique infra |

Détail complet des 4 premiers dans [[outils-vector-db]].

**La question piège : « Quel vector DB choisir ? »**. Mauvaise question. La bonne question est : « Quel modèle d'embedding + quelle pipeline de reranking ? ». Le vector DB n'est qu'un moteur de stockage. La qualité vient de l'embedding et du reranking.

**Réflexe par défaut si pas encore d'avis** : Qdrant self-hosted pour démarrer (gratuit, contrôle, EU). Migration vers Pinecone managé si atteinte des limites ops.

## Les 5 écueils typiques RAG en production

**Écueil 1 — Mauvais chunking = mauvais résultats**, indépendamment du modèle. Sweet spot : 256-512 tokens Q&A, 512-1024 tokens analytique. Trop petit → perte de contexte. Trop grand → bruit dans le retrieval.

**Écueil 2 — Croire que le choix vector DB est central**. C'est le modèle d'embedding qui pèse le plus sur la qualité finale (30-40 %). Investir le temps de réflexion en proportion de l'impact réel.

**Écueil 3 — Oublier le reranking**. -30 % de précision en moyenne. C'est un composant non négociable d'une pipeline RAG production.

**Écueil 4 — RAG dense pur sur corpus métier avec acronymes/codes**. Rate les références techniques précises. Le retrieval hybride (dense + sparse BM25) est obligatoire pour ces corpus.

**Écueil 5 — Construire un RAG sans eval pipeline**. Impossible de mesurer si une modification améliore ou dégrade le système. Tout choix devient subjectif et instable.

**Écueil 6 (transverse) — Ignorer la confidentialité du corpus indexé**. Un RAG mal configuré peut exposer un visiteur à du contenu qu'il ne devrait pas voir (RH, négociations, comptes). Le filtrage des droits doit être implémenté en amont de l'indexation, pas au moment de la génération. Cadrage complet dans [[vigilance-confidentialite|brique transverse confidentialité]] et architecture détaillée dans [[cu-008]] (piège 2).

## Cycle d'itération Stitch → Evaluate → Iterate

**Constat largement documenté en 2026** : rien sur les leaderboards ne prédit la performance d'un RAG sur tes données spécifiques. Les benchmarks publics ([[glossaire#mteb]], BEIR, etc.) testent sur des datasets génériques. Sur ton corpus métier, l'écart entre la performance benchmark et la performance réelle peut être significatif.

**Implication pratique** : tu ne peux pas choisir ton stack RAG sur la base des leaderboards. Tu dois itérer sur tes données réelles.

**Le cycle Stitch → Evaluate → Iterate** :
1. **Stitch** : assembler une première version du pipeline (chunking + embeddings + retrieval + reranking + génération) avec des choix par défaut raisonnables. Ne pas chercher l'optimum dès le départ.
2. **Evaluate** : évaluer la performance sur un [[glossaire#eval-set|eval set]] réel (50-200 cas représentatifs de tes données et requêtes), avec un [[glossaire#llm-as-judge|LLM-as-judge]] aligné sur le feedback humain (calibrer le LLM-as-judge sur 10-20 cas annotés humain).
3. **Iterate** : modifier un seul composant à la fois (changer d'embedding, ajuster le chunking, ajouter un reranker, etc.), réévaluer, comparer.

**RetEx documenté — embeddings open-source qui battent OpenAI** (cas mai 2026, dataset d'enchères) : un embedding open-source classé #130 sur le leaderboard [[glossaire#mteb]] a battu les embeddings d'OpenAI (#1 du leaderboard) :
- +11 % de qualité (mesurée sur l'eval set spécifique au dataset)
- 240× plus rapide (latence par requête)
- Gratuit (vs coût API OpenAI)

**Leçon** : les leaderboards ne prédisent pas la performance sur tes données. L'eval set sur ton corpus est le seul juge fiable.

**Implication pour la PME** : construire son eval set est l'investissement le plus rentable d'un projet RAG en production. Coût : 1-3 jours de travail manuel pour annoter 50-200 cas. ROI : permanent (tout choix futur s'évalue dessus). Itérer cheapest-first : changer le chunking ou ajouter un reranker coûte moins cher que changer le modèle de génération.

## Plan d'action 60 jours pour un RAG production-ready

**Jours 1-15 — Cadrage**
- Inventaire du corpus (volume, nature, fréquence MAJ)
- Décision architecture via tableau de décision plus haut
- Définition KPI (précision sur dataset golden, latence cible, coût/requête max)

**Jours 16-30 — Pilote**
- Mise en œuvre de la pipeline (chunking + embedding + retrieval + reranking + generation)
- Construction du [[glossaire#eval-set|dataset golden]] (50-100 questions/réponses)
- Mesure des KPI sur le pilote
- Premier go/no-go

**Jours 31-45 — Itération**
- Optimisation cheapest-first (chunking, reranker avant modèle de génération)
- A/B testing entre composants alternatifs (modèles d'embedding, stratégies de chunking)
- Calibration du [[glossaire#llm-as-judge|LLM-as-judge]] sur 10-20 cas annotés humain

**Jours 46-60 — Mise en production**
- Monitoring continu (latence, coût, taux d'erreur)
- Capture de feedback utilisateur (👍/👎, signalements)
- Premier rapport qualité avec scoring eval set automatisé

## Pour aller plus loin

- Module fonctionnel orienté décideur : [[cu-008]] (Knowledge base RAG)
- Cadrage du projet IA pour la mise en production : [[dep-01]] (Cadrer un projet IA pour la mise en production)
- Context engineering et coût par requête : [[dep-03]] (Context engineering et coût par requête)
- Fine-tuning : quand y aller : [[dep-04]] (Fine-tuning : quand y aller, quand ne pas)
- Inférence et coûts SaaS vs self-hosted : [[dep-06]] (Inférence et coûts : SaaS vs self-hosted)
- Évaluation continue et golden set détaillé : [[dep-07]] (Évaluation continue et qualité IA)
- Outils vector DB : [[outils-vector-db]] (panorama 4 acteurs)
- Discipline anti-hallucinations : [[vigilance-hallucinations]]

**Sources externes** :
- Karpathy A., LLM Wiki — gist GitHub avril 2026
- Techment 2026, hallucinations reduction with retrieval discipline
- VentureBeat Q1 2026, adoption metrics hybrid retrieval
- TiDB benchmarks recall hybride vs vectoriel pur
- MTEB leaderboard (huggingface.co/spaces/mteb/leaderboard)
