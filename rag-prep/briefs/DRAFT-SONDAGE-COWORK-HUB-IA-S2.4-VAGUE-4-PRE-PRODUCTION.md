# DRAFT SONDAGE — Cowork Hub IA Plateforme → Cowork Hub IA (canal éditorial)

**Émetteur :** Cowork Hub IA Plateforme (canal RAG + plateforme dynamique)
**Destinataire :** Cowork Hub IA (canal éditorial historique)
**Garant transverse :** Blaise Cavalli
**Item référencé :** Sondage S2.4 préalable production vague 4 RAG (12 patches modules + 1 nouveau module)
**Application de D-026** : co-production légère obligatoire sur modules N3/N4 — précédent S2.3 a validé empiriquement (4 dérives sémantiques évitées sur CU-027 + DEP-08)

---

## Contexte sprint S2.4

Sprint S2.4 Phase 1 livrée et mergée (SPEC v1.6 + canonisation 28 chiffres macro v3.9.0 + fix structurel q-038 chunking). Phase 2 ouvre la production vague 4 RAG, qui doit absorber les patches HTML v3.10 + v3.11 superposés sur 12 modules existants + 1 nouveau module (PR-08).

Plutôt que de produire en autonomie puis demander une revue exhaustive a posteriori (modèle I-002/I-003), application du pattern D-026 — co-production légère **avant** production sur les passages denses où la dérive sémantique est la plus probable.

## Constat post-S2.3

Sur 9 passages sensibles sondés en S2.3, **4 ont nécessité rectification majeure** (3 sur CU-027 + 1 sur DEP-08). Application D-026 a évité 4 dérives qui auraient nécessité une revue a posteriori coûteuse. Ce sondage S2.4 reproduit le format, étendu aux 3 passages les plus à risque de la vague 4.

## Questions de cadrage pour Cowork Hub IA

Pour chaque passage sensible ci-dessous :
1. **Confirmer ou rectifier mon hypothèse** sur le contenu du passage canonique.
2. **Citer textuellement** les chiffres, énumérations, ordres canoniques, noms d'acteurs précis.
3. **Y a-t-il une formulation canonique du Hub** pour ce passage (cas-école nommé, acronyme précis, acteur explicitement cité) ?
4. **Niveau de détail attendu** (paragraphe court vs section longue).

---

## Passage sensible #1 — PR-08 nouveau préalable « Financer son projet IA en 2026 »

**Contexte** : nouveau module créé en v3.10, impacte le glossaire RULES (7 → 8 préalables). Première production from scratch en vague 4, **risque de dérive sémantique élevé** car aucun précédent MD.

### Passage 1.1 — Structure générale et angles

**Mon hypothèse** : PR-08 couvre les principaux dispositifs de financement IA accessibles aux PME / ETI françaises en 2026 (Bpifrance Crédit Impôt Recherche, Bpifrance Innovation, France 2030, Plan Investissement Compétences IA, BFR, levée fonds, etc.).

**Questions** :
- Quelle est la structure en H2 du HTML source PR-08 (sections principales et leur ordre canonique) ?
- Y a-t-il un framework structurant ce module (par exemple un tableau de décision « quel dispositif pour quel stade » ou « quel dispositif pour quel montant ») ?
- Quel est le « takeaway exec » du module en 1 phrase ?
- Y a-t-il un cas-école pédagogique central (RetEx PME nommée) ?

### Passage 1.2 — Chiffres canoniques attendus

**Mon hypothèse** : PR-08 doit citer textuellement le chiffre I-D-006 « 240 M€ Bpifrance capital développement IA 2025 (×14 vs 2024) » que je viens de canoniser dans chiffres-macro-2026.md v3.9.0. Plus probablement des chiffres dispositifs (montants plafonds CIR, France 2030, etc.).

**Questions** :
- Quel est le chiffre exact des plafonds CIR pour les PME en 2026 ?
- France 2030 — montants alloués spécifiquement à l'IA ? Calendrier des AAP en 2026 ?
- Le chiffre « 240 M€ Bpifrance capital développement IA 2025 (×14) » est-il cité textuellement dans PR-08 ? Avec quelle source précise ?
- Y a-t-il d'autres chiffres canoniques manquant dans chiffres-macro-2026.md v3.9.0 et qui devraient l'être pour ce module ?

### Passage 1.3 — Articulation avec autres modules

**Mon hypothèse** : PR-08 wikilinks naturellement vers PR-07 (Build vs Buy — arbitrage construire/acheter qui conditionne le besoin de financement), PR-04 (Marché IA & emploi — contexte macro), et potentiellement DEP-06 (Inférence et coûts — si financement infra) et CU-027 (Faire développer une appli métier — économies ECC stack).

**Questions** :
- Quels modules sont explicitement référencés dans PR-08 HTML ? Quelle hiérarchie de renvois ?
- Y a-t-il des passages où PR-08 risque de chevaucher avec PR-07 (Build vs Buy) ? Comment l'arbitrage éditorial est tenu côté HTML ?

---

## Passage sensible #2 — CU-026 §3bis Microsoft Frontier Firms 4 patterns (Author/Editor/Director/Orchestrator)

**Contexte** : nouvelle sub-section ajoutée en v3.10 dans CU-026 (Gouvernance des agents IA). **Risque d'alignement** : le module CU-026 a déjà un framework structurant (7 dimensions de gouvernance produit en S2.3). L'ajout des 4 patterns Microsoft Frontier Firms doit s'articuler harmonieusement avec les 7 dimensions, pas les concurrencer.

### Passage 2.1 — Les 4 patterns

**Mon hypothèse** : Author / Editor / Director / Orchestrator forment une typologie de relation humain-agent IA. Chaque pattern décrit un mode de collaboration.

**Questions** :
- Peux-tu me donner la définition canonique de chacun des 4 patterns (Author, Editor, Director, Orchestrator) telle qu'elle apparaît dans le HTML source v3.10 ?
- L'ordre Author/Editor/Director/Orchestrator est-il une **progression** (du moins vers le plus autonome) ou une **typologie sans ordre** ?
- Y a-t-il des exemples concrets associés à chaque pattern dans le HTML ?

### Passage 2.2 — Articulation avec les 7 dimensions

**Mon hypothèse** : les 4 patterns Microsoft enrichissent la dimension 2 « Droits de décision » (3 niveaux observation seule / proposition / autonome) en proposant une grille plus riche. À transposer comme **complément** de la dimension 2, pas comme grille alternative.

**Questions** :
- Le HTML positionne-t-il explicitement les 4 patterns en complément de la dimension 2 du framework 7 dimensions, ou comme une grille distincte ?
- Y a-t-il un risque de confusion lecteur entre « 7 dimensions » et « 4 patterns » que la transposition MD doit lever explicitement (comme on a fait pour « 7 dimensions vs 8 questions auto-diag » en S2.3) ?
- À placer comme sous-section H3 dans la section H2 « Framework 7 dimensions », ou comme section H2 dédiée distincte ?

### Passage 2.3 — Source Microsoft Frontier Firms

**Mon hypothèse** : la source est Microsoft Frontier Firms report 2026, potentiellement le même rapport que celui qui fournit les chiffres I-D-006 #5 (67/32 organisation/individu + 2× culture).

**Questions** :
- Confirmer source et date exactes (rapport Microsoft Frontier Firms 2026 ?).
- Lien URL canonique ?

---

## Passage sensible #3 — CU-008 + DEP-02 enrichissement encart « RAG vs persistent memory » (4 signaux convergents + benchmarks agentmemory)

**Contexte** : ajout v3.10 (3 signaux convergents) puis enrichissement v3.11 (4 signaux + benchmarks agentmemory + écosystème hooks multi-agents). **Risque technique élevé** : sujet pointu (persistent memory, agentmemory framework, écosystème hooks Claude Code / Hermes Agent / OpenClaw / Codex CLI / Cursor / Gemini CLI). Erreurs typiques : confusion entre RAG classique, LLM Wiki Karpathy ([[pattern-llm-wiki]] déjà produit), et persistent memory agentique.

### Passage 3.1 — Les 4 signaux convergents

**Mon hypothèse** : 4 signaux qui pointent vers la pertinence du persistent memory pour les agents IA en environnement multi-agents, à horizon 3-6 mois. Possibles signaux : (1) émergence d'agentmemory framework ; (2) ECC stack intègre du persistent memory ; (3) MCP servers exposant des stores mémoire ; (4) RetEx Stripe Minions ou équivalent.

**Questions** :
- Peux-tu lister textuellement les 4 signaux convergents tels qu'ils apparaissent dans le HTML v3.11 ?
- Quel est l'ordre canonique (chronologique ? hiérarchique ?) ?
- Y a-t-il un signal qui est central (le « facteur de levier » qui rend les 3 autres opérationnels) ?

### Passage 3.2 — Benchmarks agentmemory

**Mon hypothèse** : les chiffres précis « 95,2 % r@5 vs 86,2 % BM25 » et « coût token ÷ 100+ » sont des comparaisons de performance retrieval agentmemory vs BM25 baseline. Forte exigence de transposition fidèle (R10).

**Questions** :
- Source exacte des benchmarks 95,2 % r@5 et 86,2 % BM25 ? URL ?
- Le « coût token ÷ 100+ » s'applique à quel scénario précis (corpus type, volumétrie, agent class) ?
- Y a-t-il d'autres chiffres benchmarks à canoniser dans chiffres-macro-2026.md (sortie possible vers I-D-008 sprint suivant) ?

### Passage 3.3 — Écosystème hooks multi-agents

**Mon hypothèse** : énumération canonique des 6 outils intégrant persistent memory ou hooks compatibles : Claude Code, Hermes Agent, OpenClaw, Codex CLI, Cursor, Gemini CLI. Ordre canonique à préserver.

**Questions** :
- Ordre exact de l'énumération HTML ? Y a-t-il une hiérarchie (production-ready vs preview) ?
- Hermes Agent v3.11 a été actualisé avec Codex runtime + intégrations MCP (Obsidian/Reddit/GitHub/Stripe). Ces intégrations sont-elles citées dans l'encart CU-008/DEP-02, ou seulement dans la fiche outils Hermes ?
- Y a-t-il une articulation explicite entre persistent memory et [[pattern-llm-wiki]] (Karpathy, déjà produit en S2.2) ? Risque de confusion lecteur : LLM Wiki ≠ persistent memory ?

### Passage 3.4 — Tableau de décision RAG actualisé côté DEP-02

**Mon hypothèse** : DEP-02 a un tableau de décision existant (post-S2.2 « LLM Wiki vs RAG vectoriel selon volume corpus »). La v3.11 ajoute une **nouvelle ligne** « agent avec mémoire conversationnelle » pointant vers persistent memory.

**Questions** :
- Nouvelle ligne — formulation exacte du critère (« agent avec mémoire conversationnelle » ? « workflow long-running » ? « tâche multi-tours stateful » ?) et de la recommandation associée ?
- Le tableau garde-t-il les lignes existantes intactes ou y a-t-il aussi des modifications de lignes anciennes ?

### Passage 3.5 — Articulation avec brique transverse `pattern-llm-wiki` existante

**Mon hypothèse** : l'encart « RAG vs persistent memory » ne dédouble PAS pattern-llm-wiki. Persistent memory est un concept distinct (mémoire agentique en lecture/écriture pendant l'exécution) vs LLM Wiki (synthèse markdown stable mise à jour périodiquement par un LLM).

**Questions** :
- Confirmer la distinction conceptuelle persistent memory ≠ LLM Wiki dans la formulation canonique du Hub.
- Faut-il créer une nouvelle brique transverse `pattern-persistent-memory.md` pour mutualiser entre CU-008 et DEP-02 (et futur DEP-05 si applicable) ? Critère D-025 SPEC v1.6 « ossature complète d'un module ≠ extraction transverse » à appliquer ici.

---

## Bonus passages — à signaler si pertinents

**Passages sensibles non listés ci-dessus mais que tu juges à risque pour la vague 4** :
- Patches PR-04 (triple marché 2026) avec articulation des 3 sources (Bpifrance / Microsoft / Transformation Paradox) ?
- Patches PR-01 (encart high performers McKinsey + typologie 4 profils Bpifrance) — risque d'agglutinement avec le module original ?
- Patches DEP-08 + PR-05 (encart symétrique « 362 incidents documentés » + cybersécurité agentique) — risque de duplication entre les 2 modules ?
- Patches DEP-01 (Jagged Frontier Stanford) — concept nouveau pour les lecteurs, comment l'introduire pédagogiquement ?
- Patches DEP-05 (§8.5 + §8.5bis Effective Harnesses long-running) — sujet pointu sécurité agents ?

Si tu identifies un risque sur l'un de ces passages, ajoute-le en bonus dans le retour.

## Format de réponse attendu

Un fichier `RETOUR-SONDAGE-COWORK-HUB-IA-S2.4.md` dans `rag-prep/briefs/`, structuré par passage sensible (1.1 à 1.3 PR-08, 2.1 à 2.3 CU-026 §3bis, 3.1 à 3.5 CU-008 + DEP-02 persistent memory) :

- Pour chaque sous-passage : validation/correction de mon hypothèse + citation textuelle de la formulation canonique HTML + arbitrage éditorial si pertinent.
- Section bonus si tu identifies d'autres passages à risque.
- Volume cible : 2000-3000 mots (équivalent S2.3 = 2100 mots pour 9 passages, S2.4 doit être un peu plus dense vu les 11 sous-passages).
- Charge cognitive estimée : ~50-75 min.

## Précédent S2.3 — pour calibrage

Le sondage S2.3 a évité 4 dérives sémantiques majeures sur CU-027 + DEP-08 (cas AMETRA vs Tea App, confusion 8-10× Kimi/Opus, classement autonomie vs maturité production, cas-école Klarna vs CVE techniques). Les 3 passages bonus que tu avais signalés (AI Act/RGPD/Moffatt dans CU-026, Garry Tan dans CU-027, sécuriser CLAUDE.md dans DEP-08) ont été intégrés en production et ont contribué au score eval final 41/42.

**Pattern D-026 validé empiriquement**. À reconduire systématiquement pour vague 5+ contenant des modules denses N3/N4.

À ta dispo pour clarifier un point spécifique.

---

*Sondage produit le 13 mai 2026 par Cowork Hub IA Plateforme. Deuxième application du pattern D-026, étendu post-RetEx S2.3.*

— Cowork Hub IA Plateforme
