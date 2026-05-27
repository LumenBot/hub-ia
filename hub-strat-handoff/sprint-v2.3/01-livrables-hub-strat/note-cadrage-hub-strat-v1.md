# Note de cadrage — Cowork Hub Strat

**Version** : v1 — 25 mai 2026
**Statut** : note d'engagement opérationnel, première production du canal Hub Strat post-ouverture
**Garant** : Blaise Cavalli (porteur Hub v2 + SUM Quai Alpha)
**Émetteur** : Cowork Hub Strat
**Destinataires** : Cavalli (validation), pour notification ultérieure aux canaux Hub Content / Hub RAG / Claude Design / DEV IA Head via Cavalli
**Périmètre** : cadrage du mandat, de la posture, de la méthodologie et du calendrier du canal — applicable aux sprints S3.1 et suivants, révisable en fonction des apprentissages

---

## 1. Objet, mandat et déclencheur (pattern P15)

Cowork Hub Strat est le canal **stratégie produit et go-to-market** du projet **Hub v2** — side project entrepreneurial personnel de Blaise Cavalli, distinct du rôle salarié à Quai Alpha / Quest for Change. Le canal a été ouvert le 25 mai 2026 en réponse au **pattern P15 — trou produit-commercial** formalisé par le canal head Initiative IA en méta-gouvernance des canaux Hub.

Diagnostic P15 (synthèse) : la convention multi-acteurs Cowork v1 instrumente solidement la production technique (matière éditoriale, HTML, UX, RAG), mais sous-instrumente la couche **produit-marché-go-to-market** — analyse concurrentielle structurée, segmentation validée, modèle économique chiffré, garde-fous juridiques, plan d'acquisition. Sans cette couche, Hub v2 reste un POC technique séduisant et ne devient pas un produit commercialisable.

Hub Strat ferme ce trou. Son **mandat** couvre sept axes de travail : analyse concurrentielle (Bpifrance Hub IA, French AI Lab, EDIH régionaux, Diagnostic IA Numeum, plateformes privées) ; segmentation et qualification persona Camille (+ secondaires éventuels) ; modèle économique chiffré 24 mois (CAC, LTV, churn, scenarios) ; stratégie d'acquisition (territorial / SEO / partenariats QFC-CCI-POLARIS-French Tech Est-Bpifrance / événementiel / communauté) ; garde-fous juridiques (RGPD, AI Act, CGV/CGU, IP, statut side project) ; plan d'acquisition 10 premiers utilisateurs ; veille marché et signaux faibles.

Le canal ne fait **pas** : production de matière éditoriale RAG (Hub Content), production UX/design (Claude Design), production HTML/code (Claude Code Content / RAG / Console), méta-gouvernance inter-canaux (DEV IA Head), décision finale stratégique (Cavalli arbitre), contact direct avec startups réelles accompagnées à Quai Alpha (étanchéité QFC stricte), production de matière confidentielle QFC.

---

## 2. Architecture multi-canaux 10 acteurs — positionnement Hub Strat

La cartographie d'orchestration v1.0 (25 mai 2026, soir) actualise l'architecture Cowork du projet : on est passé d'un modèle 4 acteurs (Cowork Hub IA + Claude Code + Claude Design + Cavalli) à **10 acteurs** simultanément actifs sur les projets Cavalli. Hub Strat (A1) s'insère dans cet écosystème :

| # | Acteur | Cluster | Périmètre |
|---|--------|---------|-----------|
| A1 | **Hub Strat** | Hub v2 | Stratégie produit / GTM / juridique / acquisition (ce canal) |
| A2 | Hub Content | Hub v2 | Contenu site, modules formation, ressources (ex-Hub IA, renommé) |
| A3 | Hub RAG | Hub v2 | Pilotage technique RAG, structuration MD, golden set, eval |
| A4 | Claude Code Content | Hub v2 | Production HTML site / Hub Learning Center |
| A5 | Claude Code RAG | Hub v2 | Préparation environnement logiciel RAG (skills, scripts) |
| A6 | Claude Code Console | Hub v2 | Implémentation RAG local (ChromaDB, exécutions coûteuses) |
| A7 | Claude Design | Hub v2 | UX, signature visuelle, parcours, prototypes interactifs |
| A8 | DEV IA Head | Initiative IA | Méta-gouvernance, patterns transverses |
| A9 | DEV IA Archi-Sys | Initiative IA | Architecture système agents, investigation tech |
| A10 | Blaise Cavalli | Humain | Décideur, garant des interfaces inter-canaux |

**Flux Hub Strat** (extraits matrice cartographie v1.0) : **actifs et fréquents** avec Hub Content (A2), Claude Design (A7), Cavalli (A10) ; **ponctuels** avec Hub RAG (A3), DEV IA Head (A8) ; **pas de flux direct** avec les trois Claude Code (A4-A6) ni DEV IA Archi-Sys (A9) — transmission via Cavalli systématique.

**Risque méta-gouvernance #1** identifié par le canal head : Cavalli est interface active avec les 9 autres acteurs, 9 interfaces inter-canaux portées manuellement, 27 % du trafic de coordination passant par lui. Indisponibilité 1-2 semaines → projet bloqué.

**Contrainte de design auto-imposée par Hub Strat** : chaque livrable structurant sera **packagé pour transmission autonome** — bloc résumé exécutif transmissible en un copier-coller vers les canaux pairs, sans que Cavalli ait à reformuler. Cette pratique réduit la charge orchestrateur sans dévier du périmètre Hub Strat. Elle est compatible avec la règle « pas de transmission directe canal à canal » (Cavalli reste le relai décisionnaire, mais le coût marginal de relai tend vers zéro).

---

## 3. Posture et règles de travail

**Règle des 5 doigts (SUM virtuel)** — Hub Strat n'est ni stagiaire, ni alternant, ni employé, ni associé, ni cofondateur de Cavalli. Hub Strat **propose**, Cavalli **décide**. Le canal aide à structurer, traque les biais, formule les questions qui dérangent — mais ne produit pas de livrables clé en main qui se substituent à l'arbitrage du porteur.

**Étanchéité QFC stricte** — aucune matière confidentielle des startups réelles accompagnées à Quai Alpha ne transite par ce canal. La méthodologie publique (Vianeo, 6 critères QFC, patterns anonymisés) est mobilisable. Les CR de comités, évaluations de projets, contenus internes QFC ne sortent pas. Hub Strat est le canal le plus exposé au risque d'érosion d'étanchéité (matière marché, commercialisation, partenariats régionaux potentiels) : règle renforcée à chaque livrable via le check pré-livrable §8.

**Posture critique constructive** — Hub Strat critique sans complaisance les hypothèses Hub v2, y compris celles de Cavalli. La bienveillance s'exprime dans la qualité de l'argument, pas dans l'évitement du désaccord.

**Alignement avec les règles d'utilisation de l'IA enseignées en StarterClass J3** (cohérence externe avec la méthodologie Quai Alpha) :

1. **Anonymisation** des informations transmises (pas de nom d'organisation ni de personne identifiable hors public).
2. **L'IA aide, elle ne décide pas** — elle structure la réflexion, elle ne valide pas les hypothèses.
3. **Esprit critique en permanence** — les productions peuvent contenir des biais, simplifications, erreurs.
4. **Ne pas s'approprier les résultats** — les productions Hub Strat sont des matériaux analysés et adaptés par Cavalli, pas des conclusions du canal.
5. **La compréhension humaine reste prioritaire** — si Cavalli ne comprend pas ou n'est pas d'accord, il n'utilise pas.

Ces cinq règles convergent avec la règle des 5 doigts et la posture SUM virtuel — elles ne créent pas de contrainte nouvelle, elles formalisent ce que le canal s'engage déjà à respecter.

**Arbitrage IP / statut side project — préalable Étape 4** — avant Étape 4 de la roadmap produit (bascule monétisation Pro tier), Hub Strat produit un dossier d'arbitrage destiné à la direction QFC sur le statut du projet (side project 100 % personnel / convention QFC à formaliser / bascule projet interne QFC). Aucune communication externe engageante (pricing public, ouverture beta, partenariat) ne se fait avant cet arbitrage. Anticipation actée : production du dossier en module 4 (fin juillet 2026) plutôt qu'au seuil de l'Étape 4 calendaire (8-12 mois), afin que Hub Strat ne travaille pas 5-6 mois sans visibilité sur ce qui est diffusable publiquement.

---

## 4. Cadre méthodologique : Vianeo en grille parallèle itérée

### 4.1 Résolution d'une tension structurelle

Le `_instructions.md` du canal (règle 3) prescrit une **séquence Vianeo stricte** : Légitimité → Désirabilité → Acceptabilité → Faisabilité/Viabilité, sans saut de module, pas de modèle économique chiffré tant que la désirabilité n'est pas validée. L'arbitrage Cavalli du 25 mai pose un **mode lean startup itératif** avec progression parallèle sur les quatre dimensions, itérée au fur et à mesure.

Il y a une **tension assumée** entre les deux énoncés. Hub Strat la résout ainsi :

**Vianeo n'est plus mobilisée comme une séquence stricte mais comme une grille de lecture à 4 dimensions itérée en parallèle.** Les quatre modules sont travaillés simultanément, à granularité différente selon la maturité du sujet. La cohérence n'est plus assurée par l'ordre, mais par des **règles de cohérence inter-modules** qui jouent le rôle de garde-fous.

### 4.2 Règles de cohérence inter-modules (garde-fous)

1. **Pas d'engagement public sur pricing** tant que l'acceptabilité documentaire (module 3) n'est pas tenue sur le pricing v1 hybride 3 leviers — i.e. tant qu'on n'a pas confronté Free / Pro 29€ / Équipe 19€/siège / crédits flexibles au benchmark et aux signaux d'usage en ligne.
2. **Pas de plan financier détaillé public** (deck investisseur, ARR projeté communiqué) tant que l'arbitrage IP (module 4 anticipé) n'est pas instruit.
3. **Pas de plan d'acquisition externe** (campagnes, partenariats engageants) tant que la légitimité Cavalli (module 1) n'est pas clarifiée vis-à-vis de son rôle QFC — i.e. statut side project assumé ou convention QFC formalisée.
4. **Pas de modélisation économique chiffrée engageante** (scenarios 24 mois figés) tant que la désirabilité documentaire (module 2) n'a pas produit des hypothèses convergentes sur le persona principal.

Ces règles permettent l'itération parallèle sans saut hasardeux. Elles posent des **seuils de cohérence**, pas des barrières temporelles.

### 4.3 Ancrage frameworks StarterClass par module

Hub Strat mobilise la matière pédagogique StarterClass v26 Quai Alpha (J3 à J10) comme **boîte à outils méthodologique**, sans reproduire les contenus pédagogiques sous licence Vianeo. Correspondance frameworks-modules :

| Module Vianeo | Frameworks StarterClass mobilisés | Source |
|---|---|---|
| **1 — Légitimité** | Cercle d'or Sinek (Why-How-What) ; Mission/Vision/Valeurs ; canevas proposition de valeur « Pour [client] qui [problème] nous proposons [produit] qui [valeur] grâce à [innovation] » | J3 |
| **2 — Désirabilité** | Matrice d'Opportunité (5 critères) ; Pain DUR (Douloureux-Urgent-Reconnu) vs Vitamine ; Persona ; Value Proposition Map ; Customer Journey ; méthode « Et alors ? » (caractéristique → bénéfice fonctionnel → bénéfice financier → valeur intrinsèque) ; méthode promesse → preuve | J4, J5 |
| **3 — Acceptabilité** | MVP comme offre minimale ; matrice atout/attrait ; PMF Paul Graham (usage obsessionnel qui remplace, rétention structurelle ≠ déclaratif) ; stratégie Go-To-Market Porter (choisir ce qu'il ne faut pas faire) | J8 |
| **4 — Faisabilité/Viabilité** | Modèle économique 5 variantes (Simultanéité, Durabilité, Revenus, Traction, Interdépendance) ; mécanique de revenus ; hypothèse d'activité = CA en équation ; axe Volume (Cible A) vs Vélocité (Cible B) justifié par l'Atout ; tunnel de vente V1 ; Roadmap squelette first / jalons / KPI / crantage | J7, J9, J10 |

### 4.4 Pièges traités explicitement

- **Effectuation** — ne pas confondre « je porte Hub v2 parce que je peux » (ressources existantes : Cavalli a la stack, le réseau, la matière éditoriale, les canaux Cowork) avec « Hub v2 répond à un problème suffisamment douloureux pour justifier le projet ». Le canal questionne régulièrement ce point.
- **Solutionnisme** — la solution Hub v2 (plateforme conversationnelle + RAG dirigeants PME/ETI) cherche son problème, pas l'inverse. Risque accentué par le fait que la matière éditoriale et le POC technique sont déjà avancés. Le canal traque les rationalisations a posteriori.
- **Lean data** — l'arbitrage Cavalli « pas d'interviews, approche documentaire » écarte le risque de noyer le porteur dans la data quantitative, mais introduit le **risque inverse** : biais de confirmation sur des hypothèses non confrontées au terrain. Garde-fou explicite en §5.

### 4.5 Proposition de mise en cohérence du `_instructions.md`

Recommandation : **réécrire la règle 3 du `_instructions.md` en v1.1** pour refléter la grille parallèle itérée, sinon contradiction interne durable entre les deux documents fondateurs du canal. Hub Strat propose un avenant prêt à intégrer, à valider par Cavalli avant prochaine session de sprint.

---

## 5. Désirabilité documentaire — écart méthodologique assumé vs StarterClass canonique

### 5.1 Nature de l'écart

La StarterClass v26 place l'**enquête terrain** au cœur des modules 2 (Désirabilité) et au-delà : J4 prépare l'enquête, J5 outille la conduite d'entretiens, J6 fournit les guides d'entretien anonymisés, J7-J8-J9 réinjectent les apprentissages terrain. L'arbitrage Cavalli du 25 mai écarte les interviews pour Hub Strat. Il s'agit d'un **écart méthodologique structurel**, à assumer explicitement plutôt qu'à camoufler.

### 5.2 Substitution opérationnelle

Hub Strat opère en **mode désirabilité documentaire** — la grille Vianeo module 2 est nourrie par cinq familles de sources, et non par des entretiens semi-directifs :

1. **Benchmark concurrentiel approfondi** — 8 à 12 acteurs cartographiés (Bpifrance Hub IA, French AI Lab, Diagnostic IA Numeum, EDIH régionaux, cabinets conseil IA pour dirigeants, plateformes privées émergentes type Tom AI, Hyko, etc.).
2. **Analyse usages en ligne** — reviews G2 / Capterra / Trustpilot des plateformes concurrentes ; témoignages publics utilisateurs Bpifrance Hub IA et French AI Lab ; études de cas publiées par Numeum et autres organisations.
3. **Forums dirigeants et LinkedIn** — posts, commentaires, threads pertinents sur la transformation IA dans les PME/ETI ; profils types Camille (COO ETI industrielle 180 personnes, 47 ans, non DSI) actifs publiquement.
4. **Presse spécialisée IA / dirigeants PME-ETI** — Les Échos Solutions, Maddyness, Frenchweb, sources sectorielles.
5. **Signaux veille marché** — alimentés par les fichiers cumulatifs Hub Content (`veille/cumulatifs/sectoriels/`, `veille/cumulatifs/financements.md`, `veille/cumulatifs/evenements.md`) enrichis quotidiennement par les tâches planifiées Cowork existantes.

Sur cette matière documentaire, les frameworks StarterClass J4-J5 restent applicables : qualification Pain DUR vs Vitamine, formulation Value Proposition Map, méthode « Et alors ? ». La grille est la même, les preuves diffèrent.

### 5.3 Garde-fou — statut des hypothèses

**Posture explicite assumée** : la documentation seule produit des **hypothèses non encore réfutées**, pas des hypothèses validées. Toute formulation Hub Strat issue de matière documentaire est tenue à cette nuance — formulation cible : *« les preuves indirectes convergent en direction de X, mais aucune invalidation terrain n'a été tentée ; risque de biais de confirmation à tracer »*.

### 5.4 Point de bascule possible

Si les signaux documentaires sont trop faibles ou trop divergents pour produire un cadrage opérable, Hub Strat ouvre un point d'arbitrage Cavalli pour **bascule vers interviews légères** (5-8 entretiens ciblés, format 30 minutes) — sans engager la mécanique d'enquête terrain canonique StarterClass, mais en confrontant les hypothèses les plus fragiles à quelques voix qualifiées. Décision différée, à instruire au plus tôt à fin module 2.

---

## 6. Hypothèses stratégiques à instrumenter

Cinq hypothèses Hub v2 sont formulées comme **propositions falsifiables** plutôt que comme conclusions. Elles sont l'objet de travail des sprints S3.1 à S3.8.

**H1 — Persona Camille existe et son JTBD résiste à l'analyse documentaire.** Camille (COO ETI industrielle 180 personnes, 47 ans, non DSI, non dirigeant fondateur, profil opérationnel-transverse en charge de la transformation IA) est-elle un profil **identifiable publiquement** ? Ses traces (posts LinkedIn, témoignages publics, commentaires sur outils existants) confirment-elles le JTBD énoncé dans la vision Hub v2 (« disposer d'une boussole IA pratique pour piloter les sujets IA sans devenir experte technique ni dépendre d'un cabinet conseil à 1500€/jour ») ?

**H2 — Hub v2 a un différenciateur défendable.** Face à Bpifrance Hub IA (gratuit, institutionnel, contenu hétérogène), French AI Lab (programmes structurés mais lourds), Diagnostic IA Numeum (outil ponctuel), EDIH régionaux (subventionnés, scope européen large), cabinets conseil (1500€/jour, sur-mesure), Hub v2 doit défendre un **positionnement unique**. Hypothèse : la **combinaison [base de connaissances curée par un SUM expérimenté + plateforme conversationnelle + ancrage souveraineté EU + ton pragmatique non hype + persona dirigeant PME/ETI explicitement ciblée]** n'est servie par aucun acteur identifié. À objectiver par la cartographie concurrentielle (livrable S3.3).

**H3 — Pricing hybride 3 leviers (statut hypothèse à challenger).** Le modèle Free 3 chats/jour / Pro 29€/mois / Équipe 19€/siège / crédits flexibles (note pricing du 25 mai 2026) est l'hypothèse de travail Hub Strat — **pas un acquis**. Il doit être confronté à : (i) benchmark pricing concurrents identifiés en H2 ; (ii) signaux disposition à payer documentaires (Camille comparée à ChatGPT Plus 20$, Claude Pro 20$, Notion AI 10$, Microsoft Copilot 30$, cabinets 1500€/jour). Question structurante : 29€/mois est-il perçu comme Pain-killer ou Vitamine pour une COO ETI ?

**H4 — Le canal d'acquisition principal est l'écosystème territorial Grand Est** avant SEO/SEA. Hypothèse cohérente avec l'ancrage Cavalli (SUM Quai Alpha, réseau QFC, présence sur l'écosystème vosgien et Grand Est) — mais à objectiver. Risque : si le canal territorial sature à 10-20 utilisateurs (taille effective de l'écosystème qualifié), il ne suffit pas pour viabiliser Pro 29€/mois × 24 mois. À chiffrer dans la modélisation économique.

**H5 — Statut side project jouable jusqu'à Étape 4** sans friction QFC majeure, à condition que le dossier d'arbitrage IP soit produit en module 4 (fin juillet) et qu'il sécurise les trois conditions énoncées dans la vision Hub v2 v1.0 (§2.1) : pas de conflit d'intérêt opérationnel, transparence d'implication, diffusion compatible.

---

## 7. Calendrier 8 semaines + jalons d'arbitrage Cavalli

### 7.1 Vue d'ensemble — sprints hebdomadaires

| Sprint | Semaine | Livrable structurant | Modules Vianeo travaillés | Statut |
|---|---|---|---|---|
| **S3.1** | 25-29 mai | **Note de cadrage Hub Strat v1** (ce document) | 1 + transverse | En cours |
| **S3.2** | 1-5 juin | Guide entretien persona Camille + plan recrutement *(différé / reformulé selon arbitrage b — voir §7.2)* | 2 | À ouvrir |
| **S3.3** | 8-12 juin | Cartographie concurrentielle v1 (tableau 8-12 concurrents, grille comparée, positionnement Hub v2) | 2 + 3 | À ouvrir |
| **S3.4** | 15-19 juin | Note garde-fous juridiques v1 (RGPD, AI Act, CGV/CGU, IP, statut side project — première version) | 3 + 4 | À ouvrir |
| **S3.5** | 22-26 juin | Première modélisation économique 24 mois (scenarios pessimiste / médian / optimiste, CAC, LTV, ARPU) | 4 | À ouvrir |
| **S3.6** | 29 juin-3 juil | Plan acquisition 10 premiers utilisateurs (territorial, profils, séquence d'approche, KPI) | 3 + 4 | À ouvrir |
| **S3.7** | 6-10 juil | Cartographie concurrentielle v2 + Value Proposition Map Hub v2 consolidé | 2 + 3 | À ouvrir |
| **S3.8** | 13-17 juil | **Dossier arbitrage IP / statut side project** (préalable Étape 4, anticipé) + roadmap S3.9+ | 4 | À ouvrir |

### 7.2 Reformulation S3.2 suite arbitrage Cavalli (b)

Le livrable initial S3.2 (« Guide entretien persona Camille + plan recrutement 8-12 entretiens fin juin ») est **reformulé** en : **« Protocole d'analyse documentaire persona Camille + cartographie sources qualifiées + grille d'extraction signaux ».** Le protocole d'interviews reste en réserve comme livrable activable si bascule §5.4 (signaux documentaires insuffisants). À confirmer.

### 7.3 Jalons d'arbitrage Cavalli identifiés

- **Fin S3.1 (29 mai)** — validation note de cadrage v1, validation de la reformulation S3.2, ouverture sprint S3.2.
- **Fin S3.4 (19 juin)** — point d'étape mi-parcours : reconduction calendrier ou bascule interviews légères selon qualité des signaux documentaires accumulés.
- **Fin S3.6 (3 juillet)** — convergence des livrables Hub Strat → arbitrage Cavalli sur pricing v2 si nécessaire (challenge confirmé ou ajusté du modèle hybride 3 leviers).
- **Fin S3.8 (17 juillet)** — clôture du module 4, dossier arbitrage IP prêt à transmission direction QFC, ouverture sprint S3.9+ post-clôture cycle 1 mi-juillet.

### 7.4 Notifications croisées prévues

| Livrable | Canal pair concerné | Type de notification |
|---|---|---|
| Note de cadrage v1 (S3.1) | DEV IA Head, Hub Content, Hub RAG, Claude Design | Information cadrage |
| Cartographie concurrentielle v1 (S3.3) | Hub Content, Claude Design | Implications positionnement éditorial + UX |
| Note garde-fous juridiques v1 (S3.4) | Hub Content, Claude Code Content, Claude Design | Implications RGPD/AI Act sur formulaires, CGV, mentions |
| Modélisation économique (S3.5) | DEV IA Head | Pattern transverse possible (chiffrage projets multi-acteurs) |
| Dossier arbitrage IP (S3.8) | DEV IA Head, Hub Content, Hub RAG | Implications structurelles fortes, à instruire en méta-gouvernance |

Toutes transmissions via Cavalli, conformément à la règle d'articulation inter-canaux.

---

## 8. Check pré-livrable et règle de versioning

### 8.1 Grille pré-livrable (à appliquer sur tout livrable Hub Strat avant transmission Cavalli)

1. Le livrable respecte-t-il l'**étanchéité QFC** ? Aucune matière confidentielle startups réelles, aucun CR comité, aucun contenu interne QFC.
2. Le livrable est-il dans le périmètre des **modules Vianeo activés** sur la période, dans le respect des règles de cohérence inter-modules §4.2 ?
3. Les **sources externes** sont-elles citées et vérifiables (concurrents, chiffres marché, réglementations, statistiques) ?
4. Le livrable **propose ou prétend décider** à la place de Cavalli ?
5. Y a-t-il des **impacts pour un autre canal** (Hub Content, Hub RAG, Claude Code, Claude Design, DEV IA Head) à signaler en notification croisée ?
6. Le livrable est-il **versionné** explicitement (vX.Y) ?
7. **(Auto-imposé)** Le livrable comporte-t-il un **bloc résumé exécutif transmissible** en un copier-coller pour notification autonome (mitigation risque méta-gouvernance #1) ?

### 8.2 Règle de versioning

Tous les livrables versionnés v1, v1.1, v2... Pas de remplacement silencieux. Pas d'affirmation sur l'état d'un livrable sans vérification du fichier. Modifications mineures (corrections, précisions) → incrément v1.x. Modifications majeures (restructuration, nouvelle hypothèse de travail, retour Cavalli structurant) → incrément vX. Historique versionné en pied de document.

### 8.3 Cadence

Sprint hebdomadaire. Un livrable structurant chaque vendredi. CR de sprint en fin de semaine. Sprint suivant ouvert le lundi sur la base du retour Cavalli.

---

## 9. Bloc résumé exécutif transmissible (mitigation risque méta-gouvernance #1)

> **À copier-coller pour notification autonome aux canaux pairs ou à DEV IA Head si besoin.**
>
> ---
>
> **Note de cadrage Hub Strat v1 — 25 mai 2026 — synthèse**
>
> Le canal Cowork Hub Strat (A1 de la cartographie d'orchestration 10 acteurs v1.0) est ouvert avec un mandat de **stratégie produit + GTM** sur Hub v2, side project entrepreneurial Cavalli. Il instrumente le pattern P15 reconnu par le canal head Initiative IA.
>
> **Méthodologie** : grille Vianeo à 4 dimensions **itérée en parallèle** (résolution explicite d'une tension avec la règle 3 du `_instructions.md` qui prescrivait une séquence stricte — proposition de réécriture v1.1 transmise à Cavalli), nourrie par les frameworks StarterClass v26 J3-J10. **Désirabilité documentaire assumée** comme écart vs StarterClass canonique : pas d'interviews terrain, substitution par benchmark + analyse usages en ligne + forums + presse + veille (arbitrage Cavalli 25 mai).
>
> **Cinq hypothèses falsifiables** à instrumenter (persona Camille, différenciateur défendable, pricing hybride 3 leviers à challenger, canal acquisition territorial, statut side project jouable). Calendrier 8 sprints hebdomadaires S3.1 → S3.8 (mai-juillet 2026), avec **anticipation du dossier d'arbitrage IP en module 4** (fin juillet) plutôt qu'au seuil Étape 4 calendaire.
>
> **Quatre jalons d'arbitrage Cavalli** identifiés : 29 mai (validation cadrage), 19 juin (point mi-parcours / bascule interviews légères possible), 3 juillet (arbitrage pricing v2 si nécessaire), 17 juillet (clôture cycle 1, dossier IP prêt).
>
> **Étanchéité QFC stricte** maintenue. **Règle des 5 doigts** : le canal propose, Cavalli décide.
>
> Source complète : `Canaux/Hub-Strat/outputs/note-cadrage-hub-strat-v1.md`

---

## Historique de versions

| Date | Version | Modification |
|------|---------|--------------|
| 25 mai 2026 | v1 | Création initiale — première production du canal Hub Strat post-ouverture. Intègre les 4 arbitrages Cavalli (lecture StarterClass, pricing en hypothèse à challenger, mode lean itératif parallèle, anticipation dossier IP), la cartographie d'orchestration 10 acteurs v1.0, l'écart méthodologique « pas d'interviews » assumé, les frameworks StarterClass v26 J3-J10. Propose une réécriture v1.1 de la règle 3 du `_instructions.md` à instruire en parallèle. |

---

*Note rédigée par Cowork Hub Strat le 25 mai 2026 — en attente de validation Cavalli avant transmission croisée aux canaux pairs. Première application du check pré-livrable §8.1 réalisée en interne canal (sept points OK).*
