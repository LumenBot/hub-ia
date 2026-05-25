---
code: outils-frameworks-rag
titre: "Outils — Frameworks RAG"
type: fiche-outil
axe: transverse
niveau: 3
tags: [framework-rag, langchain, llamaindex, haystack, langflow, rag, embeddings, retrieval]
version: 3.12.0
last_updated: 2026-05-25
glosaire_termes: [rag, llm, embeddings, vector-store, agent, prompt]
derives: ["[[cu-008]]", "[[cu-013]]", "[[dep-02]]", "[[dep-04]]", "[[outils-llm]]", "[[outils-vector-db]]", "[[outils-workflow-automation]]", "[[pattern-souverainete-eu]]"]
public_cible: [ops, r&d, tech]
---

# Outils — Frameworks RAG

## Quand utiliser un framework RAG

Un framework [[glossaire#rag]] est une bibliothèque (Python ou TypeScript généralement) qui pré-cable les briques essentielles d'un système RAG : ingestion documents, chunking, calcul d'[[glossaire#embeddings]], stockage dans un [[glossaire#vector-store]], retrieval, prompting LLM, parsing des réponses. Il évite de réécrire le pipeline RAG à la main et apporte des intégrations testées avec les principaux outils ([[outils-llm]], [[outils-vector-db]]).

3 frameworks Python sont des références marché 2026 : **LangChain** (le plus large écosystème + complexité), **LlamaIndex** (focus RAG natif, plus simple), **Haystack** (alternative européenne mature). En complément, des frameworks **visuels low-code** existent : **LangFlow** (visuel pour LangChain) et **Flowise** (visuel orchestré, voir [[outils-workflow-automation]]) pour les équipes non-Python.

Hybrides à signaler : **Dify** et **Flowise** sont catégorisés [[outils-workflow-automation]] car leur vocation principale est l'orchestration de workflows (RAG inclus mais pas central). À mentionner avec wikilink depuis cette fiche.

## LangChain — référence Python framework RAG

LangChain est le **framework RAG le plus utilisé** marché 2026 en Python (et JavaScript via LangChainJS). Combo : énorme catalogue d'intégrations (200+ LLM, 50+ vector stores, 100+ document loaders) + abstractions composables (chains, agents, tools) + écosystème massif (LangSmith pour observabilité, LangGraph pour agents complexes).

Inconvénient : complexité conceptuelle (beaucoup d'abstractions, courbe d'apprentissage), évolution rapide de l'API (breaking changes fréquents jusqu'à v1.0 stabilisée fin 2025).

**Quand l'utiliser** : RAG production avec besoin d'intégrations multiples, agents complexes (LangGraph), équipe Python expérimentée prête à investir dans la courbe d'apprentissage.

**Quand ne pas l'utiliser** : POC simple (LlamaIndex sera plus direct), équipe peu expérimentée Python (préférer Dify low-code, voir [[outils-workflow-automation]]), exigence de simplicité de stack.

**Modèle économique** : **open-source gratuit (MIT)** · LangSmith observabilité SaaS payant (voir [[outils-observabilite-llm]]) · LangGraph Platform managé (en preview 2026, tarification variable). Souveraineté niveau **Strong** (open-source auto-hébergeable, voir [[pattern-souverainete-eu]]).

**Cas d'usage Hub** : [[cu-008]] (Knowledge base RAG production), [[cu-013]] (Workflow email-CRM avec RAG), [[dep-02]] (RAG en production).

**Lien** : python.langchain.com / langchain.com

## LlamaIndex — référence Python framework RAG simplifié

LlamaIndex est l'**alternative LangChain focus RAG natif**. Plus simple à prendre en main, moins d'abstractions, API stable et pédagogique. Spécialisé dans le RAG (ingestion → index → query) avec des patterns de retrieval avancés (auto-merging, hierarchical, hybrid). Bonne pour les équipes qui veulent du RAG efficace sans la complexité de LangChain.

**Quand l'utiliser** : RAG en production avec focus simplicité, POC RAG rapide, équipe Python intermédiaire, patterns RAG avancés (hybrid search, reranking).

**Quand ne pas l'utiliser** : agents complexes multi-étapes (LangChain/LangGraph plus complet), besoin d'intégrations exotiques (catalogue plus restreint que LangChain).

**Modèle économique** : **open-source gratuit (MIT)** · LlamaCloud SaaS managé (ingestion + parsing + retrieval, en preview 2026, tarification variable). Souveraineté niveau **Strong** (open-source auto-hébergeable).

**Cas d'usage Hub** : [[cu-008]] (Knowledge base RAG simplifiée), [[dep-02]] (RAG en production focus simplicité).

**Lien** : llamaindex.ai / docs.llamaindex.ai

## Haystack — référence européenne mature

Haystack (deepset, DE) est le **framework RAG européen mature**, plus orienté production enterprise. Combo : architecture pipeline modulaire claire + composants production-ready + éditeur DE (souveraineté EU avancée) + intégrations avec LLMs locaux (Hugging Face natif).

**Quand l'utiliser** : RAG production enterprise EU avec exigence de souveraineté, équipe Python avec besoin d'architecture pipeline structurée, intégration avec modèles Hugging Face.

**Quand ne pas l'utiliser** : POC très rapide (LlamaIndex plus direct), équipe préférant l'écosystème LangChain dominant (plus large catalogue intégrations).

**Modèle économique** : **open-source gratuit (Apache 2.0)** · deepset Cloud SaaS managé (sur devis, cible enterprise). Souveraineté niveau **Strong à Sovereign** (éditeur DE, open-source, hébergement EU).

**Cas d'usage Hub** : [[cu-008]] (RAG production souverain EU), [[dep-02]] (RAG en production architecture pipeline), [[pattern-souverainete-eu]] (acteur de référence).

**Lien** : haystack.deepset.ai

## LangFlow — RAG visuel low-code pour LangChain

LangFlow est un **framework visuel low-code** qui permet de construire des chaînes LangChain par glisser-déposer (UI web). Avantage : prototypage rapide sans écrire de code Python, partage facile avec des équipes non-dev, génération du code Python sous-jacent en sortie.

**Quand l'utiliser** : prototypage rapide RAG ou agent, démo client/sponsor, équipe mixte tech + non-tech, génération de code Python LangChain pour reprise en main par dev.

**Quand ne pas l'utiliser** : production avec besoin de contrôle fin (code Python direct préférable), workflows complexes multi-systèmes (préférer n8n / Make, voir [[outils-workflow-automation]]).

**Modèle économique** : **open-source gratuit (MIT)** · LangFlow Cloud SaaS managé (freemium puis variable). Souveraineté niveau **Strong** (open-source auto-hébergeable).

**Cas d'usage Hub** : [[cu-008]] (POC RAG visuel), [[cu-027]] (Faire développer une appli métier sans être IT, alternative low-code).

**Lien** : langflow.org

## Outils hybrides à mentionner (workflows + RAG)

Pour les outils qui mêlent **workflows + RAG** (orchestration low-code + capacités RAG intégrées), voir leur fiche principale [[outils-workflow-automation]] :

- **Dify** — plateforme no-code/low-code, RAG inclus mais positionnement principal = orchestration agents/workflows
- **Flowise** — équivalent visuel low-code, orchestration multi-LLM + RAG basique

Si la priorité est **RAG pur en Python**, préférer LangChain / LlamaIndex / Haystack. Si la priorité est **orchestration workflow no-code avec RAG en option**, voir [[outils-workflow-automation]].

## Comparatif synthétique

| Framework | Type | Souveraineté | Tarif | Volume cible | Cas Hub principal |
|---|---|---|---|---|---|
| **LangChain** | Python framework dense | Strong (open-source) | Gratuit (MIT) | RAG production complexe | KB RAG, agents LangGraph |
| **LlamaIndex** | Python framework focus RAG | Strong (open-source) | Gratuit (MIT) | RAG production simplifié | KB RAG focus simplicité |
| **Haystack** | Python framework enterprise EU | Strong à Sovereign (DE) | Gratuit (Apache 2.0) | RAG production souverain | KB RAG souverain EU |
| **LangFlow** | Visuel low-code LangChain | Strong (open-source) | Gratuit (MIT) | POC + démos | POC RAG visuel |

## Recommandations PME par profil

**PME tech avec équipe Python (5-20 dev)** : LangChain pour le RAG production complexe + LangGraph pour les agents + LangSmith pour l'observabilité (voir [[outils-observabilite-llm]]).

**PME tech focus simplicité (1-5 dev)** : LlamaIndex pour RAG efficace + démos rapides + déploiement simplifié.

**PME EU avec exigence souveraineté forte** : Haystack (deepset DE) + Mixtral self-hosted (voir [[outils-llm]]) + Qdrant self-hosted (voir [[outils-vector-db]]) = stack RAG souveraine niveau Strong (voir [[pattern-souverainete-eu]]).

**PME mixte non-tech / tech légère** : LangFlow pour prototypage + Dify ou Flowise (voir [[outils-workflow-automation]]) pour usages low-code production.

## Pour aller plus loin

- **RAG en production** ([[dep-02]]) : architecture, chunking, retrieval, eval pipeline
- **Vector stores** ([[outils-vector-db]]) : Qdrant, pgvector, Pinecone, ChromaDB
- **Modèles LLM** ([[outils-llm]]) : Claude, GPT, Mistral, Mixtral, Llama, etc.
- **Workflows automation** ([[outils-workflow-automation]]) : n8n, Make, Dify, Flowise (hybrides RAG)
- **Observabilité LLM** ([[outils-observabilite-llm]]) : Langfuse, LangSmith, Phoenix
- **Pattern souveraineté EU** ([[pattern-souverainete-eu]]) : critères et niveaux de qualification
