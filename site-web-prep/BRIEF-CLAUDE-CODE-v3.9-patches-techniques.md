# Brief Claude Code — Hub IA Learning Center (passation v3.9)

**Auteur :** Blaise Cavalli — Startup Manager Quai Alpha (Quest for Change)
**Repo :** https://github.com/LumenBot/hub-ia
**Branche cible :** main
**Itération précédente :** v3.8 (expansion réglementaire + CU-026 + 4 fiches outils + RULES v1.5.14 → v1.6 consolidée)
**Nature de cette itération :** PATCHES TECHNIQUES CIBLÉS — refonte ciblée DEP-05 (4 patterns industriels 2026), patch chiffres macro PR-04 (maturité agentique 2026), patches DEP-03 (harness engineering) + DEP-04 (fine-tuning SLM 1B-8B).

---

## 0. Contexte court — pourquoi v3.9

L'itération **v3.9** consolide les **16 pistes** accumulées dans la veille `veille/hub-ia/pistes-cumulatives.md` après le run du 12 mai 2026 (seuil > 12 franchi). Itération **chirurgicale** : aucun nouveau module créé, aucune nouvelle fiche outil, aucune évolution RULES.

**3 lots organisés** :

| Lot | Périmètre | Volume | Source MD Cowork |
|---|---|---|---|
| **Lot A** | Refonte ciblée DEP-05 — nouvelle section 8 « Production-grade : 4 patterns industriels 2026 » (9-layer architecture, gates TOML, Code Execution MCP, Agent Skills) | 1 module enrichi (refonte) | `v3.9/lot-A-dep-05-production-grade.md` |
| **Lot B** | Patch chiffres macro PR-04 — nouvelle section 2ter « Maturité agentique et bottlenecks 2026 » (McKinsey State of AI Trust + Gartner + MIT Sloan) | 1 module patché | `v3.9/lot-B-pr-04-chiffres-macro.md` |
| **Lot C** | Patches DEP-03 (harness engineering) + DEP-04 (fine-tuning SLM 1B-8B + signal faible ELMs) | 2 modules patchés | `v3.9/lot-C-dep-03-dep-04-patches.md` |

**Tu travailles en autonomie**. Cowork (côté Blaise) a produit toute la matière éditoriale en MD structuré dans `site-web-prep/v3.9/`. Ton rôle : transformer cette matière en HTML conforme RULES v1.6 à partir des canoniques existantes.

**Effort estimé Claude Code** : 6-9 h (itération courte par rapport à v3.8).

---

## 1. Préalable obligatoire

**AVANT toute action de code**, tu dois :

1. Lire `site-web-prep/RULES-IMPLEMENTATION.md` v1.6 (référentiel actuel).
2. Lire `site-web-prep/v3.9/lot-A-dep-05-production-grade.md`, `lot-B-pr-04-chiffres-macro.md`, `lot-C-dep-03-dep-04-patches.md` (les 3 fichiers de matière éditoriale).
3. Te référer à `modules/cu-008-knowledge-base-rag.html` comme référence canonique HTML pour patterns techniques denses.
4. Te référer aux états actuels des modules à patcher :
   - `deploiement/dep-05-agents-observabilite.html` (sections 1-7 + Ressources à conserver)
   - `prealables/pr-04-marche-ia-emploi.html` (sections 1-2bis + 3-5 + Ressources à conserver)
   - `deploiement/dep-03-context-engineering-couts.html` (sections 1-3 + 4-6 + Ressources à conserver)
   - `deploiement/dep-04-fine-tuning-pme.html` (sections 1-4 + 5-6 + Ressources à conserver)
5. **Exécuter `python3 site-web-prep/audit-global.py`** pour confirmer l'état de départ (0 hit attendu).

---

## 2. Méthode — 4 lots dans l'ordre

### Lot 0 — Préalable (20 min)

Lectures + audit-global.py de départ.

### Lot 1 — Lot A — Refonte DEP-05 (3-4 h)

**Source MD** : `site-web-prep/v3.9/lot-A-dep-05-production-grade.md`

Détail complet de la nouvelle section 8 dans le MD source. Synthèse :

- **Insertion de la section 8** entre la section 7 « Plan d'action 30 jours » et la section `#ressources`.
- **4 sous-sections** :
  - 8.1 — Pattern 9-layer production architecture (tableau 9 lignes)
  - 8.2 — Gates machine-checkable TOML (avec exemple TOML)
  - 8.3 — Code Execution with MCP (tableau comparatif 2 approches)
  - 8.4 — Agent Skills (avec arborescence de fichiers en exemple)
- **Ajout TOC** : `<li><a href="#section-8"><span class="toc-icon">🏭</span>Production-grade 2026</a></li>`
- **Renvois croisés** à insérer dans sections 3, 4 du même module + DEP-03, CU-026.
- **Badge temps de lecture** : passer de « 20 min » à « 28 min ».
- **Métadonnées meta description** : aucune modification (description actuelle reste juste).

**Composants HTML existants à réutiliser** :
- `.tech-comparison-table` pour le tableau 9-layer
- `<pre><code>` pour les exemples TOML / arborescence Skills
- `.callout-info` ou `.alert-block` pour les encarts de renvoi inter-sections

**Livrable Lot 1** : commit `feat(v3.9): refonte DEP-05 + nouvelle section 8 Production-grade (4 patterns industriels 2026)`.

### Lot 2 — Lot B — Patch chiffres PR-04 (1-2 h)

**Source MD** : `site-web-prep/v3.9/lot-B-pr-04-chiffres-macro.md`

Détail complet de la nouvelle section 2ter dans le MD source. Synthèse :

- **Insertion de la section 2ter** entre la section 2bis « Tendances macro 2026 » et la section 3 « Prime salariale ».
- **4 sous-parties** :
  - Shift de palier 2025 → 2026 + chiffres McKinsey State of AI Trust
  - Avertissement Gartner — l'échec ROI le plus coûteux (80 % suppriment postes)
  - Émergence du Chief AI Officer + 5 trends MIT Sloan
  - Synthèse — cartographie des 4 paliers de maturité (tableau)
- **Ajout TOC** : `<li><a href="#section-2ter"><span class="toc-icon">🤖</span>Maturité agentique</a></li>`
- **Métadonnées meta description** : à actualiser (cf. lot B MD source).
- **Renvois croisés** vers PR-01, CU-026, DEP-05 §8.

**Composants HTML existants à réutiliser** :
- Style tableau existant pour les 4 paliers
- `.callout-info` pour l'encart « Avertissement Gartner »

**Livrable Lot 2** : commit `feat(v3.9): patch PR-04 + nouvelle section 2ter Maturité agentique 2026`.

### Lot 3 — Lot C — Patches DEP-03 + DEP-04 (2-3 h)

**Source MD** : `site-web-prep/v3.9/lot-C-dep-03-dep-04-patches.md`

Détail des 2 patches dans le MD source. Synthèse :

- **C.1 DEP-03** : insertion section 3bis « Du context engineering au harness engineering » (entre section 3 et section 4)
  - Shift conceptuel prompt → context → harness
  - Tableau 8 leviers du harness (checklist PME)
  - Lien explicite vers DEP-05 §8.3 (Code Execution MCP)
  - TOC : `<li><a href="#section-3bis"><span class="toc-icon">🎛️</span>Du context au harness</a></li>`
- **C.2 DEP-04** : insertion section 4bis « Fine-tuning SLM 1B-8B en 2026 » (entre section 4 et section 5)
  - Heuristique « 7-10 SLM avant tout GPU »
  - Tableau stack pratique 2026 (Colab, Unsloth, LoRA/QLoRA, llama.cpp)
  - ROI métier 50 K€+
  - Encart prospectif ELMs (signal faible)
  - TOC : `<li><a href="#section-4bis"><span class="toc-icon">🧪</span>SLM 1B-8B en 2026</a></li>`
- **Renvois croisés** vers PR-07 (depuis DEP-04), DEP-05 §8 (depuis les 2).

**Composants HTML existants à réutiliser** :
- `.tech-comparison-table` pour les 2 tableaux
- `.callout-info` ou nouvelle classe `.signal-faible` pour l'encart prospectif ELMs

**Livrable Lot 3** : commit `feat(v3.9): patches DEP-03 (harness engineering) + DEP-04 (fine-tuning SLM 1B-8B)`.

### Lot 4 — Audit final + rapport (45 min)

- Exécuter `python3 site-web-prep/audit-global.py` — confirmer 0 hit.
- Vérifier visuellement :
  - Renvois croisés cohérents (pas de lien mort)
  - TOC à jour sur les 4 modules patchés
  - Badge temps de lecture mis à jour (DEP-05 → 28 min, PR-04 → +2 min, DEP-03 → +3 min, DEP-04 → +4 min)
  - Cohérence des sections finales `#ressources` (sources ajoutées)
- Produire `RAPPORT-v3.9.md` (synthèse de l'itération, fichiers touchés, métriques avant/après si pertinent).

**Livrable Lot 4** : commit `chore(v3.9): audit final + rapport itération`.

---

## 3. Règles à respecter (rappel synthétique)

- **RULES v1.6** : référentiel actuel — 13 règles essentielles + annexes. Pas de dérive structurelle (Schéma A `#ressources` final maintenu, 9-blocs squelette modules respecté).
- **Pas de nouveau composant CSS** : tous les besoins de v3.9 sont couverts par les classes existantes. Exception possible : classe utilitaire `.signal-faible` si l'encart prospectif ELMs justifie un style distinct (à arbitrer).
- **Sources** : tout ajout dans `#ressources` suit le format des sous-rubriques existantes (📰 Articles de fond, 🎓 Tutoriels & cas pratiques, etc.). Cohérence des liens X.com (Twitter) en URL complète.
- **Audit-global.py** : doit passer à 0 hit avant ET après l'itération.

---

## 4. Coordination inter-canaux

**Item descendant I-D-003 ouvert** dans `Canaux/Hub-IA-Plateforme/rag-prep/SYNC-INTER-CANAUX.md` (12 mai 2026) : canonisation de **6 nouveaux chiffres macro 2026** côté MD RAG (`transverses/chiffres-macro-2026.md`) — issus directement du Lot B v3.9. Pas de dépendance bloquante côté HTML : le HTML PR-04 §2ter cite les sources directement.

Aucune autre coordination requise pour v3.9.

---

## 5. Effort estimé total

| Lot | Effort estimé | Livrable |
|---|---|---|
| Lot 0 (préalable) | 20 min | Audit-global.py |
| Lot 1 (DEP-05 refonte) | 3-4 h | Section 8 complète |
| Lot 2 (PR-04 patch) | 1-2 h | Section 2ter |
| Lot 3 (DEP-03 + DEP-04 patches) | 2-3 h | 2 sous-sections |
| Lot 4 (audit + rapport) | 45 min | Rapport v3.9 |
| **Total** | **6-9 h** | 4 modules patchés + rapport |

---

*Brief produit par Cowork Hub IA le 12 mai 2026. Itération v3.9 chirurgicale — pas de refonte structurelle, pas de nouveau module ou fiche outil, pas d'évolution RULES. Focus sur 4 modules existants (DEP-05, PR-04, DEP-03, DEP-04). Item I-D-003 transmis en parallèle au couple 2 pour canonisation 6 chiffres macro.*
