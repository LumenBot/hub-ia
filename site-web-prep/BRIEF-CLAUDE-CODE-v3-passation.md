# Brief Claude Code — Hub IA Learning Center (passation V3)

**Auteur :** Blaise Cavalli — Startup Manager Quai Alpha (Quest for Change)
**Date :** mai 2026
**Repo :** https://github.com/LumenBot/hub-ia
**Branche cible :** main
**Hébergement :** GitHub Pages

---

## 0. Contexte du projet

Le Hub IA Learning Center est un site éducatif que je porte au sein du réseau Quest for Change. Il agrège **19 modules pédagogiques** (CU-001 à CU-019) couvrant les usages IA pour PME/ETI, des fondamentaux à l'agentique avancée. Le mockup V3 vient d'être finalisé en local — architecture mutualisée (`module-v3.css` / `module-v3.js`), sticky sidebar TOC, executive summary, sections numérotées, 3 formats pédagogiques par niveau.

**Cette itération a 3 objectifs majeurs** :
1. **Branding & identité** — passer de « Hub IA » à « Hub IA — Learning Center » avec branding Quest for Change officiel et bandeau incubateurs partenaires
2. **Cohérence visuelle** — auditer et corriger l'homogénéité des 19 modules après push (le front est actuellement cassé sur certains modules en ligne car les fichiers mutualisés n'étaient pas encore poussés)
3. **Page Ressources** — créer une nouvelle section qui sert de wiki / glossaire / dictionnaire des outils IA mentionnés dans les modules

---

## 1. Lot 1 — Refonte structure & branding (livrable 1)

### 1.1 Renommage du site

Partout dans le site (titre, balises `<title>`, header `<nav>`, footer, OpenGraph) :
- **Avant** : « Hub IA territorial »
- **Après** : « Hub IA — Learning Center »

### 1.2 Logos & bandeau partenaires

**6 logos requis** (à déposer dans `mockup/assets/logos/`) :

| Fichier attendu | Usage | Notes |
|---|---|---|
| `qfc.svg` ou `qfc.png` | Header principal + footer (logo brand) | Quest for Change — logo principal du site |
| `quai-alpha.png` | Bandeau partenaires footer | Incubateur — logo blanc sur fond sombre |
| `the-pool.png` | Bandeau partenaires footer | Incubateur — logo blanc sur fond sombre |
| `semia.png` | Bandeau partenaires footer | Incubateur — logo gris/rouge |
| `innovact.png` | Bandeau partenaires footer | Incubateur — logo blanc sur fond sombre |
| `rimbaud-tech.png` | Bandeau partenaires footer | Incubateur — logo blanc sur fond sombre |

**Note :** Les logos sources sont fournis par Blaise dans le repo (à déposer manuellement dans `mockup/assets/logos/` au moment du push). Format préféré : SVG pour QFC, PNG haute résolution avec transparence pour les incubateurs.

**Header / nav** :
- Remplacer `<span class="nav-logo">🧭</span>` par `<img src="assets/logos/qfc.svg" alt="Quest for Change" class="nav-logo">`
- Le titre `<span class="nav-title">` devient « Hub IA — Learning Center »
- Logo cliquable → retour à `index.html`

**Footer** :
- Logo principal QFC à gauche
- Texte « Un programme du réseau Quest for Change · Mai 2026 »
- **Nouveau bandeau partenaires** : ligne séparée avec les 5 logos incubateurs (Quai Alpha, The Pool, SEMIA, Innovact, Rimbaud'Tech), titre « Incubateurs partenaires », tailles homogènes, niveaux de gris ou désaturés au repos avec hover couleur, espacement 24px minimum entre logos

### 1.3 Refonte page « À propos »

Remplacer la section actuelle par le texte suivant (à valoriser visuellement) :

> Le Hub IA — Learning Center est une initiative portée par Quest for Change, à destination de ses incubateurs territoriaux, des startups accompagnées et de leurs alumni, des partenaires institutionnels, et des entreprises du territoire au sens large.
>
> L'objectif : disséminer les connaissances autour des enjeux et applications de l'IA, au service du développement économique territorial et de la compétitivité de nos entreprises.
>
> Le savoir ne devrait pas être une ressource exclusive. Seule l'exécution compte.
>
> **Contact :** [blaise.cavalli@questforchange.eu](mailto:blaise.cavalli@questforchange.eu)
>
> Toute remarque, suggestion ou retour d'expérience sur les cas d'usage présentés est bienvenue — l'objectif est d'améliorer la qualité du contenu et d'en sourcer de nouveaux.

### 1.4 Email de contact (remplacement global)

Remplacer **partout** dans le site `contact@questforchange.eu` → `blaise.cavalli@questforchange.eu` (mailto, footer, page À propos, autres mentions).

### 1.5 Suppression des labels catégorie sur l'index

Sur la page d'accueil (`index.html`), supprimer les badges « 🟢 Fondamentaux », « 🟡 Applications métier », « 🔴 Industrialisation » sur les cartes des modules. Ils sont **redondants** avec le filtre niveau qui est déjà présent. Les badges « axe » (📚 Productivité, 🧭 Décision, etc.) et le tag « durée » sont conservés.

### 1.6 Ajout tags « Architecture agentique » manquants

Ajouter le badge `🤖 Architecture agentique` (style violet `#F8F4FF`/`#4A3A8C`/`#7A5CB8`) sur :
- **CU-010 Pipeline contenu social** (4 agents en chaîne documentés)
- **CU-019 Newsletter locale** (5 sub-agents documentés)

À placer dans `<div class="module-badges">` après les badges axe(s) et avant le badge niveau, avec un lien vers `index.html?axe=agentique#modules`.

### 1.7 Renommage catégorie de niveau N7-N8

Le label de la **catégorie** N7-N8 devient « **Usages avancés / experts** » (au lieu d'« Industrialisation »).

Important : le **badge** rouge « 🔴 Industrialisation » sur les modules N3 reste — c'est un tag de niveau spécifique (≥ niveau 7 sur l'échelle MOR-IA). Le renommage concerne uniquement le **filtre/regroupement** sur la page index.

Cohérence des libellés à l'index :
- N1-N3 : **Fondamentaux**
- N4-N6 : **Applications métier**
- N7-N8 : **Usages avancés / experts**

Le tag « Architecture agentique » devient un **label transverse** indépendant des niveaux — il peut apparaître sur des modules N4-N6 (CU-010, CU-019) ou N7-N8 (CU-012-015), selon la complexité réelle.

### 1.8 Push fichiers mutualisés et audit cohérence visuelle

**Critique** : les fichiers `mockup/css/module-v3.css` et `mockup/js/module-v3.js` doivent être correctement poussés — c'est probablement la cause du front cassé sur les modules en ligne (ex : CU-011). Vérifier que ces 2 fichiers existent bien dans le repo et qu'ils sont bien référencés par les 19 modules.

Après push, **auditer la cohérence visuelle des 19 modules** :
- Hero hauteur uniforme
- Sticky TOC opérationnel sur tous (avec scroll-spy actif)
- Executive summary rendu correctement
- SVG schemas correctement dimensionnés
- Sections numérotées uniformes
- Footer aligné

Liste des 19 modules à passer en revue :
- CU-001 Recherche & veille augmentée
- CU-002 Assistant rédactionnel personnel
- CU-003 Comptes-rendus de réunion
- CU-004 Traduction multi-langues
- CU-005 Devis & propositions
- CU-006 Qualification leads chatbot
- CU-007 CV & entretiens RH
- CU-008 Knowledge base RAG
- CU-009 Content repurposing
- CU-010 Pipeline contenu social
- CU-011 Veille concurrentielle
- CU-012 Veille AAP + drafting
- CU-013 Workflow email → CRM
- CU-014 Multi-agents par fonction
- CU-015 Stripe Minions / agents codeurs
- CU-016 Maintenance prédictive
- CU-017 Contrôle qualité vision IA
- CU-018 Optimisation production
- CU-019 Newsletter locale

**Livrable Lot 1 :** PR avec preview GitHub Pages fonctionnel sur les 19 modules + page d'accueil + page À propos refondue.

---

## 2. Lot 2 — Page Ressources V1 (livrable 2)

### 2.1 Concept

Une nouvelle page `ressources.html` accessible depuis le menu de navigation principal. Elle sert de **wiki / glossaire / dictionnaire** des outils IA mentionnés dans les modules. Logique inspirée des modules :
- Sticky sidebar TOC
- Executive summary en page 1
- Catégorisation claire
- Progressivité des informations
- Lien retour depuis chaque module vers la fiche outil correspondante

### 2.2 Architecture éditoriale

Distinguer **2 grandes familles** :

**A. Outils SaaS propriétaires** (avec abonnement / licences)
- LLM commerciaux : Claude (Anthropic), GPT (OpenAI), Mistral (souverain EU), Gemini (Google), Le Chat
- Plateformes orchestration no-code : Make, Zapier, n8n Cloud
- Plateformes content : Beehiiv, Substack, Buttondown, Buffer, Typefully
- IDE / agents code : Cursor, Devin, GitHub Copilot
- Vision industrielle : Cognex, Keyence, Landing AI
- Vector store managés : Pinecone, Qdrant Cloud
- Autres SaaS : Perplexity, NotebookLM, Otter.ai, Fireflies, DeepL Pro

**B. Outils open-source / libraries**
- LLM open : Llama, Mistral open-weight, Qwen, Kimi K2, Mixtral
- Frameworks agents : LangGraph, CrewAI, AutoGen, OpenClaw, Aider
- Vector stores self-hosted : Qdrant OSS, Postgres pgvector, ChromaDB
- ML frameworks : PyTorch, TensorFlow, YOLO, Stable-Baselines3, Mask R-CNN
- Orchestration self-hosted : n8n self-hosted, Dify, Flowise
- Scraping : Scrapling, Apify
- Optimisation : OR-Tools (Google), CPLEX, OpenSolver

### 2.3 Démarrage V1 — 15 outils prioritaires avec deep-dive

**Liste prioritaire à traiter en V1** (fiches détaillées 1 page chacune) :

1. **Claude (Anthropic)** — LLM SaaS, long-form, Claude Projects, Claude Code
2. **GPT-4 / GPT-5 (OpenAI)** — LLM SaaS, robustesse industrielle, tools-use
3. **Mistral (souverain EU)** — LLM SaaS + open-weight, souveraineté EU, Mistral Forge
4. **n8n** — orchestration self-hosted (open-source) + cloud, référence pour les workflows agentiques
5. **Make** — orchestration no-code, alternative cloud rapide
6. **Cursor** — IDE avec mode Composer agent autonome
7. **Claude Code** — agent codeur autonome CLI Anthropic
8. **OpenClaw** — framework agentique émergent, cité par communauté ZHC
9. **LangGraph** — framework Python multi-agents avec mémoire partagée
10. **CrewAI** — alternative LangGraph plus accessible
11. **Qdrant** — vector store open-source de référence pour RAG / mémoire agents
12. **Beehiiv** — plateforme newsletter (Lot 2 cas-école Barcelona Brief)
13. **Perplexity** — recherche augmentée + Spaces, veille structurée
14. **AgentMail** — infrastructure email autonome pour agents, citée ZHC
15. **YOLO + OpenCV** — vision industrielle open-source de référence

### 2.4 Format de fiche outil (deep-dive)

Inspiré de l'architecture V3 des modules. Structure type :

```
[Hero]
- Logo / icône outil
- Badges : SaaS ou Open-source · Catégorie (LLM, Orchestration, Vision, etc.) · Maturité (Établi / Émergent)
- Titre + sous-titre

[Sticky TOC à gauche]
- Synthèse rapide
- 1. Qu'est-ce que c'est
- 2. À quoi ça sert
- 3. Quand l'utiliser (et quand ne pas)
- 4. Stack et intégrations
- 5. Modèle économique / coût
- 6. Cas d'usage dans nos modules
- 7. Alternatives
- 8. Pour aller plus loin

[Executive summary]
- 1 paragraphe « pourquoi cet outil compte »
- 4 takeaways clés
- Stats (date de création, nombre d'users, point fort, point faible)
- Quand l'utiliser

[Sections]
1. Qu'est-ce que c'est — description, fondateurs, philosophie
2. À quoi ça sert — usages canoniques avec exemples concrets
3. Quand l'utiliser (et quand ne pas) — discipline d'arbitrage
4. Stack et intégrations — comment l'intégrer (API, MCP, n8n, Python)
5. Modèle économique / coût — pricing, free tier, plans
6. Cas d'usage dans nos modules — liens vers CU-XXX qui le mentionnent
7. Alternatives — autres outils du même usage
8. Pour aller plus loin — doc officielle, tutoriels, communautés
```

### 2.5 Index complet (par catégorie, format fiche courte)

Pour les 60-70 autres outils mentionnés dans les modules (au-delà des 15 deep-dives), créer un **index par catégorie** avec fiches courtes (3-5 lignes) :

**Catégories proposées :**
- 🧠 LLM & modèles génératifs
- 🛠️ Orchestration & workflows agentiques
- 🤖 Frameworks multi-agents
- 💾 Vector stores & RAG
- 📨 Email & messaging pour agents
- 🌐 Scraping & collecte web
- 👁️ Vision industrielle
- 🧮 Recherche opérationnelle & optimisation
- 📊 Outils de productivité augmentée
- 📰 Plateformes content & newsletter
- 🇪🇺 Solutions souveraines / françaises

### 2.6 Liens depuis modules vers fiches outils

Dans chaque module, quand un outil est mentionné en `<strong>Outil</strong>`, ajouter un lien vers la fiche outil correspondante dans la page Ressources. Format suggéré :

```html
<a href="../ressources.html#claude" class="tool-link">Claude</a>
```

avec un style discret (souligné fin, hover plus marqué).

**Critère** : seuls les outils qui ont une fiche dans Ressources sont liés. Les autres restent en `<strong>` simple.

### 2.7 Navigation

Ajouter « **Ressources** » dans le menu principal de navigation, entre « Modules » et « Axes ».

**Livrable Lot 2 :** page `ressources.html` avec 15 fiches outils deep-dive + index complet par catégorie + liens depuis ≥ 5 modules pilotes (à préciser ensemble).

---

## 3. Lot 3 — Extensions par lots (livrable 3+)

Une fois Lot 2 validé, étendre la page Ressources par **lots de 10-15 outils supplémentaires** (deep-dives ou enrichissement de l'index par catégorie). Cadence à définir avec Blaise selon les retours utilisateurs.

**Outils candidats pour Lot 3 (par ordre de pertinence)** :
- Devin, Aider, GitHub Copilot Workspace
- AutoGen (Microsoft), Dify, Flowise
- Kimi K2, Llama, Mixtral
- ChromaDB, Postgres pgvector
- NotebookLM, Otter.ai, Fireflies
- DeepL Pro, Whisper, Goodweek, EthiqAIS
- Cognex, Keyence, Landing AI, Cadwork, TopSolid, Lectra
- Apify, Composio, Brand24, Crayon, Klue
- IBM CPLEX, FICO Xpress, OR-Tools deep-dive
- HubSpot, Pipedrive, Salesforce, Monday.com
- Mistral Forge (souveraineté EU)

---

## 4. Spécifications techniques transverses

### 4.1 Stack
- HTML5 / CSS3 / Vanilla JavaScript (pas de framework, GitHub Pages compatible)
- Pas de build step nécessaire
- Mobile-friendly (responsive sur les 3 viewports : mobile, tablet, desktop)

### 4.2 Architecture mutualisée existante (à conserver)
- `mockup/css/style.css` (design system de base)
- `mockup/css/module-v3.css` (architecture V3 mutualisée — sticky TOC, executive summary, sections numérotées)
- `mockup/js/module-v3.js` (reading progress, scroll-spy, toggle TOC)

### 4.3 Conventions de naming
- Fichiers HTML : kebab-case
- Classes CSS : kebab-case avec préfixe scope (`module-`, `tool-`, `nav-`, etc.)
- IDs : kebab-case
- Variables JS : camelCase

### 4.4 Accessibilité
- Tous les images ont des `alt` descriptifs
- Hiérarchie `<h1>` → `<h6>` respectée
- Contraste suffisant (WCAG AA minimum)
- Navigation clavier opérationnelle

---

## 5. Livrables et validation

### 5.1 Format de livraison
- 1 PR par lot (3 PR au total minimum)
- Branche feature → main
- Preview GitHub Pages fonctionnel sur la branche avant merge

### 5.2 Validation Lot 1
- Le site visible à `https://lumenbot.github.io/hub-ia/` doit afficher :
  - Logo Quest for Change dans le header
  - Bandeau partenaires en footer
  - Page À propos refondue
  - Email contact correct partout
  - 19 modules accessibles avec rendu V3 cohérent (sticky TOC fonctionnel, exec summary visible, sections numérotées)
- Test croisé sur Chrome, Firefox, Safari (desktop + mobile)

### 5.3 Validation Lot 2
- Page Ressources accessible depuis menu nav
- 15 fiches outils deep-dive complètes et cohérentes entre elles
- Index par catégorie navigable
- Liens depuis ≥ 5 modules pilotes opérationnels

### 5.4 Validation Lot 3+
- Cadence à définir avec Blaise (revue mensuelle suggérée)

---

## 6. Questions ouvertes à confirmer avec Blaise avant démarrage

Aucune ! Le brief est complet. Blaise a validé :
- Démarrage V1 page Ressources avec 15 outils prioritaires (extension par lots ensuite)
- Renommage catégorie N7-N8 en « Usages avancés / experts »
- Tag « Architecture agentique » ajouté à CU-010 et CU-019
- Brief intégral d'un coup, livrables intermédiaires par lot

---

## 7. Notes additionnelles

### 7.1 Positionnement éditorial
Le ton du Hub IA Learning Center est **pragmatique et opérationnel**. Pas de jargon inutile. Vocabulaire QFC respecté quand pertinent (SUM, Starter Class, Comité d'Engagement, etc.). Les modules incarnent cette philosophie : « le savoir ne devrait pas être une ressource exclusive ; seule l'exécution compte ».

### 7.2 Public cible
- SUMs et PMs des incubateurs Quest for Change
- Startups accompagnées et alumni
- PME et ETI du territoire (industriels, services B2B, créateurs de contenu)
- Partenaires institutionnels (Région Grand Est, Bpifrance, Cluster IA Grand Est ENACT, fondations universitaires)

### 7.3 Pipeline de retours
Après mise en ligne du Lot 1, Blaise va diffuser largement le site dans son réseau pour collecter des retours. Ces retours alimenteront :
- L'amélioration éditoriale des cas d'usage existants
- Le sourcing de nouveaux cas d'usage (CU-020+)
- L'enrichissement de la page Ressources

---

**Contact pour questions techniques pendant la mission :**
Blaise Cavalli — blaise.cavalli@questforchange.eu

**Bonne mission, et merci pour le travail !**
