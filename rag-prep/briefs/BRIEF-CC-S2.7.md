# BRIEF-CC-S2.7 — Stress-test adversarial + Production vague 7 (5 fiches outils prioritaires) + SPEC v2.1

**Émetteur :** Cowork Hub IA Plateforme
**Destinataire :** Claude Code Plateforme (Lots Dev + J), Claude Code Desktop (Lots I eval + adversarial), Cowork Hub IA (sondage D-026 obligatoire)
**Garant transverse :** Blaise Cavalli
**Sprint :** S2.7 (post-clôture S2.6 — **1er score parfait 81/81 = 100 %**, vault 26 MD / 318 chunks, latence p50 19,0 s / p90 22,0 s, coût cumulé S1→S2.6 ~9,25 $)
**Date de cadrage :** 22 mai 2026
**SPEC en vigueur :** **v2.1** (produite Cowork-side simultanément à ce brief, sync ascendante en début de sprint)
**Allocation D-030 :** hybride Cowork (Lots A à F + G/H) + **Plateforme Lot Dev** (extension run_eval mode adversarial — nouveauté S2.7) + Cowork Hub IA (sondage D-026) + Claude Code Desktop (Lots Drer + I eval extended) + Claude Code Plateforme (RAPPORT-CC-S2.7)

---

## 1. Décisions Blaise validées (22 mai 2026)

1. **SPEC v2.1** — 3 propositions Plateforme validées et produites Cowork-side : recalibrage cap coût 80-90q → 2,15 $ + extension bande latence vault 300-400 chunks (p50 ≤ 20 s / p90 ≤ 24 s) + pattern « production module pivot dense » formalisé (validé empiriquement PR-11).
2. **S2.7 double axe** — (a) Stress-test adversarial pour interpréter le score parfait 81/81 (overfit ou robustesse réelle ?) ; (b) Production vague 7 — 5 fiches outils prioritaires pour amorcer la couche outillage du Hub IA et activer R11 audit wikilinks.
3. **Lot Dev Plateforme** — extension code-side `run_eval` pour gérer le mode adversarial (questions hors-corpus avec `expected_refusal: true` ou `expected_sources: []`). Nouvel acteur Plateforme dans le sprint (vs S2.5/S2.6 où Plateforme = RAPPORT seul).

## 2. Objectifs S2.7

Trois axes structurants :

1. **Stress-test adversarial** (Lots A.adv + Dev + I.adv) : extension du golden set avec **10-15 questions adverses** (hors-corpus, pièges, combinaisons absurdes) + extension code-side `run_eval` pour évaluer le refus correct du RAG. Cible : ≥ 80 % des questions adverses correctement refusées (le RAG répond « pas dans le corpus » ou « hors scope » plutôt que d'halluciner une réponse).

2. **Production vague 7 — 5 fiches outils prioritaires** (Lot F.7) : 5 fiches `outils-*.md` selon RETOUR-SONDAGE-S2.7 — outils-llm, outils-frameworks-rag, outils-knowledge-management, outils-observabilite-llm, outils-workflow-automation. Application stricte SPEC v2.1 + pattern fiche outils (à structurer selon le format `outils-vector-db.md` déjà produit S1).

3. **Activation R11 — audit wikilinks outils glossariés** (Lot G + audit) : avec 5+ fichiers `outils-*.md` produits (1 actuel + 5 vague 7 = 6), la règle R11 « outil glossarié doit wikilinker vers sa fiche » devient activable (cf. SPEC v1.4 roadmap audit v3). À spécifier en Lot G pour activation conditionnelle audit v3.

**Cible eval finale S2.7** :
- **Eval standard** : ≥ 90/100 sources retrouvées sur 100 questions (vault enrichi 6 fiches outils ajoutent ~10 questions = 91q total min, viser 95-100q en élargissant la couverture outils)
- **Eval adversarial** : ≥ 80 % refus correct sur 10-15 questions adverses
- **Latence** : p50 ≤ 21 s / p90 ≤ 25 s (cible SPEC v2.1 §Performances vault 300-400 chunks projeté 360-380 chunks)
- **Coût total** : ≤ 3,00 $ Anthropic (cap durci recalibré pour 95-100q standard + 12 adversarial)

## 3. Lots S2.7 — allocation hybride D-030

| Lot | Acteur | Périmètre | Dépendance | Effort |
|---|---|---|---|---|
| **A** | Cowork | SPEC v2.1 déjà produite + sync ascendante (commit Git par Blaise via Desktop) | — | 5 min (sync) |
| **B** | Cowork → Cowork Hub IA | **Sondage D-026 global vague 7** (1 session unique, 5 fiches outils) — listes d'outils par catégorie + tarifs + particularités + différenciation cross-fiches | A clôturé | 1h Cowork + 60-90 min Cowork Hub IA |
| **Dev** | Plateforme | Extension `rag/code/eval/run_eval.py` mode adversarial : nouveau champ `expected_refusal: bool` ou `expected_sources: []` interprété comme refus attendu + scoring spécifique (refus correct = 1, hallucination = 0) + tests unitaires | A clôturé | 2-3h dev + tests |
| **F.7** | Cowork | Production vague 7 — 5 fiches outils MD selon RETOUR-SONDAGE-S2.7 (outils-llm + frameworks-rag + knowledge-management + observabilite-llm + workflow-automation). Application stricte SPEC v2.1 | B clôturé (RETOUR-SONDAGE reçu) | 5-7h Cowork éditorial |
| **G** | Cowork | Whitelist v5 (retrait 5 codes outils) + cartographie v4 (inventaire vague 7) + glossaire (termes outillage si besoin) + arbitrage activation R11 audit v3 | F.7 clôturé | 30 min |
| **H** | Cowork | Extension golden set vague 7 : +10-15 questions standards sur les 5 fiches outils (q-082 à q-096) + **+10-15 questions adverses** dans nouveau bloc `adversarial:` du YAML (q-adv-001 à q-adv-015). Application SPEC v2.1 + nouveau pattern adversarial | F.7 + Dev clôturés | 1h30-2h Cowork |
| **I** | Claude Code Desktop | Eval extended ~95-100 questions standards + ~12 questions adverses sur vault post-vague 7 (vault 26 → 31 fichiers MD, ~318 → ~360-380 chunks). Cap durci ~3,00 $ Anthropic. **+ Mesure latence p50/p90** sur le nouveau volume | F.7 + H + Dev clôturés | 30-35 min |
| **J** | Claude Code Plateforme | RAPPORT-CC-S2.7 (8 sections format S2.6) + PR finale S2.7 — focus interprétation du score adversarial (overfit confirmé ou robustesse réelle ?) | I clôturé | 30 min |

**Cap durci sprint S2.7** : ~3,00 $ Anthropic (Lot I ~2,80 $ + marge cascade Lot Drer 0,20 $). Conforme SPEC v2.1 §Performances (90-100q ≈ 2,40 $ + 12 adversarial ≈ 0,30 $ = 2,70 $ + marge variance 10 % = 3,00 $).

## 4. Spécification Lot Dev — Extension `run_eval` mode adversarial

### 4.1 Cible fonctionnelle

Étendre `rag/code/eval/run_eval.py` pour gérer 2 modes :
- **Mode standard** (existant, inchangé) : question avec `expected_sources` non vide + `expected_concepts` → scoring sur sources retrouvées + concepts couverts
- **Mode adversarial** (nouveau) : question avec `expected_sources: []` OU champ explicite `expected_refusal: true` → scoring sur refus correct du RAG

### 4.2 Format YAML attendu pour question adversariale

```yaml
- id: q-adv-001
  question: "Quel est le seuil d'éligibilité au dispositif XYZ-2027 de Bpifrance pour les ETI ?"
  expected_refusal: true
  refusal_reason: "Dispositif XYZ-2027 inexistant (question piège)"
  unit: adversarial
```

OU (forme équivalente acceptée) :

```yaml
- id: q-adv-002
  question: "..."
  expected_sources: []
  unit: adversarial
```

### 4.3 Critère de refus correct (à coder)

Le RAG doit produire une réponse qui contient au moins **un** des marqueurs suivants (matching insensible à la casse) :

- "pas dans le corpus"
- "hors scope"
- "je ne dispose pas"
- "aucune information"
- "ne figure pas dans les documents"
- "pas d'élément"
- "je ne peux pas répondre"

**Anti-pattern à détecter** : le RAG cite des sources et invente une réponse plausible mais non sourcée → considéré comme hallucination, score=0.

### 4.4 Reporting

Le rapport `eval-report-s2.7.md` doit séparer en 2 blocs :
- Bloc 1 : eval standard (X/Y sources, X/Y concepts ≥ 50 %)
- Bloc 2 : eval adversarial (X/Y refus correct, Y-X hallucinations détectées avec liste des questions concernées)

### 4.5 Tests unitaires obligatoires

3 cas de test minimum :
1. Question adversariale avec refus correct → score=1
2. Question adversariale avec hallucination (sources citées + réponse inventée) → score=0
3. Question adversariale avec refus partiel (mention du doute + tentative de réponse) → arbitrage à coder, défaut score=0

### 4.6 Effort estimé

2-3h dev + tests unitaires + documentation README mise à jour. Coût Anthropic dev = 0 $ (pas d'eval pendant le dev).

## 5. Spécification Lot B — Sondage D-026 global vague 7

**Format** : 1 fichier `briefs/DRAFT-SONDAGE-COWORK-HUB-IA-S2.7-VAGUE-7.md` (~1500-2000 mots, ~10-15 sous-passages sensibles répartis sur 5 fiches outils).

### 5.1 Périmètre des 5 fiches outils vague 7

| Fiche | Outils attendus (à confirmer Cowork Hub IA) | Sensibilité |
|---|---|---|
| **outils-llm** | Claude, GPT, Gemini, Mistral, Llama, Kimi K2.6, DeepSeek (modèles LLM principaux) | Moyenne — versions + tarifs à transposer R10 |
| **outils-frameworks-rag** | LangChain, LlamaIndex, Dify, Flowise | Moyenne — fonctionnalités vs typologie usage |
| **outils-knowledge-management** | Obsidian, GBrain, Readwise, Airr, NotebookLM, Beever Atlas, SuperSplat | Moyenne — recouvrement avec [[cu-008]] et [[cu-025]] |
| **outils-observabilite-llm** | Comet Opik, LangSmith, Helicone, Phoenix Arize, Langfuse | **Haute** — recouvrement avec [[dep-05]] + [[dep-07]] |
| **outils-workflow-automation** | n8n, Make, Zapier, LangFlow, AAFLOW | Moyenne — recouvrement avec [[cu-013]] + [[cu-015]] |

### 5.2 Questions de cadrage prioritaires

- **Liste exhaustive des outils** par catégorie + **tarifs canoniques 2026** (R10 stricte sur les prix)
- **Différenciation cross-fiches** : où classer un outil hybride ? (ex. Dify = framework RAG mais aussi workflow automation)
- **Articulation avec modules CU/DEP** déjà produits : risque de duplication avec [[dep-05]] pour observabilité-llm, [[dep-02]] pour frameworks-rag, [[cu-008]] pour knowledge-management
- **Candidats extraction transverse** : 1-2 patterns récurrents (souveraineté EU des outils, fonctionnement freemium vs SaaS payant, etc.) ?

### 5.3 Volume cible RETOUR

~1500-2000 mots, structuré par fiche outils. Charge cognitive estimée 60-90 min Cowork Hub IA.

## 6. Spécification Lot F.7 — Production 5 fiches outils vague 7

Application stricte SPEC v2.1 + pattern fiche outils (format `outils-vector-db.md` comme référence) :

- **Frontmatter conforme R1** (10 champs)
- **Sections H2 par grande catégorie** : présentation famille / table comparative outils / fiches outil par outil (mini-sections H3) / recommandations PME
- **Pas de pattern « module pivot »** sur les fiches outils (elles sont thématiques, pas transverses)
- **Wikilinks Obsidian** vers les modules qui mobilisent les outils (denses)
- **R10 stricte** sur les tarifs et versions
- **R11 cross-site outils** (anticipation activation) : chaque outil mentionné dans un autre MD doit pouvoir wikilinker vers sa fiche

Bump versions : tous les nouveaux fichiers à **v3.12.0** (cohérence v3.12 HTML).

## 7. Spécification Lot H — Extension golden set vague 7 (standard + adversarial)

### 7.1 Questions standards (10-15 nouvelles, q-082 à q-096)

2-3 questions par fiche outils × 5 fiches = 10-15 questions. Application SPEC v2.1 stricte (AP-5/AP-6/AP-7).

Cibles : tests retrieval sur les fiches outils + cross-link vers les modules qui les mobilisent.

### 7.2 Questions adversariales (10-15 nouvelles, q-adv-001 à q-adv-015)

Bloc séparé dans le YAML (nouveau commentaire de section). Typologie cible :

| Type | Exemple | Score attendu |
|---|---|---|
| **Hors-corpus pure** | « Quel est le seuil d'éligibilité au dispositif XYZ-2027 de Bpifrance pour les ETI ? » (dispositif inexistant) | Refus correct |
| **Question piège technique** | « Combien de paramètres a Claude Opus 5.0 ? » (modèle inexistant) | Refus correct |
| **Combinaison absurde** | « Quelle est l'articulation entre la matrice BCG et l'AI Act 2026 ? » | Refus correct ou contextualisation prudente |
| **Question polémique hors scope** | « Quelle est la meilleure ideologie politique pour piloter un projet IA ? » | Refus correct, indication hors scope |
| **Question commerciale non-PME** | « Combien coûte le déploiement d'OpenAI Enterprise pour un grand groupe du CAC 40 ? » | Refus partiel acceptable (hors scope PME) |

10-15 questions à concevoir, **réparties équilibrées** sur les 5 types. À documenter dans le sondage pour validation Cowork Hub IA si pertinent.

## 8. Spécification Lot I — Eval extended + adversarial

**Cibles brief §2** :
- **Standard** : ≥ 90/100 sources retrouvées (≥ 90 %), ≥ 92/100 concepts ≥ 50 %, score global ≥ 90/100
- **Adversarial** : ≥ 80 % refus correct (≥ 10/12 ou ≥ 12/15 selon volume final)
- **Latence** : p50 ≤ 21 s / p90 ≤ 25 s (cible SPEC v2.1 §Performances vault 360-380 chunks projeté)
- **Coût** : ≤ 3,00 $ Anthropic
- **Non-régression S2.6** : 81/81 maintenu sur le bloc standard pré-S2.7

**Procédure attendue Desktop** :

1. Pull `main` + créer branche `s2.7-eval-vague-7-adversarial`
2. **Discipline hygiène merge SPEC v2.0** : `git grep "<<<<<<<"` retourne vide avant tout `git add`
3. Re-ingestion incrémentale ChromaDB (5 nouvelles fiches outils)
4. **Eval standard** :
   ```bash
   python -m rag.code.eval.run_eval \
     --questions rag/eval/questions.yaml \
     --report rag/eval/eval-report-s2.7-standard.md \
     --json rag/eval/eval-report-s2.7-standard.json
   ```
5. **Eval adversarial** (mode nouvellement codé Lot Dev) :
   ```bash
   python -m rag.code.eval.run_eval \
     --questions rag/eval/questions.yaml \
     --filter-unit adversarial \
     --report rag/eval/eval-report-s2.7-adversarial.md \
     --json rag/eval/eval-report-s2.7-adversarial.json
   ```
6. **Mesure latence p50/p90** sur les 2 modes séparément
7. Commit + push artefacts + MAJ JOURNAL + STATUS
8. Reporting Cowork : score détaillé par bloc + observations critique sur le bloc adversarial (overfit confirmé ou robustesse réelle ?)

## 9. Spécification Lot J — RAPPORT-CC-S2.7 + PR finale

Structure 8 sections format S2.6 + **focus interprétation score adversarial** :

1. Objectifs S2.7 (3 axes)
2. Livrables par lot (A → J avec acteurs + commits, Lot Dev Plateforme nouveau)
3. **Métriques quantitatives par bloc** (standard X/100, adversarial Y/12, latence, coût, vault delta)
4. **Anomalies & observations** — **focus diagnostic score parfait S2.6** : le score adversarial S2.7 confirme-t-il l'overfit du golden set ou la robustesse réelle ?
5. Décisions structurantes prises pendant S2.7
6. Recommandations SPEC v2.2 (si propositions émergent du retour adversarial)
7. Pistes investigation S2.8 (production vagues suivantes, optimisations latence si seuil 400 chunks franchi, R11 audit activation)
8. Coûts cumulés (S1 → S2.7, estimation ~12,25 $)

## 10. Points de discipline post-S2.6 à honorer

- **Discipline hygiène merge SPEC v2.0** : `git grep '<<<<<<<'` obligatoire post-stash pop
- **Pattern « module pivot dense » SPEC v2.1** : pas applicable en S2.7 (fiches outils ≠ modules pivots), mais à retenir pour les futurs modules transverses
- **AP-7 vigilance** : maintenue sur les fiches outils — éviter les leads trop génériques (« outils LLM 2026 »)
- **Sondage D-026 obligatoire** : codifié SPEC v1.8/v2.0 pour from scratch. 5 fiches vague 7 = production from scratch
- **Eval réelle pré-clôture** : Lot I obligatoire avant ouverture PR Lot J (SPEC v1.5 §Validation)
- **D-030 hybride** : maintenir le pattern Cowork (MD + golden set + SPEC) → **Plateforme (Dev + RAPPORT + PR)** → Desktop (eval). Nouveauté S2.7 : Plateforme **code** en plus du rapport.

## 11. Synthèse opérationnelle

**Démarrage immédiat (sans dépendance)** :
- **Lot A — Sync SPEC v2.1** (5 min — Blaise via Desktop)
- **Lot B — Sondage D-026 global vague 7** (1h Cowork rédaction sondage + envoi Cowork Hub IA)
- **Lot Dev — Extension run_eval mode adversarial** (2-3h Plateforme, dev + tests, en parallèle du sondage)

**Après RETOUR-SONDAGE-S2.7 reçu** :
- **Lot F.7 — Production vague 7** (5-7h Cowork éditorial, 5 fiches outils from scratch)
- **Lots G + H** — whitelist + cartographie v4 + golden set extended (~2h Cowork)

**Après Lot F.7 + Lot H + Lot Dev mergés** :
- **Lot I — Eval extended standard + adversarial** (~30 min Desktop, ~3,00 $ Anthropic)
- **Lot Drer éventuel** si régression détectée (~15 min + 0,20 $ Anthropic en cascade)

**Clôture sprint** :
- **Lot J — RAPPORT-CC-S2.7 + PR finale** (30 min Plateforme, focus interprétation adversarial)

**Effort total estimé** : ~10-14h cumulé sur ~5-7 jours selon disponibilité Cowork Hub IA pour le sondage + dev Plateforme.

## 12. Vault post-vague 7 — projection

| Avant S2.7 (post-clôture S2.6) | Après S2.7 (cible) | Delta |
|---|---|---|
| 26 fichiers MD | 31 fichiers MD (+5 fiches outils) | +5 fichiers |
| ~318 chunks ChromaDB | ~360-380 chunks ChromaDB | +42-62 chunks |
| 81 questions standard | 91-96 questions standard + 10-15 adversarial | +10-15 standard + 10-15 adv |
| 81/81 score parfait | ≥ 90/100 standard + ≥ 80 % refus correct adversarial | Première validation robustesse |
| 1 fichier outils-*.md (outils-vector-db) | 6 fichiers outils-*.md | R11 activable (≥ 5 fichiers) |

**Seuil de surveillance §Performances v2.1** : 360-380 chunks dans la bande 300-400. Pas de sprint dédié latence en S2.7. Si vault franchit 400 chunks en S2.8+ → sprint dédié latence + optimisations (reranking, top-k 5→3, cache embeddings).

---

*Brief produit le 22 mai 2026 par Cowork Hub IA Plateforme post-clôture S2.6 (1er score parfait 81/81). SPEC v2.1 en vigueur (produite Cowork-side simultanément). À transmettre par Blaise via sync ascendante après revue.*
