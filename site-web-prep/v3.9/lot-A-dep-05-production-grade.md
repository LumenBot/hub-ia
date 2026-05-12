# Lot A v3.9 — Refonte ciblée DEP-05 (Agents en production)

**Brief consolidé pour Claude Code** : refonte d'envergure du module DEP-05 par ajout d'une **nouvelle section 8 « Production-grade : 4 patterns industriels 2026 »**. Quatre pistes virales convergent vers la même thèse : « production ≠ démo ». Les sections 1 à 7 restent **intactes**.

**Sources** : veille `pistes-cumulatives.md` run 2026-05-12 (techNmak, wernerk_au, Anthropic Engineering x2).

---

## Patch A.1 — Nouvelle section 8 : « Production-grade : 4 patterns industriels 2026 »

**Module cible** : `deploiement/dep-05-agents-observabilite.html`
**Position** : insérer **après** la section 7 « Plan d'action 30 jours » et **avant** la section `#ressources`.
**Anchor id** : `section-8`
**Icône TOC** : 🏭
**Label TOC** : « Production-grade 2026 »

### Intro de section (à intégrer en tête de section 8)

> **The demo is one file. Production is this.**

Quatre patterns sont sortis du buzz de la communauté builders en mai 2026. Ils ne sont pas exotiques : ils décrivent ce que **les équipes qui ont passé la barre des 6 mois en production** ont structuré dans leur stack. Si vous êtes en POC ou en pilote, regardez-les comme une cartographie de ce qui vous attend. Si vous êtes déjà en prod, utilisez-les comme grille d'audit.

Les 4 patterns se complètent :
1. **9-layer production architecture** — la cartographie macro (5 services + agents auto-correcting + sécurité + observabilité).
2. **Gates machine-checkable TOML** — anti-pattern « overclaimed completeness » : forcer la conformité par contrat.
3. **Code Execution with MCP** — agents qui chargent les tools à la demande, filtrent les données avant le modèle.
4. **Agent Skills** — variante structurée du LLM Wiki appliquée aux compétences agent.

---

### 8.1 — Le pattern « 9-layer production architecture »

**Le constat** : une démo d'agent tient dans un fichier Python de 200 lignes (un LLM call + un tool + un loop). En production, l'architecture explose en **9 couches indépendantes** parce que chaque dimension (mémoire, sécurité, observabilité, coût) devient un service à part entière.

**Les 9 couches** (proposées par @techNmak en référence à 7 cycles de production observés en 2026) :

| # | Couche | Fonction | Service typique |
|---|---|---|---|
| 1 | **RAG service** | Récupération de contexte par requête | Vector store + retriever |
| 2 | **Semantic cache** | Cache de réponses à requêtes sémantiquement proches | Redis vector / dedicated |
| 3 | **Memory service** | Mémoire long terme persistante (utilisateur, session, organisation) | KV store + summarization |
| 4 | **Query rewriter** | Réécriture de la requête utilisateur pour optimiser le retrieval | LLM léger ou rule-based |
| 5 | **Router** | Orientation de la requête vers le bon modèle / la bonne stack | Model router (cost / latency / qualité) |
| 6 | **Auto-correcting agents** | Document grader, decomposer, adaptive router — agents qui auto-évaluent leurs sorties | LangGraph / patterns CRITIC |
| 7 | **Security layer 3 niveaux** | Input validation / content filtering / output sanitization | Guardrails AI, Lakera, etc. |
| 8 | **Observabilité par-stage** | Tracing distribué + cost-per-query + qualité par stage | LangSmith, Phoenix, Arize |
| 9 | **Cost attribution** | Imputation des coûts LLM par feature, par utilisateur, par requête | FinOps custom ou outillé |

**Pourquoi ça compte pour une PME** : une PME qui se lance ne peut pas (et ne doit pas) tout monter d'un coup. Mais elle doit savoir **où elle est sur cette carte** et **quelle couche elle ajoutera ensuite**. L'erreur la plus fréquente : empiler les fonctionnalités produit avant d'avoir l'observabilité (couche 8) et le routing (couche 5). Résultat : coûts qui dérivent, pas de visibilité sur la qualité.

**Heuristique de mise en place** (ordre recommandé) :
1. **Démarrer** : couches 1 (RAG) + 6 (auto-correcting) + 8 (observabilité minimale)
2. **Scaler** : ajouter 2 (semantic cache) + 5 (router) quand les coûts dépassent 500 €/mois
3. **Industrialiser** : ajouter 3 (memory) + 4 (query rewriter) quand le produit a un usage régulier
4. **Finaliser** : 7 (sécurité 3 niveaux) + 9 (cost attribution) avant tout déploiement client externe

**Composant HTML suggéré** : tableau `.tech-comparison-table` (existant) ou nouvelle classe `.production-layers-table` si meilleur rendu.

### Sources à ajouter dans la section finale (sous-rubrique 📰 Articles de fond)

- Compte X @techNmak — « The demo is one file. Production is this. » thread sur architecture 9-layer (mai 2026, 2 739 likes, 370 RT)

---

### 8.2 — Pattern « Gates machine-checkable TOML »

**Le constat** : sur 7 cycles d'observation d'agents LLM en production, trois causes d'échec reviennent systématiquement :
1. **Artifact manquant** — l'agent dit qu'il a produit un livrable mais le fichier n'existe pas, ou est vide, ou est incomplet.
2. **Contrat ambigu** — l'instruction donnée à l'agent autorise plusieurs interprétations, l'agent en choisit une qui passe les tests mais rate l'intention.
3. **Overclaimed completeness** — l'agent déclare une tâche terminée alors qu'il a couvert 70 % du périmètre. C'est l'anti-pattern le plus coûteux.

**Le pattern correctif** : poser des **gates machine-checkable** au format TOML **dès le design** de l'agent, avant la première ligne de code. Une gate est un contrat structuré que l'agent **doit** satisfaire pour qu'un livrable soit accepté.

**Exemple de gate TOML** :

```toml
[gate.cr_reunion]
artifact_required = "fichier_md"
min_length_chars = 1500
required_sections = ["decisions", "actions", "prochains_rdv"]
forbidden_phrases = ["selon mes informations", "je pense que"]
validation_llm = "haiku"
validation_prompt = "Le CR contient-il au moins 3 décisions et 5 actions assignées ?"
```

L'agent ne peut **pas** marquer la tâche comme terminée tant que la gate n'est pas validée. Validation machine-checkable (parsing du fichier) + validation LLM-as-judge sur les critères qualitatifs.

**Implications pour la PME** :
- À mettre en place pour **tout agent en production qui produit un livrable**.
- Le surcoût de design est faible (1-2 h par agent) mais le ROI est très élevé : 0 % de livrables silencieusement incomplets.
- Compatible avec les frameworks d'évaluation existants (LangSmith, Phoenix, custom evals).

**Lien avec section 3** : les gates TOML sont une **forme de garde-fou** mais opèrent en aval (output validation) là où la section 3 traite des garde-fous en amont (input + execution). À mentionner en renvoi croisé.

### Sources à ajouter dans la section finale

- Compte X @wernerk_au — audit 7 cycles LLM-agent + pattern gates TOML (mai 2026)

---

### 8.3 — Pattern « Code Execution with MCP »

**Le constat** : un agent qui orchestre des tools (API calls, requêtes DB, lectures de fichiers) consomme **massivement** des tokens à chaque step parce que les tools renvoient leurs résultats bruts dans le contexte du modèle. Sur un workflow à 15 steps, on peut facilement dépasser 80 000 tokens de contexte rien que pour les outputs intermédiaires.

**Le pattern correctif** (publié par Anthropic Engineering en mai 2026) : transformer l'agent en **exécuteur de code Python** qui appelle les MCP tools **localement**, traite les données dans le sandbox d'exécution, et ne renvoie au modèle **que ce qui est strictement nécessaire** pour la décision suivante.

**Le changement de paradigme** :

| Approche | Tools chargés | Données dans le contexte | Coût tokens |
|---|---|---|---|
| Classique (tool calling) | Tous chargés au démarrage | Outputs bruts injectés à chaque step | Élevé |
| **Code Execution with MCP** | Chargés à la demande dans le code | Filtrés / agrégés avant injection | Réduit 60-80 % |

**Bénéfices observés** :
- **Réduction tokens** 60-80 % sur workflows longs
- **Efficacité contextuelle** : le modèle ne voit que les données pertinentes
- **Performance** : moins de tokens = moins de latence

**Implications pour la PME** :
- Particulièrement pertinent pour les agents qui traitent **du volume de données** (CRM, fichiers, logs).
- Nécessite une exécution Python sandboxée — coût d'infra léger mais réel.
- Intégration naturelle avec MCP servers existants (la couche reste compatible).

**Lien avec DEP-03** : à mentionner explicitement dans DEP-03 (Context engineering) comme **pattern d'optimisation contextuelle** — c'est l'application opérationnelle des principes de context engineering.

### Sources à ajouter dans la section finale

- Anthropic Engineering — « Code Execution with MCP » (anthropic.com/engineering/code-execution-with-mcp, mai 2026)

---

### 8.4 — Pattern « Agent Skills »

**Le constat** : un agent généraliste qui doit accomplir des tâches très diverses devient rapidement ingérable. Soit le system prompt explose (10 000+ tokens d'instructions), soit la qualité chute sur les tâches spécialisées.

**Le pattern correctif** (publié par Anthropic Engineering en mai 2026) : les **Agent Skills** sont des **dossiers organisés** d'instructions, scripts et ressources que l'agent **découvre et charge dynamiquement** selon la tâche en cours.

**Structure type d'une Skill** :

```
skills/
└── compta-export-tva/
    ├── SKILL.md          # description + triggers + usage
    ├── prompts/
    │   ├── extract.md
    │   └── validate.md
    ├── scripts/
    │   └── export_tva.py
    └── examples/
        └── exemple_q1_2026.json
```

L'agent ne charge la Skill que **quand sa description match** la tâche utilisateur. Pour 50 Skills disponibles, seules 1 ou 2 sont chargées par requête → coût contextuel maîtrisé, qualité élevée sur chaque domaine.

**Liens conceptuels** :
- C'est une **variante structurée du LLM Wiki** (CU-008) appliquée aux **compétences agent** plutôt qu'à la knowledge base.
- Cohérent avec le principe « agent = employé » de CU-014 / CU-026 : chaque Skill = une compétence cadrée et documentée.
- Pattern compatible avec le 9-layer (couche 6 auto-correcting agents peuvent invoquer des Skills).

**Implications pour la PME** :
- À envisager dès qu'un agent dépasse 5-10 cas d'usage distincts.
- Coût de mise en place faible (organisation de fichiers + descriptions).
- Permet une **gouvernance lisible** : chaque Skill peut être auditée, versionnée, désactivée indépendamment.

**Lien avec CU-026** : les Agent Skills s'inscrivent parfaitement dans le framework de gouvernance des agents IA — chaque Skill est une compétence avec son onboarding, ses KPI, son périmètre.

### Sources à ajouter dans la section finale

- Anthropic Engineering — « Equipping agents for the real world with Agent Skills » (anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills, mai 2026)

---

## Conclusion de section (à intégrer en fin de section 8)

> **Synthèse** : la production en 2026, ce n'est plus une pipeline RAG bien réglée. C'est une **stack en 9 couches**, des **gates contractuelles** sur chaque livrable, une **exécution de code** qui filtre les données avant le modèle, et des **compétences chargées dynamiquement**. La barre s'est levée. La bonne nouvelle : aucun de ces 4 patterns n'exige une équipe de 20 ingénieurs. Tous sont accessibles à une PME outillée — à condition de les empiler dans le bon ordre.

---

## Mise à jour TOC du module

Ajouter dans le sommaire (`<aside class="module-toc">`) après l'entrée « Plan d'action 30 jours » :

```html
<li><a href="#section-8"><span class="toc-icon">🏭</span>Production-grade 2026</a></li>
```

## Renvois internes à mettre à jour dans DEP-05

- En section 3 (garde-fous obligatoires) : encart renvoyant vers section 8.2 (gates TOML) comme « pattern complémentaire output ».
- En section 4 (panorama outils) : mention des frameworks de gates (à signaler en encart léger) — Guardrails AI, instructor, outlines.
- Footer « Pour aller plus loin » : renvoyer vers DEP-03 (Code Execution MCP comme pattern de context engineering) et vers CU-026 (Agent Skills comme briques de gouvernance).

## Renvois internes à mettre à jour dans les autres modules

- **DEP-03** (Context engineering) : ajouter encart renvoyant vers DEP-05 §8.3 (Code Execution with MCP) — voir Lot C.
- **CU-026** (Gouvernance agents) : ajouter mention des Agent Skills comme brique opérationnelle — encart court avec renvoi DEP-05 §8.4.

## Métadonnées module

- `<meta name="description">` : aucune modification (la description actuelle reste juste).
- Badge « 20 min de lecture » → **passer à 28 min** (section 8 ajoute ~8 min de lecture).
