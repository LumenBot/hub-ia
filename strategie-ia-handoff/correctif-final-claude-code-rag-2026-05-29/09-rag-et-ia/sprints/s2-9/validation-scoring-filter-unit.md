# VALIDATION-SCORING-S2.9-FILTER-UNIT — Bug-fix `--filter-unit`

**Émetteur :** Claude Code Plateforme (Lot Dev S2.9)
**Garant :** Blaise Cavalli
**Sprint :** S2.9
**Date :** 26 mai 2026
**SPEC en vigueur :** v2.3 §Validation manuelle d'une nouvelle règle de scoring (héritée v2.2)
**Cible :** validation ex-ante du flag `--filter-unit` de `run_eval.py` avant rejeu Lot I référence (cap 0,50 $) et Lots Bench-1 à Bench-5 (~3,00 $).

---

## Pourquoi cette validation

Le bug-fix `--filter-unit` n'introduit pas une « nouvelle règle de scoring » au
sens strict (le scoring `EvalItem` est inchangé), mais il **modifie la
sélection des questions** soumises au scoring. Une erreur silencieuse de
filtrage (filtre vide retournant tout, ou filtre adversarial loupant une
question, etc.) aurait le même effet pratique qu'une erreur de scoring : un
résultat de Lot I/Bench faussement rassurant ou faussement inquiétant.

→ Validation SPEC v2.2 §Validation manuelle **appliquée par analogie** (5 cas
représentatifs, 3 positifs + 2 négatifs) avant tout rejeu eval.

---

## Méthodologie

Pour chaque cas, on construit une mini-YAML golden set fixture (3 std + 3 adv)
et on exécute `filter_questions_by_unit(questions, filter)` directement
(unit-level), puis on vérifie le compte et l'ordre des questions retenues.
Comparaison stricte sur les `id`.

**Fixture** :

```python
QUESTIONS = [
    {"id": "q-001", "unit": "cu-001", "expected_sources": ["cu-001"]},
    {"id": "q-002", "unit": "dep-05", "expected_sources": ["dep-05"]},
    {"id": "q-adv-001", "unit": "adversarial", "expected_refusal": True},
    {"id": "q-adv-002", "expected_refusal": True},        # pas de champ unit
    {"id": "q-adv-003", "expected_sources": []},          # adv via sémantique
]
```

---

## Cas 1 — Positif : `--filter-unit adversarial` retient les 3 adversariales

**Attendu :** `[q-adv-001, q-adv-002, q-adv-003]`
**Obtenu :** `[q-adv-001, q-adv-002, q-adv-003]`
**Diagnostic :** ✅ Conforme. Les 3 signaux adversariaux sont reconnus :
- `unit: adversarial` explicite (q-adv-001)
- `expected_refusal: true` sans champ `unit` (q-adv-002)
- `expected_sources: []` explicitement vide (q-adv-003)

Couvert par `test_filter_adversarial_keeps_adversarial`.

## Cas 2 — Positif : `--filter-unit standard` retient les 2 standards

**Attendu :** `[q-001, q-002]`
**Obtenu :** `[q-001, q-002]`
**Diagnostic :** ✅ Conforme. Aucune fuite adversariale dans le bucket standard. La discipline `S2.7/S2.8 brief` (« --filter-unit standard et --filter-unit adversarial doivent être disjoints et exhaustifs ») est satisfaite : `|std| + |adv| = |all|` (2 + 3 = 5). Couvert par `test_filter_standard_keeps_non_adversarial`.

## Cas 3 — Positif : `--filter-unit all` (ou absence de flag) garde tout

**Attendu :** `[q-001, q-002, q-adv-001, q-adv-002, q-adv-003]` (5 questions, ordre stable)
**Obtenu :** identique pour `filter_unit="all"` et `filter_unit=None`
**Diagnostic :** ✅ Conforme. Rétro-compat absolue : un appel pré-S2.9 sans flag se comporte exactement comme avant le fix. Couvert par `test_filter_none_keeps_all` + `test_filter_all_keeps_all`.

## Cas 4 — Négatif : valeur inconnue → `ValueError` (fail-fast)

**Cmd :** `filter_questions_by_unit(QUESTIONS, "azerty")`
**Attendu :** lève `ValueError` avec message mentionnant les valeurs autorisées
**Obtenu :** `ValueError: --filter-unit doit appartenir à ('standard', 'adversarial', 'all'), reçu : 'azerty'`
**Diagnostic :** ✅ Conforme. **Choix de design délibéré** : fail-fast vs silent fallback. Une erreur de typage côté CLI ne doit pas être absorbée silencieusement (sinon on retomberait dans le pattern « un brief référence un flag inexistant et personne ne s'en aperçoit »). Couvert par `test_filter_unknown_value_raises`. Côté argparse, ce cas est intercepté plus tôt par `choices=FILTER_UNIT_CHOICES`.

## Cas 5 — Négatif : aucune mutation de la liste source

**Cmd :** snapshot de `QUESTIONS` avant et après plusieurs appels successifs avec différents filtres
**Attendu :** la liste source est inchangée (immutabilité fonctionnelle)
**Obtenu :** identique avant/après
**Diagnostic :** ✅ Conforme. **Choix de design délibéré** : `filter_questions_by_unit` retourne une nouvelle liste, ne mute pas l'input. Évite les surprises si la même YAML est réutilisée plusieurs fois dans un script de bench. Couvert par `test_filter_does_not_mutate_input`.

---

## Synthèse validation

| Cas | Type | Filtre | Attendu | Obtenu | Diagnostic |
|---|---|---|---|---|---|
| 1 | Positif | `adversarial` | 3 adv (3 signaux union) | 3 adv | ✅ |
| 2 | Positif | `standard` | 2 std (disjoint de adv) | 2 std | ✅ |
| 3 | Positif | `all` / `None` | 5 (rétro-compat) | 5 | ✅ |
| 4 | Négatif | `"azerty"` | ValueError fail-fast | ValueError fail-fast | ✅ |
| 5 | Négatif | combiné | Pas de mutation | Pas de mutation | ✅ |

**Score validation : 5/5 conforme.** Flag `--filter-unit` prêt pour intégration Lot I référence + Lots Bench-1 à Bench-5.

---

## Tests automatisés associés

Le module `rag/code/eval/test_run_eval.py` couvre les 5 cas ci-dessus via 9 tests dans la classe `TestFilterQuestionsByUnit` + smoke `TestFilterUnitCLI` :

```text
rag/code/eval/test_run_eval.py::TestFilterQuestionsByUnit::test_filter_none_keeps_all PASSED
rag/code/eval/test_run_eval.py::TestFilterQuestionsByUnit::test_filter_all_keeps_all PASSED
rag/code/eval/test_run_eval.py::TestFilterQuestionsByUnit::test_filter_adversarial_keeps_adversarial PASSED
rag/code/eval/test_run_eval.py::TestFilterQuestionsByUnit::test_filter_standard_keeps_non_adversarial PASSED
rag/code/eval/test_run_eval.py::TestFilterQuestionsByUnit::test_filter_unknown_value_raises PASSED
rag/code/eval/test_run_eval.py::TestFilterQuestionsByUnit::test_filter_does_not_mutate_input PASSED
rag/code/eval/test_run_eval.py::TestFilterQuestionsByUnit::test_filter_empty_input PASSED
rag/code/eval/test_run_eval.py::TestFilterQuestionsByUnit::test_filter_unit_case_sensitive_for_yaml_value PASSED
rag/code/eval/test_run_eval.py::TestFilterUnitCLI::test_cli_choices_include_three_values PASSED
```

**Non-régression** : `pytest rag/code/` → **243/243 verts** (vs 234 avant Lot Dev S2.9).

---

## Risques de régression identifiés (et mitigations en place)

1. **Mutation accidentelle de la liste source** : mitigée par retour de nouvelle liste (`return [q for q in questions if ...]`). Couvert par `test_filter_does_not_mutate_input`.
2. **Filtre silencieusement vide** : un filtre laissant 0 question ferait croire à un succès trivial du runner (aucune question = 0 erreur). Mitigé par un avertissement stderr explicite dans `main()` : « aucune question après filtrage --filter-unit=… ». Pas une erreur dure pour préserver les usages CI éventuels qui acceptent un sub-set vide.
3. **Valeurs non-supportées** : double protection — `argparse choices=` (intercepte au parsing) + `ValueError` dans la fonction (intercepte les appels programmatiques).
4. **Variantes de casse YAML** (`unit: Adversarial`) : tolérées par `.strip().lower()` côté détection. Couvert par `test_filter_unit_case_sensitive_for_yaml_value`.
5. **Question adversariale sans champ `unit:` mais avec `expected_refusal: true`** : capturée par le 2ᵉ signal (sémantique). Couvert par fixture `q-adv-002`.
6. **Question avec `expected_sources: []` mais sans `expected_refusal`** : capturée par `is_adversarial()`. Couvert par fixture `q-adv-003`.

---

*Document produit Plateforme-side conformément SPEC v2.2/v2.3 §Validation manuelle. Reproductible via `pytest rag/code/eval/test_run_eval.py -v` (54 tests verts) + `python3 rag/code/eval/run_eval.py --help` (flag visible).*
