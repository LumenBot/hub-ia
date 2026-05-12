---
code: glossaire
titre: "Glossaire canonique du Hub IA"
type: transverse
axe: transverse
niveau: 1
tags: [glossaire, definitions, vocabulaire]
version: 3.8.4
last_updated: 2026-05-12
glosaire_termes: []
derives: []
public_cible: [dirigeant, ops, r&d, tech, transverse]
---

# Glossaire canonique du Hub IA

> Ce fichier est la **source unique de vérité** pour les définitions de termes techniques utilisés dans le Hub IA. Tous les fichiers MD du vault y font référence via wikilink `[[glossaire#terme]]`. Les définitions sont alignées sur les gloses obligatoires de RULES-IMPLEMENTATION du couple 1 (RULES v1.6 §1.3 / v1.5.14 §1.3.2).

## RAG

Retrieval-Augmented Generation : un agent IA qui consulte ta documentation interne avant de répondre, plutôt que de répondre seulement à partir de ce qu'il a appris à l'entraînement. Concrètement, l'IA recherche les passages pertinents dans une base documentaire (vector store), puis les utilise comme contexte pour générer sa réponse, avec citation des sources. Le pattern qui résout structurellement le « temps perdu à chercher l'info » dans toute organisation de plus de 5-10 personnes.

## Vector store

Aussi appelé « vector database » ou « base vectorielle ». Brique centrale de tout système [[glossaire#rag]] : base de données spécialisée dans le stockage et la recherche de représentations numériques de texte ([[glossaire#embeddings]]). Permet de retrouver les passages sémantiquement proches d'une requête. Exemples : Qdrant, Pinecone, ChromaDB, pgvector.

## Embeddings

Représentation numérique d'un texte (un vecteur de quelques centaines à quelques milliers de nombres) qui capture son sens. Deux textes proches sémantiquement ont des embeddings proches géométriquement. Permet à l'IA de comparer, classer et retrouver du contenu par sens et non par mots-clés. Produits par un modèle d'embedding (OpenAI text-embedding-3, Mistral Embed, sentence-transformers, etc.).

## LLM

Large Language Model : modèle d'IA générative type ChatGPT, Claude, Gemini, Mistral, Llama. Capable de comprendre et produire du texte en langage naturel sur la base de milliards de paramètres entraînés sur d'énormes corpus.

## POC

Proof of Concept : prototype rapide destiné à valider une faisabilité technique ou un usage avant de décider d'industrialiser. Quelques jours à quelques semaines d'effort. À ne pas confondre avec [[glossaire#mvp]] (vise un usage par un vrai utilisateur).

## MVP

Minimum Viable Product : version la plus simple d'un produit qu'on peut déjà mettre dans les mains d'un client réel pour valider l'intérêt et apprendre. Plus engageant qu'un [[glossaire#poc]] : il doit fonctionner en conditions réelles, même de manière minimale.

## API

Interface de programmation qui permet à un logiciel d'en appeler un autre. Les LLM modernes (Claude, GPT, Mistral) sont accessibles par API pour intégration dans des applications custom — c'est ce qui permet de construire un agent ou un [[glossaire#rag]] sur leur capacité de génération.

## SaaS

Software as a Service : logiciel hébergé chez l'éditeur, accessible par navigateur, généralement facturé à l'usage ou par abonnement. Pas d'installation ni de maintenance côté utilisateur, mais dépendance à l'hébergeur.

## Open-source

Logiciel dont le code source est public et modifiable. Permet le self-hosting, l'audit de sécurité, l'absence de lock-in vendor. Compromis : nécessite des compétences techniques pour opérer en production.

## Self-hosting

Hébergement d'un logiciel sur ses propres serveurs ou son propre cloud, plutôt que de consommer une version managée chez un éditeur. Avantages : souveraineté, contrôle, parfois moins cher à grande échelle. Inconvénients : compétences d'opération requises, responsabilité de l'uptime et de la sécurité.

## On-premise

Hébergement sur tes propres serveurs, dans ton infrastructure (par opposition au [[glossaire#saas]] hébergé chez l'éditeur). Variante de [[glossaire#self-hosting]] plus stricte : tu opères même la couche matérielle, sans intermédiaire cloud. Pertinent quand les contraintes réglementaires ou de souveraineté excluent tout cloud public, même européen.

## Souveraineté

Capacité à garder le contrôle de ses données et de leur localisation. En contexte IA, deux dimensions principales : (1) hébergement géographique (EU vs US/autres) pour conformité RGPD, (2) absence de dépendance à un acteur unique pour l'opération critique. Voir [[glossaire#cloud-souverain]].

## Cloud souverain

Hébergement cloud opéré sous juridiction européenne, certifié SecNumCloud le cas échéant. Permet de stocker et traiter des données sensibles avec garanties juridiques fortes (pas de Cloud Act US applicable). Acteurs : OVH, Scaleway, 3DS Outscale, Cloud Temple.

## Hallucination

Affirmation fausse présentée avec assurance par un [[glossaire#llm]]. Particulièrement fréquente sur les chiffres précis, les dates, les sources citées qui n'existent pas. Risque structurel à mitiger en RAG par : (1) ancrage dans des sources sourcées, (2) citation systématique avec lien vérifiable, (3) refus du modèle quand aucune source ne couvre la question.

## HNSW

Hierarchical Navigable Small World : algorithme d'indexation des vecteurs qui permet une recherche de similarité rapide même sur de très grands volumes. C'est le standard de fait des [[glossaire#vector-store]] modernes (Qdrant, Pinecone, pgvector le supporte). À privilégier sur ivfflat pour la plupart des cas d'usage RAG.

## Chunk

Segment de texte de taille contrôlée (typiquement 400-700 [[glossaire#token]]s, soit ~250-500 mots, conformément à la convention SPEC-MD-POUR-RAG §R3) extrait d'un document plus long et stocké dans le [[glossaire#vector-store]]. L'unité d'indexation et de retrieval du [[glossaire#rag]]. La qualité du chunking (où coupe-t-on ?) influe énormément sur la qualité des réponses finales.

## Fine-tuning

Ajustement d'un [[glossaire#llm]] sur tes propres données pour spécialiser son comportement. À distinguer du [[glossaire#rag]] qui ajoute du contexte au moment de la requête. Long et coûteux (compute + données + expertise) ; généralement à privilégier seulement si un cas d'usage très spécifique avec domaine stable n'est pas couvrable par le RAG. [[chiffres-macro-2026#90-pourcent-cas-pme-ou-le-rag-bat-le-fine-tuning-hub-ia-learning-center|Pour 90 % des cas PME/ETI, le RAG suffit]].

## Token

Unité de texte traitée par un LLM, environ 3-4 caractères en moyenne (ou 0,75 mot). Les modèles facturent à l'usage en tokens (input + output). Une page A4 = ~500 mots ≈ 700 tokens.

## Prompt

Instruction donnée à un [[glossaire#llm]] en langage naturel. La qualité du prompt (clarté, contexte, structure, exemples) influe fortement sur la qualité de la réponse — d'où la pratique du « prompt engineering ».

## Eval-set

Aussi appelé « golden set » ou « test set ». Ensemble de questions/réponses de référence utilisé pour évaluer la qualité d'un système IA ([[glossaire#rag]] ou [[glossaire#llm]]). Chaque question est associée à une réponse attendue ou à des critères qualitatifs (sources à citer, concepts à mentionner). Permet de mesurer les régressions à chaque évolution du système. Discipline obligatoire en production (cycle Stitch → Evaluate → Iterate documenté dans DEP-02).

## LLM-as-judge

Pattern où un [[glossaire#llm]] est utilisé pour évaluer les sorties d'un autre LLM, à la place ou en complément d'une évaluation humaine. Permet de scaler l'évaluation qualité quand le volume de cas test devient trop grand pour une revue manuelle. À utiliser avec prudence : un LLM-as-judge peut hériter des biais du LLM évalué.

## Reranker

Modèle spécialisé qui re-classe les top-K résultats retournés par le retrieval initial du [[glossaire#rag]] avant de les passer au LLM générateur. Améliore significativement la précision du retrieval (les passages réellement pertinents remontent en tête). Acteurs de référence : Cohere Rerank, BAAI bge-reranker, Voyage. Composant qui devient standard dans les architectures RAG hybrides en production.

## Retrieval hybride

Stratégie de retrieval combinant **recherche dense** (similarité sémantique sur [[glossaire#embeddings]]) et **recherche sparse** (recherche par mots-clés type BM25). Cumule la robustesse du keyword matching (acronymes, codes produits, noms propres) et la flexibilité sémantique de la recherche vectorielle. Standard 2026 pour les RAG en production sur corpus moyens et grands. Détaillé dans [[dep-02]].

## MTEB

Massive Text Embedding Benchmark : benchmark public de référence pour évaluer la qualité des modèles d'[[glossaire#embeddings]]. Permet de comparer objectivement les modèles open-source et propriétaires sur des tâches standard (retrieval, classification, similarité, clustering). Mise à jour continue. Source d'arbitrage technique objectif pour le choix d'un modèle d'embedding.

---

*Glossaire — v3.8.4. À enrichir au fil des productions MD du vault.*
