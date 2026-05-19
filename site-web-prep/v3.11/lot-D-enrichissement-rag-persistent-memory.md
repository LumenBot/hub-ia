# Lot D v3.11 — Enrichissement encart RAG vs persistent memory (CU-008 + DEP-02)

**Brief consolidé pour Claude Code** : enrichissement ciblé des encarts symétriques produits en **v3.10 Lot A** (CU-008 `#llm-wiki-shelf-life` et DEP-02 `#section-2bis` ou équivalent). Pas de nouvelle section — actualisation du contenu existant avec une **4ème confirmation convergente** et des **benchmarks chiffrés concrets**.

**Sources** : run veille 2026-05-19 (Grok screener 6 + agentmemory benchmarks publiés @ghumare64 + relais @BeauJohnson89 / @CliffDoesAI / @JE4NVRG).

**Justification** : la trajectoire intégrée en v3.10 sur 3 signaux convergents (SubQ long context + LLM Wiki Karpathy + Hermes persistent memory) reçoit en mai 2026 une **4ème confirmation forte** avec **données chiffrées publiées** et **écosystème de hooks multi-agents réel**. Le pattern passe du stade « discussion narrative » au stade « infrastructure réelle avec benchmarks publics ». L'enrichissement permet de maintenir la crédibilité du Hub face à la maturation rapide de l'écosystème.

---

## Patch D.1 — CU-008 — enrichissement de la sous-section `#llm-wiki-shelf-life`

**Module cible** : `modules/cu-008-knowledge-base-rag.html`
**Position** : actualiser la sous-section `#llm-wiki-shelf-life` (ou anchor équivalent retenu par Claude Code en v3.10) créée en v3.10 Lot A.1.

### Modifications à apporter

#### 1. Passer de « 3 signaux convergents » à « 4 signaux convergents »

**Texte v3.10 à remplacer** (ou similaire) :

> Trois signaux convergents — un horizon qui se resserre
> [...] trois sources indépendantes ont signalé la même hypothèse [...]

**Nouveau texte à intégrer** :

> Quatre signaux convergents — la trajectoire bascule de « discussion » à « infrastructure »
>
> En mai-juin 2026, quatre sources indépendantes ont signalé la même hypothèse. Le signal mérite désormais d'être pris très au sérieux par toute PME qui investit dans une stack RAG.

#### 2. Ajouter le 4e signal (agentmemory) en complément des 3 existants

**Nouveau bloc à intégrer après les 3 signaux existants** (SubQ + LLM Wiki Karpathy + Hermes Vargas) :

> **Signal 4 — agentmemory et l'écosystème de hooks partagés (mai 2026)**
>
> Le passage de discussion à infrastructure : un projet open-source nommé **agentmemory** (créé par @ghumare64, **13 200+ stars GitHub en quelques semaines**) propose une **couche de persistent memory commune à tous les coding agents** (Claude Code, Hermes Agent, OpenClaw, Codex CLI, Cursor, Gemini CLI) via un serveur local SQLite + FAISS.
>
> Les benchmarks publiés sont **mesurables et explicites** :
> - **95,2 % r@5 (recall at 5) vs 86,2 % BM25 fallback** — gain net de qualité sur la récupération de contexte pertinent
> - **Coût token divisé par 100+ vs full context injection** — gain d'ordre de grandeur sur la facture LLM
>
> L'argument structurel : si **plusieurs coding agents partagent la même mémoire persistante**, l'agent ponctuel devient un **système qui se souvient** du codebase, des décisions passées et des corrections d'erreur — sans réingestion à chaque session. Cohérent avec le pattern « Fat Skills + Persistent Memory » (Garry Tan) et avec le pattern LLM Wiki original (Karpathy).

#### 3. Ajouter une mention de claude-smart en complément (signal additionnel)

À insérer comme **note en bas du paragraphe « Signal 4 »** :

> 💡 **Pattern adjacent à surveiller** — **claude-smart** (plugin self-improving lancé 18 mai 2026 par Yi Lu, Tech Lead Meta AI / ReflexioAI) automatise la création de skills réutilisables Claude Code à partir de l'analyse des sessions passées. C'est l'**automatisation de la création d'Agent Skills** (cf. DEP-05 §8.4). Pas encore mesuré, mais cohérent avec la trajectoire persistent memory.

#### 4. Cross-links à mettre à jour

- Vers la nouvelle **fiche agentmemory** dans `ressources.html` (créée en Lot B v3.11 — catégorie « Stack agentique Claude/Anthropic » sous-catégorie ECC & écosystème Anthropic)
- Vers la nouvelle **fiche claude-smart** dans `ressources.html` (si fiche créée en Lot B — sinon mention en texte avec lien GitHub direct)
- Conserver le cross-link existant vers **DEP-02 §section-2bis** (patch D.2 ci-dessous)

### Sources à ajouter dans #ressources de CU-008

À insérer dans la sous-rubrique « 📰 Articles de fond » :

- **@ghumare64 (Rohit Ghumare)** — agentmemory : persistent memory layer for coding agents (github.com/rohitg00/agentmemory, mai 2026)
- **Relais @BeauJohnson89 / @CliffDoesAI / @JE4NVRG** — adoption agentmemory dans la communauté builders ECC

### Métadonnées module

- `<meta name="description">` : aucune modification majeure.
- Badge temps de lecture : passer à **+2 min** (encart enrichi).

---

## Patch D.2 — DEP-02 — enrichissement symétrique de la sous-section `#section-2bis`

**Module cible** : `deploiement/dep-02-rag-architecture-prod.html`
**Position** : actualiser la sous-section `#section-2bis` (ou anchor équivalent retenu par Claude Code en v3.10) créée en v3.10 Lot A.2.

### Modifications à apporter

#### 1. Passer de « 3 signaux convergents » à « 4 signaux convergents »

Même modification structurelle que Patch D.1 — passer de 3 à 4 signaux dans le texte d'intro.

#### 2. Ajouter le 4e signal (agentmemory) avec angle production

**Nouveau bloc à intégrer après les 3 signaux existants** :

> **Signal 4 — agentmemory : la persistent memory devient infrastructure mutualisable (mai 2026)**
>
> Côté production, **agentmemory** (13 200+ stars GitHub en quelques semaines, créé par @ghumare64) est la première implémentation **mutualisable cross-agents** d'une couche de persistent memory :
>
> - Serveur **local SQLite + FAISS** (pas de SaaS — souveraineté / RGPD respectés)
> - Hooks officiels pour **Claude Code, Hermes Agent, OpenClaw, Codex CLI, Cursor, Gemini CLI**
> - Benchmarks publiés : **95,2 % r@5 vs 86,2 % BM25 fallback** + **coût token ÷ 100+**
> - Pattern de déploiement local-first, compatible avec les architectures A3/A4 (souveraineté contrôlée / forte)
>
> **Implication pour l'équipe qui industrialise un projet RAG en 2026** : avant de surinvestir dans une infrastructure RAG classique, évaluer si un **pattern hybride RAG-light + persistent memory** ne suffit pas. La barre de qualité (95,2 % r@5) et le ratio coût (÷ 100+) rendent l'arbitrage non trivial.

#### 3. Actualiser le tableau de décision RAG (section 4) si applicable

Si la section 4 « Tableau de décision RAG » contient déjà une ligne « agent avec mémoire conversationnelle » (intégrée en v3.10), **actualiser la recommandation associée** :

- **Avant v3.10** : « cas non couvert »
- **v3.10** : « privilégier persistent memory plutôt que RAG hybride »
- **v3.11** : *« privilégier une couche persistent memory mutualisable (cf. agentmemory) plutôt que RAG hybride. Architecture local-first (SQLite + FAISS) compatible souveraineté A3/A4. Benchmark de référence : 95,2 % r@5 + coût token ÷ 100+. »*

#### 4. Cross-links à mettre à jour

- Vers la nouvelle **fiche agentmemory** dans `ressources.html`
- Conserver le cross-link existant vers **CU-008** (patch D.1 ci-dessus)
- Vers la **page Architectures** pour la mention du futur pattern A5 (à laisser en préfiguration, pas encore créé)

### Sources à ajouter dans #ressources de DEP-02

À insérer dans la sous-rubrique « 📰 Articles de fond » :

- **@ghumare64 (Rohit Ghumare)** — agentmemory : persistent memory layer (github.com/rohitg00/agentmemory, mai 2026)
- **Benchmarks publiés** : 95,2 % r@5 vs 86,2 % BM25 fallback + coût token ÷ 100+

### Métadonnées module

- `<meta name="description">` : aucune modification majeure.
- Badge temps de lecture : passer à **+2 min**.

---

## Cohérence cross-modules Lot D

Les 2 patches D.1 (CU-008) et D.2 (DEP-02) doivent rester **strictement symétriques** dans leur formulation, comme l'étaient déjà les encarts v3.10 Lot A :

- Même nombre de signaux convergents (passage de 3 à 4)
- Mêmes chiffres agentmemory cités (95,2 % r@5, coût token ÷ 100+, 13 200+ stars)
- Même formulation de la trajectoire (« discussion → infrastructure »)
- Mêmes sources citées avec mêmes URLs
- Mêmes cross-links réciproques + cross-link vers fiche agentmemory du Lot B v3.11

L'angle pédagogique diffère légèrement entre CU-008 (dirigeant découvrant) et DEP-02 (équipe industrialisant) — c'est conforme aux conventions des 2 modules et déjà acté en v3.10.

## Renvois croisés vers d'autres modules

- **CU-026** (Pattern « agent = employé ») : encart léger « la persistent memory partagée s'intègre naturellement au pattern agent = employé — chaque employé garde sa mémoire à long terme »
- **DEP-05 §8.4** (Agent Skills v3.9) : encart léger « claude-smart automatise la création de skills à partir de l'analyse des sessions Claude Code »

## Item parallèle (à compiler dans brief v3.11)

Pas de nouveau chiffre macro à canoniser pour ce Lot D — les chiffres agentmemory (95,2 % r@5, coût token ÷ 100+) sont **spécifiques à un outil** et restent local à CU-008 / DEP-02. Ils ne feront pas l'objet d'un wikilink chiffres-macro côté MD RAG.
