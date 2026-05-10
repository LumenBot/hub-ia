# Brief Claude Code — Hub IA Learning Center (correctifs v3.6.3)

**Auteur :** Blaise Cavalli — Startup Manager Quai Alpha (Quest for Change)
**Date :** mai 2026
**Repo :** https://github.com/LumenBot/hub-ia
**Branche cible :** main
**Hébergement :** GitHub Pages
**Itération précédente :** v3.6.2 (harmonisation autonome — 7 lots, 8 commits)
**Nature de cette itération :** CORRECTIFS RÉSIDUELS — incohérences résiduelles signalées par Blaise après audit visuel + 5 écarts ouverts par v3.6.2 + amendements RULES v1.3 → v1.4. Pas de nouveau contenu. Préparation du terrain propre avant v3.7.

---

## 0. Contexte court — pourquoi v3.6.3 avant v3.7

L'audit visuel post-v3.6.2 (côté Blaise sur le site déployé) révèle **deux incohérences UX résiduelles** sur CU-024 et CU-027 qui n'ont pas été détectées par les audits automatiques :

1. **Cards CU-024 et CU-027 promettent « Étude de cas + checklist »** mais le contenu réel ne contient pas d'étude de cas formelle (CU-024 : aucune ; CU-027 : a un cas pédagogique Tea App, pas une étude de cas). **Violation RULES § 1.5** (cohérence card index ↔ contenu réel).
2. **Format des checklists CU-024/CU-027 non homogène** avec les auto-diags interactifs des autres modules N4 (CU-008, CU-013, CU-023). Checklist statique simple alors que le pattern dominant est form interactif + verdict + export.

S'ajoutent les **5 écarts résiduels** du rapport Claude Code v3.6.2 (section dédiée du `rapport-mission-v3.6.2.md`) et les **3 amendements RULES** que Claude Code a proposés.

**Cette itération règle TOUT ce qui est ouvert avant qu'on attaque v3.7** (section Déploiement + 14 fiches outils + 5 enrichissements + nouveau CU-025).

**Tu travailles en autonomie.** Blaise ne sera pas en revue continue. Rapport de mission obligatoire à la fin.

---

## 1. Préalable obligatoire — RULES v1.4

**AVANT toute action de code**, tu dois :

1. Lire **intégralement** la version mise à jour `site-web-prep/RULES-IMPLEMENTATION.md` (version **1.4**, mise à jour aujourd'hui — intègre tes 3 amendements proposés au rapport v3.6.2 + une précision sur la cohérence card↔contenu).
2. Te référer en parallèle à `modules/cu-008-knowledge-base-rag.html` (référence canonique) et `modules/cu-023-devis-intelligent.html` (référence pour le pattern auto-diag interactif Oui/Non + verdict 3 niveaux).

---

## 2. Méthode — 7 lots dans l'ordre

### Lot 1 — Cohérence cards CU-024 et CU-027 ↔ contenu réel (30 min)

**Référence RULES** : § 1.5 (cohérence card index ↔ contenu).

**Méthode.**

1. Dans `index.html`, identifier les cards CU-024 et CU-027 (autour des lignes 570-590 et 745-765).
2. Modifier les `<span class="card-quiz">` :

| Module | Avant | Après |
|---|---|---|
| **CU-024** | « Étude de cas + checklist » | **« Checklist projet O2C »** |
| **CU-027** | « Étude de cas + checklist » | **« Cas pédagogique + checklist sécurité »** |

**Justification éditoriale** :
- **CU-024** : aucune étude de cas dans le module. Le contenu est : timeline réglementaire 2026-2027 + cycle O2C 6 étapes + grille PA agréées DGFiP + checklist 12 points. Le label « Checklist projet O2C » reflète exactement ce qui est livré.
- **CU-027** : le module contient un **« incident emblématique Tea App »** (section 2) déjà labellé en interne `<span class="incident-card-label">Cas pédagogique</span>`. Le label de card aligné « Cas pédagogique + checklist sécurité » est cohérent.

**Livrable Lot 1.**
- Commit `fix(v3.6.3): cohérence cards CU-024/CU-027 ↔ contenu réel`
- Vérification grep : aucune autre card ne dit « Étude de cas + checklist » sans avoir effectivement les deux.

### Lot 2 — Refonte checklists CU-024 et CU-027 en format interactif (3-4 h)

**Référence RULES** : § 1.5.5 (format hybride accepté avec 3 propriétés obligatoires : form + génération plan + export). § 1.5.5 amendée v1.4 : checklist statique reste valide sous un autre nom — MAIS pour cohérence UX avec les autres modules N4, on convertit ces 2 checklists en interactives.

**Méthode.**

#### 2.1 — CU-024 : refonte de la section 6 « Checklist projet O2C »

Reprendre exactement le pattern de `modules/cu-023-devis-intelligent.html` section 5 (form interactif Oui/Non + scoring + verdict 3 niveaux + export `.txt` + persistance `localStorage`) :

- **Form** : `<form id="o2cChecklistForm">` avec 12 questions Oui/Non (les 12 points actuels de la checklist projet O2C, à reformuler en questions à la 1re personne : « Mon outil cible est PA agréée DGFiP ou interopérable avec une PA. », « Mon ERP / outil compta a un connecteur natif documenté avec mon outil cible. », etc.)
- **Bouton** : « Générer mon verdict O2C » → fonction `evaluateO2CChecklist()`
- **Verdict 3 niveaux** :
  - 🟢 **GO** si 10+/12 : « L'outil cible coche l'essentiel — tu peux signer en exigeant que les 1-2 points manquants soient ajoutés au contrat. »
  - 🟡 **À MÛRIR** si 7-9/12 : « Plusieurs points clés manquent — exige les correctifs par écrit avant signature, ou compare avec une autre PA. »
  - 🔴 **NO-GO** si < 7/12 : « Plus de la moitié des points clés manquent — change d'outil cible. Le marché compte 120 PA agréées, tu as de la marge. »
- **Bouton** : « 📥 Exporter en `.txt` » → fonction `exportO2CChecklist()`
- **Persistance** : `localStorage.setItem('hubia_cu024_o2c', ...)`

Pattern script : adapter mot pour mot `evaluateDevisDiag()` / `exportDevisDiag()` de CU-023, en remplaçant les libellés.

#### 2.2 — CU-027 : refonte de la section 4 « Checklist sécurité minimale à exiger d'un prestataire »

Même méthode que 2.1, adaptée :

- **Form** : `<form id="secuChecklistForm">` avec 12 questions Oui/Non (les 12 points actuels de la checklist sécurité, reformulés : « Le prestataire s'engage à activer l'authentification par défaut sur toutes les routes. », « Le prestataire scanne automatiquement le code à chaque commit (Snyk, Semgrep ou équivalent). », etc.)
- **Verdict 3 niveaux** :
  - 🟢 **GO** si 10+/12 : « Le prestataire prend la sécurité au sérieux — tu peux signer en exigeant les 1-2 points restants en annexe technique. »
  - 🟡 **À NÉGOCIER** si 7-9/12 : « Plusieurs garde-fous manquent — exige les correctifs avant signature ou compare avec un autre prestataire. »
  - 🔴 **CHANGE DE PRESTATAIRE** si < 7/12 : « Plus de la moitié des garde-fous manquent — c'est un risque sécurité majeur. Le marché est suffisamment large pour ne pas accepter ce niveau de compromis. »
- **Bouton** : « 📥 Exporter en `.txt` »
- **Persistance** : `localStorage.setItem('hubia_cu027_secu', ...)`

#### 2.3 — Mise à jour des badges de section et des TOC

- CU-024 section 6 : conserver le titre « Checklist projet O2C — 12 points avant de signer ». Mettre à jour le label TOC si nécessaire.
- CU-027 section 4 : conserver le titre « Checklist sécurité minimale à exiger d'un prestataire ». Mettre à jour le label TOC si nécessaire.

#### 2.4 — Réutilisation des classes centralisées

Utiliser exclusivement les classes déjà dans `module-v3.css` : `.diagnostic`, `.diag-question`, `.diag-option`, `.diag-result`, `.diag-submit`, `.diag-action` (mêmes que CU-023). **Aucun nouveau `<style>` inline** introduit.

**Livrable Lot 2.**
- Commit `feat(v3.6.3): refonte checklists CU-024 et CU-027 en format interactif`
- Tests visuels : ouvrir chaque page, remplir, vérifier verdict + export
- Vérification : pas de nouveau composant CSS introduit, alignement avec CU-023

### Lot 3 — RULES v1.3 → v1.4 (amendements proposés v3.6.2) (15 min)

Le fichier `RULES-IMPLEMENTATION.md` a été mis à jour à v1.4 dans cette itération. Tu dois **vérifier que les 3 amendements** que tu avais proposés en rapport v3.6.2 sont bien intégrés correctement :

- **A1 (§ 1.5.5)** : précision que le format checklist statique reste valide sous un autre nom (« Checklist d'éligibilité », « Checklist projet », « Checklist sécurité »).
- **A2 (§ 1.5.3)** : extension de la règle « pas de couleurs hardcodées » aux espacements (utilisation obligatoire de `var(--space-X)` plutôt que valeurs en `rem`).
- **A3 (§ 1.5.6)** : ajout de la commande grep pour générer dynamiquement la liste à jour des ancres outils dans `ressources.html`.

Si un amendement te semble mal formulé, **signale-le dans le rapport** (section « Propositions d'amendement à RULES v1.4 »). Ne le modifie pas de toi-même.

**Livrable Lot 3.**
- Pas de commit (RULES v1.4 déjà commité côté Cowork avant lancement de cette itération)
- Vérification de cohérence dans le rapport de mission

### Lot 4 — Refonte structurelle PR-07 (anti-pattern `<main>` direct) (1-2 h)

**Référence RULES** : § 1.5.1 (squelette HTML), § 1.5.3 (anti-pattern `<main>` direct sans `module-layout`).

**Méthode.**

PR-07 (`prealables/pr-07-build-vs-buy.html`) utilise actuellement `<main>` direct sans `<div class="module-layout">` ni `<aside class="module-toc">`. Refonte structurelle complète :

1. Wrapper le contenu dans `<div class="module-layout">` + `<aside class="module-toc">` + `<main class="module-main">`
2. Construire la `module-toc` sticky avec les ancres des sections existantes (#executive-summary, #section-1, #section-2, …, #ressources)
3. Conserver intégralement le contenu éditorial actuel (executive summary, sections 1-7, section ressources)
4. Vérifier la sticky TOC + scroll-spy fonctionnels après refonte

**Livrable Lot 4.**
- Commit `refactor(v3.6.3): refonte structurelle PR-07 (module-layout + sticky TOC)`
- Test visuel : sticky TOC OK, scroll-spy OK, pas de régression contenu

### Lot 5 — Patch massif `.exec-takeaway-icon` → `.exec-takeaway-num` (3-4 h)

**Référence RULES** : § 1.5.3 (anti-pattern `.exec-takeaway-icon` au lieu de `.exec-takeaway-num`).

**Méthode.**

18 modules anciens (CU-011 à CU-022, PR-01 à PR-06 + autres détectés) utilisent `<div class="exec-takeaway-icon">EMOJI</div>` au lieu de `<div class="exec-takeaway-num">N</div>`.

**Pour chaque module concerné** :

1. Identifier les 4 takeaways de la section executive summary
2. Remplacer chaque `<div class="exec-takeaway-icon">EMOJI</div>` par `<div class="exec-takeaway-num">N</div>` (N = 1, 2, 3, 4 selon ordre)
3. Vérifier visuellement que le rendu est cohérent (cercle numéroté centré)

**Liste exhaustive à vérifier par grep** :

```bash
grep -rln 'exec-takeaway-icon' modules/ prealables/
```

Patcher tous les fichiers retournés par cette commande, **sauf** ceux où la classe `.exec-takeaway-icon` serait justifiée (à signaler dans le rapport — mais la règle § 1.5.3 ne prévoit pas d'exception, donc en principe : tous à patcher).

**Livrable Lot 5.**
- Commit `refactor(v3.6.3): patch massif exec-takeaway-icon → exec-takeaway-num (18 modules)`
- Vérification grep finale : 0 hit `exec-takeaway-icon`

### Lot 6 — Audit CU-016 (`<style>` inline géant 65 classes) (1-2 h)

**Référence RULES** : § 1.5.2 (composants CSS de référence — éviter `<style>` inline qui redéfinit des composants centralisés).

**Méthode.**

`modules/cu-016-maintenance-predictive.html` n'importe **pas** `module-v3.css` et a tout son CSS dans un `<style>` inline qui inclut le pattern complet (`module-layout`, `module-toc`, etc.). Anti-pattern majeur.

**Étapes** :

1. **Diagnostic** : lire le `<style>` inline complet de CU-016. Identifier :
   - Les classes qui sont des doublons exacts de `module-v3.css` (à remplacer par l'import + suppression)
   - Les classes qui sont des variantes de `module-v3.css` (à comparer visuellement, choisir : alignement vers la version centrale, ou justifier la divergence)
   - Les classes spécifiques single-use à CU-016 (à conserver inline avec commentaire explicatif RULES § 1.4.4)
2. **Migration** : ajouter l'import `<link rel="stylesheet" href="../css/module-v3.css">` dans le `<head>` + supprimer les classes inline qui sont des doublons
3. **Tests visuels** : vérifier qu'il n'y a pas de régression visuelle après migration (les classes centrales peuvent avoir évolué depuis la création de CU-016)
4. **Si la migration crée des régressions trop importantes** : **stopper et signaler dans le rapport** plutôt que de patcher partiellement. Blaise tranchera.

**Livrable Lot 6.**
- Commit `refactor(v3.6.3): migration CU-016 vers module-v3.css` (si migration réussie sans régression)
- Ou rapport détaillé des écarts visuels constatés (si migration ajournée)

### Lot 7 — Audit léger des `<style>` inline résiduels (1-2 h)

**Référence RULES** : § 1.4.4 (composants single-use peuvent rester inline ; composants utilisés sur 2+ modules doivent migrer).

**Méthode.**

13 modules ont du `<style>` inline résiduel : CU-006, CU-007, CU-009, CU-011, CU-013, CU-014, CU-015, CU-017, CU-018, CU-019, PR-01, PR-03, PR-05.

**Pour chaque module** :

1. Lister les classes définies inline
2. Pour chaque classe :
   - Si elle existe déjà dans `module-v3.css` ou `style.css` : doublon → suppression de l'inline (vérifier rendu identique)
   - Si elle est utilisée sur 2+ modules : migration vers `module-v3.css` (avec variables du design system)
   - Si elle est single-use : conserver inline mais ajouter un commentaire explicatif `/* Single-use spécifique à [usage] */` + utiliser les variables CSS du design system (RULES § 1.5.3 amendée v1.4 : aussi pour les espacements `var(--space-X)`)

**Si volume trop important pour cette itération** (> 30 classes à arbitrer) : faire la moitié et signaler le reste pour v3.6.4 ou v3.7.

**Livrable Lot 7.**
- Commit `refactor(v3.6.3): nettoyage <style> inline résiduel sur N modules`
- Rapport détaillé des décisions prises (migration / conservation single-use / suppression doublon)

### Lot 8 — Audit final + rapport (1 h)

**Méthode.**

1. Exécuter la **checklist § 2** de RULES v1.4 dans son intégralité.
2. Exécuter les **grep des anti-patterns § 1.5.3** :
   ```bash
   grep -rln 'exec-takeaway-icon' modules/ prealables/  # doit être vide
   grep -rln 'id="section-7"' modules/ prealables/      # doit être vide
   grep -rn '<main>' modules/ prealables/ | grep -v 'module-main'  # doit être vide
   ```
3. Vérifier la **cohérence numérique** (RULES § 1.2.3) inchangée : 25 modules / 7 préalables / 83 fiches / 5 entrées de nav.
4. **Production du rapport** dans `site-web-prep/rapport-mission-v3.6.3.md` — même structure que rapport v3.6.2 (Synthèse exécutive + un sous-titre par lot + écarts résiduels + propositions d'amendement RULES v1.4 si pertinent).

**Livrable Lot 8.**
- Commit `chore(v3.6.3): rapport de mission + checklist audit finale`

---

## 3. Décisions explicites de NE PAS faire dans cette itération

- **Pas de création des 14 fiches outils manquantes** (Pennylane, Sellsy, Axonaut, PandaDoc, Esker, Sidetrade, Tacton, Lovable, Bolt.new, v0, Replit Agent, Windsurf, GitHub Copilot Workspace, autres). Ces fiches nécessitent une **matière éditoriale Cowork** (recherche, sourcing, formatage). **Reporté à v3.7** où Cowork produira la matière en MD que Claude Code transformera en HTML.
- **Pas de modification du contenu éditorial** des modules (uniquement structure HTML / CSS / JS).
- **Pas de création de nouveau module / préalable**.
- **Pas de modification des chiffres macro** (95 % MIT, +270 % Microsoft, etc.).

---

## 4. Estimation effort consolidée

| Lot | Sujet | Effort estimé |
|---|---|---|
| Lot 0 | Préalable (lecture RULES v1.4, rapport v3.6.2) | 30 min |
| Lot 1 | Cohérence cards CU-024 / CU-027 | 30 min |
| Lot 2 | Refonte checklists CU-024 / CU-027 en interactif | 3-4 h |
| Lot 3 | Vérification RULES v1.4 (amendements) | 15 min |
| Lot 4 | Refonte structurelle PR-07 | 1-2 h |
| Lot 5 | Patch massif `.exec-takeaway-icon` → `.exec-takeaway-num` (18 modules) | 3-4 h |
| Lot 6 | Audit CU-016 (`<style>` inline géant) | 1-2 h |
| Lot 7 | Audit léger `<style>` inline résiduels (13 modules) | 1-2 h |
| Lot 8 | Audit final + rapport mission | 1 h |
| **Total** | | **12-17 h** |

Effort similaire à v3.6.2 (15-22 h) — itération de consolidation finale avant v3.7.

---

## 5. Workflow recommandé

1. **Vérifier que la PR v3.6.2 est mergée** sur main avant de commencer.
2. **Créer une branche `chore/v3.6.3-correctifs`**.
3. **Lire RULES v1.4 + rapport v3.6.2** (Lot 0).
4. **Exécuter les Lots 1 → 8 dans l'ordre indiqué**, un commit par lot.
5. **Tests croisés** Chrome / Firefox / Safari, mobile + desktop, sticky TOC fonctionnel.
6. **PR avec description structurée** :
   - Lien vers ce brief
   - Lien vers RULES v1.4
   - Lien vers le rapport v3.6.2 (référence des écarts traités)
   - Liste des commits (un par lot)
   - Lien vers ton rapport `rapport-mission-v3.6.3.md`

---

## 6. Règles de prudence

Identiques à v3.6.2 (autonomie, signalement plutôt qu'interprétation, pas de réécriture éditoriale, commits incrémentaux, arrêt et documentation en cas de blocage).

**Spécifique v3.6.3** :
- Sur Lot 2 (refonte checklists interactives) : si tu hésites sur les seuils GO/À MÛRIR/NO-GO ou les libellés des verdicts, garde mes formulations ci-dessus telles quelles. Ce sont des décisions éditoriales validées.
- Sur Lot 6 (CU-016) : si la migration vers `module-v3.css` crée des régressions visuelles importantes, **stoppe et documente** plutôt que de patcher au jugé.

---

## 7. Validation finale avant PR

```
☐ RULES v1.4 lu en intégralité avant de commencer.
☐ Rapport v3.6.2 lu en intégralité.
☐ Les 8 lots ont été exécutés dans l'ordre.
☐ Chaque lot a fait l'objet d'un commit séparé (ou d'un rapport documenté si bloqué).
☐ Le rapport rapport-mission-v3.6.3.md est complet et structuré.
☐ Tous les écarts non corrigés sont signalés dans le rapport.
☐ Aucune régression visuelle (vérifiée par tests croisés).
☐ Les anti-patterns § 1.5.3 sont absents (vérifié par grep).
☐ La cohérence numérique cross-site est préservée.
☐ La description de PR pointe vers ce brief + RULES v1.4 + le rapport mission.
```

---

## 8. Fichiers de référence (dans `site-web-prep/`)

- **Référentiel non négociable** : `RULES-IMPLEMENTATION.md` v1.4 ← À LIRE EN PRÉALABLE
- **Brief de cette itération** : `BRIEF-CLAUDE-CODE-v3.6.3-correctifs.md` (ce fichier)
- **Rapport v3.6.2** (référence) : `rapport-mission-v3.6.2.md`
- **Brief v3.6.2** (référence) : `BRIEF-CLAUDE-CODE-v3.6.2-harmonisation.md`
- **Référence canonique** : `modules/cu-008-knowledge-base-rag.html`
- **Référence pattern auto-diag interactif** : `modules/cu-023-devis-intelligent.html` (section 5)

---

## 9. Contact

Pour toute question pendant l'exécution : Blaise Cavalli — blaise.cavalli@questforchange.eu

**Tu travailles en autonomie sur cette itération.** Si tu es bloqué, **arrête-toi et documente** plutôt que d'interpréter. Blaise relira le rapport et tranchera les cas signalés.

**Bonne mission, et merci pour le travail !**

---

*Brief produit par Cowork (Claude desktop) le 9 mai 2026. Cette itération v3.6.3 règle les correctifs résiduels avant le démarrage de v3.7 (section Déploiement + 14 fiches outils + 5 enrichissements + nouveau CU-025).*
