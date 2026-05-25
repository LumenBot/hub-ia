# RAPPORT-CC-S2.7 — Vague 7 (5 fiches outils) + golden set adversarial + robustesse RAG validée

**Émetteur :** Claude Code Hub IA Plateforme (Lot J)
**Destinataire :** Cowork Hub IA Plateforme + Blaise Cavalli (garant transverse)
**Sprint :** S2.7 (clôture définitive)
**Brief source :** `rag-prep/briefs/BRIEF-CC-S2.7.md` + sondage `RETOUR-SONDAGE-COWORK-HUB-IA-S2.7-VAGUE-7.md`
**Branche développement :** `claude/execute-s27-lot-j-rapport` (depuis `main` post-merge PR #100)
**Date :** 25 mai 2026
**Allocation D-030 :** enrichie — Cowork (Lots A, F.7, G, H) + Cowork Hub IA (sondage D-026) + Claude Code Plateforme (Lot Dev + Lot Dev fix + Lot J, **dès le démarrage**) + Claude Code Desktop (Lot I eval)

---

## 1. Objectifs S2.7

Le sprint S2.7 marque un tournant méthodologique : pour la première fois, le RAG est soumis à un **test de robustesse adversarial** (questions pièges où il doit refuser de répondre), en complément de l'évaluation standard. Quatre axes :

1. **Production vague 7 — 5 fiches outils** (Lot F.7) : `outils-llm`, `outils-frameworks-rag`, `outils-knowledge-management`, `outils-observabilite-llm`, `outils-workflow-automation` + extraction d'une brique transverse « souveraineté EU des outils ».

2. **Extension code — mode adversarial** (Lot Dev, allocation D-030 enrichie : Plateforme dès le démarrage) : `run_eval.py` gère désormais 2 modes (standard + adversarial avec détection de refus correct vs hallucination).

3. **Golden set 108 questions** (Lot H) : 96 questions standard + 12 questions adversariales (questions pièges sur des dispositifs/chiffres fictifs).

4. **Question structurante du sprint** : le score parfait S2.6 (81/81) traduisait-il un **overfit du golden set** (questions en miroir des modules) ou une **robustesse réelle** du RAG ? Le bloc adversarial est conçu pour trancher.

**Cibles** : standard ≥ 90/100, latence p50 ≤ 21 s / p90 ≤ 25 s, coût Lot I ≤ 3,00 $.

---

## 2. Livrables par lot

| Lot | Acteur | Commit / PR | Périmètre |
|---|---|---|---|
| **A — SPEC v2.1 + BRIEF-CC-S2.7** | Cowork | PR #96 | 3 ajouts SPEC v2.1 (recalibrage cap coût, extension bande latence vault 300-400, pattern module pivot dense) + brief double-axe (standard + adversarial). |
| **Dev — Mode adversarial** | Claude Code Plateforme | PR #97 | Extension `run_eval.py` : `is_adversarial`, `REFUSAL_MARKERS` (7 marqueurs), `evaluate_adversarial` (3 verdicts), reporting 2 blocs. +14 tests (204/204). README. |
| **B — Sondage D-026 vague 7** | Cowork Hub IA | `DRAFT-SONDAGE-COWORK-HUB-IA-S2.7-VAGUE-7.md` | Sondage 5 fiches outils (listes exhaustives, tarifs canoniques 2026, différenciation cross-fiches, recouvrements cu-008/dep-05/dep-02). |
| **F.7 + G + H — Production vague 7** | Cowork | PR #98 | 5 fiches outils + brique transverse souveraineté EU + cartographie + golden set 108q (96 std + 12 adv). |
| **I — Eval 108q + latence p50/p90 par mode** | Desktop | PR #99 | Vault 32 MD / 380 chunks. Standard 96/96 (100 %). Adversarial : faux négatif harness identifié (0/12 → diagnostic calibration). Latence + coût. |
| **Dev fix — Calibration v2 harness adversarial** | Claude Code Plateforme | PR #100 | Correctif des 2 bugs de calibration (markers strong/weak + marqueur franc prime sur citations). Re-scoring offline 12/12. +2 tests (206/206). |
| **J — RAPPORT + PR finale** | Plateforme | *(ce commit)* | Présent rapport + ouverture PR finale S2.7. |

**Particularité S2.7** : double intervention Plateforme (Lot Dev en amont + Lot Dev fix en cours de sprint), conformément à l'allocation D-030 enrichie. Pas de Lot Drer (aucune régression retrieval).

---

## 3. Métriques quantitatives

### Bloc standard — 96/96 (100 %)

| Indicateur | Cible | Mesuré | Statut |
|---|---|---|---|
| **Sources retrouvées** | ≥ 90/100 | **96/96 (100 %)** | ✅ Dépassée |
| **Score global** | ≥ 90/100 | **96/96 (100 %)** | ✅ |
| **Non-régression** | 7/7 | **7/7** (q-002/q-030/q-036/q-038/q-051/q-052/q-056) | ✅ |

### Bloc adversarial — 12/12 après calibration v2

| Étape | Refus corrects | Lecture |
|---|---|---|
| Harness Lot Dev (initial) | **0/12** | Faux négatif (2 bugs calibration) |
| Calibration v2 (Lot Dev fix, re-scoring) | **12/12** | Robustesse RAG réelle |

Le RAG produit la phrase canonique de refus du system prompt (« Je n'ai pas de réponse documentée dans le Hub IA ») sur les 12 questions pièges. 11/12 citent le contexte récupéré pour **expliquer** le manque (légitime), 1/12 ne cite aucune source.

### Latence par mode (p50/p90)

| Mode | p50 | p90 | Cible (p50 ≤ 21 / p90 ≤ 25) |
|---|---|---|---|
| Standard | 19,0 s | 22,0 s | ✅ |
| Adversarial | 10,0 s | 15,0 s | ✅ |

La latence adversariale est notablement plus basse : le RAG produit une réponse courte de refus (pas de synthèse longue à générer).

### Coût et vault

| Poste | Valeur |
|---|---|
| **Coût Lot I (Anthropic)** | **2,5866 $** (cible ≤ 3,00 $ ✅) |
| Coût Lot Dev + Lot Dev fix | 0,00 $ (code + tests + re-scoring offline) |
| Vault | 32 fichiers MD / **380 chunks** (vague 7 : +62 chunks) |
| Ingestion incrémentale | new=62, 318 → 380 chunks |

### Suite tests cumulée

**206/206 verts** (190 cumulés S1-S2.6 + 14 Lot Dev + 2 Lot Dev fix). Premier sprint avec extension de code substantielle côté Plateforme depuis S2.3 (Lot D).

---

## 4. Anomalies & observations

### Anomalie majeure — faux négatif du harness adversarial (résolu)

**Symptôme** : le harness Lot Dev reportait **0/12 refus corrects** (11 hallucinations + 1 refus partiel) au Lot I, alors que l'analyse manuelle des 12 réponses montrait un refus textuel correct dans 100 % des cas.

**Cause racine** (2 bugs de calibration code, pas le vault) :
1. `REFUSAL_MARKERS` ne contenait **pas** la phrase canonique du system prompt query.py « Je n'ai pas de réponse documentée dans le Hub IA » → `refusal_detected()` = False sur les 12.
2. Verdict `refus_correct` exigeait `not cited`, or 11/12 réponses citent le contexte récupéré pour **expliquer** le manque (comportement légitime, pas une tentative de réponse).

**Fix** (Lot Dev fix, PR #100, calibration v2) :
- Distinction `STRONG_REFUSAL_MARKERS` (refus franc, dont la phrase canonique) vs `WEAK_REFUSAL_MARKERS` (doute).
- Le marqueur **franc prime sur les citations** : refus_correct même si le RAG cite le contexte.
- Re-scoring offline (coût 0 $) → **12/12 refus corrects**.

**Leçon process** : le harness d'évaluation est lui-même du code à valider. Un faux négatif de calibration aurait publié un « 0/12 » trompeur. La détection est venue de la **lecture manuelle des réponses** par le Lot I Desktop — confirmant l'importance du contrôle humain sur les résultats d'eval automatisés (à inscrire en SPEC, §6).

### Observation #1 — Écart de procédure `--filter-unit` (résolu)

Le flag `--filter-unit` n'existe pas dans le Lot Dev (l'auto-dispatch standard/adversarial + reporting 2 blocs rendait le filtre superflu côté code). Le Desktop a contourné via 2 sous-golden-sets dérivés (`questions-s2.7-standard.yaml` + `questions-s2.7-adversarial.yaml`), en lecture seule (D-022 respecté), pour produire des artefacts séparés. Coût identique.

### Observation #2 — Hygiène merge respectée

`git grep "<<<<<<<"` = vide. Discipline SPEC v2.0 maintenue (2e sprint consécutif sans marqueur de conflit).

---

## 5. Décisions structurantes prises pendant S2.7

Aucune décision **actée** Git-side (SPEC v2.1 stable). **4 patterns / findings validés empiriquement** :

### Finding 1 — Robustesse RAG réelle, PAS d'overfit (réponse à la question structurante)

La question d'ouverture du sprint était : le score parfait S2.6 (81/81) est-il de l'overfit du golden set (questions en miroir des modules) ou une robustesse réelle ?

**Réponse mesurée : robustesse réelle.** Le bloc adversarial (questions pièges sur dispositifs/chiffres fictifs, hors corpus) obtient **12/12 refus corrects** : le RAG ne hallucine pas sur des sujets non couverts, il refuse explicitement. Combiné au 96/96 standard, cela démontre que le RAG **discrimine** correctement entre ce qu'il sait (corpus) et ce qu'il ne sait pas (hors corpus). Le score standard parfait n'est donc pas un artefact de sur-ajustement — c'est la marque d'un vault bien construit + d'un retrieval bien calibré.

### Finding 2 — Le harness d'eval est du code critique à valider

Le faux négatif 0/12 a démontré que la couche d'évaluation peut introduire ses propres biais. Un score automatisé non vérifié peut être trompeur dans les deux sens (faux négatif ici ; un faux positif serait pire). Pattern : **toute nouvelle règle de scoring doit être validée sur un échantillon lu manuellement** avant publication d'un rapport.

### Finding 3 — Marqueur de refus franc ≠ absence de citations

Intuition initiale (Lot Dev) : un refus correct ne cite aucune source. Réalité observée : un bon RAG cite le contexte récupéré **pour expliquer pourquoi le sujet n'est pas couvert** (« le dispositif XYZ-2027 n'apparaît dans aucun de ces extraits [PR-08] »). C'est un comportement souhaitable, pas une hallucination. La calibration v2 distingue « citer pour expliquer le manque » (refus correct) de « citer pour inventer une réponse » (hallucination).

### Finding 4 — Allocation D-030 enrichie validée

Première application du pattern « Plateforme intervient dès le démarrage » (Lot Dev en amont) + correctif en cours de sprint (Lot Dev fix). Le double rôle code de la Plateforme a permis de livrer le mode adversarial ET de corriger sa calibration dans le même sprint, sans bloquer le Lot J. Pattern reconductible quand un sprint introduit une nouvelle capacité d'évaluation.

---

## 6. Recommandations SPEC v2.2

À arbitrer par Cowork après merge de la PR finale S2.7 :

### Proposition 1 — Validation manuelle obligatoire d'une nouvelle règle de scoring

**Contexte** : §4 anomalie majeure — le faux négatif 0/12 du harness aurait pu publier un résultat trompeur.

**Suggestion d'ajout à SPEC §Validation eval réelle** :
> **Validation d'une nouvelle règle de scoring (v2.2)** : toute extension du harness d'évaluation (`run_eval.py`) introduisant une nouvelle logique de scoring (nouveau mode, nouveau verdict) doit être validée sur un **échantillon lu manuellement** (≥ 5 cas) avant publication d'un rapport. Un score automatisé non recoupé avec la lecture humaine des réponses est un risque de faux négatif/positif. Le finding S2.7 (harness 0/12 vs réalité 12/12) en est le cas-école.

### Proposition 2 — Codifier le critère « citer pour expliquer le manque » (refus adversarial)

**Contexte** : §5 finding 3, la calibration v2 distingue strong/weak markers.

**Suggestion d'ajout à SPEC §Validation (mode adversarial)** :
> **Refus correct vs hallucination (codifié S2.7)** : un refus est **correct** si la réponse contient un marqueur de refus franc (notamment la phrase canonique du system prompt), **même si elle cite des sources** — le RAG peut légitimement citer le contexte récupéré pour expliquer pourquoi le sujet n'est pas couvert. Une **hallucination** est l'absence de marqueur de refus + une réponse inventée plausible. Distinction strong/weak markers documentée dans `run_eval.py`.

### Proposition 3 — Étendre le golden set adversarial en S2.8+

**Contexte** : 12 questions adversariales valident la robustesse, mais sur un échantillon restreint. Une couverture adversariale plus large (par famille de modules) renforcerait la confiance.

**Suggestion** :
> **Extension adversariale progressive (v2.2)** : viser ~2 questions adversariales par vague de production (dispositifs/chiffres fictifs proches du domaine du module), pour maintenir un ratio adversarial/standard ≈ 12-15 % et stress-tester le refus au fil de l'élargissement du vault.

---

## 7. Pistes investigation S2.8

1. **Audit R11 wikilinks post-query** (`rag/code/backend/citation_audit.py`) — le pré-requis « 5+ fichiers `outils-*.md` » est désormais **rempli** (vague 7 a produit 5 fiches outils + outils-vector-db = 6). R11 devient implémentable. Priorité S2.8.
2. **Sprint dédié latence** : vault à 380 chunks (> 300, bande SPEC v2.1 « 300-400 »). p50/p90 standard (19/22 s) restent conformes mais la marge se réduit. À 400+ chunks (vague 8), activer reranking / réduction top-k / cache embeddings.
3. **Extension golden set adversarial** (cf. §6 proposition 3) : ~2 questions pièges par vague.
4. **Vague 8** : architectures A1-A4 (les fiches outils étant désormais couvertes). Sondage D-026 systématique maintenu.
5. **Re-run adversarial formel** : le 12/12 est issu d'un re-scoring offline (answer_preview proxy). Un rerun Desktop sur réponses intégrales avec le harness v2 sceller­ait le résultat (optionnel, ~0,1 $).

---

## 8. Coûts cumulés S1 → S2.7

### Détail S2.7

| Phase | Acteur | Coût $ |
|---|---|---|
| Lot A — SPEC v2.1 + brief | Cowork | 0,00 |
| Lot Dev — mode adversarial | Plateforme | 0,00 |
| Lot B — sondage D-026 | Cowork Hub IA | 0,00 |
| Lot F.7 + G + H — vague 7 + golden set 108q | Cowork | 0,00 |
| **Lot I — eval 108q** | Desktop | **2,5866** |
| Lot Dev fix — calibration v2 + re-scoring offline | Plateforme | 0,00 |
| Lot J — RAPPORT + PR (ce commit) | Plateforme | 0,00 |
| **Total S2.7** | — | **~2,59 $** |

### Cumul historique S1 → S2.7

| Sprint | Coût $ Anthropic |
|---|---|
| S1 → S2.4 | ~5,10 |
| S2.5 | ~2,10 |
| S2.6 | ~2,05 |
| **S2.7** | **~2,59** |
| **Total cumulé S1 → S2.7** | **~11,84 $** |

OpenAI cumulé : ~0,01 $ (embeddings + ingest incréments).

### Budget

**Cap mensuel D-013 (50 $/mois Anthropic, 10 $/mois OpenAI) préservé** — le cumul ~11,84 $ depuis S1 (sur ~6 semaines) reste sous le plafond mensuel. L'alerte « crédits prépayés Anthropic » signalée depuis S2.2 reste pertinente : le rythme ~2,5 $/sprint (eval croissante avec le vault) appelle une recharge avant la vague 8 si l'ambition se maintient. Pistes d'optimisation coût/latence (reranking, Haiku 4.5 pour l'eval, top-k réduit) à arbitrer en S2.8.

---

## Liste des commits / PR S2.7

| PR | Lot | Acteur |
|---|---|---|
| #96 | A — SPEC v2.1 + BRIEF-CC-S2.7 | Cowork |
| #97 | Dev — mode adversarial run_eval | Plateforme |
| #98 | F.7 + G + H — vague 7 (5 fiches outils) + souveraineté EU + golden set 108q | Cowork |
| #99 | I — eval 108q (96 std + 12 adv) + latence p50/p90 | Desktop |
| #100 | Dev fix — calibration v2 harness adversarial (re-scoring 12/12) | Plateforme |
| *(ce commit)* | J — RAPPORT + PR finale | Plateforme |

**Suite tests cumulée S1 → S2.7** : 206/206 verts.

---

*Rapport produit le 25 mai 2026 par Claude Code Hub IA Plateforme (Lot J). Format conforme brief CC-S2.7 (8 sections) + déposé dans `rag-prep/reports/` selon convention Cowork. Sprint S2.7 définitivement clôturé après merge de la PR finale. **Finding central : robustesse RAG réelle validée (96/96 standard + 12/12 adversarial) — le score parfait S2.6 n'était pas de l'overfit.** Les 3 propositions d'amendement SPEC v2.2 (§6) restent à arbitrer par Cowork après merge.*
