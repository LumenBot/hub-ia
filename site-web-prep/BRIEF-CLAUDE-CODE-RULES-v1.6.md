# Brief Claude Code — Refonte RULES v1.5.14 → v1.6

**Auteur :** Blaise Cavalli — Startup Manager Quai Alpha (Quest for Change)
**Repo :** https://github.com/LumenBot/hub-ia
**Branche cible :** main
**Nature de l'itération :** REFONTE STRUCTURELLE du référentiel RULES.md — pas de modification du site, pas de nouveau contenu éditorial, uniquement remplacement du fichier de règles + audit de cohérence.

---

## 0. Contexte court

Le canal Cowork Hub IA Plateforme a transmis l'item I-001 qui souligne que `RULES-IMPLEMENTATION.md` a évolué par accumulation (14 sous-versions v1.5.1 → v1.5.14). Constat partagé : référentiel devenu lourd à maintenir et à lire pour un Claude Code qui démarre une nouvelle itération. Risque : règles non lues ou mal interprétées faute de lisibilité.

Cowork a produit une **refonte v1.6 simplifiée** : 13 règles consolidées + annexes + alignement audit-global.py. **Aucune règle structurelle abandonnée** — pure consolidation, traçabilité garantie par une table de migration.

**Mission de cette itération** : pousser RULES v1.6 sur le repo en remplacement de v1.5.14, ajouter la table de migration, vérifier que `audit-global.py` continue à retourner `0 hit`, produire un rapport de mission court.

**Tu travailles en autonomie.**

---

## 1. Fichiers sources produits par Cowork

| Fichier source Cowork | Fichier cible repo |
|---|---|
| `site-web-prep/RULES-IMPLEMENTATION-v1.6.md` (refonte complète, 13 règles + annexes) | Remplace `site-web-prep/RULES-IMPLEMENTATION.md` |
| `site-web-prep/RULES-MIGRATION-v1.5-vers-v1.6.md` (table de mapping exhaustive) | Nouveau fichier, à pousser tel quel |
| `site-web-prep/BRIEF-CLAUDE-CODE-RULES-v1.6.md` (ce brief) | Référence, à pousser tel quel |

---

## 2. Méthode — 4 lots dans l'ordre

### Lot 0 — Préalable (15 min)

1. Lire `site-web-prep/RULES-IMPLEMENTATION-v1.6.md` en intégralité (la nouvelle version).
2. Lire `site-web-prep/RULES-MIGRATION-v1.5-vers-v1.6.md` (la table de migration).
3. Exécuter `python3 site-web-prep/audit-global.py` pour confirmer l'état de départ (`Total hits : 0` attendu sur v1.5.14).

### Lot 1 — Sauvegarde v1.5.14 + remplacement par v1.6 (15 min)

**Méthode** :

1. **Sauvegarder l'ancien fichier** sous un nom horodaté pour traçabilité :
   ```bash
   cp site-web-prep/RULES-IMPLEMENTATION.md \
      site-web-prep/archives/RULES-IMPLEMENTATION-v1.5.14-archive.md
   ```
   Créer le dossier `archives/` s'il n'existe pas. Mettre un README dans le dossier qui explique : « Archives des versions précédentes de RULES.md pour traçabilité historique. Le référentiel actif est `site-web-prep/RULES-IMPLEMENTATION.md` à la racine de `site-web-prep/`. »

2. **Remplacer le fichier actif** par v1.6 :
   ```bash
   cp site-web-prep/RULES-IMPLEMENTATION-v1.6.md \
      site-web-prep/RULES-IMPLEMENTATION.md
   ```

3. **Supprimer le fichier source `RULES-IMPLEMENTATION-v1.6.md`** (pour éviter la confusion deux fichiers actifs) :
   ```bash
   rm site-web-prep/RULES-IMPLEMENTATION-v1.6.md
   ```

4. **Conserver la table de migration** `RULES-MIGRATION-v1.5-vers-v1.6.md` telle quelle dans `site-web-prep/` (elle reste utile pour traçabilité long terme).

**Livrable Lot 1** : commit `refactor(rules): refonte v1.5.14 → v1.6 simplifiée (13 règles consolidées + annexes)`

### Lot 2 — Audit de cohérence (30 min)

**Méthode** :

1. **Exécuter** `audit-global.py` :
   ```bash
   python3 site-web-prep/audit-global.py
   ```
   Vérifier `Total hits : 0`. Si hits détectés, **STOP** et analyse :
   - Soit la refonte v1.6 a introduit une incohérence non détectée (très improbable car v1.6 ne modifie aucune règle, juste leur organisation)
   - Soit un drift est apparu sur main entre la lecture de RULES v1.6 par Cowork et le push (peu probable mais possible)
   - Dans tous les cas, documenter l'écart dans le rapport mission et **ne pas merger sans correction**.

2. **Lire RULES v1.6 mis en place** et vérifier que :
   - L'en-tête affiche bien `**Version :** 1.6 (refonte simplifiée)`
   - La section 1 contient bien les 13 règles essentielles (A.1 à K.1)
   - L'annexe Section 4 est présente avec ses sous-sections (§ 4.A.1 à § 4.K.1)
   - La section 3 mappe les 13 règles audit aux règles RULES v1.6
   - La section 7 « Historique condensé » mentionne explicitement l'absence de règle abandonnée

3. **Lire la table de migration** et vérifier que :
   - Toutes les règles v1.5.14 sont mentionnées
   - Aucune règle marquée « ❌ Abandonnée » sans justification
   - La synthèse confirme : « Aucune règle abandonnée »

**Livrable Lot 2** : pas de commit dédié. Si OK → passer Lot 3. Si NOK → rapport mission avec écart documenté et arrêt avant merge.

### Lot 3 — Tests croisés (15 min)

**Méthode** :

1. **Test 1 — Simulation d'usage** : ouvrir le nouveau RULES.md et vérifier qu'un Claude Code qui démarre une nouvelle itération peut trouver rapidement l'information clé :
   - Chercher « squelette HTML » → doit trouver F.1
   - Chercher « audit-global » → doit trouver K.1 + section 3
   - Chercher « auto-diagnostic » → doit trouver H.1
   - Chercher « cohérence numérique » → doit trouver B.1
   - Chercher « anti-patterns » → doit trouver J.1

2. **Test 2 — Granularité préservée** : ouvrir l'annexe Section 4 et vérifier que tous les détails opérationnels (gloses canoniques, bibliothèque d'emojis, script d'audit biais sectoriel, règle CSS défensive contraste, anti-patterns historiques) sont bien présents. Cette annexe est le « compendium » qui évite la perte de granularité.

3. **Test 3 — Lisibilité du référentiel principal** : la section 1 (les 13 règles) doit tenir en 6-10 pages A4 imprimées. Si elle dépasse 15 pages, signaler dans le rapport mission — c'est un signal que la refonte n'a pas atteint son objectif de simplification.

**Livrable Lot 3** : pas de commit dédié. Notes de test à inclure dans le rapport mission.

### Lot 4 — Rapport de mission (15 min)

**Méthode** :

Produire `site-web-prep/rapport-mission-rules-v1.6.md` (rapport court, ~500-800 mots) :

```markdown
# Rapport de mission Claude Code — Refonte RULES v1.5.14 → v1.6

**Date** : [date]
**Branche** : [branche]
**Auteur** : Claude Code

## Synthèse exécutive

[2-3 phrases : refonte effectuée, audit OK, écarts éventuels]

## Lots exécutés

[Détail par lot avec preuves]

## Audit-global.py — résultats

- État de départ (v1.5.14) : Total hits : X
- État de fin (v1.6) : Total hits : Y
- [Si X ≠ Y, expliquer]

## Tests croisés

- Test 1 (simulation d'usage) : OK / NOK
- Test 2 (granularité préservée) : OK / NOK
- Test 3 (lisibilité référentiel principal) : OK / NOK (estimation pages)

## Écarts résiduels signalés

[s'il y en a, sinon "Aucun"]

## Recommandations

[suggestions opérationnelles pour la prochaine itération éditoriale du Hub]
```

**Livrable Lot 4** : commit `chore(rules): rapport mission refonte v1.6`

---

## 3. Estimation effort consolidée

| Lot | Sujet | Effort estimé |
|---|---|---|
| Lot 0 | Préalable (lecture v1.6 + migration + audit de départ) | 15 min |
| Lot 1 | Sauvegarde v1.5.14 + remplacement par v1.6 | 15 min |
| Lot 2 | Audit de cohérence (audit-global.py + lecture v1.6) | 30 min |
| Lot 3 | Tests croisés | 15 min |
| Lot 4 | Rapport mission | 15 min |
| **Total** | | **~1h30** |

Itération courte et focalisée. Pas de risque éditorial (aucune modification de contenu du site, uniquement refactor du référentiel).

---

## 4. Workflow recommandé

1. Vérifier que la branche est à jour avec `origin/main` (post-v3.8 mergée).
2. Créer une branche `refactor/rules-v1.6-consolidation`.
3. Exécuter les Lots 0 → 4 dans l'ordre.
4. **PR avec description structurée** :
   - Lien vers ce brief
   - Lien vers `RULES-MIGRATION-v1.5-vers-v1.6.md` (justification de la refonte)
   - Confirmation `audit-global.py` à 0 hit avant et après
   - Confirmation « Aucune règle structurelle abandonnée »
   - Lien vers rapport mission

---

## 5. Règles de prudence

**Spécifique à cette refonte** :

1. **Ne modifie rien dans `audit-global.py`** dans cette itération. La refonte v1.6 mappe les 13 règles automatisées existantes (cf. Section 3 de v1.6), mais n'introduit pas de nouvelle fonction d'audit. Toute évolution de `audit-global.py` se fera dans une itération ultérieure.

2. **Ne modifie aucun fichier HTML, CSS, JS du site**. Cette refonte concerne uniquement le référentiel `RULES-IMPLEMENTATION.md` et les fichiers de documentation associés.

3. **Si tu détectes une règle v1.5.14 qui n'est pas claire dans son mapping vers v1.6**, signale dans le rapport mission plutôt que d'interpréter de ton côté. Blaise tranchera.

4. **L'archive `RULES-IMPLEMENTATION-v1.5.14-archive.md`** doit rester lisible mais ne plus être en chemin actif. Le seul fichier de référence pour les itérations futures est `RULES-IMPLEMENTATION.md` à la racine de `site-web-prep/`.

---

## 6. Décisions explicites de NE PAS faire

- **Pas de modification du site** (HTML, CSS, JS).
- **Pas de modification d'`audit-global.py`** dans cette itération.
- **Pas de nouvelles règles** dans v1.6. C'est une pure consolidation.
- **Pas de suppression de règle** v1.5.14 sans justification explicite dans la table de migration.

---

## 7. Validation finale avant PR

```
☐ RULES v1.6 lu en intégralité avant de commencer.
☐ Table de migration lue (vérification cohérence avec v1.5.14).
☐ audit-global.py de départ exécuté (0 hit confirmé).
☐ Les 4 lots ont été exécutés.
☐ RULES-IMPLEMENTATION.md sur le repo est désormais la v1.6.
☐ RULES-IMPLEMENTATION-v1.5.14-archive.md est dans site-web-prep/archives/.
☐ RULES-IMPLEMENTATION-v1.6.md (le source) a été supprimé pour éviter la confusion.
☐ RULES-MIGRATION-v1.5-vers-v1.6.md est conservé dans site-web-prep/.
☐ audit-global.py de fin exécuté (0 hit confirmé).
☐ Aucun fichier HTML/CSS/JS du site modifié.
☐ Rapport mission rapport-mission-rules-v1.6.md produit et committé.
☐ Description de PR pointe vers ce brief + RULES v1.6 + migration + rapport mission.
```

---

## 8. Fichiers de référence

- **Brief de cette itération** : `BRIEF-CLAUDE-CODE-RULES-v1.6.md` (ce fichier)
- **Source v1.6** : `site-web-prep/RULES-IMPLEMENTATION-v1.6.md` (à pousser comme remplacement de v1.5.14)
- **Table migration** : `site-web-prep/RULES-MIGRATION-v1.5-vers-v1.6.md`
- **Garde-fou** : `site-web-prep/audit-global.py`
- **Référentiel actuel à remplacer** : `site-web-prep/RULES-IMPLEMENTATION.md` v1.5.14

---

## 9. Contact

Pour toute question : Blaise Cavalli — blaise.cavalli@questforchange.eu

**Tu travailles en autonomie sur cette itération courte.** Si tu détectes une règle v1.5.14 imparfaitement mappée vers v1.6, arrête-toi et documente dans le rapport mission.

**Bonne mission, et merci pour le travail !**

---

*Brief produit par Cowork le 11 mai 2026 à la demande de Blaise (item I-001 transmis par le canal Cowork Hub IA Plateforme). Cette refonte est une consolidation pure — aucune nouvelle règle, aucune règle abandonnée.*
