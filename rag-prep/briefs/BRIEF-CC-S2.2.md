# BRIEF-CC-S2.2 — Brique pattern-llm-wiki + extension golden set + métriques + pre-commit

**Statut :** v1 finalisé post-v3.9 + SPEC v1.4 — prêt à transmettre
**Émetteur :** Cowork Hub IA Plateforme
**Destinataire mixte (D-030)** :
- Cowork (production MD pattern-llm-wiki + extension golden set questions)
- Claude Code Plateforme (métriques coût + pre-commit hook + enrichissement system prompt)
- Claude Code Desktop (exécution eval extended sur 30 questions)

**Sprint :** S2.2 — préparation production vague 3
**Prérequis :** S2.1 mergé (audit v2 opérationnel) + itération couple 1 terminée (pour synchronisation éditoriale)

---

## 1. Métadonnées

- **Repo cible :** `hub-ia` (partir de `main` post-merge PR #45)
- **Sprint précédent :** S2.1 (audit v2 livré, 0 erreur + 183 warnings catégorisés)
- **Nature de l'itération :** consolidation pré-vague 3 — extraire la première brique transverse (LLM Wiki), étendre l'eval (10→30 questions), instrumenter les coûts, renforcer la discipline pre-commit
- **Coût API attendu** : Cowork 0 $ (production MD pure), Plateforme 0 $ (refactor + tests), Desktop ~0,30-0,50 $ (eval sur 30 questions vs 10)

---

## 2. Contexte court

Vague 3 (modules CU-026, CU-027, DEP-08) imminente. Avant production, 3 préparatifs structurels :

1. **Extraire `pattern-llm-wiki.md`** : recouvrement cu-008 ↔ dep-02 déjà confirmé en revue I-003 (~30-40 lignes dupliquées). Sans extraction, la vague 3 va aggraver le recouvrement (cu-014 et cu-025 référenceront aussi LLM Wiki). Extraction urgente — D-025 actée.
2. **Extension golden set 10 → 30 questions** : audit-report-s2.1 a 134/134 tests verts sur 10 questions, mais 10 c'est trop peu pour valider la robustesse sur un vault élargi (vague 3 portera le vault à 12 fichiers, donc ~50 % de plus). 30 questions couvrent mieux les nouveaux modules.
3. **Métriques de coût + pre-commit hook** : recommandation RAPPORT-CC-S2.1 §7 + RAPPORT-CC-S1ter §7 (récurrente). Garde-fous pour vague 3 et au-delà.

---

## 3. Préalable obligatoire (lectures avant exécution)

À lire dans cet ordre :

1. **RAPPORT-CC-S2.1** (`rag-prep/briefs/RAPPORT-CC-S2.1.md`) — bilan audit v2 + 3 propositions d'amendement SPEC v1.4
2. **ARBITRAGE-COWORK-SPEC-v1.4** (`rag-prep/briefs/ARBITRAGE-COWORK-SPEC-v1.4.md`) — arbitrages Cowork sur les 3 propositions
3. **SPEC-MD-POUR-RAG.md v1.4** (si actée par Cowork à la reprise) ou v1.3 sinon
4. **STATUS-RAG.md** + **JOURNAL-POC-RAG.md** post-reprise itération couple 1
5. **DECISIONS-RAG.md** — 30 décisions actées (focus D-025 pattern transverses, D-026 co-production légère, D-030 allocation hybride)
6. **cartographie-rag.md** — entrées actuelles du vault + recouvrements identifiés (pattern-llm-wiki déjà flagué urgent)

**Audit de départ obligatoire** (D-018) : `git fetch && git status` sur `hub-ia`. Vérifier que main inclut le merge PR #45 et tout commit issu de l'itération couple 1.

---

## 4. Méthode — 4 lots, allocation D-030 hybride

### Lot S2.2.A — Production pattern-llm-wiki.md + refactor wikilinks (Cowork)

**Acteur principal** : Cowork Hub IA Plateforme (peut éventuellement solliciter Cowork Hub IA pour validation contextuelle des nuances éditoriales — D-026 sondage léger)

**Livrables** :
1. `rag/content/transverses/pattern-llm-wiki.md` (~120-180 lignes selon le pattern brique transverse type vigilance-hallucinations.md) — distillation du pattern LLM Wiki Karpathy + 5 patterns post-Karpathy (persistent memory, self-maintaining KB, contradiction detection, multi-agent vaults, sleep consolidation) actuellement dupliqués entre cu-008 et dep-02
2. **Refactor cu-008.md** : remplacer les sections « Au-delà du RAG classique » et « Patterns LLM Wiki post-Karpathy » par un renvoi `[[pattern-llm-wiki]]` + résumé court (3-4 lignes)
3. **Refactor dep-02.md** : remplacer la section « LLM Wiki Karpathy — alternative pour petits corpus » par un renvoi `[[pattern-llm-wiki]]` + résumé court
4. Mise à jour `cartographie-rag.md` avec nouvelle entrée pattern-llm-wiki + correction recouvrements
5. Retirer `pattern-llm-wiki` de `whitelist-wikilinks-futurs.md` (puisque maintenant produit)

**Critères de succès** :
- pattern-llm-wiki.md respecte SPEC v1.4 (ou v1.3 si v1.4 pas encore actée) : frontmatter 10 champs, H2 autonomes, wikilinks vers glossaire et chiffres-macro
- cu-008.md et dep-02.md restent éditorialement complets après refactor (résumé court suffit pour la cohérence narrative)
- Audit v2 passe sur le vault de 12 fichiers (9 originaux + 3 modifiés rétrofittés... attendre, c'est plutôt 10 fichiers : 9 originaux + 1 nouveau pattern-llm-wiki ; cu-008 et dep-02 sont refactorés, pas nouveaux)

**Pas de commit Claude Code sur ce lot** — c'est de la production MD côté Cowork. Le commit sera fait par Blaise lors de la sync ascendante post-Lot A.

---

### Lot S2.2.B — Extension golden set 10 → 30 questions (Cowork + Claude Code Plateforme)

**Acteur Cowork** : produit 20 nouvelles questions dans `rag/eval/questions.yaml`, en couvrant :
- 4 questions sur `cu-001.md` (Recherche & veille) — au-delà des 2 actuelles
- 4 questions sur `cu-008.md` (Knowledge base RAG) — au-delà des 2 actuelles
- 4 questions sur `pr-07.md` (Build vs Buy) — au-delà des 2 actuelles
- 4 questions sur `dep-02.md` (RAG en production) — au-delà des 2 actuelles
- 2 questions sur `outils-vector-db.md` — au-delà des 2 actuelles
- 2 questions sur les 3 briques transverses (1 vigilance-hallucinations + 1 vigilance-confidentialite + 1 chiffres-macro-2026 + 1 pattern-llm-wiki)

Chaque question doit suivre le pattern `id / question / expected_sources / expected_concepts` du golden set initial.

**Acteur Claude Code Plateforme** : vérifie via dry-run que les 30 questions sont bien parsables par `run_eval.py` (sans appel API). Pas de changement de code, juste validation.

**Commit attendu côté Cowork (via Blaise)** : `feat(rag-eval): extension golden set 10 → 30 questions (s2.2 lot B)`.

---

### Lot S2.2.C — Métriques de coût + pre-commit hook + system prompt enrichi (Claude Code Plateforme)

**Acteur** : Claude Code Plateforme (session web, refactor code + tests mockés)

**Livrables** :

1. **Métriques de coût instrumentées** dans `query.py` et `ingest.py` :
   - À chaque appel API, logger le nombre de tokens input/output + coût estimé (tarif par M de tokens × volume)
   - Sortie dans `rag/code/.cost-log.jsonl` (gitignored)
   - Format JSONL : `{"timestamp", "script", "model", "tokens_in", "tokens_out", "cost_usd"}`
   - Cumul affiché en fin d'exécution (`run_eval.py` notamment)
2. **Pre-commit hook** dans `.githooks/pre-commit` (à activer manuellement par Blaise via `git config core.hooksPath .githooks`) :
   - Exécute `audit-md-rag.py --vault rag/content` avant chaque commit qui touche `rag/content/**.md`
   - Bloque le commit en cas d'erreur (warnings tolérés sauf si CI durcie)
3. **Enrichissement system prompt** dans `query.py` :
   - Mentionner explicitement les briques transverses comme sources préférées (vigilance-*, chiffres-macro-*, pattern-*)
   - Mentionner la convention wikilinks Obsidian `[[code]]` comme citation préférée (pas en clair)
   - Tests : vérifier que le system prompt contient bien les nouvelles mentions

**Critères de succès** :
- Tests : 134 originaux + ~10-15 nouveaux verts (estimés)
- `.cost-log.jsonl` produit lors d'un dry-run avec mocks (sans vrais appels API en S2.2.C)
- Pre-commit hook fonctionne en simulation locale (test bash sur fixtures)

**Commit attendu** : `feat(rag): métriques coût + pre-commit hook + system prompt enrichi (s2.2 lot C)`.

---

### Lot S2.2.D — Exécution eval extended (30 questions) sur le vault enrichi (Claude Code Desktop)

**Acteur** : Claude Code Desktop (local sur Mac de Blaise, accès `.env` et clés API)

**Livrables** :
1. `python3 rag/code/eval/run_eval.py --questions rag/eval/questions.yaml --report rag/eval/eval-report-s2.2.md --json rag/eval/eval-report-s2.2.json` sur le vault enrichi (10 fichiers avec pattern-llm-wiki)
2. Cible : **≥ 24/30 sources retrouvées** (équivalent 8/10), **≥ 50 %** concepts couverts
3. Vérification métriques coût : le `.cost-log.jsonl` doit contenir 30 entrées avec coût total < **0,50 $** (durci par rapport à l'estimation)

**Commit attendu côté Blaise** : `feat(rag-eval): eval extended 30 questions sur vault enrichi (s2.2 lot D)`.

---

### Lot S2.2.E — RAPPORT + PR (Claude Code Plateforme ou Desktop selon Blaise)

**Livrable A** : `rag-prep/briefs/RAPPORT-CC-S2.2.md` (~1500 mots, structure modèle 8 sections incluant résultats eval extended)

**Livrable B** : PR vers main avec titre `feat(rag): Sprint S2.2 - pattern-llm-wiki + extension golden set 30q + métriques + pre-commit`

---

## 5. Estimation effort consolidée

| Lot | Acteur | Effort estimé |
|---|---|---|
| A — pattern-llm-wiki + refactor | Cowork | 2-3 h Cowork (avec validation Cowork Hub IA si sollicitée — D-026) |
| B — Extension golden set 30q | Cowork | 1-2 h Cowork |
| C — Métriques + pre-commit + prompt | Claude Code Plateforme | 2-3 h |
| D — Eval extended local | Claude Code Desktop | 30 min + ~0,30-0,50 $ API |
| E — RAPPORT + PR | Claude Code Plateforme ou Desktop | 1 h |
| **Total** | — | **~7-10 h split entre Cowork, Plateforme, Desktop** |

---

## 6. Règles de prudence (S2.2)

1. **Pas de modification des MD du vault par Claude Code** (D-022). Toute production MD est rôle Cowork. Claude Code Plateforme peut **lire** le vault pour les tests de regex prompt enrichi, jamais l'éditer. Si l'audit-md-rag détecte un écart sur les MD post-S2.2 → signaler à Blaise sans corriger.
2. **Pas de modification des fichiers de gouvernance** dans `rag-prep/` (sauf `JOURNAL-POC-RAG.md`, `STATUS-RAG.md`, et tes propres rapports `briefs/RAPPORT-CC-S2.2.md`).
3. **Plafonds API durcis pour S2.2 Lot D** (eval extended sur 30 questions) : alerte > **0,50 $ Anthropic** + > **0,15 $ OpenAI** (vs 0,30/0,10 brief S1ter). Crédits disponibles : ~2,70 $ Anthropic + ~4,70 $ OpenAI (post-S1c.2). Marge confortable mais discipline maintenue.
4. **Pas de re-ingestion exhaustive** : le vector store ChromaDB contient déjà les 107 chunks indexés en S1c.2 (+ ce qui sera ajouté pour `pattern-llm-wiki.md` après production Cowork du Lot A). Re-indexation incrémentale uniquement.
5. **Limiter les retries** : pas plus de 2 tentatives par question en cas d'erreur API. Au-delà, signaler à Blaise sans re-itérer en boucle.
6. **Coordination entre lots** : ne pas commencer Lot D (eval extended) avant que les Lots A et B soient committés et que les MD pattern-llm-wiki + les 20 nouvelles questions soient présents sur la branche.

---

## 7. Décisions explicites de NE PAS faire dans ce sprint

1. ❌ Pas de production de modules CU/PR/DEP (rôles Cowork S2.3 vague 3 et S2.5 vague 3.5)
2. ❌ Pas de portage TypeScript / Cloudflare Worker (livrable S3)
3. ❌ Pas de capture feedback Supabase (livrable S3)
4. ❌ Pas d'extension de la whitelist wikilinks futurs (entretien Cowork lors de la production des modules)
5. ❌ Pas de modification du code de l'audit-md-rag v2 (audit v3 reporté post-vague 3, cf. SPEC v1.4 roadmap)
6. ❌ Pas de merge automatique de la PR (Blaise valide manuellement côté GitHub)
7. ❌ Pas de canonisation de nouveaux chiffres macro dans S2.2 (déjà 22 chiffres dans `chiffres-macro-2026.md` v3.8.5 post-v3.9 — suffit pour les 20 nouvelles questions du golden set)

---

## 8. Validation finale avant clôture S2.2

Checklist à exécuter avant d'ouvrir la PR :

**Lot A (Cowork production MD)** :
- [ ] `rag/content/transverses/pattern-llm-wiki.md` produit (~120-180 lignes, conformité SPEC v1.4)
- [ ] `rag/content/modules/cu-008.md` refactoré (sections « Au-delà du RAG classique » + « Patterns LLM Wiki post-Karpathy » remplacées par renvoi `[[pattern-llm-wiki]]` + résumé court). Bump version v3.8.5 → v3.8.6.
- [ ] `rag/content/deploiement/dep-02.md` refactoré (section « LLM Wiki Karpathy » remplacée par renvoi `[[pattern-llm-wiki]]` + résumé court). Bump version v3.8.5 → v3.8.6.
- [ ] `cartographie-rag.md` mis à jour avec entrée `pattern-llm-wiki` + correction recouvrements cu-008/dep-02
- [ ] `whitelist-wikilinks-futurs.md` : retrait du code `pattern-llm-wiki` (puisque produit)
- [ ] Audit-md-rag v2 passe sur le vault enrichi : **0 erreurs** attendues

**Lot B (Cowork production questions + validation parsing CC)** :
- [ ] `rag/eval/questions.yaml` étendu à 30 questions (10 originales + 20 nouvelles selon répartition §4 Lot B)
- [ ] `rag/eval/golden-answers.yaml` étendu en miroir (20 nouvelles réponses attendues)
- [ ] Dry-run de parsing Claude Code Plateforme : `python3 rag/code/eval/run_eval.py --dry-run` valide les 30 questions (sans appel API)

**Lot C (Claude Code Plateforme refactor + tests)** :
- [ ] `python-dotenv` toujours OK (régression check)
- [ ] Métriques de coût instrumentées dans `query.py` et `ingest.py` (sortie `.cost-log.jsonl`)
- [ ] `.gitignore` étendu pour exclure `rag/code/.cost-log.jsonl`
- [ ] Pre-commit hook `.githooks/pre-commit` produit, testable via simulation locale
- [ ] System prompt `query.py` enrichi (mention briques transverses + wikilinks préférés)
- [ ] Tests : 134 originaux + ~10-15 nouveaux verts (~145+ tests total)

**Lot D (Claude Code Desktop eval extended)** :
- [ ] `python3 rag/code/eval/run_eval.py` sur les 30 questions du golden set
- [ ] **≥ 24/30 sources retrouvées** (équivalent 80 % cible 8/10)
- [ ] ≥ 50 % concepts attendus couverts par question
- [ ] Coût accumulé < **0,65 $** total (Anthropic + OpenAI)
- [ ] `rag/eval/eval-report-s2.2.md` + `.json` produits

**Lot E (rapport + PR)** :
- [ ] `RAPPORT-CC-S2.2.md` produit en 8 sections
- [ ] PR ouverte avec titre conforme
- [ ] `JOURNAL-POC-RAG.md` mis à jour (append S2.2)
- [ ] `STATUS-RAG.md` mis à jour (S2.2 ✅, S2.3 prêt à transmettre sondage couple 1)

---

## 9. Fichiers de référence

**Référentiels du couple 2** (tous dans `rag-prep/` du clone Git) :
- `_instructions-rag.md` v1
- `DECISIONS-RAG.md` (30 décisions actées, focus D-025 briques transverses + D-026 co-production légère + D-030 architecture hybride)
- `SPEC-MD-POUR-RAG.md` **v1.4** (10 règles + 9 anti-patterns + R6 warning par défaut codifié + roadmap audit v3 enrichie R11)
- `STRATEGIE-MD-RAG.md` v1
- `cartographie-rag.md` (9 entrées vault à jour)
- `whitelist-wikilinks-futurs.md` (69 codes whitelistés — à mettre à jour au Lot A en retirant `pattern-llm-wiki`)
- `STATUS-RAG.md` (sprint S2.2 ouvert)
- `JOURNAL-POC-RAG.md`
- `SYNC-INTER-CANAUX.md` (4 archivés dont I-D-004 nouveau, 2 descendants ouverts I-D-001 et I-D-002)
- `briefs/RAPPORT-CC-S1.md` + `RAPPORT-CC-S1bis.md` + `RAPPORT-CC-S1ter.md` + `RAPPORT-CC-S2.1.md` (tes rapports précédents)
- `briefs/ARBITRAGE-COWORK-SPEC-v1.4.md` (3 arbitrages SPEC v1.4 actés)

**Référentiels du vault à connaître** :
- `rag/content/transverses/chiffres-macro-2026.md` **v3.8.5** (22 chiffres canoniques post-v3.9 — utilisable pour les nouvelles questions du golden set)
- `rag/content/transverses/vigilance-hallucinations.md` (référencée par les nouvelles questions sécurité)
- `rag/content/transverses/vigilance-confidentialite.md`

**Contact** : Blaise Cavalli (garant transverse). Toute question, blocker, ou écart par rapport au brief remonte via lui.

---

*Brief finalisé le 12 mai 2026 post-intégration v3.9 + SPEC v1.4. Allocation D-030 hybride confirmée : 3 acteurs Cowork + Plateforme + Desktop selon les 4 lots. Cible eval extended : ≥ 24/30 sources retrouvées, coût < 0,65 $.*
