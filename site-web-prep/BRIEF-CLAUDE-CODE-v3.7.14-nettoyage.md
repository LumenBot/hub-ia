# Brief Claude Code — Hub IA Learning Center (v3.7.14 — nettoyage technique)

**Auteur :** Blaise Cavalli — Startup Manager Quai Alpha (Quest for Change)
**Repo :** https://github.com/LumenBot/hub-ia
**Branche cible :** main
**Itération précédente :** v3.7.13 (sommaire emojis fallback, RULES v1.5.12)
**Nature de cette itération :** NETTOYAGE TECHNIQUE — adresser les 3 écarts résiduels signalés dans le rapport `site-web-prep/rapport-etat-post-v3.7.md` (§ 8.1). Pas d'ajout de contenu, pas de nouveau module. Préparation du terrain propre avant v3.8 (qui apportera : patch réglementaire AI Act Article 50, enrichissements 8 modules, 4 fiches outils, nouveau CU-026 Gouvernance des agents IA).

---

## 0. Contexte court

Le rapport `rapport-etat-post-v3.7.md` produit récemment a identifié 3 priorités opérationnelles ouvertes après les 13 PRs correctives v3.7.1 → v3.7.13. Cette itération v3.7.14 les traite **en autonomie** et **dans l'ordre suggéré par le rapport § 8.3** (Templates → Préalables → Migration `.case-deep-actor` → Lots éditoriaux substantiels — ces derniers en v3.8).

**Tu travailles en autonomie**. Aucun appel à Cowork. Rapport de mission obligatoire à la fin.

---

## 1. Préalable obligatoire

**AVANT toute action de code**, tu dois :

1. Lire `site-web-prep/RULES-IMPLEMENTATION.md` v1.5.12 (référentiel actuel).
2. Lire `site-web-prep/rapport-etat-post-v3.7.md` (rapport que tu as produit toi-même — base de cette itération).
3. Te référer à `modules/cu-008-knowledge-base-rag.html` comme référence canonique.
4. **Exécuter `python3 site-web-prep/audit-global.py`** pour confirmer l'état de départ (0 hit attendu sur les 13 règles automatisées).

---

## 2. Méthode — 5 lots dans l'ordre

### Lot 1 — Mise à jour `_template-auto-diagnostic.html` (15-30 min)

**Référence rapport** : § 7.2 et § 8.1 priorité 1.

**Problème identifié** : la nav du template contient encore `Préalables / Architectures / Modules / Ressources / À propos` (nav obsolète v3.5-v3.6). La nav canonique v3.7+ est `Préalables / Architectures / Modules / Déploiement / Ressources`.

**Méthode** :

1. Ouvrir `modules/_template-auto-diagnostic.html`.
2. Repérer le bloc `<div class="nav-links">` et le mettre à jour pour refléter la nav 5 entrées canoniques :
   ```html
   <a href="../prealables.html" class="nav-link">Préalables</a>
   <a href="../architectures.html" class="nav-link">Architectures</a>
   <a href="../index.html#modules" class="nav-link nav-link-active">Modules</a>
   <a href="../deploiement.html" class="nav-link">Déploiement</a>
   <a href="../ressources.html" class="nav-link">Ressources</a>
   ```
   Retirer toute mention `À propos` de la nav. La page Home reste accessible via `<a href="../index.html">` du logo / nav-brand.
3. Vérifier que la section finale `<section id="ressources">` du template respecte le **Schéma A** (4 sous-rubriques externes uniquement : Articles de fond / Tutoriels / Documentation officielle / Communautés + callout vers `ressources.html#bibliographie`). Si ce n'est pas le cas, corriger.
4. Vérifier que le h1 du template a un emoji ouvrant placeholder (ex : `<h1>[EMOJI] [TITRE]</h1>` — tu peux laisser le placeholder).
5. Mettre à jour le commentaire d'en-tête du template si applicable (mention version ou date).

**Cas similaires** : vérifier rapidement `_template-etude-de-cas.html` et `_template-quiz.html` (fragments partiels, pas de nav d'après le rapport § 7.1). Si ces deux templates contiennent des references à la nav obsolète ou des renvois `À propos`, les corriger aussi. Sinon, laisser tel quel.

**Livrable Lot 1**.
- Commit : `chore(v3.7.14): mise à jour _template-auto-diagnostic.html (nav 5 entrées canoniques)`

---

### Lot 2 — Nettoyage des renvois internes dans section finale des 6 préalables (1-2 h)

**Référence rapport** : § 6.2 anti-pattern 6 et § 8.1 priorité 2.

**Problème identifié** : 19 renvois internes (vers CU-XXX, autres PR-YY) restent à l'intérieur des sections finales `<section id="ressources">` des 6 préalables PR-01 à PR-06. Pattern v3.4 que RULES v1.3 § 1.5.6 a interdit, mais qui n'a jamais été nettoyé sur les préalables. PR-07 a déjà été nettoyé en v3.6.3.

**Détail par préalable** (extrait du rapport § 6.2 anti-pattern 6) :
- `prealables/pr-01-maturite-organisationnelle.html` : 4 renvois (CU-020, CU-014, PR-02, PR-03)
- `prealables/pr-02-preables-data-si.html` : 5 renvois (CU-008, CU-013, CU-014, PR-01, PR-03)
- `prealables/pr-03-maturite-humaine-formation.html` : 3 renvois (CU-020, CU-007)
- `prealables/pr-04-marche-ia-emploi.html` : 2 renvois
- `prealables/pr-05-securite-ia.html` : 3 renvois (CU-020, CU-014)
- `prealables/pr-06-qualite-code-ia.html` : 2 renvois (CU-015)

**Méthode pour chaque préalable** :

1. Localiser la section `<section id="ressources">` finale.
2. Repérer les sous-rubriques internes qui sortent du **Schéma A** (typiquement « Modules complémentaires », « Préalables associés », ou « Pour aller plus loin sur le Hub »).
3. **Déplacer ces renvois internes dans le corps du préalable** (dans une section existante contextuellement pertinente, ou en fin de la dernière section avant la section ressources finale). Les renvois doivent rester contextualisés (« Pour cadrer ta data avant de te lancer, voir [titre métier] »), pas en simple liste à puces.
4. **Garder uniquement les 4 sous-rubriques externes Schéma A** dans `<section id="ressources">` : 📰 Articles de fond / 🎓 Tutoriels & cas pratiques / 📚 Documentation officielle & études / 👥 Communautés & veille + callout en tête vers `ressources.html#bibliographie`.
5. Si certaines sous-rubriques Schéma A sont vides après nettoyage, **les conserver avec un placeholder** (« Tutoriels et démos vidéo : recherche par mot-clé sur la chaîne YouTube de l'éditeur ») plutôt que de les supprimer (cohérence visuelle).

**Référence canonique** : `modules/cu-008-knowledge-base-rag.html` pour le rendu cible Schéma A.

**Règle de prudence** : si un renvoi interne est déjà mentionné dans le corps du préalable (doublon avec section finale), il suffit de retirer de la section finale sans rien réécrire.

**Livrable Lot 2**.
- Commit : `refactor(v3.7.14): nettoyage renvois internes section finale 6 préalables (Schéma A strict)`
- Vérification : `audit-global.py` reste à 0 hit après nettoyage.

---

### Lot 3 — Migration `.case-deep-actor.warm` (1 h)

**Référence rapport** : § 6.2 anti-pattern 4 et § 8.1 priorité 3.

**Problème identifié** : 3 modules contiennent des styles inline avec couleurs hardcodées sur des `.case-deep-actor` thématiques (ambre/orange) :
- `modules/cu-002-assistant-redactionnel.html` lignes 254-255 : `style="background: #FDF4DC; border-left-color: #B89030;"` et `style="color: #7A5C20;"`
- `modules/cu-003-cr-reunion.html` lignes 243-244 : idem
- `modules/cu-006-leads-chatbot.html` ligne 272+ : idem

**Méthode** :

1. **Ouvrir `css/module-v3.css`** et ajouter une variante centralisée `.case-deep-actor.warm` (ou `.case-deep-actor--warm` si la convention BEM est plus cohérente avec le reste du CSS) :
   ```css
   .case-deep-actor.warm {
     background: var(--color-n2-bg);              /* #FDF4DC */
     border-left-color: var(--color-n2-border);   /* #B89030 */
     color: var(--color-n2-fg);                   /* #7A5C20 */
   }
   ```
   Utiliser les variables CSS du design system existant. Les valeurs hexa sont à mapper aux variables `--color-n2-*` déjà définies dans `style.css` (niveau N2 jaune). Vérifier la correspondance exacte avant commit.

2. **Sur cu-002, cu-003, cu-006** :
   - Repérer chaque bloc `.case-deep-actor` avec `style="background: #FDF4DC; ..."` ou `style="color: #7A5C20"`.
   - Remplacer par `class="case-deep-actor warm"` (ajout du modificateur `warm`).
   - Supprimer l'attribut `style` correspondant.
   - Vérifier que le rendu visuel reste identique (variables CSS doivent produire le même rendu que les hexa).

3. **Tester visuellement** sur les 3 modules : le rendu doit être strictement identique à avant migration (test visuel humain ou capture si dispo).

**Variantes éventuelles** : si tu identifies d'autres tons utiles (`.case-deep-actor.cool`, `.case-deep-actor.danger`), tu peux les pré-définir dans `module-v3.css` mais **ne les déploie que si déjà utilisés ailleurs**. Sinon, garder uniquement `.warm` pour cette itération.

**Livrable Lot 3**.
- Commit : `refactor(v3.7.14): migration .case-deep-actor.warm centralisée (cu-002, cu-003, cu-006)`
- Vérification : `audit-global.py` reste à 0 hit + audit visuel sur les 3 modules.

---

### Lot 4 — Mise à jour en-tête RULES (5 min)

**Référence rapport** : § 4.1.

**Problème identifié** : l'en-tête de `site-web-prep/RULES-IMPLEMENTATION.md` indique `**Version :** 1.5 (mai 2026)` alors que l'historique en bas de fichier liste les sous-versions jusqu'à v1.5.12.

**Méthode** :

1. Ouvrir `site-web-prep/RULES-IMPLEMENTATION.md`.
2. Mettre à jour la ligne d'en-tête :
   - Avant : `**Version :** 1.5 (mai 2026)`
   - Après : `**Version :** 1.5.13 (mai 2026)`
3. Ajouter en bas du fichier dans la section « Historique » une entrée v1.5.13 :
   ```markdown
   - **v1.5.13** — itération v3.7.14 : nettoyage technique (template auto-diag aligné nav canonique, Schéma A strict sur 6 préalables, migration `.case-deep-actor.warm` centralisée). Aucune nouvelle règle structurelle introduite.
   ```

**Livrable Lot 4**.
- Commit : `chore(v3.7.14): RULES en-tête 1.5 → 1.5.13 + entrée historique`

---

### Lot 5 — Audit final + rapport mission (30 min)

**Méthode** :

1. **Exécuter** :
   ```bash
   python3 site-web-prep/audit-global.py
   ```
   Vérifier `Total hits : 0` après les 4 lots précédents.

2. **Audit visuel manuel** des 3 anti-patterns non automatisés mentionnés en § 6.2 du rapport d'état :
   - Anti-pattern 4 (couleurs hardcodées) : 0 hit attendu après Lot 3
   - Anti-pattern 6 (renvois internes section finale) : 0 hit attendu après Lot 2
   - Tous les autres anti-patterns § 1.5.3 doivent rester à 0 hit

3. **Tests croisés** Chrome / Firefox / Safari, mobile + desktop sur :
   - 1 préalable touché par Lot 2 (ex : PR-01)
   - 1 module touché par Lot 3 (ex : CU-002)
   - 1 page template touchée par Lot 1 (`_template-auto-diagnostic.html` ouvert via file://)

4. **Production du rapport** dans `site-web-prep/rapport-mission-v3.7.14.md` (même structure que rapports v3.7, v3.6.3) :
   - Synthèse exécutive (lots traités, écarts résolus)
   - Détail par lot avec preuves (extraits commits, résultats audit)
   - Écarts résiduels (s'il en reste — préciser pourquoi non traités cette itération)
   - Recommandations pour v3.8 (qui sera l'itération éditoriale majeure suivante)

**Livrable Lot 5**.
- Commit : `chore(v3.7.14): rapport de mission + checklist audit finale`

---

## 3. Estimation effort consolidée

| Lot | Sujet | Effort estimé |
|---|---|---|
| Lot 0 | Préalable (lecture RULES + rapport état) | 15 min |
| Lot 1 | Template _template-auto-diagnostic.html | 15-30 min |
| Lot 2 | Nettoyage 6 préalables (Schéma A) | 1-2 h |
| Lot 3 | Migration `.case-deep-actor.warm` | 1 h |
| Lot 4 | RULES en-tête + historique v1.5.13 | 5 min |
| Lot 5 | Audit final + rapport mission | 30 min |
| **Total** | | **~3-4 h** |

Itération courte et focalisée — la plus petite depuis v3.6.3.

---

## 4. Workflow recommandé

1. **Vérifier que la branche est à jour** avec `origin/main` (v3.7.13 mergée).
2. **Créer une branche `chore/v3.7.14-nettoyage`**.
3. **Lire RULES v1.5.12 + rapport état post-v3.7** (Lot 0).
4. **Exécuter les Lots 1 → 5 dans l'ordre** indiqué, un commit par lot.
5. **PR avec description structurée** :
   - Lien vers ce brief
   - Lien vers le rapport d'état post-v3.7 (qui motive cette itération)
   - Liste des commits (un par lot)
   - Lien vers le rapport mission `rapport-mission-v3.7.14.md`
   - Confirmation `audit-global.py` à 0 hit

---

## 5. Règles de prudence pendant l'exécution autonome

Identiques aux briefs précédents (autonomie, signalement plutôt qu'interprétation, pas de réécriture éditoriale, commits incrémentaux, arrêt et documentation en cas de blocage).

**Spécifique v3.7.14** :
- **Sur Lot 2** : ne pas réécrire le contenu éditorial des préalables. Le but est uniquement de déplacer les renvois internes hors de la section finale, pas d'enrichir ou de reformuler.
- **Sur Lot 3** : si les variables CSS `--color-n2-*` du design system ne produisent pas exactement le rendu hexa actuel, **signaler dans le rapport** plutôt que d'inventer des nouvelles variables.
- **Sur Lot 1** : si les 2 autres templates (`_template-etude-de-cas.html`, `_template-quiz.html`) sont des fragments partiels sans nav (comme le suggère le rapport § 7.1), **les laisser tels quels** sauf si tu identifies un problème manifeste.

---

## 6. Décisions explicites de NE PAS faire dans cette itération

- **Aucun ajout de contenu éditorial** (modules, préalables, fiches outils, sections).
- **Aucune modification des chiffres macro** (95 % MIT NANDA, etc.) — sauf si une source citée a été dépréciée et qu'il faut la corriger.
- **Pas de refonte structurelle** au-delà des 3 priorités du rapport.
- **Pas d'ajout de nouvelles règles d'audit dans `audit-global.py`** — ce sera traité en v3.8 ou plus tard.

---

## 7. Validation finale avant PR

```
☐ RULES v1.5.12 lu en intégralité avant de commencer.
☐ Rapport état post-v3.7 lu en intégralité.
☐ audit-global.py exécuté avant le démarrage (0 hit confirmé).
☐ Les 5 lots ont été exécutés dans l'ordre.
☐ Chaque lot a fait l'objet d'un commit séparé.
☐ Le rapport rapport-mission-v3.7.14.md est complet.
☐ audit-global.py exécuté à la fin (0 hit confirmé).
☐ Anti-patterns 4 et 6 vérifiés manuellement (0 hit confirmé).
☐ Tests croisés Chrome / Firefox / Safari, mobile + desktop OK.
☐ RULES en-tête mis à jour de 1.5 à 1.5.13 + entrée historique.
☐ Description de PR pointe vers ce brief + rapport mission + rapport état.
```

---

## 8. Fichiers de référence

- **Brief de cette itération** : `BRIEF-CLAUDE-CODE-v3.7.14-nettoyage.md` (ce fichier)
- **Rapport d'état post-v3.7** (motivation) : `rapport-etat-post-v3.7.md`
- **Référentiel actuel** : `RULES-IMPLEMENTATION.md` v1.5.12 → à amender en v1.5.13 (Lot 4)
- **Référence canonique** : `modules/cu-008-knowledge-base-rag.html`
- **Garde-fou automatisé** : `site-web-prep/audit-global.py`

---

## 9. Annonce de v3.8 (pour mémoire)

Une fois v3.7.14 mergée, Cowork produira en parallèle la matière éditoriale **v3.8 « Expansion réglementaire et nouveau module »**. Périmètre prévu :

- Patch réglementaire AI Act Article 50 + Omnibus VII (sur CU-020 + CU-002 / CU-009 / CU-010 / CU-019)
- Mise à jour calendrier facturation électronique sur CU-024
- Enrichissements techniques : CU-008 (LLM Wiki forks), CU-014 (agent=employé), DEP-02 (itération continue), DEP-05 (data plane)
- Actualisations chiffrées : PR-01 (95 % échec orga), PR-04 (Baromètre France Num 2025)
- 4 nouvelles fiches outils : Hermes Agent, SuperSplat, AAFLOW, Beever Atlas
- **Nouveau module CU-026 — Gouvernance des agents IA**

→ La base nettoyée par v3.7.14 facilitera cette itération.

---

## 10. Contact

Pour toute question pendant l'exécution : Blaise Cavalli — blaise.cavalli@questforchange.eu

**Tu travailles en autonomie sur cette itération.** Si tu es bloqué, **arrête-toi et documente** plutôt que d'interpréter.

**Bonne mission, et merci pour le travail !**

---

*Brief produit par Cowork. Itération v3.7.14 = nettoyage technique focalisé sur les 3 priorités du rapport d'état post-v3.7.13. Prépare le terrain pour la v3.8 éditoriale majeure.*
