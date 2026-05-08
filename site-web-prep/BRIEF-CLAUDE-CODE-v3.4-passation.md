# Brief Claude Code — Hub IA Learning Center (passation v3.4)

**Auteur :** Blaise Cavalli — Startup Manager Quai Alpha (Quest for Change)
**Date :** mai 2026
**Repo :** https://github.com/LumenBot/hub-ia
**Branche cible :** main
**Hébergement :** GitHub Pages
**Itération précédente :** v3.3 (3 nouveaux modules CU-020/021/022 + 13 fiches outils + nouvelle catégorie Voice)

---

## 0. Contexte court

L'itération **v3.4** introduit une **nouvelle section structurelle** au site : **« Préalables / Pré-requis »**. C'est un changement éditorial important qui clarifie la promesse du site :

- **Modules (CU-001 → CU-022)** = cas d'usage opérationnels (« j'ai un problème métier, voici la solution IA »)
- **Préalables (PR-01 → PR-06)** ← NOUVEAU = cadrages transverses (« qu'est-ce que je dois maîtriser avant de me lancer ? »)
- **Ressources** = fiches outils
- **À propos**

La logique pédagogique : <em>comprendre avant de faire</em>. Position dans la nav : **Préalables AVANT Modules** (mais la home reste centrée sur les modules — c'est le cœur de valeur du Learning Center).

**Tous les fichiers sources sont prêts dans `site-web-prep/mockup/`** :
- `prealables.html` — page d'index de la section
- `prealables/pr-01-maturite-organisationnelle.html` (15 min, avec auto-éval 10 questions)
- `prealables/pr-02-preables-data-si.html` (15 min, avec checklist 12 critères + verdict)
- `prealables/pr-03-maturite-humaine-formation.html` (12 min, avec grille dispositifs financement)
- `prealables/pr-04-marche-ia-emploi.html` (10 min, article chiffré PwC)
- `prealables/pr-05-securite-ia.html` (12 min, 3 cas DGSI + check-list)
- `prealables/pr-06-qualite-code-ia.html` (10 min, 7 alertes + 7 garde-fous Toad)

---

## 1. Lot 1 — Intégration de la section Préalables

### 1.1 Source

Les 7 fichiers HTML (1 index + 6 PR) sont **déjà au format V3 standard** (architecture mutualisée `module-v3.css` / `module-v3.js`, sticky TOC, executive summary, sections numérotées avec icônes). Aucune adaptation structurelle nécessaire pour l'essentiel.

### 1.2 Action principale

**Copier les fichiers** depuis `site-web-prep/mockup/` vers la racine du repo :
- `prealables.html` → `/prealables.html` (racine, page d'index)
- `prealables/pr-01-*.html` à `pr-06-*.html` → `/prealables/pr-01-*.html` à `pr-06-*.html` (nouveau dossier)

### 1.3 Spécificités à signaler

**Composants CSS spécifiques** introduits dans certains PR (à mutualiser dans `module-v3.css` ou conserver inline selon ton choix) :
- `.maturity-scale` + `.maturity-level` (5 niveaux colorés, PR-01 modèle 5R™ Cnam-Dejoux)
- `.funding-table` (table dispositifs financement, PR-03 — proche de `.compare-table` existant)
- `.case-card` (cartes cas DGSI rouges, PR-05)
- `.alert-block` + `.guardrail` (cartes alertes orange + garde-fous verts, PR-06)
- `.stat-block` (encart chiffre choc bleu marine, PR-04)
- `.pr-card` + `.prealables-grid` + `.prealables-hero` + `.prealables-intro` + `.prealables-footer-cta` (page d'index)

**Recommandation** : les composants spécifiques aux PR peuvent rester inline dans chaque fichier pour cette itération (ils ne sont utilisés qu'à un endroit). Si tu décides de mutualiser, créer un fichier dédié `prealables.css` plutôt que polluer `module-v3.css` qui est déjà chargé.

### 1.4 Mise à jour navigation principale

Sur **toutes les pages du site** (index, ressources, axes, modules CU, etc.), ajouter le lien **« Préalables »** dans la nav principale, **avant « Modules »**.

Format actuel (4 entrées) → nouveau format (5 entrées) :

```html
<!-- Avant -->
<a href="index.html#modules" class="nav-link">Modules</a>
<a href="ressources.html" class="nav-link">Ressources</a>
<a href="axes.html" class="nav-link">Axes</a>
<a href="index.html#a-propos" class="nav-link">À propos</a>

<!-- Après -->
<a href="prealables.html" class="nav-link">Préalables</a>
<a href="index.html#modules" class="nav-link">Modules</a>
<a href="ressources.html" class="nav-link">Ressources</a>
<a href="axes.html" class="nav-link">Axes</a>
<a href="index.html#a-propos" class="nav-link">À propos</a>
```

Les 7 fichiers PR + l'index utilisent `nav-link-active` sur l'entrée Préalables — cohérent avec le pattern v3.2.

---

## 2. Lot 2 — Mises à jour ciblées sur la page d'accueil

### 2.1 Intégration des 2 chiffres macro

**Page d'accueil (index.html)** : intégrer 2 chiffres choc identifiés par la veille complémentaire en accroche, à un endroit visible (idéalement dans le hero ou juste après la synthèse principale).

**Chiffre 1 — pourquoi les Préalables existent**
> **94 % des projets IA échouent** malgré 77 % de priorité dirigeants (étude AdvisoryX/DXC, janvier 2026). Pas la technologie — l'organisation, la data, la formation. Avant de te lancer, parcours les [Préalables](prealables.html).

**Chiffre 2 — pourquoi le Learning Center existe**
> **Productivité ×5** dans les secteurs très exposés à l'IA, **77 000 offres d'emploi** exigeant des compétences IA en France en 2023 (×7 vs 2018), **prime salariale +25 %** en moyenne. Le marché ne va pas attendre — le Hub IA donne les clés concrètes pour s'y mettre. (Source : PwC AI Jobs Barometer 2024)

**Format suggéré** : 2 encarts visuels distincts dans le hero ou en section dédiée juste après. Possible mise en forme avec `.stat-block` (composant introduit dans PR-04, à factoriser).

### 2.2 Lien depuis la home vers les Préalables

Ajouter un appel à l'action visible vers la nouvelle section : **« Avant de te lancer dans un cas d'usage, parcours les 6 préalables → »**

Position naturelle : entre la synthèse de la home et la grille des modules. Idéalement avec une icône distinctive (⚡ par ex.).

### 2.3 Section À propos — encart « Réseau QFC en chiffres » (déjà présent en v3.2)

L'encart existe déjà depuis v3.2. **Pas de modification nécessaire**, sauf si Blaise veut intégrer les chiffres macro (94 % / ×5). Au choix.

---

## 3. Lot 3 — Mise à jour CU-008 RAG (mention AMETRA)

### 3.1 Contexte

La veille complémentaire mai 2026 a identifié un retour d'expérience pertinent : **AMETRA Group + ECE — RAG documentaire technique** (cas client EvoliaStrategie, mais utilisé ici comme illustration de pattern, pas comme pub cabinet). Le cas est intéressant car concret et FR : « décennies d'expertise technique débloquées par un chatbot RAG sécurisé sur documentation interne ».

### 3.2 Action

Dans le module **CU-008 Knowledge base RAG** (`modules/cu-008-knowledge-base-rag.html`), ajouter dans la section « Pour aller plus loin » ou dans une section RetEx existante un paragraphe court :

> **Cas type — RAG documentaire technique en industrie française**. Une ETI industrielle (secteur infrastructures / défense, anonymisée) a déployé un agent RAG souverain sur sa documentation technique cumulant des décennies d'expertise — manuels, procédures, retours terrain, normes sectorielles. Output : moteur de connaissance qui répond aux questions des techniciens en 10 secondes là où une recherche manuelle prenait 30-60 minutes. Stack souveraine SecNumCloud, déploiement 4-6 mois. Témoignage public : « Outil maintenant indispensable pour transmettre l'expertise aux nouvelles équipes ».

**Note importante** : ne pas nommer le cabinet conseil (EvoliaStrategie) ni le client final (AMETRA Group) explicitement. Présenter comme un **pattern** illustré par un cas FR documenté, sans pub.

---

## 4. Lot 4 — Brief de communication

### 4.1 Mise à jour potentielle de l'À propos

L'introduction du site peut intégrer une phrase mentionnant la nouvelle section :

> Le Hub IA — Learning Center est une initiative portée par Quest for Change [...]. Il documente **22 cas d'usage opérationnels** (modules), **6 préalables transverses** (cadrages indispensables avant tout projet IA), et **76 fiches outils** (référentiel pour évaluer la stack adaptée à ton besoin).

### 4.2 Ordre suggéré pour les nouveaux porteurs Starter Class

Comme indiqué dans l'index `prealables.html` :

> **Ordre suggéré pour les nouveaux porteurs Starter Class** : PR-01 (organisationnel) → PR-02 (data/SI) → PR-03 (formation/financement) → un module CU correspondant à leur cas d'usage prioritaire.

Cet ordre peut servir de **parcours pédagogique guidé** dans la home ou la page À propos, voire dans une page dédiée « Par où commencer ? » à terme (pas dans cette itération, à mettre en pipeline v3.5).

---

## 5. Estimation effort Claude Code

| Lot | Sujet | Effort estimé |
|---|---|---|
| Lot 1 | Intégration 7 fichiers Préalables + nav cross-pages | 3-4 h |
| Lot 2 | Mises à jour home (2 chiffres macro + CTA Préalables) | 1-2 h |
| Lot 3 | Mention RetEx AMETRA dans CU-008 | 30 min |
| Lot 4 | Mise à jour À propos | 30 min |
| **Total** | | **5-7 h** |

C'est une itération plus légère que v3.3 — la matière éditoriale est déjà au format V3 propre, l'essentiel est l'intégration et la mise à jour structurelle de la nav.

---

## 6. Workflow recommandé

1. **Vérifier que la PR v3.3 est mergée** sur main avant de commencer
2. **Créer une branche `feat/v3.4-prealables`**
3. **Lot 1 d'abord** : intégrer la section Préalables, déployer en preview GitHub Pages, tester chaque page
4. **Lot 2 ensuite** : mises à jour home pour annoncer la nouvelle section
5. **Lot 3 et 4** : mises à jour mineures
6. **Tests croisés** Chrome / Firefox / Safari, mobile + desktop, sticky TOC fonctionnel sur les 6 PR
7. **PR avec description structurée** pointant vers ce brief

---

## 7. Décisions explicites de NE PAS faire dans cette itération

- **Pas de nouveaux modules CU** au-delà des 22 existants (les angles « préalables » deviennent des PR, pas des CU)
- **Pas de nouvelle catégorie d'outils Cabinets / Intégrateurs** dans la page Ressources (décision éditoriale Blaise : pas de pub pour acteurs)
- **Pas de fiches outils EvoliaStrategie / BusinessDigital** (même raison)
- **Pas de refonte de la home** (cœur de valeur, à préserver)
- **Pas de modification du reframing géographique** (validé en v3.1 / v3.2 / v3.3)

---

## 8. Notes éditoriales structurantes

### Distinction CU vs PR

Cette distinction est **importante éditorialement** et doit être respectée à la lettre :

- **Modules CU (cas d'usage)** : adressent une situation métier concrète (« je veux automatiser mes factures fournisseurs » → CU-021). Format : auto-diag ou étude de cas, plan d'action ou checklist d'éligibilité.
- **Préalables PR (cadrages)** : adressent une dimension transverse (« comment évaluer la maturité de mon SI ? » → PR-02). Format : article wiki avec auto-évaluation ou checklist quand pertinent, **mais pas** de plan d'action exportable comme les CU.

Cette distinction préserve la cohérence éditoriale et évite la confusion utilisateur.

### Liens croisés

Les 6 PR contiennent des **liens croisés systématiques** vers les modules CU pertinents et vice-versa. Vérifier l'intégrité de ces liens lors de l'intégration. Liens types :
- PR-01 → CU-020, CU-014
- PR-02 → CU-008, CU-013, CU-014
- PR-03 → CU-007, CU-020, CU-026 (CU-026 n'existe pas — c'est un placeholder pour une future fiche dédiée formation, à supprimer si non créée)
- PR-05 → CU-014, CU-020 + ressources Mistral, EthiqAIS
- PR-06 → CU-015 + ressources Claude Code, Cursor, Aider

### Composants visuels nouveaux

Les PR introduisent quelques composants visuels nouveaux. Tu peux les laisser inline (recommandation), ou les factoriser dans une feuille de style dédiée `prealables.css`. Choix d'architecture qui dépend de ton appréciation à la lecture du code.

---

## 9. Fichiers de référence (dans `site-web-prep/`)

- **Brief de cette itération** : `BRIEF-CLAUDE-CODE-v3.4-passation.md` (ce fichier)
- **Page d'index** : `mockup/prealables.html`
- **6 PR** : `mockup/prealables/pr-01-*.html` à `pr-06-*.html`
- **Veille complémentaire mai 2026** (référence) : `veille-complementaire-mai2026.md`
- **Brief v3.3** (référence) : `BRIEF-CLAUDE-CODE-v3.3-passation.md`

---

## 10. Contact

Pour toute question pendant l'intégration : Blaise Cavalli — blaise.cavalli@questforchange.eu

**Bonne mission, et merci pour le travail !**

---

*Brief produit par Cowork (Claude desktop) le 8 mai 2026. Cette itération v3.4 fait suite à la v3.3 (intégrée par Claude Code).*
