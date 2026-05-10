# Audit éditorial complet — Hub IA Learning Center (mai 2026)

> Audit conjoint Cowork + Claude Code visant à harmoniser fond et forme avant la prochaine itération éditoriale (v3.7). Périmètre : 25 modules CU + 7 préalables PR + page Architectures + page Ressources + home.
> Date : 9 mai 2026.
> Auditeur : Cowork (matière éditoriale) + agents général-purpose (lectures ciblées repo cloné).

---

## Synthèse exécutive

L'audit fait apparaître **deux niveaux d'incohérence** à corriger avant v3.7 :

1. **Sur le fond éditorial** — un point chaud confirmé (CU-015 vs CU-027 : 50 % de chevauchement non explicité dans les hero), un chevauchement à clarifier (CU-021 vs CU-024 : compta entrante vs cycle commercial sortant), un triptyque non articulé (CU-001 / CU-011 / CU-012 sur la veille). Aucune fusion ni suppression — uniquement des amendements éditoriaux ciblés.

2. **Sur la forme technique** — quatre formats d'auto-diagnostic coexistent (template normalisé jamais suivi, CU-008 custom à scoring, CU-013 à verdict GO/NO-GO, CU-023 statique non interactif), deux schémas pour la section "Pour aller plus loin" (4 sous-rubriques externes pré-existantes vs 3 sous-rubriques mixtes des modules v3.6), aucun renvoi vers les fiches outils dans le corps des modules v3.6 (alors que les ancres existent), et un anti-pattern persistant de `<style>` inline qui redéfinit des composants non centralisés (`.alert-block`, `.checklist-block`, `.stat-block`, `.tool-table`).

**Décisions Blaise prises pour cadrer la remédiation :**

- **Option A** retenue pour la section "Pour aller plus loin" : 4 sous-rubriques externes uniquement (Articles de fond, Tutoriels, Documentation officielle, Communautés) + callout vers `ressources.html#bibliographie`. Les renvois internes (modules, préalables, fiches outils, architectures) vivent dans le corps du module au fil du texte, contextualisés.
- **Format auto-diagnostic hybride** : custom toléré, mais **3 propriétés non négociables** — form interactif, génération de plan d'action, export téléchargeable.
- **Template `_template-auto-diagnostic.html`** : à mettre à jour dans la même itération corrective.

**Charge de travail estimée pour Claude Code** : 12-18 h sur l'itération corrective v3.6.2.

---

## A. Cohérence éditoriale (fond)

### A.1 — Point chaud : CU-015 vs CU-027

**Diagnostic.** Les deux modules partagent l'axe agentique, le niveau N4, l'emoji 🛠️, et listent en partie les mêmes outils (Cursor, Claude Code). Ils s'adressent au même type de lecteur (dirigeant), mais visent en réalité deux questions distinctes :

- **CU-015 = pattern d'orchestration managérial** illustré par le code Stripe — l'enseignement est l'asynchronicité agentique transposable à toute fonction (support, admin, contenu).
- **CU-027 = guide d'achat / cadrage projet** pour faire développer une appli métier sans être IT.

Le problème : les hero, les cards index, et les outils mis en avant ne disent pas cette différence. Un lecteur ne sait pas pourquoi il y a deux modules.

**Action requise.**
- Renommer CU-015 sur card et hero pour effacer toute ambiguïté « guide d'achat » : passer de « Agents codeurs internes » à **« Asynchronicité agentique — cas Stripe Minions »**. Le mot « codeur » crée la confusion.
- Renommer CU-027 sur card pour effacer l'allusion aux agents : passer de « Développement applicatif métier IA-assisté » à **« Faire développer une appli métier (sans être IT) »**. Reformuler la card index pour mettre l'accent sur le pilotage projet (cadrage, choix prestataire, sécurité) plutôt que sur le panorama d'outils.
- Cross-links mutuels dans les sous-titres hero : « Pour comprendre ce que change le pattern agentique côté pilotage cognitif → CU-015 » et « Pour cadrer un projet de dev concret → CU-027 ».
- Diversifier les outils mis en avant : retirer Cursor / Claude Code de la première impression visuelle de CU-015 (les pousser plus bas dans le module) ; garder le panorama complet sur CU-027.

### A.2 — Chevauchement à clarifier : CU-021 vs CU-024

**Diagnostic.** CU-021 (finance & comptabilité augmentées) couvre la fonction comptable fournisseur entrante (extraction factures fournisseurs, rapprochement bancaire, prévision cash, anomalies). CU-024 (order-to-cash) couvre le cycle commercial sortant (devis, BC, facturation client, relance, encaissement). Pas de redondance — les deux modules sont complémentaires (fournisseurs vs clients sur le cycle financier). Mais aucun cross-link, et CU-021 ne mentionne pas CU-024 alors que l'inverse est vrai. Risque concret : un dirigeant lit CU-021 et croit avoir tout couvert sur la compta — il manquera l'enjeu réglementaire e-facturation 2026.

**Action requise.**
- Cross-link bidirectionnel dans les sous-titres hero des deux modules.
- Optionnel : mini-schéma « cartographie cycle financier » qui place les deux modules côte à côte et matérialise la complémentarité.

### A.3 — Triptyque non articulé : CU-001 / CU-011 / CU-012

**Diagnostic.** Les trois modules forment naturellement un parcours progressif (réflexe individuel ponctuel → système permanent ciblé → système agentique sur cas pivot startup). Aucun chevauchement de périmètre fonctionnel — mais aucun cross-link entre les trois. Le lecteur qui découvre la home avec « Recherche & veille augmentée » (CU-001) ne sait pas qu'il existe deux applications industrialisées plus loin.

**Action requise.**
- Mention de parcours dans chacun des trois exec summary (« Pour passer du réflexe à un système permanent → CU-011 / CU-012 »).
- Optionnel : visualisation « parcours veille » sur la home (3 jalons N1 → N2 → N3).

### A.4 — Paires sans action structurelle

- **CU-005 vs CU-023** — les hero se renvoient explicitement, niveaux distincts (N3 vs N2), périmètres fonctionnels distincts (RAG sur corpus interne vs activation couche IA SaaS). Status quo.
- **CU-013 vs CU-024** — frontière implicite mais nette (workflow agentique entrant générique vs cycle commercial sortant réglementé). Cross-link mineur souhaitable mais pas urgent.

### A.5 — À auditer en v3.7

- **CU-009 vs CU-010** (content repurposing vs pipeline contenu social) — non audité en détail dans cette itération, mérite une lecture rapide.

---

## B. Cohérence technique (forme)

### B.1 — Format auto-diagnostic non uniforme (4 formats coexistent)

| Module | Format | Conformité template |
|---|---|---|
| `_template-auto-diagnostic.html` | Form 5 questions standardisées (positionnement / cas / frein / premier pas / indicateur), génération plan, export .txt, localStorage | ✅ Référence |
| CU-008 Knowledge base RAG | Form 6 questions custom de maturité (volume doc, sensibilité, référent, politique d'accès), scoring → plan priorisé, export Markdown + texte | ⚠️ Custom interactif (acceptable selon décision Blaise : form + plan + export = OK) |
| CU-013 Workflow email-CRM | Form 5 prérequis bloquants + 5 critères qualité (Oui/Partiel/Non, scoring 0-20), verdict GO/NO-GO/À MÛRIR, export | ⚠️ Custom interactif (acceptable) |
| CU-023 Devis simples | **Aucun form, aucun JS** — checklist statique 8 questions à compter manuellement | ❌ Non interactif — non conforme |
| CU-024 Order-to-cash | Pas d'auto-diag à proprement parler (checklist projet) | À clarifier |
| CU-027 Dev applicatif IA | Pas d'auto-diag à proprement parler (checklist sécurité) | À clarifier |

**Décision Blaise** : on accepte les **formats hybrides custom** (CU-008, CU-013) sous réserve qu'ils respectent **3 propriétés non négociables** : form interactif, génération de plan d'action, export téléchargeable.

**Action requise.**
- CU-023 : refonte de la section auto-diag en form interactif (8 questions OUI/NON suffisent en termes de questions, mais doivent être interactives + générer un plan + permettre export).
- CU-024 et CU-027 : clarifier — soit la section devient un vrai auto-diag interactif (avec form + plan + export), soit elle est renommée en « Checklist d'éligibilité » ou « Checklist projet » sans prétendre être un auto-diag.
- Mise à jour du template `_template-auto-diagnostic.html` pour refléter le pattern v1.2 (nav 5 entrées, `module-layout` 2 colonnes, exec-takeaway-num, h1 emoji, etc.) + clarifier que le format peut être custom mais doit respecter les 3 propriétés.

### B.2 — Section "Pour aller plus loin" : refonte uniforme selon Option A

**Constat.** Deux schémas coexistent.

- **Schéma A (CU-008, CU-016, CU-021)** : 4 sous-rubriques **toutes externes** (Articles de fond, Tutoriels, Documentation officielle, Communautés), + un callout `callout-info` qui renvoie vers `ressources.html#bibliographie`. Les renvois internes (modules, préalables, architectures) sont dans le corps du module, contextualisés.
- **Schéma B (CU-023, CU-024, CU-027 v3.6)** : 3 sous-rubriques **mixtes** — Modules complémentaires + Préalables associés + Sources et études. Les renvois internes sont à la fois dans le corps et récapitulés à la fin.

**Décision Blaise : Option A retenue.** Cette option correspond à la règle pré-établie. Plus simple à expliquer, plus respectueuse du principe « les renvois internes vivent dans leur contexte d'usage ». Cela demande de réviser CU-023 / CU-024 / CU-027 + d'amender RULES § 1.5.1 (qui actuellement codifie Schéma B).

**Action requise.**
- Refonte de la section finale `id="ressources"` sur CU-023, CU-024, CU-027 en Schéma A : 4 sous-rubriques externes + callout vers `ressources.html#bibliographie`.
- Migration des renvois internes (modules, préalables) actuellement dans la section finale vers le corps du module aux endroits contextuellement pertinents.
- Audit en passant des 22 autres modules pour vérifier la conformité au Schéma A et corriger les écarts éventuels.

### B.3 — Renvois vers fiches outils absents dans le corps

**Constat.** `ressources.html` expose des ancres exploitables sur chaque fiche outil (`id="cursor"`, `id="claude-code"`, `id="pinecone"`, `id="n8n"`, `id="dify"`, etc.). Pourtant, **aucun module v3.6** ne lie vers ces ancres. Les outils sont systématiquement cités en `<strong>` sans renvoi.

Les modules antérieurs (CU-008, CU-016, CU-021) n'ont pas non plus généralisé les renvois — ils utilisent un callout en haut de section finale qui pointe vers `ressources.html#bibliographie` (pattern A.5 existant).

**Action requise.**
- Mettre en place un standard : à chaque mention en `<strong>` d'un outil ayant une fiche dans `ressources.html`, ajouter un lien `<a href="../ressources.html#XXX">` vers la fiche outil correspondante (à la première occurrence par module suffit).
- Audit de tous les modules pour appliquer ce standard rétroactivement (Cowork prépare la matière, Claude Code applique).

### B.4 — `<style>` inline anti-pattern persistant sur v3.6

**Constat.** Les modules v3.6 (CU-023, CU-024, CU-027) ont conservé un bloc `<style>` inline de 80-100 lignes qui :

- Redéfinit `.pull-quote` (déjà centralisé dans `module-v3.css`) → **doublon**
- Définit `.alert-block`, `.checklist-block`, `.stat-block`, `.tool-table`, `.timeline-block`, `.pa-table`, `.stage-card`, `.arch-callout`, `.incident-card`, `.legal-grid` → **composants utilisés sur 3+ modules mais jamais migrés vers le CSS central**
- Utilise des couleurs hardcodées (`#1e3a8a`, `#dc2626`, `#059669`) qui court-circuitent les variables `--color-primary`, `--color-surface` du design system

CU-008 (référence canonique) n'a aucun `<style>` inline — uniquement les imports `style.css` + `module-v3.css`.

**Action requise.**
- Migration des composants utilisés sur 2+ modules vers `module-v3.css` :
  - `.alert-block` (CU-023, CU-024, CU-027 + PR-06)
  - `.checklist-block` (CU-023, CU-024, CU-027 + PR-02, PR-03, PR-06, PR-07)
  - `.stat-block` (CU-023, PR-04)
  - `.tool-table` (CU-023, CU-027)
  - `.arch-callout` (CU-024, CU-027 + futurs modules sensibles)
  - `.timeline-block`, `.pa-table`, `.stage-card`, `.incident-card`, `.legal-grid` : selon usage, migrer ou laisser inline si single-use.
- Suppression des `<style>` inline correspondants sur CU-023, CU-024, CU-027.
- Refactorisation pour utiliser les variables CSS du design system (`--color-primary`, `--color-surface`, etc.) plutôt que des couleurs hardcodées.
- Vérification croisée : `.pull-quote` doit utiliser uniquement la définition centrale.

### B.5 — Conventions hétérogènes (à harmoniser à la marge)

- **3 conventions d'icônes de section** : `purple/warning` (CU-008) vs `icon-diag` (CU-013) vs `icon-method/context/resources` (CU-023/024/027). Trancher en faveur d'une convention unique (recommandation Cowork : `icon-context/method/warning/resources` car plus sémantique).
- **2 structures de header de section** : avec ou sans `<div class="section-number">` imbriqué. Trancher (recommandation : avec `section-number` car il visualise mieux la progression).
- **Templates obsolètes** : `_template-auto-diagnostic.html`, `_template-etude-de-cas.html`, `_template-quiz.html` ont une nav 3 entrées (sans Préalables ni Architectures), pas de `module-layout`. À mettre à jour pour refléter le pattern v1.2.

---

## C. Punch-list par module (extraits prioritaires)

| Module | Action | Priorité |
|---|---|---|
| CU-015 | Renommer card + hero (« Asynchronicité agentique — cas Stripe Minions »), retirer Cursor/Claude Code de la première impression | 🔴 |
| CU-027 | Renommer card + hero (« Faire développer une appli métier (sans être IT) »), recentrer sur le pilotage projet | 🔴 |
| CU-015 + CU-027 | Cross-links mutuels dans les sous-titres hero | 🔴 |
| CU-021 + CU-024 | Cross-links bidirectionnels dans les sous-titres hero | 🟠 |
| CU-001 + CU-011 + CU-012 | Mention de parcours dans les 3 exec summary | 🟠 |
| CU-023 | Refonte section auto-diag en form interactif + plan + export | 🔴 |
| CU-024 | Renommer la checklist projet (pas de prétention auto-diag) ou la rendre interactive | 🟠 |
| CU-027 | Renommer la checklist sécurité (pas de prétention auto-diag) | 🟠 |
| CU-023, CU-024, CU-027 | Refonte section finale "Pour aller plus loin" en Schéma A | 🔴 |
| CU-023, CU-024, CU-027 | Suppression `<style>` inline + migration composants vers `module-v3.css` | 🔴 |
| Tous modules | Ajout des renvois vers fiches outils (`ressources.html#xxx`) à la 1re mention de chaque outil ayant une fiche | 🟠 |
| Templates | Mise à jour `_template-auto-diagnostic.html` + `_template-etude-de-cas.html` + `_template-quiz.html` (nav 5 entrées, `module-layout`, exec-takeaway-num, etc.) | 🟠 |

---

## D. Recommandations consolidées

1. **Itération corrective v3.6.2** dédiée à l'harmonisation, avant tout nouveau contenu éditorial.
2. **RULES v1.3** amendé pour codifier : Option A pour section ressources finale, format auto-diag hybride avec 3 propriétés obligatoires, anti-pattern composants centralisés renforcé, partage Cowork/Claude Code en MD uniquement.
3. **Brief Claude Code v3.6.2 autonome** : 7 lots, 12-18 h estimés, exécution par Claude Code en autonomie avec rapport de fin de mission.
4. **Pour la suite (v3.7+)** : Cowork ne produit plus de mockup HTML — uniquement de la matière éditoriale en MD structuré (brief par module). Claude Code construit le HTML à partir du gabarit canonique CU-008.

---

*Audit produit par Cowork (Claude desktop) le 9 mai 2026. Sources : audit redondances éditoriales (général-purpose agent #1) + audit conformité technique (général-purpose agent #2) + lecture ciblée Cowork (templates, CU-008, CU-023, ressources.html). Périmètre : repo cloné `repo-current/` à la date du 9 mai 2026.*
