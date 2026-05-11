# SPEC-MD-POUR-RAG.md — Cahier des charges des fichiers MD pour le RAG

**Statut :** v1 minimaliste (8 règles essentielles)
**Dernière mise à jour :** 11 mai 2026
**Maintainer :** Cowork Hub IA Plateforme

> **Rôle :** spécifier le **format technique** des fichiers MD du vault `rag/content/`. Ce fichier traite des conventions concrètes (frontmatter, chunking, naming, wikilinks). Pour la stratégie de retranscription, voir `STRATEGIE-MD-RAG.md`.

> **Principe directeur (RetEx couple 1 Q3 §3) :** démarrer minimaliste, enrichir au fil des écarts détectés par audit-md-rag.py. Cette v1 contient 8 règles essentielles. Les règles ajoutées en v2+ proviendront des apprentissages du pilote S1.

> **Règle de gouvernance (D-023, issue retour couple 1 sur I-001) :** toute nouvelle règle ajoutée à ce fichier au-delà de la v1 doit s'accompagner, **dans le même commit**, d'une fonction de validation correspondante dans `audit-md-rag.py`. Sinon, la règle bascule en « anti-pattern documenté » (recommandation forte mais non opposable), pas en règle stricte. Pattern aligné sur K.1 de RULES-IMPLEMENTATION v1.6 du couple 1.

---

## Règle 1 — Frontmatter YAML obligatoire

Tout fichier MD du vault DOIT contenir un frontmatter YAML en tête, avec ces 10 champs canoniques :

```yaml
---
code: cu-008
titre: "Knowledge base interne (RAG)"
type: module-cu        # valeurs autorisées : module-cu | prealable-pr | deploiement-dep | architecture | fiche-outil | transverse
axe: B                 # A (Productivité) | B (Décision) | C (Création) | D (Croissance) | E (Industrie) | agentique | transverse
niveau: 3              # 1 | 2 | 3 | 4
tags: [rag, llm-wiki, retrieval, embeddings, vector-db]
version: 3.8.2         # version Hub IA d'origine du contenu
last_updated: 2026-05-11
glosaire_termes: [rag, fine-tuning, embedding, vector-db, llm-wiki]
derives: ["[[dep-02]]", "[[pr-07]]"]  # wikilinks vers modules apparentés
public_cible: [dirigeant, ops, r&d]   # valeurs autorisées : dirigeant | ops | r&d | tech | transverse
---
```

**Validation** : audit-md-rag.py vérifie présence et conformité de chaque champ.

---

## Règle 2 — Structure : H1 unique, sections H2 sémantiquement autonomes

- **Un seul H1** par fichier, identique au champ `titre` du frontmatter (sans guillemets)
- **Sections H2** : chaque section est lisible isolément, hors contexte du reste du fichier
- **H3 facultatif** : utilisé si une section H2 dépasse 800 tokens et doit être subdivisée
- **Pas de H4+** dans cette v1 : si besoin de granularité plus fine, refactoriser en deux H2 distincts

**Critère d'autonomie sémantique** : si on coupe une section H2 et qu'on la donne seule à un LLM avec la question type associée, le LLM doit pouvoir produire une réponse pertinente sans avoir besoin du reste du fichier.

**Anti-pattern à éviter** : « comme vu plus haut », « contrairement à la section précédente », « cette procédure complète la suivante » — ces formulations rendent la section dépendante du fichier entier.

---

## Règle 3 — Convention de chunking

- **Chunk principal** : une section H2 = un chunk, longueur cible **400-700 tokens** (~ 250-500 mots)
- **Subdivision** : si une section dépasse **800 tokens**, la subdiviser par H3 (chaque H3 devient un sous-chunk)
- **Injection du frontmatter** : à l'indexation, le frontmatter du fichier est injecté en tête de chaque chunk pour préserver le contexte métadonnées (code, titre, type, axe, niveau)

**Validation** : audit-md-rag.py mesure la longueur de chaque section et signale les sections > 800 tokens non subdivisées.

---

## Règle 4 — Wikilinks pour les références internes

- **Syntaxe** : Obsidian native
  - Sans alias : `[[cu-008]]`
  - Avec alias : `[[cu-008|Knowledge base RAG]]`
  - Vers section interne : `[[cu-008#nom-de-section]]`
- **Vers le glossaire** : `[[glossaire#rag]]` (alias optionnel)
- **Cibles** : code de fichier MD du vault, sans extension `.md`

**Liens externes** (hors vault) : MD standard `[texte](url)`. Toujours inclure le domaine source dans le texte si pertinent.

**Validation** : audit-md-rag.py vérifie que les cibles des wikilinks existent dans le vault.

---

## Règle 5 — Glossaire canonique unique

Tous les termes techniques utilisés dans le vault sont définis **une seule fois canoniquement** dans `glossaire.md`, et **toujours référencés par wikilink** ailleurs.

**Forme du glossaire** : un fichier `glossaire.md` à la racine de `rag/content/`, avec une section H2 par terme. La définition est strictement alignée sur les gloses obligatoires de RULES-IMPLEMENTATION v1.4 §1.3.2 du couple 1 (alignement éditorial).

**Anti-pattern** : redéfinir un terme dans plusieurs fichiers. Si un fichier MD doit clarifier un terme localement, il référence `[[glossaire#terme]]` au lieu de redonner la définition.

---

## Règle 6 — Citations et chiffres sourcés

Tout chiffre statistique ou citation directe doit être suivi de sa source datée dans un format identifiable :

```markdown
95 % des projets GenAI échouent (Source : MIT Sloan / NANDA, août 2025, [URL](https://...)).
```

**Pas de chiffre orphelin** (alignement RULES couple 1 §1.1.1).

**Bloc citation** pour les citations longues :

```markdown
> « Toute organisation au-dessus de 5-10 personnes perd structurellement du temps à chercher de l'information. »
> — Source : Bpifrance Le Lab, 2025, [URL]
```

**Anti-pattern** : citations sans source, ou source vague (« selon une étude »).

---

## Règle 7 — Convention de nommage de fichier

- **Unités numérotées** : `{type}-{numero}.md` — exemples : `cu-008.md`, `pr-01.md`, `dep-02.md`, `a1.md`
- **Fiches outils regroupées par catégorie** : `outils-{categorie}.md` — exemples : `outils-vector-db.md`, `outils-llm-gateway.md`, `outils-embeddings.md`
- **Brain pages transverses** : `transverse-{slug}.md` — exemples : `transverse-rag-vs-llm-wiki.md`, `transverse-financement-ia-pme.md`
- **Glossaire** : `glossaire.md` (singulier, à la racine de `rag/content/`)

**Hors vault** : pas d'extensions exotiques, pas d'espaces dans les noms, tout en kebab-case lowercase.

---

## Règle 8 — Versioning et `last_updated`

À chaque modification substantielle d'un fichier MD :
- Bump du champ `version` du frontmatter (aligné avec la version Hub IA d'origine si modif liée à une évolution du contenu HTML, ou bump patch sinon — ex. 3.8.2 → 3.8.3)
- Mise à jour du champ `last_updated` (date ISO YYYY-MM-DD)

**Pourquoi** : permet le versioning par chunk dans le vector store (D-019), purge des versions obsolètes, détection des dérives.

**Validation** : audit-md-rag.py signale tout fichier dont `last_updated` est antérieur à la dernière modification git de plus de 7 jours (incohérence probable).

---

## Anti-patterns identifiés a priori (à enrichir post-pilote)

1. **Frontmatter incomplet ou champs vides** : `tags: []` est un signal de paresse, à éviter
2. **Sections H2 dépassant 1000 tokens sans subdivision** : rend le chunk trop dilué
3. **Wikilinks vers cibles inexistantes** : pollution du graphe, à corriger immédiatement
4. **Définitions redondantes** : termes redéfinis localement au lieu d'être référencés au glossaire
5. **Chiffres sans source ou sources non vérifiables** : alignement RULES couple 1 §1.1
6. **Phrases narratives liantes** : « comme on vient de voir », « dans la suite de ce module » — rendent la section non autonome

---

## Validation par audit-md-rag.py (5 règles initiales en v1)

Le script `audit-md-rag.py` (livré en S1 par Claude Code Plateforme) valide à minima :

1. **R1-frontmatter-complet** : les 10 champs du frontmatter sont présents et non vides
2. **R2-h1-unique** : exactement un H1 par fichier, identique à `titre`
3. **R3-chunking-respecte** : aucune section H2 > 800 tokens sans subdivision H3
4. **R4-wikilinks-valides** : toutes les cibles de wikilinks existent dans le vault
5. **R6-chiffres-sources** : tout chiffre numérique de pattern `%`, `×`, `k€`, `M€` est suivi à moins de 50 caractères d'une mention « Source : » ou d'un lien `[...](...)` ou d'une mention `URL`

Les règles R5 (glossaire), R7 (nommage), R8 (versioning) sont validées manuellement dans v1, candidats à automatisation en v2.

---

## Historique des versions

| Version | Date | Modification |
|---|---|---|
| v1 | 11 mai 2026 | Version initiale, 8 règles essentielles |

**Évolution prévue** : enrichissement en v2 post-pilote S1 sur la base des écarts détectés.
