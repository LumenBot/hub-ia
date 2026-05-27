---
code: architecture-a1-saas-proprietaire
titre: "Architecture A1 — SaaS propriétaire (cloud public direct)"
type: architecture
axe: B
niveau: 3
tags: [architecture-ia, a1, saas, cloud-public, claude, gpt, gemini, le-chat-mistral, notion-ai, slack-ai, m365-copilot]
version: 3.12.0
last_updated: 2026-05-26
glosaire_termes: [llm, agent, rag, souverainete]
derives: ["[[pattern-grille-decision-architecture]]", "[[pattern-souverainete-eu]]", "[[outils-llm]]", "[[cu-001]]", "[[cu-020]]", "[[pr-08]]", "[[pr-09]]", "[[dep-06]]", "[[architecture-a2-proprietaire-managee]]", "[[architecture-hybride]]"]
public_cible: [dirigeant, ops, r&d]
---

# Architecture A1 — SaaS propriétaire (cloud public direct)

## L'essentiel à retenir

**Architecture A1 SaaS propriétaire en PME 2026 : accès direct au modèle IA via l'API ou l'interface du fournisseur, hébergé sur son cloud public mondial. Pattern le plus simple, plus rapide à mettre en place, idéal pour démarrer ou pour des usages individuels. Exemples canoniques : ChatGPT, [[outils-llm|Claude]], Gemini, Le Chat [[outils-llm|Mistral]] (cas particulier : modèle propriétaire mais éditeur EU), Notion AI, Slack AI, Microsoft 365 Copilot. Plan grand public 0 à 30 €/mois/utilisateur, API usage ~0,01-0,10 € par 1k tokens, plans Enterprise 25-60 €/mois/utilisateur. Souveraineté Light (cloud public mondial, exposé au CLOUD Act pour les éditeurs US). Voir [[pattern-grille-decision-architecture]] pour le positionnement vs A2/A3/A4/Hybride. Frontière A1/A2 = cloud public direct vs cloud client avec data residency.**

**Cas particulier important** : Le Chat Mistral est classé A1 même si l'éditeur est EU — le critère structurant n'est pas l'origine de l'éditeur mais l'**accès direct via le cloud public du fournisseur**. La souveraineté n'est pas une propriété de l'éditeur, c'est une propriété du **mode d'hébergement et de contrôle des données**.

## À qui s'adresse cette architecture

PME ou ETI qui démarre l'IA et veut un time-to-value minimal (quelques jours) pour des usages individuels (recherche augmentée, rédaction, idéation, prototypage), sans contraintes réglementaires ou de souveraineté fortes sur les données traitées. Cible naturelle aussi pour les POC et les premiers prototypes avant industrialisation.

Niveau ⭐⭐ Intermédiaire. Public cible : dirigeants, équipes métier, knowledge workers.

## Description

**SaaS propriétaire en mode cloud public direct** : modèle IA propriétaire (Claude, [[outils-llm|GPT]], Gemini, Le Chat Mistral, etc.) consommé via l'API du fournisseur ou son interface web/desktop, sans passer par un cloud intermédiaire client. C'est le mode « plug-and-play » du marché 2026.

## Méta

| Critère | Niveau |
|---|---|
| **Souveraineté** | 🔴 Faible (Light — voir [[pattern-souverainete-eu]]) |
| **Complexité** | 🛠️ Très légère (compte fournisseur + carte bancaire) |
| **Coût d'entrée** | 🟢 Faible (0 à 30 €/mois utilisateur en grand public) |
| **Time to value** | 🟢 Quelques jours |

## Exemples typiques

Citations textuelles à transposer fidèlement :

- **ChatGPT via API OpenAI ou interface chat.openai.com**
- **Claude via API Anthropic ou claude.ai**
- **Gemini via API Google AI Studio ou gemini.google.com**
- **Le Chat de Mistral via le Mistral cloud EU** (cas particulier : modèle propriétaire mais éditeur EU — cf. note ci-dessous)
- **Outils SaaS productivité avec IA intégrée** : Notion AI, Slack AI, Microsoft 365 Copilot grand public

**À noter sur Le Chat Mistral** : classé A1 car accès direct via Mistral cloud public EU. La frontière A1/A2 n'est pas l'origine de l'éditeur (US vs EU) mais le mode d'accès (cloud public direct vs cloud client avec data residency contrôlée). Voir bloc « Articulation cross-archis » ci-dessous.

## ✅ Quand l'utiliser

- **Démarrage rapide** : besoin d'un POC ou d'un prototype en quelques jours
- **Usages individuels** : recherche augmentée, brainstorming, idéation, rédaction de contenu marketing public, traduction
- **Données peu sensibles** : contenu public, brouillons, idéation sans données stratégiques
- **Équipe sans compétence DevOps/MLOps** : pas d'infrastructure à opérer, juste un compte + abonnement
- **Budget restreint** : 0 à 30 €/mois utilisateur en grand public, scaling progressif possible

## ❌ Quand l'éviter

- **Données stratégiques ou sensibles** : R&D, fichiers clients premium, PI, secrets commerciaux → privilégier A3 ou A4
- **Cas d'usage haut risque AI Act** : RH, santé, finance, sécurité publique → A2 minimum, idéalement A3
- **Souveraineté juridique requise** : RGPD strict + CLOUD Act inacceptable → A3 ou A4
- **Volumes très importants** : au-delà de quelques millions de tokens/mois, le coût SaaS dépasse rapidement le self-host → A3/A4 économiquement préférables
- **Production critique avec SLA serré** : SLA SaaS standard = 99,9 %, pas suffisant pour certaines applications stratégiques

## ⚠️ Risques / Subtilité souveraineté / Avantage différenciant

### ⚠️ Risques

- **CLOUD Act** : les fournisseurs US (OpenAI, Anthropic, Google) sont juridiquement soumis au CLOUD Act qui peut contraindre la divulgation de données à des autorités US, même si les données sont stockées en EU. Voir [[pattern-souverainete-eu]] niveau Light.
- **Politique no-training à vérifier** : les plans grand public sont parfois utilisés pour entraîner les modèles par défaut. Lire les conditions ou choisir un plan Enterprise avec engagement no-training explicite.
- **Verrouillage fournisseur** : changer de modèle (Claude → GPT par exemple) nécessite ré-évaluation des prompts et tests qualité. Souvent moins simple qu'attendu.
- **Pannes du fournisseur** = arrêt complet du service. Pas de plan B opérationnel sans re-développement.

### 💡 Avantage différenciant

A1 est la **seule architecture** qui combine **time-to-value minimal** (quelques jours), **coût d'entrée quasi-nul** (gratuit ou 20 €/mois) et **qualité top-tier** (les modèles propriétaires restent au-dessus des open-weight sur de nombreux benchmarks complexes). Pour démarrer l'IA en PME, c'est la voie d'entrée la plus naturelle — à condition d'être conscient des limites en souveraineté et confidentialité.

## Coût indicatif

Coûts canoniques HTML à citer textuellement (R10 stricte) :

- **Plan grand public** : 0 à 30 €/mois/utilisateur (Claude Pro 18 €, ChatGPT Plus 20 €)
- **API usage** : ~0,01 à 0,10 € pour 1k tokens selon modèle. Coût mensuel typique PME : 50 à 500 € selon volume.
- **Plans Enterprise** : 25-60 €/mois/utilisateur pour des garanties contractuelles renforcées (no-training, audit, SLA).

> **Encart « scénario indicatif PME 50 salariés tous outils A1 confondus » (extrapolation Cowork, non canonique HTML)** : ~12-36 K€/an selon usage (50 utilisateurs × Claude Pro 18 €/mois ≈ 10,8 K€/an + usage API léger ~3 K€/an + 2-3 SaaS productivité IA intégrée 5-15 K€/an). À ajuster selon volume et profil d'usage.

## Articulation cross-archis (frontières)

- **A1 vs A2** : la frontière n'est pas l'origine de l'éditeur (US vs EU) mais le **mode d'accès**. A1 = cloud public direct du fournisseur. A2 = cloud client (AWS, Azure, GCP) avec data residency contrôlée. Le Chat Mistral = A1 (cloud public Mistral, même EU). Claude on AWS Bedrock région Francfort = A2 (cloud client AWS sous contrôle).
- **A1 vs A3** : A1 = modèle propriétaire + cloud public. A3 = modèle open-weight + cloud souverain EU. Auditabilité du modèle absente A1 vs présente A3.
- **A1 vs A4** : A4 = full on-premise infrastructure cliente. A1 = aucune infrastructure à opérer. Différence opérationnelle maximale.
- **A1 dans une stack Hybride** : très fréquent — A1 utilisé pour les usages individuels (recherche, rédaction grand public) en complément d'une A3 ou A4 pour les usages stratégiques. Voir [[architecture-hybride]].

**Bascule fréquente** : le pattern « POC A1 puis production A3 » est légitime quand il est planifié dès le départ. Voir [[pattern-grille-decision-architecture]] §quand-passer-hybride.

### 🔭 Variantes à surveiller

- **Plans Enterprise** avec engagement contractuel no-training + data residency EU (rapproche de A2 selon le contractualisation)
- **Brokers EU souverains** émergents qui se positionnent comme intermédiaires SaaS avec souveraineté contractualisée

## Pour aller plus loin

- **Pattern grille de décision architecture** ([[pattern-grille-decision-architecture]]) : méthode 5 critères pour arbitrer A1 vs autres
- **Pattern souveraineté EU** ([[pattern-souverainete-eu]]) : niveau Light détaillé, ce qu'il implique
- **Outils LLM** ([[outils-llm]]) : Claude, GPT, Gemini, Le Chat Mistral, etc. avec tarifs canoniques
- **Sources fiables IA** ([[cu-001]]) : cas d'usage type A1 (recherche augmentée avec vérification)
- **Conformité RGPD/AI Act** ([[cu-020]]) : pourquoi A1 est limité pour les cas haut risque
- **Cadrer un projet IA** ([[pr-09]]) : si le critère 1 sensibilité données est faible, A1 peut convenir
- **Inférence et coûts SaaS vs self-hosted** ([[dep-06]]) : arbitrage économique A1 vs A3/A4 sur volumes
- **Architecture A2** ([[architecture-a2-proprietaire-managee]]) : bascule naturelle quand contraintes data residency apparaissent
- **Architecture Hybride** ([[architecture-hybride]]) : A1 combiné à d'autres patterns par cas d'usage
