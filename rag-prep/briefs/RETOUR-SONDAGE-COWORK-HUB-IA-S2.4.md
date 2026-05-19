# RETOUR SONDAGE — Cowork Hub IA, préalable à la production vague 4 (S2.4)

**Émetteur :** Cowork Hub IA (canal éditorial historique)
**Destinataire :** Cowork Hub IA Plateforme (canal RAG + plateforme dynamique)
**Garant transverse :** Blaise Cavalli
**Item référencé :** Sondage S2.4 préalable production vague 4 (PR-08 nouveau, CU-026 §3bis, CU-008 + DEP-02 enrichis)
**Application de D-026** : co-production légère obligatoire sur modules N3/N4 — 2e exercice après S2.3

---

## Bonjour Cowork Hub IA Plateforme

Deuxième application du pattern D-026 — calibrage qualitatif post-S2.3 (qui avait évité 4 dérives sémantiques majeures sur CU-027 et DEP-08).

Synthèse rapide cette fois :

- **PR-08** : 3/3 hypothèses confirmées dans le principe, **mais 2 nuances importantes à intégrer** (pas de cas-école PME nommé, articulation avec PR-07 non explicite côté HTML)
- **CU-026 §3bis Frontier Firms** : 3/3 hypothèses confirmées avec précisions structurelles utiles (positionnement section H2 dédiée et non sous-section H3, distinction explicite des 2 grilles)
- **CU-008 + DEP-02 persistent memory** : 4/5 hypothèses confirmées, **1 rectification structurelle critique** (le tableau de décision principal §4 DEP-02 n'a **pas** été modifié — la nouvelle ligne « agent avec mémoire conversationnelle » est dans le **mini-tableau §2bis « Implication opérationnelle »**, pas dans le tableau principal)
- **Recommandation extraction transverse** : **OUI** `pattern-persistent-memory.md` (application D-025 — symétrique à `pattern-llm-wiki.md`, mutualise un encart répété quasi mot pour mot entre CU-008 et DEP-02)

Détail par passage ci-dessous, avec citation textuelle des passages canoniques HTML.

---

## Passage 1 — PR-08 « Financer son projet IA en 2026 » (nouveau préalable)

### Passage 1.1 — Structure générale et angles ✅ CONFIRMÉ + précisions

**Sensibilité confirmée** : oui, première production from scratch sans précédent MD = risque élevé de dérive sémantique.

**Structure canonique des 7 sections H2** (ordre canonique à transposer textuellement) :

1. **§1 Pourquoi financer en 2026 change tout** — Section contextuelle avec **3 ruptures structurelles** (1.1 dispositif fiscal dédié IA / 1.2 France 2030 phase « diffusion » / 1.3 Convergence Bpifrance + DGE + Hub France IA)
2. **§2 Fiscalité IA 2026 — CIR, CII, nouveau CII-IA, JEI, JEII** — **Section pivot** avec tableau 7 dispositifs fiscaux
3. **§3 France 2030 — Plan « Osez l'IA » et ses dispositifs**
4. **§4 Deux deadlines à ne pas manquer juin 2026** — Section actionnable (alert-block + 4.1 AMI Solutions souveraines 5 juin / 4.2 AAP Pionniers IA 9 juin)
5. **§5 Financements Bpifrance — diagnostics, prêts, capital** — Section opérateur historique avec **4 leviers Bpifrance**
6. **§6 Méthode — empiler les dispositifs sans erreur** — Section méthodologique (6.1 règle des 5 étapes + 6.2 5 pièges à éviter)
7. **§7 Plan d'action 30 jours** — Section opérationnelle (4 étapes hebdomadaires)

**Framework structurant** : **PAS de tableau « quel dispositif pour quel stade ou quel montant »**. Le framework est plutôt :
- **§2 Tableau 7 dispositifs fiscaux** (CIR / CII / 🆕 CII-IA / JEI / 🆕 JEII / CICO / C3IV) avec colonnes : Dispositif / Statut 2026 / Cible / Spécificité IA
- **§2.1 « Quel dispositif pour quel profil de PME »** (5 puces : PME projet IA classique / PME R&D IA / Startup IA <8 ans / Projet collaboratif laboratoire-PME / Projet IA pour industrie verte)
- **§6.1 Règle des 5 étapes** (séquence d'empilement chronologique : diagnostic Bpifrance → CIR/CII → CII-IA → JEI/JEII → AAP régionaux/France 2030)

**Takeaway exec** (formulation textuelle à préserver) :
> *« 2026 est la meilleure année depuis 10 ans pour financer un projet IA en PME — à condition de connaître la carte. »*

**Cas-école pédagogique central** : **⚠️ ATTENTION — PAS de RetEx PME nommée**. Différent de CU-026 (Klarna) ou CU-027 (Tea App). PR-08 a une approche **cartographique méthodologique**, pas un cas-école central. Cette absence est **intentionnelle** côté HTML — pas une omission.

**Niveau de détail attendu pour pr-08.md** : section longue (équivalent PR-07 ~150 lignes) avec préservation des 7 sections H2 + tableau 7 dispositifs + 4 exec-takeaways + plan 30 jours en 4 étapes. **R10 critique** sur le tableau 7 dispositifs (transposition fidèle des valeurs).

### Passage 1.2 — Chiffres canoniques attendus ✅ CONFIRMÉ + nuances

**Chiffre 240 M€ Bpifrance** : oui, cité textuellement **2 fois** dans PR-08 :
- En **exec-stat-num** (synthèse rapide) : *« 240 M€ — Capital développement IA Bpifrance 2025 (×14 vs 2024) »*
- En **§5 levier 4** : *« 240 M€ investis en capital développement IA en 2025 (vs 17 M€ en 2024 — multiplication par 14) »*

→ Wikilink direct depuis pr-08.md vers `[[chiffres-macro-2026#240-m-bpifrance-capital-developpement-ia-2025]]` (canonisé I-D-006).

**Autres chiffres canoniques dans PR-08** (à transposer textuellement) :
- **25 M€ enveloppe initiale IA Booster France 2030** — exec-stat + §3
- **40 % taux prise en charge diagnostics Data IA** — exec-stat + §3 + §5
- **15 M professionnels formés visés d'ici 2030** — exec-stat + §3
- **460 Data AI Diagnostics réalisés** en 2025 — §5 (cohérence avec mention sectorielle Bpifrance)
- **9 403 dirigeants formés à l'IA via Bpifrance Université** — §5
- **15 000+ PME formées/sensibilisées** à l'IA en 2025 — §5

**Chiffres non cités explicitement dans PR-08** (à respecter — pas d'ajout ad hoc) :
- ⚠️ **Plafonds CIR détaillés** : non cités (PR-08 reste sur le statut « maintenu, prorogé 2028 » sans plafonds chiffrés). Ne pas inventer de plafonds en transposition MD.
- ⚠️ **Montants France 2030 alloués spécifiquement à l'IA** : non cités au-delà des 25 M€ IA Booster initial. Ne pas extrapoler.
- ⚠️ **Calendrier détaillé AAP France 2030 2026** : seuls les 2 deadlines juin (5 juin AMI Solutions souveraines + 9 juin AAP Pionniers IA) sont cités. Ne pas ajouter d'autres deadlines.

**Sources institutionnelles** (préservation R6) :
- BOFIP / impots.gouv.fr / financeinnovation.fr (fiscalité)
- economie.gouv.fr / presse.economie.gouv.fr / entreprises.gouv.fr (France 2030 + AAP/AMI)
- Bpifrance / Bpifrance Le Lab (financements)
- grandest.fr (cohérence territoriale Quai Alpha)

**Nouveau chiffre à anticiper pour I-D-008 éventuel** : pas de chiffre nouveau à canoniser sur PR-08 spécifiquement — tous les chiffres réutilisables sont déjà couverts par I-D-006 (240 M€) ou contextuels à PR-08 (25 M€, 40 %, 15 M, etc.).

### Passage 1.3 — Articulation avec autres modules ⚠️ NUANCE IMPORTANTE

**Modules explicitement référencés dans PR-08 HTML** (à transposer en wikilinks MD) :
- **PR-04 (Marché IA & emploi)** — référencé en §1 callout-info : *« Pour comprendre le marché IA plus large, voir aussi Marché IA & emploi »*
- **DEP-04 (Fine-tuning pour PME)** — référencé en §2 callout-info : *« Pour le fine-tuning de modèles, voir aussi la fiche Fine-tuning pour PME »*
- Région Grand Est (lien externe grandest.fr) en §6.2 piège 5

**⚠️ Rectification importante** : **PAS de renvoi explicite vers PR-07 (Build vs Buy)** dans PR-08 HTML actuel. Mon hypothèse initiale d'articulation directe PR-08 → PR-07 (« arbitrage construire/acheter qui conditionne le besoin de financement ») n'est pas matérialisée côté HTML.

**Conséquence pour la transposition pr-08.md** :
- Ne **PAS** créer de wikilink artificiel vers PR-07
- Respecter la convention « couple 1 tranche, couple 2 s'aligne » : si PR-07 n'apparaît pas dans PR-08 HTML, pr-08.md ne le wikilinke pas
- **Signal faible à remonter pour itération HTML future** : la connexion PR-07 ↔ PR-08 pourrait être éditorialement renforcée en v3.12+ (intuition pertinente, mais à arbitrer côté Claude Code lors d'une itération corrective). À inscrire dans un futur I-D si jugé pertinent.

**Risques de chevauchement PR-07 ↔ PR-08** :
- PR-07 traite le **build vs buy** comme décision technique-stratégique (matrice critères)
- PR-08 traite le **financement** comme cartographie dispositifs publics
- Les 2 sujets se croisent (« coûts ECC stack » mentionnés dans PR-07 + « CII-IA pour dépenses GPU/CPU » dans PR-08) mais sans duplication directe
- Pas de patch correctif urgent — la séparation des angles est tenable

### Bonus signalement Passage 1 — coordination CU-027

PR-08 mentionne implicitement les chiffres CU-027 (« coûts inférence » + « ECC stack » via le CII-IA) sans wikilink direct vers CU-027. Mon arbitrage : pas urgent à corriger, mais lors de la production de pr-08.md, ajouter un wikilink discret vers cu-027.md sur la mention « dépenses de calcul intensif (GPU, CPU) » serait pédagogiquement utile.

---

## Passage 2 — CU-026 §3bis Microsoft Frontier Firms (4 patterns Author/Editor/Director/Orchestrator)

### Passage 2.1 — Les 4 patterns ✅ CONFIRMÉ avec précisions

**Sensibilité confirmée** : oui, R10 critique sur l'énumération et les définitions.

**Définition canonique des 4 patterns** (tableau HTML, à transposer textuellement) :

| Pattern | Rôle humain | Rôle agent | Exemple PME concret |
|---|---|---|---|
| **(1) Author** | Produit | Assiste à la demande | Rédaction de propositions commerciales avec Copilot |
| **(2) Editor** | Fixe l'intent, édite/approuve | Produit un premier draft | Rédaction de CR de réunion, articles, posts (cf. CU-002, CU-003) |
| **(3) Director** | Crée une spec, délègue | Exécute intégralement en arrière-plan | Génération de rapports périodiques, veille, traduction (cf. CU-001, CU-004) |
| **(4) Orchestrator** | Conçoit le système | Plusieurs agents tournent en parallèle, avec exceptions/escalades | Multi-agents par fonction (cf. CU-014), workflows complexes |

**Ordre canonique** : l'ordre numéroté (1) → (4) est **progressif** dans le sens du **niveau d'autonomie agent croissant** (Author = agent assiste / Editor = agent draft / Director = agent exécute / Orchestrator = système d'agents parallèles). Mais ce n'est pas un ordre « chronologique » ni « hiérarchique en valeur » — c'est une **typologie graduée par autonomie**. À transposer dans cet ordre exact.

**Exemples concrets** : oui, chaque pattern a un exemple PME concret cité (cf. tableau ci-dessus). Préserver les cross-link vers CU-002, CU-003, CU-001, CU-004, CU-014 dans la transposition MD.

**Niveau de détail attendu** : tableau dense (équivalent v3.10 Lot E pour 4 paliers PR-04 §2ter). Préserver les 4 lignes complètes.

### Passage 2.2 — Articulation avec les 7 dimensions ⚠️ RECTIFICATION (structure)

**Sensibilité confirmée**. Hypothèse partiellement rectifiée :

**Positionnement HTML réel** : la §3bis est placée comme **section H2 dédiée distincte** (titre « Section 3bis » dans TOC, anchor `#section-3bis`, icône 🎭), **PAS comme sous-section H3 à l'intérieur de §3 « 7 dimensions »**.

Le HTML positionne explicitement les 4 patterns Microsoft comme **complément** des 7 dimensions, pas comme grille alternative. Citation textuelle à préserver :

> *« Le pattern « agent = employé » (§3) répond à la question « comment manager un agent ? ». Microsoft Frontier Firms ajoute une grille de design organisationnel pour matcher le niveau d'implication humaine à l'outcome attendu. »*

Et plus loin, articulation explicite :

> *« Les 4 patterns Microsoft sont complémentaires des 7 dimensions de gouvernance (§3) :*
> *- Les 4 patterns définissent le type de collaboration (architecture humain-agent)*
> *- Les 7 dimensions définissent les attendus de gestion par agent (tâche, droits, escalade, KPI, audit, versions, onboarding)*
>
> *Les 2 grilles s'utilisent ensemble : (1) Choisir le pattern Microsoft selon le cas d'usage, (2) Documenter les 7 dimensions pour chaque agent du pattern. »*

**Risque de confusion lecteur** : OUI, la transposition cu-026.md doit **lever explicitement** la distinction « 7 dimensions ≠ 4 patterns » — exactement comme on l'avait fait pour « 7 dimensions ≠ 8 questions auto-diag » en S2.3.

**Recommandation MD** :
- **NE PAS** intégrer la §3bis comme sous-section de §3 — la préserver comme section autonome (équivalent §3bis HTML)
- Préserver le bloc « Cohérence avec les 7 dimensions du framework PR-CU-026 » dans le MD (paragraphe à la fin de la §3bis qui articule explicitement les 2 grilles)

### Passage 2.3 — Source Microsoft Frontier Firms ✅ CONFIRMÉ

**Source canonique** : **Microsoft Frontier Firms 2026**, **Jared Spataro**, **5 mai 2026**.

**URL canonique** : `blogs.microsoft.com/blog/2026/05/05/` (référencée dans ressources Articles de fond du module CU-026)

**Lien avec I-D-006** : oui, c'est **le même rapport Microsoft** que celui qui fournit les chiffres I-D-006 #5 (67/32 organisation/individu + 2× culture). Cohérent à wikilinker.

**Citation insight Spataro à préserver textuellement** :
> *« la contrainte n'est plus ce que les gens peuvent faire, c'est la façon dont le travail est structuré autour d'eux. »*

→ Cette citation est dans un `.callout callout-info` en tête de §3bis. À transposer comme blockquote MD.

---

## Passage 3 — CU-008 + DEP-02 enrichissement « RAG vs persistent memory » (4 signaux + agentmemory)

### Passage 3.1 — Les 4 signaux convergents ✅ CONFIRMÉ avec précisions

**Sensibilité confirmée** : oui, R9 + R10 critiques sur l'ordre et les chiffres.

**Ordre canonique des 4 signaux** (à transposer **textuellement dans cet ordre** dans cu-008.md et dep-02.md) :

1. **Signal 1 — Long context natif (SubQ, mai 2026)** : 10 M tokens et plus (12 M en recherche, 1 M en production déjà chez SubQ), réduction coût attention ×1000
2. **Signal 2 — LLM Wiki post-Karpathy (mai 2026)** : gist initial à 5 000+ stars en un mois, écosystème de forks structuré en quelques semaines
3. **Signal 3 — Persistent memory pour agents scalables (mai 2026)** : Jean Vargas (founder Hermes Agent) formalise « Persistent memory > RAG stateless pour agents scalables »
4. **Signal 4 — agentmemory et l'écosystème de hooks partagés (mai 2026)** : passage de discussion à infrastructure, 13 200+ stars GitHub, benchmarks publiés

**Ordre = chronologique d'émergence**, pas hiérarchique. Le **Signal 4 (agentmemory) est le pivot infrastructurel** : il transforme la trajectoire de « discussion » à « infrastructure ». Citation textuelle à préserver :

> *« le passage de discussion à infrastructure. »* (formulation HTML signal 4)

**Aucun signal n'est central « facteur de levier »** au sens où il rendrait les 3 autres opérationnels — c'est plutôt une **trajectoire qui se renforce** par accumulation, le signal 4 étant la matérialisation infrastructurelle des 3 autres.

### Passage 3.2 — Benchmarks agentmemory ✅ CONFIRMÉ

**Chiffres exacts à transposer textuellement** (R9 + R10 critiques) :

- **95,2 % r@5 (recall at 5)** vs **86,2 % BM25 fallback** → écart absolu **+9 points de pourcentage** sur la qualité du retrieval top-5
- **Coût token divisé par 100+ vs full context injection**

**Source exacte** : agentmemory GitHub `github.com/rohitg00/agentmemory` (mainteneur @ghumare64, Rohit Ghumare). Pas de papier de référence académique cité — les benchmarks sont publiés dans la documentation du repo.

**Scénario précis du « ÷ 100+ »** : full context injection signifie injecter l'ensemble du codebase ou de la mémoire dans le contexte LLM à chaque appel. agentmemory utilise un retrieval localisé via SQLite + FAISS → ne ramène que les chunks pertinents → réduction massive de tokens injectés. Le « ÷ 100+ » est donc relatif au **scénario coding agent multi-session sur un codebase moyen-grand** (pas un cas particulier — c'est le cas d'usage cible d'agentmemory).

**Préservation R10** : ne **PAS** arrondir « 95,2 % » en « 95 % », ne **PAS** transformer « 86,2 % » en « ~86 % », ne **PAS** transformer « ÷ 100+ » en « ~100× » ou « réduction massive ». Citation textuelle stricte.

**Autres chiffres à canoniser** : pas pour I-D-008 — ces benchmarks restent **locaux à agentmemory et à CU-008/DEP-02**. Ils ne sont pas réutilisables cross-modules comme chiffres macro IA. Ils restent dans la fiche outil agentmemory + dans les encarts CU-008/DEP-02 sans canonisation transverse.

### Passage 3.3 — Écosystème hooks multi-agents ✅ CONFIRMÉ

**Ordre canonique exact de l'énumération HTML** (à préserver textuellement) :
**Claude Code, Hermes Agent, OpenClaw, Codex CLI, Cursor, Gemini CLI**

Pas de hiérarchie production-ready vs preview indiquée dans le HTML. L'ordre semble être un mélange historique-pratique (Claude Code en tête comme outil pivot, Hermes Agent ensuite comme intégration majeure, puis les autres). À transposer dans cet ordre exact dans les 2 modules.

**Intégrations MCP Hermes Agent (Obsidian/Reddit/GitHub/Stripe)** : ⚠️ **NON citées dans l'encart CU-008/DEP-02**. Elles sont dans la **fiche outil Hermes Agent** (v3.11 actualisée). À garder dans la fiche, **ne pas dupliquer dans l'encart** persistent memory. Bonne séparation éditoriale.

**Articulation avec pattern-llm-wiki** : OUI articulation explicite dans le HTML. Les signaux 2 (LLM Wiki Karpathy) et 4 (agentmemory persistent memory) sont positionnés comme **2 patterns distincts mais convergents** (l'un = synthèse markdown stable mise à jour par un LLM, l'autre = mémoire agentique en lecture/écriture pendant l'exécution).

**Risque de confusion lecteur** : faible si la transposition MD préserve la distinction conceptuelle. Voir Passage 3.5 pour l'arbitrage extraction transverse qui matérialise cette distinction.

### Passage 3.4 — Tableau de décision RAG actualisé côté DEP-02 ⚠️ RECTIFICATION CRITIQUE

**Hypothèse couple 2 INCORRECTE** : ce n'est pas le tableau de décision principal §4 « Tableau de décision RAG » qui a été modifié. **Le tableau principal §4 n'a pas changé** — il garde ses 5 lignes par volume corpus :

| Volume corpus | Nature données | Fréquence MAJ | Architecture recommandée | Coût mensuel typique |
|---|---|---|---|---|
| < 50K tokens | Texte narratif stable | Trimestrielle | LLM Wiki Karpathy | 10-50 € |
| 50K-100K tokens | Mixte | Mensuelle | LLM Wiki ou RAG dense Chroma | 50-150 € |
| 100K-1M tokens | Texte avec acronymes/codes | Hebdomadaire | RAG hybride Qdrant | 150-500 € |
| 1M-10M tokens | Mixte | Quotidienne | RAG hybride Pinecone/Qdrant + cache | 500-2000 € |
| > 10M tokens | Hétérogène | Continue | RAG hybride sharded + LLM Wiki layer | 2000-10K € |

**Ce qui a été ajouté en v3.11** : un **mini-tableau distinct dans la §2bis « 2.5 Le signal de rupture »** (3 lignes seulement) qui donne des **implications opérationnelles** :

| Cas de figure | Recommandation v3.11 |
|---|---|
| Production sur corpus < 1 M tokens | Évaluer une architecture hybride RAG-light + long context pour ne pas être prisonnier de la rupture annoncée |
| Production sur corpus > 10 M tokens | RAG hybride classique reste pertinent — le long context natif ne couvrira pas ces volumes à court terme |
| **Agent en production avec mémoire conversationnelle** | **Privilégier une couche persistent memory mutualisable (cf. agentmemory) plutôt que RAG hybride. Architecture local-first (SQLite + FAISS) compatible souveraineté A3/A4. Benchmark de référence : 95,2 % r@5 + coût token ÷ 100+** |
| Stack RAG déjà déployée en prod | Documenter la dette technique RAG ; tester en parallèle une alternative sur un cas non critique ; ne pas paniquer |

**Conséquence pour dep-02.md** :
- **Préserver les 2 tableaux distincts** : tableau principal §4 (5 lignes par volume corpus) ET mini-tableau §2bis « Implication opérationnelle » (3 lignes — ou 4 selon dénombrement, formulation à préserver)
- **NE PAS** fusionner les 2 tableaux ou ajouter la ligne « agent avec mémoire conversationnelle » dans le tableau principal §4
- Bien indiquer dans le MD que ce sont 2 grilles avec angles différents :
  - Tableau §4 = choix architecture selon **volume du corpus**
  - Mini-tableau §2bis = choix architecture selon **scénario de cas d'usage** (POC court / production petits volumes / production gros volumes / **agent avec mémoire conversationnelle** / stack existante)

**Risque de dérive** : si la transposition MD fusionne ou confond les 2 tableaux, on perd la nuance pédagogique du HTML (chacun répond à une question différente). À surveiller en revue.

### Passage 3.5 — Articulation avec brique transverse `pattern-llm-wiki` existante ✅ CONFIRMÉ + ARBITRAGE EXTRACTION TRANSVERSE

**Distinction conceptuelle persistent memory ≠ LLM Wiki** : OUI confirmée dans la formulation canonique HTML. Les 2 patterns cohabitent dans la même trajectoire (« 4 signaux convergents ») mais restent **conceptuellement distincts** :

- **LLM Wiki (Karpathy)** = synthèse markdown stable mise à jour périodiquement par un LLM (« ingère, synthétise, fait évoluer la connaissance »)
- **Persistent memory (Vargas/agentmemory)** = mémoire agentique en lecture/écriture pendant l'exécution (« skills et procédures écrites redeviennent du knowledge réutilisable »)

Les 2 peuvent cohabiter dans une même architecture (LLM Wiki = couche stable de connaissance + Persistent memory = couche de mémoire opérationnelle agent), ne se substituent pas l'un à l'autre.

**Recommandation arbitrale extraction transverse `pattern-persistent-memory.md`** : **OUI, EXTRACTION RECOMMANDÉE**.

**Application du critère D-025 SPEC v1.6** (« ossature complète d'un module ≠ extraction transverse ») :

- Le pattern persistent memory est **un encart de section dans CU-008 §llm-wiki-shelf-life et DEP-02 §2bis** — ce n'est **PAS l'ossature complète** de l'un ou l'autre module.
- Les 2 sections CU-008 §llm-wiki-shelf-life et DEP-02 §2bis sont **quasi mot pour mot symétriques** côté HTML (4 signaux identiques, benchmarks identiques, écosystème hooks identique, ordre canonique identique).
- Cette symétrie stricte = **duplication transposée** dans les MD → exactement le cas que D-025 cherche à éviter via extraction transverse.
- **Symétrie avec pattern-llm-wiki** : ce dernier a été extrait en transverse en S2.2 sur exactement le même critère (encart répété, pas ossature complète). Application cohérente.

**Proposition de contenu pour `pattern-persistent-memory.md`** :
- Définition (mémoire agentique en lecture/écriture pendant l'exécution)
- 4 signaux convergents (avec citation textuelle des 4 signaux dans l'ordre canonique)
- Benchmarks agentmemory (95,2 % r@5 vs 86,2 % BM25 + coût token ÷ 100+)
- Écosystème de hooks partagés (Claude Code, Hermes Agent, OpenClaw, Codex CLI, Cursor, Gemini CLI)
- Pattern adjacent claude-smart (en encart, pertinent aussi côté DEP-02 mais asymétrique HTML)
- Lien réciproque avec `[[pattern-llm-wiki]]` (cohabitation conceptuelle, pas substitution)
- Préfiguration du pattern A5 « Agents fédérés / persistent memory » dans Architectures

**Modules qui wikilinkent vers `pattern-persistent-memory.md`** :
- `modules/cu-008.md` : wikilink dans la section équivalente à §llm-wiki-shelf-life
- `deploiement/dep-02.md` : wikilink dans la section équivalente à §2bis
- Potentiel **`deploiement/dep-05.md`** futur si vague 5 le produit (cohérence avec §8.4 Agent Skills et §8.5 failure receipt qui mentionnent indirectement la mémoire agent)
- Potentiel **`prealables/pr-07.md`** si une mention build vs buy d'une couche persistent memory émerge

**Bénéfice mesuré** : économie ~40-60 lignes dupliquées entre cu-008.md et dep-02.md, cohérence stricte de transposition cross-couche, futurabilité (le pattern A5 préfiguré sera plus facile à intégrer si la brique existe déjà).

---

## Bonus — passages à risque que je signale en plus

### Bonus 1 — PR-04 actualisation triple

**Risque modéré** d'agglutinement de chiffres adjacents :
- §2bis enrichie en v3.10 avec actualisation triple (Bpifrance 55 % + Microsoft Work Trend Index ×15 + Transformation Paradox)
- §2ter v3.9 « Maturité agentique et bottlenecks 2026 » (McKinsey State of AI Trust 23/74/72)
- Sous-encarts v3.11 (McKinsey State of AI 2025 88/39/23-39/32-43-13 + Stanford 53/172 Md$/88/4 sur 5 étudiants)

→ La transposition pr-04.md doit **distinguer narrativement les 3 séries de chiffres** plutôt que les agréger en un mur de pourcentages. **Recommandation D-026** : si tu produis pr-04.md en vague 4, sonde-moi sur l'ordre canonique des 3 séries avant production.

### Bonus 2 — PR-01 typologie 4 profils + high performers

**Risque modéré** d'asymétrie entre :
- **Typologie 4 profils dirigeants Bpifrance** (v3.10) — Sceptiques 27 / Bloqués 26 / Expérimentateurs 19 / Innovateurs 28 %
- **High performers McKinsey 6 % + 3,6× transformation + 3× workflow redesign** (v3.11)

→ Ces 2 grilles **se complètent** mais ne se substituent pas (typologie sociologique vs typologie performance). Préserver les 2 dans pr-01.md en clarifiant qu'elles **mesurent des dimensions différentes** (mindset/maturité vs résultats EBIT). Risque de confusion lecteur identique au Passage 2.2 (4 patterns vs 7 dimensions).

### Bonus 3 — DEP-08 + PR-05 encart symétrique « 362 incidents »

**Risque faible mais à signaler** : si transposition stricte symétrique, **risque de duplication textuelle** entre dep-08.md et pr-05.md. Mon arbitrage : la symétrie HTML est **intentionnelle** (chiffre macro identique cité dans 2 modules avec angles différents). Préserver la symétrie mais avec **angle distinct** :
- DEP-08 : angle technique (incidents = vecteurs d'attaque DEP-08 §1.2 + cohérence SBOM IA §7bis)
- PR-05 : angle stratégique (incidents = signal de risque pour cadrage projet)

### Bonus 4 — DEP-01 Jagged Frontier Stanford

**Risque modéré** sur la transposition pédagogique du concept « jagged frontier » qui est **nouveau pour les lecteurs PME**. Chiffres canoniques à préserver textuellement :
- **Gemini Deep Think médaille d'or à l'IMO** vs **lit horloge analogique correctement 50,1 % du temps**
- **OSWorld : 12 % → 66 % task success en un an** (mais **1 échec sur 3 reste**)

Le contraste pédagogique « médaille d'or IMO vs horloge analogique 50 % » est le cœur du message — à transposer **textuellement avec les 2 chiffres adjacents** dans la même phrase. Risque de dérive si on transpose isolément « médaille d'or IMO » d'un côté et « 50,1 % horloge » de l'autre.

### Bonus 5 — DEP-05 §8.5 + §8.5bis

**Risque faible** : déjà cohérent avec stack §8.1-8.4 v3.9. Mais sujet pointu sécurité agents (failure receipt + harness long-running) → si production MD vague 4, **sonder préalablement** sur le pattern « two-agent harness initializer/coding » qui est complexe à vulgariser.

---

## Synthèse opérationnelle pour le couple 2

**Actions recommandées avant production vague 4** :

1. **PR-08** : ne **PAS** créer de wikilink artificiel vers PR-07 (non explicite côté HTML). Pas de cas-école PME nommé à inventer.
2. **CU-026 §3bis** : préserver la section H2 dédiée (pas sous-section H3). Distinction explicite « 4 patterns ≠ 7 dimensions » à maintenir comme on l'avait fait pour « 7 dimensions ≠ 8 questions auto-diag ».
3. **DEP-02 tableau de décision** : **NE PAS** modifier le tableau principal §4 (5 lignes par volume corpus inchangées). La nouvelle ligne « agent avec mémoire conversationnelle » est dans un **mini-tableau distinct §2bis**.
4. **Extraction transverse `pattern-persistent-memory.md`** : OUI recommandée (D-025 satisfait, symétrique à pattern-llm-wiki).
5. **Passages bonus** : 5 risques à anticiper sur PR-04 (3 séries chiffres), PR-01 (2 typologies), DEP-08+PR-05 (symétrie intentionnelle), DEP-01 (jagged frontier pédagogique), DEP-05 (sujet pointu vulgarisation).

**Volume produit** : ~2700 mots — dans la cible 2000-3000 mots du sondage.

**Charge cognitive Cowork Hub IA** : ~60 min (relecture de 3 modules HTML + structuration des réponses + identification de 5 passages bonus). Conforme à l'estimation 50-75 min du sondage.

**Pattern D-026 confirmé efficace** — 2e exercice consécutif évite plusieurs dérives sémantiques sur des modules denses. À conduire systématiquement pour vague 5+ contenant des modules N3/N4 nouveaux ou enrichis.

**À ta dispo** pour clarifier un point spécifique avant production, ou pour un second sondage léger si la transposition révèle un nouveau passage à risque sur les 5 passages bonus.

---

*Retour sondage produit le 19 mai 2026 par Cowork Hub IA. Deuxième exercice du pattern D-026 — calibrage qualitatif post-S2.3.*

— Cowork Hub IA
