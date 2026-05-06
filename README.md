# Hub IA territorial

Site de micro-learning sur les usages de l'IA en entreprise — programme du **réseau Quest for Change**.

🌐 **Site en ligne** : https://lumenbot.github.io/hub-ia/

## V1.1 — Mai 2026

18 modules courts (10-15 min de lecture) classés par niveau de complexité, avec un format pédagogique différencié selon le niveau :

- 🟢 **N1-N3 Fondamentaux** — quiz 5 questions
- 🟡 **N4-N6 Applications métier** — auto-diagnostic + plan d'action exportable (.txt)
- 🔴 **N7-N8 Industrialisation** — étude de cas + checklist d'éligibilité pondérée

## Structure

```
hub-ia/
├── index.html              ← landing page (3 sections, 18 cards)
├── css/style.css           ← design system unique
├── modules/                ← une page par cas d'usage
│   ├── cu-NNN-*.html       ← modules pédagogiques
│   ├── _template-quiz.html             ← gabarit N1-N3
│   ├── _template-auto-diagnostic.html  ← gabarit N4-N6
│   └── _template-etude-de-cas.html     ← gabarit N7-N8
└── .nojekyll               ← désactive Jekyll côté GitHub Pages
```

## Statut

- ✅ 18 modules publiés et linkés depuis l'index (CU-001 → CU-018)
- ➕ CU-019 (Newsletter locale) disponible en accès direct, hors index V1

## Stack

HTML5 + CSS3 + JS vanilla. Pas de framework, pas de build, pas de backend. Persistance des progressions via `localStorage` (clé `hubia_<module-id>`). Hébergement GitHub Pages.

## Licence

[MIT](LICENSE).

---

Un programme du **réseau Quest for Change**.
