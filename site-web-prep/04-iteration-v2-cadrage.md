# Itération V2 — Document de cadrage

> Suite aux retours utilisateurs sur la V1 du site Hub IA territorial. Ce document formalise les décisions transversales avant la refonte module par module.

---

## Décisions structurantes — récapitulatif

| Sujet | Décision V2 |
|---|---|
| Organisation des axes | Réorganisation par valeur ajoutée IA (cf. ci-dessous) |
| Page présentation des axes | Nouvelle page `axes.html` avec description et exemples |
| Filtres dynamiques | Implémentation V2 — filtres par axe / cible / filière / niveau |
| Structure des modules | 10 sections (vs 6 actuellement) — ajout cas d'étude guidé + schéma + ressources externes |
| Section « Pour aller plus loin » | Refonte stricte — **ressources externes uniquement** |
| Illustrations / schémas | SVG inline pour chaque module — schéma de fonctionnement de principe |
| Profondeur croissante | Volume éditorial proportionnel au niveau (N1-N3 court / N7-N8 long et technique) |

---

## 1. Réorganisation des axes

### Critique de l'organisation V1

L'ordre actuel (1 Automatisation / 2 Décision / 3 Idéation / 4 Marketing / 5 Production / 6 Multi-agents) pose deux problèmes :

1. **L'axe 6 « Orchestration multi-agents » n'est pas un axe métier** mais un *pattern technique transversal* applicable à tous les autres axes. Il génère des doublons (CU-013 Workflow email-CRM est tagué axe 6 mais aussi axe 4 Marketing).
2. **L'ordre n'a pas de logique pédagogique évidente** — pourquoi automatisation avant décision ? Les utilisateurs cherchent la valeur d'usage, pas une numérotation arbitraire.

### Nouvelle organisation proposée — par valeur ajoutée IA

Une organisation en **5 axes métier + 1 dimension transverse** :

| ID | Nom | Description courte | Exemples de modules |
|---|---|---|---|
| **A — Productivité** | Productivité opérationnelle et individuelle | Automatiser les tâches répétitives — premier ROI tangible pour toute organisation | Recherche augmentée, assistant rédactionnel, CR de réunion, traduction, RH simple |
| **B — Décision** | Aide à la décision et veille | Augmenter l'intelligence collective et la qualité des décisions stratégiques | Knowledge base RAG, veille concurrentielle, veille AAP, scenarios prospectifs |
| **C — Création** | Création et innovation produit | Accélérer l'idéation, la conception et la personnalisation produit | Generative design, content repurposing, idéation IA, simulation |
| **D — Croissance** | Expérience client et croissance | Qualifier, attirer, fidéliser, vendre | Devis et propositions, leads chatbot, pipeline contenu, workflow email-CRM |
| **E — Industrie** | Performance industrielle | Optimiser les opérations physiques et la production | Maintenance prédictive, contrôle qualité vision, optimisation production |
| **+ Architecture agentique** | Dimension transverse | Pattern d'orchestration multi-agents — applicable à tous les axes ci-dessus quand la complexité le justifie | Multi-agents par fonction, Stripe Minions |

**Avantages** :
- Lettres au lieu de chiffres → plus mémorisable, moins de hiérarchie implicite
- Noms courts et pédagogiques (« Productivité », « Décision »)
- L'architecture agentique est positionnée comme une dimension d'avancement, pas un axe parallèle
- Permet de mieux placer les modules (CU-013 Workflow email-CRM = axe D Croissance, avec mention « architecture agentique » comme dimension)

### Mapping V1 → V2

| Module | Axe V1 | Axe V2 | Notes |
|---|---|---|---|
| CU-001 Recherche & veille | 2 — Décision | A — Productivité | Le réflexe de base individuel relève de la productivité avant d'être un sujet décisionnel |
| CU-002 Assistant rédactionnel | 1 — Automatisation | A — Productivité | |
| CU-003 CR de réunion | 1 — Automatisation | A — Productivité | |
| CU-004 Traduction | 1 — Automatisation | A — Productivité | |
| CU-005 Devis et propositions | 4 — Marketing/Com | D — Croissance | |
| CU-006 Leads chatbot | 4 — Marketing/Com | D — Croissance | |
| CU-007 RH CV entretiens | 1 — Automatisation | A — Productivité | + flag AI Act |
| CU-008 Knowledge base RAG | 2 — Décision | B — Décision | |
| CU-009 Content repurposing | 4 — Marketing/Com | C — Création (avec hyperlink vers D) | Tag double valable |
| CU-010 Pipeline contenu social | 4 — Marketing/Com | D — Croissance | |
| CU-011 Veille concurrentielle | 2 — Décision | B — Décision | |
| CU-012 Veille AAP + drafting | 2 — Décision | B — Décision | + dimension agentique |
| CU-013 Workflow email-CRM | 6 — Multi-agents | D — Croissance | + dimension agentique |
| CU-014 Multi-agents fonctions | 6 — Multi-agents | Dimension transverse | Cas-école d'architecture agentique pure |
| CU-015 Stripe Minions | 1 — Automatisation | Dimension transverse | Cas-école d'orchestration sur cycle court |
| CU-016 Maintenance prédictive | 5 — Production | E — Industrie | |
| CU-017 Contrôle qualité vision | 5 — Production | E — Industrie | |
| CU-018 Optimisation production | 5 — Production | E — Industrie | |
| CU-019 Newsletter locale | 4 — Marketing/Com | C — Création (avec hyperlink vers D) | Tag double valable |

---

## 2. Page « axes.html » — nouvelle entrée pédagogique

### Objectif

Donner aux utilisateurs une compréhension rapide de l'organisation des modules avant qu'ils n'attaquent un cas d'usage spécifique. Particulièrement utile pour :
- Les dirigeants qui veulent une vision d'ensemble
- Les nouveaux visiteurs qui découvrent l'IA en entreprise
- L'usage en atelier (introduction au format)

### Structure proposée

```
[Nav]

[Hero court — titre + sous-titre]
"L'IA en entreprise se déploie sur 5 axes de valeur"
"Comprends où chaque cas d'usage te crée de la valeur, et choisis ton point d'entrée selon tes priorités"

[Pour chaque axe — 5 cards larges]
  [Icône + Lettre + Nom de l'axe]
  Description (3-5 lignes pédagogiques avec un exemple parlant)
  "Modules associés : X cas d'usage"
  [Bouton "Explorer les modules de cet axe →"]

[Section Architecture agentique — encart distinct]
  Description du pattern transverse
  "Pertinent à partir du niveau N7-N8"
  [Bouton "Voir les modules dimension agentique →"]

[CTA - retour vers /modules avec filtres]

[Footer]
```

### Liens depuis les autres pages

- Lien dans la navbar : « Axes »
- Lien depuis les badges d'axe sur les cards modules → page axe correspondante
- Lien depuis le hero de chaque module → page axe associée

---

## 3. Système de filtres

### UX cible

Au-dessus de la grille de modules sur `index.html`, ajouter un **panel de filtres dépliable** (closed par défaut, ouvert par clic sur « Filtrer »).

### Filtres à implémenter

```
┌──────────────────────────────────────────────────┐
│  ⚙ Filtrer les modules                       [▼] │
├──────────────────────────────────────────────────┤
│                                                  │
│  Axe de valeur                                   │
│  [□ A Productivité] [□ B Décision] [□ C Création]│
│  [□ D Croissance] [□ E Industrie]                │
│  [□ + Architecture agentique]                    │
│                                                  │
│  Niveau de complexité                            │
│  [□ N1-N3 Fondamentaux]                          │
│  [□ N4-N6 Applications métier]                   │
│  [□ N7-N8 Industrialisation]                     │
│                                                  │
│  Cible                                           │
│  [□ Startup] [□ PME-ETI] [□ Les deux]            │
│                                                  │
│  Filière (pour cas industriels)                  │
│  [□ Industrie] [□ Bois/Papier] [□ Textile]       │
│  [□ Agro] [□ Tertiaire] [□ Transverse]           │
│                                                  │
│  [Réinitialiser]              [Appliquer X de Y] │
└──────────────────────────────────────────────────┘
```

### Logique technique

- Multi-sélection sur chaque catégorie (OR au sein d'une catégorie)
- Intersection entre catégories (AND entre catégories)
- Filtre via `data-attributes` sur les cards (déjà prévu dans le brief V1)
- Persistance dans localStorage (`hubia_filters`)
- Compteur de modules visibles affiché en temps réel

### Cards modules — data-attributes à ajouter

```html
<a class="card n2"
   data-module="cu-005"
   data-axe="d"
   data-niveau="n2"
   data-cible="les-deux"
   data-filieres="transverse"
   data-agentique="false">
```

---

## 4. Structure type des modules — V2

### Structure complète

Chaque module suit désormais 10 sections obligatoires :

```
1. Hero
   - Titre + emoji
   - Badges (axe / niveau / temps de lecture / format)
   - Promesse pédagogique courte (1 phrase)

2. "Ce que tu vas pouvoir faire après ce module" (4 puces actionnables)
   - Tournée action, pas connaissance
   - Ex: "Identifier les 3 cas d'usage les plus rentables pour ta structure"
   - Ex: "Mettre en place un outil de recherche augmentée en moins de 30 min"

3. Le cas / le contexte
   - 2-3 paragraphes de cadrage
   - Citation impactante éventuelle

4. SCHÉMA DE FONCTIONNEMENT DE PRINCIPE  ← NOUVEAU
   - SVG inline ou image embedded
   - Représente les acteurs, étapes, flux

5. Comment ça fonctionne (étapes détaillées)
   - Liste numérotée des étapes-clés
   - Pour les modules N7-N8, ajouter spécifications techniques

6. Stack et outils
   - Outils par catégorie
   - Liens vers documentation officielle

7. CAS D'ÉTUDE GUIDÉ — Mise en situation  ← NOUVEAU
   - Contexte fictif réaliste (ex: "Tu es CEO d'une PME industrielle de 30 salariés...")
   - 3-5 étapes pratiques pas à pas
   - Pour chaque étape : action attendue + outil à utiliser + output
   - Encart résultat final / livrable produit
   - Variantes possibles selon profil

8. Limites et points de vigilance
   - Pièges techniques
   - Conformité (AI Act, RGPD)
   - Bonnes pratiques

9. [Format pédagogique selon niveau]
   - N1-N3 → Quiz 5 questions
   - N4-N6 → Auto-diagnostic + plan d'action exportable
   - N7-N8 → Étude de cas + checklist d'éligibilité

10. Pour aller plus loin  ← REFONTE STRICTE
    - 4-6 ressources EXTERNES uniquement
    - Articles de fond, tutoriels, documentation officielle
    - PAS de modules internes du site
    - PAS de partenaires QFC
    - PAS de programmes de financement
    - Format type :
      "📖 Article — [Titre] (source.com, 2026) — description courte"
      "🎥 Tutoriel vidéo — [Titre] (YouTube, 30 min)"
      "📚 Documentation officielle — [Outil] (lien)"
```

### Volume éditorial selon le niveau

| Niveau | Sections 1-6 | Section 7 (cas d'étude) | Section 8-10 | Volume cible |
|---|---|---|---|---|
| N1-N3 | Concis (300-500 mots) | 3 étapes simples (200 mots) | Standard | ~1500 mots |
| N4-N6 | Modéré (500-800 mots) | 4 étapes structurées (400 mots) | Standard | ~2500 mots |
| N7-N8 | Approfondi (800-1500 mots) | 5 étapes techniques détaillées (700 mots) | Étendu (méthodo, archi, troubleshooting) | ~4000 mots |

---

## 5. Section « Pour aller plus loin » — règles strictes

### Ce qu'on inclut

✅ **Articles de fond externes** — McKinsey, BCG, MIT, HBR, Sifted, FT, Les Échos, blogs spécialisés
✅ **Tutoriels vidéo** — YouTube, conférences, masterclasses
✅ **Documentation officielle des outils cités** — lien direct vers Anthropic, OpenAI, Mistral, n8n, etc.
✅ **Études de cas tiers documentés** — blogs entreprises (Stripe, Notion, etc.)
✅ **Communautés** — Discord publics, subreddits pertinents (Hub IA propose, ne juge pas)
✅ **Livres et publications académiques** quand pertinents

### Ce qu'on n'inclut pas

❌ Modules internes du site (sauf en navigation footer)
❌ Partenaires QFC (NIN-IA, Spinalia, EthiqAIS, etc.)
❌ Programmes de financement (DECARB IND, Pionniers IA, etc.)
❌ Acteurs commerciaux promotionnels
❌ Liens-affiliés ou rémunérés

### Format type

```
## Pour aller plus loin

### 📖 Articles de fond
- [State of AI in Sales 2025](https://hubspot.com/state-of-ai-sales) — HubSpot, 2025 — benchmarks adoption commerciale et gains documentés
- [The Generative AI Tipping Point](https://hbr.org/2024/...) — Harvard Business Review, 2024 — analyse du basculement post-2024

### 🎥 Tutoriels et démos
- [Building your first sales assistant in Claude](https://www.youtube.com/watch?v=...) — YouTube, 25 min
- [n8n complete walkthrough for sales automation](https://...) — Tutoriel pas à pas

### 📚 Documentation officielle
- [Claude API documentation](https://docs.anthropic.com)
- [n8n nodes for sales workflows](https://docs.n8n.io/...)

### 💬 Communautés
- [r/SalesAutomation](https://reddit.com/r/...) — communauté pratique
```

### Conventions de présentation

- Toujours mentionner la **source et l'année** (crédibilité)
- Privilégier les **liens stables** (pas des tweets, sauf cas exceptionnel)
- **3-6 ressources max** par module (qualité > quantité)
- Émojis catégoriels en début de ligne pour scanabilité

---

## 6. Schémas de fonctionnement de principe

### Approche

Chaque module doit avoir un schéma SVG inline qui représente :
- Les **acteurs** impliqués (humain, agents, outils)
- Les **étapes** du processus (flèches numérotées)
- Les **outils mobilisés** à chaque étape
- L'**output** produit

### Style visuel

Cohérent avec la charte du site :
- Couleurs primaires Hub IA (`#1F3864`, `#2E5395`)
- Couleurs sémantiques par étape (selon palette niveau N1/N2/N3)
- Boîtes arrondies, flèches simples
- Police Inter, taille lisible

### Templates par type de module

**Type 1 — Schéma linéaire** (modules N1-N3, simples)
```
[Humain] → [Outil IA] → [Output]
```

**Type 2 — Schéma en chaîne** (modules N4-N6, multi-étapes)
```
[Humain] → [Étape 1] → [Étape 2] → [Étape 3] → [Output]
                ↓ outil A     ↓ outil B    ↓ outil C
```

**Type 3 — Schéma multi-agents** (modules N7-N8, complexes)
```
        [Orchestrateur]
       /       |        \
  [Agent 1] [Agent 2] [Agent 3]
       \       |        /
       [Mémoire partagée]
            ↓
        [Output unifié]
```

Un fichier `schema-template.svg` sera produit avec ces 3 patterns à recopier.

---

## 7. Roadmap d'itération module par module

### Ordre proposé

**Vague 1 — N1-N3 Fondamentaux (4 modules, sessions courtes)**
1. CU-001 Recherche & veille augmentée
2. CU-002 Assistant rédactionnel
3. CU-003 CR de réunion automatisé
4. CU-004 Traduction multi-langues

**Vague 2 — N4-N6 Applications métier (8 modules, sessions modérées)**
5. CU-005 Devis et propositions
6. CU-006 Leads chatbot
7. CU-007 RH CV entretiens (avec section AI Act renforcée)
8. CU-008 Knowledge base RAG
9. CU-009 Content repurposing
10. CU-010 Pipeline contenu social
11. CU-011 Veille concurrentielle
12. CU-019 Newsletter locale automatisée

**Vague 3 — N7-N8 Industrialisation (7 modules, sessions longues)**
13. CU-012 Veille AAP + drafting
14. CU-013 Workflow email-CRM
15. CU-014 Multi-agents par fonction métier
16. CU-015 Stripe Minions / agents codeurs
17. CU-016 Maintenance prédictive industrielle
18. CU-017 Contrôle qualité par vision IA
19. CU-018 Optimisation production / nesting

### Cadence suggérée

- 1-2 modules N1-N3 par session (rapides)
- 1 module N4-N6 par session (modérés)
- 1 module N7-N8 par session ou demi-session (longs et techniques)

Total estimé : 12-15 sessions Cowork pour la refonte complète.

---

## 8. Modifications du brief Claude Code

Pour la prochaine session Claude Code, lui transmettre :

1. **Ce document `04-iteration-v2-cadrage.md`** comme nouvelle référence
2. **Demander la création de la page `axes.html`** avec la structure proposée
3. **Demander l'implémentation du système de filtres** sur `index.html`
4. **Demander la mise à jour des `data-attributes`** sur les cards modules selon le mapping V1→V2
5. **Demander la modification de la navbar** pour ajouter « Axes »

Une fois ces modifications transversales déployées, on enchaîne avec les itérations module par module.

---

## 9. Conventions de versioning

- Branches Git : `feat/v2-axes-refonte`, `feat/v2-filters`, `content/v2-cuNNN`
- Commits : `feat(v2): ...` pour les évolutions structurelles, `content(v2): ...` pour les contenus
- Tags : `v1.0` pour la version actuelle live, `v2.0` quand la refonte transversale est complète

---

*Document de cadrage V2 — Mai 2026. À itérer avec Blaise au fil des sessions.*
