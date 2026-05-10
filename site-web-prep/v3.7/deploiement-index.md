# Page d'index « Déploiement » — brief structurel pour Claude Code

**Fichier cible** : `deploiement.html` (à la racine du repo, parallèle à `prealables.html`)

---

## Objectif

Page d'index de la nouvelle section **Déploiement** (section transverse v3.7), analogue à `prealables.html` :
- Présentation de la section
- 8 cards vers les 8 fiches DEP
- Aiguillage par cas d'usage
- Footer avec liens connexes

## Structure HTML attendue (Claude Code)

Reprendre le pattern de `prealables.html` avec adaptations :

### Hero

- **Titre h1** : `🚀 Déploiement` (emoji ouvrant)
- **Sous-titre** : « Passer du pilote à la production. 95 % des projets GenAI en entreprise n'ont aucun impact P&L mesurable (MIT NANDA 2025). La cause n'est jamais la technologie, mais le cadrage. Cette section te donne les 8 cadrages essentiels pour ne pas faire partie des 95 %. »
- **Badge** : « Section transverse · Cadrage stratégique »

### Intro courte (~150 mots)

> La section **Déploiement** s'adresse aux dirigeants PME/ETI qui pilotent un projet IA en mise en production, et à leurs interfaces techniques (CTO, prestataire, équipe IT interne). Elle complète les **Préalables** (cadrage transverse) et les **Modules** (cas d'usage opérationnels) avec les **8 cadrages techniques essentiels** pour passer du pilote à la production : cadrage projet, RAG en production, context engineering, fine-tuning, observabilité, inférence, évaluation, sécurité.
>
> **Public** : Niveau ⭐⭐⭐ Avancé à ⭐⭐⭐⭐ Expert. Tu pilotes ou tu commandites un projet qui doit tenir en production.

### Grille des 8 cards

Format card identique aux préalables et modules, avec :
- Emoji ouvrant
- Titre métier
- Sous-titre court (1-2 phrases)
- Badge niveau (⭐⭐⭐ ou ⭐⭐⭐⭐)
- Badge durée
- Lien vers la fiche

#### Card DEP-01

- **Emoji** : 🎯
- **Titre** : « Cadrer un projet IA pour la mise en production »
- **Sous-titre** : « 95 % des projets GenAI échouent. La cause n'est jamais la technologie. »
- **Badge** : ⭐⭐⭐ Avancé · 18 min
- **Lien** : `deploiement/dep-01-cadrer-projet-prod.html`

#### Card DEP-02

- **Emoji** : 🔎
- **Titre** : « RAG en production : choisir son architecture »
- **Sous-titre** : « Le RAG hybride a triplé en Q1 2026. Voici comment décider entre LLM Wiki, RAG dense et hybride. »
- **Badge** : ⭐⭐⭐ Avancé · 22 min
- **Lien** : `deploiement/dep-02-rag-architecture-prod.html`

#### Card DEP-03

- **Emoji** : 💰
- **Titre** : « Context engineering et coût par requête »
- **Sous-titre** : « Prompt caching = -90 % sur les input tokens. Workslop = 9 M$/an pour 10 000 employés. »
- **Badge** : ⭐⭐⭐ Avancé · 18 min
- **Lien** : `deploiement/dep-03-context-engineering-couts.html`

#### Card DEP-04

- **Emoji** : 🎓
- **Titre** : « Fine-tuning : quand y aller, quand ne pas »
- **Sous-titre** : « Pour 80 % des cas PME, prompt + RAG suffit. Voici les 3 cas où le fine-tuning est vraiment justifié. »
- **Badge** : ⭐⭐⭐ Avancé · 15 min
- **Lien** : `deploiement/dep-04-fine-tuning-pme.html`

#### Card DEP-05

- **Emoji** : 🔭
- **Titre** : « Agents en production : observabilité et garde-fous »
- **Sous-titre** : « 89 % des organisations ont une forme d'observabilité. Les 5 layers essentiels et les garde-fous obligatoires. »
- **Badge** : ⭐⭐⭐⭐ Expert · 20 min
- **Lien** : `deploiement/dep-05-agents-observabilite.html`

#### Card DEP-06

- **Emoji** : ⚙️
- **Titre** : « Inférence et coûts : SaaS vs self-hosted »
- **Sous-titre** : « Kimi K2.6 = 8-10× moins cher qu'Opus. vLLM = 2-4× plus de débit. Le tableau de décision. »
- **Badge** : ⭐⭐⭐⭐ Expert · 18 min
- **Lien** : `deploiement/dep-06-inference-saas-self-hosted.html`

#### Card DEP-07

- **Emoji** : ✅
- **Titre** : « Évaluation continue et qualité IA »
- **Sous-titre** : « Tu ne peux pas piloter ce que tu ne mesures pas. La pipeline d'évaluation minimale en PME. »
- **Badge** : ⭐⭐⭐⭐ Expert · 17 min
- **Lien** : `deploiement/dep-07-evaluation-qualite.html`

#### Card DEP-08

- **Emoji** : 🛡️
- **Titre** : « Sécurité agents et MCP servers »
- **Sous-titre** : « 12 % de skills malveillants sur OpenClaw janvier 2026. CVE-2025-59536 sur Claude Code. Audit obligatoire. »
- **Badge** : ⭐⭐⭐⭐ Expert · 22 min
- **Lien** : `deploiement/dep-08-securite-agents-mcp.html`

### Aiguillage par cas d'usage (en bas de page)

Encart « Par où commencer ? » avec 3 parcours suggérés :

#### Parcours 1 — Tu démarres un projet IA

> 1. [DEP-01 Cadrer un projet IA pour la mise en production](deploiement/dep-01-cadrer-projet-prod.html)
> 2. [PR-07 Build vs Buy à l'ère de l'IA](prealables/pr-07-build-vs-buy.html)
> 3. Le module CU correspondant à ton cas d'usage métier

#### Parcours 2 — Tu mets en production un agent ou un RAG

> 1. [DEP-02 RAG en production : choisir son architecture](deploiement/dep-02-rag-architecture-prod.html) ou [DEP-05 Agents en production : observabilité et garde-fous](deploiement/dep-05-agents-observabilite.html)
> 2. [DEP-07 Évaluation continue et qualité IA](deploiement/dep-07-evaluation-qualite.html)
> 3. [DEP-08 Sécurité agents et MCP servers](deploiement/dep-08-securite-agents-mcp.html)

#### Parcours 3 — Tu maîtrises le coût d'inférence

> 1. [DEP-03 Context engineering et coût par requête](deploiement/dep-03-context-engineering-couts.html)
> 2. [DEP-06 Inférence et coûts : SaaS vs self-hosted](deploiement/dep-06-inference-saas-self-hosted.html)
> 3. [DEP-04 Fine-tuning : quand y aller, quand ne pas](deploiement/dep-04-fine-tuning-pme.html)

### Footer-CTA

> **Tu hésites encore sur l'architecture de déploiement ?** Va voir les [4 patterns d'architecture](architectures.html) (SaaS, propriétaire managé, open-source cloud souverain, on-premise).

## Implications navigation cross-pages

La nav 5 entrées (RULES § 1.2.3) devient **6 entrées** avec l'ajout de Déploiement :

```
Préalables · Architectures · Modules · Déploiement · Ressources · À propos
```

→ **Mise à jour cohérence numérique** : RULES § 1.2.3 doit être amendé en v1.5 pour refléter « 6 entrées de nav ».

## Composants CSS

- Reprendre le pattern `.prealables-grid` + `.pr-card` de `prealables.html`
- Renommer en `.deploiement-grid` + `.dep-card` (ou réutiliser tel quel si visuellement cohérent)
- Si nouveaux composants utilisés sur 2+ pages → migration `module-v3.css` (RULES § 1.5.3)

## Note Cowork
Page index brève et claire, miroir de prealables.html. Aiguillage par cas d'usage = nouveauté UX pour faciliter la prise en main de la section.
