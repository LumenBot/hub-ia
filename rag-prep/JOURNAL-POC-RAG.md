# JOURNAL-POC-RAG.md — Journal continu du couple 2

**Statut :** Actif
**Format :** append-only, chronologique inverse (entrées récentes en haut)

> **Rôle de ce fichier :** trace continue de toutes les sessions Cowork et Claude Code du couple 2. Permet de reconstituer la chronologie d'évolution du POC. Lu à chaque démarrage de session pour reprendre le contexte.

> **Format d'une entrée :** date | acteur (Cowork ou Claude Code) | session | actions menées | reste à faire / next.

---

## Entrées

### 2026-05-11 (tardive) — Cowork Hub IA Plateforme — Migration vers rag-prep/ et D-024

**Actions menées :**
- Clarification par Blaise du fonctionnement réel observé côté couple 1 : pas de modification croisée entre dossier Cowork local et clone Git local. Le clone Git est source de vérité unique. Cowork ne modifie jamais le clone Git, écrit uniquement dans son dossier de travail.
- 4 options soumises à Blaise pour la gestion des fichiers vivants. **Option D retenue** (rebaselining manuel par Blaise avant chaque session Cowork significative).
- Création du sous-dossier `Canaux/Hub-IA-Plateforme/rag-prep/` côté Cowork.
- Déplacement (mv) des 10 fichiers de gouvernance + dossier `briefs/` vers `rag-prep/`. La racine `Canaux/Hub-IA-Plateforme/` ne conserve que `README.md`, `analyses/`, `roadmap/` (méta-doc non transmise sur Git).
- Mise à jour `_instructions-rag.md` §8 (réécriture complète) : intégration de D-024 (architecture de circulation Cowork ↔ Git ↔ Claude Code), Option D rebaselining détaillée, distinction stables/briefs/rapports/vivants.
- Mise à jour `BRIEF-CC-S1-pilote-pipeline.md` :
  - Chemins de référence : `rag-prep/...` (dans le clone Git) au lieu de `Canaux/Hub-IA-Plateforme/...`
  - Lot 1 : ajout de `rag/docs/` dans la structure cible (créé à la main de Claude Code, contient doc technique, ne duplique pas les conventions de `rag-prep/`)
  - Précision sur la circulation des MD pilotes (Cowork-side → `rag-prep/content-drafts/` du clone Git → `rag/content/` final)
- Acte **D-024** dans `DECISIONS-RAG.md` (architecture de circulation à 3 espaces + Option D).

**Décisions structurantes prises :**
- D-024 — Architecture de circulation Cowork ↔ Git ↔ Claude Code Plateforme

**Reste à faire — clôture S0 :**
- Blaise effectue le push initial : `mkdir -p Canaux/Hub-IA/repo-current/rag-prep && cp -r Canaux/Hub-IA-Plateforme/rag-prep/* Canaux/Hub-IA/repo-current/rag-prep/ && cd Canaux/Hub-IA/repo-current && git add rag-prep/ && git commit -m "feat: rag-prep/ canal plateforme — gouvernance S0" && git push`
- Création du canal Claude Code Plateforme par Blaise, transmission du chemin `rag-prep/briefs/BRIEF-CC-S1-pilote-pipeline.md` comme premier ordre de mission.
- En parallèle, Cowork peut attaquer la production des 5 fichiers MD pilotes.

**Blockers :**
- Push initial par Blaise + création canal Claude Code Plateforme.

---

### 2026-05-11 (soir) — Cowork Hub IA Plateforme — Retour couple 1 sur I-001 + intégration

**Actions menées :**
- Réception du retour structuré de Cowork Hub IA sur l'item I-001 (refonte RULES v1.6).
- Item I-001 traité immédiatement côté couple 1 (3-4 h Cowork + 1-2 h Claude Code attendues). 3 livrables produits : `RULES-IMPLEMENTATION-v1.6.md`, `RULES-MIGRATION-v1.5-vers-v1.6.md`, `BRIEF-CLAUDE-CODE-RULES-v1.6.md`. Push effectué, intégration par Claude Code Hub IA sur branche `refactor/rules-v1.6-consolidation`.
- Intégration des 3 apprentissages partagés par couple 1 vers couple 2 :
  - Apprentissage 1 (démarrer minimaliste) : déjà appliqué dans `SPEC-MD-POUR-RAG.md` v1
  - Apprentissage 2 (nouvelle règle = nouvelle fonction d'audit) : acté en **D-023**, intégré dans `_instructions-rag.md` §7 garde-fou n°9, et dans le préambule de `SPEC-MD-POUR-RAG.md`
  - Apprentissage 3 (référentiel principal court vs annexes longues) : déjà appliqué
- Codification du pattern canonique de coordination inter-canaux dans `SYNC-INTER-CANAUX.md` sur la base du flux validé empiriquement sur I-001
- Item I-001 archivé dans `SYNC-INTER-CANAUX.md` (section « Items résolus / archivés ») avec trace temporelle complète et apprentissages capitalisés
- Référence v1.5.14 dans `BRIEF-CC-S1-pilote-pipeline.md` mise à jour : pointe désormais vers v1.6 dès merge, v1.5.14 transitoire

**Décisions structurantes prises :**
- D-023 — Principe « nouvelle règle = nouvelle fonction d'audit » codifié dès v1

**Suivi post-clôture :**
- Attendre notification (via Blaise) du merge de la branche `refactor/rules-v1.6-consolidation` par couple 1
- À réception du merge : substituer définitivement la référence v1.5.14 par v1.6 dans nos fichiers
- Premier cycle de coordination inter-canaux fonctionnel et capitalisé. Pattern canonique opposable pour les items futurs.

**Reste à faire — clôture S0 :**
- Identique à l'entrée précédente : Blaise crée le canal Claude Code Plateforme + transmet `BRIEF-CC-S1-pilote-pipeline.md`. En parallèle, Cowork attaque la production des 5 fichiers MD pilotes.

**Blockers :**
- Création du canal Claude Code Plateforme par Blaise pour ouvrir S1.

---

### 2026-05-11 (fin de journée) — Cowork Hub IA Plateforme — Clôture S0

**Actions menées :**
- Validation Blaise sur l'ensemble du bloc D-005 à D-014 et D-017 (11 décisions techniques actées en une passe sur recommandations Cowork).
- Production des 4 artefacts S0 majeurs :
  - `STRATEGIE-MD-RAG.md` v1 (méthodologie de retranscription HTML → MD, 5 questions d'analyse, démarche pilote → scale, co-production avec couple 1 cadrée)
  - `SPEC-MD-POUR-RAG.md` v1 (8 règles minimalistes : frontmatter 10 champs, H1 unique, sections H2 autonomes, chunking 400-700 tokens, wikilinks Obsidian, glossaire canonique, chiffres sourcés, nommage MD, versioning)
  - `cartographie-rag.md` v0 (structure définie, 8 sujets à fort recouvrement identifiés pour vigilance)
  - `SYNC-INTER-CANAUX.md` v0 (triggers de coordination définis + premier item I-001 sur refonte RULES v1.6 simplifiée)
- Consolidation `_instructions-rag.md` v1 (intégrant toutes les décisions actées, spécialisation rôles renforcée, procédure boot avec resync git, glossaire couple 2)
- Production du `BRIEF-CC-S1-pilote-pipeline.md` (6 lots, ~15-19 h Claude Code, cible ~1900 mots conforme D-021)

**Décisions structurantes prises :**
- D-005 à D-014 et D-017 toutes actées
- Choix de 5 unités pilotes pour S1 : CU-001, CU-008 (référence canonique), PR-07, DEP-02, outils-vector-db

**Reste à faire — clôture S0 :**
- Blaise transmet l'item I-001 (`SYNC-INTER-CANAUX.md`) au canal Cowork Hub IA (opportunité refonte RULES v1.6 simplifiée)
- Création du canal Claude Code Hub IA Plateforme par Blaise (déclenche l'ouverture du sprint S1)
- Démarrage en parallèle de la production des 5 unités MD pilotes côté Cowork (en co-production avec Cowork Hub IA pour CU-008, PR-07, DEP-02)

**Blockers :**
- Création du canal Claude Code Plateforme par Blaise pour ouvrir S1.

---

### 2026-05-11 (après-midi) — Cowork Hub IA Plateforme — Réception RetEx couple 1

**Actions menées :**
- Réception du `RETEX-COWORK-HUB-IA-vers-PLATEFORME.md` (~2800 mots, ADN QFC respecté).
- Lecture intégrale. Extraction des enseignements structurants :
  - **4 leviers principaux** identifiés par couple 1 : (1) spécialisation rôles Cowork/Code, (2) audit automatisé, (3) référence canonique unique, (4) resync systématique post-merge.
  - **5 frictions historiques à éviter** : Cowork produisant du code, absence resync, RULES qui grossit, cartographie imprécise, pas de recouvrement sémantique.
  - **7 signaux faibles à monitorer**.
- Mise à jour `DECISIONS-RAG.md` : ajout D-016 à D-022 (décisions issues directement du RetEx).
- Mise à jour `STATUS-RAG.md` : L0.3 marqué fait, ajout de livrables liés aux nouvelles décisions.

**Décisions structurantes prises :**
- D-016 — Mise en place d'un audit-md-rag.py automatisé dès S1 (équivalent audit-global.py couple 1)
- D-017 — Référence canonique MD à identifier dès S1 (proposition à valider Blaise)
- D-018 — Procédure de resync git systématique en début de session
- D-019 — Cartographie d'ancrage RAG distincte du contenu indexé (angles thématiques par chunk)
- D-020 — Pas de référence temporelle absolue dans les briefs et conventions (sauf échéance hackathon)
- D-021 — Discipline de concision des briefs (cible max 2000 mots)
- D-022 — Spécialisation des rôles couple 2 explicitée : Cowork = matière MD, Claude Code = code RAG (Python/JS), pas de mélange

**Reste à faire — next steps S0 :**
- Validation Blaise des décisions techniques D-005 à D-013 (LLM, vector DB, embeddings, backend, MCP Obsidian, plafonds API).
- Validation Blaise des décisions issues du RetEx (D-016 à D-022) ou amendements.
- Production de `STRATEGIE-MD-RAG.md` et `SPEC-MD-POUR-RAG.md` v1 (en démarrant minimaliste — leçon Q3 RetEx).
- Production du `SYNC-INTER-CANAUX.md` initial.
- Consolidation `_instructions-rag.md` v1.

**Blockers :**
- Décisions techniques D-005 à D-013 et D-016 à D-022 en attente de validation Blaise.

---

### 2026-05-11 — Cowork Hub IA Plateforme — Session de cadrage initial

**Actions menées :**
- Lecture du README du canal, de la roadmap globale, et du fichier `analyses/build-vs-buy-agent.md`.
- Échanges stratégiques avec Blaise sur 4 itérations successives :
  1. Premières observations + 5 questions de cadrage budget/compétences/délai/widget/souveraineté
  2. Implications des contraintes (POC démonstrateur < 100 €/mois, zéro compétence IT, hackathon septembre)
  3. Exploration du repo Hub IA (87 HTML, 56 MD, 145 unités éditoriales) + question Obsidian
  4. Décision architecturale finale : **architecture à 2 couches HTML/MD complémentaires** (D-001)
  5. Décision : **repo unique `hub-ia` avec dossier `rag/` séparé** (D-002)
  6. Décision : **architecture à 4 canaux** (D-003)
  7. Décision : **pas de bascule de source de vérité** (D-004)
- Création des 4 fichiers de référence (`_instructions-rag.md` v0, `DECISIONS-RAG.md` initial, ce `JOURNAL`, `STATUS-RAG.md`).
- Création du dossier `briefs/`.
- Rédaction du `BRIEF-RETEX-COWORK-HUB-IA.md` à transmettre au couple 1.

**Décisions structurantes prises :**
- D-001 à D-004 (cf. `DECISIONS-RAG.md`)
- Plan d'action S0 à S4 défini (cf. `STATUS-RAG.md`)

**Reste à faire — next steps S0 :**
- Blaise transmet le `BRIEF-RETEX-COWORK-HUB-IA.md` au canal Cowork Hub IA.
- Réception du RetEx couple 1 → consolidation `_instructions-rag.md` v1.
- Benchmark restreint des options techniques (LLM, vector DB, embeddings, backend) pour acter D-005 à D-008.
- Production de `STRATEGIE-MD-RAG.md` (méthodologie de retranscription) et `SPEC-MD-POUR-RAG.md` v1 (cahier des charges format).

**Blockers :** aucun.

---

*Format de toute nouvelle entrée :*

### YYYY-MM-DD — [Cowork ou Claude Code] — Description session

**Actions menées :**
- ...

**Décisions structurantes prises :**
- ... (ou : aucune)

**Reste à faire :**
- ...

**Blockers :**
- ... (ou : aucun)

---
