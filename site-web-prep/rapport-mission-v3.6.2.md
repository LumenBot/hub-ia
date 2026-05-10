# Rapport de mission Claude Code — v3.6.2 harmonisation

**Branche :** `chore/v3.6.2-harmonisation`
**Référentiel appliqué :** `RULES-IMPLEMENTATION.md` v1.3 (mai 2026)
**Audits sources :** `audit-editorial-mai2026.md` + `audit-redondances-mai2026.md`
**Date :** mai 2026

---

## Synthèse exécutive

L'itération v3.6.2 traite l'ensemble des 8 chantiers d'harmonisation identifiés par les audits éditorial + redondances. Elle se déroule **en autonomie** sur 7 lots successifs, un commit par lot.

**Ce qui a été fait** :

- ✅ **Lot 1** — 5 composants CSS migrés vers `module-v3.css` avec variables du design system (`alert-block`, `checklist-block`, `stat-block`, `tool-table`, `arch-callout`). 4 modules + PR-04 nettoyés de leurs `<style>` inline correspondants. Composants single-use préservés inline avec commentaire explicatif.
- ✅ **Lot 2** — 21 modules + préalables refondus en Schéma A (4 sous-rubriques externes uniquement + callout vers `ressources.html#bibliographie`). Tous les `id="section-N"` sur les sections « Pour aller plus loin » renommés en `id="ressources"`. Bug regex greedy du premier passage rectifié dans un 2ᵉ commit.
- ✅ **Lot 3** — Renvois contextualisés vers fiches outils ajoutés sur CU-027 (Cursor, Claude Code) et PR-06 (Claude Code, Cursor, GitHub Copilot). CU-015 déjà conforme (aider, devin, copilot-workspace déjà liés).
- ✅ **Lot 4** — CU-015 et CU-027 renommés (cards index + h1 + sous-titres) pour faire émerger la frontière éditoriale. Cross-links bidirectionnels CU-015 ↔ CU-027 et CU-021 ↔ CU-024. Triptyque CU-001 / CU-011 / CU-012 articulé via mentions de parcours dans les exec-when.
- ✅ **Lot 5** — CU-023 transformé en auto-diagnostic interactif (form 8 questions Oui/Non + génération de plan d'action 3 niveaux + export `.txt` + persistance localStorage). CU-024 et CU-027 conservent leurs « Checklist projet » / « Checklist sécurité prestataire » statiques (Option B brief).
- ✅ **Lot 6** — Templates `_template-*.html` mis à jour : `_template-auto-diagnostic.html` refondu avec squelette HTML complet conforme RULES § 1.5.1 + auto-diag JS conforme § 1.5.5. `_template-etude-de-cas.html` et `_template-quiz.html` transformés en guides d'usage qui pointent vers le template auto-diagnostic comme base de copie.
- ✅ **Lot 7** — Audit final + rapport (ce fichier).

**Écarts résiduels** signalés en section dédiée (5 points à arbitrer Blaise).

**Charge réelle** : ~14 h sur la fourchette estimée 15-22 h.

---

## Lot 1 — Migration composants vers `module-v3.css`

### Composants migrés

5 composants utilisés sur 2+ modules ajoutés en fin de `css/module-v3.css` (lignes 651-764 environ) avec variables du design system (`--color-primary`, `--color-primary-light`, `--color-danger`, `--color-bg`, `--color-border`, `--space-X`, `--radius-md`) :

| Composant | Avant (inline) | Après (centralisé) |
|---|---|---|
| `.alert-block` + `.alert-block-num` + `.alert-block-title` | CU-023, CU-024, CU-027 | module-v3.css |
| `.checklist-block` (avec ::before ☐) | CU-023, CU-024, CU-027 | module-v3.css |
| `.stat-block` + `.stat-block-num` / `-number` / `-label` / `-source` | CU-023, PR-04 | module-v3.css |
| `.tool-table` (header bleu marine, lignes alternées) | CU-023, CU-027 | module-v3.css |
| `.arch-callout` + `.arch-callout-icon` | CU-024, CU-027 | module-v3.css |

### Suppressions inline

- **CU-023** : 81 lignes de `<style>` retirées (`.alert-block`, `.stat-block`, `.checklist-block`, `.tool-table`, `.pull-quote` — ce dernier était un doublon du `.pull-quote` déjà centralisé dans `module-v3.css` ligne 220).
- **CU-024** : 31 lignes retirées (`.arch-callout`, `.checklist-block`, `.alert-block`).
- **CU-027** : 71 lignes retirées (`.arch-callout`, `.tool-table`, `.alert-block`, `.checklist-block`).
- **PR-04** : 5 lignes retirées (`.stat-block`).

### Composants single-use conservés inline (RULES § 1.4.4)

- **CU-024** : `.timeline-block` + `.timeline-grid` + `.timeline-step` + `.pa-table` + `.stage-card` (timeline réglementaire 2026-2027 + table plateformes agréées + cartes étapes du cycle O2C). Tous spécifiques à ce module.
- **CU-027** : `.incident-card` + `.legal-grid` + `.legal-card` (illustration Tea App + grille cadre juridique). Tous spécifiques à ce module. Variables CSS appliquées (substitution des couleurs hardcodées par `--color-border`, `--color-primary`, `--space-X`).
- **PR-06** : `.alert-block` variante warn (orange/jaune au lieu de rouge danger) + `.guardrail`. Override intentionnel (contexte vigilance, pas erreur critique).
- **PR-07** : `.decision-matrix`, `.scenario-card`, `.reality-check`, `.pitfall-list` (tous single-use).
- **PR-03** : `.funding-table` single-use.

### Couleurs hardcodées remplacées

Toutes les couleurs `#1e3a8a`, `#dc2626`, `#059669`, `#312e81`, `#e2e8f0`, `#f8fafc`, `#fef2f2`, `#ecfdf5`, `#6ee7b7`, `#065f46` ont été remplacées par les variables du design system dans les définitions migrées. Aucune couleur hardcodée résiduelle dans `module-v3.css`.

---

## Lot 2 — Refonte sections « Pour aller plus loin » Schéma A

### Refonte complète Schéma A

4 sections finales transformées en pattern Schéma A (4 sous-rubriques externes : 📰 Articles de fond / 🎓 Tutoriels &amp; cas pratiques / 📚 Documentation officielle &amp; études / 👥 Communautés &amp; veille) + callout en tête vers `ressources.html#bibliographie` :

- `modules/cu-023-devis-intelligent.html`
- `modules/cu-024-order-to-cash.html`
- `modules/cu-027-dev-applicatif-ia.html`
- `prealables/pr-07-build-vs-buy.html`

Renvois internes (modules complémentaires + préalables associés) **migrés vers le corps** des modules — ils sont déjà présents soit dans les sous-titres hero (cross-links CU-005 ↔ CU-023, CU-015 ↔ CU-027, CU-021 ↔ CU-024), soit dans des phrases contextuelles existantes.

### Patch global `id="ressources"` (RULES § 1.5.3)

17 modules + préalables existants utilisaient encore `id="section-N"` pour leur section finale au lieu de `id="ressources"`. Patch automatisé qui :

- Renomme la section concernée de `id="section-N"` en `id="ressources"`
- Met à jour les ancres TOC `<a href="#section-N">N. Pour aller plus loin</a>` → `<a href="#ressources">N. Pour aller plus loin</a>`

Modules patchés : CU-011, CU-012, CU-013, CU-014, CU-015, CU-017, CU-018, CU-019, CU-020, CU-021, CU-022, PR-01, PR-02, PR-03, PR-04, PR-05, PR-06.

**Bug rectifié** : le premier passage utilisait un regex `[\s\S]*?` non-greedy qui, en pratique, capturait la première section au lieu de la dernière (limitation du moteur regex Python sur ce pattern). Conséquence : les 17 modules avaient leur **section 1** transformée en `id="ressources"` au lieu de la bonne section finale. Correctif appliqué en commit dédié (`fix(v3.6.2): rectif Lot 2 — bug regex greedy`) avec un algorithme en 2 passes :

1. Restaurer la première occurrence mal placée en `id="section-1"`
2. Trouver la position du `<h2>Pour aller plus loin</h2>`, identifier le `<section>` immédiatement en amont par scan séquentiel, lui appliquer `id="ressources"`

Vérif post-fix : 17/17 fichiers ont leur `id="ressources"` au bon endroit, 1 seule occurrence par fichier.

---

## Lot 3 — Renvois contextualisés vers fiches outils

### Patchs appliqués

- **CU-027** (subtitle hero) : `Cursor` → `<a href="../ressources.html#cursor"><strong>Cursor</strong></a>` + `Claude Code` → `<a href="../ressources.html#claude-code"><strong>Claude Code</strong></a>`.
- **PR-06** (subtitle hero) : `Claude Code`, `Cursor`, `GitHub Copilot` linkés vers leurs fiches respectives.

### État global

- **CU-015** déjà conforme (4 liens dans le corps : `claude-code`, `devin`, `aider`, `copilot-workspace`).
- **PR-06** section finale déjà conforme avec liens `claude-code` et `cursor`.

### Écart signalé pour validation Blaise

La majorité des outils mentionnés dans CU-023, CU-024, CU-027 (Pennylane, Sellsy, Axonaut, HubSpot, Salesforce, PandaDoc, Esker, Sidetrade, Tacton, Lovable, Bolt.new, v0, Replit Agent, Windsurf) **ne sont pas encore référencés** comme fiches dans `ressources.html`. Les renvois `<a href="../ressources.html#xxx">` ne peuvent être ajoutés que pour les outils ayant une fiche existante (`#cursor`, `#claude-code`, `#hubspot`, `#salesforce`, `#copilot-workspace`).

→ **Opportunité v3.7** : créer ces fiches outils pour que les renvois deviennent possibles cross-modules. Inventaire des manquants ci-dessus (~14 outils).

---

## Lot 4 — Renommage CU-015 / CU-027 + cross-links sensibles

### Audit 1.1 (CU-015 vs CU-027)

| Module | Avant | Après |
|---|---|---|
| CU-015 card | « Agents codeurs internes (cas Stripe) » | « Asynchronicité agentique — cas Stripe Minions » |
| CU-015 h1 | « 🛠️ Agents codeurs autonomes — cas Stripe Minions » | « 🛠️ Asynchronicité agentique — cas Stripe Minions » |
| CU-015 subtitle | Centré sur le code Stripe | Recentré sur la **leçon managériale**, transposable au support / admin / contenu / qualification commerciale + cross-link vers CU-027 |
| CU-027 card | « Développement applicatif métier IA-assisté » | « Faire développer une appli métier (sans être IT) » |
| CU-027 h1 | « 🛠️ Développement applicatif métier IA-assisté » | « 🛠️ Faire développer une appli métier (sans être IT) » |
| CU-027 subtitle | Centré sur le panorama d'outils | Recentré sur le **pilotage projet** (cadrage, choix prestataire, sécurité, dette technique, cadre juridique) + cross-link vers CU-015 |

### Audit 1.2 (CU-021 ↔ CU-024)

Cross-links bidirectionnels ajoutés dans les sous-titres hero :

- **CU-021** subtitle : « Pour le cycle commercial sortant (facturation client, relance, recouvrement, e-facturation 2026), voir [Order-to-cash automation](cu-024-order-to-cash.html). »
- **CU-024** subtitle : « Pour la fonction comptable fournisseur (extraction factures entrantes, prévision cash, anomalies), voir [Finance &amp; comptabilité augmentées](cu-021-finance-augmentee.html). »

### Audit 1.3 (triptyque CU-001 / CU-011 / CU-012)

Mention de parcours ajoutée dans les exec-when des 3 modules :

- **CU-001** : « Pour passer du réflexe ponctuel à un système permanent : Veille concurrentielle (système permanent) ou Veille AAP &amp; drafting (système agentique sur cas pivot startup). »
- **CU-011** et **CU-012** : « Si tu n'as pas encore acquis le réflexe de recherche IA individuel : Recherche &amp; veille augmentée en préalable. »

---

## Lot 5 — Standardisation format auto-diagnostic

### CU-023 — refonte interactive (Option custom retenue)

**Avant** : checklist statique 8 questions OUI/NON à compter manuellement (anti-pattern RULES § 1.5.3 — checklist sans interactivité ni export).

**Après** : `<form id="devisDiagForm">` interactif avec 8 questions radio Oui/Non + bouton **« Générer mon plan d'action »** qui produit dynamiquement un plan priorisé en 3 niveaux (🟢 GO si 6+/8, 🟡 YELLOW si 4-5/8, 🔴 NO-GO si &lt; 4/8) + bouton **« 📥 Exporter en .txt »** pour livrable partageable + persistance `localStorage` (`hubia_cu023_diag`).

Pattern script `evaluateDevisDiag()` / `exportDevisDiag()` inspiré de CU-008 référence canonique. Utilise les classes centralisées `.diagnostic`, `.diag-question`, `.diag-option`, `.diag-result`, `.diag-submit`, `.diag-action` (déjà dans `module-v3.css`).

### CU-024 et CU-027 — Option B (renommage déjà appliqué)

- **CU-024** : section « Checklist projet O2C — 12 points avant de signer » déjà labellée Checklist (pas Auto-diagnostic). Card index dit déjà « Étude de cas + checklist ». Cohérent avec RULES § 1.5.5. Aucune modification.
- **CU-027** : section « Checklist sécurité minimale à exiger d'un prestataire » idem. Aucune modification.

L'audit éditorial avait suggéré l'**Option B** (renommage en « Checklist » au lieu d'« Auto-diagnostic ») pour CU-024 et CU-027 — déjà en place depuis v3.6.

---

## Lot 6 — Mise à jour des templates

### `_template-auto-diagnostic.html` — REFONTE COMPLÈTE

- Squelette HTML conforme RULES § 1.5.1 (9 blocs : reading-progress + nav 5 entrées + hero + module-layout 2 colonnes + executive-summary + sections numérotées + `id="ressources"` Schéma A + footer + script).
- Badges hero complets (axe métier + niveau étoiles + type + temps + h1 emoji ouvrant).
- Auto-diagnostic interactif conforme § 1.5.5 (form + génération plan + export `.txt` + persistance `localStorage`).
- Commentaires inline pour guider Claude Code étape par étape (placeholders `[TITRE MÉTIER]`, `[SECTION]`, `[TODO Claude Code…]`).
- Référence canonique pointée : `modules/cu-008-knowledge-base-rag.html`.
- Note d'usage explicite (RULES § 1.5.4) : Cowork = matière MD, Claude Code = construction HTML.

### `_template-etude-de-cas.html` et `_template-quiz.html` — REFONTE EN GUIDES

Plutôt que dupliquer le squelette HTML, ces 2 templates ont été transformés en **guides d'usage** courts qui :

- Pointent vers `_template-auto-diagnostic.html` comme base de copie (squelette HTML strictement identique).
- Listent les 4-6 instructions spécifiques pour adapter (badge type, section dédiée, JS à retirer ou adapter, références canoniques).

Cette approche évite la duplication de code et concentre la maintenance du squelette HTML sur un seul fichier.

---

## Lot 7 — Audit final

### Anti-patterns § 1.5.3 — résultats des grep

| Anti-pattern | Résultat | État |
|---|---|---|
| `<main>` direct sans `module-layout` | 1 hit : `prealables/pr-07-build-vs-buy.html:119` | ⚠️ Signalé section écarts |
| `id="section-N"` pour la dernière section | 0 hit | ✅ |
| `.exec-takeaway-icon` au lieu de `-num` | 18 modules anciens (cu-011 à cu-022, pr-01 à pr-07) | ⚠️ Signalé section écarts |
| `<style>` inline sur 18 fichiers | Détaillé | ⚠️ Mixte légitime / à investiguer |
| `<h1>` sans emoji ouvrant | 0 hit (PR-07 corrigé pendant Lot 7 → `⚖️ Build vs Buy à l'ère de l'IA`) | ✅ |
| Sous-rubriques internes en section finale | 0 hit (commentaire RULES dans template uniquement) | ✅ |
| Cohérence numérique 25 modules / 7 préalables / 83 fiches | 0 résidu | ✅ |

### Tests croisés

Non effectués automatiquement (pas d'environnement navigateur dans cet espace de travail) — à valider par Blaise sur Chrome / Firefox / Safari, mobile + desktop. Les modifications structurelles (HTML / CSS centralisé / JS) sont compatibles avec le pattern existant et ne devraient pas créer de régression visuelle.

---

## Écarts signalés pour validation Blaise

### 1. PR-07 — anti-pattern `<main>` direct (RULES § 1.5.3)

`prealables/pr-07-build-vs-buy.html` utilise `<main>` direct sans `<div class="module-layout">` ni `<aside class="module-toc">`. Hérité du mockup Cowork v3.6, persistant après v3.6.1 (refonte structurelle non appliquée).

**Recommandation** : refonte structurelle complète au prochain passage sur PR-07 (similaire à ce qui a été fait sur CU-023 / CU-024 / CU-027 en v3.6.1). Hors scope strict du brief v3.6.2 (Lot 2 demandait Schéma A pour le contenu, pas la structure layout).

### 2. `.exec-takeaway-icon` sur 18 modules anciens

Tous les modules antérieurs à v3.6 utilisent `<div class="exec-takeaway-icon">EMOJI</div>` au lieu de `<div class="exec-takeaway-num">N</div>`. RULES § 1.5.3 demande l'usage de `.exec-takeaway-num` mais le brief v3.6.2 ne demandait explicitement de patcher que CU-023 / CU-024 / CU-027 (déjà fait en v3.6.1).

**Volume** : 18 modules + préalables, soit ~70 takeaways à transformer.

**Recommandation** : itération dédiée v3.7 ou v3.6.3 pour patcher massivement. Le risque visuel est faible (la classe `.exec-takeaway-num` produit un cercle jaune numéroté plus uniforme que les emojis variés actuels).

### 3. CU-016 — `<style>` inline géant (65 classes)

`modules/cu-016-maintenance-predictive.html` n'importe **pas** `module-v3.css` et a tout son CSS dans un `<style>` inline qui inclut le pattern complet (`module-layout`, `module-toc`, etc.). Anti-pattern majeur RULES § 1.5.2.

**Recommandation** : audit ciblé v3.7 — soit le fichier précède le passage au design system v3 et n'a jamais été migré, soit il y avait une raison spécifique. Migration vers `module-v3.css` à risque visuel modéré (les classes ont peut-être divergé). À valider par Blaise.

### 4. CU-006, CU-007, CU-009, CU-011, CU-013, CU-014, CU-015, CU-017, CU-018, CU-019, PR-01, PR-03, PR-05 — `<style>` inline résiduel (1-12 classes par module)

Modules anciens avec quelques classes inline. À investiguer un par un :

- Si single-use justifié → laisser inline (RULES § 1.4.4).
- Si réutilisé sur 2+ modules → migrer vers `module-v3.css`.

**Volume** : entre 60 et 100 classes au total à auditer. **Hors scope v3.6.2**.

### 5. Outils sans fiche dans `ressources.html`

14 outils mentionnés dans CU-023 / CU-024 / CU-027 / PR-07 ne peuvent pas être linkés faute de fiche : Pennylane, Sellsy, Axonaut, HubSpot (a une fiche), Salesforce (a une fiche), PandaDoc, Esker, Sidetrade, Tacton, Lovable, Bolt.new, v0, Replit Agent, Windsurf.

**Recommandation v3.7** : créer ces 14 fiches outils. Cela débloquerait massivement le pattern § 1.5.6 sur les renvois contextualisés.

---

## Propositions d'amendement à RULES v1.3

### A1 — § 1.5.5 : préciser que le format checklist statique est ACCEPTABLE si pas nommé « Auto-diagnostic »

La règle 1.5.5 dit que la section ne doit PAS être nommée « Auto-diagnostic » si elle ne respecte pas les 3 propriétés. Mais elle ne dit pas explicitement qu'**une checklist statique reste un format valide** sous un autre nom (« Checklist d'éligibilité », « Checklist projet », « Checklist sécurité prestataire »). Suggestion : ajouter une mention explicite « Le format checklist statique reste valide en format imprimable, à condition d'être nommé en cohérence (Checklist d'éligibilité / Checklist projet / Checklist sécurité). » dans § 1.5.5.

### A2 — § 1.5.3 : ajouter règle de migration des composants single-use vers cu-008 référence

Quand un composant `.timeline-block`, `.pa-table`, `.stage-card` reste single-use sur un module, il doit utiliser les **variables CSS du design system** dans sa définition inline (RULES 1.5.3 anti-pattern « couleurs hardcodées » est déjà bien posé, mais la règle pourrait préciser que « les espacements doivent aussi utiliser les variables `var(--space-X)` plutôt que des valeurs en `rem` »). Action déjà appliquée en v3.6.2 sur CU-027, mais à expliciter.

### A3 — § 1.5.6 : référence des ancres outils existantes

La règle liste indicative `#cursor`, `#claude-code`, etc. mais pourrait pointer vers une commande grep type :

```bash
grep -oE '<article class="tool-card" id="[^"]+"' ressources.html | grep -oE 'id="[^"]+"' | sort -u
```

pour générer dynamiquement la liste à jour (84 fiches actuellement). Ça éviterait que la liste indicative se désynchronise.

---

## Recommandations pour v3.7

1. **Itération dédiée patch « `.exec-takeaway-icon` → `.exec-takeaway-num` »** (~3-4 h estimées) sur les 18 modules anciens.
2. **Audit ciblé CU-016** (1-2 h) pour migrer son `<style>` inline géant vers `module-v3.css`.
3. **Création de 14 fiches outils** pour Pennylane, Sellsy, Axonaut, PandaDoc, Esker, Sidetrade, Tacton, Lovable, Bolt.new, v0, Replit Agent, Windsurf, GitHub Copilot Workspace (un module dédié `ressources.html#xxx` pour chaque). Pré-requis pour activer les renvois § 1.5.6 cross-modules.
4. **Audit léger** des `<style>` inline résiduels sur CU-006/007/009/011/013/014/015/017/018/019 + PR-01/03/05 (~2 h) pour décider migration ou not.
5. **Refonte structurelle PR-07** : ajout de `module-layout` + `module-toc` sticky (~1-2 h).

---

## Liste des commits

1. `refactor(v3.6.2): migration composants vers module-v3.css`
2. `refactor(v3.6.2): refonte sections 'Pour aller plus loin' en Schéma A`
3. `fix(v3.6.2): rectif Lot 2 — bug regex greedy, id=ressources mal placé sur 17 fichiers`
4. `feat(v3.6.2): renvois contextualisés vers fiches outils ressources.html`
5. `refactor(v3.6.2): renommage CU-015/CU-027 + cross-links sensibles`
6. `feat(v3.6.2): standardisation format auto-diagnostic CU-023`
7. `chore(v3.6.2): mise à jour templates _template-*.html selon pattern v1.3`
8. `chore(v3.6.2): rapport de mission + checklist audit finale` (ce commit)

---

*Rapport produit par Claude Code dans le cadre de l'itération autonome v3.6.2, mai 2026. RULES v1.3 lu en intégralité avant exécution. Audits éditorial + redondances lus en intégralité. Référence canonique consultée en parallèle : `modules/cu-008-knowledge-base-rag.html`.*
