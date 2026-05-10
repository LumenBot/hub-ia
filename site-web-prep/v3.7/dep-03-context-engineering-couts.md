# DEP-03 — Context engineering et coût par requête

**Public cible :** dirigeant + DAF qui pilote le coût IA, équipe technique qui implémente

---

## Métadonnées (pour Claude Code)

- **Section** : Déploiement
- **Niveau** : ⭐⭐⭐ Avancé
- **Type** : Cadrage stratégique
- **Durée lecture** : 18 min
- **Emoji h1** : 💰
- **Titre métier visible** : « Context engineering et coût par requête »
- **Sous-titre hero** : Le prompt caching Anthropic réduit de 90 % le coût des input tokens cachés. Mais 40 % des employés reçoivent du « workslop » qui coûte 9 M$/an dans une entreprise de 10 000 personnes. Le coût IA n'est pas seulement le prix du token.
- **Card index promesse** : « Cadrage stratégique »

## Synthèse exécutive

### Pourquoi cette page ?

Tu es dirigeant ou DAF. Tu vois les premières factures Anthropic / OpenAI et tu te demandes : **« comment maîtriser ces coûts qui explosent ? »**. Cette fiche te donne les **5 leviers documentés** qui font la différence entre une facture qui s'envole et une facture maîtrisée :

1. Le prompt caching (Anthropic, AWS Bedrock) — **-90 % sur les input tokens cachés**
2. La gouvernance prompts comme du code (versioning, tests)
3. La gestion du contexte (le « context window » a un coût et une limite cognitive)
4. Le choix de modèle par cas d'usage (Kimi K2.6 = **8-10x moins cher** que Claude Opus 4.7)
5. Le pilotage du « workslop » (le coût caché de l'IA mal cadrée)

L'enjeu n'est plus uniquement technique. C'est devenu un sujet de pilotage budgétaire.

### 4 takeaways

1. **Le prompt caching change l'économie de l'IA.** Anthropic propose -90 % sur les input tokens cachés (0,1× le prix standard sur cache hit). Sur des conversations longues (RAG, agents, support client), le caching peut diviser la facture par 5 à 10. Coût d'écriture du cache : 1,25× standard pour TTL 5 min.

2. **Workslop = 186 $/employé/mois de coût caché.** Étude BetterUp x Stanford septembre 2025 : 40 % des employés ont reçu du « workslop » (contenu IA poli mais inutile/inexact) sur 30 jours. Coût moyen : 1h56 par incident, **9 M$/an pour une entreprise de 10 000 personnes**. Argument-massue pour vendre la gouvernance prompts.

3. **Le reasoning des LLM se dégrade au-delà de 3 000 tokens.** Sweet spot pratique : 150-300 mots dans le prompt utilisateur. Une JSON schema complexe consomme 500+ tokens. 90 outils disponibles dans un agent = 50 000+ tokens **avant la première interaction**. La gestion du contexte est devenue un métier.

4. **Le choix de modèle est devenu un arbitrage stratégique.** Kimi K2.6 (open-source, chinois) est 8-10x moins cher que Claude Opus 4.7 pour ~75 % de la qualité. Pour 80 % des cas d'usage PME, un modèle moyen suffit largement. Garder Opus pour 20 % de cas réellement complexes.

### Stats (3-4)

- **-90 %** sur les input tokens cachés avec prompt caching Anthropic (0,1× prix standard)
- **40 %** des employés ont reçu du « workslop » sur 30 jours, **186 $/employé/mois** (BetterUp x Stanford, sept. 2025)
- **Dégradation à 3 000 tokens** : reasoning des LLM commence à perdre en qualité (état de l'art context engineering 2026)
- **8-10×** : Kimi K2.6 vs Claude Opus 4.7 (75 % de la qualité pour 10 % du prix)

### Quand cette page est utile

Tu as commencé à utiliser l'IA en production. Tu vois les premières factures. Tu veux **maîtriser les coûts sans sacrifier la qualité**. Tu cherches un cadre pour gouverner les prompts comme du code. Tu te demandes si tu peux switcher de modèle pour réduire la facture.

## Section 1 — Le prompt caching, levier n°1 d'optimisation coût

### 1.1 Comment ça marche

Le prompt caching permet de **réutiliser** le calcul d'une portion du contexte qu'on envoie à plusieurs reprises au modèle. Concrètement : si tu as un long système prompt + un long manuel produit que tu envoies à chaque conversation, le modèle peut « mémoriser » cette portion stable et la facturer **0,1× le prix standard** (cache hit).

Anthropic a popularisé le pattern. AWS Bedrock l'a adopté. OpenAI propose un équivalent.

### 1.2 Cas d'usage où le caching divise la facture

- **RAG sur corpus stable** : système prompt + chunks récupérés similaires entre requêtes
- **Agents multi-tour** : conversation longue où le contexte initial reste identique
- **Support client** : FAQ / base de connaissance envoyée à chaque interaction
- **Génération de code** : codebase ou documentation envoyée en contexte stable

### 1.3 Coûts du caching à connaître

- **Lecture cache (cache hit)** : 0,1× prix standard input
- **Écriture cache** : 1,25× prix standard input pour TTL 5 min, 2× pour TTL 1h
- **Pas de cache** : prix standard

→ **Stratégie type** : tout ce qui est stable > 5 min (système prompt, FAQ, manuel produit) → cacher avec TTL 1h. Tout ce qui change vite → ne pas cacher.

### 1.4 Économie type pour une PME

Pour une PME utilisant Claude pour du support client (1000 conversations/mois × 4000 tokens contexte stable) :
- **Sans caching** : ~150-200 €/mois
- **Avec caching** (90 % cache hit) : ~30-50 €/mois

→ Économie de 70 à 80 % sur la facture d'inférence.

## Section 2 — Le workslop, coût caché documenté

### 2.1 Définition (BetterUp x Stanford 2025)

Le **workslop** = contenu produit par IA qui a l'air poli et professionnel, mais qui est **inutile, inexact, ou pire**, qui force des corrections en aval. Exemples :
- Mail commercial parfaitement rédigé mais qui dit n'importe quoi sur le produit
- Compte-rendu de réunion qui invente des engagements
- Code qui appelle une fonction qui n'existe pas
- Synthèse documentaire qui omet l'élément critique

### 2.2 Les chiffres qui doivent t'arrêter

- **40 % des employés** ont reçu du workslop sur les 30 derniers jours (étude BetterUp x Stanford, septembre 2025, n=1100)
- **1h56** : temps moyen perdu par incident workslop (correction, vérification, refonte)
- **186 $/employé/mois** de coût caché en moyenne
- **9 M$/an** pour une entreprise de 10 000 personnes

### 2.3 Comment réduire le workslop : la gouvernance prompts comme du code

Cinq pratiques documentées :

1. **Versionner les prompts** dans un repo git (pas dans des chat éphémères)
2. **Tester les prompts** avec un dataset golden (50-100 cas) avant déploiement
3. **Documenter chaque prompt** : objectif, audience, format de sortie attendu, contre-exemples
4. **Reviewer les prompts** comme du code (PR avec relecture par un pair)
5. **Mesurer les regressions** quand on change de modèle ou qu'on optimise

→ Outils : promptlayer, langfuse, helicone (open-source), phoenix arize (open-source)

## Section 3 — La gestion du contexte (context engineering)

### 3.1 Le contexte n'est pas infini, ni cognitivement neutre

Bien que les modèles annoncent des fenêtres de **1M, 2M, 10M tokens**, leur **reasoning se dégrade dès 3 000 tokens** (recherche état de l'art 2026 sur la dégradation de l'attention long-context).

Conclusion pratique : **le contexte qui compte = celui que le modèle utilise effectivement**, pas celui qu'on lui envoie.

### 3.2 Le coût des tools et schemas dans un agent

Quand on construit un agent avec MCP servers (Model Context Protocol) ou tool calling :
- Une JSON schema complexe = **500+ tokens** par outil
- 90 outils disponibles = **50 000+ tokens avant la première interaction utilisateur**
- Multiplié par chaque appel à l'agent

→ Stratégie : **filtrer les outils** par contexte (un agent commercial n'a pas besoin des outils techniques). Réduit le contexte initial de 80-90 %.

### 3.3 Sweet spot pratique en context engineering

Pour un prompt utilisateur :
- **150-300 mots** : sweet spot reasoning
- **300-1000 mots** : encore acceptable pour tâches structurées
- **> 1000 mots** : commence à diluer l'attention

Pour le contexte total (système + retrieval + historique) :
- **< 8K tokens** : excellent
- **8K-32K tokens** : acceptable avec discipline
- **> 32K tokens** : nécessite caching et filtrage

## Section 4 — Le choix de modèle comme arbitrage stratégique

### 4.1 La règle 80/20 du choix de modèle

Pour la majorité des cas d'usage PME :
- **80 % des requêtes** sont gérables par un modèle moyen (Claude Sonnet, GPT-4 mini, Mistral Medium, Kimi K2.6)
- **20 % des requêtes** complexes nécessitent un modèle haut de gamme (Claude Opus, GPT-4 Turbo)

Coût typique :
- **Modèle moyen** : 0,5-3 $/M input tokens, 2-15 $/M output tokens
- **Modèle haut de gamme** : 5-15 $/M input, 15-75 $/M output

→ Bien dispatcher = diviser la facture par 5 à 10.

### 4.2 Le cas Kimi K2.6 — la bascule chinoise

Kimi K2.6 (open-source Moonshot AI, sortie 2026) :
- **0,80 $/M input, 3,60 $/M output** (vs Claude Opus 4.7 à 5 $/M input et 25 $/M output)
- Performance proche de Claude Opus sur SWE-Bench, Terminal-Bench, agentic coding
- Open-source, self-hostable
- Hébergement EU possible

→ Pour les use cases coding agentique (cf. [CU-027 Faire développer une appli métier](../modules/cu-027-dev-applicatif-ia.html)), Kimi K2.6 devient un challenger sérieux à Opus.

### 4.3 Stratégie de routage (LLM gateway)

Outils type **LiteLLM** (open-source) ou **OpenRouter** permettent de :
- Router selon complexité de la requête (simple → modèle pas cher, complexe → modèle premium)
- Implémenter un fallback (si Anthropic down → bascule OpenAI)
- Tracker le coût par cas d'usage
- A/B tester deux modèles en parallèle

→ Gain typique : 30-60 % de réduction de facture sur 6 mois après déploiement d'un LLM gateway.

## Section 5 — Tableau récapitulatif des leviers

| Levier | Effort initial | Gain typique | Quand y aller |
|---|---|---|---|
| **Prompt caching** | 1-3 jours dev | -50 à -80 % facture inférence | Dès que contexte stable > 5 min |
| **Gouvernance prompts** (versioning, tests) | 1-2 semaines setup | -30 à -50 % workslop | Avant la mise en prod |
| **Filtrage outils MCP** | 1-2 jours | -50 à -90 % contexte initial agent | Dès que > 10 outils |
| **LLM gateway + routage modèle** | 1-2 semaines | -30 à -60 % facture totale | Dès 500 €/mois de facture |
| **Switch modèle premium → moyen** | Quelques heures | -50 à -90 % par requête | Audit régulier des cas d'usage |

## Section 6 — Plan d'action 30 jours pour maîtriser les coûts IA

### Jours 1-7 — Audit
- Extraire la facture détaillée par cas d'usage
- Identifier les 3-5 cas d'usage les plus consommateurs
- Mesurer le contexte moyen et le ratio cache hit actuel

### Jours 8-15 — Quick wins
- Activer le prompt caching sur les cas d'usage à contexte stable
- Filtrer les outils MCP des agents (ne garder que les utilisés)
- Switcher les cas d'usage simples vers un modèle moyen

### Jours 16-30 — Gouvernance
- Mettre en place le versioning de prompts dans un repo git
- Construire un dataset golden de 50-100 cas (par cas d'usage)
- Déployer un LLM gateway (LiteLLM open-source) pour routage et tracking

→ **Économie typique attendue à 30 jours** : 40 à 70 % de la facture initiale.

## Section 7 — Pour aller plus loin (Schéma A)

### Callout d'aiguillage

> Pour le panorama complet des outils LLM gateway, monitoring et observabilité, retrouve les fiches détaillées sur la [page Ressources du Hub](../ressources.html#bibliographie).

### 📰 Articles de fond
- [HBR — AI-generated workslop is destroying productivity (sept. 2025)](https://hbr.org/2025/09/ai-generated-workslop-is-destroying-productivity) — Étude BetterUp x Stanford
- [Anthropic News — Prompt caching announcement](https://www.anthropic.com/news/prompt-caching) — Annonce officielle + benchmarks
- [Aurimas Griciūnas / SwirlAI — State of context engineering 2026](https://www.newsletter.swirlai.com/p/state-of-context-engineering-in-2026) — Synthèse pratique

### 🎓 Tutoriels & cas pratiques
- [Anthropic Docs — Prompt caching guide](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) — Documentation officielle
- [Avi Chawla — Context engineering pillar](https://blog.dailydoseofds.com/p/foundations-of-ai-engineering-and-0a6) — Pilier 3 du LLM Engineering Roadmap

### 📚 Documentation officielle & études
- [Maxim AI — Context engineering for AI agents](https://www.getmaxim.ai/articles/context-engineering-for-ai-agents-production-optimization-strategies/) — Token economics 2026
- [LiteLLM Docs](https://docs.litellm.ai/) — LLM gateway open-source de référence
- [BetterUp x Stanford — Workslop study](https://hbr.org/2025/09/ai-generated-workslop-is-destroying-productivity) — Méthodologie + chiffres

### 👥 Communautés & veille
- [Anthropic Discord](https://www.anthropic.com/discord) — Échanges techniques pratiques
- [LangChain GitHub Discussions](https://github.com/langchain-ai/langchain/discussions) — Patterns context engineering

## Renvois internes pour Claude Code

- **Section 4.2** : lien `<a href="../modules/cu-027-dev-applicatif-ia.html">CU-027</a>` pour le coding agentique
- **Section corps** : si fiche Kimi K2.6 créée → lien `<a href="../ressources.html#kimi-k2">Kimi K2.6</a>`
- **Section corps** : si fiche LiteLLM créée → lien `<a href="../ressources.html#litellm">LiteLLM</a>`

## Composants visuels suggérés

- **Section 1.4** : `.stat-block` pour le « 70-80 % d'économie avec caching »
- **Section 2.2** : `.alert-block` pour les chiffres workslop (rouge = enjeu)
- **Section 5** : `.tool-table` pour le tableau récapitulatif des leviers
- **Section 6** : `.timeline-block` pour le plan d'action 30 jours

## Note Cowork
Sources prioritaires : Anthropic, BetterUp x Stanford / HBR, Avi Chawla, Maxim AI. Données vérifiées : -90 % cache (pas 92 %), 9M$/an pour 10 000 employés. Conforme RULES § 1.1.
