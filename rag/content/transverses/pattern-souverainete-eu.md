---
code: pattern-souverainete-eu
titre: "Pattern — Souveraineté EU des outils IA"
type: transverse
axe: transverse
niveau: 3
tags: [souverainete, eu, rgpd, ai-act, hebergement-eu, open-weight, secnumcloud, pattern-architectural]
version: 3.12.0
last_updated: 2026-05-25
glosaire_termes: [souverainete, llm, agent, rag]
derives: ["[[outils-llm]]", "[[outils-frameworks-rag]]", "[[outils-knowledge-management]]", "[[outils-observabilite-llm]]", "[[outils-workflow-automation]]", "[[outils-vector-db]]", "[[pr-05]]", "[[cu-020]]", "[[dep-02]]", "[[dep-06]]"]
public_cible: [dirigeant, ops, r&d]
---

# Pattern — Souveraineté EU des outils IA

> Brique transverse référencée par les fiches outils du Hub IA quand un outil offre des garanties de souveraineté EU. Critères de qualification + 4 niveaux de souveraineté + acteurs de référence par catégorie. Cohérence avec [[pr-05]] (Sécurité IA) et [[cu-020]] (Conformité RGPD/AI Act).

## Pourquoi la souveraineté IA matters pour une PME EU en 2026

Pour une PME basée en UE qui pilote un usage IA, la **souveraineté** est l'une des 4 dimensions structurantes du choix d'outils (les 3 autres : fonctionnalités, coût, conformité réglementaire). Les enjeux sont triples :

- **Réglementaire** : AI Act, RGPD, NIS2 imposent des exigences de localisation, de transparence, de garde-fous qui ne sont pas systématiquement honorées par les acteurs US ou CN.
- **Stratégique** : dépendance à un fournisseur extra-européen = risque géopolitique (sanctions, restrictions export, changements de conditions d'usage) qui peut figer un projet en cours.
- **Cyber-sécurité** : un acteur EU avec hébergement EU réduit la surface d'attaque transfrontière + facilite la conformité documentée.

**Définition opérationnelle** : un outil IA est dit « souverain EU » s'il combine au moins **2 des 4 critères** ci-dessous, et qu'il offre une trajectoire crédible d'amélioration sur les autres.

## Les 4 critères de qualification de la souveraineté

### Critère 1 — Hébergement EU contrôlé

L'outil tourne sur des infrastructures localisées en UE (datacenters EU, fournisseurs cloud EU type OVHcloud, Scaleway, Outscale, ou self-hosted on-premise EU). Pas d'export de données hors UE même de manière transitoire.

Cas idéal : certification SecNumCloud (qualification ANSSI) ou équivalent national. Cas acceptable : hébergement EU contractualisé par l'éditeur (cloud act non applicable, GDPR pleinement opposable).

### Critère 2 — Licence open-weight ou open-source

L'outil est disponible en licence permissive (Apache 2.0, MIT, BSD) ou en licence open-weight (poids du modèle distribués, code d'inférence open-source). L'utilisateur peut self-héberger sans dépendre du fournisseur, auditer le code, forker en cas de fork stratégique.

Cas idéal : licence Apache 2.0 + repository GitHub actif. Cas acceptable : licence open-weight ([[outils-llm|Llama]] Community License, [[outils-llm|Mistral]] Research License) avec restrictions commerciales raisonnables.

### Critère 3 — Origine éditeur EU

L'éditeur de l'outil est une entreprise dont le siège social, l'équipe de direction et la majorité des collaborateurs sont basés en UE. Garantit l'application du droit EU au capital et à la gouvernance de l'éditeur, et limite le risque d'acquisition / pivot par un acteur non-EU.

Cas idéal : éditeur français ou EU avec capitalisation EU (BPI France, fonds EU). Cas acceptable : filiale EU d'un acteur global avec autonomie opérationnelle effective.

### Critère 4 — Mode d'inférence vérifiable

L'utilisateur peut auditer où et comment ses données sont traitées (logs, traces, attestations). En cas d'inférence cloud, l'éditeur fournit des attestations conformes (rapports SOC 2, certifications ISO 27001 + ISO 27018, transparence des sous-traitants).

Cas idéal : inférence on-premise full + audit logs locaux. Cas acceptable : inférence cloud EU certifiée avec attestations annuelles indépendantes.

## Les 4 niveaux de souveraineté

Échelle à utiliser pour qualifier un outil et arbitrer son usage en PME selon le niveau de sensibilité des données traitées.

### Niveau 1 — Light (souveraineté minimale)

L'outil **satisfait 1 critère sur 4**, typiquement l'hébergement EU optionnel (mais hors UE par défaut). Usage acceptable pour des données peu sensibles, des POC, du prototypage. À éviter pour la production avec données métier critiques.

**Exemples** : la plupart des SaaS US avec option « EU region » (ChatGPT, [[outils-llm|GPT]] API en région EU sans Cloud Act protection effective, certains outils [[outils-llm|Claude]] Code en région UE).

### Niveau 2 — Moderate (souveraineté partielle)

L'outil **satisfait 2 critères sur 4**, typiquement hébergement EU contractualisé + licence open-weight. Adapté à la production en PME pour des cas d'usage standards (productivité, KM, génération texte).

**Exemples** : Mistral Le Chat (hébergé EU + Mistral Large open-weight optionnel), Le Chat Pro avec garanties contractuelles EU.

### Niveau 3 — Strong (souveraineté avancée)

L'outil **satisfait 3 critères sur 4**, typiquement hébergement EU + open-weight + éditeur EU. Recommandé pour les cas d'usage sensibles (données clients, R&D, propriété intellectuelle, conformité réglementaire stricte).

**Exemples** : [[outils-llm|Pleias-RAG]] (open-weight + éditeur FR + hébergement EU possible), [[outils-llm|Lucie]] (souverain FR open-weight), [[outils-observabilite-llm|Langfuse]] (open-source + éditeur DE + self-hosting EU).

### Niveau 4 — Sovereign Cloud SecNumCloud (souveraineté maximale)

L'outil **satisfait les 4 critères**, certification SecNumCloud (ANSSI) ou équivalent national. Niveau requis pour les opérateurs d'importance vitale (OIV), opérateurs de services essentiels (OSE) au sens de NIS2, données de santé (HDS), données classifiées.

**Exemples** : [[outils-llm|LightOn]] enterprise (éditeur FR, hébergement on-premise ou SecNumCloud, licence enterprise), certaines installations Mistral on-premise avec contractualisation SecNumCloud, déploiements Outscale + Mistral.

## Acteurs de référence par catégorie

### Modèles LLM souverains EU

- **Mistral** (FR) — Mistral Large 2, [[outils-llm|Mixtral]], Le Chat. Niveau Moderate à Strong selon configuration. Voir [[outils-llm]].
- **Lucie** (FR) — Modèle open-weight souverain France. Niveau Strong. Voir [[outils-llm]].
- **Pleias-RAG** (FR) — Spécialisé RAG juridique/réglementaire. Niveau Strong. Voir [[outils-llm]].
- **LightOn** (FR) — Solution enterprise full souveraine. Niveau Sovereign. Voir [[outils-llm]].

### Frameworks et orchestration souverains

- **[[outils-workflow-automation|n8n]]** (DE, open-source) — workflow automation auto-hébergeable. Niveau Strong. Voir [[outils-workflow-automation]].
- **Composio** (open-source) — outils agents auto-hébergeables. Niveau Moderate à Strong. Voir [[outils-workflow-automation]].

### Knowledge management & RAG souverains

- **Beever Atlas** (FR) — knowledge management souverain. Niveau Strong. Voir [[outils-workflow-automation]].
- **[[outils-vector-db|Qdrant]]** (DE, open-source) — vector store self-hostable EU. Niveau Strong. Voir [[outils-vector-db]].
- **pgvector** (open-source, PostgreSQL) — extension auto-hébergeable. Niveau Strong selon hébergement. Voir [[outils-vector-db]].

### Observabilité LLM souveraine

- **Langfuse** (DE, open-source) — observabilité LLM self-hostable. Niveau Strong. Voir [[outils-observabilite-llm]].

## Cohérence avec le cadre réglementaire 2026

La souveraineté EU n'est pas seulement un choix éditorial — elle s'inscrit dans un cadre réglementaire structurant :

- **AI Act Art. 50** (transparence GenAI) : les fournisseurs de modèles à usage général doivent publier des informations détaillées sur leurs données d'entraînement et leurs procédures de mitigation des risques. Les acteurs EU sont structurellement mieux alignés sur ces exigences.
- **RGPD** : un éditeur EU avec hébergement EU élimine la complexité du transfert de données hors UE (SCC, BCR, dérogations). Voir [[cu-020]].
- **NIS2** : pour les OIV/OSE, la souveraineté est une exigence opérationnelle, pas seulement réputationnelle.
- **AI Continent Action Plan** (avril 2026) : 5 fronts dont la souveraineté technologique européenne, soutien explicite aux acteurs EU dans les marchés publics et les programmes d'innovation.

## Quand prioriser la souveraineté en PME

### Cas où la souveraineté est critique

- Données personnelles sensibles (santé, biométrie, données mineurs)
- Données stratégiques de l'entreprise (R&D, propriété intellectuelle, fichiers clients premium)
- Conformité réglementaire imposée (santé HDS, défense, services publics)
- Risque géopolitique élevé (dépendance critique à un fournisseur extra-EU)

→ Cible niveau **Strong à Sovereign**, hébergement EU contractualisé minimum.

### Cas où la souveraineté est souhaitable mais arbitrable

- Productivité bureautique générique (génération texte, synthèse)
- Knowledge management interne
- Prototypage et POC

→ Cible niveau **Moderate**, arbitrage acceptable avec acteurs US si fonctionnalités décisives.

### Cas où la souveraineté est secondaire

- Recherche personnelle, exploration, apprentissage
- Cas d'usage non-critiques sans données sensibles

→ Niveau **Light** acceptable, choix par fonctionnalité ou prix.

## Anti-patterns à éviter

- **Souveraineté décrétée sans audit** : affirmer qu'un outil est « souverain » parce que l'éditeur le dit, sans vérifier les 4 critères. Risque : découverte tardive d'un sous-traitant US ou d'un Cloud Act applicable.
- **Souveraineté binaire** (soit 100 % soit 0 %) : la souveraineté est graduée (4 niveaux). Refuser un outil EU au niveau Moderate parce qu'il n'est pas niveau Sovereign est souvent disproportionné.
- **Souveraineté comme alibi anti-IA** : utiliser l'argument souveraineté pour reporter indéfiniment l'adoption IA. La bonne approche est de cartographier le niveau requis par cas d'usage puis de choisir.
- **Souveraineté de façade** (washing) : un outil avec landing page « EU sovereign » mais inférence US derrière. Vérifier l'attestation contractuelle, pas la com.

## Pour aller plus loin

- **Sécurité IA cadrage stratégique** ([[pr-05]]) : la souveraineté est l'une des dimensions de la sécurité IA en PME 2026.
- **Conformité RGPD/AI Act** ([[cu-020]]) : cadre réglementaire EU qui motive structurellement la souveraineté.
- **Inférence et coûts SaaS vs self-hosted** ([[dep-06]]) : arbitrage économique entre souveraineté self-hosted et confort SaaS.
- **RAG en production** ([[dep-02]]) : la souveraineté du vector store est une décision structurante du RAG en PME.
- **Fiches outils par catégorie** : [[outils-llm]], [[outils-frameworks-rag]], [[outils-knowledge-management]], [[outils-observabilite-llm]], [[outils-workflow-automation]], [[outils-vector-db]] — chaque fiche signale le niveau de souveraineté de chaque outil.
