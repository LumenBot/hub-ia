# DEP-05 — Agents en production : observabilité et garde-fous

**Public cible :** dirigeant qui pilote un projet agents IA + équipe technique opérationnelle

---

## Métadonnées (pour Claude Code)

- **Section** : Déploiement
- **Niveau** : ⭐⭐⭐⭐ Expert
- **Type** : Cadrage stratégique
- **Durée lecture** : 20 min
- **Emoji h1** : 🔭
- **Titre métier visible** : « Agents en production : observabilité et garde-fous »
- **Sous-titre hero** : 89 % des organisations ont une forme d'observabilité pour leurs agents, 94 % parmi celles en prod. La qualité reste le blocker n°1 (32 %), la sécurité monte en n°2 (24,9 %). Voici le cadre opérationnel.
- **Card index promesse** : « Cadrage stratégique »

## Synthèse exécutive

### Pourquoi cette page ?

Tu as un agent IA en production (ou tu t'apprêtes à en mettre un). Sans **observabilité** (tracing, monitoring, logs structurés) et sans **garde-fous** (retry logic, fail-safe, cap budgétaire), un agent en prod est une bombe à retardement. LangChain *State of Agent Engineering 2026* est sans appel : **57 % des organisations ont des agents en prod, 89 % ont une forme d'observabilité, 94 % parmi celles en prod**. Si tu n'es pas dans ces 94 %, tu fais partie des structures qui apprendront à leurs dépens.

Cette fiche te donne le cadre minimum : les 5 layers d'observabilité essentiels, les outils 2026 (open-source et SaaS), les patterns de garde-fous, et les KPI à monitorer.

### 4 takeaways

1. **L'observabilité = obligatoire en prod, non négociable.** 94 % des organisations ayant des agents en prod ont déployé une forme d'observabilité (LangChain 2026). Sans tracing structuré, retry monitoring, alertes, tu ne sais pas que ton agent est cassé jusqu'à ce qu'un client appelle.

2. **5 layers d'observabilité à connaître.** (a) Logs LLM (chaque appel modèle), (b) Tool calls (chaque action exécutée), (c) Retry/fallback (chaque échec géré), (d) Coût par session, (e) Satisfaction utilisateur. Sans ces 5 layers, tu pilotes à l'aveugle.

3. **Les garde-fous sauvent ta facture.** Un agent en boucle infinie peut consommer **10 000 € en 24h** sans cap budgétaire. Cap obligatoire : par session, par utilisateur, par jour. Plus retry-with-backoff, fail-safe gracieux, step-limit absolu.

4. **La qualité reste le blocker n°1 (32 %), la sécurité monte au n°2 (24,9 %).** LangChain 2026. Implications : ton plan d'observabilité doit prévoir mesure qualité (eval pipeline) ET monitoring sécurité (anomalies, prompt injections détectées).

### Stats (3-4)

- **57 %** des organisations ont des agents en production (LangChain 2026)
- **89 %** ont une forme d'observabilité, **94 %** parmi celles en prod (LangChain 2026)
- **32 %** : qualité = blocker n°1 ; **24,9 %** : sécurité = blocker n°2 dans grandes entreprises (LangChain 2026)
- **23 %** des organisations scalent un système agentique en au moins une fonction (McKinsey, novembre 2025)

### Quand cette page est utile

Tu as un agent IA en production ou en pilote avancé. Tu cherches le cadre minimum d'observabilité avant de monter en charge. Tu as déjà eu des incidents (réponses fausses, boucles infinies, factures qui explosent) et tu veux les prévenir.

## Section 1 — Pourquoi l'observabilité d'agents est différente du monitoring traditionnel

### 1.1 Le problème spécifique aux agents

Un agent IA fait plusieurs choses **non déterministes** à chaque appel :
- Choisir un outil (qui peut être le mauvais)
- Lire un résultat (qui peut être ambigu)
- Décider du prochain step (qui peut diverger)
- Générer une réponse (qui peut halluciner)

Un monitoring traditionnel (HTTP 200/500, latence, erreurs) **ne suffit pas**. Un agent peut renvoyer 200 OK avec une latence parfaite et une réponse complètement fausse.

### 1.2 La règle « tu ne pilotes pas ce que tu ne mesures pas »

Sans observabilité spécifique aux agents, tu ne sais pas :
- Combien d'erreurs sont remontées par les utilisateurs (vs subies silencieusement)
- Pourquoi un agent boucle (mauvais outil ? prompt mal cadré ? modèle qui dérive ?)
- Combien chaque session coûte
- Si la qualité moyenne se dégrade au fil du temps (drift)

→ La direction conduit à l'aveugle. Les incidents sont systémiquement détectés trop tard.

## Section 2 — Les 5 layers d'observabilité essentiels

### 2.1 Layer 1 — Logs LLM structurés

À chaque appel modèle, on log :
- Modèle utilisé (Claude Sonnet, GPT-4, etc.)
- Tokens input / output
- Coût estimé
- Latence
- Système prompt + user prompt (anonymisés)
- Réponse complète

**Outil de référence** : Comet Opik, LangSmith, Helicone, Phoenix Arize, Langfuse (open-source), promptlayer.

### 2.2 Layer 2 — Tool calls tracking

Chaque outil appelé par l'agent :
- Nom de l'outil
- Paramètres passés
- Résultat retourné
- Succès/échec
- Latence

→ Permet de détecter : outils qui échouent souvent, outils sous-utilisés (à supprimer pour réduire le contexte), patterns de chaînage anormaux.

### 2.3 Layer 3 — Retry / fallback / fail-safe

Quand un outil échoue ou retourne du garbage :
- Stratégie retry (combien de fois, avec quel backoff)
- Fallback déclenché (autre outil, autre modèle)
- Fail-safe activé (réponse standard, escalade humaine)

→ Sans tracking de ces patterns, tu ne sais pas combien d'utilisateurs reçoivent une réponse dégradée.

### 2.4 Layer 4 — Coût par session / utilisateur / jour

Tracking continu :
- Coût par session conversationnelle
- Coût par utilisateur (pour détecter abus ou usage massif inattendu)
- Coût agrégé par jour (pour anticiper la facture mensuelle)

→ Sans ce tracking : la facture mensuelle est une surprise.

### 2.5 Layer 5 — Satisfaction utilisateur (feedback explicite)

Pour chaque interaction :
- 👍/👎 utilisateur si possible
- Champ texte feedback
- Drop-off (l'utilisateur abandonne sans terminer)

→ Sans feedback, le drift qualité passe inaperçu.

## Section 3 — Les garde-fous obligatoires pour un agent en prod

### 3.1 Cap budgétaire (le plus critique)

Un agent en boucle infinie peut consommer **10 000 € en 24h** sur un compte Anthropic ou OpenAI. Cap obligatoire :
- **Cap par session** : max X € par session conversationnelle (ex : 0,50 €)
- **Cap par utilisateur** : max Y €/jour par utilisateur
- **Cap global jour** : max Z €/jour total — alerte sonore et arrêt automatique au dépassement

→ Sans ces 3 caps, c'est juste une question de temps avant l'incident.

### 3.2 Step-limit absolu

Tout agent doit avoir un **nombre maximum de steps** par session. Typiquement 10-20 steps. Au-delà, fail-safe vers une réponse standard ou escalade humaine.

→ Évite les boucles infinies (bug le plus fréquent en agents).

### 3.3 Retry avec backoff exponentiel

Quand un outil ou un modèle échoue : retry 3 fois max, avec backoff exponentiel (1s, 4s, 16s). Au-delà : fallback ou fail-safe.

→ Évite de saturer le modèle ou l'outil distant.

### 3.4 Fail-safe gracieux

En cas d'échec définitif : **ne jamais retourner une erreur technique brute** à l'utilisateur. Préparer une réponse standard du type : « Je n'arrive pas à traiter ta demande pour l'instant. Veux-tu que je l'escalade à un humain ? ».

### 3.5 Détection prompt injection

Tracker les patterns de prompt injection (cf. [DEP-08 Sécurité agents](dep-08-securite-agents-mcp.html)) :
- Tentatives de override du système prompt
- Tentatives d'extraction de données via prompt
- Patterns d'attaque connus (DAN, etc.)

→ Outil : guard rails open-source (NeMo Guardrails, Lakera Guard, Rebuff).

## Section 4 — Panorama outils 2026 par budget

### 4.1 Stack open-source self-hosted (gratuit ou faible coût hosting)

| Outil | Rôle | Coût |
|---|---|---|
| **Langfuse** | Observabilité LLM/agents complète | Gratuit OSS, hosting ~20-100 €/mois |
| **Phoenix Arize** | Tracing + eval LLM | Gratuit OSS |
| **NeMo Guardrails (Nvidia)** | Garde-fous prompt injection | Gratuit |
| **OpenInference** | Standard de tracing OSS | Gratuit |

### 4.2 Stack SaaS managed (plus rapide à déployer)

| Outil | Rôle | Coût typique PME |
|---|---|---|
| **Comet Opik** | Eval + observabilité LLM | Free tier puis ~50-200 €/mois |
| **LangSmith** | Observabilité LangChain | ~30-200 €/mois |
| **Helicone** | LLM gateway + monitoring | ~20-100 €/mois |
| **Lakera Guard** | Garde-fous sécurité | ~50-300 €/mois |

### 4.3 Recommandation pratique pour démarrer

Pour une PME qui démarre :
- **Langfuse self-hosted** + **NeMo Guardrails** (gratuit, contrôle, EU)
- Si manque de bandwidth ops : **Comet Opik free tier** + **Helicone free tier**

→ Setup possible en 1-2 semaines.

## Section 5 — KPI à monitorer en continu

### 5.1 KPI techniques

- **Latence p95, p99** : temps de réponse au 95e et 99e percentile
- **Taux d'échec** : % de sessions terminant sur fail-safe
- **Tokens consommés / session** : moyenne et médiane
- **Coût / session** : moyenne et médiane

### 5.2 KPI qualité

- **Score eval automatique** : sur dataset golden (50-200 cas)
- **Feedback explicite** : ratio 👍 / total
- **Drop-off rate** : % de sessions abandonnées avant complétion
- **Retry rate** : % de sessions avec retry déclenché

### 5.3 KPI sécurité

- **Prompt injections détectées** : nombre/jour
- **Anomalies de pattern** : sessions atypiques (volume, requêtes, accès)
- **Tool calls inhabituels** : agent qui appelle un outil rarement utilisé

### 5.4 KPI business

- **Sessions / jour**
- **Sessions par utilisateur / mois**
- **Taux de résolution sans escalade humaine** (pour agents support)

## Section 6 — DevOps vs MLOps vs LLMOps : les différences fondamentales

Beaucoup de PME tentent d'appliquer des pratiques DevOps à leurs agents IA. **C'est un piège.** Trois disciplines distinctes :

### 6.1 DevOps

- **Objet** : code logiciel
- **Cycle** : code → test → deploy → monitor
- **Critère succès** : code fonctionne comme spécifié
- **Reproductibilité** : 100 % (même input → même output)

### 6.2 MLOps

- **Objet** : modèles ML statistiques
- **Cycle** : data → train → evaluate → deploy → retrain
- **Critère succès** : modèle prédit avec qualité acceptable
- **Reproductibilité** : haute (même data + même algo → même modèle)

### 6.3 LLMOps

- **Objet** : agents LLM, prompts, RAG
- **Cycle** : prompt → eval → deploy → monitor → adjust prompt / RAG / model
- **Critère succès** : valeur métier (ROI, satisfaction utilisateur)
- **Reproductibilité** : faible (LLM intrinsèquement non déterministes)

→ Implication : les outils LLMOps (observabilité, eval, garde-fous) sont **différents** des outils DevOps. Ne pas tenter de tout faire avec Datadog ou Prometheus.

## Section 7 — Plan d'action 30 jours pour observabilité minimale

### Jours 1-7 — Setup observabilité minimale
- Choisir stack (Langfuse self-hosted ou Comet Opik free tier)
- Instrumenter chaque appel LLM et tool call
- Dashboard de base : latence, coût, taux d'échec

### Jours 8-15 — Garde-fous critiques
- Cap budgétaire 3 niveaux (session, utilisateur, jour)
- Step-limit absolu sur chaque agent
- Retry avec backoff exponentiel
- Fail-safe gracieux

### Jours 16-23 — Eval pipeline
- Construction dataset golden 50-100 cas
- Run eval automatique quotidienne
- Alerte si dégradation > 5 %

### Jours 24-30 — Monitoring sécurité
- Garde-fous prompt injection (NeMo Guardrails ou Lakera)
- Tracking anomalies pattern
- Procédure réponse incident

## Section 8 — Pour aller plus loin (Schéma A)

### Callout d'aiguillage

> Pour le panorama complet des outils observabilité et garde-fous LLM, retrouve les fiches détaillées sur la [page Ressources du Hub](../ressources.html#bibliographie).

### 📰 Articles de fond
- [LangChain — State of Agent Engineering 2026](https://blog.langchain.dev/) — Étude annuelle référence
- [Avi Chawla — Layers of observability in AI systems](https://blog.dailydoseofds.com/p/foundations-of-ai-engineering-and-0a6) — Pilier 8 LLM Engineering Roadmap
- [Anthropic Engineering — Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) — Patterns d'agents production-ready

### 🎓 Tutoriels & cas pratiques
- [Langfuse Docs](https://langfuse.com/docs) — Open-source tracing LLM/agents
- [Phoenix Arize](https://phoenix.arize.com/) — Eval + tracing OSS
- [Comet Opik](https://www.comet.com/site/products/opik/) — Évaluation et observabilité LLM

### 📚 Documentation officielle & études
- [NeMo Guardrails (Nvidia)](https://github.com/NVIDIA/NeMo-Guardrails) — Framework garde-fous open-source
- [LangSmith Docs](https://docs.smith.langchain.com/) — Référence observabilité LangChain
- [OpenInference](https://github.com/Arize-ai/openinference) — Standard de tracing OSS

### 👥 Communautés & veille
- [Anthropic Discord](https://www.anthropic.com/discord) — Échanges agents production
- [r/LocalLLaMA](https://reddit.com/r/LocalLLaMA) — Communauté LLM open-source

## Renvois internes pour Claude Code

- **Section 3.5** : lien `<a href="dep-08-securite-agents-mcp.html">DEP-08 Sécurité agents/MCP</a>`
- **Section 4** : lien `<a href="../ressources.html#bibliographie">page Ressources</a>`

## Composants visuels suggérés

- **Section 2** : diagramme SVG des 5 layers empilés (du plus bas au plus haut)
- **Section 4.1/4.2** : 2 `.tool-table` côte-à-côte (open-source vs SaaS)
- **Section 6** : tableau comparatif DevOps / MLOps / LLMOps en `.tool-table`
- **Section 7** : `.timeline-block` pour les 30 jours

## Note Cowork
Sources prioritaires : LangChain State of Agent Engineering 2026, Avi Chawla, Anthropic Engineering. Conforme RULES § 1.1.
