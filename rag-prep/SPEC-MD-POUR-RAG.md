# SPEC-MD-POUR-RAG.md — Cahier des charges des fichiers MD pour le RAG

**Statut :** v2.1 (v2.0 + 3 ajouts validés post-clôture S2.6 — RAPPORT-CC-S2.6 §6 + arbitrage Cowork) : (1) **Recalibrage cap coût 80-90q → 2,15 $** (mesure empirique S2.6 — 81q × 0,0253 $/q = 2,05 $ + marge variance 5 %) ; (2) **Extension bande latence vault 300-400 chunks** (p50 ≤ 20 s / p90 ≤ 24 s, mesure empirique S2.6 vault 318 chunks p50 19,0 s / p90 22,0 s) + recommandations reranking / réduction top-k / cache embeddings pour vault > 400 chunks ; (3) **Pattern production module pivot dense formalisé** (H2 autonome + lead-scope restreint AP-7 préventif + chunking ≤ 900 tokens, validé empiriquement PR-11 — 1er score parfait 81/81).
**Dernière mise à jour :** 22 mai 2026 (révision post-S2.6 — 3 propositions Plateforme validées par Cowork)
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
- **Tolérance empirique 800-900 tokens** (post-S2.4, validé sur Frontier Firms cu-026 850 tokens) : le seuil 800 est une **recommandation** ; tolérance jusqu'à ~900 tokens **si le chunk est thématiquement cohérent** (un seul angle traité, pas d'enchaînement de sous-sujets distincts). **Au-delà de 900 tokens : refactoring H3 obligatoire** pour préserver la qualité du retrieval.
- **Injection du frontmatter** : à l'indexation, le frontmatter du fichier est injecté en tête de chaque chunk pour préserver le contexte métadonnées (code, titre, type, axe, niveau)

**Validation** : audit-md-rag.py mesure la longueur de chaque section et signale les sections > 900 tokens non subdivisées (warning entre 800-900 tokens, erreur > 900 tokens).

**Précision empirique post-S2.4.1 Lot D-ter (chunking H2 autonome + lead bridge)** : pour qu'un chunk de specs précises soit retrouvé sur des questions au vocabulaire générique, il ne suffit pas de mettre les specs en sub-section H3 dans une H2 < 800 tokens (le H3 sera agglutiné au chunk H2 parent). Promotion en H2 dédiée + lead bridge enrichi avec vocabulaire question canonique attendu (premier paragraphe en gras) sont les **deux conditions nécessaires et indissociables**. Cf. §Conception MD et questions golden set ci-dessous.

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

### Extraction côté code RAG (formalisation post-S2.2 Lot E.1)

Les réponses produites par le pipeline RAG citent les sources selon deux formats, lus par `extract_cited_codes()` dans `rag/code/backend/query.py` :

- **Format préféré** : wikilink Obsidian — `[[code]]`, `[[code#ancre]]`, `[[code|alias]]`, `[[code#ancre|alias]]`. Codé dans `WIKILINK_CITATION_PATTERN`. C'est le format demandé au LLM par le `SYSTEM_PROMPT` enrichi (D-025, Lot C S2.2).
- **Format accepté (rétro-compatibilité)** : crochets simples — `[CU-NNN]`, `[PR-NN]`, `[DEP-NN]`, `[A1]`, `[OUTILS-*]`, `[TRANSVERSE-*]`. Codé dans `BRACKET_CITATION_PATTERN` avec lookbehind/lookahead `(?<!\[)...(?!\])` pour éviter la double-capture à l'intérieur d'un wikilink.

**Contrat de sortie** : `extract_cited_codes()` normalise en lowercase, préserve l'ordre d'apparition, déduplique case-insensitive. L'évaluation contre `expected_sources` (lowercase) est donc cohérente.

**Pourquoi cette formalisation** : le bug S2.2 Lot D (9/15 sources retrouvées au lieu de 30/30 après fix Lot E.1) est resté invisible jusqu'à l'eval réelle car les tests unitaires mockés ne validaient que le format crochets historique. Toute évolution future du format de citation (nouveau type, nouvelle famille de codes, séparateur supplémentaire) doit s'accompagner d'une mise à jour des patterns d'extraction ET d'un rejeu eval réelle (voir §Validation).

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

### v1.4 — Mode par défaut R6 = warning (codification post-S2.1)

R6 signale par défaut un **warning** (non bloquant en CI standard) pour les chiffres orphelins, afin de tolérer les heuristiques pédagogiques internes au Hub (impacts relatifs documentés par RetEx interne, fourchettes techniques sans source primaire publique, formulations marketing acceptables type « 80 % entreprises ont Postgres »). Cette codification consacre la convention déjà appliquée empiriquement par Claude Code Plateforme audit v2 (cf. RAPPORT-CC-S2.1 §5 P1, validée par arbitrage Cowork SPEC v1.4).

Le **mode strict** (R6 → erreur bloquante) est activable via `audit-md-rag.py --strict-r6` quand Cowork veut durcir la CI (typiquement post-vague 3 ou pour audit ponctuel pré-publication).

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

**Précision D-025 post-S2.3 — ossature complète d'un module ≠ brique transverse extractible** (issue RAPPORT-CC-S2.3 §6 P2, validée empiriquement par RETOUR-SONDAGE-COWORK-HUB-IA-S2.3 sur le pattern « agent = employé » de CU-026) :

Si un concept constitue l'**ossature complète** d'un module — c'est-à-dire qu'il en structure le titre de Section 1, un Takeaway exec, ET la base d'un framework structurant du module — alors **il ne doit PAS être extrait en transverse**, même s'il est mentionné dans un autre module.

Une mention satellite avec wikilink depuis un autre module ne constitue pas une duplication justifiant l'extraction : la dissymétrie « module dédié + mention satellite » est éditorialement saine et n'introduit pas de dette de maintenance significative.

Critère de test : si on retirait le concept du module candidat, le module perdrait-il son ossature ? Si oui → pas d'extraction. Si non → l'extraction reste possible selon les autres critères.

*Exemple d'application* : le pattern « agent = employé » est l'ossature complète de CU-026 (Gouvernance des agents IA) — titre Section 1, Takeaway 3, base conceptuelle des 7 dimensions du framework. CU-014 (Multi-agents) ne fait qu'y faire un renvoi wikilink. **Décision** : pas d'extraction en `transverses/pattern-agent-employe.md`, maintien dans CU-026 entier.

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

10. **AP-5 — Valeurs numériques non quotées dans `expected_concepts`** (golden set eval, issue S2.2 Lot D blocker) : toute valeur du champ `expected_concepts` d'une entrée du golden set YAML qui commence par un chiffre doit être **explicitement quotée** (`"95 %"`, `"1,8 heures"`, `"21 %"`). PyYAML parse sinon les nombres en `int`/`float`, faisant crasher `evaluate_one()` sur `int.lower()`.
   - *Cas réels détectés* (S2.2 Lot D) : q-016 (`[1,8, heures, McKinsey]` → `1,8` lu comme float), q-019 (`[95, ROI, ...]` → `95` int), q-027 (`[21, McKinsey, workflow]` → `21` int).
   - *Recommandation* : à chaque ajout d'une question au golden set, vérifier visuellement le typage YAML. À terme, soit défense côté code (`str(c).lower()` dans `evaluate_one`), soit pre-commit golden set côté Cowork (audit YAML).
   - *Statut* : anti-pattern fort. Renforcé côté Plateforme via Lot D S2.3 — `concept_matched()` applique `str(syn).lower()` défensivement.

11. **AP-6 — Synonymes excessifs dans `expected_concepts` liste de listes** (option B matching sémantique, issue RAPPORT-CC-S2.3 §6 P3) : une entrée `expected_concepts` au format liste de listes (synonymes pour un même concept) ne doit **pas dépasser 4 synonymes**. Plafond recommandé : **2-4 synonymes par concept**.
   - *Risque* : au-delà de 4 synonymes, augmentation linéaire du risque de **faux positifs** (un synonyme large matche un concept différent de celui visé). Exemple : `[économie, économies, gain, réduction, optimisation, performance]` matcherait « économie d'énergie » qui n'est pas le concept attendu.
   - *Variations à privilégier* : morphologiques évidentes (substantif/verbe : `vérification/vérifier`), pluriel/singulier (`heures/heure`), racine commune (`persistant/persistance/persistent`). Éviter les synonymes thématiquement proches mais sémantiquement distincts.
   - *Recommandation* : audit visuel à chaque ajout/modification. Si plus de 4 synonymes semblent nécessaires, c'est probablement que le concept est mal défini — le scinder en 2 concepts distincts est préférable.

12. **AP-7 — Lead bridge sur-élargi** (anti-pattern symétrique inverse du garde-fou « concepts détaillés » SPEC v1.6, issue RAPPORT-CC-S2.4 §6 P1 — validé empiriquement par régressions q-002 + q-030 S2.4 Lot I) : un lead de chunk H2 ne doit pas étendre son vocabulaire bridge **au-delà du scope strict du module**. Sinon, ce chunk peut **saturer le top-5 retrieval sur des questions transversales** et étouffer d'autres modules plus pertinents.
   - *Cas-école* : `pr-08` lead « **financer un projet IA en 2026 pour PME — à condition de connaître la carte** » contient les termes « projet IA », « 2026 », « PME » trop génériques. Conséquence : saturation top-5 cosine sur q-002 (cu-001 — sources fiables actualité IA 2026 + PME) et q-030 (pr-07 — obligations réglementaires projet IA PME 2026). pr-07 absent du top-10, cu-001 rang #8 sim 0,109.
   - *Discipline* : le lead doit contenir le vocabulaire bridge **du scope effectif du module**, pas un vocabulaire générique qui matcherait des questions hors scope. Pour un module thématiquement spécifique (financement, sécurité, gouvernance, etc.), le lead doit explicitement contenir le scope dès la première phrase (« **dispositifs fiscaux** + **Bpifrance** + **France 2030** » pour pr-08, pas « projet IA PME »).
   - *Audit* : à chaque production module, lister 3-5 questions hors scope que le module ne doit PAS dominer en top-5 ; reformuler le lead s'il les domine au retrieval.
   - *Statut* : anti-pattern fort, audit manuel à la production (audit automatisable en v3 audit-md-rag.py si signature distance cosine).

---

## Conception MD et questions golden set — garde-fou « concepts détaillés » (issue RAPPORT-CC-S2.3 §6 P4)

Quand une question du golden set cible des **specs techniques précises** — chiffres exacts (« 1 282 tests », « 102 règles »), noms d'outils nommés (Snyk, Semgrep, AgentShield), paramètres CLI (`--opus`, `--strict-r6`) — deux disciplines complémentaires doivent être appliquées simultanément :

1. **Côté MD source** : prévoir une **sous-section H3 dédiée** dans le module concerné, regroupant les specs précises en un chunk identifiable. Le retrieval RAG est plus susceptible de retourner un chunk H3 ciblé « specs opérationnelles AgentShield » que de capter ces specs noyées dans un chunk H2 généraliste « outils de mitigation ».

2. **Côté `expected_concepts`** : prévoir un format **plus tolérant aux variations numériques** via l'option B (liste de synonymes). Exemples :
   - `["1 282", "1282", "1 282 tests", "milliers de tests"]` plutôt que `1 282` scalaire
   - `["102 règles", "102", "centaine de règles"]` plutôt que `102 règles` scalaire
   - `["--opus", "mode --opus", "mode Opus"]` plutôt que `--opus` scalaire

**Pourquoi cette double discipline** : l'eval S2.3 Lot E a identifié q-038 (dep-08 sécurité agents) comme seul échec score=0 sur 42 questions. La source dep-08 a bien été retrouvée, mais les concepts détaillés (Snyk, Semgrep, « 1 282 », « 102 règles », `--opus`) étaient absents de la réponse — le retrieval avait sélectionné des chunks dep-08 généralistes plutôt que le chunk « outils de mitigation » avec les specs précises. Le découpage H3 + format `expected_concepts` tolérant aurait permis d'éviter cet échec en amont.

**Application pratique** : lors de la production d'un nouveau module ou de la rédaction d'une question golden set, **identifier ex-ante les concepts détaillés** (chiffres exacts, noms d'outils précis, paramètres) et appliquer la double discipline. À auditer dans la revue de production MD et dans la revue de questions golden set.

### Pattern « 3 niveaux d'intervention retrieval » (validé empiriquement S2.4.1 + S2.5)

Quand un chunk cible n'apparaît pas dans le top-5 retrieval sur une question canonique attendue, **3 niveaux d'intervention** se composent successivement selon l'écart résiduel :

**Niveau 1 — Lead bridge enrichi** (validé Lot D-ter S2.4.1 sur q-038) : reformuler le premier paragraphe d'un chunk H2 pour inclure dès la première phrase en gras le vocabulaire question canonique attendu (termes génériques + termes techniques précis). Cible : un chunk qui contient textuellement les concepts mais reste hors top-5 du fait d'un embedding dominé par les termes techniques.

*Cas-école Lot D-ter* : q-038 dep-08 — chunk « specs opérationnelles AgentShield » contenait textuellement 1 282 tests / 102 règles / `--opus` mais ne figurait pas dans le top-5. Promotion H3 → H2 autonome **+** lead enrichi avec vocabulaire « **Outils et patterns de mitigation pour sécuriser des agents IA en production** » → chunk passé rang ≥11 → rang **#1 sim 0,2239**, q-038 score=0 → score=1.

**Niveau 2 — H2 dédiée concurrente** (validé Lot S2.5.0-bis sur q-030) : si le top-10 retrieval est saturé par un module concurrent dominant (plusieurs chunks du même module), un simple patch lead du module dominé ne suffit pas — il faut créer une **nouvelle section H2 dédiée** dans le module dominé pour produire un chunk concurrent en propre, indépendant des autres chunks existants.

*Cas-école Lot S2.5.0-bis* : q-030 (obligations réglementaires projet IA PME 2026) — top-10 saturé 100 % par pr-08 (Financement IA). Le lead pr-07 enrichi ne remontait qu'au rang #13. Création d'une nouvelle H2 « Obligations réglementaires IA pour un projet en PME 2026 » dans pr-07 → chunk passé rang #13 → rang **#6 sim 0,3062** (+0,1204).

**Niveau 3 — Densification chirurgicale du lead** (validé Lot S2.5.0-ter sur q-030) : si le chunk concurrent est entré dans le top-10 mais reste hors top-5 (écart résiduel typiquement 0,01-0,02 sim), densifier le lead par **répétition contrôlée** du vocabulaire question canonique. Discipline : titre H2 verbatim de la formulation de la question canonique attendue, premier paragraphe en gras qui reformule la question puis enchaîne la réponse, répétition explicite des 4-6 termes-clés (3-5 occurrences par terme).

*Cas-école Lot S2.5.0-ter* : q-030 — chunk pr-07 « Obligations réglementaires » entré rang #6 (Niveau 2) mais hors top-5 (gap 0,0144 sim). Densification du lead : titre H2 inclut « **à anticiper** » verbatim de la question, premier paragraphe reformulé en mode question + réponse 4 ancrages, répétition « obligations réglementaires » 3× / « projet IA » 5× / « RGPD/AI Act/conformité/2026 » 5× chacun → chunk passé rang #6 → rang **#3 sim 0,3635** (+0,0573), q-030 score=0 → score=1.

**Application** : appliquer les niveaux successivement selon l'écart résiduel observé. Niveau 1 d'abord (le plus léger). Niveau 2 si saturation par module concurrent dominant. Niveau 3 en finalisation si le chunk concurrent reste proche mais hors top-5.

**Mise en garde** : la densification de Niveau 3 augmente la taille du chunk (~+50-100 mots typiquement). Surveiller la tolérance seuil R3 800-900 tokens. Au-delà, refactoring H3 obligatoire (cf. §R3).

### Procédure normée « Lot Drer + N1/N2/N3 » pour traiter une régression retrieval (codifiée SPEC v2.0)

Quand une question du golden set passe `score=1` → `score=0` entre deux évals consécutives (régression retrieval typiquement causée par une production from scratch qui dilue le top-5 du fait de leads concurrents), appliquer la procédure normée suivante avant de réécrire le module dominé :

**Étape 1 — Diagnostic ciblé via Lot Drer** : avant tout patch éditorial, exécuter un **Lot Drer** (rerun eval ciblé sur 4-8 questions touchées + 1-2 questions de contrôle). Coût typique ~0,10-0,20 $ Anthropic, ~10-15 min Desktop. Sortie attendue : rang du chunk cible attendu dans le top-10 + sim cosine + identifié des modules concurrents qui saturent.

**Étape 2 — Choix du niveau d'intervention** selon le diagnostic :
- **Si chunk cible présent top-10 mais rang #6-10** (gap < 0,02 sim avec rang #5) → **Niveau 1** (lead bridge enrichi, ~20-30 min Cowork)
- **Si chunk cible absent top-10 ET top-10 saturé par module concurrent (≥ 3 chunks du même module)** → **Niveau 2** (créer H2 dédiée concurrente, ~45 min Cowork)
- **Si chunk cible #6-#10 après Niveau 2 mais hors top-5 (gap résiduel 0,01-0,02 sim)** → **Niveau 3** (densification chirurgicale, ~30 min Cowork)

**Étape 3 — Validation par Lot Drer post-patch** : rejouer le même Lot Drer (4-8 questions ciblées) pour mesurer le delta de rang et confirmer la résolution. Si Niveau N n'a pas suffi (chunk cible toujours hors top-5), enchaîner avec Niveau N+1 (pattern observé empiriquement sur q-030 : Lot S2.5.0 + bis + ter = 3 itérations Niveau 1 → Niveau 2 → Niveau 3).

**Étape 4 — Inscription au JOURNAL** : tracer chaque itération (rang avant/après, sim cosine, lots éditoriaux appliqués). Cas-école q-038 et q-030 servent de référence empirique pour calibrer le diagnostic des sprints futurs.

**Mise en garde — Surcoût budgétaire des Lot Drer en cascade** : 3 itérations de Lot Drer ≈ 0,30-0,60 $ Anthropic. Documenter ex-ante au brief sprint si > 1 cascade Lot Drer attendue (typiquement quand le sprint produit plusieurs modules from scratch sur des thèmes adjacents).

**Anti-pattern à éviter** : sauter directement au Niveau 3 (densification chirurgicale) sans diagnostic Lot Drer préalable — risque de gonfler inutilement la taille des chunks au-delà de la tolérance R3, sans résoudre une saturation top-10 qui aurait nécessité un Niveau 2.

### Pattern « production module pivot dense » (codifié SPEC v2.1)

Un **module pivot** est un module dont la valeur principale tient à la séquence d'ensemble qu'il structure (carte de navigation, cycle de vie, framework transverse), avec cross-links denses vers de nombreux autres modules. Caractéristiques typiques : module dense (≥ 500 lignes HTML, ≥ 200 lignes MD attendues), vocabulaire transverse, mention de la majorité des autres modules du domaine.

**Risque structurel** : ce type de module est **maximalement exposé à AP-7** (lead bridge sur-élargi → saturation top-5 retrieval sur questions transversales étouffant les modules d'étape plus pertinents).

**Pattern préventif validé empiriquement S2.6 sur PR-11** (cycle de vie projet IA — 1er score parfait 81/81 sans Lot Drer, validation AP-7 réussie en prévention) :

1. **H2 autonome stricte** : chaque concept propre du module pivot devient une H2 dédiée et sémantiquement autonome, jamais une simple subdivision H3 d'une H2 large. Cas-école PR-11 : tableau 9 étapes en H2 dédiée + 3 quality gates en H2 dédiée + tableau coûts courts-circuits en H2 dédiée + cas-école order-to-cash en H2 dédiée + tableau articulation préalables/DEP en H2 dédiée.

2. **Lead-scope restreint (AP-7 préventif)** : le lead du module pivot doit contenir dès la première phrase en gras le **vocabulaire propre** du module (« 9 étapes séquencées non interchangeables », « 3 quality gates obligatoires », « carte de navigation bout en bout ») PLUTÔT QUE le vocabulaire transverse générique (« projet IA », « cycle », « étapes »). Les termes génériques restent présents mais associés systématiquement aux mots-clés ancrants spécifiques.

3. **Chunking ≤ 900 tokens strict** : tolérance R3 800-900 tokens applicable mais à ne pas dépasser sur un module pivot — la densité crosslinks augmente naturellement la taille effective des chunks à l'embedding du fait de la répétition de vocabulaire transverse. Si une H2 du module pivot dépasse 900 tokens, refactoring H3 obligatoire (cf. R3).

4. **Audit AP-7 préventif** : à la production, lister 5-6 questions hors scope que le module pivot ne doit PAS dominer en top-5. Vérifier visuellement le lead avant Lot I. Pas besoin de Lot Drer si la discipline est appliquée à la production.

**Application** : pour tout module identifié comme pivot avant production (typiquement : modules de type « cycle de vie », « cartographie transverse », « framework structurant cross-domaines »), appliquer le pattern dès la conception MD. Indication ex-ante au brief sprint si module pivot prévu.

**Distinction vs procédure normée Lot Drer + N1/N2/N3** : le pattern module pivot est **préventif** (appliqué à la production from scratch), la procédure Lot Drer + N1/N2/N3 est **curative** (appliquée post-régression détectée par Lot I). Les deux sont complémentaires.

---

## Validation — Eval réelle comme garde-fou structurel (issue RAPPORT-CC-S2.2 §6 P4)

Tests unitaires mockés et eval réelle ont des rôles complémentaires non substituables :

- **Tests unitaires mockés** valident le **contrat de chaque brique** (fonction d'extraction, parser frontmatter, audit-md-rag, ingestion, query) — ils répondent à la question « le code respecte-t-il son contrat ? ».
- **Eval réelle sur le golden set** valide **l'effet observé bout-en-bout** sur le vrai corpus — elle répond à la question « le pipeline produit-il les résultats attendus quand on lui donne le vrai vault ? ».

**Règle structurelle (post-S2.2)** : toute évolution du pipeline RAG susceptible d'affecter les résultats — modification du `SYSTEM_PROMPT`, des regex d'extraction (`extract_cited_codes`, autres parsers réponse), du modèle (LLM, embedding), du chunking, des paramètres de retrieval/reranking — doit déclencher un **rejeu eval golden set complet** sur le vault courant **avant clôture du sprint**, en complément des tests unitaires.

**Pourquoi** : les deux anomalies S2.2 (YAML int + bug extraction wikilinks) ont été détectées exclusivement par eval réelle, pas par les 171 tests unitaires verts. Les mocks ne peuvent pas capter l'écart entre le format réel produit par le LLM et l'attendu de l'extraction.

**Mise en œuvre** : à inscrire dans tout brief Plateforme/Desktop qui touche au pipeline. Cible-discipline budgétaire : un rejeu eval = ~0,70 $ Anthropic (estimation S2.2 sur 30 questions, Sonnet 4.6), à intégrer dans le cap durci sprint.

### Sondage D-026 systématique pour production from scratch (issue RAPPORT-CC-S2.4 §6 P3, validé empiriquement S2.3 + S2.4)

Tout module produit **from scratch** (sans précédent MD dans le vault, c'est-à-dire première production de ce code module) doit faire l'objet d'un **sondage préalable D-026** au canal détenteur de la source canonique HTML (Cowork Hub IA dans la configuration POC).

**Format du sondage** : draft Cowork-side `briefs/DRAFT-SONDAGE-COWORK-HUB-IA-S{N}-{slug}.md` listant 3-15 sous-passages sensibles avec **hypothèses Cowork** sur chaque passage. Le sondage cible en priorité :
- Les **chiffres exacts** à transposer textuellement (R10 stricte)
- Les **énumérations canoniques** (ordre, complétude)
- Les **cas-écoles nommés** (Klarna, Tea App, OpenClaw, etc.) — risque de confusion entre cas-écoles
- Les **frameworks structurants** (les 7 dimensions cu-026, les 4 patterns Frontier Firms, etc.)
- Les **risques de duplication ou chevauchement** entre modules

**Retour attendu** : `briefs/RETOUR-SONDAGE-COWORK-HUB-IA-S{N}.md` (~1500-3500 mots selon volume) avec, pour chaque passage : confirmation/rectification de l'hypothèse Cowork + citation textuelle de la formulation canonique HTML + arbitrage éditorial si pertinent (notamment extraction transverse D-025).

**Effort estimé** : 1h Cowork (rédaction sondage) + 60-90 min Cowork Hub IA (retour) + intégration au moment de la production = **~2-3h de surcoût par module ou groupe de modules**. **Gain attendu** : 1-4 dérives sémantiques majeures évitées par sprint (validation empirique S2.3 = 4 dérives évitées, S2.4 = 1 rectification critique sur tableau DEP-02 §4).

**Sondage global vs sondages séparés** : pour un sprint produisant plusieurs modules from scratch simultanément (cas Lot F.5 S2.5 = 8 modules), un **sondage global unique** sur l'ensemble des modules est plus efficace (1 session Cowork Hub IA ~60-90 min vs N sessions séparées). Validé empiriquement S2.5.

**Statut** : règle structurelle pour production from scratch. Pour production de patches sur modules existants déjà produits (cas Lot F.3 S2.4 = patches CU-026/CU-027/DEP-08), le sondage D-026 reste recommandé sur les passages denses mais n'est pas systématique.

---

## Discipline opérationnelle Git — Hygiène merge (codifiée SPEC v2.0)

**Issue empirique** : 3 occurrences récurrentes signalées par Cowork Hub IA Desktop sur les sprints S2.3 / S2.4 / S2.5 (PR #84, #86, #88) où un `git stash pop` conflictuel a été committé tel quel avec marqueurs `<<<<<<<` / `=======` / `>>>>>>>` non résolus dans le `JOURNAL-POC-RAG.md` ou le `whitelist-wikilinks-futurs.md`. À chaque occurrence, Desktop a dû nettoyer avant merge final, créant un cycle de revue supplémentaire évitable.

**Discipline à appliquer systématiquement avant tout `git add` post-`git stash pop`** :

```bash
# Vérification obligatoire : aucun marqueur de conflit n'a été oublié
cd /path/to/repo-current
git grep '<<<<<<<' && echo "BLOQUER : conflits non résolus" || echo "OK : aucun conflit résiduel"
```

**Procédure pre-commit normée** :
1. `git stash pop` exécuté
2. Vérification immédiate `git grep '<<<<<<<'` (si non vide → bloquer)
3. Résolution manuelle des conflits (ouvrir chaque fichier signalé, supprimer les marqueurs `<<<<<<<` / `=======` / `>>>>>>>`, garder la version voulue)
4. Re-vérification `git grep '<<<<<<<'` (doit retourner vide)
5. `git add` puis `git commit`

**Application** : à intégrer dans tous les briefs émettant des `git stash pop` (typiquement après pull main pour rapatrier les derniers commits réseau avant ajout de nouveaux changements Cowork-side ou Desktop-side). À documenter dans la procédure-type d'ouverture de sprint des briefs Lot d'ingestion / Lot de production.

**Effort additionnel** : ~5 secondes par stash pop. **Gain** : ~1 cycle de revue Desktop évité par sprint (~15-20 min de coûts cumulés sur 3 PR).

**Justification structurelle** : la discipline est codifiée en SPEC pour bénéficier à tous les acteurs (Cowork, Desktop, Plateforme) et toutes les itérations futures. Pas d'automatisation par hook git Cowork-side (Cowork n'a pas accès au .git/hooks/), mais la discipline est plus simple que la mise en place d'un hook côté Desktop.

**Anti-pattern à éviter** : faire confiance aux warnings éventuels de l'IDE sans relire le fichier modifié post-stash pop. Cas observés où le warning a été masqué par d'autres notifications, ou contourné par habitude.

---

## Performances — Cible latence Sonnet 4.6 (recalibrage post-S2.2)

Cible latence par question recalibrée empiriquement post-S2.2 Lot E.2 sur 30 questions :

| Configuration | Cible latence par question |
|---|---|
| Sonnet 4.6, volumes ~3–5 k tokens in / ~0,5–1,5 k tokens out (RAG standard sur vault < 200 chunks) | **12–18 s acceptable** (mesure moyenne S2.2 : 16,4 s, min 9 s, max 22 s) |
| Sonnet 4.6, vault 200-300 chunks (cas S2.5 vague 5 vault ~250 chunks) | **14-20 s acceptable** (mesure S2.5 Lot I à confirmer) |
| **Sonnet 4.6, vault 300-400 chunks** (cas S2.6 vault 318 chunks) | **p50 ≤ 20 s / p90 ≤ 24 s** (mesure empirique S2.6 Lot I : p50 **19,0 s** / p90 **22,0 s** sur 81q) |
| Sonnet 4.6, vault > 400 chunks (cas vague 7+ projeté) | **À mesurer en sprint dédié** — envisager optimisations : reranking, réduction top-k (5 → 3), cache embeddings, partitioning par axe |
| Sonnet 4.6, volumes > 5 k tokens in (vault > 500 chunks ou retrieval k > 8) | 18–25 s acceptable, à mesurer en sprint dédié |
| Haiku 4.5 sur mêmes volumes (option future S3 si optimisation latence prioritaire) | ~5 s estimé (~3× plus rapide), à mesurer avec impact qualitatif |

**Cible précédente abandonnée** : la cible 5 s/question des briefs S1 et S2.2 était irréaliste pour Sonnet 4.6 sur ces volumes. Elle reste valable comme objectif optimisation S3+ avec Haiku 4.5 si la qualité est maintenue.

**Application briefs futurs** : tout brief Desktop/Plateforme qui exécute une eval doit utiliser la cible 12–18 s/question pour Sonnet 4.6 (vault < 200 chunks) ou 14-20 s/q (vault 200-300 chunks). Ne pas reproduire la cible 5 s du brief S2.2 (corrigée post-mortem dans le RAPPORT-CC-S2.2 §6 P3).

### Surveillance latence pour vault > 300 chunks (codifiée SPEC v2.0)

À partir du moment où le vault dépasse **300 chunks** (cas attendu vague 6+ : production PR-09 + PR-10 + PR-11 fait monter le vault de ~250 à ~285 chunks, puis vagues 7-8 fiches outils +30-50 chunks attendus), un **sprint dédié de mesure latence** doit être planifié pour :

1. **Mesurer empiriquement** la latence p50 / p90 sur l'eval golden set complet à ce volume
2. **Identifier les points d'inflexion** : retrieval ChromaDB (cosine sur N vecteurs), génération Sonnet 4.6 (volumes in), reranking si activé
3. **Recalibrer la cible §Performances** avec la mesure réelle (table à mettre à jour)
4. **Arbitrer si optimisation nécessaire** : bascule Haiku 4.5 sur retrieval seul, top-k reduction, vector store partitioning par axe, etc.

**Déclencheur** : franchissement du seuil 300 chunks lors de la production d'un sprint vague N+. Le RAPPORT-CC du sprint qui franchit ce seuil doit lister la mesure latence p50/p90 et émettre une recommandation §Performances.

**Effort estimé** : ~30 min Desktop (rejeu eval existant + extraction latences depuis JSON report) + ~30 min Plateforme (analyse + reco SPEC v2.x).

**Justification empirique** : vault S2.5 ~250 chunks (mesure post-Lot I 16,4 s/q médiane Sonnet 4.6, stable depuis S2.2 à 155 chunks). Hypothèse intuitive : la latence retrieval ChromaDB scale en O(log N) sur cosine avec index HNSW (négligeable), mais la latence génération Sonnet scale en O(N) avec les tokens in. Tant que la stratégie top-k restant fixe (5), le volume in reste stable → la latence ne devrait pas exploser. **Mais ceci doit être mesuré, pas postulé**.

### Cap budgétaire par sprint (issue RAPPORT-CC-S2.3 §6 P1)

Cap durci par sprint recalibré post-S2.3 (mesure empirique Lot E sur 42 questions = ~0,025 $/q Sonnet 4.6 sur volumes ~3-5k tokens in / ~0,5-1,5k tokens out) :

| Volume eval | Cap durci sprint (Anthropic) | Note |
|---|---|---|
| ≤ 20 questions | 0,55 $ | Cap S2.2 conservé pour évals légères |
| 20-40 questions | 0,90 $ | Cap intermédiaire |
| **40-50 questions** | **1,10 $** | Cap calibré sur S2.3 (42q × 0,025 $/q = 1,05 $ + marge variance ~5 %) |
| 50-60 questions | 1,35 $ | Extrapolation linéaire — à confirmer empiriquement |
| **70-80 questions** | **1,90 $** | Cap calibré sur S2.5 (72q × 0,0253 $/q = 1,82 $ + marge variance 5 %) |
| **80-90 questions** | **2,15 $** | **Cap calibré empiriquement S2.6** (81q × 0,0253 $/q = 2,05 $ + marge variance 5 %) |
| 90-100 questions | 2,40 $ | Extrapolation linéaire — à confirmer empiriquement S2.7 |
| > 100 questions | À cadrer ad hoc | Considérer eval ciblée par sous-ensemble ou bascule Haiku 4.5 |

Le cap durci sprint est une **alerte opérationnelle**, pas un hard-stop absolu (cf. décision S2.2 Lot D). Tant que le cap mensuel D-013 (50 $/mois Anthropic) est respecté, un dépassement de cap durci est acceptable s'il est documenté ex-ante au RAPPORT-CC-* du sprint.

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

### Options CLI de l'audit v2 (implémentées en S2.1, documentées en SPEC v1.4)

L'audit `rag/code/audit/audit-md-rag.py` accepte ces options (cumulables) pour ajuster le niveau de strictness :

- **`--strict-future`** : transforme les warnings R4 « wikilink vers code whitelisté » en erreurs bloquantes. À activer en CI quand la whitelist doit être maintenue stricte (typiquement post-vague 3 ou pré-publication).
- **`--strict-r6`** : transforme les warnings R6 « chiffre orphelin » en erreurs bloquantes. À activer pour un audit éditorial ponctuel ou en CI durcie.

**Combinaison courante pré-publication** : `audit-md-rag.py --strict-future --strict-r6` pour audit strict (0 warnings tolérés).

### Roadmap audit v3 (post-vague 3, à activer selon RetEx d'usage)

14. **R5 v3 « première occurrence seulement »** : R5 v2 actuelle (S2.1) signale toute occurrence d'un terme glossaire utilisé en clair (51 warnings observés). Évolution prévue en audit v3 : ne signaler que la première occurrence par fichier MD, pour encourager le wikilink initial sans saturer le texte de wikilinks répétés. Mise en œuvre conditionnelle à un RetEx post-vague 3 confirmant le besoin.
15. **R11 — outil glossarié doit wikilinker vers sa fiche** (inspiré couple 1 v3.9 Règle I.1 « cross-site outils ») : toute mention dans un MD d'un outil ayant sa propre fiche `outils-{categorie}.md` doit la wikilinker à sa première occurrence dans le fichier. Application différée à audit v3, après que 5+ fichiers `outils-*.md` soient produits dans le vault (actuellement 1 seul : `outils-vector-db.md`).

---

## Historique des versions

| Version | Date | Modification |
|---|---|---|
| v1 | 11 mai 2026 | Version initiale, 8 règles essentielles |
| v1.1 | 11 mai 2026 | + R9 (citation textuelle chiffres canoniques, règle stricte issue retour I-002) ; + section méthodologique « briques transverses » (D-025) ; enrichissement anti-patterns (AP-2 conversion monétaire, AP-3 édulcoration contextuelle) ; ajout glose « On-premise » au glossaire (alignement RULES §C.2)|
| v1.2 | 12 mai 2026 | + R10 (transposition fidèle des valeurs numériques dans les tableaux, règle stricte issue retour I-003) ; AP-4 promu en règle R10 plutôt qu'anti-pattern documenté ; audit R10 ajouté à la roadmap v2 audit-md-rag.py |
| v1.3 | 12 mai 2026 | + Exception structurelle R1 pour fichiers racines transverses (D-028, issue S1bis catégorie A) ; + Politique des wikilinks vers MD planifiés (D-029, issue S1bis catégorie B) ; roadmap audit v2 enrichie de 3 évolutions (exception R1, R4 tolérante, R6 reconnaît wikilinks canoniques) |
| v1.4 | 12 mai 2026 | + Codification R6 warning par défaut (issue RAPPORT-CC-S2.1 §5 P1 — convention déjà appliquée empiriquement par Claude Code Plateforme audit v2) ; + Documentation des options `--strict-future` et `--strict-r6` (issue P3) ; + Roadmap audit v3 enrichie : R5 v3 « première occurrence seulement » (P2 reportée audit v3) et R11 « outil glossarié wikilinké » (inspiré couple 1 v3.9 Règle I.1 cross-site outils, application différée audit v3) |
| v1.5 | 13 mai 2026 | Intégration des 4 propositions RAPPORT-CC-S2.2 §6 (validation Cowork post-clôture S2.2) : (1) AP-5 valeurs numériques non quotées dans `expected_concepts` (anti-pattern fort, validation visuelle au commit Cowork) ; (2) Formalisation des deux patterns d'extraction côté code RAG — `WIKILINK_CITATION_PATTERN` préféré + `BRACKET_CITATION_PATTERN` rétro-compat (sous-section dans R4) ; (3) Nouvelle section §Performances : recalibrage cible latence Sonnet 4.6 à 12-18 s/question (cible 5 s S1/S2.2 abandonnée comme irréaliste) ; (4) Nouvelle section §Validation : eval réelle comme garde-fou structurel pré-clôture sprint (toute évolution prompt/regex/modèle/chunking déclenche rejeu eval, mocks ≠ substituable). |
| v1.6 | 13 mai 2026 | Intégration des 4 propositions RAPPORT-CC-S2.3 §6 (validation Cowork post-clôture S2.3 — sprint clôturé à 41/42 score global) : (1) Cap budgétaire par sprint formalisé en §Performances (recalibrage 0,90 $ → 1,10 $ pour 42q, table par volume) ; (2) Précision D-025 en §Briques transverses : « ossature complète d'un module ≠ brique transverse extractible » (validé empiriquement RETOUR-SONDAGE sur pattern « agent = employé » CU-026) ; (3) AP-6 : synonymes excessifs dans `expected_concepts` liste de listes (plafond 2-4 synonymes, anti-faux-positifs) ; (4) Nouvelle section §Conception MD et questions golden set : garde-fou « concepts détaillés » (sub-section H3 dédiée + format `expected_concepts` tolérant aux variations numériques, issue diagnostic q-038). |
| v1.8 | 20 mai 2026 | Intégration des 3 propositions RAPPORT-CC-S2.4 §6 (validation Cowork post-clôture S2.4 — sprint clôturé à 50/52 score global) : (1) **AP-7 « Lead bridge sur-élargi »** dans §Anti-patterns (symétrique inverse du garde-fou « concepts détaillés » v1.6 — cas-école pr-08 saturant top-5 sur q-002 + q-030 transversales) ; (2) **Tolérance R3 800-900 tokens** si chunk thématiquement cohérent (validé empiriquement chunk Frontier Firms cu-026 850 tokens) ; (3) **Sondage D-026 systématique pour production from scratch** dans §Validation (validé empiriquement 2 sprints S2.3 + S2.4, 4 + 1 dérives évitées). Précision empirique post-Lot D-ter ajoutée à §R3 sur les 2 conditions nécessaires et indissociables : chunking H2 autonome + lead bridge enrichi. |

| v1.9 | 22 mai 2026 | Inscription du **pattern empirique « 3 niveaux d'intervention retrieval »** dans §Conception MD (précision opérationnelle du garde-fou « concepts détaillés ») : (1) Lead bridge enrichi (validé Lot D-ter S2.4.1 — q-038 rang ≥11 → #1) ; (2) H2 dédiée concurrente si saturation par module dominant (validé Lot S2.5.0-bis — q-030 #13 → #6) ; (3) Densification chirurgicale du lead par répétition contrôlée si chunk concurrent hors top-5 (validé Lot S2.5.0-ter — q-030 #6 → #3). Cas-école q-030 (3 itérations Lot S2.5.0/bis/ter) documenté empiriquement. |
| **v2.0** | **22 mai 2026** | Intégration des 3 propositions RAPPORT-CC-S2.5 §6 (validation Cowork post-clôture S2.5 — sprint clôturé à 72/72 score global extrapolé) : (1) **§Discipline opérationnelle Git — Hygiène merge** : procédure pre-commit normée `git grep '<<<<<<<'` obligatoire post-`git stash pop` (issue 3 occurrences récurrentes PR #84/#86/#88 S2.3/S2.4/S2.5 signalées par Desktop) ; (2) **Procédure normée « Lot Drer + N1/N2/N3 »** ajoutée à §Conception MD : diagnostic Lot Drer ciblé d'abord (~0,10-0,20 $) puis choix du niveau d'intervention selon écart résiduel (Niveau 1 si rang #6-#10, Niveau 2 si saturation par module concurrent, Niveau 3 si gap résiduel < 0,02 sim) — anti-pattern « sauter directement au Niveau 3 sans diagnostic » documenté ; (3) **§Performances surveillance latence vault > 300 chunks** : déclencheur sprint dédié de mesure quand vault franchit 300 chunks (cas attendu vague 6+ → ~285 chunks puis ~330 chunks fiches outils). Table §Performances enrichie d'une ligne « vault 200-300 chunks » + ligne « vault > 300 chunks à mesurer ». |
| **v2.1** | **22 mai 2026** | Intégration des 3 propositions RAPPORT-CC-S2.6 §6 (validation Cowork post-clôture S2.6 — **1er score parfait 81/81** sur vault 26 MD / 318 chunks, sans Lot Drer en cascade) : (1) **Recalibrage cap coût** §Performances : table Cap budgétaire enrichie de 3 lignes empiriques 70-80q (1,90 $ calibré S2.5), **80-90q (2,15 $ calibré S2.6)**, et 90-100q (2,40 $ extrapolation à confirmer S2.7) — dépassement +2,5 % mécanique S2.6 documenté ; (2) **Extension bande latence vault 300-400 chunks** §Performances : ligne « > 300 chunks à mesurer » de v2.0 remplacée par mesure empirique S2.6 — **p50 ≤ 20 s / p90 ≤ 24 s** (mesure réelle p50 19,0 s / p90 22,0 s sur 81q vault 318 chunks) + recommandations optimisations pour vault > 400 chunks (reranking, top-k réduction 5→3, cache embeddings, partitioning par axe) ; (3) **Pattern « production module pivot dense »** ajouté à §Conception MD : H2 autonome stricte + lead-scope restreint (AP-7 préventif) + chunking ≤ 900 tokens + audit AP-7 préventif à la production — validé empiriquement PR-11 (629 lignes HTML, 9 H2 dédiées, score parfait sans Lot Drer). Distinction explicite vs procédure normée Lot Drer + N1/N2/N3 : pattern module pivot = **préventif** (production from scratch), Lot Drer + N1/N2/N3 = **curatif** (post-régression Lot I). |

**Évolution prévue** : enrichissement en v2.2+ post-S2.7 sur la base de la production vague 7 (5 fiches outils prioritaires) + extension run_eval mode adversarial (10-15 questions hors-corpus / pièges pour stress-tester le refus du RAG). Mesure empirique latence vault > 400 chunks projetée post-vague 7 (vault ~360-380 chunks attendu).
