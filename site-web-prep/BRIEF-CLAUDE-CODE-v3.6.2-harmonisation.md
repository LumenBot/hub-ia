# Brief Claude Code — Hub IA Learning Center (harmonisation v3.6.2)

**Auteur :** Blaise Cavalli — Startup Manager Quai Alpha (Quest for Change)
**Date :** mai 2026
**Repo :** https://github.com/LumenBot/hub-ia
**Branche cible :** main
**Hébergement :** GitHub Pages
**Itération précédente :** v3.6.1 (correction technique des mockups Cowork v3.6)
**Nature de cette itération :** HARMONISATION CONJOINTE FOND + FORME — pas d'ajout de contenu, uniquement consolidation transversale après audit conjoint Cowork + Claude Code.

---

## 0. Contexte court — pourquoi v3.6.2

L'audit éditorial complet du site (`audit-editorial-mai2026.md`) a fait apparaître 8 chantiers d'harmonisation à mener avant tout nouveau contenu (v3.7). Cette itération v3.6.2 est **dédiée à la consolidation**. Aucun nouveau module, aucune nouvelle fiche outil, aucun nouveau préalable. **Uniquement de la révision transversale.**

**Tu travailles en autonomie.** Blaise ne sera pas en revue continue. Tu suis ce brief, tu produis le rapport de mission à la fin, tu pousses la PR.

**Origine et grain de l'audit :**
- Audit redondances éditoriales (`audit-redondances-mai2026.md`) — 5 paires/triplets analysés
- Audit conformité technique (constats détaillés repris ci-dessous + `audit-editorial-mai2026.md`)
- Décisions Blaise sur 3 points clés (Option A pour section ressources finale, format auto-diag hybride, mise à jour template)

---

## 1. Préalable obligatoire — RULES v1.3

**AVANT toute action de code**, tu dois lire **intégralement** `site-web-prep/RULES-IMPLEMENTATION.md` (version **1.3**, mise à jour aujourd'hui suite à cet audit). Trois nouveautés majeures qui structurent ta mission :

- **§ 1.5.1 (squelette HTML)** : la section finale `id="ressources"` est désormais refondue en **Schéma A** — 4 sous-rubriques **externes uniquement** (Articles de fond / Tutoriels / Documentation officielle / Communautés) + callout vers `ressources.html#bibliographie`. **Plus de sous-rubriques internes** (Modules complémentaires, Préalables associés) à cet endroit.
- **§ 1.5.5 (NOUVELLE)** : Format auto-diagnostic standard — 3 propriétés obligatoires (form interactif + génération plan + export). Si une section ne les respecte pas, elle ne peut plus s'appeler « Auto-diagnostic ».
- **§ 1.5.6 (NOUVELLE)** : Renvois internes contextualisés dans le corps des modules (vers fiches outils via `ressources.html#xxx`, vers préalables, vers architectures). Cross-links obligatoires sur paires sensibles (CU-015↔CU-027, CU-021↔CU-024, triptyque CU-001/011/012).

**Référence visuelle commune** : `modules/cu-008-knowledge-base-rag.html` reste le module canonique. C'est la cible vers laquelle harmoniser.

---

## 2. Méthode — 7 lots à exécuter dans l'ordre

### Lot 0 — Préalable (15-30 min)

1. Lire `site-web-prep/RULES-IMPLEMENTATION.md` v1.3 en intégralité.
2. Lire `site-web-prep/audit-editorial-mai2026.md` en intégralité.
3. Lire `site-web-prep/audit-redondances-mai2026.md` en intégralité.
4. Ouvrir `modules/cu-008-knowledge-base-rag.html` comme onglet de référence (à consulter en parallèle pendant tout le brief).
5. Ouvrir `css/module-v3.css` pour vérifier les composants déjà centralisés.

### Lot 1 — Migration des composants vers `module-v3.css` (3-4 h)

**Référence RULES** : §§ 1.4.4, 1.5.2, 1.5.3 (renforcée v1.3).

**Méthode.**

1. Identifier les composants qui apparaissent en `<style>` inline sur 2+ modules (CU-023, CU-024, CU-027 + potentiellement PR-06, PR-07, autres) :
   - `.alert-block` (utilisé sur CU-023, CU-024, CU-027, PR-06)
   - `.checklist-block` (utilisé sur CU-023, CU-024, CU-027 + PR-02, PR-03, PR-06, PR-07)
   - `.stat-block` (CU-023, PR-04)
   - `.tool-table` (CU-023, CU-027)
   - `.arch-callout` (CU-024, CU-027 + futurs modules sensibles)

2. Pour chacun, **migrer la définition vers `module-v3.css`** en adaptant les couleurs hardcodées vers les variables du design system (`--color-primary`, `--color-warning`, `--color-success`, `--color-surface`, etc.). Lire les variables définies dans `style.css` pour identifier les bonnes correspondances.

3. **Supprimer** les définitions correspondantes dans les `<style>` inline des modules concernés.

4. Cas particulier `.pull-quote` : déjà centralisé dans `module-v3.css` (ligne 220-222 environ) — donc CU-023 le redéfinit en doublon. **Supprimer la redéfinition** dans `<style>` inline de CU-023.

5. Composants utilisés une seule fois (ex : `.timeline-block` dans CU-024, `.incident-card` dans CU-027, `.legal-grid` dans CU-027) : laisser inline pour cette itération, mais migrer si réutilisés.

**Livrable Lot 1.**
- Commit `refactor(v3.6.2): migration composants vers module-v3.css`
- Diff lisible : ajouts dans `module-v3.css` + suppressions correspondantes dans modules
- Pas de régression visuelle (vérifier visuellement chaque module impacté)

### Lot 2 — Refonte des sections finales "Pour aller plus loin" en Schéma A (3-4 h)

**Référence RULES** : §§ 1.5.1 (squelette mis à jour v1.3), 1.5.3 (anti-pattern), 1.5.6 (renvois internes contextualisés).

**Méthode.**

1. Identifier tous les modules dont la section finale `id="ressources"` mélange internes et externes. Patterns à grep :

   ```bash
   # Trouver les modules avec sous-rubrique "Modules complémentaires" ou "Préalables associés" en fin
   grep -rn "Modules complémentaires\|Préalables associés" modules/ prealables/
   ```

   Modules connus déviants : **CU-023, CU-024, CU-027** (intégrés en v3.6/v3.6.1).

2. Pour chacun, refondre la section finale en **Schéma A** :
   ```html
   <section class="module-section" id="ressources">
     <div class="module-section-header">…</div>
     <div class="callout callout-info">
       Pour le panorama complet des outils, retrouve les fiches détaillées sur la
       <a href="../ressources.html#bibliographie">page Ressources du Hub</a>.
     </div>
     <div class="resources-cat">
       <h3>📰 Articles de fond</h3>
       <ul><!-- liens externes --></ul>
     </div>
     <div class="resources-cat">
       <h3>🎓 Tutoriels & cas pratiques</h3>
       <ul><!-- liens externes --></ul>
     </div>
     <div class="resources-cat">
       <h3>📚 Documentation officielle & études</h3>
       <ul><!-- liens externes (les sources actuellement présentes) --></ul>
     </div>
     <div class="resources-cat">
       <h3>👥 Communautés & veille</h3>
       <ul><!-- liens externes --></ul>
     </div>
   </section>
   ```

3. **Migrer les renvois internes** (modules complémentaires, préalables associés) **dans le corps du module** :
   - **Vers les modules complémentaires** : si le renvoi a déjà du sens dans le corps (ex : CU-023 mentionne déjà CU-024 dans sa Phase 4 et CU-005 dans son hero), pas besoin de re-mentionner. Sinon, ajouter une phrase contextuelle dans la section pertinente.
   - **Vers les préalables** : ajouter une phrase contextuelle dans le corps quand le module touche à un cadrage transverse (ex : CU-023 mentionne déjà PR-01 en cas de < 4 OUI dans l'auto-diag — OK).

4. **Important** : si certains liens externes manquent dans la section finale après migration, c'est OK de les ajouter — les sources des modules récents (Bpifrance Le Lab, MIT NANDA, Microsoft, etc.) sont à la fois articles de fond ET documentation officielle. Tu peux distribuer dans les sous-rubriques selon nature.

5. **Les sources actuellement présentes en sous-rubrique « Sources et études »** doivent rester en place — déplace-les juste dans la sous-rubrique appropriée du Schéma A (Articles de fond / Documentation officielle).

6. **Tutoriels et Communautés** : si tu n'as pas matière, laisser la sous-rubrique avec une mention type « Tutoriels et démos vidéo : recherche par mot-clé sur la chaîne YouTube de l'éditeur de l'outil » plutôt que de la supprimer. La cohérence visuelle prime.

**Livrable Lot 2.**
- Commit `refactor(v3.6.2): refonte sections "Pour aller plus loin" en Schéma A (externes uniquement)`
- Modules touchés listés dans le commit
- Pas de lien interne perdu (vérification : les renvois internes supprimés de la fin doivent exister ailleurs dans le corps)

### Lot 3 — Refonte des renvois internes vers fiches outils (3-4 h)

**Référence RULES** : § 1.5.6 (NOUVELLE v1.3).

**Méthode.**

1. Construire l'inventaire des ancres `id="..."` des fiches outils dans `ressources.html` :
   ```bash
   grep -n 'class="tool-card"' ressources.html | head -100
   grep -n 'id="' ressources.html | grep -v 'section\|article-fond\|tutoriel'
   ```

2. Pour chaque module, à la **première mention en `<strong>`** d'un outil ayant une fiche dans `ressources.html`, transformer en lien :
   ```html
   <!-- Avant -->
   <strong>Cursor</strong> est un éditeur IDE IA…

   <!-- Après -->
   <a href="../ressources.html#cursor"><strong>Cursor</strong></a> est un éditeur IDE IA…
   ```

3. Les mentions suivantes du même outil dans le même module n'ont pas besoin du lien (1 lien par outil et par module suffit, pour éviter la pollution visuelle).

4. **Modules prioritaires** (forte densité d'outils mentionnés sans lien) :
   - **CU-023** : Pennylane, Sellsy, Axonaut, HubSpot, Salesforce, PandaDoc, Esker, Tacton
   - **CU-024** : Pennylane, Sellsy, Axonaut, Esker, Sidetrade, Aston AI
   - **CU-027** : Cursor, Claude Code, Lovable, Bolt.new, v0, Replit Agent, Windsurf, GitHub Copilot
   - **PR-07** : tous les outils mentionnés ayant une fiche

5. **Modules antérieurs (CU-001 à CU-022)** : audit en passant pour appliquer le standard rétroactivement, mais **ne pas surcharger** — si un module mentionne 15 outils, ne lier que les 5-7 outils centraux à son propos. Le but est l'utilité, pas l'exhaustivité.

**Livrable Lot 3.**
- Commit `feat(v3.6.2): renvois contextualisés vers fiches outils ressources.html`
- Mentionner dans le commit le nombre de renvois ajoutés et les modules concernés

### Lot 4 — Renommage CU-015 / CU-027 + cross-links sensibles (1-2 h)

**Référence** : `audit-redondances-mai2026.md` section 1, § 1.5.6 (cross-links obligatoires).

**Méthode.**

#### 4.1 — CU-015 (Stripe Minions / agents codeurs)

- **Card index `index.html`** : changer le titre `<h3>` de la card CU-015. Proposition : remplacer « 1000+ PRs/semaine produits par agents… » par un titre + phrase d'accroche centrés sur l'**asynchronicité agentique managériale** (transposable au-delà du dev). Exemple : `<h3>Asynchronicité agentique — cas Stripe Minions</h3><p>Comment fonctionne le passage d'une équipe IA assistant à une équipe IA autonome sur cycle court : un cas-école managérial transposable bien au-delà du code.</p>`.
- **Hero du module** : changer le `<h1>` (en gardant l'emoji 🛠️ ouvrant), changer le `module-subtitle` pour effacer toute confusion avec « guide d'achat dev applicatif ».
- **Section 1 ou exec summary** : ajouter cross-link vers CU-027 — « Pour cadrer un projet de dev applicatif concret, voir [Faire développer une appli métier (sans être IT)](cu-027-dev-applicatif-ia.html). »

#### 4.2 — CU-027 (Dev applicatif IA-assisté)

- **Card index `index.html`** : changer le titre `<h3>` de la card CU-027. Proposition : `<h3>Faire développer une appli métier (sans être IT)</h3><p>Cadrage projet pour dirigeant non-IT qui veut faire développer une application métier sur mesure : choix prestataire, sécurité, cadre juridique. Ce qui demandait 3 dev et 6 mois se prototype en 2-3 semaines en 2026.</p>`.
- **Hero du module** : changer le `<h1>` (en gardant l'emoji 🛠️ ouvrant), reformuler le `module-subtitle` pour mettre l'accent sur le pilotage projet, pas le panorama d'outils.
- **Cross-link vers CU-015** : déjà présent ou à ajouter dans le hero ou section 1 — « Pour comprendre le pattern d'asynchronicité agentique sous-jacent, voir [Asynchronicité agentique — cas Stripe Minions](cu-015-stripe-minions.html). »

#### 4.3 — Diversification de la première impression

- Sur **CU-015** : si la section 1 ou 2 met en avant Cursor / Claude Code en gros, **les pousser plus bas** dans le module (vers le panorama outils en fin). Le lecteur de CU-015 doit voir d'abord le pattern managérial, pas un panorama d'outils dev.
- Sur **CU-027** : garder le panorama complet en section 1 (c'est le cœur du module).

#### 4.4 — Cross-links bidirectionnels CU-021 ↔ CU-024

Dans le sous-titre hero de **CU-021** : « Pour le cycle commercial sortant (facturation client, relance, recouvrement, e-facturation 2026), voir [Order-to-cash automation](cu-024-order-to-cash.html). »

Dans le sous-titre hero de **CU-024** : « Pour la fonction comptable fournisseur (extraction factures entrantes, prévision cash, anomalies), voir [Finance & comptabilité augmentées](cu-021-finance-augmentee.html). »

#### 4.5 — Mention de parcours pour le triptyque CU-001 / CU-011 / CU-012

Dans l'exec summary de chacun des 3 modules, ajouter (à la fin du callout `exec-when` ou en takeaway dédié) :

- **CU-001** : « Pour passer du réflexe ponctuel à un système permanent : [Veille concurrentielle](cu-011-veille-concurrentielle.html) (système permanent) ou [Veille AAP & drafting](cu-012-veille-aap-drafting.html) (système agentique sur cas pivot startup). »
- **CU-011** et **CU-012** : « Si tu n'as pas encore acquis le réflexe de recherche IA individuel : [Recherche & veille augmentée](cu-001-recherche-veille.html) en préalable. »

**Livrable Lot 4.**
- Commit `refactor(v3.6.2): renommage CU-015/CU-027 + cross-links sensibles`
- Liste explicite des changements de titres dans le commit

### Lot 5 — Standardisation du format auto-diagnostic (2-3 h)

**Référence RULES** : § 1.5.5 (NOUVELLE v1.3).

**Méthode.**

#### 5.1 — Refonte CU-023 (auto-diag actuellement statique)

CU-023 a une « checklist statique 8 questions à compter manuellement » qui ne respecte aucune des 3 propriétés obligatoires (form interactif + génération plan + export). À refondre.

- **Option simple recommandée** : reprendre le pattern du template `_template-auto-diagnostic.html` (5 questions standardisées : positionnement / cas concret / frein / premier pas / indicateur) en l'adaptant au sujet « activation de l'IA sur la génération de devis ». Le contenu actuel des 8 questions OUI/NON peut être condensé en 1-2 questions du form.
- **Option custom** : garder l'esprit des 8 questions OUI/NON mais les transformer en form interactif (radio Oui/Non par question), avec un bouton « Générer mon plan d'action » qui produit dynamiquement un plan (« Tu as 6 OUI : actives la fonction IA de ton outil actuel ce mois-ci. Donne-toi 60 jours de mesure avant de tirer un bilan… ») + un bouton « Exporter en .txt ».

Recommandation Cowork : **Option custom**, plus fidèle au contenu éditorial actuel et plus pédagogique.

#### 5.2 — Clarification CU-024 et CU-027

CU-024 et CU-027 ont chacun une **checklist 12 points** qui n'est pas un auto-diagnostic au sens de la règle 1.5.5 (pas de form interactif). Deux options :

- **Option A** : transformer en form interactif (12 cases à cocher) + génération d'un récap personnalisé (« Tu as coché 8/12 : avant de signer, exige les 4 points manquants par écrit dans le contrat »). + export.
- **Option B** : renommer la section pour qu'elle ne s'appelle plus « Auto-diagnostic » — choisir « Checklist projet » (CU-024) ou « Checklist sécurité prestataire » (CU-027). Garder le format statique. Mettre à jour la card index correspondante (le label actuel « Étude de cas + checklist » est cohérent avec cette option).

Recommandation Cowork : **Option B** pour CU-024 et CU-027 (les checklists d'éligibilité contractuelles ont leur valeur en format statique imprimable). **Option A** pour CU-023 uniquement.

#### 5.3 — Mise à jour des cards index

Si tu choisis l'Option B pour CU-024/CU-027, vérifier que la card index ne dit pas « Auto-diagnostic » mais bien « Étude de cas + checklist » (ou équivalent). Cohérence card ↔ contenu (RULES § 1.5).

**Livrable Lot 5.**
- Commit `feat(v3.6.2): standardisation format auto-diagnostic (CU-023 interactif + CU-024/027 renommés en checklist)`
- Tests visuels du form (ouvrir la page, remplir, vérifier que le plan se génère et s'exporte)

### Lot 6 — Mise à jour des templates obsolètes (1-2 h)

**Référence RULES** : § 1.5.1, 1.5.4 (Cowork ne produit plus de mockups → templates pour Claude Code).

**Méthode.**

Les 3 templates dans `modules/_template-*.html` sont obsolètes (nav 3 entrées sans Préalables ni Architectures, pas de `module-layout`, ancien pattern). À mettre à jour pour refléter le pattern v1.3.

1. **`_template-auto-diagnostic.html`** : refonte complète selon pattern § 1.5.1 + intégration de la règle § 1.5.5 (form interactif + génération plan + export). Garder le code JS du `generatePlan()` + `exportPlan()` qui est déjà bon.

2. **`_template-etude-de-cas.html`** : refonte selon pattern § 1.5.1, garder l'esprit étude de cas (un cas concret approfondi + leçons à tirer + transposabilité).

3. **`_template-quiz.html`** : refonte selon pattern § 1.5.1, garder l'esprit quiz (questions multi-choix avec correction immédiate). Note : aucun module récent n'utilise ce format — à conserver pour les modules N1-N3 futurs.

4. Pour les 3 templates : nav 5 entrées (Préalables + Architectures + Modules + Ressources + À propos), `module-layout` 2 colonnes, `module-toc` sticky, executive summary obligatoire avec `exec-takeaway-num`, sections numérotées avec `section-number`, dernière section `id="ressources"` selon **Schéma A** (4 sous-rubriques externes + callout bibliographie), h1 avec emoji ouvrant.

**Livrable Lot 6.**
- Commit `chore(v3.6.2): mise à jour templates _template-*.html selon pattern v1.3`

### Lot 7 — Audit final + rapport de mission (1-2 h)

**Méthode.**

1. Exécuter la **checklist § 2** de RULES v1.3 dans son intégralité.
2. Exécuter les **grep des anti-patterns § 1.5.3** :
   ```bash
   # Anti-pattern : <main> direct sans module-layout
   grep -rn "<main>" modules/ prealables/ | grep -v "module-main"

   # Anti-pattern : id="section-7" pour la dernière section
   grep -rn 'id="section-7"' modules/ prealables/

   # Anti-pattern : exec-takeaway-icon
   grep -rn "exec-takeaway-icon" modules/ prealables/

   # Anti-pattern : <style> inline sur composants centralisés
   grep -rn "<style>" modules/ prealables/ | wc -l

   # Anti-pattern : h1 sans emoji ouvrant
   grep -rn "<h1>" modules/ prealables/ | grep -v "<h1>[^a-zA-Z]"

   # Vérifier sections finales : Modules complémentaires / Préalables associés ne doivent plus apparaître
   grep -rn "Modules complémentaires\|Préalables associés" modules/ prealables/
   ```

3. Vérifier la **cohérence numérique** (RULES § 1.2.3) : le glossaire reste « 25 modules / 7 préalables / 83 fiches / 5 entrées de nav / 6 familles métier ». Si un chiffre a bougé suite aux changements, le propager.

4. **Tests croisés** Chrome / Firefox / Safari, mobile + desktop. Sticky TOC + scroll-spy + reading progress fonctionnels sur tous les modules touchés.

5. **Production du rapport** dans `site-web-prep/rapport-mission-v3.6.2.md` :

   ```markdown
   # Rapport de mission Claude Code — v3.6.2 harmonisation

   ## Synthèse exécutive
   [3-5 prises clés, ce qui a été fait, écarts résiduels]

   ## Lot 1 — Migration composants vers module-v3.css
   [composants migrés, nombre de fichiers touchés, écarts résiduels]

   ## Lot 2 — Refonte sections "Pour aller plus loin" Schéma A
   [modules touchés, renvois internes migrés vers le corps]

   ## Lot 3 — Renvois fiches outils
   [nombre de renvois ajoutés, modules concernés]

   ## Lot 4 — Renommage CU-015/CU-027 + cross-links
   [titres avant/après, cross-links ajoutés]

   ## Lot 5 — Standardisation auto-diag
   [option retenue par module, tests visuels]

   ## Lot 6 — Mise à jour templates
   [3 templates mis à jour, conformité v1.3 vérifiée]

   ## Lot 7 — Audit final
   [résultats des grep anti-patterns, cohérence numérique, tests croisés]

   ## Écarts signalés pour validation Blaise
   [s'il y a des cas où tu as hésité — préfère signaler que d'interpréter]

   ## Propositions d'amendement à RULES v1.3
   [si des règles se sont révélées imprécises pendant l'exécution]
   ```

**Livrable Lot 7.**
- Commit `chore(v3.6.2): rapport de mission + checklist audit finale`
- Le rapport est dans la PR

---

## 3. Estimation effort consolidée

| Lot | Sujet | Effort estimé |
|---|---|---|
| Lot 0 | Préalable (lecture RULES + audits) | 30 min |
| Lot 1 | Migration composants vers module-v3.css | 3-4 h |
| Lot 2 | Refonte sections "Pour aller plus loin" Schéma A | 3-4 h |
| Lot 3 | Renvois contextualisés vers fiches outils | 3-4 h |
| Lot 4 | Renommage CU-015/CU-027 + cross-links sensibles | 1-2 h |
| Lot 5 | Standardisation format auto-diag | 2-3 h |
| Lot 6 | Mise à jour templates | 1-2 h |
| Lot 7 | Audit final + rapport mission | 1-2 h |
| **Total** | | **15-22 h** |

C'est plus lourd que l'audit v3.5.1 (6-10 h) car cette itération combine refonte technique + harmonisation éditoriale + mise à jour templates.

---

## 4. Workflow recommandé

1. **Vérifier que la PR v3.6.1 est mergée** sur main avant de commencer.
2. **Créer une branche `chore/v3.6.2-harmonisation`**.
3. **Lire RULES v1.3 + les 2 audits** (Lot 0).
4. **Exécuter les Lots 1 → 7 dans l'ordre indiqué**, un commit par lot.
5. **Tests croisés** à la fin (Lot 7) — Chrome / Firefox / Safari, mobile + desktop, sticky TOC fonctionnel sur tous les modules touchés.
6. **PR avec description structurée** :
   - Lien vers ce brief
   - Lien vers RULES v1.3
   - Lien vers les 2 audits (`audit-editorial-mai2026.md`, `audit-redondances-mai2026.md`)
   - Lien vers ton rapport de mission `rapport-mission-v3.6.2.md`
   - Liste des commits (un par lot)

---

## 5. Règles de prudence pendant l'exécution autonome

Tu travailles seul. Cinq principes pour ne pas créer de régression :

**Règle 1 — Quand tu hésites, tu signales, tu n'interprètes pas.**
Mieux vaut un rapport qui liste 10 points à valider qu'un commit qui en a appliqué 10 dont 3 mal interprétés. Section « Écarts signalés pour validation Blaise » du rapport prévue à cet effet.

**Règle 2 — Tu ne touches pas au design system sans mesure.**
La refonte des composants `.alert-block`/`.checklist-block`/`.stat-block`/`.tool-table` doit utiliser les variables CSS existantes (`--color-primary`, etc.). Si tu introduis une nouvelle variable CSS, signale-le dans le rapport.

**Règle 3 — Tu ne réécris pas le contenu éditorial.**
Si une formulation est maladroite, tu la signales dans le rapport. Tu ne la réécris pas — c'est une compétence Cowork.

**Règle 4 — Tu commits par petits incréments.**
Un commit par lot, message clair et structuré. Pas de commit géant en fin de mission.

**Règle 5 — En cas de blocage, tu t'arrêtes et tu documentes.**
Si tu rencontres un cas qui ne rentre dans aucune règle, écris « ⚠️ À discuter avec Blaise » dans le rapport et passe au lot suivant.

---

## 6. Décisions explicites de NE PAS faire dans cette itération

- **Pas de nouveau module** (CU-025/026/028 toujours réservés v3.7).
- **Pas de nouvelle fiche outil** (l'expansion ressources est gelée v3.6.2).
- **Pas de nouveau préalable**.
- **Pas de refonte du design system** au-delà de la migration des composants vers `module-v3.css`.
- **Pas de modification des chiffres macro** (95 % MIT, +270 % Microsoft, 76 % France Num, etc.) — sauf si une source citée a été dépréciée et qu'il faut la remplacer (le signaler dans le rapport).
- **Pas de modification de la nomenclature des axes / familles métier / niveaux** (échelle ⭐ à ⭐⭐⭐⭐, axes a-e + agentique, 6 familles métier).

---

## 7. Validation finale avant PR

```
☐ RULES v1.3 lu en intégralité avant de commencer.
☐ Les 2 audits lus en intégralité.
☐ Les 7 lots ont été exécutés dans l'ordre.
☐ Chaque lot a fait l'objet d'un commit séparé.
☐ Le rapport rapport-mission-v3.6.2.md est complet et structuré.
☐ Tous les écarts non corrigés sont signalés dans le rapport.
☐ Aucune régression visuelle (vérifiée par tests croisés).
☐ Les anti-patterns § 1.5.3 sont absents (vérifié par grep).
☐ La cohérence numérique cross-site est préservée.
☐ La description de PR pointe vers ce brief + RULES v1.3 + les 2 audits + le rapport mission.
```

---

## 8. Fichiers de référence (dans `site-web-prep/`)

- **Référentiel non négociable** : `RULES-IMPLEMENTATION.md` v1.3 ← À LIRE EN PRÉALABLE
- **Brief de cette itération** : `BRIEF-CLAUDE-CODE-v3.6.2-harmonisation.md` (ce fichier)
- **Audit éditorial complet** : `audit-editorial-mai2026.md`
- **Audit redondances** : `audit-redondances-mai2026.md`
- **Référence canonique** : `modules/cu-008-knowledge-base-rag.html`
- **Briefs précédents** (référence) : `BRIEF-CLAUDE-CODE-v3.6-passation.md`, `BRIEF-CLAUDE-CODE-v3.5.1-audit.md`

---

## 9. Contact

Pour toute question pendant l'exécution : Blaise Cavalli — blaise.cavalli@questforchange.eu

**Tu travailles en autonomie sur cette itération.** Si tu es bloqué, **arrête-toi et documente** plutôt que d'interpréter. Blaise relira le rapport et tranchera les cas signalés.

**Bonne mission, et merci pour le travail !**

---

*Brief produit par Cowork (Claude desktop) le 9 mai 2026. Cette itération v3.6.2 est une harmonisation conjointe fond + forme suite à audit éditorial complet du site (25 modules + 7 préalables + Architectures + Ressources + home). Elle prépare le terrain propre pour v3.7 (nouveau contenu : CU-025/026/028 + page « Par où commencer ? »).*
