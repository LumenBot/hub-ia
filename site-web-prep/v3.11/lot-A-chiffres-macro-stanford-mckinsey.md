# Lot A v3.11 — Patches chiffres macro Stanford + McKinsey

**Brief consolidé pour Claude Code** : 5 patches courts dispersés sur PR-04, PR-01, CU-027, DEP-08/PR-05 + encart « jagged frontier » Stanford dans DEP-01. Sources institutionnelles premium (Stanford AI Index Report 2026 + McKinsey State of AI 2025).

**Sources** :
- Stanford AI Index Report 2026 (425 pages, 9 chapitres) — Stanford HAI, référence annuelle internationale
- McKinsey « The state of AI in 2025: Agents, innovation, and transformation » (novembre 2025, 30 pages)

**Urgence** : moyenne. Chiffres canoniques 2026 manquants dans le Hub, à intégrer avant d'autres modules pour assurer la cohérence cross-couche.

---

## Patch A.1 — PR-04 (Marché IA & emploi) — enrichissement triple

**Module cible** : `prealables/pr-04-marche-ia-emploi.html`
**Position** : enrichir la section 2bis « Tendances macro 2026 » (existante, déjà patchée en v3.9 §2ter et v3.10 actualisation triple). Compléter avec les nouvelles sources Stanford + McKinsey.

### Contenu à intégrer

#### McKinsey State of AI 2025 — chiffres complémentaires aux runs précédents

À insérer comme **sous-encart** dans la section 2bis (en complément des chiffres Bpifrance + Microsoft déjà intégrés en v3.10) :

> 📊 **McKinsey State of AI 2025 (nov. 2025)** — enquête mondiale 1 993 répondants, juin-juillet 2025

- **88 % des organisations utilisent régulièrement l'IA dans au moins 1 fonction** (vs 78 % l'année précédente)
- **39 % rapportent un EBIT impact attribuable à l'IA**, mais **la plupart à moins de 5 % de l'EBIT**
- **23 % scalent un système agentique** (cohérent avec McKinsey State of AI Trust 2026 déjà canonisé) + **39 % expérimentent**
- **Anticipation employeur sur l'emploi à 1 an** : **32 % baisse / 43 % stable / 13 % hausse** (chiffre nuancé — perspective employeur, pas réalité observée)

#### Stanford AI Index Report 2026 — chiffres adoption globale

À insérer comme **sous-encart** dans la section 2bis :

> 📊 **Stanford AI Index Report 2026** — référence internationale Stanford HAI, 425 pages

- **53 % d'adoption population de la GenAI en 3 ans** (plus rapide que le PC ou internet)
- France et Europe occidentale dans la moyenne ; Singapour à **61 %**, UAE à **54 %**, US 24e mondial à **28,3 %**
- **172 Md$ / an** : valeur estimée de la GenAI pour les consommateurs US (médiane × 3 entre 2025 et 2026)
- **88 % adoption organisationnelle** mondiale (cohérent avec McKinsey ci-dessus)
- **4 étudiants sur 5 utilisent la GenAI** (cadre éducation, signal de bascule génération suivante)

### Sources à ajouter dans #ressources

- **McKinsey & Company** — « The state of AI in 2025: Agents, innovation, and transformation » (mckinsey.com/capabilities/quantumblack/our-insights, novembre 2025)
- **Stanford HAI** — AI Index Report 2026 (aiindex.stanford.edu, mars 2026)

### Métadonnées module

- `<meta name="description">` : pas de modification majeure (l'angle PR-04 reste cohérent — actualisation enrichissement).
- Badge temps de lecture : passer à **+3 min** (2 nouveaux sous-encarts).

---

## Patch A.2 — PR-01 (Maturité organisationnelle) — high performers + redesign

**Module cible** : `prealables/pr-01-maturite-organisationnelle.html`
**Position** : enrichir la section consacrée aux facteurs de succès (en complément de la typologie 4 profils dirigeants Bpifrance intégrée en v3.10).

### Contenu à intégrer

#### Le pattern « high performers » — qui se distingue vraiment ?

> 🎯 **6 % des organisations sont des « AI high performers »** (McKinsey State of AI 2025) — c'est-à-dire celles qui rapportent un EBIT impact >5 % attribuable à l'IA **ET** une valeur significative.

**Ce qui distingue ces 6 %** (chiffres comparatifs à transposer textuellement) :

- **3,6× plus à pousser une transformation IA fondamentale** de leur business (vs autres répondants)
- **3× plus à redessiner fondamentalement leurs workflows** autour de l'IA
- Ils combinent **3 objectifs simultanés** : efficience + croissance + innovation (vs seulement efficience pour les autres)

**Citation à préserver textuellement** :

> *« The intentional redesigning of workflows has one of the strongest contributions to achieving meaningful business impact of all the factors tested. »* (McKinsey State of AI 2025)

#### Implication pour la PME

Si la PME se positionne dans la **typologie Bpifrance** (Sceptiques / Bloqués / Expérimentateurs / Innovateurs — intégrée v3.10) :
- Le passage **Expérimentateurs → Innovateurs** se fait souvent par le **redesign de workflows**, pas par l'ajout de nouveaux outils
- Les **Innovateurs (28 %)** correspondent approximativement aux **AI high performers (6 %)** dans l'enquête McKinsey — la convergence des 2 grilles d'analyse est cohérente

### Sources à ajouter dans #ressources

- **McKinsey & Company** — « The state of AI in 2025 » (déjà ajoutée Patch A.1, mention cross-module)

### Métadonnées module

- Badge temps de lecture : passer à **+2 min**.

---

## Patch A.3 — CU-027 (Faire développer une appli métier) — accélération coding agents 2026

**Module cible** : `modules/cu-027-dev-applicatif-ia.html`
**Position** : enrichir la section 1bis « État de l'art 2026 : Kimi K2.6 + ECC » avec les nouveaux chiffres Stanford (déjà des chiffres ECC + Kimi K2.6 + benchmark Aqua Voice/DEV.to).

### Contenu à intégrer

#### Encart « L'accélération mesurable des coding agents en 2026 »

À insérer dans la section 1bis (avant ou après le point 1 Kimi K2.6, selon l'angle pédagogique préféré) :

> 🚀 **SWE-bench Verified : de 60 % à ~100 % du baseline humain en un an** (Stanford AI Index Report 2026).

C'est le chiffre qui matérialise pourquoi 2026 est l'année où les coding agents passent du « prometteur » au « réellement productif ». **SWE-bench Verified** est un benchmark de référence qui mesure la capacité d'un agent à résoudre de vrais bugs sur de vrais repos GitHub. Le passage de 60 % à ~100 % du baseline humain en 12 mois est **une accélération sans équivalent dans l'histoire récente du software engineering**.

**Implication pour la PME** : si tu fais développer une appli métier en 2026, ton prestataire doit **utiliser un coding agent récent** (Claude Code, Cursor, Windsurf) sur un modèle de pointe (Claude Opus 4.7, Kimi K2.6) — sinon il facture 8-10 K€/mois pour un travail qui peut être fait à 20 $/mois Claude Pro + 50-200 €/mois infra (cohérence avec chiffres CU-027 déjà intégrés).

#### Encart « Productivité mesurée et effet sur l'emploi »

> 📊 **Productivité 14-26 % en customer support et software dev** (Stanford AI Index Report 2026)
>
> Effet secondaire mesuré : **emploi des développeurs US 22-25 ans : -20 % depuis 2024** (alors que les seniors continuent d'embaucher).

**Implication pour la PME** : la productivité gagne, mais elle se redistribue par **niveau de séniorité**. Le junior généraliste perd, le senior augmenté gagne. À anticiper dans toute stratégie de recrutement ou de prestation IA-assistée — privilégier un prestataire senior + ECC stack plutôt qu'une équipe de juniors.

### Sources à ajouter dans #ressources

- **Stanford HAI** — AI Index Report 2026 (déjà ajoutée Patch A.1, mention cross-module)

### Métadonnées module

- Badge temps de lecture : passer à **+2 min**.

---

## Patch A.4 — DEP-08 (Sécurité agents et MCP servers) / PR-05 (Sécurité IA) — incidents documentés en hausse

**Modules cibles** : `deploiement/dep-08-securite-agents-mcp.html` et `prealables/pr-05-securite-ia.html`
**Position** : encart court à intégrer dans la section 1 ou 3 de chaque module (selon état actuel des sections après v3.10).

### Contenu à intégrer (encart symétrique sur les 2 modules)

> 🚨 **362 incidents IA documentés en 2025** vs 233 en 2024 — **+55 % en un an** (Stanford AI Index Report 2026).

Le rapport Stanford documente une **explosion des incidents IA** en 2025, parallèle à l'adoption massive. Catégories observées (à enrichir si le rapport fournit le détail dans les chapitres dédiés) :
- Failles de sécurité agents et MCP servers (cohérent avec DEP-08 §1.3 : CVE-2025-59536, MCP STDIO vulnerability, OpenClaw 12 %, Moltbook breach)
- Hallucinations en production avec conséquences réelles
- Compromissions supply chain
- Mésusages d'outils par agents

**Implication pour la PME** : la **probabilité d'incident IA augmente plus vite que les capacités de mitigation** des PME. Les patterns de la section 2 (5 défenses prompt injection) + section 3 (AgentShield) + section 7bis (SBOM IA v3.10) deviennent un **minimum opérationnel**, pas une option avancée.

### Sources à ajouter dans #ressources de DEP-08 et PR-05

- **Stanford HAI** — AI Index Report 2026, chapitre 3 « Responsible AI » (aiindex.stanford.edu, mars 2026)

### Métadonnées modules

- Badge temps de lecture : passer à **+1 min** chacun (encart court).

---

## Patch A.5 — DEP-01 (Cadrer un projet IA) — encart « Jagged Frontier » Stanford

**Module cible** : `deploiement/dep-01-cadrer-projet-ia.html`
**Position** : nouvelle sous-section ou encart dans la section consacrée au cadrage du projet (en complément de l'heuristique anti-hype intégrée en v3.10).

### Contenu à intégrer

#### Encart « Le "Jagged Frontier" de l'IA en 2026 »

> 🪨 **« Jagged Frontier »** (Stanford AI Index Report 2026) — l'IA n'est pas uniformément bonne ou mauvaise sur tous les sujets. C'est une **frontière dentelée** : excellente sur certaines tâches, défaillante sur d'autres pourtant proches.

**Exemples documentés par Stanford** (à transposer textuellement comme cadrage pédagogique) :

- **Gemini Deep Think a gagné une médaille d'or à l'International Mathematical Olympiad** (sommet du raisonnement mathématique)
- ... mais **le même modèle ne lit correctement l'heure sur une horloge analogique que 50,1 % du temps** (tâche triviale pour un enfant de 7 ans)
- **OSWorld** (tests d'agents sur tâches PC réelles) : **passage de 12 % à 66 % de task success en un an**
- ... mais **1 échec sur 3 reste**, et les benchmarks structurés ne reflètent pas la variabilité des tâches du monde réel

**Implication pour le dirigeant PME qui cadre un projet IA** :

1. **Ne jamais extrapoler d'une démo réussie à un déploiement universel.** Un agent qui marche sur 10 cas testés peut échouer catastrophiquement sur le 11e cas.
2. **Documenter le périmètre exact** où l'IA est testée et valide. Tout ce qui sort de ce périmètre est **frontière non testée**.
3. **Maintenir un fallback humain** sur tous les cas qui sortent du périmètre testé (cohérence avec pattern « agent = employé » CU-026 + failure receipt DEP-05 §8.5 v3.10).
4. **Ne pas confondre « le modèle peut faire X » et « l'agent en production fera X de manière fiable »**. La fiabilité opérationnelle est une propriété distincte de la capacité brute.

### Sources à ajouter dans #ressources

- **Stanford HAI** — AI Index Report 2026, chapitre 2 « Technical Performance » (aiindex.stanford.edu, mars 2026)

### Métadonnées module

- Badge temps de lecture : passer à **+3 min**.

---

## Synthèse cohérence Lot A

Les 5 patches partagent une narration cohérente — **« 2026 est l'année du passage à l'échelle, avec ses asymétries »** :

- **Adoption massive** (88 % organisations, 53 % population — A.1)
- **Maturité organisationnelle qui se polarise** (high performers vs autres — A.2)
- **Accélération technique mesurable** (SWE-bench 60→100 %, productivité 14-26 % — A.3)
- **Incidents en hausse parallèle** (362 vs 233, +55 % — A.4)
- **Frontière dentelée** comme cadre pédagogique pour ne pas confondre capacité et fiabilité (A.5)

Cette narration peut être renforcée dans un encart de synthèse en tête de PR-04 ou dans une mise à jour de PR-01.

## Item parallèle (à compiler dans brief v3.11)

12 nouveaux chiffres macro à canoniser dans `chiffres-macro-2026.md` côté MD RAG (item I-D-007). Recouvrement attendu avec quasi tous les modules adoption/maturité/agents/sécurité.
