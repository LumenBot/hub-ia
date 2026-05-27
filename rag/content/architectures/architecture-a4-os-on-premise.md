---
code: architecture-a4-os-on-premise
titre: "Architecture A4 — Open-source on-premise (infrastructure cliente)"
type: architecture
axe: B
niveau: 3
tags: [architecture-ia, a4, on-premise, sovereign, lighton-paradigm, ollama, llama-cpp, vllm, tgi, edge-ai, secnumcloud, oiv, ose, hds]
version: 3.12.0
last_updated: 2026-05-26
glosaire_termes: [llm, agent, rag, souverainete]
derives: ["[[pattern-grille-decision-architecture]]", "[[pattern-souverainete-eu]]", "[[outils-llm]]", "[[dep-02]]", "[[dep-06]]", "[[pr-05]]", "[[cu-020]]", "[[architecture-a3-os-cloud-souverain]]", "[[architecture-hybride]]"]
public_cible: [dirigeant, ops, r&d]
---

# Architecture A4 — Open-source on-premise (infrastructure cliente)

## L'essentiel à retenir

**Architecture A4 open-source on-premise en PME/grandes administrations 2026 : modèles open-source/open-weight ([[outils-llm|Lucie]], [[outils-llm|Mistral]], [[outils-llm|Llama]], [[outils-llm|Mixtral]]) déployés sur infrastructure cliente — data centers internes, GPU on-premise, edge devices. Aucune donnée ne sort de l'organisation. Pattern requis pour les cas ultra-stratégiques : défense, santé sensible HDS, R&D protégée, OIV/OSE, edge industriel, robotique. Exemples canoniques : Lucie/Mistral/Llama/Mixtral on GPU internes (NVIDIA H100, A100, stations DGX), Ollama + llama.cpp pour déploiements légers, vLLM ou TGI pour industriels, [[outils-llm|LightOn]] Paradigm on-premise pour grandes administrations, Edge AI sur appareils embarqués (NVIDIA Jetson, IoT industriel). Hardware GPU 30-150 K€ initial, MLOps 0,5 à 1 ETP, énergie 1-3 K€/mois, setup ≥ 50 K€. Souveraineté Sovereign (full self-host EU + équivalent SecNumCloud). Voir [[pattern-grille-decision-architecture]] pour positionnement vs A1/A2/A3/Hybride.**

**Subtilité importante** : A4 n'est pas « A3 + on-premise ». La complexité opérationnelle est qualitativement différente (équipe MLOps + SRE + sécurité internes, hardware GPU, mises à jour modèles tous les 3-6 mois). Ne pas s'engager A4 sans capacité à prendre en charge la sécurité de bout en bout.

## À qui s'adresse cette architecture

Grandes administrations, opérateurs OIV/OSE (NIS2), établissements santé HDS, structures défense, ETI avec R&D protégée critique, organisations industrielles avec edge AI ou contraintes latence ultra-critique.

Niveau ⭐⭐⭐⭐ Expert. Public cible : DSI, RSSI, équipes MLOps + SRE internes, dirigeants tech avec exigences souveraineté maximales.

## Description

**Modèle open-source/open-weight déployé sur infrastructure cliente** : data centers internes, GPU on-premise (NVIDIA H100, A100, stations DGX), ou edge devices (NVIDIA Jetson, IoT industriel). Aucune donnée ne sort de l'organisation à aucun moment du cycle (inférence, monitoring, fine-tuning).

## Méta

| Critère | Niveau |
|---|---|
| **Souveraineté** | 🟢 Maximale (Sovereign — voir [[pattern-souverainete-eu]] niveau 4) |
| **Complexité** | 🛠️🛠️🛠️🛠️ Élevée (hardware + MLOps + SRE + sécurité) |
| **Coût d'entrée** | 🔴 Élevé (hardware GPU 30-150 K€ + setup ≥ 50 K€) |
| **Time to value** | 🔴 6-12 mois |

## Exemples typiques

Citations textuelles à transposer fidèlement :

- **Lucie / Mistral / Llama / Mixtral auto-hébergés** sur GPU internes (NVIDIA H100, A100, ou stations DGX)
- **Ollama + llama.cpp** pour des déploiements légers (modèles 7B-13B sur stations de travail)
- **vLLM ou TGI** (Text Generation Inference) pour des déploiements industriels
- **LightOn Paradigm** en mode on-premise pour grandes administrations
- **Edge AI** sur appareils embarqués (NVIDIA Jetson, smartphones, IoT industriel)

**À noter** : LightOn Paradigm est explicitement cité côté HTML pour les **grandes administrations** — c'est la solution enterprise full souveraine française de référence A4. Pour les déploiements légers et flexibles, Ollama + llama.cpp suffisent souvent. Pour les industriels, vLLM ou TGI.

## ✅ Quand l'utiliser

- **Données ultra-stratégiques où aucune sortie de l'organisation n'est tolérable** : défense, santé sensible HDS, R&D protégée
- **Réglementations sectorielles strictes** : OIV (opérateurs d'importance vitale), OSE (opérateurs de services essentiels, NIS2), secteurs à exigences nationales spécifiques (énergie, eau, télécoms, finance systémique)
- **Volumes très importants** où l'amortissement du hardware devient économiquement supérieur au cloud (millions de requêtes/jour)
- **Cas d'usage avec contraintes de latence ultra-critique** : edge industriel, robotique, contrôle de processus temps réel
- **Capacité à mobiliser une équipe DevOps / MLOps interne ou via prestataire dédié** : 0,5-1 ETP MLOps minimum

## ❌ Quand l'éviter

- **TPE / PME sans compétence DevOps interne** : pas de capacité à opérer hardware GPU + modèle + monitoring
- **Pas de budget setup ≥ 50 K€** : l'investissement initial hardware + setup est un seuil
- **Volumes faibles** : le hardware ne sera pas amorti, le cloud est économiquement supérieur
- **Cas d'usage standards sans exigence souveraineté maximale** : A3 suffit dans 80-90 % des cas PME/ETI
- **Time-to-value urgent** : 6-12 mois de setup, incompatible avec démarrage rapide

## ⚠️ Risques / Subtilité souveraineté / Coûts cachés

### ⚠️ Risques

- **Hardware obsolescence** : les GPU se déprécient (Moore's Law IA accéléré 2025-2026) → renouvellement hardware tous les 3-5 ans, coût à provisionner
- **Mises à jour modèles** : un nouveau modèle open-source majeur sort tous les 3-6 mois → réinstallation, fine-tuning, validation = effort récurrent significatif
- **Sécurité physique et logique** : si on choisit on-premise, c'est aussi parce qu'on prend en charge la sécurité de bout en bout (incendie, intrusion, sauvegardes, redondance) → coûts cachés importants
- **Indisponibilité = arrêt complet** : pas de backup cloud pour un service A4 critique → DRP (Disaster Recovery Plan) coûteux à mettre en place
- **Talent MLOps rare** : MLOps senior compétent on-premise GPU = profil rare et cher en 2026

### 💡 Avantage différenciant

A4 est **la seule architecture** qui garantit **aucune sortie de données hors de l'organisation** à aucun moment du cycle. Pour les cas où cette garantie est obligatoire (santé HDS, défense classifiée, OIV NIS2), il n'y a pas d'alternative possible. Pour ces cas, A4 n'est pas un choix d'optimisation — c'est une exigence réglementaire ou stratégique non négociable.

## Coût indicatif

Coûts canoniques HTML à citer textuellement (R10 stricte) :

- **Hardware GPU** : 30-150 K€ pour une station ou serveur GPU industriel adapté
- **MLOps** : 0,5 à 1 ETP pour assurer le run, les mises à jour, le monitoring
- **Énergie** : 1-3 K€/mois selon la charge (impact carbone à documenter)
- **Mises à jour modèles** : un nouveau modèle open-source majeur sort tous les 3-6 mois — réinstallation, fine-tuning, validation
- **Sécurité physique et logique** : si on choisit on-premise, c'est aussi parce qu'on prend en charge la sécurité de bout en bout
- **Setup initial** : ≥ 50 K€ mentionné explicitement HTML pour qualifier le seuil minimal

> **Encart « scénario indicatif PME santé 50 salariés HDS A4 dominant » (extrapolation Cowork, non canonique HTML)** : ~150-400 K€/an selon ambition (amortissement hardware 30-100 K€/an + MLOps 0,5-1 ETP 30-80 K€/an + énergie 12-36 K€/an + sécurité physique + mises à jour modèles + DRP + maintenance). À ajuster selon volume et secteur réglementaire.

## Articulation cross-archis (frontières)

- **A4 vs A3** : la frontière est **cloud souverain EU managé** (A3) vs **infrastructure cliente** (A4 — datacenter interne, GPU on-prem, ou edge). Bascule A3 → A4 = passage de cloud externe à infrastructure interne, motivée par « aucune sortie de l'organisation tolérable » ou volume massif rentabilisant le hardware.
- **A4 vs A2** : A4 = full on-premise, équipe MLOps interne. A2 = cloud hyperscaler géré, équipe cloud existante. Différence opérationnelle qualitative.
- **A4 vs A1** : différence maximale sur tous les axes — opérationnel, souveraineté, complexité, coût.
- **A4 dans une stack Hybride** : fréquent pour les cas ultra-stratégiques uniquement, complété par A1/A3 pour les usages moins sensibles. Voir [[architecture-hybride]].

### 🔭 Variantes à surveiller

- **Edge AI** : déploiement sur appareils embarqués (NVIDIA Jetson, smartphones, IoT industriel) — sous-pattern A4 pour latence ultra-critique
- **Federated Learning** : pattern émergent permettant l'entraînement décentralisé sans centralisation des données — variante A4 pour cas multi-sites
- **LightOn Paradigm** comme référence enterprise full souveraine française

## Pour aller plus loin

- **Pattern grille de décision architecture** ([[pattern-grille-decision-architecture]]) : méthode 5 critères pour arbitrer A4 vs A3 (la frontière est subtile)
- **Pattern souveraineté EU** ([[pattern-souverainete-eu]]) : niveau Sovereign détaillé + SecNumCloud
- **Outils LLM** ([[outils-llm]]) : Lucie, Mistral, Mixtral, Llama, LightOn open-source/open-weight
- **RAG en production** ([[dep-02]]) : architecture RAG complète pour A4
- **Inférence et coûts SaaS vs self-hosted** ([[dep-06]]) : seuil de bascule économique vers A4
- **Sécurité IA cadrage stratégique** ([[pr-05]]) : A4 dans le cadre sécurité critique
- **Conformité RGPD/AI Act** ([[cu-020]]) : A4 pour cas haut risque AI Act + HDS + NIS2
- **Architecture A3** ([[architecture-a3-os-cloud-souverain]]) : alternative cloud souverain EU si A4 surdimensionnée
- **Architecture Hybride** ([[architecture-hybride]]) : A4 combiné à A1/A3 par cas d'usage
