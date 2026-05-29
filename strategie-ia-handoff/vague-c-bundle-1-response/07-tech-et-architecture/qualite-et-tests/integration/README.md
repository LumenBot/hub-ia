# `07-tech-et-architecture/qualite-et-tests/integration/` — Tests d'intégration UI (Playwright)

**Version** : v0.1.0 (smoke test §2.1 JOURNEY — extension à venir avec composants conversation §2.2)
**Date de création** : 2026-05-29
**Dernière mise à jour** : 2026-05-29
**Statut** : validé
**Auteur principal** : Cowork Hub IA Plateforme (Claude Code RAG)
**Owner fonctionnel** : 07-tech-et-architecture
**Confidentialité** : public
**Tags** : tests, integration, playwright, ui, composants, vague-c, smoke-test

---

## 1. Synthèse exécutive

Tests d'intégration UI au runtime navigateur (Playwright) pour les composants front
de `06-produit-et-site/produit-app/*` et `site-public/*`.

**Périmètre exclusif** : tests browser-driven (DOM, interactions, localStorage,
JavaScript runtime). **Hors périmètre** : tests pipeline RAG (pytest, `09/tests/`,
owner Hub RAG) + tests audit gouvernance (`audit_conformity.sh`, CI Vague A).

**État actuel** : 1 fichier de test (smoke test JOURNEY), 7 tests fonctionnels.
Extension Vague C contributions (~2026-06-22) avec tests composants conversation
(chat-input + message-bubble + source-card).

## 2. Contexte

Issu de l'amendement #5 de la réponse `_handoffs/claude-code-rag-vers-claude-code-content/reponse-brief-vague-c-2026-05-29.md`
et adopté par Content dans `_handoffs/claude-code-content-vers-claude-code-rag/accuse-reception-arbitrage-vague-c-2026-05-29.md`.

Objectif du smoke test : **valider la portabilité technique** de la migration §2.1
(fork de `hub-ia/{css,js}/journey.*` vers composant content-agnostic dans
`strategie-ia/06/produit-app/composants/journey/`) après :

- Variables CSS renommées `--color-X` → `--st-color-X` avec fallbacks inline
- STARTER_LIBRARY hardcodée remplacée par injection config `window.STRATEGIE_IA_JOURNEY_CONFIG`
- `localStorage` préfixe `hubia_` → `strategie-ia_`
- API publique `window.StrategieIAJourney.{init, refreshBadges, readCompleted}`

7 tests couvrent les 6 sous-composants + l'API publique. **Pas de pixel-perfect**,
pas de visual regression — compatible avec le fallback style-agnostic si maquettes
Claude Design indispos.

## 3. Stack technique

| Outil | Version | Rôle |
|-------|---------|------|
| `@playwright/test` | ^1.45.0 | Test runner + assertions + browser automation |
| `http-server` | ^14.1.1 | Static file server pour servir `journey-example.html` |
| Node | >=18 | Runtime requis Playwright |
| Chromium | (auto) | Navigateur cible (Firefox + Webkit ajoutables Vague C contribs) |

**Pas de dépendance externe additionnelle** (pas de TypeScript compilation step requise —
Playwright gère TS nativement via tsx).

## 4. Installation et exécution locale

```bash
cd 07-tech-et-architecture/qualite-et-tests/integration/

# 1. Install
npm install

# 2. Install browsers (Chromium uniquement par défaut)
npm run install:browsers

# 3. Run smoke tests
npm test

# 4. UI mode (debug visuel)
npm run test:ui

# 5. Voir le rapport HTML après échec
npm run report
```

Le `webServer` Playwright (cf. `playwright.config.ts`) démarre `http-server`
automatiquement sur le port 3000 et l'arrête à la fin. **Aucune action manuelle
de démarrage du serveur**.

## 5. Tests inclus (1 fichier — `tests/journey-smoke.spec.ts`)

| # | Test | Sous-composant validé |
|---|------|------------------------|
| 1 | page charge sans erreur console + titre présent | Page entry point |
| 2 | 6 sous-composants visibles dans le DOM | SC1-SC6 (existence) |
| 3 | fil ariane : 5 stations + "Conversation" current | SC1 fil d'Ariane (état) |
| 4 | wizard happy path : profil + objectif → 3 recommandations | SC3 wizard (logique injection config) |
| 5 | localStorage écrit avec préfixe `strategie-ia_` (pas `hubia_`) | Régression test clé de l'adaptation §2.1 |
| 6 | API publique `window.StrategieIAJourney` exposée | API publique (init/refreshBadges/readCompleted) |
| 7 | badge progression : 1/5 complète après clic card | SC5 badges (intégration localStorage + UI) |

**Pas couvert volontairement** (sortie de scope smoke test, à étendre Vague C contribs) :
- Sticky scroll behavior (`.journey` reste en haut au scroll)
- Restart wizard (`.starter-restart` clear state)
- Multiple cards completion (gradient progress fill)
- Mobile responsive (viewport adjustments)
- A11y (Lighthouse CI couvre — cf. `../lighthouse/`)

## 6. CI/CD

Intégration au workflow `audit-conformity.yml` de Vague A : **différée à mes contributions
Vague C** (2026-06-19 → 2026-06-24). Pour ce smoke test livré en early-bird, exécution
locale uniquement (validation de la portabilité technique de §2.1).

Quand l'intégration CI sera faite (Vague C contribs), ajout d'un job `ui-integration`
au workflow existant — distinct du job `audit-conformity` (différentes natures de
vérification).

## 7. Frontières (FRONTIERES.md v1.0 §2.8 — système livré vs orchestration interne)

| Domaine | Dossier | Owner |
|---------|---------|-------|
| Tests d'intégration UI (browser-driven) | **`07/qualite-et-tests/integration/`** (ce dossier) | Claude Code RAG |
| Tests pipeline RAG (pytest, in-process) | `09/tests/` | Hub RAG |
| Audit gouvernance MD/YAML (statique) | `07/qualite-et-tests/` (Vague A `audit_conformity.py`) | Claude Code RAG |
| Lighthouse CI (perf + a11y) | `07/qualite-et-tests/lighthouse/` (à venir Vague C contribs) | Claude Code RAG |
| Composants UI sources (HTML/CSS/JS) | `06/produit-app/composants/*` | Claude Code Content |

**Frontière nette** : ce dossier teste le **comportement** des composants 06 ; Content
owne le **code** des composants. Pas de chevauchement structurel.

## 8. Évolutions à prévoir (Vague C contribs 2026-06-19 → 2026-06-24)

- **`tests/composants-conversation.spec.ts`** : tests des 7 fichiers consolidés
  `06/produit-app/composants/conversation/*` (chat-input + message-bubble + source-card)
  — dès leur livraison Content Bundle Vague C #3
- **`tests/landing-soft-launch.spec.ts`** : tests landing `06/site-public/landing/soft-launch/*`
  — dès Pack H bis Cavalli débloqué
- **`composants-ui-spec.md`** : spec des interactions attendues (référencée par les tests)
- Multi-browser support (Firefox + Webkit)
- Intégration CI bloquante dans `.github/workflows/audit-conformity.yml` (job `ui-integration`)
- **`baseline-seuils-proposee.md`** : draft tech web vitals seuils (cf. amendement #2 réponse
  brief Vague C) — input précurseur pour `06/monitoring-site/web-vitals/web-vitals-config.md`

## 9. Coordination

- **Claude Code Content** : owne `06/produit-app/composants/*` et `06/site-public/*` (les cibles
  à tester). Coordination via `_handoffs/coordination-cc-content-cc-rag/coordination-bidirectionnelle.md`
- **Hub RAG** : reviewer croisé R2 fast-track tech sur 07 + 09 (cf. CONTRIBUTING.md v1.1 §2 R2).
  Pas de chevauchement direct (tests UI vs tests pipeline)
- **Hub Strat** : reviewer transverse (conventions + cohérence) — relit ce README + structure dossier

## 10. Sources et références

- `_handoffs/claude-code-content-vers-claude-code-rag/brief-scope-vague-c-claude-code-content-2026-05-28.md` §2.1
- `_handoffs/claude-code-rag-vers-claude-code-content/reponse-brief-vague-c-2026-05-29.md` amendement #5 + §9
- `_handoffs/claude-code-content-vers-claude-code-rag/accuse-reception-arbitrage-vague-c-2026-05-29.md` §2 adoption #5
- `06-produit-et-site/produit-app/composants/journey/journey-example.html` (cible des tests)
- `_handoffs/coordination-cc-content-cc-rag/coordination-bidirectionnelle.md` (état partagé)

---

## Historique

| Date | Version | Modification |
|------|---------|--------------|
| 2026-05-29 | v0.1.0 | Création — smoke test JOURNEY §2.1 (7 tests Playwright + config + package.json + ce README). Livraison early-bird vs mon planning 19-24 juin (pré-Vague B, fenêtre J-10 → J+10 utilisée). Validation portabilité migration content-agnostic §2.1 (variables `--st-*`, localStorage `strategie-ia_`, API `StrategieIAJourney`). Extension prévue Vague C contribs : composants conversation + landing + multi-browser + CI intégration. |

---

*Tests d'intégration UI `strategie-ia` v0.1.0 — Cowork Hub IA Plateforme (Claude Code RAG), 29 mai 2026. Smoke test §2.1 livré en accélération vs planning initial. Extension Vague C contribs entre 2026-06-19 et 2026-06-24.*
