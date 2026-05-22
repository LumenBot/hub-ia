# Lot A v3.12 — PR-09 « Cadrer un projet IA avant de choisir un outil » (nouveau préalable)

**Brief consolidé pour Claude Code** : création complète d'un nouveau préalable PR-09 dédié au cadrage amont d'un projet IA pour un dirigeant non-IT. Premier préalable d'une série de 3 (PR-09 amont + PR-10 vérification + PR-11 cycle de vie complet).

**Décision validée par Blaise** : nouveau préalable PR-09 (pas DEP, pas CU). Positionnement complémentaire de DEP-01 « Cadrer un projet IA » côté Déploiement — angles différenciés à codifier explicitement.

**Référence canonique structure HTML** : `prealables/pr-08-financer-projet-ia.html` (préalable le plus récent, créé en v3.10, structure 7 sections H2 + executive summary + ressources).

---

## Architecture du préalable PR-09

**Module cible** : `prealables/pr-09-cadrer-projet-ia.html` (à créer)
**Titre** : « Cadrer un projet IA avant de choisir un outil »
**Sous-titre/accroche** : « Les 8 questions à se poser avant de regarder le moindre outil — pourquoi 80 % du soin doit aller sur le cadrage initial, et comment éviter le piège du tech push. »
**Badge complexité** : ⭐⭐ Opérationnel
**Badge angle** : 🧭 Cadrage stratégique
**Badge temps de lecture** : 15 min

### Sommaire (TOC) proposé

```html
<ul class="module-toc-list" id="tocList">
  <li><a href="#executive-summary">⚡ L'essentiel</a></li>
  <li><a href="#section-1">🚨 Le piège du tech push</a></li>
  <li><a href="#section-2">🧭 Les 8 questions de cadrage</a></li>
  <li><a href="#section-3">⚖️ Pattern « refuser d'avancer sans clarification »</a></li>
  <li><a href="#section-4">⚠️ 5 anti-patterns courants</a></li>
  <li><a href="#section-5">🎯 Le livrable de cadrage minimal</a></li>
  <li><a href="#section-6">🔗 Articulation avec les autres préalables</a></li>
  <li><a href="#section-7">🚀 Plan d'action 30 jours</a></li>
  <li><a href="#ressources">📚 Pour aller plus loin</a></li>
</ul>
```

---

## Contenu détaillé par section

### Executive summary (à transposer en `.exec-summary`)

**Titre exec** : *« 80 % du soin d'un projet IA doit aller sur le cadrage initial — avant le moindre choix d'outil. »*

**5 takeaways** :

1. **Le piège du tech push est la cause n°1 d'échec des projets IA en PME.** Choisir d'abord un outil (parce qu'on l'a vu en démo, parce qu'on en a entendu parler, parce que le DSI l'utilise) puis chercher rétroactivement à quoi il va servir, mène mécaniquement à un projet sans valeur métier — même si l'outil est techniquement excellent.
2. **8 questions de cadrage doivent recevoir une réponse claire avant tout choix d'outil** : quel problème métier ? quel utilisateur ? quelles données disponibles ? quelles contraintes RGPD ? quel critère de succès ? quel budget ? quel calendrier ? quel arbitrage en cas d'échec ?
3. **Le pattern « refuser d'avancer sans clarification » est une discipline projet — pas une posture obstructionniste.** Mieux vaut perdre 2 heures à clarifier qu'aller 2 mois dans une mauvaise direction.
4. **5 anti-patterns courants à reconnaître** : tech push (« j'ai vu, je veux »), boîte noire (« on verra à l'usage »), périmètre extensible, mesure de succès floue, absence de plan d'arrêt.
5. **Le livrable de cadrage minimal tient sur 1 page** : c'est un document partageable, datable, contestable. Sans lui, aucune décision projet n'est défendable.

**Stat block** suggéré :

- **80 %** des échecs interviennent **avant la première ligne de code** (cohérence avec heuristique DEP-01 v3.10)
- **8 questions** de cadrage minimal
- **1 page** pour le livrable de cadrage
- **2 heures** d'effort cadrage = plusieurs semaines d'effort projet économisé en moyenne

### Section 1 — Le piège du tech push

**3 manifestations à reconnaître** :

1. **Le « j'ai vu Copilot Studio, je veux ça »** — un dirigeant assiste à une démo impressionnante d'un outil et veut le déployer chez lui, sans avoir identifié le problème métier que l'outil résoudrait. La démo a fait son effet, mais la démo n'est pas le contexte de la PME.
2. **Le « tout le monde fait du RAG, on doit en faire »** — un dirigeant lit qu'un pattern technique est mainstream et veut le mettre en place. Le pattern peut être pertinent ou pas selon le contexte de la PME, mais la pression sociale ne fait pas un projet.
3. **Le « notre DSI maîtrise ChatGPT, on va l'utiliser pour tout »** — un dirigeant s'appuie sur les compétences disponibles en interne pour orienter le projet, plutôt que sur le besoin métier. Le risque : un outil généraliste utilisé partout, sans qu'aucun cas d'usage ne soit traité avec précision.

**Pourquoi ces réflexes sont structurants** : ils paraissent rationnels (« on choisit le meilleur outil », « on suit la tendance », « on s'appuie sur l'expertise interne ») mais ils inversent l'ordre logique du projet. **L'outil est une réponse, pas une question.** Tant que la question n'est pas posée, l'outil n'a pas de sens.

**Coût observé** : les projets IA PME démarrés par le tech push aboutissent dans une majorité de cas à des outils déployés mais peu utilisés, à des budgets engagés sans ROI mesurable, à des équipes démotivées par des solutions qui ne résolvent pas leurs problèmes réels. Dans le pire des cas, ils consomment 6 à 12 mois de bandwidth managériale avant d'être abandonnés.

### Section 2 — Les 8 questions de cadrage

Ces 8 questions doivent recevoir une réponse claire — pas une intention, pas une approximation — avant tout choix d'outil.

| # | Question | Critère de réponse claire |
|---|---|---|
| **1** | Quel problème métier précis veut-on résoudre ? | Formulation en 1-2 phrases, mesurable, validée par la personne qui vit le problème |
| **2** | Quel est l'utilisateur final qui consommera l'output ? | Profil précis (poste, contexte d'usage, fréquence), pas « les équipes en général » |
| **3** | Quelles données sont disponibles et utilisables ? | Liste des sources accessibles, formats, qualité, conformité RGPD validée |
| **4** | Quelles contraintes réglementaires s'appliquent ? | RGPD, AI Act, sectorielles (santé, finance), souveraineté requise (UE/SecNumCloud) |
| **5** | Comment mesure-t-on le succès du projet ? | KPI quantifiable défini avant lancement, valeur cible, fréquence de mesure |
| **6** | Quel est le budget engageable (initial + récurrent 12 mois) ? | Ordre de grandeur validé, ligne budgétaire identifiée, marge pour itérations |
| **7** | Quel est le calendrier réaliste (POC + déploiement) ? | Étapes datées, dépendances explicites, marge pour imprévus |
| **8** | Quel est le plan d'arrêt en cas d'échec mesuré ? | Critères d'arrêt définis, décisionnaire identifié, coûts d'arrêt anticipés |

**Pourquoi 8 et pas plus** : 8 questions suffisent à éliminer 80 % des projets mal-conçus. Au-delà, on entre dans le détail de la spec qui appartient à l'étape suivante (cf. PR-11 cycle de vie projet IA).

**Pourquoi 8 et pas moins** : chacune de ces questions correspond à une cause classique d'échec documentée. Les sauter, c'est s'exposer au piège correspondant.

### Section 3 — Le pattern « refuser d'avancer sans clarification »

Une fois les 8 questions identifiées, le pattern complémentaire est la **discipline de refuser d'avancer** tant qu'une réponse n'est pas claire. C'est un pattern managérial, pas technique.

**Formulation opérationnelle** : *« Mieux vaut perdre 2 heures à clarifier qu'aller 2 mois dans une mauvaise direction. »*

**Application concrète** :
- Devant un prestataire qui propose un outil sans avoir entendu les réponses aux 8 questions : refuser d'engager, demander un cadrage commun
- Devant une équipe interne qui veut « commencer à tester » sans cadrage : refuser le lancement, demander d'abord le document de cadrage
- Devant soi-même quand on s'enthousiasme pour une démo : refuser de signer, prendre 48 h pour passer les 8 questions

**Garde-fou** : cette discipline doit rester **proportionnée**. Pour un POC à 500 € sur 2 semaines, le cadrage peut tenir en 30 minutes. Pour un projet à 50 000 € sur 6 mois, il vaut probablement 1-2 jours de travail. La proportion = ~1 % du coût total projet en effort de cadrage.

### Section 4 — 5 anti-patterns courants

**Anti-pattern 1 — Le tech push** (cf. § 1)

**Anti-pattern 2 — La boîte noire « on verra à l'usage »**
Le projet est lancé sans critère de succès clair. L'argument : « on verra ce que ça donne en production ». Résultat : 6 mois plus tard, personne ne sait dire si le projet a réussi ou échoué, et le budget continue à couler.
**Correctif** : la question 5 (mesure du succès) doit recevoir une réponse **avant** le lancement.

**Anti-pattern 3 — Le périmètre extensible**
Le projet démarre sur un cas d'usage précis (ex : « automatiser le tri des factures fournisseurs »), puis s'étend de proche en proche (« et tant qu'à faire, ajoutons les avoirs, les notes de frais, la TVA, etc. »). Au bout de 3 mois, le périmètre ne ressemble plus du tout au cadrage initial et le projet n'aboutit jamais.
**Correctif** : poser explicitement « ce qui est hors périmètre v1 » dans le document de cadrage.

**Anti-pattern 4 — La mesure de succès floue**
Le KPI annoncé est « gagner du temps », « améliorer la qualité », « être plus moderne ». Aucun de ces critères n'est mesurable.
**Correctif** : la mesure de succès doit être chiffrable et vérifiable (« réduire le temps moyen de traitement d'une facture de 8 minutes à <3 minutes », « atteindre 95 % de précision sur l'extraction du numéro de TVA »).

**Anti-pattern 5 — L'absence de plan d'arrêt**
Le projet est engagé sans définir à quel moment on l'arrête s'il échoue. Résultat : il continue par inertie même quand les signaux sont mauvais, parce que personne n'est mandaté pour le stopper.
**Correctif** : la question 8 (plan d'arrêt) doit recevoir une réponse opérationnelle : qui décide, sur quels critères, avec quel coût d'arrêt anticipé.

### Section 5 — Le livrable de cadrage minimal

Le livrable de cadrage tient sur **1 page**. Sa structure :

```
PROJET : [titre court du projet en 5-8 mots]
DATE DE CADRAGE : [date]
PORTEUR : [nom + rôle]

1. PROBLÈME MÉTIER (1-2 phrases) : ...
2. UTILISATEUR FINAL : ...
3. DONNÉES DISPONIBLES : ...
4. CONTRAINTES RÉGLEMENTAIRES : ...
5. MESURE DE SUCCÈS : [KPI chiffrable] = [valeur cible] mesuré [fréquence]
6. BUDGET : [initial] + [récurrent annuel]
7. CALENDRIER : POC [date début] → déploiement [date cible]
8. PLAN D'ARRÊT : [critères] / décideur [nom] / coût d'arrêt anticipé [montant]

HORS PÉRIMÈTRE V1 (explicite) : ...
DEMANDE DE VALIDATION : signature / date
```

Ce document est **partageable** (peut être envoyé à un prestataire ou à un comité interne), **datable** (sert de référence dans le temps), **contestable** (chaque ligne peut être discutée avant validation).

Sans ce document, **aucune décision d'engagement** ne devrait être prise.

### Section 6 — Articulation avec les autres préalables

**Avant PR-09** : si la maturité organisationnelle (PR-01) n'est pas validée — l'entreprise n'a pas la capacité de mener un projet IA — alors PR-09 est prématuré. Lire PR-01 d'abord.

**En complément de PR-09** : PR-02 (marché IA) donne le contexte macro nécessaire pour calibrer le projet (où en est l'écosystème ? quels acteurs ? quels coûts moyens observés ?). PR-04 (marché IA et emploi) éclaire l'impact organisationnel à anticiper.

**Après PR-09** : une fois le cadrage validé, PR-07 (build vs buy) aide à arbitrer le « comment » (interne / externe / SaaS). PR-08 (financer son projet IA) cartographie les dispositifs financiers mobilisables. **PR-10 (vérifier et limiter les hallucinations IA)** prépare la phase d'exécution.

**Cycle de vie complet** : pour une vue séquentielle bout en bout, voir **PR-11 (cycle de vie d'un projet IA)** qui intègre PR-09 + PR-10 dans une séquence opérationnelle.

**Articulation avec DEP-01 « Cadrer un projet IA »** côté Déploiement : DEP-01 traite l'angle **technique** du cadrage (choix d'architecture, heuristique anti-hype, arbre single LLM → multi-agent) une fois que le projet est validé. PR-09 traite l'angle **stratégique amont** du cadrage (décision d'engager le projet, alignement métier, allocation de ressources). Les 2 sont complémentaires et séquentiels : PR-09 d'abord, DEP-01 ensuite.

### Section 7 — Plan d'action 30 jours

**Jours 1-7 — Identifier le projet candidat**
- Lister les irritants métier qui pourraient bénéficier d'une démarche IA
- Choisir 1 problème prioritaire (pas 3, pas 5)
- Vérifier que ce problème vaut la peine d'être résolu (impact business, fréquence, coût actuel)

**Jours 8-14 — Répondre aux 8 questions de cadrage**
- Bloquer 2-3 heures dans l'agenda pour le cadrage
- Inviter les personnes pertinentes (utilisateur final, responsable données, contrôleur de gestion si budget)
- Documenter les réponses dans le format 1 page

**Jours 15-21 — Faire valider le cadrage**
- Présenter le document à la direction ou au comité ad hoc
- Recueillir les retours, les intégrer
- Obtenir une validation explicite (signature ou équivalent)

**Jours 22-30 — Préparer la suite**
- Selon le résultat du cadrage, orienter vers PR-07 (build vs buy) ou DEP-01 (cadrage technique)
- Si le cadrage révèle que le projet n'est pas mûr, archiver et passer au projet suivant
- Si le cadrage révèle un besoin de financement, mobiliser PR-08

---

## Ressources à intégrer

### Articles de fond
- **McKinsey State of AI 2025** — « 80 % des échecs interviennent avant la première ligne de code » (référence cohérente avec heuristique DEP-01 v3.10 intégrée). Source canonique déjà dans Hub.
- **Cloud Security Alliance** — recommandations cadrage projet IA (déjà citée dans CU-027 + DEP-08)
- **Bpifrance Le Lab** — études PME et adoption IA (déjà citées dans PR-04 + PR-08)

### Tutoriels & cas pratiques
- **Template de document de cadrage 1 page** (à fournir en téléchargement depuis la page, format `.docx` neutre)
- **Auto-diagnostic** : 8 questions sous forme de checklist interactive (extension possible Phase 3 plateforme dynamique, en attendant version statique)

### Documentation officielle & études
- **CNIL** — recommandations sur le cadrage d'un projet IA et la documentation préalable
- **AI Act EU** — articles relatifs à la documentation préalable des systèmes IA (Article 9 risk management, Article 13 transparence)

### Contacts opérationnels
- **Bpifrance** — diagnostic Data IA (étape 1 souvent recommandée — cohérence avec PR-08)
- **Région Grand Est** — dispositifs d'accompagnement amont
- **Réseau QFC / QFB / QA** — accompagnement structurant des projets IA des PME/ETI

---

## Mise à jour RULES / glossaire chiffres-clés

Le **glossaire des chiffres-clés** RULES § 1.2.3 doit être actualisé :
- Nombre de préalables PR : **8 → 9** (PR-09 ajouté). À cumuler avec PR-10 et PR-11 du Lot B et Lot C → **8 → 11** total v3.12.

Entrée historique à ajouter dans la section versions RULES :
```markdown
- **v1.6.3** — itération v3.12 (3 nouveaux préalables PR-09 + PR-10 + PR-11) :
  - Glossaire § 1.2.3 : 8 → 11 préalables PR
  - Nouveaux préalables : PR-09 « Cadrer un projet IA avant de choisir un outil », PR-10 « Vérifier et limiter les hallucinations IA », PR-11 « Cycle de vie d'un projet IA »
  - Aucune nouvelle règle structurelle. RULES reste à 1.6.X.
```

## Mise à jour navigation et page préalables

- Ajouter une **card PR-09** dans `prealables.html` (suivre le template des cards existantes PR-01 à PR-08)
- Position dans la liste : à la suite de PR-08 (ordre numérique)
- Icône suggérée : 🧭
- Catégorie : « Cadrage stratégique »
- Cross-link depuis PR-01, PR-02, PR-07, PR-08 vers PR-09 (renvois croisés à intégrer dans ces préalables existants)

## Métadonnées module

- `<meta name="description">` : *« Cadrer un projet IA avant de choisir un outil : les 8 questions à se poser pour éviter le piège du tech push. Pourquoi 80 % du soin doit aller sur le cadrage initial, et comment refuser d'avancer sans clarification. »*
- Badge temps de lecture : **15 min**

## Item parallèle (à compiler dans brief v3.12)

Pas de canonisation chiffre macro nouveau pour PR-09 — les chiffres mobilisés (80 % d'échecs avant code, McKinsey, Bpifrance) sont déjà canonisés via I-D-003/I-D-005/I-D-006/I-D-007.
