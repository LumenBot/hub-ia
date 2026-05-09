# Brief Claude Code — Hub IA Learning Center (audit qualité v3.5.1)

**Auteur :** Blaise Cavalli — Startup Manager Quai Alpha (Quest for Change)
**Date :** mai 2026
**Repo :** https://github.com/LumenBot/hub-ia
**Branche cible :** main
**Hébergement :** GitHub Pages
**Itération précédente :** v3.5 (architectures.html + 5 RetEx Bpifrance + refresh stats macro + navigateurs agentiques + 12 anti-patterns PR-01)
**Nature de cette itération :** AUDIT QUALITÉ AUTONOME (pas d'ajout de contenu, uniquement consolidation et corrections)

---

## 0. Contexte et objectif

Au fil des itérations v3 → v3.5, plusieurs petits écarts de qualité se sont accumulés sur le site :
- Incohérences numériques cross-pages (« 22 modules » vs « 23 modules » vs « 22 cas d'usage »)
- Sources non datées ou non liées
- Jargon technique non explicité
- Désynchronisations visuelles (head banner, padding, footer)
- Liens potentiellement morts entre les CU et les PR

**Cette itération est dédiée à corriger ces écarts.** Pas d'ajout de contenu, pas de nouveau module, pas de nouvelle ressource. **Uniquement de la consolidation.**

**Objectif final** : préparer un terrain propre avant l'itération v3.6 (qui ajoutera 4 nouveaux livrables : CU-023, CU-024, CU-027, PR-07).

**Tu travailles en autonomie** : Blaise ne sera pas en revue continue pendant cette itération. Tu suis ce brief, tu produis le rapport d'audit, tu appliques les corrections, tu pousses la PR.

---

## 1. Préalable obligatoire — lecture de RULES-IMPLEMENTATION.md

**AVANT toute action de code**, tu dois :

1. Lire **intégralement** le fichier `site-web-prep/RULES-IMPLEMENTATION.md` (référentiel non négociable créé pour cette itération).
2. Comprendre que toutes les règles qui y figurent sont **prescriptives**, pas indicatives.
3. Si tu détectes pendant l'audit que le `RULES.md` est imprécis sur un point, **propose un amendement dans ton rapport d'audit** plutôt que d'interpréter de ton propre chef.

**Ce fichier est la grille de lecture de tout l'audit.** Toutes les corrections que tu vas appliquer doivent dériver d'une règle explicite du `RULES.md`. Si tu corriges un truc qui n'a pas de règle associée, tu l'écris dans le rapport (point d'amendement à proposer à Blaise).

---

## 2. Méthode de l'audit — 5 lots à exécuter dans l'ordre

### Lot 1 — Audit cohérence numérique cross-site (1-2 h)

**Référence RULES** : section 1.2

**Méthode** :

1. Exécuter sur tout le repo :
   ```bash
   grep -rn "22 modules\|23 modules\|24 modules\|22 cas d'usage\|23 cas d'usage" .
   grep -rn "6 préalables\|5 préalables\|7 préalables" .
   grep -rn "76 fiches\|75 fiches\|77 fiches\|76 outils" .
   grep -rn "CU-001 → CU-022\|CU-001 → CU-021\|CU-001 → CU-023" .
   grep -rn "CU-001 à CU-022\|CU-001 à CU-021" .
   grep -rn "PR-01 → PR-06\|PR-01 → PR-05\|PR-01 à PR-06" .
   grep -rn "5 entrées\|6 entrées\|4 entrées" .
   ```

2. **Valeurs de référence (mai 2026 v3.5)** :
   - 22 modules CU
   - 6 préalables PR
   - 76 fiches outils
   - 4 patterns d'architecture + 1 hybride
   - 6 axes pédagogiques
   - 6 entrées de nav (Préalables, Architectures, Modules, Ressources, Axes, À propos)

3. **Pour chaque écart détecté** : noter dans le rapport (page + ligne + valeur trouvée + valeur attendue), corriger dans le commit dédié au Lot 1.

4. **Vérifier** que les méta-descriptions HTML et les titres de page sont synchronisés avec ces chiffres.

**Livrable** : section « 1. Cohérence numérique » du rapport d'audit + commit `fix(v3.5.1): cohérence numérique cross-site`.

---

### Lot 2 — Audit sourcing & véracité (2-3 h)

**Référence RULES** : section 1.1

**Méthode** :

1. Lister **tous les chiffres** présents dans le site (regex sur `[0-9]+\s*%` et `\+[0-9]+\s*%` et nombres en gras dans `<strong>`).

2. Pour chaque chiffre, vérifier :
   - **Source citée ?** (institution + date)
   - **Lien vers la source ?** (`<a href>` cliquable)
   - **Source vérifiable ?** (URL valide, pas un chemin rompu)

3. **Sources autorisées** (référence) :
   - MIT Sloan / NANDA (2025)
   - Microsoft New Future of Work Report (2025)
   - France Num (baromètre 2025)
   - Bpifrance Le Lab (2025-2026)
   - PwC AI Jobs Barometer (2024)
   - AdvisoryX / DXC (janvier 2026)
   - McKinsey State of AI (2025)
   - INSEE, Pôle emploi, OECD

4. **Sources à éliminer** : tout chiffre sans source, blogs marketing d'éditeurs, posts LinkedIn cités comme source primaire, hallucinations détectables (chiffre rond suspect, étude non vérifiable).

5. **En cas de doute sur un chiffre** : marquer dans le rapport « ⚠️ À vérifier par Blaise » et **ne pas supprimer** sans validation. Mieux vaut signaler que de couper.

**Livrable** : section « 2. Sourcing » du rapport + commit `fix(v3.5.1): sourcing — liens et dates ajoutés` (uniquement les corrections sûres).

---

### Lot 3 — Audit jargon & niveau de langue (1-2 h)

**Référence RULES** : section 1.3

**Méthode** :

1. Liste des termes techniques à grep et vérifier la glose à la 1re occurrence dans chaque page :
   ```
   RAG, MVP, POC, fine-tuning, embeddings, LLM, API, SaaS,
   on-premise, open-source, fine-tuning, prompt, token,
   cloud souverain, SecNumCloud, vector store, RLHF, agent,
   benchmark, pipeline, scaling, monitoring, observabilité
   ```

2. Pour chaque page, vérifier :
   - 1re occurrence d'un terme technique → glose présente ?
   - Si non → ajouter la glose en se basant sur la table de RULES.md section 1.3.2.

3. Repérer les codes internes visibles dans l'UX (RULES section 1.3.6) :
   ```bash
   grep -rn ">PR-0[1-6]<\|>CU-0[0-2][0-9]<\|>A[1-4]<" --include="*.html" .
   ```
   Tout `PR-XX` / `CU-XXX` / `A1`-`A4` qui apparaît **dans un titre, une card, un badge visible** doit être remplacé par le titre métier. Les ancres URL et les commentaires HTML peuvent rester.

4. **Cas particulier** : sur la page `architectures.html`, les noms `A1 / A2 / A3 / A4` sont **acceptés** car ce sont les noms canoniques des patterns (validés par Blaise v3.5). Ils peuvent rester visibles.

5. Repérer les phrases trop longues (> 35 mots) : à signaler dans le rapport, pas à corriger automatiquement (réécriture éditoriale = compétence Cowork, pas Claude Code).

**Livrable** : section « 3. Jargon & niveau de langue » du rapport + commit `fix(v3.5.1): gloses terminologiques + retrait codes internes UX`.

---

### Lot 4 — Audit harmonisation visuelle cross-pages (1 h)

**Référence RULES** : section 1.4

**Méthode** :

1. **Nav principale** : extraire le HTML de la nav sur toutes les pages, comparer. Toute divergence (ordre, libellé, classe `nav-link-active` mal placée) est un écart à corriger.

2. **Head banner** : vérifier hauteur, logo, accroche, comportement sticky. Idéal : capture d'écran headless via puppeteer ou playwright pour comparaison automatique. Sinon, lecture du HTML/CSS pour vérifier que les pages utilisent le même gabarit.

3. **Footer** : extraire et comparer. Doit être identique partout (mention QFC, année, lien repo, lien à propos, lien méthodologie).

4. **Composants structurants** : chaque module CU et PR a-t-il bien :
   - Executive summary en tête (gradient bleu marine + 4 takeaways + stats grid + callout when) ?
   - Sticky TOC fonctionnelle ?
   - Reading progress bar ?
   - Sections numérotées avec icônes ?

5. **CSS** : repérer les styles inline qui pourraient être mutualisés dans `module-v3.css`. À documenter dans le rapport, **ne pas refactorer automatiquement** (refactor CSS = risque de régression visuelle, à valider).

**Livrable** : section « 4. Harmonisation visuelle » du rapport + commit `fix(v3.5.1): harmonisation nav / head / footer cross-pages`.

---

### Lot 5 — Audit liens & parcours (30 min - 1 h)

**Méthode** :

1. **Liens internes morts** : scanner tous les `href="..."` internes (pas `http://`), vérifier que les fichiers cibles existent. Idéal : script Node ou Python qui crawle le site déployé.

2. **Liens externes** : vérifier que les sources citées (MIT, Microsoft, Bpifrance, etc.) ont des URL valides. Si une URL renvoie 404, marquer dans le rapport (« ⚠️ source à actualiser »), ne pas supprimer.

3. **Liens croisés CU ↔ PR ↔ Architectures** :
   - Les 6 PR doivent linker vers les CU pertinents (cf. brief v3.4 section 8.2)
   - Les 5 modules sensibles (CU-007, CU-008, CU-013, CU-020, CU-021) doivent linker vers `architectures.html` (cf. brief v3.5 Lot 7)
   - La page `architectures.html` doit être accessible depuis la nav de toutes les pages (Lot 6 v3.5)

4. **Ancres** : vérifier que `#a1`, `#a2`, `#a3`, `#a4`, `#decision` sur `architectures.html` existent et fonctionnent.

**Livrable** : section « 5. Liens & parcours » du rapport + commit `fix(v3.5.1): liens morts et liens croisés`.

---

## 3. Production du rapport d'audit (livrable obligatoire)

Format : `site-web-prep/audit-v3.5.1-mai2026.md`

**Structure attendue** :

```markdown
# Audit qualité Hub IA — v3.5.1 (mai 2026)

## Synthèse exécutive

- Nombre total d'écarts détectés : XX
- Nombre d'écarts corrigés automatiquement : XX
- Nombre d'écarts signalés pour validation Blaise : XX
- Estimation d'effort résiduel pour Blaise : XX h

## 1. Cohérence numérique
[liste des écarts trouvés + corrections appliquées]

## 2. Sourcing
[chiffres sans source + chiffres avec source ajoutée + chiffres à valider]

## 3. Jargon & niveau de langue
[gloses ajoutées + codes internes retirés + phrases trop longues signalées]

## 4. Harmonisation visuelle
[divergences nav / head / footer corrigées]

## 5. Liens & parcours
[liens morts + liens croisés corrigés]

## 6. Propositions d'amendement à RULES.md
[éventuelles règles imprécises détectées pendant l'audit]

## 7. Recommandations pour v3.6
[points d'attention à propager dans le brief v3.6]
```

Ce rapport est **livré dans la PR** et constitue la trace écrite de l'audit. Blaise le relit avant merge.

---

## 4. Workflow recommandé

1. **Vérifier que la PR v3.5 est mergée** sur main avant de commencer.
2. **Créer une branche `chore/v3.5.1-audit-qualite`**.
3. **Lire RULES-IMPLEMENTATION.md** (préalable obligatoire).
4. **Exécuter les Lots 1 → 5 dans l'ordre**, un commit par lot.
5. **Produire `audit-v3.5.1-mai2026.md`** au fur et à mesure (un commit final pour le rapport).
6. **Tests croisés** Chrome / Firefox / Safari, mobile + desktop, sticky TOC fonctionnel sur toutes les pages avec contenu long.
7. **PR avec description structurée** :
   - Lien vers ce brief
   - Lien vers le rapport d'audit
   - Liste des commits (un par lot)
   - Liste des points signalés pour validation Blaise (s'il y en a)

---

## 5. Règles de prudence pendant l'audit autonome

Tu travailles seul, sans revue continue. Trois principes pour ne pas créer de régression :

**Règle de prudence 1 — Quand tu hésites, tu signales, tu ne corriges pas.**
Mieux vaut un rapport qui liste 30 points à valider qu'un commit qui en a corrigé 30 dont 5 mal interprétés.

**Règle de prudence 2 — Tu ne touches pas au design system.**
`module-v3.css`, `module-v3.js` : tu ne modifies pas leur structure. Tu peux corriger des classes mal appliquées sur les pages, mais tu ne refactores pas la feuille de style centrale.

**Règle de prudence 3 — Tu ne réécris pas le contenu éditorial.**
Si un paragraphe est mal formulé, tu le signales dans le rapport (« phrase à réécrire »). Tu ne le réécris pas. La réécriture est une compétence Cowork (côté Blaise).

**Règle de prudence 4 — Tu commits par petits incréments.**
Un commit par lot, message clair (`fix(v3.5.1): cohérence numérique - 12 écarts corrigés`). Pas de commit géant en fin de mission.

**Règle de prudence 5 — En cas de blocage, tu t'arrêtes et tu documentes.**
Si tu rencontres un cas qui ne rentre dans aucune règle, tu écris dans le rapport « ⚠️ À discuter avec Blaise » et tu passes au point suivant.

---

## 6. Estimation effort consolidée

| Lot | Sujet | Effort estimé |
|---|---|---|
| Lot 1 | Cohérence numérique cross-site | 1-2 h |
| Lot 2 | Sourcing & véracité | 2-3 h |
| Lot 3 | Jargon & niveau de langue | 1-2 h |
| Lot 4 | Harmonisation visuelle | 1 h |
| Lot 5 | Liens & parcours | 30 min - 1 h |
| Production rapport | `audit-v3.5.1-mai2026.md` | 1 h (en continu) |
| **Total** | | **6-10 h** |

C'est une itération **plus courte que v3.5** (19-24 h) car il n'y a pas de production de contenu — uniquement de l'audit + correction.

---

## 7. Décisions explicites de NE PAS faire dans cette itération

- **Pas d'ajout de contenu** (pas de nouveau module, pas de nouvelle fiche outil, pas de nouvelle ressource).
- **Pas de refactor du design system** (`module-v3.css`, `module-v3.js` restent tels quels).
- **Pas de réécriture éditoriale** (signalement uniquement).
- **Pas de changement de structure de navigation** (la nav 6 entrées reste).
- **Pas de modification de RULES.md sans signalement préalable** dans le rapport (point 6 du rapport).

---

## 8. Validation finale avant PR

Avant d'ouvrir la PR, vérifier :

```
☐ RULES.md a bien été lu en intégralité avant de commencer.
☐ Les 5 lots ont été exécutés dans l'ordre.
☐ Chaque lot a fait l'objet d'un commit séparé.
☐ Le rapport audit-v3.5.1-mai2026.md est complet et structuré.
☐ Tous les écarts non corrigés sont signalés dans le rapport (pas un dans le commit, l'autre dans le rapport).
☐ Aucune modification de RULES.md n'a été commitée (uniquement signalement section 6 du rapport).
☐ Les tests croisés (Chrome / Firefox / Safari, mobile + desktop) ont été effectués.
☐ La description de PR pointe vers ce brief + le rapport d'audit.
```

---

## 9. Fichiers de référence (dans `site-web-prep/`)

- **Référentiel non négociable** : `RULES-IMPLEMENTATION.md` ← À LIRE EN PRÉALABLE
- **Brief de cette itération** : `BRIEF-CLAUDE-CODE-v3.5.1-audit.md` (ce fichier)
- **Brief v3.5** (référence pour comprendre les ajouts récents) : `BRIEF-CLAUDE-CODE-v3.5-passation.md`
- **Brief v3.4** (référence) : `BRIEF-CLAUDE-CODE-v3.4-passation.md`
- **Patches v3.5** (référence pour comprendre les valeurs cibles) : `patches-v3.5-mai2026.md`
- **Page Architectures** (référence pour les exceptions UX A1-A4) : `mockup/architectures.html`

---

## 10. Contact

Pour toute question pendant l'audit : Blaise Cavalli — blaise.cavalli@questforchange.eu

**Tu travailles en autonomie sur cette itération.** Si tu es bloqué, **arrête-toi et documente** plutôt que d'interpréter. Blaise relira le rapport et tranchera les cas signalés.

**Bonne mission, et merci pour le travail !**

---

*Brief produit par Cowork (Claude desktop) le 9 mai 2026. Cette itération v3.5.1 est une itération d'audit qualité autonome qui prépare v3.6 (CU-023 / CU-024 / CU-027 / PR-07).*
