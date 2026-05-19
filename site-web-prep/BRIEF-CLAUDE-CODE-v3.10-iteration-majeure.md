# Brief Claude Code — Hub IA Learning Center (passation v3.10)

**Auteur :** Blaise Cavalli — Startup Manager Quai Alpha (Quest for Change)
**Repo :** https://github.com/LumenBot/hub-ia
**Branche cible :** main (via PR `feat/v3.10-iteration-majeure`)
**Itération précédente :** v3.9 (patches techniques + Lot D bonus 307 hyperliens cross-site outils + RULES v1.6 rule 14)
**Nature de cette itération :** ITÉRATION MAJEURE — 5 lots, 14 patches/créations + 1 nouveau préalable PR-08, intégration de 28 pistes accumulées sur 1 semaine de veille intensive.

---

## 0. Contexte court — pourquoi v3.10

L'itération **v3.10** consolide les **28 pistes** accumulées dans `veille/hub-ia/pistes-cumulatives.md` sur les runs des 13-19 mai 2026 (5 inputs Grok + 26 sources web institutionnelles scannées). Itération **majeure** en volume — comparable à v3.8 expansion réglementaire.

**Arbitrage de périmètre** : sur les 28 pistes, **15 sont intégrées en v3.10**, 3 reportées v3.11 (fiche outil Onyx, actualisation fiche Hermes, éventuellement NIST Critical Infrastructure si capacité), 10 conservées en surveillance signaux faibles.

**5 lots organisés** :

| Lot | Périmètre | Volume | Source MD Cowork |
|---|---|---|---|
| **Lot A** | CU-008 + DEP-02 — Encart symétrique « RAG vs persistent memory » (3 signaux convergents, horizon 3-6 mois) | 2 patches encart | `v3.10/lot-A-cu-008-dep-02-persistent-memory.md` |
| **Lot B** | Réglementaire & conformité : CU-020 ×3 (AI Act Art. 50 + fiches CNIL + guide HAS-CNIL) + CU-024 (PDP→PA + calendrier) | 4 patches | `v3.10/lot-B-reglementaire-conformite.md` |
| **Lot C** | **Création nouveau préalable PR-08 « Financer son projet IA en 2026 »** (CIR/CII/CII-IA/JEI/JEII + France 2030 + Bpifrance + 2 deadlines juin 2026) | 1 nouveau préalable complet + impact glossaire chiffres-clés | `v3.10/lot-C-pr-08-financement-ia-2026.md` |
| **Lot D** | Sécurité agentique : DEP-08 §7bis SBOM IA + PR-05 encarts McKinsey + NIST CAISI | 2 patches (1 section + 2 encarts) | `v3.10/lot-D-securite-agentique.md` |
| **Lot E** | Marché, maturité, patterns agentiques : PR-04 actualisation triple + PR-01 4 profils + DEP-01 heuristique + DEP-05 §8.5 failure receipt + §8.5bis harness long-running + CU-026 Frontier Firms + DEP-07 evals | 6 patches | `v3.10/lot-E-marche-maturite-patterns.md` |

**Tu travailles en autonomie.** Cowork (côté Blaise) a produit toute la matière éditoriale en MD structuré dans `site-web-prep/v3.10/`. Ton rôle : transformer cette matière en HTML conforme RULES v1.6 + rule 14 cross-site outils.

**Effort estimé Claude Code** : 12-16 h (équivalent v3.8 expansion réglementaire).

---

## 1. Préalable obligatoire

**AVANT toute action de code**, tu dois :

1. Lire `site-web-prep/RULES-IMPLEMENTATION.md` v1.6 (référentiel actuel, intègre rule I.1 explicitée + rule 14 audit cross-site outils issus de v3.9).
2. Lire les **5 fichiers de matière éditoriale Lot A à E** dans `site-web-prep/v3.10/`.
3. Te référer aux **canoniques HTML** pour chaque module patché :
   - CU-008 / DEP-02 / DEP-08 (Lot A et D)
   - CU-020 / CU-024 (Lot B)
   - PR-07 comme référence canonique structure préalable pour création PR-08 (Lot C)
   - PR-04 / PR-05 / PR-01 / DEP-01 / DEP-05 / DEP-07 / CU-026 (Lot E)
4. **Exécuter `python3 site-web-prep/audit-global.py`** pour confirmer l'état de départ (0 hit attendu).
5. Branche `feat/v3.10-iteration-majeure` créée depuis `main`.

---

## 2. Méthode — 6 lots dans l'ordre

### Lot 0 — Préalable (30 min)

Lectures + audit-global.py de départ.

### Lot 1 — Lot A — RAG vs persistent memory (2 h)

**Source MD** : `site-web-prep/v3.10/lot-A-cu-008-dep-02-persistent-memory.md`

Patches A.1 (CU-008) et A.2 (DEP-02) — symétrie stricte requise (mêmes 3 signaux convergents, même formulation « ce qui ne change pas », même horizon 3-6 mois, mêmes sources).

**Composants HTML** : sous-section h3 dans section existante `#llm-wiki` (CU-008) et `#section-2` (DEP-02). Pas de nouveau composant CSS.

**Livrable Lot 1** : commit `feat(v3.10): CU-008 + DEP-02 — encart symétrique RAG vs persistent memory`.

### Lot 2 — Lot B — Réglementaire & conformité (3 h)

**Source MD** : `site-web-prep/v3.10/lot-B-reglementaire-conformite.md`

4 patches :
- **B.1 CU-020** — AI Act Art. 50 Draft Guidelines (calendrier 3 juin / 2 août / 2 décembre 2026)
- **B.2 CU-020** — Fiches CNIL finales + guide HAS-CNIL santé
- **B.3 CU-020** — Encart de synthèse 3 échéances 2026 (en tête de module ou section AI Act)
- **B.4 CU-024** — Patch terminologique PDP → PA + actualisation calendrier 125 PA / 1er sept 2026/2027

**Composants HTML** : `.alert-block` ou `.callout-info` existants pour les encarts. Aucun nouveau composant.

**Livrable Lot 2** : commit `feat(v3.10): CU-020 + CU-024 — patches réglementaires (AI Act Art. 50 draft guidelines, fiches CNIL, terminologie PA)`.

### Lot 3 — Lot C — Création PR-08 « Financer son projet IA » (4-5 h)

**Source MD** : `site-web-prep/v3.10/lot-C-pr-08-financement-ia-2026.md`

**Création complète** d'un nouveau préalable :
- `prealables/pr-08-financer-projet-ia.html` (création — utiliser PR-07 comme référence canonique structure)
- 8 sections + executive summary + ressources
- 6 dispositifs cartographiés (CIR, CII, CII-IA, JEI, JEII, CICO/C3IV)
- 2 deadlines critiques (5 juin AMI Solutions souveraines, 9 juin AAP Pionniers IA)
- Plan d'action 30 jours

**Impacts cross-site (rule 1.2.x — cohérence numérique cross-site)** :
- `index.html` : meta + hero stats + filter count + section À propos → **7 préalables → 8 préalables**
- `prealables.html` : meta + accroche + footer-cta + **nouvelle card PR-08** ajoutée à la liste
- `README.md` : mention « 8 préalables »
- Footers de tous les modules CU et PR : mention « 8 préalables »
- Méta-descriptions de toutes les pages : mention « 8 préalables »

**Mise à jour RULES** :
- Glossaire § 1.2.3 : **7 → 8 préalables PR**
- Entrée historique à ajouter dans la section versions

**Composants HTML** : réutiliser le pattern de PR-07. Aucun nouveau composant.

**Livrable Lot 3** : commit `feat(v3.10): création nouveau préalable PR-08 Financer son projet IA + impact glossaire 7→8 préalables`.

### Lot 4 — Lot D — Sécurité agentique (2 h)

**Source MD** : `site-web-prep/v3.10/lot-D-securite-agentique.md`

2 patches :
- **D.1 DEP-08** — Nouvelle section 7bis « SBOM IA & supply chain » (entre §7 et `#ressources`)
- **D.2 PR-05** — 2 encarts : D.2.a cybersécurité agentique (McKinsey) + D.2.b NIST CAISI

**Décision arbitrale** : intégrer aussi en encart léger **NIST AI RMF Profile Critical Infrastructure** (avril 2026) dans PR-05 section 3 si capacité — sinon report v3.11. **Mon arbitrage recommandé : intégrer** (patch léger, cohérence avec bloc D, pertinence territoriale PME industrielles vosgiennes).

**Composants HTML** : tableau pour les composants SBOM (`.tech-comparison-table`), encarts existants.

**Livrable Lot 4** : commit `feat(v3.10): DEP-08 §7bis SBOM IA + PR-05 encarts McKinsey + NIST CAISI`.

### Lot 5 — Lot E — Marché, maturité, patterns agentiques (3-4 h)

**Source MD** : `site-web-prep/v3.10/lot-E-marche-maturite-patterns.md`

6 patches :
- **E.1 PR-04** — Actualisation triple section 2bis + encart Transformation Paradox section 5
- **E.2 PR-01** — Encart typologie 4 profils dirigeants Bpifrance
- **E.3 DEP-01** — Heuristique anti-hype architecture (arbre 6 étapes)
- **E.4 DEP-05** — §8.5 Failure receipts & ownership + §8.5bis Effective Harnesses long-running
- **E.5 CU-026** — §3bis Microsoft Frontier Firms 4 patterns de collaboration
- **E.6 DEP-07** — Anthropic Demystifying Evals (terminologie canonique + heuristique « eval first »)

**Composants HTML** : tableaux `.tech-comparison-table` ou équivalent pour les 4 patterns Microsoft et les 4 profils Bpifrance. Pas de nouveau composant.

**Livrable Lot 5** : commit `feat(v3.10): patches marché + maturité + patterns agentiques (PR-04, PR-01, DEP-01, DEP-05, CU-026, DEP-07)`.

### Lot 6 — Audit final + rapport (45 min)

- Exécuter `python3 site-web-prep/audit-global.py` — confirmer **0 hit** (14 règles dont rule 14 cross-site outils)
- Si Lot C a ajouté PR-08 : vérifier la cohérence numérique « 8 préalables » partout (le glossaire RULES + audit-global.py rule sur la cohérence numérique doit passer)
- Vérifier visuellement :
  - Renvois croisés cohérents (pas de lien mort entre les 5 lots qui se cross-référencent dense)
  - TOC à jour sur tous les modules patchés
  - Badges temps de lecture mis à jour
  - Cohérence sections `#ressources` (nouvelles sources ajoutées)
  - Rule 14 : si nouveaux outils mentionnés (Onyx ? — non, pas dans cette itération), bien hyperlinkés
- Produire `RAPPORT-v3.10.md` (synthèse, fichiers touchés, métriques avant/après)

**Livrable Lot 6** : commit `chore(v3.10): audit final + rapport itération`.

---

## 3. Règles à respecter (rappel synthétique)

- **RULES v1.6** : 13 règles essentielles + annexes + rule 14 cross-site outils (issue v3.9). Pas de dérive structurelle (Schéma A `#ressources` final maintenu, 9-blocs squelette modules respecté).
- **Cohérence numérique cross-site** : impact majeur du Lot C (création PR-08) → mise à jour systématique « 7 préalables → 8 préalables » partout.
- **Rule 14 (cross-site outils)** : appliquer aux nouvelles mentions d'outils dans les patches v3.10 (notamment dans PR-08 où plusieurs outils Bpifrance/France 2030 sont mentionnés — vérifier qu'ils n'ont pas de fiche dédiée dans `ressources.html` ; sinon laisser en texte brut).
- **Sources** : tout ajout dans `#ressources` suit le format des sous-rubriques existantes.
- **Audit-global.py** : doit passer à 0 hit avant ET après l'itération.

---

## 4. Coordination inter-canaux

**Item descendant I-D-005 à ouvrir** dans `Canaux/Hub-IA-Plateforme/rag-prep/SYNC-INTER-CANAUX.md` (12 mai 2026 → 19 mai 2026) : canonisation de **~7 nouveaux chiffres macro 2026** côté MD RAG (`transverses/chiffres-macro-2026.md`) — issus directement des Lots D et E.

Chiffres à canoniser :
1. **55 % TPE-PME utilisent l'IA générative fin 2025** (Bpifrance Le Lab, vs 31 % fin 2024, ×1,8) — Lot E.1
2. **240 M€ Bpifrance capital développement IA 2025** (vs 17 M€ en 2024, ×14) — Lot C + E.1
3. **49 % conversations Copilot M365 = cognitive work** (Microsoft Work Trend Index) — Lot E.1
4. **×15 augmentation YoY agents actifs M365** (Microsoft) — Lot E.1
5. **67/32 organisation/individu** + **2× plus d'impact culture vs mindset** (Microsoft) — Lot E.1
6. **40 % workslop reçu sur dernier mois** (Microsoft) — Lot E.1
7. **Typologie 4 profils dirigeants Bpifrance** (Sceptiques 27 / Bloqués 26 / Expérimentateurs 19 / Innovateurs 28 %) — Lot E.2
8. **RAI maturité moyenne 2,3/5 en 2026** (McKinsey Securing Agentic) — Lot D.2

Pas de dépendance bloquante côté HTML.

---

## 5. Effort estimé total

| Lot | Effort estimé | Livrable |
|---|---|---|
| Lot 0 (préalable) | 30 min | Audit-global.py |
| Lot 1 (A — RAG persistent memory) | 2 h | 2 encarts symétriques |
| Lot 2 (B — réglementaire) | 3 h | 4 patches CU-020 + CU-024 |
| Lot 3 (C — PR-08 financement) | 4-5 h | 1 nouveau préalable + impacts cross-site |
| Lot 4 (D — sécurité agentique) | 2 h | 1 section + 2-3 encarts |
| Lot 5 (E — marché + patterns) | 3-4 h | 6 patches dispersés |
| Lot 6 (audit + rapport) | 45 min | Rapport v3.10 |
| **Total** | **15-17 h** | 4 modules patchés Lot B + 2 modules patchés Lot A + 1 nouveau préalable Lot C + 2 modules patchés Lot D + 6 modules patchés Lot E + rapport |

---

## 6. Hors périmètre v3.10 — reporté v3.11

- **Fiche outil Onyx** (recroiser une 2e source institutionnelle avant fichage)
- **Actualisation fiche Hermes Agent** (Codex runtime + intégrations MCP — consolider semaine prochaine)
- **NIST AI RMF Profile Critical Infrastructure** : intégré en encart léger PR-05 si capacité Lot D, sinon v3.11
- **Pattern A5 « Agents fédérés / persistent memory »** dans Architectures (à produire quand le pattern sera consolidé hors signaux faibles, probablement v3.11 ou v3.12)

---

## 7. Hors périmètre — surveillance signaux faibles (non actionnables v3.10)

10 pistes conservées en surveillance dans `pistes-cumulatives.md` :
- MCP Server v2 + observabilité native
- AnythingLLM / PrivateGPT
- LLM-ification of data (MIT Sloan)
- Heuristique délégation IA-assistée (Anthropic)
- MIT NANDA Protocol / Agentic Web
- CNIL IA santé mentale jeunes
- Speculative decoding
- x402 protocole paiement agents
- Pattern PME industrielle FR 45 pers (besoin source institutionnelle)
- Acquisition Anthropic → Stainless

Pistes écartées définitivement : Grok Build CLI (paywall), ERA Living Guidelines UE (hors cible PME tertiaire).

---

*Brief produit par Cowork Hub IA le 19 mai 2026. Itération v3.10 majeure — 5 lots, 14 patches/créations + 1 nouveau préalable PR-08, intégration de 15 pistes sur 28 accumulées. Item I-D-005 transmis en parallèle au couple 2 pour canonisation 8 chiffres macro.*
