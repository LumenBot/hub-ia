# Lot C v3.9 — Patches DEP-03 (Harness engineering) + DEP-04 (Fine-tuning SLM)

**Brief consolidé pour Claude Code** : 2 enrichissements éditoriaux ciblés sur des modules existants. Patches courts, structurellement légers (1 nouvelle sous-section par module).

**Sources** : veille `pistes-cumulatives.md` run 2026-05-12 (akshay_pachaar + Anthropic Engineering pour DEP-03 ; cjzafir + tendance ELMs pour DEP-04).

---

## Patch C.1 — DEP-03 (Context engineering & coûts) — concept harness engineering

**Module cible** : `deploiement/dep-03-context-engineering-couts.html`
**Position** : insérer **après** la section 3 « Gestion du contexte » et **avant** la section 4 « Choix de modèle stratégique ».
**Anchor id** : `section-3bis`
**Icône TOC** : 🎛️
**Label TOC** : « Du context au harness »

### Contenu à intégrer

#### 1. Le shift conceptuel 2026 — vers le « harness engineering »

Le **prompt engineering** (2023-2024) a centré l'attention sur la formulation des instructions. Le **context engineering** (2025-2026, traité dans les sections précédentes) a élargi le périmètre à la gestion du contexte injecté dans le modèle. **Mai 2026 marque un nouveau palier** : l'émergence du **harness engineering** comme discipline englobante.

> Le harness, c'est tout ce qui entoure l'appel LLM : orchestration, tools, loops, guardrails, observabilité, fallback. Le prompt n'est plus qu'un composant parmi d'autres.

Le terme s'impose dans la communauté builders (concept formalisé notamment par @akshay_pachaar et Anthropic Engineering en mai 2026, publication « Effective harnesses for long-running agents »). Le shift est **stratégique** : on ne réfléchit plus en termes de « comment je formule mon prompt ? » mais en termes de **« quel est le système d'exécution qui rend mon agent fiable, économique et observable sur la durée ? »**.

#### 2. Checklist opérationnelle PME — les 8 leviers du harness

Une PME qui industrialise un agent ou un pipeline IA doit formaliser **8 leviers** :

| # | Levier | Question opérationnelle |
|---|---|---|
| 1 | **Prompt caching vs semantic caching** | Quels prompts ré-utilise-t-on tel quel (caching exact) ? Quels appels acceptent une similarité sémantique (caching approximé) ? |
| 2 | **KV cache à l'échelle** | Est-ce que la stack supporte le KV cache pour les conversations longues ? Quel impact sur la latence ? |
| 3 | **Speculative decoding vs quantization** | Pour réduire la latence : un petit modèle qui propose et un gros qui valide (speculative) ? Ou un gros modèle quantifié (8 bits, 4 bits) ? |
| 4 | **LLM-as-judge + human evals** | Quels critères sont évalués par un LLM juge (cohérence, format, factualité) ? Quels critères restent sur évaluation humaine (jugement métier, ton, conformité) ? |
| 5 | **Cost attribution par feature** | Combien coûte chaque feature produit par mois ? Par utilisateur ? Par requête ? |
| 6 | **Agent guardrails & loop budgets** | Combien de tools un agent peut-il appeler avant escalade ? Combien de tokens max par session ? Quels patterns d'output sont interdits ? |
| 7 | **Model routing** | Quel modèle traite quel type de requête ? Sur quels critères ? (coût, latence, qualité, sensibilité) |
| 8 | **Graceful fallback** | Que se passe-t-il quand le modèle principal est indisponible ou répond mal ? Y a-t-il un fallback testé ? |

**Implication pour la PME** : ces 8 leviers ne sont **pas** à mettre en place tous d'un coup. Mais ils doivent être **listés et arbitrés** dès que l'agent passe en production. Une PME qui n'a pas tranché sur ces 8 questions opère « au feeling » — ce qui marche en POC, pas en production.

#### 3. Lien avec le pattern Code Execution with MCP

L'un des patterns les plus efficaces du harness 2026 est le **Code Execution with MCP** publié par Anthropic Engineering. Il s'agit de transformer l'agent en exécuteur de code Python qui appelle les MCP tools localement, traite les données dans le sandbox, et ne renvoie au modèle que les données strictement nécessaires.

> Bénéfice mesuré : **réduction de 60-80 % de la consommation de tokens** sur les workflows longs (15+ steps), avec amélioration de la latence à la clé.

Pattern documenté en détail dans **DEP-05 §8.3 (Production-grade : Code Execution with MCP)**. À considérer comme **brique d'optimisation du levier 6** (loop budgets) et du levier 5 (cost attribution).

---

### Sources à ajouter dans la section finale (sous-rubrique 📰 Articles de fond)

À insérer dans la section `#ressources` :
- **Compte X @akshay_pachaar** — thread harness engineering (mai 2026, 2 233 likes)
- **Anthropic Engineering** — « Effective harnesses for long-running agents » (anthropic.com/engineering/effective-harnesses-for-long-running-agents, mai 2026)

### Mise à jour TOC du module

Ajouter dans le sommaire entre l'entrée « Gestion du contexte » et l'entrée « Choix de modèle stratégique » :

```html
<li><a href="#section-3bis"><span class="toc-icon">🎛️</span>Du context au harness</a></li>
```

### Renvois internes à mettre à jour dans DEP-03

- En executive summary : ajouter une mention « Le harness engineering est l'évolution naturelle du context engineering — voir section 3bis. »
- En section 6 (Plan d'action 30 jours) : intégrer la checklist 8 leviers comme **étape 4 du plan d'action** ou en encart de synthèse.

### Renvois croisés

- Renvoi vers **DEP-05 §8.3 (Code Execution with MCP)** depuis section 3bis (déjà intégré).
- Renvoi vers **DEP-05 §8.1 (9-layer architecture)** comme « cartographie macro complémentaire au harness ».
- Renvoi depuis CU-008 (Knowledge base RAG) en encart léger : « Pour gérer le coût d'un RAG en production, voir DEP-03 §3bis. »

### Métadonnées module

- `<meta name="description">` : à actualiser pour mentionner le harness. Suggestion : *« Du prompt engineering au harness engineering : les 8 leviers opérationnels pour qu'un agent IA tienne en production sans dériver en coût ni en qualité. »*
- Badge temps de lecture : passer à **+3 min** (estimation +3 min pour section 3bis).

---

## Patch C.2 — DEP-04 (Fine-tuning PME) — guide pratique SLM 1B-8B + signal faible ELMs

**Module cible** : `deploiement/dep-04-fine-tuning-pme.html`
**Position** : insérer **après** la section 4 « LoRA et QLoRA en pratique » et **avant** la section 5 « La discipline data ».
**Anchor id** : `section-4bis`
**Icône TOC** : 🧪
**Label TOC** : « SLM 1B-8B en 2026 »

### Contenu à intégrer

#### 1. Le palier opérationnel 2026 — fine-tuner avant 27B

En 2025, le discours dominant sur le fine-tuning était : « si vous avez moins de 50K exemples de qualité, n'y allez pas ». En 2026, ce discours évolue avec l'émergence d'un palier intermédiaire **réellement accessible aux PME** : le fine-tuning de **petits modèles (SLM, 1B-8B paramètres)** avant d'envisager les modèles 27B+ ou les frontier models.

**Heuristique opérationnelle 2026** (formalisée notamment par @cjzafir, mai 2026, 1 875 likes) :

> **Ne pas acheter de GPU avant d'avoir fine-tuné 7-10 modèles SLM avec succès.**

L'intuition : avant d'investir 5-15 K€ dans une carte GPU, l'équipe doit **avoir prouvé sa capacité** à itérer sur un fine-tuning et à mesurer un gain réel. Sinon, le GPU dort dans un placard et la dette technique s'installe.

#### 2. La stack pratique 2026 pour fine-tuner sans GPU local

| Brique | Outil recommandé | Coût |
|---|---|---|
| **Compute** | Colab Pro / WebGPU / A100 cloud à la demande | ~0,60 $/h sur A100 |
| **Modèles instruct + notebooks** | Unsloth (huggingface.co/unsloth) | Gratuit, open-source |
| **Méthode SFT** | Supervised Fine-Tuning sur dataset propre | Coût compute uniquement |
| **Méthodes RL** | GRPO / DPO / PPO selon objectif | Coût compute uniquement |
| **Adaptation paramétrique** | LoRA / QLoRA (déjà couvert section 4) | Économie de RAM ×4 |
| **Quantization** | 8 bits, 4 bits, GPTQ, AWQ | Réduction taille ×2 à ×4 |
| **Inférence locale** | llama.cpp (CPU + GPU léger) | Gratuit, déploiement on-prem |
| **Optimisation contexte** | KV cache + prompt cache | Économie tokens 30-50 % |

**Lecture pour la PME** : un cycle complet (collecte data → SFT → eval → déploiement local) sur un modèle 7B est faisable en **4-6 semaines** avec un junior data scientist + 200-500 € de compute cloud. C'est l'ordre de grandeur qui rend le fine-tuning **réellement éligible** au plan IA d'une PME en 2026.

#### 3. Le ROI métier observé

Données de marché 2026 : **les entreprises paient 50 K€+ pour des modèles personnalisés sur leurs données** (sources : annonces sociétés de services IA spécialisées, mai 2026). Cette valorisation reflète :

- L'absence d'alternative équivalente côté SaaS (pas de fine-tuning Claude / GPT-4 à 100 K exemples métier dans la plupart des cas)
- La valeur du **on-premise** (souveraineté, confidentialité, RGPD)
- La pérennité (le modèle fine-tuné devient un actif de l'entreprise, pas un abonnement)

**Implication stratégique** : pour une PME qui a 6-12 mois d'historique IA et un cas d'usage métier mature, internaliser une compétence de fine-tuning SLM peut représenter un **ROI direct supérieur à un abonnement SaaS sur 18 mois**. La condition : avoir validé le cas d'usage **avant** d'investir dans le fine-tuning.

#### 4. Encart prospectif — l'émergence des « Expert Language Models » (ELMs)

> ⚠️ **Signal faible 2026 à surveiller** : un déplacement progressif du marché des « frontier models 1T+ paramètres » vers des **Expert Language Models (ELMs)** de 5-15B paramètres, fine-tunés sur des données métier. Hypothèse : la prochaine vague de différenciation IA en entreprise ne viendra pas de qui a accès au plus gros modèle, mais de qui maîtrise **son propre modèle spécialisé**.
>
> Implication PME : si cette tendance se confirme dans 12-18 mois, la stack 2027 PME pourrait être **SLM/ELM on-premise + privacy-first** plutôt que SaaS frontier. À surveiller.

---

### Sources à ajouter dans la section finale (sous-rubrique 📰 Articles de fond)

À insérer dans la section `#ressources` :
- **Compte X @cjzafir** — guide pratique fine-tuning SLM 1B-8B + heuristique 7-10 modèles avant GPU (mai 2026, 1 875 likes, 226 RT)

### Mise à jour TOC du module

Ajouter dans le sommaire entre l'entrée « LoRA et QLoRA en pratique » et l'entrée « La discipline data » :

```html
<li><a href="#section-4bis"><span class="toc-icon">🧪</span>SLM 1B-8B en 2026</a></li>
```

### Renvois internes à mettre à jour dans DEP-04

- En executive summary : ajouter une mention « Le palier opérationnel 2026, c'est le fine-tuning de SLM 1B-8B sur compute cloud — voir section 4bis. »
- En section 6 (Plan d'action 60 jours) : intégrer la séquence « 7-10 SLM fine-tunés avant tout investissement GPU » comme **règle de discipline budgétaire**.

### Renvois croisés

- Renvoi depuis **PR-07** (Build vs Buy) : « Une troisième voie en 2026 — le fine-tuning SLM, voir DEP-04 §4bis. »
- Renvoi depuis **DEP-05 §8.1 (9-layer)** : couche 5 (router) peut router vers un SLM fine-tuné pour les cas d'usage spécialisés.

### Métadonnées module

- `<meta name="description">` : à actualiser pour mentionner SLM. Suggestion : *« Le fine-tuning de SLM 1B-8B est le palier opérationnel 2026 pour les PME — guide pratique stack et heuristiques. »*
- Badge temps de lecture : passer à **+4 min** (estimation +4 min pour section 4bis).
