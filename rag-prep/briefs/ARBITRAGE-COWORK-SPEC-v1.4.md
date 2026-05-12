# Arbitrage Cowork — 3 propositions SPEC v1.3 → v1.4

**Source :** RAPPORT-CC-S2.1 §5 (Claude Code Plateforme post-audit v2)
**Date d'arbitrage :** 12 mai 2026
**Statut :** draft Cowork — à valider Blaise avant production SPEC v1.4
**Reprise prévue :** post-itération couple 1 (en pause actuellement)

---

## Synthèse rapide

3 propositions à arbitrer, **toutes recommandées en acceptation** (avec une nuance sur P2 — à acter pour audit v3 et non v2 vu que R5 v2 est déjà déployée).

| # | Proposition | Verdict Cowork | Action |
|---|---|---|---|
| P1 | Codifier R6 warning par défaut dans SPEC §R6 | ✅ Accepter | Intégrer dans SPEC v1.4 |
| P2 | R5 v3 « première occurrence seulement » | ✅ Accepter mais reporter en audit v3 | Documenter en roadmap v3, pas en SPEC v1.4 |
| P3 | Documenter `--strict-future` et `--strict-r6` dans SPEC §Validation | ✅ Accepter | Intégrer dans SPEC v1.4 |

---

## P1 — Codifier R6 warning par défaut

**Rappel contexte (RAPPORT §5) :** R6 v1 signalait tout chiffre orphelin en erreur. Le vault contient ~42 chiffres pédagogiques que Cowork a explicitement arbitrés comme acceptables en étape B post-S1bis (catégorie D du rapport audit-report-s1bis). R6 v2 émet warning par défaut, le strict est rétabli via `--strict-r6`.

**Verdict Cowork** : ✅ **Accepter.**

**Justification :**
- C'est la convention que Claude Code Plateforme a déjà appliquée empiriquement en S2.1 sur la base des arbitrages Cowork étape B post-S1bis
- Sans cette codification, on garde un décalage entre la SPEC formelle (R6 strict) et l'implémentation effective (R6 warning par défaut)
- Le mode strict reste disponible via `--strict-r6` pour la CI durcie post-vague 3 — flexibilité préservée
- Anti-pattern AP-3 (édulcoration éléments contextuels) reste documenté à part — R6 warning ne tolère pas l'édulcoration sémantique, juste les chiffres pédagogiques sans source primaire

**Formulation suggérée pour SPEC v1.4 §R6** (à insérer en fin de R6) :

> **v1.4 — Mode par défaut :** R6 signale par défaut un **warning** (non bloquant en CI standard) pour les chiffres orphelins, afin de tolérer les heuristiques pédagogiques internes au Hub (impacts relatifs documentés par RetEx interne, fourchettes techniques sans source primaire publique). Le **mode strict** (erreur bloquante) est activable via `audit-md-rag.py --strict-r6` quand Cowork veut durcir la CI (typiquement post-vague 3 ou pour audit ponctuel pré-publication).

---

## P2 — R5 v3 « première occurrence seulement »

**Rappel contexte (RAPPORT §5) :** R5 v2 signale 51 warnings — parfois sur des termes du glossaire utilisés plusieurs fois dans un même module. Un texte saturé de wikilinks devient illisible côté lecture humaine (or les MD doivent aussi rester potentiellement lisibles).

**Proposition CC :** R5 v3 — ne signaler que la **première occurrence** d'un terme glossaire dans un module (encourage le wikilink initial puis citation en clair).

**Verdict Cowork** : ✅ **Accepter, mais reporter à audit v3** (pas SPEC v1.4).

**Justification du report :**
- R5 v2 est implémentée et opérationnelle dans audit v2 (51 warnings actuels, non bloquants)
- Changer le comportement de R5 maintenant casserait potentiellement des tests automatisés écrits en S2.1
- Mieux : laisser R5 v2 tourner pendant le sprint S2.2 et S2.3 pour collecter des données réelles sur la valeur du signal
- Si les 51 warnings R5 ne révèlent que des cas « pédagogiquement justifiés », alors basculer en R5 v3 lors d'un futur audit v3 (post-vague 3 ou Phase 2)
- Documentation dès SPEC v1.4 : inscrire R5 v3 en roadmap, sans changer R5 v2

**Formulation suggérée pour SPEC v1.4 §R5 (note de roadmap)** :

> **Roadmap audit v3 — R5 v3 « première occurrence seulement »** : R5 v2 actuelle signale toute occurrence d'un terme glossaire utilisé en clair (51 warnings observés en S2.1). Évolution prévue en audit v3 : ne signaler que la première occurrence par fichier MD, pour encourager le wikilink initial sans saturer le texte de wikilinks répétés. Mise en œuvre conditionnelle à un retour utilisateur post-vague 3 confirmant le besoin.

---

## P3 — Documenter `--strict-future` et `--strict-r6` dans SPEC

**Rappel contexte (RAPPORT §5) :** Les options `--strict-future` (R4 whitelist → erreur) et `--strict-r6` (R6 → erreur) sont implémentées dans audit v2 mais pas mentionnées dans SPEC v1.3.

**Verdict Cowork** : ✅ **Accepter.**

**Justification :**
- Discipline de cohérence SPEC ↔ implémentation : toute option d'audit doit être documentée dans SPEC
- Convention « nouvelle règle = nouvelle fonction d'audit » (D-023) implique « nouvelle option d'audit = nouvelle ligne de doc dans SPEC »
- Ces options sont des leviers de gouvernance (CI souple vs CI durcie) — leur usage attendu doit être documenté

**Formulation suggérée pour SPEC v1.4 §Validation (en complément du point 11-13 actuels)** :

> **Options d'audit v2 disponibles** (cumulables) :
> - `--strict-future` : transforme les warnings R4 « wikilink vers code whitelisté » en erreurs bloquantes. À activer en CI quand la whitelist doit être maintenue stricte (typiquement post-vague 3 ou pré-publication).
> - `--strict-r6` : transforme les warnings R6 « chiffre orphelin » en erreurs bloquantes. À activer pour un audit éditorial ponctuel ou en CI durcie.
> 
> Combinaison courante : `audit-md-rag.py --strict-future --strict-r6` pour audit strict pré-publication.

---

## Plan d'intégration SPEC v1.4

Une fois ces 3 arbitrages validés par Blaise, production de SPEC v1.4 :

1. Bump SPEC v1.3 → v1.4
2. Insertion du paragraphe « v1.4 — Mode par défaut » en fin de §R6 (P1)
3. Insertion de la note roadmap « audit v3 — R5 v3 » en fin de §R5 (P2)
4. Extension de la section §Validation avec les 2 options documentées (P3)
5. Bump tableau « Historique des versions » avec ligne v1.4

Effort estimé : 30-45 min Cowork.

**À faire** : post-itération couple 1, en ouverture du sprint S2.2.

---

## Question pour Blaise

Tu valides ces 3 arbitrages en bloc (P1 ✅, P2 ✅ reporté audit v3, P3 ✅) ? Ou ajustement sur l'un d'eux ?

Une fois validé, je produirai SPEC v1.4 à la reprise post-itération couple 1, en même temps que je transmettrai le brief CC-S2.2 à Claude Code Plateforme.

---

*Mini-doc d'arbitrage Cowork produit le 12 mai 2026, en attente de validation Blaise. Pas d'intégration immédiate (pause sprint S2 jusqu'à fin itération couple 1).*
