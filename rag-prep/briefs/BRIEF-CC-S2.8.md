# BRIEF-CC-S2.8 — Lot Dev R11 audit + Production vague 8 (4 architectures A1-A4) + +2 questions adv + SPEC v2.2

**Émetteur :** Cowork Hub IA Plateforme
**Destinataire :** Claude Code Plateforme (Lot Dev R11 + Lot J), Claude Code Desktop (Lot I eval), Cowork Hub IA (sondage D-026 obligatoire)
**Garant transverse :** Blaise Cavalli
**Sprint :** S2.8 (post-clôture S2.7 — **double validation 96/96 standard + 12/12 adversarial = robustesse RAG confirmée**, vault 31 MD / ~380 chunks, latence p50 19 s / p90 22 s, coût cumulé S1→S2.7 ~11,84 $)
**Date de cadrage :** 25 mai 2026
**SPEC en vigueur :** **v2.2** (produite Cowork-side simultanément à ce brief, sync ascendante en début de sprint)
**Allocation D-030 :** hybride **Plateforme Lot Dev R11** (code citation_audit.py — récurrence pattern Lot Dev S2.7 mode adversarial) + Cowork (Lots A à F + G/H) + Cowork Hub IA (sondage D-026) + Claude Code Desktop (Lots Drer + I eval) + Claude Code Plateforme (RAPPORT-CC-S2.8)

---

## 1. Décisions Blaise validées (25 mai 2026)

1. **SPEC v2.2** — 3 propositions Plateforme validées et produites Cowork-side : validation manuelle obligatoire d'une nouvelle règle de scoring + pattern « citer pour expliquer le manque » = refus correct codifié + extension golden set adversarial systématique ~2 questions/vague.
2. **S2.8 sprint hybride triple axe** — (a) Lot Dev R11 citation_audit.py (Plateforme) ; (b) Production vague 8 = 4 architectures A1-A4 (Cowork) ; (c) +2 questions adversariales selon rythme SPEC v2.2.
3. **Activation R11** — seuil 5+ fichiers `outils-*.md` franchi en S2.7 (6 fichiers total : outils-vector-db S1 + 5 fiches vague 7). R11 « outil glossarié doit wikilinker vers sa fiche » devient implémentable.
4. **Alerte vault > 400 chunks** : si Lot I S2.8 mesure vault > 400 chunks (projection ~420-440 chunks avec 4 architectures denses), **recommandation explicite sprint S2.9 dédié optimisation** (reranking / Haiku 4.5 sur eval / top-k réduction 5→3).

## 2. Objectifs S2.8

Trois axes structurants :

1. **Activation R11 audit wikilinks outils glossariés** (Lot Dev) : extension `rag/code/audit/citation_audit.py` — pour chaque outil mentionné dans un MD du vault qui a sa propre fiche `outils-*.md`, vérifier qu'il est wikilinké à sa première occurrence dans le MD. Reporting des manquements (mentions outils en clair sans wikilink). Effort Plateforme ~2-3h dev + tests.

2. **Production vague 8 — 4 architectures A1-A4** (Lot F.8) : 4 fiches `architecture-*.md` selon RETOUR-SONDAGE-S2.8 — A1 SaaS propriétaire, A2 Propriétaire managé EU, A3 Open-source cloud souverain, A4 Open-source on-premise. Application stricte SPEC v2.2.

3. **Extension golden set vague 8 + +2 adv** (Lot H) : +6-8 questions standards sur les 4 architectures (q-097 à q-104) + +2 questions adversariales (q-adv-013 + q-adv-014) selon SPEC v2.2 §rythme. Cible total 102-104 standards + 14 adversariales.

**Cible eval finale S2.8** :
- **Standard** : ≥ 95/104 sources retrouvées (≥ 91 %), ≥ 96/104 concepts ≥ 50 % couverts (≥ 92 %), score global ≥ 96/104
- **Adversarial** : ≥ 12/14 refus corrects (≥ 86 %)
- **Latence** : standard p50 ≤ 22 s / p90 ≤ 26 s (cible SPEC v2.1 §Performances vault 300-400 chunks, bordure haute), adversarial p50 ≤ 12 s / p90 ≤ 17 s
- **Coût total** : ≤ 2,80 $ Anthropic (cap durci recalibré pour 104q standards + 14 adv)

## 3. Lots S2.8 — allocation hybride D-030

| Lot | Acteur | Périmètre | Dépendance | Effort |
|---|---|---|---|---|
| **A** | Cowork | SPEC v2.2 déjà produite + sync ascendante (commit Git par Blaise via Desktop) | — | 5 min (sync) |
| **B** | Cowork → Cowork Hub IA | **Sondage D-026 global vague 8** (1 session unique, 4 architectures) | A clôturé | 1h Cowork + 60-90 min Cowork Hub IA |
| **Dev R11** | Plateforme | Extension `rag/code/audit/citation_audit.py` — règle R11 (outil glossarié → wikilink obligatoire) + tests unitaires + **VALIDATION-SCORING-S2.8 obligatoire** (5 cas représentatifs, SPEC v2.2 §Validation manuelle) | A clôturé | 2-3h dev + tests + validation |
| **F.8** | Cowork | Production vague 8 — 4 architectures MD selon RETOUR-SONDAGE-S2.8 (A1 SaaS / A2 Managé EU / A3 OS Cloud Souverain / A4 OS On-premise). Application stricte SPEC v2.2 | B clôturé (RETOUR-SONDAGE reçu) | 5-7h Cowork éditorial |
| **G** | Cowork | Whitelist v6 (retrait 4 codes architectures) + cartographie v5 (inventaire vague 8) + glossaire (termes nouveaux si besoin) | F.8 clôturé | 30 min |
| **H** | Cowork | Extension golden set vague 8 : +6-8 questions standards q-097 à q-104 + +2 questions adversariales q-adv-013 + q-adv-014 (codification SPEC v2.2 §rythme +2/vague) | F.8 clôturé | 1h Cowork |
| **I** | Claude Code Desktop | Eval extended ~104 standards + ~14 adversariales sur vault post-vague 8 (vault 31 → 35 fichiers MD, ~380 → ~420-440 chunks). Cap durci ~2,80 $ Anthropic. **+ Mesure latence p50/p90** sur les 2 modes + **alerte vault > 400 chunks** si franchi | F.8 + H + Dev R11 clôturés | 30-35 min |
| **J** | Claude Code Plateforme | RAPPORT-CC-S2.8 (8 sections format S2.7) + PR finale S2.8 — focus **interprétation latence vault > 400 chunks** + bilan R11 audit (combien de manquements détectés, propositions de patch) | I clôturé | 30 min |

**Cap durci sprint S2.8** : ~2,80 $ Anthropic (Lot I uniquement, R11 dev = 0 $). Conforme SPEC v2.1 §Performances (100-110q ≈ 2,60-2,70 $ + adv 14q ≈ 0,28 $ = 2,90 $ avec marge).

## 4. Spécification Lot Dev R11 — Audit wikilinks outils glossariés (citation_audit.py)

### 4.1 Cible fonctionnelle

Étendre `rag/code/audit/citation_audit.py` (à créer ou compléter selon état actuel) pour implémenter la règle R11 :

> **R11** : tout outil ayant sa propre fiche `outils-*.md` dans le vault, lorsqu'il est mentionné dans un autre MD, doit être **wikilinké à sa première occurrence** dans ce MD (ex. première mention « Mistral » dans `pr-05.md` doit être `[[outils-llm#mistral]]` ou `[[outils-llm|Mistral]]` au moins une fois dans le fichier).

### 4.2 Algorithme proposé

1. Parser tous les fichiers `rag/content/ressources/outils-*.md` pour extraire la liste canonique des outils (par section H2 par outil).
2. Pour chaque autre MD du vault (`rag/content/modules/`, `rag/content/prealables/`, `rag/content/deploiement/`, `rag/content/transverses/`), parcourir le texte en cherchant les mentions d'outils.
3. Pour la **première occurrence** de chaque outil dans le MD : vérifier qu'elle est dans un wikilink valide.
4. Reporter au format JSON + Markdown les MD avec mentions d'outils sans wikilink.

### 4.3 Format de reporting attendu

```markdown
## R11 audit — wikilinks outils glossariés

| Fichier MD | Outil mentionné | Première occurrence (ligne) | Wikilink présent ? | Recommandation |
|---|---|---|---|---|
| pr-05.md | Mistral | L42 | ❌ Non | Ajouter `[[outils-llm|Mistral]]` à la première occurrence |
| dep-05.md | Langfuse | L67 | ✅ Oui (L67) | OK |
| ... | ... | ... | ... | ... |

**Total** : X mentions outils détectées, Y manquements (Z %)
```

### 4.4 VALIDATION-SCORING-S2.8 obligatoire (SPEC v2.2)

Avant rejeu eval complet Lot I, produire `briefs/VALIDATION-SCORING-S2.8-R11.md` avec :
- **3 cas attendus positifs** : MD avec mention wikilinkée correctement → R11 doit retourner OK
- **2 cas attendus négatifs** : MD avec mention en clair sans wikilink → R11 doit signaler manquement

### 4.5 Reporting

Le rapport `audit-md-rag-R11-s2.8.md` doit lister les manquements + recommandations de patch. Cowork intégrera les patches en fin de sprint ou les déférera S2.9 selon volume.

### 4.6 Effort estimé

2-3h dev + tests unitaires + validation. Coût Anthropic dev = 0 $ (pas d'eval pendant le dev).

## 5. Spécification Lot B — Sondage D-026 global vague 8

**Format** : 1 fichier `briefs/DRAFT-SONDAGE-COWORK-HUB-IA-S2.8-VAGUE-8.md` (~1500-2000 mots, ~8-12 sous-passages sensibles répartis sur 4 architectures).

### 5.1 Périmètre des 4 architectures vague 8

| Architecture | Description hypothèse | Sensibilité |
|---|---|---|
| **A1 — SaaS propriétaire** | Stack 100 % SaaS (Claude API + Pinecone + LangSmith + outils mainstream US). Cible PME tech non-souveraine | Moyenne |
| **A2 — Propriétaire managé EU** | Stack propriétaire mais hébergement EU (Mistral La Plateforme + OVHcloud + Outscale) | **Haute** (intersection souveraineté + propriétaire) |
| **A3 — Open-source cloud souverain** | Stack open-source hébergée EU (Mixtral / Qdrant / Langfuse sur Scaleway/OVHcloud) | **Haute** (niveau Strong souveraineté) |
| **A4 — Open-source on-premise** | Stack full self-hosted EU (Mixtral on-premise / Qdrant on-premise / Langfuse on-premise) | **Haute** (niveau Sovereign) |

### 5.2 Questions de cadrage prioritaires

- **Structure-type d'une fiche architecture** : sections H2 attendues (cas d'usage cible / stack technique / coût total / souveraineté / complexité opérationnelle / cas-école), recouvrement avec [[outils-vector-db]] + [[pattern-souverainete-eu]]
- **Décisions structurantes** par architecture (qui choisit A1 vs A4 ?)
- **Coût total** par architecture (TCO 12 mois pour PME 50 salariés type)
- **Articulation avec préalables et fiches outils déjà produits** : risque massif de duplication
- **Niveau de souveraineté** explicite par architecture (cf. [[pattern-souverainete-eu]])
- **Candidats extraction transverse** (pattern « TCO 12 mois calculé pour PME 50 sal » récurrent ?)

### 5.3 Volume cible RETOUR

~1500-2000 mots, structuré par architecture + arbitrages cross-architectures.

## 6. Spécification Lot F.8 — Production 4 architectures vague 8

Application stricte SPEC v2.2 :

- **Frontmatter conforme R1** (10 champs, type=`architecture`)
- **Sections H2 thématiquement cohérentes** : cas d'usage cible / stack technique détaillée / TCO / souveraineté / complexité opérationnelle / cas-école PME / wikilinks outils
- **AP-7 strict** : leads scope strict (« A1 SaaS propriétaire pour PME non-souveraine », pas « architecture IA PME »)
- **Chunking H2 autonome** (cible 400-700 tokens, tolérance 800-900)
- **Wikilinks Obsidian denses** vers [[outils-llm]], [[outils-vector-db]], [[outils-frameworks-rag]], [[outils-observabilite-llm]], [[outils-workflow-automation]], [[pattern-souverainete-eu]] (R11 vérifié post-Lot Dev)
- **R10 stricte** sur tarifs et TCO

Bump versions : tous les nouveaux fichiers à **v3.12.0**.

### 6.1 Pattern « architecture » — H2 attendues

Hypothèse structure-type (à valider via RETOUR-SONDAGE-S2.8) :

1. L'essentiel à retenir (lead AP-7 scope strict)
2. À qui cette architecture s'adresse
3. Stack technique détaillée (LLM + vector store + framework + observabilité + workflow)
4. TCO 12 mois pour PME 50 salariés type (en € HT)
5. Niveau de souveraineté (cf. [[pattern-souverainete-eu]])
6. Complexité opérationnelle (équipe requise, compétences, MTBF)
7. Cas d'usage type (déploiement PME 50 sal — non nommée)
8. Comparaison aux 3 autres architectures (renvoi cross-fiche)
9. Anti-patterns à éviter sur cette architecture
10. Plan d'action 30 jours pour démarrer

## 7. Spécification Lot H — Extension golden set vague 8

### 7.1 Questions standards (6-8 nouvelles, q-097 à q-104)

1-2 questions par architecture × 4 architectures = 6-8 questions. Application SPEC v2.2 stricte (AP-5/AP-6/AP-7).

### 7.2 Questions adversariales (2 nouvelles, q-adv-013 + q-adv-014)

Codification rythme SPEC v2.2 : +2 questions adversariales par vague. 2 types nouveaux à introduire :

- **q-adv-013** : variante hors-corpus (architecture inexistante, sigle fabriqué, dispositif fictif) — typiquement « Quelle est l'architecture XYZ-2027 de la French Tech pour les ETI ? »
- **q-adv-014** : variante piège technique (TCO précis non documenté, MTBF exact) — typiquement « Quel est le MTBF exact en heures de l'architecture A4 on-premise pour une PME 50 salariés ? »

## 8. Spécification Lot I — Eval extended + alerte vault > 400 chunks

**Cibles brief §2** :
- Standard ≥ 96/104, Adversarial ≥ 12/14
- Latence p50 ≤ 22 s / p90 ≤ 26 s (vault 300-400 chunks bordure haute), adv p50 ≤ 12 s / p90 ≤ 17 s
- Coût ≤ 2,80 $ Anthropic
- Non-régression S2.7 : 96/96 + 12/12 maintenus

**Procédure attendue Desktop** :

1. Pull `main` + créer branche `s2.8-eval-vague-8`
2. **Discipline hygiène merge SPEC v2.0** : `git grep "<<<<<<<"` retourne vide avant tout `git add`
3. Re-ingestion incrémentale ChromaDB (4 nouvelles architectures + vérification audit R11 propre)
4. **Eval standard + adversarial** :
   ```bash
   python -m rag.code.eval.run_eval \
     --questions rag/eval/questions.yaml \
     --report rag/eval/eval-report-s2.8-standard.md \
     --json rag/eval/eval-report-s2.8-standard.json

   python -m rag.code.eval.run_eval \
     --questions rag/eval/questions.yaml \
     --filter-unit adversarial \
     --report rag/eval/eval-report-s2.8-adversarial.md \
     --json rag/eval/eval-report-s2.8-adversarial.json
   ```
5. **Mesure latence p50/p90** sur les 2 modes
6. **ALERTE vault > 400 chunks** : si franchi, inscrire **recommandation explicite sprint S2.9 dédié optimisation** dans le reporting Desktop
7. Commit + push artefacts + MAJ JOURNAL + STATUS
8. Reporting Cowork : score détaillé par bloc + observations latence + recommandation S2.9 si déclencheur 400 chunks atteint

## 9. Spécification Lot J — RAPPORT-CC-S2.8 + PR finale

Structure 8 sections format S2.7 :

1. **Objectifs S2.8** (3 axes : R11 + vague 8 + +2 adv)
2. **Livrables par lot** (A → J, **Lot Dev R11 nouveau pattern récurrent** Plateforme)
3. **Métriques quantitatives par bloc** (standard, adversarial, latence p50/p90 par mode, coût, vault delta)
4. **Anomalies & observations** — **focus dérive R11 audit** : combien de manquements détectés ? Patches Cowork prévus ?
5. **Décisions structurantes** prises pendant S2.8
6. **Recommandations SPEC v2.3** (si propositions émergent — typiquement pattern « architecture » formalisé si production réussie + ajustements R11 si dérive massive)
7. **Pistes investigation S2.9** : **sprint dédié optimisation latence si vault > 400 chunks** (reranking, top-k 5→3, cache embeddings, Haiku 4.5 sur eval) + démarrage vague 9 (production CU vagues restantes : CU-002, CU-003, CU-005, etc.)
8. **Coûts cumulés** (S1 → S2.8, estimation ~14,65 $)

## 10. Points de discipline post-S2.7 à honorer

- **Discipline hygiène merge SPEC v2.0** : `git grep "<<<<<<<"` obligatoire post-stash pop
- **Pattern « production module pivot dense » SPEC v2.1** : pas applicable en S2.8 (architectures ≠ modules pivots), mais à retenir pour les futures productions
- **AP-7 vigilance** : maintenue sur les 4 architectures — leads scope strict (« A1 SaaS propriétaire » pas « architecture IA »)
- **Sondage D-026 obligatoire** : codifié SPEC v1.8/v2.0/v2.1 pour from scratch. 4 architectures vague 8 = production from scratch
- **VALIDATION-SCORING-S2.8 obligatoire pour R11** (SPEC v2.2 §Validation manuelle) : 5 cas représentatifs avant rejeu Lot I
- **+2 questions adversariales** SPEC v2.2 §rythme codifié — discipline continue dans Lot H
- **Eval réelle pré-clôture** : Lot I obligatoire avant ouverture PR Lot J (SPEC v1.5 §Validation)
- **D-030 hybride** : maintenir le pattern Cowork (MD + golden set + SPEC) → Plateforme (Dev + RAPPORT + PR) → Desktop (eval). Lot Dev récurrent depuis S2.7.

## 11. Synthèse opérationnelle

**Démarrage immédiat (sans dépendance)** :
- **Lot A — Sync SPEC v2.2** (5 min — Blaise via Desktop)
- **Lot B — Sondage D-026 global vague 8** (1h Cowork rédaction sondage + envoi Cowork Hub IA)
- **Lot Dev R11 — citation_audit.py** (2-3h Plateforme dev + tests + VALIDATION-SCORING obligatoire, en parallèle du sondage)

**Après RETOUR-SONDAGE-S2.8 reçu** :
- **Lot F.8 — Production vague 8** (5-7h Cowork éditorial, 4 architectures from scratch)
- **Lots G + H** — whitelist + cartographie v5 + golden set extended +6-8 std + +2 adv (~1h30 Cowork)

**Après Lot F.8 + Lot H + Lot Dev R11 mergés** :
- **Lot I — Eval extended standard + adversarial + alerte latence** (~30 min Desktop, ~2,80 $ Anthropic)

**Clôture sprint** :
- **Lot J — RAPPORT-CC-S2.8 + PR finale** (30 min Plateforme, focus R11 audit + latence)

**Effort total estimé** : ~10-13h cumulé sur ~5-7 jours.

## 12. Vault post-vague 8 — projection

| Avant S2.8 (post-clôture S2.7) | Après S2.8 (cible) | Delta |
|---|---|---|
| 31 fichiers MD | 35 fichiers MD (+4 architectures) | +4 fichiers |
| ~380 chunks ChromaDB | ~420-440 chunks ChromaDB | +40-60 chunks (franchissement seuil 400) |
| 96 questions standard | 102-104 questions standard | +6-8 std |
| 12 questions adversarial | 14 questions adversarial | +2 adv (rythme SPEC v2.2) |
| 96/96 + 12/12 score parfait | ≥ 96/104 standard + ≥ 12/14 adversarial | Maintien robustesse |
| 6 fichiers `outils-*.md` (R11 activable) | 6 fichiers + audit R11 actif | R11 implémenté + audit en production |

**Seuil de surveillance §Performances v2.1** : ~420-440 chunks **franchit le seuil 400**. Si Lot I confirme, **sprint S2.9 dédié optimisation latence** est recommandé (reranking, top-k 5→3, cache embeddings, benchmark Haiku 4.5 sur eval).

---

*Brief produit le 25 mai 2026 par Cowork Hub IA Plateforme post-clôture S2.7 (double validation 96/96 + 12/12 = robustesse RAG confirmée). SPEC v2.2 en vigueur (produite Cowork-side simultanément). À transmettre par Blaise via sync ascendante après revue.*
