# Mapping pédagogique — Site Hub IA territorial

> Architecture pédagogique du site web inspiré de qfc-num. Organisation des 18 cas d'usage en parcours d'apprentissage progressifs.

---

## Principe directeur

Le site reprend la **logique micro-learning** du site qfc-num : modules courts, indépendants, consultables au rythme de l'utilisateur, avec un quiz court à la fin de chaque module pour ancrer l'apprentissage.

**Différence clé avec qfc-num** : qfc-num organise par discipline (maquette / tech). Notre site organise par **niveau de complexité IA** (les 3 niveaux de l'échelle MOR-IA), ce qui permet à un dirigeant ou un porteur de **commencer par ce qui est accessible** et de **progresser à son rythme** vers les usages plus avancés.

---

## Structure de la landing page

Trois sections principales, chacune avec un ton et une couleur distinctifs :

### 🟢 Section 1 — Fondamentaux IA (Niveau N1-N3)

**Sous-titre proposé** : « Les premiers pas avec l'IA — usages individuels accessibles à tous »

**Promesse pédagogique** : « En 4 modules, comprendre comment l'IA peut transformer ta journée de travail dès demain matin. »

**Public premier** : tout dirigeant, collaborateur, porteur découvrant l'IA.

**4 modules** :
1. 📚 **Recherche & veille augmentée** (CU-001)
2. ✍️ **Assistant rédactionnel** (CU-002)
3. 🎙️ **Compte-rendus de réunion automatisés** (CU-003)
4. 🌍 **Traduction et adaptation multi-langues** (CU-004)

---

### 🟡 Section 2 — Applications métier (Niveau N4-N6)

**Sous-titre proposé** : « Industrialiser l'usage de l'IA dans tes fonctions clés »

**Promesse pédagogique** : « En 7 modules, identifier où l'IA peut transformer ton commercial, ton marketing, ta gestion documentaire ou tes RH. »

**Public premier** : responsables fonctionnels (commercial, marketing, RH, R&D), dirigeants en réflexion stratégique.

**7 modules** :
5. 📄 **Génération de devis et propositions** (CU-005)
6. 💬 **Qualification de leads par chatbot** (CU-006)
7. 👥 **IA en RH : CV et entretiens** ⚠️ AI Act (CU-007)
8. 🧠 **Knowledge base RAG** (CU-008)
9. 🔁 **Content repurposing** (CU-009)
10. 📱 **Pipeline contenu social** (CU-010)
11. 🔭 **Veille concurrentielle continue** (CU-011)

---

### 🔴 Section 3 — Industrialisation (Niveau N7-N8)

**Sous-titre proposé** : « Construire des systèmes agentiques et industrialiser l'IA dans ton organisation »

**Promesse pédagogique** : « En 7 modules, comprendre les architectures avancées et les cas d'usage industriels — de la chaîne email-CRM à la maintenance prédictive en production. »

**Public premier** : profils techniques, dirigeants d'ETI industrielles, R&D, IT.

**7 modules** :
12. 💸 **Veille AAP + drafting de candidatures** (CU-012)
13. 📧 **Workflow email → CRM → réponse** (CU-013)
14. 🤖 **Multi-agents par fonction métier** (CU-014)
15. 👨‍💻 **Agents codeurs internes (cas Stripe)** (CU-015)
16. 🔧 **Maintenance prédictive industrielle** (CU-016)
17. 👁️ **Contrôle qualité par vision IA** (CU-017)
18. ⚙️ **Optimisation de production / nesting** (CU-018)

---

## Roadmap des fonctionnalités

### V1 — Site statique fonctionnel

Périmètre minimum viable, calé sur qfc-num :

- Landing page avec 3 sections + 18 cards
- Navigation directe vers chaque module
- Page module avec contenu + quiz 5 questions + scoring
- Marquage local des modules complétés (localStorage)
- Design responsive
- Footer avec mentions QA / QFC

### V2 — Filtres dynamiques

Ajout d'une couche de navigation par tags pour permettre l'entrée selon le profil de l'utilisateur :

- **Filtre par cible** : Startup / PME-ETI / Les deux
- **Filtre par fonction métier** : DG, Commercial, Marketing, RH, R&D, IT, Opérations, Finance
- **Filtre par filière** (pour les cas industriels) : Industrie, Bois/Papier, Textile, Agro, Tertiaire, Transverse
- **Filtre combinatoire** (intersection de plusieurs tags)

### V3 — Parcours guidés par profil

Création de parcours pédagogiques préconçus qui séquencent les modules selon le profil :

- **Parcours « Dirigeant PME industrielle »** — focus N1-N3 transverses + N7-N8 production
- **Parcours « Founder startup tech »** — focus accélération produit + N7-N8 builders
- **Parcours « Responsable marketing »** — focus N4-N6 axe 4 marketing/com
- **Parcours « Responsable opérations »** — focus N1-N3 productivité + N7-N8 industriel
- **Parcours « Découverte IA »** — focus exclusif N1-N3 progressifs

---

## Anti-patterns à éviter

À partir de l'observation du site qfc-num et de la matière de l'encyclopédie :

1. **Pas de jargon technique en page index.** La landing doit être lisible par un dirigeant non-tech. Les termes (RAG, agents, fine-tuning) sont expliqués DANS les modules, pas affichés sur les cards.

2. **Pas de classement par axe ou par fonction en première intention.** Trop de catégories → désorientation. La progression par complexité (3 sections) est plus naturelle.

3. **Pas de modules trop longs.** Un module = 1 page lisible en 10-15 minutes max + un quiz court (5 questions). Si un sujet demande plus, on le découpe en 2 modules.

4. **Pas de promesse commerciale.** Le ton reste neutre, pédagogique, factuel. Pas de « la meilleure solution », pas de « l'outil incontournable ».

5. **Pas de surcharge visuelle.** Reprendre la sobriété de qfc-num : navbar simple, hero épuré, cards lisibles, pas d'animations gratuites.

---

## Cohérence avec l'écosystème QA / QFC

- **Marquee logos incubateurs** (comme qfc-num) : Quai Alpha + Innovact + SEMIA + Rimbaud Tech + The Pool + Quest for Health + Quest Bioéco + Quest for Industry. Permet de montrer que la démarche est un actif **réseau QFC**, pas QA seul.
- **Footer** : positionnement réseau QFC, contact SUM Quai Alpha, mention « Mai 2026 ».
- **Branding** : couleurs et typographie cohérentes avec la note de cadrage QA (bleu primaire `#1F3864`, bleu secondaire `#2E5395`).

---

## Modules à produire en priorité

Pour amorcer la matière éditoriale dès la session suivante, je propose les **5 premiers modules** dans l'ordre suivant :

1. **CU-001 Recherche & veille augmentée** — porte d'entrée évidente, accessible immédiatement, ROI rapide.
2. **CU-002 Assistant rédactionnel** — usage le plus fréquent pour un dirigeant.
3. **CU-005 Génération de devis** — premier cas N4-N6 à fort ROI tangible.
4. **CU-013 Workflow email-CRM** — premier cas N7-N8 illustrant le passage à l'orchestration.
5. **CU-016 Maintenance prédictive** — premier cas industriel sectoriel pour le territoire vosgien.

Ces 5 modules couvrent les 3 niveaux et donnent une vue représentative de l'amplitude du site dès la mise en ligne.

---

*Mapping pédagogique V1 — Mai 2026. À itérer selon les retours.*
