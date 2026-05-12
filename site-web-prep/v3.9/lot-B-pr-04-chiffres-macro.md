# Lot B v3.9 — Patch chiffres macro PR-04 (Marché IA & emploi)

**Brief consolidé pour Claude Code** : enrichissement chiffré de PR-04 avec **3 nouvelles sources institutionnelles 2026** convergentes sur un thème nouveau : **la maturité agentique et les bottlenecks de confiance**.

**Sources** : veille `pistes-cumulatives.md` run 2026-05-12 (Gartner via @Srini_Pa, McKinsey State of AI Trust 2026, MIT Sloan Davenport & Bean).

**Item parallèle** : transmission **I-004 au couple 2** (Hub IA Plateforme) pour canonisation des chiffres dans `chiffres-macro-2026.md` côté RAG.

---

## Patch B.1 — Nouvelle section 2ter : « Maturité agentique et bottlenecks 2026 »

**Module cible** : `prealables/pr-04-marche-ia-emploi.html`
**Position** : insérer **après** la section 2bis « Tendances macro 2026 » et **avant** la section 3 « Prime salariale ».
**Anchor id** : `section-2ter`
**Icône TOC** : 🤖
**Label TOC** : « Maturité agentique »

### Contenu à intégrer

#### 1. Le shift de palier 2025 → 2026

Les chiffres 2024-2025 mesuraient l'**adoption** de la GenAI (qui utilise ChatGPT ? quelles fonctions ? quelle fréquence ?). Les chiffres 2026 mesurent autre chose : la **mise en production d'agents** et les **bottlenecks** qui empêchent de scaler. Le palier change.

**McKinsey State of AI Trust 2026** (publié mars 2026) :
- **23 %** des organisations interrogées **scalent au moins un système agentique** (passage de pilote à production large)
- **39 %** sont en phase d'**expérimentation** (pilotes en cours, pas encore généralisés)
- **74 %** identifient **l'inexactitude** comme un risque hautement pertinent
- **72 %** identifient **la cybersécurité** comme un risque hautement pertinent

**Lecture** : on est passé d'une question « est-ce que l'IA marche ? » à « est-ce que je peux lui faire confiance en production ? ». Les bottlenecks ne sont plus techniques (modèles, infra) mais opérationnels (qualité des sorties, sécurité des accès).

#### 2. L'avertissement Gartner — l'échec ROI le plus coûteux

Une étude Gartner publiée en mai 2026 a interrogé **350 executives d'entreprises >1 Md$** déjà en production avec des agents IA. Le résultat est brutal :

> **80 % de ces entreprises ont supprimé des postes sans gain de ROI mesuré.**

C'est un **échec architectural**, pas un échec d'idée. Le pattern observé : les entreprises ont décidé de remplacer des fonctions humaines par des agents avant d'avoir prouvé que les agents tenaient en production. Conséquence : suppression de postes → agents non fiables → re-création des postes 6-12 mois plus tard, à coût élevé.

**Implication pour la PME** : ne **jamais** supprimer un poste sur la base d'un POC ou d'un pilote. La règle opérationnelle : un agent ne remplace une fonction qu'après **6 mois minimum** en production parallèle (l'agent fait, l'humain valide, on mesure). Si cette parallélisation n'est pas tenable financièrement, c'est que le ROI réel n'est pas démontré.

#### 3. La gouvernance comme nouveau différenciateur — l'émergence du Chief AI Officer

**MIT Sloan Management Review** (Davenport & Bean, mai 2026, « Five trends in AI and data science for 2026 ») met en évidence un signal organisationnel fort :

> **38 % des grandes entreprises répondantes ont nommé un Chief AI Officer ou équivalent** (CAIO, Head of AI, VP AI).

Le profil émerge comme **fonction stratégique** distincte du CDO (Chief Data Officer) et du CTO. Sa mission : arbitrer entre les demandes business, la dette technique IA, la conformité (AI Act) et la cohérence du portefeuille de projets.

**Les 5 tendances IA 2026 identifiées par MIT Sloan** :
1. **Déflation possible de la bulle IA** — correction de marché anticipée (valorisations vs ROI réel)
2. **« Factory » infrastructure** pour les all-in adapters (entreprises qui industrialisent leur stack IA)
3. **GenAI comme ressource organisationnelle vs individuelle** — passage de l'usage personnel ChatGPT à l'usage structuré entreprise
4. **Valeur agentique malgré le hype** — les premiers ROI mesurables apparaissent
5. **Gouvernance data&IA** comme nouveau différenciateur stratégique

**Implication pour la PME** : il n'est pas réaliste pour une PME de 30-200 salariés de recruter un CAIO. Mais le rôle existe **diffusé** : DG + DSI + un référent IA opérationnel (souvent un chef de projet ou un directeur métier). La question pour 2026 n'est pas « qui est notre CAIO ? » mais **« qui arbitre nos décisions IA et avec quelle grille ?»**.

#### 4. Synthèse — la cartographie de la maturité 2026

À fin 2026, le marché se segmente en **4 paliers** :

| Palier | Caractéristiques | % entreprises |
|---|---|---|
| **Découverte** | Usage individuel ChatGPT, pas de stratégie | ~40 % |
| **Expérimentation** | Pilotes IA, POC en cours, premiers cas d'usage | ~39 % |
| **Mise en production** | Agents scalés, observabilité, gouvernance émergente | ~23 % |
| **Industrialisation** | Stack mature, CAIO ou équivalent, ROI mesuré | ~15 % |

(Les paliers ne s'additionnent pas à 100 % car l'industrialisation est un sous-ensemble de la mise en production.)

**Question opérationnelle pour le dirigeant** : sur quel palier est-on aujourd'hui ? Sur quel palier sera-t-on dans 12 mois ? Quels sont les bottlenecks qui nous empêchent de passer au palier suivant ? Ces 3 questions sont le cœur de la démarche IA stratégique 2026.

---

## Sources à ajouter dans la section finale (sous-rubrique 📰 Articles de fond)

À insérer dans la section `#ressources` :
- **McKinsey State of AI Trust 2026** — mckinsey.com/capabilities/tech-and-ai/our-insights/tech-forward/state-of-ai-trust-in-2026-shifting-to-the-agentic-era (mars 2026)
- **MIT Sloan Management Review — Davenport & Bean** — sloanreview.mit.edu/article/five-trends-in-ai-and-data-science-for-2026/ (mai 2026)
- **Compte X @Srini_Pa** — étude Gartner 350 executives agents IA (mai 2026, 428 likes, 154 RT)

---

## Mise à jour TOC du module

Ajouter dans le sommaire (`<aside class="module-toc">`) entre l'entrée « Tendances macro 2026 » et l'entrée « Prime salariale » :

```html
<li><a href="#section-2ter"><span class="toc-icon">🤖</span>Maturité agentique</a></li>
```

## Renvois internes à mettre à jour dans PR-04

- En section 2bis (Tendances macro 2026) : ajouter une mention de transition vers section 2ter — « Au-delà des chiffres d'adoption GenAI, le palier 2026 se mesure autrement (voir section suivante). »
- En section 5 (Implications stratégiques) : encart court mentionnant les 4 paliers de maturité comme grille d'auto-positionnement.

## Renvois croisés vers d'autres modules

- **PR-01** (Maturité organisationnelle) : ajouter un encart léger « complémentaire à PR-04 §2ter » dans la section pertinente.
- **CU-026** (Gouvernance agents IA) : renvoyer vers PR-04 §2ter en encart « contexte marché ».
- **DEP-05** (Agents en production) §8 nouvelle : renvoyer vers PR-04 §2ter en encart « contexte marché » de la section 8.

## Métadonnées module

- `<meta name="description">` : à actualiser. Suggestion : *« 23 % des entreprises scalent un agent IA, mais 80 % de celles qui ont supprimé des postes l'ont fait sans gain ROI mesuré. Comprendre la maturité agentique 2026 et ses bottlenecks. »*
- Badge temps de lecture : passer de l'actuel à **+2 min** (estimation +2 min pour section 2ter).

---

## Item I-004 à transmettre au couple 2 (Hub IA Plateforme)

**Périmètre** : canonisation des **3 nouveaux chiffres macro** dans `transverses/chiffres-macro-2026.md` côté RAG.

Chiffres à canoniser :
- **23 % organisations scalent un système agentique** — McKinsey State of AI Trust 2026
- **39 % organisations en phase d'expérimentation agentique** — McKinsey State of AI Trust 2026
- **74 % identifient l'inexactitude comme risque hautement pertinent** — McKinsey State of AI Trust 2026
- **72 % identifient la cybersécurité comme risque hautement pertinent** — McKinsey State of AI Trust 2026
- **80 % entreprises >1 Md$ ont supprimé des postes sans gain ROI** — Gartner via @Srini_Pa
- **38 % grandes entreprises ont nommé un Chief AI Officer** — MIT Sloan Davenport & Bean 2026

Justification du recouvrement attendu : ces chiffres seront repris dans CU-026 (gouvernance agents), DEP-05 (production agents), PR-01 (maturité orga). R9 SPEC v1.1 → wikilinks plutôt que reformulation.

**Format brief I-004** : à compiler dans le brief de passation v3.9 + inscription `SYNC-INTER-CANAUX.md`.
