# Brief Claude Code — Hub IA Learning Center (passation v3.6)

**Auteur :** Blaise Cavalli — Startup Manager Quai Alpha (Quest for Change)
**Date :** mai 2026
**Repo :** https://github.com/LumenBot/hub-ia
**Branche cible :** main
**Hébergement :** GitHub Pages
**Itération précédente :** v3.5.1 (audit qualité autonome — RULES.md référentiel + corrections cross-site)
**Nature de cette itération :** Production éditoriale — 1 nouveau préalable + 3 nouveaux modules ciblés sur le cœur opérationnel PME et le développement applicatif IA-assisté

---

## 0. Contexte court — pourquoi v3.6

L'itération **v3.6** comble un **angle mort éditorial** identifié par retour utilisateur (entrepreneur PME à la retraite ayant testé le site) : le Hub IA couvrait fortement les fonctions support et communication, mais peu le **cœur opérationnel d'une PME industrie/services** (devis, order-to-cash, pilotage financier) et **pas du tout** un cas d'usage majeur de l'IA — le **développement applicatif sur mesure IA-assisté** (Cursor, Claude Code, Lovable, Bolt, Windsurf).

**4 livrables produits dans cette itération :**

| Livrable | Type | Rôle | Statut |
|---|---|---|---|
| **PR-07 — Build vs Buy à l'ère de l'IA** | Préalable transverse | Cadrage conceptuel — la matrice de décision en 6 critères + les 7 écueils | ✅ Produit |
| **CU-027 — Développement applicatif métier IA-assisté** | Module CU (étude de cas + checklist) | Comment piloter un dev IA-assisté sans être IT — public dirigeant PME non-IT | ✅ Produit |
| **CU-024 — Order-to-cash automation** | Module CU (étude de cas + checklist) | Le cycle complet devis→encaissement, calé sur la facturation électronique 2026 | ✅ Produit |
| **CU-023 — Génération de devis intelligente** | Module CU (auto-diag + plan d'action) | Le cas d'usage IA le plus accessible pour démarrer | ✅ Produit |

**Position éditoriale après v3.6 :**
- Modules CU : **22 → 25** (CU-023, CU-024, CU-027 ajoutés ; CU-025/026/028 reportés à v3.7)
- Préalables PR : **6 → 7** (PR-07 ajouté)
- Fiches outils : 76 (inchangé en v3.6, prochains ajouts v3.7)

---

## 1. Préalable obligatoire — RULES-IMPLEMENTATION.md

**AVANT toute action de code**, tu dois lire **intégralement** `site-web-prep/RULES-IMPLEMENTATION.md`. C'est le référentiel non négociable produit en v3.5.1. Toutes les règles qui y figurent sont prescriptives.

Points de vigilance v3.6 sur RULES :

- **Règle 1.2.1 (cohérence numérique)** : tu vas passer de 22 à 25 modules CU et de 6 à 7 préalables. Tous les lieux qui mentionnent ces chiffres doivent être mis à jour dans le **même commit**. Le glossaire de la règle 1.2.3 te liste les endroits.
- **Règle 1.3.6 (pas de jargon PR-XX / CU-XXX visible)** : sur les pages d'index, ne fais apparaître que les titres métier. Les codes restent dans les URL et ancres.
- **Règle 1.4.5 (executive summary obligatoire)** : les 4 fichiers HTML produits respectent déjà le pattern. À vérifier en intégration.
- **Règle 1.1.5 (RetEx institutionnels uniquement)** : aucun cabinet de conseil intermédiaire n'est mentionné dans les 4 livrables. À préserver.

---

## 2. Fichiers sources de référence (dans `site-web-prep/`)

| Fichier | Rôle | Statut |
|---|---|---|
| `mockup/prealables/pr-07-build-vs-buy.html` | Préalable PR-07 prêt à intégrer | ✅ Produit |
| `mockup/modules/cu-027-dev-applicatif-ia.html` | Module CU-027 prêt à intégrer | ✅ Produit |
| `mockup/modules/cu-024-order-to-cash.html` | Module CU-024 prêt à intégrer | ✅ Produit |
| `mockup/modules/cu-023-devis-intelligent.html` | Module CU-023 prêt à intégrer | ✅ Produit |
| `veille-v3.6-mai2026.md` | Veille sourcée (matière éditoriale) | Référence |
| `RULES-IMPLEMENTATION.md` | Référentiel non négociable | À LIRE EN PRÉALABLE |
| `BRIEF-CLAUDE-CODE-v3.6-passation.md` | Ce brief | ✅ Tu lis |

**À lire dans l'ordre :** RULES.md → ce brief → veille-v3.6 (pour comprendre les choix éditoriaux) → les 4 fichiers HTML.

---

## 3. Lot 1 — Intégration PR-07 (Build vs Buy)

### 3.1 Action principale

Copier `mockup/prealables/pr-07-build-vs-buy.html` → `/prealables/pr-07-build-vs-buy.html`.

### 3.2 Mise à jour de la page d'index `prealables.html`

Ajouter une 7e card sur la page d'index, alignée avec le format des 6 cards existantes :

- **Titre visible :** « Build vs Buy à l'ère de l'IA »
- **Sous-titre :** « Faut-il acheter un SaaS ou faire développer sur mesure ? Matrice de décision en 6 critères. »
- **Durée :** 15 min
- **Icône suggérée :** ⚖️ ou 🎯
- **Lien :** `prealables/pr-07-build-vs-buy.html`

**Placement** : à la suite des 6 PR existants. Le PR-07 est le préalable conceptuel le plus structurant pour les nouveaux modules CU-023/024/027 — il peut justifier une mise en avant dans l'intro de page d'index si tu juges utile.

### 3.3 Composants CSS spécifiques

Le fichier `pr-07-build-vs-buy.html` introduit quelques composants inline :

- `.decision-matrix` (table de décision colorée — vert BUY, jaune BUILD, violet HYBRID)
- `.scenario-card` avec variantes `.buy` / `.build` / `.hybrid`
- `.reality-check` (encart rouge sur le 95 % d'échec)
- `.pitfall-list` (liste numérotée écueils)

**Recommandation** : laisser inline pour cette itération. Si tu juges utile de mutualiser après lecture du code (cohérence avec PR-05, PR-06), créer `prealables.css` plutôt que polluer `module-v3.css`.

---

## 4. Lot 2 — Intégration CU-027 (Dev applicatif IA-assisté)

### 4.1 Action principale

Copier `mockup/modules/cu-027-dev-applicatif-ia.html` → `/modules/cu-027-dev-applicatif-ia.html`.

### 4.2 Ajout sur la home / page Modules

Ajouter une nouvelle card module sur `index.html#modules` (et sur la page modules dédiée si elle existe), au format des cards existantes :

- **Titre visible :** « Développement applicatif métier IA-assisté »
- **Niveau :** 7-8 (avancé)
- **Durée :** 25 min
- **Type :** Étude de cas + checklist
- **Axe pédagogique :** **Architecture agentique** (le 6e axe v2)
- **Lien :** `modules/cu-027-dev-applicatif-ia.html`

### 4.3 Composants CSS spécifiques

Le fichier introduit :

- `.arch-callout` (encart bleu marine recommandation architecture)
- `.tool-table` (tableau outils 7 lignes)
- `.alert-block` (déjà présent dans PR-06, à mutualiser si pas déjà fait)
- `.incident-card` (encart pédagogique Tea App, fond orange)
- `.checklist-block` (déjà présent dans PR, à mutualiser)
- `.legal-grid` (grille 4 cartes cadre juridique)

### 4.4 Tagging architectures

Le fichier inclut déjà l'`arch-callout` recommandant **A2 ou A3 selon sensibilité de la donnée**. Vérifier que le lien vers `architectures.html` fonctionne (et que la page existe — produite en v3.5).

---

## 5. Lot 3 — Intégration CU-024 (Order-to-cash)

### 5.1 Action principale

Copier `mockup/modules/cu-024-order-to-cash.html` → `/modules/cu-024-order-to-cash.html`.

### 5.2 Ajout sur la home / page Modules

Ajouter une nouvelle card module :

- **Titre visible :** « Order-to-cash automation »
- **Niveau :** 7-8
- **Durée :** 22 min
- **Type :** Étude de cas + checklist
- **Axe pédagogique :** **B Décision** ou **A Productivité** (Blaise à trancher selon mapping axes existant — l'order-to-cash est productivité opérationnelle avec dimension décision/scoring)
- **Lien :** `modules/cu-024-order-to-cash.html`

### 5.3 Composants CSS spécifiques

- `.timeline-block` (frise calendrier réglementaire 2026-2027 — composant nouveau)
- `.timeline-grid` + `.timeline-step` (grille 4 colonnes)
- `.pa-table` (table plateformes agréées par segment)
- `.stage-card` (cartes 6 étapes du cycle)
- Reprend `.checklist-block`, `.alert-block`, `.arch-callout`

### 5.4 Tagging architectures

Le fichier recommande **A2 (propriétaire managé EU)** car la quasi-totalité des PA agréées DGFiP sont des SaaS européens. À préserver tel quel.

---

## 6. Lot 4 — Intégration CU-023 (Devis intelligent)

### 6.1 Action principale

Copier `mockup/modules/cu-023-devis-intelligent.html` → `/modules/cu-023-devis-intelligent.html`.

### 6.2 Ajout sur la home / page Modules

- **Titre visible :** « Génération de devis intelligente »
- **Niveau :** 4-6 (intermédiaire)
- **Durée :** 15 min
- **Type :** Auto-diagnostic
- **Axe pédagogique :** **A Productivité** ou **D Croissance** (Blaise à trancher)
- **Lien :** `modules/cu-023-devis-intelligent.html`

### 6.3 Composants CSS spécifiques

- `.tool-table` (table 7 outils, ré-utilisé de CU-027)
- `.stat-block` (encart bleu marine 36 min — composant introduit en PR-04, déjà mutualisé idéalement)
- `.alert-block` (5 écueils typiques)
- `.checklist-block` (auto-diagnostic 8 questions)
- `.pull-quote` (déjà présent dans plusieurs PR)

### 6.4 Pas de tagging architectures

CU-023 n'a pas d'arch-callout — c'est un cas SaaS sans débat (cf. veille). Pas d'encart d'architecture nécessaire.

---

## 7. Lot 5 — Mises à jour cross-site (cohérence numérique RULES 1.2)

**Le plus exigeant en attention.** Tu vas faire bouger 2 chiffres structurels. Tous les lieux doivent être synchronisés dans le **même commit** (RULES 1.2.1).

### 7.1 Chiffres à mettre à jour

| Avant v3.6 | Après v3.6 | Lieux à vérifier |
|---|---|---|
| `22 modules` / `22 cas d'usage` | `25 modules` / `25 cas d'usage` | home, page modules, à propos, méta-descriptions, footer textes |
| `CU-001 → CU-022` | `CU-001 → CU-027` (en notant que CU-025, CU-026 sont absents) | OU mieux : `25 cas d'usage` sans rangée numérotée |
| `6 préalables` | `7 préalables` | prealables.html, home, à propos |
| `CU-001 → CU-022` | À reformuler — la nouvelle séquence n'est plus continue | À discuter si tu rencontres ce pattern |

**Important** : la numérotation passe de 22 à 27 mais sans CU-025/026 (réservés v3.7). Si la formulation actuelle parle de « modules CU-001 à CU-022 », il faut la transformer en formulation neutre : « 25 cas d'usage opérationnels » (sans énumération continue qui supposerait une séquence sans trou).

### 7.2 Recherche cross-site obligatoire

Avant ton commit Lot 5, exécute :

```bash
grep -rn "22 modules\|22 cas d'usage\|22 cas\|CU-001 → CU-022\|CU-001 à CU-022" .
grep -rn "6 préalables\|PR-01 → PR-06\|PR-01 à PR-06" .
```

Tous les hits anciens doivent disparaître. Vérifie ensuite :

```bash
grep -rn "25 modules\|25 cas d'usage\|7 préalables"
```

Tous les nouveaux doivent apparaître. Si écart, le commit Lot 5 n'est pas prêt.

### 7.3 Mise à jour de la page À propos

L'introduction du site doit mentionner :

> Le Hub IA — Learning Center documente **25 cas d'usage opérationnels** (modules), **7 préalables transverses** (cadrages indispensables avant tout projet IA), **76 fiches outils** (référentiel), et une page transverse **Architectures de déploiement** (4 patterns canoniques).

---

## 8. Estimation effort consolidée

| Lot | Sujet | Effort estimé |
|---|---|---|
| Préalable | Lecture RULES.md | 30 min |
| Lot 1 | Intégration PR-07 + maj page index préalables | 1-2 h |
| Lot 2 | Intégration CU-027 + maj home | 1-2 h |
| Lot 3 | Intégration CU-024 + maj home | 1-2 h |
| Lot 4 | Intégration CU-023 + maj home | 1-2 h |
| Lot 5 | Mises à jour cross-site (cohérence numérique 22→25, 6→7) | 2-3 h |
| Tests croisés | Chrome/Firefox/Safari, mobile/desktop, sticky TOC | 1 h |
| **Total** | | **8-13 h** |

C'est une itération **plus dense que v3.5.1** (audit, 6-10 h) mais moins lourde que v3.5 (19-24 h). Le gros morceau attentionnel est le Lot 5 (cohérence numérique cross-site).

---

## 9. Workflow recommandé

1. **Vérifier que la PR v3.5.1 est mergée** sur main avant de commencer.
2. **Créer une branche `feat/v3.6-cu-pr-cycle-operationnel`**.
3. **Lire RULES.md en intégralité** avant toute action (préalable obligatoire).
4. **Ordre des lots** :
   - Lot 1 → Lot 2 → Lot 3 → Lot 4 (intégration des 4 fichiers, peut être en parallèle)
   - **Lot 5 EN DERNIER** : la cohérence numérique cross-site doit se faire après l'intégration des 4 nouveaux contenus.
5. **Tests croisés** Chrome / Firefox / Safari, mobile + desktop, sticky TOC fonctionnel sur les 4 nouvelles pages.
6. **PR avec description structurée** :
   - Lien vers ce brief
   - Lien vers RULES.md
   - Liste des commits (un par lot)
   - Confirmation que la checklist commit RULES section 2 a été passée

---

## 10. Décisions explicites de NE PAS faire dans cette itération

- **Pas de CU-025 / CU-026 / CU-028** (reportés à v3.7).
- **Pas de page « Par où commencer ? »** (encore reportée — pas de bande passante).
- **Pas de modification du design system** (`module-v3.css`, `module-v3.js` restent stables).
- **Pas d'ajout de fiches outils** (la catégorie « Outils de développement IA-assisté » sera renforcée en v3.7 si pertinente — voir CU-027 qui mentionne déjà Cursor, Claude Code, Windsurf etc.).
- **Pas de modification de l'audit qualité v3.5.1** (l'audit a corrigé les écarts existants — ne pas y rajouter de matière).

---

## 11. Notes éditoriales structurantes

### 11.1 PR-07 est le préalable conceptuel des 3 CU

L'agent de veille recommande explicitement de **publier PR-07 avant les 3 CU**. Si tu organises la home, mets PR-07 en avant (ex : « Avant de te lancer, lis PR-07 sur l'arbitrage build vs buy »). Les 3 CU font ensuite référence à PR-07 dans leur section 7 (« Pour aller plus loin »).

### 11.2 Distinction angle PME non-IT (CU-027) vs angle développeur (CU-015)

CU-027 et CU-015 traitent tous deux de l'IA appliquée au code — mais avec deux publics distincts :

- **CU-015** (existant, Stripe Minions / agents codeurs) : public **développeur professionnel** qui veut accélérer.
- **CU-027** (nouveau) : public **dirigeant PME non-IT** qui veut faire développer un outil métier sans recruter d'équipe.

Cette distinction doit rester lisible. Les deux modules linkent l'un vers l'autre dans leur section 7.

### 11.3 Le « scaling gap » est l'angle éditorial transversal

Les 4 livrables référencent le même chiffre structurant : <strong>95 % d'échec MIT NANDA + 88 % d'adoption / 6 % AI high performers McKinsey</strong>. C'est le contre-poison au FOMO. À préserver à l'identique partout.

### 11.4 Calendrier réglementaire 2026-2027 omniprésent

Trois échéances reviennent dans CU-024 et PR-07 : facturation électronique (sept. 2026 réception, sept. 2027 émission PME), AI Act haut-risque (août 2026). Ces dates doivent rester synchronisées entre CU-024, PR-05 (déjà existant), PR-07 et CU-027 si applicable.

### 11.5 Cohérence des sources prioritaires

Toutes les statistiques chiffrées des 4 livrables proviennent de sources prioritaires (Bpifrance Le Lab, McKinsey, MIT NANDA, Microsoft, France Num, Banque de France, CNIL, economie.gouv.fr). Aucune référence à un cabinet de conseil intermédiaire. À préserver.

---

## 12. Fichiers à modifier — récapitulatif rapide

**Création :**
- `/prealables/pr-07-build-vs-buy.html`
- `/modules/cu-023-devis-intelligent.html`
- `/modules/cu-024-order-to-cash.html`
- `/modules/cu-027-dev-applicatif-ia.html`

**Modification (cohérence numérique 22→25 et 6→7) :**
- `/index.html` (home)
- `/prealables.html` (page d'index préalables — ajout card PR-07 + chiffre 6→7)
- `/architectures.html` (mention « 22 cas d'usage » si présente)
- `/ressources.html` (mention « 22 modules » si présente)
- `/axes.html` (mention « 22 modules » si présente)
- Tous les fichiers `/prealables/pr-01-*.html` à `/prealables/pr-06-*.html` (mention « 6 préalables » dans les liens croisés)
- Tous les fichiers `/modules/cu-*.html` existants (footer ou mentions de nombre de modules)
- Méta-descriptions HTML de toutes les pages mentionnant le chiffre

**Vérification visuelle nav 6 entrées** :
La nav existante (Préalables / Architectures / Modules / Ressources / Axes / À propos) doit être identique sur les 4 nouveaux fichiers — c'est déjà le cas dans les sources, mais à vérifier par grep.

---

## 13. Validation finale avant PR

```
☐ RULES.md lu en intégralité avant de commencer.
☐ Les 4 fichiers HTML sont intégrés à la racine du repo.
☐ La nav 6 entrées est identique sur toutes les pages.
☐ La cohérence numérique cross-site est vérifiée par grep (22 → 25, 6 → 7).
☐ Les liens croisés CU↔PR↔Architectures fonctionnent.
☐ Aucun « PR-XX » ou « CU-XXX » visible dans les titres ou cards (RULES 1.3.6).
☐ Tests croisés Chrome / Firefox / Safari, mobile + desktop.
☐ Sticky TOC fonctionnelle sur les 4 nouvelles pages.
☐ Description de PR pointe vers ce brief + RULES.md.
☐ Checklist commit RULES section 2 passée intégralement.
```

---

## 14. Fichiers de référence (dans `site-web-prep/`)

- **Référentiel non négociable** : `RULES-IMPLEMENTATION.md` ← À LIRE EN PRÉALABLE
- **Brief de cette itération** : `BRIEF-CLAUDE-CODE-v3.6-passation.md` (ce fichier)
- **Veille v3.6 (matière éditoriale)** : `veille-v3.6-mai2026.md`
- **Brief audit v3.5.1** (référence) : `BRIEF-CLAUDE-CODE-v3.5.1-audit.md`
- **Brief v3.5** (référence) : `BRIEF-CLAUDE-CODE-v3.5-passation.md`

---

## 15. Contact

Pour toute question pendant l'intégration : Blaise Cavalli — blaise.cavalli@questforchange.eu

**Bonne mission, et merci pour le travail !**

---

*Brief produit par Cowork (Claude desktop) le 9 mai 2026. Cette itération v3.6 fait suite à v3.5.1 (audit qualité). Source du contenu : `veille-v3.6-mai2026.md` + 4 fichiers HTML produits en mockup.*
