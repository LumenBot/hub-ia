# Debrief Claude Cowork — Hub IA Learning Center (post-itérations Lots 5, 6 et v3.1)

**Auteur :** Blaise Cavalli — Startup Manager Quai Alpha (Quest for Change)
**Date :** mai 2026
**Repo :** https://github.com/LumenBot/hub-ia
**Site live :** https://lumenbot.github.io/hub-ia/
**Branche actuelle :** `feat/v3.1-corrections-globales` (à merger)

---

## 0. Contexte court

Hub IA Learning Center = site éducatif (19 modules CU-001 → CU-019) qui couvre l'IA appliquée aux PME/ETI, du quiz N1 à l'étude de cas N8. Architecture front statique (HTML/CSS/JS vanilla, pas de build, GitHub Pages). Contenu pédagogique mutualisé via `module-v3.css` / `module-v3.js`.

Depuis ton dernier brief (passation V3, début mai 2026), nous avons enchaîné 4 itérations majeures avec Claude Code. Ce document fait le point pour que tu reprennes la main avec le contexte complet — soit pour approfondir le contenu, soit pour faire de la veille sur de nouveaux cas d'usage / outils, soit pour challenger les itérations récentes.

---

## 1. Itérations menées depuis ton dernier brief

### 1.1 Lot 5 — Page Ressources V2.5 (PR #11, mergée)

Passage **39 → 51 fiches outils** en deep-dive. 12 nouvelles fiches structurées :

- **LLM** : Qwen (Alibaba — multilingue, alternative Llama/Mistral pour usages internationaux)
- **Productivité** : Fireflies.ai (focus conversation intelligence + analytics commerciaux)
- **Agents codeurs** : GitHub Copilot Workspace (workflow natif issue → PR)
- **Souverains français QFC** : Spinalia (Marjory Canonne, Épinal — diagnostic IA et plan d'action PME)
- **CRM (3 nouvelles)** : Pipedrive (pipeline-first), Salesforce (Customer 360 + Agentforce), Attio (CRM next-gen API-first)
- **Compétitive intelligence (2 nouvelles)** : Brand24 (social listening PME), Crayon (battlecards auto)
- **Vision industrielle (2 nouvelles)** : Keyence (concurrent japonais Cognex), Landing AI (Andrew Ng — no-code pour PME sans équipe ML)
- **Métier industriel** : Cadwork (CAO/CAM filière bois, nesting matière)

**Nouveauté structurelle :** création d'une 14ᵉ catégorie **🔍 Compétitive intelligence & veille** dans l'index.

### 1.2 Lot 6 — Page Ressources V3.0 (PR #12, mergée)

Passage **51 → 63 fiches outils** — couverture complète des outils mentionnés dans les modules. 12 nouvelles fiches :

- **LLM** : Kimi K2 (Moonshot — long context jusqu'à 2M tokens)
- **Productivité** : tl;dv (replay réunion AI, approche Loom-style)
- **Vision (2)** : Roboflow (annotation + training dataset), Mask R-CNN (segmentation pixel-level)
- **Métier industriel (2)** : TopSolid (Missler, France — CAO/CAM métal/bois), Lectra (France — leader textile/cuir)
- **Optimisation (2)** : Gurobi (solveur premium), FICO Xpress (banque/finance/supply chain)
- **CRM (2)** : Microsoft Dynamics 365, Zoho CRM
- **Compétitive intel** : Klue
- **ML frameworks** : PyTorch (Meta — référence 2026)

**Nouveauté structurelle :** création d'une 15ᵉ catégorie **🛠️ ML frameworks & training** (PyTorch deep-dive + index TensorFlow / JAX / HuggingFace Transformers / PyTorch Lightning / Stable-Baselines3).

État après Lot 6 : 63 deep-dives, 90+ outils indexés, 15 catégories, 130 liens depuis les 19 modules.

### 1.3 v3.1 — Corrections globales (PR à créer, branche `feat/v3.1-corrections-globales`)

**8 corrections macros** demandées par Blaise après lecture exhaustive du site :

#### 1.3.1 Head banner refondu (commit `37e6f5f`)
- Layout grid 3 zones : titre à gauche · logo QFC grand centré (×3-4) · liens à droite.
- `--nav-height: 64px` → `96px`. Logo : `height: 72px`.
- HTML refactoré sur les 24 fichiers (index, ressources, 19 modules, 3 templates).

#### 1.3.2 TOC cassés sur 8 modules (commit `8abd9be`)
- 8 modules (CU-011, 012, 013, 014, 015, 017, 018, 019) utilisaient une structure `.module-toc-header / .module-toc-nav` non stylée.
- Fix : ajout du CSS dans `module-v3.css` + JS scroll-spy étendu pour supporter les 2 structures (`.module-toc-list a, .module-toc-nav a`).

#### 1.3.3 Scrub jargon CU-XXX (commit `0dcf22f`)
- Préfixes `CU-XXX` retirés des liens internes sur la page Ressources (ex: `CU-008 — Knowledge base RAG` → `Knowledge base RAG`).

#### 1.3.4 Reframing géographique (commit `b3344e1`)
- 33 mentions « vosgien / Vosges / Épinal » remplacées par « Grand Est / réseau QFC » sur 5 modules (CU-011, 016, 017, 018, 019).
- Vosges conservé comme **exemple concret**, plus comme prisme exclusif.
- CU-018 (optimisation production) ajusté pour le contexte ENSTIB / LERMAB / CRAN (Épinal-Nancy).

#### 1.3.5 Refonte archi-block (commit `aa33ee2`)
- Les blocs « Architecture de référence » étaient en ASCII dans une boîte bleue marine — illisible.
- Refonte en composant visuel `.archi-flow` (HTML/CSS structuré) sur 7 modules : CU-012, 013, 014, 015, 016, 017, 018.
- Sous-composants : `.archi-flow-section`, `.archi-step`, `.archi-arrow`, `.archi-branches`, `.archi-branch`.
- 6 variants sémantiques colorées : `.is-trigger` (orange), `.is-agent` (violet), `.is-output` (vert), `.is-store` (bleu), `.is-human` (rouge), `.is-decision` (jaune).

#### 1.3.6 Page Ressources réorganisée (commit `b8bf744`)
- **Sommaire** passé d'une liste chronologique de 63 entrées à un sommaire structuré par 15 catégories d'usage.
- **Nouvelle section « Légende des badges »** placée entre la Synthèse et les fiches outils. Explique les 4 dimensions :
  - Type / modèle économique (SaaS, Open-source, Open-weight, Hybride)
  - Catégorie d'usage (LLM, Orchestration, etc.)
  - Maturité (N1-N3 quiz · N4-N6 pilote · N7-N8 mise à l'échelle)
  - Souveraineté 🇪🇺 (éditeur basé UE/France, hébergement UE possible)
- **12 outils EU/français** badgés `🇪🇺 Souverain` : Mistral, Mixtral, Qdrant, Mistral Forge, Goodweek, EthiqAIS, NIN-IA, Spinalia, DeepL Pro, Cadwork, TopSolid, Lectra, tl;dv.
- **3 nouveaux variants CSS `.tool-badge`** : `sovereign`, `hybrid`, `openweight`.
- **Nouvelle catégorie 16ᵉ « 🪵 Métier industriel »** dans le TOC pour Cadwork / TopSolid / Lectra.

#### 1.3.7 Bibliographie transverse (commit `899a5c9`)
- **Nouvelle section dédiée** sur ressources.html (`#bibliographie`) pour centraliser ce qui était duplicué dans les modules :
  - 📊 **Études & rapports** : AI Index Stanford, State of AI, Bpifrance Le Lab, France Num, CNIL IA & RGPD, EU AI Act, OECD AI Policy Observatory, McKinsey State of AI
  - 💬 **Communautés** : HuggingFace Hub, r/LocalLLaMA, LangChain Discord, n8n Community, QFC alumni, Hub France IA, French Tech
  - 📰 **Newsletters** : Import AI, The Batch, Ben's Bites, Latent Space, Génération IA, Goodweek
  - 🎥 **Tutoriels & formations** : DeepLearning.AI, HuggingFace Course, Anthropic docs, OpenAI Cookbook, 3Blue1Brown, Karpathy Zero-to-Hero, OpenClassrooms
  - 📖 **Livres** : Chip Huyen, Burkov, Luc Julia, Yann Le Cun, Stuart Russell
  - ✍️ **Blogs de référence** : Anthropic Research, OpenAI, DeepMind, Mistral, Simon Willison, Sebastian Raschka
- **Pointer ajouté** dans le « Pour aller plus loin » des **19 modules** (callout `callout-info`) qui renvoie vers `ressources.html#bibliographie`.
- **Fix URL Bpifrance Le Lab** cassée (`bpifrance-lelab.fr/etudes-et-rapports` → `lelab.bpifrance.fr`) sur CU-001, CU-002, CU-005.
- **Nouveau composant CSS** : `.callout` / `.callout-info` / `.callout-warn` / `.callout-success`.

---

## 2. État final du site

| Métrique | Valeur |
|---|---|
| Modules pédagogiques | 19 (CU-001 → CU-019) |
| Formats | 3 (quiz N1-N3 / auto-diag N4-N6 / étude de cas N7-N8) |
| Axes de valeur | 5 (A Productivité, B Décision, C Création, D Croissance, E Industrie) + dimension agentique |
| Fiches outils deep-dive (Ressources) | 63 |
| Outils indexés (catégories courtes) | 90+ |
| Catégories Ressources | 16 (avec « Métier industriel » ajouté en v3.1) |
| Liens tool-link depuis modules | 130 |
| Modules avec pointer Bibliographie | 19/19 |
| Outils 🇪🇺 souverains badgés | 12 |
| Branche en attente de merge | `feat/v3.1-corrections-globales` |

---

## 3. Couverture actuelle des outils (par catégorie)

1. **🧠 LLM & modèles** (8 deep-dives) : Claude, GPT-4/5, Mistral 🇪🇺, Mixtral 🇪🇺, Llama, Qwen, Kimi K2, NotebookLM
2. **🛠 Orchestration / no-code** (5) : n8n, Make, Dify, Flowise, Composio
3. **🤖 Multi-agents** (4) : OpenClaw, LangGraph, CrewAI, AutoGen
4. **💻 IDE & agents codeurs** (5) : Cursor, Claude Code, Aider, Devin, GitHub Copilot Workspace
5. **💾 Vector stores** (4) : Qdrant 🇪🇺, Pinecone, ChromaDB, pgvector
6. **📨 Email & scraping** (2) : AgentMail, Apify
7. **🔍 Compétitive intelligence** (3) : Brand24, Crayon, Klue
8. **📊 Productivité & recherche** (5) : Perplexity, Whisper, Otter.ai, Fireflies.ai, tl;dv 🇪🇺
9. **📰 Contenu & traduction** (2) : Beehiiv, DeepL Pro 🇪🇺
10. **📈 CRM** (6) : HubSpot, Pipedrive, Salesforce, Attio, Microsoft Dynamics 365, Zoho CRM
11. **👁️ Vision industrielle** (6) : YOLO+OpenCV, Cognex, Keyence, Landing AI, Roboflow, Mask R-CNN
12. **🧮 Optimisation / OR** (4) : OR-Tools, IBM CPLEX, Gurobi, FICO Xpress
13. **🪵 Métier industriel** (3) : Cadwork 🇪🇺, TopSolid 🇪🇺, Lectra 🇪🇺
14. **🛠️ ML frameworks** (1) : PyTorch
15. **🇪🇺 Souverains & spécialisés** (5) : Mistral Forge, Goodweek, EthiqAIS, NIN-IA, Spinalia

---

## 4. Pistes pour ta nouvelle itération

Voici les angles où une intervention de Cowork apporterait le plus de valeur. À toi de prioriser selon ton temps et ton angle.

### 4.1 Veille sur nouveaux cas d'usage à ajouter

L'arc 19 modules couvre :
- A. Productivité (CR, traduction, rédaction, recherche)
- B. Décision (RAG knowledge, veille, AAP)
- C. Création (contenu, social, repurposing, newsletter locale)
- D. Croissance (chatbot leads, CRM, devis)
- E. Industrie (vision, maintenance prédictive, optimisation production)
- + multi-agents transverses

**Cas d'usage potentiellement manquants (à challenger)** :
- 🏥 **IA pour la conformité RGPD/AI Act** — au-delà d'EthiqAIS comme outil, un module dédié au cadrage gouvernance pour PME ?
- 🛒 **e-commerce / parcours d'achat** — recommandation produit, search vector, A/B testing IA. Aucun module ne traite explicitement ces sujets.
- 💰 **Finance / contrôle de gestion** — extraction de factures, rapprochement bancaire, prévisions de cash. Cas concrets PME, pas couvert.
- 🎓 **Onboarding & formation interne** — un cas d'usage pédagogique très demandé. Possible étude de cas N7-N8.
- 🤖 **Voicebots & accueil téléphonique** — tendance forte 2026, pas couvert.
- 🌍 **IA & impact environnemental** — sujet en forte montée chez QFC. À traiter en module ou en bibliographie ?

### 4.2 Outils émergents 2026 à ajouter

Notre couverture est bonne mais évolue vite. À surveiller :

- **LLM** : Gemini 2.5, GPT-5.5 / GPT-6, Claude Opus 5, DeepSeek R2, Qwen 3, Phi-4 (Microsoft)
- **Agents** : Mistral Agents, Anthropic Computer Use (production-grade en 2026 ?), OpenAI Agents SDK
- **Souverains EU** : suivre Pleias (français, RAG juridique), Linagora, OpenLLM-France, Aleph Alpha (allemand)
- **Vision** : SAM 2 (Meta), DINOv2, Florence-2 (Microsoft), Owl-ViT
- **Voice** : ElevenLabs, Cartesia (TTS temps réel), Deepgram, AssemblyAI

### 4.3 Approfondissement contenu existant

- **Études de cas N7-N8** : actuellement nous en avons une poignée seulement. Cowork pourrait rédiger 2-3 nouvelles études basées sur des cas réels du réseau QFC (avec Blaise pour le sourcing).
- **Quiz N1-N3** : certains quiz pourraient être enrichis (questions plus contemporaines, références plus à jour).
- **Auto-diagnostics N4-N6** : la mise à jour du marché (notamment l'AI Act qui entre vraiment en application 2026) impose de revisiter les questions de gouvernance.

### 4.4 Point de vue externe sur l'itération v3.1

J'aimerais ton regard sur :

- **La nouvelle structure du sommaire Ressources** (16 catégories) : est-ce que c'est lisible ou trop fragmenté ? Faut-il regrouper ?
- **La légende des badges** : est-ce que les 4 dimensions (Type / Catégorie / Maturité / Souveraineté) sont bien posées ? Manque-t-il une dimension (ex : prix indicatif, complexité d'intégration) ?
- **La bibliographie transverse** : la sélection est-elle bien équilibrée (pas trop anglosaxonne, contenu francophone bien représenté) ?
- **L'archi-flow** : as-tu d'autres modules qui mériteraient d'être repris dans ce format (au-delà des 7 déjà refait) ?
- **Reframing géographique** : on a élargi Vosges → Grand Est. Faut-il aller plus loin et ouvrir au national / européen pour ne pas s'enfermer dans une cible territoriale ?

---

## 5. Stack technique pour intervenir

- **Pas de build step** — édition directe de HTML/CSS/JS vanilla.
- **Architecture mutualisée** : `css/module-v3.css` + `js/module-v3.js` pour les 19 modules.
- **Hébergement** : GitHub Pages, branche `main`.
- **Workflow** : feature branch → PR → merge dans `main`. Conventions : commits préfixés `feat(v3.X) / fix(v3.X) / chore(v3.X)`.
- **Templates** : `modules/_template-quiz.html`, `_template-auto-diagnostic.html`, `_template-etude-de-cas.html` pour créer un nouveau module.

---

## 6. Demande à Cowork

Choisis 1 à 3 angles parmi les pistes ci-dessus (4.1 à 4.4) selon ton intérêt et le temps disponible, et propose à Blaise un plan d'attaque chiffré (estimation outils à ajouter / modules à créer / modifications structurelles) avant d'attaquer la rédaction. Les itérations précédentes ont fonctionné en 4 lots de 12 outils — on peut garder ce rythme ou changer de cadence selon ce qui fait sens.

Pour rappel, la branche en cours `feat/v3.1-corrections-globales` doit être mergée avant que tu attaques quoi que ce soit. Le lien PR : https://github.com/LumenBot/hub-ia/pull/new/feat/v3.1-corrections-globales

Bonne reprise 🚀
