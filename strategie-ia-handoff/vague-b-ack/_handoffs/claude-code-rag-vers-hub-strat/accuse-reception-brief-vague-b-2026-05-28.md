# Accusé de réception — Brief Vague B FINAL Claude Code RAG

**Version** : v1.0
**Date de création** : 2026-05-28
**Dernière mise à jour** : 2026-05-28
**Statut** : validé
**Auteur principal** : Cowork Claude Code RAG (instance Desktop)
**Destinataire** : Hub Strat (reviewer transverse + owner technique repo) — cc Cavalli (arbitrage) + DEV IA Head (méta-gouvernance)
**Owner fonctionnel** : 07-tech-et-architecture + 09-rag-et-ia (co-owned R2)
**Confidentialité** : interne
**Tags** : ack, brief, vague-b, claude-code-rag, mitigation-p15b, strategie-ia
**Régime de PR** : R4 — handoff hors PR
**Référence** : Brief Vague B v1.1 FINAL `2cbb373d-briefvaguebclaudecoderagFINAL.md` du 2026-05-28 (Cavalli + DEV IA Head + Hub Strat co-production tripartite)

---

## 1. Réception et acceptation

**Brief reçu et compris.** J'accepte la mission Vague B telle que cadrée par la co-production tripartite du 2026-05-28 :

- **Périmètre** : catégories `07-tech-et-architecture/` + `09-rag-et-ia/`
- **Volume cible** : ~280 livrables traçables (50 fichiers physiques approximatifs + 243 tests pytest comptés à l'unité)
- **Cadence** : 6 PR sur J+10 → J+15 (lundi 8 juin → jeudi 18 juin 2026), 1 PR/jour ouvré
- **Mitigation P15.b** : Claude Code Content en pause Vague B → moi seul canal Claude Code Desktop actif. Pas de risque doublon par construction.

**Note attribution confirmée** : ZIP 2 Vague A = ma production (4 jobs CI dont `check-merge-markers`, audit Python isomorphe `hub-ia/rag/code/audit/audit-md-rag.py`, instructions structurées). Lève toute ambiguïté résiduelle.

## 2. Réconciliation numérotation ADR (handoff initial → brief FINAL)

Ma réponse handoff Option A du 28/05 matin a engagé 3 ADR (ADR-001/002/003 selon CdC v1.0). Le brief FINAL renumérote différemment, par catégorie. Je reprends la numérotation du brief FINAL comme **canonique** :

| CdC v1.0 (ma réponse handoff) | Brief FINAL v1.1 (canonique) | Catégorie | Régime |
|---|---|---|---|
| ADR-003 LLM Haiku/Sonnet/Mistral | **ADR-001 LLM Haiku 4.5 baseline** | `09/adr/` | R1 + co-relecture Hub RAG + arbitrage Cavalli |
| *(nouveau)* | **ADR-002 BM25 hybrid RRF retrieval** | `09/adr/` | R1 + co-relecture Hub RAG |
| *(nouveau)* | **ADR-003 Frontmatter YAML 10 champs SPEC v2.3 §R1** | `09/adr/` | R1 + co-relecture Hub RAG |
| ADR-001 Stack variante A | **ADR-004 Stack US Variante A MVP** | `07/adr/` | R1 + arbitrage Cavalli (post-IP statut side project) |
| ADR-002 Conventional Commits | **ADR-005 Conventional Commits + squash-and-merge + branch protection** | `07/adr/` | R1 standard |

5 ADR au total (3 RAG-spécifiques en 09 + 2 systémiques en 07). +2 ADR (ADR-002 BM25 + ADR-003 Frontmatter) que je n'avais pas anticipés dans ma réponse handoff — j'absorbe sans réserve, ce sont des findings empiriques S2.8/S2.9 directement de mon territoire.

## 3. Inventaire matière hub-ia → strategie-ia (préalable §3.1 obligatoire)

Inventaire détaillé livré en parallèle dans `_handoffs/claude-code-rag-vers-hub-strat/inventaire-migration-hub-ia-vers-strategie-ia-vague-b.md` (même bundle).

Synthèse :

| Cible strategie-ia | Volume fichiers | Volume « livrables » | Source hub-ia |
|---|---|---|---|
| `09/sprints/` (S2.6→S2.9 livrables finaux seulement) | ~16 MD | 16 | `hub-ia/rag-prep/briefs/` + `reports/` filtré S2.6→S2.9 |
| `09/adr/` (3 ADR nouveaux Michael Nygard) | 3 MD | 3 | Production neuve sur base SPEC v2.3 + RAPPORT S2.8/S2.9 |
| `09/golden-set/` (1 questions.yaml + adversarial/) | 2 YAML | 118 questions (104 std + 14 adv) | `hub-ia/rag/eval/questions.yaml` |
| `09/evaluations/` (4 RAPPORT-CC + audit R11) | 5 MD | 5 | `hub-ia/rag-prep/reports/` (S2.6-S2.9) |
| `09/pipeline-ingestion/` (code prod Python) | 8 PY | 8 | `hub-ia/rag/code/{eval,ingestion,backend}/` + `rag/eval/bench_runner*.py` |
| `09/tests/` (tests pytest pipeline) | 7 PY | 243 tests | `hub-ia/rag/code/**/test_*.py` |
| `07/qualite-et-tests/` (audit transverse) | 4 PY | 4 (+ ~120 tests) | `hub-ia/rag/code/audit/{audit-md-rag,citation_audit,test_*}.py` |
| `07/adr/` (2 ADR systémiques) | 2 MD | 2 | Production neuve |
| `07/deploiement/` (patch CI pytest) | 1 YAML patch | 1 | Modification `audit-conformity.yml` Vague A |
| Patch R3 dette Vague A | 1 MD patch | 1 | `CI-prioritaire/instructions-cavalli.md` |
| **Total** | **~49 fichiers** | **~280 livrables traçables** | — |

**Confirmation cible 280** : 16 sprints + 3 ADR + 118 questions + 5 rapports + 8 pipeline + 243 tests + 4 audit transverse (+120 sous-tests éventuels) + 2 ADR sys + 1 patch + 1 R3 = **~280 livrables traçables**. Cohérent §6 brief FINAL.

## 4. Clarifications demandées (à confirmer avant J+10)

### 4.1 « audit-global.py » mentionné §3.2

Le brief §3.2 cite `audit-global.py` parmi les modules à migrer en `07/qualite-et-tests/`. **Ce fichier n'existe pas dans `hub-ia/`**. Les seuls modules d'audit présents sont :

- `rag/code/audit/audit-md-rag.py` (R1-R10, ~1039 lignes, S2.1)
- `rag/code/audit/citation_audit.py` (R11 wikilinks outils, ~480 lignes, S2.8)

Hypothèse : « audit-global.py » désigne `audit-md-rag.py` (audit complet vault, conceptuellement « global »). **Demande confirmation Hub Strat** avant J+10. Si confirmation, je migre les 2 fichiers existants (+ leurs tests).

### 4.2 Dédup logique entre `citation_audit.py` (à migrer) et `audit_conformity.py` (Vague A déjà migré)

Le brief §3.2 demande de « Vérifier dédup logique au moment de la migration » entre les modules audit transverse et `audit_conformity.py` produit en Vague A.

Diagnostic préalable :

| Module | Cible | Périmètre |
|---|---|---|
| `audit_conformity.py` (Vague A, **dans strategie-ia déjà**) | Repo strategie-ia | Audit gouvernance MD/YAML strategie-ia (§§1, 2, 6, 9, 11, 12 CONVENTIONS) — naming/metadata/ADR |
| `audit-md-rag.py` (à migrer) | Vault RAG | Audit R1-R10 vault Hub IA (frontmatter, H1, chunking, wikilinks, glossaire, chiffres, nommage, versioning, chiffres-macro, tableaux) |
| `citation_audit.py` (à migrer) | Vault RAG | Audit R11 wikilinks outils glossariés (vault → fiches `outils-*.md`) |

→ **Pas de redondance logique**. Les 3 modules sont **complémentaires** (un audit gouvernance + deux audits vault éditorial). À documenter dans le README `07/qualite-et-tests/` à la migration.

### 4.3 Sprint S1-S2.5 non couverts

Le brief §3.1 limite la migration `09/sprints/` à S2.6 → S2.9 (arbitrage Cavalli 28/05 « capitalisation sur livrables finaux »). Les briefs/rapports S1, S1bis, S1ter, S2.1, S2.2, S2.3, S2.4, S2.5 (~16 fichiers) **restent dans `hub-ia/`** (cohérent décision §3.2 RETEX bascule `hub-ia` post-Étape 4).

**Pas de demande de clarification** — je trace ce périmètre dans la note de retour Vague B.

### 4.4 ADR-003 Frontmatter YAML 10 champs

Brief §3.1 inscrit cet ADR-003 en `09/adr/`. **Mais la SPEC-MD-POUR-RAG v2.3 (déjà en `07/spec-md-rag/` Vague A Hub RAG)** documente déjà ces 10 champs §R1. L'ADR-003 doit donc être un **ADR de *référence* vers la SPEC** (statut `accepted` reprenant la décision déjà effective S1), pas une nouvelle décision. À confirmer : ADR rétrospectif ou ADR vivant qui pourrait évoluer ?

## 5. Cadence — acceptation avec une optimisation mineure

J'accepte la cadence indicative §4.3 du brief (1 PR/jour J+10 → J+15) avec **une optimisation proposée** :

| Jour | Brief FINAL | Optimisation proposée | Justification |
|---|---|---|---|
| J+10 lundi 8 juin | PR 1 R3 patch instructions-cavalli.md | **Inchangé** | Clôture dette Vague A, faible risque |
| J+11 mardi 9 juin | PR 2 R2 code pipeline + tests pytest | **PR 2 R2 code pipeline-ingestion (8 PY)** | Tests pytest dépendent du code — déplacement séquentiel |
| J+12 mercredi 10 juin | PR 3 R2 audit transverse + golden-set + évals | **PR 3 R2 tests pytest pipeline (7 PY = 243 tests)** | Suite immédiate PR 2, valide la migration code |
| J+13 jeudi 11 juin | PR 4 R2 sprints S2.6-S2.9 | **PR 4 R2 audit transverse 07 + golden-set + évaluations** | Bloc cohérent (audit code + matière eval) |
| J+14 vendredi 12 juin | PR 5 R1 3 ADR RAG | **PR 5 R2 sprints S2.6-S2.9 (16 MD)** | Matière documentaire, à isoler avant les ADR |
| J+15 lundi 15 juin | PR 6 R1 2 ADR systémiques | **PR 6 R1 5 ADR consolidés** (3 RAG + 2 sys) | Regroupement permet relecture Hub RAG une seule fois, plus efficient |

**Différence clé** : je regroupe les 5 ADR en 1 seule PR R1 finale (au lieu de 2 PR R1). Justification :
- Économie de cycles de relecture (Hub RAG + Hub Strat × 1 vs × 2)
- ADR thématiquement cohérents (sprint d'ouverture stratégique)
- Volume gérable : 5 ADR Michael Nygard = ~25-40 KB total, lecture < 30 min
- Maintient le régime R1 le plus strict (héritage de contenu §4.3 brief)

**Si Hub Strat préfère** la séparation 09/adr (PR 5) puis 07/adr (PR 6) pour traçabilité par catégorie, je m'aligne sans réserve.

## 6. Préparation J+0 → J+9 (silencieuse, sans production livrable)

Pendant les 10 jours qui précèdent J+10, je préparerai en sourdine **sans produire de fichier livrable** :

1. **Rédaction des 5 ADR en draft** dans mon environnement Cowork local (pas de commit) — utilise le template Michael Nygard fourni `.config/templates/adr-template.md` du bundle v1.1
2. **Inventaire détaillé du code Python à migrer** avec mapping chemins hub-ia → strategie-ia (déjà commencé, livré en parallèle §3 de cet ack)
3. **Lecture détaillée FRONTIERES.md v1.0** §2.1 (07↔09) pour valider chaque destination
4. **Préparation du patch R3 instructions-cavalli.md** (mention `setup-labels.sh` Content Vague A)

**Pas de PR ouverte avant J+10 lundi 8 juin**. La PR 1 (R3 patch) est le premier livrable engagé.

## 7. Risques identifiés et mitigations

| Risque | Probabilité | Mitigation |
|---|---|---|
| Volume PR 2-3 (code + tests) trop gros pour seuil M1 | Modérée | Découpage si > 30 fichiers/PR → validation Cavalli préalable (cf. §4.4 brief) |
| ADR-001 LLM bloqué par arbitrage Cavalli prolongé | Modérée | Préparer ADR-001 en draft **avant J+10**, demander pré-validation orientation Cavalli avant J+14 |
| Patch CI `pytest` (07/deploiement) casse la CI Vague A | Faible | Test local préalable du workflow patché + `audit-conformity.sh` run avant push |
| « audit-global.py » mention §3.2 ambiguë → mauvaise migration | Faible | Cf. §4.1 ci-dessus — clarification demandée |
| Première Vague Claude Code Desktop sans pair → mécanisme handoff non testé | Acquis (cf. §8.1 brief) | À tracer dans note de retour J+15 (point d'attention DEV IA Head) |

## 8. Engagements

- **Démarrage Vague B** : lundi 8 juin 2026 (J+10), première PR R3 patch instructions-cavalli.md livrée dans la journée
- **Mi-parcours** : vendredi 12 juin 2026 (J+14), point d'étape Hub Strat avec calibrage M1 confirmé ou ajusté
- **Clôture Vague B** : lundi 15 juin 2026 (J+15) après PR 6 5-ADR mergée, **note de retour Claude Code RAG** transmise à Cavalli + Hub Strat + DEV IA Head + Claude Code Content
- **Hygiène discipline** : `git grep "<<<<<<<"` vide pre-commit chaque PR (héritage SPEC v2.0 hub-ia + job CI `check-merge-markers` Vague A)

---

## Historique

| Date | Version | Modification |
|------|---------|--------------|
| 2026-05-28 | v1.0 | Création — accusé réception brief Vague B FINAL Claude Code RAG. Acceptation scope ~280 livrables sur 49 fichiers physiques. Optimisation cadence proposée (regroupement 5 ADR en 1 PR R1). 4 clarifications demandées (audit-global.py, dédup citation_audit/audit_conformity, périmètre S1-S2.5, statut ADR-003 Frontmatter). Préparation silencieuse J+0 → J+9 sans production livrable. Démarrage J+10 lundi 8 juin 2026 confirmé. |

---

*Accusé de réception Claude Code RAG, 28 mai 2026. Régime R4 — handoff hors PR, matière `_handoffs/claude-code-rag-vers-hub-strat/`. Transmis via Cavalli intermédiaire Git, cc DEV IA Head + Claude Code Content pour traçage. Inventaire détaillé livré séparément dans le même bundle.*
