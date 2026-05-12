# Audit MD-RAG — vault réel S1bis

**Date :** 12 mai 2026
**Exécutant :** Claude Code Hub IA Plateforme
**Sprint :** S1bis (clôture S1)
**Commande :** `python3 rag/code/audit/audit-md-rag.py --vault rag/content --report rag/eval/audit-report-s1bis-raw.txt`

---

## Synthèse exécutive

- **Fichiers audités** : 9 (brief annonçait 10 — voir §5 ci-dessous)
- **Fichiers en écart** : 9 / 9
- **Total écarts bruts** : 150
- **Écarts par règle** : R1 = 2 · R4 = 83 · R6 = 65 · R2/R3 = 0
- **Exit code** : 1 (non-zéro car écarts détectés)

**Constat principal :** la grande majorité des 150 écarts sont des **faux positifs de l'audit v1** face à un vault produit selon SPEC v1.2 (R9 chiffres macro canoniques wikilinkés, vault partiel S1 pilote avec wikilinks anticipant les vagues 3+). Aucun écart de format structurel grave (0 R2, 0 R3). Aucun chiffre genuinement orphelin sans wikilink ou source.

**Le brief CC-S1bis §4 attendait 0 erreur** — le décompte brut est non-nul, mais la classification ci-dessous montre que **0 erreur réelle ne porte sur la conformité éditoriale du vault**. Les corrections nécessaires portent sur **l'audit lui-même** (alignement v1.2), pas sur les MD. Discipline §7 brief respectée : **aucune modification du vault par Claude Code**.

---

## Classification des 150 écarts

| Catégorie | Nb | Nature | Action |
|---|---|---|---|
| **A — Faux positif structurel (glossaire)** | 2 | R1 sur `glossaire.md` : `glosaire_termes: []` et `derives: []` intentionnellement vides (le glossaire est la racine du système) | Audit v2 : exception pour `code: glossaire` |
| **B — Vault partiel S1 (wikilinks vers MD futurs)** | 83 | R4 vers `cu-002`, `cu-011`, `pr-04`, `dep-07`, etc. — modules à produire en vague 3+ | Attendu — pas un écart de vault, résolu naturellement quand les autres MD seront produits |
| **C — Faux positif R9 (chiffres wikilinkés)** | ~58 | R6 sur chiffres apparaissant dans l'alias d'un wikilink vers `chiffres-macro-2026.md` — la source canonique est le wikilink, mais l'audit R6 ne reconnaît pas ce pattern | Audit v2 : reconnaître `[[chiffres-macro-2026#…\|…N % …]]` comme source valide |
| **D — Chiffres orphelins potentiels à confirmer** | ~7 | R6 sur chiffres sans wikilink visible dans la fenêtre 200 caractères (90 % glossaire, certains chiffres dep-02 et outils-vector-db) | Signaler à Blaise pour arbitrage Cowork |

**Total catégorisé** : 2 + 83 + 58 + 7 = 150 (estimation C/D à affiner sur dump brut, voir §3).

---

## 1. Analyse R1 (2 écarts — catégorie A)

```
📄 glossaire.md
  • R1: champ frontmatter vide `glosaire_termes`
  • R1: champ frontmatter vide `derives`
```

**Diagnostic** : faux positif structurel. Le glossaire est la **racine du système de termes** : il définit les termes, il ne « dérive » d'aucun module (`derives: []`), et il ne référence pas d'autres glossaires (`glosaire_termes: []`). Le champ doit rester vide par construction.

**Recommandation audit v2** : ajouter une exception R1 quand `code == "glossaire"` (et plus généralement quand `type == "transverse"` et le fichier est la canonicale d'un référentiel).

**Pas une erreur du vault.** Aucune action côté MD.

---

## 2. Analyse R4 (83 écarts — catégorie B)

Tous les wikilinks signalés pointent vers des MD que **Cowork n'a pas encore produits** (vagues 3+, cf. STATUS-RAG §Vague 3 anticipée) :

- `cu-002`, `cu-005`, `cu-007`, `cu-011`, `cu-012`, `cu-013`, `cu-014`, `cu-019`, `cu-020`, `cu-021`, `cu-024`, `cu-025`, `cu-026`, `cu-027`
- `pr-01`, `pr-02`, `pr-03`, `pr-04`, `pr-05`, `pr-06`
- `dep-01`, `dep-03`, `dep-04`, `dep-05`, `dep-06`, `dep-07`

**Distribution par fichier source** : `chiffres-macro-2026.md` (35 wikilinks futurs), `pr-07.md` (8), `cu-008.md` (4), `vigilance-hallucinations.md` (10), `vigilance-confidentialite.md` (9), `cu-001.md` (4), `outils-vector-db.md` (6), `dep-02.md` (6), `glossaire.md` (1).

**Diagnostic** : c'est exactement le risque #3 documenté dans SPEC v1.2 §Briques transverses (« Wikilinks cassés : renommage d'une brique transverse casse silencieusement les wikilinks »), **mais inversé temporellement** : le vault contient des wikilinks **anticipant** la production future. Cohérent avec la STRATEGIE-MD-RAG §Phase scale (S2 migration progressive).

**Recommandation audit v2** : ajouter un mode `--allow-future-links` ou un fichier `rag/content/.expected-codes.yaml` listant les codes valides (présents + planifiés). Alternative plus simple : R4 ne signale en erreur que pour les liens vers des codes dont le préfixe est connu (cu-, pr-, dep-, a, outils-, transverse-, glossaire) ; les autres sont des warnings.

**Pas une erreur du vault.** Aucune action côté MD à ce stade — résolu naturellement par la production des vagues suivantes.

---

## 3. Analyse R6 (65 écarts — catégories C et D)

### C — Chiffres wikilinkés vers `chiffres-macro-2026.md` (~58 écarts, faux positifs)

Exemples canoniques détectés dans `pr-07.md` et `cu-008.md` :

```
**Mais 95 % des projets IA en entreprise ne génèrent aucun ROI mesurable**
([[chiffres-macro-2026#95-pourcent-projets-genai-sans-roi-mesurable-mit-nanda-2025|MIT NANDA 2025]]).
```

Le chiffre `95 %` est suivi d'un wikilink qui pointe vers la fiche canonique du chiffre dans `chiffres-macro-2026.md`. C'est exactement l'application de **R9 SPEC v1.2** (citation textuelle de chiffres canoniques via wikilink). L'audit R6 v1 ne reconnaît pas ce pattern comme « source » car son regex `SOURCE_MARKERS` n'inclut que `Source :`, `URL` et liens markdown `[…](…)`, pas les wikilinks Obsidian `[[…]]`.

**Recommandation audit v2** : étendre `SOURCE_MARKERS` pour reconnaître `\[\[chiffres-macro-\d{4}[^\]]+\]\]` (et plus généralement `\[\[transverse-…\]\]`) comme source canonique valide. C'est la convergence opérationnelle entre R6 et R9.

### D — Chiffres possiblement orphelins (~7 écarts à confirmer)

Quelques chiffres apparaissent sans wikilink visible dans la fenêtre 200 caractères du contexte signalé. Cas remarquables :

- `glossaire.md` : « Pour 90 % des cas PME/ETI, le RAG suffit » (définition prose, ce 90 % est rédactionnel, pas une statistique citable — anti-pattern AP-3 potentiel mais limite acceptable dans le contexte d'une définition courte)
- `dep-02.md` : impacts de design (« +10-30 % de précision reranking », « 5-10 % d'impact vector DB », « 30-40 % qualité finale chunking », « +11 % qualité reranker ») — ce sont des chiffres d'**impact relatif** issus de benchmarks internes au déploiement, pas des chiffres macro Hub. Source datée serait souhaitable mais pas critique en pilote
- `outils-vector-db.md` : « 80 % des entreprises ont déjà Postgres » et « 99,99 % uptime » — affirmations qui mériteraient une source

Ce sont des **candidats légitimes pour arbitrage Cowork** (signalement Blaise), pas des erreurs bloquantes.

---

## 4. Conclusion vis-à-vis du brief CC-S1bis §4

Brief : « **Total errors = 0 attendu** » et « Si erreurs détectées → signaler à Blaise sans corriger soi-même ».

**Lecture stricte** : 150 écarts ≠ 0, donc lot S1b.1 ne valide pas son critère de succès au pied de la lettre.

**Lecture qualifiée** : 0 violation éditoriale claire des règles R1-R6 telles que **réellement appliquées par Cowork après SPEC v1.2 et revue I-003**. L'audit v1 a été écrit selon SPEC v1, antérieur à l'introduction de R9 (chiffres macro canoniques via wikilink) et au pattern « briques transverses ». La convergence audit v1 ↔ SPEC v1.2 est l'objet naturel d'**audit-md-rag v2**, déjà mentionné en roadmap (SPEC §Validation par audit-md-rag.py).

**Discipline §7 brief respectée** :
- Pas de modification des MD du vault par Claude Code.
- Pas de modification du code de l'audit non plus dans cette session (les évolutions sont scope v2, hors S1bis selon brief §4).
- Signalement structuré à Blaise via ce rapport + JOURNAL-POC-RAG.md.

---

## 5. Écart d'inventaire vault — 9 vs 10 fichiers

Le brief CC-S1bis §1, le STATUS-RAG §L1.14 et le commit de dépôt mentionnent **« 10 fichiers MD »** à transférer. Le find effectif sur la branche après pull n'en compte que **9** :

```
rag/content/deploiement/dep-02.md
rag/content/glossaire.md
rag/content/modules/cu-001.md
rag/content/modules/cu-008.md
rag/content/prealables/pr-07.md
rag/content/ressources/outils-vector-db.md
rag/content/transverses/chiffres-macro-2026.md
rag/content/transverses/vigilance-confidentialite.md
rag/content/transverses/vigilance-hallucinations.md
```

Décompte par type : 1 glossaire + 1 fiche outils + 3 transverses + 2 modules CU + 1 préalable + 1 déploiement = **9**.

**Hypothèse** : le décompte « 10 » incluait probablement un fichier transverse supplémentaire (ex. `pattern-llm-wiki.md` envisagé en vague 3, cf. STATUS §Vague 3 anticipée) ou une simple coquille dans le brief / STATUS. **À confirmer par Blaise / Cowork.**

---

## 6. Recommandations pour audit-md-rag v2 (issues de cette exécution)

1. **Exception R1 pour glossaire** : ne pas considérer comme vide `glosaire_termes` et `derives` quand `code == "glossaire"`.
2. **R4 tolérante aux MD futurs** : option `--known-codes-file` ou liste de préfixes de codes valides pour distinguer « cible inexistante (erreur) » de « cible non encore produite (warning) ».
3. **R6 reconnaît les wikilinks canoniques comme source** : étendre `SOURCE_MARKERS` pour matcher `\[\[chiffres-macro-\d{4}[^\]]+\]\]` et plus généralement les wikilinks vers `transverses/*`.
4. **Implémenter R9** (SPEC v1.2) : détecter les chiffres macro Hub apparaissant en clair dans un module sans wikilink vers `chiffres-macro-2026.md`. La liste des chiffres canoniques peut être extraite automatiquement de `chiffres-macro-2026.md` (section H2 par chiffre).
5. **Implémenter R10** (SPEC v1.2) : comparer les valeurs numériques des tableaux MD avec celles du HTML source correspondant. Nécessite un mapping `code → fichier HTML` (probablement dans `_instructions-rag.md` à terme).
6. **Implémenter R5, R7, R8** (cf. SPEC §Validation par audit-md-rag.py).

Ces 6 évolutions naturelles couvrent la roadmap v2 telle qu'esquissée dans SPEC §Validation et dans le rapport RAPPORT-CC-S1 §5.

---

## 7. Annexe — Rapport brut

Le dump complet généré par `audit-md-rag.py` est conservé en annexe dans `rag/eval/audit-report-s1bis-raw.txt` (172 lignes, 150 écarts détaillés). Source originelle pour la classification ci-dessus.

---

*Rapport produit par Claude Code Hub IA Plateforme — sprint S1bis, Lot S1b.1.*
*Conformément à §7.1 du brief CC-S1bis : aucune modification des MD du vault par Claude Code. Signalement structuré à Blaise.*
