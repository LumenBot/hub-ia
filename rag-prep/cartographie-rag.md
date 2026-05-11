# cartographie-rag.md — Cartographie d'ancrage du vault RAG

**Statut :** v0 (initial, à enrichir au fil des productions MD)
**Dernière mise à jour :** 11 mai 2026
**Maintainer :** Cowork Hub IA Plateforme

> **Rôle :** inventorier, par fichier MD du vault `rag/content/`, les 3-5 **angles thématiques principaux** qu'il couvre. Lu par Cowork avant chaque nouvelle production MD pour éviter les doublons d'indexation (D-019, RetEx couple 1 Q3 §4).

> **Différence avec `veille/cartographie-hub-ia.md` du couple 1** : ce fichier-ci porte sur les **chunks RAG indexés**, pas sur les unités éditoriales du site. Granularité plus fine, focus angles thématiques.

---

## Structure d'une entrée

Pour chaque fichier MD produit, on consigne :

```
### `{nom-fichier}.md` ({type})

**Titre** : ...
**Version** : ...
**Date d'ajout au vault** : YYYY-MM-DD
**Angles thématiques principaux** (3-5 angles) :
1. Angle 1 — courte description
2. Angle 2 — ...
...

**Mots-clés sémantiques** : ...

**Recouvrements connus avec d'autres fichiers** :
- `xxx.md` (angle commun : ...)
- ...
```

---

## Inventaire des fichiers MD du vault

*Vide à l'initialisation. Premières entrées attendues lors du sprint S1 pilote (5 unités).*

---

## Sujets à fort recouvrement attendu (vigilance prioritaire)

D'après la cartographie d'ancrage du couple 1 (`Canaux/Hub-IA/veille/cartographie-hub-ia.md`), les sujets suivants apparaissent dans plusieurs modules sources et nécessitent une vigilance particulière à l'indexation RAG pour éviter les doublons :

1. **RAG vs Fine-tuning** : traité dans CU-008 (orienté décideur) et DEP-02 (orienté technique) — angles complémentaires à préserver
2. **LLM Wiki Karpathy** : CU-008 (présentation) + DEP-02 (comparatif avec RAG hybride) + transverse possible Phase 2
3. **Architectures (4 patterns A1-A4 + hybride)** : page Architectures + nombreux modules CU qui y renvoient
4. **AI Act / RGPD** : CU-020 (module dédié) + encarts dans CU-002, CU-009, CU-010, CU-019, CU-024
5. **Gouvernance des agents** : CU-014 (multi-agents) + CU-026 (gouvernance dédiée) + DEP-05 (observabilité agents)
6. **Build vs Buy** : PR-07 (cadrage transverse) + CU-027 (appli métier)
7. **Compression coûts dev IA-assisté** : CU-027 + PR-07
8. **Chiffres macro** (95 % MIT NANDA, 76 % France Num, 70-95 % Gartner/McKinsey/Deloitte) : présents dans plusieurs modules — gérer par référence unique au glossaire ou à un fichier transverse plutôt que duplication

**Stratégie pour ces sujets à recouvrement** : créer des fichiers `transverse-{slug}.md` qui portent canoniquement l'angle, et faire référencer ces fichiers via wikilinks depuis les modules concernés au lieu de réindexer le même contenu.

---

## Historique des versions

| Version | Date | Modification |
|---|---|---|
| v0 | 11 mai 2026 | Initialisation, structure définie, premiers sujets à recouvrement identifiés |
