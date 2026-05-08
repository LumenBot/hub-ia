# Brief Claude Code — Hub IA Learning Center (passation v3.5)

**Auteur :** Blaise Cavalli — Startup Manager Quai Alpha (Quest for Change)
**Date :** mai 2026
**Repo :** https://github.com/LumenBot/hub-ia
**Branche cible :** main
**Hébergement :** GitHub Pages
**Itération précédente :** v3.4 (6 préalables PR-01 → PR-06 + section transverse, 2 chiffres macro, mention RetEx CU-008)

---

## 0. Contexte court — itération de consolidation

L'itération **v3.5** est une **itération de consolidation et d'enrichissement éditorial**, pas d'expansion massive. Elle introduit cependant **une nouvelle section structurelle majeure : « Architectures »** (4 patterns canoniques + variante hybride), positionnée entre Préalables et Modules.

**Posture éditoriale v3.5 :**
- Le site a atteint sa **maturité de couverture** : 22 cas d'usage (CU) + 6 préalables (PR) + 76 fiches outils. Il est temps de **consolider** plutôt que d'ajouter.
- Les seules nouveautés acceptées : (i) la section Architectures (choix d'implémentation manquant), (ii) la catégorie « Navigateurs agentiques » sur Ressources (catégorie 100 % nouvelle apparue en mai 2026), (iii) les enrichissements RetEx Bpifrance Le Lab (matière FR de référence).
- Tout le reste est **patch / mise à jour / refactor UX**.

**Architecture éditoriale finale après v3.5 :**

```
Préalables (PR-01 → PR-06)         ← cadrages transverses : « avant de te lancer »
   ↓
Architectures (NOUVEAU)            ← choix d'implémentation : « comment je déploie »
   ↓
Modules (CU-001 → CU-022)          ← cas d'usage opérationnels : « j'ai un problème »
   ↓
Ressources (76 fiches outils)      ← référentiel : « quel outil pour quoi »
```

La logique pédagogique est **séquentielle et explicite** : comprendre → cadrer → faire → outiller.

---

## 1. Fichiers sources de référence (dans `site-web-prep/`)

| Fichier | Rôle | Statut |
|---|---|---|
| `mockup/architectures.html` | Page complète prête à intégrer (4 patterns + hybride + tableau comparatif + méthode décision + ouverture patterns complémentaires) | ✅ Produit |
| `patches-v3.5-mai2026.md` | MD consolidé : tous les patches à appliquer (UX, stats, RetEx, tagging, PR-01, ressources) | ✅ Produit |
| `veille-v3.5-mai2026.md` | Rapport de veille (32 sources scannées) — référence pour comprendre la genèse des patches | Référence |
| `BRIEF-CLAUDE-CODE-v3.5-passation.md` | Ce brief | ✅ Tu lis |

**À lire dans l'ordre :** ce brief → `patches-v3.5-mai2026.md` (la matière) → `architectures.html` (la nouveauté structurelle).

---

## 2. Lot 0 — Corrections UX globales (1-2 h)

Détaillé en **section 0** de `patches-v3.5-mai2026.md`. Cinq points à appliquer :

1. **Harmonisation du head banner** (couleurs / hauteur / sticky) entre toutes les pages — quelques pages PR sont légèrement décalées par rapport aux modules CU.
2. **Padding** : aérer les blocs `executive-summary` et `arch-card` (cf. CSS de `architectures.html`).
3. **Titre section Préalables** : remplacer le libellé actuel par **« Avant de te lancer dans un projet IA »** (validation Blaise) sur la home + page d'index.
4. **Retirer le jargon « PR-XX » de l'UX visible** : conserver les noms de fichiers `pr-01-*.html`, mais supprimer toute occurrence visible « PR-01 », « PR-02 » etc. dans les titres / cards / nav. Ne garder que le titre métier (« Maturité organisationnelle », « Préalables data & SI », etc.).
5. **À propos** : actualiser la mention « 6 préalables » en cohérence avec la nouvelle nav 5 entrées (Préalables + Architectures + Modules + Ressources + À propos = on est passé à **5 entrées**).

---

## 3. Lot 1 — Refresh stats macro (3-4 h)

Détaillé en **section 1** de `patches-v3.5-mai2026.md`.

**Objectif** : réactualiser les 3 chiffres choc avec les sources les plus fraîches mai 2026 :

- **95 % d'échec des projets GenAI** (étude MIT Sloan / NANDA, août 2025) — remplace le 94 % AdvisoryX/DXC en home et PR-01.
- **+270 % ROI moyen IA générative** (Microsoft New Future of Work Report 2025) — à intégrer en accroche home (contrepoids au 95 %).
- **76 % de digitalisation des PME/ETI françaises** (France Num, baromètre 2025) — à intégrer en PR-02 ou home pour cadrer le marché.

Les chiffres précédents (94 %, ×5 productivité, 77 000 offres PwC) restent valables mais sont **complétés / actualisés**, pas remplacés en bloc — voir le détail dans le patch MD.

---

## 4. Lot 2 — Intégration des 5 RetEx Bpifrance Le Lab (4-5 h)

Détaillé en **section 2** de `patches-v3.5-mai2026.md`.

Bpifrance Le Lab a publié en avril-mai 2026 plusieurs études FR documentées sur l'IA en PME/ETI. **5 cas concrets** sont intégrables comme illustrations dans des modules existants (sans nommer les cabinets conseil, posture éditoriale Blaise) :

| Cas Bpifrance | Module cible | Apport |
|---|---|---|
| Alfi (assistant onboarding) | CU-016 | Pattern conversationnel RH |
| Transarc (logistique) | CU-018 | Pattern optimisation tournées |
| Géoloc / asset tracking | CU-006 + CU-013 | Pattern IoT + analytique terrain |
| Time to Fly (formation immersive) | CU-008 | Pattern RAG + simulation |
| Meero (qualité photo) | CU-002 + CU-009 | Pattern computer vision + automation créative |

**Posture éditoriale obligatoire** : présenter comme **patterns illustrés**, ne pas mentionner les noms de cabinets conseils ni systématiquement les noms d'entreprises (cf. règle Blaise validée v3.4 : « pas de pub pour acteurs commerciaux »). Les noms d'entreprises sont OK quand le cas est **publiquement documenté par Bpifrance** (source institutionnelle).

---

## 5. Lot 3 — Catégorie Navigateurs agentiques + 7 fiches outils (2-3 h)

Détaillé en **section 6** de `patches-v3.5-mai2026.md`.

**Nouvelle catégorie d'outils** sur la page Ressources : **« Navigateurs agentiques »** — apparue avec la sortie publique d'Atlas (OpenAI, mai 2026), Comet (Perplexity), Operator, Claude pour Chrome. C'est une catégorie 100 % nouvelle qui n'existait pas il y a 6 mois.

**7 fiches à créer** :

**Navigateurs agentiques (4)** :
- Atlas (OpenAI)
- Comet (Perplexity)
- Operator (OpenAI, complémentaire)
- Claude pour Chrome (Anthropic)

**Agents complémentaires (3)** :
- Lindy (orchestration agents low-code)
- Manus (agent autonome)
- ClickUp Brain (agent intégré PM)

**Format obligatoire** : reprendre le pattern de fiche existant (6 dimensions Type/Catégorie/Maturité/Souveraineté/Coût/Complexité, executive summary, sections numérotées). Le contenu détaillé est dans le patch MD section 6.

**Mise à jour des versions de modèles** : profiter du passage pour actualiser les versions sur les fiches existantes (GPT, Claude, Gemini, Mistral) — détaillé dans le patch.

---

## 6. Lot 4 — Refonte CU-007 RH avec alerte anti-pattern (2 h)

Détaillé en **section 3** de `patches-v3.5-mai2026.md`.

Le module **CU-007 IA générative en RH** mérite une mise à jour : la jurisprudence et les retours d'expérience 2025-2026 montrent un **anti-pattern récurrent** (déploiement sans cadrage RGPD/AI Act, biais systémiques sur le tri CV).

**Action** : ajouter en début de module un **bloc d'alerte rouge** (composant `.alert-block` réutilisé de PR-06) qui liste les 3 erreurs typiques + renvoie vers PR-05 (sécurité/conformité IA) et PR-01 (cadrage organisationnel).

Ne pas refondre tout le module — juste ajouter ce bloc en tête + 1 paragraphe de cadrage en section « Pour aller plus loin ».

---

## 7. Lot 5 — Mise à jour PR-01 avec 12 anti-patterns (2 h)

Détaillé en **section 5** de `patches-v3.5-mai2026.md`.

Plutôt que de créer un module CU-023 « anti-patterns » (qui aurait été un PR déguisé en CU), on **enrichit PR-01** avec une **nouvelle sous-section : « Diagnostic projet en cours — 12 anti-patterns à détecter »**.

**Format** : checklist 12 items, regroupés en 4 catégories (Cadrage / Data / Humain / Pilotage). Chaque anti-pattern : 1 ligne diagnostic + 1 ligne correctif.

**Composant JS** : une fonction simple `evaluateAntiPatterns()` (cf. patch MD section 5.3) qui calcule un score sur 12 et donne un verdict coloré (vert / orange / rouge). Réutilise le pattern d'auto-éval déjà présent dans PR-01 (les 10 questions modèle 5R™).

---

## 8. Lot 6 — Intégration de la nouvelle section Architectures (3-4 h)

**LE plus gros lot de cette itération.** Source : `mockup/architectures.html` (déjà produit, prêt à intégrer).

### 8.1 Action principale

Copier `mockup/architectures.html` → `/architectures.html` (racine du repo).

### 8.2 Mise à jour navigation principale (cross-pages)

Sur **toutes les pages du site** (index, ressources, axes, prealables, tous les modules CU, tous les PR), ajouter le lien **« Architectures »** dans la nav principale, **entre « Préalables » et « Modules »**.

Format actuel (5 entrées v3.4) → nouveau format (6 entrées v3.5) :

```html
<!-- Avant (v3.4) -->
<a href="prealables.html" class="nav-link">Préalables</a>
<a href="index.html#modules" class="nav-link">Modules</a>
<a href="ressources.html" class="nav-link">Ressources</a>
<a href="axes.html" class="nav-link">Axes</a>
<a href="index.html#a-propos" class="nav-link">À propos</a>

<!-- Après (v3.5) -->
<a href="prealables.html" class="nav-link">Préalables</a>
<a href="architectures.html" class="nav-link">Architectures</a>
<a href="index.html#modules" class="nav-link">Modules</a>
<a href="ressources.html" class="nav-link">Ressources</a>
<a href="axes.html" class="nav-link">Axes</a>
<a href="index.html#a-propos" class="nav-link">À propos</a>
```

`architectures.html` utilise `nav-link-active` sur sa propre entrée — cohérent avec les patterns v3.2/v3.3/v3.4.

### 8.3 Composants CSS spécifiques à `architectures.html`

Tous **inline** dans le `<head>` du fichier (pas de pollution `module-v3.css`) :

- `.arch-card` avec variantes `.a1` / `.a2` / `.a3` / `.a4` / `.hybrid` (cartes pattern colorées)
- `.arch-meta` (grille 4 colonnes : coût / souveraineté / complexité / maturité)
- `.arch-pros-cons` (grille 2 colonnes vert/rouge)
- `.arch-decision-card` (carte de décision à 5 critères)

**Recommandation** : laisser inline pour cette itération. Si tu juges utile de mutualiser après inspection, créer `architectures.css` plutôt que polluer `module-v3.css`.

### 8.4 Liens croisés à ajouter

Depuis la home : ajouter un encart d'appel vers Architectures dans le bloc « Avant de te lancer » (idéalement en complément de l'encart Préalables, pas à la place).

Depuis PR-02 (data/SI) : ajouter un lien sortant en fin de page : « Tu as cadré ta data ? Va voir les [4 patterns d'architecture](architectures.html) pour choisir ton mode de déploiement ».

Depuis 5 modules sensibles : voir Lot 7 ci-dessous (tagging architectures).

---

## 9. Lot 7 — Tagging architectures sur 5 modules sensibles (2 h)

Détaillé en **section 4** de `patches-v3.5-mai2026.md`.

**Principe** : 5 modules CU touchent à des données sensibles (RH, juridique, sécurité, finance) où le **choix d'architecture est critique**. Sur ces 5 modules uniquement, ajouter un **encart de recommandation architecture** en début de module qui pointe vers `architectures.html`.

| Module | Architecture recommandée | Pourquoi |
|---|---|---|
| CU-007 IA RH | A3 (open-source cloud souverain) ou A4 (on-premise) | RGPD strict, biais à auditer |
| CU-008 RAG documentaire | A3 ou A4 selon sensibilité doc | Données métier confidentielles |
| CU-013 Data analytique | A2 (propriétaire managé EU) ou A3 | Volume + souveraineté |
| CU-020 Veille concurrentielle | A1 ou A2 acceptables | Données publiques majoritaires |
| CU-021 Automatisation factures | A2 ou A3 | Données financières mais flux standardisés |

**Format de l'encart** (composant à factoriser ou inline) :

```html
<div class="arch-callout">
  <span class="arch-callout-icon">⚙️</span>
  <div>
    <strong>Architecture recommandée :</strong> A3 (open-source cloud souverain) ou A4 (on-premise).
    <br><small>Données sensibles RGPD — voir <a href="../architectures.html#a3">le pattern A3</a> et le <a href="../architectures.html#decision">tableau de décision</a>.</small>
  </div>
</div>
```

---

## 10. Estimation effort consolidée

| Lot | Sujet | Effort estimé |
|---|---|---|
| Lot 0 | Corrections UX globales (5 fixes) | 1-2 h |
| Lot 1 | Refresh stats macro (95 % MIT, +270 %, 76 %) | 3-4 h |
| Lot 2 | Intégration 5 RetEx Bpifrance | 4-5 h |
| Lot 3 | Catégorie Navigateurs agentiques + 7 fiches | 2-3 h |
| Lot 4 | CU-007 RH alerte anti-pattern | 2 h |
| Lot 5 | PR-01 + 12 anti-patterns checklist | 2 h |
| Lot 6 | Intégration `architectures.html` + nav 6 entrées | 3-4 h |
| Lot 7 | Tagging architectures sur 5 modules sensibles | 2 h |
| **Total** | | **19-24 h** |

C'est une itération **plus dense que v3.4** (5-7 h) mais reste consolidatoire. Le gros morceau est Lot 6 (intégration architectures + propagation nav cross-pages).

---

## 11. Workflow recommandé

1. **Vérifier que la PR v3.4 est mergée** sur main avant de commencer.
2. **Créer une branche `feat/v3.5-architectures`**.
3. **Lot 0 d'abord** (UX) : préparer le terrain propre.
4. **Lot 6 ensuite** (architectures) : la grosse pièce structurelle, à valider en preview avant de propager les Lots 7 et autres.
5. **Lots 1, 2, 3** : enrichissement contenu (stats, RetEx, fiches outils).
6. **Lots 4, 5, 7** : touches finales sur modules existants.
7. **Tests croisés** Chrome / Firefox / Safari, mobile + desktop, sticky TOC fonctionnel sur `architectures.html`, scroll-spy OK.
8. **PR avec description structurée** pointant vers ce brief + `patches-v3.5-mai2026.md`.

**Ordre suggéré pour limiter les conflits** : Lot 0 → Lot 6 (nav + page) → Lot 7 (tagging cross-modules) → Lots 1-5 en parallèle.

---

## 12. Décisions explicites de NE PAS faire dans cette itération

- **Pas de nouveau module CU** (les anti-patterns deviennent enrichissement PR-01, pas CU-023).
- **Pas de nouvelles catégories d'outils** au-delà de « Navigateurs agentiques » (cabinet / intégrateurs toujours exclus, cf. v3.4).
- **Pas de fiches sur des cabinets de conseil** (EvoliaStrategie, BusinessDigital, etc.) — règle stable Blaise.
- **Pas de modification du reframing géographique** (validé en v3.1).
- **Pas de refonte du design system** — `module-v3.css` / `module-v3.js` restent stables.
- **Pas de page « Par où commencer ? »** (idée v3.4 reportée — pas de bande passante v3.5).

---

## 13. Notes éditoriales structurantes

### 13.1 Distinction CU / PR / Architectures

Cette distinction est **importante éditorialement** et doit être respectée à la lettre :

- **Modules CU (cas d'usage)** : « j'ai un problème métier, voici la solution IA » — auto-diag ou étude de cas, plan d'action ou checklist.
- **Préalables PR (cadrages)** : « qu'est-ce que je dois maîtriser avant de me lancer ? » — article wiki avec auto-éval ou checklist.
- **Architectures (NOUVEAU)** : « comment je déploie techniquement ? » — page longue unique, 4 patterns canoniques + hybride + méthode de décision.

Les 3 sections sont **complémentaires** et chacune a son public d'entrée différent.

### 13.2 Posture sur les RetEx Bpifrance

Les cas Bpifrance sont **publiquement documentés** (source institutionnelle Le Lab) — pas de problème à les nommer. **Mais** : ne jamais transformer en pub pour le cabinet de conseil intermédiaire qui aurait fait le projet (cas EvoliaStrategie sur AMETRA en v3.4 = présenté comme pattern anonyme). Vérifier au cas par cas.

### 13.3 Architecture page format

`architectures.html` est volontairement **une page longue unique** (pas de sous-pages A1, A2, A3, A4) parce que :
- la lecture séquentielle aide à la décision (on compare en lisant)
- la sticky TOC + scroll-spy gèrent la navigation interne
- chaque pattern fait ~600-800 mots → encore raisonnable en lecture continue

Si après mesure d'usage (analytics) un pattern devait être éclaté en sous-page dédiée, ce serait une décision v3.6+, pas maintenant.

### 13.4 Tagging architectures parcimonieux

**Tagger seulement les 5 modules listés au Lot 7**, pas plus. La majorité des modules CU sont architecture-agnostiques (un agent de génération de mail peut fonctionner sur n'importe quelle architecture). Ne pas saturer le site de callouts.

---

## 14. Fichiers à modifier — récapitulatif rapide

**Création** :
- `/architectures.html` (depuis `mockup/architectures.html`)
- `/ressources/navigateurs-agentiques/atlas.html`
- `/ressources/navigateurs-agentiques/comet.html`
- `/ressources/navigateurs-agentiques/operator.html`
- `/ressources/navigateurs-agentiques/claude-pour-chrome.html`
- `/ressources/agents/lindy.html`
- `/ressources/agents/manus.html`
- `/ressources/agents/clickup-brain.html`

**Modification** (toutes pages, nav 6 entrées) :
- `/index.html`
- `/prealables.html`
- `/ressources.html`
- `/axes.html`
- `/prealables/pr-01-*.html` à `/prealables/pr-06-*.html` (6 fichiers)
- `/modules/cu-001-*.html` à `/modules/cu-022-*.html` (22 fichiers)

**Modification ciblée (contenu)** :
- `/index.html` (Lot 1 stats + Lot 6 encart architectures)
- `/prealables/pr-01-*.html` (Lot 5 anti-patterns + Lot 0 stats refresh)
- `/prealables/pr-02-*.html` (Lot 6 lien sortant architectures)
- `/modules/cu-002-*.html` (Lot 2 RetEx Meero)
- `/modules/cu-006-*.html` (Lot 2 RetEx géoloc)
- `/modules/cu-007-*.html` (Lot 4 alerte RH + Lot 7 tag archi)
- `/modules/cu-008-*.html` (Lot 2 RetEx Time to Fly + Lot 7 tag archi)
- `/modules/cu-009-*.html` (Lot 2 RetEx Meero création)
- `/modules/cu-013-*.html` (Lot 7 tag archi)
- `/modules/cu-016-*.html` (Lot 2 RetEx Alfi)
- `/modules/cu-018-*.html` (Lot 2 RetEx Transarc)
- `/modules/cu-020-*.html` (Lot 7 tag archi)
- `/modules/cu-021-*.html` (Lot 7 tag archi)

**Mise à jour ressources existantes (versions modèles)** :
- Fiches GPT, Claude, Gemini, Mistral (dans `/ressources/`) — versions modèles à actualiser, cf. patch MD section 6.

---

## 15. Contact

Pour toute question pendant l'intégration : Blaise Cavalli — blaise.cavalli@questforchange.eu

**Bonne mission, et merci pour le travail !**

---

*Brief produit par Cowork (Claude desktop) le 8 mai 2026. Cette itération v3.5 fait suite à la v3.4 (intégrée par Claude Code). Source du contenu : `patches-v3.5-mai2026.md` + `mockup/architectures.html`.*
