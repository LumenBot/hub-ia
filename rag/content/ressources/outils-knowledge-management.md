---
code: outils-knowledge-management
titre: "Outils — Knowledge management augmenté par IA"
type: fiche-outil
axe: transverse
niveau: 3
tags: [knowledge-management, km, obsidian, readwise, airr, gbrain, supersplat, capitalisation-connaissances, notes-personnelles]
version: 3.12.0
last_updated: 2026-05-25
glosaire_termes: [llm, rag, agent, embeddings]
derives: ["[[cu-001]]", "[[cu-008]]", "[[cu-025]]", "[[dep-02]]", "[[outils-llm]]", "[[outils-workflow-automation]]", "[[pattern-souverainete-eu]]"]
public_cible: [dirigeant, ops, r&d]
---

# Outils — Knowledge management augmenté par IA

## Quand utiliser un outil de knowledge management IA

Un outil de **knowledge management (KM) augmenté par IA** permet de capitaliser les connaissances (notes personnelles, articles lus, documents reçus, comptes-rendus de réunion) et de les **rendre interrogeables intelligemment** via un LLM. C'est l'équivalent personnel ou en équipe d'un [[cu-008]] (Knowledge base RAG), mais focalisé sur la production individuelle quotidienne du knowledge worker.

5 outils de référence marché 2026 pour le KM individuel ou en petite équipe : **Obsidian** (wiki local-first), **Readwise** (agrégation highlights + IA), **Airr** (alternative Readwise plus récente), **GBrain** (KM entreprise), **SuperSplat** (KM visuel/cartographique).

À mentionner avec wikilink (catégorisés ailleurs HTML) : **NotebookLM** est rangé [[outils-llm]] (RAG conversationnel Google) — l'utiliser comme **dialogue sur sources uploadées** plutôt que comme système KM persistant. **Beever Atlas** est rangé [[outils-workflow-automation]] (orchestration souveraine FR).

## Obsidian — référence wiki local-first

Obsidian est le **wiki personnel local-first** de référence marché 2026 (~2M utilisateurs actifs). Combo : stockage en fichiers Markdown locaux (souveraineté maximale, pas de cloud par défaut) + écosystème de plugins riche + graphe de liens entre notes + workflows complexes via templates.

Pour le KM IA-augmenté : nombreux plugins community (Copilot for Obsidian, Smart Connections, Khoj) qui ajoutent du RAG, des suggestions IA, ou un chat sur ses propres notes.

**Quand l'utiliser** : KM personnel ou équipe restreinte (1-5 personnes), souveraineté maximale exigée (local-first), workflow notes en Markdown (compatible Git, exportable), expérimentation plugins IA tiers.

**Quand ne pas l'utiliser** : KM entreprise multi-utilisateurs collaboratif temps réel (préférer GBrain ou Notion), équipe non-tech sans appétence pour la prise en main wiki.

**Modèle économique** : **gratuit (usage personnel)** · **Sync 10 $/mois** (synchronisation E2E entre devices) · **Publish 16 $/mois** (publication web) · **Catalyst 25-50 $ one-shot** (early access + badge). Souveraineté niveau **Sovereign** (local-first, hébergement utilisateur, pas de cloud requis).

**Cas d'usage Hub** : [[cu-025]] (Knowledge management dirigeant), [[cu-001]] (Sources fiables — capitalisation veille), workflow personnel quotidien knowledge worker.

**Lien** : obsidian.md

## Readwise — agrégation highlights + IA

Readwise est l'**agrégateur de highlights** marché 2026 : il rassemble automatiquement les highlights de tes lectures (Kindle, Pocket, Instapaper, Twitter, articles web, podcasts via transcription) dans une bibliothèque centrale + Daily Review (révision quotidienne par spaced repetition).

Pour le KM IA-augmenté : feature **Reader IA** qui suggère des notes connexes, génère des résumés, permet de dialoguer avec la bibliothèque.

**Quand l'utiliser** : capitalisation des lectures sans effort manuel, révision quotidienne par spaced repetition, intégration avec Obsidian/Notion via export, équipe partage de highlights.

**Quand ne pas l'utiliser** : KM avec stockage souverain strict (Readwise est cloud US), workflow notes complexes (Obsidian plus puissant), équipe non-lectrice intensive (l'outil prend tout son sens avec >5 lectures/semaine).

**Modèle économique** : Free tier limité (3 sources max) · **Readwise Pro 7,99 $/mois** ou **79,99 $/an** · Readwise Reader inclus dans Pro depuis 2024. Souveraineté niveau **Light** (US cloud).

**Cas d'usage Hub** : [[cu-001]] (Sources fiables — capitalisation veille systématique), [[cu-025]] (Knowledge management dirigeant — lectures hiérarchisées).

**Lien** : readwise.io

## Airr — alternative Readwise plus récente

Airr est l'**alternative Readwise plus récente et plus orientée IA native**. Combo : agrégation highlights + chat avec sa bibliothèque + génération de notes structurées + intégration calendrier (mise en avant des highlights en fonction du contexte du jour).

**Quand l'utiliser** : alternative à Readwise pour les early adopters, focus IA native (chat sur bibliothèque), intégration contextuelle calendrier.

**Quand ne pas l'utiliser** : exigence outil mature (Readwise plus établi), intégration avec Kindle/Pocket très ancienne (Readwise plus complet sur les sources legacy), souveraineté EU (Airr cloud US).

**Modèle économique** : Free tier limité · **Pro ~5-10 $/mois** (tarification à vérifier 2026, alternative aggressive). Souveraineté niveau **Light** (US).

**Cas d'usage Hub** : [[cu-001]] (Sources fiables — alternative IA-native), [[cu-025]] (Knowledge management dirigeant).

**Lien** : airr.app

## GBrain — KM entreprise

GBrain est la **plateforme KM entreprise** orientée capitalisation des connaissances métier. Combo : ingestion massive (docs, intranet, Slack, emails, Drive) + RAG conversationnel + recherche cross-sources + collaboratif équipe + permissions fines.

**Quand l'utiliser** : KM entreprise multi-utilisateurs (>10 personnes), capitalisation cross-sources (docs + Slack + emails + Drive), équipe de support ou vente avec besoin de réponses sourcées.

**Quand ne pas l'utiliser** : KM personnel (overkill, préférer Obsidian), budget restreint (GBrain enterprise plutôt qu'individuel), souveraineté EU stricte (vérifier hébergement contractualisé).

**Modèle économique** : **Tarification enterprise sur devis** (cible PME 50+ salariés et ETI). Souveraineté niveau **Light à Moderate** selon configuration contractuelle (vérifier hébergement EU si critique).

**Cas d'usage Hub** : [[cu-008]] (Knowledge base RAG entreprise, alternative SaaS), [[cu-025]] (Knowledge management dirigeant équipe étendue).

**Lien** : gbrain.com

## SuperSplat — KM visuel/cartographique

SuperSplat est un **outil KM visuel** qui structure les connaissances sous forme de cartes interactives 2D/3D (mind maps avancées, knowledge graphs visualisables). Combo : import depuis sources variées + visualisation graphique + interaction tactile/souris + export vers formats standards.

**Quand l'utiliser** : KM visuel-spatial (apprentissage cartographique, dirigeants visuels), présentation de connaissances complexes à des stakeholders non-techniques, brainstorming structurés.

**Quand ne pas l'utiliser** : KM textuel quotidien (préférer Obsidian ou Notion), équipe sans besoin de représentation visuelle structurée.

**Modèle économique** : Free tier limité · **Pro ~10-20 $/mois** (tarification à vérifier 2026). Souveraineté niveau **Light** (cloud).

**Cas d'usage Hub** : [[cu-025]] (Knowledge management dirigeant — alternative visuelle), présentation et facilitation d'ateliers stratégiques.

**Lien** : supersplat.com

## Outils satellites à mentionner

Pour les cas d'usage adjacents au KM, voir leur fiche principale :

- **NotebookLM** ([[outils-llm]]) — RAG conversationnel sur sources uploadées (Google). Idéal pour le **dialogue** sur petits corpus de référence (<100 sources), pas un système KM persistant.
- **Beever Atlas** ([[outils-workflow-automation]]) — KM souverain FR + orchestration. Catégorisé orchestration HTML car positionnement principal = workflows automation.

## Comparatif synthétique

| Outil | Type | Souveraineté | Tarif | Cas Hub principal |
|---|---|---|---|---|
| **Obsidian** | Wiki local-first | Sovereign | Gratuit / 10-16 $/mois | KM personnel ou petite équipe |
| **Readwise** | Agrégation highlights + IA | Light (US) | 7,99 $/mois | Capitalisation lectures systématique |
| **Airr** | Alternative IA-native Readwise | Light (US) | ~5-10 $/mois | Capitalisation IA-first |
| **GBrain** | KM entreprise | Light à Moderate | Enterprise sur devis | KM multi-utilisateurs entreprise |
| **SuperSplat** | KM visuel/cartographique | Light | ~10-20 $/mois | KM visuel-spatial dirigeant |

## Recommandations PME par profil

**Dirigeant solo PME 5-15 salariés** : Obsidian (gratuit) + Readwise Pro (7,99 $/mois) + claude.ai Pro (20 $/mois pour dialogue sur notes). Total ~28 $/mois. Niveau Sovereign + Light.

**Équipe PME 15-50 salariés avec besoin de KM partagé** : Obsidian + Readwise + GBrain ou alternative équivalente. Budget 50-200 $/mois selon taille équipe. Niveau Moderate.

**PME 50+ avec sensibilité souveraineté** : Obsidian + Beever Atlas (voir [[outils-workflow-automation]]) + Pleias-RAG pour RAG souverain (voir [[outils-llm]]). Niveau Strong.

**Dirigeant visuel/cartographique** : Obsidian (base notes) + SuperSplat (présentations stratégiques) + NotebookLM (RAG ponctuel sur dossiers thématiques). Budget ~30-50 $/mois.

## Pour aller plus loin

- **Knowledge base RAG cas-école** ([[cu-008]]) : architecture RAG en PME
- **Knowledge management dirigeant** ([[cu-025]]) : cas d'usage stratégique knowledge management
- **Sources fiables IA** ([[cu-001]]) : capitalisation veille avec sources vérifiées
- **Modèles LLM** ([[outils-llm]]) : choix du LLM pour le dialogue sur knowledge base
- **Vector stores** ([[outils-vector-db]]) : brique technique pour RAG sur knowledge base
- **Pattern souveraineté EU** ([[pattern-souverainete-eu]]) : qualification souveraineté par outil
