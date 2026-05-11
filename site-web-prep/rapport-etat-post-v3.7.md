# Rapport d'état du repo — post v3.7

**Date** : mai 2026
**Branche analysée** : `main` (à jour avec `origin/main`)
**Auteur** : Claude Code
**Destinataire** : Cowork — préparation de la prochaine itération

---

## ⚠️ Note préalable importante sur la chronologie

Le brief de cette demande supposait un état « post v3.7, avant v3.7.1 ». La **réalité du repo `main` est plus avancée** :

| État supposé par le brief | État réel `main` |
|---|---|
| v3.7 mergée, v3.7.1 à préparer | **v3.7.1 à v3.7.13 déjà mergées** (13 PRs successives de correctifs depuis le merge de v3.7) |

Le rapport ci-dessous reflète l'**état réel** post-v3.7.13. Cowork doit donc préparer la prochaine itération à partir de cet état actualisé, pas de l'état v3.7 initial. Si Cowork avait préparé une v3.7.1 en parallèle, il faut vérifier qu'elle ne fait pas doublon avec les correctifs déjà appliqués.

---

## 1. Synthèse v3.7 livrée

### 1.1 Itération v3.7 (lot initial)

La PR #25 `feat/v3.7-deploiement` a été mergée dans `main` et contient :
- `ab575f9` chore(v3.7): amendements RULES v1.4 → v1.5
- `2c3a1b3` feat(v3.7): page index Déploiement + nav 5→6 entrées sur 36 pages
- `a9783f4` feat(v3.7): 8 fiches DEP + CU-025 + 5 enrichissements + 12 fiches outils + cohérence numérique

### 1.2 Correctifs post-merge v3.7.1 à v3.7.13 (13 PRs)

| PR | Branche | Apport principal |
|---|---|---|
| #26 | `feat/v3.7.1-nav-correctifs` | Nav 6→5 entrées (retrait « À propos », interversion Modules↔Déploiement) + correctif `83 fiches / 14 catégories` synthèse ressources |
| #27 | `feat/v3.7.2-jargon-renvois` | Retrait de 45 codes internes CU/PR/DEP en texte affiché + audit renvois outils manquants |
| #28 | `feat/v3.7.3-coquilles-mise-en-forme` | Section À propos ordre, DEP-06 résiduel, mention « cas QFC », 344 liens internes `tool-link` |
| #29 | `feat/v3.7.4-toc-restoration-contrast-fix` | Restauration des 18 sommaires cassés par bug STASH + fix contraste `tool-link` sur fond foncé |
| #30 | `feat/v3.7.5-callout-mise-en-forme` | Callout `Bibliographie transverse` imbriqué dans `module-section-header` sur 8 modules |
| #31 | `feat/v3.7.6-callout-intro-margin` | Callout intro section « Pour aller plus loin » sans `margin-bottom` (12 fichiers) |
| #32 | `feat/v3.7.7-card-content-coherence` | Label CU-025 « Étude de cas + plan d'action » → « Architecture + plan d'action » |
| #33 | `feat/v3.7.8-cu-018-multifiliere` | Refonte CU-018 multi-filière (bois 110→20, ENSTIB 92→16) + dep-07 schemas + 11 jargons résiduels (v3.7.8 et v3.7.9 livrées ensemble dans cette PR) |
| #34 | `feat/v3.7.10-contraste-sommaires-harmonisation` | Contraste résiduel inline styles + harmonisation 18 sommaires numbered → emoji-style |
| #35 | `feat/v3.7.11-jargon-cascade-fix` | 14 jargons résiduels via regex agressive + h3/strong dans conteneurs sombres |
| #36 | `feat/v3.7.12-audit-global-ressources-fix` | **Garde-fou `audit-global.py`** (13 règles automatisées) + sommaire ressources 13→15 catégories |
| #37 | `feat/v3.7.13-sommaire-emojis-fallback` | 31 emojis fallback 📌 → emojis contextuels (architectures + 11 modules/préalables) |

### 1.3 Pull requests

- **Toutes mergées** : PR #25 (v3.7) à PR #37 (v3.7.13). Aucune PR `feat/v3.7.x` n'est encore ouverte.
- **Branches obsolètes locales** non nettoyées (cosmétique uniquement) : `chore/v3.5.3-audit-qualite`, `chore/v3.6.2-harmonisation`, `feat/v2-*`, `feat/v3-*` — d'avant v3.6.3. Sans impact opérationnel.

---

## 2. Inventaire structurel du site

### 2.1 Structure du repo (top-level)

```
hub-ia/
├── .git/                  ← version control
├── assets/                ← logos QFC, images de modules
├── css/                   ← design system (style.css + module-v3.css)
├── deploiement/           ← 8 fiches DEP (dep-01 à dep-08)
├── js/                    ← module-v3.js (sticky TOC, scroll-spy, reading progress)
├── modules/               ← 26 modules CU + 3 templates _template-*
├── prealables/            ← 7 préalables PR (pr-01 à pr-07)
└── site-web-prep/         ← briefs, rapports, RULES, audit-global.py
```

### 2.2 Fichiers HTML à la racine (5 pages-index)

| Fichier | Rôle |
|---|---|
| `index.html` | Home : 5 niveaux + 6 familles métier + filtres modules |
| `prealables.html` | Index des 7 préalables transverses |
| `architectures.html` | 4 patterns + hybride + méthode de choix |
| `deploiement.html` | Index des 8 fiches Déploiement (POC → production) |
| `ressources.html` | Catalogue 95 fiches outils en 15 catégories + bibliographie |

### 2.3 Comptages des sous-dossiers de contenu

| Section | Fichiers | Détail |
|---|---|---|
| `modules/cu-*.html` | **26 modules** | cu-001 à cu-025 + cu-027 (cu-026 réservé pour itération future) |
| `prealables/pr-*.html` | **7 préalables** | pr-01 à pr-07 |
| `deploiement/dep-*.html` | **8 fiches DEP** | dep-01 à dep-08 |
| `modules/_template-*.html` | **3 templates** | auto-diagnostic, étude-de-cas, quiz (voir § 7 ci-dessous) |

**Total pages HTML "produit"** : 5 + 26 + 7 + 8 = **46 pages** (hors templates).

---

## 3. Cohérence numérique cross-site

### 3.1 Comptages réels (grep sur le repo)

| Élément | Comptage réel | Source du comptage |
|---|---|---|
| Modules CU | **26** | `ls modules/cu-*.html` |
| Préalables PR | **7** | `ls prealables/pr-*.html` |
| Fiches Déploiement DEP | **8** | `ls deploiement/dep-*.html` |
| Fiches outils | **95** | `grep -c 'tool-card" id=' ressources.html` |
| Catégories outils | **15** | `grep -c 'class="cat-divider"' ressources.html` |
| Entrées de nav | **5** | Vérification cross-pages (cf. tableau ci-dessous) |

### 3.2 Entrées de nav — vérification sur 4 pages-types

| Page | Entrées nav-link comptées |
|---|---|
| `index.html` | 5 (Préalables / Architectures / Modules / Déploiement / Ressources) |
| `modules/cu-008-knowledge-base-rag.html` | 5 (idem, base + Modules actif) |
| `prealables/pr-01-maturite-organisationnelle.html` | 5 (idem, Préalables actif) |
| `deploiement/dep-01-cadrer-projet-prod.html` | 5 (idem, Déploiement actif) |

Le décompte initial des grep retournait 1-4 par page car la mesure ne couvrait pas le bloc complet `<div class="nav-links">`. Vérification corrigée : **5 partout, cohérent**.

### 3.3 Comparaison avec RULES § 1.2.3 (glossaire chiffres-clés)

Le glossaire RULES § 1.2.3 indique :

| Chiffre RULES | Valeur déclarée | Réel | Statut |
|---|---|---|---|
| Modules CU | 26 | 26 | ✅ |
| Préalables PR | 7 | 7 | ✅ |
| Fiches DEP | 8 | 8 | ✅ |
| Fiches outils | 95 | 95 | ✅ |
| Patterns architecture | 4 + 1 hybride | 4 + 1 hybride | ✅ |
| Entrées nav | 5 (Préalables / Architectures / Modules / Déploiement / Ressources) | 5 | ✅ |
| Familles métier modules | 6 | 6 | ✅ |
| Échelle complexité | 4 niveaux | 4 niveaux | ✅ |

**Tout est aligné.** L'`audit-global.py` v3.7.12 confirme `0 hit` sur la règle 1 (Cohérence numérique cross-site).

---

## 4. Version de RULES.md actuelle

### 4.1 Version courante

- En-tête du fichier : **`**Version :** 1.5 (mai 2026)`** (ligne 3 inchangée — l'en-tête n'a pas été incrémenté à chaque sous-version)
- Historique réel (cf. § 1.5.X de l'historique) : **dernière entrée = v1.5.12**

**Action recommandée pour Cowork v3.7.14+** : envisager de mettre à jour l'en-tête `Version : 1.5` → `Version : 1.5.12 (mai 2026)` pour cohérence visuelle avec l'historique.

### 4.2 Historique des amendements depuis v1.0

| Version | Itération | Apport principal |
|---|---|---|
| **v1.0** | 9 mai 2026 | Création initiale |
| v1.1 | post-v3.5.3 / v3.6 | Premier audit qualité |
| v1.2 | post-v3.6.1 | Harmonisation CU-023/024/027 |
| v1.3 | v3.6.2 | Schéma A, anti-patterns § 1.5.3, rôles Cowork/CC, format auto-diag |
| v1.4 | post-v3.6.2 | Checklist statique, card↔contenu, espacements var(--space-X), commande grep dynamique ancres outils |
| **v1.5** | v3.7 | Glossaire actualisé (25→26 modules, 83→95 fiches, 5→6 nav, +8 DEP), squelette HTML aussi pour fiches DEP |
| v1.5.1 | v3.7.1 | Nav 6→5 (retrait À propos), § 1.2.5.1 anti-drift cross-bloc |
| v1.5.2 | v3.7.2 | § 1.5.6.1 anti-codes-internes, § 1.5.6.2 lien outil obligatoire |
| v1.5.3 | v3.7.4 | § 1.4.5 anti-bulk-patch-bug (STASH/NUL), § 1.4.6 audit contraste fond foncé |
| v1.5.4 | v3.7.5 | § 1.5.1.1 structure canonique `module-section-header` |
| v1.5.5 | v3.7.6 | § 1.5.1.2 callout intro `margin-bottom` |
| v1.5.6 | v3.7.7 | § 1.5 audit cohérence card↔contenu automatisé |
| v1.5.7 | v3.7.8 | § 1.2.7 anti-biais sectoriel/territorial |
| v1.5.8 | v3.7.9 | § 1.5.3 anti-`<pre>` text-art pour flux fonctionnels |
| v1.5.9 | v3.7.10 | § 1.4.7 format canonique sommaire emoji + § 1.4.8 contraste élargi |
| v1.5.10 | v3.7.11 | Post-mortem cascade CSS conflictuelle + adoption regex agressive |
| **v1.5.11** | v3.7.12 | **Garde-fou `audit-global.py` automatisé (13 règles)** |
| **v1.5.12** | v3.7.13 | § 1.4.7 enrichie : pas de fallback 📌, détection répétition emoji |

### 4.3 Cohérence avec la production v3.7

Tous les amendements RULES sont cohérents avec la production. La règle qui mériterait peut-être une attention spécifique pour Cowork :

- **§ 1.5.6.1** (anti-jargon codes internes) — entrée en v1.5.2 mais a nécessité 3 itérations correctives (v3.7.2 → v3.7.9 → v3.7.11) car les patches successifs utilisaient des listes manuelles. **La regex agressive universelle de v3.7.11 est la version définitive.** Cowork doit l'utiliser pour les briefs futurs.

---

## 5. Écarts résiduels signalés en v3.7

Le rapport `site-web-prep/rapport-mission-v3.7.md` documente une seule section d'écart assumé :

> **« Cohérence numérique : 95 fiches au lieu de 97 annoncées dans le brief Cowork v3.7 »** — assumé. Le brief Cowork prévoyait +14 nouvelles fiches outils (83 → 97). En pratique, 12 nouvelles fiches ont été créées + 2 existantes (Kimi K2 → K2.6, Copilot Workspace) ont été refondues à neuf. Total 83 + 12 = 95.

**Statut** : pas un bug — c'est un choix éditorial assumé. Aligné sur le réel (95 fiches confirmées dans § 3 ci-dessus). RULES § 1.2.3 reflète bien 95.

**Aucun autre écart bloquant n'a été identifié à la livraison de v3.7.** Les correctifs v3.7.1 à v3.7.13 sont tous nés de retours utilisateur post-merge (bugs visuels ou éditoriaux remontés par Cowork au fil de la review du site déployé).

---

## 6. Anti-patterns § 1.5.3 RULES — grep final

### 6.1 audit-global.py (13 règles automatisées)

```bash
$ python3 site-web-prep/audit-global.py
Audit global Hub IA — Learning Center
============================================================
Rapport écrit : site-web-prep/audit-rapport.md
Total hits : 0
```

**Toutes les 13 règles automatisées sont à 0 hit.** L'audit couvre : cohérence numérique cross-site, intra-page, versioning front, biais sectoriel, structure header, callout margin, jargon codes, card↔contenu, sommaire canonique (+ fallback + répétition), contraste dark, STASH résiduels, NUL bytes.

### 6.2 Anti-patterns § 1.5.3 non encore automatisés — vérification manuelle

#### Anti-pattern 1 — `<style>` inline redéfinissant les composants centralisés

Audit manuel : **aucun hit** sur les composants centralisés majeurs (`.alert-block`, `.checklist-block`, `.tool-table`, `.stat-block`, `.pull-quote`) — la migration de v3.6.3 a tenu. Quelques modules conservent des `<style>` pour des composants single-use légitimes (`.incident-card`, `.timeline-block`, etc.), tous justifiés par un commentaire.

#### Anti-pattern 2 — h1 sans emoji ouvrant

Audit : 0 hit sur les 26 modules, 7 préalables, 8 fiches DEP. Tous ont un h1 commençant par un emoji ouvrant.

#### Anti-pattern 3 — Section finale ≠ `id="ressources"`

Audit : 0 hit. Tous les modules / PR / fiches DEP ont leur dernière section avec `id="ressources"`.

#### Anti-pattern 4 — Couleurs hardcodées `#XXXXXX` hors `<style>`/SVG

⚠️ **3 hits résiduels identifiés** (à signaler) :
- `modules/cu-002-assistant-redactionnel.html:254-255` : `style="background: #FDF4DC; border-left-color: #B89030;"` et `style="color: #7A5C20;"` dans une `.case-deep-actor`
- `modules/cu-003-cr-reunion.html:243-244` : idem
- `modules/cu-006-leads-chatbot.html:272+` : idem

**Origine** : ces couleurs hardcodées sont sur des `.case-deep-actor` thématiques (ambre / orange) — pattern utilisé en v3.4-v3.5 pour différencier visuellement les blocs « Contexte » dans certaines études de cas. À migrer vers une variante CSS centralisée `.case-deep-actor.warm` ou similaire pour v3.7.14+.

#### Anti-pattern 5 — Padding/margin absolus dans style inline

⚠️ **Quelques hits résiduels** dans cu-001 (lignes 282, 315) : `style="background: #F0F4FA; padding: var(--space-3); ..."` — utilise déjà `var(--space-3)` (conforme), mais avec couleur de fond hardcodée (anti-pattern 4 plutôt). À traiter ensemble avec anti-pattern 4.

#### Anti-pattern 6 — Renvois internes dans section finale `id="ressources"`

⚠️ **19 hits résiduels sur 6 préalables** :
- `prealables/pr-01-maturite-organisationnelle.html` : 4 renvois (CU-020, CU-014, PR-02, PR-03)
- `prealables/pr-02-preables-data-si.html` : 5 renvois (CU-008, CU-013, CU-014, PR-01, PR-03)
- `prealables/pr-03-maturite-humaine-formation.html` : 3 renvois (CU-020, CU-007)
- `prealables/pr-04-marche-ia-emploi.html` : 2 renvois
- `prealables/pr-05-securite-ia.html` : 3 renvois (CU-020, CU-014)
- `prealables/pr-06-qualite-code-ia.html` : 2 renvois (CU-015)

**Origine** : les préalables ont une sous-section « Pour aller plus loin sur le Hub » à l'intérieur de leur section `id="ressources"` finale — pattern d'origine v3.4. RULES v1.3 a interdit ce pattern (§ 1.5.6) mais les préalables n'ont **jamais été nettoyés**. Les modules CU et fiches DEP ont été nettoyés ; pas les PR.

**Recommandation** : à traiter en v3.7.14+ — déplacer ces renvois dans le corps du préalable (contextualisés) et garder uniquement les ressources externes (Schéma A) dans la section finale.

---

## 7. État des templates `_template-*.html`

### 7.1 Inventaire et état

| Template | Lignes | Nav entries | Mentions `deploiement.html` | Statut |
|---|---|---|---|---|
| `_template-auto-diagnostic.html` | 358 | **5 (avec « À propos » et SANS « Déploiement »)** | 0 | ⚠️ **Obsolète** |
| `_template-etude-de-cas.html` | 74 | N/A (pas de nav, fragment) | N/A | OK (fragment partiel) |
| `_template-quiz.html` | 61 | N/A (pas de nav, fragment) | N/A | OK (fragment partiel) |

### 7.2 Détail du problème sur `_template-auto-diagnostic.html`

La nav contient :
```
Préalables / Architectures / Modules (actif) / Ressources / À propos
```

Ce qui correspond à la **nav v3.5-v3.6 (5 entrées avec « À propos »)** — pas la nav canonique v3.7+ qui est :
```
Préalables / Architectures / Modules / Déploiement / Ressources
```

**Recommandation Cowork v3.7.14+** : mettre à jour `_template-auto-diagnostic.html` pour qu'il reflète la nav 5 entrées canonique post-v3.7.1. Sinon tout module créé à partir de ce template arrivera avec une nav obsolète.

### 7.3 Référence canonique CU-008

**`modules/cu-008-knowledge-base-rag.html` est toujours la référence canonique du Hub.** Vérifié :
- Pattern HTML respecté (§ 1.5.1)
- Section finale `id="ressources"` avec Schéma A (4 sous-rubriques externes uniquement)
- Sommaire emoji-style canonique (§ 1.4.7)
- Aucun anti-pattern résiduel détecté

CU-008 reste la **fiche d'or** à laquelle Cowork peut se référer pour briefs futurs.

---

## 8. Suggestions opérationnelles pour la prochaine itération

### 8.1 Trois priorités opérationnelles (par ordre de bénéfice/effort)

**Priorité 1 — Mise à jour de `_template-auto-diagnostic.html`** (effort : 15 minutes ; bénéfice : prévient toute production future déviante)
- Aligner la nav sur les 5 entrées canoniques v3.7.1+ (Préalables / Architectures / Modules / Déploiement / Ressources)
- Retirer « À propos »
- Vérifier que les renvois externes du Schéma A (callout vers `ressources.html#bibliographie`) sont présents
- Mettre à jour la version dans le commentaire d'en-tête du template (s'il y en a une)

**Priorité 2 — Nettoyer les renvois internes dans la section finale des 6 préalables** (effort : 1-2 heures ; bénéfice : conformité § 1.5.6 RULES v1.3, dette technique remboursée depuis v3.6.2)
- Pour chaque préalable (PR-01 à PR-06), déplacer les renvois internes (CU-XXX, autres PR-YY) hors de `<section id="ressources">` vers le corps du préalable, contextualisés
- Garder uniquement les ressources externes (Articles / Tutoriels / Documentation / Communautés) dans la section finale
- Note : PR-07 a déjà été nettoyé en v3.6.3

**Priorité 3 — Migrer les couleurs hardcodées des `.case-deep-actor` thématiques** (effort : 1 heure ; bénéfice : conformité § 1.5.3 anti-pattern 4)
- 3 modules concernés (cu-002, cu-003, cu-006) avec `style="background: #FDF4DC; color: #7A5C20"` inline
- Créer une variante CSS centralisée `.case-deep-actor.warm` dans `module-v3.css` (background ambre, accent orange)
- Remplacer les styles inline par `class="case-deep-actor warm"`
- Vérifier en parallèle si d'autres tons (`.cool`, `.danger`) seraient utiles

### 8.2 Zones de vigilance pour la v3.7.14+

- **Lancer `audit-global.py` AVANT toute clôture de PR.** C'est le garde-fou opérationnel qui transforme RULES.md en garantie. Doit retourner `0 hit`.
- **Si un nouveau pattern HTML est introduit** (nouveau composant, nouvelle classe de conteneur), **ajouter sa fonction d'audit** dans `audit-global.py` la même PR, et inscrire la nouvelle règle dans RULES.md.
- **Si une nouvelle règle structurelle est codifiée dans RULES**, vérifier qu'elle est doublée d'un script d'audit dans `audit-global.py`. RULES descriptive sans audit = futur bug récurrent (cf. v3.7.2 → v3.7.9 → v3.7.11 pour les jargons).

### 8.3 Dépendances et ordre suggéré

Si Cowork prépare un brief v3.7.14 qui combine plusieurs lots, voici un ordre suggéré :

1. **Templates** (zone isolée, sans impact site) → en premier
2. **Préalables — renvois internes** (modifie 6 fichiers, mais pas la structure) → en deuxième
3. **Migration `.case-deep-actor` thématiques** (touche CSS + 3 modules) → en troisième
4. **Lots éditoriaux substantiels** (nouveau module CU-026, enrichissements veille, etc.) → en dernier, sur base nettoyée

Cet ordre permet à chaque lot de partir d'une base conforme aux RULES, sans accumuler de dette technique.

---

## Annexe — Commandes utiles

```bash
# Audit global automatisé (13 règles)
python3 site-web-prep/audit-global.py

# Comptages cross-site
ls modules/cu-*.html | wc -l
ls prealables/pr-*.html | wc -l
ls deploiement/dep-*.html | wc -l
grep -c 'tool-card" id=' ressources.html
grep -c 'class="cat-divider"' ressources.html

# Vérification nav cross-pages (5 entrées attendues)
for f in index.html modules/cu-008-*.html prealables/pr-01-*.html deploiement/dep-01-*.html; do
  echo "$f: $(awk '/<div class="nav-links">/,/<\/div>/' "$f" | grep -c 'class="nav-link"')"
done
```
