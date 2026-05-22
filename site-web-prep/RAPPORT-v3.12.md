# Rapport d'itération v3.12 — Hub IA Learning Center

**Date** : 2026-05-22  
**Branch** : `feat/v3.12-trois-nouveaux-prealables`  
**Pilote** : Blaise Cavalli / Claude Code

---

## Périmètre

Création de 3 nouveaux préalables (PR-09, PR-10, PR-11) + cohérence cross-site 8 → 11 préalables.

---

## Livrables créés

### PR-09 — Cadrer un projet IA avant de choisir un outil
- **Badge** : ⭐⭐ Opérationnel · 🧭 Cadrage stratégique · 15 min
- **Sections** : 7 (+ exec-summary + ressources)
- **Contenu clé** : 3 manifestations du tech push, 8 questions de cadrage (table), pattern de refus, 5 anti-patterns en alert-blocks, livrable 1-page en `<pre>`
- **Cross-links** : PR-01, PR-02, PR-04, PR-07, PR-08, PR-10, PR-11, DEP-01

### PR-10 — Vérifier et limiter les hallucinations IA
- **Badge** : ⭐⭐ Opérationnel · 🛡️ Discipline managériale · 18 min
- **Sections** : 7 (+ exec-summary + ressources)
- **Contenu clé** : hallucination silencieuse, 4 familles (chiffres inventés, citations fabriquées, conclusions hors-périmètre, faux positifs de complétion), table types de sorties, 4 niveaux de vérification, golden set / eval / humain
- **Cross-links** : PR-09, PR-11, DEP-05, DEP-07, AgentShield

### PR-11 — Cycle de vie d'un projet IA
- **Badge** : ⭐⭐ Opérationnel · 🔄 Vue d'ensemble séquentielle · 20 min
- **Sections** : 7 (+ exec-summary + ressources)
- **Contenu clé** : table 9 étapes (livrables + durées + ressources), 3 quality gates, coût des raccourcis, cas order-to-cash (9 case-deep-step), table articulation PR×DEP complète
- **Cross-links denses** : PR-01 à PR-10, DEP-01 à DEP-08

---

## Cohérence cross-site

| Fichier | Modification |
|---------|-------------|
| `index.html` | hero-stat 8 → 11, meta description, section À propos |
| `prealables.html` | 3 pr-cards ajoutées (PR-09/10/11), texte hero, footer-cta |
| `README.md` | 8 → 11 préalables, pr-01 à pr-08 → pr-01 à pr-11 |
| `RULES-IMPLEMENTATION.md` | v1.6.3 → v1.6.4, glossaire B.1 mis à jour, entrée historique ajoutée |

---

## Cross-links réciproques

Callout `💡 Pour la vue séquentielle complète...` ajouté avant `<section id="ressources">` dans :
- Préalables : PR-01, PR-02, PR-04, PR-05, PR-07, PR-08
- Déploiement : DEP-01, DEP-02, DEP-03, DEP-04, DEP-05, DEP-06, DEP-07, DEP-08

---

## Audit final

```
Total hits : 0
```

14 règles vérifiées — zéro violation.

---

## Commits

1. `feat(v3.12): création préalable PR-09 « Cadrer un projet IA avant de choisir un outil »`
2. `feat(v3.12): création préalable PR-10 « Vérifier et limiter les hallucinations IA »`
3. `feat(v3.12): création préalable PR-11 « Cycle de vie d'un projet IA » + cross-links réciproques`
4. `chore(v3.12): cohérence cross-site 8→11 préalables + RULES v1.6.4 + audit final + rapport`
