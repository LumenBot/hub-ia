---
code: architecture-a3-os-cloud-souverain
titre: "Architecture A3 — Open-source sur cloud souverain EU"
type: architecture
axe: B
niveau: 3
tags: [architecture-ia, a3, open-weight, cloud-souverain-eu, mistral-cloud, lucie, pleias-rag, ovhcloud, scaleway, outscale, numspot, mistral-forge, hugging-face]
version: 3.12.0
last_updated: 2026-05-26
glosaire_termes: [llm, agent, rag, souverainete]
derives: ["[[pattern-grille-decision-architecture]]", "[[pattern-souverainete-eu]]", "[[outils-llm]]", "[[outils-vector-db]]", "[[dep-02]]", "[[dep-06]]", "[[pr-05]]", "[[cu-020]]", "[[architecture-a2-proprietaire-managee]]", "[[architecture-a4-os-on-premise]]", "[[architecture-hybride]]"]
public_cible: [dirigeant, ops, r&d]
---

# Architecture A3 — Open-source sur cloud souverain EU

## L'essentiel à retenir

**Architecture A3 open-source cloud souverain EU en PME 2026 : modèles à poids ouverts ([[outils-llm|Mistral]], [[outils-llm|Lucie]], [[outils-llm|Pleias-RAG|Pleias]], [[outils-llm|Llama]], [[outils-llm|Mixtral]]) hébergés sur des clouds européens souverains (OVHcloud, Scaleway, Outscale, Numspot). Pattern de référence pour les PME/ETI avec exigence souveraineté juridique forte + auditabilité du modèle. 80-90 % des cas PME/ETI sont éligibles à A3 selon le HTML canon Hub IA. Exemples canoniques : Mistral Cloud EU (Mistral Large 2, Codestral, Voxtral en région EU), Lucie/OpenLLM-France via OVHcloud-Scaleway-Outscale, Pleias-RAG pour juridique/compliance, Llama 3.x/Mixtral auto-hébergés OVHcloud-Scaleway, Mistral Forge fine-tuning souverain, Hugging Face Inference Endpoints région EU. API Mistral Cloud EU ~0,002-0,008 €/1k tokens, infrastructure GPU OVHcloud/Scaleway 80-300 €/mois TPE/PME, setup 5-20 K€. Souveraineté Strong (cloud souverain EU non soumis CLOUD Act + open-weight inspectable). Voir [[pattern-grille-decision-architecture]] pour positionnement vs A1/A2/A4/Hybride. Frontière A3/A4 = cloud souverain EU managé vs infrastructure cliente.**

**Avantage différenciant unique** : A3 offre la combinaison rare de la souveraineté EU juridique forte (cloud non soumis au CLOUD Act) ET de l'auditabilité du modèle (poids ouverts inspectables). Pour les organisations qui doivent à la fois respecter le RGPD strict et démontrer une maîtrise de leur stack IA, c'est le compromis le plus pragmatique en 2026.

## À qui s'adresse cette architecture

PME ou ETI avec :
- Exigence de souveraineté juridique forte (RGPD strict + données stratégiques)
- Volonté d'auditer le modèle utilisé (R&D protégée, PI, données clients premium)
- Capacité technique pour mobiliser un cloud souverain EU (équipe IT avec compétences cloud, 0,5-1 ETP MLOps disponible)
- Cible 80-90 % des cas PME/ETI selon HTML Hub IA

Niveau ⭐⭐⭐ Avancé. Public cible : DSI, RSSI, dirigeants tech avec sensibilité souveraineté.

## Description

**Modèle open-weight ou open-source hébergé sur cloud souverain EU** : le modèle (Mistral, Lucie, Pleias-RAG, Llama, Mixtral) tourne sur un cloud européen sous juridiction EU (OVHcloud français, Scaleway français, Outscale français, Numspot). Souveraineté juridique forte (non-CLOUD-Act) + auditabilité du modèle (poids ouverts inspectables).

## Méta

| Critère | Niveau |
|---|---|
| **Souveraineté** | 🟢 EU forte (Strong — voir [[pattern-souverainete-eu]]) |
| **Complexité** | 🛠️🛠️🛠️ Moyenne (cloud + déploiement + MLOps) |
| **Coût d'entrée** | 🟡 Moyen (5-20 K€ setup + infrastructure GPU) |
| **Time to value** | 🟡 Quelques semaines à quelques mois |

## Exemples typiques

Citations textuelles à transposer fidèlement :

- **Mistral Cloud EU** : Mistral Large 2, Codestral, Voxtral hébergés en région EU par Mistral AI directement
- **Lucie / OpenLLM-France** via OVHcloud, Scaleway ou Outscale
- **Pleias-RAG** hébergé sur infrastructure souveraine EU pour les usages juridique / compliance
- **Llama 3.x / Mixtral auto-hébergés** sur OVHcloud / Scaleway avec instances GPU
- **Mistral Forge** pour fine-tuning souverain sur dataset propriétaire
- **Hugging Face Inference Endpoints** en région EU pour des modèles open-weight précis

**À noter** : Mistral Cloud EU est classé A3 (et pas A1) car il offre une **garantie souveraineté contractuelle EU** sur les modèles open-weight Mistral, là où Le Chat Mistral grand public est en A1 (cloud public sans contrôle data residency contractuel équivalent).

## ✅ Quand l'utiliser

- **Souveraineté juridique requise** : RGPD strict + CLOUD Act inacceptable → A3 est la réponse principale 2026
- **Auditabilité du modèle nécessaire** : R&D, compliance, secteurs où la traçabilité du modèle est requise (juridique, médical en partie)
- **Qualité open-source mature suffisante** : pour 80-90 % des cas PME/ETI selon HTML, les modèles open-weight matures (Mistral Large 2, Mixtral, Llama 3.x) couvrent les besoins
- **Équipe technique mobilisable** : 0,5-1 ETP MLOps disponible + compétences cloud existantes
- **Cas d'usage haut risque AI Act** : RH, santé, finance — la conformité est mieux documentable avec un modèle open-weight + cloud souverain
- **Volumes significatifs avec contrôle des coûts** : l'auto-hébergement GPU permet d'amortir mieux que le SaaS au-delà de certains volumes

## ❌ Quand l'éviter

- **Démarrage ultra-rapide POC** : le setup cloud + déploiement open-weight prend plusieurs semaines → préférer A1 pour validation rapide, basculer A3 ensuite
- **Pas d'équipe technique MLOps** : opérer un modèle open-weight sur cloud requiert des compétences MLOps minimales (0,5 ETP) → préférer A2 (cloud hyperscaler géré)
- **Cas d'usage qui exige absolument la qualité top-tier des modèles propriétaires** : si [[outils-llm|Claude]] Opus / GPT-5 sont strictement supérieurs sur le cas (~10-20 % de cas en 2026), A1 ou A2 restent préférables
- **Données ultra-stratégiques avec aucune sortie de l'organisation tolérable** : santé HDS, défense, R&D classifiée → A4 obligatoire
- **TPE sans budget infrastructure** : 5-20 K€ setup peut être un seuil

## ⚠️ Risques / Subtilité souveraineté / Avantage différenciant

### ⚠️ Risques

- **Qualité variable selon modèle open-weight** : Mistral Large 2 et Mixtral sont matures, mais d'autres open-weight peuvent être en deçà sur des tâches complexes → tester sur le cas d'usage réel
- **Mises à jour modèles** : un nouveau modèle open-source majeur sort tous les 3-6 mois → discipline de re-bench + ré-évaluation qualité régulière
- **Dépendance cloud souverain** : si OVHcloud / Scaleway changent leurs offres ou tarifs, migration nécessaire (moins critique que CLOUD Act, mais non nul)
- **Complexité observabilité** : monitoring d'un modèle auto-hébergé est plus complexe qu'un SaaS (voir [[outils-observabilite-llm]] avec Langfuse self-host EU)

### 💡 Avantage différenciant

A3 offre la **combinaison rare** de la souveraineté EU juridique forte (cloud non soumis au CLOUD Act) **ET** de l'auditabilité du modèle (poids ouverts inspectables). Pour les organisations qui doivent à la fois respecter le RGPD strict et démontrer une maîtrise de leur stack IA, c'est le compromis le plus pragmatique en 2026.

## Coût indicatif

Coûts canoniques HTML à citer textuellement (R10 stricte) :

- **API Mistral Cloud EU** : ~0,002 à 0,008 € / 1k tokens (compétitif avec OpenAI)
- **Infrastructure GPU sur OVHcloud / Scaleway** pour auto-hébergement open-weight : ~80-300 €/mois pour un déploiement TPE/PME (modèle moyen, charge modeste)
- **Coût initial setup** : 5-20 K€ selon ambition (PoC vs déploiement industriel)
- **Hugging Face Inference Endpoints EU** : tarification à l'heure GPU + bande passante

> **Encart « scénario indicatif PME 50 salariés A3 dominant » (extrapolation Cowork, non canonique HTML)** : ~60-120 K€/an selon usage (API Mistral Cloud EU + infrastructure GPU OVHcloud Scaleway pour cas avancés + 0,5-1 ETP MLOps interne ou externalisé 40-80 K€/an + observabilité Langfuse self-host EU + setup amorti). À ajuster selon volume et ambition.

## Articulation cross-archis (frontières)

- **A3 vs A2** : double frontière — modèle (open-weight A3 vs propriétaire A2) ET cloud (cloud souverain EU non-CLOUD-Act A3 vs hyperscaler CLOUD Act A2). Différence souveraineté juridique majeure.
- **A3 vs A1** : A3 = cloud souverain EU + open-weight. A1 = cloud public direct + propriétaire. Différence complète sur les 2 axes.
- **A3 vs A4** : la frontière est **cloud souverain EU managé** (A3) vs **infrastructure cliente** (A4 — datacenter interne, GPU on-prem, ou edge). Bascule A3 → A4 = passage de cloud externe à infrastructure interne, généralement motivé par exigence « aucune donnée ne sort de l'organisation tolérable » (défense, santé HDS, OIV/OSE).
- **A3 dans une stack Hybride** : très fréquent — A3 utilisé pour les cas d'usage standards et stratégiques EU, complété par A1 pour les usages individuels et par A4 pour les cas ultra-stratégiques. Voir [[architecture-hybride]].

**Pattern « POC A1 → production A3 »** : très fréquent. POC rapide en A1 pour valider la valeur métier, puis bascule A3 pour industrialiser avec souveraineté. À condition de l'avoir planifié dès le départ.

### 🔭 Variantes à surveiller

- **Hugging Face Inference Endpoints région EU** : alternative souple pour déployer des modèles open-weight spécifiques sans gérer l'infrastructure cloud
- **BYOM (Bring Your Own Model)** : mode émergent où le modèle fine-tuné est déployé sur cloud souverain mais conserve une licence Mistral/OpenAI sous-jacente
- **Coopératives EU** (Petals, EuroLLM) : déploiement décentralisé émergent

## Pour aller plus loin

- **Pattern grille de décision architecture** ([[pattern-grille-decision-architecture]]) : méthode 5 critères pour arbitrer A3 vs A1/A2/A4
- **Pattern souveraineté EU** ([[pattern-souverainete-eu]]) : niveau Strong détaillé
- **Outils LLM** ([[outils-llm]]) : Mistral, Lucie, Pleias-RAG, Llama, Mixtral avec tarifs
- **Vector stores** ([[outils-vector-db]]) : Qdrant self-hostable EU pour la stack RAG A3
- **RAG en production** ([[dep-02]]) : architecture RAG complète pour A3
- **Inférence et coûts SaaS vs self-hosted** ([[dep-06]]) : arbitrage économique sur volumes
- **Sécurité IA cadrage stratégique** ([[pr-05]]) : A3 dans le cadre sécurité PME
- **Conformité RGPD/AI Act** ([[cu-020]]) : conformité facilitée par A3
- **Architecture A2** ([[architecture-a2-proprietaire-managee]]) : alternative cloud hyperscaler
- **Architecture A4** ([[architecture-a4-os-on-premise]]) : bascule si aucune sortie organisation tolérable
- **Architecture Hybride** ([[architecture-hybride]]) : A3 combiné à A1/A2/A4 par cas d'usage
