# Lot E v3.10 — Marché, maturité, patterns agentiques

**Brief consolidé pour Claude Code** : 6 patches dispersés sur modules existants. Le plus volumineux des lots v3.10 mais chaque patch reste léger (encart ou sous-section, pas de refonte).

**Sources** : runs veille 13 + 18 + 19 mai 2026 (Bpifrance Le Lab, Microsoft Work Trend Index, Microsoft Frontier Firms, Anthropic Engineering ×2, @CliffDoesAI, @LearnWithBrij).

---

## Patch E.1 — PR-04 (Marché IA & emploi) — actualisation triple marché 2026

**Module cible** : `prealables/pr-04-marche-ia-emploi.html`
**Position** : intégrer dans la section **2bis « Tendances macro 2026 »** existante (enrichissement) + un encart « Transformation Paradox » dans la section 5 (Implications stratégiques).

### Contenu à intégrer

#### Bpifrance Le Lab fin 2025 — adoption TPE/PME × 1,8

**Chiffres à intégrer dans la section 2bis** (à transposer textuellement) :

- **55 % des TPE-PME utilisent l'IA générative fin 2025** (vs 31 % fin 2024, **×1,8 en un an**)
- **17 % en usage régulier (+11 points)**
- Usages dominants : **génération de contenu (72 %)** et **analyse de données (67 %)**

**Cadrage de la trajectoire Bpifrance 2025** (chiffres bilan dispositifs) :
- **240 M€ investis** en capital développement IA en 2025 (vs 17 M€ en 2024, ×14)
- **15 000+ PME formées/sensibilisées**
- **460 Data AI Diagnostics réalisés**
- **9 403 dirigeants formés** à l'IA Curriculum Bpifrance Université

Ces chiffres complètent (sans remplacer) les chiffres v3.8 déjà intégrés (Baromètre France Num 26 % adoption TPE/PME, étude Bpifrance Le Lab 58 % enjeu vital / 33 % adoption quotidienne) — métriques différentes mais cohérentes.

#### Microsoft Work Trend Index 2026 — l'effet d'échelle observable

**À ajouter en sous-encart de la section 2bis** :

Microsoft 2026 Work Trend Index — analyse de **trillions de signaux M365** + enquête **20 000 travailleurs dans 10 pays** :

- **49 % des conversations Copilot M365** sont du « cognitive work » (analyse, problème, évaluation, création)
- **×15 d'augmentation YoY des agents actifs sur M365** (×18 chez les grandes entreprises)
- **58 % des utilisateurs IA produisent un travail qu'ils ne pouvaient pas réaliser un an plus tôt** (80 % chez les Frontier Professionals)
- **42 % des utilisateurs sont dans le segment « émergent »** (compétences individuelles ET appui org. encore en construction)

#### Le « Transformation Paradox » — culture vs techno

**À intégrer en encart dans la section 5 (Implications stratégiques)** :

> 🎯 **Le Transformation Paradox (Microsoft 2026)** : le principal frein à la valeur IA n'est ni la technologie ni les collaborateurs, mais la **culture de l'organisation**.

**Chiffres à transposer textuellement** :
- **Culture / appui managérial / pratiques RH = 2× plus d'impact sur la valeur IA que le mindset individuel** (Work Trend Index 2026)
- **67 % de l'impact IA s'explique par les facteurs organisationnels vs 32 % par le mindset individuel** (chiffre actualisé dans le Microsoft New Future of Work Report 2025, publié déc. 2025)

**Phénomène associé — « workslop »** :
- **40 % des employés US déclarent avoir reçu du « workslop »** (contenu IA poli mais inexact/inutile) sur le dernier mois
- Quand cela arrive, **les gains de temps disparaissent**

**Implication PME** : le dirigeant ne peut pas se contenter de déployer un outil IA. Sans alignement culture + appui managérial + pratiques RH adaptées, la valeur ne se matérialise pas. Ce constat justifie l'approche PR-01 (maturité organisationnelle) ET la grille « agent = employé » CU-026.

#### Cadrage des « ordres de grandeur » individuels

À ajouter en mention courte dans la section 2bis :

- **40-60 min gagnées par jour** par les utilisateurs IA (Microsoft Research)
- **66 % du temps réalloué à des tâches à plus forte valeur**

### Sources à ajouter

À insérer dans la section finale `#ressources` de PR-04 :

- **Bpifrance Le Lab** — 31 % à 55 % des TPE-PME utilisent l'IA générative (lelab.bpifrance.fr/Etudes/31-des-tpe-et-pme-utilisent-l-ia-generative, mai 2026)
- **Bpifrance Presse** — Bilan dispositifs IA 2025 (presse.bpifrance.fr)
- **Microsoft Work Lab** — 2026 Work Trend Index (microsoft.com/en-us/worklab/work-trend-index, mai 2026)
- **Microsoft Blogs** — How Frontier Firms are rebuilding the operating model for the age of AI (blogs.microsoft.com/blog/2026/05/05, 5 mai 2026)
- **Microsoft Research** — New Future of Work AI driving rapid change, uneven benefits (microsoft.com/en-us/research/blog/new-future-of-work-ai-is-driving-rapid-change-uneven-benefits/, déc. 2025)

### Métadonnées module

- `<meta name="description">` : à actualiser. Suggestion : *« 55 % des TPE-PME utilisent l'IA générative fin 2025 (×1,8 en un an). Le Transformation Paradox : culture = 2× plus d'impact que mindset individuel. Comprendre le marché IA PME 2026. »*
- Badge temps de lecture : passer à **+4 min**.

---

## Patch E.2 — PR-01 (Maturité organisationnelle) — typologie 4 profils dirigeants Bpifrance

**Module cible** : `prealables/pr-01-maturite-organisationnelle.html`
**Position** : nouvel encart en ouverture du parcours d'auto-éval (ou nouvelle sous-section dans la section d'introduction).

### Contenu à intégrer

#### La typologie Bpifrance Le Lab — 4 profils de dirigeants face à l'IA

**Étude 1 200+ dirigeants** (Bpifrance Le Lab, mai 2026).

| Profil | % dirigeants | Caractéristique | Levier prioritaire |
|---|---|---|---|
| **Sceptiques** | **27 %** | Doutent de la valeur réelle de l'IA pour leur métier | Démonstration sur cas d'usage métier précis |
| **Bloqués** | **26 %** | Reconnaissent l'enjeu mais manquent de compétences | Formation + accompagnement opérationnel |
| **Expérimentateurs** | **19 %** | Testent activement, sans plan de scaling | Structuration d'une stratégie IA |
| **Innovateurs** | **28 %** | Intègrent l'IA dans leur stratégie globale | Scaling et industrialisation |

**Insight clé à transposer textuellement** :

> *« Dans 73 % des cas l'initiative IA part directement du dirigeant — mais la transformation ne peut pas reposer uniquement sur lui. »*

#### Comment utiliser cette typologie

L'auto-positionnement du dirigeant sur l'un de ces 4 profils permet d'**identifier immédiatement son levier prioritaire** plutôt que d'appliquer une recommandation uniforme :

- Un **Sceptique** n'a pas besoin de formation IA générique — il a besoin d'une démonstration sur **son** problème métier
- Un **Bloqué** n'a pas besoin de stratégie IA — il a besoin d'une montée en compétences accompagnée
- Un **Expérimentateur** doit passer du POC au déploiement structuré (cf. PR-04 §2ter maturité agentique v3.9)
- Un **Innovateur** doit industrialiser et anticiper la gouvernance (cf. CU-026 + PR-05)

Cohérent avec la grille de maturité PR-01 existante — la typologie Bpifrance ajoute une **lecture sociologique** complémentaire de la lecture organisationnelle.

### Sources à ajouter

- **Bpifrance Le Lab** — Étude 1 200+ dirigeants, typologie 4 profils (lelab.bpifrance.fr, mai 2026)

### Renvois croisés

- Vers **PR-04 §2ter** (maturité agentique v3.9) : cohérence avec les 4 paliers (Découverte / Expérimentation / Mise en production / Industrialisation)
- Vers **CU-026** : pour les profils Innovateurs/Expérimentateurs qui déploient des agents

### Métadonnées module

- `<meta name="description">` : actualiser pour mentionner la typologie 4 profils. Suggestion : *« Typologie Bpifrance Le Lab 4 profils dirigeants face à l'IA (Sceptiques 27 %, Bloqués 26 %, Expérimentateurs 19 %, Innovateurs 28 %). Auto-positionnement + levier prioritaire. »*
- Badge temps de lecture : passer à **+2 min**.

---

## Patch E.3 — DEP-01 (Cadrer un projet IA) — heuristique anti-hype architecture

**Module cible** : `deploiement/dep-01-cadrer-projet-ia.html` (à confirmer le nom exact)
**Position** : nouvelle sous-section dans la section consacrée au choix d'architecture, ou nouvelle section dédiée.
**Anchor id** suggéré : `heuristique-anti-hype` ou intégration h3 dans section existante.

### Contenu à intégrer

#### L'heuristique 2026 — single LLM call d'abord

**Constat à intégrer** (source : @LearnWithBrij, mai 2026) :

> **80 % des échecs de projet IA interviennent avant la première ligne de code** — parce qu'on choisit d'emblée l'architecture la plus sophistiquée (multi-agent) alors qu'un single LLM call aurait suffi.

#### L'arbre de décision (à transposer comme schéma ou liste numérotée)

Ordre canonique des architectures à tester **dans l'ordre** :

1. **Single LLM call** — l'appel le plus simple : un prompt, une réponse. Suffit pour la majorité des cas (résumé, génération, classification, extraction)
2. **Long context** — si le single LLM call manque de contexte, fournir plus de matière dans le prompt (jusqu'à 200 k tokens disponibles sur les modèles 2026)
3. **RAG** — si le contexte ne tient pas dans la fenêtre, ajouter un retrieval (vector DB + chunking + embeddings)
4. **Fine-tuning** — si le RAG manque de précision sur un domaine spécifique, fine-tuner un SLM (cf. DEP-04 §4bis v3.9)
5. **Single agent** — si une décision/action dynamique est nécessaire, passer à l'agent (tool use)
6. **Multi-agent** — uniquement si plusieurs spécialistes coopèrent réellement (cf. CU-014 + CU-026)

#### La règle d'or

> **Single LLM call d'abord, scaler seulement si prouvé nécessaire.**

#### Contexte 2026 — la moitié des cas RAG classiques rendue obsolète

À ajouter en remarque (cohérence avec Lot A) :

> ⚠️ **Long context a déjà tué la moitié des cas RAG classiques** (<200 k tokens). Avant de mettre en place une stack RAG complexe, vérifier si un long context ne suffit pas.

### Sources à ajouter

- **@LearnWithBrij** — Heuristique anti-hype architecture (x.com/LearnWithBrij/status/2053836732454572298, mai 2026)

### Renvois croisés

- Vers **DEP-02** + Lot A v3.10 (signal RAG vs persistent memory)
- Vers **DEP-04 §4bis** (fine-tuning SLM v3.9) pour l'étape 4
- Vers **CU-014 + CU-026** pour les étapes 5 et 6
- Vers **DEP-05 §8** (production-grade v3.9) pour les patterns multi-agent en production

### Métadonnées module

- Badge temps de lecture : passer à **+2 min**.

---

## Patch E.4 — DEP-05 — nouvelle §8.5 « Failure receipts & ownership » + §8.5bis « Effective Harnesses long-running »

**Module cible** : `deploiement/dep-05-agents-observabilite.html`
**Position** : 2 nouvelles sous-sections dans la **section 8 « Production-grade » créée en v3.9** (entre 8.4 Agent Skills et `#ressources`).

### Patch E.4.a — §8.5 Failure receipts & ownership

#### Contenu à intégrer

#### Le constat — un agent peut faire des dégâts irréversibles en quelques secondes

**Exemple à transposer textuellement** (signal @CliffDoesAI, 19 mai 2026, avec exemple @SSheth) :

> Un coding agent a supprimé **une base de production + ses backups en 9 secondes**. Sans traçabilité forensique, l'incident devient ingouvernable : qui était responsable ? Que faisait l'agent à ce moment ? Pourquoi le garde-fou a-t-il failli ?

Ce cas n'est pas isolé — il illustre **la nouvelle classe de risques agentiques 2026** (cf. PR-05 D.2.a).

#### Le pattern correctif — failure receipt + human owner

**Tout agent en production** doit pouvoir produire un **failure receipt** complet en cas d'incident :

| Élément du failure receipt | Question répondue |
|---|---|
| **Inputs reçus** | Quel prompt / contexte / donnée d'entrée a déclenché l'action ? |
| **Actions entreprises** | Quelle séquence d'appels tools / décisions internes a été exécutée ? |
| **Vérification des résultats** | Quelles validations (gates TOML, LLM-as-judge) ont été passées ou contournées ? |
| **Propriétaire clair** | Qui est le human owner de l'agent ? Qui contacter immédiatement ? |

**Règle absolue à transposer textuellement** :

> Sans cette traçabilité élémentaire, **l'agent ne doit pas être autorisé près des systèmes critiques**.

#### Implications opérationnelles

- **Pour chaque agent en production** : checklist gouvernance enrichie (à intégrer aussi dans CU-026)
- **Pour chaque outcome agent** : un **human owner désigné** (cohérent avec le pattern « agent = employé » CU-026 = chaque employé a un manager)
- **Cohérence avec § 8.2 (gates TOML)** : les gates bloquent en amont, le failure receipt documente en aval
- **Cohérence avec § 7 (sécurité 3 niveaux)** et DEP-08 (sécurité agents) : le failure receipt est la **traçabilité forensique** complémentaire des défenses préventives

### Patch E.4.b — §8.5bis Effective Harnesses pour agents long-running

#### Contenu à intégrer

#### Le constat — agents qui tournent sur plusieurs heures/jours

**Source** : Anthropic Engineering — « Effective Harnesses for Long-Running Agents » (nov. 2025) + « Harness Design for Long-Running Application Development » (mars 2026).

Les patterns § 8.1 à § 8.4 v3.9 couvrent l'**orchestration intra-session**. Manque la dimension **continuité cross-sessions** pour les agents qui tournent sur des tâches multi-heures ou multi-jours (refactor de codebase, audit complet, projet itératif).

#### Le pattern two-agent harness

Architecture à 2 rôles complémentaires :

| Rôle | Mission | Artefacts produits |
|---|---|---|
| **Initializer agent** | Crée le projet, les scripts d'init, la feature list structurée, le progress log | `claude-progress.txt`, fichiers de structure, premier commit git |
| **Coding agent** | Implémente **une feature par session**, exécute les tests E2E, met à jour le progress log | Code, tests, mises à jour `claude-progress.txt`, commits git |

**Insight clé** : **les artefacts externes deviennent la mémoire de l'agent**. Chaque session reconstruit son contexte à partir du progress log + de l'historique git. Pas de mémoire interne persistante (cohérent avec Lot A — persistent memory vs RAG stateless).

#### Implications pour la PME

- **Cas d'usage typique** : projet de migration / refactor majeur d'une application, audit qualité complet d'un repo, génération itérative d'un site / d'une documentation
- **Stack** : framework existant (Claude Code, Cursor) + discipline d'externalisation des artefacts
- **Pas un investissement infra lourd** : surtout une discipline d'organisation des fichiers et du process

### Sources à ajouter dans DEP-05

À insérer dans la section finale `#ressources` :

- **@CliffDoesAI** — Failure receipt & ownership pattern (x.com/CliffDoesAI/status/2056511828952273286, 19 mai 2026)
- **Anthropic Engineering** — Effective harnesses for long-running agents (anthropic.com/engineering/effective-harnesses-for-long-running-agents, nov. 2025)
- **Anthropic Engineering** — Harness Design for Long-Running Application Development (mars 2026)
- **GitHub Anthropic** — cwc-long-running-agents (github.com/anthropics/cwc-long-running-agents)

### Mise à jour TOC de DEP-05

Ajouter en sommaire (dans l'entrée « Production-grade 2026 » section 8 — sous-niveau si possible) :

- §8.5 — Failure receipts & ownership
- §8.5bis — Harnesses long-running

### Métadonnées module DEP-05

- Badge temps de lecture : passer à **28 min → 32 min** (estimation +4 min pour les 2 sous-sections).

---

## Patch E.5 — CU-026 — Microsoft Frontier Firms 4 patterns de collaboration

**Module cible** : `modules/cu-026-gouvernance-agents-ia.html`
**Position** : nouvelle sous-section dans la section 1 « Le shift de framing 2026 » ou nouvelle section 3bis.
**Anchor id** suggéré : `section-3bis` (avec icône 🎭, label TOC « 4 patterns de collaboration »)

### Contenu à intégrer

#### Cadrage Microsoft Frontier Firms

**Source** : Blog Microsoft 5 mai 2026 (Jared Spataro) — « How Frontier Firms are rebuilding the operating model for the age of AI ».

> **Insight cadre** : *« la contrainte n'est plus ce que les gens peuvent faire, c'est la façon dont le travail est structuré autour d'eux. »*

Le pattern « agent = employé » (CU-026 v3.8) répond à la question « comment manager un agent ? ». Microsoft Frontier Firms ajoute une **grille de design organisationnel** pour matcher le niveau d'implication humaine à l'outcome attendu.

#### Les 4 patterns de collaboration humain-agent

À transposer textuellement (préserver les noms en anglais comme cadre canonique) :

| Pattern | Rôle humain | Rôle agent | Cas d'usage type PME |
|---|---|---|---|
| **(1) Author** | Produit | Assiste à la demande | Rédaction de propositions commerciales avec Copilot |
| **(2) Editor** | Fixe l'intent, édite/approuve | Produit un premier draft | Rédaction de CR de réunion, articles, posts (cf. CU-002, CU-003) |
| **(3) Director** | Crée une spec, délègue | Exécute intégralement en arrière-plan | Génération de rapports périodiques, veille, traduction (cf. CU-001, CU-004) |
| **(4) Orchestrator** | Conçoit le système | Plusieurs agents tournent en parallèle, avec exceptions / escalades | Multi-agents par fonction (cf. CU-014), workflows complexes (cf. CU-026) |

#### Comment utiliser cette grille

Chaque cas d'usage IA d'une PME peut être positionné sur **l'un des 4 patterns**. Le pattern détermine :

- Le **niveau de supervision** requis
- Les **garde-fous** à mettre en place (validation humaine vs revue échantillonnée vs failure receipt seul)
- Le **KPI de succès** (rapport assistance / autonomie / parallélisation)
- Le **profil de l'employé** qui pilote (Author = niveau senior, Orchestrator = niveau lead avec compétence design organisationnel)

#### Cohérence avec les 7 dimensions CU-026

Les 4 patterns Microsoft sont **complémentaires** des 7 dimensions de gouvernance CU-026 :
- Les 4 patterns définissent **le type de collaboration** (architecture humain-agent)
- Les 7 dimensions définissent **les attendus de gestion** par agent (tâche, droits, escalade, KPI, audit, versions, onboarding)

Les 2 grilles s'utilisent ensemble :
1. Choisir le **pattern Microsoft** (Author / Editor / Director / Orchestrator) selon le cas d'usage
2. Documenter les **7 dimensions CU-026** pour chaque agent du pattern

### Sources à ajouter

- **Microsoft** — Blog How Frontier Firms are rebuilding the operating model for the age of AI (blogs.microsoft.com/blog/2026/05/05, 5 mai 2026)

### Mise à jour TOC

```html
<li><a href="#section-3bis"><span class="toc-icon">🎭</span>4 patterns de collaboration</a></li>
```

### Renvois croisés

- Depuis **CU-014** (Multi-agents) : encart « pattern Orchestrator Microsoft, voir CU-026 §3bis »
- Depuis **CU-002, CU-003, CU-001, CU-004** : encart en footer mentionnant le pattern correspondant
- Vers **PR-04 §2ter** (maturité agentique) : cohérence narrative

### Métadonnées module

- Badge temps de lecture : passer à **+3 min**.

---

## Patch E.6 — DEP-07 (Évaluation continue et qualité IA) — Anthropic Demystifying Evals

**Module cible** : `deploiement/dep-07-evaluation-qualite.html` (à confirmer)
**Position** : nouvelle sous-section ou enrichissement de la section principale sur les évaluations.

### Contenu à intégrer

#### Définitions canoniques (Anthropic Engineering, mai 2026)

À transposer textuellement comme référentiel terminologique :

| Terme | Définition |
|---|---|
| **eval** | Mesure quantifiable de la qualité d'une sortie ou d'une décision agent sur une tâche donnée |
| **harness** | Cadre d'exécution qui orchestre l'agent + les tools + les gates + les évaluations (cf. DEP-03 §3bis v3.9) |
| **multi-turn evaluations** | Évaluation sur une séquence d'échanges, pas seulement un appel unique |
| **state-modifying agents** | Agents qui modifient un état externe (fichier, DB, API) — évaluation = vérification de l'état post-action, pas seulement de la réponse |

#### Heuristique « eval first, optimize second »

À intégrer comme principe opérationnel :

> **Construire les évaluations AVANT d'optimiser l'agent.**

Pourquoi : sans baseline d'évaluation, toute optimisation est mesurée à l'aveugle. Les premiers gains paraissent grands (« ça marche mieux ») mais on découvre 6 mois plus tard que la qualité est restée stable, voire a régressé.

#### Bruit infra vs régression modèle

**Source complémentaire** : Anthropic « Quantifying infrastructure noise in agentic coding evals » (mai 2026).

Quand un eval baisse, deux causes possibles :

1. **Régression modèle** : le modèle de base a changé, ou le prompt a dérivé
2. **Bruit infra** : latence variable, indisponibilité ponctuelle d'un tool, instabilité de l'API

Méthode pour distinguer : **répéter l'eval N fois sur le même input** et mesurer la variance. Si variance haute = bruit infra. Si variance basse mais score bas = régression réelle.

### Sources à ajouter

- **Anthropic Engineering** — Demystifying evals for AI agents (anthropic.com/engineering/demystifying-evals-for-ai-agents, mai 2026)
- **Anthropic Engineering** — Quantifying infrastructure noise in agentic coding evals (anthropic.com/engineering/infrastructure-noise, mai 2026)

### Renvois croisés

- Vers **DEP-03 §3bis** (harness engineering v3.9) — cohérence terminologique
- Vers **DEP-05 §8.2** (gates TOML v3.9) — les gates sont un type d'eval mécanique
- Vers **DEP-05 §8.5** (failure receipt, Patch E.4 ci-dessus) — l'eval mesure le succès, le failure receipt documente l'échec

### Métadonnées module

- Badge temps de lecture : passer à **+3 min**.

---

## Synthèse cohérence Lot E

6 patches dispersés mais **3 fils narratifs cohérents** :

1. **Marché IA 2026 mature** (E.1 + E.2) : PR-04 et PR-01 enrichis avec Bpifrance + Microsoft → la maturité organisationnelle est le différenciateur, plus l'adoption technique
2. **Patterns techniques agentiques** (E.3 + E.4 + E.5 + E.6) : DEP-01 (heuristique anti-hype) + DEP-05 §8.5 (failure receipt + harness long-running) + CU-026 (Frontier Firms 4 patterns) + DEP-07 (evals) → consolidation du référentiel technique agents 2026
3. **Convergence cross-modules** : les renvois croisés sont denses (E.5 → E.4 → CU-014 → CU-002…). Le Lot E renforce la **toile pédagogique** du Hub plutôt que d'ajouter des îlots isolés.

## Items parallèles (à compiler dans brief v3.10)

Chiffres macro à canoniser dans `chiffres-macro-2026.md` (item I-D-005) :

1. **55 % des TPE-PME utilisent l'IA générative fin 2025** (Bpifrance Le Lab, vs 31 % fin 2024) — recouvrement avec CU-008, CU-014, autres modules adoption
2. **240 M€ investis par Bpifrance en capital développement IA en 2025** (vs 17 M€ en 2024, ×14) — recouvrement avec PR-08 (nouveau préalable Lot C)
3. **49 % conversations Copilot M365 = cognitive work** (Microsoft Work Trend Index 2026) — recouvrement avec CU-002, CU-009, CU-027
4. **×15 augmentation YoY agents actifs sur M365** (Microsoft) — recouvrement avec CU-014, CU-026, DEP-05
5. **67/32 organisation/individu** + **2× plus d'impact culture vs mindset** (Microsoft Frontier Firms / New Future of Work) — recouvrement avec PR-01, CU-026, PR-04
6. **40 % workslop reçu sur dernier mois** (Microsoft) — recouvrement avec DEP-03, DEP-05, CU-002 (qualité production IA)
7. **Typologie 4 profils dirigeants Bpifrance** (Sceptiques 27 % / Bloqués 26 % / Expérimentateurs 19 % / Innovateurs 28 %) — recouvrement avec PR-01, PR-04

→ Soit ~7 nouveaux chiffres macro à canoniser via I-D-005.
