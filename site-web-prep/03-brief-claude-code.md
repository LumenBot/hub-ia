# Brief technique — Site Hub IA territorial

> **Destinataire** : session Claude Code
> **Objectif** : implémenter et déployer un site web statique de micro-learning sur l'IA en entreprise, inspiré de qfc-num, hébergé sur GitHub Pages dans le repo `LumenBot/hub-ia`.
> **Statut V1.1** — Mai 2026, intègre les 3 formats pédagogiques validés par Blaise.

---

## Contexte

Le site est un **support pédagogique du programme Hub IA territorial** porté par Quai Alpha (incubateur du réseau Quest for Change). Il vise deux publics :

1. **Cible primaire** : les startups que Quai Alpha accompagne (réseau QFC).
2. **Cible secondaire** : les entreprises (PME/ETI) du territoire vosgien.

Le site reprend le pattern de **micro-learning par modules courts** du site qfc-num (https://louislecce.github.io/qfc-num) et l'adapte à 18+ cas d'usage de l'IA en entreprise classés par complexité croissante.

---

## Décisions structurantes (validées avec Blaise)

| Sujet | Décision |
|---|---|
| Repo | `LumenBot/hub-ia` créé, MIT License |
| Domaine | `lumenbot.github.io/hub-ia/` en V1, domaine custom à arbitrer en V2 |
| Branding | Logo « Hub IA » seul en V1, cobranding QFC/QA en V2 |
| Communication de lancement | Partage interne au GT IA QFC, pas de LinkedIn en V1 |
| Format pédagogique | **Mix selon le niveau** (cf. section dédiée ci-dessous) |

---

## Format pédagogique différencié par niveau

C'est le choix structurant de la V1.1 :

### 🟢 Niveau N1-N3 (Fondamentaux) — **Quiz court**

5 questions QCM avec 4 options. Validation côté client avec feedback immédiat. Score affiché. Persistance localStorage. Format adapté à la vérification de compréhension de notions fondamentales.

**Template à reprendre** : `mockup/modules/cu-001-recherche-veille.html` ou `mockup/modules/cu-002-assistant-redactionnel.html`.

**Modules concernés** : CU-001, CU-002, CU-003, CU-004.

### 🟡 Niveau N4-N6 (Applications métier) — **Auto-diagnostic + plan d'action**

Échelle de positionnement (1-5) sur la maturité actuelle, identification du cas concret applicable, formulation du frein principal, planification du premier pas concret, définition d'un indicateur de succès. Génération automatique d'un plan d'action personnalisé. **Export en .txt** pour partage / archivage. Format adapté à des décideurs qui ont besoin d'**appliquer** plutôt que de réviser.

**Template à reprendre** : `mockup/modules/_template-auto-diagnostic.html` et exemple complet `mockup/modules/cu-005-devis-propositions.html`.

**Modules concernés** : CU-005, CU-006, CU-007, CU-008, CU-009, CU-010, CU-011, CU-019.

### 🔴 Niveau N7-N8 (Industrialisation) — **Étude de cas + checklist d'éligibilité**

Cas concret guidé suivi d'une **checklist d'éligibilité pondérée** (~10 items répartis en 3 sections : prérequis techniques, compétences, conditions organisationnelles). Score d'éligibilité calculé, verdict commenté avec recommandation contextuelle (« forte / partielle / à construire »). Format adapté à des projets structurants où la maturité organisationnelle conditionne le déploiement.

**Template à reprendre** : `mockup/modules/_template-etude-de-cas.html` et exemples complets `mockup/modules/cu-013-workflow-email-crm.html`, `mockup/modules/cu-016-maintenance-predictive.html`.

**Modules concernés** : CU-012, CU-013, CU-014, CU-015, CU-016, CU-017, CU-018.

### Tableau récapitulatif

| Niveau | Format | Logique pédagogique | Persistance | Export |
|---|---|---|---|---|
| N1-N3 | Quiz 5 questions | Vérifier compréhension | Score + date | Non |
| N4-N6 | Auto-diagnostic + plan d'action | Faire appliquer | Plan personnalisé + date | .txt |
| N7-N8 | Étude de cas + checklist | Évaluer maturité | Score d'éligibilité + date | Non (V1) |

---

## Ressources fournies dans `site-web-prep/`

Six fichiers prêts à utiliser dans Claude Code :

1. **`01-mapping-pedagogique.md`** — architecture pédagogique : 18 modules en 3 sections, sélection des 5 premiers à produire.

2. **`02-design-system.md`** — charte visuelle complète : couleurs (héritées QA), typo Inter, composants UI, conventions iconographiques, responsive.

3. **`03-brief-claude-code.md`** (ce fichier) — specs techniques détaillées + roadmap d'implémentation.

4. **`mockup/index.html`** — page d'accueil complète avec les 18 cards modules.

5. **`mockup/css/style.css`** — design system complet (~850 lignes), variables CSS, navbar, hero, cards par niveau coloré, page module, quiz, responsive.

6. **`mockup/modules/`** — pages modèles **prêtes à dupliquer** :
   - `cu-001-recherche-veille.html` — exemple **format quiz** (N1-N3)
   - `cu-002-assistant-redactionnel.html` — exemple **format quiz** (N1-N3)
   - `cu-005-devis-propositions.html` — exemple **format auto-diagnostic** (N4-N6)
   - `cu-013-workflow-email-crm.html` — exemple **format étude de cas** (N7-N8)
   - `cu-016-maintenance-predictive.html` — exemple **format étude de cas** (N7-N8)
   - `_template-auto-diagnostic.html` — template vierge auto-diagnostic
   - `_template-etude-de-cas.html` — template vierge étude de cas

L'**encyclopédie source** (`Canaux/Hub-IA/encyclopedie/`) contient les **19 fiches détaillées** de cas d'usage qui doivent être adaptées en modules pédagogiques.

---

## Stack technique

Cohérent avec qfc-num (sobriété et simplicité) :

- **HTML5 + CSS3 + JS vanilla** — pas de framework, pas de build process
- **Polices** : Inter (Google Fonts) + emoji système
- **Hébergement** : GitHub Pages, branche `main`, dossier racine
- **Pas de backend** — toute persistance via `localStorage`
- **Pas de dépendances JS** — code natif, lecture facile, maintenance simple

---

## Structure du repo cible

```
hub-ia/                          ← repo LumenBot/hub-ia
├── index.html                   ← landing page (depuis mockup)
├── README.md                    ← présentation du repo
├── LICENSE                      ← MIT (déjà créé)
├── css/
│   └── style.css                ← design system unique
├── js/
│   └── main.js                  ← logique navbar + persistence
├── modules/
│   ├── cu-001-recherche-veille.html       ← N1 quiz (fait)
│   ├── cu-002-assistant-redactionnel.html ← N1 quiz (fait)
│   ├── cu-003-cr-reunion.html             ← N1 quiz (TODO)
│   ├── cu-004-traduction.html             ← N1 quiz (TODO)
│   ├── cu-005-devis-propositions.html     ← N2 auto-diag (fait)
│   ├── cu-006-leads-chatbot.html          ← N2 auto-diag (TODO)
│   ├── cu-007-rh-cv-entretiens.html       ← N2 auto-diag (TODO)
│   ├── cu-008-knowledge-base-rag.html     ← N2 auto-diag (TODO)
│   ├── cu-009-content-repurposing.html    ← N2 auto-diag (TODO)
│   ├── cu-010-pipeline-contenu-social.html← N2 auto-diag (TODO)
│   ├── cu-011-veille-concurrentielle.html ← N2 auto-diag (TODO)
│   ├── cu-012-veille-aap-drafting.html    ← N3 étude cas (TODO)
│   ├── cu-013-workflow-email-crm.html     ← N3 étude cas (fait)
│   ├── cu-014-multi-agents.html           ← N3 étude cas (TODO)
│   ├── cu-015-stripe-minions.html         ← N3 étude cas (TODO)
│   ├── cu-016-maintenance-predictive.html ← N3 étude cas (fait)
│   ├── cu-017-controle-qualite-vision.html← N3 étude cas (TODO)
│   ├── cu-018-optimisation-production.html← N3 étude cas (TODO)
│   ├── cu-019-newsletter-locale.html      ← N2 auto-diag (TODO V1+)
│   ├── _template-quiz.html                ← template recopiable
│   ├── _template-auto-diagnostic.html     ← template recopiable
│   └── _template-etude-de-cas.html        ← template recopiable
├── assets/
│   ├── logo.svg
│   ├── favicon.ico
│   └── og-image.png
└── .nojekyll                    ← important pour GitHub Pages
```

---

## Roadmap d'implémentation

### Phase 1 — Mise en place (estimé 2 h)

1. Cloner `LumenBot/hub-ia` localement.
2. Copier le contenu de `mockup/` à la racine du repo (en respectant la structure `index.html`, `css/`, `modules/`).
3. Créer un fichier `.nojekyll` à la racine.
4. Activer GitHub Pages dans Settings → Pages → Source : `main` / `(root)`.
5. Tester l'accès au site via `https://lumenbot.github.io/hub-ia/`.
6. Mettre à jour le `README.md` du repo avec une description courte + lien vers le site.

### Phase 2 — Adaptation des liens et déploiement de la base

1. Vérifier que tous les liens internes de `index.html` pointent bien vers `modules/cu-NNN-...html`.
2. Tester le rendu mobile, tablette, desktop.
3. Pousser un premier déploiement avec les 5 modules déjà produits (CU-001, CU-002, CU-005, CU-013, CU-016).
4. Pour les modules non encore produits, créer des pages stub (titre + redirection vers une page « bientôt disponible ») pour ne pas avoir de liens cassés.

### Phase 3 — Production des 13 modules manquants (estimé 8-12 h selon volume éditorial)

Pour chacun :

1. Recopier le template adapté au niveau (`_template-quiz.html`, `_template-auto-diagnostic.html`, `_template-etude-de-cas.html`).
2. Adapter le contenu pédagogique à partir de la fiche encyclopédie correspondante (`encyclopedie/03-cas-usage/cu-NNN-...md`).
3. Pour les **quiz** : préparer 5 QCM avec corrections argumentées dans la fiche source.
4. Pour les **auto-diagnostics** : adapter les 5 questions (positionnement + cas concret + frein + premier pas + indicateur).
5. Pour les **études de cas** : adapter la checklist d'éligibilité (3 sections : prérequis / compétences / conditions, ~10 items pondérés au total).
6. Tester chaque module : rendu, persistance localStorage, export (pour auto-diag).

> **Note importante** : la matière éditoriale détaillée des modules manquants peut être produite en parallèle dans Cowork (sessions de travail avec Blaise). Claude Code peut commencer par la mise en place technique et les modules dont la matière est prête.

### Phase 4 — Polish (estimé 2 h)

1. Ajouter assets : logo.svg « Hub IA », favicon.ico, og-image.png pour partage social.
2. Vérifier accessibilité (audit Lighthouse — viser > 90).
3. Optimiser performances (compression images, lazy loading si applicable).
4. Ajouter meta tags SEO (description, og:image, og:title, twitter:card).
5. Tester sur Chrome, Safari, Firefox.

### Phase 5 — V2 (futurs sprints) — Filtres dynamiques

1. Panel de filtres au-dessus des sections : cible, fonction métier, filière.
2. `data-attributes` sur chaque card.
3. JavaScript de filtrage dynamique.
4. Persistance des filtres dans localStorage.

### Phase 6 — V3 (futurs sprints) — Parcours guidés par profil

5 parcours préconçus avec progression séquentielle. Voir `01-mapping-pedagogique.md`.

---

## Conventions importantes

### IDs de module

Format strict : `cu-NNN-titre-court-tirets` (ex. `cu-001-recherche-veille`).

### Persistance localStorage

Clé : `hubia_<module-id>` (ex. `hubia_cu-001`).

Valeur (JSON) selon format pédagogique :

**Quiz** :
```json
{ "completed": true, "score": 4, "total": 5, "date": "..." }
```

**Auto-diagnostic** :
```json
{ "completed": true, "positionnement": "3", "casConcret": "...", "frein": "...", "premierPas": "...", "indicateur": "...", "date": "..." }
```

**Étude de cas** :
```json
{ "completed": true, "score": 9, "total": 14, "percent": 64, "date": "..." }
```

### Tags dans les cards (data-attributes pour V2)

```html
<a href="..." class="card n2"
   data-module="cu-005"
   data-cible="les-deux"
   data-niveau="n4-n6"
   data-fonctions="commercial,direction-generale"
   data-filieres="transverse"
   data-axe="4">
```

### Conventions Git

- Branches : `main` (prod), `dev` (intégration), `feat/...` ou `fix/...`
- Commits conventionnels : `feat: ...`, `fix: ...`, `content: ...`, `docs: ...`

---

## Checklist V1 — Site fonctionnel publié

- [ ] Repo cloné, structure mise en place
- [ ] index.html déployé et fonctionnel
- [ ] CSS centralisé dans `css/style.css`
- [ ] JavaScript extrait dans `js/main.js`
- [ ] 19 pages modules créées (au moins squelette pour les TODO)
- [ ] Au minimum les 5 modules avec contenu pédagogique complet et format adapté (quiz / auto-diag / étude de cas) déployés
- [ ] Responsive testé sur mobile, tablette, desktop
- [ ] localStorage testé (persistance fonctionnelle pour les 3 formats)
- [ ] Auto-diagnostic — export .txt fonctionnel
- [ ] Étude de cas — calcul de score et verdict fonctionnel
- [ ] Accessibilité Lighthouse > 90
- [ ] Performance Lighthouse > 90
- [ ] GitHub Pages configuré et accessible sur `lumenbot.github.io/hub-ia/`
- [ ] README du repo mis à jour
- [ ] Logo « Hub IA » créé et placé dans assets
- [ ] OG image pour partage social

---

## Articulation avec les sessions Cowork à venir

Pendant que Claude Code implémente le site, Cowork continue de produire :

- **Matière éditoriale détaillée** des modules manquants (CU-003, CU-004 quiz / CU-006-011 auto-diag / CU-012, CU-014, CU-015, CU-017, CU-018 étude de cas / CU-019 newsletter).
- **Itération sur le design** si Blaise valide une orientation différente après avoir vu le mockup en ligne.
- **Préparation du message de partage** au GT IA QFC pour le lancement (format court, factuel, pas marketing).

Cette répartition optimise la valeur ajoutée de chaque outil : Cowork sur la conception et la rédaction, Claude Code sur l'implémentation.

---

## Liens utiles

- **Référence** : qfc-num site web — https://louislecce.github.io/qfc-num
- **Référence** : qfc-num repo — https://github.com/louislecce/qfc-num
- **Repo cible** : LumenBot/hub-ia — https://github.com/LumenBot/hub-ia (créé MIT)
- **Encyclopédie source** : `Canaux/Hub-IA/encyclopedie/` (19 fiches cas d'usage en V1.1)
- **Note de cadrage** : `Canaux/Hub-IA/outputs/note-cadrage-Hub-IA-territorial.docx`

---

*Brief produit en mai 2026 — V1.1, intègre les 3 formats pédagogiques différenciés.*
