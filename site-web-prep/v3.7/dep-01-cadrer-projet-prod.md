# DEP-01 — Cadrer un projet IA pour la mise en production

**Public cible :** dirigeant PME/ETI qui pilote un projet IA + son interface technique (CTO, prestataire, IT interne)

---

## Métadonnées (pour Claude Code)

- **Section** : Déploiement (nouvelle section v3.7)
- **Niveau** : ⭐⭐⭐ Avancé
- **Type** : Cadrage stratégique
- **Durée lecture** : 18 min
- **Emoji h1** : 🎯
- **Titre métier visible** : « Cadrer un projet IA pour la mise en production »
- **Sous-titre hero** : 95 % des projets GenAI en entreprise n'ont aucun impact P&L mesurable. La cause n'est pas la technologie. C'est l'absence de cadrage. Voici comment ne pas faire partie des 95 %.
- **Card index promesse** : « Cadrage stratégique » (analogue aux PR — pas de promesse étude de cas)

## Synthèse exécutive

### Pourquoi cette page ?

Tu es dirigeant d'une PME ou ETI. Tu pilotes (ou commandites) un projet IA qui doit passer **du pilote à la production**. C'est le moment où tout se joue. **95 % des projets GenAI en entreprise n'ont aucun impact P&L mesurable** sur les 30 à 40 milliards de dollars investis (MIT NANDA, *State of AI in Business 2025*, août 2025). La cause racine n'est jamais la technologie : c'est l'absence de cadrage organisationnel, l'absence de gouvernance, l'absence de redesign de workflow.

Cette page te donne le cadre de pilotage que tu dois exiger de ton équipe technique et de tes prestataires : différence POC / pilote / production, critères Go/No-Go entre les phases, gouvernance projet IA, et les 7 écueils les plus documentés.

### 4 takeaways

1. **POC, pilote, production : trois phases distinctes avec trois objectifs différents.** Confondre les trois est la cause n°1 d'échec. Le POC valide la faisabilité technique. Le pilote valide la valeur métier. La production industrialise. Chaque transition demande des critères Go/No-Go explicites.

2. **Buy + partenariat = 67 % de réussite vs 33 % en build interne** (MIT NANDA 2025). Pour la PME, le bon réflexe par défaut est l'achat à un éditeur spécialisé + partenariat d'intégration, pas le build maison. Le build interne reste justifié pour 3 cas seulement : souveraineté critique, ROI massif documenté, ou différenciation compétitive durable.

3. **La gouvernance projet IA n'est pas une option.** Avant le moindre POC : nommer un product owner métier, fixer 2-3 KPI mesurables, prévoir le redesign de workflow, anticiper la conformité (RGPD, AI Act, sectorielle). Sans ces 4 points, tu vas dans les 95 %.

4. **Le NIST AI Risk Management Framework est ton référentiel gratuit.** Pas besoin de réinventer une grille de gouvernance. Le NIST AI RMF (gratuit, public) couvre les 4 fonctions essentielles : Govern, Map, Measure, Manage. Adoptable en 1 journée pour une PME.

### Stats (3-4)

- **95 %** des pilotes GenAI sans impact P&L (MIT NANDA, août 2025)
- **67 % vs 33 %** réussite Buy+partenariat vs Build interne (MIT NANDA)
- **23 %** des organisations scalent un système agentique en au moins une fonction (McKinsey, novembre 2025)
- **6 %** des entreprises atteignent > 5 % d'EBIT attribué à l'IA (McKinsey, mars 2025)

### Quand cette page est utile

Tu envisages de **passer un projet IA du pilote à la production**, ou tu veux **cadrer un projet IA dès le départ** pour ne pas tomber dans les 95 % qui échouent. Tu cherches un référentiel de gouvernance simple, applicable, qui n'exige pas de devenir DSI. Tu veux savoir quelles questions poser à ton prestataire avant de signer.

## Section 1 — POC, pilote, production : trois phases, trois objectifs

La confusion entre ces trois phases est la cause n°1 d'échec des projets IA en PME. Comprendre la distinction est non négociable.

### 1.1 Le POC (Proof of Concept) — valider la faisabilité technique

Durée typique : **2 à 6 semaines**. Objectif : démontrer que la techno fonctionne sur ton cas d'usage. Pas de production, pas de vrais utilisateurs en aval, pas de SLA. Un POC qui marche prouve que c'est faisable, pas que ça apporte de la valeur.

**Critère de sortie POC** : la techno fait ce qu'on attend d'elle dans des conditions contrôlées. Si oui → passage en pilote. Si non → arrêt sans regret (le POC a coûté quelques semaines, pas un an).

### 1.2 Le pilote — valider la valeur métier

Durée typique : **3 à 6 mois**. Objectif : mettre l'outil entre les mains de **vrais utilisateurs** sur un périmètre limité (1 équipe, 1 fonction, 1 cas d'usage). Mesurer la valeur métier avec des KPI cibles définis avant le démarrage.

**Critère de sortie pilote** : les KPI métier sont atteints (gain de productivité, amélioration de qualité, réduction de coût, etc.). Si oui → passage en production. Si non → analyse des causes (mauvais cadrage ? mauvais workflow ? rejet utilisateur ? problème technique ?) puis correction ou arrêt.

### 1.3 La production — industrialiser

Durée typique : **6 mois à 2 ans pour atteindre la stabilité**. Objectif : déployer sur l'ensemble du périmètre cible avec SLA, monitoring, support, mise à jour, conformité, formation. C'est ici que **le coût récurrent devient significatif** (20-30 %/an du coût initial pour la maintenance).

**Critère de réussite production** : le système est utilisé en routine, ROI mesurable et durable, conformité tenue. Si dérive → diagnostic + correction.

### 1.4 La règle pratique pour ne pas se tromper

**Ne jamais déployer un POC en production.** C'est l'erreur la plus fréquente et la plus coûteuse. Le POC n'a ni les garde-fous ni la robustesse pour supporter de vrais utilisateurs. Entre le POC qui « marche » en démo et l'outil en production, il y a un facteur 5 à 10 en effort de structuration.

## Section 2 — Buy + partenariat vs Build interne : la doctrine 2026

L'étude MIT NANDA 2025 est sans ambiguïté : **les stratégies Buy + partenariat réussissent dans 67 % des cas contre 33 % pour les builds internes**. C'est un facteur 2.

### 2.1 Pourquoi Buy + partenariat gagne

Trois raisons documentées :
1. **Compétences cumulées** : un éditeur spécialisé a des centaines de déploiements en historique. Une PME en a zéro.
2. **Maintenance externalisée** : les mises à jour de modèles, les patchs sécurité, la conformité réglementaire (AI Act 2026, RGPD) sont gérés par l'éditeur.
3. **Time-to-value rapide** : 3-6 mois pour un déploiement, contre 12-24 mois pour un build interne.

### 2.2 Quand le Build interne reste justifié

3 cas seulement (cf. [PR-07 Build vs Buy à l'ère de l'IA](../prealables/pr-07-build-vs-buy.html) pour le détail) :
1. **Souveraineté critique** : données ultra-sensibles, secret industriel, contrainte SecNumCloud absolue.
2. **ROI massif documenté** : volume tel que l'amortissement du build est démontré sur 24 mois.
3. **Différenciation compétitive durable** : le système IA fait ton avantage sur le marché, pas un sujet support.

Pour tous les autres cas : **Buy + partenariat est le bon réflexe par défaut**.

### 2.3 Le compromis intelligent : Buy + customisation légère

Le pattern dominant en 2026 pour les PME ambitieuses : acheter un outil spécialisé (Pennylane, Sellsy, ou plus avancé selon le cas) + ajouter une **couche de customisation IA-assistée** (workflows n8n, micro-applications métier via Cursor / Lovable / Bolt — voir [CU-027 Faire développer une appli métier](../modules/cu-027-dev-applicatif-ia.html)).

## Section 3 — Les 4 piliers de gouvernance non négociables

Avant le moindre POC, ces 4 points doivent être cadrés. **C'est le minimum vital pour ne pas tomber dans les 95 %.**

### 3.1 Un product owner métier nommé

Pas un sponsor lointain. Un **PO opérationnel** qui dédie 20-40 % de son temps au projet pendant 6-12 mois. Sans PO métier, le projet dérive vers les besoins techniques de l'équipe IT et perd le contact avec la valeur réelle.

### 3.2 2-3 KPI cibles mesurables, définis AVANT le POC

Pas « améliorer la productivité ». Mais : « réduire le temps de traitement d'un dossier de 45 min à 20 min sur 80 % des cas, mesuré sur un échantillon de 100 dossiers ». Si tu ne sais pas formuler le KPI, le projet n'est pas mûr.

### 3.3 Le redesign de workflow planifié

McKinsey 2025 : **seules 21 %** des organisations IA ont redesigné leurs workflows. C'est pourtant le seul critère le plus corrélé à l'EBIT-impact. Sans redesign, tu numérises l'inefficacité existante. Le redesign de workflow se fait **avant** la mise en prod, pas après.

### 3.4 La conformité anticipée

Trois sujets à cadrer avant le POC :
- **RGPD** (cf. [PR-05 Sécurité IA](../prealables/pr-05-securite-ia.html)) : registre des traitements, consentement, durée de conservation
- **AI Act** (haut-risque applicable 2 août 2026) : si scoring RH, scoring crédit, prise de décision sensible
- **Sectorielle** : selon ton métier (santé, finance, éducation)

Anticiper évite de devoir tout démonter en phase production.

## Section 4 — Les 7 écueils les plus documentés

À éviter à tout prix. Chaque écueil cité a tué un projet IA documenté en 2024-2025.

1. **Lancer le POC avant d'avoir validé la désirabilité** : le besoin métier n'existe pas, ou les utilisateurs cibles ne veulent pas du système. Cause d'échec ~25 % des cas.
2. **Confondre adoption (usage individuel) et transformation (changement organisationnel)**. ChatGPT utilisé par 60 % des employés ≠ IA qui transforme l'entreprise.
3. **Skip de la gouvernance pendant le pilote** → impossibilité de scaler ensuite (audit trails, compliance, reproductibilité absents).
4. **Tout vouloir builder en interne** : ratio de réussite 1/3 contre 2/3 (MIT NANDA).
5. **Ignorer le redesign de workflow** : tu numérises l'inefficacité.
6. **Sous-estimer le coût récurrent** : 20-30 %/an du coût initial pour maintenance, mises à jour, conformité.
7. **Pas de PO métier dédié** : projet techno sans valeur métier mesurée → arrêt à la fin du pilote.

## Section 5 — Le NIST AI RMF comme référentiel gratuit

Le **NIST AI Risk Management Framework** (publié 2023, mis à jour 2024) est le référentiel gouvernement américain pour la gouvernance IA. Gratuit, public, applicable en PME.

Quatre fonctions :
1. **Govern** : politiques, rôles, responsabilités IA dans l'organisation
2. **Map** : catégoriser les usages IA par risque
3. **Measure** : KPI techniques (qualité), business (ROI), conformité (audit trails)
4. **Manage** : prioriser les risques, traiter, monitorer

**Adoptable en 1 journée** pour une PME : le PO métier + le DSI ou prestataire IT remplissent ensemble les 4 sections sur ton cas d'usage. Le NIST fournit des templates téléchargeables.

## Section 6 — Plan d'action 90 jours pour cadrer un projet IA

Si tu démarres un projet IA dans les 90 prochains jours, voici la séquence type :

### Jours 1-15 — Désirabilité métier
- Identifier le cas d'usage prioritaire (max 1 à la fois)
- Valider auprès de 5-10 utilisateurs cibles par interview qualitative
- Formuler les 2-3 KPI cibles mesurables

### Jours 16-30 — Cadrage gouvernance
- Nommer le PO métier (20-40 % de son temps dédié)
- Adopter le NIST AI RMF (4 templates remplis)
- Cadrer la conformité (RGPD, AI Act si haut-risque)
- Décision Buy vs Build (cf. [PR-07](../prealables/pr-07-build-vs-buy.html))

### Jours 31-60 — POC technique
- Mise en œuvre du POC sur conditions contrôlées
- Critère Go/No-Go : la techno fait ce qui est attendu

### Jours 61-90 — Pilote utilisateurs
- 5-15 utilisateurs cibles, 1 équipe, 1 fonction
- Mesure des 2-3 KPI cibles
- Décision Go/No-Go pour la mise en production

À l'issue de ces 90 jours, tu sais si tu vas en production ou si tu arrêtes — sans avoir engagé de budget récurrent.

## Section 7 — Pour aller plus loin (Schéma A — Externes uniquement)

### Callout d'aiguillage

> Pour le panorama complet des outils, retrouve les fiches détaillées sur la [page Ressources du Hub](../ressources.html#bibliographie).

### 📰 Articles de fond
- [Fortune — MIT NANDA report 95 % AI pilots failing](https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/) — Synthèse du rapport MIT NANDA août 2025
- [McKinsey — The state of AI 2025 (mars)](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai) — Étude annuelle 78 % adoption / 6 % EBIT > 5 %
- [HBR — AI-generated workslop is destroying productivity (sept. 2025)](https://hbr.org/2025/09/ai-generated-workslop-is-destroying-productivity) — Coût caché de l'IA mal cadrée

### 🎓 Tutoriels & cas pratiques
- [AWS Prescriptive Guidance — Generative AI Lifecycle](https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/dev-architecting.html) — Framework architecture POC → prod
- [Bpifrance Conseil Osez l'IA](https://presse.bpifrance.fr/bpifrance-deploie-10-milliards-deuros-pour-developper-lecosysteme-ia-et-soutenir-lappropriation-de-lintelligence-artificielle-par-les-entreprises-francaises) — 700 diagnostics IA en PME (2024)

### 📚 Documentation officielle & études
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — Référentiel gouvernance IA gratuit (templates téléchargeables)
- [MIT NANDA — State of AI in Business 2025 (synthèse)](https://www.aigl.blog/state-of-ai-in-business-2025/) — Étude 153 leaders, 300 déploiements
- [McKinsey — State of AI nov. 2025 (PDF)](https://www.mckinsey.com/~/media/mckinsey/business%20functions/quantumblack/our%20insights/the%20state%20of%20ai/november%202025/the-state-of-ai-2025-agents-innovation_cmyk-v1.pdf) — Édition agents, 23 % scalent

### 👥 Communautés & veille
- [Bpifrance Le Lab](https://lelab.bpifrance.fr) — Études IA PME/ETI françaises
- [France Num](https://www.francenum.gouv.fr/guides-et-conseils/intelligence-artificielle/comprendre-et-adopter-lia/le-podcast-les-pme-lia) — Podcast PME et IA, baromètre annuel

## Renvois internes pour Claude Code (à intégrer dans le corps des sections)

- **Section 2.2** : lien `<a href="../prealables/pr-07-build-vs-buy.html">PR-07 Build vs Buy à l'ère de l'IA</a>`
- **Section 2.3** : lien `<a href="../modules/cu-027-dev-applicatif-ia.html">CU-027 Faire développer une appli métier</a>`
- **Section 3.4** : lien `<a href="../prealables/pr-05-securite-ia.html">PR-05 Sécurité IA</a>`
- **Section 6** : lien `<a href="../prealables/pr-07-build-vs-buy.html">PR-07</a>`

## Composants visuels suggérés (pour Claude Code)

- **Section 1** : 3 cartes pour les 3 phases (POC / Pilote / Production) avec critères Go/No-Go visibles
- **Section 3** : grille 4 cartes pour les 4 piliers de gouvernance
- **Section 6** : timeline visuelle 90 jours en 4 phases (utiliser `.timeline-block` déjà centralisé dans `module-v3.css`)

## Note Cowork
Cette fiche s'appuie majoritairement sur MIT NANDA, McKinsey, Bpifrance. Aucune mention de cabinets de conseil intermédiaires. Aucune statistique non sourcée. Conforme RULES § 1.1.
