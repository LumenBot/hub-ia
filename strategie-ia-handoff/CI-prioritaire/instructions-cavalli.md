# Instructions Cavalli — Activation CI conformité + branch protection + labels

**Version** : v1.0
**Date de création** : 2026-05-27
**Dernière mise à jour** : 2026-05-27
**Destinataire** : Blaise Cavalli (admin GitHub `LumenBot/strategie-ia`)
**Émetteur** : Cowork Hub IA Plateforme (Claude Code)
**Auteur principal** : Cowork Hub IA Plateforme (Claude Code)
**Owner fonctionnel** : 07-tech-et-architecture
**Confidentialité** : interne
**Statut** : validé
**Tags** : ci, github, branch-protection, labels, cavalli

---

## Actions Cavalli à effectuer côté GitHub

Le code est livré (cf. fichiers du bundle). Pour activer la CI bout-en-bout,
3 actions à effectuer côté GitHub Settings du repo `LumenBot/strategie-ia` —
**aucune ne peut être faite Plateforme-side** (permissions admin requises).

Ordre recommandé : 1 → 2 → 3 (le 3 dépend du 1 pour fonctionner).

---

## 1. Copier les fichiers du bundle dans le repo

Depuis le bundle `CI-prioritaire/`, copier dans le clone local de `strategie-ia` :

```bash
cd /chemin/vers/clone/strategie-ia

# 1. Workflow GitHub Actions
mkdir -p .github/workflows
cp /chemin/vers/CI-prioritaire/.github/workflows/audit-conformity.yml .github/workflows/

# 2. Scripts CI + README
mkdir -p 07-tech-et-architecture/deploiement/ci-cd/scripts
cp /chemin/vers/CI-prioritaire/07-tech-et-architecture/deploiement/ci-cd/README.md \
   07-tech-et-architecture/deploiement/ci-cd/
cp /chemin/vers/CI-prioritaire/07-tech-et-architecture/deploiement/ci-cd/scripts/* \
   07-tech-et-architecture/deploiement/ci-cd/scripts/

# 3. Rendre les scripts exécutables
chmod +x 07-tech-et-architecture/deploiement/ci-cd/scripts/*.sh

# 4. Vérification locale rapide (depuis la racine du repo)
./07-tech-et-architecture/deploiement/ci-cd/scripts/audit-conformity.sh
./07-tech-et-architecture/deploiement/ci-cd/scripts/check-links.sh

# 5. Régénérer l'INDEX.md (qui inclura les nouveaux fichiers)
./07-tech-et-architecture/deploiement/ci-cd/scripts/generate-index.sh
```

Ouvrir la PR `claude-code/07-tech/ci-conformite-prioritaire` avec :
- Titre : `feat(07-tech): CI conformité prioritaire (audit + links + index + merge markers)`
- Co-authored-by trailer : `Co-authored-by: Cowork Claude Code Plateforme <cc-plateforme@cowork.local>`
- Régime PR : R1 standard (production structurante CI = relecture Hub Strat)

---

## 2. Activer la branch protection sur `main`

GitHub → `Settings` → `Branches` → `Add rule` (branch name pattern : `main`) :

### Règles à activer (MVP, post-Étape 2 = J0)

- ☑ **Require a pull request before merging**
  - ☑ Require approvals : **1**
  - ☑ Dismiss stale pull request approvals when new commits are pushed
  - ☑ Require review from Code Owners
- ☑ **Require status checks to pass before merging**
  - ☑ Require branches to be up to date before merging
  - **Required status checks** (apparaîtront après le 1ᵉʳ run de la CI) :
    - `audit-conformity`
    - `check-links`
    - `check-index`
    - `check-merge-markers`
- ☑ **Require conversation resolution before merging**
- ☑ **Require linear history** (cohérent avec squash-and-merge, ADR-002)
- ☐ Require signed commits (non bloquant — à activer en v1.X si besoin)
- ☑ **Do not allow bypassing the above settings** (incluant admins, sauf
  cas exceptionnel — à conserver coché par défaut)
- ☑ **Restrict pushes that create matching branches**
  - Restreindre à : `@cavalli` + `@hub-strat`

### Durcissement Étape 2 MVP (juin 2026)

Quand le repo passe en Étape 2 (MVP commercialisable), durcir :
- Require approvals : **2** pour les catégories sensibles
  (`/04-juridique/`, `/02-finance/`, `/_internal/`)
- Mécanisme : via CODEOWNERS multi-reviewer ou règle dédiée par path

### Justification

- 1 approve = équilibre vélocité / qualité pour la phase post-ouverture (étape 3
  contributions massives)
- CI must pass = pierre angulaire du régime R3 fast-track mineur (auto-approve
  owner uniquement si CI verte)
- Linear history = compatible avec Conventional Commits + squash-and-merge (ADR-002)
- Pas de force push, pas de bypass admin = traçabilité totale (cf. discipline
  hygiène merge SPEC v2.0 héritée hub-ia)

---

## 3. Créer les labels GitHub `impact:*`

GitHub → `Issues` → `Labels` → `New label` (3 labels à créer) :

| Label | Couleur recommandée | Description |
|-------|---------------------|-------------|
| `impact:juridique` | `#d93f0b` (rouge) | PR touchant `/04-juridique/`, CGV/CGU, IP, RGPD/AI Act |
| `impact:securite` | `#b60205` (rouge foncé) | PR touchant `/07-tech-et-architecture/securite/`, secrets, incident response |
| `impact:finance` | `#0e8a16` (vert) | PR touchant `/02-finance/`, pricing, modélisation économique |

Usage : si une PR porte un de ces labels, **arbitrage Cavalli systématique** avant
merge (cf. `CONTRIBUTING.md` v1.1 §2 régime R2 fast-track tech : *« Cavalli arbitre
uniquement si signalé impact:juridique / impact:securite / impact:finance »*).

**Labels complémentaires utiles (optionnel)** :
- `regime:R1` / `regime:R2` / `regime:R3` — pour expliciter le régime PR
- `catégorie:07-tech` / `catégorie:09-rag` / etc. — pour le tri rapide
- `bundle:claude-code` / `bundle:hub-rag` / etc. — pour identifier l'origine
  Cowork de la contribution (à créer au fil des contributions)

---

## 4. Connexion Vercel deploy preview (différée à vague C)

Réponse Q2 CdC §8 : **attendre vague C (J+15-J+20)** pour connecter Vercel à
`strategie-ia.pro`. Avant ça, pas de matière front à déployer.

Quand la première PR vague C touchant `06/site-public/` arrive :
- Ouvrir handoff Cavalli ↔ Claude Code Plateforme + Claude Design
- Connecter le compte Vercel au repo `LumenBot/strategie-ia` (Settings → Integrations)
- Configurer le projet Vercel pour pointer sur `06-produit-et-site/site-public/landing/`
  (ou le sous-chemin retenu)
- Activer GitHub Actions Vercel (preview à chaque PR, deploy auto sur merge `main`)

---

## 5. Vérification post-activation

Une fois les 3 actions effectuées, ouvrir une PR test (par ex. fix typo dans
`README.md`) pour vérifier :

1. La CI s'exécute et les 4 jobs apparaissent dans la PR
2. La branch protection bloque le merge tant que la CI n'est pas verte
3. Les labels sont disponibles dans l'UI PR
4. Le merge fonctionne avec squash-and-merge et un commit Conventional Commits propre

**Critère de succès CI prioritaire (J+7) acquis** : 4 jobs verts sur la PR test
+ branch protection bloquante observable + 3 labels disponibles.

---

## 6. Contact

Pour toute question d'interprétation : Cowork Hub IA Plateforme (Claude Code) — via session.

---

## Historique

| Date | Version | Modification |
|------|---------|--------------|
| 2026-05-27 | v1.0 | Instructions initiales — 3 actions GitHub à effectuer par Cavalli pour activer la CI prioritaire (copie + branch protection + labels) + différé Vercel vague C. |

---

*Instructions Cavalli — bundle CI-prioritaire, Cowork Hub IA Plateforme, 27 mai 2026.*
