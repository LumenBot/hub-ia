# Bundle CI-prioritaire — Claude Code étape 3 vague A préalable

**Version** : v1.0
**Date de création** : 2026-05-27
**Dernière mise à jour** : 2026-05-27
**Émetteur** : Cowork Hub IA Plateforme (Claude Code)
**Destinataire** : Cavalli (intermédiaire Git) → repo `LumenBot/strategie-ia`
**Auteur principal** : Cowork Hub IA Plateforme (Claude Code)
**Owner fonctionnel** : 07-tech-et-architecture
**Référence CdC** : CdC Claude Code étape 2 §3.1 *« CI conformité prioritaire J+3 à J+7 »*
**Statut** : validé
**Confidentialité** : public
**Tags** : bundle, ci, handoff, étape-3

---

## 1. Contenu du bundle

```
CI-prioritaire/
├── README.md                                      ← ce fichier
├── instructions-cavalli.md                        ← 3 actions Cavalli côté GitHub
├── .github/workflows/
│   └── audit-conformity.yml                       ← workflow CI principal (4 jobs)
└── 07-tech-et-architecture/deploiement/ci-cd/
    ├── README.md                                  ← doc CI complète (politique, usage, évolutions)
    └── scripts/
        ├── audit-conformity.sh                    ← entry bash (kebab-case, §1)
        ├── audit_conformity.py                    ← cœur Python (snake_case, §11)
        ├── check-links.sh                         ← liens internes morts (bash pur)
        ├── generate-index.sh                      ← entry bash de l'indexation
        └── _generate_index_helper.py              ← helper Python (extraction métadonnées)
```

**Total** : 9 fichiers (8 productions + ce README).

## 2. Ce qui est livré

| Production CdC §3.1 | Fichier | Statut |
|---|---|---|
| `audit-conformity.yml` workflow GitHub Actions | `.github/workflows/audit-conformity.yml` | ✅ livré |
| `audit-conformity.sh` vérification naming/en-têtes/métadonnées | `scripts/audit-conformity.sh` + `audit_conformity.py` | ✅ livré |
| `check-links.sh` vérification dead links | `scripts/check-links.sh` | ✅ livré |
| Industrialisation `generate-index.sh` | `scripts/generate-index.sh` + `_generate_index_helper.py` | ✅ livré |
| Branch protection sur `main` | Action Cavalli — cf. `instructions-cavalli.md` §2 | ⚠ Cavalli |
| Labels GitHub `impact:*` | Action Cavalli — cf. `instructions-cavalli.md` §3 | ⚠ Cavalli |

## 3. Règles vérifiées par la CI

Le workflow `audit-conformity.yml` orchestre 4 jobs (en parallèle) qui vérifient
collectivement les conventions de `CONVENTIONS.md` v1.1 :

| Job | Règles | Sévérité bloquante |
|---|---|---|
| `audit-conformity` | §1 naming, §2 en-tête + footer, §6 dates ISO, §9 confidentialité, §11 Python snake_case + docstring, §12 ADR | erreurs (warnings tolérés) |
| `check-links` | Liens Markdown relatifs + wikilinks Obsidian | erreurs |
| `check-index` | INDEX.md synchrone avec contenu repo | erreurs |
| `check-merge-markers` | Aucun `<<<<<<<` non résolu (hygiène merge importée hub-ia SPEC v2.0) | erreurs |

Détail complet : `07-tech-et-architecture/deploiement/ci-cd/README.md` §3.

## 4. Stack technique choisi (et pourquoi)

- **Bash** pour les entry points (kebab-case `.sh`, §1 CONVENTIONS) — facile à
  débugger, pas de dépendance externe
- **Python 3.11 stdlib** pour le parsing YAML/Markdown (snake_case `_*.py`, §11
  exceptions techniques) — robuste, pas de `requirements.txt` à maintenir, déjà
  disponible sur les runners GitHub Actions
- **GitHub Actions** pour l'orchestration CI — natif, gratuit jusqu'à 2000 min/mois
  sur repos privés, dispo immédiatement sans config réseau

**Hygiène pattern** : le style des scripts est volontairement isomorphe à
`hub-ia/rag/code/audit/audit-md-rag.py` (style importé : `RuleResult`, classes
simples, exit codes). Conserve le pattern dual repo pendant la transition
`hub-ia` → `strategie-ia` (cf. décision §3.2 CdC, source de vérité = `hub-ia`
jusqu'à janvier 2027).

## 5. Étapes pour Cavalli

Lire `instructions-cavalli.md` puis :

1. **Copier les fichiers du bundle dans le clone local** (§1 INSTRUCTIONS) — ~5 min
2. **Activer branch protection sur `main`** (§2 INSTRUCTIONS) — ~10 min côté Settings GitHub
3. **Créer les 3 labels `impact:*`** (§3 INSTRUCTIONS) — ~5 min côté Labels GitHub
4. **Ouvrir une PR test** (§5 INSTRUCTIONS) — ~10 min, vérifie que tout fonctionne

Effort total Cavalli : ~30 min.

## 6. Critère d'acceptation CI prioritaire (J+7)

D'après CdC §3.1 *« 5-6 fichiers dans 07/deploiement/ci-cd/ + .github/workflows/ »* :

- [x] **6 fichiers livrés** : 1 workflow YAML + 4 scripts (2 bash entry + 1 Python core + 1 Python helper) + 1 README CI ✓ (8 si on compte les wrappers/helpers séparément)
- [ ] Workflow actif sur `main` (dépend de l'étape Cavalli §1+§2)
- [ ] Branch protection « must pass » active (dépend Cavalli §2)
- [ ] 3 labels créés (dépend Cavalli §3)
- [ ] PR test verte (vérification finale Cavalli §5)

## 7. Suite après CI prioritaire

Une fois ce bundle mergé + branch protection active, je démarre la **Vague A**
(échéance J+5 à J+10, possible chevauchement avec installation CI) :

- ADR-001 — Variante A stack US (Vercel + Supabase EU regions) en MVP
- ADR-002 — Conventional Commits + squash-and-merge sur main + branch protection
- ADR-003 — Choix LLM par défaut Haiku 4.5 + Sonnet 4.6 routing (co-relecture Hub RAG)
- Migration SPEC-MD-POUR-RAG v2.3 depuis `hub-ia/rag-prep/` → `07/spec-md-rag/`
- Schéma architecture stack envisagée → `07/architecture-systeme/`
- Référence technique fournisseur LLM → `07/stack/dependencies/`

Bundle Vague A à venir.

## 8. Coordination

- **Hub RAG** : peut consulter les scripts (régime R2 fast-track tech sur 07/09).
  La logique d'audit est isomorphe à `hub-ia/rag/code/audit/audit-md-rag.py`.
- **Hub Strat** : approuve la PR en relecture transverse R1 (production
  structurante CI). Peut suggérer évolutions de politique (sévérité, exclusions).
- **Cavalli** : exécute les 3 actions GitHub (§1+§2+§3 INSTRUCTIONS) et arbitre
  les ajustements de politique de blocage.

## 9. Tests effectués côté Plateforme

- [x] Scripts bash : syntaxe `bash -n` OK sur les 3 `.sh`
- [x] Python : `python3 -m py_compile audit_conformity.py` + `_generate_index_helper.py` OK
- [x] Workflow YAML : structure conforme schéma GitHub Actions
- [ ] Test end-to-end sur le repo réel (à effectuer Cavalli §5 INSTRUCTIONS après copie)

## 10. Bonus — proposition SPEC v2.4 hub-ia importée

La discipline hub-ia **« hygiène merge `git grep <<<<<<<` vide avant `git add` »**
(SPEC v2.0, héritée des 3 occurrences PR #84/#86/#88 — cf. `RAPPORT-CC-S2.X`)
est automatisée ici par le job `check-merge-markers` du workflow. Aucune action
contributeur — la CI bloque automatiquement.

---

## Historique

| Date | Version | Modification |
|------|---------|--------------|
| 2026-05-27 | v1.0 | Bundle CI-prioritaire initial — 8 productions (1 workflow + 5 scripts + 1 README CI + 1 INSTRUCTIONS Cavalli). Livré J+0 (Cavalli pour exécution avant J+7 cible). |

---

*Bundle CI-prioritaire `strategie-ia` — Cowork Hub IA Plateforme (Claude Code), 27 mai 2026.*
