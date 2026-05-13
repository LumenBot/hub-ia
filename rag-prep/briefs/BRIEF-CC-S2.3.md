# BRIEF-CC-S2.3 — Vague 3 (modules denses CU-026/CU-027/DEP-08) + matching sémantique synonymes + co-production sondage

**Émetteur :** Cowork Hub IA Plateforme
**Destinataire :** Claude Code Plateforme (Lots techniques), Claude Code Desktop (Lots eval), Cowork Hub IA (co-production sondage parallèle)
**Garant transverse :** Blaise Cavalli
**Sprint :** S2.3 (post-clôture S2.2 — 30/30 atteint sur golden set)
**Branche développement :** à créer `claude/execute-pilot-batches-{slug}` selon D-027 — pattern à confirmer en début Lot C
**Date de cadrage :** 13 mai 2026
**SPEC en vigueur :** v1.5 (post-S2.2, 4 propositions Plateforme validées)
**Allocation D-030 :** hybride Cowork (Lots A, B, D production MD + golden set) + Cowork Hub IA en parallèle (sondage) + Claude Code Plateforme (Lots C, F) + Claude Code Desktop (Lot E)

---

## 1. Objectifs S2.3

Trois axes structurants :

1. **Compléter le vault avec la vague 3 — 3 modules denses** : `cu-026.md` (Gouvernance des agents IA), `cu-027.md` (Faire développer une appli métier sans être IT), `dep-08.md` (Sécurité agents et MCP servers). Ces modules sont les plus exposés à la dérive sémantique (cf. AP-1 chiffres canoniques, AP-3 édulcoration, AP-4/R10 tableaux numériques) — production sous protocole de co-production sondage avec Cowork Hub IA pour ancrer les passages techniques pointus avant production.

2. **Résoudre les 5 faux négatifs matching exact** identifiés dans RAPPORT-CC-S2.2 §7 (méthode/méthodologie, vérification/vérifier, 1,8 heures/heure, persistant/persistance, économie/gain) — application de l'**option 2** (liste de synonymes par concept) arbitrée par Cowork comme plus pragmatique (minimal effort, zéro coût API, contrôle éditorial préservé).

3. **Étendre le golden set à 39 questions** — 3 nouvelles questions par module vague 3 (q-031 à q-039), tout en enrichissant les `expected_concepts` des 30 questions existantes avec leurs synonymes/dérivés.

**Cible eval finale S2.3** : ≥ 32/39 sources retrouvées (≥ 82 %), ≥ 35/39 concepts ≥ 50 % couverts (avec matching synonymes activé), latence 12-18 s/question (SPEC v1.5 §Performances), coût total Lot E < 0,90 $ Anthropic (post top-up — vérifier crédits avant lancement).

---

## 2. Préalable bloquant — Sondage Cowork Hub IA → retour sensible

Avant de produire les 3 MD vague 3, transmettre à Cowork Hub IA (autre canal) le sondage `rag-prep/briefs/DRAFT-SONDAGE-COWORK-HUB-IA-S2.3-PRE-PRODUCTION.md` (déjà produit, contient 9 passages sensibles structurés par module).

**Retour attendu** : un fichier `RETOUR-SONDAGE-COWORK-HUB-IA-S2.3.md` dans `rag-prep/briefs/` couvrant les 9 passages sensibles avec, pour chacun, la formulation canonique du Hub (chiffres exacts, ordre des dimensions, noms d'acteurs, cas-écoles, niveau de détail).

**Allocation** : sondage produit côté Cowork Hub IA Plateforme (canal séparé), transmis à Cowork Hub IA par Blaise via sync ascendante du `DRAFT-SONDAGE-...`. Le retour est attendu **avant Lot B** (production MD), mais **les Lots A, C, D peuvent commencer en parallèle sans bloquer**.

---

## 3. Lots S2.3 — allocation hybride D-030

| Lot | Acteur | Périmètre | Dépendance |
|---|---|---|---|
| **A** | Cowork | Transmission sondage à Cowork Hub IA (canal séparé) + attente RETOUR-SONDAGE | — (peut démarrer immédiatement) |
| **B** | Cowork | Production `cu-026.md`, `cu-027.md`, `dep-08.md` sous SPEC v1.5 + intégration RETOUR-SONDAGE | Lot A clôturé (RETOUR reçu) |
| **C** | Cowork | Enrichissement `expected_concepts` des 30 questions existantes avec listes de synonymes (option 2) + ajout 9 questions vague 3 (q-031 à q-039) | — (peut démarrer immédiatement en parallèle de A) |
| **D** | Claude Code Plateforme | Adapt `evaluate_one()` dans `rag/code/eval/run_eval.py` pour parcourir liste de synonymes (cf. §4 ci-dessous) + tests unitaires + audit-md-rag.py R11 si formalisation pattern wikilinks décidée | Lot C clôturé (format synonymes choisi et inscrit dans questions.yaml) |
| **E** | Claude Code Desktop | Eval extended 39 questions sur vault enrichi (10 + 3 = 13 fichiers MD, ré-ingestion incrémentale) post-Lot D | Lots B + D clôturés |
| **F** | Claude Code Plateforme | RAPPORT-CC-S2.3 (8 sections) + ouverture PR finale S2.3 | Lot E clôturé |

**Cap durci sprint** : 1,20 $ Anthropic (Lot E rerun + variance) + 0,003 $ OpenAI (ingest 3 nouveaux fichiers). Top-up Blaise effectif → vérifier crédits restants avant lancement Lot E.

---

## 4. Spécification matching sémantique synonymes — option 2 retenue

### Format YAML retenu pour `expected_concepts`

**Option B (Cowork préférence — RAPPORT §7 piste 2)** : liste de listes, un concept = match si au moins un terme de la sous-liste est dans la réponse. Permet de garder la lisibilité YAML et un contrat explicite.

**Avant (v1, S2.2)** :
```yaml
expected_concepts: [méthode, vérification, "1,8 heures"]
```

**Après (v2, S2.3)** :
```yaml
expected_concepts:
  - [méthode, méthodologie, approche]
  - [vérification, vérifier]
  - ["1,8 heures", "1,8 heure"]
```

**Rétro-compatibilité** : une string scalaire en `expected_concepts` reste valide et matche comme avant. `evaluate_one()` doit distinguer `isinstance(c, list)` (match si ≥ 1 synonyme présent) vs `isinstance(c, str)` (match littéral sous-chaîne).

### Adaptation `evaluate_one()` (Lot D)

Pseudo-code Plateforme :
```python
def concept_matched(concept_entry, answer_text_lower: str) -> bool:
    if isinstance(concept_entry, list):
        return any(str(syn).lower() in answer_text_lower for syn in concept_entry)
    return str(concept_entry).lower() in answer_text_lower
```

Tests unitaires attendus dans `rag/code/eval/test_run_eval.py` :
- Concept scalaire seul (cas v1) → match comme avant
- Liste de synonymes, 1 trouvé → match True
- Liste de synonymes, 0 trouvé → match False
- Mix scalaire + liste dans une même `expected_concepts` → comportement homogène
- Concept liste vide `[]` → match False (cas dégénéré, à signaler comme warning)

### Enrichissement golden set existant (Lot C, Cowork)

Sur les 30 questions de `rag/eval/questions.yaml`, enrichir au minimum les 5 entrées suivantes (résolution faux négatifs S2.2 §7) :

| Question | Concept v1 | Concept v2 (liste synonymes) |
|---|---|---|
| q-001 | `méthode` | `[méthode, méthodologie, approche]` |
| q-012 | `vérification` | `[vérification, vérifier]` |
| q-016 | `"1,8 heures"` | `["1,8 heures", "1,8 heure"]` |
| q-028 | `persistant` | `[persistant, persistance, persistent]` |
| q-029 | `économie` | `[économie, économies, gain, réduction]` |

Pour les 25 autres questions, élargissement optionnel selon le diagnostic des faux négatifs marginaux observés au prochain rerun.

### Anti-pattern à inscrire dans SPEC v1.6 (post-S2.3)

Synonymes excessifs (5+ termes par concept) → risque de faux positifs (`économie` matcherait `économie d'énergie` qui n'est pas le concept attendu). Garder 2-4 synonymes par concept, alignés sur les variations morphologiques attendues du même concept.

---

## 5. Production MD vague 3 — directives SPEC v1.5

Pour chaque module (Lot B post-RETOUR-SONDAGE) :

### CU-026 — Gouvernance des agents IA

- **Frontmatter** : `type: module-cu`, `axe: B`, `niveau: 3`, `tags: [agentique, gouvernance, mcp, agents]`, `derives: ["[[cu-014]]"]` + autres à compléter post-sondage, `public_cible: [dirigeant, ops, tech]`.
- **Sections H2 prévues** (à affiner avec RETOUR-SONDAGE) :
  1. Pourquoi gouverner les agents
  2. Le cas Klarna (RetEx documenté — chiffres exacts à préserver via RETOUR §passage 1)
  3. Framework de gouvernance (les N dimensions exactes — RETOUR §passage 2)
  4. Pattern « agent = employé » — *arbitrage extraction transverse à acter au moment de la production : si pattern présent dans CU-026 + CU-014 + (potentiellement CU-022), extraire en `transverses/pattern-agent-employe.md` (D-025). Sinon, le maintenir dans CU-026 et y wikilinker depuis CU-014.*
  5. Risques de dérive et points d'attention
  6. Récap actionnable + renvoi DEP-05 (observabilité agents)
- **Wikilinks à anticiper** : `[[cu-014]]`, `[[dep-05]]`, `[[dep-08]]` (sécurité agents — produit dans même vague), `[[pattern-llm-wiki]]` si renvoi, `[[chiffres-macro-2026#...]]` pour Klarna si chiffré canonique.

### CU-027 — Faire développer une appli métier (sans être IT)

- **Frontmatter** : `type: module-cu`, `axe: agentique`, `niveau: 4`, `tags: [agentique, appli-metier, dev-ia-assiste, no-code, low-code]`, `derives: ["[[pr-07]]", "[[cu-008]]"]`, `public_cible: [dirigeant, ops]`.
- **Sections H2 prévues** :
  1. Le contexte : démocratisation du dev IA-assisté
  2. Stack ECC (compression coûts) — *arbitrage canonisation chiffre « 8-10× moins cher qu'Opus » : si validé par RETOUR §passage 4, ajouter en 23e chiffre canonique de `chiffres-macro-2026.md`, sinon citer local.*
  3. Niveaux d'autonomie des outils (Cursor, Claude Code, Lovable…) — préserver ordre canonique RETOUR §passage 6
  4. Cas-école AMETRA (PME FR industrielle) — détail à partir RETOUR §passage 5
  5. Risques et garde-fous (PI, sécurité du code généré, maintenance)
  6. Récap actionnable
- **Wikilinks à anticiper** : `[[pr-07]]` (build vs buy), `[[cu-008]]` (RAG si applis assistantes), `[[dep-08]]` (sécurité), `[[chiffres-macro-2026]]`.

### DEP-08 — Sécurité agents et MCP servers

- **Frontmatter** : `type: deploiement-dep`, `axe: B`, `niveau: 4`, `tags: [securite, agents, mcp, gouvernance-tech]`, `derives: ["[[cu-026]]", "[[dep-05]]"]`, `public_cible: [tech, r&d, ops]`.
- **Sections H2 prévues** :
  1. Pourquoi la sécurité agents est un sujet à part
  2. Cadrage des risques MCP servers — *énumération exacte RETOUR §passage 7 (3-5 catégories : injection, exfiltration, escalade privilèges, etc.)*
  3. Patterns de mitigation (sandboxing, droits explicites, escalade, audit logs)
  4. Cas-école sécurité — angle RETOUR §passage 9 (Klarna ? Stripe Minions ? autre — à préserver fidèlement)
  5. Architecture d'observabilité agents — articulation avec DEP-05
  6. Récap actionnable
- **Wikilinks à anticiper** : `[[cu-026]]`, `[[cu-014]]`, `[[dep-05]]`, `[[vigilance-confidentialite]]`.

**Briques transverses potentielles à arbitrer (D-025)** :
- `pattern-agent-employe.md` si recouvrement CU-014 + CU-026 confirmé
- Pas d'autre extraction prévue sur cette vague — à confirmer post-production si recouvrement émerge

---

## 6. Audit-md-rag — évolutions optionnelles Lot D

À arbitrer côté Plateforme selon temps disponible (non bloquant) :

- **R11 — formalisation pattern wikilinks** : nouvelle règle d'audit qui vérifie que les chunks de réponse RAG (post-query) utilisent bien le format wikilink `[[code]]`. Strictement parlant ce n'est pas une règle MD, mais une règle de validation post-query. À inscrire éventuellement comme **règle backend** dans un fichier dédié (`rag/code/backend/citation_audit.py`).
- **R5 v3 « première occurrence seulement »** (déjà en roadmap SPEC v1.4) : à mettre en œuvre quand 5+ fichiers vague 3+ stabilisés. Pas prioritaire pour S2.3.

**Recommandation** : si charge Plateforme tendue post-Lot D matching synonymes, reporter R11 / R5 v3 à S2.4 sans pénalité.

---

## 7. Eval extended 39 questions — Lot E (Desktop)

Pré-requis pré-lancement :
- Vérifier crédits Anthropic restants (post top-up) — minimum 1,00 $ recommandé pour le rerun
- Vault à 13 fichiers MD (10 actuels + cu-026 + cu-027 + dep-08) → re-ingestion incrémentale OpenAI : ~12 000-18 000 tokens estimés × text-embedding-3-small = ~0,001 $
- `evaluate_one()` Lot D mergé sur main

Procédure attendue :
1. Pull main + merge dans branche dédiée
2. Ré-ingestion : `python -m rag.code.ingestion.ingest` (incrémental sur les 3 nouveaux fichiers)
3. Eval : `python -m rag.code.eval.run_eval --questions rag/eval/questions.yaml --report rag/eval/eval-report-s2.3.md --json rag/eval/eval-report-s2.3.json`
4. Commit + push artefacts
5. MAJ JOURNAL + STATUS (Git-side, sync descendante par Blaise post-clôture)

Métriques cibles :
- **Sources retrouvées** : ≥ 32/39 (≥ 82 %) — équivalent au seuil 30/30 atteint en S2.2 lissé sur 39
- **Concepts ≥ 50 %** : ≥ 35/39 (≥ 90 %) avec matching synonymes activé
- **Score global** : ≥ 32/39
- **Latence** : moyenne 12-18 s/question (cible SPEC v1.5 §Performances)
- **Coût** : ≤ 0,90 $ Anthropic (cap durci sprint S2.3) + ≤ 0,002 $ OpenAI

---

## 8. RAPPORT-CC-S2.3 — Lot F (Plateforme)

Structure attendue (8 sections, conforme format S2.2) :
1. Objectifs S2.3
2. Livrables par lot (A à F avec commits)
3. Métriques quantitatives (eval 39q avant/après synonymes, latence, ingest incrémentale)
4. Anomalies & fixes (s'il y en a — sinon paragraphe vide explicite)
5. Décisions structurantes prises pendant le sprint
6. Recommandations SPEC v1.6 (si propositions émergent)
7. Pistes investigation S2.4 (à imaginer selon résultats)
8. Coûts cumulés (S1 + S2.1 + S2.2 + S2.3, alerte budget Anthropic si pertinent)

PR finale titre : `feat(rag): Sprint S2.3 - vague 3 (cu-026 cu-027 dep-08) + matching sémantique synonymes + golden set 39q`.

---

## 9. Points de discipline post-S2.2 à honorer

- **AP-5 vigilance commit golden set** : à chaque ajout/modification de question, vérifier visuellement le typage YAML (cf. SPEC v1.5 §Anti-patterns AP-5). Quotation explicite si une valeur commence par un chiffre.
- **Eval réelle pré-clôture** (SPEC v1.5 §Validation) : Lot E obligatoire avant ouverture PR Lot F. Pas de clôture S2.3 sur tests unitaires seuls.
- **D-022 délégation Desktop** : exception ciblée auto-correction maintenue pour Lot E si blocker formel détecté (validation ex-ante Blaise selon pattern S2.2 Lot D bis).
- **Allocation hybride** : maintenir le pattern Cowork (MD + golden set) → Plateforme (code) → Desktop (eval) → Plateforme (rapport). Validé empiriquement S2.2.

---

## 10. Synthèse opérationnelle

**Démarrage immédiat possible** :
- Cowork → Lot A (transmettre sondage à Cowork Hub IA) + Lot C (enrichir synonymes golden set existant + ajouter q-031/039)
- Pas de dépendance bloquante avant RETOUR-SONDAGE pour Lots A et C

**Après RETOUR-SONDAGE reçu** :
- Cowork → Lot B (production cu-026/cu-027/dep-08)
- Claude Code Plateforme → Lot D (adapt evaluate_one + tests)

**Après Lots B et D mergés** :
- Claude Code Desktop → Lot E (eval extended 39q)

**Après Lot E clôturé** :
- Claude Code Plateforme → Lot F (RAPPORT + PR finale)

**Garant transverse** : Blaise valide les jalons inter-lots, effectue sync ascendante/descendante des fichiers de gouvernance (JOURNAL, STATUS, briefs), arbitre les ambiguïtés.

---

*Brief produit le 13 mai 2026 par Cowork Hub IA Plateforme post-clôture S2.2. Format conforme briefs S2.1/S2.2. SPEC v1.5 en vigueur. À transmettre par Blaise via sync ascendante après revue.*
