# Lot D v3.8 — 4 nouvelles fiches outils

**Brief consolidé pour Claude Code** : 4 nouvelles fiches `<article class="tool-card">` à créer dans `ressources.html`.

**Sources** : veille v3.7.13 (Grok input 1 + Grok input 2).

**Avant intégration** : vérifier le format exact des fiches outils existantes dans `ressources.html` (composant `.tool-card`, métadonnées affichées, structure des badges) pour cohérence visuelle.

---

## Fiche D.1 — Hermes Agent (NousResearch)

- **Ancre HTML** : `id="hermes-agent"`
- **Catégorie** : Agents IA / frameworks multi-agents
- **Émoji** : 🪽 (ou autre selon convention catégorie)
- **Type** : Agent open-source auto-améliorant
- **Maturité** : Émergent (publié par NousResearch en 2026)
- **Souveraineté** : 🟡 Open-source / self-hostable / dépend du modèle backend choisi (peut être souverain si modèle EU)
- **Coût indicatif** : Gratuit (logiciel) + coût modèle backend (variable selon OpenRouter, modèle local, etc.)
- **Complexité** : Moyenne-élevée (configuration self-host, gestion des skills)

### Description courte

Hermes Agent est un agent IA **open-source auto-améliorant** publié par NousResearch en 2026. Il combine plusieurs caractéristiques avancées : **mémoire persistante multi-niveaux** (court-terme, long-terme, épisodique), **génération de skills à la volée** (l'agent apprend de nouveaux comportements en cours de mission), **accès à une machine dédiée** (sandbox d'exécution), et **compatibilité multi-modèles** (OpenRouter, modèles locaux via Ollama ou vLLM).

### Atouts pour PME

- Open-source et auto-hostable (souveraineté)
- Mémoire persistante = l'agent s'enrichit au fil des sessions
- Génération de skills = capacité d'évolution sans intervention
- Multi-modèles = pas de lock-in sur un éditeur LLM

### Limites

- Configuration et maintenance demandent un profil technique
- L'auto-amélioration nécessite un cadre de gouvernance solide (cf. CU-026 Gouvernance des agents IA)
- Documentation encore en construction (projet récent)

### Quand le choisir

- PME ou ETI avec équipe technique interne capable de self-hoster
- Cas d'usage agentic complexes nécessitant une évolution continue de l'agent
- Besoin de souveraineté forte (alternatives aux agents SaaS US)

### Modules / fiches du Hub qui mentionnent Hermes Agent

- CU-014 (Multi-agents par fonction)
- CU-026 Gouvernance des agents IA (nouveau v3.8)
- DEP-05 (Agents en production)

### URL officielle

https://hermes-agent.nousresearch.com/

---

## Fiche D.2 — SuperSplat (PlayCanvas)

- **Ancre HTML** : `id="supersplat"`
- **Catégorie** : Knowledge management / Visualisation 3D no-code
- **Émoji** : 🪄 (ou ✨, selon convention)
- **Type** : Éditeur open-source navigateur
- **Maturité** : Émergent (~2025-2026)
- **Souveraineté** : 🟢 Open-source, browser-based, pas de cloud requis
- **Coût indicatif** : Gratuit
- **Complexité** : Faible (drag & drop)

### Description courte

SuperSplat (par PlayCanvas) est un **éditeur open-source dans le navigateur** pour les **3D Gaussian Splats** — une technologie qui permet de transformer un simple **scan smartphone** d'un objet ou d'un lieu en **modèle 3D interactif** consultable en browser. Cas d'usage typiques : visite virtuelle 3D pour PME (immobilier, tourisme, formation industrielle, expositions), pour un **coût drastiquement réduit** (~200 $ vs 15 K$ pour une prestation 3D professionnelle classique).

### Atouts pour PME

- Coût ultra-réduit pour de la 3D interactive
- Pas d'expertise 3D requise (scan smartphone + outil web)
- Open-source et navigateur (pas de logiciel à installer)
- Sortie directement publiable sur un site web

### Limites

- Technologie récente, qualité dépend fortement de la qualité du scan smartphone
- Pas adapté à la 3D métier précise (CAO, plans techniques)
- Cible spécifique : visite/présentation/communication, pas conception

### Quand le choisir

- PME tourisme : visite virtuelle d'un gîte, d'un site touristique
- PME immobilier : présentation immersive d'un bien
- PME industrielle : présentation d'un atelier, d'un poste de travail, d'une formation outillée
- Communication / marketing : valorisation visuelle de l'entreprise

### Modules / fiches du Hub qui mentionnent SuperSplat

- CU-009 (Content repurposing) — pour valorisation de contenu visuel
- CU-019 (Newsletter locale) — pour enrichir une newsletter avec une expérience immersive

### URL officielle

https://superspl.at/

---

## Fiche D.3 — AAFLOW

- **Ancre HTML** : `id="aaflow"`
- **Catégorie** : Workflow agentique / Runtime distribué
- **Émoji** : ⚡ (ou autre selon convention performance)
- **Type** : Framework open-source distribué
- **Maturité** : Émergent (publication 2026)
- **Souveraineté** : 🟢 Open-source, self-hostable
- **Coût indicatif** : Gratuit (logiciel) + infrastructure distribuée nécessaire
- **Complexité** : Élevée (profil DevOps / data engineering)

### Description courte

AAFLOW est un **unified distributed runtime** pour les pipelines agentic IA, basé sur **Apache Arrow et Cylon**. Il propose une approche **zero-copy serialization** (les données ne sont pas sérialisées/désérialisées entre les étapes du pipeline), une **abstraction par opérateurs composables**, et un **scheduling resource-deterministic** (planification déterministe de l'exécution). Documentations publiques : speedup pipeline jusqu'à **4,64×** sur des benchmarks comparatifs.

### Atouts pour PME

- Performance significative sur les pipelines agentic complexes
- Open-source et self-hostable (souveraineté)
- Architecture data plane optimisée (pas seulement « optimisation LLM »)

### Limites

- Configuration et exploitation demandent un profil DevOps / data engineering avancé
- Surdimensionné pour des cas d'usage agentic simples (1-3 agents séquentiels)
- Documentation encore en construction

### Quand le choisir

- PME ayant déployé des pipelines agentic complexes en production avec des problèmes de latence ou de coût
- ETI avec équipe data engineering interne capable d'opérer
- Volume de requêtes significatif justifiant l'investissement infrastructure

### Modules / fiches du Hub qui mentionnent AAFLOW

- DEP-05 (Agents en production : observabilité et garde-fous) — bottlenecks data plane
- DEP-06 (Inférence et coûts : SaaS vs self-hosted) — optimisation de production

### URL officielle

À renseigner depuis le repo GitHub de référence du projet (à vérifier au moment de la création de la fiche).

---

## Fiche D.4 — Beever Atlas

- **Ancre HTML** : `id="beever-atlas"`
- **Catégorie** : Knowledge management / LLM Wiki
- **Émoji** : 🐝 (ou autre selon convention)
- **Type** : Fork open-source du pattern LLM Wiki
- **Maturité** : Très émergent / signal faible (2026)
- **Souveraineté** : 🟢 Open-source, self-hostable
- **Coût indicatif** : Gratuit (logiciel) + coût modèle LLM backend
- **Complexité** : Moyenne (setup self-host)

### Description courte

Beever Atlas est un **fork open-source** du pattern **LLM Wiki** popularisé par Andrej Karpathy en avril 2026. Il propose une implémentation pratique des principes du LLM Wiki (`ingest → synthesize → evolve`) avec des fonctionnalités complémentaires émergentes : persistent memory, contradiction detection, multi-agent vaults. **Signal faible à confirmer** : le projet est récent et l'écosystème de forks LLM Wiki post-Karpathy est en pleine effervescence.

### Atouts pour PME

- Implémentation concrète et open-source du pattern LLM Wiki
- Self-hostable (souveraineté)
- Aligné sur les principes éprouvés (mémoire persistante, synthèse vivante)

### Limites

- Projet très récent — maturité à valider
- Documentation et communauté encore limitées
- Plusieurs forks alternatifs en compétition (à benchmarker)

### Quand le choisir

- PME explorant le pattern LLM Wiki sur un corpus interne stable et de taille moyenne
- Cas d'usage knowledge management évolutif (manuel produit, FAQ, procédures qui évoluent)
- Volonté de contribuer à l'écosystème open-source

### Modules / fiches du Hub qui mentionnent Beever Atlas

- CU-008 (Knowledge base RAG) — pattern LLM Wiki post-Karpathy

### URL officielle

À renseigner depuis le repo GitHub de référence du projet (à vérifier au moment de la création de la fiche).

---

## Synthèse Lot D pour Claude Code

**Volume** : 4 nouvelles fiches outils dans `ressources.html`.

**Effort estimé Claude Code** : 1-2 h.

**Format à respecter** : pattern existant des `<article class="tool-card" id="...">` dans `ressources.html`. Vérifier la structure exacte d'une fiche existante avant de créer les nouvelles, pour cohérence visuelle.

**Catégorisation** :
- **Hermes Agent** → catégorie « Agents IA » ou « Frameworks multi-agents » (selon classification existante)
- **SuperSplat** → catégorie « Knowledge management » ou créer une nouvelle catégorie « Visualisation / 3D » si pertinent (à arbitrer selon contenu existant)
- **AAFLOW** → catégorie « Workflow / Automatisation » ou « Frameworks LLM »
- **Beever Atlas** → catégorie « Knowledge management »

### Cohérence numérique post-Lot D

**95 fiches outils → 99 fiches outils** (passage de 95 à 99 avec les 4 ajouts).

À mettre à jour cross-site (RULES § 1.2.3) : home `index.html`, `prealables.html`, `architectures.html`, `deploiement.html`, `ressources.html` (badge synthèse), section À propos, README.md, méta-descriptions de toutes les pages mentionnant le chiffre.

### Renvois inter-lots

- Hermes Agent référencé dans CU-014 (Lot B.2), CU-026 (Lot E), DEP-05 (Lot B.4)
- SuperSplat référencé éventuellement dans CU-009 / CU-019 (à voir si Cowork ou Claude Code décide d'ajouter ces renvois)
- AAFLOW référencé dans DEP-05 (Lot B.4)
- Beever Atlas référencé dans CU-008 (Lot B.1)

À ajouter dans le corps de ces modules à la première mention de chaque outil (RULES § 1.5.6).

## Note Cowork

Sources confirmées via veille v3.7.13. URLs officielles : à vérifier au moment de la création des fiches HTML (les projets émergents ont parfois des URLs qui changent rapidement). Si une URL est introuvable au moment de la création, **ne pas inventer** — laisser un placeholder « URL officielle à renseigner » et signaler dans le rapport mission. Conforme RULES § 1.1.
