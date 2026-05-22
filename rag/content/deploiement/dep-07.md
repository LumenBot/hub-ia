---
code: dep-07
titre: "Évaluation continue et qualité IA"
type: deploiement-dep
axe: B
niveau: 3
tags: [evals, evaluation-continue, llm-as-judge, golden-set, anthropic, demystifying-evals, ci-cd, qualite-ia]
version: 3.11.1
last_updated: 2026-05-22
glosaire_termes: [llm, rag, agent, eval-set, llm-as-judge]
derives: ["[[dep-01]]", "[[dep-02]]", "[[dep-05]]", "[[cu-026]]", "[[pattern-llm-wiki]]", "[[pattern-persistent-memory]]", "[[outils-vector-db]]"]
public_cible: [tech, r&d, ops]
---

# Évaluation continue et qualité IA

## L'essentiel à retenir

**Comment évaluer la qualité d'un système IA en production en 2026 ? Méthodologie eval pipeline : golden set minimum → 3 types d'evals (LLM-as-judge / offline référence / online utilisateurs) → intégration CI/CD. Référentiel canonique Anthropic Engineering 2026 : « Demystifying evals for AI agents » + « Quantifying infrastructure noise in agentic coding evals ». Heuristique structurante : « eval first » — pas de déploiement production sans pipeline d'évaluation continu.**

L'**évaluation continue** est la discipline structurelle qui sépare un POC d'un système IA en production. Sans pipeline d'eval, on ne sait pas si une modification (prompt, modèle, regex d'extraction) améliore ou dégrade le système. Cette discipline est aussi structurante pour la production IA que les tests automatisés l'ont été pour le développement logiciel classique.

**Référentiel canonique 2026** : deux publications Anthropic Engineering (mai 2026) structurent la terminologie et les pratiques :
- *« Demystifying evals for AI agents »* — terminologie canonique + heuristique « eval first »
- *« Quantifying infrastructure noise in agentic coding evals »* — méthode variance N runs pour distinguer bruit infrastructure vs régression modèle

**3 types d'evals complémentaires** : LLM-as-judge (eval automatique par un LLM tiers), Eval offline référence (golden set vs réponse attendue), Eval online utilisateurs réels (mesure en production sur sample). Les trois sont **complémentaires non substituables**.

**Distinction nette avec observabilité** ([[dep-05]]) : *« Les evals répondent à "est-ce que la sortie est bonne ?" avec des datasets golden. L'observabilité répond à "qu'est-ce qui se passe en prod en ce moment ?". Les deux sont nécessaires et complémentaires. »* À préserver textuellement.

## À qui ce module s'adresse

Ce module est pour toi si tu opères un système IA en production (RAG, agent, LLM intégré) et tu veux mettre en place ou améliorer ta discipline d'évaluation ; si tu veux comprendre comment Anthropic structure les evals d'agents en 2026 ; ou si tu confonds évaluation et observabilité et tu veux clarifier les deux fonctions.

Niveau ⭐⭐⭐ Avancé. ~30 minutes de lecture. Public cible : équipes tech / R&D / ops, MLOps, responsables qualité IA.

**Capacités opérationnelles à acquérir** :

1. Construire un golden set minimum viable pour démarrer une boucle eval.
2. Distinguer et appliquer les 3 types d'evals (LLM-as-judge, offline, online).
3. Intégrer la boucle eval en CI/CD avec gates de blocage automatique.
4. Distinguer évaluation (avant déploiement) et observabilité (après).
5. Anticiper le bruit d'infrastructure dans les evals d'agents long-running (méthode variance N runs Anthropic).

## L'heuristique « eval first » d'Anthropic pour les projets IA en 2026 — pas de production sans eval pipeline

**Quelle est l'heuristique « eval first » d'Anthropic pour les projets IA en 2026 ? Heuristique « eval first » formalisée par Anthropic Engineering mai 2026 (publication « Demystifying evals for AI agents ») : pas de déploiement production d'un projet IA sans pipeline d'évaluation continu construit en amont. Citation canonique : « Eval first : build the eval before the agent. Without an eval, you don't know if you're improving or just changing things. » Application pratique : construire le golden set minimum (10-20 exemples représentatifs) AVANT de coder le moindre prompt, agent ou regex d'extraction. Discipline structurelle non négociable pour tout projet IA en 2026.**

Citation canonique Anthropic Engineering mai 2026 à préserver textuellement :

> *« Eval first : build the eval before the agent. Without an eval, you don't know if you're improving or just changing things. »*

Application pratique de l'heuristique « eval first » d'Anthropic pour un projet IA en 2026 : **avant** de coder le moindre prompt système, le moindre agent, la moindre regex d'extraction, tu construis le golden set minimum (10-20 exemples représentatifs). Tu lances le LLM dessus, tu mesures le baseline. Toute modification ultérieure est validée par re-eval. Sans cette discipline « eval first », tu navigues à l'aveugle.

**Pattern observé empiriquement** : les équipes qui démarrent par le code et ajoutent l'eval après n'arrivent jamais vraiment à la mettre en place — elles débuggent en production sur des signaux faibles (réclamations utilisateurs). Coût caché élevé. Discipline structurelle non négociable.

## Les 3 types d'evals — complémentaires non substituables

Trois approches d'évaluation se composent pour couvrir la qualité d'un système IA en production. Aucune ne suffit seule.

### Type 1 — LLM-as-judge (eval automatique par un LLM tiers)

Un LLM différent du modèle évalué juge la qualité de la sortie. Utilisé pour des critères subjectifs ou ouverts (qualité rédactionnelle, pertinence d'une réponse libre, conformité à un ton).

**Force** : automatisable, scalable (1000 réponses jugées en ~10 min), pas de référence humaine requise pour chaque cas.

**Limite** : le LLM-juge a ses propres biais. À calibrer avec un sous-ensemble de jugements humains pour valider l'alignement.

**Cas type** : juger 200 réponses de support client sur « ton bienveillant + factuellement correct + sources citées ». Coût ~1-5 $ par run de 200 cas.

### Type 2 — Eval offline référence (golden set vs réponse attendue)

Tu disposes d'un **golden set** (corpus de N exemples question → réponse attendue) construit en amont par des experts humains. Tu compares chaque sortie du système IA à la référence par une métrique précise (sous-chaîne match, embedding similarity, structure JSON, etc.).

**Force** : reproductible, métrique objective, traçable.

**Limite** : nécessite l'effort initial de construction du golden set (~1-3 jours pour 50-200 cas). Couvre seulement les cas anticipés.

**Cas type** : golden set 50 questions/réponses pour un RAG documentaire ([[dep-02]] cycle Stitch → Evaluate → Iterate). Métrique : sources retrouvées + concepts ≥ 50 % couverts. Coût ~0,1-1 $ par run complet.

### Type 3 — Eval online utilisateurs réels

Mesure sur un échantillon d'utilisateurs en production. Indicateurs : feedback explicite (thumbs up/down), feedback implicite (taux d'abandon, reformulation, clarification demandée), métriques métier (taux de containment, NPS support, time-to-resolution).

**Force** : mesure ce qui compte vraiment — la perception utilisateur réel sur les cas réels, pas un sous-ensemble curé.

**Limite** : lente (semaines à mois pour avoir un signal stable), nécessite un volume utilisateur suffisant, biaisée par les utilisateurs qui prennent le temps de donner du feedback.

**Cas type** : sample 5 % des conversations support client + thumbs up/down + revue humaine mensuelle sur 100 conversations. Coût infra négligeable, coût humain ~1-2 jour/mois.

### Composition des 3 types

Une organisation mature combine les trois : **Type 2 (offline)** pour la CI/CD à chaque déploiement, **Type 1 (LLM-as-judge)** pour scaler des jugements subjectifs à coût bas, **Type 3 (online)** pour valider que l'expérience réelle correspond aux mesures offline.

## Définitions canoniques Anthropic

À préserver dans l'ordre canonique (Anthropic Engineering 2026) :

- **Eval** : un dataset golden + une métrique de comparaison. L'unité élémentaire d'évaluation.
- **Harness** : l'infrastructure d'exécution autour de l'eval (runner, orchestrateur, gestion artefacts).
- **Multi-turn evaluations** : evals qui mesurent une conversation multi-tours, pas un échange isolé. Critique pour agents conversationnels.
- **State-modifying agents** : agents qui modifient un état externe (base de données, API, fichier). Evals plus complexes car effets de bord à isoler ou rollback.

À utiliser textuellement dans tout référentiel d'eval interne. La cohérence terminologique cross-équipes est un levier d'efficacité.

## Outils d'évaluation 2026 — panorama

Cinq plateformes principales (cf. fiche outils-observabilite-llm à produire post-vague 5+) :

| Outil | Profil | Force différentielle |
|---|---|---|
| **LangSmith** | LangChain native, SaaS | Intégration native LangChain, traces complètes |
| **Phoenix Arize** | Open-source self-host possible | Embeddings drift detection, monitoring offline |
| **Langfuse** | Open-source self-host | Eval + observability unifié, prix bas |
| **Comet Opik** | SaaS focus LLM | LLM-as-judge templates, dashboards |
| **Braintrust** | **Eval-first SaaS** | Outil dédié au type 2 (golden set + CI/CD intégré) |

Choix dépend de la stack existante et de la maturité de l'équipe. Pour démarrer minimaliste, un golden set YAML + un script Python suffisent (pattern POC validé empiriquement, cf. [[dep-02]]).

## Bruit infrastructure dans les evals d'agents — méthode variance N runs

Anthropic Engineering 2026 (*« Quantifying infrastructure noise in agentic coding evals »*) documente un problème spécifique aux agents long-running : **le même agent, sur le même input, peut produire des résultats différents** à cause du bruit d'infrastructure (API timing, network jitter, contexte LLM stochastique).

**Méthode canonique** : exécuter chaque cas de test **N fois** (typiquement N=3-5), mesurer la variance. Si la variance est élevée et la moyenne est dans la cible, le bruit infrastructure est dominant. Si la moyenne est hors cible, c'est une régression réelle du modèle/prompt à corriger.

**Implication pratique** : sur une eval agentic, ne jamais conclure sur un seul run. La méthode 3 runs minimum est devenue standard en 2026 pour les agents long-running.

## Intégration CI/CD — gates de blocage automatique

L'eval pipeline mature s'intègre en CI/CD : chaque commit qui touche au prompt, au modèle, à un script d'extraction déclenche une eval automatique. **Gates de blocage** : si le score eval dégrade en dessous d'un seuil (ex. < 95 % du baseline), le déploiement est bloqué automatiquement.

**Pattern de gates TOML** (cohérent avec [[dep-05]] §8.2) : configuration centralisée des seuils par environnement (dev / staging / prod), audit des changements de seuils en revue PR, alertes Slack/email sur dégradation. Wikilinker [[dep-05]] §8.2 pour le détail opérationnel — ne pas dupliquer.

**Coût eval CI/CD** : ~0,5-2 $ par run selon volume golden set. Sur un projet à 5-10 commits/jour touchant à l'IA, ~150-500 $/mois en frais d'eval automatique. Investissement structurellement rentable (évite les régressions silencieuses).

## Distinction évaluation vs observabilité

À préserver textuellement (formulation canonique HTML) :

> *« La distinction clé : evals (avant déploiement) vs observabilité (après). Les evals répondent à "est-ce que la sortie est bonne ?" avec des datasets golden. L'observabilité (cf. la fiche Agents en production : observabilité) répond à "qu'est-ce qui se passe en prod en ce moment ?". Les deux sont nécessaires et complémentaires. »*

Les deux fonctions s'appuient sur des outillages partiellement communs (LangSmith, Langfuse traitent les deux) mais répondent à des questions distinctes. Confondre les deux = lacune structurelle.

Pour l'observabilité agents en production, voir [[dep-05]] (Agents en production : observabilité et garde-fous).

## Articulation avec DEP-02 — pas de duplication structurelle

Le cycle **Stitch → Evaluate → Iterate** documenté dans [[dep-02]] §6bis (RAG en production) est un cas particulier de l'évaluation continue, spécifique au RAG. Il s'appuie sur les principes du présent module mais avec une instanciation concrète RAG. Pas de duplication structurelle : DEP-07 = méthodologie générale, DEP-02 = application RAG.

## Risques de dérive et points d'attention

**Démarrer sans golden set** : pattern observé fréquemment. « On verra plus tard. » Conséquence : impossibilité de valider toute amélioration ou de détecter une régression. Discipline non négociable, voir « eval first » ci-dessus.

**LLM-as-judge non calibré** : déléguer aveuglément à un LLM-juge sans valider son alignement avec un échantillon humain. Le biais du juge n'est pas mesuré → mesure faussée mais avec apparence d'objectivité. Calibrer périodiquement avec 50-100 jugements humains.

**Confondre eval et observabilité** : « on a notre dashboard LangSmith, on est bons » — non. L'observabilité ne valide pas la qualité, elle décrit l'état. Les deux sont nécessaires.

**Single run sur agent long-running** : ne jamais conclure sur un seul run d'un agent stochastique. Méthode variance N runs canonique (Anthropic 2026).

**Sur-investir le golden set initial** : tenter de couvrir tous les cas dès le départ. Démarrer avec 20-50 cas représentatifs, étendre par vagues selon les régressions observées. La taille moyenne d'un golden set mature est 100-300 cas, pas 10 000.

## Récap actionnable

Pour mettre en place une évaluation continue de qualité IA en production, **fais ces 7 actions** :

1. **Construis un golden set minimum** (10-20 cas) avant de coder le système IA.
2. **Mesure le baseline** dès le premier run avant toute optimisation.
3. **Combine les 3 types d'evals** (LLM-as-judge + offline + online) selon le cycle de vie projet.
4. **Adopte la terminologie canonique Anthropic** (eval / harness / multi-turn / state-modifying).
5. **Intègre en CI/CD** avec gates de blocage sur seuil.
6. **Applique la méthode variance N runs** (3-5) pour les agents long-running.
7. **Distingue évaluation et observabilité** — voir [[dep-05]] pour l'observabilité production.

**Renvois utiles** : [[dep-01]] (Cadrer un projet IA — heuristique anti-hype, à articuler avec « eval first »), [[dep-02]] (RAG en production — cycle Stitch → Evaluate → Iterate spécifique RAG), [[dep-05]] (Agents en production — observabilité complémentaire), [[cu-026]] (Gouvernance des agents IA — dimension 4 KPI agent).

Sources : Anthropic Engineering 2026 (« Demystifying evals for AI agents », « Quantifying infrastructure noise in agentic coding evals »), Hub IA Learning Center.
