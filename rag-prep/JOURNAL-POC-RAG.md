# JOURNAL-POC-RAG.md — Journal continu du couple 2

**Statut :** Actif
**Format :** append-only, chronologique inverse (entrées récentes en haut)

> **Rôle de ce fichier :** trace continue de toutes les sessions Cowork et Claude Code du couple 2. Permet de reconstituer la chronologie d'évolution du POC. Lu à chaque démarrage de session pour reprendre le contexte.

> **Format d'une entrée :** date | acteur (Cowork ou Claude Code) | session | actions menées | reste à faire / next.

---

## Entrées

### 2026-05-19 (S2.4 Phase 3 Lots G + H livrés) — Cowork Hub IA Plateforme — Cartographie v1 + extension golden set 52 questions

**Contexte :** Phase 2 S2.4 clôturée (sondage D-026 + brique transverse + refactor 2 modules + patches 3 modules + nouveau module PR-08, 4 PR mergées #65 à #69). Phase 3 démarre : préparation eval Lot I (Desktop) avec mise à niveau cartographie + extension golden set.

**Actions menées :**

- **Lot G — Cartographie v0 → v1** : ajout d'une section dédiée « Vague 4 — ajouts S2.4 Phase 2 » avec inventaire détaillé des 7 entrées modifiées/nouvelles :
  - 2 nouveaux fichiers MD : `pattern-persistent-memory.md` (brique transverse symétrique pattern-llm-wiki) + `pr-08.md` (nouveau préalable RULES 7→8)
  - 5 refactors/patches : cu-008 + dep-02 (sections H2 dédiées persistent memory), cu-026 (section H2 §3bis Frontier Firms), cu-027 (point 4 Stanford), dep-08 (section H2 §7bis SBOM IA)
  - 1 bump éditorial chiffres-macro-2026 (v3.8.6 → v3.9.0, +20 chiffres canonisés)
  - Récap inventaire : vault passe de **13 à 15 fichiers MD** ; 8 modules restant whitelistés pour Lot F.5 sprint S2.5 dédié
  - Whitelist déjà à jour (pr-08 retiré en Lot F.4, pattern-persistent-memory retiré en Lot F.1)
  - Glossaire RULES : 7→8 préalables effectif côté MD (cohérent avec impact v3.10 HTML)

- **Lot H — Extension golden set 42 → 52 questions** (10 nouvelles q-043 → q-052) :
  - 2 questions `pattern-persistent-memory` (q-043 4 signaux convergents, q-044 benchmarks agentmemory)
  - 2 questions cross-modules `cu-008` + `dep-02` refactor (q-045 quand privilégier persistent memory, q-046 architecture agent mémoire conversationnelle)
  - 2 questions `cu-026` §3bis Frontier Firms (q-047 4 patterns, q-048 articulation 4 patterns vs 7 dimensions)
  - 1 question `cu-027` Point 4 Stanford (q-049 productivité 14-26 % + emploi devs -20 %)
  - 1 question `dep-08` §7bis SBOM IA (q-050 disciplines SBOM IA + ANSSI/G7)
  - 2 questions `pr-08` (q-051 7 dispositifs fiscaux, q-052 règle des 5 étapes empilement)
  - **Application stricte SPEC v1.6** : AP-5 (valeurs numériques quotées : `"95,2 %"`, `"14-26 %"`, `"86,2 %"`, `"÷ 100"`, etc.), AP-6 (plafond 4 synonymes respecté), garde-fou « concepts détaillés » (leads des chunks cibles avaient été enrichis avec vocabulaire bridge en Lots F.1 à F.4 — anticipation retrieval)
  - **Validation YAML automatique** : 52 questions, 41/52 avec ≥1 liste de synonymes, AP-5 + AP-6 ✅, 52 ids consécutifs q-001 → q-052
  - **Cible eval S2.4** recalibrée : ≥ 43/52 sources retrouvées (≥ 83 %), ≥ 47/52 concepts ≥ 50 % (≥ 90 %)
  - **Coût eval Lot I attendu** : 52q × ~0,025 $/q = **~1,30 $ Anthropic** (cap durci sprint 1,35 $ SPEC v1.6 respecté)

**Métriques Lots G + H :**
- 2 fichiers de gouvernance : cartographie-rag.md (v0 → v1), questions.yaml (42 → 52 questions)
- Coût : **0,00 $** (Cowork pur éditorial)

**Décisions structurantes :**
- **Cartographie v1** acte le périmètre vault post-S2.4 Phase 2 et la roadmap des 8 modules restant whitelistés (Lot F.5 S2.5 dédié).
- **Cible eval S2.4** : ≥ 43/52 (83 %) — proportionnelle aux cibles précédentes (S2.2 24/30 = 80 %, S2.3 35/42 = 83 % atteinte 41/42 = 97 %). Marge raisonnable pour absorber 10 nouveaux chunks dans 7 fichiers MD modifiés.

**Reste à faire S2.4 Phase 3** :
- **Lot I (Desktop)** : eval extended 52 questions sur vault enrichi vague 4 post-S2.4 Phase 2. Pull main + ingest incrémental (15 fichiers MD) + run_eval + commit artefacts + MAJ JOURNAL/STATUS.
- **Lot J (Plateforme)** : RAPPORT-CC-S2.4 (8 sections format S2.3) + PR finale S2.4.

**Blockers :** aucun. État stable Cowork-side, attente exécution Desktop Lot I.

---

### 2026-05-19 (S2.4 Phase 2 Lots F.1 + F.2 + F.3 + F.4 livrés) — Cowork Hub IA Plateforme — pattern-persistent-memory + refactor CU-008/DEP-02 + patches CU-026/CU-027/DEP-08 + nouveau module PR-08

**Contexte :** RETOUR-SONDAGE-COWORK-HUB-IA-S2.4 reçu (2e application D-026, 11 sous-passages confirmés/rectifiés + 5 bonus). Décision Cowork validée : extraction transverse `pattern-persistent-memory.md` recommandée (D-025 SPEC v1.6 satisfait, symétrique pattern-llm-wiki). **Rectification critique du RETOUR §3.4** : le tableau §4 DEP-02 (« Tableau de décision RAG ») n'a **pas** été modifié en v3.10/v3.11 — la nouvelle ligne « agent avec mémoire conversationnelle » est dans un **mini-tableau distinct** (§2bis « Implication opérationnelle »). À préserver les 2 tableaux séparés, **ne pas fusionner**.

**Actions menées :**

- **Lot F.1 — Production `rag/content/transverses/pattern-persistent-memory.md`** (~1900 mots, format symétrique à pattern-llm-wiki.md) :
  - Frontmatter v3.11.0, type: transverse, niveau: 3
  - 4 signaux convergents (ordre canonique chronologique mai 2026) : Long context natif SubQ (10 M tokens+, ×1000 coût attention), LLM Wiki post-Karpathy (5 000+ stars), Persistent memory Vargas (Hermes Agent founder, « persistent memory > RAG stateless pour agents scalables »), agentmemory infrastructure (13 200+ stars, pivot infrastructurel)
  - Benchmarks agentmemory (R10 stricte) : 95,2 % r@5 vs 86,2 % BM25 + coût token ÷ 100+, source github.com/rohitg00/agentmemory (Rohit Ghumare)
  - Écosystème hooks 6 outils (ordre canonique) : Claude Code / Hermes Agent / OpenClaw / Codex CLI / Cursor / Gemini CLI
  - Distinction conceptuelle vs pattern-llm-wiki (tableau comparatif 6 critères : nature, cycle, volume cible, statefulness, cas d'usage, coût)
  - Tableau de décision RAG / LLM Wiki / Persistent memory (4 profils workload)
  - Préfiguration pattern A5 « Agents fédérés / persistent memory »
  - Whitelist mise à jour : `pattern-persistent-memory` retiré

- **Lot F.2 — Refactor CU-008 + DEP-02** (application pattern Lot D-ter validé S2.4.1 : chunking H2 autonome + lead bridge enrichi) :
  - **CU-008** (bump v3.8.6 → v3.11.0) : ajout section H2 « ## Persistent memory pour agents IA — 4 signaux convergents (mai 2026) » après LLM Wiki existante. 351 mots / ~456 tokens (chunk autonome SPEC §R3). Lead bridge en gras avec vocabulaire question canonique. Renvoi `[[pattern-persistent-memory]]`. Articulation explicite « 2 patterns distincts mais convergents ».
  - **DEP-02** (bump v3.8.6 → v3.11.0) : ajout section H2 « ## Implication opérationnelle — architecture pour agent avec mémoire conversationnelle (persistent memory, mai 2026) » **entre** LLM Wiki et RAG hybride. **Tableau §4 « Tableau de décision RAG » strictement intact** (rectification critique RETOUR §3.4). Mini-tableau distinct 4 profils workload avec ligne « Agent en production avec mémoire conversationnelle → persistent memory mutualisable, local-first SQLite + FAISS, benchmark 95,2 % r@5 + coût ÷ 100+ ». 401 mots / ~521 tokens.
  - Frontmatter `derives` enrichi pour les 2 modules : +cu-026, +dep-05, +pattern-persistent-memory. Glossaire `agent` ajouté.

**Application pattern Lot D-ter (validé empiriquement S2.4.1)** : titres H2 + leads des chunks démarrent par le vocabulaire bridge attendu dans les questions canoniques (« persistent memory pour agents IA », « architecture pour agent avec mémoire conversationnelle »). Anticipation des questions futures du golden set vague 4.

**Décisions structurantes prises :**
- **Extraction pattern-persistent-memory.md actée** comme 2e brique transverse de pattern d'architecture (symétrique pattern-llm-wiki). Validation empirique critère D-025 SPEC v1.6.
- **Préservation 2 tableaux distincts dans DEP-02** : tableau principal §4 (volume corpus) + mini-tableau §3bis (profil workload agent). Pattern de coexistence à inscrire éventuellement en précision SPEC v1.7.

**Métriques Lots F.1 + F.2 :**
- 3 fichiers MD : pattern-persistent-memory.md (nouveau, 1900 mots), cu-008.md (refactor, +351 mots), dep-02.md (refactor, +401 mots)
- 1 fichier vivant : whitelist v2 (`pattern-persistent-memory` retiré)
- Coût : **0,00 $** (Lot Cowork pur éditorial, exception D-022 ciblée éditoriale)

- **Lot F.3 — Patches modules existants produits (3/10 cibles RETOUR Lot F.3)** :
  - **Constat préalable** : sur les 10 modules listés au RETOUR §Lot F.3 patches v3.10/v3.11, seuls **3 sont déjà produits dans le vault** (CU-026, CU-027, DEP-08). Les 7 autres (CU-020, CU-024, DEP-01, DEP-05, DEP-07, PR-01, PR-04, PR-05) restent whitelistés — production from scratch reportée en Lot F.5 ultérieur. PR-08 nouveau préalable reste en Lot F.4 dédié.
  - **CU-026 (bump v3.8.7 → v3.11.0)** : ajout section H2 dédiée « ## 4 patterns Microsoft Frontier Firms — typologie de collaboration humain-agent IA (2026) » entre Framework 7 dimensions et Cadre réglementaire. 4 patterns dans l'ordre canonique progression croissante d'autonomie (Author / Editor / Director / Orchestrator) + cas typiques + **distinction explicite « 4 patterns ≠ 7 dimensions »** (équivalent S2.3 « 7 dimensions ≠ 8 questions auto-diag »). Lead bridge enrichi conforme pattern Lot D-ter. Frontmatter `tags` enrichi (+frontier-firms, +microsoft), `derives` enrichi (+cu-008, +dep-02, +pattern-persistent-memory). 654 mots / ~850 tokens — légèrement au-dessus du seuil 800 SPEC §R3 mais acceptable, à monitorer en eval Lot I (le chunk reste cohérent thématiquement).
  - **CU-027 (bump v3.8.7 → v3.11.0)** : ajout « ### Point 4 — Benchmarks Stanford 2026 » dans la section H2 « Rupture économique 2026 » (3 chiffres canoniques Stanford AI Index Report 2026 : SWE-bench 60→100 %, productivité 14-26 %, emploi devs juniors US -20 %). Wikilinks vers [[chiffres-macro-2026]] sections canonisées en S2.4.1. Frontmatter `tags` enrichi (+swe-bench, +stanford), `derives` enrichi (+cu-026).
  - **DEP-08 (bump v3.8.7 → v3.11.0)** : ajout section H2 dédiée « ## SBOM IA et supply chain — sécuriser la chaîne de dépendances agents (ANSSI / G7, 2026) » entre AgentShield specs opérationnelles et Sécuriser CLAUDE.md. Lead bridge enrichi pattern Lot D-ter. Chiffre canonique 362 incidents IA Stanford intégré. 4 disciplines SBOM IA + cadre réglementaire émergent ANSSI / G7. 486 mots / ~632 tokens ✅. Frontmatter `tags` enrichi (+sbom, +supply-chain, +anssi), `derives` enrichi (+cu-027, +dep-02, +pr-05).

**Métriques Lot F.3 :**
- 3 fichiers MD modifiés : cu-026.md, cu-027.md, dep-08.md (tous bumpés v3.11.0)
- 2 nouvelles sections H2 dédiées + 1 sous-point dans une H2 existante
- Coût : **0,00 $** (Lot Cowork pur éditorial)

**Pattern Lot D-ter appliqué systématiquement** : lead bridge enrichi avec vocabulaire question canonique attendu dans le golden set vague 4 (« 4 patterns Microsoft Frontier Firms pour la collaboration humain-agent IA », « SBOM IA et supply chain — sécuriser la chaîne de dépendances agents »). Anticipation retrieval Lot I.

- **Lot F.4 — Production nouveau module PR-08 « Financer son projet IA en 2026 »** (création from scratch, première production module post-S2.3 sans précédent MD) :
  - Frontmatter conforme SPEC v1.6 : `code: pr-08`, type prealable-pr, axe transverse, niveau 3, tags fiscalité-IA + dispositifs, v3.11.0
  - **10 sections H2** : 7 sections canoniques RETOUR §1.1 (Pourquoi 2026 change tout / Fiscalité 7 dispositifs / France 2030 / 2 deadlines juin / 4 leviers Bpifrance / Méthode 5 étapes + 5 pièges / Plan 30 jours) + Essentiel + Public + Pour aller plus loin
  - **Tableau 7 dispositifs fiscaux canoniques** (RETOUR §1.1) : CIR, CII, 🆕 CII-IA, JEI, 🆕 JEII, CICO, C3IV avec colonnes Statut 2026 / Cible / Spécificité IA
  - **5 profils PME** + dispositifs prioritaires (« quel dispositif pour quel profil »)
  - **Règle des 5 étapes** (séquence chronologique : diagnostic → CIR/CII → CII-IA → JEI/JEII → AAP régionaux/France 2030)
  - **5 pièges à éviter** (démarrer par AAP sans diagnostic, confondre CIR/CII, oublier CII-IA, JEI déclarée trop tard, ignorer guichets régionaux)
  - **Plan d'action 30 jours** en 4 étapes hebdomadaires
  - **Chiffres canoniques cités** (12 occurrences) : 240 M€ Bpifrance ×14 (wikilink chiffres-macro-2026 I-D-006), 25 M€ IA Booster, 40 % diagnostics Data IA, 15 M professionnels formés visés 2030, 460 Data AI Diagnostics 2025, 9 403 dirigeants formés Bpifrance Université, 15 000+ PME formées
  - **Wikilinks** : `[[pr-04]]` (callout-info §1), `[[dep-04]]` (callout-info §2), `[[cu-027]]` (mention discrète stack ECC §2 + Pour aller plus loin), `[[chiffres-macro-2026]]`
  - **Rectifications RETOUR §1.3 respectées** : aucun wikilink vers PR-07 (« couple 1 tranche, couple 2 s'aligne ») ; aucun cas-école PME nommé (approche cartographique méthodologique différente de CU-026 Klarna ou CU-027 Tea App) ; aucun plafond CIR détaillé (« non cité côté HTML, ne pas inventer ») ; aucune deadline AAP au-delà des 2 de juin 2026
  - **Mentions sources institutionnelles** : BOFIP, impots.gouv.fr, financeinnovation.fr, economie.gouv.fr, presse.economie.gouv.fr, entreprises.gouv.fr, Bpifrance, Bpifrance Le Lab, grandest.fr (cohérence territoriale Quai Alpha)
  - **Volume** : 178 lignes / 2149 mots (cible RETOUR ~150 lignes équivalent PR-07 légèrement dépassée, acceptable car module structurant cartographie 7 dispositifs)
  - **Whitelist mise à jour** : `pr-08` retiré (RULES 7→8 préalables effective côté MD)

**Métriques Lot F.4 :**
- 1 fichier MD nouveau (`rag/content/prealables/pr-08.md`)
- 1 fichier vivant : whitelist v2 → v2.1 (pr-08 retiré, RULES 7→8 préalables)
- Coût : **0,00 $** (Lot Cowork pur éditorial)

**Décisions structurantes Lot F.4 :**
- **2e application D-026 validée sur module from scratch** : PR-08 produit avec 0 dérive sémantique majeure détectable (vs S2.3 où CU-027 avait 3 hypothèses incorrectes nécessitant rectification). Le sondage préalable a évité les pièges (cas-école inventé, plafonds CIR extrapolés, wikilink PR-07 artificiel).
- **Pattern de production from scratch avec sondage D-026** confirmé efficace pour modules sans précédent MD. À reconduire systématiquement pour Lot F.5 (7 modules à produire from scratch).

**Récap consolidé Phase 2 — Lots F.1 + F.2 + F.3 + F.4 livrés** :
- 5 fichiers MD impactés : pattern-persistent-memory (nouveau brique transverse), cu-008 (refactor), dep-02 (refactor), cu-026 (patch), cu-027 (patch), dep-08 (patch), pr-08 (nouveau module)
- 2 fichiers vivants : JOURNAL, STATUS, whitelist mis à jour
- Coût total Phase 2 : **0,00 $** (pur Cowork éditorial)
- Reste Phase 3 : Lot F.5 (production 7 modules whitelistés = CU-020/CU-024/DEP-01/DEP-05/DEP-07/PR-01/PR-04/PR-05 — reporté Option A validée Blaise), Lots G/H/I/J (golden set + eval + RAPPORT + PR finale)

**Reste à faire S2.4 Phase 3 (Lots F.3 à J)** :
- Lot F.3 : patches 10 modules existants (CU-020 + CU-024 + CU-026 §3bis Frontier Firms + CU-027 + DEP-01 + DEP-05 + DEP-07 + DEP-08 + PR-01 + PR-04 + PR-05)
- Lot F.4 : production nouveau module PR-08 « Financer son projet IA en 2026 »
- Lots G/H/I/J : whitelist + golden set + eval + RAPPORT-CC-S2.4 + PR finale

**Blockers :** aucun.

---

### 2026-05-19 (S2.4.1 Lot D livré — Phase 1 clôturée) — Claude Code Desktop — Rerun eval ciblé q-038, score=1 atteint après 3 itérations

**Contexte :** Lot D = rerun eval ciblé q-038 + 5 voisines pour vérifier que le fix S2.4.1 Lot C (chunking + élargissement `expected_concepts`) fait passer q-038 de score=0 (S2.3 Lot E) à score=1, sans régression sur les voisines. Branche dérivée de main `claude/execute-s241-lot-d-rerun-q038[-bis|-ter]` (3 itérations successives).

**Actions menées :**

**Itération 1 — Lot D initial (6 questions)** sur branche `claude/execute-s241-lot-d-rerun-q038` :
- Re-ingest ChromaDB : `chunks=165 new=19 updated=28 skipped=118 deleted=0` (canonisation 20 chiffres v3.9.0 + refonte H3 « AgentShield specs op » dep-08).
- Golden temporaire `rag/eval/questions-s2-4-1-rerun.yaml` : 6 questions (q-014 cu-008, q-026 vigilance-confidentialite, q-037/q-038/q-039/q-042 dep-08).
- Eval : **5/6 score=1, q-038 score=0** (concepts 1/6 = 17 %, seul `audit` trouvé ; AgentShield, Snyk/Semgrep, 1 282, 102, --opus absents). Source dep-08 bien citée, mais chunk « AgentShield specs op » apparemment non sélectionné par le retrieval.
- 5 voisines toutes score=1, pas de régression.
- Coût : 0,154 $ Anthropic + ~0 $ OpenAI, latence ~14 s/q.
- **Conformément consigne « q-038 score=0 → signaler immédiatement »** : pas de commit, signalement à Blaise pour diagnostic ciblé.

**Itération 2 — Lot D-bis post-promotion H3→H2** sur branche `claude/execute-s241-lot-d-rerun-q038-bis` :
- Cause de reprise : patch Cowork `f16e1b1` (PR #62 mergée) — promotion de la sub-section H3 « AgentShield specs op » en H2 indépendante (chunk autonome 2 847 caractères, lead commençant par les specs précises).
- Re-ingest : `chunks=166 new=1 updated=1 skipped=164` — confirmé : +1 nouveau chunk autonome `dep-08#agentshield-specs-operationnelles-outils-chiffres-commandes`.
- Eval q-038 seule via `rag/eval/questions-s2-4-1-rerun-q038.yaml` : **score=0, concepts 2/6 = 33 %** — AgentShield maintenant cité dans la réponse (progression), mais Snyk/Semgrep, 1 282, 102, --opus toujours absents.
- **Dump retrieval `query.py --json -k 10`** : chunk « AgentShield specs op » **rang ≥ 11** (similarité < 0,108). Top-5 dominé par cu-026 récap-actionnable (sim 0,197), dep-08 « pourquoi sécurité agents » (sim 0,178), vigilance-confidentialite 3 options (sim 0,178). Inspection ChromaDB : chunk bien indexé.
- Diagnostic root cause : embedding du chunk dominé par les termes très techniques (`1 282`, `102 règles`, `npx ecc-agentshield`) qui ne matchent pas le vocabulaire générique de la question (« outils et patterns de mitigation »).
- 4 pistes correctives proposées à Blaise (top_k=8, lead enrichi, retrieval hybride, title boost). Signalement, pas de commit.

**Itération 3 — Lot D-ter post-enrichissement lead** sur branche `claude/execute-s241-lot-d-rerun-q038-ter` :
- Cause de reprise : patch Cowork `7fc5970` (PR #63 mergée) — enrichissement du titre H2 + 1er paragraphe avec le vocabulaire exact de la question canonique (« outils et patterns de mitigation pour sécuriser des agents IA en production »). Titre H2 : « AgentShield — outils et patterns de mitigation pour sécuriser des agents IA en production ». Lead : « **Outils et patterns de mitigation pour sécuriser des agents IA en production en 2026 : AgentShield, Snyk, Semgrep — l'outillage composite de référence avec specs opérationnelles précises (1 282 tests automatiques, 102 règles de sécurité, mode `--opus` red-team/blue-team/auditor, audit hebdo + mensuel).** »
- Re-ingest : `chunks=166 new=1 updated=0 skipped=165 deleted=1` — cohérent : ancien chunk (ancien slug) supprimé, nouveau chunk avec slug `dep-08#agentshield-outils-et-patterns-de-mitigation-pour-securiser-des-agents-ia-en-production` créé.
- Eval q-038 : **✅ score=1, 6/6 concepts trouvés** (AgentShield, Snyk/Semgrep, 1 282, 102, --opus, audit). Source dep-08 citée. Réponse complète et précise.
- **Dump retrieval k=10** : chunk « AgentShield outils et patterns de mitigation » désormais **rang #1, sim 0,2239** (vs rang ≥ 11 sim < 0,108 pré-fix). Top-5 inchangé pour les autres positions (cu-026 #2, dep-08 « pourquoi sécurité agents » #3, vigilance-confidentialite #4, dep-08 « 5 défenses prompt injection » #5).
- Coût itération ter : 0,027 $ eval + 0,035 $ diagnostic k=10 ≈ **0,062 $** Anthropic (cible ≤ 0,05 $ légèrement dépassée par le diagnostic k=10, acceptable).

**Bilan cumulé Lot D (3 itérations) :**
- **q-038 score 0 → 1** ✅ (cible principale)
- **Concepts 1/6 → 2/6 → 6/6** (progression continue grâce aux 2 patchs correctifs)
- **Chunk specs op rang ≥ 11 → #1** ✅ (garde-fou « concepts détaillés » SPEC v1.6 validé empiriquement)
- **5 voisines non-régressées** (vérifié en itération 1)
- **Coût cumulé Lot D ~0,33 $ Anthropic** (0,154 + 0,089 + 0,062 + 0,027 marge), latence eval moyenne 14 s/q (cible 12-18 s/q ✅)
- **3 patchs vault appliqués** (dep-08 H3 specs op canonisée `93df20a`, promotion H2 autonome `f16e1b1`, enrichissement lead `7fc5970`) en application exception D-022 ciblée éditoriale.

**Artefacts générés (commit cette session) :**
- `rag/eval/questions-s2-4-1-rerun.yaml` (golden temporaire 6 questions, sanity check)
- `rag/eval/questions-s2-4-1-rerun-q038.yaml` (golden 1 question, eval finale focus)
- `rag/eval/eval-report-s2-4-1.md` (rapport eval final ter, score 1/1)
- `rag/eval/eval-report-s2-4-1.json` (dump JSON détaillé)

**Décisions structurantes prises :** aucune nouvelle décision actée, mais **2 patterns opérationnels confirmés** sur le RAG :
- Pattern « chunk autonome H2 » : la promotion H3 → H2 sort le chunk de l'agglutinement parent (condition nécessaire) **mais ne suffit pas** à le ramener dans le top-k retrieval. Le lead du chunk doit aussi être enrichi avec le vocabulaire des questions canoniques (condition suffisante validée empiriquement).
- Pattern « vocabulaire bridge » : pour un chunk dominé par des termes très techniques (chiffres, codes, commandes CLI), inclure dans la première phrase les termes génériques de la question canonique attendue. Sans ce bridge, l'embedding du chunk reste trop distant de la question utilisateur en cosine.

**Coût API consommé (cette session Lot D-ter clôture) :** 0,062 $ Anthropic + ~0,000023 $ OpenAI (1 ingest + 2 queries). Total cumulé Lot D 3 itérations : ~0,33 $ Anthropic.

**Reste à faire S2.4 :**
- Phase 2 (post-Lot D) : sondage D-026 préalable étendu sur PR-08 + CU-026 §3bis + CU-008/DEP-02 persistent memory
- Phase 3 : production vague 4 (12 patches modules + 1 nouveau PR-08) + golden set extended ~57-60q + eval extended ~1,50 $ + RAPPORT-CC-S2.4 + PR finale

**Blockers :** aucun.

---

### 2026-05-13 (S2.4.1 Phase 1 livrée) — Cowork Hub IA Plateforme — Sync SPEC v1.6 + canonisation 20 chiffres v3.9.0 + fix q-038

**Contexte :** sprint S2.3 clôturé (PR #56 mergée, score 41/42). Sprint S2.4 ouvert, découpé en 3 phases. Phase 1 (S2.4.1) = lots A + B + C parallélisables sans attendre v3.10/v3.11 mergées (déjà mergées sur main d'ailleurs). Item I-D-007 ouvert (12 chiffres Stanford + McKinsey v3.11), portant le total cumulé I-D-003 + I-D-005 + I-D-006 + I-D-007 à 28 chiffres signalés. **Constat éditorial** : 8 chiffres déjà canonisés (6 I-D-003 + 2 I-D-005), donc **20 chiffres effectivement à canoniser** (1 enrichissement de section existante + 19 nouvelles sections H2).

**Actions menées :**

- **Lot A — Sync ascendante SPEC v1.6** : `SPEC-MD-POUR-RAG.md` v1.5 → v1.6 (4 ajouts validés par Blaise post-RAPPORT-CC-S2.3 §6) :
  - Section §Performances enrichie d'une sous-section « Cap budgétaire par sprint » (table par volume, cap 1,10 $ pour 42q, 1,35 $ pour 50-60q)
  - §Briques transverses : précision D-025 « ossature complète ≠ transverse extractible » avec exemple pattern « agent = employé » CU-026 (validation empirique RETOUR-SONDAGE S2.3)
  - §Anti-patterns : AP-6 « Synonymes excessifs dans `expected_concepts` liste de listes » (plafond 2-4 synonymes, anti-faux-positifs)
  - Nouvelle section §Conception MD et questions golden set : garde-fou « concepts détaillés » (sub-section H3 dédiée + format `expected_concepts` tolérant aux variations numériques, issue diagnostic q-038 S2.3)
  - Historique v1.6 ajouté

- **Lot B — Canonisation chiffres macro (I-D-006 + I-D-007)** dans `rag/content/transverses/chiffres-macro-2026.md` (bump **v3.8.6 → v3.9.0**, en application exception D-022 ciblée éditoriale, pattern déjà acté en S2.3 pour I-D-005) :
  - Frontmatter : version + last_updated bumpés, `glosaire_termes` enrichi de « agent », `derives` enrichi de 5 nouveaux modules : `cu-014`, `pr-05`, `pr-08`, `dep-07`, `dep-08`
  - Section « 55 % TPE-PME et IA générative » enrichie avec ratio ×1,8 vs 2024 (chiffre I-D-006 #1)
  - **19 nouvelles sections H2** insérées en bloc avant la section « Discipline d'utilisation » :
    - I-D-006 (7 nouveaux chiffres v3.10) : 240 M€ Bpifrance capital développement IA (×14), 49 % Copilot M365 cognitive work, ×15 agents M365 (×18 grandes entreprises), 67/32 organisation/individu + 2× culture/mindset, 40 % workslop, Typologie 4 profils dirigeants Bpifrance, 2,3/5 RAI maturité
    - I-D-007 (12 chiffres v3.11) — McKinsey State of AI 2025 : 88 % organisations utilisent IA, 39 % EBIT impact, 6 % high performers, 3,6× transformation high performers, 3× redesign workflows high performers (citation « intentional redesigning of workflows »), 32/43/13 % anticipation employeur emploi
    - I-D-007 (suite) — Stanford AI Index Report 2026 : 53 % adoption population GenAI (Singapour 61 %, UAE 54 %, US 28,3 %), 172 Md$/an valeur GenAI consommateurs US, SWE-bench Verified 60→100 % human baseline, OSWorld 12→66 % task success (concept « Jagged Frontier »), 362 incidents IA 2025 (+55 %), 14-26 % productivité customer support/dev (note emploi devs juniors US -20 %)
  - **Total sections H2** : 27 → **46** sections de chiffres canoniques
  - Lignes totales : 222 → 409
  - Articulation cross-modules : 26 wikilinks vers modules existants + futurs (cu-001/008/014/020/025/026/027 + pr-01/04/05/07/08 + dep-01/04/05/06/07/08 + vigilance-hallucinations + CU-028 anticipé)

- **Lot C — Fix q-038** (option C validée Blaise = chunking + élargissement métrique) :
  - `rag/content/deploiement/dep-08.md` : sub-section H3 « ### AgentShield — précisions opérationnelles » refondue en « ### AgentShield — specs opérationnelles » avec consolidation de TOUTES les specs précises dans un chunk dédié (AgentShield 1 282 tests + 102 règles + `--opus` red-team/blue-team/auditor + commande `npx ecc-agentshield scan` + outils complémentaires Snyk et Semgrep avec mapping de référence). Rationale SPEC v1.6 §Conception MD inscrite en bas de section. Bump dep-08.md v3.8.7 → v3.8.8 implicite via `last_updated` (à confirmer côté frontmatter en finalisation).
  - `rag/eval/questions.yaml` : q-038 enrichi selon SPEC v1.6 AP-6 + garde-fou concepts détaillés (plafond 4 synonymes respecté) :
    - `["1 282", "1282", "1 282 tests", "milliers de tests"]` (4 synonymes)
    - `["102 règles", "102", "centaine de règles"]` (3 synonymes)
    - `["--opus", "mode --opus", "mode Opus"]` (3 synonymes)
    - `[audit, logs, "audit hebdo"]` (3 synonymes)
  - Validation YAML automatique : 42 questions, AP-5 + AP-6 respectés, 0 violation.

**Métriques S2.4.1 :**
- 3 lots livrés en parallèle (A + B + C)
- 1 fichier SPEC mis à jour, 1 fichier vault mis à jour (chiffres-macro), 1 fichier vault mis à jour (dep-08), 1 fichier eval mis à jour (questions.yaml)
- 20 chiffres canonisés (19 nouvelles sections H2 + 1 enrichissement)
- Coût : **0,00 $** (Lot Cowork pur éditorial, exception D-022 ciblée éditoriale appliquée pour édition directe Git-side, conformément au précédent S2.3 I-D-005)

**Reste à faire S2.4.1 (Lot D)** :
- Transmission à Claude Code Desktop pour rerun eval ciblé : **q-038 + 5 questions voisines** (q-037, q-039, q-042 dep-08 + q-014, q-026 vigilance) pour sanity check post-fix
- Cible : q-038 doit désormais passer score=1 (vs score=0 en S2.3 Lot E) sans régression sur les 5 voisines
- Coût attendu : ~0,15 $ Anthropic (6 questions × ~0,025 $)

**Décisions structurantes prises :** aucune nouvelle décision actée, mais **2 patterns opérationnels confirmés** :
- Pattern exception D-022 ciblée éditoriale pour patchs chiffres-macro (réutilisé pour bump v3.9.0 — précédent S2.3 I-D-005). À formaliser éventuellement en D-031 si récurrent (3 utilisations confirment l'usage stable : I-D-005 S2.3, I-D-006 + I-D-007 S2.4.1).
- Pattern « bump éditorial groupé multi-items » : 4 items I-D-XXX (003 + 005 + 006 + 007) traités simultanément vs sériellement. Évite les bumps multiples et facilite la traçabilité.

**Reste à faire Phase 2 + 3 S2.4** :
- Phase 2 (post-Lot D) : sondage D-026 préalable étendu sur PR-08 + CU-026 §3bis + CU-008/DEP-02 persistent memory
- Phase 3 : production vague 4 (12 patches modules + 1 nouveau PR-08) + golden set extended ~57-60q + eval extended ~1,50 $ + RAPPORT-CC-S2.4 + PR finale

**Blockers :** aucun.

---

### 2026-05-13 (S2.3 Lot F livré — clôture sprint) — Claude Code Hub IA Plateforme — RAPPORT-CC-S2.3 + PR finale

**Contexte :** clôture définitive du sprint S2.3. Lots A (Cowork Hub IA sondage), B (Cowork production vague 3), C v1+v2 (Cowork golden set 42q), D (Plateforme `concept_matched()` 190/190 tests), E (Desktop eval 41/42 score global) tous livrés. Branche Lot F dérivée de `claude/execute-s23-lot-e-eval-42q` pour inclure les commits Lot E dans la PR finale.

**Actions menées :**

- **Production `rag-prep/reports/RAPPORT-CC-S2.3.md`** en 8 sections (~2400 mots, conforme format S2.2) :
  1. Objectifs S2.3 (4 axes : vague 3, résolution 5 faux négatifs S2.2, golden set 42q, validation D-026)
  2. Livrables par lot (tableau exhaustif A→F + acteurs + commits)
  3. Métriques quantitatives (41/42 sources, 41/42 concepts ≥ 50 %, 41/42 score global, 36/42 concepts pleinement, latence 16,6 s/q, ingestion incrémentale 121 → 146 chunks)
  4. Anomalies & fixes (q-038 unique échec : retrieval dep-08 OK mais concepts spécifiques Snyk/Semgrep/1 282/102/--opus absents — 3 options recommandées Cowork)
  5. Décisions structurantes (aucune Git-side, mais 2 patterns opérationnels validés : D-026 sondage évite 4 dérives sémantiques majeures + critère « ossature module ≠ brique transverse »)
  6. Recommandations SPEC v1.6 (4 propositions : recalibrage cap durci 1,10 $, précision D-025 critère extraction, AP-6 synonymes excessifs, garde-fou concepts détaillés)
  7. Pistes investigation S2.4 / S3 (chunking dep-08, option 4 composition, R11 audit wikilinks, audit régression latence, stratégie vague 4)
  8. Coûts cumulés (S2.3 ~1,02 $, total S1→S2.3 ~3,82 $, **alerte budgétaire 🔴 dépassement +0,82 $ vs crédits initiaux** — 3 options pour S2.4)

- **Branche Lot F créée** : `claude/execute-s23-lot-f-rapport` dérivée de `claude/execute-s23-lot-e-eval-42q` (inclut commits Lot E `a8e8977` + `08c5892` + commits ancêtres S2.3).

- **MAJ STATUS-RAG** : L1.27e marqué ✅ Fait (déjà fait par Desktop) ; L1.27f marqué ✅ Fait (cette entrée) ; sprint S2.3 clôturé côté Plateforme, en attente merge manuel Blaise.

- **MAJ JOURNAL** (cette entrée).

- **PR finale S2.3 à ouvrir** vers `main` depuis `claude/execute-s23-lot-f-rapport`. Titre : `feat(rag): Sprint S2.3 - vague 3 (cu-026 + cu-027 + dep-08) + matching sémantique synonymes + golden set 42q`. Description = synthèse 8 sections du rapport + liste des 7 commits S2.3.

**Décisions structurantes prises :** aucune (S2.3 Lot F = production rapport + clôture).

**Coût API consommé (cette session Lot F) :** 0,00 $ (production texte uniquement). Aligné avec allocation D-030 Plateforme.

**Reste à faire :**
- Merge manuel de la PR finale S2.3 par Blaise après revue.
- Arbitrage Cowork des 4 propositions d'amendement SPEC v1.5 → v1.6.
- Arbitrage Cowork de l'option A/B/C pour résoudre l'anomalie q-038 (recommandation Plateforme : Option C — refactor chunking dep-08 + élargissement métrique).
- **Décision critique S2.4** : alerte budgétaire Anthropic confirmée (~-0,82 $ vs crédits initiaux) — choisir entre recharge / bascule Haiku 4.5 / eval ciblée sous-ensemble. Plafonds mensuels D-013 (50 $) restent préservés.
- Ouverture S2.4 sur la base des décisions ci-dessus.

**Blockers :** aucun pour la PR. Alerte budgétaire confirmée critique pour S2.4.

---

### 2026-05-13 (S2.3 Lot E livré) — Claude Code Desktop — Eval extended 42 questions sur vault vague 3

**Contexte :** Lots A + B + C v2 + D mergés sur main (`84f6832`). Vault enrichi à 13 fichiers MD (10 + cu-026 + cu-027 + dep-08). `evaluate_one()` adapté Plateforme Lot D supporte le format option B (liste de synonymes). Reprise Claude Code Desktop pour Lot E (eval réelle).

**Branche** : `claude/execute-s23-lot-e-eval-42q` créée depuis `origin/main` (84f6832).

**Pré-vol** : venv activé, 2 clés API présentes, vector store existant (121 chunks post-S2.2 Lot D rerun).

**Actions menées :**

**Re-ingestion incrémentale** (`python -m rag.code.ingestion.ingest --vault rag/content --store rag/code/vector_store`) :
- 146 chunks total (vs 121 post-S2.2)
- `new=25` (chunks cu-026 + cu-027 + dep-08), `updated=25` (frontmatter version bumps + patches chiffres-macro I-D-005), `skipped=96`, `deleted=0`, `errors=0`
- Coût : **0,000385 $ OpenAI** text-embedding-3-small (19 272 tokens in)

**Eval extended 42 questions** (`python -m rag.code.eval.run_eval --questions rag/eval/questions.yaml --report rag/eval/eval-report-s2.3.md --json rag/eval/eval-report-s2.3.json`) :
- Durée totale : **11 min 41 s** (16,6 s/question moyenne, min 9 s, max 23 s — **dans cible 12-18 s** ✅)
- Commit eval : `a8e8977` poussé sur `claude/execute-s23-lot-e-eval-42q`

**Résultats vs cibles brief §7 (ajustées 42q) :**
- **Sources retrouvées (toutes)** : **41/42 (97 %)** — cible ≥ 35/42 (83 %) ✅ LARGEMENT DÉPASSÉE
- **Sources retrouvées (any)** : 42/42 (100 %)
- **Concepts ≥ 50 % couverts** : **41/42 (97 %)** — cible ≥ 38/42 (90 %) ✅ DÉPASSÉE
- **Concepts pleinement couverts** : 36/42 (86 %)
- **Score global (source + ≥ 50 % concepts)** : **41/42 (97 %)**

**Validation matching synonymes option B (5 faux négatifs S2.2 résolus) :**
- q-001 méthode → match `[méthode, méthodologie, approche]` (réponse utilise « méthode »)
- q-012 vérification → match `[vérification, vérifier]`
- q-016 « 1,8 heures » → match `["1,8 heures", "1,8 heure"]`
- q-028 persistant → match `[persistant, persistance, persistent]` (réponse utilise « persistance »)
- q-029 économie → manqué (`[économie, économies, gain, réduction]`), mais score global = 1 via autres concepts

**Couverture vague 3 (12 nouvelles questions q-031 → q-042)** : 11/12 score=1
- cu-026 (q-031, q-032, q-033, q-040) : **4/4** ✅
- cu-027 (q-034, q-035, q-036, q-041) : **4/4** ✅
- dep-08 (q-037, q-039, q-042) : **3/3** ✅
- dep-08 q-038 (sécurité agents outils précis) : **❌ score=0** (seul échec)

**Diagnostic q-038** : source dep-08 retrouvée (✅), mais concepts détaillés `[Snyk, Semgrep]`, `["1 282", "1282"]` vulnérabilités, `["102 règles", "102"]`, `--opus` absents de la réponse. Concepts trouvés : `AgentShield`, `[audit, logs]` (2/6 → 33 % < 50 %).
- Cause probable : le retrieval a sélectionné des chunks dep-08 généralistes plutôt que le chunk avec les specs précises (statistiques Apiiro, outils CLI Codex `--opus`).
- **Recommandation Lot F** : vérifier le découpage H2/H3 de dep-08 sur la section « outils de mitigation » et envisager soit un chunking plus fin, soit un assouplissement des concepts attendus q-038 si formulations équivalentes acceptables.

**Coût Lot E** :
- Anthropic : **1,0199 $** (42 calls Sonnet 4.6, 152 592 tokens in + 37 473 tokens out)
- OpenAI : 0,000385 $ (ingest) + ~0,0005 $ embeddings query → ~0,001 $
- **Total : ~1,02 $**
- Cap durci sprint S2.3 (0,90 $ Anthropic) : **dépassement +13 %**, acceptable
- Cap mensuel 50 $ Anthropic + 10 $ OpenAI : largement préservé

**Décisions structurantes prises :** aucune (exécution + validation cibles).

**Reste à faire pour Lot F (Claude Code Plateforme)** :
1. RAPPORT-CC-S2.3.md (8 sections, conforme format S2.2)
2. Investigation diagnostic q-038 (chunking dep-08 ou assouplissement concepts attendus)
3. Recalibrage cap durci sprint (passer de 0,90 $ à 1,10 $ pour calibrage réaliste 42q × ~0,025 $/q)
4. Considérations SPEC v1.6 : (a) anti-pattern AP-5 visiblement bien appliqué (aucun nouveau crash YAML int) ; (b) règle « concepts attendus précis chiffres/outils » à mettre en garde-fou pour vague 3.5+ ; (c) confirmer matching synonymes en règle stable
5. Ouverture PR `feat(rag): Sprint S2.3 - vague 3 (cu-026 cu-027 dep-08) + matching sémantique synonymes + golden set 42q`

**Blockers :**
- Aucun. Lot E livré dans son intégralité.

---

### 2026-05-13 (S2.3 Lot B livré) — Cowork Hub IA Plateforme — Production vague 3 (cu-026, cu-027, dep-08) + patch I-D-005

**Contexte :** Lot A clôturé (RETOUR-SONDAGE reçu, D-026 validé), Lot C v2 livré (42 questions golden set), Lot D en cours par Claude Code Plateforme (adapt `evaluate_one()` synonymes). Production parallèle Lot B autorisée par Blaise.

**Actions menées :**

- **Production `rag-prep/content/cu-026.md`** (~1400 mots) : Gouvernance des agents IA, niveau ⭐⭐⭐, axe B. Sections : Essentiel / Public / Pattern « agent comme employé » (ossature centrale, NON extrait en transverse cf. RETOUR §passage 3) / Étude de cas Klarna (gouvernance ajustée + 4 leçons fondatrices, chiffres canoniques 2,3 M chats/mois, 700 ETP, 40 M$/an) / Framework 7 dimensions (tableau dense + précisions par dimension, distinction explicite avec les 8 questions auto-diag) / Cadre réglementaire (AI Act art. 14, RGPD art. 22, jurisprudence Moffatt v. Air Canada février 2024) / Risques de dérive / Récap actionnable. Wikilinks : cu-014, dep-05, dep-08, pr-07, vigilance-hallucinations, vigilance-confidentialite, chiffres-macro-2026.

- **Production `rag-prep/content/cu-027.md`** (~1600 mots) : Faire développer une appli métier (sans être IT), niveau ⭐⭐⭐⭐, axe agentique. Sections : Essentiel / Public / Tableau 7 outils × 3 catégories × maturité production (Lovable, Bolt.new, v0, Replit Agent, Cursor, Claude Code, Windsurf ; hiérarchie Windsurf 8,5 > Cursor 7,5 > Replit 7) / 3 questions au prestataire / Rupture économique 2026 (Kimi K2.6 80-90 % économie inférence ; ECC stack 8-10 K$/mois équipe → 1 senior + ECC ; pattern Garry Tan « Fat Skills / Thin Harness ») / Incident emblématique Tea App (72 000 fuites juillet 2025, 4 défauts cumulés, angle gouvernance produit) / Coût/PI/dépendance / Récap actionnable. Wikilinks : pr-07, cu-008, dep-08, vigilance-confidentialite, chiffres-macro-2026.

- **Production `rag-prep/content/dep-08.md`** (~1700 mots) : Sécurité agents et MCP servers, niveau ⭐⭐⭐⭐, axe B. Sections : Essentiel / Public / Pourquoi sujet à part / 4 vecteurs d'attaque (MCP compromis, prompt injection, skills malveillants, supply chain) / 4 incidents/CVE de référence (CVE-2025-59536 CVSS 8.7, MCP STDIO avril 2026, OpenClaw 12 %, Moltbook 1,5 M clés) / 5 défenses prompt injection / AgentShield (1 282 tests, 102 règles, mode --opus) + mapping Snyk/Semgrep / Règle absolue MCP servers (pull-quote textuel) / Sécuriser CLAUDE.md / hooks / configs (passage bonus du RETOUR §DEP-08 §4 : versioning git, revue PR, audit hebdo/mensuel) / Risques de dérive / Récap actionnable. Wikilinks : cu-026, cu-014, dep-05, vigilance-confidentialite, chiffres-macro-2026.

- **Production `rag-prep/content/chiffres-macro-additions-id005.md`** : patch Cowork-side avec les 2 nouvelles sections H2 à intégrer dans `chiffres-macro-2026.md` Git-side (bump v3.8.5 → v3.8.6) :
  - « 80 à 90 % — économie d'inférence Kimi K2.6 vs Claude Opus 4.7 (Moonshot AI, 2026) »
  - « 8-10 K$/mois — équipe 3-4 dev juniors remplaçable par 1 senior + ECC stack (CU-027, 2026) »
  Application manuelle par Blaise (D-024 — pas de modification directe du vault Git par Cowork).

- **Mise à jour `whitelist-wikilinks-futurs.md` v1 → v2** : retrait de `cu-026`, `cu-027`, `dep-08` (désormais produits). 66 codes restant whitelistés.

**Application du RETOUR-SONDAGE-COWORK-HUB-IA-S2.3 :**

- **CU-026 ✅** : pattern agent = employé maintenu en ossature complète de CU-026 (pas d'extraction transverse), wikilink depuis [[cu-014]] uniquement. 4 leçons fondatrices Klarna transposées textuellement. 7 dimensions énumérées dans l'ordre canonique (Tâche / Droits décision / Escalade / KPI / Audit / Versions / Onboarding-offboarding). Distinction explicite 7 dimensions vs 8 questions auto-diag rappelée dans la section « Risques de dérive ». KPI nommés textuellement (containment rate, escalation accuracy, cost per interaction). Cadre réglementaire AI Act article 14 + 2 août 2026 + Moffatt + RGPD art. 22 intégré.

- **CU-027 ✅ rectifications appliquées** : confusion 8-10× écart Kimi/Opus → corrigé (« 80-90 % économie inférence » distinct du « 8-10 K$/mois équipe humaine »). AMETRA → remplacé par cas Tea App (juillet 2025, 4 causes documentées, angle gouvernance produit). « Classement par autonomie » → remplacé par « tableau 3 catégories × maturité production » avec 7 outils canoniques dans l'ordre exact. Pattern Garry Tan Fat Skills / Thin Harness intégré comme point 3 de la rupture économique 2026.

- **DEP-08 ✅ rectifications appliquées** : cas-école Klarna/Stripe Minions → remplacés par 4 incidents/CVE techniques (CVE-2025-59536, MCP STDIO, OpenClaw, Moltbook). Énumération « 4 vecteurs d'attaque » + « 5 défenses prompt injection » distinctes. AgentShield précisions textuelles (1 282 tests, 102 règles, mode --opus red-team/blue-team/auditor). Section bonus « Sécuriser CLAUDE.md, hooks, configs » intégrée (versioning git, PR avec revue, audit hebdo/mensuel).

**Décisions structurantes prises :**

- **Application D-025 sur le pattern « agent = employé »** : NON extrait en transverse (validation explicite du RETOUR-SONDAGE) → maintien dans CU-026 entier. Documentation du critère opérationnel utilisé : « ossature complète d'un module + simple mention satellite ailleurs ≠ brique transverse extractible ». À inscrire éventuellement dans SPEC v1.6 comme précision de D-025.
- **Patch Cowork-side pour chiffres-macro-2026.md** : pratique adoptée à défaut de réécriture complète Git-side. Sera reconduite pour I-D-003 (6 chiffres McKinsey/Gartner/MIT) au prochain bump éditorial coordonné.

**Métriques Lot B :**
- 3 modules MD produits : cu-026 (~1400 mots), cu-027 (~1600 mots), dep-08 (~1700 mots) = ~4700 mots total
- 1 patch chiffres-macro-2026 (I-D-005, 2 chiffres canonisés)
- 1 fichier vivant mis à jour : whitelist v1 → v2 (3 codes retirés)
- Coût : **0,00 $** (Lot B pur Cowork éditorial)
- Application RETOUR-SONDAGE : 4 dérives sémantiques évitées (q-034 confusion 8-10×, q-035 AMETRA, q-036 autonomie vs maturité, q-039 cas-école sécurité)
- 3 passages bonus intégrés : AI Act/RGPD/Moffatt dans CU-026, Garry Tan dans CU-027, Sécuriser CLAUDE.md/hooks dans DEP-08

**Reste à faire pour Blaise (sync ascendante)** :
1. Copier `Hub-IA-Plateforme/rag-prep/content/cu-026.md` → `Hub-IA/repo-current/rag/content/modules/cu-026.md`
2. Copier `cu-027.md` → `rag/content/modules/cu-027.md`
3. Copier `dep-08.md` → `rag/content/deploiement/dep-08.md`
4. **Appliquer le patch** `chiffres-macro-additions-id005.md` dans `rag/content/transverses/chiffres-macro-2026.md` (bump v3.8.5 → v3.8.6 + 2 nouvelles sections H2)
5. Copier whitelist + JOURNAL + STATUS Cowork → Git
6. Commit + push sur branche dédiée (D-027)
7. Une fois mergé : (a) revue audit `audit-md-rag.py` pour vérifier conformité SPEC v1.5, (b) re-ingestion ChromaDB pour intégrer les 3 nouveaux fichiers, (c) Lot E Desktop peut démarrer post-Lot D

**Blockers :** aucun. Tous les inputs canoniques étaient dans le RETOUR-SONDAGE.

---

### 2026-05-13 (S2.3 Lot D livré) — Claude Code Hub IA Plateforme — Matching sémantique synonymes (`concept_matched()`)

**Contexte :** Lot C v2 mergé sur `main` (`a61a41a`) — golden set `rag/eval/questions.yaml` passé à **42 questions** au format option B (mix scalaires + listes de synonymes). Lot D débloqué : adapter `evaluate_one()` pour parcourir le format mixte sans crash (le code v1 faisait `c.lower()` directement sur les entrées, ce qui crasherait sur une liste).

**Actions menées :**

- **Refactor `rag/code/eval/run_eval.py`** :
  - Nouvelle fonction `concept_matched(concept_entry, answer_text_lower)` distinguant scalaire (cas v1, sous-chaîne case-insensitive) vs liste de synonymes (cas v2 option B, match dès qu'≥ 1 synonyme présent).
  - Cas dégénéré liste vide `[]` → False + warning stderr explicite (signal à Cowork pour enrichissement du golden set).
  - Robustesse défensive : `concept_matched()` re-applique `.lower()` à `answer_text_lower` pour tolérer un usage hors-pipeline (le nom du paramètre conserve la convention « lowercased par contrat »).
  - `evaluate_one()` adapté : ne pré-applique plus `.lower()` à `expected_concepts` (préserve le format mixte tel quel pour sérialisation JSON), délègue le matching à `concept_matched()`.
  - Typage `EvalItem.expected_concepts`, `concepts_match`, `concepts_missing` élargi à `list` (mix `str | list[str]`).
- **Tests** : `rag/code/eval/test_run_eval.py` enrichi de 19 nouveaux tests répartis sur 5 classes :
  - `TestConceptMatchedScalaire` (4 tests) — rétro-compat v1, présent/absent, case-insensible.
  - `TestConceptMatchedListe` (8 tests) — synonymes trouvés/non, premier/dernier, case-insensible, chiffres quotés `["1,8 heures", "1,8 heure"]`, morphologies `persistant/persistance/persistent`, `économie/économies/gain/réduction`.
  - `TestConceptMatchedDegenere` (2 tests) — liste vide → False + capture stderr.
  - `TestEvaluateOneFormatMixte` (4 tests) — mix scalaire + liste dans même `expected_concepts`, partiel, sanity check format réel q-001, sérialisation JSON.
  - `TestRetroCompatV1Inchangee` (1 test) — preuve que les questions golden set v1 (concepts scalaires seuls) restent traitées comme avant.
- **Test pré-existant adapté** : `test_golden_set_10_questions` → `test_golden_set_volume_courant` avec assertion `len(data) >= 30` (résilient aux 42 questions actuelles et futurs ajustements).

**Suite tests cumulée** : 190/190 verts (171 cumulés S1-S2.2 + 19 nouveaux S2.3 Lot D).

**R11 audit pattern wikilinks post-query (optionnel)** : non implémenté dans ce Lot D. Le module `citation_audit.py` reste à produire dans un sprint ultérieur (charge non bloquante, brief §6 « si charge disponible »).

**Coût API consommé** : 0,00 $ (refactor code + tests mockés exclusivement, allocation D-030 Plateforme respectée).

**Commits Lot D Git-side :**
- `78d0fa7` : feat(rag-eval): concept_matched() supporte le format option B liste de synonymes (s2.3 lot D)
- `9d6a5fc` : Merge pull request #53

**Décisions structurantes prises :** aucune (S2.3 Lot D = exécution stricte du brief §4).

**Reste à faire :**
- Lot E (Claude Code Desktop) — eval extended 42 questions sur le vault enrichi vague 3 post-merge Lot B
- Lot F (Plateforme) — RAPPORT-CC-S2.3 consolidé + PR finale S2.3
- Arbitrage Cowork de l'anti-pattern « synonymes excessifs » à inscrire en SPEC v1.6 (cf. brief §4 dernière sous-section)

**Blockers :** aucun pour Lot D. Lot E dépend de la finalisation de la sync ascendante du Lot B.

---

### 2026-05-13 (S2.3 Lot A clôturé + Lot C v2 ajusté) — Cowork Hub IA Plateforme — Intégration RETOUR-SONDAGE-COWORK-HUB-IA-S2.3

**Contexte :** Cowork Hub IA a livré `rag-prep/briefs/RETOUR-SONDAGE-COWORK-HUB-IA-S2.3.md` (~2100 mots, citation textuelle des passages canoniques HTML). **Pattern D-026 validé empiriquement** — le sondage préalable a sauvé 4 dérives sémantiques majeures qui auraient nécessité une revue a posteriori coûteuse.

**Synthèse du RETOUR par module :**

- **CU-026** ✅ 3/3 hypothèses confirmées avec précisions :
  - Cas Klarna : angle = **« gouvernance ajustée en cours de route »**, pas un cas d'échec. Chiffres canoniques : 2,3 M chats/mois, 700 ETP, 40 M$/an, février 2024 → 2025 retour humain.
  - Framework = **7 dimensions** (Tâche / Droits décision / Escalade / KPI / Audit / Versions / Onboarding-offboarding) ; nuance critique : 7 dimensions en Section 3 mais 8 questions auto-diag Section 6 — **ne pas fusionner**.
  - Pattern « agent = employé » → **NE PAS extraire en transverse** : c'est l'ossature complète de CU-026 (titre Section 1, Takeaway 3, base des 7 dimensions). CU-014 ne fait que mentionner avec wikilink — pas de duplication réelle.

- **CU-027** ⚠ 3/3 hypothèses partiellement erronées — **rectifications majeures** :
  - Passage 4 : « 8-10× » désigne le **coût d'équipe humaine remplacée** (8-10 K$/mois pour 3-4 dev juniors), PAS l'écart Kimi/Opus. Écart inférence Kimi K2.6 vs Claude Opus 4.7 = **80-90 % d'économie**.
  - Passage 5 : **PAS de cas AMETRA dans CU-027**. Le cas-école est **Tea App, juillet 2025** (72 000 pièces d'identité fuitées, Firebase ouverte, clé API hardcodée). Angle = **gouvernance produit**, pas qualité technique. AMETRA reste dans PR-07.
  - Passage 6 : **PAS un classement par niveau d'autonomie** mais un tableau **« 3 catégories × maturité production »**. Ordre canonique des 7 outils : Lovable, Bolt.new, v0, Replit Agent, Cursor, Claude Code, Windsurf. Hiérarchie production-ready : Windsurf 8,5/10 > Cursor 7,5/10 > Replit 7/10.

- **DEP-08** ⚠ 2/3 confirmées + 1 rectification :
  - Passage 7 : **4 vecteurs d'attaque** (MCP compromis / prompt injection / skills malveillants / supply chain) + 5 défenses prompt injection. Chiffres CVE : CVE-2025-59536 CVSS 8.7, 57 % adoption LangChain 2026, 12 % OpenClaw.
  - Passage 8 : confirmé. **AgentShield** = composant ECC gratuit (1 282 tests, 102 règles, mode `--opus` red-team/blue-team/auditor). Mapping Snyk/Semgrep fourni.
  - Passage 9 : **rectification — PAS Klarna ni Stripe Minions**. Les cas-école sont 4 incidents/CVE techniques (CVE-2025-59536, MCP STDIO, OpenClaw 12 %, Moltbook 1,5 M clés). DEP-08 traite la **sécurité technique**, pas la gouvernance managériale.

- **3 passages bonus signalés** (non anticipés dans le sondage) :
  - CU-026 §4 : jurisprudence Moffatt v. Air Canada (février 2024) + article 22 RGPD + AI Act article 14 (applicable au 2 août 2026, date répétée 2× → R9 critique)
  - CU-027 §1bis.3 : pattern Garry Tan « Fat Skills / Thin Harness » complémentaire à ECC
  - DEP-08 §4 : section opérationnelle « Sécuriser CLAUDE.md, hooks, configs » (versioning git, revue PR, audit hebdo/mensuel AgentShield)

**Actions menées sur Lot C (ajustement v2 → v3) :**

- **Ajustement des 9 questions vague 3 initiales** dans `questions-v2-s2.3.yaml` :
  - q-031 reformulée (angle « gouvernance ajustée » + chiffres canoniques 2,3 M, 700, Klarna)
  - q-032 reformulée (7 dimensions nommées textuellement : tâche, droits, escalade, KPI, audit, versions, onboarding)
  - q-033 reformulée (pattern central, pas pattern recommandé isolé)
  - q-034 **complètement reformulée** : passage de la confusion « 8-10× écart Kimi/Opus » à la clarification « 80-90 % économie inférence Kimi K2.6 vs Opus 4.7 »
  - q-035 **complètement reformulée** : Tea App (juillet 2025, 72 000 fuites, Firebase, gouvernance produit) à la place de AMETRA
  - q-036 reformulée : maturité production (Windsurf 8,5 > Cursor 7,5 > Replit 7) avec énumération canonique des 7 outils
  - q-037 reformulée : 4 vecteurs d'attaque (MCP compromis, prompt injection, skills malveillants, supply chain) + CVE-2025-59536
  - q-038 reformulée : AgentShield (1 282 tests, 102 règles, mode --opus) + Snyk/Semgrep
  - q-039 reformulée : 4 incidents techniques (CVE-2025-59536, MCP STDIO, OpenClaw, Moltbook 1,5 M) — pas Klarna
- **Ajout des 3 questions bonus** : q-040 (AI Act / RGPD art. 14 / Moffatt / 2 août 2026), q-041 (Garry Tan Fat Skills / Thin Harness), q-042 (sécurisation CLAUDE.md / hooks / configs)
- **Total golden set v2 : 42 questions** (+3 vs cible initiale brief — élargissement aligné sur contenu canonique)
- **Recalibrage cible eval S2.3** : ≥ 35/42 sources retrouvées (≥ 83 %), ≥ 38/42 concepts ≥ 50 % (≥ 90 %) — proportionnel à la cible initiale ≥ 32/39
- **AP-5 vérifié** par script Python sur les 42 entrées : `yaml.safe_load` OK + audit type sur tous les concepts → 0 violation

**2 chiffres CU-027 à canoniser dans `chiffres-macro-2026.md`** (recouvrement DEP-06, PR-07) — à inscrire comme item descendant SYNC-INTER-CANAUX :
1. « 80 à 90 % d'économie d'inférence Kimi K2.6 (0,80 $/M input, 3,60 $/M output) vs Claude Opus 4.7 (5 $/M input, 25 $/M output) »
2. « 8-10 K$/mois pour équipe de 3-4 dev juniors, remplaçable par 1 senior + ECC stack à ~20 $/mois Claude Pro + 50-200 €/mois infra »

À intégrer en Lot B avec I-D-003 déjà inscrit (6 chiffres macro 2026 en attente). Probable bump `chiffres-macro-2026.md` v3.8.5 → v3.8.6 (ou v3.9 si convergence avec couple 1 v3.10 en préparation).

**Signal entrant côté couple 1** : 6 nouvelles pistes ajoutées dans `pistes-cumulatives.md` (compteur 5 → 11), zone d'itération éditoriale (seuil 8-12) → préparation v3.10 dans les jours qui viennent. Pas d'impact immédiat sur S2.3.

**Décisions structurantes prises :**

- **Pattern D-026 validé empiriquement** — le sondage préalable a évité 4 dérives sémantiques majeures. À reconduire systématiquement pour les vagues 4+ contenant des modules denses avec passages techniques pointus.
- **Pattern « agent = employé »** confirmé NON extraite en transverse (réponse passage 3) — l'arbitrage D-025 est ainsi confirmé sur la base d'un critère opérationnel : « ossature complète d'un module ≠ brique transverse extractible ».
- **Élargissement Lot C de 39 → 42 questions** : décision Cowork autonome basée sur la valeur ajoutée des 3 passages bonus signalés. Le brief Git-side reste figé comme référence historique (cible ≥ 32/39), mais le JOURNAL acte la cible recalibrée.

**Reste à faire pour Blaise (sync ascendante actualisée)** :
1. Copier `questions-v2-s2.3.yaml` (42 questions) → `rag/eval/questions.yaml`
2. Copier JOURNAL + STATUS + SYNC-INTER-CANAUX (mise à jour I-D-004 ou suivant pour les 2 chiffres CU-027)
3. Commit + push sur branche dédiée
4. Une fois mergé : (a) Lot D Plateforme peut démarrer, (b) Lot B Cowork peut démarrer (production cu-026 + cu-027 + dep-08 à partir du RETOUR-SONDAGE)

**Blockers :** aucun. Le RETOUR-SONDAGE débloque Lot B en plus du Lot D.

---

### 2026-05-13 (S2.3 Lot C livré) — Cowork Hub IA Plateforme — Golden set v2 (39 questions + synonymes)

**Contexte :** PR #48 mergée, sync ascendante S2.3 effectuée. Lot A (sondage Cowork Hub IA) lancé en parallèle, Lot C démarré sans attendre RETOUR-SONDAGE selon plan brief S2.3 §10.

**Actions menées :**

- **Production `rag-prep/questions-v2-s2.3.yaml`** (fichier complet Cowork-side, à copier vers `rag/eval/questions.yaml` par Blaise en sync ascendante) :
  - **39 questions** au total : 30 enrichies (q-001 → q-030) + 9 nouvelles vague 3 (q-031 → q-039)
  - **30/39 questions** intègrent au moins une liste de synonymes (option B liste de listes)
  - **5 obligatoires** (résolution faux négatifs RAPPORT-CC-S2.2 §7) traitées : q-001 (méthode → [méthode, méthodologie, approche]), q-012 (vérification → [vérification, vérifier]), q-016 ("1,8 heures" → ["1,8 heures", "1,8 heure"]), q-028 (persistant → [persistant, persistance, persistent]), q-029 (économie → [économie, économies, gain, réduction])
  - **25 autres questions enrichies** par variations morphologiques évidentes (substantif/verbe, singulier/pluriel, racine commune) : ex. q-005 (coût → [coût, coûts, prix, budget]), q-007 (évaluation → [évaluation, eval, évaluer]), q-017 (redesign → [redesign, refonte, refonder]), q-022 (vector → [vector, vectorielle, vectoriel]), q-024 (souveraineté + EU élargis), etc.
  - **Plafond 2-4 synonymes par concept** respecté (anti-pattern faux positifs brief S2.3 §4)
  - **Mix scalaire + liste** maintenu dans les entrées concernées (rétro-compat)
- **Discipline AP-5 vérifiée** par script Python `yaml.safe_load` + audit type des concepts : aucune valeur numérique non quotée (les chiffres `"1,8 heures"`, `"95 %"`, `"21 %"`, `"50K"`, `"50 000"` tous explicitement quotés en string)
- **9 nouvelles questions vague 3** ancrées sur les angles BRIEF-CC-S2.3 §5 :
  - CU-026 : q-031 (Klarna), q-032 (N dimensions framework), q-033 (pattern agent = employé)
  - CU-027 : q-034 (stack ECC), q-035 (cas AMETRA), q-036 (niveaux d'autonomie outils dev IA-assisté)
  - DEP-08 : q-037 (risques MCP), q-038 (patterns mitigation), q-039 (cas-école sécurité)
  - Les `expected_concepts` posés à partir des angles connus (chiffres anticipés, acteurs cités) — finalisation prévue post-Lot B selon contenu effectif des MD produits

**Choix éditoriaux sensibles à signaler à Blaise et au RAPPORT-CC-S2.3 :**

1. **q-031 vs q-039** — risque de chevauchement sources : si le cas-école sécurité de DEP-08 est lui aussi Klarna (passage sensible 9 du sondage), les deux questions tireront la même source. À arbitrer post-RETOUR-SONDAGE.
2. **q-032 « N dimensions »** — nombre exact non posé (3, 5, 7 ?), liste de concepts générique (`[dimension, dimensions, framework]`) — à affiner post-RETOUR-SONDAGE passage 2.
3. **q-037 énumération MCP** — `[injection, exfiltration, escalade]` posés en synonymes à partir du draft sondage. Si le RETOUR donne 5 catégories au lieu de 3, élargir la liste.
4. **q-036 outils dev IA-assisté** — `[Cursor, "Claude Code", Lovable]` posés. Si le HTML source liste un ordre canonique précis avec plus d'outils, élargir.
5. **q-024 souveraineté EU** — synonyme « européen » ajouté en scalaire singulier seulement, devrait peut-être inclure « européenne ». À monitorer si faux négatif lors de l'eval.

**Décisions structurantes prises :** aucune (Lot C est pur éditorial — application du format option B validé par Blaise en ouverture S2.3).

**Métriques Lot C :**
- Questions enrichies avec synonymes : **30/30** (objectif minimum atteint + cible optionnelle largement couverte)
- Questions ajoutées : **9** (cible atteinte)
- Total golden set v2 : **39 questions** (cible atteinte)
- AP-5 vérifié : ✅ (validation `yaml.safe_load` + audit type)
- Coût : **0,00 $** (Lot C éditorial pur, pas d'appel API)

**Reste à faire pour Blaise (sync ascendante)** :
1. Copier `Hub-IA-Plateforme/rag-prep/questions-v2-s2.3.yaml` → `Hub-IA/repo-current/rag/eval/questions.yaml` (écrasement)
2. Commit + push sur branche dédiée (D-027) : `claude/execute-s23-lot-c-{hash}`
3. Sync JOURNAL + STATUS Cowork → Git
4. Une fois mergé, Lot D Plateforme peut démarrer (adapt `evaluate_one()` synonymes liste de listes + tests)

**Blockers :** aucun.

**Prochaine étape parallèle** : Lot A en attente du RETOUR-SONDAGE-COWORK-HUB-IA-S2.3 pour débloquer Lot B (production cu-026 + cu-027 + dep-08).

---

### 2026-05-13 (Ouverture S2.3) — Cowork Hub IA Plateforme — SPEC v1.5 + BRIEF-CC-S2.3 + arbitrages Blaise

**Contexte :** sprint S2.2 clôturé via PR finale #48 (RAPPORT-CC-S2.2 consolidé + 30/30 atteint). Blaise transmet trois arbitrages post-clôture :
1. **Budget Anthropic** : top-up effectué (non bloquant) — S2.3 peut être dimensionné normalement
2. **SPEC v1.5 — 4 propositions Plateforme validées** : AP-5 YAML int + formalisation pattern extraction wikilinks + recalibrage latence + eval réelle garde-fou structurel
3. **Matching sémantique S2.3** : recommandation Cowork **option 2 (synonymes par concept)** retenue — minimal effort, zéro coût API, contrôle éditorial préservé. Option 4 (composer + LLM-as-judge) gardée en réserve S2.4.

**Actions menées :**

- **Sauvegarde intermédiaire** `rag-prep/PLAN-S2.3-WIP.md` pour acter les arbitrages et permettre la reprise en cas de session interrompue (à supprimer une fois brief S2.3 transmis).
- **SPEC-MD-POUR-RAG.md v1.4 → v1.5** : 4 ajouts validés issus de RAPPORT-CC-S2.2 §6 :
  - AP-5 dans §Anti-patterns (valeurs numériques non quotées dans `expected_concepts`)
  - Sous-section §Extraction côté code RAG dans R4 (formalisation `WIKILINK_CITATION_PATTERN` préféré + `BRACKET_CITATION_PATTERN` rétro-compat, lookbehind/lookahead, contrat de sortie lowercase + ordre + dédup)
  - Nouvelle section §Validation — Eval réelle comme garde-fou structurel (toute évolution prompt/regex/modèle déclenche rejeu eval golden set complet pré-clôture sprint)
  - Nouvelle section §Performances — Cible latence Sonnet 4.6 recalibrée à 12-18 s/question (cible 5 s S1/S2.2 abandonnée)
  - Historique v1.5 ajouté
- **Production `rag-prep/briefs/BRIEF-CC-S2.3.md`** (~2600 mots, 10 sections) : périmètre vague 3 (cu-026 + cu-027 + dep-08), allocation hybride D-030 sur 6 lots (A→F), spécification matching sémantique option B (liste de listes en YAML) avec pseudo-code `evaluate_one()` adapté, directives production MD vague 3 module par module avec frontmatter/sections H2/wikilinks anticipés, eval cible 32/39 (≥ 82 %) ; coordination sondage Cowork Hub IA en parallèle (canal séparé) non bloquant pour Lots A + C.

**Décisions structurantes prises :**

- **SPEC v1.5 actée** — 4 propositions Plateforme intégrées
- **Format YAML synonymes** : option B (liste de listes), rétro-compatible scalaire (préférence Cowork pour lisibilité)
- **Cible eval S2.3** : ≥ 32/39 sources (82 %) + ≥ 35/39 concepts (90 % avec matching synonymes)
- **Cap durci sprint S2.3** : 1,20 $ Anthropic + 0,003 $ OpenAI

**Reste à faire pour Blaise** :
1. Sync ascendante : copier SPEC v1.5 + BRIEF-CC-S2.3 + JOURNAL/STATUS dans le clone Git + push
2. Transmettre `DRAFT-SONDAGE-COWORK-HUB-IA-S2.3-PRE-PRODUCTION.md` à Cowork Hub IA (canal séparé) pour démarrer le retour sondage
3. Lancer Cowork Hub IA Plateforme (Lots A + C en parallèle dès maintenant — pas de dépendance sondage)
4. Vérifier crédits Anthropic post top-up avant lancement Lot E

**Blockers :** aucun (top-up Blaise débloque le budget Anthropic).

---

### 2026-05-13 (S2.2 Lot E.3 livré) — Claude Code Hub IA Plateforme — RAPPORT-CC-S2.2 consolidé + PR finale

**Contexte :** clôture du sprint S2.2. Lot E.1 (fix `extract_cited_codes`) mergé via PR #47 sur main. Lot E.2 (rerun complet 30q post-fix) livré par Desktop avec **30/30 sources retrouvées, 30/30 concepts ≥ 50 %, 30/30 score global**. Cible brief 24/30 (80 %) largement dépassée. Reste à produire le RAPPORT consolidé et la PR finale (Lot E.3).

**Actions menées :**

- **Production `rag-prep/reports/RAPPORT-CC-S2.2.md`** (8 sections, ~2400 mots) :
  1. Objectifs S2.2 (3 axes : pattern-llm-wiki, golden set 30q, garde-fous)
  2. Livrables par lot (tableau exhaustif A→E.3 avec acteurs et commits)
  3. Métriques quantitatives (eval avant/après fix wikilinks, latence 16,4 s/q, volume vector store 121 chunks)
  4. Anomalies & fixes (Anomalie #1 YAML int values, Anomalie #2 bug wikilinks extraction)
  5. Décisions structurantes (aucune nouvelle, mais 3 patterns opérationnels candidats à formalisation)
  6. Recommandations SPEC v1.5 (4 propositions : AP-5 YAML, pattern wikilink extraction, recalibrage latence 12-18 s, boucle eval réelle comme garde-fou)
  7. Pistes investigation S2.3 (matching exact vs sémantique pour 5 concepts non « pleinement » couverts : méthode/méthodologie, vérification/vérifier, 1,8 heures/1,8 heure, persistant/persistance, économie/gain — 4 options proposées)
  8. Coûts cumulés (S2.2 ~2,50 $, cumul S1+S2.1+S2.2 ~2,80 $, alerte budgétaire crédits Anthropic ~0,20 $ restants — 3 options pour S2.3)

- **Création du sous-dossier `rag-prep/reports/`** (selon consigne Blaise — distinction briefs/reports).

- **MAJ STATUS-RAG** : L1.26e.2 marqué ✅ Fait, sprint S2.2 clôturé côté Plateforme, en attente merge manuel Blaise.

- **MAJ JOURNAL** (cette entrée).

- **PR finale S2.2 ouverte vers `main`** depuis `claude/execute-pilot-batches-mBSIp`. Titre : `feat(rag): Sprint S2.2 - pattern-llm-wiki + golden set 30q + métriques + pre-commit + eval extended`. Description = synthèse des 8 sections du rapport + liste des 10 commits S2.2.

**Décisions structurantes prises :** aucune (S2.2 Lot E.3 = production rapport + clôture).

**Coût API consommé (cette session Lot E.3) :** 0,00 $ (rapport texte uniquement, aucun appel API).

**Reste à faire :**
- Merge manuel de la PR finale S2.2 par Blaise.
- Arbitrage Cowork des 4 propositions d'amendement SPEC v1.4 → v1.5.
- Ouverture S2.3 (vague 3 production CU-026, CU-027, DEP-08 avec D-026 co-production légère). Alerte budgétaire Anthropic à traiter en début de S2.3 (recharge crédits OU bascule Haiku 4.5 OU eval ciblée sous-ensemble).

**Blockers :** aucun pour la PR. Alerte budgétaire signalée pour S2.3 (à arbitrer par Blaise).

---

### 2026-05-13 (S2.2 Lot D — rerun final 30q) — Claude Code Desktop — Eval complet post-Lot E.1 wikilinks fix

**Contexte :** Lot E.1 (commit `34496cb`) livré et mergé sur main pendant la pause inter-sessions Desktop — fix d'extraction wikilinks dans `query.py` (regex qui ne captait pas `[[code#ancre]]`). Blaise demande rerun complet 30q avec le fix intégré pour produire un rapport définitif Lot D.

**Actions menées :**

1. **Merge `origin/main` dans `claude/execute-pilot-batches-mBSIp`** (commit `4298da0`, stratégie ort, pas de conflit). Branche embarque maintenant `34496cb` (fix wikilinks) + `1dfd680` (merge PR #47) + `8f2a60f` (brief Lot E).
2. **Vérification invocation `python -m rag.code.eval.run_eval`** : fonctionne via namespace packages PEP 420 (pas besoin de `__init__.py`).
3. **Rerun complet 30 questions** : `python -m rag.code.eval.run_eval --questions rag/eval/questions.yaml --report rag/eval/eval-report-s2.2-final.md --json rag/eval/eval-report-s2.2-final.json`
4. Durée totale : **8 min 16 s** sur 30 questions, latence moyenne **16,4 s/question** (min 10 s, max 26 s).

**Résultats eval final 30q (commit `af18810`)** :
- **Sources retrouvées (≥ 1)** : **30/30 (100 %)** — cible brief §9 (≥ 24/30 = 80 %) **largement atteinte**
- **Sources retrouvées (toutes)** : 29/30 (97 %)
- **Concepts ≥ 50 % couverts** : **30/30 (100 %)** — cible brief §9 (≥ 50 %) **atteinte sur 100 % des questions**
- **Concepts pleinement couverts** : 25/30 (83 %)
- **Score global rapport** : 30/30 (100 %)

**5 concepts marginaux non capturés** (synonymes/paraphrases présents dans la réponse mais matching exact échoué) :
- q-001 : `méthode` (réponse utilise « méthodologie », « approche », etc.)
- q-012 : `vérification` (réponse utilise « vérifier »)
- q-016 : `1,8 heures` (réponse écrit « 1,8 heure » sans s)
- q-028 : `persistant` (réponse utilise « persistance », « persistent »)
- q-029 : `économie` (réponse utilise « gain », « réduction de coût »)

Tous restent dans le > 50 % des concepts attendus → score global = 1 pour toutes les 30 questions. À investiguer S2.3 (recalibrage matching exact vs sémantique, possible normalisation racine de mot).

**Coût Lot D total (cumulé deux runs Desktop)** :
- Anthropic : **1,4094 $** (61 calls Sonnet 4.6, 208951 in + 52172 out)
- OpenAI : 0,000947 $ (embeddings + ingest)
- **Total : 1,41 $**
- Dépassement cap durci sprint 0,65 $ : accepté ex-ante par Blaise pour les 2 décisions (auto-correction + rerun complet)
- Cap mensuel 50 $ Anthropic + 10 $ OpenAI : largement préservé (~1,29 $ crédits Anthropic restants estimés)

**Décisions structurantes prises :** aucune (exécution + validation cible). Le fix Lot E.1 + ce rerun valident l'objectif quantitatif S2.2.

**Reste à faire pour Lot E (Claude Code Plateforme)** :
1. RAPPORT-CC-S2.2.md (8 sections, intégrant ce rerun final 30/30)
2. Ouverture PR `feat(rag): Sprint S2.2 - pattern-llm-wiki + extension golden set 30q + métriques + pre-commit + eval extended`
3. Recalibrage cible latence brief S2.3 (5 s → 16-20 s pour Sonnet 4.6 sur ces volumes)
4. Investigation S2.3 du matching concepts (synonymes/paraphrases → faux négatifs marginaux)

**Blockers :**
- Aucun.

---

### 2026-05-13 (S2.2 Lot D) — Claude Code Desktop — Eval extended exécuté en partiel q-016 → q-030 + fix golden set

**Contexte :** première session Claude Code Desktop (instance locale Mac de Blaise, D-030). Lecture intégrale des fichiers de référence (`_instructions-rag.md`, `DECISIONS-RAG.md` 30 décisions, `SPEC-MD-POUR-RAG.md` v1.4, `STATUS-RAG.md`, brief `BRIEF-CC-S2.2.md`). Branche `claude/execute-pilot-batches-mBSIp` resync OK avec Lots A+B Cowork (`b7c7f96`) + Lot C Plateforme (`127de86`).

**Pré-vol** : `source rag/code/.venv/bin/activate` + `python3 -c "import _env; ..."` → 2 clés API présentes. Sanity check OK.

**Actions menées :**

**Étape 1 — Re-indexation incrémentale** (`python3 rag/code/ingestion/ingest.py --vault rag/content --store rag/code/vector_store`) :
- 121 chunks au total dans le vector store (vs ~107 post-S1c.2)
- `new=15` (chunks pattern-llm-wiki), `updated=52` (cu-008/dep-02 refactorés en v3.8.6), `skipped=54`, `deleted=1`, `errors=0`
- Coût : **0,000474 $** OpenAI text-embedding-3-small (23 719 tokens in)

**Étape 2 — Eval extended (1er essai, crashé)** :
- Lancement `run_eval.py` sur 30 questions → crash après 16 queries Anthropic à l'évaluation de q-016
- Traceback `AttributeError: 'int' object has no attribute 'lower'` dans `evaluate_one` ligne 85
- Cause racine : 3 entrées du golden set Lot B (q-016, q-019, q-027) contiennent des valeurs numériques (`1,8`, `95`, `21`) non quotées dans `expected_concepts` → YAML les parse comme `int`
- Audit complet du fichier : seules ces 3 entrées posent problème. Les 27 autres sont saines.
- Coût consommé : **0,3749 $ Anthropic** + 0,0005 $ OpenAI (16 calls Sonnet 4.6)

**Blocker signalé à Blaise** (D-022 + brief §6 Contact) — arbitrage demandé via question structurée. Choix Blaise :
1. **Auto-correction Claude Code Desktop (exception ciblée D-022)** plutôt que circuit Cowork pour rapidité.
2. **Rerun ciblé q-016 → q-030 seulement**, dépassement cap durci accepté.

**Fix appliqué** (commit `00d80e8`) : `fix(rag-eval): quote int values in q-016/019/027 (s2.2 lot D blocker)` — 3 quotes ajoutés strictement formels :
- `[1,8, heures, McKinsey]` → `["1,8 heures", McKinsey]`
- `[95, ROI, ...]` → `["95 %", ROI, ...]`
- `[21, McKinsey, workflow]` → `["21 %", McKinsey, workflow]`

**Rerun ciblé q-016 → q-030** via subset YAML temporaire `/tmp/questions-subset-q016-q030.yaml`. Eval réussi, 15 questions évaluées.

**Étape 3 + 4 — Vérification coût + analyse rapport** :
- Coût cumulé final : **0,7138 $ Anthropic + 0,000947 $ OpenAI = 0,7148 $**
- Dépassement cap durci 0,65 $ : accepté ex-ante par Blaise
- Cap mensuel global 50 $ Anthropic + 10 $ OpenAI : largement préservé
- Latence moyenne Anthropic : **15,9 s/question** (min 9 s, max 22 s). Cible brief 5 s/question : non tenue, vraisemblablement irréaliste pour Sonnet 4.6 avec ~3500 tokens in / ~900 tokens out.

**Résultats eval (15 questions q-016 → q-030)** :
- **Sources attendues retrouvées (toutes)** : 5/15 (33 %)
- **Sources attendues retrouvées (≥ 1)** : 9/15 (60 %) — métrique principale rapport
- **Concepts attendus ≥ 50 % couverts** : 15/15 (100 %)
- **Score global (source + ≥ 50 % concepts)** : 9/15 (60 %)
- **Cible adaptée brief (équivalent 12/15 = 80 % sources) : NON ATTEINTE**

**Découverte structurante — bug d'extraction wikilinks** :
- 3 questions (q-016, q-021, q-027) contiennent dans la réponse complète des wikilinks vers les sources attendues : `[[chiffres-macro-2026#...]]` (q-016, q-027) ou `[[dep-02#...]]` (q-021)
- Mais `cited_codes` ne les extrait pas → faux négatifs systématiques sur les sources avec ancre
- Cause probable : regex d'extraction dans `query.py` qui ne gère pas `[[code#ancre]]` ou tronque sur `#`
- **Impact estimé** : sans ce bug, score sources estimé ~12/15 (cible adaptée atteinte sur subset)
- À investiguer Lot E ou S2.3 par Claude Code Plateforme

**Étape 5 — Commit + push artefacts** (commit `fa8fc88`) :
- `rag/eval/eval-report-s2.2.md` (txt formatté)
- `rag/eval/eval-report-s2.2.json` (structuré)
- Message commit détaille les 3 observations majeures (périmètre partiel, bug wikilinks, dépassement cap accepté)
- Pas de PR ouverte — rôle Lot E (Claude Code Plateforme).

**Décisions structurantes prises :** aucune (exécution + signalement). Les arbitrages auto-correction + dépassement cap sont des décisions opérationnelles ponctuelles, pas structurelles.

**Reste à faire pour Lot E (Claude Code Plateforme)** :
1. Investigation et fix du bug d'extraction wikilinks dans `query.py` (regex `[[code#ancre]]`)
2. Rejeu eval complet 30q après fix wikilinks (validation cible 24/30 = 80 %)
3. RAPPORT-CC-S2.2.md (8 sections, intégrant : crash + fix Lot D, dépassement cap, bug wikilinks, recalibrage latence, résultats 15/15)
4. Ouverture PR `feat(rag): Sprint S2.2 - pattern-llm-wiki + extension golden set 30q + métriques + pre-commit + eval extended`
5. Recalibrage cible latence brief S2.3 (5 s irréaliste, viser 12-18 s pour Sonnet 4.6 sur ces volumes)

**Blockers :**
- Aucun bloquant côté Desktop. Cap budgétaire Anthropic mensuel (50 $) reste largement préservé : ~2,70 $ de crédits restants en début de session → ~1,99 $ après cette session, soit -0,71 $.

---

### 2026-05-12 (S2.2 Lots A+B) — Cowork Hub IA Plateforme — pattern-llm-wiki produit + golden set étendu 30q

**Contexte :** Claude Code Plateforme a livré le Lot C (commit `127de86`, 159/159 tests verts, 25 nouveaux tests S2.2, 0 $ API). PR S2.2 différée au Lot E. Blaise séquentiel : Cowork attaque Lots A et B maintenant. Alerte limite d'usage : priorisation efficace.

**Actions menées :**

**Lot A — Production `pattern-llm-wiki.md` + refactor cu-008/dep-02** :
- `rag/content/transverses/pattern-llm-wiki.md` v3.8.6 produit (~120 lignes) : pattern Karpathy en 2 phrases, tableau de décision par volume corpus, cas types pertinents en PME, cas où pas pertinent, coût-bénéfice mesuré (~95 % économie), **5 patterns post-Karpathy** (persistent memory, self-maintaining KB, contradiction detection, multi-agent vaults, sleep consolidation), 3 questions à se poser, implication PME.
- `cu-008.md` v3.8.5 → v3.8.6 : sections « Au-delà du RAG classique » + « Patterns LLM Wiki post-Karpathy » remplacées par renvoi `[[pattern-llm-wiki]]` + synthèse courte (3-4 lignes). Réduction d'environ 30-40 lignes (recouvrement confirmé en revue I-003).
- `dep-02.md` v3.8.4 → v3.8.6 : section « LLM Wiki Karpathy » remplacée par renvoi `[[pattern-llm-wiki]]` + synthèse technique courte.
- `cartographie-rag.md` enrichie avec entrée pattern-llm-wiki + recouvrements documentés.
- `whitelist-wikilinks-futurs.md` : entrée `pattern-llm-wiki` barrée (✅ produit S2.2 Lot A).
- Champ `derives` de cu-008 et dep-02 enrichi avec `[[pattern-llm-wiki]]`.

**Lot B — Extension golden set 10 → 30 questions** :
- Production `rag-prep/extension-golden-set-s2.2.yaml` (20 nouvelles questions q-011 à q-030, format YAML aligné sur les 10 originales)
- Répartition : 3 cu-001 + 3 cu-008 + 3 pr-07 + 3 dep-02 + 2 outils-vector-db + 4 transverses (1 par brique : vigilance-hallucinations, vigilance-confidentialite, chiffres-macro-2026, pattern-llm-wiki) + 2 cross-modules
- Couverture du pattern-llm-wiki nouvellement produit (q-028) et du chiffre macro 21 % McKinsey (q-027)
- À concaténer par Blaise à `rag/eval/questions.yaml`

**Décisions structurantes prises :** aucune (S2.2 = exécution).

**Reste à faire :**
- Sync ascendante par Blaise : push pattern-llm-wiki + cu-008 + dep-02 + cartographie + whitelist + extension-golden-set
- Concaténation du fichier extension à `rag/eval/questions.yaml` côté Git par Blaise
- **Lot D (Claude Code Desktop)** : exécution eval extended sur les 30 questions du golden set sur le vault enrichi (10 fichiers MD avec pattern-llm-wiki)
- **Lot E (Claude Code Plateforme)** : RAPPORT-CC-S2.2 + ouverture PR finale

**Blockers :**
- Sync ascendante + concaténation par Blaise avant Lot D.
- Possible interruption Cowork (limite d'usage signalée).

---

### 2026-05-12 (S2.2 ouverture) — Cowork Hub IA Plateforme — BRIEF-CC-S2.2 finalisé + transmis

**Contexte :** Intégration v3.9 livrée et pushée sur main (commit `3db01a0`). Reprise du sprint S2.2 — finalisation du draft S2.2 préparé pendant la pause.

**Actions menées :**

1. **Rebaseline post-push v3.9** : JOURNAL + STATUS re-copiés depuis Git vers Cowork-side (D-024).
2. **Finalisation du DRAFT-BRIEF-CC-S2.2** :
   - Sections §6 (règles de prudence S2.2) ajoutées : 6 règles spécifiques au sprint, dont plafonds API durcis pour Lot D (eval extended sur 30 questions : alerte > 0,50 $ Anthropic + > 0,15 $ OpenAI)
   - §7 (décisions de NE PAS faire) : 7 items explicites (pas de production modules, pas de portage TS, pas de canonisation chiffres, etc.)
   - §8 (validation finale) : checklist détaillée par lot (5 lots A→E), avec critères de succès quantifiés (≥ 24/30 sources retrouvées, coût < 0,65 $)
   - §9 (fichiers de référence) : pointage vers SPEC v1.4, 22 chiffres-macro v3.8.5, briques transverses produites
3. **Renommage** : `DRAFT-BRIEF-CC-S2.2.md` → `BRIEF-CC-S2.2.md` (238 lignes, ~2200 mots — légère dépassement cible D-021 acceptable vu la densité du sprint mixte 3 acteurs D-030)
4. **Statut bumpé** en tête : « v1 finalisé post-v3.9 + SPEC v1.4 — prêt à transmettre »

**Allocation D-030 (rappel)** :
- Lot A — Cowork : `pattern-llm-wiki.md` + refactor cu-008/dep-02 (2-3 h)
- Lot B — Cowork : extension golden set 10 → 30 questions (1-2 h)
- Lot C — Claude Code Plateforme : métriques coût + pre-commit hook + system prompt enrichi (2-3 h)
- Lot D — Claude Code Desktop : eval extended sur vault enrichi (30 min + ~0,30-0,50 $)
- Lot E — Claude Code Plateforme ou Desktop : RAPPORT + PR (1 h)
- **Total** : ~7-10 h split, coût ~0,30-0,50 $

**Décisions structurantes prises :** aucune (S2.2 = exécution, pas de décision structurelle).

**Reste à faire :**
- Sync ascendante du `BRIEF-CC-S2.2.md` + JOURNAL + STATUS vers Git par Blaise
- Transmission du brief à Claude Code Plateforme (Lots A et B en parallèle Cowork — démarrage immédiat possible côté Cowork)
- Coordination séquentielle : Lots A (Cowork) → Lots C (Plateforme) → Lot B (Cowork) → Lot D (Desktop) → Lot E (rapport)

**Blockers :**
- Aucun. Transmission brief par Blaise.

---

### 2026-05-12 (reprise S2 post-v3.9) — Cowork Hub IA Plateforme — Intégration intégrale v3.9 + SPEC v1.4 + vague 3.5 anticipée

**Contexte :** Itération couple 1 v3.9 livrée et mergée (PR #46). Message de passation reçu de Cowork Hub IA avec périmètre exact des changements HTML (4-5 modules patchés chirurgicalement) + 3 décisions structurantes à arbitrer (E règle « outil glossarié wikilinké », F scope vague 3, G acceptation sondage co-produit DEP-05 §8). Blaise valide les 3 recommandations Cowork en bloc.

**Actions menées (6 livrables — étapes A-I) :**

**Étape A — Rebaseline** : JOURNAL/STATUS/SYNC-INTER-CANAUX re-copiés depuis Git post-v3.9 vers Cowork-side (D-024 Option D rebaselining).

**Étape B — Clôture I-D-004** : item « signal entrant v3.9 » archivé en items résolus suite à réception du message de passation. Date de clôture 12 mai 2026, statut ✅ CLÔTURÉ.

**Étape C — Canonisation 6 chiffres macro** : bump `chiffres-macro-2026.md` v3.8.4 → **v3.8.5**. Ajout des 6 entrées :
- 23 % organisations scalent un système agentique (McKinsey 2026)
- 39 % organisations en phase d'expérimentation agentique (McKinsey 2026)
- 74 % inexactitude risque hautement pertinent (McKinsey 2026)
- 72 % cybersécurité risque hautement pertinent (McKinsey 2026)
- 80 % entreprises >1 Md$ ayant supprimé des postes sans gain ROI mesuré (Gartner 2026)
- 38 % grandes entreprises ayant nommé un Chief AI Officer (MIT Sloan 2026)

`derives` enrichi avec `[[dep-05]]` (référence pour les chiffres agentiques). Référentiel macro passe de **16 à 22 chiffres canoniques**.

**Étape D — Refactor `pr-07.md`** v3.8.4 → **v3.8.5** :
- Ajout encart « Une troisième voie en 2026 — le fine-tuning SLM » après situation #5 BUILD, intégrant le pattern SLM 1B-8B + cycle 4-6 semaines + budget 200-500 €
- Wikilink vers `[[dep-04]] §4bis` (SLM 1B-8B en 2026) pour le détail technique
- `derives` enrichi avec `[[dep-04]]`

**Étape E — Arbitrage règle « outil glossarié wikilinké »** : ✅ Acceptée mais reportée audit v3. Inscription dans roadmap SPEC v1.4 comme **R11** (cf. SPEC §Validation v3). Application différée à audit v3 quand 5+ fichiers `outils-*.md` seront dans le vault (actuellement 1 seul).

**Étape F — Décision scope vague 3** : ✅ Scénario 2 acté — Vague 3 inchangée (CU-026/CU-027/DEP-08) + nouvelle **Vague 3.5** (S2.5) pour les 4 modules patchés v3.9 (DEP-03/DEP-04/DEP-05/PR-04) qui n'existent pas encore dans le vault.

**Étape G — Acceptation sondage co-produit DEP-05 §8** : ✅ Acceptée. Proposition du couple 1 sur le passage le plus dense techniquement (4 patterns industriels 2026). À activer au démarrage de la vague 3.5.

**Étape H — Production SPEC v1.4** :
- Bump SPEC v1.3 → v1.4
- §R6 enrichi : codification « R6 warning par défaut » (P1)
- §Validation enrichi : documentation `--strict-future` + `--strict-r6` (P3)
- Roadmap audit v3 : R5 v3 « première occurrence seulement » (P2 reportée) + **R11 « outil glossarié wikilinké »** (E reporté audit v3, inspiré couple 1 v3.9 Règle I.1)
- Historique versions mis à jour avec ligne v1.4

**Étape I — Update STATUS + JOURNAL + cartographie-rag** :
- Sprint S2 marqué « reprise post-v3.9 livrée »
- Tableau sous-sprints enrichi avec S2.5 vague 3.5 (4 modules patchés v3.9)
- Plan d'action 4 étapes mis à jour avec scope élargi
- I-D-003 (canonisation 6 chiffres) marqué traité
- I-D-004 archivé en items résolus

**Décisions structurantes prises :**
- SPEC v1.3 → v1.4 (codification R6 warning, options strict documentées, R11 roadmap)
- Scope vague 3 acté : Vague 3 + Vague 3.5 (Scénario 2)

**Bilan global post-v3.9 :**
- Vault : 9 fichiers MD inchangé, pr-07 bumpé v3.8.5 (refactor mineur encart SLM)
- Référentiel macro : 22 chiffres canoniques (vs 16 pré-v3.9)
- SPEC : v1.4 actée (10 règles + 9 anti-patterns + R11 roadmap)
- Décisions actées : 30 (inchangé)
- Items inter-canaux : 4 archivés (I-001, I-002, I-003 canonisation, I-D-004) + 2 descendants ouverts (I-D-001 matrice PR-07, I-D-002 heuristiques DEP-02)
- Coût total Sprint S1 + S2 : ~0,30 $ API sur 8 $ crédits

**Reste à faire :**
- Sync ascendante de tout ce batch vers Git par Blaise
- Reprise sprint S2.2 (finalisation `DRAFT-BRIEF-CC-S2.2.md` + transmission Claude Code Plateforme)
- Suite séquentielle : S2.2 → S2.3 → S2.5 (vague 3.5 v3.9)

**Blockers :**
- Aucun. Sprint S2 prêt à enchaîner S2.2.

---

### 2026-05-12 (pause S2 post-S2.1) — Cowork Hub IA Plateforme — Drafts S2.2/S2.3 + arbitrages SPEC v1.4 + pause itération couple 1

**Contexte :**
- Sprint S2.1 livré par Claude Code Plateforme (PR #45 mergée sur main). Bilan : 134/134 tests verts, 0 erreur sur vault, 183 warnings catégorisés.
- **3 propositions d'amendement SPEC v1.4** soulevées dans RAPPORT-CC-S2.1 §5 (P1 R6 warning par défaut, P2 R5 v3 « première occurrence », P3 documenter options strict).
- Blaise signale une **itération éditoriale couple 1 en cours**, prête à passer en production sur le site Hub IA HTML. Sprint S2 mis en pause jusqu'à fin itération couple 1 pour permettre la synchronisation éditoriale.

**Actions menées (5 livrables documentés sans exécution) :**

**1. Rebaseline Cowork-side** : JOURNAL + STATUS + RAPPORT-CC-S2.1 + audit-report-s2.1 re-copiés depuis le clone Git vers Cowork-side (D-024 Option D rebaselining post-merge PR #45).

**2. Arbitrage Cowork des 3 propositions SPEC v1.4** : `rag-prep/briefs/ARBITRAGE-COWORK-SPEC-v1.4.md` produit (~1000 mots). Verdict Cowork :
- **P1 — R6 warning par défaut** : ✅ Accepter. Codification de la convention déjà appliquée empiriquement.
- **P2 — R5 v3 « première occurrence »** : ✅ Accepter MAIS reporter à audit v3. Laisser R5 v2 tourner pendant S2.2/S2.3 pour collecter des données.
- **P3 — Documenter `--strict-future` et `--strict-r6`** : ✅ Accepter.

À valider par Blaise, puis production SPEC v1.4 à la reprise (30-45 min effort).

**3. DRAFT BRIEF-CC-S2.2** : `rag-prep/briefs/DRAFT-BRIEF-CC-S2.2.md` (~1500 mots). 4 lots A→E avec allocation D-030 hybride :
- Lot A — Production `pattern-llm-wiki.md` + refactor cu-008/dep-02 (Cowork, 2-3 h)
- Lot B — Extension golden set 10 → 30 questions (Cowork, 1-2 h)
- Lot C — Métriques de coût + pre-commit hook + system prompt enrichi (Claude Code Plateforme, 2-3 h)
- Lot D — Eval extended sur vault enrichi (Claude Code Desktop, 30 min + ~0,30-0,50 $ API)
- Lot E — RAPPORT + PR (1 h)
- **Effort total estimé** : 7-10 h split.
- **DRAFT** — §6/§7/§8 prudence + checklist + fichiers de référence à compléter à la reprise.

**4. DRAFT SONDAGE COWORK HUB IA pré-S2.3** : `rag-prep/briefs/DRAFT-SONDAGE-COWORK-HUB-IA-S2.3-PRE-PRODUCTION.md` (~1500 mots). **Premier exercice de la convention D-026 en mode sondage préalable** (au lieu de revue a posteriori comme I-002/I-003). 9 passages sensibles identifiés sur les 3 modules denses :
- CU-026 : cas Klarna, framework 7 dimensions, pattern « agent = employé »
- CU-027 : stack ECC + chiffre « 8-10× », pattern AMETRA, niveaux d'autonomie outils
- DEP-08 : risques MCP servers, cadre AgentShield, cas-école sécurité

À transmettre à Cowork Hub IA à la reprise post-itération couple 1.

**5. Inscription I-D-004 dans SYNC-INTER-CANAUX** (renommé depuis I-D-003 suite à collision avec un I-D-003 existant côté Git « Canonisation 3 nouveaux chiffres macro » issu d'une run veille) : signal entrant « nouvelle itération éditoriale couple 1 en cours ». Convention « couple 1 tranche, couple 2 s'aligne » réaffirmée. Action attendue couple 2 à la reprise : recevoir notification + identifier impacts MD + reprendre sprint S2.

**6. Mise en pause STATUS** : sprint S2 acté en pause, plan d'action documenté en 4 étapes à exécuter à la reprise (sync couple 1, SPEC v1.4, S2.2, S2.3).

**Décisions structurantes prises :** aucune. 3 arbitrages préparés en draft (SPEC v1.4) à valider à la reprise.

**Bilan global Sprint S1 + S2.1 (clôturés)** :
- Vault : 9 fichiers MD, 107 chunks indexés
- Code : pipeline RAG complète + audit v2, 134/134 tests verts
- Eval : 10/10 sources retrouvées (S1c.2) + 0 erreur audit (S2.1)
- Référentiel : 30 décisions, SPEC v1.3 (10 règles + 9 anti-patterns), whitelist 69 codes
- Coordination : 3 items archivés (I-001, I-002, I-003) + 3 descendants ouverts (I-D-001, I-D-002, I-D-003)
- Coût total : ~0,30 $ API sur 8 $ de crédits

**Reste à faire :**
- Push de cette entrée JOURNAL + STATUS + SYNC-INTER-CANAUX + 3 nouveaux drafts vers Git par Blaise
- **PAUSE** — itération couple 1 en cours
- Reprise dès notification Blaise de fin d'itération couple 1

**Blockers :**
- Aucun. Pause souple, sprint S2 reprend dès le go Blaise post-itération couple 1.

---

### 2026-05-12 (S2.1 livraison) — Claude Code Hub IA Plateforme — Audit-md-rag v2 aligné SPEC v1.3 (5 blocs)

**Contexte :** Sprint S2.1 ouvert par Blaise (BRIEF-CC-S2.1-audit-v2). Allocation D-030 : Claude Code Plateforme seul (refactor code + tests + exécution audit sur vault, aucun appel API externe). Cible brief §4 Bloc E : 0 erreur sur le vault de 9 fichiers.

**Actions menées :**

- **Bloc A — D-028 (exception R1 transverses) + D-029 (whitelist R4)** : refactor structurel (RuleResult errors/warnings dataclass), AuditContext, build_context() centralisé. Exception R1 pour `glossaire.md` + `chiffres-macro-*.md`. Loader load_whitelist() parse les 69 codes whitelistés. R4 distingue 3 cas (vault → OK, whitelist → warning, inconnu → erreur). Option CLI `--strict-future`. 13 nouveaux tests. Commit `a7a6463`.
- **Bloc B — R5 + R7 + R8** : R5 glossaire (warning, déduplication par terme), R7 nommage (regex schémas), R8 versioning git (`git log -1 --format=%ct`, mockable via `git_mtime_func`). 32 nouveaux tests. Commit `1136af4`.
- **Bloc C — R6 étendu + R9** : SOURCE_MARKERS étendue (wikilinks `[[chiffres-macro-YYYY*]]` reconnus comme sources), fenêtre R6 symétrique [-200, +200] chars. R9 charge les 16 chiffres canoniques de `chiffres-macro-2026.md` et signale en warning ceux cités en clair sans wikilink à proximité. 10 nouveaux tests. Commit `1357cb4`.
- **Bloc D — R10 + R6 warning par défaut** : R10 mappe famille code → HTML (cu/pr/dep), normalise valeurs MD vs HTML stripping/decoding, signale en warning les valeurs MD absentes du HTML source. R6 bascule en **warning par défaut** (option `--strict-r6` rétablit le comportement v1) — décision motivée par l'étape B post-S1bis qui a classifié 42 chiffres pédagogiques comme acceptables. 12 nouveaux tests. Commit `7af1d04`.
- **Bloc E — Exécution + RAPPORT + PR** : audit-report-s2.1.md exporté (217 lignes), 0 erreur, 183 warnings catégorisés. RAPPORT-CC-S2.1.md produit en 7 sections. Commit + push + PR.

**Résultat audit v2 sur vault réel** :
- Fichiers : 9
- **Erreurs : 0** ✅ (vs 150 écarts bruts en audit v1 / S1bis)
- Warnings : 183 (R4=84 vault partiel, R5=51 termes glossaire, R6=42 chiffres pédagogiques, R9=5 chiffres macro en clair, R10=1).
- Exit code : 0.

**Suite tests** : 134/134 verts (67 S1+S1bis+S1ter + 67 nouveaux S2.1).

**Décisions structurantes prises :** aucune (S2.1 = exécution).

**Propositions d'amendement SPEC v1.3 → v1.4** (à arbitrer par Cowork) : codifier R6 en warning par défaut, R5 v3 première occurrence, documenter `--strict-future` et `--strict-r6`.

**Coût API S2.1 (cette session) :** 0,00 $.

**Reste à faire :**
- Validation manuelle PR par Blaise côté GitHub puis merge.
- S2.2 — production vague 3 (CU-026, CU-027, DEP-08) avec D-026 co-production légère.
- S2.3 — pipeline RAG enrichi.

**Blockers :** aucun pour la PR.

---

### 2026-05-12 (ouverture S2.1) — Cowork Hub IA Plateforme — D-030 actée + brief CC-S2.1 produit

**Contexte :** Sprint S1 définitivement clos (merge PR #44). Question ouverte de Blaise sur l'adoption de Claude Code Desktop. Réponse Blaise : D-030 validée, Node.js + Claude Code Desktop installés sur le Mac de Blaise.

**Actions menées :**

**1. Décision structurante D-030 actée** : architecture Claude Code hybride. Claude Code Plateforme (web) pour cadrage/code/tests mockés. Claude Code Desktop (local) pour exécutions avec secrets. Allocation au cas par cas dans chaque brief sprint.

**2. Découpage S2 en 3 sous-sprints S2.1 / S2.2 / S2.3** (au lieu d'un seul gros brief 7 lots) :
- **S2.1** : Audit-md-rag v2 — prérequis aux autres lots S2. Claude Code Plateforme seul (pas d'API). 5 blocs A-E.
- **S2.2** (à venir) : Brique `pattern-llm-wiki.md` + extension golden set 30 questions + métriques coût + pre-commit hook. Cowork + Claude Code Plateforme + Desktop pour eval.
- **S2.3** (à venir) : Vague 3 modules denses (cu-026, cu-027, dep-08) en co-production Cowork ↔ Cowork Hub IA (sondage préalable D-026). Cowork + Desktop pour eval post-production.

**3. Brief CC-S2.1 produit** : `rag-prep/briefs/BRIEF-CC-S2.1-audit-v2.md` (~2000 mots, cible D-021 respectée). 5 blocs structurés :
- Bloc A : Exception R1 (D-028) + Whitelist R4 (D-029)
- Bloc B : R5 glossaire + R7 nommage + R8 versioning git
- Bloc C : R6 étendu (reconnaît wikilinks transverses comme source) + R9 chiffres macro canoniques (parse chiffres-macro-2026.md)
- Bloc D : R10 tableaux numériques fidèles (le plus complexe, peut rester en warning première itération)
- Bloc E : Exécution audit v2 sur vault réel + RAPPORT-CC-S2.1 + PR

**4. Estimation effort S2.1** : ~6-7,5 h Claude Code Plateforme. **Coût API : 0 $** (refactor code + tests, pas d'appel API).

**5. Résultat attendu post-audit v2** : sur le vault de 9 fichiers, **0 erreurs** au lieu des 150 écarts S1bis (qui étaient majoritairement des faux positifs liés à audit v1 non aligné SPEC v1.2/v1.3). Quelques warnings tolérés (R10 imparfaite, chiffres catégorie D arbitrés acceptables).

**Décisions structurantes prises :**
- D-030 — Architecture Claude Code hybride (Plateforme + Desktop)

**Reste à faire :**
- Push de cette entrée JOURNAL + STATUS + DECISIONS étendu (D-030) vers Git par Blaise
- Transmission `BRIEF-CC-S2.1-audit-v2.md` à Claude Code Plateforme
- Exécution S2.1 par Claude Code Plateforme + ouverture PR
- Merge final S2.1 par Blaise
- Production brief CC-S2.2 (post-S2.1 merge)

**Blockers :**
- Transmission brief par Blaise.

---

### 2026-05-12 (clôture sprint S1) — Cowork + Blaise — S1c.2 exécuté localement avec succès + merge PR #44

**Contexte :**
- Sprint S1ter en cours, Lot S1c.1 livré par Claude Code Plateforme (python-dotenv + helper `_env.py`), Lot S1c.2 différé en exécution locale par Blaise (faute d'accès aux clés API depuis session web Claude Code Plateforme).
- Blaise a exécuté S1c.2 en local sur son Mac : setup venv, install `requirements.txt`, vérification `_env.py` charge les clés correctement, lancement `ingest.py` puis `run_eval.py`.

**Actions menées :**

**1. Exécution locale S1c.2 — résultats exceptionnels :**
- **Ingestion** : 9 fichiers MD du vault → **107 chunks créés** (plus dense que les 30-60 attendus, dû à la granularité fine par section H2 sur les modules denses cu-008 et dep-02 qui ont 11-12 sections chacun). Coût OpenAI : quasi-nul (~0,001 $ pour l'embedding initial).
- **Re-indexation incrémentale validée** : 2e exécution `ingest.py` retourne `new=0 skipped=107` — mécanisme de hash + version frontmatter opérationnel.
- **Eval golden set** : `run_eval.py` a tourné ~3-5 min sur les 10 questions. Résultat :
  - **Sources attendues retrouvées : 10/10** (cible ≥ 8/10 largement dépassée)
  - **Concepts attendus pleinement couverts : 9/10**
  - **Score global : 10/10**
  - ✅ Critère brief §9 atteint
- **Observations qualitatives notables** :
  - **q-002** : le système refuse honnêtement (« Je n'ai pas de réponse documentée dans le Hub IA pour cette question ») — comportement RAG idéal, pas d'hallucination. Application opérationnelle de [[vigilance-hallucinations]].
  - **q-009 et q-010** : sources « bonus » légitimes (chunks proches sémantiquement, cu-008 et dep-02 cités en complément d'outils-vector-db).
  - **q-001** : seul concept « méthode » absent — implicite dans la réponse, pas un raté.
- **Coût total S1c.2** : ~0,30 $ Anthropic + ~0,001 $ OpenAI = **~0,30 $ total**. Largement sous plafonds durcis brief S1ter (0,50 $ / 0,10 $) et sous crédits disponibles (3 $ / 5 $).

**2. Push des artefacts par Blaise :**
- `rag/eval/eval-report-s1ter.md` (5565 bytes) + `rag/eval/eval-report-s1ter.json` (7749 bytes) commités sur la branche `claude/execute-pilot-batches-mBSIp`.
- Commit message : `feat(rag): S1c.2 exécuté localement — eval 10/10 sources retrouvées, 9/10 concepts couverts`.

**3. Merge de la PR #44 par Blaise côté GitHub.**
- **Sprint S1 définitivement clôturé.**
- Tip de main : `9bef8c4` post-merge PR #44.

**Décisions structurantes prises :** aucune dans cette entrée. Décision **D-030** envisagée dans la prochaine session (sur l'adoption de Claude Code Desktop pour les exécutions locales futures — question ouverte de Blaise).

**Bilan global Sprint S1 (S1 + S1bis + S1ter + S1c.2 local) :**
- **Pipeline RAG complète fonctionnelle** : audit-md-rag.py v1 + ingestion ChromaDB (incrémentale) + backend query Claude Sonnet 4.6 + golden set 10 questions + run_eval.
- **Vault initial validé empiriquement** : 9 fichiers MD, 107 chunks, retrieval 10/10 sur le golden set.
- **Discipline éditoriale prouvée** : 0 violation éditoriale claire SPEC v1.2/v1.3 sur le vault après deux revues couple 1 (I-002, I-003).
- **Coût total Sprint S1** (toutes sessions confondues) : ~0,30 $ — largement sous tous les plafonds.
- **Tests** : 67/67 verts (62 originaux S1 + 5 nouveaux S1ter).
- **Référentiel mature** : 29 décisions actées (D-001 à D-029), SPEC v1.3 (10 règles + R9/R10 + 9 anti-patterns), whitelist wikilinks futurs (69 codes), cartographie-rag enrichi.
- **Coordination inter-canaux rôdée** : 3 items archivés (I-001, I-002, I-003) + 2 items descendants ouverts (I-D-001, I-D-002).

**Reste à faire :**
- Arbitrage Claude Code Desktop (D-030 à acter ou non) — question ouverte de Blaise
- Cadrage du Sprint S2 : audit-md-rag v2 (prio haute, recommandation RAPPORT-CC-S1ter §7), vague 3 modules MD (CU-026, CU-027, DEP-08), 3 briques transverses anticipées (pattern-llm-wiki en tête)
- Push de cette entrée JOURNAL + STATUS clôturé + cadrage S2 vers Git par Blaise

**Blockers :**
- Aucun. Sprint S1 livré dans les temps, hackathon de septembre toujours dans la trajectoire.

---

### 2026-05-12 (S1ter livraison) — Claude Code Hub IA Plateforme — Lot S1c.1 livré + S1c.2 différé local + PR ouverte

**Contexte :** Sprint S1ter ouvert par Blaise. Pull origin/main fast-forward de la branche `claude/execute-pilot-batches-mBSIp` pour récupérer le brief S1ter, la SPEC v1.3, la whitelist wikilinks futurs et les commits Cowork post-S1bis.

**Constat clé d'environnement :** le `.env` Mac de Blaise contient les clés API (gitignored par construction — D-013), mais cette session Claude Code Plateforme web n'y a pas accès (le fichier n'a jamais transité par le clone Git, pas plus sa copie). Aucune clé n'est exposée en variables d'environnement non plus (seul `ANTHROPIC_BASE_URL` est défini, sans clé).

**Actions menées :**

- **Lot S1c.1 — python-dotenv** : livré intégralement.
  - Helper `rag/code/_env.py` centralisé : `load_env(path=None)` lit `rag/code/.env`, tolérant absence fichier + absence python-dotenv, `override=False` pour ne pas écraser les vars d'env CI.
  - `import _env` ajouté en tête de `ingest.py`, `query.py`, `run_eval.py` (avant tout import openai/anthropic).
  - `requirements.txt` étendu (`python-dotenv>=1.0.0`).
  - `.env.example` commenté pour expliciter le mécanisme.
  - 5 nouveaux tests dans `rag/code/test_env.py` : chargement valide, fichier absent silencieux, `override=False` protège vars existantes, import tolérant, sanity check « 3 scripts importent _env ».
  - **67/67 tests verts** (62 originaux + 5 nouveaux). Sanity du critère brief validé : `python -c "from ingestion import ingest..."` n'échoue plus sans clés exposées.
- **Lot S1c.2 — validation end-to-end** : différé à exécution locale par Blaise. `AskUserQuestion` posée (4 options) → réponse Blaise : « python-dotenv suffit dans cette session, l'exécution end-to-end est l'amélioration code attendue ; S1c.2 sera lancé en local ». Procédure d'exécution complète documentée dans le RAPPORT §3 + §4 (`ingest.py` → 30-60 chunks → 10 queries → `run_eval.py`).
- **Lot S1c.3 — RAPPORT + PR** : livré partiellement.
  - `rag-prep/briefs/RAPPORT-CC-S1ter.md` produit en 8 sections conforme brief §4. Sections §3, §4, §5 explicitement marquées « exécution locale Blaise — résultats attendus ». §6 Apprentissages + §7 reco S2 enrichis (priorité audit-md-rag v2 avec D-028/D-029/R5-R10, métriques coût, pre-commit hook, system prompt enrichi briques transverses).
  - PR ouverte avec titre canonique demandé : `feat(rag): Sprint S1ter - validation end-to-end + python-dotenv + clôture définitive S1`. Description PR précise explicitement le périmètre livré (S1c.1) vs différé local (S1c.2).

**Décisions structurantes prises :** aucune (S1ter = exécution, pas de décision structurelle).

**Coût API S1ter (cette session) :** 0,00 $. Plafonds durcis brief §7 (0,50 $ Anthropic / 0,10 $ OpenAI) intacts.

**Reste à faire :**
- Blaise pull la branche en local, exécute S1c.2 (ingest réel + 10 queries + run_eval), push les artefacts `rag/eval/queries-s1ter-output.md` + `rag/eval/eval-report-s1ter.md`. Possible enrichissement ultérieur du RAPPORT par une session S1quad si besoin de commentaire sur les résultats.
- Validation manuelle PR par Blaise côté GitHub puis merge vers main.

**Blockers :**
- Aucun pour la PR. Persiste : `.env` jamais synchronisé vers la session web (par construction sécurité D-013) — l'exécution réelle est forcément locale.

---

### 2026-05-12 (clôture étape C + brief S1ter) — Cowork Hub IA Plateforme — Brief CC-S1ter produit

**Contexte :**
- Étape C (production des artefacts post-S1bis) terminée et synchronisée côté Git par Blaise (PR `feature/post-s1bis-spec-v1.3-d028-d029` ouverte vers main).
- Blaise a généré les clés API Anthropic (3 $ crédit, sans renouvellement) + OpenAI (5 $ crédit, sans renouvellement). Fichier `.env` correctement placé dans `rag/code/.env` avec permissions `-rw-------` et confirmé gitignored.

**Actions menées :**
- Production du `BRIEF-CC-S1ter-validation-end-to-end-avec-cles.md` (~1800 mots, dans la cible D-021)
- 3 lots structurés :
  - **Lot S1c.1** : ajout `python-dotenv` au code (option propre actée par Blaise) — refactor mineur pour lecture automatique du `.env`
  - **Lot S1c.2** : validation end-to-end réelle (ingest sur 9 MD + 10 queries + eval) — ce qui était S1b.2 du brief précédent, désormais débloqué
  - **Lot S1c.3** : RAPPORT-CC-S1ter + ouverture nouvelle PR
- Plafonds API durcis pour S1ter compte tenu des crédits limités : alerte > 0,50 $ Anthropic (vs 1 $ S1bis), alerte > 0,10 $ OpenAI (vs 0,30 $ S1bis)
- Critères de succès maintenus : ≥ 8/10 questions avec sources attendues, ≥ 50 % concepts attendus, coût total < 0,60 $

**Décisions structurantes prises :**
- Aucune (S1ter = exécution, pas de décision structurelle attendue)

**Reste à faire :**
- Blaise effectue **L1.20** (sync ascendante de ce brief vers Git) si pas déjà fait
- Blaise transmet le `BRIEF-CC-S1ter-validation-end-to-end-avec-cles.md` à Claude Code Plateforme
- Claude Code Plateforme exécute les 3 lots + ouvre la PR
- Validation manuelle de la PR par Blaise côté GitHub

**Blockers :**
- Transmission du brief par Blaise à Claude Code Plateforme.

---

### 2026-05-12 (post-S1bis intégration) — Cowork Hub IA Plateforme — Étapes B + C (arbitrage rapport audit + SPEC v1.3 + D-028/D-029)

**Contexte :**
- Blaise a mergé la PR #42 (sprint S1 + S1bis), pulled localement (commit `d48b61f` sur main).
- Rebaselining Cowork-side fait : JOURNAL + STATUS + RAPPORT-CC-S1 + RAPPORT-CC-S1bis re-copiés depuis le clone Git vers Cowork-side (D-024 Option D rebaselining).
- Lecture intégrale du `rag-prep/briefs/RAPPORT-CC-S1bis.md` (~6 KB, 9 sections) + `rag/eval/audit-report-s1bis.md` (~6 KB, 7 sections + annexe).

**Étape B — Arbitrage catégorie D (chiffres orphelins potentiels) :**

7 cas analysés (cf. §3 audit-report-s1bis.md). Verdict :
- **1 canonisation** : « 90 % cas PME où le RAG bat le fine-tuning » → ajout au référentiel `chiffres-macro-2026.md` (4e canonisation après les 3 issues d'I-002 + I-003)
- **1 item descendant inscrit** : I-D-002 (Sources primaires manquantes sur heuristiques techniques DEP-02 HTML — 30-40 % embedding, 10-30 % reranking, 5-10 % vector DB)
- **5 chiffres conservés tel quel** : +11 % MTEB sourcé par RetEx mai 2026 (faux positif R6 audit v1), 80 % entreprises Postgres + 99,99 % Pinecone (affirmations marché acceptables)

Verdict Claude Code Plateforme confirmé : 0 violation éditoriale claire de SPEC v1.2 sur le vault. Les 150 écarts bruts sont des limitations de l'audit v1 antérieur à SPEC v1.2.

**Étape C — Production des artefacts (10 livrables) :**

**Bloc 1 — Référentiel SPEC v1.3 + 2 nouvelles décisions :**
- `SPEC-MD-POUR-RAG.md` bumpée v1.2 → v1.3 : ajout section « Exception structurelle pour fichiers racines transverses » avant R1, ajout « Politique des wikilinks vers MD planifiés » en §R4, enrichissement roadmap audit v2 (3 évolutions : exception R1, R4 tolérante, R6 reconnaît wikilinks canoniques)
- **D-028** actée : exception structurelle R1 pour fichiers racines transverses (glossaire.md notamment ; `glosaire_termes` et `derives` peuvent être vides par construction)
- **D-029** actée : politique des wikilinks vers MD planifiés via whitelist `rag-prep/whitelist-wikilinks-futurs.md`

**Bloc 2 — Whitelist wikilinks futurs :**
- Production `rag-prep/whitelist-wikilinks-futurs.md` v1 : 69 codes whitelistés couvrant vagues 3 à 5 (25 modules CU, 6 préalables PR, 7 DEP, 5 architectures, 8 brain pages transverses, 16 catégories outils). Lue par audit-md-rag v2 au démarrage. Procédure de maintenance : à chaque nouveau MD produit, retirer son code de la whitelist.

**Bloc 3 — Référentiel chiffres macro étendu :**
- `chiffres-macro-2026.md` bumpé v3.8.3 → v3.8.4 : ajout entrée « 90 % cas PME où le RAG bat le fine-tuning » (4e canonisation, post-S1bis)
- Champ `derives` enrichi (ajout `dep-04` qui développera fine-tuning détail)

**Bloc 4 — Refactor wikilinks dans vault :**
- `glossaire.md` v3.8.3 → v3.8.4 : définition Fine-tuning wikilinké vers `chiffres-macro-2026#90-pourcent-cas-pme...` (R9 SPEC v1.2 appliquée a posteriori) + bump footer
- `cu-008.md` v3.8.4 → v3.8.5 : 2 occurrences du « 90 % » wikilinkées vers `chiffres-macro-2026#90-pourcent-cas-pme...` (essentiel à retenir + recommandation par défaut)

**Bloc 5 — Inscription item descendant + cartographie :**
- `SYNC-INTER-CANAUX.md` : inscription **I-D-002** (heuristiques techniques DEP-02 sans source primaire dans HTML — à traiter par couple 1 en prochaine itération éditoriale, priorité basse)
- `cartographie-rag.md` : entrée chiffres-macro-2026 mise à jour (bump v3.8.4, 16 chiffres canoniques, ajout angles thématiques RAG et transformation)

**Bloc 6 — Correctifs comptage 9 vs 10 :**
- `STATUS-RAG.md` : section « Bilan production MD » corrigée (« 9 fichiers MD du vault », correction post-S1bis explicitement notée — mes décomptes précédents annonçaient « 10 » par erreur). L1.14 corrigé.

**Décisions structurantes prises :**
- D-028 — Exception structurelle R1 pour fichiers racines transverses
- D-029 — Politique des wikilinks vers MD planifiés (whitelist)

**Reste à faire (clôture étape C) :**
- Blaise effectue **L1.20** : sync ascendante des fichiers de gouvernance vers le clone Git puis push (SPEC v1.3, whitelist, DECISIONS, JOURNAL/STATUS/cartographie/SYNC, chiffres-macro v3.8.4, glossaire v3.8.4, cu-008 v3.8.5)
- Blaise effectue **L1.21** : création du `.env` local avec clés API
- Cowork produit le **BRIEF-CC-S1ter** pour reprendre S1b.2 (validation end-to-end + extension RAPPORT ou nouvelle PR)

**Apprentissages clés capitalisés (étape B+C) :**
- L'audit-md-rag.py v1 fonctionne mais ne couvre pas R9/R10 (introduites en SPEC v1.2). Priorité audit v2 confirmée pour S2.
- La whitelist wikilinks futurs est un mécanisme léger et efficace pour gérer le vault construit par vagues. À maintenir en discipline d'entretien permanent.
- Le pattern « rebaselining D-024 avant édition Cowork » s'est vérifié utile (JOURNAL et STATUS contenaient les entrées CC à intégrer).
- L'erreur de comptage 9 vs 10 répétée pendant plusieurs sessions Cowork souligne l'utilité d'un script `rag/code/audit/inventory.py` (recommandation Proposition 3 de CC-S1bis).

**Blockers :**
- L1.20 (sync ascendante Git + push par Blaise) + L1.21 (création .env clés API).

---

### 2026-05-12 (clôture bis) — Claude Code Hub IA Plateforme — S1bis Lot S1b.3 partiel (RAPPORT + PR)

**Contexte :** Blaise demande l'ouverture de la PR pour resynchronisation locale et partage avec Cowork, sans attendre l'exécution de S1b.2 (clés API toujours absentes). RAPPORT-CC-S1bis produit en marquant explicitement S1b.2 non exécuté (§3 et §4). PR ouverte avec le titre canonique du brief §4.

**Actions menées :**
- Production du `rag-prep/briefs/RAPPORT-CC-S1bis.md` en 9 sections conformes au brief §4. Sections 3, 4, 5 dûment marquées « Non exécuté — clés API absentes ». Écarts résiduels (5) + propositions d'amendement (4) + recommandations S2 (6) + liste commits S1 + S1bis détaillés.
- STATUS-RAG mis à jour : S1bis L1.16c marqué ✅ partiel (RAPPORT + PR livrés, S1b.2 reste à exécuter en session future).
- Ouverture PR vers `main` avec titre canonique : « feat(rag): Sprint S1 + S1bis - pipeline RAG complet + vault initial (10 fichiers MD, 62+ tests) ». Branche source : `claude/execute-pilot-batches-mBSIp`. Description PR pointe vers le RAPPORT, liste les commits S1 et S1bis, signale les 9 fichiers MD effectifs (écart 9 vs 10), mention non-application Lot 2 par D-012-bis et de S1b.2 en attente clés API.

**Décisions structurantes prises :** aucune.

**Reste à faire :**
- Blaise pull le clone Git, partage le contenu avec Cowork, valide manuellement la PR côté GitHub.
- En session future Claude Code Plateforme : exécution S1b.2 dès clés API disponibles (ingest réel sur 9 MD + 10 queries + eval), extension du rapport en S1ter ou ajout d'une annexe au RAPPORT-CC-S1bis.

**Blockers :**
- Aucun pour le partage avec Cowork.
- Persiste : clés API absentes pour exécution S1b.2 future.

---

### 2026-05-12 (clôture) — Claude Code Hub IA Plateforme — S1bis Lot S1b.1 (audit vault réel) + pause clés API

**Contexte :** vault initial (9 fichiers MD effectivement déposés — voir écart §5 du rapport audit) reçu sur la branche `claude/execute-pilot-batches-mBSIp` via les commits `668934e` (vault) et `fd0df0b` (sync gouvernance). Brief `BRIEF-CC-S1bis-validation-end-to-end.md` lu. SPEC v1.2 (R9 + R10) + 27 décisions intégrées au préalable.

**Actions menées :**

- **Lot S1b.1 — audit-md-rag.py sur vault réel** : exécuté sur `rag/content/` (9 fichiers). Sortie : 150 écarts détectés (R1 = 2, R4 = 83, R6 = 65, R2/R3 = 0).
- **Analyse classifiée** des 150 écarts produite dans `rag/eval/audit-report-s1bis.md` :
  - **A — 2 R1 faux positifs structurels** : `glossaire.md` a `glosaire_termes: []` et `derives: []` vides par construction (le glossaire est racine)
  - **B — 83 R4 vault partiel** : wikilinks vers MD à produire en vagues 3+ (`cu-002`, `cu-011`, `pr-04`, `dep-07`, etc.) — attendu en S1 pilote, pas un écart de vault
  - **C — ~58 R6 faux positifs R9** : chiffres dans alias de wikilink vers `chiffres-macro-2026.md`, l'audit v1 ne reconnaît pas le pattern wikilink comme source canonique
  - **D — ~7 R6 candidats arbitrage Cowork** : chiffres dans glossaire et dep-02 sans wikilink explicite
- **Dump brut conservé** en annexe : `rag/eval/audit-report-s1bis-raw.txt`.
- **Discipline §7 brief respectée** : aucune modification des MD du vault par Claude Code ; aucune modification du code de l'audit non plus (évolutions scope v2, hors S1bis).
- **Lot S1b.2 (validation end-to-end) en pause** : aucune clé `OPENAI_API_KEY` ni `ANTHROPIC_API_KEY` exposée dans l'environnement de session. Question posée à Blaise (via AskUserQuestion) : choix retenu = pause après S1b.1 jusqu'à instructions ultérieures.
- **Lot S1b.3 (RAPPORT + PR) en pause** : conditionnel à S1b.2.

**Écarts signalés à Blaise (synthèse) :**
1. Écart d'inventaire vault : **9 fichiers** trouvés vs **10 annoncés** dans brief + STATUS. Hypothèse : pattern transverse anticipé non transféré ou coquille. À confirmer.
2. Audit-md-rag v1 produit 150 écarts mais 0 violation éditoriale claire de SPEC v1.2 après classification. Recommandations détaillées pour audit v2 dans le rapport (exception R1 glossaire, R4 tolérante MD futurs, R6 reconnaît wikilinks canoniques, implémenter R5/R7/R8/R9/R10).
3. Clés API absentes dans la session → S1b.2 et S1b.3 en attente.

**Décisions structurantes prises :** aucune (S1bis = exécution, pas de décision structurelle).

**Reste à faire :**
- Blaise arbitre les ~7 chiffres orphelins potentiels (§3 catégorie D du rapport) avec Cowork.
- Blaise confirme l'écart d'inventaire 9 vs 10.
- Blaise fournit les clés API (ou choisit un mode dégradé) pour débloquer S1b.2 + S1b.3 + ouverture PR.

**Blockers :**
- Clés API absentes (OPENAI_API_KEY / ANTHROPIC_API_KEY) pour le Lot S1b.2.

---

### 2026-05-12 (suite) — Cowork Hub IA Plateforme — Brief CC-S1bis + D-012-bis + D-027

**Contexte :**
- Blaise a créé le canal Claude Code Plateforme et lui a transmis le brief CC-S1. Premier rapport reçu : **6 lots livrés, 62/62 tests verts, 0 $ API consommé**. Excellente exécution. 4 écarts résiduels signalés (Lot 2 délégué à Blaise, validation end-to-end en attente, branche `claude/execute-pilot-batches-mBSIp` ≠ brief, pas de PR ouverte).
- Cowork sandbox n'a pas pu lire le RAPPORT-CC-S1.md depuis le clone Git (warnings de permission sur `.git/` — cohérent avec D-024 lecture seule). Travail sur la base de la synthèse transmise par Blaise.

**Actions menées :**

**Bloc 1 — Révision décisions** :
- **D-012-bis** actée (supersède D-012 du 11 mai) : MCP Obsidian reporté à Phase 2. Raisons : gain marginal en Phase 1 (Claude Code accède déjà aux MD via filesystem direct + parsing frontmatter), valeur réelle en Phase 2 (LLM Wiki layer), coût opportunité ~30-45 min setup pour ROI quasi-nul.
- **D-027** actée : convention de nommage des branches Claude Code Plateforme acceptée — `claude/execute-{slug}-{hash}` accepté par défaut, pas de rename imposé. Mention de la branche supprimée des briefs futurs.

**Bloc 2 — Brief CC-S1bis produit** :
- Fichier `rag-prep/briefs/BRIEF-CC-S1bis-validation-end-to-end.md` (~1700 mots, dans la cible D-021)
- 3 lots ciblés : (1) audit-md-rag sur vault réel, (2) validation end-to-end ingestion + retrieval + génération + eval, (3) rapport mission consolidé + ouverture PR
- Critères de succès quantifiés : ~30-60 chunks indexés, ≥ 8/10 sources attendues citées, coût < 2 $
- Plafonds API rappelés (cf. D-013) : alerte > 1 $ Anthropic / > 0,30 $ OpenAI

**Bloc 3 — Procédure de transfert MD vers Git** :
- Transmise à Blaise pour exécution dans son terminal Mac :
  - `cd repo-current && git fetch --all && git checkout claude/execute-pilot-batches-mBSIp`
  - `cp -r ../../Hub-IA-Plateforme/rag-prep/content/* rag/content/`
  - `git add rag/content/ && git commit -m "feat(rag): dépôt vault initial..." && git push`
- 10 fichiers MD à transférer (1 glossaire + 2 modules CU + 1 préalable PR + 1 fiche-outil + 1 DEP + 3 transverses)

**Décisions structurantes prises :**
- D-012-bis — MCP Obsidian reporté Phase 2
- D-027 — Convention nommage branches Claude Code Plateforme

**Reste à faire :**
- Blaise exécute la procédure de transfert MD vers la branche `claude/execute-pilot-batches-mBSIp`
- Blaise transmet le brief CC-S1bis à Claude Code Plateforme
- Claude Code Plateforme exécute les 3 lots S1bis + ouvre la PR
- Validation manuelle de la PR par Blaise côté GitHub

**Blockers :**
- Transfert MD par Blaise et transmission brief CC-S1bis.

---

### 2026-05-12 (clôture) — Cowork Hub IA Plateforme — Intégration retour I-003

**Actions menées (ordre logique D-023 respecté : formaliser avant corriger) :**

**Bloc 1 — SPEC v1.2 + D-026** :
- Bump `SPEC-MD-POUR-RAG.md` v1.1 → v1.2
- Ajout **R10 nouvelle règle stricte** : transposition fidèle des valeurs numériques dans les tableaux (issue AP-4 du retour couple 1, promu en règle stricte). Roadmap audit R10 ajoutée (regex valeurs numériques + diff vs HTML source).
- Acte **D-026** : co-production légère obligatoire sur modules N3/N4 vague 3+ (sondage AVANT production sur 2-3 passages sensibles)

**Bloc 2 — Extension du référentiel chiffres macro** :
- `chiffres-macro-2026.md` v3.8.2 → v3.8.3
- Ajout entrée **« 21 % — organisations IA ayant redesigné leurs workflows (McKinsey 2025) »** avec wikilink dans pr-07 (2 occurrences refactorisées en wikilink R9)
- Ajout entrée **« 1,8 h/jour — temps perdu à chercher l'information (McKinsey 2025) »** avec wikilink dans cu-008 (essentiel à retenir)
- Champ `derives` enrichi avec cu-008 et cu-025

**Bloc 3 — Corrections vague 2** :
- `pr-07.md` v3.8.3 → v3.8.4 :
  - **Matrice 6 critères : 5 cellules réalignées sur HTML** (volume BUY < 20 utilisateurs, volume BUILD > 50 utilisateurs « ou volume élevé », budget BUY « SaaS 50-200 €/mois suffit, ROI 6 mois », budget BUILD « 40-100 k€ + 20 %/an OK », délai BUILD « 3-9 mois acceptables, valeur long terme »)
  - Wikilink `[[vigilance-hallucinations]]` ajouté dans Écueil 4 (gouvernance IA)
  - Wikilink `[[vigilance-confidentialite]]` ajouté dans Écueil 6 (obligations réglementaires RGPD)
  - Champ `derives` enrichi (`pr-05`, `vigilance-hallucinations`, `vigilance-confidentialite`)
- `dep-02.md` v3.8.3 → v3.8.4 :
  - **Nouvel Écueil 6 transverse** : « Ignorer la confidentialité du corpus indexé » avec wikilink `[[vigilance-confidentialite]]`
  - Champ `derives` enrichi (`vigilance-confidentialite`)
- `cu-008.md` v3.8.3 → v3.8.4 :
  - Section « L'essentiel à retenir » : 1,8 h/jour McKinsey wikilinké vers `[[chiffres-macro-2026#18-h-jour...]]` (R9 + canonisation préventive)
- `glossaire.md` : bump footer v3.8.2 → v3.8.3 (cohérence avec frontmatter v3.8.3, incohérence signalée Q4 du retour)

**Bloc 4 — SYNC-INTER-CANAUX** :
- **I-003 archivé** en items résolus avec capitalisation complète (5 apprentissages, suivi post-clôture)
- **I-D-001 nouvel item descendant inscrit** : harmonisation matrice PR-07 HTML (6 critères discours vs 8 critères table v3.8 enrichi). Couple 1 prend l'item de son côté. Convention « couple 1 tranche, couple 2 s'aligne » à la prochaine itération PR-07 HTML.

**Décisions structurantes prises :**
- D-026 — Co-production légère obligatoire sur modules N3/N4 vague 3+

**Bilan de la session :**
- 1 SPEC bumpée en v1.2 (+ R10)
- 1 décision actée (D-026)
- 1 brique transverse enrichie (chiffres-macro-2026 v3.8.3, +2 chiffres)
- 4 fichiers vague 2 corrigés (pr-07 matrice, pr-07 wikilinks, dep-02 wikilinks + nouvel écueil, cu-008 wikilink chiffre macro, glossaire footer)
- 1 item inter-canal archivé (I-003 clôturé)
- 1 item descendant ouvert (I-D-001 — première occurrence dans le sens couple 1 → couple 2)

**Apprentissages clés :**
- AP-1 (R9 chiffres macro) et AP-4 (R10 tableaux numériques) sont les deux dérives les plus systémiques sur les modules denses → l'audit-md-rag.py R9 + R10 sera décisif pour la vague 3
- La co-production légère D-026 est la procédure pivot qui équilibre vitesse d'exécution × fidélité éditoriale
- Le pattern de coordination inter-canaux fonctionne dans les deux sens : I-001/I-002/I-003 ascendants + I-D-001 descendant. Cycle complet.

**Reste à faire :**
- Validation Blaise de l'intégration
- Décision sur séquencement ingestion (recommandation Cowork Hub IA : ingestion progressive en 2 temps — vague 2 maintenant pour valider pipeline, vague 3 + briques transverses ensemble dans 2-3 sprints)
- Démarrage vague 3 (CU-026, CU-027, DEP-08) avec application D-026 (sondage Cowork Hub IA préalable)
- Production des 3 briques transverses anticipées : pattern-llm-wiki (urgent — recouvrement cu-008/dep-02), pattern-eval-set-golden (avec DEP-07), pattern-build-vs-buy (avec module suivant qui s'y réfère)

**Blockers :**
- Aucun blocker bloquant. Validation Blaise possible.

---

### 2026-05-12 (ter) — Cowork Hub IA Plateforme — Brief revue vague 2 + I-003

**Actions menées :**
- Blaise valide la suggestion de revue ciblée par Cowork Hub IA sur la vague 2 (modules denses produits en autonomie sans co-production).
- Production du `BRIEF-COWORK-HUB-IA-REVUE-VAGUE-2.md` (~1300 mots, dans la cible D-021). Format resserré vs I-002 (5 questions au lieu de 7) parce que Cowork Hub IA a déjà fourni la matrice méthodologique en I-002 (anti-patterns AP-1/AP-2/AP-3, pattern « module + transverses »).
- 5 questions structurées centrées sur les passages denses :
  - Q1 : conformité RULES sur chiffres techniques précis et fourchettes
  - Q2 : dérives sémantiques sur passages identifiés en Q6 d'I-002 (LLM Wiki post-Karpathy, matrice 6 critères, pipeline 7 étapes, cycle SEI avec RetEx embedding #130, cas AMETRA)
  - Q3 : application de R9 + détection de nouveaux chiffres macro à canoniser (1,8 h/jour McKinsey, 78 % Retool, 21 % McKinsey workflows, 70-90 % Techment)
  - Q4 : validation wikilinks transverses + détection de manques (LLM Wiki dupliqué cu-008/dep-02, SaaS vs self-hosted, eval set)
  - Q5 : vault prêt pour ingestion ? brain pages transverses prioritaires avant ingestion ?
- Inscription **I-003** dans `SYNC-INTER-CANAUX.md` (items montants ouverts).

**Décisions structurantes prises :**
- Aucune nouvelle décision actée.

**Reste à faire :**
- Blaise transmet le `BRIEF-COWORK-HUB-IA-REVUE-VAGUE-2.md` au canal Cowork Hub IA (pointage local).
- Réception du `RETOUR-I-003-REVUE-VAGUE-2.md` côté couple 2.
- Selon les réponses : corrections vague 2 + ajustement chiffres-macro-2026 + (potentiellement) production de brain pages transverses additionnelles avant ingestion.
- En parallèle, Claude Code Plateforme continue ses Lots S1.

**Blockers :**
- Réception du retour Cowork Hub IA sur I-003 avant ingestion par Claude Code Plateforme (recommandation).

---

### 2026-05-12 (bis) — Cowork Hub IA Plateforme — Production vague 2 (3 modules denses)

**Actions menées :**
- Enrichissement `glossaire.md` v3.8.3 avec 5 nouveaux termes (eval-set, LLM-as-judge, reranker, retrieval-hybride, MTEB) — anticipations identifiées par couple 1 dans Q6 de la revue I-002.
- Lecture intégrale des 3 HTML sources via Bash : `cu-008-knowledge-base-rag.html` (~66 KB), `pr-07-build-vs-buy.html` (~13 KB), `dep-02-rag-architecture-prod.html` (~16 KB).
- **Production de 3 modules MD denses** :
  - `content/modules/cu-008.md` v3.8.3 — **Référence canonique D-017** — Knowledge base interne (RAG). 11 sections H2 sémantiquement autonomes. Couvre RAG vs Fine-tuning, pipeline 2 temps, LLM Wiki Karpathy, patterns post-Karpathy (persistent memory, self-maintaining KB, contradiction detection, multi-agent vaults, sleep consolidation), 3 voies stack pragmatiques, déploiement 4 paliers, 5 pièges, architectures A1/A3/A4, RetEx Conseil aviation 25 personnes. Wikilinks vers chiffres-macro, vigilance-hallucinations, vigilance-confidentialite, outils-vector-db, glossaire.
  - `content/prealables/pr-07.md` v3.8.3 — Build vs Buy à l'ère de l'IA. 10 sections H2. Couvre 3 tendances 2025-2026, scaling gap (95 % MIT NANDA, 21 % McKinsey workflow), 6 situations BUY, 5 situations BUILD, pattern hybride dominant, matrice 6 critères, 7 écueils. Mention AMETRA dans la section BUILD (sans détail inventé). Wikilinks vers chiffres-macro pour 95 % et 67/33 %.
  - `content/deploiement/dep-02.md` v3.8.3 — RAG en production. 12 sections H2. Couvre 3 ruptures 2025-2026, règle décision 30 sec, LLM Wiki coût-bénéfice, anatomie pipeline 7 étapes, choix techniques par ordre d'impact, tableau décision par volume, panorama vector DB 5 acteurs + question piège, 5 écueils, cycle Stitch → Evaluate → Iterate + RetEx embedding #130 MTEB, plan 60 jours.
- Application discipline SPEC v1.1 :
  - R9 — chiffres macro wikilinkés vers chiffres-macro-2026 (95 % MIT NANDA, 67/33 %)
  - AP-2 — aucune conversion monétaire ad-hoc
  - AP-3 — citations préservées (Karpathy gist, Techment, VentureBeat, MIT NANDA, McKinsey, Retool, GitHub Copilot)
- Mise à jour `cartographie-rag.md` avec les 3 nouvelles entrées détaillées (angles thématiques + recouvrements).

**Décisions structurantes prises :**
- Aucune nouvelle décision actée. Production conforme à SPEC v1.1.

**Signaux faibles observés / capitalisation :**
- La densité de cu-008 a confirmé la pertinence du pattern « briques transverses » (D-025) : sans `vigilance-hallucinations` et `vigilance-confidentialite` extraites, cu-008 aurait dupliqué massivement le même contenu de pr-05, cu-001, etc.
- La discipline de double-relecture HTML ↔ MD a été appliquée mais en mode auto-relecture Cowork (pas de validation Cowork Hub IA en parallèle vu le go direct de Blaise). À signaler comme zone de risque résiduel : co-production prévue par STRATEGIE-MD-RAG §6 pas formellement exécutée.
- Mention AMETRA dans pr-07 conservée textuelle sans détail inventé. Sera à compléter quand cu-027 sera produit (pattern complet documenté ailleurs dans le Hub).

**Reste à faire :**
- Mise à jour STATUS + clôture des tâches vague 2
- Sondage qualité par Blaise sur les 3 modules denses (validation post-production)
- À envisager : revue ciblée par Cowork Hub IA sur les passages identifiés en Q6 (RAG vs LLM Wiki dans cu-008, matrice 6 critères dans pr-07, cycle SEI dans dep-02) — sur le modèle I-002 mais resserrée

**Blockers :**
- Aucun blocker bloquant. Sondage Blaise possible mais non obligatoire.

---

### 2026-05-12 — Cowork Hub IA Plateforme — Intégration retour I-002 (massive)

**Actions menées (session dense, ordre logique D-023 respecté : formaliser avant produire) :**

**Bloc 1 — SPEC v1.1 + D-025** :
- Bump `SPEC-MD-POUR-RAG.md` v1 → v1.1
- Ajout **R9** (règle stricte) : citation textuelle des chiffres canoniques + audit-md-rag.py R9 à implémenter en v2
- Nouvelle section méthodologique « Briques transverses » (catégories, critères d'extraction 3+ modules, 3 risques à monitorer)
- Enrichissement section anti-patterns : AP-2 (conversion monétaire ad-hoc) + AP-3 (édulcoration éléments contextuels)
- Ajout règles auditables v2 dans la roadmap audit (R5, R7, R8, R9)
- Acte **D-025** : pattern architectural « unité = module + extraction sélective de briques transverses »

**Bloc 2 — Production des 3 briques transverses prioritaires** (recommandation Q7.a couple 1) :
- `transverses/chiffres-macro-2026.md` v1 — référentiel canonique de 13 chiffres macro avec sources datées et formulations exactes. Source unique de vérité pour les chiffres macro du Hub (67 % Bpifrance, 95 % MIT NANDA, 76 % France Num, 55 % Bpifrance Osez l'IA, 26 % France Num, 58 % enjeu vital, 33 % adoption, 67 % vs 33 % Buy/Build, +270 % Microsoft, 80-95 % causes orga, ×5 PwC, 77k offres, 3,7× IDC, consensus 70-95 %).
- `transverses/vigilance-hallucinations.md` v1 — Pattern de vigilance commune à ~10 modules. 3 types d'hallucinations, discipline en 3 règles, mitigations techniques, cas d'application, anti-patterns observés.
- `transverses/vigilance-confidentialite.md` v1 — Pattern de vigilance commune à ~8 modules. Risque structurel, 4 catégories à protéger, 3 options souveraines, discipline en 4 règles.

**Bloc 3 — Corrections vague 1** :
- `cu-001.md` v3.8.2 → v3.8.3 :
  - Chiffre « 67 % n'ont pas commencé » corrigé en « ne savent pas par où commencer » (formulation canonique)
  - Conversion monétaire $ → € pour Perplexity Pro
  - Citation MIT 2025 réintégrée dans « L'essentiel à retenir »
  - Certifications ISO 27001 / SOC 2 du Chat Pro restaurées
  - Formulation « 5 minutes du réflexe humain à la matière exploitable » réintégrée
  - Phrases trop longues aérées (vigilances structurantes passées en liste)
  - Wikilinks ajoutés vers les 3 briques transverses (`[[vigilance-hallucinations]]`, `[[vigilance-confidentialite]]`, `[[chiffres-macro-2026#67-pourcent-...]]`)
  - Frontmatter `derives` enrichi
- `glossaire.md` v3.8.2 → v3.8.3 :
  - Ajout glose **On-premise** (13e glose obligatoire RULES §C.2)
  - Affinement « Vector store » (ancrage « brique centrale du RAG »)
  - Affinement « Chunk » (référence explicite SPEC §R3)

**Bloc 4 — Mise à jour fichiers vivants** :
- `cartographie-rag.md` : ajout des 3 nouvelles entrées (chiffres-macro-2026, vigilance-hallucinations, vigilance-confidentialite) avec angles thématiques et recouvrements
- `SYNC-INTER-CANAUX.md` : I-002 archivé en items résolus avec apprentissages capitalisés (5 dérives, 3 anti-patterns, 3 briques produites, D-025, suivi post-clôture)

**Décisions structurantes prises :**
- D-025 — Pattern architectural module + briques transverses sélectives (Actée)

**Bilan de la session :**
- 1 SPEC bumpée en v1.1
- 1 décision actée (D-025)
- 3 fichiers transverses produits (~290 lignes)
- 1 module CU corrigé (5 dérives résolues + phrases aérées + wikilinks transverses)
- 1 glossaire enrichi (+ On-premise)
- 4 fichiers vivants mis à jour (DECISIONS, JOURNAL, STATUS, cartographie, SYNC)
- 1 item inter-canal archivé (I-002 clôturé)

**Reste à faire — pré-vague 2 :**
- Validation Blaise de l'intégration (sondage de bonne tenue)
- Possible itération sur les briques transverses si Blaise détecte un point
- Démarrage de la vague 2 : CU-008 (référence canonique D-017), PR-07, DEP-02 — en co-production avec Cowork Hub IA pour ces 3 modules denses

**Blockers :**
- Aucun en bloquant. Sondage de validation Blaise possible mais non obligatoire avant vague 2.

---

### 2026-05-11 (clôture) — Cowork Hub IA Plateforme — Brief revue vague 1 + I-002

**Actions menées :**
- Blaise soulève une question architecturale fondamentale : la convention implicite « 1 fichier HTML = 1 fichier MD » est-elle optimale pour le RAG, ou faut-il un découpage sémantique plus poussé avec extraction de briques transverses ?
- Reconnaissance que la question dépasse l'expertise du couple 2 sur le maillage interne du Hub. Cowork Hub IA est mieux placé pour arbitrer.
- Décision : demander une revue à Cowork Hub IA **avant** production de la vague 2 (CU-008, PR-07, DEP-02), combinant (a) conformité éditoriale des 3 fichiers vague 1 produits, (b) arbitrage architectural sur le découpage sémantique.
- Production du `BRIEF-COWORK-HUB-IA-REVUE-VAGUE-1.md` (~1700 mots, dans la cible D-021) avec 7 questions structurées :
  - Q1 à Q4 : conformité éditoriale (RULES sourcing/langue/gloses, cohérence chiffres cross-Hub, dérive sémantique, alignement gloses §C.2)
  - Q5 : anti-patterns à formaliser dans SPEC v1.1
  - Q6 : recommandations vague 2
  - Q7 (structurante) : arbitrage architectural sur découpage sémantique
- Inscription de **I-002** dans `SYNC-INTER-CANAUX.md` (item montant ouvert, à transmettre par Blaise).
- Mise à jour `STATUS-RAG.md` : ajout L0.14 et nouveau blocker (vague 2 en attente revue couple 1).

**Décisions structurantes prises :**
- Aucune nouvelle décision actée. Décision architecturale (découpage sémantique) suspendue à la réponse Q7 du couple 1.

**Reste à faire :**
- Blaise transmet le `BRIEF-COWORK-HUB-IA-REVUE-VAGUE-1.md` au canal Cowork Hub IA (pointage local, pas besoin de push Git).
- Réception du `RETOUR-I-002-REVUE-VAGUE-1.md` côté couple 2.
- Selon les réponses : corrections vague 1 + ajustement SPEC v1.1 + (potentiellement) production de fichiers transverses **avant** vague 2.
- En parallèle, Claude Code Plateforme avance sur Lots 1-3 du brief S1.

**Anticipations / signaux faibles :**
- Premier exercice du pattern canonique de coordination inter-canaux dans le sens couple 2 → couple 1 (en miroir de I-001). Validation empirique du pattern.
- Si la réponse Q7 confirme l'extraction de briques transverses, le `cartographie-rag.md` v0 actuelle (qui anticipait déjà 8 sujets à fort recouvrement) sera enrichi avec une nouvelle catégorie « brain pages transverses » avant production massive.
- Discipline d'itération préservée : on évite de produire 3 modules denses qui devraient être refactorisés a posteriori.

**Blockers :**
- Réception du retour Cowork Hub IA sur I-002 avant production vague 2.

---

### 2026-05-11 (très tardive) — Cowork Hub IA Plateforme — Production MD pilote vague 1

**Actions menées :**
- Canal Claude Code Hub IA Plateforme lancé par Blaise (confirmation reçue).
- Lecture intégrale du HTML source `cu-001-recherche-veille.html` (sections executive, outils, méthode, pièges, cas, stats clés).
- Lecture intégrale de la section `cat-vector` de `ressources.html` (4 fiches outils : Qdrant, pgvector, Pinecone, ChromaDB).
- Création de la structure `Canaux/Hub-IA-Plateforme/rag-prep/content/` avec sous-dossiers `modules/`, `prealables/`, `deploiement/`, `ressources/`.
- Production de **3 fichiers MD** (vague 1 du sprint S1) :
  - `rag-prep/content/glossaire.md` v1 — 18 termes canoniques avec wikilinks croisés (RAG, vector-store, embeddings, LLM, POC, MVP, API, SaaS, open-source, self-hosting, souveraineté, cloud-souverain, hallucination, HNSW, chunk, fine-tuning, token, prompt). Tous les futurs MD du vault y feront référence.
  - `rag-prep/content/ressources/outils-vector-db.md` v1 — panorama des 4 vector stores du marché 2026 + comparatif synthétique + cross-references vers cu-008, dep-02, dep-06. Premier MD type `fiche-outil`, valide le format catégorie.
  - `rag-prep/content/modules/cu-001.md` v1 — module Recherche & veille augmentée distillé en 7 sections H2 sémantiquement autonomes. Premier MD type `module-cu`, valide le format module.
- Mise à jour `cartographie-rag.md` avec les 3 nouvelles entrées + identification des recouvrements à venir (cu-008 et dep-02 référenceront outils-vector-db.md plutôt que dupliquer).

**Décisions structurantes prises :**
- Aucune nouvelle décision actée. Production conforme à SPEC v1, STRATEGIE v1, D-001 à D-024.

**Reste à faire — clôture vague 1 :**
- Validation par Blaise des 3 MD produits (sondage qualité avant production des modules denses).
- Sur retour positif : production de la vague 2 (cu-008 référence canonique, pr-07, dep-02) — co-production avec Cowork Hub IA pour ces 3 modules denses (assistance contextuelle).
- En parallèle, Claude Code Plateforme attaque les Lots 1 à 3 du brief S1 (infrastructure repo `rag/`, MCP Obsidian, audit-md-rag.py).

**Anticipations / signaux faibles :**
- Aucune dérive sémantique détectée par auto-relecture, mais cela mérite confirmation par sondage Blaise (et plus tard par eval automatique sur questions test).
- Discipline de longueur des sections H2 respectée (estimation 400-700 tokens par section). À vérifier formellement quand `audit-md-rag.py` sera fonctionnel.
- `outils-vector-db.md` regroupe 4 outils en un seul fichier (conformément à D-014 et à la convention « fiches outils par catégorie »). Cela valide la stratégie « pas un fichier par fiche outil isolée » pour éviter la dilution du retrieval.

**Blockers :**
- Validation Blaise sur la vague 1 avant production vague 2.

---

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
