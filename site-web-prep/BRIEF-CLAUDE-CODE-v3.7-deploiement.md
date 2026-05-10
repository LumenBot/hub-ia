# Brief Claude Code — Hub IA Learning Center (passation v3.7)

**Auteur :** Blaise Cavalli — Startup Manager Quai Alpha (Quest for Change)
**Date :** mai 2026
**Repo :** https://github.com/LumenBot/hub-ia
**Branche cible :** main
**Hébergement :** GitHub Pages
**Itération précédente :** v3.6.3 (correctifs résiduels — 7 commits, 0 anti-pattern résiduel)
**Nature de cette itération :** EXPANSION ÉDITORIALE — nouvelle section Déploiement (8 fiches DEP) + nouveau module CU-025 + 5 enrichissements modules existants + 14 fiches outils + amendements RULES v1.5.

---

## 0. Contexte court — pourquoi v3.7

L'itération **v3.7** est une **expansion éditoriale majeure** qui ajoute :

1. **Une nouvelle section transverse « Déploiement »** (8 fiches DEP) — pour les dirigeants pilotant un projet IA en mise en prod, et leurs interfaces techniques.
2. **Un nouveau module CU-025** « Knowledge management IA-augmenté pour dirigeant » — application du pattern Obsidian + Claude + n8n.
3. **5 enrichissements de modules existants** (CU-027, PR-07, CU-008, CU-014, CU-015) — actualisation 2026.
4. **14 nouvelles fiches outils** dans `ressources.html` — comble les renvois manquants signalés en v3.6.2.

**Tu travailles en autonomie**. Cowork (côté Blaise) a produit toute la matière éditoriale en MD structuré dans `site-web-prep/v3.7/`. Ton rôle : transformer cette matière en HTML conforme RULES v1.5 (à amender) à partir de la canonique CU-008.

---

## 1. Préalable obligatoire — RULES v1.5

**AVANT toute action de code**, tu dois :

1. Lire **intégralement** `site-web-prep/RULES-IMPLEMENTATION.md` v1.4 (version actuelle).
2. **Amender RULES en v1.5** dans le commit Lot 1 ci-dessous (les amendements sont listés en section 2.1).
3. Te référer à `modules/cu-008-knowledge-base-rag.html` (référence canonique) et `modules/cu-023-devis-intelligent.html` (référence pour le pattern auto-diag interactif Oui/Non).
4. Lire la veille `site-web-prep/veille-v3.7-mai2026.md` qui a sourcé toute la matière éditoriale.

---

## 2. Méthode — 9 lots dans l'ordre

### Lot 1 — Amendements RULES v1.4 → v1.5 (15 min)

Amendements à intégrer suite à v3.7 :

- **§ 1.2.3 (glossaire chiffres-clés)** : mise à jour des valeurs courantes :
  - Modules CU : **25 → 26** (CU-025 ajouté)
  - Préalables PR : 7 (inchangé)
  - Fiches outils : **83 → 97** (14 ajoutées en v3.7)
  - Nouvelle section : **Déploiement** (8 fiches DEP-01 → DEP-08)
  - Entrées nav : **5 → 6** (ajout « Déploiement » entre Architectures et Modules)
- **§ 1.5.1 (squelette HTML)** : pas de changement structurel, mais le pattern reste applicable aux fiches DEP (mêmes principes que les PR).
- **§ Historique v1.5** : ajout du changelog avec : section Déploiement créée, glossaire actualisé, ajout référence canonique pour fiches DEP (suggestion : `deploiement/dep-01-cadrer-projet-prod.html` une fois produit).

**Livrable Lot 1** : commit `chore(v3.7): amendements RULES v1.4 → v1.5`

### Lot 2 — Création de la section Déploiement (4-6 h)

#### 2.1 Page d'index Déploiement

**Source MD** : `site-web-prep/v3.7/deploiement-index.md`

Créer `deploiement.html` à la racine du repo, sur le pattern de `prealables.html` :
- Hero avec emoji ouvrant 🚀 + sous-titre cadrage
- 8 cards vers les 8 fiches DEP (libellés et badges spécifiés dans le MD)
- Section « Aiguillage par cas d'usage » avec 3 parcours suggérés
- Footer-CTA vers `architectures.html`

#### 2.2 Création du dossier `deploiement/` + 8 fiches DEP

Créer `deploiement/dep-01-*.html` à `deploiement/dep-08-*.html` à partir des sources MD :

| Fichier MD source | Fichier HTML cible |
|---|---|
| `site-web-prep/v3.7/dep-01-cadrer-projet-prod.md` | `deploiement/dep-01-cadrer-projet-prod.html` |
| `site-web-prep/v3.7/dep-02-rag-architecture-prod.md` | `deploiement/dep-02-rag-architecture-prod.html` |
| `site-web-prep/v3.7/dep-03-context-engineering-couts.md` | `deploiement/dep-03-context-engineering-couts.html` |
| `site-web-prep/v3.7/dep-04-fine-tuning-pme.md` | `deploiement/dep-04-fine-tuning-pme.html` |
| `site-web-prep/v3.7/dep-05-agents-observabilite.md` | `deploiement/dep-05-agents-observabilite.html` |
| `site-web-prep/v3.7/dep-06-inference-saas-self-hosted.md` | `deploiement/dep-06-inference-saas-self-hosted.html` |
| `site-web-prep/v3.7/dep-07-evaluation-qualite.md` | `deploiement/dep-07-evaluation-qualite.html` |
| `site-web-prep/v3.7/dep-08-securite-agents-mcp.md` | `deploiement/dep-08-securite-agents-mcp.html` |

**Pattern HTML obligatoire** : RULES § 1.5.1 (squelette 9 blocs : reading-progress + nav 6 entrées + hero + module-layout 2 colonnes + executive-summary + sections numérotées + `id="ressources"` Schéma A + footer + script).

**Composants à utiliser** :
- Centralisés (RULES § 1.5.2) : `.exec-summary`, `.exec-takeaway-num`, `.alert-block`, `.checklist-block`, `.tool-table`, `.timeline-block`, `.arch-callout`, `.pull-quote`, `.callout-info`
- Suggestions composants visuels listées dans chaque fichier MD source

**Renvois internes** : chaque MD source liste les renvois à intégrer (vers autres DEP, modules CU, préalables, fiches outils). À implémenter selon RULES § 1.5.6.

**Livrable Lot 2** : commit `feat(v3.7): nouvelle section Déploiement (8 fiches DEP + page index)`

### Lot 3 — Mise à jour navigation cross-pages (1-2 h)

La nav passe de 5 à 6 entrées. Mise à jour sur **TOUTES les pages du site** (RULES § 1.4.1) :

```html
<div class="nav-links">
  <a href="../prealables.html" class="nav-link">Préalables</a>
  <a href="../architectures.html" class="nav-link">Architectures</a>
  <a href="../deploiement.html" class="nav-link">Déploiement</a>  <!-- NOUVEAU -->
  <a href="../index.html#modules" class="nav-link">Modules</a>
  <a href="../ressources.html" class="nav-link">Ressources</a>
  <a href="../index.html#a-propos" class="nav-link">À propos</a>
</div>
```

Adapter chemins relatifs selon profondeur (`../` pour modules, `../../` si nécessaire).

**Livrable Lot 3** : commit `refactor(v3.7): mise à jour navigation 5 → 6 entrées (ajout Déploiement)`

### Lot 4 — Nouveau module CU-025 (2-3 h)

**Source MD** : `site-web-prep/v3.7/cu-025-knowledge-management-dirigeant.md`

Créer `modules/cu-025-knowledge-management-dirigeant.html` selon pattern RULES § 1.5.1.

**Card index** : ajouter dans `index.html` selon spécifications du MD source (emoji 🧠, titre, sous-titre, badges, axe métier `axe-a` + secondaire `axe-b`, niveau ⭐⭐⭐, type « Étude de cas + plan d'action »).

**Livrable Lot 4** : commit `feat(v3.7): nouveau module CU-025 Knowledge management IA-augmenté pour dirigeant`

### Lot 5 — 5 enrichissements modules existants (2-3 h)

Patches éditoriaux ciblés sur des modules existants. Sources MD dans `site-web-prep/v3.7/` :

| Source MD | Module cible | Volume |
|---|---|---|
| `enrichissement-cu-027-outils-2026.md` | `modules/cu-027-dev-applicatif-ia.html` | ~400 mots à intégrer |
| `enrichissement-pr-07-couts.md` | `prealables/pr-07-build-vs-buy.html` | ~250 mots + maj matrice |
| `enrichissement-cu-008-llm-wiki.md` | `modules/cu-008-knowledge-base-rag.html` | ~400 mots (nouvelle section) |
| `enrichissement-cu-014-fat-skills.md` | `modules/cu-014-multi-agents.html` | ~350 mots (nouvelle section) |
| `enrichissement-cu-015-renvoi-cu-027.md` | `modules/cu-015-stripe-minions.html` | ~150 mots (renvois + chiffre) |

Suivre les instructions de chaque MD source (position, contenu, sources à ajouter, renvois internes à insérer).

**Livrable Lot 5** : commit `feat(v3.7): 5 enrichissements modules existants (CU-027, PR-07, CU-008, CU-014, CU-015)`

### Lot 6 — 14 nouvelles fiches outils (3-4 h)

**Source MD** : `site-web-prep/v3.7/fiches-outils-v3.7.md`

Créer 14 nouvelles fiches `<article class="tool-card" id="...">` dans `ressources.html` selon le format des fiches existantes (à confirmer par lecture rapide d'une fiche existante).

Liste des ancres à créer :
- `pennylane`, `sellsy`, `axonaut`, `pandadoc`, `esker`, `sidetrade`, `tacton` (catégorie « Compta / facturation / O2C »)
- `lovable`, `bolt-new`, `v0`, `replit-agent`, `windsurf`, `copilot-workspace` (catégorie « Outils dev IA-assisté »)
- `kimi-k2` (catégorie « Modèles LLM »)

Chaque fiche : titre, badges (Type/Maturité/Souveraineté/Coût/Complexité), description, atouts, limites, quand l'utiliser, liens vers modules Hub mentionnant l'outil, URL officielle.

**Important** : à mesure que ces fiches sont créées, les modules qui mentionnent ces outils peuvent désormais les référencer via `<a href="../ressources.html#xxx">`. **Audit post-création** : ajouter ces renvois contextuels dans CU-023, CU-024, CU-027, PR-07 (cf. spécifications RULES § 1.5.6).

**Livrable Lot 6** : commit `feat(v3.7): 14 nouvelles fiches outils + renvois contextuels modules`

### Lot 7 — Cohérence numérique cross-site (1-2 h)

**Référence RULES** : § 1.2.1, § 1.2.2, § 1.2.3 (mises à jour Lot 1).

Grep et mise à jour cross-site des chiffres :
- « 25 modules » → « 26 modules » (et variantes : « 25 cas d'usage », etc.)
- « 83 fiches outils » → « 97 fiches outils »
- « 5 entrées de nav » → « 6 entrées de nav »

Lieux à vérifier (cf. RULES § 1.2.2) :
- `index.html` (meta, hero stats, filter count, section À propos)
- `prealables.html`, `architectures.html`, `deploiement.html`, `ressources.html`
- `README.md`
- Méta-descriptions toutes pages

**Livrable Lot 7** : commit `chore(v3.7): cohérence numérique cross-site (26 modules, 97 fiches, 6 nav)`

### Lot 8 — Page d'accueil — bandeau « Nouveau » Déploiement (30 min — optionnel)

Ajouter sur `index.html` un bandeau ou callout discret signalant la nouvelle section Déploiement (sans utiliser de versioning interne, RULES § 1.2.6 — préférer « Nouvelle section 2026 » ou « Section récente »).

**Livrable Lot 8** : commit `feat(v3.7): callout home pour la nouvelle section Déploiement`

### Lot 9 — Audit final + rapport mission (1 h)

**Méthode**.

1. Exécuter la **checklist § 2** de RULES v1.5 dans son intégralité.
2. Exécuter les **grep des anti-patterns § 1.5.3** (doivent être tous vides).
3. Vérifier la **cohérence numérique** (RULES § 1.2.3) et la **cohérence intra-page** (§ 1.2.5) — pas d'incohérence type « 26 modules » vs « 25 cas d'usage » sur une même page.
4. Vérifier la **cohérence card index ↔ contenu réel** sur les nouvelles cards (CU-025 + 8 cards DEP).
5. Tests croisés Chrome / Firefox / Safari, mobile + desktop, sticky TOC fonctionnel sur toutes les nouvelles pages.
6. **Production du rapport** dans `site-web-prep/rapport-mission-v3.7.md` (même structure que rapports v3.6.2 et v3.6.3).

**Livrable Lot 9** : commit `chore(v3.7): rapport de mission + audit final v3.7`

---

## 3. Estimation effort consolidée

| Lot | Sujet | Effort estimé |
|---|---|---|
| Lot 0 | Préalable (lecture RULES + veille) | 30 min |
| Lot 1 | Amendements RULES v1.4 → v1.5 | 15 min |
| Lot 2 | Section Déploiement (page index + 8 fiches DEP) | 4-6 h |
| Lot 3 | Mise à jour navigation cross-pages | 1-2 h |
| Lot 4 | Nouveau module CU-025 | 2-3 h |
| Lot 5 | 5 enrichissements modules existants | 2-3 h |
| Lot 6 | 14 nouvelles fiches outils + renvois | 3-4 h |
| Lot 7 | Cohérence numérique cross-site | 1-2 h |
| Lot 8 | Callout home Déploiement (optionnel) | 30 min |
| Lot 9 | Audit final + rapport mission | 1 h |
| **Total** | | **15-22 h** |

---

## 4. Workflow recommandé

1. **Vérifier que la PR v3.6.3 est mergée** sur main avant de commencer.
2. **Créer une branche `feat/v3.7-deploiement`**.
3. **Lire RULES v1.4 + veille v3.7** (Lot 0).
4. **Exécuter les Lots 1 → 9 dans l'ordre indiqué**, un commit par lot.
5. **Tests croisés** à la fin (Lot 9) sur tous les navigateurs et tailles d'écran.
6. **PR avec description structurée** :
   - Lien vers ce brief
   - Lien vers RULES v1.5 (après amendement Lot 1)
   - Lien vers la veille v3.7
   - Liste des commits (un par lot)
   - Lien vers ton rapport `rapport-mission-v3.7.md`

---

## 5. Règles de prudence pendant l'exécution autonome

Identiques aux briefs précédents (signaler plutôt qu'interpréter, pas de réécriture éditoriale, commits incrémentaux, arrêt et documentation en cas de blocage).

**Spécifique v3.7** :
- Sur Lot 2 (8 fiches DEP) : si un fichier MD source contient une section dont tu n'es pas sûr de la mise en forme HTML idéale, **utilise par défaut le pattern de la fiche déjà existante équivalente** (PR pour les fiches DEP). Documente dans le rapport les choix de conversion HTML que tu as faits.
- Sur Lot 6 (14 fiches outils) : **ne pas dupliquer la création** d'une fiche si tu détectes qu'une fiche existante similaire existe déjà sous une autre ancre. Vérifier d'abord par grep.
- Sur Lot 7 (cohérence numérique) : si tu trouves un chiffre incohérent dont la source n'est pas claire, **signaler dans le rapport** plutôt que d'interpréter.

---

## 6. Décisions explicites de NE PAS faire dans cette itération

- **Pas de modification du design system** (CSS centralisé inchangé).
- **Pas de refonte des modules anciens** au-delà des 5 enrichissements ciblés.
- **Pas de modification des chiffres macro** (95 % MIT NANDA, +270 % Microsoft, etc.) — sauf si une source citée dans la veille v3.7 invalide une source précédente, auquel cas signaler dans le rapport.
- **Pas de création de nouvelle catégorie de section** au-delà de Déploiement.
- **Pas d'ajout des modules CU-026 / CU-028** (réservés à v3.8 si pertinent).

---

## 7. Validation finale avant PR

```
☐ RULES v1.4 lu en intégralité avant de commencer.
☐ Veille v3.7 lue en intégralité.
☐ RULES v1.5 amendée et committée (Lot 1).
☐ Les 9 lots ont été exécutés dans l'ordre.
☐ Chaque lot a fait l'objet d'un commit séparé.
☐ Le rapport rapport-mission-v3.7.md est complet et structuré.
☐ Tous les écarts non corrigés sont signalés dans le rapport.
☐ Aucune régression visuelle (vérifiée par tests croisés).
☐ Les anti-patterns § 1.5.3 sont absents (vérifié par grep).
☐ La cohérence numérique cross-site est préservée (26 modules / 7 préalables / 97 fiches / 6 entrées nav).
☐ La cohérence intra-page est préservée (pas de stat contradictoire sur une même page).
☐ La cohérence card index ↔ contenu réel est préservée (cards promettent ce que les modules livrent).
☐ La description de PR pointe vers ce brief + RULES v1.5 + veille + rapport mission.
```

---

## 8. Fichiers de référence (dans `site-web-prep/`)

- **Référentiel non négociable** : `RULES-IMPLEMENTATION.md` v1.4 → à amender en v1.5 (Lot 1)
- **Brief de cette itération** : `BRIEF-CLAUDE-CODE-v3.7-deploiement.md` (ce fichier)
- **Veille sourcée** : `veille-v3.7-mai2026.md`
- **Matière éditoriale v3.7** : dossier `site-web-prep/v3.7/` avec :
  - 8 fichiers `dep-XX-*.md` (fiches DEP)
  - 1 fichier `deploiement-index.md` (page index Déploiement)
  - 1 fichier `cu-025-knowledge-management-dirigeant.md` (nouveau module CU-025)
  - 5 fichiers `enrichissement-*.md` (5 enrichissements modules existants)
  - 1 fichier `fiches-outils-v3.7.md` (14 fiches outils)
- **Référence canonique HTML** : `modules/cu-008-knowledge-base-rag.html`
- **Référence pattern auto-diag interactif** : `modules/cu-023-devis-intelligent.html` (pour CU-025 si auto-diag intégré)

---

## 9. Contact

Pour toute question pendant l'exécution : Blaise Cavalli — blaise.cavalli@questforchange.eu

**Tu travailles en autonomie sur cette itération.** Si tu es bloqué, **arrête-toi et documente** plutôt que d'interpréter. Blaise relira le rapport et tranchera les cas signalés.

**Bonne mission, et merci pour le travail !**

---

*Brief produit par Cowork (Claude desktop) le 9 mai 2026. Cette itération v3.7 est l'expansion éditoriale majeure du Hub IA : nouvelle section Déploiement (8 fiches DEP), nouveau module CU-025 (knowledge management IA-augmenté pour dirigeant), 5 enrichissements modules existants, 14 nouvelles fiches outils. Prépare le terrain pour v3.8 (consolidation et nouvelles fonctionnalités) puis v4 (agent front + plateforme dynamique — voir canal séparé Hub-IA-Plateforme).*
