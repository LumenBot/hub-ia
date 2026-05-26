---
code: pattern-grille-decision-architecture
titre: "Pattern — Grille de décision architecture IA par 5 critères"
type: transverse
axe: transverse
niveau: 3
tags: [architecture-ia, grille-decision, 5-criteres, souverainete, ai-act, time-to-value, maturite-technique, budget, pattern-architectural]
version: 3.12.0
last_updated: 2026-05-26
glosaire_termes: [llm, agent, rag, souverainete]
derives: ["[[architecture-a1-saas-proprietaire]]", "[[architecture-a2-proprietaire-managee]]", "[[architecture-a3-os-cloud-souverain]]", "[[architecture-a4-os-on-premise]]", "[[architecture-hybride]]", "[[pattern-souverainete-eu]]", "[[pr-05]]", "[[pr-07]]", "[[pr-09]]", "[[cu-020]]"]
public_cible: [dirigeant, ops, r&d]
---

# Pattern — Grille de décision architecture IA par 5 critères

> Brique transverse référencée par les 5 fiches architectures du Hub IA (A1, A2, A3, A4, Hybride). Méthode canonique de choix d'architecture IA en PME 2026 selon 5 critères de qualification métier et technique. Cohérence avec [[pr-09]] (Cadrer un projet IA) et [[pr-07]] (Build vs Buy).

## Pourquoi une grille de décision dédiée architecture

Le choix d'**architecture IA** structure tous les autres choix techniques d'un projet : modèle LLM, hébergement, vector store, framework, observabilité. Mais ce choix est souvent fait par défaut (le SaaS connu, le cloud déjà en place) plutôt que par arbitrage explicite.

La **grille de décision en 5 critères** permet d'objectiver le choix entre les 5 architectures de référence Hub IA :
- **A1** : SaaS propriétaire — accès direct au modèle via API ou interface du fournisseur, cloud public
- **A2** : Propriétaire managé — modèle propriétaire déployé dans cloud client avec data residency (hyperscaler)
- **A3** : Open-source cloud souverain — modèle open-weight sur cloud EU souverain
- **A4** : Open-source on-premise — modèle open-source/open-weight sur infrastructure cliente
- **Hybride** : combinaison orientée flux, calibrée par cas d'usage

Chaque architecture a un profil de risques/avantages spécifique. La grille permet d'éviter les choix par inertie ou par mode.

## Les 5 critères canoniques

### Critère 1 — Sensibilité des données traitées

La nature des données soumises à l'IA détermine le niveau de confidentialité requis et donc le niveau de souveraineté minimal (cf. [[pattern-souverainete-eu]]).

| Niveau de sensibilité | Caractéristiques | Architectures éligibles |
|---|---|---|
| **Publique** | Données déjà publiques (web, presse, documentation publique) | A1, A2, A3, A4 |
| **Standard PME** | Données internes non personnelles, échanges commerciaux génériques | A1, A2, A3, A4 |
| **Personnelle** | RGPD applicable (clients, employés, prospects) | A2, A3, A4 |
| **Stratégique** | R&D, PI, fichiers clients premium, secrets commerciaux | A3, A4 |
| **Ultra-sensible** | Santé HDS, défense, OIV/OSE, biométrie, données mineurs | A4 |

**Question opérationnelle** : à quel niveau se situent les données du cas d'usage le plus sensible ? L'architecture choisie doit couvrir ce niveau.

### Critère 2 — Haut risque AI Act

Le règlement européen AI Act (entrée en vigueur progressive 2025-2027) qualifie certains systèmes IA en « haut risque » (santé, RH, éducation, sécurité publique, infrastructures critiques). Ces systèmes sont soumis à des obligations renforcées (cf. [[cu-020]] §4 niveaux de risque + Art. 14 supervision humaine + Art. 50 transparence).

**Question opérationnelle** : le cas d'usage est-il classé haut risque AI Act ?
- **Non haut risque** : A1, A2, A3, A4 ouverts (selon autres critères)
- **Haut risque** : A3 ou A4 fortement recommandé (auditabilité du modèle + souveraineté juridique facilitent la conformité)

### Critère 3 — Time-to-value attendu

Le délai entre la décision d'engager un projet IA et la mise en production opérationnelle structure significativement le choix d'architecture.

| Time-to-value cible | Architectures éligibles |
|---|---|
| **Quelques jours** (POC, prototype) | A1 (plug-and-play maximal) |
| **Quelques semaines** | A1, A2 |
| **Quelques mois** | A2, A3 |
| **6-12 mois** (industrialisation soignée) | A3, A4 |

**Question opérationnelle** : quelle est l'urgence ? Le pattern « POC rapide A1 puis production A3 » est légitime quand il est planifié dès le départ — voir [[pr-09]] §pattern « refuser d'avancer ».

### Critère 4 — Maturité technique de l'organisation

L'opération d'une architecture IA requiert des compétences variables selon le niveau d'autonomie souhaité.

| Maturité technique | Compétences disponibles | Architectures éligibles |
|---|---|---|
| **Faible** (PME non-tech) | Aucune équipe DevOps/MLOps | A1 |
| **Moyenne** (équipe IT générique) | Équipe cloud existante AWS/Azure/GCP | A1, A2 |
| **Avancée** (équipe MLOps) | DevOps/MLOps 0,5-1 ETP | A1, A2, A3 |
| **Experte** (équipe MLOps dédiée + SRE) | MLOps + SRE + sécurité internes | A1, A2, A3, A4 |

**Question opérationnelle** : quelle équipe technique est mobilisable, à quel niveau d'effort ?

### Critère 5 — Budget annuel mobilisable

Le coût global (CAPEX initial + OPEX annuel) varie significativement entre architectures, avec un seuil important entre A2/A3 (cloud sans hardware) et A4 (hardware on-premise + équipe dédiée).

| Budget annuel global | Architectures éligibles |
|---|---|
| **< 10 K€/an** | A1 (usages individuels et POC) |
| **10-50 K€/an** | A1, A2 (usages PME standard) |
| **50-150 K€/an** | A1, A2, A3 (usages PME/ETI avec souveraineté) |
| **> 150 K€/an** | A1, A2, A3, A4 (cas avec exigences fortes ou volumes massifs) |

**Question opérationnelle** : quel budget annuel total (initial amorti + récurrent) est mobilisable pour le projet IA ?

## Application — Méthode décisionnelle

### Étape 1 — Qualifier les 5 critères pour le cas d'usage

Pour chaque cas d'usage identifié, qualifier les 5 critères et noter les architectures éligibles à l'intersection (architectures qui satisfont les 5 conditions simultanément).

### Étape 2 — Identifier les contraintes éliminatoires

Si un critère élimine toutes les architectures sauf une (ex. ultra-sensible santé HDS = A4 uniquement), le choix est largement fait.

Si plusieurs architectures restent éligibles, passer à l'étape 3.

### Étape 3 — Arbitrage final par critère dominant

Choisir l'architecture qui maximise le critère le plus important pour le cas d'usage :
- Time-to-value prioritaire → A1
- Souveraineté juridique forte → A3 ou A4
- Auditabilité du modèle (PI, R&D) → A3 ou A4
- Économie sur les volumes massifs → A4

### Étape 4 — Vérifier la cohérence avec les autres cas d'usage

Si l'organisation a plusieurs cas d'usage IA, vérifier la cohérence d'architecture cross-usages. **Une stack [[architecture-hybride]] orientée flux** est souvent plus réaliste qu'une stack monoarchitecturale forcée.

## Quand passer à une architecture Hybride

L'architecture Hybride (voir [[architecture-hybride]]) devient pertinente quand :

- **Plusieurs cas d'usage** ont des profils de sensibilité différents (le RH = A2 stricte ; la veille = A1 ; le R&D = A4)
- **Aucune architecture monolithique** ne satisfait tous les cas d'usage sans surdimensionnement
- **L'organisation peut maintenir** 2-3 patterns sans tomber dans le « patchwork ingérable »

Le pattern Hybride orienté flux (« chaque cas d'usage est analysé pour sa sensibilité, et la stack est calibrée en conséquence ») est explicitement décrit côté HTML Hub IA comme « le pattern le plus fréquent en réalité opérationnelle ».

## Cas d'application en PME

### Cas 1 — PME services BtoB 50 salariés, démarrage IA

- Critères : standard PME / non haut risque / time-to-value semaines / maturité faible-moyenne / budget 20-40 K€/an
- **Architectures éligibles** : A1, A2
- **Recommandation** : démarrer A1 (Le Chat Pro + ChatGPT Plus + Claude Pro pour usages individuels) → bascule A2 si volumétrie justifie API d'entreprise

### Cas 2 — PME industrielle 100 salariés, R&D protégée

- Critères : stratégique (R&D) / non haut risque / time-to-value 6-12 mois / maturité avancée / budget 80-150 K€/an
- **Architectures éligibles** : A3, A4
- **Recommandation** : A3 (Mistral Cloud EU + Lucie OVHcloud pour les outils R&D, auditabilité du modèle + souveraineté EU forte)

### Cas 3 — PME santé 30 salariés, données patients

- Critères : ultra-sensible (HDS) / haut risque AI Act / time-to-value 6-12 mois / maturité moyenne / budget 60-100 K€/an
- **Architectures éligibles** : A4 (HDS impose on-premise typiquement)
- **Recommandation** : A4 light (Mistral self-host sur infrastructure HDS + équipe MLOps externalisée)

### Cas 4 — ETI multi-cas 250 salariés, usages variés

- Critères : variable selon cas (RH = personnel ; veille = public ; R&D = stratégique)
- **Architectures éligibles** : combinaison
- **Recommandation** : **Hybride** orientée flux ([[architecture-hybride]]) — A1 pour usages individuels, A2 pour RH/finance, A3 pour R&D

## Anti-patterns à éviter

- **Choix par inertie** : utiliser ChatGPT par défaut parce que tout le monde l'utilise, sans qualifier la sensibilité des données traitées
- **Cloud-first sans réflexion** : aller systématiquement vers SaaS US sans considérer la souveraineté
- **Souverain partout** : choisir A4 même pour les cas où A1 ou A2 suffiraient → surdimensionnement coûteux
- **Patchwork ingérable** : multiplier les architectures sans gouvernance → 5+ patterns en parallèle deviennent ingérables
- **Décision figée** : ne jamais ré-évaluer le choix au-delà du démarrage → POC A1 en production pendant 3 ans alors que A3 serait plus approprié

## Pour aller plus loin

- **Architectures de référence** : [[architecture-a1-saas-proprietaire]], [[architecture-a2-proprietaire-managee]], [[architecture-a3-os-cloud-souverain]], [[architecture-a4-os-on-premise]], [[architecture-hybride]]
- **Pattern souveraineté EU** ([[pattern-souverainete-eu]]) : 4 critères + 4 niveaux + acteurs souverains par catégorie
- **Cadrer un projet IA** ([[pr-09]]) : 8 questions de cadrage stratégique amont (le critère sensibilité données = question 3 PR-09, contraintes réglementaires = question 4)
- **Build vs Buy** ([[pr-07]]) : arbitrage post-cadrage, complémentaire à la grille architecture
- **Conformité RGPD/AI Act** ([[cu-020]]) : cadre réglementaire qui qualifie le critère 2 (haut risque AI Act)
- **Sécurité IA cadrage stratégique** ([[pr-05]]) : la sécurité IA est l'une des dimensions transverses du choix d'architecture
