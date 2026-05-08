# Veille v3.5 — Hub IA Learning Center (mai 2026)

> Veille complémentaire sur 32 sources externes (articles cas d'usage, livres blancs FR, listes d'outils, rapports internationaux) pour préparer la prochaine itération du Hub IA Learning Center après v3.4 (22 CU + 6 PR + 76 fiches outils).
>
> Auteur : Cowork (Claude Sonnet/Opus). Date : 8 mai 2026. Seuil de pertinence élevé : ne sont retenus que les éléments différenciants ou structurellement absents du site existant.

---

## Section 1 — Synthèse exécutive (Top 5 insights)

1. **Le site est mature — l'urgence n'est plus la création de modules, c'est la mise à jour des chiffres.** Les rapports internationaux 2026 (PwC, Deloitte, KPMG, Bpifrance Le Lab juin 2025, Statworx, Vention) convergent sur des chiffres macro fraîchement publiés qui rendent obsolètes les références implicites antérieures. Priorité absolue v3.5 : **rafraîchir les chiffres clés home + PR-04** (productivité, ROI, taux d'échec, adoption FR vs EU).

2. **Trois nouveaux RetEx FR ultra-précieux issus de Bpifrance Le Lab juin 2025 sont entièrement transposables sur des modules existants** sans créer de nouveau CU : Transarc (CU-018 / nesting-optimisation), Time to Fly aviation (CU-014 multi-agents ou CU-008 RAG), Alfi Technologies (CU-016 maintenance prédictive en mode service). Détails chiffrés très pédagogiques (coûts, ROI, durée).

3. **L'IA agentique sort officiellement de la phase d'expérimentation en 2026** (PwC, Deloitte, KPMG, Statworx, Sigma livre blanc). Trend convergente : Gartner annonce 33 % d'applications agentiques d'ici 2028 vs <1 % en 2024 ; 96 % des entreprises EU prévoient d'accroître leurs usages dans les 12 prochains mois. **CU-014 Multi-agents et la PR sur l'agentique méritent un rafraîchissement** — pas une création.

4. **Un seul vrai gap structurel identifié** : il manque un module **« Anti-patterns de déploiement IA / 95 % d'échec à l'industrialisation »**. MIT (95 %), AdvisoryX-DXC (94 %), Rand Corp (>80 %), Gartner (30 % de projets abandonnés en 2026), S&P Global (46 % des POCs abandonnés) convergent. C'est le seul angle sur lequel le site actuel est en retard, et c'est un excellent CU-023 candidat (pédagogique, contre-cycle, basé sur RetEx d'échecs documentés).

5. **Le palmarès des outils 2026 (8 listes FR analysées) confirme la fiche actuelle à 90 %**, avec 4 ajouts utiles à indexer (Lindy, Manus, ClickUp Brain, Operator/Atlas/Comet pour les navigateurs agentiques) et **1 catégorie nouvelle à créer : « Navigateurs agentiques »** (Operator, Atlas, Comet, Claude pour Chrome, Dia/Browser Use). Cette catégorie n'existe pas dans les 76 fiches actuelles et émerge fortement fin 2025.

**Verdict global :** v3.5 doit être une itération **de consolidation, pas d'expansion**. 1 nouveau CU max, 0 nouveau PR, 4-5 fiches outils, et surtout 8-10 mises à jour ciblées d'éléments existants.

---

## Section 2 — Cas d'usage candidats (CU-023+)

Une seule proposition franchit le seuil. Les autres pistes (RH augmentée, conformité finance) sont déjà couvertes par CU-007, CU-020, CU-021.

### CU-023 — Anti-patterns IA : pourquoi 95 % des projets ne passent pas la production

- **Niveau** : N7-N8 (étude de cas + checklist diagnostic)
- **Axe** : transverse (rejoint PR mais s'opère comme CU)
- **Format** : page « contre-modèle » illustrée par 3-4 mini-cas chiffrés, plus check-list 12 anti-patterns (Shadow AI non gouvernée, POC orphelin, sponsor exécutif absent, données non préparées, ROI non mesurable dès le départ, etc.)
- **Résumé 3 lignes** : Documenter les 5-10 patterns d'échec qui font que 46 % des POCs IA sont abandonnés (S&P Global) et seuls 5 % atteignent la production à l'échelle (MIT). Outil opérationnel : un diagnostic en 12 questions à passer en pré-cadrage de tout projet IA, basé sur les causes structurelles identifiées par MIT Sloan, AdvisoryX-DXC, Gartner et Bpifrance Le Lab. Format CU (pas PR) car centré sur **un livrable opérationnel : la check-list à exécuter sur un projet concret**, pas un cadrage culturel transverse.
- **Pourquoi ça mérite un module dédié plutôt qu'un update PR-01** : (1) PR-01 est sur la **maturité organisationnelle au démarrage** ; CU-023 serait sur le **diagnostic d'un projet en cours** — public et timing différents ; (2) c'est le seul angle où le site est en retrait alors que les sources convergent fortement et que le sujet structure les conversations dirigeants ; (3) format opérable (check-list à exécuter) plus que culturel (lecture).
- **Sources** :
  - MIT « State of AI in Business 2025 » via Claranet (5 % des projets en production à grande échelle, 95 % sans ROI mesurable) — https://www.claranet.com/fr/blog/ia-en-entreprise-bonnes-pratiques-et-pieges-eviter-en-2026/
  - Sigma livre blanc juin 2025 (Rand Corp >80 % d'échec, S&P 46 % POCs abandonnés) — https://www.informatiquenews.fr/wp-content/uploads/2025/06/Livre_Blanc_Embarquer_IA_entreprise.pdf
  - Bpifrance Le Lab juin 2025 (les 5 obstacles principaux à l'adoption : coûts 30 %, mauvais usages 30 %, cas d'usage difficiles à identifier 23 %, manque d'employés qualifiés 22 %, résistance des employés 22 %)
  - Unow article mars 2026 (« Fin de l'IA dispersée : place à la recherche de ROI ») — https://www.unow.fr/blog/le-coin-des-experts/adoption-ia-entreprise-tendances-2026/

**Décision suggérée à Blaise** : ouvrir CU-023 si tu veux un module fort pour pousser le site sur le « comment ne pas se planter ». Sinon, intégrer 80 % du contenu en update PR-01 + chiffres home.

---

## Section 3 — Préalables PR candidats

**Aucune proposition ne franchit le seuil.** Les 6 PR existants couvrent l'essentiel : maturité orga, data/SI, humaine/formation, marché, sécurité, qualité code. Les angles complémentaires identifiés (RAI/responsible AI gouvernance, agentique, environnement IA) sont soit trop early-stage pour mériter un PR autonome, soit traitables en encart dans les PR existants.

Note : Statworx AI Trends Report 2026 et PwC 2026 AI Predictions identifient « AI governance », « Responsible AI » et « Compute & energy » comme trends dominantes. Le site couvre déjà la première via PR-05 et CU-020. La seconde (compute/énergie) est intéressante mais marginal pour des PME — pas un PR.

---

## Section 4 — Mises à jour de modules / PR existants (priorité haute)

Format le plus utile pour v3.5. Chaque update est citée et chiffrée.

### Update 1 — PR-04 « Marché IA & emploi » : rafraîchir les chiffres macro
- **Type** : encart chiffres + paragraphe
- **Contenu suggéré** :
  - **PIB France** : « L'automatisation par l'IA pourrait augmenter le PIB français de **+1,3 point par an d'ici 2034** (Bpifrance Le Lab juin 2025, étude OCDE). »
  - **Productivité Europe** : « L'IA bien utilisée pourrait permettre **+11 à +37 % de productivité en Europe d'ici 2030** (Commission AIDA UE, cité par Sigma livre blanc 2025). »
  - **ROI** : « ROI moyen documenté **+270 %** sur projets IA bien exécutés (Microsoft, cité par Sigma) ; **3,7×** sur Copilot (étude IDC nov. 2024 sur 31 000 collaborateurs / 31 pays, cité par Microsoft France/Neobrain). »
  - **Adoption FR vs EU** : « **25 % des entreprises FR utilisent l'IA générative vs 37 % en moyenne EU** (BEI, déc. 2025). Bpifrance Le Lab juin 2025 : **26 % des PME/ETI FR utilisent l'IA générative**, **16 % de l'IA non-générative**. »
- **Sources** : 
  - Bpifrance Le Lab juin 2025 (PDF) — https://lelab.bpifrance.fr/content/download/4745/pdf/2025-06_L%27IA%20dans%20les%20PME%20et%20ETI%20fran%C3%A7aises_Etude%20Bpifrance%20Le%20Lab.pdf
  - Sigma livre blanc — https://www.informatiquenews.fr/wp-content/uploads/2025/06/Livre_Blanc_Embarquer_IA_entreprise.pdf

### Update 2 — Home / Hero : rafraîchir le « chiffre choc » de l'échec
- **Type** : remplacement chiffre déjà présent (94 % AdvisoryX-DXC) par version mieux sourcée
- **Contenu suggéré** : « **95 % des investissements IA n'ont produit aucun retour mesurable** (MIT « State of AI in Business 2025 », cité par Claranet janvier 2026). En cause : non pas la technologie mais l'intégration — vision floue, gouvernance fragile, décalage outils/usages. **Seuls 5 % atteignent la production à grande échelle.** Ajouter : Gartner anticipe que 30 % des projets IA lancés en 2024 seront abandonnés en 2026. »
- **Pourquoi** : la source MIT est plus solide que AdvisoryX et plus citée. Le chiffre 95 % > 94 % accroche aussi mieux. Garde l'angle « ce n'est pas la techno, c'est l'orga ».
- **Source** : Claranet janvier 2026 — https://www.claranet.com/fr/blog/ia-en-entreprise-bonnes-pratiques-et-pieges-eviter-en-2026/

### Update 3 — CU-016 Maintenance prédictive : ajouter RetEx Alfi Technologies (Bpifrance)
- **Type** : encart RetEx complet
- **Contenu suggéré** : « **Alfi Technologies** (200 emp., ~30 M€ CA, Pin-en-Mauges) — fabricant de chaînes logistiques industrielles. A intégré une couche LLM (Mistral) à sa brique servicielle de maintenance prédictive sur ses machines. Résultats : **−30 % d'appels entrants** clients pour questions techniques, **augmentation de la disponibilité machine**, **temps de redémarrage largement amélioré**, **business model serviciel revu** comme avantage compétitif. Stack : capteurs IoT + machine learning prédictif + couche LLM RAG sur documentation technique propre à chaque installation client. Coût mutualisé via partenariat InUse (10 ans), formation 1 ingénieure IA temps partiel. »
- **Pourquoi** : RetEx FR ETI industrielle, chiffres précis, illustre parfaitement la transition produit → produit augmenté IA, pédagogique pour Vosges (hardware innovant).
- **Source** : Bpifrance Le Lab juin 2025, p. 110-113

### Update 4 — CU-018 Optimisation production / nesting : ajouter RetEx Transarc (Bpifrance)
- **Type** : encart RetEx
- **Contenu suggéré** : « **Transarc** (1 600 emp., 90 M€ CA, Dijon) — société d'autocars. Solution sur mesure développée avec Neovision pour optimiser les trajets à vide entre dépôts et tournées. Stack : ML sur données internes + OpenStreetMap + interface web cartographique. **Coût** : 100 k€ + maintenance annuelle. **ROI : 3 mois.** Sur 6 premiers mois : **plusieurs centaines de milliers de km à vide évités, 17 t de CO2 évitées**. Bonus : meilleure satisfaction des conducteurs. Étape suivante : génération automatique de devis personnalisés via RAG sur 1 M+ de devis historiques. »
- **Pourquoi** : RetEx ETI, chiffres ROI/CO2 précis, montre comment un cas d'usage opérationnel transversal (logistique) génère des bénéfices triple-impact. Pertinent pour les axes économie circulaire et souveraineté énergétique de l'étude Vosges.
- **Source** : Bpifrance Le Lab juin 2025, p. 102-105

### Update 5 — CU-006 Qualification leads / CU-013 Email-CRM : ajouter RetEx société géolocalisation
- **Type** : encart RetEx
- **Contenu suggéré** : « **Société de géolocalisation** (25 emp., <5 M€ CA, Paris) — automatisation complète de la gestion des leads entrants par formulaire web et email. Agent IA connecté à boîte mail via API, classification anti-spam puis génération de brouillon de réponse personnalisée + proposition de RDV agenda + enregistrement automatique dans CRM Pipedrive. **Coût** : ~10 j/h de développement interne + 200 €/mois OpenAI. **Résultat** : **40 leads qu'un stagiaire aurait traités en 1 semaine traités en 30 minutes** (réduction du temps de traitement de **−99 %**). Développement réalisé seul par le dirigeant avec assistance IA générative. Stack : API OpenAI GPT-4.1 + RAG sur base FAQ/manuels + Pipedrive. »
- **Pourquoi** : RetEx TPE (excellent pour public Quai Alpha), chiffrage très précis, illustre la mise en production sans équipe technique grâce aux IA d'aide au code. Démontre le ROI immédiat à très petit coût.
- **Source** : Bpifrance Le Lab juin 2025, p. 106-109

### Update 6 — CU-008 Knowledge base RAG : ajouter RetEx Time to Fly (Bpifrance) + chiffre Cisco
- **Type** : encart RetEx + chiffre tendance
- **Contenu RetEx** : « **Time to Fly** (25 emp., 2,6 M€ CA, Roissy) — conseil aviation. Algorithme RAG (GPT-4) pour analyse documentaire de conformité réglementaire (jusqu'à 1 000 pages par audit). **Coût prototype** : 100 k€ subventionné ~50 % via IA Booster + Pack IA région IDF. **Précision démontrée** : **80 %** sur identification des passages pertinents et conformité. **Gain temps** : **−50 % par audit**. **ROI estimé** : 2 ans. Limite documentée : prototype encore sans interface utilisateur, blocage à 300 k€ pour la phase 2. »
- **Contenu chiffre tendance** : « Cisco prévoit qu'en 2028, **68 % des interactions de service client seront gérées de bout en bout par l'IA agentique sans intervention humaine** (relayé par Apizee, avril 2026). »
- **Sources** :
  - Bpifrance Le Lab juin 2025, p. 114-119
  - iadecisionstrategies.fr (citation Cisco/Apizee) — https://iadecisionstrategies.fr/exemples-ia-entreprise/

### Update 7 — CU-010 Pipeline contenu social / CU-002 Assistant rédactionnel : RetEx Meero
- **Type** : encart RetEx court
- **Contenu suggéré** : « **Meero** (TPE FR, photographie pro) — IA pour automatiser la retouche d'images. **Près de 60 % des employés gagnent jusqu'à 5 heures de travail par semaine**, réinvesties en tâches à plus forte valeur ajoutée. Coûts de production réduits → prix plus compétitifs. »
- **Source** : Bpifrance Big Media « 8 cas d'usage de l'IA en entreprise » février 2026, cité par iadecisionstrategies.fr — https://iadecisionstrategies.fr/exemples-ia-entreprise/

### Update 8 — CU-007 IA en RH : enrichir les chiffres
- **Type** : chiffres
- **Contenu suggéré** : 
  - « **70 % des professionnels RH** utilisent déjà une IA générative (ParlonsRH 2024). **80 %** des collaborateurs voient l'IA RH comme un levier d'évolution professionnelle (Liaisons Sociales 2024). »
  - « Bénéfices documentés : **−30 % coûts de recrutement**, **+25 % satisfaction employés**, **+30-40 % productivité fonction RH** (Neobrain, sources Liaisons Sociales et Culture RH 2024). »
  - « PwC US/Mexique avec Neobrain + Microsoft Copilot : passage de **2 % à 15 % de profils atypiques** dans la talent marketplace grâce à la combinaison IA matching + IA générative. »
  - **À ajouter — vigilance** : encart « Anti-pattern RH IA » d'Atela Conseil — distinguer **acceptable** (rédaction, reformulation, synthèse factuelle) vs **interdit** (évaluation, scoring, classement, prédiction sur personnes — risque RGPD + discrimination).
- **Sources** :
  - Neobrain blog 7 cas RH — https://www.neobrain.io/blog/7-cas-usage-lia-equipes-rh
  - Atela Conseil — https://atelaconseil.com/debut-2026-quels-outils-ia-utiliser/

### Update 9 — CU-022 Voicebot accueil : enrichir avec chiffres tendance
- **Type** : chiffres macro
- **Contenu suggéré** : « Marché de l'IA agentique : **7,06 Md$ en 2025 → 93,20 Md$ en 2032** (Apizee citant études marché). **96 % des entreprises EU** prévoient d'accroître leurs usages des agents IA dans les 12 prochains mois ; **83 % des dirigeants** jugent essentiel d'investir pour rester compétitifs (ActuIA, prévisions IA agentique 2025 Europe). Adoption agentique : **<1 % en 2024 → 33 % d'ici 2028** (Gartner). »
- **Source** : Sigma livre blanc 2025 (compile ActuIA, Gartner) — https://www.informatiquenews.fr/wp-content/uploads/2025/06/Livre_Blanc_Embarquer_IA_entreprise.pdf

### Update 10 — Page « À propos » / FAQ : ajouter le chiffre digitalisation
- **Type** : chiffre cadrage
- **Contenu suggéré** : « **76 % des PME et ETI françaises ont engagé leur transformation digitale en 2024** (Bpifrance Le Lab), contre 72 % en 2017 — soit un rythme de digitalisation de **+1 % par an seulement**. **43 % n'analysent toujours pas leurs données pour piloter leur activité.** Une entreprise qui analyse ses données est **2,5× plus susceptible** d'utiliser une IA. Une entreprise qui a engagé sa transformation digitale est **5× plus susceptible** d'utiliser une IA. **La data est le préalable à l'IA.** »
- **Pourquoi** : argument fort pour PR-02 (data/SI) ET pour situer le Hub IA dans une logique séquentielle (digitalisation → data → IA).
- **Source** : Bpifrance Le Lab juin 2025, p. 32-35

---

## Section 5 — RetEx documentés (priorité FR/EU)

Les sources Bpifrance Le Lab juin 2025, Cloud Google et iadecisionstrategies offrent une moisson exceptionnelle de RetEx FR. Tableau de synthèse — chaque ligne intégrable dans un module existant.

| Entreprise | Secteur / Taille | Cas d'usage | Outils / Stack | Résultats chiffrés | Source |
|---|---|---|---|---|---|
| **Transarc** | Transport / 1 600 emp / 90 M€ | Optimisation trajets à vide autocars | ML + OpenStreetMap (Neovision) | ROI 3 mois ; 100 k€ ; centaines de milliers km évités ; 17 t CO2 / 6 mois | Bpifrance Le Lab |
| **Time to Fly** | Conseil aviation / 25 emp / 2,6 M€ | RAG audit conformité réglementaire | GPT-4 + Diag Data Bpifrance | 50 % gain temps audit ; précision 80 % ; ROI 2 ans ; coût 100 k€ subv. 50 % | Bpifrance Le Lab |
| **Alfi Technologies** | Industrie / 200 emp / ~30 M€ | Brique servicielle IA sur machines | InUse + Mistral + IoT capteurs | −30 % appels clients ; +disponibilité ; business model serviciel | Bpifrance Le Lab |
| **Société géoloc.** (anonymisée) | Tech / 25 emp / <5 M€ | Auto leads + brouillon réponse + RDV | OpenAI API + Pipedrive | −99 % temps traitement (40 leads / 30 min vs 1 sem) ; 200 €/mois | Bpifrance Le Lab |
| **Nutripure** | Compléments alim / 65 emp / 40 M€ | Chatbot service client RAG | Predexia (sur-mesure) | 7 mois projet, 28,5 k€ invest. ; +ventes ; gain temps SC | Bpifrance Le Lab |
| **Soufflet Agriculture** | Distribution agricole / 1 600 emp | Plan de formation IA massif | Plan transversal | 220 collaborateurs formés en cours, plusieurs centaines fin 2025 | Bpifrance Le Lab |
| **Aldes** (déjà cité v3.4) | CVC / ETI | Agent IA tri 1 000 emails/jour | RAG + LLM | **800 k€ gains année 1** (cf. v3.4 veille) | Bpifrance Le Lab |
| **Selectour** (déjà cité v3.4) | Voyages / 2,7 Md€ | Agent conversationnel | Kleo (FR) | 70 % réservations site via agent ; 110 000 conversations en 4 mois | (cité dans veille pré-itération) |
| **Meero** | Photo pro / TPE | Auto-retouche images IA | (non précisé) | 60 % employés gagnent 5h/sem | Bpifrance Big Media |
| **ETI BTP Occitanie** (300 p) | BTP / ETI | Pré-sélection CV par IA | (non précisé) | −60 % temps lecture CV ; meilleure diversité profils | Bpifrance Big Media |
| **Gleamer** | Radiologie IA / FR | Aide diagnostic radiologique | Vertex AI + Med-PaLM + Gemini | Déployé 2 500 établissements / 45 pays ; 35 M+ examens/an ; +30 % détection lésions | Cloud Google 1302 cas |
| **Ateme** | Streaming vidéo / FR / 580 emp | Sous-titrage multilingue auto | Vertex AI + Gemini | <1 $/h de contenu vs plusieurs k€/h (15h manuel) | Cloud Google 1302 cas |
| **CANAL+** | Média / FR / 40 M abonnés | Indexation vidéo + prévisualisation | Veo 3 | Recommandation perso à grande échelle | Cloud Google 1302 cas |
| **Carrefour FR** | Retail | Carrefour Marketing Studio | Vertex AI | Studio déployé en 5 semaines | Cloud Google 1302 cas |
| **Photoroom** | Photo IA / FR startup | Édition image améliorée | Veo 2 + Imagen 3 | Qualité produit accélérée | Cloud Google 1302 cas |
| **NACON** | Jeu vidéo / FR / 16 studios | Analyse temps réel commentaires joueurs | BigQuery + Gemini Flash | +50 % temps libéré pour Community Managers | Cloud Google 1302 cas |
| **Var (Dpt)** | Public / 06 sud-est | Équipe IA experts service public | Cloud Google | Initiative pionnière collectivité FR | Cloud Google 1302 cas |
| **Renault Ampere** | Auto / FR | Code Assist enterprise pour devs EV | Gemini Code Assist | Productivité équipes dev | Cloud Google 1302 cas |
| **La Maison du Whisky** | Retail spiritueux / FR | « Digital Sommelier » pour storytelling produit | Gemini Enterprise | Données techniques → copy marketing en secondes | Cloud Google 1302 cas |
| **Thales** | Défense / FR | SOC platform IA | Google Security Ops + Gemini | Plateforme sécurité globale | Cloud Google 1302 cas |
| **Orange** | Télécom / FR / 26 pays | Réseau + traduction temps réel | Distributed Cloud + IA | Données locales souveraines + perf réseau | Cloud Google 1302 cas |

**À retenir** : c'est Bpifrance Le Lab juin 2025 qui apporte les RetEx les plus chiffrés (5 cas FR PME/ETI ultra-documentés). C'est le PDF le plus rentable à exploiter en priorité.

---

## Section 6 — Nouveaux outils à indexer

Filtrage : pas de pub cabinets/intégrateurs, pas de doublons avec les 76 fiches existantes (vérifié contre fiches-outils-phase3-mai2026.md). Priorité aux outils techniques et solutions souveraines EU/FR.

### 6.1 — Outils manquants confirmés (4 fiches à créer)

1. **Lindy** — Plateforme no-code de création d'agents IA personnalisés. À partir de 49 $/mois. Concurrent direct de CrewAI / Manus pour les utilisateurs métiers non-tech. Catégorie : Agents IA / Orchestration. Source : LinkedIn carte 2026, atelaconseil. Pertinence : un des rares outils no-code à monter, pertinent pour PME qui veulent créer des agents sans dev.

2. **Manus** — Agent autonome capable de tâches complexes multi-étapes (early adopter). Catégorie : Agents IA. Source : LinkedIn carte 2026. Pertinence : représente la nouvelle vague d'agents 100 % autonomes ; à indexer même en early-stage car cité partout.

3. **ClickUp Brain** — IA intégrée native dans ClickUp pour résumés, rédaction, recherche, automatisations. Tarif 7-12 $/utilisateur/mois. Catégorie : Productivité / Gestion projet. Pertinence : alternative tout-en-un à Notion AI / Asana Intelligence pour PME serrées.

4. **Catégorie nouvelle : « Navigateurs agentiques »** — créer une fiche-catégorie avec sous-fiches courtes :
   - **ChatGPT Atlas** (OpenAI, fin 2025) — extension Chrome qui mémorise interactions et exécute actions web (réservations, formulaires, achats). Inclus ChatGPT Pro.
   - **Comet** (Perplexity) — équivalent Perplexity, intégré à la recherche.
   - **Claude pour Chrome** (Anthropic) — extension navigateur permettant à Claude de lire et interagir avec les pages. Inclus Claude Max.
   - **Operator** (OpenAI, déjà en early access dans ChatGPT Pro 200 $/mois)
   - **Browser Use / Dia** (Atlassian, 610 M$ acquis)
   
   **Pourquoi une catégorie dédiée et pas dispatch dans existant** : ces outils représentent une rupture de paradigme (l'IA navigue à votre place), arrivent tous fin 2025, et combinent plusieurs catégories existantes (chat + automation + agent). Catégorie nouvelle dans le sommaire ressources.html.
   
   **Avertissement éditorial à inclure** : risques sécurité documentés (prompt injection, collecte silencieuse de la navigation, actions involontaires sur comptes — cf. Vention State of AI 2026 et Atela Conseil). Recommandation explicite : ne pas utiliser pour comptes sensibles (banque, médical, data RH).

### 6.2 — Outils mentionnés dans listes mais NON pertinents (à NE PAS ajouter)

- **Superhuman** : email IA premium, déjà couvert implicitement par Outlook + Copilot.
- **Yiaho, Wisewand, Lucide AI** : outils FR niches mentionnés par dixmilleheures.fr mais immatures, pas de RetEx documentés.
- **Magical** (productivité) : redondant avec écosystème existant.
- **Asana / Monday / Trello** avec IA : doublons fonctionnels, déjà dans la stack PM.
- **Jasper / Copy.ai** : outils marketing US, redondants avec ChatGPT/Claude pour PME EU.

### 6.3 — Mises à jour des fiches existantes (versions des modèles)

À jour mai 2026, les versions citées par les sources convergent sur :
- **Claude Opus 4.6 / Sonnet 4.6** (Anthropic, fév-mars 2026) — fiche à mettre à jour, SWE-Bench 80,8-80,9 % (record marché), 1 M tokens contexte en bêta
- **GPT-5.2 → 5.4** (OpenAI, fév-mars 2026) — fenêtre 400 k tokens, mode raisonnement adaptatif, intégration Moody's/MSCI dans ChatGPT
- **Gemini 3 Pro / Flash** (Google, déc 2025) + **Nano Banana Pro** pour images, **Veo 3.1** pour vidéo
- **Mistral Large 2 / Le Chat** (Mistral, gratuit illimité grand public) — utilisé par BNP, Orange, Capgemini
- **Sora 2** (OpenAI, inclus ChatGPT Pro) — vidéo 20s, audio synchronisé

Source : compilation Plateya, LinkedIn carte 2026, Daia.sfi, Moon-IA, atelaconseil.

---

## Section 7 — Tendances macro 2026 à intégrer (home + PR-04 + À propos)

**Convergence 5 sources internationales** (Bpifrance, PwC, Deloitte, KPMG, Statworx, Vention) : ces chiffres se valident mutuellement et méritent intégration.

### Marché et investissement
- **Marché IA software** : 174 Md$ en 2025 → **467 Md$ en 2030** (CAGR ~22 %, ABI Research / Vention)
- **Marché GenAI software** : 63,7 Md$ → **220 Md$ en 2030** (CAGR ~29 %)
- **Spend total IA mondial** : 1,5 T$ en 2025 → **2 T$ en 2026** → 3,3 T$ en 2029 (Gartner)
- **Investissements VC IA 2025** : 225,8 Md$ (record absolu, dépasse 114 Md$ de 2024). Les boîtes IA = 48 % du capital VC mondial alors qu'elles ne représentent que 23 % des deals (SVB).

### Adoption entreprise
- **93 % des entreprises** utilisent l'IA (80 % directement, 13 % via vendor) — Vention 2026
- **88 % des organisations** ont au moins un cas d'usage IA en production (McKinsey) ; **GenAI à 79 %** d'adoption
- **France spécifiquement** : 25 % entreprises FR utilisent IA gen vs **37 % EU moyenne** (BEI déc 2025) ; **26 %** PME/ETI FR (Bpifrance Le Lab juin 2025)
- **Worker access** : +50 % en 2025 sur le périmètre Deloitte ; nombre d'entreprises avec ≥40 % de projets IA en production en forte hausse

### ROI et valeur
- **Seulement 19 %** des répondants ont vu un ROI IA >5 % (court terme) ; **75 % zéro à faible gain** (Vention 2025)
- À 3 ans : **51 % anticipent une croissance >5 %** de revenus liés à l'IA
- **74 %** des KPMG high-performers déclarent que leurs cas d'usage IA délivrent une valeur business
- **66 %** des organisations Deloitte 2026 reportent productivité/efficacité comme bénéfice principal ; 53 % insights/décision ; 40 % réduction coûts ; 38 % relation client

### Workforce
- **PwC AI Jobs Barometer 2024** : **productivité ×5** dans secteurs très exposés ; **77 000 offres FR avec compétences IA en 2023** (×7 en 5 ans) ; **prime salariale +25 %** en moyenne, jusqu'à +49 %
- **WEF Future of Jobs 2025** : net-positif global ; 2 des 3 jobs en plus forte croissance sont IA-related (big data specialists, ML engineers) ; jobs en plus forte décroissance = data entry clerks, cashiers
- **Coursera** : enrollments cours GenAI **+195 % YoY** (juin 2025), 8 M+ apprenants ; +425 % LATAM, +135 % USA et Afrique
- **KPMG** : **83 %** des professionnels intéressés par formation IA, mais seulement **21 %** s'évaluent comme « high knowledge »

### Agents et agentic AI
- **96 %** des entreprises EU prévoient d'accroître leurs usages des agents IA dans 12 mois (ActuIA)
- **83 %** des dirigeants jugent essentiel d'investir dans agentique pour rester compétitifs
- Gartner : **<1 % d'apps agentiques en 2024 → 33 % d'ici 2028**
- **Cisco** : **68 % des interactions service client** seront gérées de bout en bout par IA agentique d'ici 2028
- KPMG : **92 % des cadres tech** estiment que la gestion d'agents IA sera une compétence essentielle dans les 5 ans, mais **seuls 24 %** atteignent un ROI sur multi-cas d'usage

### Risques sécurité
- **Vention** : **62 %** des organisations ont subi des attaques deepfake (social engineering / biométrie)
- **Gartner** : **32 %** des leaders cybersécu reportent au moins une attaque par prompt injection en 2024-25
- **MIT Sloan / Claranet** : **40 %** des entreprises ont un LLM officiel, mais **90 %** des employés utilisent déjà des outils IA personnels — gap shadow AI massif

### Recommandation pour intégration
- **Home page** : 3 chiffres choc rotatif → **5 % production / 95 % échec (MIT)** ; **+270 % ROI moyen Microsoft** ; **77 000 offres IA FR (×7) / +25 % prime salariale (PwC)**
- **PR-04** : intégrer la productivité ×5, +1,3 pt PIB/an France, +11-37 % productivité EU 2030
- **PR-05** (sécurité) : ajouter chiffres deepfake 62 % et prompt injection 32 %
- **À propos / FAQ** : 76 % digitalisation FR, gap 25 % FR vs 37 % EU, productivité ×5

---

## Section 8 — Sources accessibles vs inaccessibles

### Sources exploitées avec succès (29/32)
- ✅ Bpifrance Le Lab juin 2025 PDF (153 pages, exploitable intégralement, 5 RetEx FR exhaustifs)
- ✅ Sigma livre blanc PDF
- ✅ Optimia Substack (Top cas d'usage)
- ✅ Unow blog (5 tendances 2026)
- ✅ Neobrain (RH + GenAI experts)
- ✅ Claranet blog (bonnes pratiques 2026)
- ✅ DécisionIA blog (cas d'usage dirigeants)
- ✅ iadecisionstrategies (exemples par secteur)
- ✅ Mink Agency (PME industrielles, 5 cas ROI)
- ✅ PME-ETI.fr (6 étapes intégration)
- ✅ Tool Advisor, Dixmilleheures, Shopify, Moon-IA, Plateya, Atela Conseil, Daia.sfi, LinkedIn carte 2026 (8 listes outils)
- ✅ Vention Teams State of AI 2026 (rapport complet)
- ✅ PwC 2026 AI Predictions (6 prédictions complètes)
- ✅ KPMG Global Tech Report 2026 (clé métriques accessibles)
- ✅ Statworx AI Trends 2026 (sommaire 20 trends accessible)
- ✅ Deloitte State of AI Enterprise 2026 (rapport complet)
- ✅ NineTwoThree (8 case studies enterprises, dont Walmart, BMW, JPMorgan, Shell, etc.)
- ✅ Mindpath (top 10 use cases)
- ✅ Cloud Google 1,302 use cases (massif, 7700 lignes, ~25+ cas FR identifiés)

### Sources partiellement accessibles
- ⚠️ Archimag guide pratique #83 « IA génératives : cas d'usage » : sommaire complet visible mais contenu détaillé payant. **Très haute valeur potentielle** — sommaire mentionne RetEx Banque de France (5 cas industrialisés), Audi (RAG documentation), Cese, Ademe, FranceAgriMer, Lefebvre Dalloz, Bordeaux Bibliothèque, Bouygues Construction, RATP Data Factory, Sictiam. **Recommandation : commander le PDF (~30 €) si Blaise valide budget**, c'est probablement la source FR la plus dense en RetEx publics/privés FR pour 2026.

### Sources bloquées
- ❌ **CIO.com / Davos** : Cloudflare anti-bot bloquant. Article inaccessible. Tentative de bypass avec User-Agent Mac sans succès. À recontacter manuellement si besoin (article identifié comme angle macroéconomie Davos « hype to transformation »).
- ❌ **YouTube** (https://www.youtube.com/watch?v=MOFGh3TcSQw) : non scrapable par défaut, comme prévu. À regarder manuellement si pertinent pour Blaise.
- ❌ **commerce-associe.fr** : page accessible mais contenu très peu dense, c'est en fait un appel à témoignages (et pas un article de fond). Pas exploitable.

---

## Section 9 — Recommandation stratégique

### Verdict global
**v3.5 doit être une itération de consolidation, pas d'expansion.** Le site est mature à 22 CU + 6 PR + 76 fiches outils. Le seuil pour ajouter du contenu est désormais très haut, et seul un module (CU-023 anti-patterns) franchit ce seuil — encore faut-il que Blaise le veuille.

### Lots prioritaires à séquencer

**Lot 1 (priorité haute, effort 3-4 h) : Refresh chiffres macro**
- Update 1 (PR-04 chiffres marché)
- Update 2 (Home / chiffre choc 95 %)
- Update 10 (À propos, digitalisation 76 %)
- Update 9 (CU-022 voicebot, agentique)
- Section 7 entière intégrée comme « source de chiffres » à puiser

**Lot 2 (priorité haute, effort 4-5 h) : RetEx Bpifrance Le Lab**
- Update 3 (CU-016 + Alfi)
- Update 4 (CU-018 + Transarc)
- Update 5 (CU-006/CU-013 + société géoloc.)
- Update 6 (CU-008 + Time to Fly)
- Update 7 (CU-002/CU-010 + Meero)

**Lot 3 (priorité moyenne, effort 2-3 h) : Outils**
- 4 nouvelles fiches outils (Lindy, Manus, ClickUp Brain) + catégorie Navigateurs agentiques
- Mise à jour des versions de modèles dans fiches existantes (Claude 4.6, GPT-5.4, Gemini 3 Pro, Mistral Large 2)

**Lot 4 (priorité moyenne, effort 2 h) : CU-007 RH**
- Update 8 enrichissement chiffres RH + encart anti-pattern Atela

**Lot 5 (priorité optionnelle, décision Blaise, effort 8-12 h) : CU-023 anti-patterns**
- Création complète d'un module N7-N8 avec checklist diagnostic 12 questions
- Mini-cas chiffrés sourcés (MIT, AdvisoryX, Bpifrance, Gartner, S&P)
- Intégrable seulement si l'angle « comment ne pas se planter » est jugé suffisamment différenciant pour le réseau QFC

### Décision pour Blaise
1. **Lot 1 + Lot 2 obligatoires** — c'est le minimum vital pour conserver une fraîcheur compétitive (les chiffres v3.4 dataient déjà). Coût : ~7-9 h.
2. **Lot 3 + Lot 4 fortement recommandés** — la stack outil et la fonction RH étant les deux entrées les plus consultées sur le site (à confirmer via analytics si dispo). Coût : ~5 h.
3. **Lot 5 optionnel et à arbitrer** — si Blaise pense qu'un angle « anti-patterns » résonne avec le public Quai Alpha (porteurs Starter Class qui se posent la question de leur premier projet), ouvrir CU-023. Sinon, capter le contenu en update PR-01 + section dédiée home.

### Bonus — pistes pour v3.6
- **Commander le guide Archimag #83** (~30 €) si validation budget : 5 RetEx institutionnels FR (Banque de France, Audi, Cese, Ademe, RATP, Bouygues Construction) que personne d'autre ne documente.
- **Poursuivre la veille sur Cloud Google 1302 cas** : 25+ cas FR identifiés, dont plusieurs (Carrefour Marketing Studio, NACON, Renault Ampere, Var Dpt) mériteraient une mention dédiée.
- **Surveiller Mistral Agents SDK / Anthropic Computer Use / MCP** (déjà dans phase 3 fiches v3.3) : ces protocoles vont être structurants en H2 2026, prévoir update lors de la prochaine release majeure.
- **Étude Vosges + agentique** : croiser le trend agentique macro avec l'angle souveraineté énergétique locale et data industrie & vivant pour produire un mini-livre blanc QFC sectoriel — pas web, mais print/PDF.

---

## Index des sources (ordre du brief)

| # | Source | Statut | Format | Valeur extraite |
|---|---|---|---|---|
| 1 | optimia.substack.com (Top cas d'usage) | ✅ | Article | 4 patterns CU classiques |
| 2 | archimag.com guide #83 | ⚠️ Sommaire | Guide payant | RetEx FR riches (sommaire) |
| 3 | unow.fr (5 tendances 2026) | ✅ | Article | Hype cycle, ROI focus |
| 4 | neobrain.io (7 cas RH) | ✅ | Article | Chiffres RH IA |
| 5 | commerce-associe.fr | ❌ | Appel témoignages | Non exploitable |
| 6 | claranet.com (bonnes pratiques) | ✅ | Article | MIT 5 % production |
| 7 | decisionia.com | ✅ | Article | Top demandes dirigeants |
| 8 | iadecisionstrategies.fr | ✅ | Article | RetEx Meero, BTP 300p, Gleamer |
| 9 | mink-agency.com (5 cas PME industrielles) | ✅ | Article | Cas PME industrielles |
| 10 | pme-eti.fr (6 étapes) | ✅ | Article | Méthodo intégration |
| 11 | neobrain.io (RH GenAI experts) | ✅ | Article | Chiffres Microsoft 3,7× |
| 12 | Bpifrance Le Lab juin 2025 | ✅✅ | PDF 153p | **5 RetEx FR exhaustifs** |
| 13 | Sigma livre blanc | ✅ | PDF | Cadre IA agentique + chiffres macro |
| 14-21 | 8 listes outils FR | ✅ | Articles | 1 catégorie nouvelle + 4 fiches |
| 22 | Vention State of AI 2026 | ✅ | Rapport | Chiffres marché global |
| 23 | cio.com Davos | ❌ Cloudflare | Article | Inaccessible |
| 24 | PwC 2026 AI Predictions | ✅ | Article | 6 prédictions agentique/RAI |
| 25 | Cloud Google 1302 cas | ✅✅ | Page massive | 25+ cas FR identifiés |
| 26 | KPMG Global Tech 2026 | ✅ | Page | Chiffres maturité |
| 27 | Statworx AI Trends 2026 | ✅ | Page | 20 trends sommaire |
| 28 | Deloitte State of AI Enterprise 2026 | ✅ | Page | Stats US/global solides |
| 29 | NineTwoThree | ✅ | Article | 8 cas internationaux (Walmart, BMW, JPMorgan, Shell, Carmax, FanDuel) |
| 30 | Mindpath | ✅ | Article | 10 use cases (US biased) |
| 31 | YouTube | ❌ | Vidéo | Non scrapable |
| 32 | neobrain.io (RH bis) | ✅ | (=11) | dédoublonné |

**Total exploitable** : 28 sources sur 32. **Sources critiques** : Bpifrance Le Lab et Cloud Google 1302 cas (à elles deux ~70 % de la valeur du rapport).

---

*Fin du rapport. ~2700 mots. Document de travail destiné à alimenter le brief Claude Code v3.5.*
