# Lot B v3.8 — Enrichissements techniques (CU-008, CU-014, DEP-02, DEP-05)

**Brief consolidé pour Claude Code** : 4 enrichissements éditoriaux ciblés sur des modules existants.

**Sources** : veille v3.7.13 (Grok inputs 2 et 5).

---

## Patch B.1 — CU-008 (Knowledge base RAG) — pattern LLM Wiki post-Karpathy + forks émergents

**Module cible** : `modules/cu-008-knowledge-base-rag.html`
**Position** : nouvelle sous-section dans la section actuelle qui parle du LLM Wiki, OU enrichissement de la section dédiée existante. Titre suggéré : **« Le pattern LLM Wiki post-Karpathy — l'écosystème de mai 2026 »**.

### Contenu à intégrer

#### 1. Le shift architectural (rappel et précision)

Le pattern **LLM Wiki** popularisé par Andrej Karpathy en avril 2026 propose une rupture architecturale par rapport au RAG classique :

- **RAG classique** : `retrieve → answer → forget`. À chaque requête, le système récupère des chunks dans le vector store, les injecte dans le prompt, génère une réponse, et oublie tout. Pas de mémoire de synthèse.
- **LLM Wiki** : `ingest → synthesize → evolve`. Le système maintient une **base de connaissances vivante** que les LLM mettent à jour à chaque ingestion (synthèses, contradictions, évolutions). La mémoire de synthèse devient persistante.

#### 2. Les forks émergents 2026 — l'écosystème se structure

Depuis le gist initial de Karpathy (avril 2026), un **écosystème de forks** s'est développé qui introduit des patterns complémentaires :

- **Persistent memory** : la mémoire de l'agent persiste entre les sessions et entre les utilisateurs (avec gestion de droits)
- **Self-maintaining KB** : la base de connaissances se met à jour automatiquement quand de nouveaux documents sont ingérés (synthèses regénérées)
- **Contradiction detection** : le système identifie automatiquement les contradictions entre nouveaux contenus et synthèses existantes, et alerte
- **Multi-agent vaults** : plusieurs agents spécialisés partagent et enrichissent un vault commun
- **Sleep consolidation** : pattern inspiré du sommeil humain — la base se consolide « hors ligne » pendant les périodes creuses (regénération de synthèses, déduplication, archivage)
- **Graph-based layers** : couche graph (nœuds/relations) ajoutée par-dessus la base markdown pour requêtes structurelles
- **MCP local-first** : intégration MCP servers locaux pour la souveraineté
- **Self-healing knowledge graphs** : le graph détecte les liens manquants ou incohérents et les corrige

#### 3. Implications pour la PME

Trois questions à se poser avant de partir sur un LLM Wiki ou un RAG classique :

1. **Volume du corpus** : < 100 K tokens stable et structuré → LLM Wiki potentiellement plus efficace. Volume large et hétérogène → RAG hybride toujours plus pertinent.
2. **Évolutivité** : tu prévois d'ingérer en continu ? Le LLM Wiki s'enrichit naturellement par synthèse, le RAG nécessite une re-indexation systématique.
3. **Qualité des inputs** : le LLM Wiki dépend très fortement de la qualité des inputs. Inputs structurés (manuels, procédures) → résultats qualité. Inputs hétérogènes (web, YouTube, X crawl) → bruit. C'est un signal documenté en mai 2026.

> 💡 **Heuristique pratique 2026** : itérer cheapest-first. Sur un projet RAG, l'instinct est souvent de prendre « le modèle le plus puissant ». L'inverse est plus rentable : optimiser le retrieval → améliorer les embeddings → puis seulement augmenter la taille du modèle. Cf. retours communauté sur dataset enchères : embedding open-source #130 MTEB bat OpenAI embeddings (+11 % qualité, 240× plus rapide, gratuit).

### Sources à ajouter dans la section finale

À insérer dans la sous-rubrique « 📰 Articles de fond » :
- Compte X @pauliusztin_ — heuristique itérer cheapest-first (mai 2026)
- Compte X @Spacepilot77 — limites LLM Wiki sur inputs non structurés (mai 2026)

À insérer dans la sous-rubrique « 🎓 Tutoriels & cas pratiques » :
- Beever Atlas (fork open-source du pattern Karpathy LLM Wiki) — voir fiche outil dans le Hub

### Renvois internes à mettre à jour

- Renvoyer vers la fiche outil **Beever Atlas** (créée en Lot D)
- Renvoyer vers DEP-02 (RAG en production) qui sera enrichi en parallèle (Lot B.3)

---

## Patch B.2 — CU-014 (Multi-agents par fonction) — principe « agent = employé »

**Module cible** : `modules/cu-014-multi-agents.html`
**Position** : nouvelle section ou sous-section, à intégrer entre la section actuelle « Patterns d'orchestration » et la section « Étude de cas » (ou équivalent). Titre suggéré : **« Principe émergent 2026 — l'agent comme employé »**.

### Contenu à intégrer

#### 1. Le shift de framing 2026

Jusqu'en 2025, le discours dominant sur les agents IA était **techno-centré** : « comment construire ? quelle architecture ? quel framework ? ». En 2026, un nouveau cadrage émerge, contre-courant et plus mature : **traiter l'agent IA comme un employé**. Cela signifie :

- **Une tâche claire et bornée** : un agent ≠ un employé multifonction. Chaque agent a un périmètre de responsabilité défini.
- **Des droits de décision explicites** : que peut décider l'agent seul ? Que doit-il faire valider par un humain ? Que doit-il escalader ?
- **Des points d'escalade documentés** : quand l'agent est en doute, à qui escalade-t-il ? (humain superviseur, autre agent, file d'attente)
- **Une évaluation périodique** : KPI agent comme KPI employé (taux de succès, satisfaction utilisateur, coût, qualité des sorties). Évaluation hebdomadaire ou mensuelle.
- **Des contrôles** : audit des décisions (échantillonnage), revue qualité, garde-fous techniques.
- **Onboarding et offboarding** : un agent qui démarre doit être briefé (système prompt, exemples, contraintes). Un agent qui sort doit être archivé proprement.

#### 2. Pourquoi ce framing fonctionne

Trois raisons documentées :

1. **Il rend la gouvernance lisible pour les non-IT** : le dirigeant comprend mieux « cet agent fait le travail d'un junior commercial » que « ce système est un graphe LangGraph avec des nœuds tool-call ».
2. **Il force la discipline managériale** : si tu traites un agent comme un employé, tu dois lui définir un périmètre, des objectifs, des KPI. Cela évite le « projet IA flou » qui finit en abandon.
3. **Il prépare la conformité réglementaire** : l'AI Act exige une supervision humaine (Article 14) et une traçabilité des décisions. Le pattern « agent = employé » colle naturellement à ces obligations.

#### 3. La grille de gouvernance type

Pour chaque agent en production, documenter :

| Dimension | Question à formaliser |
|---|---|
| Tâche | Quelle est la mission unique de cet agent ? |
| Droits de décision | Que peut-il décider seul ? |
| Points d'escalade | À qui adresse-t-il les cas qui sortent de son périmètre ? |
| KPI | Comment mesure-t-on sa performance ? À quelle fréquence ? |
| Audit | Qui revoit ses décisions ? À quelle fréquence ? |
| Versions | Comment gère-t-on l'évolution de son prompt / modèle / outils ? |
| Onboarding | Quel briefing initial ? |
| Offboarding | Comment archiver son travail si l'agent est désactivé ? |

#### 4. Renvoi vers le module dédié

> 📘 Le **module CU-026 Gouvernance des agents IA** (à créer en parallèle) approfondit ce sujet en module dédié, avec étude de cas complète, framework opérationnel et auto-diagnostic. Le présent module CU-014 reste centré sur l'**architecture multi-agents** ; CU-026 traite du **management** des agents en production.

### Sources à ajouter dans la section finale

À insérer dans la sous-rubrique « 📰 Articles de fond » :
- Compte X @JeromeMONANGE (origine du framing « agent = employé », mai 2026)
- Renvoi vers les sources institutionnelles utilisées dans CU-026 (Anthropic Engineering, NIST AI RMF, ISO 42001)

### Renvois internes à mettre à jour

- Renvoyer explicitement vers **CU-026 Gouvernance des agents IA** (nouveau module v3.8, Lot E)
- Renvoyer vers PR-05 (sécurité IA) et CU-020 (conformité)

---

## Patch B.3 — DEP-02 (RAG en production) — itération continue Stitch → Evaluate → Iterate

**Module cible** : `deploiement/dep-02-rag-architecture-prod.html`
**Position** : nouvelle sous-section dans la section actuelle « Méthode de déploiement » ou « Bonnes pratiques production ». Titre suggéré : **« Le cycle d'itération continue — Stitch, Evaluate, Iterate »**.

### Contenu à intégrer

#### 1. Le constat 2026 sur le RAG en production

Constat largement documenté en 2026 : **rien sur les leaderboards ne prédit la performance d'un RAG sur tes données spécifiques**. Les benchmarks publics (MTEB, BEIR, etc.) testent sur des datasets génériques. Sur ton corpus métier, l'écart entre la performance benchmark et la performance réelle peut être significatif.

**Implication pratique** : tu ne peux pas choisir ton stack RAG sur la base des leaderboards. Tu dois **itérer sur tes données réelles**.

#### 2. Le cycle Stitch → Evaluate → Iterate

Le pattern d'itération continue qui s'impose en 2026 :

1. **Stitch** : assembler une première version du pipeline (chunking + embeddings + retrieval + reranking + génération) avec des choix par défaut raisonnables. Ne pas chercher l'optimum dès le départ.
2. **Evaluate** : évaluer la performance sur un **eval set réel** (50-200 cas représentatifs de tes données et requêtes), avec un **LLM Judge aligné sur le feedback humain** (calibrer le LLM Judge sur 10-20 cas annotés humain).
3. **Iterate** : modifier un seul composant à la fois (changer d'embedding, ajuster le chunking, ajouter un reranker, etc.), réévaluer, comparer.

#### 3. RetEx documenté — embeddings open-source qui battent OpenAI

Cas documenté mai 2026 : sur un dataset d'enchères, un embedding open-source classé **#130 sur le leaderboard MTEB** a battu les embeddings d'OpenAI (#1 du leaderboard) :

- **+11 % de qualité** (mesurée sur l'eval set spécifique au dataset)
- **240× plus rapide** (latence par requête)
- **Gratuit** (vs coût API OpenAI)

**Leçon** : les leaderboards ne prédisent pas la performance sur tes données. L'eval set sur ton corpus est le seul juge fiable.

#### 4. Implication pour la PME

- **Construire son eval set** est l'investissement le plus rentable d'un projet RAG en production. Coût : 1-3 jours de travail manuel pour annoter 50-200 cas. ROI : permanent (tout choix futur s'évalue dessus).
- **Itérer cheapest-first** : changer le chunking ou ajouter un reranker coûte moins cher que changer le modèle de génération. Le réflexe « plus gros modèle » est souvent le plus coûteux et le moins efficace.
- **LLM Judge aligné** : utiliser un LLM (Claude, GPT) comme juge automatisé pour scorer les sorties contre les attendus, mais **calibrer ce juge sur 10-20 cas annotés humain** pour vérifier qu'il reproduit ton jugement.

### Sources à ajouter dans la section finale

À insérer dans la sous-rubrique « 📰 Articles de fond » :
- Compte X @pauliusztin_ — Stitch / Evaluate / Iterate + RetEx embedding #130 (mai 2026)

### Renvois internes à mettre à jour

- Renvoyer vers DEP-07 (Évaluation continue et qualité IA) qui détaille les eval sets
- Renvoyer vers le pattern LLM Wiki dans CU-008 (alternative au RAG)

---

## Patch B.4 — DEP-05 (Agents en production) — bottlenecks data plane vs LLM call

**Module cible** : `deploiement/dep-05-agents-observabilite.html`
**Position** : nouvelle sous-section dans la section actuelle sur la performance ou la production. Titre suggéré : **« Le nouveau bottleneck — data plane vs LLM call »**.

### Contenu à intégrer

#### 1. Le shift d'attention 2026

Jusqu'en 2025, le focus dominant sur les agents IA en production était **le LLM call** : optimiser les prompts, le caching, le choix de modèle. En 2026, un nouveau constat émerge : **les bottlenecks d'un système agentic en production ne sont plus dans le LLM, mais dans le data plane** (sérialisation, coordination, transit de données entre composants).

#### 2. Le pattern AAFLOW (runtime distribué agentique)

Un nouveau framework apparu en 2026 illustre cette tendance : **AAFLOW** propose un **unified distributed runtime** pour les pipelines agentic :

- **Zero-copy serialization** sur Apache Arrow / Cylon (pas de désérialisation/sérialisation entre les étapes)
- **Operator abstraction** (chaque étape du pipeline est un opérateur composable)
- **Resource-deterministic scheduling** (planification déterministe, pas best-effort)
- **Speedup pipeline jusqu'à 4,64×** documenté sur des benchmarks publics

#### 3. L'appel à plus de « system engineering »

Le message émergent en 2026 dans la communauté technique : **le context engineering est devenu mature, le system engineering reste le défi**. Les agents en production échouent souvent non pas parce que le prompt est mauvais, mais parce que la coordination entre composants (retrieval → reranking → tool call → génération → action externe) est mal architecturée.

**Implication pour la PME** : si ton agent est lent ou cher en production, ne commence pas par changer de modèle. Audite d'abord le data plane :
- Combien de fois tes données sont-elles sérialisées/désérialisées dans le pipeline ?
- Combien de hops réseau y a-t-il entre le user et la réponse finale ?
- Combien de tool calls successifs ?
- Y a-t-il des aller-retours redondants ?

#### 4. Outils 2026 à connaître

- **AAFLOW** (cf. fiche outil dans le Hub — Lot D)
- **LangGraph** (déjà très répandu) — gère la coordination mais pas l'optimisation data plane
- **Ray** (framework Python) — pour scaler les pipelines agentic horizontalement

### Sources à ajouter dans la section finale

À insérer dans la sous-rubrique « 📰 Articles de fond » :
- Compte X @omarsar0 — AAFLOW + bottlenecks data plane (mai 2026)

### Renvois internes à mettre à jour

- Renvoyer vers la fiche outil **AAFLOW** (créée en Lot D)
- Renvoyer vers DEP-06 (Inférence et coûts) qui touche à l'optimisation

---

## Synthèse Lot B pour Claude Code

**Volume** : 4 enrichissements éditoriaux ciblés sur 4 modules existants.

**Effort estimé Claude Code** : 2-3 h.

**Composants à utiliser** : pas de nouveau composant, réutilisation des composants centralisés (`.callout-info`, `.tool-table` pour la grille de gouvernance B.2, `.pull-quote` pour les heuristiques).

**Cohérence numérique** : aucun changement de chiffre structurel.

**Renvois inter-lots** : B.1 et B.4 renvoient vers des fiches outils créées en Lot D (Beever Atlas, AAFLOW). B.2 renvoie vers le nouveau module CU-026 créé en Lot E. À orchestrer dans l'ordre des commits.

## Note Cowork

Sources prioritaires utilisées : comptes X identifiés (Karpathy via gist, @pauliusztin_, @omarsar0, @Spacepilot77, @JeromeMONANGE), sourcing technique de référence. Aucune source non institutionnelle ou non technique. Conforme RULES § 1.1.
