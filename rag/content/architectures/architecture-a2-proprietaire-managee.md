---
code: architecture-a2-proprietaire-managee
titre: "Architecture A2 — Propriétaire managé (cloud client avec data residency EU)"
type: architecture
axe: B
niveau: 3
tags: [architecture-ia, a2, hyperscaler, aws-bedrock, azure-openai, vertex-ai, anthropic-on-vertex, data-residency-eu, cloud-act]
version: 3.12.0
last_updated: 2026-05-26
glosaire_termes: [llm, agent, rag, souverainete]
derives: ["[[pattern-grille-decision-architecture]]", "[[pattern-souverainete-eu]]", "[[outils-llm]]", "[[cu-020]]", "[[pr-05]]", "[[pr-08]]", "[[dep-06]]", "[[architecture-a1-saas-proprietaire]]", "[[architecture-a3-os-cloud-souverain]]", "[[architecture-hybride]]"]
public_cible: [dirigeant, ops, r&d]
---

# Architecture A2 — Propriétaire managé (cloud client avec data residency EU)

## L'essentiel à retenir

**Architecture A2 propriétaire managé en PME 2026 : modèle IA propriétaire (Anthropic, OpenAI, Cohere) déployé dans un environnement cloud sous contrôle du client (AWS, Azure, GCP), avec data residency garantie (souvent EU). Pattern de référence pour les organisations déjà engagées sur un hyperscaler pour leur SI général. Exemples canoniques : AWS Bedrock, Azure OpenAI, Vertex AI, Anthropic on Vertex, OpenAI Enterprise. Tarification au token équivalente au SaaS direct avec overhead infrastructure ~10-20 %, coût récurrent typique 200-2 000 €/mois selon volume, setup compte cloud / VPC 5-15 K€ si pas déjà en place. Souveraineté Moderate avec caveat CLOUD Act (hyperscalers juridiquement US). Frontière A2/A3 : modèle propriétaire + hyperscaler CLOUD Act vs modèle open-weight + cloud souverain EU non-CLOUD-Act. Voir [[pattern-grille-decision-architecture]] pour le positionnement.**

**Subtilité souveraineté critique** : A2 offre une data residency contrôlée (les données restent en EU pendant le traitement) mais pas une souveraineté juridique complète. AWS, Azure, GCP sont des entités US soumises au CLOUD Act, qui peut théoriquement contraindre la divulgation de données à des autorités US même si les données sont stockées en EU. Pour les données vraiment stratégiques, A3 ou A4 sont préférables. Pour les données « simplement RGPD », A2 est une réponse pragmatique.

## À qui s'adresse cette architecture

PME ou ETI déjà engagée sur un hyperscaler (AWS, Azure, GCP) pour son SI général qui veut intégrer l'IA en cohérence avec sa stack cloud existante, sans introduire de nouveau fournisseur. Cible aussi les organisations ayant des exigences RGPD strictes (data residency EU contractualisée) mais pour qui le CLOUD Act reste acceptable.

Niveau ⭐⭐⭐ Avancé. Public cible : DSI, RSSI, dirigeants tech.

## Description

**Modèle propriétaire managed via cloud hyperscaler** : le modèle propriétaire (Claude via AWS Bedrock, GPT via Azure OpenAI, Gemini via Vertex AI) est consommé via le cloud du client. Le client garde la maîtrise du VPC, des contrats, de la data residency. Le fournisseur du modèle ne voit pas les données client (engagement no-training contractuel typique).

## Méta

| Critère | Niveau |
|---|---|
| **Souveraineté** | 🟡 Moyenne (Moderate avec caveat CLOUD Act — voir [[pattern-souverainete-eu]]) |
| **Complexité** | 🛠️🛠️ Setup léger (compte cloud + VPC + IAM + monitoring) |
| **Coût d'entrée** | 🟡 Moyen (5-15 K€ setup si pas de cloud déjà en place) |
| **Time to value** | 🟡 Quelques semaines |

## Exemples typiques

Citations textuelles à transposer fidèlement :

- **AWS Bedrock** : Claude (Anthropic), Llama (Meta), Mistral, Cohere, etc. — région EU possible
- **Azure OpenAI** : GPT-4o, GPT-5 — région EU possible (France Central, Sweden Central)
- **Vertex AI** (Google Cloud) : Gemini, Anthropic Claude on Vertex AI, Cohere on Vertex AI — région EU possible (europe-west)
- **OpenAI Enterprise** : engagement no-training contractualisé + data residency EU + audit + SLA renforcé

**À noter** : la combinaison « Anthropic Claude on Vertex AI » illustre que le **fournisseur du modèle** (Anthropic) et le **fournisseur du cloud** (Google) sont distincts en A2 — c'est précisément ce qui différencie A2 de A1 (où l'éditeur du modèle héberge directement).

## ✅ Quand l'utiliser

- **Organisation déjà engagée hyperscaler** : intégration native, contrats consolidés, équipe cloud existante mobilisable
- **Données RGPD strict** : data residency EU contractualisée par le contrat hyperscaler
- **Cas d'usage modérément sensibles** : RH générique, finance opérationnelle, communication client — pas les données ultra-stratégiques
- **Besoin SLA serré** : SLA Enterprise des hyperscalers (99,9-99,99 %) supérieur aux plans SaaS individuels
- **Conformité auditée** : audit logs, monitoring, conformité documentée par l'hyperscaler

## ❌ Quand l'éviter

- **Données ultra-stratégiques** : R&D protégée, PI critique, secrets industriels — privilégier A3 ou A4
- **Réglementations sectorielles strictes** (OIV, OSE, santé HDS, défense) : le CLOUD Act peut être incompatible → A3 ou A4 obligatoires
- **PME sans équipe cloud existante** : le setup AWS/Azure/GCP from scratch ajoute une complexité non justifiée → préférer A1
- **Volumes très faibles** : la surcharge overhead infrastructure (~10-20 %) n'est pas amortie sur petits volumes → préférer A1
- **Recherche de souveraineté juridique forte** : CLOUD Act rédhibitoire → A3 (cloud souverain EU non-CLOUD-Act) ou A4

## ⚠️ Risques / Subtilité souveraineté / Avantage différenciant

### ⚠️ Risques

- **CLOUD Act applicable** : AWS, Azure, GCP sont des entités US soumises au CLOUD Act. Même avec data residency EU contractualisée, les autorités US peuvent théoriquement contraindre la divulgation. Voir [[pattern-souverainete-eu]] niveau Moderate.
- **Lock-in hyperscaler** : changer de cloud (AWS → OVHcloud par exemple) nécessite re-développement significatif. Souvent plus difficile qu'attendu.
- **Coûts cachés** : transfer egress fees (sortie de données du cloud), stockage logs, support Enterprise = surcoûts récurrents non négligeables.
- **Dépendance fournisseur double** : modèle (Anthropic/OpenAI) ET cloud (AWS/Azure) — 2 contractualisations à maintenir, 2 chaînes de support.

### 💡 Avantage différenciant

A2 est **le compromis pragmatique** entre A1 (simplicité maximale, souveraineté minimale) et A3 (souveraineté forte, complexité élevée). Pour les organisations déjà cloud-native, A2 minimise la friction d'intégration tout en améliorant significativement le niveau de contrôle vs A1. C'est souvent l'architecture de transition naturelle quand les premiers usages A1 démontrent leur valeur et qu'on cherche à industrialiser.

## Coût indicatif

Coûts canoniques HTML à citer textuellement (R10 stricte) :

- **Modèle de tarification au token** : équivalent au SaaS direct (~0,01-0,10 €/1k tokens selon modèle) mais avec un **overhead infrastructure ~10-20 %** lié au passage par le cloud client
- **Coût initial setup compte cloud / VPC** : ~5-15 K€ si pas déjà en place (sinon négligeable car infrastructure déjà mobilisée)
- **Coût récurrent typique PME/ETI** : **200-2 000 €/mois** selon volume

> **Encart « scénario indicatif PME 50 salariés A2 dominant » (extrapolation Cowork, non canonique HTML)** : ~30-60 K€/an selon usage (consommation API 12-24 K€/an + overhead cloud 2-5 K€/an + accompagnement intégration cloud 10-20 K€/an + monitoring/observabilité 3-5 K€/an + support Enterprise 5-10 K€/an). À ajuster selon volume et profil cloud existant.

## Articulation cross-archis (frontières)

- **A2 vs A1** : la frontière est **cloud public direct vs cloud client avec data residency contrôlée**. Pas l'origine de l'éditeur. Le Chat Mistral via cloud Mistral public = A1. Anthropic Claude on AWS Bedrock région Francfort = A2. Le modèle peut être identique (Claude), c'est le mode d'accès et de contrôle qui change.
- **A2 vs A3** : double frontière — modèle (propriétaire vs open-weight) ET cloud (hyperscaler CLOUD Act vs cloud souverain EU). A2 = Anthropic Claude on AWS Bedrock. A3 = Mixtral sur OVHcloud. Auditabilité du modèle absente A2 vs présente A3.
- **A2 vs A4** : A4 = full on-premise. A2 = cloud hyperscaler géré. Différence opérationnelle maximale (équipe MLOps interne requise A4 vs équipe cloud existante mobilisable A2).
- **A2 dans une stack Hybride** : fréquent pour les cas RH/finance (haut risque AI Act demande data residency contractuelle, sans aller jusqu'à on-premise). Voir [[architecture-hybride]].

### 🔭 Variantes à surveiller

- **Anthropic Claude on Vertex AI** : combinaison hybride d'éditeurs (modèle Anthropic, cloud Google) avec data residency EU
- **Cohere on Vertex AI** : alternative pour cas multilingues
- **OpenAI Enterprise avec engagement no-training renforcé** : rapproche de A2 même quand l'accès est direct via OpenAI

## Pour aller plus loin

- **Pattern grille de décision architecture** ([[pattern-grille-decision-architecture]]) : méthode 5 critères pour arbitrer A2 vs A1/A3
- **Pattern souveraineté EU** ([[pattern-souverainete-eu]]) : niveau Moderate détaillé + caveat CLOUD Act
- **Outils LLM** ([[outils-llm]]) : Claude, GPT, Gemini disponibles via hyperscalers
- **Conformité RGPD/AI Act** ([[cu-020]]) : data residency EU et limites du CLOUD Act
- **Sécurité IA cadrage stratégique** ([[pr-05]]) : A2 dans le cadre sécurité PME
- **Inférence et coûts SaaS vs self-hosted** ([[dep-06]]) : arbitrage A2 vs A3/A4 sur volumes
- **Architecture A1** ([[architecture-a1-saas-proprietaire]]) : entrée naturelle avant A2
- **Architecture A3** ([[architecture-a3-os-cloud-souverain]]) : bascule naturelle si CLOUD Act devient bloquant
- **Architecture Hybride** ([[architecture-hybride]]) : A2 combiné à A1/A3/A4 par cas d'usage
