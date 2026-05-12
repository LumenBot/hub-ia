# BRIEF-CC-S2.1 — Audit-md-rag v2 (alignement SPEC v1.3)

**Émetteur :** Cowork Hub IA Plateforme
**Destinataire :** Claude Code Hub IA Plateforme (session web — pas besoin de clés API en S2.1)
**Garant transverse :** Blaise Cavalli
**Sprint :** S2.1 (audit v2 — prérequis aux sprints suivants)
**Allocation D-030 :** Claude Code Plateforme **seul** (refactor code + tests + exécution audit sur vault, aucun appel API externe)
**Statut :** v1, à transmettre

---

## 1. Métadonnées

- **Repo cible :** `hub-ia` (partir de `main` post-merge PR #44, commit `9bef8c4`)
- **Sprint précédent :** S1ter (clôturé définitivement par merge PR #44 le 12 mai)
- **Nature de l'itération :** refactor de `rag/code/audit/audit-md-rag.py` pour aligner avec SPEC v1.3 + 6 nouvelles règles (R5, R6 étendu, R7, R8, R9, R10) + 2 décisions structurantes (D-028 exception R1, D-029 whitelist R4)
- **Coût API attendu :** **0,00 $** (l'audit ne fait aucun appel API externe — refactor de code Python pur)

---

## 2. Contexte court

Sprint S1bis Lot S1b.1 a produit 150 écarts bruts sur le vault réel, dont **0 violation éditoriale claire de SPEC v1.2 après classification** (cf. `rag/eval/audit-report-s1bis.md`). Tous les écarts sont des **limitations de l'audit v1** antérieur à SPEC v1.2/v1.3 :
- 2 faux positifs R1 sur le glossaire (champs vides par construction — D-028)
- 83 faux positifs R4 sur wikilinks vers MD futurs (vague 3+ — D-029)
- ~58 faux positifs R6 sur chiffres dans alias de wikilinks vers `chiffres-macro-2026.md` (R9 introduite après audit v1)
- ~7 chiffres orphelins potentiels (catégorie D — déjà arbitrés par Cowork dans étape B post-S1bis)

L'audit v2 doit aligner l'audit avec SPEC v1.3 actuelle, éliminer les faux positifs, et activer les règles R5/R7/R8/R9/R10 documentées en roadmap audit v2 de SPEC §Validation.

**Bénéfice attendu** : avant production vague 3 (CU-026, CU-027, DEP-08), le vault de 9 fichiers doit passer un audit propre (0 erreurs, possiblement quelques warnings tolérés). Ainsi la production de la vague 3 démarre sur un état conforme.

---

## 3. Préalable obligatoire (lectures avant code)

À lire dans cet ordre, intégralement :

1. **Ton propre rapport audit S1bis** : `rag/eval/audit-report-s1bis.md` (méthodologie + classification + 6 propositions audit v2)
2. **SPEC v1.3** : `rag-prep/SPEC-MD-POUR-RAG.md` (10 règles canoniques + section « Exception structurelle » + politique R4 wikilinks futurs + roadmap audit v2 §Validation point 11-13)
3. `rag-prep/DECISIONS-RAG.md` — 30 décisions actées, focus sur **D-028** (exception R1) + **D-029** (whitelist) + **D-023** (nouvelle règle = nouvelle fonction d'audit, à respecter inversement)
4. `rag-prep/whitelist-wikilinks-futurs.md` — 69 codes whitelistés à lire au runtime pour R4
5. `rag-prep/content/transverses/chiffres-macro-2026.md` — 16 chiffres canoniques à parser pour R9
6. `rag-prep/_instructions-rag.md` v1 + STATUS-RAG.md à jour (sprint S1 clôturé)
7. **Ton audit v1 actuel** : `rag/code/audit/audit-md-rag.py` (pour comprendre la structure existante avant refactor)

**Audit de départ obligatoire** (D-018) : `git fetch && git status` sur `hub-ia`, partir d'un main à jour incluant le merge PR #44.

---

## 4. Méthode — 5 blocs de refactor + 1 bloc exécution

### Bloc A — Implémenter D-028 (exception R1) + D-029 (whitelist R4)

**Livrables** :

1. **Exception R1 pour fichiers racines transverses** :
   - Si `frontmatter.code == "glossaire"` OU si `frontmatter.type == "transverse"` ET le fichier est racine canonique (à définir : critère pragmatique « fichier ne dépendant d'aucun autre par construction » — ex. glossaire.md, chiffres-macro-2026.md) → autoriser `glosaire_termes: []` et `derives: []`
   - Documenter le critère dans le code (commentaire ou docstring)
2. **Whitelist R4** :
   - Au démarrage de l'audit, charger `rag-prep/whitelist-wikilinks-futurs.md` (parser les codes whitelistés depuis les tableaux markdown)
   - Pour chaque wikilink vers un code absent du vault :
     - Si le code est dans la whitelist → produire un **warning** (sortie distincte des erreurs, exit code reste 0)
     - Sinon → erreur réelle (exit code non-zéro)
   - Ajouter une option CLI `--strict-future` qui transforme les warnings en erreurs (utile pour CI quand on veut bloquer l'élargissement de la whitelist)

**Tests** : étendre `test_audit_md_rag.py` avec fixtures (glossaire avec champs vides → valide ; module ordinaire avec champs vides → erreur ; wikilink vers code whitelisté → warning ; wikilink vers code inconnu → erreur).

**Commit attendu** : `feat(rag-audit): D-028 exception R1 glossaire + D-029 whitelist R4 wikilinks futurs`.

---

### Bloc B — Implémenter R5, R7, R8 (alignement SPEC §Validation)

**R5 — glossaire** : tout terme listé dans `glossaire.md` (sections H2) utilisé dans un autre MD doit l'être via wikilink `[[glossaire#terme]]`, pas en clair. Sortie : erreur (ou warning si on veut être doux la première itération).

**R7 — nommage** : conformité du nom de fichier au schéma `{type}-{numero}.md` pour modules/préalables/DEP/architectures, ou `outils-{categorie}.md` pour fiches outils, ou `{slug}.md` pour transverses et `glossaire.md` pour le glossaire. Erreur si non conforme.

**R8 — versioning** : `last_updated` du frontmatter doit être cohérent avec la dernière modification git du fichier (< 7 jours d'écart). Utiliser `git log -1 --format=%ct {file}` pour la date Git. Erreur si écart > 7 jours.

**Tests** : fixtures pour chaque règle (conforme + non conforme).

**Commit attendu** : `feat(rag-audit): R5 glossaire + R7 nommage + R8 versioning git`.

---

### Bloc C — Convergence R6 ↔ R9 + implémentation R9 (chiffres macro)

**R6 étendu** (proposition 13 SPEC §Validation v2) : étendre `SOURCE_MARKERS` pour reconnaître `\[\[chiffres-macro-\d{4}[^\]]+\]\]` (et plus généralement `\[\[transverses?/[^\]]+\]\]`) comme source canonique. Cela élimine les ~58 faux positifs R6 catégorie C identifiés en S1bis.

**R9 — chiffres macro canoniques** : 
1. Au démarrage, parser `rag-prep/content/transverses/chiffres-macro-2026.md` pour extraire les 16 chiffres canoniques (chaque section H2 = un chiffre, regex sur le titre pour extraire la valeur numérique + source)
2. Pour chaque MD du vault, détecter les valeurs numériques pouvant correspondre à un chiffre canonique (`95 %`, `67 %`, `1,8 h`, `21 %`, etc.)
3. Si le chiffre est cité en clair (pas via wikilink vers `chiffres-macro-2026.md`) → erreur (sauf si le fichier source est `chiffres-macro-2026.md` lui-même)

**Tests** : fixtures (chiffre macro wikilinké → valide ; chiffre macro en clair → erreur ; chiffre macro dans chiffres-macro-2026.md → valide).

**Commit attendu** : `feat(rag-audit): R6 étendu (wikilinks transverses comme source) + R9 chiffres macro canoniques`.

---

### Bloc D — Implémenter R10 (tableaux numériques fidèles)

**R10** : la règle la plus complexe. Comparer les valeurs numériques des tableaux MD avec celles du HTML source correspondant.

1. Mapping `code → fichier HTML` : à inscrire dans le code (ex. `cu-008` → `modules/cu-008-knowledge-base-rag.html`)
2. Pour chaque MD avec un tableau (markdown `|...|...|`), extraire les valeurs numériques (regex sur seuils, fourchettes, montants, durées, pourcentages)
3. Charger le HTML source correspondant, extraire le texte (BeautifulSoup ou regex simple), extraire les mêmes patterns numériques
4. Pour chaque valeur numérique MD, chercher une correspondance proche dans le HTML (tolérance regex sur fourchettes du genre `40-100` ↔ `40 à 100`)
5. Signaler en erreur les valeurs MD qui ne se retrouvent **pas** dans le HTML source

**Note pragmatique** : R10 est imparfaite par construction (le texte MD est distillé, le HTML source plus verbeux). Acceptable de produire des **warnings** plutôt que des erreurs pour la première implémentation, à durcir progressivement.

**Tests** : fixtures (tableau MD aligné HTML source → valide ; tableau MD avec valeur élargie → warning).

**Commit attendu** : `feat(rag-audit): R10 transposition fidèle valeurs numériques tableaux`.

---

### Bloc E — Exécution audit v2 sur vault réel + RAPPORT + PR

**Exécution** :
```bash
python3 rag/code/audit/audit-md-rag.py --vault rag/content --report rag/eval/audit-report-s2.1.md
```

**Résultat attendu** : 
- **0 erreurs** (les 150 écarts S1bis désormais classés correctement)
- **Quelques warnings** acceptables (notamment R10 imparfaite, ~7 chiffres catégorie D arbitrés en S1bis comme acceptables)
- Exit code 0

Si erreurs détectées → signaler à Blaise sans corriger les MD (D-022 spécialisation des rôles).

**RAPPORT-CC-S2.1.md** dans `rag-prep/briefs/` (~1500 mots, structure modèle) :
1. Synthèse exécutive (5 blocs traités, écarts résiduels)
2. Détail par bloc avec extraits de tests + résultats audit
3. Comparaison audit v1 vs audit v2 sur le vault (150 écarts bruts → X erreurs + Y warnings)
4. Écarts résiduels signalés
5. Proposition d'amendement SPEC le cas échéant
6. Recommandations pour S2.2 et S2.3
7. Liste des commits S2.1

**PR vers main** :
- Titre : `feat(rag): Sprint S2.1 - audit-md-rag v2 aligné SPEC v1.3 (10 règles + 30 décisions)`
- Description : pointer vers RAPPORT-CC-S2.1, lister les commits S2.1, mentionner les 6 nouvelles règles implémentées + alignement audit v1.3

**Commit attendu** : `docs(rag): rapport S2.1 + ouverture PR audit v2`.

---

## 5. Estimation effort consolidée

| Bloc | Effort estimé |
|---|---|
| A — D-028 + D-029 | 1 h |
| B — R5 + R7 + R8 | 1 h |
| C — R6 étendu + R9 | 1-1,5 h |
| D — R10 (le plus complexe) | 2-3 h |
| E — Exécution + RAPPORT + PR | 1 h |
| **Total** | **~6-7,5 h Claude Code Plateforme** |

**Coût API estimé** : **0 $** (refactor code + tests sans appel API externe).

---

## 6. Workflow recommandé

1. Confirmer la lecture des préalables (« Sync state lue, je m'apprête à faire X »).
2. Enchaîner les 5 blocs A → B → C → D → E. Ne pas commencer un bloc si le précédent n'a pas ses tests verts.
3. Commits granulaires par bloc.
4. PR ouverte à la toute fin (Bloc E).

---

## 7. Règles de prudence

1. **Pas de modification des MD du vault** (D-022). Si l'audit v2 détecte des écarts → signaler à Blaise sans corriger.
2. **Pas de modification de R1, R2, R3, R4 existants au-delà des exceptions D-028/D-029** : extension uniquement.
3. **Pas de cassure des 67 tests existants** : ajouts uniquement, refactor non destructif.
4. **R10 peut être laissée en warning** pour la première itération si l'implémentation pleine erreur est trop complexe — pragmatisme accepté.

---

## 8. Décisions explicites de NE PAS faire

1. ❌ Pas de production de fichiers MD du vault (rôle Cowork D-022)
2. ❌ Pas de modification des fichiers de gouvernance dans `rag-prep/` (sauf JOURNAL, STATUS, et ton propre RAPPORT)
3. ❌ Pas d'extension du golden set ou de la stack RAG (scope S2.2 / S2.3)
4. ❌ Pas de merge automatique de la PR (Blaise valide manuellement)

---

## 9. Validation finale avant PR

- [ ] D-028 implémentée (exception R1 fichiers racines transverses) + tests verts
- [ ] D-029 implémentée (whitelist R4 wikilinks futurs) + tests verts + option `--strict-future`
- [ ] R5 (glossaire), R7 (nommage), R8 (versioning git) implémentées + tests verts
- [ ] R6 étendu (wikilinks transverses comme source) + R9 (chiffres macro canoniques parsés depuis chiffres-macro-2026.md) + tests verts
- [ ] R10 (tableaux numériques fidèles) implémentée en warning ou erreur + tests verts
- [ ] Suite complète des tests : 67 originaux + N nouveaux (estimés 15-25 nouveaux tests)
- [ ] Audit v2 exécuté sur le vault : **0 erreurs** attendues, warnings tolérés et documentés
- [ ] `RAPPORT-CC-S2.1.md` produit en 7 sections
- [ ] PR ouverte avec titre conforme
- [ ] `JOURNAL-POC-RAG.md` mis à jour (append S2.1)
- [ ] `STATUS-RAG.md` mis à jour (Sprint S2.1 ✅, S2.2 prêt)

---

## 10. Fichiers de référence

**Référentiels du couple 2** (`rag-prep/` du clone Git) :
- `_instructions-rag.md` v1
- `DECISIONS-RAG.md` (30 décisions actées dont D-028, D-029, D-030)
- `SPEC-MD-POUR-RAG.md` v1.3 (10 règles + exception structurelle + politique whitelist + roadmap audit v2 §Validation)
- `whitelist-wikilinks-futurs.md` (69 codes whitelistés)
- `STATUS-RAG.md` (sprint S2.1 ouvert)
- `JOURNAL-POC-RAG.md`
- `briefs/RAPPORT-CC-S1.md` + `RAPPORT-CC-S1bis.md` + `RAPPORT-CC-S1ter.md`

**Contact** : Blaise Cavalli (garant transverse).

---

*Brief produit le 12 mai 2026. Volume : ~2000 mots (cible D-021 respectée). Allocation D-030 : Claude Code Plateforme seul (pas besoin de clés API ni de Desktop pour S2.1).*
