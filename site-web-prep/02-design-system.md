# Design system — Site Hub IA territorial

> Charte visuelle, choix de typo, conventions de couleurs et composants UI. Cohérent avec l'identité QA et inspiré de la sobriété de qfc-num.

---

## Couleurs

### Palette principale (héritée de la note de cadrage QA)

```
--color-primary:        #1F3864   /* bleu marine — titres, navbar, accents forts */
--color-primary-light:  #2E5395   /* bleu intermédiaire — sous-titres, liens */
--color-primary-accent: #4A6FA5   /* bleu accent — CTA hover */
```

### Couleurs de niveau MOR-IA (pour les badges et sections)

```
/* Niveau 1 — Fondamentaux (vert) */
--color-n1-bg:     #E8F4E0
--color-n1-fg:     #2E5C2E
--color-n1-border: #5C8C5C

/* Niveau 2 — Applications métier (jaune) */
--color-n2-bg:     #FDF4DC
--color-n2-fg:     #7A5C20
--color-n2-border: #B89030

/* Niveau 3 — Industrialisation (rouge sobre) */
--color-n3-bg:     #FCEFE8
--color-n3-fg:     #7A2C10
--color-n3-border: #B05A30
```

### Neutres

```
--color-bg:        #FAFAFC   /* fond global légèrement bleuté */
--color-surface:   #FFFFFF   /* fond cards et panneaux */
--color-text:      #1A1A1A   /* texte principal */
--color-text-soft: #555555   /* texte secondaire */
--color-text-mute: #888888   /* méta, dates, légendes */
--color-border:    #E5E7EB   /* bordures fines */
--color-border-strong: #D1D5DB
```

### États

```
--color-success: #16A34A   /* validation, module complété */
--color-warning: #F59E0B   /* AI Act, attention */
--color-danger:  #DC2626   /* erreurs, hors périmètre */
```

---

## Typographie

### Police principale : Inter (Google Fonts)

Justification : moderne, hautement lisible à toutes les tailles, gratuite, large adoption professionnelle, multilingue (français incluant les diacritiques).

```css
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

--font-base: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
```

### Hiérarchie typographique

```
h1 (titre hero)         3.5rem / 56px / 800 / line-height 1.1
h2 (titre section)      2rem / 32px / 700 / line-height 1.2
h3 (titre card/module)  1.25rem / 20px / 700
h4 (sous-titre)         1.0625rem / 17px / 600

body                    1rem / 16px / 400 / line-height 1.6
small                   0.875rem / 14px / 400
meta / badge            0.75rem / 12px / 600 / uppercase / letter-spacing 0.05em
```

---

## Espacement (système 8 px)

```
--space-1:  0.25rem  /* 4px */
--space-2:  0.5rem   /* 8px */
--space-3:  0.75rem  /* 12px */
--space-4:  1rem     /* 16px */
--space-5:  1.5rem   /* 24px */
--space-6:  2rem     /* 32px */
--space-7:  3rem     /* 48px */
--space-8:  4rem     /* 64px */
--space-9:  6rem     /* 96px */
```

---

## Composants UI

### Navbar

- Hauteur fixe : 64 px
- Fond : transparent au top, `#1F3864` après scroll (avec backdrop-filter blur)
- Contient : logo Hub IA territorial à gauche, lien navigation à droite (« Modules » + lien GitHub icône)
- Position : `position: fixed; top: 0; z-index: 100;`

### Hero

- Padding vertical généreux : 6rem en haut, 4rem en bas
- Fond : dégradé subtil `#1F3864` → `#2E5395`
- Texte : blanc
- Badge « Nouveau » + sous-titre court
- Titre h1 grand
- Description de 1-2 lignes
- CTA principal vers les modules
- Marquee de logos incubateurs en bas du hero (comme qfc-num)

### Cards modules

Structure typique :
```
┌─────────────────────────────────┐
│ 🧠              [BADGE NIVEAU]  │
│                                 │
│ Titre du module                 │
│ Description courte (2 lignes)   │
│                                 │
│ Commencer →    🔵 5 questions  │
└─────────────────────────────────┘
```

- Padding : `1.5rem`
- Border radius : `12px`
- Fond : blanc avec border `#E5E7EB`
- Hover : élévation légère (shadow), translation -2px sur Y, bordure colorée selon niveau
- Transition : `200ms ease`
- Badge niveau coloré en haut à droite (vert N1, jaune N4, rouge N7)
- Indicateur « Complété » avec coche verte (apparaît après quiz validé via localStorage)

### Section header

- Layout horizontal : icône à gauche (emoji dans cercle coloré), titre + description à droite
- Background icône : couleur du niveau correspondant (vert / jaune / rouge clair)
- Padding section : `4rem` vertical, `2rem` horizontal max
- Container max-width : `1280px`

### Page module

Structure :

```
[Navbar fixe]

[Hero compact]
  ← Retour aux modules
  [Badge niveau] [Badge axe]
  Titre du module (h1)
  Sous-titre / promesse pédagogique

[Contenu principal — typographie generous]
  ## Section 1
  ## Section 2
  ...
  > Encadrés / quotes
  - Listes à puces
  Code blocks (si applicable)

[Quiz 5 questions]
  Question 1 (radio buttons)
  Question 2 ...
  [Valider mon quiz]
  → Score affiché + module marqué complété

[Pour aller plus loin]
  - Liens ressources
  - Module suivant suggéré

[Footer]
```

### Quiz

- 5 questions avec 4 options chacune (3 mauvaises + 1 bonne, ou autre format pédagogique selon le module)
- Validation côté client (pas de backend nécessaire)
- Score affiché après validation : « 4/5 — bien ! »
- Bouton « Voir les corrections » qui révèle la réponse correcte de chaque question
- À la validation, écriture localStorage : `culturation_<module-id> = { completed: true, score: 4, date: "2026-05-06" }`

### Footer

- Fond : `#1F3864`
- Texte : blanc
- Logo + mention « Hub IA territorial — un programme du réseau Quest for Change »
- Liens secondaires : « À propos », « Contact », lien GitHub
- Mention « Mai 2026 » + version

---

## Responsive — breakpoints

```
/* Mobile : par défaut */

@media (min-width: 640px)  { /* Tablette portrait */ }
@media (min-width: 768px)  { /* Tablette paysage */ }
@media (min-width: 1024px) { /* Desktop */ }
@media (min-width: 1280px) { /* Large desktop */ }
```

Cards :
- Mobile : 1 colonne pleine largeur
- Tablette : 2 colonnes
- Desktop : 3 colonnes

---

## Iconographie

### Emoji par module (cohérent avec qfc-num)

| Module | Emoji | Justification |
|---|---|---|
| CU-001 Recherche & veille | 📚 | livre / référence |
| CU-002 Assistant rédactionnel | ✍️ | écriture |
| CU-003 CR de réunion | 🎙️ | enregistrement audio |
| CU-004 Traduction multi-langues | 🌍 | globe |
| CU-005 Devis et propositions | 📄 | document |
| CU-006 Leads chatbot | 💬 | conversation |
| CU-007 RH CV entretiens | 👥 | équipe |
| CU-008 Knowledge base RAG | 🧠 | mémoire |
| CU-009 Content repurposing | 🔁 | recyclage / boucle |
| CU-010 Pipeline contenu social | 📱 | mobile / social |
| CU-011 Veille concurrentielle | 🔭 | observation lointaine |
| CU-012 Veille AAP + drafting | 💸 | financement |
| CU-013 Workflow email-CRM | 📧 | email |
| CU-014 Multi-agents | 🤖 | agent |
| CU-015 Stripe Minions | 👨‍💻 | développeur |
| CU-016 Maintenance prédictive | 🔧 | outil de maintenance |
| CU-017 Contrôle qualité vision | 👁️ | œil / vision |
| CU-018 Optimisation production | ⚙️ | engrenage / process |

### Icônes UI

Utiliser **Lucide Icons** (set open source moderne, alternative à Feather) en SVG inline pour : navigation, validation, avertissement, lien externe, étoile.

Disponibles via : `https://lucide.dev` ou copier-coller direct des SVG.

---

## Animations / interactions

Sobre par défaut :

- Hover cards : élévation `transform: translateY(-2px)` + `box-shadow` légère
- Hover boutons CTA : changement de fond + petite ombre
- Marquee logos hero : défilement infini horizontal lent (`animation: scroll-x 40s linear infinite`)
- Apparition cards à scroll : optionnelle, peut être ajoutée en V2 avec IntersectionObserver
- Pas d'animation gratuite (parallax, particles, etc.)

---

## Accessibilité

Niveau visé : WCAG 2.1 AA

- Contraste texte / fond ≥ 4.5:1 (vérifié pour toutes les combinaisons)
- Navigation au clavier complète (focus visible, ordre logique)
- Liens explicites (pas de « cliquez ici »)
- Alt text sur toutes les images
- Headings hiérarchisés (h1 → h2 → h3 sans saut)
- Quiz accessible : labels associés aux radio buttons, validation avec annonce du score

---

*Design system V1 — Mai 2026. Cohérent avec la note de cadrage QA et le pattern qfc-num.*
