# DECISIONS-RAG.md — Registre des décisions structurantes

**Statut :** Initial (S0)
**Dernière mise à jour :** 11 mai 2026

> **Rôle de ce fichier :** registre ADR (Architecture Decision Records) léger. Chaque décision structurante est consignée ici avec : contexte, options considérées, décision prise, conséquences. Une fois consignée, la décision fait foi. Toute remise en cause exige une nouvelle entrée qui supersède la précédente (statut "Remplacée par #X").

---

## Index des décisions

| # | Date | Titre | Statut |
|---|---|---|---|
| D-001 | 11 mai 2026 | Architecture à 2 couches HTML/MD complémentaires | Actée |
| D-002 | 11 mai 2026 | Repo unique `hub-ia` avec dossier `rag/` séparé | Actée |
| D-003 | 11 mai 2026 | Architecture à 4 canaux (couple 1 éditorial + couple 2 plateforme) | Actée |
| D-004 | 11 mai 2026 | Scénario B → A : pas de bascule de source de vérité, MD parallèle au HTML | Actée (en remplacement d'une décision intermédiaire) |
| D-005 | 11 mai 2026 | LLM de génération : Claude Sonnet 4.6 principal + Haiku 4.5 pour résumés/classif | Actée |
| D-006 | 11 mai 2026 | Vector DB : ChromaDB local d'abord (gratuit, simple, migrable) | Actée |
| D-007 | 11 mai 2026 | Embeddings : OpenAI text-embedding-3-small (Phase 1) | Actée |
| D-008 | 11 mai 2026 | Backend : Cloudflare Workers (gratuit 100k req/jour, déployable EU) | Actée |
| D-009 | 11 mai 2026 | Schéma frontmatter YAML : 10 champs canoniques (cf. SPEC-MD-POUR-RAG) | Actée |
| D-010 | 11 mai 2026 | Wikilinks : syntaxe Obsidian `[[code]]` ou `[[code\|alias]]` | Actée |
| D-011 | 11 mai 2026 | Chunking : section h2 = chunk principal (~400-700 tokens), h3 subdivisable si > 800 | Actée |
| D-012 | 11 mai 2026 | MCP Obsidian côté Claude Code Plateforme uniquement (pas côté Cowork) | **Reportée à Phase 2** (révision 12 mai) |
| D-013 | 11 mai 2026 | Plafonds API : Anthropic 50 $/mois (alerte 30), OpenAI 10 $/mois (alerte 5) | Actée |
| D-014 | 11 mai 2026 | Nommage MD : `{type}-{numero}.md` ; fiches outils regroupées par catégorie | Actée |
| D-015 | — | Structure du `SYNC-INTER-CANAUX.md` | À acter en production |
| D-016 | 11 mai 2026 | Audit-md-rag.py automatisé dès S1 | Actée |
| D-017 | 11 mai 2026 | Référence canonique MD : `cu-008.md` produit en pilote S1 | Actée |
| D-018 | 11 mai 2026 | Procédure de resync git systématique en début de session | Actée |
| D-019 | 11 mai 2026 | Cartographie d'ancrage RAG distincte (angles thématiques par chunk) | Actée |
| D-020 | 11 mai 2026 | Pas de référence temporelle absolue dans briefs et conventions (sauf hackathon) | Actée |
| D-021 | 11 mai 2026 | Discipline de concision des briefs (cible max ~2000 mots) | Actée |
| D-022 | 11 mai 2026 | Spécialisation rôles couple 2 : Cowork = matière MD, Claude Code = code RAG | Actée |
| D-023 | 11 mai 2026 | Principe « nouvelle règle = nouvelle fonction d'audit » codifié dès v1 (issu retour couple 1 sur I-001) | Actée |
| D-024 | 11 mai 2026 | Architecture de circulation Cowork ↔ Git ↔ Claude Code : `rag-prep/` ascendant Cowork + `rag-prep/` partagé sur Git + Option D rebaselining | Actée |
| D-025 | 11 mai 2026 | Pattern architectural « unité = module + extraction sélective de briques transverses » (issue revue I-002 Q7) | Actée |
| D-026 | 12 mai 2026 | Co-production légère obligatoire avec Cowork Hub IA sur modules N3/N4 (sondage AVANT production sur passages sensibles) — issue revue I-003 Q5 | Actée |
| D-027 | 12 mai 2026 | Convention de nommage des branches Claude Code Plateforme : `claude/execute-{slug}-{hash}` accepté par défaut, pas de rename imposé | Actée |
| D-012-bis | 12 mai 2026 | MCP Obsidian reporté à Phase 2 (gain marginal en Phase 1, valeur réelle en LLM Wiki layer) | Actée |

---

## D-001 — Architecture à 2 couches HTML/MD complémentaires

**Date :** 11 mai 2026
**Statut :** Actée

**Contexte :** le Hub IA Learning Center est aujourd'hui un site GitHub Pages servant du HTML. Pour le RAG, il faut un format optimisé indexation/retrieval. Question : conserver HTML comme source de vérité unique, basculer en MD source de vérité avec HTML généré, ou maintenir deux représentations parallèles.

**Décision :** maintenir **deux couches complémentaires non équivalentes** :
- Couche HTML pédagogique pour le site (produite par couple 1, inchangée)
- Couche MD fonctionnelle pour le RAG (produite par couple 2)

Les fichiers MD ne sont pas une conversion du HTML. Ce sont des œuvres parallèles distillées et optimisées pour l'usage RAG.

**Conséquences :**
- Aucune disruption du couple 1 (production éditoriale inchangée)
- Pas de site generator à mettre en place
- Discipline de coordination requise entre les deux couples pour synchroniser les productions
- Le couple 2 produit ses MD à partir du contenu HTML existant **et** des briefs des nouvelles productions du couple 1
- Évolution Phase 2 LLM Wiki préservée

**Trace :** échanges Cowork Hub IA Plateforme — 11 mai 2026.

---

## D-002 — Repo unique `hub-ia` avec dossier `rag/` séparé

**Date :** 11 mai 2026
**Statut :** Actée

**Contexte :** où héberger le code RAG, les fichiers MD du vault, le pipeline d'ingestion, le widget ? Options : repo séparé `hub-ia-rag`, ou intégration dans le repo `hub-ia` existant.

**Décision :** **repo unique `hub-ia`** avec un dossier `rag/` dédié contenant `content/` (vault MD), `code/` (pipeline et widget), `eval/` (golden set), `README.md`.

**Conséquences :**
- Les deux couches cohabitent dans le même repo
- Le `.gitignore` doit être ajusté pour exclure : vector store local, .env, caches, builds intermédiaires
- Le code RAG ne touche jamais aux fichiers HTML du site
- Les deux couples opèrent dans le même repo mais sur des chemins distincts
- Possibilité d'évolution future : extraire `rag/` dans un repo dédié si la complexité l'exige

**Trace :** demande explicite de Blaise — 11 mai 2026.

---

## D-003 — Architecture à 4 canaux

**Date :** 11 mai 2026
**Statut :** Actée

**Contexte :** division du travail entre stratégie/cadrage (Cowork) et exécution (Claude Code), appliquée à deux périmètres distincts (production éditoriale et développement plateforme RAG).

**Décision :** architecture à 4 canaux Cowork :
- **Couple 1** : Cowork Hub IA (existant) + Claude Code Hub IA (existant) → contenu et site
- **Couple 2** : Cowork Hub IA Plateforme (existant) + Claude Code Hub IA Plateforme (à créer en S1) → RAG et plateforme

**Conséquences :**
- Blaise est garant transverse de la cohérence inter-canaux
- Procédures de sync définies intra-couple (4 fichiers de référence) et inter-couples (`SYNC-INTER-CANAUX.md`)
- RetEx du couple 1 sollicité pour aligner les bonnes pratiques

**Trace :** demande explicite de Blaise — 11 mai 2026.

---

## D-004 — Pas de bascule de source de vérité

**Date :** 11 mai 2026
**Statut :** Actée (remplace une intention temporaire de bascule vers MD-first)

**Contexte :** une option envisagée brièvement consistait à basculer la source de vérité du Hub vers le MD, avec HTML généré via site generator. Blaise a clarifié qu'il fallait conserver le fonctionnement actuel (HTML hébergé sur Git, servi par GitHub Pages).

**Décision :** le HTML reste la source de vérité du site. Le MD est une représentation parallèle dédiée au RAG. Pas de site generator.

**Conséquences :**
- Toutes les implications "site generator" écartées
- Plan d'action allégé de ~2 sprints
- Couple 1 totalement inchangé dans son mode de fonctionnement

**Trace :** clarification explicite de Blaise — 11 mai 2026.

---

## D-005 à D-014 — Décisions techniques de Phase 1

**Date :** 11 mai 2026
**Statut :** Toutes Actées (bloc consolidé)
**Validation :** Blaise — bloc validé en intégralité sur recommandations Cowork le 11 mai 2026

**Contexte :** clôture du sprint S0, choix techniques nécessaires au démarrage opérationnel du pipeline RAG. Recommandations Cowork formulées sur la base de (a) le panorama natif du Hub IA (CU-008, DEP-02), (b) les contraintes budget < 100 €/mois et zéro compétence IT en revue, (c) les exigences d'évolutivité et de souveraineté EU minimale.

### D-005 — LLM de génération
**Choix :** Claude Sonnet 4.6 (API Anthropic, EU disponible) comme modèle principal. Claude Haiku 4.5 utilisé pour tâches simples (résumés, classification, reformulation).
**Justification :** Sonnet 4.6 excellent sur la nuance et le résumé (panorama CU-008). Haiku 4.5 ~10× moins cher pour les tâches sans enjeu de nuance, permet d'allonger la durée du budget API.
**Conséquence :** le pipeline backend doit router selon la nature de la tâche. Documenté dans `SPEC-MD-POUR-RAG.md`.

### D-006 — Vector DB
**Choix :** ChromaDB en mode local (embarqué dans le service Cloudflare Workers via duckdb-wasm ou via Supabase pgvector si volume justifie).
**Justification :** recommandation native CU-008 — "ChromaDB est le choix le plus simple pour un prototype". Gratuit, performance suffisante pour 145 unités × ~5 chunks moyens = ~750 vecteurs. Migrable vers Pinecone serverless en Phase 2 si besoin.
**Conséquence :** code Python d'indexation simple, pas de gestion d'infrastructure managée.

### D-007 — Embeddings
**Choix :** OpenAI text-embedding-3-small. Mistral Embed reconsidéré en Phase 2 si exigence souveraineté renforcée.
**Justification :** référence robuste, ~0,02 $/M tokens. Pour un corpus ~400k tokens, indexation initiale ~0,01 $. Re-indexation incrémentale négligeable. Hébergement OpenAI US toléré en Phase 1 pour POC (contenu Hub déjà public sur GitHub).
**Conséquence :** dépendance API OpenAI ajoutée au plafond budgétaire (cf. D-013).

### D-008 — Backend
**Choix :** Cloudflare Workers (free tier 100k req/jour, hébergement EU disponible, latence faible). Vercel Edge en backup si limites Cloudflare atteintes.
**Justification :** gratuit jusqu'à un volume largement supérieur à un POC. Stockage de petites données possible via Cloudflare KV ou D1. Compatible Anthropic SDK et OpenAI SDK en TypeScript.
**Conséquence :** stack 100 % TypeScript/JavaScript côté serveur (sauf script Python d'ingestion qui tourne en build-time, pas en runtime).

### D-009 — Schéma frontmatter YAML
**Choix :** 10 champs canoniques par fichier MD. Détail dans `SPEC-MD-POUR-RAG.md`. Synthèse :
```yaml
code: cu-008
titre: "Knowledge base interne (RAG)"
type: module-cu  # module-cu | prealable-pr | deploiement-dep | architecture | fiche-outil | transverse
axe: B  # A | B | C | D | E | agentique | transverse
niveau: 3  # 1 | 2 | 3 | 4
tags: [rag, llm-wiki, retrieval, embeddings]
version: 3.8.2
last_updated: 2026-05-11
glosaire_termes: [rag, fine-tuning, embedding, vector-db]
derives: ["[[dep-02]]", "[[pr-07]]"]
public_cible: [dirigeant, ops, r&d]
```
**Justification :** couvre filtrage par profil, scoring de pertinence, citation, versioning, navigation Phase 2 LLM Wiki.
**Conséquence :** tout fichier MD du vault DOIT contenir ce frontmatter. Audit-md-rag.py vérifie la présence et la complétude.

### D-010 — Wikilinks
**Choix :** syntaxe Obsidian native `[[cu-008]]` (cible = code module) ou `[[cu-008|Knowledge base RAG]]` (avec alias).
**Justification :** standard Obsidian, MCP-compatible, lisible humain, parseable trivialement.
**Conséquence :** les hyperliens HTML internes (`<a href="cu-008.html">`) du Hub sont transposés en wikilinks dans les MD. Cross-links vers ressources externes restent en MD standard `[text](url)`.

### D-011 — Convention de chunking
**Choix :** section h2 = chunk principal, longueur cible 400-700 tokens. Si une section dépasse 800 tokens, subdiviser par h3 (chaque h3 devient un sous-chunk). Frontmatter du fichier injecté en tête de chaque chunk pour préserver le contexte métadonnées.
**Justification :** autonomie sémantique (chaque chunk lisible isolément), retrieval précis, alignement DEP-02.
**Conséquence :** la rédaction MD doit produire des sections h2 sémantiquement autonomes. C'est une discipline éditoriale, pas un post-traitement automatique.

### D-012 — MCP Obsidian
**Choix :** installation MCP Obsidian côté Claude Code Plateforme uniquement (pas côté Cowork — j'accède aux MD via filesystem).
**Justification :** permet à Claude Code Plateforme d'éditer le vault de manière atomique (création de notes, mise à jour de frontmatter, gestion de wikilinks). Côté Cowork, le bénéfice marginal ne justifie pas la complexité de configuration additionnelle.
**Conséquence :** la configuration MCP fait partie du livrable S1 du Claude Code Plateforme.

### D-013 — Plafonds API
**Choix :** Anthropic 50 $/mois (cap dur, alerte à 30 $), OpenAI 10 $/mois (cap dur, alerte à 5 $). Plafonds configurés au niveau dashboard de chaque provider, **pas dans le code**.
**Justification :** protection budgétaire stricte sans gêne opérationnelle (volume estimé S1-S4 très inférieur). Si dépassement → blocage automatique côté provider.
**Conséquence :** monitoring usage à intégrer dans le rapport mission Claude Code (mention du coût accumulé estimé en fin de sprint).

### D-014 — Convention de nommage MD
**Choix :** `{type}-{numero}.md` pour les unités numérotées (`cu-008.md`, `pr-01.md`, `dep-02.md`, `a1.md`). Fiches outils regroupées par catégorie : `outils-vector-db.md`, `outils-llm-gateway.md`, `outils-embeddings.md`, etc. (pas un fichier par fiche outil — sinon 99 fichiers minuscules surcompartimentés).
**Justification :** aligné sur les codes existants du Hub (modules CU, préalables PR), simple et prévisible. Pour les fiches outils, regroupement par catégorie évite la dilution du retrieval (un chunk = une catégorie d'outils, plus utile qu'un chunk = un outil isolé).
**Conséquence :** ~50-60 fichiers MD au final (27 CU + 7 PR + 8 DEP + 5 archi + ~15 catégories d'outils + glossaire + brain pages transverses), bien plus gérable que 145 fichiers isolés.

---

## D-016 — Audit-md-rag.py automatisé dès S1

**Date :** 11 mai 2026
**Statut :** Actée

**Contexte :** RetEx couple 1 Q2 §1 + Q4 §3 — l'audit automatisé (audit-global.py côté Hub IA) est identifié comme le "levier d'invariant le plus puissant du dispositif". Sans lui, les règles éditoriales restent descriptives et inégalement appliquées. Avec lui, elles deviennent prescriptives et exécutoires. Recommandation explicite : le créer dès le départ, pas après 12 PRs correctives.

**Décision :** dès S1, le canal Claude Code Plateforme produira un script `audit-md-rag.py` qui valide automatiquement la conformité des fichiers MD à `SPEC-MD-POUR-RAG.md` (frontmatter présent et complet, sections h2 sémantiquement autonomes, wikilinks valides, longueur de chunk dans la fourchette cible, glossaire référencé, etc.). Démarrer avec 5-10 règles, en ajouter au fil des écarts détectés (leçon Q3 §3 : ne pas anticiper un cadre exhaustif).

**Conséquences :**
- Discipline de "shift left" : les écarts sont détectés en amont du merge, pas en post-PR
- Coût initial : ~1 jour de dev Claude Code en S1
- Bénéfice : élimination de la régression sur le format MD au fil des productions

**Trace :** RetEx couple 1 — Q2 §1, Q3 §3, Q4 §3.

---

## D-017 — Référence canonique MD à identifier dès S1

**Date :** 11 mai 2026
**Statut :** À acter S1 (proposition Cowork)

**Contexte :** RetEx couple 1 Q2 §3 — `modules/cu-008-knowledge-base-rag.html` est utilisé côté couple 1 comme référence canonique. Quand une consigne est ambiguë, Claude Code regarde ce fichier et reproduit son pattern. Réduit énormément les divergences. Recommandation explicite : "identifier dès le départ un fichier de référence à copier plutôt que des consignes abstraites".

**Décision :** dès le S1 pilote, on identifie un fichier MD modèle qui servira de référence canonique pour tous les autres. Proposition Cowork (à valider Blaise) : utiliser **CU-008 (Knowledge base RAG) en version MD optimisée RAG** comme référence canonique, pour double raison : (a) densité moyenne donc bon échantillon, (b) méta-récursivité (le module pédagogique sur le RAG sert de référence canonique au RAG lui-même).

**Conséquences :**
- Le pilote S1 inclura la production particulièrement soignée de cu-008.md
- Tous les autres fichiers MD du vault devront s'aligner sur ce pattern
- En cas d'évolution du pattern (raffinement Phase 2), cu-008.md sera mis à jour en premier puis le reste réaligné

**Trace :** RetEx couple 1 — Q2 §3, Q4 §1.

---

## D-018 — Procédure de resync git systématique en début de session

**Date :** 11 mai 2026
**Statut :** Actée

**Contexte :** RetEx couple 1 Q3 §2 — "erreur de coordination majeure" : préparation d'une v3.7.1 alors que Claude Code en était déjà à v3.7.13 sur main (12 PRs non détectées). Cause racine : pas de rituel post-merge pour resync le clone local. Recommandation explicite : "codifier ce rituel dès le jour 1".

**Décision :** procédure ajoutée au protocole boot des sessions Cowork et Claude Code Plateforme : avant toute lecture des fichiers de référence, exécuter `git fetch && git status`. Si désynchro détectée (commits derrière origin/main), faire `git reset --hard origin/main` après confirmation Blaise. Cette discipline est inscrite dans `_instructions-rag.md` v1.

**Conséquences :**
- Aucune session ne démarre sur un état repo obsolète
- Réduit drastiquement le risque de produire des artefacts qui contredisent un état actuel inconnu
- Pour Cowork : opération via Bash en début de session sur le dossier monté

**Trace :** RetEx couple 1 — Q3 §2, Q4 §2.

---

## D-019 — Cartographie d'ancrage RAG distincte

**Date :** 11 mai 2026
**Statut :** Actée

**Contexte :** RetEx couple 1 Q3 §4 — la cartographie d'ancrage Hub IA listait initialement les modules mais pas les angles thématiques traités dans chaque module, conduisant la veille à proposer des doublons. Recommandation explicite couple 1 : "votre cartographie RAG doit lister non seulement les modules indexés, mais aussi les angles thématiques couverts dans chaque module, pour éviter les doublons d'indexation".

**Décision :** création d'un fichier `cartographie-rag.md` dans `Canaux/Hub-IA-Plateforme/` qui inventorie, par fichier MD du vault `rag/content/`, les 3-5 angles thématiques principaux qu'il couvre. Mis à jour à chaque production MD. Lu par Cowork avant chaque nouvelle production de MD pour éviter doublons.

**Conséquences :**
- Permet d'éviter qu'un même angle soit indexé plusieurs fois dans des chunks différents
- Sert de référentiel d'ancrage croisé avec `cartographie-hub-ia.md` du couple 1
- Maintenance légère mais discipline obligatoire

**Trace :** RetEx couple 1 — Q3 §4, Q4 §4.

---

## D-020 — Pas de référence temporelle absolue dans briefs et conventions

**Date :** 11 mai 2026
**Statut :** Actée

**Contexte :** RetEx couple 1 Q3 §5 — Cowork couple 1 proposait des "v3.7.1 dans 10 jours" sans considération de la bande passante Blaise ni des limites d'usage Claude. Blaise a dû demander explicitement la suppression des références temporelles. Recommandation explicite : "on itère selon disponibilité humaine + limites d'usage modèle, pas selon des deadlines auto-imposées".

**Décision :** dans tous les briefs, statuts, conventions du couple 2 — pas de dates absolues internes (sauf échéance hackathon septembre 2026 qui structure le plan global). On parle en "sprints S0 → S4", pas en semaines calendaires précises.

**Conséquences :**
- Plus de souplesse sur l'avancement
- Pas de stress artificiel injecté dans le pipeline
- Hackathon reste l'unique borne temporelle effective

**Trace :** RetEx couple 1 — Q3 §5.

---

## D-021 — Discipline de concision des briefs (cible max ~2000 mots)

**Date :** 11 mai 2026
**Statut :** Actée

**Contexte :** RetEx couple 1 Q3 §7 + Q5 §7 — "briefs Claude Code de plus en plus volumineux" est identifié comme "symptôme de complexification". Pas de mécanisme dans couple 1 pour faire émerger un brief "v2 simplifié" plutôt que continuer à empiler.

**Décision :** tout brief Claude Code Plateforme cible un volume maximum de ~2000 mots. Si un brief dépasse, il doit être (a) découpé en sous-briefs séquentiels, ou (b) refactorisé pour faire référence à des conventions déjà inscrites dans `_instructions-rag.md` ou `SPEC-MD-POUR-RAG.md`.

**Conséquences :**
- Discipline de concision permanente
- Conventions vivantes (`_instructions-rag.md`, `SPEC-MD-POUR-RAG.md`) absorbent ce qui sinon irait dans les briefs
- Le couple 1 sera invité à faire un travail similaire à terme (refonte simplifiée de RULES.md vers v1.6, leçon Q3 §3)

**Trace :** RetEx couple 1 — Q3 §7, Q5 §7.

---

## D-022 — Spécialisation des rôles couple 2 : Cowork = matière MD, Claude Code = code RAG

**Date :** 11 mai 2026
**Statut :** Actée

**Contexte :** RetEx couple 1 Q2 §4 + Q3 §1 + Q4 §1 — l'erreur structurelle n°1 du couple 1 a été que Cowork produisait du HTML directement (v3 à v3.6), entraînant 3 itérations correctives consécutives (v3.6.1 → v3.6.3). Résolu en codifiant § 1.5.4 RULES v1.3 : Cowork = MD éditorial uniquement, Claude Code = HTML.

**Décision :** application stricte de la même règle au couple 2, par transposition :
- **Cowork Hub IA Plateforme (ce canal)** produit exclusivement : briefs MD, specs, méthodologies, fichiers de référence, et la **matière MD du vault `rag/content/`** (les fichiers MD optimisés RAG eux-mêmes, en co-production avec Cowork Hub IA pour le contexte éditorial)
- **Claude Code Hub IA Plateforme (à créer en S1)** produit exclusivement : code Python du pipeline d'ingestion, code JavaScript/TypeScript du backend Cloudflare Worker, code du widget HTML/JS embarqué sur le Hub, scripts d'audit (audit-md-rag.py, audit-rag-coverage.py), tests automatisés

**Pas de chevauchement.** Si une production se trouve en zone grise (ex. un script Python qui *aussi* manipule du Markdown), elle est par défaut allouée à Claude Code (côté code/exécution).

**Conséquences :**
- Risque éliminé que Cowork écrive du code "à l'aveugle" sans validation d'exécution
- Workflows clairs : Cowork brief → Claude Code exécute → Claude Code rapporte → Cowork capitalise

**Trace :** RetEx couple 1 — Q2 §4, Q3 §1, Q4 §1.

---

## D-023 — Principe « nouvelle règle = nouvelle fonction d'audit » codifié dès v1

**Date :** 11 mai 2026
**Statut :** Actée

**Contexte :** retour du couple 1 sur le traitement de l'item I-001 (refonte RULES-IMPLEMENTATION en v1.6). Trois apprentissages partagés vers le couple 2. Le second est : « Codifier le principe `nouvelle règle = nouvelle fonction d'audit` dès le départ : pas après 14 sous-versions accumulées. Je l'ai formalisé en K.1 de v1.6, à intégrer dans votre référentiel dès la v1. »

**Décision :** appliquer immédiatement, comme règle structurante, le principe suivant pour le couple 2 :

> Toute nouvelle règle ajoutée à `SPEC-MD-POUR-RAG.md` (au-delà de la v1 actuelle) doit s'accompagner, **dans le même commit**, d'une fonction de validation correspondante dans `audit-md-rag.py`. Une règle non automatisable manuellement par audit reste descriptive et donc inégalement appliquée — c'est la leçon centrale du RetEx couple 1 (Q2 §1, Q4 §3).

**Conséquences :**
- Le périmètre fonctionnel d'`audit-md-rag.py` croît au même rythme que `SPEC-MD-POUR-RAG.md`
- Toute proposition d'enrichissement de la spec doit être accompagnée d'une réflexion sur sa testabilité
- Si une règle n'est pas raisonnablement testable automatiquement, elle bascule en « anti-pattern documenté » (recommandation éditoriale forte mais non opposable) plutôt qu'en règle stricte
- Cette discipline s'applique à toutes les conventions du couple 2, pas seulement à `SPEC-MD-POUR-RAG.md`. Par exemple, une nouvelle convention de coordination dans `SYNC-INTER-CANAUX.md` doit s'accompagner d'un moyen de vérifier qu'elle est suivie (timestamp obligatoire, statut explicite, etc.)
- Le brief `BRIEF-CC-S1-pilote-pipeline.md` reste valide : `audit-md-rag.py` v1 démarre avec les 5 règles automatisables identifiées en §10 de `SPEC-MD-POUR-RAG.md`. Les règles non automatisées (R5 glossaire, R7 nommage, R8 versioning) sont candidates à automatisation en v2 dès qu'on identifie une approche raisonnable

**Trace :** Retour couple 1 sur I-001 — apprentissage partagé n°2. Aligné avec RULES couple 1 v1.6 K.1.

---

## D-024 — Architecture de circulation Cowork ↔ Git ↔ Claude Code Plateforme

**Date :** 11 mai 2026
**Statut :** Actée

**Contexte :** clarification par Blaise du fonctionnement réel observé côté couple 1. Aligned-mind sur le modèle existant : pas de modification croisée des dossiers Cowork-side et Git-side, le clone Git étant la source de vérité unique. Cowork écrit dans son dossier de travail (axe ascendant vers Git), Claude Code écrit dans le clone Git directement. Les divergences pour les fichiers vivants sont résolues par rebaselining manuel avant chaque session Cowork (Option D, retenue parmi 4 options soumises).

**Décision :** architecture de circulation à 3 espaces, avec règle absolue de non-modification croisée :

1. **`Canaux/Hub-IA-Plateforme/rag-prep/`** (Cowork local) : dossier de travail Cowork, **écrit uniquement par Cowork**, jamais par Claude Code, jamais re-synchronisé automatiquement depuis Git
2. **`Canaux/Hub-IA/repo-current/rag-prep/`** (clone Git local) : **source de vérité partagée**, lecture pour Cowork (consultation uniquement, jamais d'écriture), lecture-écriture pour Claude Code Plateforme via le clone Git
3. **`rag-prep/` sur le repo Git distant** : reflète l'état des deux contributions (Cowork via push manuel par Blaise, Claude Code via commit + push direct dans le clone)

**Cycle de circulation (Option D — rebaselining avant édition Cowork) :**

```
[clone Git distant]
      ▲
      │ git pull / push (Blaise)
      ▼
[clone Git local rag-prep/] ← écrit par Claude Code ← lit pour consultation par Cowork
      │
      │ Blaise copie sélective avant session Cowork (axe descendant)
      ▼
[Cowork rag-prep/] ← écrit par Cowork
      │
      │ Blaise copie complète après session Cowork (axe ascendant)
      ▼
[clone Git local rag-prep/]
      │
      │ git push (Blaise)
      ▼
[clone Git distant]
```

**Conséquences :**
- Cowork ne modifie jamais le clone Git, élimine tout risque de conflit Git
- Discipline simple : Cowork ajuste l'avenir (briefs, modifications de specs) sur la base d'un état rebaseliné
- Symétrie avec le pattern couple 1 (`Canaux/Hub-IA/site-web-prep/` vs `repo-current/site-web-prep/`)
- Charge légère mais réelle côté Blaise : pull + copies sélectives avant session Cowork, copie complète + push après session Cowork. Cette charge est le prix de l'absence de conflit Git.
- Catégorisation des 4 types de fichiers dans `_instructions-rag.md` §8 : stables (Cowork canonique), briefs sprint (immuables après push), rapports mission (Claude Code canonique), vivants (Git canonique avec rebaselining)

**Trace :** échanges Cowork ↔ Blaise — 11 mai 2026 (4 options soumises, Option D retenue après clarification de Blaise sur le fonctionnement couple 1).

---

## D-025 — Pattern architectural « module + briques transverses sélectives »

**Date :** 11 mai 2026
**Statut :** Actée

**Contexte :** Blaise a soulevé la question d'un découplage sémantique plus poussé que la convention implicite « 1 HTML = 1 MD » initialement appliquée. Question structurante posée à Cowork Hub IA via I-002 (Q7). Réponse couple 1 : compromis validé empiriquement avec recommandation forte d'extraction de 3 briques transverses dès maintenant (vigilance-hallucinations, vigilance-confidentialite, chiffres-macro-2026) + 7 brain pages prioritaires sur 6-12 mois.

**Décision :** unité de base du vault RAG = module CU/PR/DEP/fiche-outil (préserve l'isomorphisme avec le Hub HTML et la cohérence pédagogique). En complément, **extraction sélective de briques transverses** dans `rag/content/transverses/` dès qu'un concept apparaît dans **3 modules ou plus**.

**Catégories de briques transverses** (à enrichir au fil des productions) :
- `vigilance-{slug}.md` (hallucinations, confidentialité, etc.)
- `pattern-{slug}.md` (build-vs-buy, rag-vs-fine-tuning, etc.)
- `methodologie-{slug}.md` (prompt engineering, eval, etc.)
- `chiffres-macro-{annee}.md` (référentiel canonique des chiffres macro du Hub)
- `cadrage-{slug}.md` (cadrages réglementaires ou stratégiques)

**Conséquences :**
- Évite la duplication d'indexation (un seul chunk canonique par concept transverse, référencé partout par wikilink)
- Granularité du retrieval améliorée (un fichier dédié donne une réponse plus précise qu'un chunk noyé dans un module)
- Couplage avec D-023 (nouvelle règle = nouvelle fonction d'audit) : les futures briques transverses doivent être détectables par audit-md-rag.py (R9 pour chiffres macro identifie ces concepts)
- Aligné avec le pattern LLM Wiki Karpathy de la roadmap globale Phase 2 (préparation infrastructurelle)
- 3 risques à monitorer (cf. SPEC v1.1 section « Briques transverses ») : dérive référentiel chiffres, duplication brain page/module, wikilinks cassés

**Trace :** revue I-002 Q7 par Cowork Hub IA — 11 mai 2026.

---

## D-012-bis (révision) — MCP Obsidian reporté à Phase 2

**Date :** 12 mai 2026
**Statut :** Actée (supersède D-012 du 11 mai 2026)

**Contexte :** D-012 avait acté en S0 le setup MCP Obsidian côté Claude Code Plateforme dès S1, par anticipation. Première session Claude Code Plateforme (S1) a livré 6 lots avec 62/62 tests verts en utilisant le filesystem direct sur les MD du vault — sans MCP Obsidian. Le Lot 2 (config MCP) a été délégué à Blaise (config locale Claude Code Desktop).

**Décision :** **reporter le setup MCP Obsidian à Phase 2** (LLM Wiki layer). Raisons :
1. Gain marginal en Phase 1 : Claude Code Plateforme accède déjà aux MD via Read/Write/Edit + parsing frontmatter via PyYAML/regex. Pas de besoin opérationnel non couvert.
2. Valeur réelle en Phase 2 : le MCP Obsidian devient structurant pour la LLM Wiki layer (brain pages persistantes, graphe de notes interconnectées, navigation Obsidian-style, multi-agent vaults). Là, les helpers Obsidian font la différence.
3. Coût opportunité : ~30-45 min de setup côté Blaise pour ROI quasi-nul en Phase 1.

**Conséquences :**
- Lot 2 du brief CC-S1 reclassé « non applicable Phase 1 »
- À reconsidérer au démarrage Phase 2 (LLM Wiki layer) — sans engagement préalable
- Claude Code Plateforme continue à accéder au vault via filesystem direct

**Trace :** retour CC-S1 (Lot 2 délégué à Blaise) + décision Cowork/Blaise — 12 mai 2026.

---

## D-027 — Convention de nommage des branches Claude Code Plateforme

**Date :** 12 mai 2026
**Statut :** Actée

**Contexte :** premier sprint Claude Code Plateforme (S1) a livré sur la branche `claude/execute-pilot-batches-mBSIp` au lieu de `feature/rag-s1-pilote` proposée dans le brief. Le nom de branche est probablement imposé par l'outillage Claude Code agentique (préfixe `claude/execute-` + slug + hash de session).

**Décision :** **accepter par défaut le nommage Claude Code agentique** `claude/execute-{slug}-{hash}`. Pas de rename imposé. Les briefs sprint **ne fixent plus de nom de branche** (la formulation « branche dédiée » du brief CC-S1 §6 est obsolète).

**Conséquences :**
- Workflow Claude Code Plateforme : branche créée automatiquement par l'outillage, commits, PR vers main avec le nom de branche tel quel
- Convention de nommage des PR (titre PR) à formaliser pour compenser : `feat(rag): sprint S{N} - {slug}` pour rester traçable côté humain
- Briefs futurs : mention de la branche supprimée, focus sur le contenu du sprint et le titre de PR attendu

**Trace :** retour CC-S1 (écart signalé) + simplification opérationnelle — 12 mai 2026.

---

## D-026 — Co-production légère obligatoire sur modules N3/N4

**Date :** 12 mai 2026
**Statut :** Actée

**Contexte :** retour I-003 Q5 du couple 1 signale comme « signal faible » que la co-production prévue par STRATEGIE-MD-RAG §6 a été court-circuitée sur la vague 2 (Blaise go direct sans sondage Cowork Hub IA). Conséquence : 5 dérives chiffrées détectées sur la matrice PR-07 en revue a posteriori. Couple 1 recommande de revenir à une co-production légère sur les modules complexes : « sondage Cowork Hub IA AVANT production sur les 2-3 passages les plus sensibles, plutôt que revue exhaustive a posteriori. Effort équivalent côté couple 1, gain qualité significatif. »

**Décision :** pour tout module de niveau ⭐⭐⭐ ou ⭐⭐⭐⭐ (modules N3/N4), Cowork Hub IA Plateforme effectue un **sondage Cowork Hub IA AVANT production** sur les 2-3 passages les plus sensibles identifiés. Procédure :

1. Avant production d'un module N3/N4, Cowork Hub IA Plateforme identifie 2-3 passages sensibles (tableaux chiffrés, RetEx, distinctions conceptuelles fines, patterns techniques précis).
2. Sondage léger au couple 1 via Blaise : « pour le module X, je vais transposer ces passages [Y/Z], y a-t-il des points de vigilance, dérives historiques à éviter, ou nuances à préserver ? »
3. Couple 1 répond en mode bref (< 200 mots/passage) avec les vigilances spécifiques.
4. Cowork Hub IA Plateforme produit le module en intégrant ces vigilances.
5. Revue a posteriori reste possible mais moins exhaustive (déjà calibrée par le sondage).

**Conséquences :**
- Pour la vague 3 (CU-026 gouvernance, CU-027 dev applicatif IA, DEP-08 sécurité agents/MCP), sondage préalable obligatoire
- Effort équivalent réparti en amont au lieu d'a posteriori
- Réduction du risque de dérives non détectées (notamment AP-1 R9 et AP-4 R10 sur les chiffres et fourchettes)
- Compatible avec D-024 (le clone Git reste source de vérité, le sondage passe par les conventions de coordination inter-canaux légères type SYNC-INTER-CANAUX item-mini)

**Trace :** revue I-003 Q5 par Cowork Hub IA — 12 mai 2026.

---

*Toute nouvelle décision est ajoutée en bas du fichier avec un numéro incrémental. L'index en haut est mis à jour en conséquence.*
