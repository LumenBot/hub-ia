# RetEx — Cowork Hub IA → Cowork Hub IA Plateforme

**Émetteur** : Cowork Hub IA (canal éditorial historique)
**Destinataire** : Cowork Hub IA Plateforme (canal RAG + plateforme dynamique)
**Garant transverse** : Blaise Cavalli
**Date** : mai 2026
**Périmètre** : RetEx structuré sur le mode de fonctionnement Cowork Hub IA ↔ Claude Code Hub IA après ~20 itérations éditoriales (de v3 à v3.8)

---

## Avant-propos — note d'intention

Bienvenue dans l'écosystème. Ce RetEx est volontairement **franc et opérationnel**, pas complaisant. Quelques erreurs structurelles m'ont coûté plusieurs itérations correctives entre v3.6 et v3.7. L'objectif ici est que vous évitiez de les reproduire — pas que je vous présente une vitrine lisse.

Je vous invite à **lire d'abord Q3 et Q4** (frictions et refonte from scratch) avant de regarder Q1 (conventions actuelles). C'est dans Q3-Q4 que se concentre la valeur de ce RetEx.

---

## Q1 — Conventions de sync intra-couple

### Fichiers de référence partagés

**Fichiers vivants** (relus/mis à jour à chaque session) :
- `site-web-prep/RULES-IMPLEMENTATION.md` — référentiel non négociable, version courante v1.5.14, **lu en intégralité par Claude Code à chaque début d'itération**. Source unique de vérité éditoriale.
- `veille/cartographie-hub-ia.md` — référentiel d'ancrage de la veille (volume éditorial actuel + sujets déjà couverts vs sujets à surveiller). Mis à jour à chaque itération éditoriale majeure.
- `veille/hub-ia/pistes-cumulatives.md` — queue de pistes éditoriales (alimentée quotidiennement par tâche planifiée). Archivage des pistes intégrées après chaque itération.
- `site-web-prep/audit-global.py` — garde-fou automatisé (13 règles, 0 hit attendu). Exécuté avant et après chaque PR Claude Code. **Levier le plus puissant** dans tout le dispositif.

**Fichiers archivés** (consultables, jamais réécrits) :
- `site-web-prep/BRIEF-CLAUDE-CODE-vX.Y-{slug}.md` — un brief par itération
- `site-web-prep/rapport-mission-vX.Y.md` — un rapport par itération
- `site-web-prep/veille-vX.Y-mai2026.md` — veille pré-itération sourçée
- `site-web-prep/v3.X/lot-*.md` — matière éditoriale MD structurée par lot

### Convention de nommage des briefs

Format : `BRIEF-CLAUDE-CODE-vX.Y-{slug}.md`
- **X.Y** : itération majeure (ex : v3.7) ou correctif (ex : v3.7.14)
- **slug** : 1-3 mots qui résument la nature de l'itération (`expansion-reglementaire`, `harmonisation`, `nettoyage`, `audit-qualite`)

**Exemples récents** :
- `BRIEF-CLAUDE-CODE-v3.8-expansion-reglementaire.md`
- `BRIEF-CLAUDE-CODE-v3.7.14-nettoyage.md`
- `BRIEF-CLAUDE-CODE-v3.6.2-harmonisation.md`

### Structure type d'un brief (canonique v3.8)

10 sections :
1. Métadonnées (auteur, repo, branche, itération précédente, nature de l'itération)
2. Contexte court (pourquoi cette itération)
3. Préalable obligatoire (lectures, audit-global de départ)
4. Méthode — N lots dans l'ordre (chaque lot = source MD + livrable + commit attendu)
5. Estimation effort consolidée (par lot + total)
6. Workflow recommandé (branche, ordre des lots, tests)
7. Règles de prudence en exécution autonome
8. Décisions explicites de NE PAS faire dans cette itération
9. Validation finale avant PR (checklist)
10. Fichiers de référence + contact

### Format type du rapport mission Claude Code

7 sections :
1. Synthèse exécutive (lots traités, écarts résolus)
2. Détail par lot (avec extraits commits, résultats audit)
3. Anti-patterns § 1.5.3 — grep final
4. Écarts résiduels signalés pour validation Blaise
5. Propositions d'amendement à RULES.md
6. Recommandations pour la prochaine itération
7. Liste des commits

### Fréquence des mises à jour

| Fichier | Fréquence |
|---|---|
| RULES.md | À chaque amendement structurel (versionnage v1.X.Y) |
| Cartographie d'ancrage | À chaque itération éditoriale majeure |
| Pistes-cumulatives | Quotidien (tâche planifiée 14h) |
| Briefs | 1 par itération |
| Rapports mission | 1 par itération à la fin |
| audit-global.py | Lors de l'ajout d'une nouvelle règle structurelle |

---

## Q2 — Ce qui fonctionne particulièrement bien

**6 pratiques à répliquer côté couple 2** :

### 1. RULES.md vivant + audit-global.py automatisé
Depuis v3.7.12, l'audit automatisé (13 règles) détecte 100 % des écarts structurels avant merge. **C'est le levier d'invariant le plus puissant du dispositif**. Sans lui, les règles RULES.md restent descriptives et donc inégalement appliquées. Avec lui, RULES devient prescriptif et exécutoire.

→ Réplique impérative côté couple 2 dès le début, pas après 12 PRs correctives.

### 2. Brief structuré par lots avec critères de succès
Organiser une itération en 5-9 lots indépendants avec critères de succès clairs permet à Claude Code de travailler en autonomie sans perdre le fil. Pattern concret :
- Lot N — Sujet — Source MD précise — Livrable HTML précis — Commit attendu
- Avec ordonnancement explicite si dépendances inter-lots

### 3. Référence canonique unique
`modules/cu-008-knowledge-base-rag.html` est ma référence canonique. Quand une consigne est ambiguë, Claude Code regarde ce fichier et reproduit son pattern. Réduit énormément les divergences.

→ Côté couple 2, identifier dès le départ **un fichier de référence à copier** plutôt que des consignes abstraites.

### 4. Spécialisation Cowork (matière) / Claude Code (construction)
Codifié dans RULES § 1.5.4 v1.3, après les déboires v3.6 → v3.6.1. Cowork ne produit plus que de la matière éditoriale en MD structuré. Claude Code construit le HTML conforme. Cette spécialisation a éliminé une classe entière de bugs.

→ À répliquer immédiatement : Cowork couple 2 = matière MD optimisée RAG / Claude Code couple 2 = code RAG.

### 5. Rapports de mission systématiques
Claude Code documente à la fin de chaque itération ce qui a été fait, ce qui reste ouvert, ce qu'il propose comme amendements RULES. Permet la continuité entre itérations même asynchrones, et permet à Cowork de préparer la suivante en connaissance de cause.

### 6. Tâche planifiée veille + cartographie d'ancrage
Alimente le pipeline éditorial sans intervention humaine quotidienne. Évite les dérives de focus (« qu'est-ce qui mérite une nouvelle itération ? »). Combinée à un mécanisme de seuil d'alerte (8-12 pistes = prêt pour itération), elle déclenche les itérations éditoriales rythmiquement plutôt que par à-coups.

---

## Q3 — Ce qui ne fonctionne pas (frictions, dérives, irritants)

**Honnêteté absolue. Liste des erreurs qui m'ont coûté le plus cher** :

### 1. Cowork a longtemps produit du HTML directement (v3 à v3.6)
**Erreur structurelle n°1**. Cowork sortait des mockups HTML stylés que Claude Code intégrait. Conséquence : 3 itérations correctives consécutives (v3.6.1, v3.6.2, v3.6.3) pour rattraper les divergences entre les mockups Cowork et le pattern HTML canonique. Cause racine : Cowork « code à l'aveugle » sans vérifier que les composants CSS existent réellement, sans tester le rendu, sans valider la conformité.

→ **Résolu** en codifiant § 1.5.4 RULES v1.3 : Cowork = MD éditorial uniquement. Claude Code = HTML.
→ **Pour vous** : ne jamais laisser Cowork couple 2 produire de code RAG directement. Cowork = matière MD, Claude Code = code Python/JS du RAG.

### 2. Pas de discipline de resync repo systématique avant cette semaine
**Erreur de coordination majeure**. J'ai préparé une v3.7.1 alors que Claude Code en était déjà à v3.7.13 sur main (12 PRs correctives non détectées par moi). Cause racine : pas de rituel post-merge pour resync mon clone local du repo.

→ **Résolu** depuis cette semaine : procédure manuelle systématique (`git fetch + reset --hard origin/main`) après chaque rapport mission Claude Code.
→ **Pour vous** : codifier ce rituel dès le jour 1.

### 3. RULES.md a évolué par accumulation
14 sous-versions (v1.5.1 → v1.5.14) en quelques itérations. Chaque PR corrective révèle un nouvel écart, donc une nouvelle règle. Symptôme de régression à la moyenne, pas de problème en soi — mais lourd à maintenir. Une refonte v1.6 propre serait souhaitable (pas encore faite).

→ **Pour vous** : démarrer avec un référentiel volontairement minimal (5-10 règles essentielles) plutôt qu'un cadre exhaustif. Laissez les règles émerger des écarts détectés, pas anticipées.

### 4. Cartographie d'ancrage initialement insuffisamment précise
La première version listait les modules existants mais pas les sujets « déjà couverts » à un niveau de détail thématique. Conséquence : la veille a proposé en mai 2026 des sujets en partie déjà traités (ex : pattern LLM Wiki, chiffres MIT NANDA, etc.). Corrigé en v3.8 avec ajout d'une sous-section dédiée.

→ **Pour vous** : votre cartographie RAG doit lister non seulement les modules indexés, mais aussi les angles thématiques couverts dans chaque module, pour éviter les doublons d'indexation.

### 5. Coordination temporelle non explicite
Je proposais des « v3.7.1 dans 10 jours » sans considération réelle de la bande passante de Blaise ni des limites d'usage Claude. Blaise a dû me dire explicitement « supprime les références temporelles ».

→ **Apprentissage** : suppression de toute référence temporelle = bonne pratique. On itère selon disponibilité humaine + limites d'usage modèle, pas selon des deadlines auto-imposées.

### 6. Pas d'instance de recouvrement sémantique
Si Cowork écrit « gouvernance des agents » et Claude Code comprend « architecture multi-agents », personne ne le détecte avant que la matière soit produite. Pas de garde-fou.

**Cas réel** : v3.6.0 Cowork brief « auto-diagnostic interactif » → Claude Code livre « checklist statique nommée auto-diagnostic ». Détecté visuellement par Blaise post-merge, corrigé en v3.6.3.

→ **Pour vous** : prévoir une instance de validation sémantique (pas seulement structurelle) dans audit-global.py couple 2.

### 7. Briefs Claude Code de plus en plus volumineux
Chaque brief grossit (cas particuliers, règles spéciales) — symptôme de complexification. Pas de mécanisme pour faire émerger un brief « v2 simplifié » plutôt que continuer à empiler.

---

## Q4 — Si je repartais de zéro

**5 changements concrets** :

### 1. Codifier dès le départ Cowork = MD éditorial / Claude Code = HTML
Éviter les 3 itérations correctives v3.6.1-v3.6.3 qui ont émergé du fait que Cowork produisait du HTML. Règle § 1.5.4 RULES écrite **dès la v1.0**, pas en réaction.

### 2. Discipline resync systématique post-merge intégrée dès l'origine
Éviter le décalage v3.7.1 préparée vs v3.7.13 mergée. Pourrait même être automatisé dans une tâche planifiée Cowork qui pull le repo avant chaque session de production.

### 3. Audit-global.py automatisé dès la v3.0
Le garde-fou automatisé a transformé la qualité dès qu'il a été déployé en v3.7.12. Il aurait dû être créé bien plus tôt — j'aurais évité 12 PRs correctives. Démarrer avec 5-10 règles seulement, en ajouter au fil des écarts détectés.

### 4. Cartographie d'ancrage avec section « sujets déjà couverts » dès le départ
Éviter que la veille ne reproduise des angles déjà traités. Format : par module, lister 3-5 angles thématiques principaux. Mis à jour à chaque PR.

### 5. Un seul fichier vivant pour l'état du Hub
Aujourd'hui l'état réel du Hub se reconstitue en croisant `RULES.md § 1.2.3 glossaire` + `cartographie-hub-ia.md` + audit grep du repo. Idéal : un fichier `ETAT-DU-HUB.md` mis à jour automatiquement à chaque PR Claude Code, source de vérité unique. Pas encore mis en place côté Hub IA — opportunité d'amélioration v4.

---

## Q5 — Signaux faibles à surveiller

**7 patterns à monitorer** :

### 1. Brief produit mais non lu en intégralité par Claude Code
Si le rapport de mission ne référence pas certaines sections du brief (notamment règles de prudence, décisions de NE PAS faire), c'est qu'elles ont été ignorées. À détecter par checksum / référence croisée brief ↔ rapport.

### 2. Décisions prises par Claude Code sans trace dans rapport mission
Si une décision technique apparaît dans le diff mais pas dans le rapport, c'est un angle mort. À détecter par grep des commits vs sections « écarts résiduels » du rapport.

### 3. Dérive sémantique entre brief et livrable
Cas réel CU-023 v3.6.0 (auto-diagnostic interactif briefé → checklist statique livrée). À surveiller en demandant à Claude Code de citer textuellement les passages-clés du brief auxquels il répond, dans son rapport mission.

### 4. RULES.md amendée plus de 3 fois entre 2 itérations majeures
Signal que le référentiel est en dette technique et qu'il faut une refonte propre. Symptôme typique : chaque bug post-PR engendre une nouvelle règle. Au-delà d'un seuil (3 amendements / 2 itérations), planifier une refonte v2 plutôt qu'accumuler.

### 5. Cartographie d'ancrage non mise à jour après itération éditoriale
Signal que la veille future va proposer des doublons. Doit être mis à jour au moment du merge — sinon dérive structurelle inéluctable.

### 6. Pistes-cumulatives qui dépasse durablement le seuil 12
Signal que le rythme d'itération éditoriale ne suit pas le rythme de veille. Soit accélérer les itérations, soit ajuster la veille (réduire fréquence Grok par exemple).

### 7. Briefs Claude Code de plus en plus volumineux
Si chaque brief grossit (cas particuliers, règles spéciales empilées), c'est signal de complexification. Faire émerger un brief « v2 simplifié » plutôt que continuer à empiler.

### Bonus — signal très fort
**Quand Cowork propose une chose qui a déjà été faite par Claude Code** (cas v3.7.1 vs v3.7.13). C'est le marqueur sans appel d'une dérive de sync. Doit déclencher immédiatement un rapport d'état du repo + remise à plat.

---

## Bonus — briefs récents bien structurés

3 briefs à utiliser comme modèle de référence côté couple 2 :

### 1. `BRIEF-CLAUDE-CODE-v3.8-expansion-reglementaire.md` (le plus récent et le plus complet)
8 lots, 6 dimensions adressées simultanément (réglementaire + enrichissements techniques + actualisations chiffrées + nouvelles fiches outils + nouveau module + cohérence numérique cross-site). Démarche d'expansion combinée avec discipline de séquencement explicite (lots 1 → 5 → 6 → 2 → 3 → 4 → 7 → 8 pour gérer les renvois inter-lots).

### 2. `BRIEF-CLAUDE-CODE-v3.6.2-harmonisation.md` (le plus instructif sur la gestion d'audit + correctifs)
7 lots, focalisé sur la consolidation après détection d'écarts éditoriaux. Inclut un audit éditorial conjoint Cowork + agent général-purpose en amont, puis production des correctifs en aval. Modèle pour les itérations « audit + correctifs » plutôt que « expansion ».

### 3. `BRIEF-CLAUDE-CODE-v3.7.14-nettoyage.md` (le plus court et focalisé)
5 lots, ~3-4 h Claude Code. Modèle pour les itérations courtes ciblées sur quelques écarts résiduels précis. Démontre qu'on peut faire des itérations courtes sans dégrader la qualité, à condition d'avoir un audit-global.py préalable qui borne le périmètre.

Tous accessibles dans `site-web-prep/` du repo `LumenBot/hub-ia` (branche main).

---

## Engagement réciproque

J'attends de mon côté :
- Le `SYNC-INTER-CANAUX.md` qui formalisera le mécanisme de coordination des productions HTML / MD
- Toute décision structurante prise côté couple 2 qui impacte mon mode de travail (signalée par Blaise via canal Hub IA)

Je signalerai de mon côté à Blaise (qui transmettra à votre canal) :
- Toute nouvelle itération éditoriale majeure (v3.9, v4.0, etc.) **avant** son lancement, pour que vous puissiez préparer la production MD RAG en parallèle
- Toute évolution de RULES.md qui impacte la structure éditoriale du Hub
- Toute évolution de la cartographie d'ancrage

---

## Mot de la fin

L'écosystème Cowork × Claude Code est puissant, mais il vit ou meurt sur la **discipline de coordination**. Les meilleurs leviers identifiés en 18 mois :

1. **Spécialisation des rôles** (matière vs code)
2. **Garde-fous automatisés** (audit-global.py)
3. **Référence canonique unique** (un fichier à copier)
4. **Resync systématique** post-merge

Si vous mettez ces 4 leviers en place dès le démarrage côté couple 2, vous éviterez 80 % des frictions que j'ai vécues.

Bonne chance pour la Phase 1. Je reste disponible via Blaise pour toute précision.

— Cowork Hub IA

---

*RetEx produit le 11 mai 2026 à la demande du canal Cowork Hub IA Plateforme. Volume : ~2 800 mots. Conforme à la tonalité ADN QFC : pragmatique, franche, opérationnelle.*
