# DIAGNOSTIC-FILTER-UNIT-S2.9 — Bug-fix `--filter-unit` de `run_eval.py`

**Émetteur :** Claude Code Plateforme (Lot Dev S2.9)
**Garant :** Blaise Cavalli
**Sprint :** S2.9
**Date :** 26 mai 2026
**Réfs :** BRIEF-CC-S2.9 §5, RAPPORT-CC-S2.8 §4 Observation #1 (2ᵉ occurrence), RAPPORT-CC-S2.7 §4 Observation #1 (1ʳᵉ occurrence)

---

## 1. Comportement attendu

Le brief Desktop des sprints S2.7 et S2.8 prescrit la commande :

```bash
python -m rag.code.eval.run_eval \
    --questions rag/eval/questions.yaml \
    --filter-unit adversarial \
    --report rag/eval/eval-report-s2.X-adversarial.md \
    --json   rag/eval/eval-report-s2.X-adversarial.json
```

…en partant du principe que le flag `--filter-unit {standard,adversarial,all}` ne garde que les questions ciblées dans la YAML golden set (104 std + 14 adv = 118 lignes pour S2.8).

## 2. Comportement constaté

**Le flag `--filter-unit` n'existe pas dans l'argparse de `rag/code/eval/run_eval.py`.**

Vérification sur `origin/main` post-merge S2.8 :

```text
$ python3 rag/code/eval/run_eval.py --help
usage: run_eval.py [-h] [--questions QUESTIONS] [--report REPORT] [--json JSON]
```

Seuls trois flags existent : `--questions`, `--report`, `--json`. Toute commande contenant `--filter-unit` rejette avec :

```text
run_eval.py: error: unrecognized arguments: --filter-unit adversarial
```

## 3. Historique de l'écart procédure

| Sprint | Observation | Statut |
|---|---|---|
| **S2.7** (PR #99 Lot I) | 1ʳᵉ occurrence — Desktop a contourné par 2 sous-golden-sets dérivés (`questions-s2.7-standard.yaml` + `questions-s2.7-adversarial.yaml`). RAPPORT-CC-S2.7 §4 a noté « écart de procédure résolu ». | Contourné, non corrigé |
| **S2.7 fix** (PR #100 Lot Dev) | Calibration v2 du harness adversarial (STRONG/WEAK markers, marqueur franc prime sur citations). **Ne touche pas à l'argparse**. | Sans rapport |
| **S2.8** (PR #105 Lot I) | 2ᵉ occurrence — même contournement Desktop (`questions-s2.8-standard.yaml` + `questions-s2.8-adversarial.yaml`). RAPPORT-CC-S2.8 §4 Observation #1 a marqué le besoin de fix durable. | Contourné, non corrigé |
| **S2.9** (ce Lot Dev) | Fix code définitif. | ✅ Résolu |

## 4. Cause root

Le flag `--filter-unit` a été spécifié dans les briefs Desktop S2.7 puis S2.8 mais **n'a jamais été implémenté côté code Plateforme**. La calibration v2 du harness adversarial S2.7 (PR #100) a corrigé la *logique de scoring* adversarial (faux négatif 0/12 → 12/12) sans toucher à la *sélection* des questions à évaluer.

Le contournement par 2 sous-YAML fonctionnel produit le bon résultat numérique (les `EvalItem` sont les mêmes) mais introduit :
- **Coût opérationnel** : Desktop doit dériver 2 fichiers à chaque sprint
- **Risque de désynchronisation** : si la YAML mère est modifiée et qu'un sub-set n'est pas re-dérivé
- **Friction CI** : un script CI ne peut pas exploiter directement la YAML canonique
- **Discipline brief↔code** : on accepte un écart de spec récurrent

## 5. Correctif minimal appliqué (S2.9 Lot Dev)

Pas de refactoring large. Trois modifications :

1. **`rag/code/eval/run_eval.py`** :
   - Ajout de la constante `FILTER_UNIT_CHOICES = ("standard", "adversarial", "all")`
   - Ajout de la fonction `filter_questions_by_unit(questions, filter_unit) -> list[dict]`
     - Détection adversarial **union de 2 signaux** (défense en profondeur) : champ explicite `unit: adversarial` dans la YAML **OU** `is_adversarial()` sémantique (`expected_refusal: true` ou `expected_sources: []`)
     - `None`/`"all"` → passe-tout (rétro-compat absolue avec les appels existants)
     - Valeur inconnue → `ValueError` (fail-fast vs silently-ignore)
   - Ajout du flag CLI `--filter-unit` à `argparse` avec `choices=FILTER_UNIT_CHOICES` (auto-validation argparse)
   - Avertissement stderr si le filtre laisse 0 questions

2. **`rag/code/eval/test_run_eval.py`** : 9 nouveaux tests (classe `TestFilterQuestionsByUnit` + `TestFilterUnitCLI`) — cf. VALIDATION-SCORING-S2.9.md.

3. **Aucune autre fonction de `run_eval.py` n'est modifiée**. Le pipeline d'eval reste identique : `run_eval(questions, runner)` continue d'itérer sur la liste qu'on lui passe.

## 6. Garde-fou anti-récurrence (proposition SPEC v2.4)

Pour éviter une 3ᵉ occurrence en S2.10+, **proposer codification SPEC v2.4** :

> Tout flag CLI prescrit dans un BRIEF Desktop pour `rag/code/eval/run_eval.py`
> ou `rag/code/audit/*` doit être validé empiriquement (`--help` + test
> argparse) **avant** ouverture du brief. Si manquant : ouverture d'un
> Lot Dev Plateforme dès l'identification (pas en fin de sprint).

Le pattern est analogue à la discipline SPEC v2.2 §Validation manuelle d'une nouvelle règle de scoring : un écart spec ↔ code doit être détecté en amont, pas absorbé par un contournement éditorial.

## 7. Effort réel

| Phase | Temps |
|---|---|
| Diagnostic + lecture code | ~10 min |
| Implémentation `filter_questions_by_unit` + argparse | ~15 min |
| 9 tests unitaires + non-régression 234 → 243 | ~20 min |
| VALIDATION-SCORING-S2.9 (5 cas SPEC v2.2) | ~15 min |
| Documentation + diagnostic + journal/status | ~10 min |
| **Total** | **~70 min** (cible brief : 1-2h) |

**Coût Anthropic** : 0 $ (dev local sans appel API).

---

*Diagnostic produit Plateforme-side dans le cadre du Lot Dev S2.9 (récurrence pattern D-030 codifié SPEC v2.3). Référence : VALIDATION-SCORING-S2.9-FILTER-UNIT.md pour la validation des 5 cas représentatifs.*
