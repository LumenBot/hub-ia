# Brief Claude Code — Hub IA Learning Center (passation v3.8)

**Auteur :** Blaise Cavalli — Startup Manager Quai Alpha (Quest for Change)
**Repo :** https://github.com/LumenBot/hub-ia
**Branche cible :** main
**Itération précédente :** v3.7.14 (nettoyage technique : template, Schéma A 6 préalables, `.case-deep-actor.warm`, RULES v1.5.13)
**Nature de cette itération :** EXPANSION ÉDITORIALE MAJEURE — patch réglementaire (AI Act Article 50 + Omnibus VII + facturation électronique), enrichissements 4 modules existants, actualisations chiffrées 2 préalables, 4 nouvelles fiches outils, NOUVEAU module CU-026 Gouvernance des agents IA, amendements RULES v1.5.14.

---

## 0. Contexte court — pourquoi v3.8

L'itération **v3.8** consolide les 22 pistes accumulées dans la veille `veille/hub-ia/pistes-cumulatives.md` après le premier run de la tâche planifiée (mai 2026), enrichies par une veille complémentaire ciblée sur la gouvernance des agents IA (`veille-cu-026-gouvernance-agents.md`).

**6 lots organisés** :

| Lot | Périmètre | Volume | Source MD Cowork |
|---|---|---|---|
| **Lot A** | 6 patches réglementaires (CU-020, CU-002, CU-009, CU-010, CU-019, CU-024) | 6 modules patchés | `v3.8/lot-A-patches-reglementaires.md` |
| **Lot B** | 4 enrichissements techniques (CU-008, CU-014, DEP-02, DEP-05) | 4 modules patchés | `v3.8/lot-B-enrichissements-techniques.md` |
| **Lot C** | 2 actualisations chiffrées (PR-01, PR-04) | 2 modules patchés | `v3.8/lot-C-actualisations-chiffrees.md` |
| **Lot D** | 4 nouvelles fiches outils (Hermes Agent, SuperSplat, AAFLOW, Beever Atlas) | 4 fiches créées | `v3.8/lot-D-fiches-outils.md` |
| **Lot E** | 1 nouveau module CU-026 Gouvernance des agents IA | 1 module créé + 1 card index ajoutée | `v3.8/cu-026-gouvernance-agents-ia.md` |
| **Lot F** | Amendements RULES + cohérence numérique cross-site + audit final + rapport | RULES + audit + rapport | (ce brief, section 8) |

**Tu travailles en autonomie**. Cowork (côté Blaise) a produit toute la matière éditoriale en MD structuré dans `site-web-prep/v3.8/`. Ton rôle : transformer cette matière en HTML conforme RULES v1.5.14 (à amender) à partir de la canonique CU-008.

**Effort estimé Claude Code** : 12-18 h.

---

## 1. Préalable obligatoire

**AVANT toute action de code**, tu dois :

1. Lire `site-web-prep/RULES-IMPLEMENTATION.md` v1.5.13 (référentiel actuel post-v3.7.14).
2. Lire `site-web-prep/v3.8/lot-A-patches-reglementaires.md`, `lot-B-enrichissements-techniques.md`, `lot-C-actualisations-chiffrees.md`, `lot-D-fiches-outils.md`, `cu-026-gouvernance-agents-ia.md` (les 5 fichiers de matière éditoriale).
3. Lire `site-web-prep/veille-cu-026-gouvernance-agents.md` (veille sourçée du nouveau module).
4. Te référer à `modules/cu-008-knowledge-base-rag.html` comme référence canonique HTML.
5. Te référer à `modules/cu-023-devis-intelligent.html` comme référence pour le pattern auto-diag interactif (utilisé en CU-026).
6. **Exécuter `python3 site-web-prep/audit-global.py`** pour confirmer l'état de départ (0 hit attendu).

---

## 2. Méthode — 7 lots dans l'ordre

### Lot 0 — Préalable (30 min)

Lectures + audit-global.py de départ.

### Lot 1 — Amendements RULES v1.5.13 → v1.5.14 (15 min)

**Mises à jour à apporter au glossaire § 1.2.3** :
- Modules CU : **26 → 27** (CU-026 ajouté)
- Préalables PR : 7 (inchangé)
- Fiches DEP : 8 (inchangé)
- Fiches outils : **95 → 99** (4 ajoutées en v3.8)
- Patterns architecture : 4 + 1 hybride (inchangé)
- Entrées nav : 5 (inchangé)
- Familles métier : 6 (inchangé)
- Échelle complexité : 4 niveaux (inchangé)

**En-tête à actualiser** : `**Version :** 1.5.14 (mai 2026)`.

**Entrée historique à ajouter** :

```markdown
- **v1.5.14** — itération v3.8 (expansion réglementaire et nouveau module) :
  - Glossaire § 1.2.3 : 26 → 27 modules (CU-026 Gouvernance des agents IA), 95 → 99 fiches outils.
  - Aucune nouvelle règle structurelle. RULES reste à 1.5.X tant que pas d'évolution structurelle (refactor majeur attendu en v1.6).
```

**Livrable Lot 1** : commit `chore(v3.8): amendements RULES v1.5.13 → v1.5.14`.

### Lot 2 — Lot A — 6 patches réglementaires (2-3 h)

**Source MD** : `site-web-prep/v3.8/lot-A-patches-reglementaires.md`

Détail des 6 patches dans le MD source. Synthèse :

- **A.1 CU-020** : nouvelle section « AI Act Article 50 — Transparence et obligations de labellisation » + Omnibus VII + watermarking reporté
- **A.2 CU-002** : encart Article 50 transparence
- **A.3 CU-009** : encart Article 50 transparence
- **A.4 CU-010** : encart Article 50 transparence
- **A.5 CU-019** : encart Article 50 transparence
- **A.6 CU-024** : actualisation calendrier facturation électronique mai 2026

**Composants HTML** : `.alert-block` ou `.callout-info` pour les encarts (centralisés). Aucun nouveau composant.

**Livrable Lot 2** : commit `feat(v3.8): 6 patches réglementaires (AI Act Article 50, Omnibus VII, facturation électronique)`.

### Lot 3 — Lot B — 4 enrichissements techniques (2-3 h)

**Source MD** : `site-web-prep/v3.8/lot-B-enrichissements-techniques.md`

Détail des 4 enrichissements :

- **B.1 CU-008** : pattern LLM Wiki post-Karpathy + forks émergents
- **B.2 CU-014** : principe « agent = employé » + grille de gouvernance + renvoi vers CU-026
- **B.3 DEP-02** : itération continue Stitch → Evaluate → Iterate + RetEx embedding open-source
- **B.4 DEP-05** : bottlenecks data plane vs LLM call + AAFLOW

**Renvois inter-lots** : B.1 et B.4 référencent des fiches outils créées en Lot 5 (Beever Atlas, AAFLOW). B.2 référence le nouveau module CU-026 créé en Lot 6. **À orchestrer après les lots 5 et 6** ou en plusieurs commits pour éviter les liens morts temporaires.

**Livrable Lot 3** : commit `feat(v3.8): 4 enrichissements techniques (CU-008 LLM Wiki forks, CU-014 agent=employé, DEP-02 itération continue, DEP-05 data plane)`.

### Lot 4 — Lot C — 2 actualisations chiffrées (30 min - 1 h)

**Source MD** : `site-web-prep/v3.8/lot-C-actualisations-chiffrees.md`

- **C.1 PR-01** : 80-95 % d'échecs imputables aux causes organisationnelles (en complément du 95 % MIT NANDA)
- **C.2 PR-04** : Baromètre France Num 2025 + étude Bpifrance Le Lab (paradoxe enjeu vs adoption)

**Composants** : `.stat-block`, `.tool-table`, `.callout-info` (centralisés).

**Vigilance** : ne pas effacer les chiffres précédents (95 % MIT NANDA, etc.). Les nouveaux chiffres viennent en complément.

**Livrable Lot 4** : commit `feat(v3.8): actualisations chiffrées PR-01 (95% échec orga) + PR-04 (Baromètre France Num 2025)`.

### Lot 5 — Lot D — 4 nouvelles fiches outils (1-2 h)

**Source MD** : `site-web-prep/v3.8/lot-D-fiches-outils.md`

4 fiches `<article class="tool-card" id="...">` à créer dans `ressources.html` :

- `id="hermes-agent"` — Hermes Agent (NousResearch) — Agents IA / frameworks multi-agents
- `id="supersplat"` — SuperSplat (PlayCanvas) — Knowledge management / 3D no-code
- `id="aaflow"` — AAFLOW — Workflow agentique / runtime distribué
- `id="beever-atlas"` — Beever Atlas — Knowledge management / LLM Wiki

**Avant intégration** : vérifier le format exact des fiches outils existantes dans `ressources.html` pour cohérence visuelle.

**Catégorisation** : à arbitrer selon la classification existante de `ressources.html`. Suggestions dans le MD source.

**Cohérence numérique** : passage 95 → 99 fiches outils (à propager cross-site, cf. Lot 7).

**Vigilance URLs** : pour Hermes Agent et SuperSplat, URLs officielles vérifiables. Pour AAFLOW et Beever Atlas, projets émergents — si une URL est introuvable au moment de la création, **ne pas inventer**, laisser un placeholder « URL officielle à renseigner » et signaler dans le rapport mission.

**Livrable Lot 5** : commit `feat(v3.8): 4 nouvelles fiches outils (Hermes Agent, SuperSplat, AAFLOW, Beever Atlas)`.

### Lot 6 — Lot E — Nouveau module CU-026 Gouvernance des agents IA (3-4 h)

**Source MD** : `site-web-prep/v3.8/cu-026-gouvernance-agents-ia.md`

**Création** : `modules/cu-026-gouvernance-agents-ia.html`

**Pattern HTML obligatoire** : RULES § 1.5.1 (squelette 9 blocs).

**Composants à utiliser (centralisés)** :
- `.exec-summary`, `.exec-takeaway-num`, `.exec-stats`, `.exec-when`
- `.stat-block` (section 1, encart 91 % vs 10 %)
- `.case-deep-actor.warm` (section 2, cas Klarna — variante warm migrée en v3.7.14)
- `.tool-table` (section 3 tableau 7 dimensions, section 4.4 tableau frameworks, section 5.2 zones de confiance)
- `.callout-info` (sections diverses)
- `.timeline-block` (section 7 plan d'action 30 jours)
- `.diagnostic`, `.diag-question`, `.diag-option`, `.diag-result` (section 6 auto-diagnostic interactif)

**Auto-diagnostic interactif** : reprendre le pattern de `modules/cu-023-devis-intelligent.html` section 5. Form `<form id="govDiagForm">` avec 8 questions Oui/Non/Partiel + génération de plan d'action + export `.txt` + persistance `localStorage` (`hubia_cu026_gov`).

**Card index dans `index.html`** : ajouter selon spécifications du MD source :
- Emoji 🪪
- Titre « Gouvernance des agents IA »
- Sous-titre « Manager un agent IA comme un employé débutant. 7 dimensions à formaliser, l'auto-diagnostic, et le cas Klarna comme leçon. »
- Type « Étude de cas + framework + auto-diagnostic »
- Niveau ⭐⭐⭐ Avancé · 25 min
- Axe métier `axe-b` (Décision) avec `axe-secondaire="agentique"`
- `data-agentique="true"`
- `data-filieres="transverse"`

**Renvois internes** : section 1.3, 3, 4, 5.4, 7 — vers CU-014, CU-020, PR-05, fiches outils Lot D, DEP-07, DEP-05.

**Livrable Lot 6** : commit `feat(v3.8): nouveau module CU-026 Gouvernance des agents IA (passage 26→27 modules)`.

### Lot 7 — Cohérence numérique cross-site (1 h)

**Référence RULES** : § 1.2.1, § 1.2.2, § 1.2.3 (mises à jour Lot 1).

Grep et mise à jour cross-site des chiffres :
- « 26 modules » / « 26 cas d'usage » → « 27 modules » / « 27 cas d'usage »
- « 95 fiches outils » → « 99 fiches outils »
- Synthèse `ressources.html` : badge « 95 fiches » → « 99 fiches »

**Lieux à vérifier** (cf. RULES § 1.2.2) :
- `index.html` (meta, hero stats, filter count, section À propos)
- `prealables.html`, `architectures.html`, `deploiement.html`, `ressources.html`
- `README.md`
- Méta-descriptions de toutes les pages

**Livrable Lot 7** : commit `chore(v3.8): cohérence numérique cross-site (27 modules, 99 fiches)`.

### Lot 8 — Audit final + rapport mission (1 h)

**Méthode** :

1. Exécuter **`python3 site-web-prep/audit-global.py`** (0 hit attendu sur les 13 règles automatisées).
2. Exécuter les **grep des anti-patterns § 1.5.3 non automatisés** (couleurs hardcodées, renvois internes section finale, etc.).
3. Vérifier la **cohérence numérique** (RULES § 1.2.3) : 27 modules / 7 préalables / 8 DEP / 99 fiches / 5 entrées nav / 6 familles / 4 niveaux étoiles.
4. Vérifier la **cohérence intra-page** (§ 1.2.5) : pas de stat contradictoire.
5. Vérifier la **cohérence card index ↔ contenu réel** sur la nouvelle card CU-026.
6. Tests croisés Chrome / Firefox / Safari, mobile + desktop sur les nouveaux contenus.
7. Production du rapport `site-web-prep/rapport-mission-v3.8.md` (même structure que rapports précédents).

**Livrable Lot 8** : commit `chore(v3.8): rapport mission + audit final v3.8`.

---

## 3. Estimation effort consolidée

| Lot | Sujet | Effort estimé |
|---|---|---|
| Lot 0 | Préalable (lecture RULES + 5 MD source) | 30 min |
| Lot 1 | Amendements RULES v1.5.13 → v1.5.14 | 15 min |
| Lot 2 | Lot A — 6 patches réglementaires | 2-3 h |
| Lot 3 | Lot B — 4 enrichissements techniques | 2-3 h |
| Lot 4 | Lot C — 2 actualisations chiffrées | 30 min - 1 h |
| Lot 5 | Lot D — 4 nouvelles fiches outils | 1-2 h |
| Lot 6 | Lot E — Nouveau module CU-026 | 3-4 h |
| Lot 7 | Cohérence numérique cross-site | 1 h |
| Lot 8 | Audit final + rapport mission | 1 h |
| **Total** | | **12-18 h** |

---

## 4. Workflow recommandé

1. **Vérifier que la branche est à jour** avec `origin/main` (post-v3.7.14 mergée).
2. **Créer une branche `feat/v3.8-expansion-reglementaire`**.
3. **Lire RULES v1.5.13 + 5 MD source** (Lot 0).
4. **Exécuter les Lots 1 → 8 dans l'ordre indiqué**, un commit par lot.
5. **Ordre recommandé pour gérer les renvois inter-lots** :
   - Lot 1 d'abord (RULES amendée)
   - Lots 5 et 6 ensuite (fiches outils + nouveau module CU-026 — les références cibles)
   - Lots 2, 3, 4 ensuite (qui peuvent renvoyer aux lots 5 et 6 sans liens morts)
   - Lots 7 et 8 en clôture
6. **Tests croisés** à la fin (Lot 8) sur tous les navigateurs et tailles d'écran.
7. **PR avec description structurée** :
   - Lien vers ce brief
   - Lien vers RULES v1.5.14 (post-amendement Lot 1)
   - Lien vers les 5 MD source de matière éditoriale
   - Lien vers la veille CU-026
   - Liste des commits (un par lot)
   - Lien vers le rapport mission `rapport-mission-v3.8.md`

---

## 5. Règles de prudence pendant l'exécution autonome

Identiques aux briefs précédents.

**Spécifique v3.8** :
- **Sur Lot 5 (fiches outils)** : si une URL officielle est introuvable pour AAFLOW ou Beever Atlas, ne pas inventer. Laisser placeholder + signaler dans le rapport.
- **Sur Lot 6 (CU-026)** : reprendre fidèlement la matière du MD source (notamment le cas Klarna en section 2 et l'auto-diagnostic en section 6). Ne pas réécrire le contenu éditorial.
- **Sur Lots 2-3-4 (patches modules existants)** : intégrer en respectant la structure éditoriale existante. Ne pas refondre les modules, juste ajouter les patches indiqués.

---

## 6. Décisions explicites de NE PAS faire dans cette itération

- **Pas de refonte structurelle des modules existants** au-delà des patches indiqués.
- **Pas de nouvelle catégorie** d'outils dans `ressources.html` sauf si nécessaire pour caser une des 4 nouvelles fiches (à arbitrer).
- **Pas de modification du design system** (CSS centralisé inchangé).
- **Pas de modification des chiffres macro** (95 % MIT NANDA, +270 % Microsoft, etc.) — sauf actualisations explicitement demandées dans Lot C.
- **Pas de création d'autres modules CU** au-delà de CU-026 (CU-028 et au-delà réservés à v3.9+).

---

## 7. Validation finale avant PR

```
☐ RULES v1.5.13 lu en intégralité avant de commencer.
☐ 5 fichiers MD source du dossier v3.8/ lus en intégralité.
☐ Veille CU-026 lue en intégralité.
☐ audit-global.py de départ exécuté (0 hit confirmé).
☐ RULES v1.5.14 amendée et committée (Lot 1).
☐ Les 8 lots ont été exécutés.
☐ Chaque lot a fait l'objet d'un commit séparé.
☐ Le rapport rapport-mission-v3.8.md est complet.
☐ audit-global.py de fin exécuté (0 hit confirmé).
☐ Anti-patterns non automatisés vérifiés manuellement.
☐ Tests croisés Chrome / Firefox / Safari, mobile + desktop OK.
☐ Cohérence numérique cross-site vérifiée (27 / 7 / 8 / 99 / 5 / 6 / 4).
☐ Cohérence card index ↔ contenu sur CU-026.
☐ Auto-diagnostic CU-026 fonctionnel (form + plan + export).
☐ Description de PR pointe vers ce brief + RULES v1.5.14 + 5 MD source + veille + rapport mission.
```

---

## 8. Fichiers de référence

- **Référentiel actuel** : `RULES-IMPLEMENTATION.md` v1.5.13 → à amender en v1.5.14 (Lot 1)
- **Brief de cette itération** : `BRIEF-CLAUDE-CODE-v3.8-expansion-reglementaire.md` (ce fichier)
- **Matière éditoriale Cowork** :
  - `v3.8/lot-A-patches-reglementaires.md`
  - `v3.8/lot-B-enrichissements-techniques.md`
  - `v3.8/lot-C-actualisations-chiffrees.md`
  - `v3.8/lot-D-fiches-outils.md`
  - `v3.8/cu-026-gouvernance-agents-ia.md`
- **Veille sourcée** : `veille-cu-026-gouvernance-agents.md`
- **Référence canonique HTML** : `modules/cu-008-knowledge-base-rag.html`
- **Référence pattern auto-diag interactif** : `modules/cu-023-devis-intelligent.html`
- **Garde-fou automatisé** : `site-web-prep/audit-global.py`

---

## 9. Contact

Pour toute question pendant l'exécution : Blaise Cavalli — blaise.cavalli@questforchange.eu

**Tu travailles en autonomie sur cette itération.** Si tu es bloqué, **arrête-toi et documente** plutôt que d'interpréter.

**Bonne mission, et merci pour le travail !**

---

*Brief produit par Cowork. Itération v3.8 = expansion réglementaire et nouveau module Gouvernance des agents IA. Issue de la veille pistes-cumulatives mai 2026 et de la veille complémentaire CU-026.*
