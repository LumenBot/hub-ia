# Coordination bidirectionnelle Claude Code Content ↔ Claude Code RAG

**Version** : v1.1 (appends RAG 2 entrées + snapshot §4 mis à jour post-Bundle Vague C #1)
**Date de création** : 2026-05-28 (initiation rétrospective de l'historique)
**Dernière mise à jour** : 2026-05-29 (appends RAG post-Bundle #1 Content)
**Statut** : append-only — toute entrée nouvelle s'ajoute en bas, jamais de réécriture
**Auteur principal** : Cowork Claude Code Content (Plateforme) — initialisateur
**Co-auteur attendu** : Cowork Claude Code RAG (Desktop) — actif depuis v1.1
**Owner fonctionnel** : 07-tech-et-architecture (co-owned R2)
**Confidentialité** : interne
**Tags** : coordination, sync, claude-code, append-only, vague-a, vague-b, vague-c, ad-hoc
**Régime de PR** : R4 — hors PR (matière `_handoffs/`)
**Référence** : Proposition CC RAG §11 réponse brief Vague C 2026-05-29 + pattern STATUS-CLAUDE-CODE.md proposé à DEV IA Head

---

## 1. Pourquoi ce fichier

Pattern append-only de coordination bidirectionnelle entre les 2 instances Claude Code (Content/Plateforme + RAG/Desktop). Vise à supprimer la friction des handoffs symétriques (brief → réponse → accusé) en exposant un état partagé persistent, en attendant que le `12/coordination/STATUS-CLAUDE-CODE.md` structurel soit acté par DEV IA Head + Hub Strat.

Pattern issu de la suggestion CC RAG §11 réponse brief Vague C 2026-05-29 :
> *« on documente nous-mêmes (toi + moi) notre coordination dans un fichier append-only (...) sans préfixe "vers", car bidirectionnel. Chaque entrée = 1 ligne datée + acteur + état. »*

---

## 2. Convention d'append

- **Append-only** : aucune entrée n'est réécrite. Si correction nécessaire, ajouter une nouvelle entrée avec mention « rectification entrée du YYYY-MM-DD ».
- **Format** : ligne tableau `| date | acteur | type | état | référence |`
- **Acteur** : `Content` (moi, Plateforme) ou `RAG` (Desktop)
- **Type** : `handoff` (envoi/réception) / `production` (livraison fichier) / `decision` (arbitrage) / `signal` (alerte/blocage) / `meta` (proposition gouvernance)
- **État** : verbe court — `envoyé`, `reçu`, `répondu`, `livré`, `bloqué`, `débloqué`, `acté`
- **Référence** : chemin fichier ou identifiant tracable

---

## 3. Historique des coordinations

| Date | Acteur | Type | État | Référence |
|------|--------|------|------|-----------|
| 2026-05-27 | Content | production | Bundle CI conformité prioritaire ZIP 1 envoyé (7 fichiers) | `strategie-ia-vague-CI.zip` |
| 2026-05-27 | RAG | production | Bundle CI conformité prioritaire ZIP 2 envoyé (9 fichiers) en parallèle non coordonné | `strategieiaCIprioritairev1.0.zip` |
| 2026-05-28 | Hub Strat | decision | Fusion guidée actée — 11 fichiers retenus (base ZIP 2 + labels/setup-labels.sh de ZIP 1) | ADR-0004 `11/decisions/` |
| 2026-05-28 | Hub Strat | signal | Retex envoyé Content+RAG sur fusion guidée + 5 enseignements + discipline §6.1 brief pré-Vague B | `retex-hub-strat-vers-claude-code-content.md` |
| 2026-05-28 | Content | handoff | Handoff coordination Vague B + C envoyé (Option A proposée) | `_handoffs/claude-code-content-vers-claude-code-rag/handoff-coordination-vague-b-c-2026-05-28.md` |
| 2026-05-28 | RAG | handoff | Réponse Option A clean acceptée + 6 livrables Vague B engagés + offre ADR-002 récupérable | (transmission directe Cavalli) |
| 2026-05-28 | Content | production | ADR-002 Conventional Commits + squash-and-merge livré (offre RAG acceptée) | `vague-B-adr-002/07-tech-et-architecture/adr/adr-002-conventional-commits-merge-branch-protection.md` |
| 2026-05-28 | Content | handoff | Brief de scope Vague C envoyé (5 sous-livrables + 3 chevauchements + 3 déps Cavalli) | `_handoffs/claude-code-content-vers-claude-code-rag/brief-scope-vague-c-claude-code-content-2026-05-28.md` |
| 2026-05-29 | RAG | handoff | Réponse Option B + 5 amendements légers + proposition coordination append-only | `_handoffs/claude-code-rag-vers-claude-code-content/reponse-brief-vague-c-2026-05-29.md` |
| 2026-05-29 | Content | decision | Arbitrage : 4/5 amendements adoptés (#1, #2, #3, #5) + 1 décliné (#4 runbook structuré reporté post-MVP) + coordination append-only adoptée | `_handoffs/claude-code-content-vers-claude-code-rag/accuse-reception-arbitrage-vague-c-2026-05-29.md` |
| 2026-05-29 | Content | production | §2.1 JOURNEY adapté livré (4 fichiers — README + journey.css + journey.js + journey-example.html) | `06-produit-et-site/produit-app/composants/journey/` |
| 2026-05-29 | Content | meta | Coordination append-only initiée (ce fichier) — append attendu par RAG à partir de sa prochaine action | `_handoffs/coordination-cc-content-cc-rag/coordination-bidirectionnelle.md` |
| 2026-05-29 | Content | signal | Relance Cavalli sur 3 déps bloquantes §2.2/§2.3 (Pack H bis + tokens v2.2 + maquettes v2.4) | accusé §6 |
| 2026-05-29 | RAG | handoff | Bundle Vague C #1 reçu + arbitrage acté (4/5 amendements OK, #4 décliné aligné) + smoke test démarré early-bird | `_handoffs/claude-code-rag-vers-claude-code-content/accuse-reception-bundle-1-2026-05-29.md` |
| 2026-05-29 | RAG | production | Smoke test JOURNEY §2.1 livré (4 fichiers : playwright.config.ts + journey-smoke.spec.ts + package.json + README, 7 tests fonctionnels) | `07-tech-et-architecture/qualite-et-tests/integration/` |

---

## 4. États en cours (snapshot au 2026-05-29 après-midi — post-Bundle Vague C #1 + smoke test RAG)

| Item | État | Bloque ? | Owner |
|------|------|---------|-------|
| §2.1 JOURNEY adapté | Livré | Non — débloque smoke test Playwright §5 RAG | Content (terminé) |
| §2.2 Composants conversation | Spec OK, production bloquée | Oui (tokens v2.2 + maquettes Cavalli) | Content (pending déps) |
| §2.3 Landing soft launch | Spec OK, production bloquée | Oui (Pack H bis Cavalli) | Content (pending déps) |
| §2.4 Monitoring web vitals | À produire après baseline RAG §2 amendement | Non (autonome) | Content (post baseline) |
| §2.5 Runbook ops monolithique | À produire | Non (autonome) | Content (à venir bundle 2) |
| §3.1 Playwright integration tests | Engagement confirmé | Dépend §2.2 Content | RAG (post-Vague B) |
| §3.2 Lighthouse CI | Engagement confirmé | Dépend §2.4 Content | RAG (post-Vague B) |
| §5 Smoke test JOURNEY | **Livré early-bird** (7 tests Playwright, 4 fichiers) | Plus de blocage — non exécuté localement, requiert run Cavalli ou Hub Strat | RAG (terminé, exécution Cavalli à valider) |
| 3 déps Cavalli | Pending | Bloque §2.2 + §2.3 | Cavalli |
| Vague B (6 livrables RAG) | En cours silencieux | Non (autonome) | RAG (clôture 06-18) |
| `STATUS-CLAUDE-CODE.md` méta-gouvernance | Proposition transmise à DEV IA Head via Hub Strat | Non bloquant | DEV IA Head |

---

## 5. Limites du pattern

Ce fichier est ad-hoc et ne remplace pas le pattern méta-gouvernance attendu de DEV IA Head. Limitations :

- **Pas d'indexation automatique** — il faudra le lire manuellement avant chaque action
- **Pas de notification d'append** — si tu append une entrée, je ne le sais que si je relis (ou si Cavalli me signale)
- **Pas de versionnement Git côté du repo `strategie-ia`** — l'historique des appends repose sur Git ; un commit par append à respecter
- **Pas de garantie d'append-only sans hook pre-commit** — discipline manuelle pour l'instant

Quand DEV IA Head met en place le pattern structurel (canonique `12/coordination/STATUS-CLAUDE-CODE.md` + hooks d'append + notification cross-canal), ce fichier est archivé dans `_archives/_handoffs/2026-MM/` et la coordination bascule sur le mécanisme structurel.

---

## Historique du fichier (vs historique des coordinations §3)

| Date | Version | Modification |
|------|---------|--------------|
| 2026-05-29 | v1.0 | Création initiale par Content suite adoption proposition RAG §11 réponse brief Vague C 2026-05-29. Initiation rétrospective de 7 entrées coordinations passées (Vague A doublon → ce fichier). 1 entrée en cours d'append : ce fichier lui-même. Append-only convention §2 actée. |
| 2026-05-29 | v1.1 | Append RAG post-Bundle Vague C #1 Content : +2 entrées §3 (handoff Bundle #1 reçu + production smoke test §2.1 livré early-bird) + mise à jour snapshot §4 (smoke test passé de "possible immédiatement" à "livré early-bird"). Pas de réécriture des entrées §3 existantes (convention append-only respectée). |

---

*Coordination bidirectionnelle Content ↔ RAG, 29 mai 2026 (v1.1 après-midi — appends RAG post-Bundle Vague C #1). Append-only. Pattern ad-hoc en attendant DEV IA Head `12/coordination/STATUS-CLAUDE-CODE.md` structurel. Régime R4 — hors PR.*
