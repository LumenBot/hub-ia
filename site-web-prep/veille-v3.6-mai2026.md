# Veille v3.6 — Hub IA (mai 2026)

> **Périmètre** : sourçage éditorial pour 4 livrables v3.6 — CU-023 (Devis intelligent), CU-024 (Order-to-cash), CU-027 (Dev applicatif IA-assisté), PR-07 (Build vs Buy à l'ère de l'IA).
> **Date de production** : 9 mai 2026.
> **Public cible** : dirigeants PME/ETI non-IT du Grand Est.

---

## Synthèse exécutive

1. **Bascule de l'adoption IA en France fin 2025** — Bpifrance Le Lab mesure **55 % des TPE-PME utilisatrices d'IA générative fin 2025** (vs 31 % fin 2024). Côté France Num (échantillon 11 021 entreprises, terrain mars-avril 2025) : **26 % des TPE-PME utilisent une IA, 34 % chez les PME** — chiffre doublé en un an. Le sujet est sorti de l'expérimentation et entre en arbitrage opérationnel — exactement la fenêtre où Hub IA devient utile.

2. **Le « scaling gap » est l'angle éditorial fort** — McKinsey State of AI 2025 : 88 % des entreprises utilisent l'IA dans au moins une fonction, mais seul **6 % sont « AI high performers »** (>5 % d'EBIT impact). MIT NANDA *State of AI in Business 2025* : **95 % des projets GenAI en entreprise ne génèrent aucun ROI mesurable** sur 30-40 Md$ investis. La vraie question n'est plus « faut-il y aller » mais « comment ne pas faire partie des 95 % qui ratent ».

3. **Build vs Buy : le seuil de rentabilité du « build » s'est effondré** — MIT NANDA : les stratégies « buy » (vendor + partenariat) réussissent **2x plus souvent** que les builds internes (~67 % vs ~33 %). Mais le dev IA-assisté change la donne : les outils 2025-2026 (Cursor, Claude Code, Lovable…) compriment les délais de 20-50 % et abaissent le break-even du custom. Le bon angle pour PR-07 : **« le build redevient une option pour des process différenciants, à condition de piloter les écueils »**.

4. **Vibe coding = opportunité ET piège mortel pour PME non-IT** — Gains documentés (Lovable : MVP en 25 min ; GitHub Copilot : -55 % de temps de tâche), mais Cloud Security Alliance & ITPro 2025 : **45 % du code généré par LLM contient des failles de sécurité**, secrets exposés à 3,2 % vs 1,5 % pour les commits humains, **8x plus de duplications** (GitClear, 211M lignes). Le fiasco **Tea App (juillet 2025, 72 000 photos d'identité fuitées)** est le contre-exemple incontournable pour CU-027.

5. **Calendrier réglementaire qui structure CU-024** — Facturation électronique obligatoire **en réception au 1er sept. 2026** (toutes entreprises), **en émission au 1er sept. 2027 pour les PME/TPE**. **120 Plateformes Agréées (PA, ex-PDP)** immatriculées DGFiP en avril 2026. Coût médian observé : **17,99 €/mois** sur 113 PA analysées. AI Act applicable au scoring client à partir d'**août 2026** (système haut risque) — sujet à intégrer dans la partie « écueils » de CU-024.

---

## Sujet 1 — CU-023 Devis intelligent

### Chiffres clés
- **55 % des TPE-PME** utilisent une IA générative fin 2025 (Bpifrance Le Lab, déc. 2025) — [presse Bpifrance](https://presse.bpifrance.fr/lia-dans-les-pme-et-eti-francaises-une-revolution-tranquille/?lang=fra)
- **28 % des entreprises** appliquent l'IA au marketing/ventes en 2025 (+11 points en un an) — [Bpifrance Le Lab — 6 chiffres à retenir](https://lelab.bpifrance.fr/Etudes/les-entreprises-francaises-et-l-ia-l-aube-d-une-revolution/l-ia-dans-les-pme-et-eti-francaises-6-chiffres-a-retenir)
- **72 % des utilisateurs IA** s'en servent pour la génération de contenus — Baromètre France Num 2025 ([rapport PDF](https://www.francenum.gouv.fr/files/2025-09/Barom%C3%A8tre%20France%20Num%202025%20-%20Rapport.pdf))
- **PandaDoc + HubSpot** — étude de cas Consensus : **temps de création de proposition divisé par 2** dans le trimestre suivant l'implémentation. Étude HPC Technology Group : passage d'1 h+ à 36 min par proposition, **+20 % de taux de closing** — [pandadoc.com](https://www.pandadoc.com/customers-case-study/goconsensus/)
- **GitHub Copilot benchmark développeur** (transposable à la productivité de rédaction structurée) : **-55 % de temps de tâche**, taux de succès passant de 70 % à 78 % — [GitHub Blog](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/)

### Outils émergents (FR + international)
**FR / EU :**
- **Pennylane** (PA agréée DGFiP, ~49 €/mois, OCR + IA pour réconciliation, module devis intégré au cycle compta)
- **Axonaut** (PA agréée, ERP/CRM tout-en-un, ~70 €/mois, conçu à Toulouse)
- **Sellsy** (CRM + pilotage ventes, ~25 €/mois/utilisateur, B2B PME)
- **Tiime, Indy, Abby** : offres PA gratuites ou très bas coût pour TPE

**International :**
- **PandaDoc AI** (proposition + e-signature, intégration HubSpot/Salesforce native — études de cas publiques disponibles)
- **HubSpot AI** (CPQ intégré au CRM, génération de devis depuis fiche deal)
- **Salesforce Einstein** (recommandation produits + pricing dynamique sur catalogue complexe)
- **Tacton** (CPQ vertical industriel, AI Product Modeling Assistant lancé 2025) — [itbrief.co.uk](https://itbrief.co.uk/story/tacton-launches-ai-assistant-to-cut-cpq-modelling-work)

### RetEx PME documentés
- **Consensus** (US, plateforme demo automation) : -50 % temps de proposition, 84 % des propositions vues par les prospects via PandaDoc + HubSpot
- **HPC Technology Group** : 36 min/proposition vs >1 h, +20 % closing rate
- **Carr Workplaces** : -15 % time-to-close, 100 K$/an d'économies sur stack précédente
- *Pas de retour public PME française documenté de qualité institutionnelle trouvé sur la génération de devis IA — angle à compenser par le contre-exemple ou l'interview directe d'un porteur Quai Alpha.*

### Écueils typiques
- **Hallucination prix / catalogue** : Gartner et littérature CPQ 2025 insistent sur la nécessité d'une IA **« déterministe, auditable, rule-bound »** plutôt que générative pure pour le pricing — sinon recommandations « black-box » dangereuses sur grand compte.
- **Désynchronisation conditions générales** : un devis IA qui régénère ses CGV à chaque appel sans contrôle juridique = risque contractuel.
- **Trop d'automatisation = aliénation des commerciaux** : la littérature CPQ 2025 documente le rejet quand l'IA décide seule sur des deals stratégiques (perte de jugement humain).
- **Workslop** : Microsoft New Future of Work 2025 — **40 % des collaborateurs subissent mensuellement** du contenu IA « qui a l'air bon mais contient des erreurs », forçant des corrections — [Microsoft Research](https://www.microsoft.com/en-us/research/publication/new-future-of-work-report-2025/)
- **Risque de dérive marge** : sans garde-fou, l'IA optimise pour la conversion, pas pour la rentabilité.

### Sources principales
- [Bpifrance Le Lab — L'IA dans les PME et ETI françaises (juin 2025, PDF)](https://lelab.bpifrance.fr/content/download/4745/pdf/2025-06_L'IA%20dans%20les%20PME%20et%20ETI%20fran%C3%A7aises_Etude%20Bpifrance%20Le%20Lab.pdf)
- [Baromètre France Num 2025 — Rapport (sept. 2025, PDF)](https://www.francenum.gouv.fr/files/2025-09/Barom%C3%A8tre%20France%20Num%202025%20-%20Rapport.pdf)
- [Microsoft New Future of Work Report 2025](https://www.microsoft.com/en-us/research/publication/new-future-of-work-report-2025/)
- [GitHub Copilot productivity research](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/)
- [PandaDoc — études de cas Consensus / HPC](https://www.pandadoc.com/customers-case-study/goconsensus/)

---

## Sujet 2 — CU-024 Order-to-cash automation

### Chiffres clés
- **DSO moyen PME/ETI françaises : 65 jours en 2025** (Observatoire des délais de paiement, Banque de France, juillet 2025) — [Daf-Mag](https://www.daf-mag.fr/tresorerie-1239/gestion-des-flux-du-cash-2118/le-dso-des-pme-et-eti-grimpe-a-65-jours-25694)
- **Délai de paiement moyen** fin 2024 : **13,6 jours** (au-dessus moyenne européenne, +1 jour vs 2023) — [Banque de France, ODP 2024 PDF](https://www.banque-france.fr/system/files/2025-07/ODP-2024.pdf)
- **Coût pour les PME** : **15 Md€** de cash flow pénalisé par les retards de paiement (ODP 2024)
- **Sidetrade** (leader européen O2C IA, 55 M€ CA 2024, +26 %) : **réduction moyenne de 30-40 % du DSO excédentaire** chez les clients — [sidetrade.com](https://www.sidetrade.com/)
- **Esker / O2C intégré** : **+35-50 % de productivité** sur les opérations recouvrement et O2C documentée par l'éditeur
- **DGCCRF 2024** : **+18,5 % d'anomalies détectées** dans les contrôles délais de paiement — la pression réglementaire monte

### Outils émergents (FR + international)
**FR / EU intégrés :**
- **Sidetrade** (O2C IA-native, plateforme « Aimie », forte sur multi-devises et grands comptes)
- **Aston AI** (recouvrement ciblé PME/ETI, scoring de risque, priorisation des relances)
- **Esker** (suite S2P/O2C complète, PA agréée e-invoicing)
- **Pennylane / Axonaut / Sellsy** (volet O2C couvert dans la suite de gestion, PA agréées DGFiP)

**International :**
- **HighRadius** (leader US, IA prédictive sur défaut de paiement)
- **Billtrust** (focus mid-market US)
- **UiPath** (RPA + IA pour O2C automation cross-applicatif)

### RetEx PME documentés
- **Sidetrade** publie des cas clients ETI avec **30-40 % de DSO excédentaire en moins** — chiffres éditeur, à pondérer.
- *Pas de RetEx public Bpifrance / France Num spécifiquement sur O2C IA en PME française trouvé. Angle à compenser par les chiffres ODP et l'angle réglementaire 2026.*

### Écueils typiques
- **Intégration ERP existant** : la majorité des PME ont un Sage / Cegid legacy ; le branchement O2C IA peut prendre 3-6 mois et représenter 30-50 % du coût total.
- **Conformité facturation électronique 2026** : tout outil O2C doit être **PA agréée DGFiP** ou interopérable avec une PA. **120 PA immatriculées avril 2026** ([economie.gouv.fr](https://www.economie.gouv.fr/actualites/facturation-electronique-la-liste-des-101-premieres-plateformes-agreees-est-disponible)).
- **AI Act et scoring client** : à partir du **2 août 2026**, les systèmes de scoring de solvabilité sont classés **« haut risque »** au sens AI Act — exigent CE marking, documentation technique exhaustive, logs, supervision humaine permanente. La CNIL est l'autorité de référence en France ([CNIL — entrée en vigueur AI Act](https://www.cnil.fr/fr/entree-en-vigueur-du-reglement-europeen-sur-lia-les-premieres-questions-reponses-de-la-cnil)).
- **Biais de scoring** : risque de discrimination algorithmique sur la priorisation des relances → contrôle ACPR obligatoire pour les fintech.
- **Sur-relance** : un agent IA peut envoyer 3 relances/jour à un bon payeur → casser la relation client.

### Sources principales
- [Banque de France — Observatoire des Délais de Paiement 2024 (PDF)](https://www.banque-france.fr/system/files/2025-07/ODP-2024.pdf)
- [Daf-Mag — Trésorerie sous tension : l'IA levier stratégique pour les DAF](https://www.daf-mag.fr/tresorerie-1239/financement-de-la-tresorerie-2119/tresorerie-sous-tension-quand-lia-devient-un-levier-strategique-pour-les-directions-financieres-22812)
- [economie.gouv.fr — Facturation électronique : 101 PA immatriculées](https://www.economie.gouv.fr/actualites/facturation-electronique-la-liste-des-101-premieres-plateformes-agreees-est-disponible)
- [Urssaf — Facturation électronique 1er sept. 2026](https://www.urssaf.fr/accueil/actualites/facturation-electronique.html)
- [CNIL — AI Act : premières Q-R](https://www.cnil.fr/fr/entree-en-vigueur-du-reglement-europeen-sur-lia-les-premieres-questions-reponses-de-la-cnil)

---

## Sujet 3 — CU-027 Dev applicatif métier IA-assisté (priorité 1)

### Chiffres clés
- **Lovable** : **20 M$ ARR atteints en 2 mois** (claim startup confirmé par utilisateurs ; MVP en ~25 min) — utile pour illustrer l'accélération.
- **GitHub Copilot** : **-55 % de temps de tâche**, satisfaction +60-75 %, **+10,6 % de PR/mois** ([GitHub Blog](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/))
- **Code AI-généré insécurisé** : **45 %** des outputs LLM contiennent des failles de sécurité sur 100 LLM testés et 80 tâches (Cloud Security Alliance, 2025) — [csa labs](https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-generated-code-security-vibe-coding-202/)
- **Secrets exposés** : commits IA-assistés exposent des secrets à **3,2 %** vs 1,5 % humain (multi-études 2025)
- **5 600 apps « vibe-codées » publiquement** scannées : **2 000 vulnérabilités critiques**, **400 secrets exposés**, **175 cas de PII** (dossiers médicaux, paiements) — analyse 2025
- **Dette technique** : analyse GitClear sur **211 millions de lignes** : **8x plus de blocs dupliqués** (5+ lignes), **-39,9 % de refactoring**
- **Fortune 50** : **10x plus de findings sécurité/mois** entre déc. 2024 et juin 2025 (~1 000 → >10 000)
- **Projection sectorielle** : **75 % des entreprises** auront une dette technique en sévérité moyenne-haute en 2026, IA citée cause majeure
- **Délai dev** : **POC IA-assisté = 6-10 semaines** vs **app production-ready = 4-7 mois** (vs 12-24 mois ESN classique)

### Outils émergents (panorama 2025-2026)

| Outil | Positionnement | Usage cible PME |
|-------|----------------|-----------------|
| **Lovable** | App builder no-code IA, MVP rapide | Dirigeant non-IT validant une idée |
| **Bolt.new** | Prototype démo, frontend-first | Démo client / pitch investisseur |
| **v0 (Vercel)** | UI generation, Next.js natif | Pages marketing + interfaces |
| **Cursor** | Éditeur IDE IA (fork VS Code) | Prestataire / dev senior |
| **Claude Code** | Agent CLI sur codebase | Refactoring massif, audit |
| **Windsurf** | IDE agentique production | Code « shippable » avec tests |
| **Replit Agent** | Cloud + déploiement intégré | App web complète sans setup |

**Comparatif benchmark Aqua Voice / DEV.to (2025-2026)** :
- **Production-ready** : Windsurf (8,5/10) > Cursor (7,5/10) > Replit (7/10)
- **Vitesse prototype** : Replit ~45 min, Windsurf ~65 min vers prototype fonctionnel
- **Sécurité** : GitHub Copilot seul outil ayant produit **0 issue de sécurité** dans le benchmark Aqua Voice (style génératif conservateur)

### RetEx documentés et incident emblématique

**Tea App (juillet 2025) — incident emblématique à intégrer :**
- App de dating « women-only » US, ~72 000 photos d'identité (selfies + permis de conduire) exposées
- Cause directe : base **Firebase ouverte sans authentification**, code généré par IA déployé sans revue
- Données conservées au-delà de la promesse de suppression immédiate
- Tous les utilisateurs pouvaient télécharger les chats des autres via la clé API
- Sources : [Barracuda blog](https://blog.barracuda.com/2025/12/22/vibe-coding-and-the-tea-app-breach--why-security-can-t-be-an-aft), [Hackread](https://hackread.com/tea-app-breach-women-dating-platform-user-images-leak/), [ainvest](https://www.ainvest.com/news/tea-app-data-breach-exposes-72-000-users-ai-generated-code-security-lapse-2507/)

**RetEx PME française documenté** : *Pas de retour public structuré trouvé d'une PME française ayant fait développer une app métier en quelques semaines via vibe coding. Angle à compléter via réseau Quai Alpha / French Tech East.*

### Écueils typiques (à structurer pour CU-027)

1. **Sécurité** — secrets en dur, auth manquante, SSRF systématique sur les apps url-handling, RGPD non-respecté.
2. **Dette technique long terme** — duplication, manque de refactoring, code « qui marche mais que personne ne comprend ».
3. **Dépendance modèle** — un changement de modèle (ex. Claude 3.5 → Claude 4) peut casser des comportements implicites.
4. **Hallucinations dans le code** — appels API inexistants, libs fantômes, signatures de fonction incorrectes.
5. **Workslop appliqué au code** — code qui « a l'air bon » mais bug en prod (Microsoft, NFOW 2025).
6. **Compétences cachées sous-estimées** — déploiement, monitoring, RGPD, backup : un dirigeant non-IT découvre vite que « faire coder par IA » ≠ « avoir une app en prod ».

### Cadre juridique synthétique (pour PME non-IT)

- **PI du code généré** : Anthropic et OpenAI cèdent les droits sur les outputs au client (CGV commerciales). En droit français, le code créé par un salarié dans le cadre de son emploi appartient à l'employeur, IA-assisté ou non. Le droit d'auteur reste réservé à l'humain (US Copyright Office janv. 2025, position relayée en France par CMS Legal et Paris Place de Droit). Sources : [droit.developpez.com](https://droit.developpez.com/actu/382670/), [livre blanc Paris Place de Droit (oct. 2025, PDF)](https://www.parisplacededroit.org/wp-content/uploads/2025/10/Livre-blanc-IA-sept-2025-V6-2.pdf)
- **RGPD** : Anthropic = sous-traitant au sens RGPD dès qu'il y a données personnelles. ISO 42001 obtenue janvier 2026. Hébergement Europe (Frankfurt/Paris) possible depuis juin 2024. Source : [CNIL — recommandations IA RGPD](https://www.cnil.fr/fr/ia-et-rgpd-la-cnil-publie-ses-nouvelles-recommandations-pour-accompagner-une-innovation-responsable)
- **AI Act** : applicable aux systèmes haut-risque dès août 2026 — impact direct si l'app fait du scoring/RH/credit.

### Sources principales
- [Cloud Security Alliance — Vibe Coding Security](https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-generated-code-security-vibe-coding-202/)
- [arxiv 2512.11922 — Vibe Coding in Practice : Flow, Technical Debt, Guidelines](https://arxiv.org/abs/2512.11922)
- [Barracuda Networks — Tea app breach analysis](https://blog.barracuda.com/2025/12/22/vibe-coding-and-the-tea-app-breach--why-security-can-t-be-an-aft)
- [GitHub Copilot — research productivity](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/)
- [DEV.to — Cursor vs Claude Code vs Windsurf vs Replit Agent vs Copilot](https://dev.to/paulthedev/i-built-the-same-app-5-ways-cursor-vs-claude-code-vs-windsurf-vs-replit-agent-vs-github-copilot-50m2)
- [CNIL — recommandations IA RGPD](https://www.cnil.fr/fr/ia-et-rgpd-la-cnil-publie-ses-nouvelles-recommandations-pour-accompagner-une-innovation-responsable)

---

## Sujet 4 — PR-07 Build vs Buy à l'ère de l'IA

### Chiffres clés
- **MIT NANDA — State of AI in Business 2025** : sur 30-40 Md$ investis en GenAI entreprise, **95 % des projets ne génèrent aucun ROI mesurable**. Les stratégies « **buy** » (vendor + partenariat) **réussissent ~67 %** du temps ; les builds internes ~33 % seulement (~2x moins). Source : [Fortune (août 2025)](https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/) ; [Virtualization Review](https://virtualizationreview.com/articles/2025/08/19/mit-report-finds-most-ai-business-investments-fail-reveals-genai-divide.aspx)
- **McKinsey State of AI 2025** : 88 % des organisations utilisent l'IA dans ≥1 fonction (vs 78 % en 2024). **39 % seulement** rapportent un effet EBIT mesurable, et **6 % seulement sont AI high performers** (>5 % EBIT). [McKinsey](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai)
- **Retool 2026 Build vs Buy report** (817 clients) : **35 % ont remplacé au moins un SaaS par un build interne**, **78 % anticipent davantage de builds internes en 2026**. Source : [retool.com](https://retool.com/blog/ai-build-vs-buy-report-2026)
- **Compression économique du « build »** : dev IA-assisté **-20 à -30 %** sur les délais (Talk Think Do), **-40 à -50 %** sur le coût/feature vs dev traditionnel.
- **Délais types 2025-2026** : POC IA = 6-10 semaines ; production-ready = 4-7 mois.
- **PwC AI Jobs Barometer 2025** : industries AI-exposées multiplient leur croissance de productivité par ~4 (de 7 % en 2018-2022 à 27 % en 2018-2024) ; **+56 % de prime salariale** sur les jobs IA — la compétence interne devient stratégique. Source : [PwC](https://www.pwc.com/gx/en/issues/artificial-intelligence/job-barometer/2025/report.pdf)

### Critères de décision actualisés en 2026

**Quand BUY (SaaS) reste le bon choix :**
- L'IA n'est pas un différenciant compétitif (cas de la majorité des process « commodity »)
- Pas d'équipe IT en interne pour maintenir
- Validation rapide d'un cas d'usage avant engagement
- Use case bien servi par un modèle généraliste
- ROI rapide nécessaire, modèle économique éprouvé
- Conformité réglementaire externalisée (PA agréée DGFiP, certifications, ISO)

**Quand BUILD redevient pertinent (avec IA-assisted dev) :**
- L'IA façonne le positionnement compétitif (process différenciant)
- Workflow propre que le SaaS ne couvre pas
- Volume utilisateurs élevé qui justifie l'amortissement
- Dépendance critique au fournisseur SaaS (lock-in, prix qui montent)
- Compétences internes mobilisables ou prestataire IA-natif accessible

**Approche hybride — pattern dominant 2026 :**
SaaS pour les briques « commodity » (compta, paie, CRM standard), build léger IA-assisté pour les **micro-applications métier** spécifiques (workflows, intégrations, reporting custom).

### RetEx FR documentés
- **Pas de RetEx FR PME publié de qualité institutionnelle (Bpifrance Le Lab, France Num) trouvé spécifiquement sur l'arbitrage build vs buy IA-assisté en PME**. Le segment ETI commence à émerger via Sidetrade, Esker (cas clients éditeurs).
- Témoignage **Forelite (Alliance Forêt-Bois)** mentionné par France Num — IA assistant les opérateurs sur le contrôle de semis forestiers ([France Num — podcast PME & IA](https://www.francenum.gouv.fr/guides-et-conseils/intelligence-artificielle/comprendre-et-adopter-lia/le-podcast-les-pme-lia)) : cas typique de build léger sur un besoin sectoriel non couvert.

### Écueils typiques

1. **Sous-estimer la maintenance** — un build n'est jamais « fini » : monitoring, mise à jour, sécurité, mise en conformité (RGPD, AI Act, facturation électronique). Coût récurrent ~20-30 %/an du coût initial.
2. **Sur-estimer les compétences internes** — beaucoup de PME pensent pouvoir « former leur stagiaire à Cursor » ; la réalité de la mise en prod (CI/CD, sécurité, RGPD) requiert un profil dev senior.
3. **Confondre démo et production** (« vibe coding revolution or danger ? ») — le « ça marche sur ma machine » est une étape, pas un livrable client.
4. **Sous-estimer la dette technique** — études GitClear / arxiv 2025 : la dette IA-assistée s'accumule plus vite qu'avec le dev humain.
5. **Choisir SaaS par défaut sans calcul total cost of ownership** — un SaaS à 50 €/mois × 10 utilisateurs × 5 ans = 30 K€ + dépendance + paramétrage. Un build IA-assisté peut concurrencer.
6. **Choisir Build sans gouvernance** — le 95 % d'échec MIT NANDA s'explique largement par l'absence de revue, de redesign de workflow, de pilotage métier.
7. **Ignorer le « workflow redesign »** — McKinsey : seul critère le plus corrélé à l'EBIT-impact, mais **21 % seulement** des organisations IA ont redesigné leurs workflows.

### Sources principales
- [MIT NANDA — State of AI in Business 2025 (relayé Fortune)](https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/)
- [McKinsey — State of AI 2025 (mars 2025, PDF)](https://www.mckinsey.com/~/media/mckinsey/business%20functions/quantumblack/our%20insights/the%20state%20of%20ai/2025/the-state-of-ai-how-organizations-are-rewiring-to-capture-value_final.pdf)
- [McKinsey — State of AI 2025 (novembre 2025, PDF)](https://www.mckinsey.com/~/media/mckinsey/business%20functions/quantumblack/our%20insights/the%20state%20of%20ai/november%202025/the-state-of-ai-2025-agents-innovation_cmyk-v1.pdf)
- [PwC AI Jobs Barometer 2025](https://www.pwc.com/gx/en/issues/artificial-intelligence/job-barometer/2025/report.pdf)
- [Retool — Build vs Buy 2026 report](https://retool.com/blog/ai-build-vs-buy-report-2026)
- [Bpifrance Le Lab — IA dans les PME et ETI françaises (juin 2025)](https://lelab.bpifrance.fr/content/download/4745/pdf/2025-06_L'IA%20dans%20les%20PME%20et%20ETI%20fran%C3%A7aises_Etude%20Bpifrance%20Le%20Lab.pdf)

---

## Recommandations éditoriales pour Cowork

**Par ordre de priorité pour la production des 4 livrables :**

1. **PR-07 (Build vs Buy) doit être publié AVANT CU-023, CU-024 et CU-027** — c'est le préalable conceptuel. L'angle fort : **« le seuil de rentabilité du build s'est effondré, mais 95 % des projets IA en entreprise ne génèrent toujours aucun ROI. La différence : la gouvernance et le redesign de workflow »**. Bibliographie : MIT NANDA, McKinsey, Retool. Construire une **matrice de décision en 6 critères** (process différenciant ? volume ? évolutivité ? budget ? compétences internes ? délai ?) que le dirigeant peut appliquer en 15 min.

2. **CU-027 (Dev applicatif IA-assisté) — angle « comment piloter sans être IT »** — le livrable doit absolument inclure : (a) panorama des 6-7 outils 2026 sous forme de tableau lisible par dirigeant, (b) **incident Tea App comme cas pédagogique** (concret, viral, dommageable), (c) checklist sécurité minimale exigée d'un prestataire vibe coding (auth, secrets, RGPD, monitoring, contrat), (d) cadre juridique PI + AI Act + RGPD synthétisé en 1 page. Éviter les contre-indications généralistes : nommer les outils, donner des prix, donner des délais.

3. **CU-024 (Order-to-cash)** doit faire de la **facturation électronique 1er sept. 2026** son ancrage temporel — c'est l'événement réglementaire qui force tous les dirigeants à arbitrer **maintenant**. Croiser avec : DSO 65 jours en 2025, 15 Md€ de cash flow PME pénalisé, AI Act haut-risque applicable août 2026 sur les scoring clients. Lister les **PA agréées DGFiP par segment** (TPE / PME B2B / PME B2C / ETI) pour passer à l'action.

4. **CU-023 (Devis intelligent)** est le cas d'usage le plus accessible (gain rapide, faible risque) — angle éditorial : **« commencer par là pour tester l'IA opérationnelle »**. Le bon framing : pas un projet IA, **un projet commercial assisté par IA**, dont le commercial reste responsable. Mettre en avant le ratio **HPC : 36 min vs 1 h+, +20 % closing** comme chiffre choc, en précisant que c'est une étude éditeur.

**Éléments transversaux à ne pas oublier dans tous les livrables :**
- Toujours rappeler le **« scaling gap »** (88 % adoptent, 6 % en tirent vraiment de l'EBIT) — c'est la prise de réalité qui distingue un dirigeant lucide d'un dirigeant FOMO.
- Toujours mentionner l'AI Act calendrier 2026 quand pertinent (scoring, RH, recouvrement).
- Quand un chiffre vient d'un éditeur (Sidetrade, Esker, PandaDoc), le préciser explicitement pour préserver la crédibilité éditoriale.
- **Données manquantes à compléter par interview directe via réseau Quai Alpha** : RetEx PME française qualifié sur (a) déploiement devis IA, (b) déploiement O2C IA, (c) build app métier IA-assisté en quelques semaines. Ces 3 témoignages PME Grand Est apporteraient une signature éditoriale unique.
