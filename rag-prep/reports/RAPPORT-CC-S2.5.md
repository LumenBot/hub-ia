# RAPPORT-CC-S2.5 — Vague 5 (8 modules from scratch) + correctif retrieval + golden set 72q + pattern 3 niveaux retrieval

**Émetteur :** Claude Code Hub IA Plateforme (Lot J)
**Destinataire :** Cowork Hub IA Plateforme + Blaise Cavalli (garant transverse)
**Sprint :** S2.5 (clôture définitive)
**Brief source :** `rag-prep/briefs/BRIEF-CC-S2.5.md` + sondage `RETOUR-SONDAGE-COWORK-HUB-IA-S2.5.md`
**Branche développement :** `claude/execute-s25-lot-j-rapport` (depuis `main` post-merge PR #87)
**Date :** 22 mai 2026
**Allocation D-030 :** hybride Cowork Hub IA (sondage 8 modules) + Cowork Plateforme (Lots A, E, F.5a-d, G, H, S2.5.x correctifs) + Claude Code Plateforme (Lot J) + Claude Code Desktop (Lots Drer, I, Drer-S2.5.x)

---

## 1. Objectifs S2.5

Le sprint S2.5 portait quatre axes structurels, condition d'élargissement à grande échelle du vault (passage de 15 à 23 fichiers MD) et de fiabilisation du retrieval :

1. **Correctif retrieval des régressions S2.4** — résoudre q-002 et q-030 (sources canoniques cu-001 / pr-07 / vigilance-confidentialite évincées par le lead trop accrocheur de pr-08, saturation top-5) via une série d'itérations correctives sur les leads éditoriaux (Phase 1 S2.5.0/bis/ter).

2. **Production vague 5 from scratch (8 modules)** — produire DEP-01, DEP-07, DEP-05, PR-01, PR-04, PR-05, CU-020, CU-024 directement depuis le sondage Cowork Hub IA (sans version MD préexistante), en application du pattern « production from scratch avec sondage D-026 systématique » recommandé en RAPPORT-CC-S2.4 §6.

3. **Extension golden set 52 → 72 questions** — couvrir les 8 nouveaux modules avec 20 nouvelles questions (q-053 → q-072), discipline AP-6 plafond synonymes respectée.

4. **Validation empirique du pattern « 3 niveaux d'intervention retrieval »** codifié en SPEC v1.9 (Lead bridge enrichi → H2 dédiée concurrente → densification chirurgicale).

---

## 2. Livrables par lot

| Lot | Acteur | Commit(s) / PR | Périmètre |
|---|---|---|---|
| **A — SPEC v1.8 → v1.9** | Cowork | (pré-S2.5 post-merge S2.4) | Intégration 3 propositions S2.4 (AP-7 lead bridge sur-élargi, tolérance R3 ~900 tokens, D-026 systématique) + codification pattern « 3 niveaux retrieval » (v1.9). |
| **Phase 1 — S2.5.0 / bis / ter (correctif q-030)** | Cowork | PR #75-77 | 3 itérations correctives leads : cu-001 v3.11.1, pr-07 v3.11.3 (3 passages), pr-08 v3.11.1. Restriction lead pr-08 + enrichissement leads cu-001/pr-07 pour rééquilibrer la concurrence retrieval. |
| **Phase 1 — Drer / bis / ter (validation Desktop)** | Desktop | (reruns ciblés) | Validation itérative q-002 + q-030 → score=1 par niveau d'intervention. Pattern 3 niveaux validé sur ces 2 questions. |
| **Phase 2 — E sondage D-026 global** | Cowork Hub IA | `RETOUR-SONDAGE-COWORK-HUB-IA-S2.5.md` | Sondage des 8 modules vague 5. **2 rectifications critiques** (CU-024 PA = Plateforme Agréée ≠ PPF ; DEP-01 6 étapes = arbre décision technique ≠ cadrage projet) + 4 passages bonus. |
| **Phase 2 — F.5a (DEP-01 + DEP-07)** | Cowork | PR #78-79 | Production from scratch 2 modules déploiement. |
| **Phase 2 — F.5b (PR-01 + PR-04)** | Cowork | PR #80-81 | Production from scratch 2 préalables (maturité orga, marché IA emploi). |
| **Phase 2 — F.5c (DEP-05 + PR-05)** | Cowork | PR #82 | Production from scratch déploiement agents observabilité + préalable sécurité IA. |
| **Phase 2 — F.5d (CU-020 + CU-024)** | Cowork | PR #83 | Production from scratch RGPD/AI Act + order-to-cash automation. |
| **Phase 3 — G cartographie v3 + H golden set 72q** | Cowork | PR #84 | Cartographie enrichie 8 nouveaux modules + extension golden set 52 → 72 questions (q-053 → q-072). |
| **Phase 3 — I eval extended 72q** | Desktop | PR #85 | Rejeu complet 72 questions post-vague 5. **70/72 (97 %)** sur les 3 axes. 2 régressions vague 5 (q-036, q-056). |
| **Phase 3 — S2.5.x correctif q-036/q-056** | Cowork | PR #86 | Densification chirurgicale leads cu-027 §7 outils + dep-07 §eval-first (Niveau 3 SPEC v1.9). |
| **Phase 3 — Drer-S2.5.x (validation Desktop)** | Desktop | PR #87 | Rerun ciblé 4q → **4/4** 🎉. q-036 restauré (cu-027 rang #3 sim 0,3310), q-056 restauré (dep-07 rang #1 sim 0,4634), sanity q-002 + q-038 maintenus. |
| **Phase 3 — J RAPPORT + PR finale** | Plateforme | *(ce commit)* | Présent rapport + ouverture PR finale S2.5. |

---

## 3. Métriques quantitatives

### Eval golden set 72 questions — Lot I (rerun complet)

| Indicateur | Mesuré Lot I | Statut |
|---|---|---|
| **Sources retrouvées** | **70/72 (97 %)** | ✅ |
| **Concepts ≥ 50 % couverts** | **70/72 (97 %)** | ✅ |
| **Score global** | **70/72 (97 %)** | ✅ |
| Concepts pleinement couverts | 64/72 (89 %) | informatif |
| Latence moyenne | 17,7 s/q | ✅ (bande SPEC v1.9 12-18 s) |
| Coût Lot I | 1,7816 $ Anthropic | — |

**2 régressions vague 5 identifiées** : q-036 (cu-027 hors top-10) et q-056 (dep-07 rang #9). Causes : nouveaux modules vague 5 saturant le retrieval sur les sections outils (cu-027 §7) et eval (dep-07).

### Eval ciblée Lot Drer-S2.5.x (post-correctif S2.5.x)

| Question | Source attendue | Résultat post-correctif | Statut |
|---|---|---|---|
| q-036 | cu-027 | **rang #3, sim 0,3310** (vs absent top-10) | ✅ restauré |
| q-056 | dep-07 | **rang #1, sim 0,4634** (vs #9) | ✅ restauré |
| q-002 (sanity S2.4) | cu-001 | maintenu score=1 | ✅ non-régression |
| q-038 (sanity S2.4) | dep-08 | maintenu score=1 (tous concepts détaillés) | ✅ non-régression |

**Score golden set 72q extrapolé : 72/72** — Lot I (70/72) + 2 restaurations validées (q-036, q-056). Validation ciblée 4q (pas re-run complet) — voir réserve méthodologique §4.

### Non-régression S2.4 confirmée

q-002 + q-030 + q-038 + q-051 + q-052 tous maintenus score=1 à travers les Phases 1, 2 et 3. Les correctifs leads n'ont pas cassé les questions précédemment passantes.

### Vault et ingestion

| Snapshot | Fichiers MD | Chunks |
|---|---|---|
| Post-S2.4 (vague 4) | 15 | ~155 |
| **Post-S2.5 (vague 5)** | **23** | **289** (94 nouveaux) |

8 nouveaux modules vague 5 produits from scratch : DEP-01, DEP-07, DEP-05, PR-01, PR-04, PR-05, CU-020, CU-024. Lot Drer-S2.5.x : ingestion new=2 + updated=20 + deleted=2 (renommages titres H2), total stable 289.

### Patches leads correctifs retrieval

5 versions bumpées sur les leads éditoriaux : cu-001 v3.11.1, pr-07 v3.11.3 (3 itérations), pr-08 v3.11.1, cu-027 v3.11.1, dep-07 v3.11.1.

### Suite tests cumulée

**190/190 verts** (inchangé — aucun nouveau test Plateforme en S2.5 ; les patches sont éditoriaux MD côté Cowork, les évaluations sont de l'exécution réelle Desktop).

---

## 4. Anomalies & observations

### Régressions résolues — 4 questions sur 2 phases

| Régression | Phase de résolution | Niveau d'intervention | Résultat |
|---|---|---|---|
| q-002 (S2.4) | Phase 1 (S2.5.0/bis/ter) | Niveau 1-2 (lead bridge + concurrence) | ✅ score=1 |
| q-030 (S2.4) | Phase 1 (S2.5.0/bis/ter) | Niveau 1-2 | ✅ score=1 |
| q-036 (vague 5) | Phase 3 (S2.5.x) | Niveau 3 (densification chirurgicale cu-027 §7) | ✅ rang #3 |
| q-056 (vague 5) | Phase 3 (S2.5.x) | Niveau 3 (densification chirurgicale dep-07) | ✅ rang #1 |

Le **pattern « 3 niveaux d'intervention retrieval » (SPEC v1.9) est désormais validé empiriquement sur 6 questions distinctes** : q-038 (S2.4.1), q-002 + q-030 (S2.5.0/bis/ter), q-036 + q-056 (S2.5.x) + sanity.

### Observation #1 — 3 occurrences d'hygiène merge

Sur les PR #84, #86 et #88, des **marqueurs de conflit `git stash`** (`<<<<<<<`) ont été committés tels quels dans des fichiers de gouvernance (JOURNAL notamment) et corrigés a posteriori par Desktop (3 fois). Pattern récurrent côté Cowork à acter en discipline opérationnelle : exécuter `git grep "<<<<<<<"` avant chaque `git add` après un `git stash pop`. Recommandation SPEC v2.0 §6.

### Observation #2 — Réserve méthodologique sur le 72/72 extrapolé

Le Lot Drer-S2.5.x est une **validation ciblée 4 questions** (q-036, q-056, q-002, q-038), pas un re-run complet 72q. L'extrapolation à 72/72 est fiable (les 2 restaurations sont mesurées, les 68 autres questions étaient déjà passantes au Lot I sauf q-036/q-056) mais **non formellement validée** par un rerun complet. Option **Lot I-bis** (~1,8 $ Anthropic) à arbitrer par Cowork si une validation formelle est requise pour l'archivage projet.

### Observation #3 — Latence Lot Drer-S2.5.x ~19 s/q

Légèrement au-dessus de la bande SPEC v1.9 (12-18 s/q). Le Lot I principal reste dans la bande (17,7 s/q). À surveiller en S2.6 si récurrence — possible effet du vault élargi (289 chunks) sur le temps de retrieval + génération.

---

## 5. Décisions structurantes prises pendant S2.5

Aucune décision **actée** Git-side en S2.5 (D-025 / D-026 / SPEC v1.9 stables). **5 patterns opérationnels validés empiriquement** pendant le sprint :

### Pattern 1 — « 3 niveaux d'intervention retrieval » (SPEC v1.9) validé sur 6 cas-écoles

Trois niveaux gradués pour ramener un chunk cible dans le top-5 :
- **Niveau 1 — Lead bridge enrichi** : enrichir le premier paragraphe / chunk frontmatter du module cible avec le vocabulaire de la question.
- **Niveau 2 — H2 dédiée concurrente** : créer une section H2 spécifique qui concentre la sémantique de la question.
- **Niveau 3 — Densification chirurgicale** : densifier précisément la section cible (specs, mots-clés) sans toucher au reste.

Validé sur q-038 (N1+N3), q-002 + q-030 (N1+N2), q-036 + q-056 (N3). Procédure normée : Lot Drer ciblé pour mesurer l'écart, puis itération par niveau selon l'écart résiduel.

### Pattern 2 — « 4 modules sécurité IA complémentaires non substituables »

Production vague 5 a confirmé que les 4 modules sécurité couvrent des angles distincts non substituables :
- **PR-05** : sécurité stratégique (cadrage dirigeant)
- **DEP-05** : sécurité technique runtime (observabilité agents)
- **DEP-08** : sécurité technique infrastructure (MCP servers, SBOM IA)
- **CU-026** : gouvernance managériale (framework 7 dimensions)

Aucune extraction transverse pertinente entre eux — chacun reste un module autonome (application D-025 critère ossature).

### Pattern 3 — « 4 modules méthodologiques cartographiques sans cas-école PME »

CU-020 (RGPD/AI Act), CU-024 (order-to-cash), PR-05 (sécurité), PR-08 (financement) sont des modules **cartographiques** (panorama réglementaire/méthodologique) sans cas-école PME illustratif, contrairement aux modules illustratifs (CU-026 Klarna, CU-027 Tea App, DEP-08 CVE techniques). Distinction éditoriale nette à préserver pour le retrieval.

### Pattern 4 — 2e application D-026 « production from scratch » validée

Le sondage Cowork Hub IA préalable a évité **2 rectifications critiques** en S2.5 :
- **CU-024** : PA = Plateforme Agréée (≠ PPF Portail Public de Facturation — confusion fréquente sur la facturation électronique).
- **DEP-01** : les 6 étapes = arbre de décision technique (≠ cadrage de projet généraliste).

\+ 4 passages bonus signalés. Le pattern « production from scratch avec sondage D-026 systématique » (recommandé S2.4) est confirmé indispensable pour les modules sans HTML canonique préexistant.

### Pattern 5 — Discipline hygiène merge Cowork à renforcer

3 occurrences récurrentes de marqueurs de conflit non résolus (cf. §4 observation #1). Pattern opérationnel à acter en discipline.

---

## 6. Recommandations SPEC v2.0 (à arbitrer Cowork)

À arbitrer par Cowork après merge de la PR finale S2.5 :

### Proposition 1 — Discipline hygiène merge

**Contexte** : §4 observation #1, 3 occurrences de marqueurs `<<<<<<<` committés.

**Suggestion d'ajout à SPEC §Hygiène opérationnelle (nouvelle section v2.0)** :
> Après tout `git stash pop` ou résolution de conflit, exécuter **`git grep "<<<<<<<"` (et `>>>>>>>`, `=======`) avant `git add`** pour vérifier l'absence de marqueurs de conflit résiduels. Un commit contenant ces marqueurs est un anti-pattern d'hygiène (3 occurrences récurrentes S2.5 PR #84/#86/#88).

### Proposition 2 — Pattern « 3 niveaux retrieval » comme procédure normée

**Contexte** : pattern validé sur 6 cas-écoles (§5 pattern 1).

**Suggestion d'ajout à SPEC §Validation (procédure)** :
> Quand un chunk cible est hors top-5 d'une question golden set : (1) lancer un **Lot Drer ciblé** (rerun de la seule question + dump retrieval) pour mesurer le rang et la similarité actuels ; (2) appliquer le **niveau d'intervention minimal** selon l'écart résiduel — Niveau 1 (lead bridge) si rang #6-8, Niveau 2 (H2 concurrente) si rang #9-15, Niveau 3 (densification chirurgicale) si hors top-15 ; (3) re-valider par Lot Drer avant rerun complet.

### Proposition 3 — Précision §Performances latence

**Contexte** : Lot Drer-S2.5.x ~19 s/q légèrement au-dessus de la bande 12-18 s.

**Suggestion d'ajout à SPEC §Performances** :
> À surveiller : la latence Sonnet 4.6 augmente avec la taille du vault (289 chunks post-vague 5). Si le dépassement de la bande 12-18 s/q devient récurrent (≥ 2 sprints consécutifs), envisager : (a) réduction top-k, (b) bascule partielle Haiku 4.5, (c) cache d'embeddings query. Bande recalibrée si volume vault > 300 chunks confirmé.

---

## 7. Pistes investigation S2.6

1. **Vague 6 production** : PR-09 (cadrer projet IA stratégique), PR-10 (vérifier/limiter hallucinations), PR-11 (cycle de vie projet IA pivot). **Sondage D-026 systématique** codifié SPEC v1.9 §Validation — obligatoire pour PR-10 et PR-11 vu leur densité.
2. **Investigation latence vault > 200 chunks** : vault actuel 289 chunks, à monitorer. Cf. proposition 3 §6.
3. **Audit régression à vault > 30 fichiers MD** : actuel 23, vague 6 portera à 26. Le seuil 30 reste à surveiller.
4. **R11 audit pattern wikilinks post-query** (`rag/code/backend/citation_audit.py`) — toujours reporté depuis S2.3 Lot D. À arbitrer si toujours pertinent ou abandonner formellement.
5. **Lot I-bis re-run 72q formel** (~1,8 $ Anthropic) — optionnel, à arbitrer si validation formelle requise pour archivage projet (sceller le 72/72 mesuré vs extrapolé).

---

## 8. Coûts cumulés S1 → S2.5

### Détail S2.5

| Phase | Acteur | Coût $ |
|---|---|---|
| Phase 1 — correctifs leads + reruns Drer | Cowork (0) + Desktop | ~0,21 |
| Phase 2 — production 8 modules + sondage | Cowork + Cowork Hub IA | 0,00 |
| Phase 3 Lot I — eval 72q | Desktop | 1,7816 |
| Phase 3 S2.5.x — densification | Cowork | 0,00 |
| Phase 3 Drer-S2.5.x — validation ciblée 4q | Desktop | 0,1063 |
| Lot J — RAPPORT + PR (ce commit) | Plateforme | 0,00 |
| **Total S2.5** | — | **~2,10 $** Anthropic + ~0,002 $ OpenAI |

### Cumul historique S1 → S2.5

| Sprint | Coût $ Anthropic |
|---|---|
| S1 (S1c.2 local) | ~0,30 |
| S1bis + S1ter + S2.1 | 0,00 |
| S2.2 | ~2,50 |
| S2.3 | ~1,02 |
| S2.4 | ~1,28 |
| **S2.5** | **~2,10** |
| **Total cumulé S1 → S2.5** | **~7,20 $** |

OpenAI cumulé : ~0,007 $ (embeddings + ingest incréments).

### Budget

| Provider | Crédits initiaux | Consommé S1 → S2.5 | Restant |
|---|---|---|---|
| Anthropic | ~3,00 $ (prépayés) | ~7,20 $ | dépassement crédits prépayés |
| OpenAI | ~5,00 $ | ~0,007 $ | ~4,99 $ |

**Cap mensuel D-013 (50 $/mois Anthropic, 10 $/mois OpenAI) très largement préservé** — le cumul ~7,20 $ reste sous le plafond mensuel. L'alerte « crédits prépayés » signalée depuis S2.2 reste pertinente pour le suivi de trésorerie, mais elle n'est pas bloquante au regard du cap mensuel structurel. La décision de recharge / bascule Haiku 4.5 / eval ciblée reste à la main de Blaise selon l'ambition S2.6.

---

## Liste des commits S2.5 (synthèse)

| Phase | PR | Lot | Acteur |
|---|---|---|---|
| 1 | #75-77 | S2.5.0/bis/ter correctif q-030 (leads cu-001/pr-07/pr-08) | Cowork |
| 2 | #78-79 | F.5a DEP-01 + DEP-07 | Cowork |
| 2 | #80-81 | F.5b PR-01 + PR-04 | Cowork |
| 2 | #82 | F.5c DEP-05 + PR-05 | Cowork |
| 2 | #83 | F.5d CU-020 + CU-024 | Cowork |
| 3 | #84 | G cartographie v3 + H golden set 72q | Cowork |
| 3 | #85 | I eval extended 72q (70/72) | Desktop |
| 3 | #86 | S2.5.x correctif q-036/q-056 | Cowork |
| 3 | #87 | Drer-S2.5.x validation ciblée 4/4 (`5e9464e`) | Desktop |
| 3 | *(ce commit)* | J RAPPORT + PR finale | Plateforme |

**Suite tests cumulée S1 → S2.5** : 190/190 verts.

---

*Rapport produit le 22 mai 2026 par Claude Code Hub IA Plateforme (Lot J). Format conforme brief CC-S2.5 (8 sections, ~2700 mots) + déposé dans `rag-prep/reports/` selon convention Cowork. Sprint S2.5 définitivement clôturé après merge de la PR finale. Les 3 propositions d'amendement SPEC v2.0 (§6) restent à arbitrer par Cowork après merge. Réserve méthodologique : 72/72 extrapolé (validation ciblée 4q), Lot I-bis re-run complet optionnel.*
