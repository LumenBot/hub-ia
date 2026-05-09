# Hub IA — Learning Center

Site pédagogique sur les usages de l'IA et des agents IA en environnements métier et corporate — programme du **réseau Quest for Change**.

🌐 **Site en ligne** : https://lumenbot.github.io/hub-ia/

## v3.5 — mai 2026

Une base de référence opérationnelle, en accès libre, structurée en 4 niveaux complémentaires :

- 🧱 **7 préalables** — qu'est-ce que je dois maîtriser avant de me lancer ? (`prealables.html`)
- 🏗️ **4 patterns d'architecture + l'option hybride** — comment je déploie techniquement ? (`architectures.html`)
- 🎯 **25 modules cas d'usage** — comment résoudre concrètement mon problème métier ? (`modules/`)
- 🛠️ **83 fiches outils** — quel outil pour ma stack ? (`ressources.html`)

Les 25 modules sont regroupés en **6 familles métier** sur la home (Découverte / Marketing &amp; croissance / Décision &amp; gouvernance / Fonctions support / Industrie / Architectures agentiques avancées) et étiquetés sur une **échelle de complexité 4 niveaux** (⭐ Initiation · ⭐⭐ Opérationnel · ⭐⭐⭐ Avancé · ⭐⭐⭐⭐ Expert).

## Structure

```
hub-ia/
├── index.html              ← landing page (4 niveaux + 6 familles métier)
├── prealables.html         ← index des 7 préalables
├── prealables/             ← une page par préalable (pr-01 à pr-06)
├── architectures.html      ← 4 patterns + hybride + méthode de décision
├── modules/                ← une page par cas d'usage (cu-001 à cu-022)
├── ressources.html         ← catalogue d'outils (83 fiches en 14 catégories)
├── css/                    ← design system (style.css + module-v3.css)
├── js/                     ← module-v3.js (TOC sticky, reading progress, scroll-spy)
└── site-web-prep/          ← briefs, patches, rapports d'audit, mockups
```

## Stack

HTML5 + CSS3 + JS vanilla. Pas de framework, pas de build, pas de backend. Persistance des progressions via `localStorage` (clé `hubia_<module-id>`). Hébergement GitHub Pages.

## Référentiel d'implémentation

Toute contribution au site doit respecter le référentiel `site-web-prep/RULES-IMPLEMENTATION.md` (sourcing rigoureux, cohérence numérique cross-site, niveau de langue dirigeant non-IT, harmonisation visuelle).

## Licence

[MIT](LICENSE).

---

Un programme du **réseau Quest for Change**.
