# _instructions-rag.md — Référentiel du couple 2 (Hub IA Plateforme)

**Statut :** v1 (consolidée post-RetEx couple 1)
**Dernière mise à jour :** 11 mai 2026
**Maintainer :** Blaise Cavalli — couple 2

> **Rôle de ce fichier :** référentiel fixe lu par Cowork et Claude Code Plateforme **à chaque démarrage de session**. Contient l'architecture, les conventions, les garde-fous, le glossaire d'acronymes. Tout ce qui est ici est opposable. Tout ce qui n'y est pas n'est pas une règle.

> **Discipline (RetEx Q3 §3) :** démarrer minimaliste, enrichir au fil des écarts détectés. Cette v1 est volontairement concise.

---

## 1. Périmètre du couple 2

**Mission :** concevoir, développer et déployer le pipeline RAG (Phase 1) du Hub IA Learning Center. Démonstrateur cible au hackathon QFC de septembre 2026. Horizons Phase 2 et 3 : LLM Wiki layer puis plateforme dynamique 4-en-1.

**Hors périmètre :** production éditoriale du Hub (modules CU, préalables PR, fiches outils, mise en prod HTML). Périmètre du couple 1.

---

## 2. Architecture cible — deux couches complémentaires

| Couche | Format | Public | Producteur | Frontend |
|---|---|---|---|---|
| **Pédagogique** | HTML | Humain (dirigeant PME/ETI Grand Est non-IT) | Couple 1 (inchangé) | Site GitHub Pages |
| **Fonctionnelle** | MD optimisé RAG | LLM (Claude API) | Couple 2 (nous) | Backend RAG → widget chat embarqué sur le Hub |

Les MD ne sont **pas** une conversion du HTML. Œuvres parallèles distillées pour l'usage RAG. (Décisions D-001, D-004).

---

## 3. Structure du repo `hub-ia` cible

```
hub-ia/
├── (HTML existant inchangé : index.html, modules/, prealables/, deploiement/, ressources.html, architectures.html, etc.)
├── rag/
│   ├── content/                  ← fichiers MD pour le RAG (vault Obsidian)
│   │   ├── modules/              ← cu-001.md, cu-002.md, ...
│   │   ├── prealables/           ← pr-01.md, ...
│   │   ├── deploiement/          ← dep-01.md, ...
│   │   ├── architectures/        ← a1.md, a2.md, ...
│   │   ├── ressources/           ← outils-vector-db.md, outils-llm-gateway.md, ...
│   │   ├── transverses/          ← brain pages, fiches transverses
│   │   └── glossaire.md          ← glossaire canonique partagé
│   ├── code/                     ← pipeline RAG : ingestion, retrieval, widget, backend
│   ├── eval/                     ← questions de test, golden answers, golden set
│   └── README.md
└── ...
```

Décision D-002.

---

## 4. Stack technique actée (décisions D-005 à D-014)

| Brique | Choix | Détail |
|---|---|---|
| LLM génération principal | Claude Sonnet 4.6 | API Anthropic, hébergement EU |
| LLM tâches simples | Claude Haiku 4.5 | Résumés, classification, reformulation |
| Embeddings | OpenAI text-embedding-3-small | ~0,02 $/M tokens |
| Vector DB | ChromaDB local | Embarqué dans backend ou Supabase pgvector si volume |
| Backend | Cloudflare Workers | Free tier 100k req/jour, déployable EU |
| Capture feedback | Supabase free tier | Questions, votes, sources citées |
| Widget front | HTML/JS minimal | Embarqué dans index.html du Hub |
| Vault éditeur | Obsidian + MCP Obsidian côté Claude Code | Édition atomique du vault |
| Plafond Anthropic | 50 $/mois (alerte 30 $) | Cap dur, configuré côté dashboard |
| Plafond OpenAI | 10 $/mois (alerte 5 $) | Cap dur, configuré côté dashboard |

Budget cible Phase 1 : **< 100 €/mois récurrent**.

---

## 5. Spécialisation des rôles (D-022 — règle non négociable)

| Rôle | Produit | Ne produit jamais |
|---|---|---|
| **Cowork Hub IA Plateforme** (ce canal) | Briefs MD, specs, méthodologies, fichiers de référence, **matière MD du vault** (co-production avec couple 1 sur modules denses) | Code Python, code JS/TS, scripts d'audit, tests |
| **Claude Code Hub IA Plateforme** (à créer S1) | Code pipeline ingestion, code backend Cloudflare Worker, widget HTML/JS, scripts d'audit (audit-md-rag.py, audit-rag-coverage.py), tests automatisés | Matière MD éditoriale, briefs stratégiques |

**Pas de chevauchement.** Erreur structurelle du couple 1 v3-v3.6 à ne pas reproduire (Cowork qui produisait du HTML).

---

## 6. Exigences d'évolutivité by design (non négociables)

1. **Re-indexation incrémentale** : seuls les chunks affectés par une modification du vault sont ré-indexés
2. **Versioning par chunk** : champ `version` du frontmatter MD → métadonnée `source_version` dans le vector store → purge des versions obsolètes
3. **Pipeline déclenchable à la demande ET planifié** : push de mise à jour ou cron quotidien
4. **Eval automatisée** : à chaque rebuild, golden set rejoué → régression détectée = alerte

Cycle **Stitch → Evaluate → Iterate** (DEP-02 du Hub).

---

## 7. Garde-fous (allégés post-validation Blaise)

1. **Plafonds API stricts** (D-013)
2. **Secrets jamais dans le code** (env vars Cloudflare/Supabase, jamais en clair dans un commit)
3. **Tests automatisés produits par Claude Code lui-même** : chaque module de code livré avec un script de test exécutable. Pas optionnel.
4. **Repo unique `hub-ia`, sur main, en prod** (D-002). `.gitignore` propre pour exclure vector store local, .env, caches.
5. **Documentation préalable des décisions structurantes** dans `DECISIONS-RAG.md`. Une fois consignée, la décision fait foi.
6. **Mentor externe consultable ponctuellement** sur les 2-3 décisions vraiment structurantes (architecture initiale, premier déploiement). Pas en permanence.
7. **Audit-md-rag.py automatisé dès S1** (D-016) : valide la conformité des MD à `SPEC-MD-POUR-RAG.md` avant tout commit
8. **Discipline de concision des briefs** : cible ~2000 mots max (D-021)
9. **Nouvelle règle = nouvelle fonction d'audit** (D-023, issue retour couple 1 sur I-001) : toute règle ajoutée à `SPEC-MD-POUR-RAG.md` au-delà de la v1 doit s'accompagner d'une fonction de validation dans `audit-md-rag.py` dans le même commit. Une règle non automatisable bascule en « anti-pattern documenté », pas en règle stricte.

Principe : documentation rigoureuse en amont, confiance totale en exécution.

---

## 8. Architecture de circulation Cowork ↔ Git ↔ Claude Code Plateforme (D-024)

### Principe absolu

**Le clone Git local est la source de vérité unique.** Cowork ne modifie **jamais** le clone Git. Cowork écrit uniquement dans son dossier de travail Cowork-side. Claude Code Plateforme écrit uniquement dans le clone Git (qui se push vers le repo distant). Pas de modification croisée.

### Deux espaces `rag-prep/` distincts

| Espace | Lieu | Qui écrit | Qui lit |
|---|---|---|---|
| `Canaux/Hub-IA-Plateforme/rag-prep/` | Cowork local (dossier de travail) | Cowork (moi) uniquement | Cowork |
| `Canaux/Hub-IA/repo-current/rag-prep/` | Clone Git local (source de vérité) | Claude Code Plateforme via clone Git + Cowork via push manuel par Blaise | Tous (lecture) |

### Source de vérité partagée — 6 fichiers de référence (couple 2)

| Fichier | Contenu | Qui écrit | Source de vérité |
|---|---|---|---|
| `_instructions-rag.md` (ce fichier) | Référentiel fixe | Cowork + validation Blaise | Cowork-side puis Git après push |
| `DECISIONS-RAG.md` | Registre ADR | Cowork (stratégique), Claude Code (technique) | Git-side (Cowork rebaseline avant édition) |
| `JOURNAL-POC-RAG.md` | Journal continu | Append-only par Cowork ET Claude Code | Git-side (Cowork rebaseline avant édition) |
| `STATUS-RAG.md` | État sprint courant | Cowork, MAJ Claude Code en fin de session | Git-side (Cowork rebaseline avant édition) |
| `cartographie-rag.md` | Inventaire angles thématiques | Cowork à chaque production MD, Claude Code peut enrichir | Git-side (Cowork rebaseline avant édition) |
| `SYNC-INTER-CANAUX.md` | Coordination couple 1 ↔ couple 2 | Cowork principalement | Git-side (Cowork rebaseline avant édition) |

### Convention de rebaselining — Option D (actée le 11 mai 2026)

Avant chaque session Cowork significative :
1. **Blaise pull le clone Git** : `cd Canaux/Hub-IA/repo-current && git pull` (synchronisation descendante depuis le repo distant, capture des ajouts Claude Code).
2. **Blaise re-copie sélectivement** depuis le clone Git vers le dossier de travail Cowork les fichiers vivants (JOURNAL, STATUS, cartographie-rag, SYNC-INTER-CANAUX, DECISIONS si modifié par Claude Code, plus tout `RAPPORT-CC-SX.md` récent) — afin que Cowork démarre sa session sur une base à jour.
3. **Cowork lit les fichiers de référence** dans `Canaux/Hub-IA-Plateforme/rag-prep/` (qui contient désormais l'état à jour grâce au rebaselining).
4. **Cowork ajuste les prochaines itérations** (briefs, modifications de specs, ajouts au journal).
5. **Blaise push** : `cp -r Canaux/Hub-IA-Plateforme/rag-prep/* Canaux/Hub-IA/repo-current/rag-prep/ && cd Canaux/Hub-IA/repo-current && git add rag-prep/ && git commit -m "..." && git push`.

**Principe pédagogique** : Cowork ne réécrit pas le passé, il ajuste l'avenir. Les modifications Claude Code récentes sont visibles via le rebaselining, et orientent la production Cowork de la session courante.

### Protocole boot Claude Code Plateforme (chaque session)

1. **Resync git** (D-018) : `git fetch && git status` sur `hub-ia`. Si désynchro → `git reset --hard origin/main` après confirmation Blaise.
2. **Lecture des 6 fichiers de référence** dans `rag-prep/` du clone Git + dernier `briefs/BRIEF-CC-SXX-titre.md` actif.
3. **Confirmation explicite** : « Sync state lue, je m'apprête à faire X ».

### Protocole shutdown Claude Code Plateforme

1. Update `rag-prep/JOURNAL-POC-RAG.md` (append) dans le clone Git
2. Update `rag-prep/STATUS-RAG.md` si état sprint évolue
3. Update `rag-prep/DECISIONS-RAG.md` si décision technique structurante prise
4. Production de `rag-prep/briefs/RAPPORT-CC-SXX.md` consolidé en fin de sprint
5. Commit + push de toutes les modifications du clone Git

### Briefs sprint

Cowork produit en amont `briefs/BRIEF-CC-SXX-titre.md` (cible ~2000 mots, D-021). Validé explicitement par Blaise avant push. Une fois pushé, le brief est consommé par Claude Code Plateforme — pas de modification après push (les amendements éventuels passent par un nouveau brief ou par un item `SYNC-INTER-CANAUX`).

---

## 9. Procédure de synchronisation inter-couples (couple 1 ↔ couple 2)

**Fichier de coordination :** `SYNC-INTER-CANAUX.md` (initialisé en S0).

**Garant transverse :** Blaise. Items légers (max 200 mots/item), pas de pression temporelle, format informatif par défaut.

---

## 10. Référence canonique MD (D-017)

`rag/content/modules/cu-008.md` est la **référence canonique** à copier pour tous les autres fichiers MD du vault. Produit en pilote S1 avec un soin particulier.

---

## 11. Glossaire et acronymes du couple 2

- **Couple 1** : Cowork Hub IA + Claude Code Hub IA — production éditoriale et déploiement HTML
- **Couple 2** : Cowork Hub IA Plateforme + Claude Code Hub IA Plateforme — développement RAG et fonctionnalités produit
- **Vault** : dossier `rag/content/` du repo `hub-ia`, contenant les fichiers MD optimisés RAG
- **Chunk** : unité d'indexation du vector store (= une section H2 d'un fichier MD du vault, frontmatter injecté en tête)
- **Garant transverse** : Blaise Cavalli, responsable de la cohérence inter-canaux
- **Sprint S0** : cadrage (en cours)
- **Sprint S1** : pilote retranscription 5 unités + setup canal Claude Code Plateforme + audit-md-rag + premier pipeline ChromaDB
- **Sprint S2** : migration MD complète (145 unités → ~50-60 fichiers selon D-014) + pipeline RAG opérationnel
- **Sprint S3** : widget public sur le Hub + capture feedback
- **Sprint S4** : eval + récit hackathon

---

## 12. Historique des versions

| Version | Date | Modification |
|---|---|---|
| v0 | 11 mai 2026 | Squelette initial avant RetEx |
| v1 | 11 mai 2026 | Consolidation post-RetEx + décisions techniques D-005 à D-022 actées |
