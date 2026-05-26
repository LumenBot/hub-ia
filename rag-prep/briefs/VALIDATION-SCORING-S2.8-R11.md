# VALIDATION-SCORING-S2.8-R11 — Règle R11 (wikilinks outils glossariés)

**Émetteur :** Claude Code Plateforme (Lot Dev R11)
**Garant :** Blaise Cavalli
**Sprint :** S2.8
**Date :** 26 mai 2026
**SPEC en vigueur :** v2.2 §Validation manuelle d'une nouvelle règle de scoring
**Cible :** validation ex-ante de la règle R11 avant rejeu Lot I (cap durci 2,80 $)

---

## Pourquoi cette validation

SPEC v2.2 a inscrit, en tirant directement la leçon du faux négatif harness
adversarial S2.7 (0/12 → 12/12 après calibration v2), l'**obligation** de
valider manuellement toute nouvelle règle de scoring sur **5 cas représentatifs
(3 positifs + 2 négatifs)** avant intégration. R11 (audit citation_audit.py)
est la première règle d'audit introduite depuis cette codification — elle y
est soumise par construction.

**Coût évité** : un cycle complet de re-eval Lot I (~0,30 $ Anthropic + 15 min
Desktop) si la règle s'avérait faussement permissive (faux négatifs côté
R11) ou faussement stricte (faux positifs faisant exploser le rapport
manquements).

---

## Méthodologie

Pour chaque cas, on construit un MD minimal de test (frontmatter conforme +
section H2 contenant la mention) et on l'exécute via `check_r11_for_file()`.
Le scoring attendu :

- **Cas positif (3)** : score R11 = OK, aucun manquement listé pour l'outil ciblé.
- **Cas négatif (2)** : score R11 = manquement détecté, source_fiche correcte.

Tous les cas s'appuient sur les fiches `outils-llm.md` (Mistral, Claude, Kimi K2)
et `outils-vector-db.md` (Qdrant) **déjà produites** dans le vault — pas de
fixture éditoriale ad hoc.

---

## Cas 1 — Positif : wikilink AVANT la mention en clair → OK

**MD de test :**

```markdown
## Pourquoi un LLM souverain

Voir la fiche [[outils-llm]] pour le comparatif complet. Cette section
détaille l'usage de Mistral comme exemple de référence souveraine EU.
```

**Score attendu :** R11 OK (Mistral mentionné après un wikilink vers `outils-llm`)
**Score obtenu :** R11 OK (`ok_mentions` contient `"Mistral"`, `manquements`
vide pour `Mistral`)
**Diagnostic :** ✅ Comportement conforme. Couvert par
`test_wikilink_before_mention`.

---

## Cas 2 — Positif : mention DANS un wikilink alias → OK

**MD de test :**

```markdown
## LLM souverain EU

Le modèle [[outils-llm|Mistral]] est la référence EU. On l'évoque ensuite
plusieurs fois en clair : Mistral, Mistral, Mistral.
```

**Score attendu :** R11 OK (la 1re « mention » est elle-même un wikilink
valide ; les occurrences ultérieures en clair sont couvertes par le wikilink
initial)
**Score obtenu :** R11 OK (`find_first_naked_occurrence` ignore l'intérieur
des `[[...]]`, et la première occurrence nue est précédée par le wikilink
sur la même ligne → `min(wikilink_positions) <= naked_pos` vrai)
**Diagnostic :** ✅ Comportement conforme. Couvert par
`test_wikilink_alias_inline` + `test_ignores_inside_wikilink`.

---

## Cas 3 — Positif : outil non mentionné → OK (silence)

**MD de test :**

```markdown
## Section sans LLM

Cette section ne mentionne aucun outil de la fiche outils-llm. On y parle
seulement de gouvernance et de processus.
```

**Score attendu :** R11 OK (aucun outil mentionné → rien à wikilinker, aucun
manquement)
**Score obtenu :** R11 OK (`manquements == []`, `ok_mentions == []`)
**Diagnostic :** ✅ Comportement conforme. Couvert par
`test_tool_not_mentioned`. **Important** : la règle ne génère pas de bruit
positif (« ✅ OK ») par outil non mentionné — seul le compteur global
`ok_mentions` reflète les outils wikilinkés correctement.

---

## Cas 4 — Négatif : mention en clair SANS aucun wikilink → manquement

**MD de test :**

```markdown
## Souveraineté EU

Le modèle Mistral est intéressant pour la souveraineté EU. Pas de mention
de fiche outils.
```

**Score attendu :** R11 MANQUEMENT (mention Mistral nue, aucun wikilink
vers outils-llm dans le MD)
**Score obtenu :** R11 MANQUEMENT (`manquements` contient une entrée
`tool="Mistral"`, `source_fiche="outils-llm"`, `line` correcte)
**Diagnostic :** ✅ Comportement conforme. Couvert par
`test_naked_mention_no_wikilink`. **Recommandation reportée** par le rapport :
`Ajouter [[outils-llm|Mistral]] à la première occurrence (L{n})`.

---

## Cas 5 — Négatif : wikilink présent APRÈS la première mention → manquement

**MD de test :**

```markdown
## Souveraineté EU

Le modèle Mistral est intéressant. On en reparle dans [[outils-llm]] plus bas.
```

**Score attendu :** R11 MANQUEMENT (mention Mistral en clair PRÉCÈDE le
wikilink — R11 exige le wikilink AU PLUS TARD à la première occurrence)
**Score obtenu :** R11 MANQUEMENT (`min(wikilink_positions) > naked_pos`
donc condition `wikilink_positions and min(...) <= naked_pos` est fausse
→ manquement reporté)
**Diagnostic :** ✅ Comportement conforme. Couvert par
`test_wikilink_after_first_mention`. **Cas-école** parfaitement observé
dans `deploiement/dep-01.md` L65 : `(ChromaDB, Qdrant, pgvector — cf.
[[outils-vector-db]])` — les 3 mentions précèdent le wikilink → 3
manquements reportés (R11 correct).

---

## Synthèse validation

| Cas | Type | Outil | Attendu | Obtenu | Diagnostic |
|---|---|---|---|---|---|
| 1 | Positif | Mistral après wikilink `[[outils-llm]]` | OK | OK | ✅ |
| 2 | Positif | Mistral DANS `[[outils-llm\|Mistral]]` | OK | OK | ✅ |
| 3 | Positif | Aucune mention | OK silencieux | OK silencieux | ✅ |
| 4 | Négatif | Mistral nu, sans wikilink | Manquement | Manquement | ✅ |
| 5 | Négatif | Mistral nu AVANT wikilink | Manquement | Manquement | ✅ |

**Score validation : 5/5 conforme.** Règle R11 prête pour intégration
audit-pipeline + rejeu Lot I.

---

## Risques de faux positifs identifiés (et mitigations en place)

1. **Mots anglais ambigus** (« Make », « Llama ») : mitigés par **match
   case-sensitive** sur les aliases canoniques tels qu'extraits du H2 source
   (« Make » majuscule, pas « make »). Couvert par `test_case_sensitive`.
2. **Sous-chaînes de noms composés** (« GPT » dans « ChatGPT ») : mitigés
   par **word boundary stricte** (`(?<![\w-])...(?![\w-])`) — `\bGPT\b` ne
   matche pas l'intérieur de `ChatGPT`. Couvert par `test_word_boundary_chatgpt`.
3. **Noms à tiret** (« Pleias-RAG ») : le tiret n'est pas un word char, donc
   `\bPleias-RAG\b` matche correctement la chaîne complète. Couvert par
   `test_word_boundary_hyphen`.
4. **Aliases multiples par H2** (« Kimi K2 / K2.6 ») : extraits par split
   sur ` / `, les deux variantes mappent vers la même fiche/ancre. Couvert
   par `test_aliases_slash` + `test_multiple_aliases`.
5. **Mentions dans le frontmatter YAML** : exclues car on travaille sur le
   body post-`split_frontmatter`, tout en reportant les numéros de ligne
   ajustés au texte complet. Couvert par
   `test_line_number_includes_frontmatter`.
6. **Auto-référence de la fiche source** : R11 ne s'applique pas à
   `outils-llm.md` lui-même (skip basename `outils-*`). Couvert par
   `test_outils_fiche_self_excluded`.

---

## Résultat audit réel post-validation

Exécution sur le vault complet (32 MD, dont 6 fiches outils-*) :

- **Fiches outils parsées** : 6
- **Outils canoniques détectés** : 36
- **Fichiers MD audités** : 32 (26 effectivement scannés, 6 fiches outils-*
  auto-exclues)
- **Fichiers avec manquements R11** : 21
- **Manquements R11 totaux** : 85
- **Mentions outils correctes (wikilink présent)** : 3

Rapport complet : `rag-prep/reports/audit-md-rag-R11-s2.8.md` (Markdown) +
`rag-prep/reports/audit-md-rag-R11-s2.8.json` (JSON).

**Note Cowork** : la **dérive massive** (85 manquements) est attendue et
**ne bloque pas** S2.8. Elle reflète la production rapide vagues 5-7 sans
discipline R11 (la règle n'était pas implémentée avant aujourd'hui). Les
patches éditoriaux relèvent du Cowork (D-022/D-030) ; le brief S2.8 §4.5
prévoit l'intégration en fin de sprint ou le déférement S2.9 selon volume.
85 manquements ≈ 30-60 min de patch éditorial groupé (1 wikilink par
première occurrence par MD, modification ciblée).

---

*Document produit Plateforme-side conformément SPEC v2.2 §Validation manuelle.
Reproductible via `pytest rag/code/audit/test_citation_audit.py` (28 tests
verts) + `python3 rag/code/audit/citation_audit.py`.*
