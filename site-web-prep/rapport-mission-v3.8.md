# Rapport de mission v3.8 — Expansion réglementaire et nouveau module

**Itération** : v3.8
**Nature** : Expansion éditoriale majeure (patches réglementaires + 4 enrichissements techniques + 2 actualisations chiffrées + 4 fiches outils + nouveau module CU-026)
**Branche** : `feat/v3.8-expansion-reglementaire`
**Date** : mai 2026
**Effort réel** : ~7 h (estimation brief : 12-18 h)

---

## 1. Synthèse exécutive

Itération éditoriale majeure consolidant la veille v3.7.13 + veille complémentaire CU-026. **8 lots livrés** dans l'ordre recommandé par le brief (Lot 0 → 1 → 5 → 6 → 2 → 3 → 4 → 7 → 8) pour gérer correctement les renvois inter-lots.

| Lot | Sujet | Statut | Volume |
|---|---|---|---|
| 0 | Lectures RULES + 5 MD source + veille CU-026 + audit baseline | ✅ | 0 hit baseline |
| 1 | RULES v1.5.13 → v1.5.14 (26→27 modules, 95→99 fiches) | ✅ | 1 commit |
| 5 | 4 fiches outils (Hermes Agent, SuperSplat, AAFLOW, Beever Atlas) | ✅ | 95 → 99 fiches |
| 6 | Nouveau module CU-026 Gouvernance des agents IA (968 lignes) + card home | ✅ | 26 → 27 modules |
| 2 | 6 patches réglementaires (CU-020 + CU-002/009/010/019 + CU-024) | ✅ | 6 modules patchés |
| 3 | 4 enrichissements techniques (CU-008, CU-014, DEP-02, DEP-05) | ✅ | 4 modules patchés |
| 4 | 2 actualisations chiffrées (PR-01 + PR-04) | ✅ | 2 modules patchés |
| 7 | Cohérence numérique cross-site (index + prealables + ressources + README) | ✅ | 5 fichiers alignés |
| 8 | Audit final + ce rapport | ✅ | 0 hit final |

**audit-global.py final** : `Total hits : 0` sur les 13 règles automatisées.

---

## 2. Détail par lot

### Lot 0 — Préalable (audit baseline)

**Audit-global.py de départ** : 0 hit. La base post-v3.7.14 est propre — confirmation que le terrain est prêt pour l'expansion v3.8.

Lectures effectuées :
- `RULES-IMPLEMENTATION.md` v1.5.13 (référentiel actif)
- `v3.8/lot-A-patches-reglementaires.md` (179 lignes)
- `v3.8/lot-B-enrichissements-techniques.md` (231 lignes)
- `v3.8/lot-C-actualisations-chiffrees.md` (142 lignes)
- `v3.8/lot-D-fiches-outils.md` (221 lignes)
- `v3.8/cu-026-gouvernance-agents-ia.md` (378 lignes)
- `veille-cu-026-gouvernance-agents.md` (283 lignes)
- Référence canonique HTML : `modules/cu-008-knowledge-base-rag.html`
- Référence auto-diag interactif : `modules/cu-023-devis-intelligent.html`

### Lot 1 — RULES v1.5.13 → v1.5.14

**Commit** : `5c401f0`

- En-tête `Version : 1.5.13` → `Version : 1.5.14 (mai 2026)`
- Glossaire § 1.2.3 : `26 → 27 modules CU` (CU-026 ajouté), `95 → 99 fiches outils` (4 nouvelles)
- Entrée historique v1.5.14 ajoutée avec récap des 6 patches A, 4 enrichissements B, 2 actualisations C

Aucune nouvelle règle structurelle introduite — l'itération v3.8 n'a pas révélé de nouveau pattern à codifier.

### Lot 5 — 4 nouvelles fiches outils

**Commit** : `7f86e4a`

Fiches `<article class="tool-card" id="...">` créées dans `ressources.html` :

| Fiche | Catégorie cible | URL officielle |
|---|---|---|
| Hermes Agent (NousResearch) | `cat-multi-agents` (9 → 11 fiches) | hermes-agent.nousresearch.com ✓ |
| AAFLOW | `cat-multi-agents` | ⚠️ placeholder « URL officielle à renseigner » |
| Beever Atlas | `cat-orchestration` (5 → 6 fiches) | ⚠️ placeholder « URL officielle à renseigner » |
| SuperSplat (PlayCanvas) | `cat-productivite` (7 → 8 fiches) | superspl.at ✓ |

Compteurs de catégories mis à jour en parallèle (3 modifications). Comptage total cross-vérifié : `grep -c 'tool-card" id='` retourne **99** ✅.

**Signalement (brief § 5)** : URLs officielles d'AAFLOW et Beever Atlas non vérifiables au moment de la création (projets émergents 2026 sans repo GitHub canonique stable). Placeholder en attente de validation Cowork.

### Lot 6 — Nouveau module CU-026 Gouvernance des agents IA

**Commit** : `36f9e50`

Génération via agent général-purpose dédié. Fichier `modules/cu-026-gouvernance-agents-ia.html` produit (**968 lignes**, HTML validé).

Sections livrées (sommaire emoji-style canonique, 9 entrées) :
- ⚡ Synthèse rapide (4 takeaways + 4 stats 91/10 / >40 % / 23 % / 40 %)
- 🧭 Section 1 Shift de framing (agent = employé) + `.stat-block` 91/10
- 📍 Section 2 Cas Klarna fondateur (`.case-deep-actor warm` + 4 leçons + pull-quote)
- 🛠️ Section 3 Framework 7 dimensions (`.tool-table` + détail dimension par dimension)
- ⚖️ Section 4 Cadre réglementaire (Article 14 AI Act, Article 22 RGPD, Moffatt v. Air Canada, NIST AI RMF, ISO 42001)
- 🚦 Section 5 Pattern d'escalade *confidence-based routing* (grille 3 zones vert/jaune/rouge)
- 🔎 Section 6 Auto-diagnostic interactif (8 questions Oui/Partiel/Non + 3 verdicts + plan généré + export `.txt` + persistance `hubia_cu026_gov`)
- 🚀 Section 7 Plan d'action 30 jours (`.timeline-block` scopée, 4 jalons)
- 📚 Section finale Pour aller plus loin (Schéma A strict)

**Card index** ajoutée dans `index.html` section « Décision & gouvernance » avec double badge `axe-b` + `axe-agentique` (data-agentique=true).

Composants utilisés : tous centralisés (`.exec-summary`, `.case-deep-actor.warm`, `.tool-table`, etc.) sauf `.timeline-block` et `.conf-grid`/`.conf-card` (single-use scopés en `<style>` inline, autorisé § 1.4.4).

### Lot 2 — 6 patches réglementaires

**Commit** : `93e8bfd`

**A.1 CU-020** : nouvelle section `section-art50` « AI Act Article 50 — Transparence et obligations de labellisation » insérée après section-2. Contenu complet : principe Article 50, draft guidelines Commission EU 8 mai 2026, paquet Omnibus VII adopté 7 mai 2026, watermarking reporté au 2 décembre 2026, 3 actions concrètes PME. 2 nouvelles sources Schéma A (digital-strategy.ec.europa.eu + consilium.europa.eu). Entrée TOC ajoutée avec emoji 📣.

**A.2 CU-002 / A.3 CU-009 / A.4 CU-010 / A.5 CU-019** : encarts `.callout-info` « ⚖️ AI Act Article 50 — applicable au 2 août 2026 » insérés juste avant la section finale `id="ressources"` de chaque module. Variantes textuelles selon le contexte (CU-010 mentionne plateformes LinkedIn/Meta/TikTok ; CU-019 propose la mention canonique pour newsletter). Renvoi vers CU-020 dans chaque.

**A.6 CU-024** : enrichissement de la section 2 « Calendrier réglementaire 2026-2027 » avec actualisation mai 2026 : qualification ChorusPro pour la sphère publique + précisions 1er sept. 2026/2027 + implications concrètes séquence 18 mois (4 étapes + audit connecteurs + vigilance ChorusPro vs PA privée). 2 nouvelles sources (economie.gouv.fr + service-public.fr).

### Lot 3 — 4 enrichissements techniques

**Commit** : `f1e1879`

**B.1 CU-008** : nouvelle sous-section dans la section LLM Wiki existante :
- Le pattern LLM Wiki post-Karpathy + 8 forks émergents (persistent memory, self-maintaining KB, contradiction detection, multi-agent vaults, sleep consolidation, graph-based layers, MCP local-first, self-healing graphs)
- Renvoi vers la fiche outil Beever Atlas
- 3 questions à se poser (volume / évolutivité / qualité des inputs)
- Heuristique « itérer cheapest-first » avec RetEx embedding #130 MTEB

**B.2 CU-014** : nouvelle section 6bis « Principe émergent 2026 — l'agent comme employé » entre Troubleshooting et Étude de cas :
- 6 dimensions du framing
- 3 raisons documentées
- Grille 8 dimensions (tâche, droits, escalade, KPI, audit, versions, onboarding, offboarding)
- Renvoi explicite vers CU-026 + PR-05 + CU-020. Entrée TOC ajoutée (🪪).

**B.3 DEP-02** : nouvelle section 6bis « Le cycle d'itération continue — Stitch, Evaluate, Iterate » :
- Constat 2026 (leaderboards ≠ performance réelle)
- Cycle Stitch → Evaluate → Iterate documenté
- RetEx embedding #130 MTEB bat OpenAI (+11 % qualité, 240× plus rapide, gratuit)
- 3 implications PME (eval set, itérer cheapest-first, LLM Judge calibré)
- Renvois vers DEP-07 et CU-008 LLM Wiki

**B.4 DEP-05** : nouvelle section 6bis « Le nouveau bottleneck — data plane vs LLM call » :
- Shift d'attention 2026 (LLM call → data plane)
- Pattern AAFLOW (zero-copy Arrow/Cylon, scheduling déterministe, speedup 4,64×)
- Appel au *system engineering*
- 4 questions PME pour auditer le data plane
- Outils 2026 (AAFLOW, LangGraph, Ray)
- Renvoi vers DEP-06

### Lot 4 — 2 actualisations chiffrées

**Commit** : `b5a7ab2`

**C.1 PR-01** : encart `.stat-block` (80-95 % causes organisationnelles) + `.callout-info` (articulation avec 95 % MIT NANDA) inséré en début de section 2 « 4 causes structurelles ». Le 95 % MIT NANDA dit COMBIEN échouent, le 80-95 % dit POURQUOI. 3 implications pratiques pour le dirigeant.

**C.2 PR-04** : enrichissement de la section 2bis « Tendances macro 2026 » avec :
- Baromètre France Num 2025 (26 % TPE-PME FR, ×2 vs 2024, 41 % ICT, 9 % agriculture)
- Étude Bpifrance Le Lab — paradoxe enjeu (58 %) vs adoption quotidienne (33 %)
- Tableau comparatif 4 indicateurs PME/ETI FR 2025 (en complément, pas en remplacement)

**Vigilance § 5 brief respectée** : les chiffres macro précédents (95 % MIT NANDA, +270 % Microsoft, 55 % Bpifrance Le Lab Osez l'IA, etc.) sont tous préservés. Les nouveaux chiffres viennent en complément (RULES § 1.2.4).

### Lot 7 — Cohérence numérique cross-site

**Commit** : `2f3fdd1`

Propagation des nouveaux comptages (26→27 modules, 95→99 fiches) sur 5 fichiers :

| Fichier | Mises à jour |
|---|---|
| `index.html` | meta description + hero stats (27 + 99) + filtres modules `26→27 sur 26→27` (top + bottom) + section À propos |
| `prealables.html` | « 27 cas d'usage IA opérationnels » (×2 occurrences) + « 99 fiches outils » |
| `ressources.html` | meta + badge hero + h2 catalogue + exec-stat + prose intro + alerte État courant |
| `README.md` | bullets niveaux + structure + suppression mention « cu-026 réservé » |

**Correctif collatéral** : 1 jargon résiduel `CU-026` détecté par `audit-global.py` sur cu-014 ligne 622 (« Le présent module CU-014 reste centré... ; CU-026 traite... ») — reformulé en « le présent module reste centré... ; le module dédié à la gouvernance traite... » (RULES § 1.5.6.1).

### Lot 8 — Audit final

**Comptages structurels finaux** :
- Modules CU : **27** ✅
- Préalables PR : **7** ✅
- Fiches DEP : **8** ✅
- Fiches outils : **99** ✅
- Catégories outils : **15** ✅

**audit-global.py** : `Total hits : 0` sur les 13 règles automatisées (cohérence numérique cross-site, intra-page, versioning, biais sectoriel, structure header, callout margin, jargon codes, card↔contenu, sommaire canonique, contraste dark, STASH, NUL).

**Anti-patterns § 1.5.3 non automatisés** vérifiés manuellement : tous inchangés à 0 hit (couleurs hardcodées migrées en v3.7.14, renvois internes section finale nettoyés en v3.7.14, etc.).

---

## 3. Écarts assumés / signalements

### 3.1 URLs manquantes pour 2 fiches outils

Le brief § 5 prévoyait explicitement le cas : URLs officielles d'**AAFLOW** et **Beever Atlas** non vérifiables au moment de la création (projets émergents 2026 sans repo GitHub canonique stable). Conformément à l'instruction « ne pas inventer », **placeholder « URL officielle à renseigner depuis le repo GitHub de référence du projet (projet émergent 2026) »** intégré dans les 2 fiches. Cowork pourra renseigner les URLs définitives lors d'une itération corrective dès qu'elles seront identifiées.

### 3.2 Effort réel vs estimation brief

- Estimation brief : 12-18 h
- Effort réel : ~7 h

Gain principal : usage de l'agent général-purpose pour générer CU-026 en parallèle des autres lots, économisant 3-4 h. Les patches Lot 2 / Lot 3 / Lot 4 ont été plus rapides que prévu car les MD source étaient très précis et structurés (insertion ciblée + reformulation minimale).

### 3.3 Pas d'écart bloquant

Aucune divergence éditoriale avec les MD source de Cowork. Toute la matière a été intégrée fidèlement. Renvois inter-lots gérés correctement (ordre 1 → 5 → 6 → 2/3/4 → 7 → 8 du brief).

---

## 4. Recommandations pour v3.9

### 4.1 Base de départ propre

- 0 hit `audit-global.py`
- 0 hit anti-patterns § 1.5.3
- RULES v1.5.14 aligné avec l'état réel du repo
- Toutes les nouveautés v3.8 (CU-026, 4 fiches outils, patches réglementaires) sont en place et liées entre elles

### 4.2 Vigilance pour la prochaine itération

1. **URLs officielles AAFLOW et Beever Atlas** : à valider et compléter dès disponibilité (mini-PR de quelques lignes suffit).
2. **Calendrier facturation électronique** : si la séquence officielle évolue d'ici fin 2026, CU-024 § 2 sera à actualiser à nouveau.
3. **Consultation publique Article 50** : la date de fin de la consultation Commission EU n'est pas explicite dans le MD source ; à surveiller dans la veille future si l'Article 50 évolue.
4. **CU-026 auto-diagnostic** : test utilisateur recommandé pour valider que les 8 questions Oui/Partiel/Non + les 3 verdicts couvrent les cas de figure réels rencontrés par les dirigeants PME.

### 4.3 Si v3.9 introduit de nouveaux modules

Penser à appliquer immédiatement la chaîne :
1. Mise à jour RULES § 1.2.3 dans le même commit
2. Card index `index.html` ajoutée
3. Cohérence numérique propagée cross-site (`audit-global.py` règles 1 et 2)

C'est le pattern qui a permis à v3.8 de retourner 0 hit final.

---

## 5. Annexes

### 5.1 Commits de l'itération v3.8

```
5c401f0 chore(v3.8): amendements RULES v1.5.13 → v1.5.14
7f86e4a feat(v3.8): 4 nouvelles fiches outils (Hermes Agent, SuperSplat, AAFLOW, Beever Atlas)
36f9e50 feat(v3.8): nouveau module CU-026 Gouvernance des agents IA (passage 26→27 modules)
93e8bfd feat(v3.8): 6 patches réglementaires (AI Act Article 50, Omnibus VII, facturation électronique)
f1e1879 feat(v3.8): 4 enrichissements techniques (CU-008 LLM Wiki forks, CU-014 agent=employé, DEP-02 itération continue, DEP-05 data plane)
b5a7ab2 feat(v3.8): actualisations chiffrées PR-01 (95% échec orga) + PR-04 (Baromètre France Num 2025)
2f3fdd1 chore(v3.8): cohérence numérique cross-site (27 modules, 99 fiches)
[à venir] chore(v3.8): rapport mission + audit final v3.8
```

### 5.2 Fichiers créés / modifiés

**Créés** (2) :
- `modules/cu-026-gouvernance-agents-ia.html` (968 lignes)
- `site-web-prep/rapport-mission-v3.8.md` (ce fichier)

**Modifiés** (16) :
- `index.html` (card CU-026 + cohérence numérique)
- `prealables.html` (cohérence numérique)
- `ressources.html` (4 nouvelles fiches outils + cohérence)
- `README.md` (cohérence numérique)
- `modules/cu-002-assistant-redactionnel.html` (encart Article 50)
- `modules/cu-008-knowledge-base-rag.html` (LLM Wiki forks)
- `modules/cu-009-content-repurposing.html` (encart Article 50)
- `modules/cu-010-pipeline-contenu-social.html` (encart Article 50)
- `modules/cu-014-multi-agents.html` (section 6bis agent=employé + 1 jargon résiduel)
- `modules/cu-019-newsletter-locale.html` (encart Article 50)
- `modules/cu-020-conformite-rgpd-ai-act.html` (nouvelle section art50)
- `modules/cu-024-order-to-cash.html` (actualisation calendrier)
- `deploiement/dep-02-rag-architecture-prod.html` (section 6bis Stitch/Evaluate/Iterate)
- `deploiement/dep-05-agents-observabilite.html` (section 6bis data plane)
- `prealables/pr-01-maturite-organisationnelle.html` (stat-block 80-95 %)
- `prealables/pr-04-marche-ia-emploi.html` (Baromètre France Num + paradoxe Bpifrance)
- `site-web-prep/RULES-IMPLEMENTATION.md` (v1.5.14)

### 5.3 Validation finale (checklist du brief § 7)

```
☑ RULES v1.5.13 lu en intégralité avant de commencer.
☑ 5 fichiers MD source du dossier v3.8/ lus en intégralité.
☑ Veille CU-026 lue en intégralité.
☑ audit-global.py de départ exécuté (0 hit confirmé).
☑ RULES v1.5.14 amendée et committée (Lot 1).
☑ Les 8 lots ont été exécutés.
☑ Chaque lot a fait l'objet d'un commit séparé.
☑ Le rapport rapport-mission-v3.8.md est complet.
☑ audit-global.py de fin exécuté (0 hit confirmé).
☑ Anti-patterns non automatisés vérifiés (couleurs hardcodées, renvois internes section finale = 0 hit).
☐ Tests croisés Chrome / Firefox / Safari, mobile + desktop OK — à valider visuellement par le mainteneur (variables CSS = rendu identique attendu).
☑ Cohérence numérique cross-site vérifiée (27 / 7 / 8 / 99 / 5 / 6 / 4).
☑ Cohérence card index ↔ contenu sur CU-026 : label « Étude de cas + framework + auto-diagnostic » avec présence effective (case-deep-actor Klarna, tool-table 7 dimensions, form auto-diag interactif).
☑ Auto-diagnostic CU-026 fonctionnel (form + plan + export + persistance localStorage).
☐ Description de PR pointe vers ce brief + RULES v1.5.14 + 5 MD source + veille + rapport mission — à finaliser à la création de la PR.
```
