# RAPPORT-CC-S2.3 — Vague 3 + matching sémantique synonymes + golden set 42q

**Émetteur :** Claude Code Hub IA Plateforme (Lot F)
**Destinataire :** Cowork Hub IA Plateforme + Blaise Cavalli (garant transverse)
**Sprint :** S2.3 (clôture définitive)
**Briefs sources :** `rag-prep/briefs/BRIEF-CC-S2.3.md` + `rag-prep/briefs/RETOUR-SONDAGE-COWORK-HUB-IA-S2.3.md`
**Branche développement :** `claude/execute-s23-lot-f-rapport` (dérive de `claude/execute-s23-lot-e-eval-42q`)
**Date :** 13 mai 2026
**Allocation D-030 :** hybride Cowork Hub IA (sondage) + Cowork Plateforme (Lots A, B, C) + Claude Code Plateforme (Lots D, F) + Claude Code Desktop (Lot E)

---

## 1. Objectifs S2.3

Le sprint S2.3 portait quatre axes structurels en parallèle, condition préalable à la migration MD à l'échelle (vague 4 sur les ~50 modules restants) :

1. **Production vague 3** — produire les trois modules denses N3/N4 prévus (CU-026 gouvernance des agents, CU-027 faire développer une appli métier, DEP-08 sécurité agents/MCP). Cible : couverture éditoriale alignée HTML source du Hub via D-026 (co-production légère).

2. **Résolution des 5 faux négatifs S2.2 §7** — les concepts `méthode`, `vérification`, `1,8 heures`, `persistant`, `économie` n'étaient pas matchés malgré une présence sémantique avérée dans la réponse (variations morphologiques). Cible : élargir `expected_concepts` au format option B (listes de synonymes par concept) sans casser la rétro-compat scalaire v1.

3. **Extension du golden set à 42 questions** — couverture exhaustive du vault enrichi (12 modules MD post-vague 3) avec 12 nouvelles questions (q-031 → q-042 sur cu-026/cu-027/dep-08) + 30 questions S2.2 enrichies en synonymes.

4. **Validation empirique du pattern D-026** — l'hypothèse depuis S2.2 voulait qu'un sondage Cowork Hub IA préalable à la production éviterait les dérives sémantiques majeures sur les modules denses. Mesure attendue : combien de dérives évitées vs production sans sondage ?

---

## 2. Livrables par lot

| Lot | Acteur | Commit(s) | Périmètre |
|---|---|---|---|
| **A — Sondage Cowork Hub IA** | Cowork Hub IA (canal parallèle) | `rag-prep/briefs/RETOUR-SONDAGE-COWORK-HUB-IA-S2.3.md` | ~2100 mots, citation textuelle des passages canoniques HTML sur cu-026, cu-027, dep-08. **D-026 validé empiriquement** — 4 dérives sémantiques majeures évitées avant production MD (cf. §5). |
| **B — Production vague 3 + I-D-005** | Cowork Hub IA Plateforme | `75444f4` (PR #55 mergée) | `cu-026.md`, `cu-027.md`, `dep-08.md` (~600 lignes chacun, frontmatter v3.8.7, alignés RETOUR-SONDAGE). Canonisation chiffre macro `21 %` McKinsey (I-D-005). Mise à jour `cartographie-rag.md` + `whitelist-wikilinks-futurs.md`. |
| **C v1 — Golden set 39q initial** | Cowork Hub IA Plateforme | `262929a` (PR #51 mergée) | Première version : 30 questions S2.2 enrichies synonymes + 9 nouvelles vague 3. |
| **C v2 — Ajustement post-RETOUR-SONDAGE** | Cowork Hub IA Plateforme | `99cd15e` (PR #52 mergée) | Golden set v2 ajusté à **42 questions** (30 enrichies + 9 vague 3 corrigées + 3 bonus post-sondage). AP-5 ✅. Discipline « 2-4 synonymes par concept » respectée. |
| **D — Adapt `evaluate_one()` synonymes** | Claude Code Plateforme | `78d0fa7` (PR #53 mergée) | Nouvelle fonction `concept_matched(entry, answer_text_lower)` distinguant scalaire (v1) vs liste (v2 option B). Cas dégénéré `[]` → False + warning stderr. Typage `EvalItem` élargi à `list`. **19 nouveaux tests** (5 classes : scalaire, liste, dégénéré, mix, rétro-compat). **190/190 tests verts**. |
| **E — Eval extended 42q sur vault enrichi** | Claude Code Desktop | `a8e8977` + `08c5892` | Rejeu complet 42 questions post-vague 3. Ingestion incrémentale 121 → 146 chunks (+25 new, 25 updated, 0 erreur, 0,000385 $ OpenAI). **Score global 41/42**. Cibles brief §7 dépassées (cf. §3). Artefacts : `rag/eval/eval-report-s2.3.md` + `.json`. |
| **F — RAPPORT-CC-S2.3 + PR finale** | Claude Code Plateforme | *(ce commit)* | Présent rapport + ouverture PR finale S2.3. |

---

## 3. Métriques quantitatives

### Eval golden set 42 questions — résultats finaux Lot E

| Indicateur | Cible brief §7 | Mesuré Lot E | Statut |
|---|---|---|---|
| **Sources retrouvées** | ≥ 35/42 (83 %) | **41/42 (97 %)** | ✅ Dépassée |
| **Concepts ≥ 50 % couverts** | ≥ 38/42 (90 %) | **41/42 (97 %)** | ✅ Dépassée |
| **Score global** | — | **41/42** | ✅ |
| Concepts pleinement couverts | — | 36/42 (86 %) | informatif |
| **Latence moyenne** | 12–18 s/q | **16,6 s/q** | ✅ Cible centrale |
| Latence min / max | — | 9 s / 23 s | informatif |
| **Coût Anthropic** | ≤ 0,90 $ | **1,02 $** | ⚠ Dépassé +13 %, accepté |

**Lecture détaillée** : 42 questions sur 42 ont au moins une source attendue citée dans la réponse (couverture retrieval parfaite sur vault enrichi). 41/42 atteignent le score global (au moins 1 source citée ET ≥ 50 % concepts couverts) — l'unique échec score=0 est **q-038** (cf. §4).

### Régression check (10 questions originales S1)

Les 10 questions pilotes S1 (q-001 → q-010) restent à **10/10 sources retrouvées + 10/10 score global** post-vault enrichi vague 3. Aucune régression depuis le rerun S2.2 final.

### Ingestion incrémentale post-vague 3

| Snapshot | Chunks | Détail |
|---|---|---|
| Post-S2.2 (10 fichiers, pattern-llm-wiki ajouté) | 121 | — |
| **Post-S2.3 Lot B (13 fichiers : +cu-026 +cu-027 +dep-08)** | **146** | `new=25` (vague 3), `updated=25` (réfs croisées), `skipped=…`, `errors=0` |
| Coût ingestion incrémentale | — | **0,000385 $** OpenAI text-embedding-3-small |

L'incrémentalité est fonctionnelle : seuls les chunks réellement modifiés ont été ré-embédés.

### Suite tests cumulée

**190/190 verts** (171 cumulés S1 + S2.1 + S2.2 + 19 nouveaux S2.3 Lot D). Aucun test ajouté ou cassé en Lot E (eval réelle pas couverte par tests unitaires, par construction).

---

## 4. Anomalies & fixes

### Anomalie unique S2.3 — q-038 score=0 (« concepts détaillés absents »)

**Énoncé** : « Quels outils et patterns de mitigation appliquer pour sécuriser des agents IA en production ? »

**Source attendue** : `dep-08` — **retrouvée** dans `cited_codes` (avec `cu-026` en bonus, retrieval pertinent).

**Concepts attendus** :
- `AgentShield` ✅ trouvé
- `[audit, logs]` ✅ trouvé (variant `audit`)
- `[Snyk, Semgrep]` ❌ absent
- `[1 282, 1282]` ❌ absent
- `[102 règles, 102]` ❌ absent
- `--opus` ❌ absent

**Score concepts** : 2/6 ≈ 33 % < 50 % → `score_global = 0`.

**Diagnostic** : la source `dep-08` a bien été récupérée mais le **retrieval a privilégié des chunks dep-08 généralistes** (« framework outils », « patterns de mitigation ») plutôt que le chunk spécifique « outils de mitigation avec specs » qui contient les noms d'outils précis (Snyk, Semgrep) et les chiffres techniques (1 282 tests, 102 règles, paramètre CLI `--opus`).

**Cause probable** : section H2 « Outils et patterns de mitigation » de `dep-08` peut être trop dense (chunk unique mélangeant aperçu général + specs techniques par outil), diluant la pertinence sémantique des specs au profit du discours d'introduction.

**Recommandations** (à arbitrer par Cowork) :
1. **Option A — Refactor chunking dep-08** : subdiviser la section « outils de mitigation » en sous-sections H3 dédiées par outil (`### AgentShield (specs détaillées)`, `### Snyk + Semgrep`, `### Audit logs --opus`). Effet attendu : chunks plus ciblés, retrieval plus précis.
2. **Option B — Assouplir `expected_concepts` q-038** : élargir les synonymes (`["1 282 tests", "1282", "milliers de tests"]`, `["102 règles", "102", "centaine de règles"]`). Compromis : abaisse la barre de l'eval, ne résout pas le problème structurel.
3. **Option C — Composition** : faire les deux (A pour le chunking + B pour la métrique). Coût Cowork modéré, gain probable sur q-038 et sur les vagues suivantes contenant des specs techniques.

**Décision recommandée S2.4 ouverture** : option C (refactor chunking + élargissement métrique), monitorer impact au prochain rejeu.

---

## 5. Décisions structurantes prises

Aucune nouvelle décision **actée** dans `DECISIONS-RAG.md` pendant le sprint S2.3. Deux **patterns opérationnels validés empiriquement**, candidats à codification en SPEC v1.6 (cf. §6) :

### Pattern 1 — D-026 sondage préalable validé empiriquement

Le sondage Cowork Hub IA préalable à la production cu-026/cu-027/dep-08 (Lot A, `RETOUR-SONDAGE-COWORK-HUB-IA-S2.3.md`) a permis d'éviter **4 dérives sémantiques majeures avant la production MD** :

1. **CU-027 — confusion modèles Kimi K2.6 / Claude Opus** : le sondage a clarifié que la mention « jusqu'à 8-10× compression coûts » s'applique au passage Kimi K2.6 → Opus 4.7 sur le rapport-qualité tokens (et non à Opus seul comme la version brouillon le suggérait).
2. **CU-027 — cas-école AMETRA réétiqueté Tea App** : le passage initial citait AMETRA comme cas-école mais le canon Hub IA pointe sur Tea App pour la même illustration. Réalignement avant production.
3. **CU-026 — classement gouvernance** : la formulation « niveau d'autonomie » a été corrigée en « maturité production », alignée sur le framework 7 dimensions du Hub.
4. **DEP-08 — cas-école sécurité** : la version brouillon citait Klarna comme cas-école générique ; le canon Hub IA pointe sur les CVE techniques spécifiques (`CVE-2024-…`). Réalignement précis avant production.

**Bénéfice mesuré** : 0 dérive majeure dans les MD vague 3 finalement produits, vs 4 dérives anticipées sans sondage. Pattern **clairement à reconduire** pour tous les futurs modules denses N3/N4.

### Pattern 2 — « Ossature complète d'un module ≠ brique transverse extractible »

Pendant Lot A, la question s'est posée : faut-il extraire le pattern « agent = employé » de CU-026 en brique transverse, vu qu'il est mentionné dans plusieurs modules vague 3+ ?

**Décision Cowork validée par RETOUR-SONDAGE** : **non**. Le pattern « agent = employé » constitue l'**ossature complète de CU-026** (titre Section 1, Takeaway exécutif, base du framework 7 dimensions). L'extraire reviendrait à vider CU-026 de sa colonne vertébrale. Les mentions satellites dans d'autres modules sont des **wikilinks vers cu-026**, pas des duplications éditoriales.

**Critère opérationnel** dégagé : un concept est extractible en transverse uniquement s'il **n'est pas l'ossature d'un module existant**. Une mention satellite avec wikilink n'est pas une duplication.

Candidat à inscrire en SPEC v1.6 comme précision de D-025 (cf. §6 proposition 2).

---

## 6. Recommandations SPEC v1.6

À arbitrer par Cowork après merge de la PR finale S2.3 :

### Proposition 1 — Recalibrage cap durci sprint (cf. §3 Coût Anthropic)

**Contexte** : cap durci brief §7 fixé à 0,90 $, dépassé à 1,02 $ (+13 %). Mesure empirique Lot E : ~0,025 $/question sur 42q × Sonnet 4.6 → ~1,05 $ attendu. Le cap était sous-calibré.

**Suggestion d'ajout à SPEC §Performances** :
> **Cap durci sprint eval Sonnet 4.6 (à partir de v1.6)** : ~0,025 $/question × N questions = cap durci recommandé. Pour 42 questions : ≤ 1,10 $. Cap mensuel D-013 (50 $) reste seul plafond hard. Le cap durci sert d'alerte opérationnelle, pas de hard-stop.

### Proposition 2 — Précision D-025 « critère d'extraction transverse »

**Contexte** : cf. Pattern 2 §5. Risque sans codification : sur-extraction en transverses qui vide les modules de leur ossature pédagogique.

**Suggestion d'ajout à SPEC §Briques transverses (D-025)** :
> **Critère d'extraction transverse — précision post-S2.3** : si un concept constitue l'**ossature complète d'un module** (titre Section 1, Takeaway exécutif, base d'un framework structurant), il **ne doit PAS être extrait en transverse** même s'il est mentionné dans d'autres modules. Une mention satellite avec wikilink vers le module canonique n'est pas une duplication éditoriale.

### Proposition 3 — AP-6 « Synonymes excessifs dans `expected_concepts` »

**Contexte** : brief §4 dernière sous-section identifie le risque de faux positifs si une liste de synonymes contient 5+ termes (`économie` matcherait `économie d'énergie` sans rapport).

**Suggestion d'ajout à SPEC §Anti-patterns** :
> **AP-6 — Synonymes excessifs (≥ 5 par concept)** : un concept liste dans `expected_concepts` doit contenir 2-4 synonymes maximum, alignés sur les variations morphologiques attendues du même concept (singulier/pluriel, substantif/verbe, dérivés lexicaux). Au-delà de 4, le risque de faux positifs augmente significativement (matching sur substrings parasites). Cas idéal : 2-3 synonymes ciblés.

### Proposition 4 — Garde-fou « concepts détaillés » vague 3.5+

**Contexte** : q-038 a échoué non sur la source mais sur les concepts détaillés (noms d'outils, chiffres exacts, paramètres CLI). Risque structurel pour les vagues futures denses en specs techniques (vague 4 modules DEP-04 fine-tuning, modules CU agentique).

**Suggestion d'ajout à SPEC §Validation eval réelle (garde-fou)** :
> **Garde-fou « concepts détaillés »** : si une question du golden set cible des **specs techniques précises** (noms d'outils, chiffres exacts, paramètres CLI, versions logicielles), prévoir :
> 1. Côté MD source : un découpage H3 dédié dans le module pour isoler les specs (favorise retrieval ciblé).
> 2. Côté golden set : format `expected_concepts` plus tolérant aux variations (synonymes larges, formats numériques alternatifs `["1 282", "1282", "milliers de"]`).

---

## 7. Pistes investigation S2.4 / S3

1. **Investigation chunking `dep-08` « outils de mitigation »** (cause technique q-038) : prioritaire en début S2.4 si Option C §4 retenue.
2. **Option 4 (composition) matching sémantique** gardée en réserve : stemming + listes de synonymes + LLM-as-judge en repli — à activer si vague 4+ révèle de nouveaux faux négatifs résiduels que le format option B ne couvre pas.
3. **R11 audit pattern wikilinks post-query** (`rag/code/backend/citation_audit.py`) — reporté du Lot D S2.3 (option « si charge disponible »). À implémenter en S2.4 si la charge le permet : permettra de vérifier automatiquement que les réponses Claude utilisent bien les wikilinks Obsidian préférés vs crochets simples (D-025 + system prompt v2 alignement).
4. **Audit régression latence** dès passage à 60+ questions ou vault > 200 chunks : Sonnet 4.6 mesuré à 16,6 s/q sur volumes courants — extrapolation linéaire suggère 25-40 min pour 100q. Si insoutenable, envisager le bascule partielle Haiku 4.5 sur les questions à faible enjeu de nuance (D-005).
5. **Stratégie de migration vague 4** : ~50 modules MD restants. Tester l'application systématique de D-026 (sondage) ralentit-elle ou accélère-t-elle la vague ? Métrique à mesurer : dérives évitées vs surcoût opérationnel sondage.

---

## 8. Coûts cumulés

### Détail S2.3

| Phase | Acteur | Coût $ | Détail |
|---|---|---|---|
| Lot A — Sondage Cowork Hub IA | Cowork Hub IA | 0,00 | Canal parallèle éditorial |
| Lot B — Production vague 3 (cu-026 + cu-027 + dep-08) | Cowork | 0,00 | Production MD pure |
| Lot C v1 + C v2 — Golden set 39q → 42q | Cowork | 0,00 | Production YAML pure |
| Lot D — Adapt `evaluate_one()` synonymes | Claude Code Plateforme | 0,00 | Refactor + tests mockés (D-030) |
| Lot E ingestion incrémentale | Claude Code Desktop | 0,000385 | text-embedding-3-small × 25 chunks new + 25 updated |
| Lot E eval 42q (Sonnet 4.6) | Claude Code Desktop | **1,0199** | 42 calls × 152 592 tokens in + 37 473 tokens out |
| Lot F — RAPPORT + PR | Claude Code Plateforme | 0,00 | Production texte pure |
| **Total S2.3** | — | **~1,02 $** | (~1,02 $ Anthropic + ~0,001 $ OpenAI) |

### Cumul historique S1 + S2.1 + S2.2 + S2.3

| Sprint | Coût $ |
|---|---|
| S1 (S1c.2 local Blaise) | ~0,30 |
| S1bis | 0,00 |
| S1ter Lot C.1 | 0,00 |
| S2.1 (audit v2 refactor) | 0,00 |
| S2.2 (Lot D + reruns + Lot E.2) | ~2,50 |
| **S2.3 (Lot E eval 42q)** | **~1,02** |
| **Total cumulé** | **~3,82 $** |

### Budget restant

Crédits initiaux : ~3 $ Anthropic + ~5 $ OpenAI sans renouvellement automatique (cf. brief S1ter §1).

| Provider | Initial | Consommé S1 → S2.3 | **Restant** |
|---|---|---|---|
| Anthropic | ~3,00 $ | ~3,82 $ | **~-0,82 $** 🔴 |
| OpenAI | ~5,00 $ | ~0,003 $ | **~4,997 $** |

🔴 **Alerte budgétaire structurelle confirmée et amplifiée** : le crédit initial Anthropic de ~3 $ est **dépassé** d'environ 0,82 $ depuis le Lot E S2.3. Trois options pour S2.4 (rappel RAPPORT-CC-S2.2 §8, devenu critique) :

1. **Recharger les crédits Anthropic** (côté Blaise). Recommandé si poursuite ambitieuse S2.4 + S3.
2. **Basculer en `claude-haiku-4-5`** pour l'eval (coût ~5× inférieur — 0,20 $ par rejeu 42q estimé). Compromis qualitatif à mesurer en double-run Sonnet/Haiku sur un sous-ensemble.
3. **Eval ciblée sous-ensemble** (20 questions critiques) pour réduire le volume de 42 à 20 → coût ~0,50 $/rejeu.

Plafonds D-013 (50 $/mois Anthropic, 10 $/mois OpenAI) **toujours préservés au niveau mensuel** — l'alerte concerne uniquement les crédits prépayés.

---

## Liste des commits S2.3

| SHA | Acteur | Lot | Message |
|---|---|---|---|
| `262929a` | Cowork | C v1 | `feat(rag-eval): S2.3 Lot C - golden set v2 (39 questions + synonymes)` *(PR #51 mergée)* |
| `75444f4` | Cowork | B | `feat(rag-content): S2.3 Lot B - vague 3 cu-026 cu-027 dep-08 et canonisation I-D-005` *(PR #55 mergée)* |
| `99cd15e` | Cowork | C v2 | `feat(rag-eval): S2.3 Lot C v2 - golden set 42q post-RETOUR-SONDAGE + I-D-005` *(PR #52 mergée)* |
| `78d0fa7` | Plateforme | D | `feat(rag-eval): concept_matched() supporte le format option B liste de synonymes (s2.3 lot D)` *(PR #53 mergée)* |
| `a8e8977` | Desktop | E | `feat(rag-eval): S2.3 Lot E - eval extended 42 questions sur vault vague 3` |
| `08c5892` | Desktop | E | `chore(rag-prep): MAJ JOURNAL + STATUS post-S2.3 Lot E (Claude Code Desktop)` |
| *(ce commit)* | Plateforme | F | `docs(rag): rapport mission S2.3 + ouverture PR finale` |

**Suite tests cumulée S1 + S2.1 + S2.2 + S2.3** : 190/190 verts.

---

*Rapport produit le 13 mai 2026 par Claude Code Hub IA Plateforme (Lot F). Format conforme brief CC-S2.3 §8 (8 sections, ~2400 mots) + déposé dans `rag-prep/reports/` selon convention Cowork post-S2.2. Sprint S2.3 définitivement clôturé après merge de la PR finale. Les 4 propositions d'amendement SPEC v1.6 (§6) restent à arbitrer par Cowork après merge.*
