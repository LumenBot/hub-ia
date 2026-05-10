# Hub IA — Learning Center

Site pédagogique sur les usages de l'IA et des agents IA en environnements métier et corporate — programme du **réseau Quest for Change**.

🌐 **Site en ligne** : https://lumenbot.github.io/hub-ia/

## État courant — mai 2026

Une base de référence opérationnelle, en accès libre, structurée en 5 niveaux complémentaires :

- 🧱 **7 préalables** — qu'est-ce que je dois maîtriser avant de me lancer ? (`prealables.html`)
- 🏗️ **4 patterns d'architecture + l'option hybride** — comment je déploie techniquement ? (`architectures.html`)
- 🚀 **8 fiches Déploiement** — comment passer du POC à la production ? (`deploiement.html`)
- 🎯 **26 modules cas d'usage** — comment résoudre concrètement mon problème métier ? (`modules/`)
- 🛠️ **95 fiches outils** — quel outil pour ma stack ? (`ressources.html`)

Les 26 modules sont regroupés en **6 familles métier** sur la home (Découverte / Marketing &amp; croissance / Décision &amp; gouvernance / Fonctions support / Industrie / Architectures agentiques avancées) et étiquetés sur une **échelle de complexité 4 niveaux** (⭐ Initiation · ⭐⭐ Opérationnel · ⭐⭐⭐ Avancé · ⭐⭐⭐⭐ Expert).

## Structure

```
hub-ia/
├── index.html              ← landing page (5 niveaux + 6 familles métier)
├── prealables.html         ← index des 7 préalables
├── prealables/             ← une page par préalable (pr-01 à pr-07)
├── architectures.html      ← 4 patterns + hybride + méthode de décision
├── deploiement.html        ← index des 8 fiches Déploiement (POC → production)
├── deploiement/            ← une page par fiche DEP (dep-01 à dep-08)
├── modules/                ← une page par cas d'usage (cu-001 à cu-025 + cu-027 ; cu-026 réservé)
├── ressources.html         ← catalogue d'outils (95 fiches en 15 catégories)
├── css/                    ← design system (style.css + module-v3.css)
├── js/                     ← module-v3.js (TOC sticky, reading progress, scroll-spy)
└── site-web-prep/          ← briefs, patches, rapports d'audit, RULES, mockups
```

## Stack

HTML5 + CSS3 + JS vanilla. Pas de framework, pas de build, pas de backend. Persistance des progressions via `localStorage` (clé `hubia_<module-id>`). Hébergement GitHub Pages.

## Référentiel d'implémentation

Toute contribution au site doit respecter le référentiel `site-web-prep/RULES-IMPLEMENTATION.md` (sourcing rigoureux, cohérence numérique cross-site, niveau de langue dirigeant non-IT, harmonisation visuelle).

## Licence

[MIT](LICENSE).

---

Un programme du **réseau Quest for Change**.
