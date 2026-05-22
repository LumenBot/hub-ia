# Lot C v3.12 — PR-11 « Cycle de vie d'un projet IA » (nouveau préalable, re-positionnement idée 2)

**Brief consolidé pour Claude Code** : création complète d'un nouveau préalable PR-11 dédié à la vue séquentielle bout en bout d'un projet IA en PME. Re-positionnement de l'idée 2 du brainstorming (initialement proposée comme CU « Cycle de vie ») en préalable transverse, validé par Blaise.

**Décision validée** : PR-11 (pas CU). Justification : un cycle de vie projet est par nature transverse à tous les cas d'usage, donc plus pertinent en préalable qu'en cas d'usage métier.

**Référence canonique structure HTML** : `prealables/pr-08-financer-projet-ia.html`.

**Particularité de ce préalable** : il intègre et séquence les autres préalables (PR-09 amont, PR-10 vérification) + cross-link dense avec les fiches DEP qui couvrent les volets techniques. C'est la **vue d'ensemble** de la section Préalables.

---

## Architecture du préalable PR-11

**Module cible** : `prealables/pr-11-cycle-de-vie-projet-ia.html` (à créer)
**Titre** : « Cycle de vie d'un projet IA »
**Sous-titre/accroche** : « 9 étapes séquencées et 3 quality gates obligatoires : la vue d'ensemble bout en bout d'un projet IA en PME, depuis le cadrage jusqu'à la mise en service. »
**Badge complexité** : ⭐⭐ Opérationnel
**Badge angle** : 🔄 Vue d'ensemble séquentielle
**Badge temps de lecture** : 20 min

### Sommaire (TOC) proposé

```html
<ul class="module-toc-list" id="tocList">
  <li><a href="#executive-summary">⚡ L'essentiel</a></li>
  <li><a href="#section-1">🧭 Pourquoi un cycle de vie séquencé</a></li>
  <li><a href="#section-2">🔢 Les 9 étapes du projet IA</a></li>
  <li><a href="#section-3">🚦 Les 3 quality gates obligatoires</a></li>
  <li><a href="#section-4">💥 Le coût des courts-circuits</a></li>
  <li><a href="#section-5">📊 Cas d'usage type — automatisation order-to-cash</a></li>
  <li><a href="#section-6">🔗 Articulation avec les autres préalables et fiches DEP</a></li>
  <li><a href="#section-7">🚀 Plan d'action 30 jours</a></li>
  <li><a href="#ressources">📚 Pour aller plus loin</a></li>
</ul>
```

---

## Contenu détaillé par section

### Executive summary

**Titre exec** : *« 9 étapes séquencées, 3 quality gates obligatoires : sauter une étape coûte généralement 5 à 10 fois l'effort gagné. »*

**5 takeaways** :

1. **Un projet IA en PME suit un cycle de vie en 9 étapes** qui ne sont pas interchangeables. L'ordre compte : l'analyse de besoin avant le cadrage, le cadrage avant la spec, la spec avant le développement, le développement avant les tests, les tests avant la mise en service.
2. **3 quality gates obligatoires séparent les phases critiques** : gate 1 (entre cadrage et spec — décision GO/NO-GO sur l'opportunité), gate 2 (entre développement et tests — validation que ce qui est livré correspond à ce qui était spécifié), gate 3 (entre tests et mise en service — validation que la qualité observée est suffisante pour la production).
3. **Le pattern « ne pas sauter d'étape » est une discipline projet** parce que chaque étape sautée se paie 5 à 10 fois plus cher en aval. Un cadrage bâclé devient un projet en dérive de scope ; une spec absente devient un développement orienté solution avant problème ; des tests insuffisants deviennent une mise en service ratée.
4. **Cette vue séquentielle est complémentaire des fiches DEP** qui couvrent chaque étape technique en détail. PR-11 donne la **carte d'ensemble** ; les DEP donnent les **boîtes à outils** pour chaque étape.
5. **Le cas d'usage type d'automatisation order-to-cash** illustre comment chaque étape s'applique à un projet concret de PME (cf. § 5).

**Stat block** suggéré :

- **9** étapes du cycle de vie
- **3** quality gates obligatoires
- **5 à 10×** coût d'une étape sautée vs effort gagné
- **80 %** des échecs interviennent avant la première ligne de code (déjà canonisé dans PR-09 + DEP-01)

### Section 1 — Pourquoi un cycle de vie séquencé

**3 raisons structurelles** à l'existence d'un cycle de vie obligatoire :

1. **L'ordre des décisions n'est pas réversible à coût égal.** Décider d'un budget après avoir engagé un prestataire coûte plus cher que l'inverse. Décider d'un critère de succès après le déploiement est inutile (on ne sait plus si on a réussi ou échoué). Le séquencement protège la rationalité économique du projet.

2. **Chaque étape produit un livrable qui entre dans l'étape suivante.** Sans le livrable de cadrage (PR-09), la spec ne peut pas être rédigée correctement. Sans la spec, le développement dérive. Sans le développement testé, la mise en service est aveugle. Sauter une étape, c'est entrer dans l'étape suivante les mains vides.

3. **Les quality gates sont des points de décision conscients** où on peut **arrêter le projet** si les critères ne sont pas atteints. Sans gates explicites, le projet continue par inertie même quand les signaux sont mauvais (cf. anti-pattern « absence de plan d'arrêt » documenté dans PR-09).

**Implication pour le dirigeant** : la fonction du dirigeant dans un projet IA n'est pas de « valider la solution » à la fin, c'est de **valider chaque gate** au moment où elle se présente. C'est un rythme managérial à intégrer dans l'agenda — pas une intervention ponctuelle en clôture.

### Section 2 — Les 9 étapes du projet IA

Chaque étape a un livrable propre et une durée typique. Les durées sont indicatives pour un projet PME standard (cas d'usage métier ciblé, équipe interne + 1 prestataire, budget 20-100 K€).

| # | Étape | Livrable | Durée typique | Préalable / DEP de référence |
|---|---|---|---|---|
| **1** | **Analyse du besoin métier** | Liste hiérarchisée des irritants métier candidats | 1-2 semaines | PR-01, PR-02 |
| **2** | **Cadrage du projet** | Document de cadrage 1 page (8 questions) | 1-2 semaines | **PR-09** |
| **3** | **Décision GO/NO-GO** | Validation explicite par décisionnaire | Quelques jours | **Quality gate 1** |
| **4** | **Spec fonctionnelle et technique** | Document de spec détaillé (5-15 pages) | 2-4 semaines | DEP-01 |
| **5** | **Plan de développement** | Roadmap technique + planning + ressources | 1-2 semaines | DEP-01, DEP-04 |
| **6** | **Développement** | Code source + documentation technique | 4-12 semaines | DEP-02, DEP-03, DEP-04, DEP-05 |
| **7** | **Tests et évaluation** | Rapport d'évaluation + golden set + corrections | 2-4 semaines | DEP-07 |
| **8** | **Validation pré-production** | Validation décisionnaire pour mise en service | Quelques jours | **Quality gate 2 et 3** |
| **9** | **Mise en service et suivi** | Production opérationnelle + KPI suivis | Continu post-déploiement | DEP-05, DEP-08, **PR-10** |

**Total durée typique projet PME** : 12 à 26 semaines (3 à 6 mois), variable selon complexité.

**Note sur les durées** : ces durées peuvent paraître longues. Elles correspondent à l'observation de projets réussis. Les projets qui visent à « aller plus vite » en sautant des étapes finissent généralement par prendre plus de temps au total — parce que les corrections en aval sont plus coûteuses que la prévention en amont.

### Section 3 — Les 3 quality gates obligatoires

Les quality gates sont des **décisions conscientes** prises par un décisionnaire identifié, avec critères explicites de GO ou NO-GO.

#### Gate 1 — Entre cadrage (étape 2) et spec (étape 4)

**Question décisionnelle** : *« Le projet vaut-il la peine d'être engagé ? »*

**Critères de GO** : les 8 questions de cadrage (cf. PR-09) ont reçu des réponses claires, le budget est validé, le décisionnaire est nommé, le critère de succès est mesurable, le plan d'arrêt est défini.

**Critères de NO-GO** : un ou plusieurs critères ci-dessus est flou, irréaliste ou non validé. Dans ce cas, retourner à l'étape de cadrage pour clarification — pas avancer en espérant que ça se précisera en cours de route.

**Décisionnaire typique** : direction (dirigeant ou comité de direction).

#### Gate 2 — Entre développement (étape 6) et tests (étape 7)

**Question décisionnelle** : *« Ce qui est livré correspond-il à ce qui était spécifié ? »*

**Critères de GO** : le livrable couvre l'ensemble du périmètre de spec, sans dérive non documentée. Les écarts éventuels sont explicitement listés et arbitrés.

**Critères de NO-GO** : dérive de scope non arbitrée, fonctionnalités majeures manquantes, qualité du livrable manifestement insuffisante. Dans ce cas, retourner au développement pour corrections — ne pas démarrer les tests sur un livrable incomplet.

**Décisionnaire typique** : chef de projet IA + représentant utilisateur final.

#### Gate 3 — Entre tests (étape 7) et mise en service (étape 9)

**Question décisionnelle** : *« La qualité observée est-elle suffisante pour la production ? »*

**Critères de GO** : le golden set est passé avec succès (score cible défini en cadrage atteint), les hallucinations critiques sont absentes (cf. PR-10), le mécanisme de vérification est en place, le human owner est désigné, le plan d'arrêt est opérationnel.

**Critères de NO-GO** : score golden set en-dessous de la cible, hallucinations critiques détectées, mécanisme de vérification non implémenté, human owner non désigné. Dans ce cas, retourner aux tests pour corrections — pas mettre en service un système non vérifié.

**Décisionnaire typique** : direction + chef de projet + responsable qualité.

**Cohérence avec PR-10** : la gate 3 intègre directement les principes de vérification définis dans PR-10 (4 niveaux proportionnés à l'enjeu, pattern « pas de claim de complétion sans preuve fraîche », human owner désigné).

### Section 4 — Le coût des courts-circuits

**Pattern observé** : la pression de calendrier ou de budget pousse régulièrement à sauter une étape ou contourner une gate. Coût réel de chaque court-circuit, observable sur des projets réels :

| Court-circuit | Économie apparente | Coût réel | Ratio coût/économie |
|---|---|---|---|
| **Sauter le cadrage** (étape 2) | 1-2 semaines | 1-3 mois de dérive de scope en aval | 4-12× |
| **Sauter le GO/NO-GO** (gate 1) | Quelques jours | Projet engagé sans alignement direction = abandon probable à mi-parcours | 10-30× |
| **Sauter la spec** (étape 4) | 2-4 semaines | Développement orienté solution avant problème, refonte en aval | 3-6× |
| **Sauter les tests** (étape 7) | 2-4 semaines | Mise en service ratée, perte de confiance utilisateurs, retours qualité | 5-15× |
| **Sauter la validation pré-production** (gate 3) | Quelques jours | Incidents en production, hallucinations non détectées, contentieux | 10-50× (dépend de la criticité) |

**Lecture** : un cadrage sauté économise apparemment 1-2 semaines mais coûte généralement 1-3 mois en dérive aval. Le ratio coût/économie est de 4× à 12×. Aucun court-circuit n'est rentable à moyen terme.

**Garde-fou** : si la pression de calendrier est telle qu'on est tenté de sauter une étape, **réduire le périmètre du projet** plutôt que sauter l'étape. Mieux vaut livrer un périmètre v1 bien construit qu'un périmètre v2 mal exécuté.

### Section 5 — Cas d'usage type — automatisation order-to-cash

Illustration concrète des 9 étapes appliquées à un projet d'automatisation order-to-cash (de la commande au paiement) dans une PME industrielle de 50 salariés.

**Étape 1 — Analyse du besoin métier** (2 semaines)
Le dirigeant identifie 3 irritants candidats : (1) délai de traitement des factures fournisseurs trop long, (2) erreurs récurrentes sur les bons de livraison, (3) DSO clients qui s'allonge. Hiérarchisation : (3) prioritaire (impact trésorerie immédiat).

**Étape 2 — Cadrage** (1 semaine)
Document de cadrage rédigé : problème = « réduire le DSO de 45 à 30 jours sur les clients PME », utilisateur = équipe comptabilité (3 personnes), données = ERP + outil de facturation + boîte mail compta, contrainte RGPD validée, KPI = DSO mensuel, budget 30 K€ initial + 500 €/mois récurrent, calendrier 4 mois jusqu'à mise en service, plan d'arrêt = si DSO non amélioré à 6 mois post-déploiement, retour au manuel.

**Étape 3 — Gate 1 GO/NO-GO** (2 jours)
Validation comité de direction. Décision GO. Mandat signé.

**Étape 4 — Spec fonctionnelle et technique** (3 semaines)
Spec détaillée : agent IA qui scanne les emails compta, identifie les factures impayées, classe par ancienneté, génère des relances personnalisées validées avant envoi (niveau 2 vérification PR-10). Stack : Claude Sonnet 4.6 + intégration ERP via API.

**Étape 5 — Plan de développement** (1 semaine)
Roadmap 8 semaines, ressources : 1 prestataire IA-natif + 1 référent interne, budget 25 K€ dev + 5 K€ tests.

**Étape 6 — Développement** (8 semaines)
Réalisation par le prestataire avec sprints hebdomadaires, démos intermédiaires.

**Étape 7 — Tests et évaluation** (3 semaines)
Construction golden set de 40 emails types, mesure de précision sur identification factures (cible 95 %), mesure qualité relances générées (cible LLM-as-judge >0.85), tests utilisateurs avec équipe compta.

**Étape 8 — Gate 2 et 3** (3 jours)
Gate 2 : livrable conforme à spec, validé par chef de projet. Gate 3 : score golden set 96 %, 0 hallucination critique détectée, mécanisme de vérification niveau 2 en place (chaque relance validée humainement avant envoi), human owner désigné (responsable compta). GO mise en service.

**Étape 9 — Mise en service et suivi** (continu)
Déploiement progressif (semaine 1 = 10 % des clients, semaine 2 = 50 %, semaine 4 = 100 %). Suivi DSO mensuel. Revue à 3 mois.

**Durée totale** : ~22 semaines (5,5 mois). **Budget total** : ~32 K€ initial + 6 K€/an récurrent. **Résultat attendu** : DSO de 45 à 30 jours dans les 6 mois post-déploiement.

**Note** : ce cas d'usage est illustratif. Les durées et budgets sont indicatifs pour calibrer les ordres de grandeur. Un projet réel sera plus ou moins long selon la complexité spécifique.

### Section 6 — Articulation avec les autres préalables et fiches DEP

**Vue de synthèse** : PR-11 est la **carte d'ensemble**. Les autres préalables et fiches DEP sont les **boîtes à outils** détaillées de chaque étape.

| Étape du cycle | Préalable détaillé | Fiche DEP détaillée |
|---|---|---|
| 1. Analyse besoin | PR-01 (maturité organisationnelle), PR-02 (marché IA) | — |
| 2. Cadrage | **PR-09** (cadrer un projet IA) | — |
| 3. Gate 1 GO/NO-GO | PR-08 (financement, si budget arbitré) | — |
| 4. Spec | — | DEP-01 (cadrer un projet IA — angle technique) |
| 5. Plan dev | PR-07 (build vs buy) | DEP-01, DEP-04 (fine-tuning si pertinent) |
| 6. Développement | — | DEP-02 (RAG en production), DEP-03 (context engineering), DEP-04 (fine-tuning), DEP-05 (agents en production) |
| 7. Tests | — | DEP-07 (évaluation continue) |
| 8. Gate 2 et 3 | **PR-10** (vérifier et limiter hallucinations) | DEP-07 |
| 9. Mise en service | PR-05 (sécurité IA), **PR-10** | DEP-05 (agents en production), DEP-08 (sécurité agents et MCP) |

**Lecture** : un dirigeant qui pilote un projet IA peut utiliser PR-11 comme **table des matières opérationnelle** et naviguer vers le préalable ou la fiche DEP correspondant à l'étape qu'il aborde.

**Cohérence avec l'axe 2 aide à la décision** (note de concept évolution Hub IA mai 2026) : PR-11 préfigure la logique de « parcours suggéré » qui sera l'ossature de l'aide à la décision Phase 3 de la plateforme dynamique. Les 9 étapes sont les **briques de parcours** que l'agent conversationnel orchestrera.

### Section 7 — Plan d'action 30 jours

**Jours 1-7 — Diagnostic existant**
- Identifier les projets IA actuellement en cours dans l'entreprise
- Pour chacun, positionner sur les 9 étapes : où en est-on ?
- Identifier les éventuelles étapes sautées ou gates non validées

**Jours 8-14 — Reprise structurée**
- Pour les projets en dérive (étape sautée ou gate non validée) : retour à l'étape manquée
- Documenter les étapes déjà franchies dans le format livrable attendu
- Mettre à jour le document de cadrage si nécessaire

**Jours 15-21 — Mise en place des gates**
- Pour les projets en cours qui n'ont pas eu de gate explicite, programmer la prochaine gate
- Identifier le décisionnaire de chaque gate
- Formaliser les critères de GO/NO-GO en amont

**Jours 22-30 — Routine projet**
- Intégrer le cycle de vie dans les routines de pilotage de l'entreprise (par exemple, revue mensuelle des projets IA = revue de gates)
- Programmer les revues à fréquence régulière
- Communiquer le cycle de vie à l'équipe pour partage de référentiel commun

---

## Ressources à intégrer

### Articles de fond
- **McKinsey State of AI 2025** — chiffre « 80 % des échecs avant première ligne de code » (déjà canonisé I-D-006, cohérence avec PR-09 et DEP-01)
- **Bpifrance Le Lab** — études cycles de projets IA en PME (déjà citées PR-04 + PR-08)
- **Cloud Security Alliance** — guidelines qualité projet IA (déjà citée CU-027 + DEP-08)

### Tutoriels & cas pratiques
- **Template de matrice de suivi** des 9 étapes pour un projet IA (à fournir en téléchargement)
- **Cas d'usage type order-to-cash** détaillé (cf. § 5) en version étendue téléchargeable
- **Auto-diagnostic** : à quelle étape se trouve mon projet IA ? Y a-t-il des étapes sautées ?

### Documentation officielle & études
- **AI Act EU** — articles relatifs à la documentation tout au long du cycle de vie (Article 11 documentation technique, Article 17 quality management system)
- **NIST AI RMF** — cycle de vie projet IA et gestion des risques par phase
- **HAS-CNIL** — guide « Accompagner le bon usage des systèmes d'IA » (10 fiches dédiées au cycle de vie — déjà cité CU-020 v3.10)

### Contacts opérationnels
- **Bpifrance** — diagnostic Data IA (souvent étape 1-2 d'un cycle de vie projet IA — cohérence PR-08)
- **Réseau QFC / QFB / QA** — accompagnement structurant tout au long du cycle

---

## Mise à jour navigation et page préalables

- Ajouter une **card PR-11** dans `prealables.html` après PR-10
- Position dans la liste : à la suite de PR-10 (ordre numérique)
- Icône suggérée : 🔄
- Catégorie : « Vue d'ensemble séquentielle »
- Cross-link denses avec **TOUS les autres préalables** (PR-01 à PR-10) et les fiches DEP-01 + DEP-02 + DEP-03 + DEP-04 + DEP-05 + DEP-07 + DEP-08 (PR-11 est la table des matières opérationnelle)

## Cross-link réciproque depuis autres préalables (à mettre à jour)

Les préalables existants doivent **tous mentionner PR-11** comme vue d'ensemble séquentielle qui les intègre :
- **PR-01** : encart « pour la vue d'ensemble séquentielle d'un projet IA, voir PR-11 »
- **PR-02, PR-04, PR-05, PR-07, PR-08, PR-09, PR-10** : encart symétrique
- Idem dans les fiches DEP-01 à DEP-08

Cette densité de cross-links est ce qui fait de PR-11 un préalable **pivot** de la section.

## Métadonnées module

- `<meta name="description">` : *« Cycle de vie d'un projet IA en PME : 9 étapes séquencées, 3 quality gates obligatoires, pourquoi sauter une étape coûte 5 à 10 fois plus cher qu'en gagnant le temps économisé. La vue d'ensemble pour piloter un projet IA bout en bout. »*
- Badge temps de lecture : **20 min**

## Item parallèle (à compiler dans brief v3.12)

Pas de canonisation chiffre macro nouveau pour PR-11 — les chiffres mobilisés sont déjà canonisés via PR-09 (« 80 % des échecs avant code ») ou sont des ordres de grandeur illustratifs.
