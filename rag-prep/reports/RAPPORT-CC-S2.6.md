# RAPPORT-CC-S2.6 — Vague 6 (PR-09 + PR-10 + PR-11) + golden set 81q + mesure latence p50/p90

**Émetteur :** Claude Code Hub IA Plateforme (Lot J)
**Destinataire :** Cowork Hub IA Plateforme + Blaise Cavalli (garant transverse)
**Sprint :** S2.6 (clôture définitive)
**Brief source :** `rag-prep/briefs/BRIEF-CC-S2.6.md` + sondage `RETOUR-SONDAGE-COWORK-HUB-IA-S2.6.md`
**Branche développement :** `claude/execute-s26-lot-j-rapport` (depuis `main` post-merge PR #94)
**Date :** 23 mai 2026
**Allocation D-030 :** hybride Cowork (Lots A à F.6 + G/H) + Cowork Hub IA (sondage D-026 obligatoire) + Claude Code Plateforme (Lot J) + Claude Code Desktop (Lot I eval)

---

## 1. Objectifs S2.6

Le sprint S2.6 portait trois axes, sous régime SPEC v2.0 (3 ajouts post-S2.5 : discipline hygiène merge, pattern « 3 niveaux retrieval » normé, surveillance latence vault > 300 chunks) :

1. **Production vague 6 — 3 nouveaux préalables** PR-09 (cadrer un projet IA avant de choisir un outil), PR-10 (vérifier et limiter les hallucinations IA), PR-11 (cycle de vie d'un projet IA — module pivot dense), issus de l'itération HTML v3.12. Application stricte SPEC v2.0 (pattern 3 niveaux retrieval + AP-7 contrôle scope lead + ossature ≠ transverse + chunking H2 autonome + hygiène merge).

2. **Extension golden set vague 6** (Lot H) : +9 questions (q-073 → q-081), 3 par module. Cible total ~78-81 questions.

3. **Mesure latence vault > 300 chunks** (Lot I bonus) : le vault post-vague 6 atteint un volume élevé. Pas de sprint dédié latence en S2.6, mais le Lot I devait signaler la mesure **p50/p90** sur Sonnet 4.6 et formuler une recommandation S2.7 si tendance à la hausse.

**Cible eval finale S2.6** : ≥ 70/81 sources (86 %), ≥ 73/81 concepts ≥ 50 % (90 %), latence 14-20 s/q, coût Lot I ≤ 2,00 $ Anthropic.

---

## 2. Livrables par lot

| Lot | Acteur | Commit / PR | Périmètre |
|---|---|---|---|
| **A — SPEC v2.0 + BRIEF-CC-S2.6** | Cowork | `b1608da` (PR #89) | 3 ajouts SPEC v2.0 (hygiène merge `git grep '<<<<<<<'`, pattern 3 niveaux normé N1/N2/N3, surveillance latence > 300 chunks) + brief ouverture vague 6 (11 sections, cap durci ~2,00 $). |
| **E — Sondage D-026 global vague 6** | Cowork Hub IA | `RETOUR-SONDAGE-COWORK-HUB-IA-S2.6.md` | Sondage obligatoire des 3 préalables vague 6 (cadrage canonique PR-09/PR-10/PR-11, rectifications structurelles). |
| **F.6 — Production PR-09 + PR-10 + PR-11** | Cowork | `891ffc1` (PR #93) | 3 préalables produits + refonte de la brique `vigilance-hallucinations` (4 familles canoniques d'hallucinations). Sections H2 thématiquement cohérentes, lead bridge enrichi (pattern Lot D-ter). |
| **G — Cartographie** | Cowork | `891ffc1` (PR #93) | `cartographie-rag.md` enrichie 3 nouveaux préalables + recouvrements vague 6. |
| **H — Golden set 81q** | Cowork | `891ffc1` (PR #93) | Extension 72 → 81 questions (q-073 → q-081, 3 par module vague 6). Discipline AP-6 + AP-5 respectée. |
| **I — Eval extended 81q + latence p50/p90** | Desktop | `411c0f6` (PR #94) | Rejeu complet 81 questions sur vault 26 MD / 318 chunks. **81/81 (100 %)** sur les 3 axes. Audit AP-7 PR-11 réussi. Mesure latence p50/p90. 2 alertes non bloquantes. |
| **J — RAPPORT + PR finale** | Plateforme | *(ce commit)* | Présent rapport + ouverture PR finale S2.6. |

**Pas de Lot Drer en cascade** : aucune régression détectée par le Lot I (81/81), donc la procédure normée Lot Drer SPEC v2.0 n'a pas eu à être déclenchée.

---

## 3. Métriques quantitatives

### Eval golden set 81 questions — Lot I

| Indicateur | Cible brief §2 | Mesuré Lot I | Statut |
|---|---|---|---|
| **Sources retrouvées** | ≥ 70/81 (86 %) | **81/81 (100 %)** | ✅ Largement dépassée |
| **Concepts ≥ 50 % couverts** | ≥ 73/81 (90 %) | **81/81 (100 %)** | ✅ Largement dépassée |
| **Score global** | ≥ 73/81 | **81/81 (100 %)** | ✅ |
| Concepts pleinement couverts | — | 73/81 (90 %) | informatif |
| **Non-régression S2.5** | 7/7 | **7/7** (q-002/q-030/q-036/q-038/q-051/q-052/q-056) | ✅ |
| **Vague 6 (q-073 → q-081)** | — | **9/9** (8 au rang #1, q-076 #2) | ✅ |

Premier score parfait (100 %) du projet sur un golden set complet — résultat de l'application cumulée des patterns retrieval validés S2.4/S2.5 (lead bridge enrichi, H2 autonome) dès la production vague 6.

### Latence Sonnet 4.6 sur vault 318 chunks

| Statistique | Valeur | Bande SPEC v2.0 (14-20 s) |
|---|---|---|
| **p50** | **19,0 s/q** | ✅ dans la bande |
| **p90** | **22,0 s/q** | ⚠️ au-dessus de la borne 20 s |
| max | 24 s/q | — |

Le vault a franchi **318 chunks** (> 300, hors de la bande SPEC v2.0 calibrée pour 200-300 chunks). La p50 reste dans la cible mais la p90 déborde de 2 s. Voir §4 alerte #2 et §6 recommandation SPEC v2.1.

### Coût API

| Poste | Valeur | Cap durci brief |
|---|---|---|
| **Coût Lot I (Anthropic)** | **2,0509 $** | ≤ 2,00 $ — ⚠️ dépassé +0,05 $ (+2,5 %) |
| Coût OpenAI (ingestion incrémentale) | ~0,001 $ | — |
| Coût Lot Drer | 0,00 $ (non déclenché) | budget contingent 0,40 $ non consommé |

Cause mécanique du léger dépassement : 81 questions × ~0,0253 $/question, alors que le cap était calibré pour 75-80 questions. Voir §6 recommandation 1.

### Vault et ingestion incrémentale

| Snapshot | Fichiers MD | Chunks |
|---|---|---|
| Post-S2.5 (vague 5) | 23 | 289 |
| **Post-S2.6 (vague 6)** | **26** | **318** |

Ingestion incrémentale Lot I : `new=30` (3 préalables vague 6 + sections refonte vigilance-hallucinations) + `updated=6` + `deleted=1`, total 289 → 318 chunks / 26 modules. Incrémentalité 100 % fonctionnelle.

### Suite tests cumulée

**190/190 verts** (inchangé — aucun nouveau code Python en S2.6 ; production MD côté Cowork + eval réelle Desktop).

---

## 4. Anomalies & observations

### Observation #1 — Audit AP-7 PR-11 réussi (module pivot dense)

PR-11 (cycle de vie d'un projet IA) est le module le plus dense de la vague 6 (9 étapes séquencées, 3 quality gates, ratios de court-circuit). Le risque AP-7 (lead bridge sur-élargi saturant le retrieval, identifié en S2.4 sur pr-08) était surveillé.

**Résultat : AP-7 respecté à la production.** PR-11 n'apparaît **pas** dans le top-5 des questions hors de son scope :
- q-073 (PR-09 cadrage) : top-5 = `pr-09 ×5` (pas de pollution PR-11)
- q-076 (PR-10 hallucinations) : top-5 = `vigilance-hallucinations + pr-10` (pas de pollution PR-11)

La discipline AP-7 (lead-scope restreint à la spécificité éditoriale du module) est validée empiriquement à la production sur le module le plus à risque. C'est la confirmation que la recommandation AP-7 issue de S2.4 (régression pr-08) a été correctement intégrée en amont par Cowork.

### Alerte #1 (non bloquante) — Coût 2,0509 $ > cap 2,00 $

Dépassement de +0,05 $ (+2,5 %), purement mécanique (volume 81q > 75-80q de calibration). Score parfait obtenu. **Recommandation** : recalibrer le cap durci à ~2,10 $ pour les golden sets de 80-85 questions (§6 proposition 1).

### Alerte #2 (non bloquante) — Latence p90 22,0 s > borne 20 s

Le vault à 318 chunks sort de la bande SPEC v2.0 §Performances (« 200-300 chunks »). p50 (19,0 s) reste conforme, mais p90 (22,0 s) déborde de 2 s. Pas de dégradation de score, mais signal de tendance à surveiller. **Recommandation §Performances v2.1** (§6 proposition 2).

### Observation #2 — Discipline hygiène merge SPEC v2.0 respectée

`git grep "<<<<<<<"` = vide, **aucun marqueur de conflit committé** cette fois. Rupture de la série de 3 occurrences S2.5 (PR #84/#86/#88). La discipline SPEC v2.0 (proposition 1 issue de S2.5) a produit son effet dès son premier sprint d'application — validation de l'utilité de la codification.

### Observation #3 — Premier score parfait du projet

81/81 sur les 3 axes (sources, concepts ≥ 50 %, score global). C'est le premier golden set complet à 100 %. Lecture prudente : ce résultat traduit la maturité des patterns retrieval (production vague 6 directement conforme), mais le golden set reste construit en miroir des modules — un score parfait n'élimine pas le besoin de questions adverses / hors-corpus en S2.7+ pour stress-tester le refus (« je n'ai pas de réponse documentée »).

---

## 5. Décisions structurantes prises pendant S2.6

Aucune décision **actée** Git-side (SPEC v2.0 stable). **3 patterns opérationnels validés empiriquement** pendant le sprint :

### Pattern 1 — AP-7 validé en prévention (et non en correction)

Première application d'AP-7 **en amont** de la production (vs S2.4 où il a été découvert en correction sur pr-08). PR-11 dense a été produit avec un lead-scope restreint dès l'origine → 0 pollution retrieval. Le passage d'un anti-pattern correctif à une discipline préventive est validé.

### Pattern 2 — Hygiène merge préventive efficace dès v2.0

La discipline `git grep "<<<<<<<"` pre-commit (SPEC v2.0) a éliminé les marqueurs de conflit dès son premier sprint d'application (0 occurrence vs 3 en S2.5). Pattern « codifier une discipline opérationnelle après ≥ 3 occurrences » validé.

### Pattern 3 — Patterns retrieval cumulés → score parfait à la première eval

La production vague 6 a appliqué dès l'origine les patterns validés S2.4/S2.5 (lead bridge enrichi, H2 autonome, chunking thématiquement cohérent, AP-7 lead-scope). Résultat : 9/9 sur les nouvelles questions sans aucun Lot Drer correctif. Le coût d'apprentissage retrieval des sprints précédents se capitalise — la production devient « retrieval-aware » par défaut.

---

## 6. Recommandations SPEC v2.1

À arbitrer par Cowork après merge de la PR finale S2.6 :

### Proposition 1 — Recalibrage du cap durci coût

**Contexte** : §4 alerte #1, coût 2,0509 $ pour 81q (cap 2,00 $ calibré 75-80q).

**Suggestion d'ajout à SPEC §Performances** :
> **Cap durci coût recalibré (v2.1)** : ~0,0253 $/question × N questions. Pour 80-85 questions : **cap ≤ 2,15 $**. Le cap durci sert d'alerte opérationnelle, pas de hard-stop (cap mensuel D-013 50 $ reste le seul plafond absolu).

### Proposition 2 — Extension de la bande latence vault 300-400 chunks

**Contexte** : §4 alerte #2, p90 22,0 s sur vault 318 chunks, hors bande SPEC v2.0 « 200-300 ».

**Suggestion d'ajout à SPEC §Performances** :
> **Bande latence par taille de vault (v2.1)** : 200-300 chunks → 14-20 s/q (v2.0) ; **300-400 chunks → p50 ≤ 20 s, p90 ≤ 24 s** (extension empirique S2.6 : p50 19 s / p90 22 s mesurés sur 318 chunks). Au-delà de 400 chunks, ou si la p90 dépasse 24 s : envisager **reranking**, **réduction top-k** (5 → 4), ou **cache d'embeddings query**. Sprint dédié latence si la dérive se confirme sur ≥ 2 sprints.

### Proposition 3 — Retour empirique production PR-11 (module pivot dense)

**Contexte** : §5 pattern 1, PR-11 produit avec succès retrieval malgré sa densité (9 étapes + 3 gates + ratios).

**Suggestion d'ajout à SPEC §Conception MD** :
> **Module pivot dense — pattern de production validé (S2.6)** : pour un module structurant très dense (séquence d'étapes, multiples sous-frameworks), appliquer dès l'origine : (1) une H2 autonome par sous-framework majeur, (2) un lead-scope strictement restreint au périmètre du module (AP-7 préventif), (3) un chunking thématiquement cohérent ≤ 900 tokens (tolérance R3 v1.8). Validé sur PR-11 : 3/3 questions cibles score=1, 0 pollution retrieval hors scope.

---

## 7. Pistes investigation S2.7

1. **Audit R11 wikilinks post-query** (`rag/code/backend/citation_audit.py`) — reporté depuis S2.3 Lot D. Pré-requis identifié par le brief : **5+ fichiers `outils-*.md` à produire** pour rendre R11 pertinent (le vault n'a qu'un `outils-vector-db.md` actuellement). À coupler avec la vague 7 (fiches outils).
2. **Sprint dédié latence si vault > 400 chunks projeté** : la vague 7 (architectures A1-A4 + fiches outils) portera le vault au-delà de 400 chunks. Activer la mesure p50/p90 systématique + arbitrer reranking / réduction top-k (§6 proposition 2).
3. **Questions adverses / hors-corpus dans le golden set** : le score parfait 81/81 appelle un stress-test du refus (« je n'ai pas de réponse documentée ») — ajouter 3-5 questions hors-corpus en S2.7 pour valider que le système ne hallucine pas sur les sujets non couverts.
4. **Démarrage vague 7** : architectures A1-A4 + premières fiches outils (`outils-llm`, `outils-frameworks-rag`, `outils-ide-dev-ia`, etc.). Sondage D-026 systématique maintenu.
5. **Lot I-bis / consolidation eval** : non requis en S2.6 (score parfait mesuré, pas extrapolé). Décision Blaise S2.5 « pas de Lot I-bis » confirmée pertinente.

---

## 8. Coûts cumulés S1 → S2.6

### Détail S2.6

| Phase | Acteur | Coût $ |
|---|---|---|
| Lot A — SPEC v2.0 + brief | Cowork | 0,00 |
| Lot E — Sondage D-026 | Cowork Hub IA | 0,00 |
| Lot F.6 — Production PR-09/10/11 + refonte vigilance | Cowork | 0,00 |
| Lot G — Cartographie | Cowork | 0,00 |
| Lot H — Golden set 81q | Cowork | 0,00 |
| **Lot I — Eval 81q + latence** | **Desktop** | **2,0509** Anthropic + ~0,001 OpenAI |
| Lot Drer (non déclenché) | — | 0,00 |
| Lot J — RAPPORT + PR (ce commit) | Plateforme | 0,00 |
| **Total S2.6** | — | **~2,05 $** |

### Cumul historique S1 → S2.6

| Sprint | Coût $ Anthropic |
|---|---|
| S1 (S1c.2 local) | ~0,30 |
| S1bis + S1ter + S2.1 | 0,00 |
| S2.2 | ~2,50 |
| S2.3 | ~1,02 |
| S2.4 | ~1,28 |
| S2.5 | ~2,10 |
| **S2.6** | **~2,05** |
| **Total cumulé S1 → S2.6** | **~9,25 $** |

OpenAI cumulé : ~0,008 $ (embeddings + ingest incréments).

### Budget

| Provider | Crédits initiaux | Consommé S1 → S2.6 | Restant |
|---|---|---|---|
| Anthropic | ~3,00 $ (prépayés) | ~9,25 $ | dépassement crédits prépayés |
| OpenAI | ~5,00 $ | ~0,008 $ | ~4,99 $ |

**Cap mensuel D-013 (50 $/mois Anthropic, 10 $/mois OpenAI) très largement préservé** — le cumul ~9,25 $ depuis S1 reste sous le plafond mensuel. L'alerte « crédits prépayés Anthropic » signalée depuis S2.2 reste pertinente pour le suivi de trésorerie (recharge à anticiper avant la vague 7 qui augmentera le volume eval), mais elle n'est pas bloquante au regard du cap mensuel structurel.

---

## Liste des commits S2.6 (synthèse)

| PR | Commit | Lot | Acteur |
|---|---|---|---|
| #89 | `b1608da` | A — SPEC v2.0 + BRIEF-CC-S2.6 | Cowork |
| #92 | `15177c6` | F.6 amont — préalables HTML v3.12 (PR-09/10/11) | Couple 1 |
| #93 | `891ffc1` | F.6 + G + H — production vague 6 + cartographie + golden set 81q | Cowork |
| #94 | `411c0f6` | I — eval extended 81q + latence p50/p90 | Desktop |
| *(ce commit)* | — | J — RAPPORT + PR finale | Plateforme |

**Suite tests cumulée S1 → S2.6** : 190/190 verts.

---

*Rapport produit le 23 mai 2026 par Claude Code Hub IA Plateforme (Lot J). Format conforme brief CC-S2.6 §8 (8 sections) + déposé dans `rag-prep/reports/` selon convention Cowork. Sprint S2.6 définitivement clôturé après merge de la PR finale. **Premier score parfait du projet (81/81 = 100 %)**. Les 3 propositions d'amendement SPEC v2.1 (§6) restent à arbitrer par Cowork après merge. 2 alertes non bloquantes (coût +2,5 %, latence p90 +2 s) signalées pour arbitrage S2.7.*
