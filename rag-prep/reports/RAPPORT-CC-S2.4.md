# RAPPORT-CC-S2.4 — Vague 4 + pattern-persistent-memory + golden set 52q + fix retrieval q-038

**Émetteur :** Claude Code Hub IA Plateforme (Lot J)
**Destinataire :** Cowork Hub IA Plateforme + Blaise Cavalli (garant transverse)
**Sprint :** S2.4 (clôture définitive)
**Brief source :** `rag-prep/briefs/BRIEF-CC-S2.4.md` + sondage `RETOUR-SONDAGE-COWORK-HUB-IA-S2.4.md`
**Branche développement :** `claude/execute-s24-lot-j-rapport` (depuis `main` post-merge PR #71)
**Date :** 19 mai 2026
**Allocation D-030 :** hybride Cowork Hub IA (sondage 11 sous-passages) + Cowork Plateforme (Lots A, B, C, E, F.1-F.4, G, H) + Claude Code Plateforme (Lot J) + Claude Code Desktop (Lots D, I)

---

## 1. Objectifs S2.4

Le sprint S2.4 portait quatre axes coordonnés, condition d'élargissement de la base vault et de fiabilisation pré-vague 5 :

1. **Production vague 4 ciblée** — extraire la deuxième brique transverse (`pattern-persistent-memory.md`), refactorer cu-008 et dep-02 pour réintégrer cette brique par wikilinks, patcher cu-026/cu-027/dep-08 (chiffres Frontier Firms, Stanford, SBOM IA), et **créer le nouveau module PR-08 « Financer son projet IA en 2026 »** (extraction depuis pr-07 sur l'angle financement spécifique).

2. **Canonisation v3.9.0 des chiffres macro du Hub** — la migration v3.10 du Hub HTML a introduit 28 nouveaux chiffres macro. Mise à jour `chiffres-macro-2026.md` en un seul bump éditorial groupé (pattern testé S2.4 — voir §5).

3. **Fix retrieval q-038** — anomalie S2.3 unique (concepts détaillés Snyk/Semgrep/1 282/102/--opus absents). Option C recommandée par RAPPORT-CC-S2.3 §4 retenue : refactor chunking dep-08 + élargissement métrique synonymes. Objectif : q-038 0 → score=1 sans casser les autres questions dep-08.

4. **Extension golden set 42 → 52 questions** — couvrir les 5 nouveaux modules + le pr-08 nouveau-né + le pattern-persistent-memory, avec une discipline AP-6 plafond 4 synonymes par concept (SPEC v1.6).

---

## 2. Livrables par lot

| Lot | Acteur | Commit(s) | Périmètre |
|---|---|---|---|
| **A — SPEC v1.6** | Cowork | (intégré pré-S2.4 post-merge S2.3) | 4 propositions S2.3 actées : recalibrage cap durci 1,35 $, précision D-025 critère extraction, AP-6 synonymes excessifs, garde-fou concepts détaillés. |
| **B — Canonisation 28 chiffres v3.9.0** | Cowork | (commits série S2.4 phase 1) | `chiffres-macro-2026.md` bump v3.8.6 → v3.9.0 en un seul commit éditorial groupé. Pattern « bump multi-items » validé empiriquement. |
| **C — Fix chunking dep-08** | Cowork | (commits série S2.4 phase 1) | Sous-section H3 dédiée pour specs Snyk/Semgrep/1 282 tests/102 règles/`--opus`. Pattern Lot D-ter validé par 3 itérations Desktop. |
| **D — Rerun ciblé q-038 (3 itérations)** | Desktop | `rag/eval/eval-report-s2-4-1.md` + `.json` | 3 reruns successifs : q-038 0 → score=1 progressivement, validation pattern « chunking H2 autonome + lead bridge enrichi ». |
| **E — Sondage Cowork Hub IA D-026** | Cowork Hub IA (canal parallèle) | `rag-prep/briefs/RETOUR-SONDAGE-COWORK-HUB-IA-S2.4.md` | 11 sous-passages canoniques. Rectification critique DEP-02 §3.4 : 2 tableaux distincts (principal §4 + mini-tableau §3bis), **non fusionnables** comme initialement envisagé. |
| **F.1 — pattern-persistent-memory** | Cowork | `(commits série phase 2)` | Nouvelle brique transverse extraite (D-025). Recouvrement cu-008 ↔ dep-02 confirmé en sondage. |
| **F.2 — Refactor cu-008 + dep-02** | Cowork | `2b69f27` (PR #69 mergée) | Réintégration pattern-persistent-memory par wikilinks. Chunk Frontier Firms cu-026 à 850 tokens (validé empiriquement OK — voir §5). |
| **F.3 — Patches cu-026 + cu-027 + dep-08** | Cowork | (commits série phase 2) | Frontier Firms (cu-026), Stanford State of AI (cu-027), SBOM IA + outils mitigation (dep-08). |
| **F.4 — Nouveau module PR-08** | Cowork | `b7ae867` | « Financer son projet IA en 2026 » créé depuis l'angle financement spécifique de pr-07. Sondage D-026 préalable validé. |
| **G — Cartographie v1** | Cowork | `4158fce` (PR #70 mergée) | `cartographie-rag.md` v1 enrichie post-vague 4 + entrée pr-08 + entrée pattern-persistent-memory + correction recouvrements. |
| **H — Golden set 52q** | Cowork | `4158fce` (PR #70 mergée) | Extension 42 → 52 questions (+10 nouvelles q-043 → q-052 couvrant les 5 nouveaux MD vague 4 + pattern-persistent-memory + pr-08). Discipline AP-6 respectée. |
| **I — Eval extended 52q** | Desktop | `96e4dcc` (PR #71 mergée) | Rejeu complet 52 questions post-vault vague 4. **Score 50/52 (96 %)**. **10/10 nouvelles q-043 → q-052 score=1**. 2 régressions S2.3 identifiées (q-002, q-030). Latence 16,5 s/q. Coût 1,2785 $ Anthropic. |
| **J — RAPPORT + PR finale** | Plateforme | *(ce commit)* | Présent rapport + ouverture PR finale S2.4. |

---

## 3. Métriques quantitatives

### Eval golden set 52 questions — résultats finaux Lot I

| Indicateur | Cible SPEC v1.6 | Mesuré Lot I | Statut |
|---|---|---|---|
| **Sources retrouvées** | ≥ 44/52 (≈ 85 %) | **50/52 (96 %)** | ✅ Dépassée |
| **Concepts ≥ 50 % couverts** | ≥ 44/52 (≈ 85 %) | **50/52 (96 %)** | ✅ Dépassée |
| **Score global** | — | **50/52 (96 %)** | ✅ |
| Concepts pleinement couverts | — | 44/52 (85 %) | informatif |
| **10/10 nouvelles vague 4** | viser 100 % | **10/10 (100 %)** | ✅ |
| **Latence moyenne** | 12–18 s/q | **16,5 s/q** | ✅ Cible centrale |
| **Coût Anthropic** | ≤ 1,35 $ (cap SPEC v1.6 recalibré) | **1,2785 $** | ✅ Respecté |

### Régression check q-038 S2.3

Le score=0 de q-038 S2.3 est devenu **score=1 maintenu en S2.4** après le pattern Lot D-ter (chunking H2 autonome dep-08 §outils-mitigation + lead bridge enrichi). Le fix structurel s'est révélé efficace dans la durée — pas de retour en arrière sur 3 reruns successifs ni sur le rerun final 52q.

### Régressions S2.3 identifiées en Lot I

Deux questions précédemment passantes en S2.3 ont basculé en échec :

- **q-002** (« Sources fiables pour suivre l'actualité IA générative en 2026 ? ») — source attendue `cu-001` **manquante**, retrieval cite à la place `chiffres-macro-2026 / pr-08 / cu-026`. Le pr-08 nouveau-né est rappelé sur la question « actualité IA générative » alors que la source canonique reste cu-001.
- **q-030** (« Obligations réglementaires à anticiper pour un projet IA en PME en 2026 ? ») — sources attendues `pr-07 + vigilance-confidentialite` **toutes manquantes**, retrieval cite uniquement `pr-08`. Le top-5 est saturé par pr-08 sur les questions transversales « projet IA 2026 PME ».

**Diagnostic Desktop** : effet de bord de la création du module pr-08 — son **lead bridge** (premier paragraphe et chunk frontmatter) est trop accrocheur sur le vocabulaire « projet IA 2026 PME », saturant le retrieval top-5 sur des questions plus génériques. Voir §4 et §6 (proposition AP-7).

### Vault et ingestion incrémentale

| Snapshot | Fichiers MD | Chunks |
|---|---|---|
| Post-S2.3 (vague 3 mergée) | 13 | 146 |
| **Post-S2.4 (vague 4 mergée)** | **15** | **~155** |

+2 fichiers (`pattern-persistent-memory.md`, `pr-08.md`), ~9 chunks nets ajoutés (le refactor cu-008/dep-02 a réduit certaines sections compensant les ajouts). Ingestion incrémentale 100 % fonctionnelle.

### Suite tests cumulée

**190/190 verts** (inchangé depuis S2.3 — aucun nouveau test Plateforme en S2.4 ; le matching synonymes liste de listes était déjà couvert par les 19 tests S2.3 Lot D, et Lot I est de l'exécution réelle non couverte par unit tests).

---

## 4. Anomalies & observations

### Anomalie #1 — Régression q-002 (`cu-001` évincée par pr-08)

**Symptôme** : q-002 demande `cu-001` (sources fiables veille IA), pr-08 est retrouvé à la place dans le top-5. Concepts `source` + `veille` matchés malgré tout, mais score=0 (source attendue manquante).

**Cause** : le lead bridge de pr-08 (chunk frontmatter + introduction) contient les mots clés « actualité IA générative » et « 2026 » qui matchent l'embedding de la question. Le retrieval privilégie pr-08 (chunk plus récent ou plus dense en mots clés query) au détriment de cu-001 qui couvre pourtant la sémantique de la veille.

### Anomalie #2 — Régression q-030 (saturation top-5 par pr-08)

**Symptôme** : q-030 demande `pr-07 + vigilance-confidentialite` (obligations réglementaires projet IA PME 2026), top-5 saturé par pr-08, **aucune** des deux sources attendues récupérée. Concepts RGPD/AI Act/conformité matchés (la réponse Claude reste pertinente) mais score=0 sur sources.

**Cause** : même phénomène — pr-08 est trop accrocheur sur la combinaison « projet IA + PME + 2026 ». La saturation top-5 (chunks 1–5 tous pr-08) prive le retrieval des sources transversales pr-07 et vigilance-confidentialite.

### Recommandations (à arbitrer Cowork)

- **Lot S2.5.0 correctif retrieval** : restreindre éditorialement le lead de pr-08 (focus financement spécifique, retirer les généralités « projet IA 2026 PME ») + enrichir les leads de cu-001 et pr-07 pour rétablir l'équilibre concurrentiel sur les questions transversales.
- Alternative : `query.py` top-k=8 au lieu de 5 pour réduire mécaniquement la saturation top-5 (compromis : coût Anthropic par question augmenté, latence aussi).
- Compromis Plateforme : Option A (refactor lead pr-08) **recommandée** — préserve top-k=5 + latence + coût + corrige la cause racine.

### Observation #1 — Chunk Frontier Firms cu-026 à 850 tokens

Le chunk « Frontier Firms » ajouté à cu-026 mesure **850 tokens**, au-dessus du seuil 800 tokens documenté en SPEC §R3. Aucune dégradation retrieval mesurée sur les questions cu-026. Validation empirique : **tolérance jusqu'à ~900 tokens** acceptable si le chunk reste **thématiquement cohérent** (pas de glissement vers deux sujets différents). Voir §6 (proposition tolérance R3).

### Observation #2 — 6 questions à concepts partiels

6 questions atteignent score=1 (≥ 50 % concepts couverts) sans atteindre 100 % de couverture. Pas d'action requise — comportement attendu de l'eval intermédiaire (≥ 50 % suffit pour score=1), les concepts manquants sont des nuances secondaires.

---

## 5. Décisions structurantes prises pendant S2.4

Aucune décision **actée** Git-side en S2.4 (D-025 / D-026 / SPEC v1.6 stables). En revanche, **5 patterns opérationnels validés empiriquement** pendant le sprint, candidats à codification en SPEC v1.7 / v1.8 :

### Pattern 1 — Lot D-ter (chunking H2 autonome + lead bridge enrichi)

**Contexte** : q-038 S2.3 score=0 (concepts détaillés Snyk/Semgrep/1 282/102/--opus absents). Recommandation S2.3 §4 Option C retenue.

**Pattern appliqué** : (1) subdiviser le H2 « outils de mitigation » en sous-sections H3 dédiées par outil (`### AgentShield`, `### Snyk + Semgrep`, `### Audit logs --opus`), (2) enrichir le lead du H2 parent (lead bridge) pour conserver le contexte transverse.

**Résultat** : q-038 0 → score=1 en 3 reruns Desktop. Pattern validé pour les modules à specs techniques denses. Reconductible en S2.5+.

### Pattern 2 — « Bump éditorial groupé multi-items »

**Contexte** : 28 chiffres macro v3.10 à canoniser. Tentation d'un commit par chiffre (28 commits) écartée.

**Pattern appliqué** : un seul bump éditorial groupé `v3.8.6 → v3.9.0` couvrant les 28 chiffres en un commit, avec une note de version structurée dans `chiffres-macro-2026.md`. Atomicité éditoriale préservée, historique git lisible.

**Justification** : lecture historique facilitée (1 entrée vs 28), audit de cohérence facilité (les 28 chiffres sont en une seule revue), rétro-compat préservée (numéro de version Hub v3.10 → frontmatter v3.9.0 par convention).

### Pattern 3 — « 2 tableaux distincts dans un même module »

**Contexte** : DEP-02 §3.4 contenait à l'origine un seul tableau de décision RAG vs LLM Wiki. Le sondage E (RETOUR-SONDAGE-COWORK-HUB-IA-S2.4.md) a révélé que le HTML canonique contient en réalité **2 tableaux distincts** : tableau principal §4 (corpus → architecture) + mini-tableau §3bis (volume → modèle).

**Pattern appliqué** : maintenir les 2 tableaux séparés dans le MD (et non les fusionner comme initialement envisagé). Argument décisif : chaque tableau répond à une question différente, fusion = perte de granularité retrieval.

### Pattern 4 — « Ossature complète d'un module ≠ brique transverse extractible » (D-025 SPEC v1.6 validé)

**Contexte** : pattern « agent = employé » de CU-026, déjà signalé en S2.3 et inscrit en SPEC v1.6 (Proposition 2 S2.3 actée).

**Pattern appliqué** : confirmation à l'usage que ce pattern reste l'ossature de cu-026 et **n'est pas extrait** en transverse. Les mentions satellites dans d'autres modules sont des wikilinks vers cu-026.

**Statut** : D-025 SPEC v1.6 validé en 2e application empirique.

### Pattern 5 — 2e application D-026 (sondage préalable) validée empiriquement

**Contexte** : sondage Cowork Hub IA préalable à la production vague 4 (Lot E, 11 sous-passages canoniques).

**Bénéfice mesuré** : 2e validation empirique du pattern après S2.3 (4 dérives évitées). Cette fois : **rectification critique DEP-02 §3.4 — 2 tableaux non fusionnables**, qui aurait nécessité une revue corrective coûteuse en post-production sans sondage. Pattern reconductible systématiquement pour vague 5+.

---

## 6. Recommandations SPEC v1.8 (à arbitrer Cowork)

À arbitrer par Cowork après merge de la PR finale S2.4 :

### Proposition 1 — AP-7 « Lead bridge sur-élargi »

**Contexte** : §4 anomalies #1 et #2 — le lead bridge de pr-08 est trop accrocheur sur les généralités « projet IA 2026 PME », saturant le retrieval top-5 sur des questions transversales et évinçant les sources canoniques (cu-001, pr-07, vigilance-confidentialite).

**Symétrie inverse du garde-fou « concepts détaillés » de SPEC v1.6** : là où le garde-fou v1.6 demandait de **densifier** les sections à specs précises pour améliorer le retrieval ciblé, AP-7 demande de **restreindre** le lead bridge sur les modules à thématique spécifique (pr-08 = financement IA, pas généralités IA PME).

**Suggestion d'ajout à SPEC §Anti-patterns** :
> **AP-7 — Lead bridge sur-élargi** : le premier paragraphe (lead bridge) d'un module thématiquement spécifique doit refléter sa **spécificité éditoriale** et non des généralités du Hub IA. Un lead trop accrocheur sur du vocabulaire générique (« projet IA », « PME 2026 », « actualité IA générative ») provoque une saturation du retrieval top-5 et évince les sources canoniques sur les questions transversales. Symétrie inverse du garde-fou « concepts détaillés » SPEC v1.6 (densifier les specs précises vs restreindre les généralités).

### Proposition 2 — Tolérance seuil 800 tokens SPEC §R3 jusqu'à ~900

**Contexte** : §4 observation #1 — chunk Frontier Firms cu-026 mesuré à 850 tokens, aucune dégradation retrieval mesurée.

**Suggestion d'ajout à SPEC §R3 (chunking)** :
> **Tolérance seuil 800 tokens** : le seuil canonique reste 800 tokens (objectif éditorial). Tolérance jusqu'à ~900 tokens **acceptable** si le chunk reste **thématiquement cohérent** (un seul sujet, pas de glissement narratif). Validation empirique : chunk « Frontier Firms » cu-026 (850 tokens) sans dégradation retrieval mesurée S2.4. Au-delà de 900 tokens : refactoring obligatoire en H3 (cf. SPEC §R3 originale).

### Proposition 3 — Codification « production from scratch avec sondage D-026 systématique »

**Contexte** : 2e application D-026 validée empiriquement (Pattern 5 §5). Le sondage préalable a maintenant fait ses preuves sur 2 sprints consécutifs (S2.3 = 4 dérives évitées, S2.4 = 1 rectification critique non triviale).

**Suggestion d'ajout à SPEC §D-026 (co-production légère)** :
> **Pattern « production from scratch avec sondage D-026 systématique »** : pour tout module produit **from scratch** en vague 5+ (pas de version HTML canonique préexistante au moment de l'extraction MD), le sondage Cowork Hub IA préalable devient **systématique** (et non plus optionnel). Justification : 2 sprints consécutifs (S2.3, S2.4) ont validé que le sondage évite 1 à 4 dérives sémantiques majeures par module dense, à un coût opérationnel modéré (Cowork Hub IA canal parallèle).

---

## 7. Pistes investigation S2.5

1. **Lot S2.5.0 correctif retrieval pr-08 saturation** — Option A recommandée (refactor lead pr-08 + enrichissement leads cu-001/pr-07). Objectif : q-002 + q-030 → score=1 sans casser les questions financement pr-08 légitimes (q-046, q-047 si applicables).
2. **Lot F.5 production 7 modules whitelistés** (CU-020/CU-024/DEP-01/DEP-05/DEP-07/PR-01/PR-04/PR-05) — initialement prévu en S2.4, reporté en S2.5 dédié pour préserver la qualité éditoriale sondage D-026. Avec D-026 systématique post-S2.4 (Proposition 3 §6), volume modéré (7 modules × ~1 h sondage = ~7 h Cowork Hub IA en canal parallèle).
3. **R11 audit pattern wikilinks post-query** (`rag/code/backend/citation_audit.py`) — toujours reporté depuis S2.3 Lot D (option « si charge disponible »). À implémenter en S2.5 si charge le permet : permettra de vérifier automatiquement que les réponses Claude utilisent bien les wikilinks Obsidian préférés vs crochets simples.
4. **Audit régression latence** — à activer dès passage à 60+ questions ou vault > 200 chunks (cf. SPEC v1.6 §Performances). Extrapolation linéaire actuelle : 16,5 s/q × 60 = 16,5 min eval, encore gérable. À 100 questions : ~28 min, à monitorer.
5. **Audit budget Anthropic** — décision critique S2.4 du précédent rapport (RAPPORT-CC-S2.3 §8) **partiellement résolue** : le cap SPEC v1.6 recalibré à 1,35 $ a été respecté en S2.4 (1,2785 $). Mais le cumul depuis S1 (~5,10 $) dépasse le crédit initial de ~3 $. Trois options toujours sur la table : recharge / Haiku 4.5 / eval ciblée.

---

## 8. Coûts cumulés S1 → S2.4

### Détail S2.4

| Phase | Acteur | Coût $ |
|---|---|---|
| Lot A — SPEC v1.6 | Cowork | 0,00 |
| Lot B — Canonisation 28 chiffres v3.9.0 | Cowork | 0,00 |
| Lot C — Fix chunking dep-08 | Cowork | 0,00 |
| Lot D — Rerun ciblé q-038 (3 itérations) | Desktop | ~0,15 (estimé) |
| Lot E — Sondage Cowork Hub IA | Cowork Hub IA | 0,00 |
| Lot F.1 — pattern-persistent-memory | Cowork | 0,00 |
| Lot F.2 — Refactor cu-008 + dep-02 | Cowork | 0,00 |
| Lot F.3 — Patches cu-026/cu-027/dep-08 | Cowork | 0,00 |
| Lot F.4 — Nouveau module PR-08 | Cowork | 0,00 |
| Lot G — Cartographie v1 | Cowork | 0,00 |
| Lot H — Golden set 52q | Cowork | 0,00 |
| **Lot I — Eval extended 52q** | **Desktop** | **1,2785** Anthropic + ~0,001 OpenAI |
| Lot J — RAPPORT + PR (ce commit) | Plateforme | 0,00 |
| **Total S2.4** | — | **~1,28 $** |

### Cumul historique S1 → S2.4

| Sprint | Coût $ Anthropic | Coût $ OpenAI |
|---|---|---|
| S1 (S1c.2 local Blaise) | ~0,30 | ~0,001 |
| S1bis | 0,00 | 0,00 |
| S1ter | 0,00 | 0,00 |
| S2.1 (audit v2 refactor) | 0,00 | 0,00 |
| S2.2 (Lot D + reruns + Lot E.2) | ~2,50 | ~0,001 |
| S2.3 (Lot E eval 42q) | ~1,02 | ~0,001 |
| **S2.4 (Lot D rerun + Lot I eval 52q)** | **~1,28** | **~0,001** |
| **Total cumulé S1 → S2.4** | **~5,10 $** | **~0,005 $** |

### Budget restant

| Provider | Initial | Consommé S1 → S2.4 | **Restant** |
|---|---|---|---|
| Anthropic | ~3,00 $ (crédits prépayés) | ~5,10 $ | **~-2,10 $** 🔴 |
| OpenAI | ~5,00 $ | ~0,005 $ | **~4,995 $** |

🔴 **Alerte budgétaire confirmée et amplifiée vs S2.3** : crédits initiaux Anthropic dépassés de ~2,10 $ depuis le Lot I S2.4. **Décision pour S2.5 devient impérative** (rappel critique RAPPORT-CC-S2.3 §8 + RAPPORT-CC-S2.2 §8) :

1. **Recharger les crédits Anthropic** (recommandé si S2.5 ambitieux + S3 widget public).
2. **Basculer en `claude-haiku-4-5`** pour l'eval future (coût ~5× inférieur → 0,25 $ par rejeu 52q estimé).
3. **Eval ciblée sous-ensemble** (20-25 questions critiques) → coût ~0,60 $/rejeu.

**Plafonds D-013 (50 $/mois Anthropic, 10 $/mois OpenAI) toujours préservés au niveau mensuel** — l'alerte concerne uniquement les crédits prépayés.

---

## Liste des commits S2.4

| SHA | Acteur | Lot | Message |
|---|---|---|---|
| (séries pré-merge) | Cowork | A + B + C | SPEC v1.6 + canonisation v3.9.0 + fix chunking dep-08 |
| `b7ae867` | Cowork | F.4 | `feat(rag-content): S2.4 Lot F.4 - nouveau module PR-08 Financer son projet IA en 2026` |
| `2b69f27` | Cowork | F.2 | `Merge pull request #69 from LumenBot/claude/execute-s242-lot-f2-refactor-cu008-dep02` (refactor cu-008 + dep-02) |
| `4158fce` | Cowork | G + H | `feat(rag): S2.4 Phase 3 Lots G + H - cartographie v1 + golden set 52q` *(PR #70 mergée)* |
| `f91deea` | Cowork | G + H | `Merge pull request #70 from LumenBot/claude/execute-s243-lots-g-h-v2` |
| `248b47c` | Cowork | G + H | `fix(rag-prep): clean STATUS doublon header post-merge PR #70` |
| `96e4dcc` | Desktop | I | `feat(rag-eval): S2.4 Phase 3 Lot I - eval 52q score 50/52 (96%), cibles depassees` |
| `d4b4e3e` | Desktop | I | `Merge pull request #71 from LumenBot/claude/execute-s24-lot-i-eval-52q` |
| *(ce commit)* | Plateforme | J | `docs(rag): rapport mission S2.4 + ouverture PR finale` |

**Suite tests cumulée S1 + S2.1 + S2.2 + S2.3 + S2.4** : 190/190 verts (aucun nouveau test Plateforme en S2.4 — la mécanique synonymes liste de listes était déjà couverte par les 19 tests S2.3 Lot D, et Lot I est de l'exécution réelle non couverte par unit tests).

---

*Rapport produit le 19 mai 2026 par Claude Code Hub IA Plateforme (Lot J). Format conforme brief CC-S2.4 §F.J (8 sections, ~2700 mots) + déposé dans `rag-prep/reports/` selon convention Cowork post-S2.2 / S2.3. Sprint S2.4 définitivement clôturé après merge de la PR finale. Les 3 propositions d'amendement SPEC v1.8 (§6) restent à arbitrer par Cowork après merge. Décision budgétaire Anthropic impérative en début S2.5.*
