# SPEC-MD-POUR-RAG.md — Cahier des charges des fichiers MD pour le RAG

**Statut :** v1.3 (8 règles essentielles + R9 + R10 + exception R1 glossaire + politique wikilinks futurs)
**Dernière mise à jour :** 12 mai 2026 (révision post-S1bis Claude Code Plateforme)
**Maintainer :** Cowork Hub IA Plateforme

> **Rôle :** spécifier le **format technique** des fichiers MD du vault `rag/content/`. Ce fichier traite des conventions concrètes (frontmatter, chunking, naming, wikilinks). Pour la stratégie de retranscription, voir `STRATEGIE-MD-RAG.md`.

> **Principe directeur (RetEx couple 1 Q3 §3) :** démarrer minimaliste, enrichir au fil des écarts détectés par audit-md-rag.py. Cette v1 contient 8 règles essentielles. Les règles ajoutées en v2+ proviendront des apprentissages du pilote S1.

> **Règle de gouvernance (D-023, issue retour couple 1 sur I-001) :** toute nouvelle règle ajoutée à ce fichier au-delà de la v1 doit s'accompagner, **dans le même commit**, d'une fonction de validation correspondante dans `audit-md-rag.py`. Sinon, la règle bascule en « anti-pattern documenté » (recommandation forte mais non opposable), pas en règle stricte. Pattern aligné sur K.1 de RULES-IMPLEMENTATION v1.6 du couple 1.

---

## Exception structurelle pour les fichiers racines transverses (issue S1bis catégorie A)

Deux champs du frontmatter peuvent être légitimement vides pour les fichiers de type `transverse` qui constituent la **racine canonique** d'un système de référence :

- `glosaire_termes: []` — pour le `glossaire.md` (le glossaire est la racine du système de termes, il ne référence pas un autre glossaire)
- `derives: []` — pour le `glossaire.md` et pour les briques transverses « pures » (celles qui ne dérivent pas d'un module identifié)

**Cette exception est inscrite par D-028 et doit être reconnue par audit-md-rag v2** (cf. roadmap audit v2 ci-dessous).

**Anti-pattern interdit** : utiliser cette exception comme prétexte pour laisser vides des champs dans des fichiers ordinaires (modules CU, préalables PR, fiches DEP, fiches outils). Cette exception est strictement limitée aux fichiers racines transverses.

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

### Politique des wikilinks vers MD planifiés mais non encore produits (issue S1bis catégorie B + D-029)

Le vault est construit par vagues successives. Les premiers modules produits font légitimement référence à des modules à produire dans les vagues suivantes (ex. `cu-001.md` référence `cu-002.md` qui n'est pas encore dans le vault). Ces wikilinks sont **anticipations planifiées**, pas erreurs.

**Mécanisme** : un fichier `rag-prep/whitelist-wikilinks-futurs.md` (côté gouvernance, hors vault) liste les codes de fichiers planifiés mais pas encore produits. L'audit-md-rag v2 le lira au démarrage et émettra des **warnings** (pas des erreurs) pour les wikilinks pointant vers ces codes.

**Politique de mise à jour de la whitelist** : à chaque nouveau MD produit, retirer son code de la whitelist. Si une wikilink pointe vers un code ni dans le vault ni dans la whitelist → erreur réelle, le wikilink est cassé.

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

## Règle 10 — Transposition fidèle des valeurs numériques dans les tableaux (issue I-003)

Lors de la transposition d'un tableau HTML vers MD, toutes les **valeurs numériques** (seuils, fourchettes, pourcentages, montants, durées) doivent être transposées **textuellement à l'identique**, sans élargissement, raboutage, abandon de précision ou reformulation.

**Exemples de dérives à éviter** (cas réels détectés en revue I-003 sur matrice PR-07) :
- HTML : « < 20 utilisateurs » → MD : « < 20-30 utilisateurs » (élargissement)
- HTML : « > 50 utilisateurs ou volume élevé » → MD : « > 30 utilisateurs ou usage quotidien massif » (abaissement seuil + reformulation)
- HTML : « Budget initial 40-100 K€ + 20 %/an OK » → MD : « Capacité d'investissement initial 40-80 k€ » (perte du 20 %/an + plafond raboté)
- HTML : « SaaS 50-200 €/mois suffit, ROI 6 mois » → MD : « Budget récurrent OK, pas de capacité d'investissement » (perte de la fourchette chiffrée + perte du ROI)
- HTML : « 3-9 mois acceptables » → MD : « 6-12 mois acceptable » (décalage de fourchette)

**Pourquoi cette discipline** : ces dérives ressemblent à des « corrections instinctives » qui semblent éditorialement bénignes (élargir pour sécuriser, perdre les chiffres précis pour ne pas s'engager). Mais elles cassent la cohérence cross-couche entre le HTML pédagogique (engageant chiffré) et le MD RAG (qui doit fournir des références exactes).

**Validation** : audit-md-rag.py R10 (à implémenter en v2 post-S1) — pour chaque tableau MD, extraire les valeurs numériques (regex `\d+(?:\s*[-–]\s*\d+)?\s*(?:%|€|K€|k€|mois|jours|tokens|utilisateurs)?`), comparer aux valeurs extraites du HTML source correspondant, signaler tout écart numérique.

---

## Règle 9 — Citation textuelle des chiffres canoniques du Hub (issue I-002)

Tout chiffre macro déjà cité dans le Hub IA (HTML source ou brique transverse `chiffres-macro-2026.md`) doit être **cité textuellement** dans un MD du vault, sans paraphrase. La reformulation paraphrastique d'un chiffre canonique change potentiellement son sens et crée une divergence cross-couche.

**Exemple de dérive à éviter** (cas réel détecté en revue I-002) :
- HTML source : « 67 % des dirigeants PME/TPE **ne savent pas par où commencer** avec l'IA »
- MD initialement produit : « 67 % des dirigeants PME/TPE **n'ont pas commencé** avec l'IA »
- Sens divergent : « ne savent pas par où commencer » = manque de méthode ; « n'ont pas commencé » = absence totale d'usage. Les deux ne mesurent pas la même chose.

**Application pratique** :
- Si le chiffre vit déjà dans `chiffres-macro-2026.md` (brique transverse) : wikilinker plutôt que reformuler — `[[chiffres-macro-2026#67-pourcent-bpifrance]]`
- Si le chiffre n'est pas encore dans la brique transverse : citer textuellement le HTML source, et ajouter le chiffre dans la brique pour les usages futurs

**Validation** : audit-md-rag.py R9 (à implémenter post-S1) — détecte les chiffres macro en clair dans un module (au lieu de wikilink vers `chiffres-macro-2026.md`).

---

## Règle 8 — Versioning et `last_updated`

À chaque modification substantielle d'un fichier MD :
- Bump du champ `version` du frontmatter (aligné avec la version Hub IA d'origine si modif liée à une évolution du contenu HTML, ou bump patch sinon — ex. 3.8.2 → 3.8.3)
- Mise à jour du champ `last_updated` (date ISO YYYY-MM-DD)

**Pourquoi** : permet le versioning par chunk dans le vector store (D-019), purge des versions obsolètes, détection des dérives.

**Validation** : audit-md-rag.py signale tout fichier dont `last_updated` est antérieur à la dernière modification git de plus de 7 jours (incohérence probable).

---

## Briques transverses — méthodologie d'extraction (issue I-002 Q7)

Pour le RAG, certaines briques sémantiques (vigilances communes, patterns récurrents, chiffres macro, définitions étendues, méthodologies transverses) traversent de nombreux modules. Plutôt que de les dupliquer dans chaque module concerné, elles sont **extraites en fichiers transverses** dans `rag/content/transverses/` (ou `transverses/` du vault) et **référencées par wikilink** depuis les modules qui les mentionnent.

**Pattern architectural validé (D-025)** : unité de base = module CU/PR/DEP, + extraction sélective de briques transverses dès qu'un concept apparaît dans **3+ modules**.

**Critères d'éligibilité à l'extraction** :
- Concept présent dans 3 modules ou plus
- Concept indépendant sémantiquement (peut être indexé seul et servir une réponse autonome)
- Concept stable dans le temps (peu d'évolution attendue) OU concept dont la mise à jour centralisée évite la dérive (ex. chiffres macro)

**Catégories de briques transverses** (à enrichir au fil des productions) :
- `vigilance-{slug}.md` — patterns de vigilance commune (hallucinations, confidentialité, dépendance vendor, etc.)
- `pattern-{slug}.md` — patterns récurrents (build-vs-buy, rag-vs-fine-tuning, etc.)
- `methodologie-{slug}.md` — méthodologies réutilisables (prompt engineering, eval, etc.)
- `chiffres-macro-{annee}.md` — référentiel des chiffres canoniques du Hub
- `cadrage-{slug}.md` — cadrages réglementaires ou stratégiques (AI Act, souveraineté EU, etc.)

**3 risques à monitorer (issus de la revue I-002)** :
1. **Dérive du référentiel de chiffres** : si `chiffres-macro-2026.md` n'est pas maintenu à jour à chaque évolution v3.X du Hub, les modules MD divergent silencieusement → audit régulier obligatoire à chaque itération éditoriale majeure
2. **Duplication entre brain page et module** : risque qu'un module mentionne en clair un concept au lieu de wikilinker → audit-md-rag.py futur (R9 pour chiffres macro, à étendre)
3. **Wikilinks cassés** : renommage d'une brique transverse casse silencieusement les wikilinks dans tous les modules qui y pointent → audit régulier des wikilinks orphelins (R4)

---

## Anti-patterns identifiés (enrichis post-revue I-002)

### Anti-patterns d'a priori (v1)

1. **Frontmatter incomplet ou champs vides** : `tags: []` est un signal de paresse, à éviter
2. **Sections H2 dépassant 1000 tokens sans subdivision** : rend le chunk trop dilué
3. **Wikilinks vers cibles inexistantes** : pollution du graphe, à corriger immédiatement
4. **Définitions redondantes** : termes redéfinis localement au lieu d'être référencés au glossaire
5. **Chiffres sans source ou sources non vérifiables** : alignement RULES couple 1 §A
6. **Phrases narratives liantes** : « comme on vient de voir », « dans la suite de ce module » — rendent la section non autonome

### Anti-patterns documentés post-revue I-002

7. **AP-2 — Conversion monétaire ad-hoc** : convertir des prix € en $ (ou inverse) sans alignement avec le HTML source du Hub. Crée des incohérences cross-couche pour le public PME/ETI européen.
   - *Exemple détecté* : « Perplexity Pro à 20 $/mois » dans le MD vs « 20 €/mois » dans le HTML.
   - *Recommandation* : aligner systématiquement le MD sur les valeurs et devises du HTML.

8. **AP-3 — Édulcoration d'éléments contextuels secondaires** : suppression de citations, certifications, références, acteurs nommés qui ajoutent du poids argumentatif au module.
   - *Exemples détectés* : référence MIT 2025 absente du MD ; certifications ISO 27001 / SOC 2 du Chat Pro édulcorées en « garanties RGPD natives » (formulation plus vague).
   - *Recommandation* : pendant la distillation, conserver explicitement les noms d'études / rapports cités, les certifications (ISO, SOC, SecNumCloud, etc.), les acteurs nommés (Bpifrance, France Num, MIT, McKinsey, etc.).

9. **Reformulation paraphrastique d'un chiffre canonique** : passé en **règle stricte R9** (cf. plus haut), pas seulement anti-pattern.

---

## Validation par audit-md-rag.py (5 règles initiales en v1)

Le script `audit-md-rag.py` (livré en S1 par Claude Code Plateforme) valide à minima en v1 (5 règles) :

1. **R1-frontmatter-complet** : les 10 champs du frontmatter sont présents et non vides
2. **R2-h1-unique** : exactement un H1 par fichier, identique à `titre`
3. **R3-chunking-respecte** : aucune section H2 > 800 tokens sans subdivision H3
4. **R4-wikilinks-valides** : toutes les cibles de wikilinks existent dans le vault
5. **R6-chiffres-sources** : tout chiffre numérique de pattern `%`, `×`, `k€`, `M€` est suivi à moins de 50 caractères d'une mention « Source : » ou d'un lien `[...](...)` ou d'une mention `URL`

À ajouter en v2 (post-S1, alignement avec règles consolidées et apprentissages S1bis) :

6. **R5-glossaire** : tout terme du glossaire utilisé dans un MD doit l'être via wikilink `[[glossaire#terme]]`, pas en clair
7. **R7-nommage** : conformité au schéma `{type}-{numero}.md` ou `outils-{categorie}.md`
8. **R8-versioning** : `last_updated` cohérent avec la dernière modification git (< 7 jours d'écart)
9. **R9-chiffres-macro-canoniques** : tout chiffre macro du Hub (95 %, 67 %, 76 %, etc.) cité dans un MD doit l'être soit textuellement (avec source), soit via wikilink vers `chiffres-macro-2026.md`. Détection par regex et comparaison avec `chiffres-macro-2026.md` parsé.
10. **R10-tableaux-numeriques-fideles** : pour chaque tableau MD, comparer les valeurs numériques extraites (regex sur seuils, fourchettes, montants, durées) avec celles du HTML source correspondant. Signaler tout écart numérique.

### Évolutions issues du retour S1bis Claude Code Plateforme (à intégrer en v2)

11. **Exception R1 pour fichiers racines transverses** (D-028) : ne pas considérer comme « champ vide » `glosaire_termes` et `derives` quand `code == "glossaire"` ou pour les briques transverses racines. Vide par construction = légitime.
12. **R4 tolérante aux wikilinks vers MD planifiés** (D-029) : lire `rag-prep/whitelist-wikilinks-futurs.md` au démarrage de l'audit. Wikilinks vers codes whitelistés → warnings (pas erreurs). Wikilinks vers codes ni dans le vault ni dans la whitelist → erreurs réelles.
13. **R6 reconnaît les wikilinks canoniques comme source** : étendre `SOURCE_MARKERS` pour matcher `\[\[chiffres-macro-\d{4}[^\]]+\]\]` et plus généralement les wikilinks vers `transverses/*`. Convergence opérationnelle R6 ↔ R9.

---

## Historique des versions

| Version | Date | Modification |
|---|---|---|
| v1 | 11 mai 2026 | Version initiale, 8 règles essentielles |
| v1.1 | 11 mai 2026 | + R9 (citation textuelle chiffres canoniques, règle stricte issue retour I-002) ; + section méthodologique « briques transverses » (D-025) ; enrichissement anti-patterns (AP-2 conversion monétaire, AP-3 édulcoration contextuelle) ; ajout glose « On-premise » au glossaire (alignement RULES §C.2)|
| v1.2 | 12 mai 2026 | + R10 (transposition fidèle des valeurs numériques dans les tableaux, règle stricte issue retour I-003) ; AP-4 promu en règle R10 plutôt qu'anti-pattern documenté ; audit R10 ajouté à la roadmap v2 audit-md-rag.py |
| v1.3 | 12 mai 2026 | + Exception structurelle R1 pour fichiers racines transverses (D-028, issue S1bis catégorie A) ; + Politique des wikilinks vers MD planifiés (D-029, issue S1bis catégorie B) ; roadmap audit v2 enrichie de 3 évolutions (exception R1, R4 tolérante, R6 reconnaît wikilinks canoniques) |

**Évolution prévue** : enrichissement en v2 post-pilote S1 sur la base des écarts détectés par les premières exécutions de `audit-md-rag.py`.
