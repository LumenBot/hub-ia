---
code: dep-05
titre: "Agents en production : observabilité et garde-fous"
type: deploiement-dep
axe: B
niveau: 4
tags: [agents, observabilite, production, garde-fous, langsmith, comet-opik, langfuse, failure-receipt, effective-harness, two-agent, anthropic, llmops]
version: 3.11.0
last_updated: 2026-05-22
glosaire_termes: [agent, llm, mcp, rag]
derives: ["[[cu-008]]", "[[cu-014]]", "[[cu-026]]", "[[cu-027]]", "[[dep-01]]", "[[dep-02]]", "[[dep-03]]", "[[dep-07]]", "[[dep-08]]", "[[pattern-persistent-memory]]", "[[vigilance-hallucinations]]"]
public_cible: [tech, r&d, ops]
---

# Agents en production : observabilité et garde-fous

## L'essentiel à retenir

**Comment opérer des agents IA en production en 2026 : observabilité 5 layers (logs, traces, métriques, événements, prompts/réponses) + garde-fous techniques + 4 patterns industriels 2026 (9-layer production architecture / gates machine-checkable TOML / Code Execution with MCP / Agent Skills) + §8.5 failure receipt + §8.5bis Effective Harness pour agents long-running (pattern two-agent harness Anthropic Engineering mars 2026 : Initializer agent + Coding agent). Distinction nette avec [[dep-07]] évaluation continue : « evals avant déploiement vs observabilité après ».**

L'observabilité des agents IA en production est la discipline **opérationnelle runtime** qui répond à la question : *« qu'est-ce qui se passe en prod en ce moment ? »* Distincte de l'évaluation pré-déploiement ([[dep-07]] répond à *« est-ce que la sortie est bonne ? »*), elle se compose avec elle pour couvrir le cycle de vie complet d'un agent.

**Pattern two-agent harness (Anthropic Engineering 2026)** pour les agents long-running : architecture à **2 rôles séparés** où un **Initializer agent** crée le projet, les scripts d'init, la feature list structurée et le progress log, puis un **Coding agent** implémente une feature par session, exécute les tests E2E et met à jour le progress log. Insight clé : *« les artefacts externes deviennent la mémoire de l'agent. Chaque session reconstruit son contexte à partir du progress log + de l'historique git. »*

**Note de positionnement** : ce module traite la **sécurité technique runtime + observabilité** des agents en production. Pour la **gouvernance managériale** (qui décide, qui escalade, KPI métier), voir [[cu-026]]. Pour la **sécurité technique des MCP servers et configs**, voir [[dep-08]]. Les 3 modules sont **complémentaires non substituables**.

## À qui ce module s'adresse

Ce module est pour toi si tu opères un agent IA en production (Claude Code, agent custom, multi-agents) et tu veux structurer l'observabilité + les garde-fous runtime ; si tu construis une stack LLMOps et tu te demandes quels outils choisir ; si tu vois des « overclaimed completions » (agents qui déclarent avoir fini sans avoir vraiment fini) et tu veux le pattern failure receipt ; ou si tu déploies un agent long-running (workflows multi-tours, multi-sessions) et tu veux le pattern two-agent harness Anthropic.

Niveau ⭐⭐⭐⭐ Expert. ~40 minutes de lecture. Public cible : équipes tech / R&D / ops, LLMOps, responsables production IA.

**Capacités opérationnelles à acquérir** :

1. Construire une architecture observabilité 5 layers pour des agents IA en production.
2. Appliquer les 4 patterns industriels 2026 (9-layer architecture / gates TOML / Code Execution MCP / Agent Skills).
3. Implémenter le pattern failure receipt + ownership (§8.5) anti-overclaimed completion.
4. Utiliser le pattern two-agent harness Anthropic pour agents long-running (§8.5bis).
5. Distinguer observabilité runtime (DEP-05) vs évaluation pré-déploiement ([[dep-07]]) vs sécurité MCP ([[dep-08]]) vs gouvernance ([[cu-026]]).

## Pourquoi l'observabilité agents est un sujet à part

Un agent IA en production produit une trace **stochastique**, **multi-étapes**, **stateful** (selon le pattern) — radicalement différente d'un service web classique. Trois propriétés justifient une observabilité dédiée :

- **Stochasticité** : le même input peut produire des outputs différents (à cause de la température LLM, du timing API, du contexte). Mesurer la régression nécessite la **variance N runs** (cf. [[dep-07]] Anthropic « Quantifying infrastructure noise »).
- **Multi-étapes** : un agent enchaîne tool calls, génération, retrieval, validation. Une erreur à l'étape N peut avoir sa cause à l'étape N-2. L'observabilité doit tracer la chaîne complète.
- **Statefulness** : un agent avec mémoire conversationnelle (cf. [[pattern-persistent-memory]]) accumule un contexte qui influence ses décisions. L'observabilité doit suivre l'état au fil des sessions.

Un dashboard d'observabilité classique (Datadog, New Relic) ne couvre pas ces 3 propriétés. D'où l'émergence des outils dédiés LLMOps (LangSmith, Phoenix Arize, Comet Opik, Langfuse, etc.).

## Architecture observabilité 5 layers

Cinq couches à instrumenter pour avoir une vue complète d'un agent en production :

1. **Logs** : journal des événements bruts (requête entrante, appels API, exceptions). Niveau le plus bas. Outil : Sentry, ELK, Datadog logs.
2. **Traces** : reconstruction de la chaîne d'exécution multi-étapes (prompt → retrieval → LLM call → tool call → réponse). Outil : LangSmith, Phoenix Arize, Langfuse.
3. **Métriques** : indicateurs agrégés (latence p50/p95, taux d'erreur, coût par requête, taux de containment). Outil : Prometheus + Grafana, Helicone, Comet Opik.
4. **Événements métier** : occurrences typées (« escalade vers humain », « décision à effet juridique », « hallucination détectée »). Outil : événements custom dans LangSmith / Langfuse.
5. **Prompts et réponses** : capture complète des inputs/outputs LLM pour analyse a posteriori et eval continue. Outil : LangSmith, Langfuse, Comet Opik.

Une observabilité opérationnelle mature **combine les 5 layers**. Manquer un layer crée un angle mort (cas le plus courant : pas de capture prompts/réponses → impossibilité de débugger une régression observée en production).

## Panorama outils LLMOps 2026 — mapping cas d'usage

Cinq plateformes principales (cf. [[dep-07]] §Outils d'évaluation 2026 pour le détail eval) :

| Outil | Focus principal | Force différentielle |
|---|---|---|
| **LangSmith** | Native LangChain | Traces complètes + eval intégré |
| **Phoenix Arize** | Open-source self-host | Embeddings drift detection |
| **Helicone** | SaaS focus métriques | Métriques coût par requête fines |
| **Comet Opik** | SaaS focus eval | LLM-as-judge templates |
| **Langfuse** | Open-source self-host | Eval + observabilité unifié, prix bas |

**AgentShield** ([[dep-08]] §AgentShield specs opérationnelles) est complémentaire pour la sécurité des configs agent (CLAUDE.md, MCP, hooks), pas l'observabilité runtime. Choix dépend de la stack existante et de la maturité de l'équipe.

## §8 — 4 patterns industriels production 2026

La section 8 du module documente 4 patterns industriels qui structurent la production d'agents IA en 2026.

### §8.1 — 9-layer production architecture (techNmak)

Architecture de référence en 9 couches pour des agents IA en production scalable. Couches typiques : ingress → auth → routing → context retrieval → policy enforcement → LLM execution → tool execution → response validation → output egress. À implémenter selon le volume cible (10 req/s ≠ 1000 req/s).

### §8.2 — Gates machine-checkable TOML (wernerk_au)

Pattern de **gates de blocage automatique** configurés en fichiers TOML versionnés. Chaque gate définit un critère machine-checkable (seuil métrique, condition de format, validation schema). Si un gate échoue à un commit ou un déploiement, le pipeline bloque automatiquement.

Articulation explicite avec [[dep-07]] §Intégration CI/CD : les gates TOML implémentent concrètement les seuils de blocage eval. **Pas de duplication structurelle** entre DEP-05 §8.2 et DEP-07 §CI/CD — wikilink réciproque, pas réécriture.

### §8.3 — Code Execution with MCP (Anthropic)

Pattern Anthropic Engineering pour exécuter du code généré par un agent dans un environnement MCP isolé. Critique pour les agents qui produisent du code (coding agents type [[cu-027]] ECC stack) : exécution sandboxée + validation + rollback. Articulation avec [[dep-03]] §3bis « Du context au harness ».

### §8.4 — Agent Skills (Anthropic)

Pattern Anthropic d'organisation des capacités d'un agent en **skills** modulaires (chaque skill = un fichier de définition + un set d'outils + un guide d'usage). Cohérent avec le pattern Garry Tan « Fat Skills / Thin Harness » documenté en [[cu-027]] §Rupture économique 2026 point 3.

### §8.5 — Failure receipt et ownership (v3.10)

Pattern correctif au risque structurel de **« overclaimed completeness »** : un agent qui déclare avoir terminé une tâche sans l'avoir vraiment terminée. Documenté empiriquement en 2026 sur les coding agents et agents de support.

**4 éléments du failure receipt** (à transposer dans cet ordre canonique) :

1. **Inputs reçus** : trace explicite de ce que l'agent a reçu en entrée
2. **Actions entreprises** : journal des actions réellement effectuées (pas juste « j'ai fait X »)
3. **Vérification des résultats** : test que les actions ont produit le résultat attendu
4. **Propriétaire clair** : qui prend en charge si la complétion est invalidée

Cohérence avec §8.2 gates TOML (en amont — qui bloque) et §3 garde-fous (en runtime — qui détecte). Trois niveaux complémentaires : gates pré-déploiement → garde-fous runtime → failure receipt post-action.

### §8.5bis — Effective Harness pour agents long-running (v3.10)

Pattern **two-agent harness** documenté par Anthropic Engineering en mars 2026. Architecture à **2 rôles séparés** pour des workflows agentic long-running (sessions multiples, plusieurs heures à jours) :

- **Initializer agent** : démarre le projet — crée la structure, les scripts d'init, la **feature list structurée** (liste exhaustive de ce qui doit être fait), le **progress log** initial. Une seule exécution par projet.
- **Coding agent** : démarre à chaque session — lit le progress log + l'historique git → choisit une feature → implémente → exécute les tests E2E → met à jour le progress log + commit. Exécutions répétées jusqu'à complétion de la feature list.

**Insight clé à préserver textuellement** :

> *« Les artefacts externes deviennent la mémoire de l'agent. Chaque session reconstruit son contexte à partir du progress log + de l'historique git. »*

C'est la **mémoire externalisée** dans des artefacts versionnés (`claude-progress.txt`, commits git, feature list). Distinct du pattern **persistent memory** ([[pattern-persistent-memory]]) qui utilise un store mémoire dédié (agentmemory SQLite + FAISS). Les deux patterns sont complémentaires :

- Pattern **two-agent harness** = mémoire externalisée en artefacts versionnés, idéal pour coding agents long-running
- Pattern **persistent memory** ([[pattern-persistent-memory]]) = mémoire stateful dans store dédié, idéal pour agents conversationnels multi-tours

**Pas de lien avec Fat Skills / Thin Harness Garry Tan** — ce sont **2 patterns distincts** (Garry Tan = [[cu-027]] §1bis.3 sur stack ECC, Anthropic = ce module §8.5bis sur agents long-running). À ne pas confondre.

## Garde-fous runtime — 5 disciplines à empiler

Au-delà de l'observabilité (qui décrit), les garde-fous runtime **interviennent** pour éviter ou contenir les dérives :

1. **Sanitisation des inputs** (Lakera Guard, Rebuff, NeMo Guardrails — cf. [[dep-08]] §5 défenses prompt injection)
2. **Validation des outputs** avant exécution d'action sensible (envoi mail, écriture base, paiement)
3. **Cap des permissions outils** (least privilege) — agent qui lit le CRM n'a pas le droit d'écrire
4. **Monitoring anomalies** — alerter sur patterns inhabituels (pic de requêtes, contenu suspect)
5. **Failure receipt** (§8.5) — capturer formellement chaque non-complétion détectée

## KPI agents en production

Trois indicateurs canoniques (cf. [[cu-026]] §Framework 7 dimensions § dimension 4 KPI agent) :

- **Containment rate** : pourcentage des interactions résolues sans intervention humaine
- **Escalation accuracy** : pourcentage des escalades vers humain qui étaient réellement justifiées
- **Cost per interaction** : coût direct (tokens + infra) par interaction

À mesurer dans le dashboard observabilité runtime. **Distinct des métriques d'eval pré-déploiement** ([[dep-07]] golden set + sources retrouvées + concepts couverts).

## Distinction DevOps / MLOps / LLMOps

Trois pratiques distinctes :

- **DevOps** : automatiser le déploiement et l'opération de services logiciels classiques
- **MLOps** : étendre DevOps aux modèles ML traditionnels (entraînement, versioning modèles, monitoring drift)
- **LLMOps** : extension MLOps spécifique aux LLM (prompt versioning, eval continue, observabilité agents stateful, gestion coûts API)

Une équipe IA mature en 2026 combine les 3 — pas seulement DevOps + un outil LLM. La maturité LLMOps est typiquement le facteur limitant pour passer du POC à la production scalable.

## Articulation modules — ne pas dupliquer

DEP-05 est dans un écosystème de 4 modules sur la sécurité / qualité IA :

- **DEP-05 (ce module)** : observabilité runtime + garde-fous + patterns production 2026
- **[[dep-07]]** : évaluation continue pré-déploiement (golden set + eval pipeline)
- **[[dep-08]]** : sécurité technique des MCP servers + configs (CLAUDE.md, hooks)
- **[[cu-026]]** : gouvernance managériale (7 dimensions + 4 patterns Frontier Firms)

**Distinction nette à préserver** : *« evals avant déploiement vs observabilité après. Les deux sont nécessaires et complémentaires. »* (cf. [[dep-07]]).

Le chiffre [[chiffres-macro-2026#362-incidents-ia-documentes-en-2025-55-vs-2024-stanford-ai-index-2026|362 incidents IA Stanford 2025 (+55 %)]] est canonisé une seule fois et wikilinké depuis ce module (angle technique observabilité runtime), DEP-08 (angle technique SBOM IA) et PR-05 (angle stratégique cadrage projet). **Pas de duplication**.

## Risques de dérive et points d'attention

**Pas d'observabilité = pas de production** : déployer un agent IA en production sans dashboard observabilité 5 layers est le pattern le plus fréquent de l'échec silencieux. À monitorer.

**Single run sur agent long-running** : ne jamais conclure sur un seul run (cf. [[dep-07]] méthode variance N runs). Sur les agents long-running du §8.5bis, c'est encore plus critique — la mémoire externalisée peut introduire des biais session après session.

**Confondre observabilité et eval** : voir [[dep-07]] pour la distinction nette. Ce sont 2 fonctions complémentaires non substituables.

**Confondre two-agent harness Anthropic et Fat Skills / Thin Harness Garry Tan** : 2 patterns distincts. Le premier (§8.5bis) traite la mémoire externalisée pour agents long-running. Le second (cu-027) traite l'architecture stack ECC pour le dev IA-assisté.

**Skills marketplace non auditée** : OpenClaw (12 % malveillants — voir [[dep-08]]). Tout skill installé doit passer un audit AgentShield ou être issu d'un vendor reconnu.

**Plan d'arrêt non défini** : un agent en production sans procédure d'arrêt formelle (qui décide, sur quel critère, comment) dérive structurellement. Voir [[cu-026]] dimension 7 Onboarding / Offboarding.

## Récap actionnable

Pour mettre en place observabilité et garde-fous d'agents IA en production, **fais ces 8 actions** :

1. **Instrumente les 5 layers observabilité** dès le déploiement initial (pas après).
2. **Choisis 1 outil LLMOps** parmi les 5 du panorama selon ta stack (LangSmith / Phoenix / Helicone / Comet Opik / Langfuse).
3. **Implémente les gates TOML §8.2** pour blocage automatique sur dégradation.
4. **Applique le pattern failure receipt §8.5** (4 éléments) pour bloquer l'overclaimed completion.
5. **Pour les agents long-running** : adopte le pattern two-agent harness §8.5bis (Initializer + Coding).
6. **Mesure les 3 KPI canoniques** : containment rate, escalation accuracy, cost per interaction.
7. **Empile les 5 garde-fous runtime** (sanitisation, validation outputs, least privilege, monitoring, failure receipt).
8. **Combine observabilité ([[dep-07]] eval ([[dep-08]] sécurité MCP) ([[cu-026]] gouvernance)** — 4 modules complémentaires non substituables.

**Renvois utiles** : [[dep-01]] (Cadrer projet IA — arbre décision technique, étapes 5-6 agents), [[dep-02]] (RAG en production), [[dep-03]] §3bis (Du context au harness — articulation §8.3), [[dep-07]] (Évaluation continue — distinction eval vs observabilité), [[dep-08]] (Sécurité agents MCP — articulation §8.5 failure receipt), [[cu-026]] (Gouvernance des agents IA — 7 dimensions + 4 patterns), [[cu-008]] §llm-wiki-shelf-life (cohérence RAG vs persistent memory), [[pattern-persistent-memory]] (mémoire stateful complémentaire au two-agent harness), [[vigilance-hallucinations]] (discipline anti-hallucination en production).

Sources : Anthropic Engineering 2026 (« Effective Harnesses for long-running agents », « Code Execution with MCP »), techNmak (9-layer architecture), wernerk_au (gates TOML), Hub IA Learning Center, Stanford AI Index Report 2026.
