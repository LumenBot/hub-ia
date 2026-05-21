# BRIEF-CC-S2.5 — Production vague 5 (8 modules whitelistés) + correctif retrieval pr-08 + SPEC v1.8

**Émetteur :** Cowork Hub IA Plateforme
**Destinataire :** Claude Code Plateforme (Lots code/tests), Claude Code Desktop (Lots eval), Cowork Hub IA (co-production sondage parallèle)
**Garant transverse :** Blaise Cavalli
**Sprint :** S2.5 (post-clôture S2.4 — 50/52 atteint sur golden set, PR #70 + PR Lot J mergées)
**Date de cadrage :** 20 mai 2026
**SPEC en vigueur :** v1.6, **bump v1.8 prévu Lot A** (AP-7 + tolérance 800-900 tokens + sondage D-026 systématique)
**Allocation D-030 :** hybride Cowork (Lots A à F + G/H) + Cowork Hub IA en parallèle (sondage) + Claude Code Plateforme (RAPPORT-CC-S2.5) + Claude Code Desktop (Lots Drer + I eval)

---

## 1. Décisions Blaise validées (20 mai 2026)

1. **SPEC v1.8** — 3 propositions Plateforme validées : AP-7 lead bridge sur-élargi + tolérance seuil 800-900 tokens + codification sondage D-026 systématique pour modules from scratch
2. **Budget Anthropic** — recharge crédits (top-up effectué par Blaise) → garde Sonnet 4.6 sur eval complète, cap durci sprint S2.5 estimé ~1,75 $ Anthropic
3. **Sondage D-026** — **1 sondage global** sur les 8 modules vague 5 (efficacité Cowork Hub IA, ~60-90 min session unique)
4. **Lot S2.5.0** (correctif retrieval pr-08) — **en tout début S2.5**, avant Lot F.5, pour éviter contamination des nouveaux modules

## 2. Objectifs S2.5

Quatre axes structurants :

1. **Correctif retrieval pr-08 saturation** (Lot S2.5.0) — restreindre lead pr-08 au scope strict financement + enrichir leads cu-001 (sources fiables actualité IA) et pr-07 (build vs buy obligations réglementaires) avec leur vocabulaire question canonique. Application AP-7 inverse Lot D-ter. Cible : q-002 et q-030 reviennent à score=1 sans régression sur q-051 et q-052.

2. **Production SPEC v1.8** (Lot A) — 3 ajouts validés : AP-7 « Lead bridge sur-élargi » + précision seuil R3 (tolérance 800-900 tokens si chunk cohérent) + nouvelle règle « production from scratch avec sondage D-026 systématique ».

3. **Production vague 5 — 8 modules whitelistés** (Lot F.5) post-RETOUR-SONDAGE-S2.5 : CU-020 (Conformité RGPD/AI Act) + CU-024 (Order-to-cash automation) + DEP-01 (Cadrer projet IA) + DEP-05 (Agents production observabilité) + DEP-07 (Évaluation continue) + PR-01 (Maturité organisationnelle) + PR-04 (Marché IA & emploi) + PR-05 (Sécurité IA). Application stricte SPEC v1.8 (pattern Lot D-ter + AP-7 contrôle scope lead + ossature ≠ transverse + chunking H2 autonome).

4. **Extension golden set vague 5** (Lot H) : +20-24 questions selon modules touchés (2-3 questions/module × 8 modules). Cible total **~72-76 questions**. Application stricte SPEC v1.8.

**Cible eval finale S2.5** : ≥ 60/72 sources retrouvées (≥ 83 %), ≥ 65/72 concepts ≥ 50 % couverts (≥ 90 %), latence 12-18 s/q, coût total Lot I ≤ 1,80 $ Anthropic (cap durci recalibré pour 70-80q sur Sonnet 4.6).

## 3. Lots S2.5 — allocation hybride D-030

| Lot | Acteur | Périmètre | Dépendance | Effort |
|---|---|---|---|---|
| **A** | Cowork | Production SPEC v1.8 (3 ajouts validés) Cowork-side + sync ascendante | — | 30 min |
| **S2.5.0** | Cowork | Correctif retrieval pr-08 (restriction lead) + enrichissement leads cu-001 + pr-07 (pattern Lot D-ter) | — | 30-45 min |
| **Drer** | Claude Code Desktop | Rerun eval ciblé q-002 + q-030 + q-051 + q-052 (4 questions, ~0,12 $) post-merge S2.5.0 | S2.5.0 mergé | 15-20 min |
| **E** | Cowork → Cowork Hub IA | **Sondage D-026 global** sur 8 modules vague 5 (1 session unique) — passages sensibles à risque dérive sémantique par module | A clôturé | 1h Cowork + 60-90 min Cowork Hub IA |
| **F.5** | Cowork | Production vague 5 — 8 modules MD selon RETOUR-SONDAGE-S2.5 (CU-020 + CU-024 + DEP-01 + DEP-05 + DEP-07 + PR-01 + PR-04 + PR-05). Application stricte SPEC v1.8. | E clôturé (RETOUR-SONDAGE reçu) | 10-15h Cowork éditorial |
| **G** | Cowork | Whitelist v3 (retrait 8 codes) + cartographie v2 (inventaire vague 5) + glossaire (termes nouveaux si besoin) | F.5 clôturé | 30 min |
| **H** | Cowork | Extension golden set vague 5 : +20-24 questions q-053 → q-072/q-076 selon nombre final. Application SPEC v1.8 + AP-7 strict | F.5 clôturé | 1h-1h30 |
| **I** | Claude Code Desktop | Eval extended ~72-76 questions sur vault post-vague 5 (vault 15 → 23 fichiers MD). Cap durci ~1,80 $ Anthropic | F.5 + H clôturés | 25-30 min |
| **J** | Claude Code Plateforme | RAPPORT-CC-S2.5 (8 sections format S2.4) + PR finale S2.5 | I clôturé | 30 min |

**Cap durci sprint S2.5** : ~1,95 $ Anthropic (Lot Drer ~0,12 $ + Lot I ~1,80 $). Conforme SPEC v1.8 §Performances (60-80q ≈ 1,80 $).

## 4. Spécification Lot A — SPEC v1.8 (3 ajouts validés)

### 4.1 AP-7 — Lead bridge sur-élargi (symétrique inverse SPEC v1.6 §Conception MD)

**À ajouter à §Anti-patterns** :

> **AP-7 — Lead bridge sur-élargi** (issue RAPPORT-CC-S2.4 §6 P1, validé empiriquement par régressions q-002 + q-030 S2.4 Lot I) : un lead de chunk H2 ne doit pas étendre son vocabulaire bridge au-delà du **scope strict du module**. Sinon, ce chunk peut saturer le top-5 retrieval sur des questions transversales et étouffer d'autres modules plus pertinents.
>
> *Cas-école* : pr-08 lead « **outils et patterns de financement projet IA en 2026 pour PME**… » → saturation top-5 sur q-002 (cu-001 sources fiables actualité IA) et q-030 (pr-07 obligations réglementaires projet IA PME), car les termes « projet IA », « 2026 », « PME » sont trop génériques.
>
> *Discipline* : le lead doit contenir le vocabulaire bridge **du scope effectif du module**, pas un vocabulaire générique qui matcherait des questions hors scope. Audit visuel à chaque production module : lister les 3-5 questions hors scope que le module ne doit PAS dominer en top-5 ; reformuler le lead s'il les domine.

### 4.2 Tolérance seuil 800-900 tokens SPEC §R3

**À ajouter à §R3 Chunking** :

> **Précision empirique post-S2.4** (validé sur chunk Frontier Firms cu-026, 850 tokens, score eval 100 % sans subdivision) : le seuil de subdivision H3 à 800 tokens est une **recommandation**, avec **tolérance jusqu'à ~900 tokens** si le chunk est thématiquement cohérent (un seul angle traité, pas d'enchaînement de sous-sujets distincts). Au-delà de 900 tokens : refactoring H3 obligatoire pour préserver la qualité du retrieval.

### 4.3 Codification production from scratch avec sondage D-026 systématique

**À ajouter à §Validation (nouvelle sous-section)** :

> **Sondage D-026 systématique pour production from scratch** (validé empiriquement S2.3 + S2.4, 2 sprints consécutifs avec 4 dérives sémantiques évitées en S2.3 et 1 rectification critique en S2.4) : tout module produit **from scratch** (sans précédent MD dans le vault) doit faire l'objet d'un **sondage préalable D-026** au canal détenteur de la source canonique HTML. Le sondage cible les passages denses : chiffres exacts, énumérations canoniques, cas-écoles nommés, frameworks structurants.
>
> *Format* : draft Cowork-side `briefs/DRAFT-SONDAGE-COWORK-HUB-IA-S{N}-{slug}.md` listant 3-15 sous-passages sensibles avec hypothèses Cowork → retour Cowork Hub IA dans `briefs/RETOUR-SONDAGE-COWORK-HUB-IA-S{N}.md` (~1500-3000 mots) → production MD post-RETOUR avec rectifications intégrées.
>
> *Effort estimé* : 1h Cowork (rédaction sondage) + 60-90 min Cowork Hub IA (retour) + intégration au moment de la production = ~2h de surcoût par module/groupe de modules vs production directe. **Gain attendu** : 1-4 dérives sémantiques majeures évitées par module dense.

### 4.4 Bump historique

```markdown
| v1.8 | 20 mai 2026 | Intégration des 3 propositions RAPPORT-CC-S2.4 §6 (validation Cowork post-clôture S2.4) : (1) AP-7 « Lead bridge sur-élargi » (anti-pattern, symétrique inverse garde-fou concepts détaillés v1.6) ; (2) Tolérance seuil R3 à 800-900 tokens si chunk thématiquement cohérent (validé empiriquement Frontier Firms cu-026 850 tokens) ; (3) Codification production from scratch avec sondage D-026 systématique (validé empiriquement S2.3 + S2.4). |
```

## 5. Spécification Lot S2.5.0 — Correctif retrieval pr-08

### 5.1 Cible

q-002 (sources fiables actualité IA 2026) score=1 + q-030 (obligations réglementaires projet IA PME 2026) score=1, **sans régression** sur q-051 (7 dispositifs fiscaux pr-08) ni q-052 (règle 5 étapes pr-08).

### 5.2 Patch pr-08 — Restriction lead H2 ouverture

Le lead actuel de la section H2 « L'essentiel à retenir » de pr-08 contient « financer un projet IA en PME — à condition de connaître la carte » trop générique. Restreindre au scope strict financement avec vocabulaire bridge **dispositifs fiscaux** et **financements publics**.

Diff proposé : ajouter explicitement le mot « financement » et les termes spécifiques (CIR, CII, Bpifrance, France 2030) dès la première phrase pour ancrer le scope.

### 5.3 Patch cu-001 — Enrichissement lead H2 ouverture

Application AP-Lot-D-ter : le lead de la H2 « L'essentiel à retenir » ou « À qui ce module s'adresse » doit inclure le vocabulaire bridge des questions canoniques q-002 type (« sources fiables actualité IA », « veille IA générative », « 2026 »).

### 5.4 Patch pr-07 — Enrichissement lead H2 ouverture

Idem cu-001 mais pour les questions q-030 type (« obligations réglementaires projet IA », « PME 2026 », « build vs buy »).

### 5.5 Bump versions

cu-001 v3.X → v3.11.1 (patch correctif retrieval), pr-07 v3.X → v3.11.1, pr-08 v3.11.0 → v3.11.1.

## 6. Spécification Lot E — Sondage D-026 global vague 5

Format : 1 fichier `briefs/DRAFT-SONDAGE-COWORK-HUB-IA-S2.5-VAGUE-5.md` (~2500-3500 mots, ~15-25 sous-passages sensibles répartis sur 8 modules).

### 6.1 Périmètre des 8 modules vague 5

| Module | Titre métier | Angle attendu | Sensibilité |
|---|---|---|---|
| **CU-020** | Conformité RGPD / AI Act pour l'IA en PME | Cadre réglementaire EU 2026, AI Act articles, dates d'effet, CNIL, sanctions | **Haute** (chiffres + dates + cas-école condamnation) |
| **CU-024** | Order-to-cash automation IA | Workflow ventes-encaissement, agents par étape, cas-école PME | Moyenne (RetEx + chiffres ROI) |
| **DEP-01** | Cadrer un projet IA pour la mise en production | Heuristique anti-hype 6 étapes, arbre de décision, Jagged Frontier Stanford | **Haute** (concept Jagged Frontier + cas-école IMO/horloge) |
| **DEP-05** | Agents en production : observabilité et garde-fous | §8.5 failure receipt + §8.5bis Effective Harnesses long-running, outils observabilité | **Haute** (sujet technique pointu) |
| **DEP-07** | Évaluation continue et qualité IA | Anthropic Demystifying Evals + golden sets, métriques, LLM-as-judge | Moyenne (techniques d'éval) |
| **PR-01** | Maturité organisationnelle | Typologie 4 profils dirigeants Bpifrance + high performers McKinsey | **Haute** (typologie 4 profils + chiffres 6 % / 3,6× / 3×) |
| **PR-04** | Marché IA & emploi | Triple marché 2026 (Bpifrance + Microsoft + Transformation Paradox) | **Haute** (3 séries chiffres adjacents à ne pas confondre) |
| **PR-05** | Sécurité IA | Cybersécurité agentique McKinsey + NIST CAISI + 362 incidents Stanford symétrie | Moyenne (recouvrement DEP-08) |

### 6.2 Questions de cadrage pour Cowork Hub IA

Le sondage doit cibler en priorité :
- Les **chiffres canoniques** non encore canonisés dans `chiffres-macro-2026.md` v3.9.0
- Les **frameworks structurants** (heuristique anti-hype 6 étapes DEP-01, typologie 4 profils PR-01, etc.)
- Les **cas-écoles** non triviaux (différences avec ceux déjà documentés CU-026/CU-027/DEP-08)
- Les **risques de duplication** entre modules (DEP-08 sécurité technique vs PR-05 sécurité orga, DEP-05 observabilité vs CU-026 gouvernance, etc.)

### 6.3 Volume cible RETOUR

~2500-3500 mots, structuré par module + bonus signalés. Charge cognitive estimée 60-90 min Cowork Hub IA.

## 7. Spécification Lot F.5 — Production 8 modules vague 5

Application stricte SPEC v1.8 sur chaque module :
- Frontmatter conforme SPEC §R1 (10 champs)
- Sections H2 thématiquement cohérentes, lead bridge enrichi avec vocabulaire question canonique attendu (pattern Lot D-ter)
- **AP-7 strict** : lead reste dans le scope strict du module, pas de vocabulaire générique qui matcherait questions hors scope
- Chunking H2 autonome (cible 400-700 tokens, tolérance 800-900 si cohérent)
- Wikilinks Obsidian préférés, briques transverses référencées (chiffres-macro-2026, pattern-llm-wiki, pattern-persistent-memory, vigilance-*)
- Frontmatter `derives` enrichi systématiquement avec modules touchés
- Sources institutionnelles citées textuellement (R6)

Bump versions : tous les nouveaux modules à v3.11.0.

## 8. Spécification Lot H — Extension golden set vague 5

**+20-24 nouvelles questions** (2-3 questions/module × 8 modules = 16-24 questions). Cible total **~72-76 questions** (52 + 20 à 24).

Application SPEC v1.8 stricte :
- AP-5 (valeurs numériques quotées)
- AP-6 (plafond 4 synonymes par concept)
- **AP-7 strict** sur la conception des questions : éviter les formulations trop génériques qui pourraient saturer le retrieval par d'autres modules (les questions doivent être ancrées sur le scope strict du module cible)
- Application AP-Lot-D-ter : vocabulaire bridge des questions doit matcher le lead bridge des chunks cibles produits en Lot F.5

## 9. Spécification Lot I — Eval extended ~72-76 questions

**Cibles brief §2** :
- Sources retrouvées : ≥ 60/72 (≥ 83 %)
- Concepts ≥ 50 % couverts : ≥ 65/72 (≥ 90 %)
- Score global : ≥ 60/72
- Latence : 12-18 s/q (cible SPEC v1.6 §Performances)
- Coût : ≤ 1,80 $ Anthropic (cap durci sprint S2.5 recalibré pour 70-80q)
- Non-régression S2.4 : q-038 score=1 maintenu + q-002 + q-030 score=1 confirmés post-Lot S2.5.0

Procédure attendue Desktop :
1. Pull main + merge dans branche dédiée
2. Re-ingestion incrémentale ChromaDB (8 nouveaux modules + 3 patches pr-08/cu-001/pr-07)
3. Eval complet : `python -m rag.code.eval.run_eval --questions rag/eval/questions.yaml --report rag/eval/eval-report-s2.5.md --json rag/eval/eval-report-s2.5.json`
4. Commit + push artefacts + MAJ JOURNAL + STATUS
5. Reporting : score détaillé + observations retrieval sur les 20-24 nouvelles questions + confirmation non-régression q-002 / q-030 / q-038 / q-051 / q-052

## 10. Spécification Lot J — RAPPORT-CC-S2.5 + PR finale

Structure 8 sections format S2.4 :
1. Objectifs S2.5 (4 axes)
2. Livrables par lot (A → J avec acteurs + commits)
3. Métriques quantitatives (eval, latence, coût, vault 15 → 23 fichiers MD, chunks ~155 → ~250)
4. Anomalies & observations (effets de bord vague 5 si détectés)
5. Décisions structurantes prises pendant S2.5
6. Recommandations SPEC v1.9 (si propositions émergent)
7. Pistes investigation S2.6 (R11 audit wikilinks, audit latence vault > 200 chunks, modules CU-028/CU-029)
8. Coûts cumulés (S1 → S2.5, alerte budgétaire si pertinent)

## 11. Points de discipline post-S2.4 à honorer

- **AP-7 vigilance lead** : à chaque production module en Lot F.5, audit visuel du lead pour vérifier qu'il reste dans le scope strict (lister 3-5 questions hors scope que le module ne doit PAS dominer en top-5 ; reformuler si dérive).
- **Sondage D-026 systématique pour from scratch** : codifié en SPEC v1.8 §Validation. Toute production from scratch passe par RETOUR-SONDAGE.
- **Eval réelle pré-clôture** : Lot I obligatoire avant ouverture PR Lot J (SPEC v1.5 §Validation).
- **D-022 exception ciblée éditoriale** : maintenue pour patches sur chiffres-macro et leads (cas-école précédents I-D-005 + Lot D-ter validés).
- **Allocation D-030 hybride** : maintenir le pattern Cowork (MD + golden set + SPEC) → Plateforme (RAPPORT + PR) → Desktop (eval).

## 12. Synthèse opérationnelle

**Démarrage immédiat (sans dépendance)** :
- **Lot A — SPEC v1.8** (30 min Cowork)
- **Lot S2.5.0 — Correctif retrieval pr-08** (30-45 min Cowork éditorial direct)
- **Lot E — Sondage D-026 global** (1h Cowork rédaction sondage)

**Après commit S2.5.0 + sync ascendante** :
- **Lot Drer** Desktop : rerun ciblé 4 questions (~0,12 $)

**Après RETOUR-SONDAGE-S2.5 reçu** :
- **Lot F.5 — Production vague 5** (10-15h Cowork éditorial, 8 modules from scratch)
- **Lots G + H** — whitelist + cartographie v2 + golden set extended (~2h Cowork)

**Après Lot F.5 + Lot H mergés** :
- **Lot I — Eval extended ~72-76q** (~25 min Desktop, ~1,80 $ Anthropic)

**Clôture sprint** :
- **Lot J — RAPPORT-CC-S2.5 + PR finale** (30 min Plateforme)

**Effort total estimé** : ~16-20h cumulé sur ~7-10 jours selon disponibilité Cowork Hub IA pour le sondage.

---

*Brief produit le 20 mai 2026 par Cowork Hub IA Plateforme post-clôture S2.4. SPEC v1.6 en vigueur, bump v1.8 prévu Lot A. À transmettre par Blaise via sync ascendante après revue.*
