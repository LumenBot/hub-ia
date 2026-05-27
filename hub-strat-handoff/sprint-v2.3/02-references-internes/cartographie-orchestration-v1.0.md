# Cartographie d'orchestration multi-canaux — Initiative IA × Hub v2

**Version** : 1.0 — 25 mai 2026 (soir)
**Statut** : provisoire — v1 lo-fi statique. Révision majeure à clôture Cycle 1 (≈ mi-juillet) en cohérence avec convention multi-acteurs v2.
**Source de vérité** : ce fichier dans `LumenBot/dev-environment/00_INSTRUCTIONS/CARTOGRAPHIE-ORCHESTRATION.md` (sync depuis Cowork via Guide-Sync-Git §4.1).
**Maintenance** : DEV IA Head (à chaque création/fermeture de canal ou détection de flux nouveau).
**Périmètre** : décrit l'architecture **opérationnelle réelle** des acteurs IA collaborant sur les projets de Blaise Cavalli (Initiative IA méta + Hub v2 side project).

---

## 1. Pourquoi ce fichier existe

Au 25/05/2026 soir, **10 acteurs IA/humains collaborent en parallèle** sur les projets de Blaise Cavalli (Initiative IA + Hub v2). Aucun fichier ne cartographiait cette architecture jusqu'à cette date — Blaise portait mentalement les 9 interfaces inter-canaux et faisait les transmissions par copier-coller manuel.

C'est le **risque méta-gouvernance #1** du système (tracé `.decisions/decisions.jsonl` 25/05 soir) : si Blaise est indisponible 1-2 semaines, tout le projet est bloqué. Et le simple porte de coordination consomme une bande passante humaine qui ne produit pas de valeur ajoutée.

Ce fichier matérialise la cartographie pour :
1. **Visibilité partagée** : chaque acteur peut consulter ce fichier pour comprendre où il s'insère dans l'écosystème (vs porter mentalement la carte).
2. **Réduction de la charge Blaise** : un nouveau canal qui démarre lit ce fichier au lieu de demander à Blaise « qui sont les autres ? ».
3. **Détection de désynchronisation** : si la cartographie observée diverge de la cartographie documentée, c'est un signal qu'un canal dérive de son périmètre.

---

## 2. Les 10 acteurs

### 2.1 Tableau récapitulatif

| # | Acteur | Type | Cluster | Périmètre |
|---|---|---|---|---|
| **A1** | Hub Strat | Cowork | Hub v2 | Stratégie produit / GTM / analyse concurrentielle / juridique / acquisition (créé 25/05 soir) |
| **A2** | Hub Content | Cowork | Hub v2 | Contenu site : modules formation, ressources, notes (ex-Hub IA, renommé 25/05) |
| **A3** | Hub RAG | Cowork | Hub v2 | Pilotage dev technique du RAG : structuration MD, golden set, eval |
| **A4** | Claude Code Content | Claude Code (Plateforme web) | Hub v2 | Production HTML du site / Hub (à partir des briefs Hub Content) |
| **A5** | Claude Code RAG | Claude Code (Plateforme web) | Hub v2 | Préparation environnement logiciel du RAG (skills, scripts d'ingestion, tests) |
| **A6** | Claude Code Console | Claude Code Desktop local | Hub v2 | Implémentation effective du RAG (ChromaDB local, exécutions coûteuses) |
| **A7** | Claude Design | Surface dédiée Anthropic | Hub v2 | UX, signature visuelle, parcours, prototypes interactifs |
| **A8** | DEV IA Head | Cowork | Initiative IA | Méta-gouvernance, patterns transverses, posture critique sur l'architecture multi-acteurs |
| **A9** | DEV IA Archi-Sys | Cowork | Initiative IA | Architecture système agents, investigation tech, Phase 0-1 (cadrage POC périmètre B) |
| **A10** | Blaise Cavalli | Humain | Orchestrateur | Décideur final, garant des interfaces inter-canaux (portage manuel actuel) |

### 2.2 Notes par cluster

- **Cluster Hub v2** (A1-A7) : 7 acteurs sur le side project entrepreneurial Cavalli. Hub v2 = projet personnel, pas QFC. Convergence opérationnelle avec POC périmètre B Initiative IA (Phase 1 mini RAG).
- **Cluster Initiative IA** (A8-A9) : 2 agents sur le projet méta (environnement de développement augmenté par IA). Pas de chevauchement de scope avec le Hub v2 — observation et coordination uniquement.
- **Orchestrateur** (A10) : Blaise, garant unique de la cohérence d'ensemble. Bandwidth = goulot structurel à instrumenter (cf. §5).

---

## 3. Matrice des interfaces (qui parle à qui)

Légende : ✅ flux actif et fréquent · 🔵 flux ponctuel · ⚪ pas de flux direct (passe par Blaise) · ❌ pas d'interaction prévue

|              | A1 Strat | A2 Content | A3 RAG | A4 CC-C | A5 CC-R | A6 CC-Cons | A7 Design | A8 DEV-H | A9 DEV-AS | A10 Blaise |
|---           |---       |---         |---     |---      |---      |---         |---        |---       |---        |---         |
| **A1 Strat** | —        | ✅          | 🔵      | ⚪       | ⚪       | ⚪          | ✅         | 🔵        | ⚪         | ✅          |
| **A2 Content** | ✅       | —          | 🔵      | ✅       | ⚪       | ⚪          | ✅         | 🔵        | ⚪         | ✅          |
| **A3 RAG**   | 🔵        | 🔵          | —      | ⚪       | ✅       | ✅          | ⚪         | 🔵        | 🔵         | ✅          |
| **A4 CC-C**  | ⚪        | ✅          | ⚪      | —       | ⚪       | ⚪          | 🔵         | ⚪        | ⚪         | ✅          |
| **A5 CC-R**  | ⚪        | ⚪          | ✅     | ⚪       | —       | ✅          | ⚪         | ⚪        | 🔵         | ✅          |
| **A6 CC-Cons** | ⚪      | ⚪          | ✅     | ⚪       | ✅       | —          | ⚪         | ⚪        | 🔵         | ✅          |
| **A7 Design** | ✅       | ✅          | ⚪      | 🔵       | ⚪       | ⚪          | —         | 🔵        | ⚪         | ✅          |
| **A8 DEV-H** | 🔵        | 🔵          | 🔵      | ⚪       | ⚪       | ⚪          | 🔵         | —        | ✅         | ✅          |
| **A9 DEV-AS** | ⚪       | ⚪          | 🔵      | ⚪       | 🔵       | 🔵          | ⚪         | ✅        | —         | ✅          |
| **A10 Blaise** | ✅      | ✅          | ✅     | ✅       | ✅       | ✅          | ✅         | ✅        | ✅         | —          |

**Lecture** : la dernière ligne (A10 Blaise) est intégralement remplie de ✅ — Blaise est interface active avec **les 9 autres acteurs**. C'est la matérialisation du portage manuel actuel.

Total des flux actifs identifiés : ~25 flux non-Blaise + 9 flux Blaise = **34 flux actifs au total**. Avec 9 flux portés par Blaise, **27 % du trafic de coordination passe par lui**.

---

## 4. Flux principaux observés (textuels)

### 4.1 Cluster Hub v2

- **Hub Strat ↔ Hub Content** : Hub Strat transmet la vision produit / pricing / positionnement à Hub Content qui produit le contenu éditorial cohérent. Flux quotidien attendu.
- **Hub Content → Claude Code Content** : briefs de production HTML pour le site / Hub Learning Center. Flux à chaque vague de fiches (vague 7 en cours côté Hub IA-Plateforme = ex-Hub Content).
- **Hub RAG ↔ Claude Code RAG ↔ Claude Code Console** : Hub RAG cadre les sprints, Claude Code RAG prépare les skills/scripts, Claude Code Console implémente en local. Triangle de production technique RAG.
- **Claude Design ↔ Hub Strat + Hub Content** : itérations UX (sprints v1.0, v2.0, v2.1 livrés à ce jour). Flux par sprint (~2-3 semaines de cadence observée).

### 4.2 Cluster Initiative IA

- **DEV IA Head ↔ DEV IA Archi-Sys** : mandats T0.x → T1.x (codifiés dans `SYNC-INTER-CANAUX.md` items I-D). Flux par mandat.
- **DEV IA Head ↔ Cluster Hub** (via Blaise) : rituel hebdo I-C mardi (item I-C-005 ouvert 25/05). Coordination méta.
- **DEV IA Archi-Sys ↔ Cluster Hub** : lecture seule sur production Hub RAG (POC périmètre B = Phase 1 mini RAG convergent).

### 4.3 Flux portés par Blaise (porte humaine)

- Transmission notification Hub Strat → DEV IA Head (25/05 soir)
- Transmission ack notification → Hub Strat + Hub Content + Hub RAG
- Transmission réponses Hub IA Q1/Q2 → DEV IA Head pour clôture I-C-005
- Transmission décisions inter-cluster (ex : reco pricing hybride Cowork Hub IA → Hub Strat repris en mandat)
- Transmission sprints Claude Design → tous les autres acteurs

→ Ces 5 catégories de flux portés par Blaise représentent **la majeure partie du trafic à valeur stratégique** du système. C'est ce que la cartographie doit aider à automatiser ou à alléger.

---

## 5. Risque méta-gouvernance #1 — portage manuel par Blaise

**Diagnostic** (25/05 soir) : 9 interfaces inter-canaux portées mentalement par Blaise, transmission par copier-coller manuel à chaque transaction d'information structurante.

**Conséquences observables** :
- Bandwidth Blaise = goulot. Si indisponibilité 1-2 semaines, blocage projet entier.
- Perte d'information en transmission (la mémoire humaine n'est pas archivable).
- Latence de coordination (un canal attend que Blaise relaie au suivant).
- Charge cognitive constante hors-production (porter la carte mentale des 10 acteurs en permanence).

**Mitigations en cours d'instruction** :
- Ce fichier (cartographie statique) = première étape, visibilité partagée.
- Source de vérité GitHub = évite les divergences de cartographie entre canaux.
- Bloc texte court à coller (cf. §7) = propagation rapide aux canaux qui ignorent l'architecture complète.

**Mitigations à instruire en Phase 2** (post-Cycle 1 mi-juillet) :
- Sortie automatisée de la matrice depuis un fichier source (GitHub Actions ?).
- Convention de transmission inter-canaux non-mémorielle (chaque canal écrit dans un fichier partagé plutôt que d'attendre Blaise).
- Évaluation A2A (Agent-to-Agent protocol) comme couche d'interopérabilité quand pertinent.

---

## 6. Source de vérité et synchronisation

**Source de vérité** : ce fichier dans le repo `LumenBot/dev-environment/00_INSTRUCTIONS/CARTOGRAPHIE-ORCHESTRATION.md`.

**Sync Cowork → Git** : selon le workflow `Guide-Sync-Git_v1` §4.1 (à amender en v1.1 pour mentionner `.decisions/` et `00_INSTRUCTIONS/` — trou identifié 25/05).

**Sync vers les canaux Hub** : par copier-coller du bloc §7 ci-dessous au démarrage de chaque session de chaque canal Hub. Pas d'intégration profonde aux prompts boot pour l'instant (cf. décision sondage D-026 25/05 soir).

**Mise à jour** : DEV IA Head propose les modifications, Blaise valide (L2). Modifications triggers :
- Création / fermeture d'un canal Cowork
- Détection de flux nouveau entre 2 acteurs qui n'en avaient pas
- Apprentissage Cycle 1 sur la qualité de la convention

---

## 7. Bloc texte à coller au démarrage d'une session Hub (Strat / Content / RAG)

> Copie-colle l'encadré suivant en début de session sur n'importe quel canal Hub pour donner à l'agent la vision complète des 10 acteurs. Le bloc se suffit à lui-même, pas besoin d'autre contexte sur l'architecture.

---

```markdown
# Contexte d'orchestration multi-canaux (v1, 2026-05-25)

Tu travailles dans un système à **10 acteurs IA/humains** collaborant en parallèle sur les projets de Blaise Cavalli. Tu n'es qu'un de ces acteurs.

## Les 10 acteurs

| Acteur | Périmètre | Cluster |
|---|---|---|
| Hub Strat | Stratégie produit / GTM / juridique | Hub v2 |
| Hub Content | Contenu site, modules formation | Hub v2 |
| Hub RAG | Pilotage technique RAG | Hub v2 |
| Claude Code Content | Production HTML site | Hub v2 |
| Claude Code RAG | Préparation env logiciel RAG | Hub v2 |
| Claude Code Console | Implémentation RAG local | Hub v2 |
| Claude Design | UX, signature, parcours | Hub v2 |
| DEV IA Head | Méta-gouvernance, patterns transverses | Initiative IA |
| DEV IA Archi-Sys | Architecture système agents | Initiative IA |
| Blaise Cavalli | Décideur, porteur des interfaces inter-canaux | Humain |

## Règles de coordination

1. **Tu restes dans ton périmètre.** Si une demande te sort de ton périmètre, signale-le à Blaise plutôt que de l'absorber silencieusement.
2. **Tes outputs structurants partent à Blaise**, qui décide vers quel(s) autre(s) canal(aux) transmettre. Pas de transmission directe entre canaux.
3. **Tu ne dupliques pas le travail d'un autre canal.** Si tu identifies un chevauchement (ex: Hub Content produit du pricing alors que c'est Hub Strat), signale-le.
4. **Pour les questions méta sur l'architecture elle-même**, oriente Blaise vers DEV IA Head (canal Initiative IA).

## Source de vérité complète

Cartographie détaillée + matrice 10x10 des interfaces + risques méta dans `LumenBot/dev-environment/00_INSTRUCTIONS/CARTOGRAPHIE-ORCHESTRATION.md` v1.0.
```

---

## 8. Historique

| Date | Version | Modification |
|------|---------|--------------|
| 25 mai 2026 (soir) | 1.0 | Création initiale en réponse au risque méta-gouvernance #1 identifié par DEV IA Head le même soir. Sondage D-026 préalable validé par Cavalli (4 hypothèses recommandées confirmées). Statut provisoire — révision majeure à clôture Cycle 1 ≈ mi-juillet en cohérence avec convention multi-acteurs v2. |
