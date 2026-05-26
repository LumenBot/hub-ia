# RAPPORT-CC-S2.8 — Vague 8 (5 architectures A1-A4 + Hybride) + R11 audit wikilinks + alerte vault > 400 chunks

**Émetteur :** Claude Code Hub IA Plateforme (Lot J)
**Destinataire :** Cowork Hub IA Plateforme + Blaise Cavalli (garant transverse)
**Sprint :** S2.8 (clôture définitive)
**Brief source :** `rag-prep/briefs/BRIEF-CC-S2.8.md` (sprint hybride triple axe)
**Branche développement :** `claude/execute-s28-lot-j-rapport` (depuis `main` post-merge PR #105)
**Date :** 26 mai 2026
**Allocation D-030 :** hybride enrichie (récurrence S2.7) — Cowork (Lots A, F.8, G, H) + Cowork Hub IA (sondage D-026) + Claude Code Plateforme (**Lot Dev R11 dès le démarrage** + Lot J) + Claude Code Desktop (Lot I eval extended)

---

## 1. Objectifs S2.8

Le sprint S2.8 prolonge l'allocation hybride S2.7 (Plateforme code + rapport, Cowork éditorial, Desktop eval) en l'appliquant à un sprint à triple axe :

1. **Activation R11 audit wikilinks outils glossariés** (Lot Dev Plateforme) — extension `rag/code/audit/citation_audit.py` pour vérifier que tout outil ayant sa propre fiche `outils-*.md` est wikilinké à sa première occurrence dans tout autre MD. Pré-requis franchi en S2.7 (6 fiches outils ≥ seuil 5+ codifié SPEC v1.4).
2. **Production vague 8 — 4+1 architectures A1-A4 + Hybride** (Lot F.8 Cowork) — fiches `architecture-a1-saas-proprietaire`, `architecture-a2-proprietaire-managee`, `architecture-a3-os-cloud-souverain`, `architecture-a4-os-on-premise`, et `architecture-hybride` (ajustement Cowork : 5 fiches au lieu des 4 annoncées dans le brief initial — +1 brique transverse `pattern-grille-archi-decisionnelle` également intégrée).
3. **Extension golden set vague 8 + +2 questions adversariales** (Lot H Cowork) — 8 nouvelles questions standards (q-082 à q-089) et 2 nouvelles questions adversariales (q-adv-013/014), codification SPEC v2.2 §rythme « ~2 questions adversariales par vague ».
4. **Question structurante** : la projection latence vault > 400 chunks se confirme-t-elle, et la robustesse RAG résiste-t-elle à l'élargissement du corpus + à 2 nouvelles questions pièges (XYZ-2027 architecture inexistante + MTBF chirurgical) ?

**Cible eval finale** : standard ≥ 96/104 (≥ 92 %), adversarial ≥ 12/14 (≥ 86 %), non-régression S2.7 intégrale, latence standard p50 ≤ 22 s / p90 ≤ 26 s, coût ≤ 2,80-3,00 $ Anthropic.

---

## 2. Livrables par lot

| Lot | Acteur | Livrable | PR | Statut |
|---|---|---|---|---|
| **A** | Cowork | SPEC v2.2 + BRIEF-CC-S2.8 | #102 | ✅ mergée |
| **B** | Cowork Hub IA | Sondage D-026 vague 8 + RETOUR-SONDAGE | — (Cowork-side) | ✅ livré |
| **F.8 + G + H** | Cowork | 5 fiches architectures A1-A4 + Hybride + brique `pattern-grille-archi-decisionnelle` + whitelist v6 + golden set 118q (104 std + 14 adv) | #103 | ✅ mergée |
| **Dev R11** | Plateforme | `rag/code/audit/citation_audit.py` (R11) + 28 tests + VALIDATION-SCORING-S2.8-R11 (5/5 conforme) + rapport vault `audit-md-rag-R11-s2.8.{md,json}` (85 manquements détectés) | #104 | ✅ mergée |
| **I** | Desktop | Eval 118q (104 std + 14 adv) sur vault 38 MD / 444 chunks + dump diagnostic q-083 | #105 | ✅ mergée |
| **J** | Plateforme | RAPPORT-CC-S2.8 (ce document) + PR finale | *(en cours)* | ⏳ |

**Récurrence du pattern Lot Dev Plateforme** (introduit S2.7) confirmée : la Plateforme intervient désormais dès le démarrage du sprint sur l'extension du code RAG (audit, eval, ingestion) et clôture par le rapport — pattern qui sera codifié SPEC v2.3 §allocation hybride D-030 (proposition §6).

---

## 3. Métriques quantitatives

### Bloc standard — 103/104 (99 %)

| Indicateur | Cible | Réalisé | Statut |
|---|---|---|---|
| Sources attendues retrouvées | ≥ 96/104 (≥ 92 %) | **103/104** (99 %) | ✅ |
| Concepts ≥ 50 % couverts | ≥ 96/104 (≥ 92 %) | **93/104** (89 %) | 🟡 sous cible mais score global OK |
| Score global (source + concepts ≥ 50 %) | ≥ 96/104 (≥ 92 %) | **103/104** (99 %) | ✅ |
| Non-régression S2.7 (9 questions surveillées) | 9/9 | **9/9** (q-002/030/036/038/051/052/056/073/076 = 1) | ✅ |

**Seul échec standard — q-083** « Quel est le tarif API de Claude Sonnet et Opus en 2026 ? ». Source attendue `outils-llm` rang #6 (sim -0,067), étouffée dans le top-5 par `chiffres-macro-2026` (#1 sim 0,141), `architecture-a1-saas-proprietaire` (#2 sim 0,123), `cu-027` (#3 sim -0,040), `architecture-a3-os-cloud-souverain` (#4), `architecture-a2-proprietaire-managee` (#5) — les 3 nouvelles fiches architectures avec leur section H2 « Coût indicatif (vague 8) » saturent la similarité sémantique sur le terme « coût/tarif » au détriment de `outils-llm`. Question à la frange du scope (vault couvre l'« économie d'inférence » macro et non les prix unitaires $/MTok). Pattern de saturation analogue à celui observé S2.4 sur q-002/030 (lead bridge sur-élargi → AP-7) mais ici sur le cluster de fiches sœurs « architectures » plutôt qu'un module pivot dense. **Non bloquant** (1/104 = 1 % d'erreur, score global > cible).

### Bloc adversarial — 14/14 (100 %)

| Indicateur | Cible | Réalisé | Statut |
|---|---|---|---|
| Refus corrects | ≥ 12/14 (≥ 86 %) | **14/14** (100 %) 🎉 | ✅ |
| Hallucinations détectées | 0 | **0** | ✅ |
| Refus partiels | ≤ 2 | **0** | ✅ |

**Premier instrument adversarial passé en production avec la calibration v2 (PR #100 S2.7) et confirmé empiriquement** : les 14/14 incluent les 12 questions du bloc S2.7 (non-régression intégrale) + les 2 nouvelles q-adv-013 (« architecture XYZ-2027 inexistante ») et q-adv-014 (« MTBF chirurgical A4 on-premise »). Le RAG refuse correctement avec la phrase canonique « Je n'ai pas de réponse documentée dans le Hub IA pour cette question. » dans les 14 cas, même quand il cite des sources pour expliquer le manque (pattern « citer pour expliquer le manque » désormais codifié SPEC v2.2 §Validation adversarial).

### Latence par mode (p50/p90)

| Mode | p50 cible | p50 réel | p90 cible | p90 réel | Statut |
|---|---|---|---|---|---|
| Standard | ≤ 22 s | **19,0 s** | ≤ 26 s | **22,0 s** | ✅ |
| Adversarial | ≤ 12 s | **10,0 s** | ≤ 17 s | **12,0 s** | ✅ |

Latence sous cibles dans les deux modes, **mais vault à 444 chunks (zone haute SPEC v2.1 §Performances « 300-400 », seuil 400 franchi)** — voir §4 alerte structurante.

### Coût et vault

| Indicateur | Cible | Réalisé | Statut |
|---|---|---|---|
| Coût Anthropic Lot I | 2,80-3,00 $ | **2,8466 $** | ✅ |
| Vault total | ≤ 440 chunks (projection brief) | **444 chunks** (38 MD) | 🟡 alerte > 400 |
| Delta chunks vs S2.7 | +40-60 (projection) | +64 (vague 8) | ✅ aligné |

### Suite tests cumulée

| Indicateur | S2.7 | S2.8 | Delta |
|---|---|---|---|
| Tests `rag/code/` | 206 | **234** | +28 (citation_audit.py) |
| Tests `rag/code/audit/` | 93 | **121** | +28 |
| Tests verts | 206/206 | **234/234** | ✅ |

---

## 4. Anomalies & observations

### Anomalie majeure — vault > 400 chunks franchit le seuil §Performances v2.1

**Constat** : 444 chunks (vault 38 MD), seuil 400 dépassé de 11 %. La latence reste sous cible (p50 19 s, p90 22 s en standard) mais en zone haute de la bande SPEC v2.1. **Le brief BRIEF-CC-S2.8 §1.4 avait anticipé** cet événement et codifié à l'avance la recommandation : « si Lot I S2.8 mesure vault > 400 chunks, recommandation explicite sprint S2.9 dédié optimisation (reranking / Haiku 4.5 sur eval / top-k réduction 5 → 3) ». **Le déclencheur est donc atteint** — sprint S2.9 d'optimisation latence/coût explicitement recommandé (cf. §7 Pistes investigation).

**Pourquoi c'est important** : à ce rythme (~+60 chunks/vague), un vault 500-550 chunks fin S2.10 conduirait à un dépassement p90 dur si aucune optimisation n'est introduite. La fenêtre S2.9 = bon moment (post-vague 8 stable, avant vague 9). À noter : la projection brief 420-440 a été légèrement débordée par la décision Cowork d'inclure +1 fiche `architecture-hybride` + 1 brique `pattern-grille-archi-decisionnelle` (5 fiches au lieu de 4 annoncées), choix éditorial pertinent qui ne remet pas en cause l'alerte.

### Anomalie — q-083 saturation sémantique tarifs API LLM

**Constat** : `outils-llm` rang #6 (hors top-5) sur q-083 « Tarif API Claude Sonnet/Opus », étouffé par les 3 chunks « Coût indicatif (vague 8) » des nouvelles fiches architectures + `chiffres-macro-2026` (économie d'inférence Kimi K2.6) + `cu-027` (rupture économique 2026). Réponse RAG correcte sur le fond (refuse de répondre par défaut de documentation précise des tarifs $/MTok Sonnet/Opus) mais échec scoring source.

**Diagnostic** :
- Question **à la frange du scope** (le vault Hub IA documente l'économie d'inférence macro et la position relative des modèles, pas les grilles tarifaires unitaires).
- Pattern de saturation propre aux **clusters de fiches sœurs** (vs cas-école S2.4 q-002/030 sur module pivot dense — pr-08). C'est un AP-7 latent côté production architectures : si chaque fiche architecture utilise la même structure H2 « Coût indicatif » avec le même lead « ce que coûte cette architecture en € / mois pour PME 50 sal », les 5 fiches occupent le même espace sémantique sur les requêtes coût.
- **Pas un défaut R11** : R11 protège la première occurrence d'un outil, pas la saturation de chunks autour d'un concept transverse.

**Mitigation possible** (à arbitrer S2.9 Cowork) : différencier les leads des sections « Coût indicatif » entre les 5 architectures (A1 = TCO mainstream US, A2 = TCO managé EU, A3 = TCO OS cloud souverain, A4 = TCO OS on-premise, Hybride = arbitrage) — ce qui réduirait la similarité croisée et libérerait du top-5 pour `outils-llm` sur les questions tarifs unitaires. Alternative : enrichir `outils-llm` avec une section H2 dédiée « Tarifs API référence (état 2026) ». **Non bloquant pour S2.8.**

### Observation #1 — Écart de procédure `--filter-unit` (2ᵉ occurrence — à fixer durablement)

**Constat** : le brief BRIEF-CC-S2.8 §8 prescrit à nouveau `--filter-unit adversarial`, mais ce flag n'a **toujours pas** été ajouté à l'argparse de `rag/code/eval/run_eval.py` (PR #100 a corrigé la calibration du harness mais n'a pas étendu le CLI). Desktop a contourné comme en S2.7 par 2 sous-golden-sets dérivés.

**C'est une 2ᵉ occurrence** : l'écart S2.7 avait été noté comme « résolu côté procédure » dans RAPPORT-CC-S2.7 §4 Observation #1, mais sans fix code. **Recommandation Plateforme S2.9** : ajouter `--filter-unit {standard,adversarial,all}` à l'argparse de `run_eval.py` (effort ~5 min code + 1 test). Évite la 3ᵉ occurrence en S2.9.

### Observation #2 — Hygiène merge respectée (3ᵉ sprint consécutif)

**Constat** : `git grep "<<<<<<<"` retourne uniquement des références documentaires (mentions de la règle elle-même dans `SPEC-MD-POUR-RAG.md` + `JOURNAL-POC-RAG.md`), aucun marqueur de conflit réel introduit. Discipline SPEC v2.0 §Hygiène merge respectée depuis S2.6 (3ᵉ sprint consécutif clean).

**Note Desktop Lot I** : un stash a été préservé pour absorber des modifications Cowork-side locales qui colidaient avec BRIEF-CC-S2.8 + citation_audit.py fraîchement committés sur main — discipline appliquée et tracée dans STATUS.

### Observation #3 — Décalage projection vague 8 (+1 fiche + 1 brique transverse)

**Constat** : Cowork a livré 5 fiches architectures (A1-A4 + Hybride) au lieu des 4 annoncées dans le brief, et a ajouté +1 brique transverse `pattern-grille-archi-decisionnelle`. Cette densification éditoriale (~+15 chunks marginaux) est cohérente avec la cible « Hybride » identifiée pendant le sondage D-026 vague 8, et avec la grille décisionnelle inter-architectures qui mérite une brique propre (extractable D-025). Vault à 444 vs 420-440 projeté. Non bloquant — alerte > 400 reste l'enjeu principal.

---

## 5. Décisions structurantes prises pendant S2.8

### Finding 1 — Robustesse RAG confirmée à 118 questions (102 % du gold set précédent)

L'extension du golden set à 118 questions (+10 vs S2.7) maintient le double score excellent : **103/104 standard + 14/14 adversarial**. La PR #100 (calibration v2 harness adversarial S2.7) est validée empiriquement sur un panel élargi — pas de régression sur les 12 questions originelles, et les 2 nouvelles q-adv-013/014 sont scorées correctement. **Le RAG discrimine correctement corpus vs hors-corpus sur un éventail désormais significatif** (XYZ-2027 architecture inexistante, MTBF chirurgical, feng shui Pleias-RAG, pisciculture vosgienne, etc.).

### Finding 2 — Le pattern « citer pour expliquer le manque » résiste à l'extension du vault

Sur 14/14 refus adversariaux, **12 citent au moins une source** pour orienter ou contextualiser le manque (pattern codifié SPEC v2.2 §Validation adversarial). Ce comportement reste discriminant du faux négatif S2.7 (avant calibration v2) : la phrase canonique « Je n'ai pas de réponse documentée » prime sur la présence de citations. **La codification SPEC v2.2 tient sur un panel +10** — pas besoin d'ajustement scoring en S2.9 sur ce point.

### Finding 3 — R11 audit livre une valeur immédiate avec 0 régression

Le Lot Dev R11 (citation_audit.py) a détecté **85 manquements R11 réels sur 21 des 32 fichiers MD audités** (avant les 5 architectures vague 8, donc encore plus à venir si Cowork ne patche pas), avec **0 régression sur les 121 tests audit existants** (93 audit-md-rag + 28 nouveaux citation_audit). La règle a été **validée ex-ante sur 5 cas (SPEC v2.2 §Validation manuelle obligatoire)** dans `VALIDATION-SCORING-S2.8-R11.md` — la nouvelle discipline issue de la leçon S2.7 (faux négatif harness 0/12) a été appliquée pour la **première fois sur une règle d'audit** et a prouvé son efficacité (5/5 conforme, pas de surprise au runtime). **La méthodologie SPEC v2.2 §Validation manuelle est désormais validée comme garde-fou structurel** (pas seulement pour les règles de scoring eval mais aussi pour les règles d'audit MD).

### Finding 4 — Saturation par cluster de fiches sœurs : nouveau pattern à observer

L'échec q-083 révèle un pattern de saturation **différent** des cas observés précédemment :
- **S2.4 q-002/030** : module pivot dense (pr-08) saturant le top-5 → résolu par AP-7 lead bridge scope strict.
- **S2.8 q-083** : cluster de 5 fiches sœurs (architectures A1-A4-Hybride) avec sections H2 quasi-identiques (« Coût indicatif ») → saturation sur le terme « coût/tarif ».

Le pattern « production en grappe symétrique » crée une similarité sémantique inter-fiches difficile à arbitrer côté retrieval seul. **À surveiller S2.9+** : si la vague 9 produit une autre grappe (CU-002/003/005), différencier les leads des sections récurrentes (« cas d'usage type », « complexité opérationnelle ») dès la conception MD.

---

## 6. Recommandations SPEC v2.3

### Proposition 1 — Codifier le pattern « cluster de fiches sœurs → différenciation des leads de sections récurrentes »

Ajouter à SPEC §AP-7 (ou nouvelle section §AP-8) une discipline « production en grappe symétrique » : quand plusieurs fiches frères/sœurs partagent une même structure H2 (Coût, Cas d'usage type, Complexité, etc.), les leads de ces sections doivent être **différenciés par scope strict** sur l'angle propre à chaque fiche (« coût A1 SaaS mainstream US » ≠ « coût A4 OS on-premise EU »), pas seulement par le contenu interne. Mitigation du pattern de saturation sémantique observé sur q-083. **Cas-école documenté** : §4 Anomalie q-083.

### Proposition 2 — Officialiser le pattern « Lot Dev Plateforme dès le démarrage du sprint »

Inscrire dans SPEC v2.3 §allocation D-030 que **la Plateforme intervient désormais dès l'ouverture d'un sprint** sur l'extension du code RAG (audit, eval, ingestion) en parallèle du sondage Cowork — pattern empirique S2.7 (mode adversarial) + S2.8 (R11), 2 sprints consécutifs avec ce schéma à 0 $ Anthropic. La récurrence justifie la codification (vs « cas particulier » en S2.7). Bénéfice : raccourcit la boucle production éditoriale ↔ infrastructure d'audit/eval, et libère le sprint suivant d'un re-fix tardif.

### Proposition 3 — Ajouter `--filter-unit` à l'argparse de `run_eval.py` (correctif Plateforme S2.9)

Petit fix code (~5 min) pour éviter la 3ᵉ occurrence du contournement Desktop (cf. §4 Observation #1). À porter en S2.9 dans le sprint d'optimisation, avec test unitaire de filtrage. Sans incidence fonctionnelle (le contournement actuel fonctionne) mais discipline brief ↔ code à rétablir.

---

## 7. Pistes investigation S2.9

**Sprint S2.9 dédié optimisation** (déclencheur vault > 400 atteint, recommandation brief BRIEF-CC-S2.8 §1.4) :

1. **Reranking post-retrieval** (cross-encoder type `bge-reranker-v2-m3`) — passe du top-10 dense → top-5 reranked, traite le pattern de saturation q-083 sans toucher au contenu MD. Effort estimé 4-6h dev + bench.
2. **Réduction top-k 5 → 3** — si l'eval tient à top-3, baisse coût (-40 %) et latence (-15 %) sans perte qualité. À benchmarker.
3. **Embeddings `text-embedding-3-large`** vs `-small` actuel — gain potentiel sur la séparation sémantique (cluster fiches sœurs), surcoût OpenAI marginal sur ingestion uniquement (~0,01 $).
4. **Index hybride BM25 + dense** — utile sur les questions à terminologie précise type q-083 (« Sonnet », « Opus », « $/MTok ») où le terme exact dans `outils-llm#tarifs-api-reference` doit l'emporter sur la similarité diffuse.
5. **Éviction de chunks low-signal** — si certains chunks vague 7-8 ont sim < -0,10 systématique, ils consomment du top-k inutilement. Audit ChromaDB recommandé.
6. **Haiku 4.5 sur eval** (vs Sonnet 4.6 actuel) — bench coût/qualité, peut diviser par 4-5 le coût Lot I (~2,85 $ → ~0,60-0,70 $) si qualité suffisante sur le scoring sources/concepts.
7. **Correctif `--filter-unit`** (cf. §6 proposition 3).

**Patches éditoriaux R11** (Cowork, S2.8 fin ou déféré S2.9) : 85 manquements détectés sur 21 fichiers, ~30-60 min de patch groupé (1 wikilink par 1re occurrence par MD). Recommandation : appliquer en fin de sprint S2.8 puis re-runner `python3 rag/code/audit/citation_audit.py --strict` pour CI-prêt.

**Vague 9** (production éditoriale) : démarrage CU restants (CU-002, CU-003, CU-005) à arbitrer post-S2.9 (priorité à l'optimisation avant nouvelle vague).

---

## 8. Coûts cumulés S1 → S2.8

### Détail S2.8

| Phase | Acteur | Coût $ |
|---|---|---|
| Lot A — SPEC v2.2 + brief | Cowork | 0,00 |
| Lot B — sondage D-026 vague 8 | Cowork Hub IA | 0,00 |
| Lot Dev R11 — citation_audit.py + tests + VALIDATION-SCORING | Plateforme | **0,00** |
| Lot F.8 + G + H — 5 archis + golden set 118q | Cowork | 0,00 |
| **Lot I — eval 118q (104 std + 14 adv)** | Desktop | **2,8466** |
| Lot J — RAPPORT + PR (ce commit) | Plateforme | 0,00 |
| **Total S2.8** | — | **~2,85 $** |

### Cumul historique S1 → S2.8

| Sprint | Coût $ Anthropic |
|---|---|
| S1 → S2.4 | ~5,10 |
| S2.5 | ~2,10 |
| S2.6 | ~2,05 |
| S2.7 | ~2,59 |
| **S2.8** | **~2,85** |
| **Total cumulé S1 → S2.8** | **~14,69 $** |

OpenAI cumulé : ~0,01 $ (embeddings + ingest incréments).

### Budget

**Cap mensuel D-013 (50 $/mois Anthropic, 10 $/mois OpenAI) préservé** — le cumul ~14,69 $ depuis S1 (sur ~7 semaines) reste sous le plafond mensuel. Alerte « crédits prépayés Anthropic » désormais prioritaire : le rythme ~2,85 $/sprint (eval croissante) + le déclencheur vault > 400 chunks rendent **la recharge avant ouverture vague 9 obligatoire**. Pistes d'optimisation coût (Haiku 4.5 sur eval, top-k 3, reranking) à arbitrer dans le sprint S2.9 d'optimisation.

---

## Liste des commits / PR S2.8

| PR | Lot | Acteur |
|---|---|---|
| #102 | A — SPEC v2.2 + BRIEF-CC-S2.8 | Cowork |
| #103 | F.8 + G + H — 5 architectures A1-A4-Hybride + brique pattern-grille + golden set 118q | Cowork |
| #104 | Dev R11 — citation_audit.py + tests + VALIDATION-SCORING + rapport vault | Plateforme |
| #105 | I — eval 118q (104 std + 14 adv) + dump q-083 + vault 444 chunks | Desktop |
| *(ce commit)* | J — RAPPORT + PR finale | Plateforme |

**Suite tests cumulée S1 → S2.8** : 234/234 verts (+28 vs S2.7 = `citation_audit.py`).

---

*Rapport produit le 26 mai 2026 par Claude Code Hub IA Plateforme (Lot J). Format conforme brief CC-S2.8 (8 sections, calque S2.7) + déposé dans `rag-prep/reports/` selon convention Cowork. Sprint S2.8 définitivement clôturé après merge de la PR finale.*

***Finding central** : **robustesse RAG confirmée sur panel élargi (103/104 std + 14/14 adv sur 118q, vault 444 chunks)** + **alerte vault > 400 atteinte → sprint S2.9 dédié optimisation explicitement recommandé**. R11 audit livré et opérationnel (85 manquements détectés, patches Cowork ~30-60 min). Les 3 propositions d'amendement SPEC v2.3 (§6) restent à arbitrer par Cowork après merge.*
