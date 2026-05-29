# Correctif final pré-shutdown — Claude Code RAG → strategie-ia

**Version** : v1.0
**Date de création** : 2026-05-29
**Dernière mise à jour** : 2026-05-29
**Statut** : validé
**Auteur principal** : Cowork Hub IA Plateforme (Claude Code RAG)
**Destinataire** : Cavalli (intermédiaire Git) → repo `LumenBot/strategie-ia` branche `main`
**Owner fonctionnel** : 07-tech-et-architecture + 09-rag-et-ia + _handoffs
**Confidentialité** : interne
**Tags** : correctif-final, pre-shutdown, vague-b-migration, adr-drafts, handoffs

---

## 1. Pourquoi ce correctif

Audit pré-shutdown demandé par Hub Strat le 2026-05-29. **Dernière occasion de migrer** la matière produite par Claude Code RAG dans `strategie-ia/main` avant retrait du canal Cowork actuel + reboot de la nouvelle cohorte d'agents.

Priorité actée : **complétude > perfection**. Mieux vaut migrer un fichier brut que le perdre.

Périmètre = tout ce qui était planifié Vague B (J+10 → J+15 = 8 → 18 juin 2026) et qui **ne sera jamais migré** si le shutdown intervient avant. Plus mes handoffs Vague A/C qui pourraient ne pas être encore poussés par Cavalli côté repo.

## 2. Inventaire — 60 fichiers, 5 dossiers cibles

### 2.1 Récapitulatif par catégorie

| Cible | Fichiers | Type | Régime PR proposé |
|---|---|---|---|
| `09-rag-et-ia/pipeline-ingestion/` | 8 PY | Code production RAG (run_eval, ingest, query, bench_runner, bench_runner_hybrid, _cost, _env, _rescore_adversarial) | **R2 fast-track tech** (reviewer croisé Hub RAG) |
| `09-rag-et-ia/tests/` | 6 PY | Tests pytest pipeline (~154 tests) | **R2 fast-track tech** |
| `09-rag-et-ia/golden-set/` | 1 YAML | Golden set canonique (104 std + 14 adv) | **R2 fast-track tech** |
| `09-rag-et-ia/evaluations/` | 7 fichiers | 4 RAPPORT-CC (S2.6→S2.9) + audit R11 (md + json) + eval-report S2.9 comparatif | **R2 fast-track tech** |
| `09-rag-et-ia/sprints/{s2-6,s2-7,s2-8,s2-9}/` | 7 MD | Briefs + validation-scoring + diagnostic filter-unit | **R2 fast-track tech** |
| `09-rag-et-ia/adr/` | 3 MD draft | ADR-001/002/003 **skeletons à finaliser** | **R1 standard** + co-relecture Hub RAG + arbitrage Cavalli (ADR-001) |
| `07-tech-et-architecture/qualite-et-tests/` | 2 PY + 2 PY tests | audit_md_rag.py + citation_audit.py + tests (~121 tests) | **R2 fast-track tech** |
| `07-tech-et-architecture/qualite-et-tests/integration/` | 4 fichiers | Smoke test Playwright JOURNEY (déjà transmis bundle Vague C #1 response — safety re-include) | **R2 fast-track tech** |
| `07-tech-et-architecture/spec-md-rag/` | 1 MD | SPEC-MD-POUR-RAG v2.3 canonique | **R2 fast-track tech** |
| `07-tech-et-architecture/adr/` | 2 MD draft | ADR-004/005 **skeletons à finaliser** | **R1 standard** + arbitrage Cavalli (ADR-004) |
| `07-tech-et-architecture/deploiement/ci-cd/` | 1 README + 5 scripts | CI conformité Vague A (safety re-include si pas déjà mergée) | **R3 fast-track mineur** si déjà mergée, sinon R1 |
| `.github/workflows/` | 1 YAML | Workflow audit-conformity (safety re-include) | **R3 fast-track mineur** |
| `_handoffs/` | 8 MD | Tous mes handoffs Vague A/B/C + coordination-bidirectionnelle.md v1.1 | **R4 hors PR** |
| **TOTAL** | **~60 fichiers** | | |

### 2.2 Mapping détaillé par dossier

```
correctif-final-claude-code-rag-2026-05-29/
├── README-CORRECTIF.md                              ← ce fichier
│
├── .github/workflows/
│   └── audit-conformity.yml                         (Vague A safety re-include)
│
├── 07-tech-et-architecture/
│   ├── adr/
│   │   ├── ADR-004-stack-variante-a-mvp.md          (DRAFT skeleton)
│   │   └── ADR-005-conventional-commits-squash-branch-protection.md (DRAFT skeleton)
│   ├── deploiement/ci-cd/
│   │   ├── README.md                                (Vague A safety)
│   │   └── scripts/
│   │       ├── audit-conformity.sh
│   │       ├── audit_conformity.py
│   │       ├── _generate_index_helper.py
│   │       ├── check-links.sh
│   │       └── generate-index.sh
│   ├── qualite-et-tests/
│   │   ├── audit_md_rag.py                          (renommé snake_case §11)
│   │   ├── citation_audit.py
│   │   ├── tests/
│   │   │   ├── test_audit_md_rag.py                 (93 tests)
│   │   │   └── test_citation_audit.py               (28 tests)
│   │   └── integration/                             (Vague C #1 response safety)
│   │       ├── README.md
│   │       ├── package.json
│   │       ├── playwright.config.ts
│   │       └── tests/journey-smoke.spec.ts          (7 tests Playwright)
│   └── spec-md-rag/
│       └── spec-md-pour-rag-v2-3.md                 (SPEC canonique)
│
├── 09-rag-et-ia/
│   ├── adr/
│   │   ├── ADR-001-llm-haiku-baseline-sonnet-routing.md  (DRAFT skeleton)
│   │   ├── ADR-002-bm25-hybrid-rrf-retrieval.md          (DRAFT skeleton)
│   │   └── ADR-003-frontmatter-yaml-10-champs.md         (DRAFT skeleton retrospectif)
│   ├── evaluations/
│   │   ├── rapport-cc-s2-6.md                       (renommé kebab)
│   │   ├── rapport-cc-s2-7.md
│   │   ├── rapport-cc-s2-8.md
│   │   ├── rapport-cc-s2-9.md
│   │   ├── audit-md-rag-r11-s2-8.md
│   │   ├── audit-md-rag-r11-s2-8.json
│   │   └── eval-report-s2-9-comparatif.md
│   ├── golden-set/
│   │   └── questions.yaml                           (104 std + 14 adv canonique)
│   ├── pipeline-ingestion/
│   │   ├── _cost.py
│   │   ├── _env.py
│   │   ├── _rescore_adversarial.py
│   │   ├── bench_runner.py
│   │   ├── bench_runner_hybrid.py
│   │   ├── ingest.py
│   │   ├── query.py
│   │   └── run_eval.py
│   ├── sprints/
│   │   ├── s2-6/brief-cc-s2-6.md
│   │   ├── s2-7/brief-cc-s2-7.md
│   │   ├── s2-8/
│   │   │   ├── brief-cc-s2-8.md
│   │   │   └── validation-scoring-r11.md
│   │   └── s2-9/
│   │       ├── brief-cc-s2-9.md
│   │       ├── diagnostic-filter-unit.md
│   │       └── validation-scoring-filter-unit.md
│   └── tests/
│       ├── test_cost.py
│       ├── test_env.py
│       ├── test_ingest.py
│       ├── test_precommit_hook.py
│       ├── test_query.py
│       └── test_run_eval.py
│
└── _handoffs/
    ├── claude-code-rag-vers-claude-code-content/
    │   ├── reponse-coordination-vague-b-c-2026-05-29.md  (handoff Option A)
    │   ├── reponse-brief-vague-c-2026-05-29.md           (Option B 5 amendements)
    │   └── accuse-reception-bundle-1-2026-05-29.md       (Bundle C#1 ack + smoke test)
    ├── claude-code-rag-vers-hub-strat/
    │   ├── accuse-reception-brief-vague-b-2026-05-28.md  (ack brief Vague B FINAL)
    │   ├── inventaire-migration-hub-ia-vers-strategie-ia-vague-b.md  (§3.1 obligatoire)
    │   └── instructions-cavalli-vague-a.md               (Vague A safety)
    └── coordination-cc-content-cc-rag/
        └── coordination-bidirectionnelle.md              (v1.1 — 13 entrées + 2 appends RAG)
```

## 3. Filtre — ce qui n'est PAS inclus (volontairement)

| Catégorie exclue | Justification |
|---|---|
| Sprints S1 / S1bis / S1ter / S2.1 / S2.2 / S2.3 / S2.4 / S2.5 | Arbitrage Cavalli 28/05 « capitalisation sur livrables finaux S2.6-S2.9 » |
| Drafts (DRAFT-BRIEF-CC-S2.2.md, ARBITRAGE-COWORK-SPEC-v1.4.md) | Brouillons intermédiaires |
| Sondages D-026 (DRAFT-SONDAGE-*, RETOUR-SONDAGE-*) | Matière éditoriale Cowork → relève `08-contenu-editorial/` (vague ultérieure Hub Content) |
| Retex Cowork (RETEX-COWORK-*, RETOUR-I-001/002/003) | Matière interne Cowork → relève `11-gouvernance/retex/` (vague ultérieure Hub Strat) |
| Sous-sets golden questions-s2.X-*.yaml (10 fichiers) | Contournements bug `--filter-unit` désormais corrigé S2.9 (PR #108 hub-ia) |
| Eval reports bruts `rag/eval/eval-report-s2.X-*.{md,json,txt}` (~30 fichiers) | Données brutes — la synthèse vit dans les RAPPORT-CC migrés. **Exception** : `eval-report-s2.9-COMPARATIF.md` migré (clé pour ADR-001 + ADR-002) |
| Vault MD `rag/content/` (38 MD) | Relève `08-contenu-editorial/hub-ia-learning-center/` — vague ultérieure Hub Content |
| `rag/code/audit/__pycache__/` etc. | Binaires Python générés |

## 4. ADR drafts — état et conditions de finalisation

Les 5 ADR sont livrés en **skeleton draft** (statut `proposed`). Sourcing empirique solide (RAPPORT-CC-S2.7/S2.8/S2.9 + RETEX Hub Strat + CONVENTIONS v1.1). Finalisation prévue PR 6 Vague B (J+15 = 2026-06-18) si la nouvelle cohorte d'agents reprend la mission.

| ADR | Statut | Conditions finalisation `accepted` |
|---|---|---|
| ADR-001 LLM Haiku baseline | `proposed` | **Arbitrage Cavalli** (cohérence promesse Pro tier + routing premium) |
| ADR-002 BM25 hybrid RRF | `proposed` | Lot Dev S2.10 Plateforme pour porter `bench_runner_hybrid.py` en module production |
| ADR-003 Frontmatter YAML 10 champs | `proposed` (rétrospectif) | Validation Hub Content + Hub RAG (déjà effectif depuis S1 — formalité) |
| ADR-004 Stack Variante A MVP | `proposed` | **Arbitrage Cavalli** (post-IP statut side project + accord souveraineté Hub Strat) |
| ADR-005 Conventional Commits + branch protection | `proposed` (partiellement effectif) | Activation branch protection Cavalli + confirmation Hub Strat |

**Si la nouvelle cohorte ne prend pas la suite immédiatement**, les drafts restent `proposed` et peuvent être :
- Reformulés librement (skeleton n'est pas un engagement définitif)
- Décomposés en plusieurs ADR si trop large
- Supersédés par d'autres décisions

## 5. Étanchéité QFC

Vérification effectuée : **aucun fichier du correctif ne contient de mention nominale Quai Alpha, QFC, ou startups réelles incubées**.

Le périmètre migré est exclusivement **technique RAG + handoffs internes Cowork** — pas de matière commerciale, juridique ou IP exposable.

Discipline `_instructions.md` Hub Strat règle 1 respectée.

## 6. Hygiène merge

Vérification effectuée localement (`git grep "<<<<<<<"` sur le périmètre `correctif-final/`) :

- Aucun marqueur de conflit `<<<<<<<` dans le code source migré
- Les mentions de la règle elle-même (dans SPEC v2.3, RAPPORT-CC-S2.5+) sont des références documentaires, pas des marqueurs réels — détectables par `git grep "^<<<<<<<"` qui retourne vide
- Job CI `check-merge-markers` (workflow Vague A safety inclus) validera automatiquement post-push

## 7. Régimes PR proposés à Cavalli

Suggestion de découpage pour pousser le correctif (Cavalli peut découper différemment) :

| PR | Régime | Contenu | Reviewer |
|---|---|---|---|
| **PR 1** | R4 hors PR | `_handoffs/*` (8 MD) | Pas de relecture — matière éphémère |
| **PR 2** | R2 fast-track tech | `09-rag-et-ia/pipeline-ingestion/*` (8 PY) + `09-rag-et-ia/tests/*` (6 PY) + `09-rag-et-ia/golden-set/questions.yaml` | Hub RAG (croisé) + Hub Strat |
| **PR 3** | R2 fast-track tech | `09-rag-et-ia/evaluations/*` (7 fichiers) + `09-rag-et-ia/sprints/{s2-6,s2-7,s2-8,s2-9}/*` (7 MD) | Hub RAG + Hub Strat |
| **PR 4** | R2 fast-track tech | `07-tech-et-architecture/qualite-et-tests/*` (2 PY + 2 PY tests) + `07-tech-et-architecture/spec-md-rag/spec-md-pour-rag-v2-3.md` + `07-tech-et-architecture/qualite-et-tests/integration/*` (4 fichiers) | Hub RAG + Hub Strat |
| **PR 5** | R1 standard | `09-rag-et-ia/adr/*` (3 ADR drafts) + `07-tech-et-architecture/adr/*` (2 ADR drafts) | Hub RAG (ADR-001/002/003) + Hub Strat (ADR-004/005) + **arbitrage Cavalli ADR-001 + ADR-004** |
| **PR 6** (optionnel) | R3 fast-track mineur | `.github/workflows/audit-conformity.yml` + `07-tech-et-architecture/deploiement/ci-cd/*` (safety re-include — skip si déjà mergé Vague A) | Auto-approve owner si CI OK |

**Cadence proposée** : tout pousser sur une fenêtre courte (24-48h post-shutdown) pour ne rien perdre, quitte à différer la relecture profonde des ADR drafts à la nouvelle cohorte.

## 8. Notes critiques pour la nouvelle cohorte d'agents

### 8.1 Ce qui n'a PAS été fait (mais devait l'être Vague B PR 1-6)

- **Adaptations imports** dans le code Python migré : `from rag.code...` → `from strategie_ia...` ou équivalent (dépend du package layout choisi en `strategie-ia`). À traiter en pré-merge ou en post-merge avec test pytest.
- **Vérification chemin webServer** dans `playwright.config.ts` : calculé sur 4 levels up depuis `07/qualite-et-tests/integration/`. À ajuster si la profondeur réelle diffère.
- **Tests pytest** non exécutés en environnement strategie-ia (la matière vient de hub-ia, les tests passent côté hub-ia 243/243). Pré-merge run recommandé.
- **README de catégorie** `09-rag-et-ia/README.md` et `07-tech-et-architecture/README.md` non touchés — les versions Vague A devraient être maintenues si elles existent, sinon à compléter avec liens vers les nouveaux sous-dossiers.

### 8.2 Décisions Hub Strat en attente

3 décisions demandées dans `_handoffs/claude-code-rag-vers-hub-strat/accuse-reception-brief-vague-b-2026-05-28.md` §4 (défauts pris si silence J+9) :
1. Confirmation « audit-global.py » = `audit_md_rag.py` (migré tel quel ici)
2. Optimisation regroupement 5 ADR en 1 PR R1 finale (j'ai groupé tous les drafts dans le même dossier ADR du correctif)
3. Statut ADR-003 Frontmatter : **rétrospectif** (default appliqué — référence SPEC v2.3 effective depuis S1)

### 8.3 Engagements RAG en suspens (non réalisés faute de shutdown)

Tous reportés à la nouvelle cohorte :
- Vague B PR 1-6 (J+10 → J+15 = 8 → 18 juin 2026) — entiers
- Contributions Vague C (19-24 juin) : baseline web vitals + composants conversation Playwright tests + Lighthouse CI + extension smoke test
- Note de retour Vague B (J+15)
- Note de retour Vague C contribs (~J+20)

### 8.4 Pattern à perpétuer

- **Hygiène merge** : `git grep "<<<<<<<"` vide pre-`git add`, désormais automatisée par job CI `check-merge-markers`
- **VALIDATION-SCORING obligatoire** (SPEC v2.2) avant tout rejeu eval avec une nouvelle règle de scoring (cas-école S2.7 0/12 → 12/12 + cas-école S2.9 `--filter-unit`)
- **Coordination append-only** `_handoffs/coordination-cc-content-cc-rag/coordination-bidirectionnelle.md` à continuer si pertinent — pattern ad-hoc en attendant `12/coordination/STATUS-CLAUDE-CODE.md` structurel DEV IA Head
- **Lot Dev Plateforme dès démarrage** (SPEC v2.3 §allocation D-030) — 3 sprints consécutifs validés (S2.7 adversarial + S2.8 R11 + S2.9 --filter-unit) côté hub-ia

## 9. Suite si shutdown intervient avant push complet

Au cas où Cavalli ne peut pas pousser le correctif intégralement avant shutdown :

**Priorité 1 — sans quoi tout est perdu** :
- `09-rag-et-ia/pipeline-ingestion/*` (code production RAG, source unique de vérité)
- `09-rag-et-ia/golden-set/questions.yaml` (canonical eval matter)
- `_handoffs/*` (continuité projet)
- `07-tech-et-architecture/spec-md-rag/spec-md-pour-rag-v2-3.md` (SPEC canonique)

**Priorité 2 — utile mais reconstructible** :
- `09-rag-et-ia/tests/*` + `07-tech-et-architecture/qualite-et-tests/tests/*` (regenerable mais fastidieux)
- `09-rag-et-ia/evaluations/*` (RAPPORT-CC + audit R11)
- `09-rag-et-ia/sprints/*` (briefs + validation-scoring)

**Priorité 3 — facilement reformable** :
- ADR drafts (5 skeletons — peuvent être réécrits sur la base des RAPPORT-CC migrés)
- `.github/workflows/` + `07/deploiement/ci-cd/` (Vague A safety, déjà mergée probablement)

## 10. Coordination

- **Cavalli** : pousse le correctif sur `main` selon le découpage §7 (ou adapté)
- **Hub Strat** : relit le présent README + matière migrée, valide la cohérence avec FRONTIERES.md v1.0
- **Hub RAG** : reviewer croisé R2 sur 09/* et 07/qualite-et-tests/* — peut **finaliser les ADR-001/002/003** drafts si la nouvelle cohorte tarde
- **DEV IA Head** : trace dans son post-mortem D-031 enrichi (Vague B avortée pour cause de shutdown) + transmet l'historique coordination append-only à la nouvelle cohorte

## 11. Annexes

### 11.1 Liens vers les ressources hub-ia (source de vérité jusqu'à janv 2027)

Le repo `LumenBot/hub-ia` reste actif jusqu'à l'archivage post-Étape 4 (janvier 2027). Toute la matière migrée ici est **isomorphe** au contenu hub-ia, ce qui permet à la nouvelle cohorte de cross-vérifier en cas de doute :

- Code prod : `hub-ia/rag/code/` (15 PY) → ici `09/pipeline-ingestion/` + `09/tests/` + `07/qualite-et-tests/`
- Rapports : `hub-ia/rag-prep/reports/` → ici `09/evaluations/`
- Briefs : `hub-ia/rag-prep/briefs/` (filtré S2.6→S2.9) → ici `09/sprints/`
- SPEC : `hub-ia/rag-prep/SPEC-MD-POUR-RAG.md` → ici `07/spec-md-rag/`
- Eval comparatif : `hub-ia/rag/eval/eval-report-s2.9-COMPARATIF.md` → ici `09/evaluations/`

### 11.2 Versions et tests hub-ia (état au shutdown)

- Suite tests hub-ia : **243/243 verts** (run S2.9 PR #108)
- Sprint clôturé : S2.9 (RAPPORT-CC-S2.9 mergée PR #112)
- Vault hub-ia : 38 MD / 444 chunks (post-vague 8 architectures)
- Coût cumulé S1→S2.9 : ~16,34 $ Anthropic (cap mensuel D-013 50 $ respecté)
- Findings clés : robustesse RAG 103/104 std + 14/14 adv, BM25 hybrid résout AP-8, Haiku 4.5 -76 % coût qualité préservée

---

## Historique

| Date | Version | Modification |
|------|---------|--------------|
| 2026-05-29 | v1.0 | Création du correctif final pré-shutdown — inventaire 60 fichiers sur 5 dossiers cibles + 5 ADR skeleton drafts + 8 handoffs + safety re-include Vague A/C. Étanchéité QFC vérifiée. Hygiène merge OK. 6 PR proposées à Cavalli (R1/R2/R3/R4). Notes critiques nouvelle cohorte §8. Priorisation §9 si push partiel. |

---

*Correctif final Claude Code RAG → strategie-ia, 29 mai 2026. Bundle pré-shutdown — dernière occasion de migrer. Complétude > perfection. Régime mixte R1/R2/R3/R4. Transmis via Cavalli intermédiaire Git, cc Hub Strat + DEV IA Head pour traçage post-shutdown.*
