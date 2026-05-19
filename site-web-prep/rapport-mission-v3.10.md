# Rapport de mission Claude Code — Itération v3.10

**Date** : mai 2026
**Branche** : `feat/v3.10-iteration-majeure` (basée sur `main` à jour, post v3.9 mergée)
**Auteur** : Claude Code
**Brief source** : `site-web-prep/BRIEF-CLAUDE-CODE-v3.10-iteration-majeure.md` + 5 MD éditoriaux Lot A à E dans `site-web-prep/v3.10/`

## Synthèse exécutive

Itération éditoriale **v3.10 majeure** livrée en **5 commits Lot A-E + ce rapport**. Intégration de **15 pistes sur 28 accumulées** dans `pistes-cumulatives.md`. Création du **8ᵉ préalable PR-08 « Financer son projet IA en 2026 »** avec impacts cohérence numérique cross-site, et 13 patches/enrichissements répartis sur 11 modules existants.

`audit-global.py` retourne **`Total hits : 0`** en clôture (14 règles dont rule 14 cross-site outils). Aucun écart résiduel bloquant.

## Lots exécutés

### Lot 0 — Préalable (réalisé)

- Lecture brief intégral + 5 MD source (lot-A à lot-E, ~1 200 lignes)
- Audit baseline confirmé : **Total hits : 0**
- Création branche `feat/v3.10-iteration-majeure` depuis `main`

### Lot A (1ᵉʳ commit) — CU-008 + DEP-02 : RAG vs persistent memory

Commit : `feat(v3.10): CU-008 + DEP-02 — encart symétrique RAG vs persistent memory` (87b6a47)

**3 signaux convergents (mai 2026)** sur la durée de vie potentiellement limitée (3-6 mois) des stacks RAG classiques :
- @0xCVYH (SubQ) — long context 10M+ natif
- @Suryanshti777 — Karpathy LLM Wiki post-écosystème
- @JE4NVRG (Hermes Agent) — persistent memory > RAG stateless

**CU-008** : nouvelle h3 `#llm-wiki-shelf-life` en fin de section `#llm-wiki` + takeaway 5 + badge 30→33 min + 4 sources.
**DEP-02** : nouvelle h3 `#section-2bis` en fin de section 2 + takeaway 5 + badge 22→24 min + 3 sources + tableau 5 lignes décision par profil projet.

Symétrie stricte des 2 patches (mêmes 3 signaux, même horizon 3-6 mois, même formulation « ce qui ne change pas », préfiguration symétrique du pattern A5 à venir).

### Lot B (2ᵉ commit) — CU-020 + CU-024 : réglementaire & conformité

Commit : `feat(v3.10): CU-020 + CU-024 — patches réglementaires (AI Act Art. 50 draft guidelines, fiches CNIL, terminologie PA)` (be6eb6c)

**CU-020 (Conformité RGPD & AI Act)** — 3 patches B.1+B.2+B.3 :
- Encart synthèse en tête de section AI Act Article 50 : 3 échéances 2026 (3 juin / 2 août / 2 décembre)
- h3 « Draft Guidelines Art. 50 — publication 8 mai 2026 » : calendrier précis + obligations confirmées fournisseurs/déployeurs
- h3 « Fiches IA finales CNIL + guide HAS-CNIL » : 3 thèmes CNIL + 12 fiches HAS-CNIL santé
- Meta description ajoutée, badge 45→49 min, 3 sources ajoutées

**CU-024 (Order-to-cash)** — patch B.4 terminologique :
- « PA (anciennement PDP, renommées par art. 27 LF 2026) » en première occurrence historique
- 120 → 125 plateformes agréées (DGFiP au 5 mai 2026, +17 en attente) — 4 occurrences
- Timeline complétée : ajout step émission grandes entreprises + ETI au 1er sept 2026
- Sources DGFiP impots.gouv.fr + service-public.fr/A18759 ajoutées
- Meta description actualisée

### Lot C (3ᵉ commit) — Création préalable PR-08 « Financer son projet IA en 2026 »

Commit : `feat(v3.10): création préalable PR-08 Financer son projet IA en 2026 + impacts cross-site 7→8 préalables` (287ed14)

**Nouveau préalable `prealables/pr-08-financer-projet-ia.html`** :
- Executive summary 5 takeaways + 4 exec-stats (25 M€ IA Booster / 40 % diagnostics / 15 M professionnels 2030 / 240 M€ capital Bpifrance ×14)
- 7 sections + ressources :
  - §1 Pourquoi 2026 change tout (3 ruptures structurelles)
  - §2 Fiscalité IA 2026 (tableau 7 dispositifs CIR/CII/CII-IA/JEI/JEII/CICO/C3IV)
  - §3 Plan « Osez l'IA » France 2030 (6 leviers)
  - §4 Deux deadlines critiques juin 2026 (AMI 5 juin / AAP 9 juin)
  - §5 Financements Bpifrance (4 leviers + chiffres 2025)
  - §6 Méthode 5 étapes empilement + 5 pièges à éviter
  - §7 Plan d'action 30 jours (4 étapes case-deep-step)
- Badge 18 min de lecture, icône 💰

**Cohérence numérique cross-site 7 → 8 préalables** :
- `prealables.html` : nouvelle card PR-08 + meta + accroche
- `index.html` : meta + hero stat (7→8) + section À propos (8 cadrages)
- `README.md` : 8 préalables + structure pr-01 à pr-08

**Cross-link ajouté** : PR-04 section 5 → encart renvoyant vers PR-08.

**RULES v1.6 → v1.6.1** :
- Glossaire chiffres-clés § 4.B.1 : 7 → 8 préalables PR
- Header version, entrée historique condensé

### Lot D (4ᵉ commit) — DEP-08 §7bis SBOM IA + PR-05 encarts McKinsey/NIST

Commit : `feat(v3.10): DEP-08 §7bis SBOM IA + PR-05 encarts McKinsey + NIST CAISI + NIST Critical Infrastructure` (b3fcab5)

**DEP-08 (Sécurité agents et MCP)** :
- Nouvelle section 7bis « SBOM IA & supply chain » entre §7 et `#ressources`
- 4 sous-parties (tableau 5 composants SBOM + 3 raisons PME + 3 approches mise en place + 5 liens internes)
- TOC entry §7bis (icône 📦), takeaway 5 ajouté, badge 22→26 min, 2 sources ANSSI/G7

**PR-05 (Sécurité IA)** :
- Nouvelle sous-section `#risques-agentiques` en fin de §3 : citation McKinsey + chiffres RAI maturité 2,3/5 + encart NIST AI RMF Critical Infrastructure (arbitrage favorable du brief — pertinence OIV/OSE et PME industrielles vosgiennes)
- Nouvelle sous-section `#nist-caisi` en fin de §4 : 6 thèmes prioritaires + calendrier précis 2026 + couples avec SBOM/AI Act/CU-026
- Meta description ajoutée, badge 12→15 min, 4 sources ajoutées
- Wikilinks réciproques DEP-08 §7bis ↔ PR-05 #nist-caisi

### Lot E (5ᵉ commit) — Marché, maturité, patterns agentiques

Commit : `feat(v3.10): Lot E — marché, maturité, patterns agentiques (6 patches)` (ba653b5)

**E.1 PR-04 (Marché IA & emploi)** : section 2bis enrichie (Bpifrance Le Lab 55 % TPE-PME ×1,8, trajectoire Bpifrance 2025, Microsoft Work Trend Index 2026, ordres de grandeur) + encart Transformation Paradox dans section 5. Meta + badge 12→16 min + 5 sources.

**E.2 PR-01 (Maturité organisationnelle)** : nouvelle h3 typologie 4 profils dirigeants Bpifrance (Sceptiques 27 / Bloqués 26 / Expérimentateurs 19 / Innovateurs 28 %) + leviers + insight 73 % initiative dirigeant. Meta + badge 15→17 min.

**E.3 DEP-01 (Cadrer un projet IA)** : nouvelle h3 « Heuristique anti-hype 2026 — single LLM call d'abord » avec arbre 6 niveaux. Badge 18→20 min + source @LearnWithBrij.

**E.4 DEP-05 (Agents en production)** : §8.5 « Failure receipts & ownership » (cas coding agent 9 secondes + pattern correctif) + §8.5bis « Effective Harnesses long-running » (two-agent harness). Conclusion synthèse mise à jour (6 patterns au lieu de 4). Badge 28→32 min + 4 sources.

**E.5 CU-026 (Gouvernance agents)** : nouvelle section 3bis « 4 patterns de collaboration » (Microsoft Frontier Firms — Author/Editor/Director/Orchestrator). TOC entry §3bis (icône 🎭). Badge 25→28 min + source Microsoft blog.

**E.6 DEP-07 (Évaluation continue)** : §3.5 Définitions canoniques Anthropic (eval, harness, multi-turn, state-modifying) + §3.6 heuristique « eval first » + §3.7 bruit infra vs régression modèle. Badge 17→20 min + 2 sources Anthropic Engineering.

### Lot 6 — Audit final + rapport (en cours)

Ce rapport. Audit final à **0 hit** ✅.

## Audit-global.py — résultats

| Étape | Total hits | Statut |
|---|---|---|
| État de départ (main post v3.9) | **0** | ✅ baseline propre |
| Après Lot A (CU-008 + DEP-02) | **0** | ✅ |
| Après Lot B (CU-020 + CU-024) | **0** | ✅ |
| Après Lot C (création PR-08 + cross-site) | **0** | ✅ |
| Après Lot D (DEP-08 §7bis + PR-05) | **0** | ✅ après correction 3 hits rule 14 |
| Après Lot E (6 patches) | **0** | ✅ après correction 3 hits transitoires |
| Audit final clôture | **0** | ✅ |

Le compteur préalables est correctement passé de 7 à 8 (détection automatique via comptage `pr-*.html`).

## Commits de l'itération

```
87b6a47 feat(v3.10): CU-008 + DEP-02 — encart symétrique RAG vs persistent memory
be6eb6c feat(v3.10): CU-020 + CU-024 — patches réglementaires (AI Act Art. 50 draft guidelines, fiches CNIL, terminologie PA)
287ed14 feat(v3.10): création préalable PR-08 Financer son projet IA en 2026 + impacts cross-site 7→8 préalables
b3fcab5 feat(v3.10): DEP-08 §7bis SBOM IA + PR-05 encarts McKinsey + NIST CAISI + NIST Critical Infrastructure
ba653b5 feat(v3.10): Lot E — marché, maturité, patterns agentiques (6 patches)
+ chore(v3.10): rapport mission v3.10 (ce commit)
```

## Métriques avant/après

| Indicateur | Avant v3.10 | Après v3.10 |
|---|---|---|
| Préalables PR | 7 (pr-01 → pr-07) | **8** (pr-01 → pr-08) |
| Modules CU | 27 | 27 (inchangé) |
| Fiches DEP | 8 | 8 (inchangé) |
| Fiches outils | 99 | 99 (inchangé) |
| Modules touchés par v3.10 | — | **11** (CU-008, CU-020, CU-024, CU-026, DEP-01, DEP-02, DEP-05, DEP-07, DEP-08, PR-01, PR-04, PR-05) + **1 nouveau** (PR-08) |
| Nouvelles sections / h3 ajoutées | — | ~15 (sections complètes ou sous-sections h3) |
| Sources ajoutées (Articles de fond) | — | ~30 (institutionnelles + comptes X qualifiés) |
| Chiffres macro nouveaux | — | **7** (à canoniser via I-D-005 côté RAG) |

## Items I-D-005 transmis (canonisation chiffres macro côté RAG)

7 nouveaux chiffres macro 2026 à canoniser dans `transverses/chiffres-macro-2026.md` (couple 2) :

1. **55 % des TPE-PME utilisent l'IA générative fin 2025** (Bpifrance Le Lab, vs 31 % fin 2024, ×1,8) — Lot E.1
2. **240 M€ Bpifrance capital développement IA 2025** (vs 17 M€ en 2024, ×14) — Lot C + Lot E.1
3. **49 % conversations Copilot M365 = cognitive work** (Microsoft Work Trend Index) — Lot E.1
4. **×15 augmentation YoY agents actifs M365** (Microsoft) — Lot E.1
5. **67/32 organisation/individu** + **2× plus d'impact culture vs mindset** (Microsoft) — Lot E.1
6. **40 % workslop reçu sur dernier mois** (Microsoft) — Lot E.1
7. **Typologie 4 profils dirigeants Bpifrance** (Sceptiques 27 / Bloqués 26 / Expérimentateurs 19 / Innovateurs 28 %) — Lot E.2
8. **RAI maturité moyenne 2,3/5 en 2026** (McKinsey Securing Agentic) — Lot D.2

## Écarts résiduels signalés

**Aucun écart bloquant.**

**Points reportés v3.11 (conformément au brief § 6)** :
- Fiche outil Onyx (recroiser une 2e source institutionnelle avant fichage)
- Actualisation fiche Hermes Agent (Codex runtime + intégrations MCP)
- Pattern A5 « Agents fédérés / persistent memory » dans Architectures (signaux convergents à attendre 6-12 mois)

**Points en surveillance signaux faibles (cf. brief § 7)** :
- 10 pistes maintenues en surveillance non actionnables v3.10 (MCP Server v2, AnythingLLM, MIT NANDA Protocol, x402, etc.)

## Recommandations pour la prochaine itération (v3.11)

1. **Suivi du signal RAG vs persistent memory (Lot A)** : si 3-6 mois après, le pattern se confirme (3 sources → 6+, premiers RetEx PME documentés), produire le pattern A5 « Agents fédérés / persistent memory » dans la page Architectures (passer de 4+1 patterns à 5+1).

2. **Suivi des deadlines juin 2026 du Lot C** : AMI Solutions souveraines IA (5 juin) + AAP Pionniers IA (9 juin). Si nouvelles deadlines AAP ou AMI s'ouvrent, actualiser PR-08 §4.

3. **Suivi du calendrier réglementaire H2 2026 (Lot B)** : applicabilité Art. 50 AI Act (2 août), facturation électronique (1er septembre), watermarking (2 décembre). Actualiser CU-020 et CU-024 à mesure que ces dates passent.

4. **Item I-D-005 côté RAG** : canonisation des 7 chiffres macro listés ci-dessus. À traiter côté couple 2 (Hub IA Plateforme RAG).

5. **Suivi des fiches outils en attente** : Onyx, Hermes Agent. Recroiser sources en juin 2026.

## Validation finale (checklist du brief § 1)

```
☑ RULES v1.6 lu en intégralité avant de commencer (incluant rule 14)
☑ 5 fichiers de matière éditoriale v3.10 lus (Lot A à E)
☑ audit-global.py de départ exécuté → Total hits : 0
☑ Branche feat/v3.10-iteration-majeure créée depuis main à jour
☑ Lot 0 (préalable) réalisé
☑ Lot A (CU-008 + DEP-02) — encart symétrique RAG vs persistent memory
☑ Lot B (CU-020 + CU-024) — 4 patches réglementaires
☑ Lot C (création PR-08) — nouveau préalable + cohérence cross-site 7→8
☑ Lot D (DEP-08 + PR-05) — SBOM IA + McKinsey + NIST CAISI + NIST CI
☑ Lot E (6 patches dispersés) — marché + maturité + patterns agentiques
☑ Lot 6 (audit final + rapport) — ce document
☑ audit-global.py de fin → Total hits : 0
☑ RULES v1.6 → v1.6.1 (glossaire chiffres-clés actualisé 7→8 préalables)
☐ Description de PR à finaliser à la création (pointer vers le brief + ce rapport)
```
