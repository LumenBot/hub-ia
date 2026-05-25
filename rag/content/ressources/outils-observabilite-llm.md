---
code: outils-observabilite-llm
titre: "Outils — Observabilité LLM"
type: fiche-outil
axe: transverse
niveau: 3
tags: [observabilite, llm, langfuse, langsmith, comet-opik, phoenix-arize, helicone, traces, evals, monitoring]
version: 3.12.0
last_updated: 2026-05-25
glosaire_termes: [llm, agent, rag, prompt]
derives: ["[[pr-05]]", "[[pr-10]]", "[[dep-02]]", "[[dep-05]]", "[[dep-07]]", "[[outils-llm]]", "[[outils-frameworks-rag]]", "[[pattern-souverainete-eu]]"]
public_cible: [ops, r&d, tech]
---

# Outils — Observabilité LLM

## Quand utiliser un outil d'observabilité LLM

Un outil d'**observabilité LLM** trace, mesure et alerte sur les appels LLM dans une application en production. Il capture les **traces** (séquence d'appels LLM avec entrées/sorties), les **métriques** (latence, coût, taux d'erreur), les **évaluations** (qualité réponses, taux d'hallucination), et permet le **debugging** post-incident. C'est l'équivalent LLM des outils APM/observabilité classiques (Datadog, New Relic), mais avec des spécificités IA : sourçage des réponses, évaluation qualité automatisée (LLM-as-judge), suivi des prompts versions.

Indispensable en production pour respecter la discipline [[pr-10]] (vérifier et limiter les hallucinations IA) et opérationnaliser les patterns de [[dep-05]] (Agents en production : observabilité et garde-fous) + [[dep-07]] (Évaluation continue et qualité IA).

5 outils de référence marché 2026 : **Langfuse** (open-source EU souverain), **LangSmith** (LangChain native, SaaS payant), **Comet Opik** (open-source alternative), **Phoenix Arize** (open-source focus eval), **Helicone** (gateway + observabilité).

> **Note S2.7** : la catégorie HTML `cat-observabilite-llm` est en cours de création côté Hub IA couple 1 (sondage léger). Cette fiche MD est produite anticipativement pour amorcer la couche RAG ; l'intégration HTML se fera en prochaine itération éditoriale.

## Langfuse — référence open-source EU souveraine

Langfuse (DE, open-source MIT) est la **référence observabilité LLM open-source et souveraine EU**. Combo : self-hosting facile (Docker Compose), interface complète (traces + sessions + prompts versioning + évaluations + alertes), SDKs Python/JS/TS, intégration native LangChain/LlamaIndex/OpenAI/Anthropic, communauté active.

**Quand l'utiliser** : observabilité LLM production avec exigence souveraineté EU (cf. [[pattern-souverainete-eu]] niveau Strong), self-hosting EU contrôlé, stack open-source intégrée, budget contrôlé (gratuit self-host).

**Quand ne pas l'utiliser** : équipe sans capacité DevOps pour self-host (préférer Langfuse Cloud SaaS), exigence d'intégration immédiate sans setup (LangSmith plus plug-and-play si déjà LangChain).

**Modèle économique** : **open-source gratuit (MIT, self-hosting illimité)** · **Langfuse Cloud free tier 50 K observations/mois** · **Pro 59 $/mois** (500 K observations) · **Team 199 $/mois** · Enterprise sur devis. Souveraineté niveau **Strong** (DE open-source, self-hosting EU).

**Cas d'usage Hub** : [[dep-05]] (Agents en production : observabilité), [[dep-07]] (Évaluation continue), [[pr-10]] (Vérifier hallucinations IA, outillage de mesure), [[pattern-souverainete-eu]] (acteur de référence souverain).

**Lien** : langfuse.com / github.com/langfuse/langfuse

## LangSmith (LangChain) — référence SaaS LangChain native

LangSmith est l'**outil observabilité native LangChain** par l'éditeur LangChain. Combo : intégration zéro effort si stack LangChain (auto-instrumentation), interface mature (traces hiérarchiques, datasets d'éval, prompt playground), équipe support qualité, écosystème LangChain dense.

**Quand l'utiliser** : stack LangChain en production avec besoin d'observabilité immédiate, équipe LangChain expérimentée, exigence d'intégration plug-and-play.

**Quand ne pas l'utiliser** : stack non-LangChain (intégration possible mais moins fluide), exigence souveraineté EU stricte (US-based, niveau Light), budget restreint pour usages volumineux.

**Modèle économique** : Free tier 5 K traces/mois (1 dev) · **Plus 39 $/dev/mois** (100 K traces) · Enterprise sur devis. Souveraineté niveau **Light** (US).

**Cas d'usage Hub** : [[dep-05]] (Agents en production : observabilité LangChain), [[dep-07]] (Évaluation continue avec datasets LangSmith), équipes utilisant LangChain en production.

**Lien** : smith.langchain.com / docs.smith.langchain.com

## Comet Opik — open-source alternative

Comet Opik est une **alternative open-source à LangSmith** par Comet (acteur ML observability historique). Combo : SDK Python simple, intégration LLM-agnostique (OpenAI, Anthropic, LangChain, LlamaIndex), focus eval (datasets, métriques personnalisées, LLM-as-judge), self-hostable ou Comet Cloud.

**Quand l'utiliser** : alternative open-source à LangSmith sans lock-in LangChain, équipe avec stack ML existante Comet, focus évaluations LLM-as-judge.

**Quand ne pas l'utiliser** : exigence d'écosystème LangChain natif (LangSmith plus intégré), équipe sans capacité DevOps pour self-host (Comet Cloud disponible mais payant).

**Modèle économique** : **open-source gratuit (Apache 2.0, self-hosting)** · **Comet Cloud free tier** · **Pro / Enterprise sur devis**. Souveraineté niveau **Strong** (open-source self-hostable).

**Cas d'usage Hub** : [[dep-05]] (Agents en production : alternative open-source), [[dep-07]] (Évaluation continue avec LLM-as-judge), équipes hybrides ML traditionnel + LLM.

**Lien** : comet.com/site/products/opik / github.com/comet-ml/opik

## Phoenix Arize — open-source focus eval

Phoenix (Arize AI) est l'**outil open-source focus évaluation et debugging LLM**. Combo : SDK Python intégré OpenTelemetry, interface notebook-first (Jupyter-friendly), focus évaluations qualité (sourçage, hallucinations, RAG retrieval quality), open-source MIT.

**Quand l'utiliser** : équipe data science / ML avec workflow Jupyter, focus évaluation RAG et qualité retrieval, intégration OpenTelemetry (stack observabilité existante), self-hosting open-source.

**Quand ne pas l'utiliser** : équipe sans workflow Jupyter (interface dédiée moins riche), production temps réel critique (focus eval plutôt que monitoring runtime).

**Modèle économique** : **open-source gratuit (MIT)** · **Arize AI Cloud** (offre commerciale ML observability étendue, sur devis). Souveraineté niveau **Strong** (open-source self-hostable).

**Cas d'usage Hub** : [[dep-07]] (Évaluation continue, focus eval RAG retrieval quality), équipes data science avec workflow Jupyter, debugging post-incident.

**Lien** : phoenix.arize.com / github.com/Arize-ai/phoenix

## Helicone — gateway + observabilité

Helicone est un **gateway LLM + observabilité** : il s'insère comme proxy devant l'API LLM (1 ligne de code change) et capture automatiquement toutes les requêtes. Combo : setup ultra-rapide (proxy URL), caching automatique (réduction coût), rate limiting, observabilité standard (traces, métriques, coûts).

**Quand l'utiliser** : besoin observabilité ultra-rapide à mettre en place (gateway proxy), réduction coût par caching automatique, rate limiting partagé multi-équipes, alternative simple à LangSmith.

**Quand ne pas l'utiliser** : pas de tolérance à un proxy supplémentaire dans le chemin (latence +10-30 ms), exigence d'intégration profonde avec framework (LangSmith plus natif pour LangChain).

**Modèle économique** : Free tier 10 K logs/mois · **Pro 25 $/mois** (1 M logs) · **Team 50 $/mois** · Enterprise sur devis · **Self-hosting open-source disponible**. Souveraineté niveau **Moderate** (open-source self-hostable + SaaS US).

**Cas d'usage Hub** : [[dep-05]] (Agents en production : observabilité gateway), équipes multi-LLM avec besoin de centraliser logs + caching, prototypes rapides.

**Lien** : helicone.ai

## Comparatif synthétique

| Outil | Type | Souveraineté | Tarif | Cas Hub principal |
|---|---|---|---|---|
| **Langfuse** | Open-source EU + Cloud | Strong (DE) | Gratuit / 59 $/mois | Observabilité souveraine EU |
| **LangSmith** | SaaS LangChain native | Light (US) | 39 $/dev/mois | Stack LangChain production |
| **Comet Opik** | Open-source alternative | Strong (open-source) | Gratuit / Cloud sur devis | Eval LLM-as-judge |
| **Phoenix Arize** | Open-source focus eval | Strong (open-source) | Gratuit | Eval RAG retrieval qualité |
| **Helicone** | Gateway + observabilité | Moderate (open-source + US) | Gratuit / 25 $/mois | Setup rapide + caching |

## Recommandations PME par profil

**PME tech avec stack LangChain en production** : LangSmith pour démarrer (intégration zéro effort) + Langfuse self-hosted EU pour migrer si souveraineté devient critique. Budget : 39 $/dev/mois LangSmith ou gratuit Langfuse.

**PME EU avec exigence souveraineté forte** : Langfuse self-hosted EU (gratuit, niveau Strong cf. [[pattern-souverainete-eu]]) + Phoenix Arize pour les évaluations spécifiques RAG.

**PME focus économie coût LLM** : Helicone gateway (caching automatique réduit 20-40 % le coût LLM sur usages répétitifs) + Langfuse Cloud free tier pour observabilité de base.

**Équipe data science / ML** : Phoenix Arize (workflow Jupyter natif) + Comet Opik si stack Comet existante.

## Pour aller plus loin

- **Agents en production : observabilité** ([[dep-05]]) : 5 layers d'observabilité agents, patterns industriels
- **Évaluation continue et qualité IA** ([[dep-07]]) : golden set, LLM-as-judge, métriques
- **Vérifier et limiter les hallucinations IA** ([[pr-10]]) : discipline managériale, outils de mesure
- **Sécurité IA cadrage stratégique** ([[pr-05]]) : observabilité dans le cadre sécurité PME
- **RAG en production** ([[dep-02]]) : intégration observabilité dans pipeline RAG
- **Pattern souveraineté EU** ([[pattern-souverainete-eu]]) : Langfuse comme acteur de référence
- **Frameworks RAG** ([[outils-frameworks-rag]]) : intégration LangSmith ↔ LangChain
