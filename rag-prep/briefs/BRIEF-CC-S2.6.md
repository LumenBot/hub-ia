# BRIEF-CC-S2.6 — Production vague 6 (3 nouveaux préalables PR-09 + PR-10 + PR-11) + SPEC v2.0

**Émetteur :** Cowork Hub IA Plateforme
**Destinataire :** Claude Code Plateforme (Lot J), Claude Code Desktop (Lots Drer + I eval), Cowork Hub IA (sondage D-026 obligatoire)
**Garant transverse :** Blaise Cavalli
**Sprint :** S2.6 (post-clôture S2.5 — 72/72 score global extrapolé, vault ~250 chunks)
**Date de cadrage :** 22 mai 2026
**SPEC en vigueur :** **v2.0** (produite Cowork-side simultanément à ce brief, sync ascendante en début de sprint)
**Allocation D-030 :** hybride Cowork (Lots A à F + G/H) + Cowork Hub IA (sondage D-026 obligatoire) + Claude Code Plateforme (RAPPORT-CC-S2.6) + Claude Code Desktop (Lots Drer + I eval)

---

## 1. Décisions Blaise validées (22 mai 2026)

1. **SPEC v2.0** — 3 propositions Plateforme validées et produites Cowork-side : discipline hygiène merge (`git grep '<<<<<<<'` pre-commit obligatoire) + pattern « 3 niveaux retrieval » formalisé en procédure normée Lot Drer → N1/N2/N3 + surveillance latence vault > 300 chunks (sprint dédié de mesure).
2. **Pas de Lot I-bis post-S2.5** — extrapolation 72/72 jugée suffisante. La consolidation eval est intégrée au Lot I S2.6 (eval full 75-80q sur vault post-vague 6).
3. **Ouverture immédiate S2.6** — sprint compact ~1 semaine. Production vague 6 = 3 nouveaux préalables PR-09 + PR-10 + PR-11 (v3.12, code itération HTML mergée).
4. **Sondage D-026 obligatoire** — codifié SPEC v1.8 §Validation pour production from scratch. Modalité **sondage global unique** (3 modules, plus léger qu'en S2.5 — 1 session Cowork Hub IA ~45-60 min vs 60-90 min S2.5).

## 2. Objectifs S2.6

Trois axes structurants :

1. **Production vague 6 — 3 nouveaux préalables PR-09 + PR-10 + PR-11** (Lot F.6) : tous des préalables nouveaux issus de l'itération HTML v3.12, à intégrer au vault `rag/content/prealables/`. Application stricte SPEC v2.0 (pattern 3 niveaux retrieval + AP-7 contrôle scope lead + ossature ≠ transverse + chunking H2 autonome + hygiène merge).

   - **PR-09** « Cadrer un projet IA avant de choisir un outil » : préalable de cadrage méthodologique (distinct de DEP-01 qui est l'arbre décision technique). Sensibilité **moyenne** — sondage léger.
   - **PR-10** « Vérifier et limiter les hallucinations IA » : discipline managériale, articulation DEP-05 §8.5 + DEP-07 + vigilance-hallucinations. Sensibilité **haute** — 4 familles d'hallucinations + 4 niveaux de gravité à transposer textuellement. Sondage approfondi.
   - **PR-11** « Cycle de vie d'un projet IA » : module **pivot / carte de navigation très dense**, cross-links denses vers tous PR + DEP. Sensibilité **haute** — densité éditoriale + risque de duplication transverse à arbitrer (D-025). Sondage approfondi.

2. **Extension golden set vague 6** (Lot H) : +6-9 questions selon modules touchés (2-3 questions/module × 3 modules). Cible total **~78-81 questions** (72 + 6 à 9). Application stricte SPEC v2.0.

3. **Mesure latence vault > 300 chunks** (Lot I bonus) : le vault post-vague 6 sera à ~285 chunks (sous le seuil 300). **Pas de sprint dédié latence en S2.6**, mais le rapport Lot I doit signaler la mesure p50/p90 sur Sonnet 4.6 et formuler une recommandation pour S2.7 si tendance à la hausse.

**Cible eval finale S2.6** : ≥ 66/78 sources retrouvées (≥ 85 %), ≥ 70/78 concepts ≥ 50 % couverts (≥ 90 %), latence 14-20 s/q (cible §Performances v2.0 vault 200-300 chunks), coût total Lot I ≤ 2,00 $ Anthropic (cap durci recalibré pour 75-80q sur Sonnet 4.6).

## 3. Lots S2.6 — allocation hybride D-030

| Lot | Acteur | Périmètre | Dépendance | Effort |
|---|---|---|---|---|
| **A** | Cowork | SPEC v2.0 déjà produite + sync ascendante (commit Git par Blaise via Desktop) | — | 5 min (sync) |
| **E** | Cowork → Cowork Hub IA | **Sondage D-026 global vague 6** (1 session unique, 3 modules) — passages sensibles PR-09 cadrage / PR-10 4 familles hallucinations + 4 niveaux gravité / PR-11 module pivot + cross-links denses | A clôturé | 1h Cowork + 45-60 min Cowork Hub IA |
| **F.6** | Cowork | Production vague 6 — 3 préalables MD selon RETOUR-SONDAGE-S2.6 (PR-09 + PR-10 + PR-11). Application stricte SPEC v2.0 | E clôturé (RETOUR-SONDAGE reçu) | 4-6h Cowork éditorial |
| **G** | Cowork | Whitelist v4 (retrait 3 codes PR-09 + PR-10 + PR-11) + cartographie v3 (inventaire vague 6) + glossaire (termes nouveaux si besoin) | F.6 clôturé | 20 min |
| **H** | Cowork | Extension golden set vague 6 : +6-9 questions q-073 → q-081 selon nombre final. Application SPEC v2.0 + AP-7 strict | F.6 clôturé | 30-45 min |
| **I** | Claude Code Desktop | Eval extended ~78-81 questions sur vault post-vague 6 (vault 23 → 26 fichiers MD, ~250 → ~285 chunks). Cap durci ~2,00 $ Anthropic. **+ Mesure latence p50/p90** à intégrer au rapport eval | F.6 + H clôturés | 25-30 min |
| **J** | Claude Code Plateforme | RAPPORT-CC-S2.6 (8 sections format S2.5) + PR finale S2.6 | I clôturé | 30 min |

**Cap durci sprint S2.6** : ~2,00 $ Anthropic (Lot I uniquement — pas de Lot Drer prévu en cascade au démarrage, sauf si Lot I détecte une régression). Conforme SPEC v2.0 §Performances (75-80q ≈ 1,90-2,05 $ extrapolation linéaire S2.5).

## 4. Spécification Lot E — Sondage D-026 global vague 6

**Format** : 1 fichier `briefs/DRAFT-SONDAGE-COWORK-HUB-IA-S2.6-VAGUE-6.md` (~1500-2200 mots, ~9-15 sous-passages sensibles répartis sur 3 modules).

### 4.1 Périmètre des 3 modules vague 6

| Module | Titre métier | Angle attendu | Sensibilité | Volume sondage |
|---|---|---|---|---|
| **PR-09** | Cadrer un projet IA avant de choisir un outil | Méthodologie de cadrage amont, **distincte de DEP-01** (arbre décision technique). Cadrage stratégique vs cadrage technique. | Moyenne | 3-4 sous-passages |
| **PR-10** | Vérifier et limiter les hallucinations IA | Discipline managériale. **4 familles d'hallucinations** + **4 niveaux de gravité** + articulation avec DEP-05 §8.5 (failure receipt) + DEP-07 (evaluation) + brique transverse `vigilance-hallucinations.md` existante (D-025) | **Haute** | 4-6 sous-passages |
| **PR-11** | Cycle de vie d'un projet IA | **Module pivot / carte de navigation très dense**. Cross-links denses vers tous PR (PR-01 → PR-10) + DEP (DEP-01 → DEP-08). Risque duplication transverse à arbitrer. | **Haute** | 4-6 sous-passages |

### 4.2 Questions de cadrage prioritaires pour Cowork Hub IA

Le sondage doit cibler en priorité :

- **PR-09** : différenciation explicite avec DEP-01 (PR-09 = amont stratégique, DEP-01 = aval technique) ; risque de chevauchement avec PR-07 (Build vs Buy) côté arbitrage outils ; chiffres canoniques du cadrage si présents
- **PR-10** : noms exacts des 4 familles d'hallucinations + 4 niveaux de gravité (à transposer textuellement, R10 stricte) ; cas-écoles nommés s'ils existent (avocat ChatGPT, Air Canada, etc.) ; lien avec `vigilance-hallucinations.md` brique transverse (mise à jour ou enrichissement nécessaire ?)
- **PR-11** : **risque de duplication massive** avec les autres PR et DEP — Cowork Hub IA doit indiquer ex-ante quels passages PR-11 sont **propres au module pivot** vs quels passages sont **synthèses récapitulatives** des autres modules (à wikilinker plutôt qu'à transposer) ; cas-écoles transverses (si présents) ; structure attendue du cycle de vie (combien d'étapes, lesquelles, nommage exact)

### 4.3 Volume cible RETOUR

~1500-2200 mots, structuré par module + arbitrages cross-modules signalés. Charge cognitive estimée 45-60 min Cowork Hub IA (volume moindre qu'en S2.5 du fait du nombre réduit de modules — 3 vs 8).

### 4.4 Sortie attendue (rectifications structurelles)

Le RETOUR doit lister explicitement pour chaque module :
- Hypothèses confirmées ✅
- Hypothèses nuancées avec citation textuelle de la formulation HTML
- Rectifications structurelles ⚠️ (typiquement 1-3 par sprint sur 3 modules)
- Recommandations d'extraction transverse (ex. si une famille d'hallucinations PR-10 doit basculer en brique `vigilance-hallucinations.md` plutôt que rester dans le module)
- Décisions cross-modules (notamment cycle de vie PR-11 : quels passages propres vs synthèses à wikilinker)

## 5. Spécification Lot F.6 — Production 3 préalables vague 6

Application stricte SPEC v2.0 sur chaque module :

- **Frontmatter conforme R1** (10 champs)
- **Sections H2 thématiquement cohérentes**, lead bridge enrichi avec vocabulaire question canonique attendu (pattern Lot D-ter validé S2.4.1)
- **AP-7 strict** : lead reste dans le scope strict du module, pas de vocabulaire générique qui matcherait questions hors scope
- **Chunking H2 autonome** (cible 400-700 tokens, tolérance 800-900 si cohérent)
- **Wikilinks Obsidian préférés**, briques transverses référencées (chiffres-macro-2026, pattern-llm-wiki, pattern-persistent-memory, vigilance-*)
- **Frontmatter `derives` enrichi systématiquement** avec modules touchés
- **Sources institutionnelles citées textuellement** (R6)
- **R10 stricte** sur transposition fidèle des valeurs numériques (familles + niveaux hallucinations PR-10, étapes cycle de vie PR-11)
- **Discipline particulière PR-11** (module pivot) : éviter la duplication massive — privilégier les wikilinks vers les modules amont/aval plutôt que la retranscription. Critère de test : si on retire PR-11, est-ce qu'on perd quelque chose qu'on n'a pas ailleurs ? Si non → enrichir PR-11 d'un angle propre. Si oui → conserver le passage.

Bump versions : tous les nouveaux modules à **v3.12.0** (cohérence avec l'itération HTML v3.12 d'origine).

### 5.1 Points de vigilance par module

**PR-09** :
- Différenciation explicite avec DEP-01 dans le lead (« cadrage **stratégique amont** » vs « arbre décision **technique** »)
- Éviter le piège AP-7 « projet IA » trop générique — ancrer dès la première phrase sur « avant le choix d'outil »
- Section H2 dédiée « Cadrage stratégique vs cadrage technique » pour articuler avec DEP-01

**PR-10** :
- Section H2 dédiée par famille d'hallucinations + section dédiée par niveau de gravité (4+4 = 8 sections H2 si nécessaire, ou refactoring en H2 « familles » + H2 « niveaux » avec H3 internes)
- Wikilinks systématiques vers DEP-05 §8.5 (failure receipt) + DEP-07 (evaluation) + `vigilance-hallucinations.md` (brique transverse existante)
- Si une famille d'hallucinations est déjà documentée dans `vigilance-hallucinations.md`, **wikilinker** plutôt que dupliquer (D-025 strict)

**PR-11** :
- **Découpage des étapes du cycle de vie** en H2 dédiées (autonomie sémantique de chaque étape)
- Lead bridge enrichi avec vocabulaire « **cycle de vie projet IA** » + verbes d'action canoniques attendus
- Cross-links wikilinks denses (1 par paragraphe pertinent) vers les modules concernés
- **Audit AP-7 obligatoire** post-production : lister 5 questions hors scope (PR-09, PR-10, DEP-01, DEP-07, CU-020) que PR-11 ne doit pas dominer en top-5

## 6. Spécification Lot H — Extension golden set vague 6

**+6-9 nouvelles questions** (2-3 questions/module × 3 modules = 6-9 questions). Cible total **~78-81 questions** (72 + 6 à 9).

Application SPEC v2.0 stricte :
- **AP-5** (valeurs numériques quotées dans `expected_concepts`)
- **AP-6** (plafond 4 synonymes par concept)
- **AP-7 strict** sur la conception des questions : éviter les formulations trop génériques qui pourraient saturer le retrieval par d'autres modules (les questions doivent être ancrées sur le scope strict du module cible)
- **Pattern Lot D-ter** : vocabulaire bridge des questions doit matcher le lead bridge des chunks cibles produits en Lot F.6
- **Format `expected_concepts` tolérant** pour les concepts détaillés (familles d'hallucinations PR-10, étapes cycle de vie PR-11)

### 6.1 Questions cibles prévisibles par module

**PR-09** (2-3 questions) :
- q-073 : « Comment cadrer un projet IA avant de choisir un outil ? » (cible : PR-09 méthodologie cadrage amont)
- q-074 : « Quelle différence entre cadrer un projet IA et arbitrer build vs buy ? » (cible : différenciation PR-09 / PR-07 / DEP-01)
- q-075 (optionnelle) : « Faut-il d'abord identifier le besoin métier ou choisir l'outil ? » (cible : PR-09 inversion d'approche)

**PR-10** (3 questions) :
- q-076 : « Quelles sont les 4 familles d'hallucinations IA et comment les gérer ? » (cible : PR-10 typologie hallucinations)
- q-077 : « Quels sont les 4 niveaux de gravité d'une hallucination IA ? » (cible : PR-10 grille gravité)
- q-078 : « Quelles disciplines managériales pour limiter les hallucinations IA en production ? » (cible : PR-10 + DEP-05 + DEP-07 articulation)

**PR-11** (2-3 questions) :
- q-079 : « Quelles sont les étapes du cycle de vie d'un projet IA ? » (cible : PR-11 carte de navigation)
- q-080 : « Comment articule-t-on cadrage, déploiement et évaluation dans un projet IA ? » (cible : PR-11 articulation transverse)
- q-081 (optionnelle) : « Quel ordre d'enchaînement entre les préalables et les fiches déploiement ? » (cible : PR-11 module pivot)

## 7. Spécification Lot I — Eval extended ~78-81 questions + mesure latence

**Cibles brief §2** :
- **Sources retrouvées** : ≥ 66/78 (≥ 85 %)
- **Concepts ≥ 50 % couverts** : ≥ 70/78 (≥ 90 %)
- **Score global** : ≥ 70/78
- **Latence** : 14-20 s/q (cible SPEC v2.0 §Performances vault 200-300 chunks)
- **Coût** : ≤ 2,00 $ Anthropic (cap durci sprint S2.6 recalibré pour 75-80q)
- **Non-régression S2.5** : 72/72 score maintenu, q-002 + q-030 + q-038 + q-051 + q-052 + q-036 + q-056 score=1 confirmés

**Procédure attendue Desktop** :

1. Pull main + merge dans branche dédiée (`s2.6-eval-vague-6`)
2. **Discipline hygiène merge SPEC v2.0** : si `git stash pop` exécuté, vérifier `git grep '<<<<<<<'` retourne vide avant `git add`
3. Re-ingestion incrémentale ChromaDB (3 nouveaux modules + 0 patch initial — uniquement nouveaux fichiers)
4. **Eval complet** : `python -m rag.code.eval.run_eval --questions rag/eval/questions.yaml --report rag/eval/eval-report-s2.6.md --json rag/eval/eval-report-s2.6.json`
5. **Mesure latence p50/p90** : extraire depuis `eval-report-s2.6.json` et reporter dans le rapport. Inscrire dans `RAPPORT-CC-S2.6.md` §3 Métriques.
6. Commit + push artefacts + MAJ JOURNAL + STATUS
7. Reporting : score détaillé + observations retrieval sur les 6-9 nouvelles questions + confirmation non-régression S2.5 + **recommandation §Performances v2.1** si latence dérive

### 7.1 Procédure normée Lot Drer S2.6 (codifiée SPEC v2.0)

Si le Lot I détecte une régression (≥ 1 question S2.5 passée à score=0), **NE PAS** réécrire directement les modules dominés. Appliquer la procédure normée SPEC v2.0 §Conception MD :

1. **Diagnostic Lot Drer** ciblé sur les questions régressives + 2 questions de contrôle (~0,10-0,20 $ Anthropic, ~15 min Desktop)
2. Identifier le niveau d'intervention requis (N1/N2/N3) selon rang + saturation détectée
3. Appliquer le niveau N (lead bridge enrichi / H2 dédiée concurrente / densification chirurgicale)
4. Re-Lot Drer post-patch pour valider (~0,10-0,20 $ Anthropic supplémentaires)

**Budget contingent Lot Drer S2.6** : 0,40 $ Anthropic (2 cycles diagnostic + validation max). Documenté ex-ante en cas de cascade.

## 8. Spécification Lot J — RAPPORT-CC-S2.6 + PR finale

Structure 8 sections format S2.5 :

1. **Objectifs S2.6** (3 axes : vague 6 + golden set + mesure latence)
2. **Livrables par lot** (A → J avec acteurs + commits)
3. **Métriques quantitatives** (eval, latence p50/p90, coût, vault 23 → 26 fichiers MD, chunks ~250 → ~285)
4. **Anomalies & observations** (effets de bord vague 6 si détectés, notamment PR-11 module pivot)
5. **Décisions structurantes prises pendant S2.6**
6. **Recommandations SPEC v2.1** (si propositions émergent — typiquement issue mesure latence + retour empirique production PR-11 dense)
7. **Pistes investigation S2.7** : audit R11 wikilinks (5+ fichiers `outils-*.md` à produire pour activer R11), sprint dédié latence si vault > 300 chunks projeté, démarrage vague 7 (architectures A1-A4 + fiches outils)
8. **Coûts cumulés** (S1 → S2.6, alerte budgétaire si pertinent — estimation ~9,50 $ cumulé)

## 9. Points de discipline post-S2.5 à honorer

- **Discipline hygiène merge SPEC v2.0** : `git grep '<<<<<<<'` obligatoire post-stash pop pour tous les acteurs (Cowork, Desktop, Plateforme)
- **AP-7 vigilance lead PR-11** : audit visuel approfondi du lead PR-11 (module pivot très dense, risque maximal de saturation top-5 du fait des cross-links et du vocabulaire transverse)
- **Sondage D-026 obligatoire** : codifié SPEC v1.8 §Validation pour from scratch. 3 modules vague 6 = production from scratch → sondage obligatoire
- **Eval réelle pré-clôture** : Lot I obligatoire avant ouverture PR Lot J (SPEC v1.5 §Validation)
- **D-022 exception ciblée éditoriale** : maintenue pour patches sur chiffres-macro et leads (cas-école précédents I-D-005 + Lot D-ter validés)
- **Allocation D-030 hybride** : maintenir le pattern Cowork (MD + golden set + SPEC) → Plateforme (RAPPORT + PR) → Desktop (eval)
- **Procédure normée Lot Drer + N1/N2/N3 SPEC v2.0** : appliquer en cascade si régression détectée par Lot I (anti-pattern « sauter au Niveau 3 sans diagnostic »)

## 10. Synthèse opérationnelle

**Démarrage immédiat (sans dépendance)** :
- **Lot A — Sync SPEC v2.0** (5 min — Blaise via Desktop)
- **Lot E — Sondage D-026 global vague 6** (1h Cowork rédaction sondage + envoi Cowork Hub IA)

**Après RETOUR-SONDAGE-S2.6 reçu** :
- **Lot F.6 — Production vague 6** (4-6h Cowork éditorial, 3 préalables from scratch)
- **Lots G + H** — whitelist + cartographie v3 + golden set extended (~1h Cowork)

**Après Lot F.6 + Lot H mergés** :
- **Lot I — Eval extended ~78-81q + mesure latence** (~25 min Desktop, ~2,00 $ Anthropic)
- **Lot Drer éventuel** si régression détectée (~15 min + 0,20-0,40 $ Anthropic en cascade)

**Clôture sprint** :
- **Lot J — RAPPORT-CC-S2.6 + PR finale** (30 min Plateforme)

**Effort total estimé** : ~8-12h cumulé sur ~5-7 jours selon disponibilité Cowork Hub IA pour le sondage.

## 11. Vault post-vague 6 — projection

| Avant S2.6 (post-clôture S2.5) | Après S2.6 (cible) | Delta |
|---|---|---|
| 23 fichiers MD (15 modules + 8 transverses/glossaire) | 26 fichiers MD (18 modules + 8 transverses/glossaire) | +3 fichiers |
| ~250 chunks ChromaDB | ~285 chunks ChromaDB | +35 chunks |
| 72 questions golden set | 78-81 questions golden set | +6-9 questions |
| 72/72 score extrapolé | ≥ 70/78 score cible | Maintien qualité retrieval |

**Seuil de surveillance §Performances v2.0** : 285 chunks sous le seuil 300. **Pas de sprint dédié latence en S2.6**, mais Lot I doit signaler p50/p90 et formuler recommandation pour S2.7 si tendance à la hausse (extrapolation des 35 chunks supplémentaires).

---

*Brief produit le 22 mai 2026 par Cowork Hub IA Plateforme post-clôture S2.5. SPEC v2.0 en vigueur (produite Cowork-side simultanément). À transmettre par Blaise via sync ascendante après revue.*
