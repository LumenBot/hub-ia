---
code: outils-workflow-automation
titre: "Outils — Workflow automation et orchestration agents"
type: fiche-outil
axe: transverse
niveau: 3
tags: [workflow-automation, orchestration, n8n, make, dify, flowise, composio, aaflow, beever-atlas, agents, no-code]
version: 3.12.0
last_updated: 2026-05-25
glosaire_termes: [agent, llm, rag, mcp]
derives: ["[[cu-013]]", "[[cu-015]]", "[[cu-022]]", "[[cu-023]]", "[[dep-05]]", "[[outils-llm]]", "[[outils-frameworks-rag]]", "[[pattern-souverainete-eu]]"]
public_cible: [ops, r&d, tech]
---

# Outils — Workflow automation et orchestration agents

## Quand utiliser un outil de workflow automation

Un outil de **workflow automation** (ou **orchestration agents**) permet de connecter des applications (CRM, email, ERP, base de données, LLM, agents) pour automatiser des séquences d'actions. Les outils 2026 intègrent nativement les capacités IA ([[glossaire#llm]] dans les nœuds de workflow, [[glossaire#agent]] orchestrés via des protocoles type [[glossaire#mcp]]).

Le marché 2026 catégorise ces outils en **deux familles complémentaires** :

1. **Workflow no-code/low-code classique** : connecte applications par triggers + actions (n8n, Make, Zapier) — usage métier non-tech.
2. **Orchestration agents IA** : connecte LLM + tools + RAG dans des workflows agentiques (Dify, Flowise, Composio, AAFLOW, Beever Atlas) — usage hybride tech + métier.

6 outils de référence catégorie HTML cat-orchestration : **n8n** (open-source self-hostable), **Make** (SaaS no-code), **Dify** (plateforme RAG + workflows), **Flowise** (visuel low-code orchestration), **Composio** (open-source agents tools), **AAFLOW** (workflow agentique), **Beever Atlas** (KM souverain FR + orchestration).

À sonder couple 1 : **Zapier** (référence historique marché, présence HTML à confirmer — non inclus dans cette fiche en l'absence de vérification HTML).

## n8n — référence open-source workflow automation

n8n (DE, open-source) est la **référence workflow automation open-source** marché 2026. Combo : 400+ intégrations natives, self-hosting facile (Docker), Sustainable Use License (gratuit usage interne), interface visuelle moderne, support IA natif (nœuds LLM Claude/GPT/Mistral + agents + outils).

**Quand l'utiliser** : workflow automation production avec exigence souveraineté EU (cf. [[pattern-souverainete-eu]] niveau Strong), self-hosting EU, alternative open-source à Make/Zapier, équipe technique capable d'opérer un Docker.

**Quand ne pas l'utiliser** : équipe non-tech sans capacité d'opérer un self-host (préférer Make ou n8n Cloud), exigence d'intégrations très spécialisées non-couvertes par n8n (préférer Make ou Zapier pour le catalogue tiers).

**Modèle économique** : **self-hosted gratuit (Sustainable Use License pour usage interne)** · **n8n Cloud free tier** (5 workflows actifs, 1 K exécutions/mois) · **Starter ~20 €/mois** · **Pro ~50 €/mois** · Enterprise sur devis. Souveraineté niveau **Strong** (DE, open-source self-hostable EU).

**Cas d'usage Hub** : [[cu-013]] (Workflow email-CRM), [[cu-015]] (Asynchronicité agentique Stripe Minions), [[cu-022]] (Voicebot accueil téléphonique — workflow inbound), [[pattern-souverainete-eu]] (acteur de référence).

**Lien** : n8n.io / docs.n8n.io

## Make (ex-Integromat) — référence SaaS no-code

Make est la **référence SaaS no-code** marché 2026. Combo : 1 500+ intégrations natives (plus large catalogue tiers), interface visuelle aboutie (scenarios drag-and-drop), tarification accessible PME, nœuds IA récents (OpenAI, Claude, Anthropic, Mistral).

**Quand l'utiliser** : workflow automation production sans capacité DevOps, intégrations tierces très larges (CRM, ERP, marketing, paiement), équipe métier non-tech autonome.

**Quand ne pas l'utiliser** : souveraineté EU stricte (cloud cz/US selon configuration, niveau Light à Moderate), self-hosting requis (préférer n8n), volumes massifs avec coût dérapant.

**Modèle économique** : **Free tier 1 000 ops/mois** (2 scenarios actifs) · **Core 9 €/mois** (10 K ops) · **Pro 16 €/mois** (10 K ops + features avancées) · **Teams 29 €/mois** (multi-utilisateurs) · Enterprise sur devis. Souveraineté niveau **Light à Moderate** (CZ/US selon configuration).

**Cas d'usage Hub** : [[cu-013]] (Workflow email-CRM, alternative SaaS), [[cu-023]] (Devis simples — porte d'entrée IA, automation commerciale).

**Lien** : make.com

## Dify — plateforme RAG + agents low-code

Dify est une **plateforme no-code/low-code** intégrée : construction d'apps RAG, agents conversationnels, workflows multi-étapes, déploiement web/API. Combo : interface visuelle complète, RAG intégré (vector store + retrieval inclus), nœuds LLM multi-providers, déploiement clé en main.

**Quand l'utiliser** : prototype rapide app IA avec UI (chatbot, assistant), RAG no-code sans installer LangChain, équipe mixte tech + métier, démo ou MVP, déploiement self-hosted EU.

**Quand ne pas l'utiliser** : workflows automation classiques sans IA (préférer n8n/Make), production grand volume avec besoin de contrôle fin (préférer LangChain Python).

**Modèle économique** : **Self-hosted gratuit (open-source)** · **Dify Cloud Sandbox gratuit** · **Professional 59 $/mois** · **Team 159 $/mois** · Enterprise sur devis. Souveraineté niveau **Strong** (open-source self-hostable EU).

**Cas d'usage Hub** : [[cu-013]] (Workflow email-CRM avec RAG conversationnel), [[cu-027]] (Faire développer une appli métier sans être IT, alternative low-code), [[outils-frameworks-rag]] (alternative low-code à LangChain/LlamaIndex).

**Lien** : dify.ai

## Flowise — orchestration visuelle low-code

Flowise est l'**équivalent low-code visuel** pour construire des chaînes LangChain et des agents. Combo : interface visuelle drag-and-drop, génération chaînes LangChain sous-jacentes, marketplace de templates, déploiement self-hosted ou cloud.

**Quand l'utiliser** : prototypage visuel chaînes LangChain (cf. [[outils-frameworks-rag]]), génération de code Python LangChain pour reprise dev, équipe mixte tech + non-tech, démos.

**Quand ne pas l'utiliser** : production critique avec contrôle fin (LangChain code direct préférable), workflows automation non-IA (préférer n8n/Make).

**Modèle économique** : **Self-hosted gratuit (open-source MIT)** · **Flowise Cloud freemium** puis variable. Souveraineté niveau **Strong** (open-source self-hostable EU).

**Cas d'usage Hub** : [[cu-027]] (Faire développer une appli métier sans être IT, alternative visuelle), [[outils-frameworks-rag]] (alternative visuelle low-code).

**Lien** : flowiseai.com

## Composio — open-source tools pour agents

Composio est une **plateforme open-source de tools pour agents IA** : 250+ intégrations pré-cablées (Gmail, Slack, GitHub, Jira, Notion, etc.) directement consommables par les agents Claude/GPT via leur SDK. Combo : alternative aux MCP servers customs, intégrations testées, gestion des permissions et auth.

**Quand l'utiliser** : agents IA en production avec besoin d'accès à des outils tiers (Gmail, Slack, GitHub, etc.), alternative à coder soi-même les MCP servers, équipe Python.

**Quand ne pas l'utiliser** : besoin de tools très spécialisés non-couverts (préférer MCP custom), exigence d'auditer chaque intégration (préférer self-hosted MCP).

**Modèle économique** : **Open-source gratuit (Elastic License v2)** · **Composio Cloud freemium** puis variable selon usage. Souveraineté niveau **Strong** (open-source self-hostable).

**Cas d'usage Hub** : [[cu-014]] (Multi-agents par fonction — agents avec tools tiers), [[cu-015]] (Asynchronicité agentique), [[dep-05]] (Agents en production : outils intégrés sécurisés), [[dep-08]] (Sécurité MCP servers — alternative).

**Lien** : composio.dev / github.com/ComposioHQ/composio

## AAFLOW — workflow agentique

AAFLOW est un **framework de workflow agentique** mentionné dans les patches DEP-05 v3.8 du Hub. Spécialisé dans la composition agents + outils + checks runtime. À documenter plus précisément au fil des productions du Hub.

**Quand l'utiliser** : workflows agentiques avec besoin de garde-fous runtime intégrés (alignement [[dep-05]] §8 patterns industriels), équipe Python.

**Quand ne pas l'utiliser** : workflows automation classiques sans agents (préférer n8n/Make).

**Modèle économique** : à confirmer (probablement open-source + SaaS). Souveraineté niveau à qualifier.

**Cas d'usage Hub** : [[dep-05]] (Agents en production : observabilité et garde-fous), [[cu-015]] (Asynchronicité agentique).

**Lien** : à confirmer (référence patches Hub DEP-05 v3.8).

## Beever Atlas — knowledge management + orchestration souverain FR

Beever Atlas est une **plateforme souveraine FR** combinant knowledge management + orchestration agents + RAG. Catégorisé cat-orchestration HTML (positionnement principal = workflows agentiques en environnement souverain). Combo : éditeur FR, hébergement EU, intégration RAG native, orchestration agents multi-étapes, focus PME ETI EU.

**Quand l'utiliser** : souveraineté EU forte (cf. [[pattern-souverainete-eu]] niveau Strong), démarche de soutien écosystème FR, plateforme intégrée KM + workflows, alternative aux stacks fragmentées US.

**Quand ne pas l'utiliser** : besoin d'écosystème mature très large (Beever Atlas plus récent, moins d'intégrations tierces que Make), équipe préférant des outils best-of-breed séparés.

**Modèle économique** : Tarification PME / ETI sur devis (vérifier auprès de l'éditeur). Souveraineté niveau **Strong** (FR, hébergement EU).

**Cas d'usage Hub** : [[cu-013]] (Workflow email-CRM souverain), [[cu-015]] (Asynchronicité agentique souveraine), [[pattern-souverainete-eu]] (acteur de référence), [[outils-knowledge-management]] (alternative orchestration souveraine).

**Lien** : beeveratlas.com

## Comparatif synthétique

| Outil | Type | Souveraineté | Tarif | Cas Hub principal |
|---|---|---|---|---|
| **n8n** | Workflow open-source | Strong (DE) | Gratuit (self) / 20-50 €/mois | Workflow souverain self-hosted |
| **Make** | Workflow SaaS no-code | Light à Moderate (CZ/US) | 9-29 €/mois | Workflow no-code intégrations larges |
| **Dify** | Plateforme RAG + agents low-code | Strong (open-source) | Gratuit (self) / 59-159 $/mois | Apps IA no-code prototype + prod |
| **Flowise** | Orchestration visuelle LangChain | Strong (open-source) | Gratuit (self) / freemium | Visuel low-code LangChain |
| **Composio** | Tools open-source pour agents | Strong (open-source) | Gratuit (self) / freemium | Intégrations agents tools tiers |
| **AAFLOW** | Workflow agentique | À qualifier | À confirmer | Garde-fous runtime agents |
| **Beever Atlas** | KM + orchestration souverain FR | Strong (FR) | Sur devis PME/ETI | Plateforme intégrée souveraine |

## Recommandations PME par profil

**PME 5-15 salariés workflow simple non-tech** : Make (9-29 €/mois selon volume) pour démarrer + nœuds IA Claude/GPT intégrés. Niveau Light à Moderate.

**PME 15-50 salariés tech-friendly avec souveraineté** : n8n self-hosted EU (gratuit) + nœuds LLM Mistral / Mixtral (cf. [[outils-llm]]) = stack workflow souveraine niveau Strong. Budget infrastructure ~50-150 €/mois.

**PME tech avec besoin app IA RAG no-code rapide** : Dify self-hosted EU pour prototypage et MVP + Mistral / Le Chat Pro pour le LLM (cf. [[outils-llm]]). Niveau Strong.

**PME souveraineté forte FR (cible démarche d'État, santé, défense)** : Beever Atlas + Pleias-RAG (cf. [[outils-llm]]) + n8n self-hosted = stack pleinement souveraine FR.

**PME tech avec agents IA en production** : Composio pour intégrations tools tiers + LangChain (cf. [[outils-frameworks-rag]]) + Langfuse pour observabilité (cf. [[outils-observabilite-llm]]).

## Pour aller plus loin

- **Workflow email-CRM** ([[cu-013]]) : cas d'usage canonique workflow automation IA-augmenté
- **Asynchronicité agentique** ([[cu-015]]) : cas Stripe Minions
- **Agents en production : observabilité** ([[dep-05]]) : garde-fous runtime agents
- **Frameworks RAG** ([[outils-frameworks-rag]]) : LangChain/LlamaIndex/Haystack pour le RAG Python pur
- **Modèles LLM** ([[outils-llm]]) : choix du LLM dans les nœuds workflow
- **Knowledge management** ([[outils-knowledge-management]]) : alternative orchestration souveraine via Beever Atlas
- **Pattern souveraineté EU** ([[pattern-souverainete-eu]]) : n8n, Composio, Beever Atlas comme acteurs souverains

---

> **Note S2.7** : Zapier (référence historique du marché workflow no-code) non vérifié HTML cat-orchestration au moment de la production. Sondage léger à transmettre couple 1 pour ajout HTML si confirmé pertinent. Patch incrémental MD prévu vague 8 si validation.
