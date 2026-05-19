# Brief Claude Code — Hub IA Learning Center (passation v3.11)

**Auteur :** Blaise Cavalli — Startup Manager Quai Alpha (Quest for Change)
**Repo :** https://github.com/LumenBot/hub-ia
**Branche cible :** main (via PR `feat/v3.11-ecosysteme-claude-chiffres-macro`)
**Itération précédente :** v3.10 majeure (5 lots, 14 patches + nouveau préalable PR-08, RULES v1.6.1)
**Nature de cette itération :** ITÉRATION MOYENNE — 3 lots, 5 patches chiffres macro + nouvelle catégorie ressources écosystème Claude (10 fiches) + enrichissement encart RAG/persistent memory v3.10. Plus légère que v3.10, plus structurante que v3.9.

---

## 0. Contexte court — pourquoi v3.11

L'itération **v3.11** combine 3 objectifs :

1. **Combler la dette de chiffres macro 2026** identifiée à la lecture du Stanford AI Index Report 2026 (425 pages) + McKinsey State of AI 2025 (nov. 2025, 30 pages).
2. **Documenter structurellement l'écosystème agentique Claude/Anthropic** (intuition Blaise validée + signal capté par le nouveau Grok screener 6).
3. **Enrichir l'encart RAG vs persistent memory** v3.10 Lot A avec la 4ème confirmation convergente (agentmemory + benchmarks publiés chiffrés).

**Arbitrage de périmètre validé** : option resserrée pour le Lot B (10 fiches, pas 15+) — extension v3.12 si feedback positif.

**3 lots organisés** :

| Lot | Périmètre | Volume | Source MD Cowork |
|---|---|---|---|
| **Lot A** | 5 patches chiffres macro Stanford + McKinsey : PR-04 (2 sous-encarts), PR-01 (high performers), CU-027 (SWE-bench + emploi devs juniors), DEP-08/PR-05 (362 incidents), DEP-01 (jagged frontier) | 5 patches dispersés | `v3.11/lot-A-chiffres-macro-stanford-mckinsey.md` |
| **Lot B** | Création nouvelle catégorie `ressources.html` « Stack agentique Claude / Anthropic » : 10 fiches en 3 sous-catégories (Frameworks ECC + MCP servers + actualisation Hermes) | 1 nouvelle catégorie + 5-7 nouvelles fiches outils (selon dédoublonnage) + 1 actualisation | `v3.11/lot-B-categorie-stack-agentique-claude.md` |
| **Lot D** | Enrichissement encarts v3.10 Lot A (CU-008 + DEP-02) : passage 3 → 4 signaux convergents + benchmarks agentmemory chiffrés + cross-links vers Lot B | 2 patches d'enrichissement | `v3.11/lot-D-enrichissement-rag-persistent-memory.md` |

**Note** : pas de Lot C dans v3.11 (Onyx et Hermes Agent intégrés dans Lot B, NIST Critical Infrastructure déjà fait en v3.10 par Claude Code).

**Tu travailles en autonomie.** Cowork (côté Blaise) a produit toute la matière éditoriale en MD structuré dans `site-web-prep/v3.11/`. Ton rôle : transformer cette matière en HTML conforme RULES v1.6.1 (rule 14 cross-site outils active).

**Effort estimé Claude Code** : 8-11 h (itération moyenne).

---

## 1. Préalable obligatoire

**AVANT toute action de code**, tu dois :

1. Lire `site-web-prep/RULES-IMPLEMENTATION.md` v1.6.1 (référentiel actuel, intègre les évolutions post-v3.10 : 8 préalables, glossaire actualisé).
2. Lire les **3 fichiers de matière éditoriale Lot A, B, D** dans `site-web-prep/v3.11/`.
3. Te référer aux **canoniques HTML** pour chaque module patché :
   - PR-04 / PR-01 / CU-027 / DEP-08 / PR-05 / DEP-01 (Lot A)
   - `ressources.html` (Lot B — état actuel à analyser pour décider dédoublonnage Claude Code / Cursor / Windsurf / Hermes)
   - CU-008 / DEP-02 (Lot D — sous-sections `#llm-wiki-shelf-life` et `#section-2bis` créées en v3.10 Lot A)
4. **Exécuter `python3 site-web-prep/audit-global.py`** pour confirmer l'état de départ (0 hit attendu, 14 règles).
5. Branche `feat/v3.11-ecosysteme-claude-chiffres-macro` créée depuis `main` à jour.

---

## 2. Méthode — 4 lots dans l'ordre

### Lot 0 — Préalable (20 min)

Lectures + audit-global.py de départ.

### Lot 1 — Lot A — Patches chiffres macro Stanford + McKinsey (2-3 h)

**Source MD** : `site-web-prep/v3.11/lot-A-chiffres-macro-stanford-mckinsey.md`

5 patches dispersés :
- **A.1 PR-04** — 2 sous-encarts dans section 2bis (McKinsey 88/39/23-39/32-43-13 + Stanford 53/172 Md$/88/4 sur 5 étudiants)
- **A.2 PR-01** — encart « high performers » (6 % + 3,6× transformation + 3× workflow redesign + citation McKinsey textuelle)
- **A.3 CU-027** — encart « SWE-bench 60→100 % » + encart « productivité 14-26 % + emploi devs juniors -20 % » dans section 1bis
- **A.4 DEP-08 + PR-05** — encart symétrique « 362 incidents documentés » (+55 % vs 2024)
- **A.5 DEP-01** — encart « Jagged Frontier » Stanford (Gemini IMO médaille d'or vs horloge analogique 50,1 %, OSWorld 12→66 %)

**Composants HTML** : encarts existants (`.callout-info`, `.alert-block`, `.tech-comparison-table` selon besoin). Aucun nouveau composant.

**Livrable Lot 1** : commit `feat(v3.11): Lot A — patches chiffres macro Stanford + McKinsey (5 modules)`.

### Lot 2 — Lot B — Nouvelle catégorie ressources « Stack agentique Claude/Anthropic » (4-5 h)

**Source MD** : `site-web-prep/v3.11/lot-B-categorie-stack-agentique-claude.md`

Création complète d'une nouvelle catégorie dans `ressources.html` :
- 3 sous-catégories : Frameworks ECC (7 fiches) + MCP servers (2 fiches) + Actualisation Hermes (1 fiche)
- Label explicite « niveau prestataire / expert » en intro de catégorie
- **Décision arbitrale à prendre par Claude Code** : pour Claude Code / Cursor / Windsurf / Hermes Agent qui existent déjà ailleurs dans `ressources.html`, retenir l'**option 3 du MD source** (conserver dans catégorie d'origine + liens transversaux depuis nouvelle catégorie) — évite duplication, préserve cohérence numérique RULES

**Impacts cross-site (rule 1.2.x — cohérence numérique)** :
- Glossaire RULES § 1.2.3 : 99 → **~105 fiches outils** (selon dédoublonnage)
- `index.html` : meta + hero stats + filter count + section À propos
- `ressources.html` : badge + accroche + exec-stats + intitulés
- `README.md` : mention compte fiches
- Méta-descriptions de toutes les pages

**Mise à jour RULES** :
- Glossaire § 1.2.3 actualisé
- Entrée historique « v1.6.2 — itération v3.11 »

**Composants HTML** : pattern de catégorie existant dans `ressources.html` (`.tool-card`, `.resources-cat`). Aucun nouveau composant. Vérifier que la **rule 14 cross-site outils** ne génère pas de hits sur les nouvelles fiches (les 10 nouvelles fiches sont les ancres canoniques — pas de hyperlink à faire vers elles depuis les modules en eux-mêmes, c'est l'inverse).

**Livrable Lot 2** : commit `feat(v3.11): Lot B — nouvelle catégorie ressources Stack agentique Claude/Anthropic (10 fiches) + impact glossaire 99→~105 fiches outils`.

### Lot 3 — Lot D — Enrichissement encarts RAG vs persistent memory (1-1,5 h)

**Source MD** : `site-web-prep/v3.11/lot-D-enrichissement-rag-persistent-memory.md`

Patches symétriques sur les encarts créés en **v3.10 Lot A** :
- **D.1 CU-008** — actualiser sous-section `#llm-wiki-shelf-life` : passer de 3 à 4 signaux convergents + ajouter bloc agentmemory avec benchmarks chiffrés (95,2 % r@5 vs 86,2 % BM25, coût token ÷ 100+) + mention claude-smart en note + cross-links vers fiches agentmemory et claude-smart du Lot B
- **D.2 DEP-02** — actualiser sous-section `#section-2bis` : même traitement symétrique côté production + actualiser tableau de décision RAG ligne « agent avec mémoire conversationnelle »

**Cohérence cross-modules** : strictement symétrique (mêmes 4 signaux, mêmes chiffres, mêmes sources).

**Composants HTML** : pas de nouveau, juste enrichissement de sections existantes.

**Livrable Lot 3** : commit `feat(v3.11): Lot D — enrichissement encarts RAG vs persistent memory (CU-008 + DEP-02) avec agentmemory benchmarks`.

### Lot 4 — Audit final + rapport (45 min)

- Exécuter `python3 site-web-prep/audit-global.py` — confirmer **0 hit** (14 règles)
- Vérifier visuellement :
  - Cohérence numérique 99 → ~105 fiches outils partout (le glossaire RULES + audit-global.py doit passer)
  - Rule 14 cross-site outils : les 10 nouvelles fiches Lot B sont les **ancres canoniques** — vérifier qu'elles ne génèrent pas de hits à elles-mêmes
  - Tous les cross-links créés ou modifiés sont valides (pas de lien mort entre Lots A, B, D)
  - Badges temps de lecture mis à jour sur les modules patchés
- Produire `RAPPORT-v3.11.md` (synthèse, fichiers touchés, métriques avant/après)

**Livrable Lot 4** : commit `chore(v3.11): audit final + rapport itération`.

---

## 3. Règles à respecter (rappel synthétique)

- **RULES v1.6.1** : 13 règles essentielles + annexes + rule 14 cross-site outils. Pas de dérive structurelle.
- **Cohérence numérique cross-site** : impact du Lot B (création fiches outils) → mise à jour systématique « 99 → ~105 fiches outils ».
- **Rule 14 (cross-site outils)** : appliquer aux nouvelles mentions d'outils dans les patches Lot A et Lot D — notamment les mentions agentmemory et claude-smart dans CU-008/DEP-02 doivent linker vers les nouvelles fiches du Lot B (cohérence rule I.1).
- **Sources** : tout ajout dans `#ressources` suit le format existant. Cohérence des liens GitHub en URL complète.
- **Audit-global.py** : doit passer à 0 hit avant ET après l'itération.

---

## 4. Coordination inter-canaux

**Item descendant I-D-007 à ouvrir** dans `Canaux/Hub-IA-Plateforme/rag-prep/SYNC-INTER-CANAUX.md` : canonisation de **~12 nouveaux chiffres macro Stanford + McKinsey** côté MD RAG.

Chiffres à canoniser :
1. **88 % organisations utilisent régulièrement l'IA** (McKinsey State of AI 2025)
2. **39 % rapportent un EBIT impact attribuable à l'IA** (la plupart <5 %) — McKinsey
3. **6 % « AI high performers »** (EBIT >5 % + valeur significative) — McKinsey
4. **3,6× plus de transformation IA** chez high performers vs autres — McKinsey
5. **3× plus de workflow redesign** chez high performers — McKinsey
6. **32 / 43 / 13 %** anticipation employeur emploi (baisse / stable / hausse) — McKinsey
7. **53 % adoption population GenAI en 3 ans** (plus rapide que PC ou internet) — Stanford AI Index 2026
8. **172 Md$ / an** valeur estimée GenAI pour consommateurs US — Stanford
9. **SWE-bench Verified : 60 → ~100 % human baseline** en un an — Stanford
10. **OSWorld : 12 → 66 % task success** en un an — Stanford
11. **362 incidents IA documentés en 2025** (+55 % vs 2024) — Stanford
12. **Productivité 14-26 % en customer support et software dev** — Stanford (avec note : emploi devs US 22-25 ans -20 % depuis 2024)

Articulation avec items en attente côté couple 2 : **I-D-003** (6 chiffres v3.9 McKinsey/Gartner/MIT) + **I-D-005** (2 chiffres CU-027 Kimi/Opus) + **I-D-006** (8 chiffres v3.10 Bpifrance/Microsoft/McKinsey) + **I-D-007** (12 chiffres v3.11 Stanford/McKinsey) = **28 chiffres macro** à canoniser cumulés depuis v3.8 si pas encore traités. Cohérent à intégrer dans un même bump éditorial.

Pas de dépendance bloquante côté HTML v3.11.

---

## 5. Effort estimé total

| Lot | Effort estimé | Livrable |
|---|---|---|
| Lot 0 (préalable) | 20 min | Audit-global.py |
| Lot 1 (A — chiffres macro) | 2-3 h | 5 patches dispersés |
| Lot 2 (B — catégorie écosystème Claude) | 4-5 h | 1 nouvelle catégorie + 5-7 nouvelles fiches |
| Lot 3 (D — enrichissement RAG/persistent memory) | 1-1,5 h | 2 patches d'enrichissement |
| Lot 4 (audit + rapport) | 45 min | Rapport v3.11 |
| **Total** | **8-11 h** | 6 modules patchés (Lot A) + nouvelle catégorie ressources (Lot B) + 2 enrichissements (Lot D) + rapport |

---

## 6. Hors périmètre v3.11 — surveillance v3.12+

- **CU-028 « Redessiner ses workflows pour l'IA »** (suggéré post-lecture McKinsey — facteur de succès n°1)
- **CU-029 « L'écosystème agentique Claude/Anthropic 2026 »** (à arbitrer 3 mois post-publication Lot B selon feedback visiteurs)
- **Pattern A5 « Agents fédérés / persistent memory »** dans `architectures.html` (laisser mûrir 6 mois)
- **Fiches outils étendues** : LangSmith / Phoenix / Langfuse / BMad Method / Lyra-Dev (option élargie reportée v3.12)
- **Signaux faibles à recroiser** : git-as-memory, SafeFlo MCP, MCP Server v2, AnythingLLM/PrivateGPT

---

*Brief produit par Cowork Hub IA le 19 mai 2026. Itération v3.11 moyenne — 3 lots, 5 patches dispersés + 1 nouvelle catégorie + 2 enrichissements. Item I-D-007 transmis en parallèle au couple 2 pour canonisation 12 chiffres macro.*
