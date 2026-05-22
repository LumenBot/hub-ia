---
code: dep-01
titre: "Cadrer un projet IA pour la mise en production"
type: deploiement-dep
axe: B
niveau: 3
tags: [cadrage, heuristique-anti-hype, arbre-decision, jagged-frontier, stanford, architecture, mise-en-production]
version: 3.11.0
last_updated: 2026-05-22
glosaire_termes: [llm, rag, fine-tuning, agent]
derives: ["[[cu-014]]", "[[cu-026]]", "[[dep-02]]", "[[dep-04]]", "[[dep-05]]", "[[pattern-llm-wiki]]", "[[pattern-persistent-memory]]", "[[chiffres-macro-2026]]"]
public_cible: [dirigeant, ops, r&d, tech]
---

# Cadrer un projet IA pour la mise en production

## L'essentiel à retenir

**Comment cadrer architecture IA pour mise en production en 2026 ? Heuristique anti-hype : single LLM call d'abord, scaler seulement si prouvé nécessaire. Arbre de décision technique en 6 niveaux (Single LLM call → Long context → RAG → Fine-tuning → Single agent → Multi-agent), à tester séquentiellement en testant chaque niveau avant de passer au suivant. Concept Jagged Frontier (Stanford AI Index Report 2026) : l'IA n'est pas uniformément bonne — frontière dentelée, excellente sur certaines tâches, défaillante sur d'autres pourtant proches.**

L'heuristique anti-hype 2026 est l'antidote au pattern le plus coûteux du marché : aller directement au multi-agent quand un single LLM call aurait suffi. Le coût caché du sur-engineering architectural ([[chiffres-macro-2026#80-pourcent-entreprises-suppression-postes-sans-gain-roi|80 % des entreprises > 1 Md$ ont supprimé des postes sans gain ROI mesuré]]) trouve souvent sa source dans cette dérive : techno avant problème.

**Règle d'or à préserver textuellement** : *« Single LLM call d'abord, scaler seulement si prouvé nécessaire. »* Tu testes chaque niveau de l'arbre, tu mesures, tu passes au suivant si et seulement si tu as une preuve empirique que le niveau actuel ne suffit pas. Pas de bond architectural par anticipation.

**Le concept « Jagged Frontier »** ([[chiffres-macro-2026#osworld-12-66-task-success-en-un-an-stanford-ai-index-2026|Stanford AI Index Report 2026]]) cadre la deuxième leçon : ne jamais extrapoler d'une démo réussie à un déploiement universel. Une IA qui réussit OSWorld à 66 % en un an échoue encore 1 fois sur 3. Une démo qui marche en POC ne garantit pas une production stable.

**Note** : ce module traite le **cadrage architectural** d'un projet IA (quelle techno choisir). Pour le **cadrage projet** au sens cadrage gestion projet (équipe, budget, planning, gouvernance), voir le futur module PR-09 v3.12 « Cadrer un projet IA » côté préalables.

## À qui ce module s'adresse

Ce module est pour toi si tu pilotes ou tu accompagnes un projet IA destiné à la production ; si tu te demandes « faut-il faire un RAG ou un fine-tuning ou un agent ? » et tu veux une grille de décision plutôt qu'une intuition ; si tu observes un projet partir directement sur multi-agent alors qu'un single LLM call suffirait probablement ; ou si tu veux comprendre pourquoi une IA peut réussir une tâche complexe et échouer sur une autre triviale.

Niveau ⭐⭐⭐ Avancé. ~30 minutes de lecture. Public cible : direction technique, équipes data/R&D, dirigeants opérationnels qui doivent arbitrer une architecture IA.

**Capacités opérationnelles à acquérir** :

1. Appliquer l'heuristique anti-hype en 6 niveaux à un projet IA concret.
2. Tester séquentiellement chaque niveau de l'arbre avant de passer au suivant.
3. Identifier les biais de sur-engineering architectural qui inflate les coûts sans gain mesurable.
4. Cadrer le concept Jagged Frontier pour anticiper les angles morts d'un déploiement IA.
5. Articuler arbre de décision et démo/POC/pilote/production sans extrapolation hâtive.

## Heuristique anti-hype 2026 — single LLM call d'abord

L'**arbre de décision architectural** en 6 niveaux, à tester séquentiellement. Tu commences au niveau 1, tu valides empiriquement que ça ne suffit pas, tu passes au niveau 2, et ainsi de suite.

### Niveau 1 — Single LLM call

L'appel le plus simple : une seule requête à un LLM (Claude, GPT, Mistral) avec un prompt bien construit. Pas de mémoire, pas de retrieval, pas d'orchestration. Si le contexte rentre dans la fenêtre du modèle et la qualité de réponse est satisfaisante, tu n'as **rien d'autre à faire**.

Cas types : génération de contenu standard (résumé, traduction, reformulation), Q&A sur un document court, classification, extraction structurée. Coût ~0,01-0,1 $ par appel selon modèle. Latence < 5 s. Maintenance quasi nulle.

**Critère pour passer au niveau 2** : la tâche nécessite un contexte plus long que la fenêtre standard du modèle ne le permet, OU le single call manque de précision sur des cas spécifiques.

### Niveau 2 — Long context

Tu utilises un modèle à long context (Claude 200K, Gemini 2M, modèles natifs long context comme SubQ qui montent à 10 M tokens et plus — cf. [[pattern-persistent-memory]] signal 1). Tu injectes tout le contexte pertinent dans le prompt. Pas de retrieval ni de chunking — juste plus de tokens en input.

Cas types : analyse d'un document long, comparaison de plusieurs sources, raisonnement sur un corpus moyen (jusqu'à ~100K tokens). Coût ~0,1-1 $ par appel (proportionnel au contexte injecté).

**Critère pour passer au niveau 3** : le contexte total dépasse ce qui rentre raisonnablement dans la fenêtre, OU le coût par requête devient prohibitif sur le volume cible.

### Niveau 3 — RAG (Retrieval-Augmented Generation)

Tu indexes ton corpus dans une base vectorielle (ChromaDB, Qdrant, pgvector — cf. [[outils-vector-db]]) et tu fais une recherche sémantique avant chaque requête pour ne ramener que les chunks pertinents. Détails dans [[dep-02]] (RAG en production — anatomie d'une pipeline) et [[cu-008]] (Knowledge base interne RAG).

Cas types : Q&A sur un corpus large (> 100K tokens), recherche d'information dans un patrimoine documentaire évolutif, support client avec base de connaissance. Coût ~0,01-0,05 $ par requête après l'investissement initial d'indexation.

**Critère pour passer au niveau 4** : le RAG manque de précision sur un domaine spécifique (jargon métier, codes internes) où le modèle générique ne peut pas comprendre sans entraînement complémentaire.

### Niveau 4 — Fine-tuning

Tu spécialises un modèle (typiquement un SLM 1B-8B paramètres) sur ton domaine. Détails dans [[dep-04]] §4bis (Fine-tuning SLM 1B-8B). Le coût initial est élevé (curation données, entraînement, validation) mais l'inférence devient moins chère.

Cas types : génération dans un style très spécifique (juridique, médical, technique propriétaire), classification fine-tunée sur un domaine, traduction spécialisée. Coût initial 1K-10K €, inférence ensuite très basse.

**Critère pour passer au niveau 5** : la tâche nécessite une **action dynamique** dans le monde réel (appel d'API, écriture en base, envoi d'email), pas seulement une réponse textuelle.

### Niveau 5 — Single agent

Tu construis un agent : un LLM qui peut **appeler des outils** (functions, API, base de données) selon le besoin de la tâche. Un seul agent gère le workflow. Détails dans [[dep-05]] (Agents en production — observabilité et garde-fous) et [[cu-026]] (Gouvernance des agents IA).

Cas types : assistant de support client qui peut consulter le CRM et ouvrir un ticket, agent de prise de rendez-vous, agent de tri d'emails. Latence 10-30 s par action. Coût ~0,1-1 $ par action selon complexité.

**Critère pour passer au niveau 6** : la tâche nécessite **plusieurs spécialistes coopérants** dont les rôles sont vraiment distincts (pas juste des sous-tâches qu'un single agent gérerait aussi bien).

### Niveau 6 — Multi-agent

Tu orchestrer plusieurs agents spécialisés qui coopèrent (un agent commercial + un agent juridique + un agent de pricing par exemple). Détails dans [[cu-014]] (Multi-agents par fonction) et [[cu-026]] (Gouvernance des agents IA — pattern Orchestrator).

**Mise en garde forte** : passer en multi-agent multiplie la complexité, les points de défaillance, les coûts d'observabilité. La majorité des cas qu'on croit multi-agent sont en réalité un single agent avec plusieurs outils. Le passage en multi-agent ne se justifie **qu'avec un cas réel de coordination entre spécialistes humains équivalents** (par exemple, un dossier complexe traité par 3 métiers distincts dans l'organisation).

### Règle d'or — Single LLM call d'abord, scaler seulement si prouvé nécessaire

Le sur-engineering architectural est la cause cachée d'une part importante des [[chiffres-macro-2026#95-pourcent-projets-genai-sans-roi-mesurable-mit-nanda-2025|95 % de projets GenAI sans ROI mesurable]] (MIT NANDA 2025). Beaucoup de POC démarrent directement en multi-agent ou RAG complexe quand un single LLM call ou un long context aurait suffi pour valider la valeur. Conséquence : effort de développement disproportionné, observabilité difficile, coûts d'inférence élevés, maintenance lourde — pour une valeur incrémentale faible.

**Application pratique** : avant tout nouveau projet IA, écris le résultat attendu en une phrase. Demande-toi si un single LLM call bien prompté suffirait. Si oui, c'est ta cible. Si non, écris pourquoi avec un test empirique (pas une intuition). Tu débloques l'étape suivante de l'arbre seulement quand tu as cette preuve.

## Jagged Frontier — la frontière dentelée de l'IA en 2026

**Définition canonique à préserver textuellement** (Stanford AI Index Report 2026) :

> *« Jagged Frontier — l'IA n'est pas uniformément bonne ou mauvaise sur tous les sujets. C'est une frontière dentelée : excellente sur certaines tâches, défaillante sur d'autres pourtant proches. »*

Le concept Jagged Frontier cadre la deuxième leçon structurante du cadrage projet IA : **ne jamais extrapoler d'une démo réussie à un déploiement universel**.

### Exemples documentés Stanford 2026 — contraste pédagogique

- **Gemini médaille d'or à l'International Mathematical Olympiad (IMO)** — preuve de capacité de raisonnement mathématique de niveau humain expert
- **MAIS** Gemini réussit **50,1 % seulement** sur la lecture d'une horloge analogique — tâche triviale pour un humain de 8 ans
- **OSWorld** (benchmark d'agents IA sur des tâches OS générales) : passage de **12 % à 66 % de task success en un an** (cf. [[chiffres-macro-2026#osworld-12-66-task-success-en-un-an-stanford-ai-index-2026]])
- **MAIS** **1 échec sur 3 reste** — non négligeable en production

Ces contrastes sont **adjacents** : une IA capable de médaille d'or IMO échoue à lire une horloge. Aucune logique a priori ne permet de prédire où elle réussira et où elle échouera dans une nouvelle tâche.

### Articulation avec l'heuristique anti-hype — 2 angles complémentaires

L'heuristique anti-hype et le Jagged Frontier sont **2 angles distincts mais complémentaires** du cadrage projet IA :

- **Heuristique anti-hype** : choisir l'**architecture la plus simple** qui résout effectivement le problème. Ne pas sur-engineer.
- **Jagged Frontier** : **ne pas extrapoler d'une démo réussie** à un déploiement universel. Tester empiriquement chaque cas d'usage.

À préserver comme 2 sections distinctes dans le cadrage projet. Ne pas fusionner.

## Démo, POC, pilote, production — distinguer les 4 stades

L'arbre de décision et le Jagged Frontier se composent avec une discipline de stade projet à respecter :

| Stade | Objectif | Critère de passage au suivant |
|---|---|---|
| **Démo** | Montrer que c'est techniquement possible (1 cas) | Capacité technique démontrée |
| **POC** ([[glossaire#poc]]) | Valider faisabilité sur 3-5 cas représentatifs | Faisabilité étendue OK |
| **Pilote** | Valider valeur sur un sous-ensemble d'utilisateurs réels (~5-20 utilisateurs) | Valeur métier prouvée + qualité stable |
| **Production** | Servir l'ensemble des utilisateurs cibles avec SLA défini | — |

Un projet IA qui passe d'une démo réussie directement à la production saute 2 stades. Le Jagged Frontier garantit que des cas non-testés vont casser en production. La discipline POC → pilote → production est la mitigation structurelle.

## Risques de dérive et points d'attention

**Confondre cadrage architectural et cadrage projet** : le présent module traite le choix d'architecture IA (techno). Pour le cadrage projet au sens gestion (équipe, budget, planning, gouvernance, ROI), voir le futur PR-09 v3.12 (à produire en vague 6 côté MD RAG).

**Sauter des étapes de l'arbre par impatience** : « on commence direct en multi-agent parce que c'est plus puissant ». Pattern observé empiriquement dans le 95 % MIT NANDA d'échecs IA. La discipline single LLM call d'abord est non négociable.

**Sur-tester l'arbre** : symétrique inverse. Passer 3 mois à comparer single LLM call vs long context vs RAG pour un cas où le single call suffit largement. La discipline est de tester rapidement (1-2 jours par niveau) puis passer.

**Extrapoler d'une démo** : le Jagged Frontier interdit de conclure que parce qu'une IA réussit la tâche X, elle réussira la tâche X' adjacente. Toujours tester X' empiriquement.

**Hallucinations en production** : voir [[vigilance-hallucinations]] pour la discipline anti-hallucination. Tout déploiement production doit intégrer un protocole de détection + correction.

## Récap actionnable

Pour cadrer un projet IA destiné à la production, **fais ces 6 actions** :

1. **Écris le résultat attendu en une phrase** (avant tout choix d'architecture).
2. **Demande-toi si un single LLM call suffit**. Si oui, c'est ta cible. Pas de bond.
3. **Monte l'arbre niveau par niveau** seulement avec une preuve empirique que le niveau actuel ne suffit pas.
4. **Cadre le Jagged Frontier** : liste 3-5 cas d'usage adjacents à ton cas principal. Teste-les empiriquement avant production.
5. **Respecte les 4 stades** démo → POC → pilote → production. Pas de raccourci.
6. **Documente l'arbitrage architectural** dans une page projet partagée (équipe + sponsor).

**Renvois utiles** : [[dep-02]] (RAG en production — étape 3 de l'arbre), [[dep-04]] (Fine-tuning — étape 4), [[dep-05]] (Agents en production — étapes 5-6 observabilité), [[cu-014]] (Multi-agents — étape 6 orchestration), [[cu-026]] (Gouvernance des agents IA — pattern de répartition humain/agent), [[pattern-llm-wiki]] (alternative architecturale pour petits corpus stables), [[pattern-persistent-memory]] (4 signaux convergents mai 2026 + signal 1 long context natif).

Source : Stanford AI Index Report 2026 (concept Jagged Frontier + benchmarks IMO/OSWorld), Hub IA Learning Center (heuristique anti-hype 2026), MIT NANDA 2025 (95 % projets sans ROI).
