---
code: outils-vector-db
titre: "Outils — Vector stores"
type: fiche-outil
axe: transverse
niveau: 3
tags: [vector-store, rag, embeddings, pinecone, qdrant, chromadb, pgvector]
version: 3.8.2
last_updated: 2026-05-11
glosaire_termes: [vector-store, rag, embeddings, hnsw, self-hosting, saas, open-source, souverainete, poc]
derives: ["[[cu-008]]", "[[dep-02]]", "[[dep-06]]"]
public_cible: [ops, r&d, tech]
---

# Outils — Vector stores

## Quand utiliser un vector store

Un [[glossaire#vector-store]] est la brique essentielle de tout système [[glossaire#rag]]. Il stocke les [[glossaire#embeddings]] de ton corpus documentaire (modules, manuels, CR de réunion, contrats…) et permet de retrouver à la volée les passages sémantiquement proches d'une question utilisateur.

Quatre acteurs principaux sont à connaître pour le marché 2026 : **Qdrant** (référence open-source self-hosted), **pgvector** (extension Postgres si Postgres est déjà en place), **Pinecone** (référence SaaS managée à grande échelle), **ChromaDB** (option dev-friendly pour POC et petits projets). Le choix dépend du volume, du besoin de souveraineté, de la présence ou non d'une équipe DevOps, et du stade du projet (POC vs production).

## Qdrant — référence open-source en production

Qdrant a gagné la bataille des vector stores open-source en 2024-2025. Combo : performances ([[glossaire#hnsw]] optimisé, filtres rapides), facilité d'opération (binaire Rust unique, container Docker simple), API REST claire, dashboard admin. Bien plus simple à opérer que ChromaDB ou Milvus en production. Choix par défaut pour le RAG souverain en France et en Europe.

**Quand l'utiliser** : RAG en production avec corpus > 10 000 documents, mémoire long terme d'agents, search sémantique full-stack, exigence de self-hosting pour souveraineté.

**Quand ne pas l'utiliser** : pour un [[glossaire#poc]] simple, pgvector dans un Postgres existant suffit. Pour volume ultra-massif (100M+ vecteurs), Pinecone ou Weaviate enterprise sont plus adaptés.

**Modèle économique** : self-hosted gratuit (Apache 2.0). Qdrant Cloud free tier 1 GB, premium à partir de 25 $/mois. Coûts qui scalent avec stockage et débit.

**Cas d'usage Hub** : [[cu-008]] (Knowledge base RAG, cas-école), [[cu-013]] (Workflow email-CRM), [[cu-019]] (Newsletter locale).

**Lien** : qdrant.tech/documentation

## pgvector — l'extension Postgres pour démarrer sans nouveau service

pgvector est une extension qui ajoute le support des vecteurs à PostgreSQL. Si tu as déjà Postgres en production dans ton SI, c'est par là que tu démarres ton RAG — pas besoin d'introduire un nouveau service à opérer. 80 % des entreprises ont déjà Postgres dans leur stack ; pgvector évite l'overhead opérationnel d'un nouveau composant.

**Fonctionnalités** : indexes ivfflat et hnsw, support des opérateurs cosine, L2, inner product, intégration native dans toutes les ORM modernes (SQLAlchemy, Prisma, etc.). Pour les volumes inférieurs à 10 millions de vecteurs, suffit largement à un Qdrant ou Pinecone, avec l'avantage de garder les vecteurs au même endroit que les données métier (requêtes hybrides SQL + similarité).

**Quand l'utiliser** : Postgres déjà en production (ne pas multiplier les services), volumes modérés (< 10 M vecteurs), requêtes hybrides SQL + similarité, souveraineté et ops simples.

**Quand ne pas l'utiliser** : volumes massifs avec contrainte de latence stricte → Qdrant ou Pinecone. Pas de Postgres existant → un service dédié sera mieux optimisé.

**Modèle économique** : gratuit (PostgreSQL License). Disponible sur RDS, Supabase, Neon, Crunchy Bridge — pricing variable selon l'hébergeur Postgres.

**Cas d'usage Hub** : [[cu-008]] (alternative pragmatique à Qdrant), [[cu-013]] (Workflow email-CRM).

**Lien** : github.com/pgvector/pgvector

## Pinecone — référence SaaS pour la production à grande échelle

Pinecone a été le premier vector store managé crédible et reste le leader sur les déploiements à grande échelle (millions à milliards de vecteurs). Pas d'opération à faire : tu pousses tes vecteurs, tu requêtes. 99,99 % uptime, scaling automatique, latence faible. Choix par défaut pour les équipes qui ne veulent pas gérer d'infrastructure mais ont besoin d'une stack RAG robuste 24/7.

**Quand l'utiliser** : RAG en production critique avec SLA serré, volumes supérieurs à 1 million de vecteurs avec scaling automatique, pas d'équipe DevOps disponible pour gérer un Qdrant.

**Quand ne pas l'utiliser** : exigence stricte de [[glossaire#souverainete]] EU (Pinecone est hébergé aux US), besoin de self-hosting, POC ou petit volume (ChromaDB ou pgvector suffiront).

**Modèle économique** : free tier 1 index et 100 000 vecteurs. Standard à partir de ~50 $/mois (scaling à l'usage : stockage + RU/s). Enterprise sur devis. Pricing peut grimper rapidement sur des volumes importants — c'est l'arbitrage économique avec Qdrant self-hosted.

**Cas d'usage Hub** : [[cu-008]] (alternative SaaS à Qdrant), [[cu-013]] (Workflow email-CRM), [[cu-014]] (Multi-agents).

**Lien** : docs.pinecone.io

## ChromaDB — vector store dev-friendly pour POC

ChromaDB est le vector store « pip install et c'est parti ». Idéal pour les POC, le développement local, les petits projets. Mode embedded (dans le process Python) ou serveur. Plus simple à mettre en main que Qdrant pour démarrer, mais moins robuste en production à grande échelle.

**Quand l'utiliser** : prototypage rapide, RAG sur petit corpus (quelques milliers de documents), apprentissage du RAG, tests locaux sans infrastructure.

**Quand ne pas l'utiliser** : production à fort trafic, volumes importants nécessitant un index optimisé et du sharding, exigence de robustesse opérationnelle.

**Modèle économique** : gratuit (open-source). Pas d'offre managée mature à ce jour (mai 2026).

**Cas d'usage Hub** : [[cu-008]] (POC RAG simple), recommandation native pour les démonstrateurs et premiers prototypes.

**Lien** : trychroma.com

## Comparatif synthétique

| Critère | Qdrant | pgvector | Pinecone | ChromaDB |
|---|---|---|---|---|
| Type | Open-source self-host | Extension Postgres | SaaS managé | Open-source self-host |
| Souveraineté EU | ✅ (self-host) | ✅ (selon hébergement) | ❌ (US) | ✅ (self-host) |
| Volume cible | 10k → 100M+ | < 10M | 1M → 1Md+ | < 1M (POC) |
| Coût initial | Gratuit (self) ou 25 $/mois | Gratuit | Free tier puis 50 $/mois+ | Gratuit |
| Effort opérationnel | Léger | Très léger (si Postgres présent) | Plug-and-play | Très léger (POC) |
| Cas Hub principal | RAG souverain prod | Postgres existant | RAG SaaS scaled | POC et démonstrateurs |

## Pour aller plus loin

- Discussion approfondie du choix vector DB selon le volume : [[dep-02]] (RAG en production)
- Choix SaaS vs self-hosted plus largement : [[dep-06]] (Inférence et coûts)
- Cas d'école RAG complet avec choix Qdrant : [[cu-008]] (Knowledge base interne RAG)
