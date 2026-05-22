# Brief Claude Code — Hub IA Learning Center (passation v3.12)

**Auteur :** Blaise Cavalli — Startup Manager Quai Alpha (Quest for Change)
**Repo :** https://github.com/LumenBot/hub-ia
**Branche cible :** main (via PR `feat/v3.12-trois-nouveaux-prealables`)
**Itération précédente :** v3.11 (catégorie ressources Stack agentique Claude/Anthropic + chiffres Stanford/McKinsey + enrichissement persistent memory, RULES v1.6.2)
**Nature de cette itération :** ITÉRATION ÉDITORIALE STRUCTURANTE — création de **3 nouveaux préalables** (PR-09, PR-10, PR-11) en une PR unique. Pas de patch sur modules existants. Impact cohérence numérique cross-site : 8 → 11 préalables.

---

## 0. Contexte court — pourquoi v3.12

L'itération **v3.12** matérialise la roadmap éditoriale validée en mai 2026 après production de la note de concept « Évolutions du Hub IA Learning Center vers comparateur d'outils et aide à la décision » (`outputs/note-concept-evolution-comparateur-aide-decision.md`).

Le diagnostic de la note de concept § 4 a identifié que **« le contenu Hub est organisé par objet, pas par parcours »**. Les 3 nouveaux préalables comblent ce manque structurel en introduisant une couche de **discipline projet** transverse à tous les cas d'usage.

**3 nouveaux préalables, séquencés logiquement** :

| Préalable | Angle | Position dans le projet IA |
|---|---|---|
| **PR-09** « Cadrer un projet IA avant de choisir un outil » | Discipline managériale **amont** (anti-tech push, 8 questions de cadrage, refuser d'avancer sans clarification) | Étapes 1-3 du cycle de vie |
| **PR-10** « Vérifier et limiter les hallucinations IA » (fusion idées 3+4) | Discipline managériale **pendant/après** (4 niveaux de vérification, typologie hallucinations métier, pattern « pas de claim de complétion sans preuve fraîche ») | Étapes 7-9 du cycle de vie |
| **PR-11** « Cycle de vie d'un projet IA » | Vue d'ensemble **séquentielle** intégrant PR-09 + PR-10 + cross-links denses vers tous les préalables et fiches DEP | Carte d'ensemble |

**Décision validée par Blaise (réponse 20 mai 2026)** :
- Roadmap éditoriale validée
- Production en **une PR unique** (= une seule itération éditoriale, pas v3.12 + v3.13 splittés)
- Renumérotation séquentielle PR-09 / PR-10 / PR-11 (cohérence ordre logique)
- Fusion idées 3 et 4 actée → PR-10 unique au lieu de PR-10 + PR-11 séparés
- Idée 2 « cycle de vie » re-positionnée en préalable (PR-11) plutôt qu'en CU

**3 lots organisés** :

| Lot | Périmètre | Volume | Source MD Cowork |
|---|---|---|---|
| **Lot A** | Création complète PR-09 « Cadrer un projet IA avant de choisir un outil » | 1 nouveau préalable (7 sections + executive summary + ressources) | `v3.12/lot-A-pr-09-cadrer-projet-ia.md` |
| **Lot B** | Création complète PR-10 « Vérifier et limiter les hallucinations IA » | 1 nouveau préalable (7 sections + executive summary + ressources) | `v3.12/lot-B-pr-10-verifier-limiter-hallucinations.md` |
| **Lot C** | Création complète PR-11 « Cycle de vie d'un projet IA » | 1 nouveau préalable (7 sections + executive summary + ressources) + cross-links denses vers tous PR et DEP | `v3.12/lot-C-pr-11-cycle-de-vie-projet-ia.md` |

**Tu travailles en autonomie.** Cowork (côté Blaise) a produit toute la matière éditoriale en MD structuré dans `site-web-prep/v3.12/`. Ton rôle : transformer cette matière en HTML conforme RULES v1.6.2 (rule 14 cross-site outils active) + actualiser le glossaire RULES + maintenir la cohérence numérique cross-site.

**Effort estimé Claude Code** : 12-16 h (3 préalables complets équivaut à v3.10 Lot C × 3, soit ~12-15 h, + impacts cross-site ~1 h).

---

## 1. Préalable obligatoire

**AVANT toute action de code**, tu dois :

1. Lire `site-web-prep/RULES-IMPLEMENTATION.md` v1.6.2 (référentiel actuel, 14 règles + rule 14 cross-site outils).
2. Lire les **3 fichiers de matière éditoriale Lot A, B, C** dans `site-web-prep/v3.12/`.
3. Te référer aux **canoniques HTML** pour structure préalable : `prealables/pr-08-financer-projet-ia.html` (préalable le plus récent créé en v3.10, structure 7 sections H2 + executive summary + ressources). Réutiliser le pattern strictement.
4. Te référer aux modules existants pour les cross-links denses du PR-11 : PR-01 à PR-08, DEP-01 à DEP-08.
5. **Exécuter `python3 site-web-prep/audit-global.py`** pour confirmer l'état de départ (0 hit attendu, 14 règles).
6. Branche `feat/v3.12-trois-nouveaux-prealables` créée depuis `main` à jour.

---

## 2. Méthode — 4 lots dans l'ordre

### Lot 0 — Préalable (30 min)

Lectures + audit-global.py de départ.

### Lot 1 — Lot A — Création PR-09 (3-4 h)

**Source MD** : `site-web-prep/v3.12/lot-A-pr-09-cadrer-projet-ia.md`

Création complète : `prealables/pr-09-cadrer-projet-ia.html`
- 7 sections H2 + executive summary + ressources (cf. structure dans MD source)
- Badge complexité ⭐⭐ Opérationnel, badge angle 🧭 Cadrage stratégique, temps de lecture 15 min
- Tableau « 8 questions de cadrage » (section 2)
- Tableau « 5 anti-patterns courants » (section 4)
- Template document de cadrage 1 page (section 5)
- Cross-links vers PR-01, PR-02, PR-07, PR-08, DEP-01

**Composants HTML** : tableaux existants `.tool-table`, encarts `.callout-info`, `.alert-block` pour les anti-patterns. Aucun nouveau composant.

**Livrable Lot 1** : commit `feat(v3.12): création préalable PR-09 « Cadrer un projet IA avant de choisir un outil »`.

### Lot 2 — Lot B — Création PR-10 (3-4 h)

**Source MD** : `site-web-prep/v3.12/lot-B-pr-10-verifier-limiter-hallucinations.md`

Création complète : `prealables/pr-10-verifier-limiter-hallucinations.html`
- 7 sections H2 + executive summary + ressources
- Badge complexité ⭐⭐ Opérationnel, badge angle 🛡️ Discipline managériale, temps de lecture 18 min
- Section 2 : 4 familles d'hallucinations (chiffres inventés, citations fabriquées, conclusions hors-périmètre, faux positifs de complétion) avec cas d'usage type pour chacune
- Section 4 : tableau « 4 niveaux de vérification proportionnés à l'enjeu »
- Section 5 : 4 dimensions à formaliser pour chaque agent en production
- Cross-links vers PR-04, PR-05, CU-026, DEP-05 §8.5, DEP-07

**Composants HTML** : tableaux `.tool-table`, encarts `.callout-info`, citation McKinsey en `.pull-quote` ou équivalent. Aucun nouveau composant.

**Livrable Lot 2** : commit `feat(v3.12): création préalable PR-10 « Vérifier et limiter les hallucinations IA »`.

### Lot 3 — Lot C — Création PR-11 (4-5 h)

**Source MD** : `site-web-prep/v3.12/lot-C-pr-11-cycle-de-vie-projet-ia.md`

Création complète : `prealables/pr-11-cycle-de-vie-projet-ia.html`
- 7 sections H2 + executive summary + ressources
- Badge complexité ⭐⭐ Opérationnel, badge angle 🔄 Vue d'ensemble séquentielle, temps de lecture 20 min
- Section 2 : tableau **les 9 étapes du projet IA** avec livrable, durée, préalable/DEP de référence (tableau central du module)
- Section 3 : 3 quality gates obligatoires avec critères GO/NO-GO par gate
- Section 4 : tableau **coût des courts-circuits** (économie apparente vs coût réel)
- Section 5 : cas d'usage type order-to-cash développé étape par étape
- Section 6 : tableau **articulation préalables + fiches DEP** par étape du cycle (carte de navigation)
- Cross-links **denses** : PR-01 à PR-10 + DEP-01 à DEP-08 mentionnés explicitement dans le module

**Composants HTML** : tableaux `.tool-table` (4 tableaux structurants), encarts `.callout-info`, gros volume de cross-links. Aucun nouveau composant.

**Particularité Lot 3** : **mise à jour réciproque dans les préalables existants** (cf. section 6 du MD Lot C — « Cross-link réciproque depuis autres préalables ») :
- PR-01, PR-02, PR-04, PR-05, PR-07, PR-08, PR-09, PR-10 : ajouter un encart léger mentionnant PR-11 comme vue d'ensemble séquentielle
- DEP-01 à DEP-08 : même chose
- Effort estimé : ~30 min de patches courts dans 16 fichiers existants

**Livrable Lot 3** : commit `feat(v3.12): création préalable PR-11 « Cycle de vie d'un projet IA » + cross-links réciproques depuis PR-01..PR-10 et DEP-01..DEP-08`.

### Lot 4 — Impacts cross-site cohérence numérique + RULES + audit (2-3 h)

#### 4.1 Cohérence numérique cross-site (rule 1.2.x)

Impact majeur : **8 → 11 préalables**. Mettre à jour partout dans le même commit :

- **`index.html`** : meta description, hero stats, filter count haut + bas, section À propos
- **`prealables.html`** : meta description, accroche, footer-cta, **3 nouvelles cards (PR-09, PR-10, PR-11)** ajoutées à la liste avec icônes 🧭, 🛡️, 🔄
- **`README.md`** : mention « 11 préalables PR »
- **`architectures.html`** : badges éventuels si compte de préalables mentionné
- **`ressources.html`** : badges éventuels
- Méta-descriptions de toutes les pages qui mentionnent le compte de préalables
- **Footers de tous les modules CU (27)** et préalables (PR-01 à PR-08) : mention « 11 préalables »

#### 4.2 Mise à jour RULES v1.6.2 → v1.6.3

- Glossaire § 1.2.3 : **8 → 11 préalables PR**
- Entrée historique à ajouter :

```markdown
- **v1.6.3** — itération v3.12 (3 nouveaux préalables) :
  - Glossaire § 1.2.3 : 8 → 11 préalables PR
  - Création PR-09 « Cadrer un projet IA avant de choisir un outil » (discipline amont)
  - Création PR-10 « Vérifier et limiter les hallucinations IA » (discipline pendant/après)
  - Création PR-11 « Cycle de vie d'un projet IA » (vue d'ensemble séquentielle)
  - Cross-links réciproques denses depuis les préalables existants vers PR-11
  - Aucune nouvelle règle structurelle. RULES reste à 1.6.X.
```

#### 4.3 Audit final + rapport

- Exécuter `python3 site-web-prep/audit-global.py` — confirmer **0 hit** (14 règles)
- Vérifier visuellement :
  - Cohérence numérique 8 → 11 préalables partout (le glossaire RULES + audit-global.py doit passer)
  - Cards PR-09, PR-10, PR-11 visibles et cliquables sur la page Préalables
  - Tous les cross-links créés sont valides (pas de lien mort entre les 3 nouveaux préalables et les modules existants)
  - Cross-links réciproques bien intégrés (PR-01..PR-10 mentionnent PR-11)
  - Badges temps de lecture corrects (15 min PR-09, 18 min PR-10, 20 min PR-11)
- Produire `RAPPORT-v3.12.md` (synthèse, fichiers touchés, métriques avant/après : 25 → 27 modules CU restent inchangés / 8 → 11 préalables / 8 fiches DEP inchangées / 16 catégories ressources inchangées / 104 fiches outils inchangées)

**Livrable Lot 4** : commit `chore(v3.12): cohérence cross-site 8→11 préalables + RULES v1.6.3 + audit final + rapport`.

---

## 3. Règles à respecter (rappel synthétique)

- **RULES v1.6.2** (à bumper v1.6.3 par le Lot 4) : 13 règles essentielles + annexes + rule 14 cross-site outils. Pas de dérive structurelle.
- **Cohérence numérique cross-site** : impact majeur (8 → 11 préalables) → mise à jour systématique partout.
- **Rule 14 (cross-site outils)** : appliquer aux mentions d'outils éventuelles dans les 3 nouveaux préalables (AgentShield, ECC, Claude Code, etc.). Premier link mentionné → hyperlink vers fiche ressources.html.
- **Sources** : tout ajout dans `#ressources` suit le format existant. Citation textuelle des chiffres canoniques (R9 SPEC v1.6.2).
- **Audit-global.py** : doit passer à 0 hit avant ET après l'itération.
- **Cross-links denses PR-11** : c'est ce qui rend PR-11 utile comme carte de navigation. Ne pas couper ces cross-links même s'ils paraissent répétitifs — c'est intentionnel.

---

## 4. Coordination inter-canaux

**Pas d'item descendant nouveau à ouvrir** dans `SYNC-INTER-CANAUX.md` pour v3.12. Les chiffres mobilisés dans les 3 préalables sont déjà canonisés via les items précédents (I-D-003 + I-D-005 + I-D-006 + I-D-007 = 28 chiffres macro cumulés).

**Signal post-merge v3.12 à transmettre à couple 2** :
- 3 nouveaux préalables créés (PR-09, PR-10, PR-11)
- Impact glossaire RULES 8 → 11 préalables
- Pas de nouveau chiffre macro à canoniser
- Modules HTML à anticiper pour vague 5 RAG (si applicable) : `prealables/pr-09.md`, `pr-10.md`, `pr-11.md`
- Application D-026 fortement recommandée sur PR-11 (module dense N3-N4 avec tableaux structurants + cross-links denses + cas d'usage type étendu)

---

## 5. Effort estimé total

| Lot | Effort estimé | Livrable |
|---|---|---|
| Lot 0 (préalable) | 30 min | Audit-global.py |
| Lot 1 (A — PR-09) | 3-4 h | 1 nouveau préalable complet |
| Lot 2 (B — PR-10) | 3-4 h | 1 nouveau préalable complet |
| Lot 3 (C — PR-11 + cross-links réciproques) | 4-5 h | 1 nouveau préalable + ~30 min patches courts dans 16 fichiers existants |
| Lot 4 (cross-site + RULES + audit + rapport) | 2-3 h | Cohérence numérique + RULES v1.6.3 + rapport |
| **Total** | **12-16 h** | 3 nouveaux préalables + impacts cross-site + bump RULES |

---

## 6. Hors périmètre v3.12 — reporté ultérieurement

- **A5 « Pattern hybride 3 acteurs »** (idée 5 du brainstorming) : non pertinent pour cible PME non-IT du Hub. Sujet plus pertinent pour méthodologie projet Initiative IA (cf. brief de passation produit le 20 mai).
- **DEP « Decision log + ticketing »** (idée 6) : trop technique pour cible. Écarté.
- **Comparateur d'outils opérationnel** (Axe 1 note de concept) : reporté post-mise en service Phase 1 RAG (sprint S3 à venir), conformément à la roadmap éditoriale validée.
- **Aide à la décision conversationnelle** (Axe 2 note de concept) : reporté Phase 3 plateforme dynamique, conformément à la hiérarchie de maturité validée.

---

## 7. Hors périmètre — surveillance signaux faibles

Compteur post-v3.11 dans `pistes-cumulatives.md` : 13 pistes en surveillance signaux faibles. Pas de nouveau seuil d'itération à déclencher dans l'immédiat.

Tâche planifiée veille `veille-hub-ia-pistes` continue son rythme quotidien avec le nouveau **Grok screener 6 « Écosystème agentique Claude/Anthropic »** actif depuis le 19 mai.

---

*Brief produit par Cowork Hub IA le 20 mai 2026. Itération v3.12 structurante — 3 nouveaux préalables (PR-09, PR-10, PR-11) en une PR unique. Aucun patch sur modules existants (hors cross-links réciproques courts). Impact cohérence numérique cross-site 8 → 11 préalables. Bump RULES v1.6.2 → v1.6.3. Aucun item descendant nouveau (pas de nouveau chiffre macro). Effort Claude Code estimé : 12-16 h.*
