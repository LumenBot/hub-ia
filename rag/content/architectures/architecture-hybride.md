---
code: architecture-hybride
titre: "Architecture Hybride — combinaison orientée flux"
type: architecture
axe: B
niveau: 3
tags: [architecture-ia, hybride, orientee-flux, politique-ia, shadow-ai, cartographie-usages, multi-pattern]
version: 3.12.0
last_updated: 2026-05-26
glosaire_termes: [llm, agent, rag, souverainete]
derives: ["[[pattern-grille-decision-architecture]]", "[[pattern-souverainete-eu]]", "[[architecture-a1-saas-proprietaire]]", "[[architecture-a2-proprietaire-managee]]", "[[architecture-a3-os-cloud-souverain]]", "[[architecture-a4-os-on-premise]]", "[[cu-020]]", "[[pr-05]]", "[[pr-09]]"]
public_cible: [dirigeant, ops, r&d]
---

# Architecture Hybride — combinaison orientée flux

## L'essentiel à retenir

**Architecture Hybride en PME/ETI 2026 : combinaison orientée flux des patterns A1/A2/A3/A4 calibrée par cas d'usage selon la sensibilité des données et les exigences de souveraineté. Pattern explicitement décrit côté HTML Hub IA comme « le pattern le plus fréquent en réalité opérationnelle » — une PME / ETI typique en 2026 a souvent une stack hybride même sans s'en rendre compte. Exemple type : ChatGPT/Claude grand public pour usages individuels (A1) + Mistral Cloud EU pour agents IA traitant des données client (A3) + AWS Bedrock data residency EU pour cas haut risque RH/finance (A2) + Mistral self-hosted on-premise pour R&D protégée (A4). 4 disciplines clés : politique IA documentée + cartographie Shadow AI + choix technologiques convergents (max 2-3 patterns) + mise à jour régulière. 3 anti-patterns : Cloud-first sans réflexion / Souverain partout / Patchwork ingérable. Voir [[pattern-grille-decision-architecture]] §quand-passer-hybride pour la méthode décisionnelle.**

**Principe directeur** : « Forcer un seul pattern pour tous les usages = inefficacité économique et organisationnelle. Le bon design est orienté flux : chaque cas d'usage est analysé pour sa sensibilité, et la stack est calibrée en conséquence. »

## À qui s'adresse cette architecture

PME ou ETI avec **plusieurs cas d'usage IA aux profils de sensibilité différents** : un cas peut justifier A1 (recherche grand public), un autre A2 (RH avec data residency), un autre A3 (R&D souveraine), un autre A4 (santé HDS). Une architecture monolithique forcée serait sous-optimale ou surdimensionnée.

Niveau ⭐⭐⭐ Avancé. Public cible : DSI, RSSI, dirigeants tech qui pilotent un portefeuille d'usages IA hétérogène.

## Description

**Combinaison orientée flux** des architectures A1, A2, A3, A4 où chaque cas d'usage est routé vers l'architecture la plus adaptée à sa sensibilité et à ses contraintes. Une politique IA documentée + une cartographie des usages + des choix technologiques convergents évitent le piège du patchwork ingérable.

## Méta

| Critère | Niveau |
|---|---|
| **Souveraineté** | Variable selon flux (Light à Sovereign) |
| **Complexité** | 🛠️🛠️🛠️ Moyenne à Élevée (gouvernance multi-architectures) |
| **Coût d'entrée** | Variable selon mix |
| **Time to value** | Variable selon flux (quelques jours pour A1 à 6-12 mois pour A4) |

## Exemples typiques

Citation textuelle HTML à transposer fidèlement (illustration ETI typique 2026) :

- **Les collaborateurs utilisent ChatGPT / Claude grand public** pour des usages individuels (pattern A1, recherche augmentée, reformulation)
- **L'équipe technique utilise Mistral Cloud EU** pour les agents IA traitant des données client (pattern A3)
- **Les cas d'usage haut risque (RH, finance) utilisent AWS Bedrock avec data residency EU** (pattern A2)
- **Le cas d'usage stratégique (R&D protégée) tourne sur Mistral self-hosted en on-premise** (pattern A4)

**À noter** : cette répartition est typique d'une ETI 200-500 salariés. Une PME 50 salariés aura plus souvent un mix A1+A3 ou A1+A2 selon profil. Une grande administration aura A2+A3+A4 selon classification des données.

## ✅ Quand l'utiliser

- **Portefeuille d'usages IA hétérogène** : 3+ cas d'usage avec sensibilités différentes
- **Organisation cloud-mature avec souveraineté différenciée** par cas d'usage
- **Volonté d'optimiser coût-souveraineté par flux** plutôt que de surdimensionner par défaut
- **ETI 200+ salariés** ou PME 50+ avec ambition IA structurée
- **Réalité empirique** : si la cartographie Shadow AI révèle déjà plusieurs patterns en parallèle, formaliser plutôt que tenter de tout standardiser

## ❌ Quand l'éviter

- **Cas d'usage unique** : pas de besoin d'architecture hybride si un seul flux IA en jeu → choisir le pattern le plus adapté (A1/A2/A3/A4)
- **PME 5-15 salariés** : la gouvernance multi-architectures est souvent disproportionnée → un seul pattern (probablement A1) suffit
- **Pas de capacité gouvernance** : sans politique IA documentée + responsable IA identifié, le hybride devient rapidement un patchwork ingérable
- **Volonté de standardisation forte** : si l'organisation privilégie la simplicité opérationnelle sur l'optimisation, monoarchitecture préférable

## ⚠️ Risques / Subtilité gouvernance / Avantage différenciant

### ⚠️ Risques (anti-patterns Hybride canoniques HTML)

3 anti-patterns à éviter (citations textuelles HTML) :

1. **Cloud-first sans réflexion** : aller systématiquement vers SaaS US sans considérer la souveraineté pour les cas qui le justifient. Symptôme : ChatGPT utilisé pour les CV RH alors que A2 serait approprié.
2. **Souverain partout** : choisir A3 ou A4 pour tous les cas, y compris ceux où A1 suffirait. Surdimensionnement coûteux. Symptôme : Mistral self-hosted pour la rédaction de notes internes.
3. **Patchwork ingérable** : multiplier les architectures (5+ patterns en parallèle) sans gouvernance. Symptôme : chaque équipe métier choisit son outil IA sans cohérence transverse.

### 💡 Avantage différenciant

Hybride est le **pattern le plus fréquent en réalité opérationnelle** selon le HTML canon Hub IA. C'est aussi le plus optimisé économiquement et organisationnellement quand il est piloté correctement (4 disciplines ci-dessous). Pour une PME/ETI avec portefeuille d'usages IA, refuser le hybride = forcer un pattern unique = sous-optimisation systématique.

## Les 4 disciplines de gouvernance Hybride

Citations textuelles HTML à transposer fidèlement :

### 1. Politique IA documentée

Un document écrit (1-3 pages) qui formalise :
- Quels outils IA sont autorisés pour quels usages
- Quels niveaux de sensibilité de données pour quelle architecture
- Qui est responsable de la gouvernance IA
- Comment l'organisation traite les demandes d'usage nouveaux

### 2. Cartographie Shadow AI

Inventaire régulier (semestriel ou annuel) des usages IA réels dans l'organisation, **y compris les usages non autorisés** (Shadow AI : ChatGPT personnel utilisé pour des tâches pro, outils non répertoriés, etc.). Permet de qualifier le mix architectures réellement opéré vs le mix politique théorique.

### 3. Choix technologiques convergents (max 2-3 patterns)

Discipline : **maintenir 2-3 patterns au maximum** dans l'organisation. Au-delà, le hybride devient patchwork ingérable. Si la cartographie Shadow AI révèle 5+ patterns, opération de rationalisation à mener (consolidation vers les patterns canoniques retenus).

### 4. Mise à jour régulière

Révision annuelle de la politique IA + cartographie + choix technologiques. Le marché IA évolue rapidement (nouveaux modèles tous les 3-6 mois, nouvelles offres cloud souverain, évolutions AI Act). Un mix figé devient rapidement sous-optimal.

## Coût indicatif

Coût variable selon le mix retenu :

- **Hybride A1 + A3** (PME 50 sal, profil tech mature) : ~50-100 K€/an (A1 grand public 10-20 K€ + A3 Mistral Cloud EU + équipe MLOps 40-80 K€)
- **Hybride A1 + A2** (PME 100 sal, profil cloud mature) : ~40-80 K€/an (A1 grand public 15-25 K€ + A2 hyperscaler 25-55 K€)
- **Hybride A1 + A2 + A3 + A4** (ETI 250 sal multi-cas) : ~200-500 K€/an (somme des contributions, gouvernance + équipe MLOps incluse)

> **Encart « scénario indicatif ETI 250 salariés Hybride 4 patterns » (extrapolation Cowork, non canonique HTML)** : A1 individuel 30-50 K€/an + A2 RH/finance 50-100 K€/an + A3 R&D souverain 100-200 K€/an + A4 cas ultra-stratégique 150-300 K€/an + gouvernance IA 20-40 K€/an. Total ~350-690 K€/an pour ETI avec ambition IA structurée. À ajuster selon mix réel.

## Articulation cross-archis (frontières)

L'architecture Hybride n'est pas un pattern « parallèle » aux 4 autres — c'est leur **mode de combinaison gouvernée**. Toutes les frontières A1/A2/A3/A4 restent valides à l'intérieur du hybride :

- **A1 dans Hybride** : usages individuels grand public, POC, prototypage
- **A2 dans Hybride** : cas RH/finance avec data residency EU, intégration cloud existante
- **A3 dans Hybride** : usages stratégiques EU avec auditabilité modèle (R&D, données premium)
- **A4 dans Hybride** : cas ultra-stratégiques (santé HDS, défense, OIV)

**Pattern courant** : `A1 (usages individuels) + A3 (production souveraine) + A4 (cas ultra-stratégiques uniquement)`. Évite A2 si l'organisation n'a pas de stack cloud hyperscaler existante.

### 🔭 Variantes à surveiller

- **Hybride orienté flux avec routing automatique** : émergence d'orchestrateurs (Composio, Beever Atlas, n8n) qui routent automatiquement vers la bonne architecture selon métadonnées du cas d'usage
- **Coopératives EU** (Petals, EuroLLM) : variante Hybride distribuée avec partage d'infrastructure entre PME/ETI
- **BYOM (Bring Your Own Model)** : pattern émergent qui floute les frontières A2/A3 (modèle propriétaire fine-tuné déployé en cloud souverain EU)

## Discipline de mise en place — méthode 5 étapes

1. **Cartographier les cas d'usage IA** existants et planifiés (au moins 3-5)
2. **Qualifier chaque cas d'usage** selon les 5 critères de la grille ([[pattern-grille-decision-architecture]])
3. **Identifier les patterns nécessaires** (souvent 2-3) pour couvrir les cas, pas plus
4. **Rédiger la politique IA** (1-3 pages) qui formalise les choix et le routing
5. **Opérer la cartographie Shadow AI** annuelle + révision politique annuelle

## Pour aller plus loin

- **Pattern grille de décision architecture** ([[pattern-grille-decision-architecture]]) : méthode 5 critères qui structure le choix par flux dans le Hybride
- **Pattern souveraineté EU** ([[pattern-souverainete-eu]]) : 4 niveaux qui qualifient chaque flux
- **Architecture A1** ([[architecture-a1-saas-proprietaire]]) : pour les usages individuels du Hybride
- **Architecture A2** ([[architecture-a2-proprietaire-managee]]) : pour les cas data residency du Hybride
- **Architecture A3** ([[architecture-a3-os-cloud-souverain]]) : pour les cas souveraineté du Hybride
- **Architecture A4** ([[architecture-a4-os-on-premise]]) : pour les cas ultra-stratégiques du Hybride
- **Cadrer un projet IA** ([[pr-09]]) : 8 questions à appliquer cas d'usage par cas d'usage dans un Hybride
- **Conformité RGPD/AI Act** ([[cu-020]]) : politique IA documentée comme exigence Art. 4 (formation IA obligatoire)
- **Sécurité IA cadrage stratégique** ([[pr-05]]) : gouvernance Hybride dans le cadre sécurité PME
