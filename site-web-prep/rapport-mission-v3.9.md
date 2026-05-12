# Rapport de mission Claude Code — Itération v3.9

**Date** : mai 2026
**Branche** : `feat/v3.9-patches-techniques`
**Auteur** : Claude Code
**Brief source** : `site-web-prep/v3.9/lot-A-dep-05-production-grade.md`, `lot-B-pr-04-chiffres-macro.md`, `lot-C-dep-03-dep-04-patches.md` + exigence éditoriale supplémentaire (Lot D) ajoutée par l'utilisateur en cours d'itération.

## Synthèse exécutive

Itération éditoriale v3.9 livrée en **5 commits** sur la branche `feat/v3.9-patches-techniques`. Trois patches structurels Cowork → HTML (Lots 1-3 conformes aux briefs), une revue cross-site des renvois outils ajoutée à la roadmap par l'utilisateur (Lot D, 307 liens ajoutés sur 44 fichiers), une mise à jour de `RULES-IMPLEMENTATION.md` v1.6 avec une nouvelle fonction d'audit (rule 14) pour rendre la règle exécutoire dans les itérations futures. `audit-global.py` retourne **`Total hits : 0`** en clôture. Aucun écart résiduel.

## Lots exécutés

### Lot 0 — Préalable

- Lecture intégrale des 3 MD source dans `site-web-prep/v3.9/` (lot-A, lot-B, lot-C).
- Audit baseline : **Total hits : 0** sur la branche `main` à jour ✅.
- Branche `feat/v3.9-patches-techniques` créée depuis `main`.

### Lot 1 — DEP-05 § 8 « Production-grade : 4 patterns industriels 2026 »

Commit : `feat(dep-05): section 8 Production-grade — 4 patterns industriels 2026` (8a65a68)

Nouvelle section 8 insérée dans `deploiement/dep-05-agents-observabilite.html` entre §7 (Plan d'action 30 jours) et `#ressources` :

- **8.1 — 9-layer production architecture** : tableau 9 couches (RAG, semantic cache, memory, query rewriter, router, auto-correcting agents, sécurité 3 niveaux, observabilité par-stage, cost attribution) + heuristique de mise en place en 4 phases.
- **8.2 — Gates machine-checkable TOML** : anti-pattern « overclaimed completeness », exemple TOML complet, implications PME.
- **8.3 — Code Execution with MCP** : tableau comparatif classique vs MCP, réduction tokens 60-80 %, bénéfices observés.
- **8.4 — Agent Skills** : arborescence type d'une Skill, liens conceptuels avec LLM Wiki / multi-agents / gouvernance.

Sources ajoutées dans Articles de fond : @techNmak (9-layer), @wernerk_au (gates TOML), Anthropic Engineering × 2 (Code Execution MCP + Agent Skills).

Renvois croisés : §3 (gates TOML en complément output validation), §4 (frameworks de gates), DEP-03 §3bis, modules Knowledge base RAG / Multi-agents / Gouvernance des agents IA.

TOC entry ajoutée. Badge **20 min → 28 min** de lecture.

### Lot 2 — PR-04 § 2ter « Maturité agentique et bottlenecks 2026 »

Commit : `feat(pr-04): section 2ter Maturité agentique et bottlenecks 2026` (a22e6ea)

Nouvelle section 2ter insérée dans `prealables/pr-04-marche-ia-emploi.html` entre §2bis et §3 :

- Le shift de palier 2025 → 2026 (McKinsey State of AI Trust 2026 : 23 % scalent un agent, 39 % en expérimentation, 74 % risque inexactitude, 72 % risque cybersécurité)
- L'avertissement Gartner — 80 % des entreprises > 1 Md$ ont supprimé des postes sans gain ROI mesuré (callout warn + implication PME : règle des 6 mois de production parallèle)
- La gouvernance comme nouveau différenciateur — 38 % grandes entreprises ont nommé un Chief AI Officer (MIT Sloan Davenport & Bean) + 5 tendances IA 2026
- Synthèse — cartographie 4 paliers de maturité (Découverte ~40 %, Expérimentation ~39 %, Mise en production ~23 %, Industrialisation ~15 %)

3 sources ajoutées dans une nouvelle rubrique « Articles de fond (maturité agentique 2026) ». Transition ajoutée en fin de §2bis. Encart d'auto-positionnement ajouté en tête de §5 (Implications stratégiques). Meta description ajoutée. Badge **10 min → 12 min**.

**Item I-004** à transmettre au couple 2 (Hub IA Plateforme) pour canonisation des 6 chiffres dans `chiffres-macro-2026.md` — **non traité dans cette itération** (relève du couple RAG, brief Cowork à venir).

### Lot 3 — DEP-03 § 3bis + DEP-04 § 4bis

Commit : `feat(dep-03,dep-04): patches harness engineering + SLM 1B-8B 2026` (ea8bd91)

**DEP-03 § 3bis « Du context au harness engineering »** :
- Shift conceptuel prompt eng → context eng → harness eng (mai 2026)
- Checklist 8 leviers du harness (caching, KV cache, speculative vs quantization, LLM-as-judge, cost attribution, guardrails & loop budgets, model routing, graceful fallback)
- Lien avec pattern Code Execution with MCP (réduction tokens 60-80 %) renvoyant vers DEP-05 §8.3 et §8.1
- Takeaway 5 ajouté dans l'exec summary, étape 4 « Synthèse harness » ajoutée dans Plan d'action 30 jours
- Sources : @akshay_pachaar, Anthropic Engineering — Effective harnesses
- Badge **18 min → 21 min**, meta description mise à jour

**DEP-04 § 4bis « SLM 1B-8B en 2026 »** :
- Heuristique 7-10 modèles SLM fine-tunés avant tout investissement GPU
- Stack pratique sans GPU local (Colab Pro / A100 cloud / Unsloth / SFT / GRPO-DPO-PPO / LoRA-QLoRA / Quantization / llama.cpp / KV cache)
- ROI métier 50 K€+ pour modèles personnalisés
- Encart prospectif « Expert Language Models (ELMs) » comme signal faible 2027
- Takeaway 5 ajouté dans l'exec summary, encart « règle de discipline budgétaire » ajouté dans Plan 60 jours
- Source : @cjzafir
- Badge **15 min → 19 min**, meta description mise à jour

**PR-07 (Build vs Buy)** : encart « Une troisième voie en 2026 — le fine-tuning SLM » ajouté en fin de section 4, renvoyant vers DEP-04 §4bis.

### Lot D (ajouté par l'utilisateur) — Revue cross-site renvois outils

Commit : `feat(cross-site): hyperlink toutes les mentions d'outils vers ressources.html` (a6f6373)

**Demande utilisateur** (verbatim) : *« au sein des modules existants, et de l'ensemble du contenu du hub, toute mention d'un outil référencé dans la page ressource doit être adossée à un lien hypertexte renvoyé vers la section associée sur la page ressources. »*

**Périmètre traité** :
- 99 outils du catalogue `ressources.html` (extraction automatique des `tool-card` avec leurs ancres)
- Pour chaque page du Hub (modules, préalables, déploiement, architectures, index), wrappage de la **première mention non-liée** de chaque outil dans un `<a href=".../ressources.html#anchor" class="tool-link">Nom</a>`
- **307 liens ajoutés sur 44 fichiers** (un seul commit, idempotent)

**Règles d'application** :
- Une seule occurrence linkée par fichier par outil (la première) — évite la surcharge visuelle
- Aliases longs traités en priorité (Mistral Large avant Mistral, Claude Code avant Claude) avec **consumed-ranges** pour éviter les overlaps
- Zones protégées : `<a>`, `<code>`, `<pre>`, `<script>`, `<style>`, `<svg>` complet, `<aside class="module-toc">`, attributs HTML
- Outils ambigus (homographes) exclus : `Make`, `v0`, `Comet`, `Operator`, `Atlas`, `Crayon`, `Whisper` — décision manuelle au cas par cas
- Script idempotent et ré-exécutable : `site-web-prep/link-tools-to-resources.py`

**Bug détecté et corrigé en cours d'itération** : première version du script avait un bug d'overlap (wrappait `Claude` à l'intérieur de `Claude Code` déjà wrappé). Détecté par grep `</a>/ressources` sur 7 fichiers post-exécution. Revert via `git checkout -- .`, script corrigé avec tracking de consumed-ranges, ré-exécution propre. 0 lien malformé en clôture.

**Correctif bonus** : 2 ancres brisées détectées dans `deploiement/dep-05-agents-observabilite.html` (`#langsmith` et `#phoenix` introduits par erreur au Lot 1 — ces outils n'ont pas de fiche dédiée dans `ressources.html`). Suppression des liens, conservation des mentions en texte brut.

### Lot D bis — Documentation de la règle dans RULES v1.6

Commit : `docs(rules): explicite I.1 + ajoute audit rule 14 cross-site outils v3.9` (b408624)

Pour rendre la règle pérenne dans les itérations futures :

- **`RULES-IMPLEMENTATION.md` v1.6** :
  - Règle I.1 enrichie de précisions opérationnelles (première occurrence non-liée par page, aliases acceptés avec exemples, zones à exclure, outils homographes)
  - Référence au script idempotent et à la fonction d'audit
  - Mapping audit-global.py mis à jour (13 → 14 règles)
  - Checklist commit/PR enrichie d'une ligne dédiée à la rule 14
  - Annexe Section 4.I.2 (nouveau) : mise en pratique avec pattern HTML attendu, aliases, outils homographes, workflow d'application

- **`audit-global.py`** :
  - Nouvelle fonction `audit_tool_link_first_mention()` (rule 14)
  - Lit `ressources.html`, extrait les 99 ancres tool-card, vérifie pour chaque page que toute mention d'un outil cité a au moins un lien vers sa fiche (sinon : hit)
  - Outils ambigus ignorés
  - Zones protégées identiques au linker
  - Test de non-régression : audit déclenche bien 1 hit quand on retire tous les liens `#claude` d'une page citant l'outil ✅

Conformément au principe v1.6 « toute nouvelle règle structurelle ajoutée → fonction d'audit dans `audit-global.py` dans la même PR ».

### Lot 4 — Audit final + rapport

Audit final : **Total hits : 0** ✅

## Audit-global.py — résultats

| Étape | Total hits | Statut |
|---|---|---|
| État de départ (`main` post-refonte RULES v1.6) | **0** | ✅ baseline propre |
| Après Lot 1 (DEP-05 §8) | **0** | ✅ |
| Après Lot 2 (PR-04 §2ter) | **0** | ✅ |
| Après Lot 3 (DEP-03 §3bis + DEP-04 §4bis + PR-07) | **0** | ✅ |
| Après Lot D (307 liens cross-site) | **0** | ✅ |
| Après Lot D bis (rule 14 ajoutée) | **0** | ✅ clôture conforme |

## Commits de l'itération

```
8a65a68 feat(dep-05): section 8 Production-grade — 4 patterns industriels 2026
a22e6ea feat(pr-04): section 2ter Maturité agentique et bottlenecks 2026
ea8bd91 feat(dep-03,dep-04): patches harness engineering + SLM 1B-8B 2026
a6f6373 feat(cross-site): hyperlink toutes les mentions d'outils vers ressources.html
b408624 docs(rules): explicite I.1 + ajoute audit rule 14 cross-site outils v3.9
```

## Écarts résiduels signalés

**Aucun écart bloquant.**

**Points à transmettre / suivre** :

1. **Item I-004 (canonisation des chiffres macro 2026)** : non traité dans cette itération HTML, à inclure dans le brief de passation au couple 2 (Hub IA Plateforme) côté RAG. Liste des 6 chiffres dans `lot-B-pr-04-chiffres-macro.md`.

2. **Outils ambigus du Lot D** : les 7 outils homographes (Make, v0, Comet, Operator, Atlas, Crayon, Whisper) ne sont pas automatiquement linkés ni flaggés par la rule 14. Une revue manuelle peut être proposée dans une itération éditoriale ultérieure si l'utilisateur souhaite forcer le wrappage dans des contextes spécifiques (à arbitrer).

3. **Frameworks d'évaluation cités sans fiche dédiée** : `LangSmith`, `Phoenix`, `Langfuse`, `Comet Opik`, `Guardrails AI`, `instructor`, `outlines` n'ont pas (encore) de `tool-card` dans `ressources.html`. À évaluer pour une éventuelle extension du catalogue (hors scope v3.9).

## Recommandations pour la prochaine itération

1. **Brief Cowork item I-004** : intégrer les 6 chiffres macro dans `chiffres-macro-2026.md` côté RAG dans le prochain sprint couple 2.

2. **Revue manuelle des outils homographes** : décision éditoriale à prendre sur les 7 outils ambigus (Make, v0, Comet, Operator, Atlas, Crayon, Whisper). Soit on accepte qu'ils restent non-linkés (simplicité), soit on les linke manuellement au cas par cas dans les contextes où ils désignent bien l'outil.

3. **Surveiller l'efficacité de la rule 14** : si une nouvelle itération éditoriale introduit un nouveau module qui cite un outil sans le linker, la rule 14 le flaggera au commit. Si le hit est trop bruyant (par exemple sur des mentions très indirectes), affiner le pattern.

4. **Cycle de fiches outils à ajouter** : `LangSmith`, `Phoenix`, `Langfuse`, `Comet Opik`, `Guardrails AI` mériteraient une fiche dédiée vu la fréquence de citation dans les modules DEP. À budgéter dans une itération éditoriale dédiée ressources (v3.10 ?).

## Validation finale

```
☑ 3 MD source du Lot v3.9 lus en intégralité.
☑ audit-global.py de départ exécuté → 0 hit.
☑ Lot 1 (DEP-05 §8) — 4 sous-sections complètes + sources + renvois + badge.
☑ Lot 2 (PR-04 §2ter) — 4 sous-parties + sources + tableau 4 paliers + meta desc.
☑ Lot 3 (DEP-03 §3bis + DEP-04 §4bis) — 8 leviers harness + SLM 1B-8B + ELMs + cross-ref PR-07.
☑ Lot D (cross-site outils) — 307 liens ajoutés sur 44 fichiers, 0 ancre brisée, 0 lien malformé.
☑ Lot D bis (RULES + audit) — règle I.1 explicitée, rule 14 ajoutée à audit-global.py.
☑ audit-global.py de fin exécuté → 0 hit.
☑ Tous les commits poussent un message structuré + lien session.
☑ Rapport mission rapport-mission-v3.9.md produit.
```
