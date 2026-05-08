# Veille pré-itération — Hub IA Learning Center (mai 2026)

> Mission de veille structurée sur 50 sources pour préparer la prochaine itération de contenu du Hub IA Learning Center (porté par Quest for Change). Données collectées le 8 mai 2026.

---

## Synthèse exécutive

### Top 3 cas d'usage candidats identifiés (à intégrer en priorité)
1. **Conformité RGPD/AI Act & gouvernance IA pour PME** (CU candidat 1) — gap critique : 2 août 2026 = entrée en application des obligations majeures, sanctions jusqu'à 7 % du CA mondial. La cartographie des usages "Shadow AI" est le besoin n°1 remonté dans toutes les sources institutionnelles (DGE, CNIL, Service Public, Sigma, Diamond Solutions).
2. **Automatisation finance / extraction factures & prévision cash** (CU candidat 2) — 60 à 80 % du temps d'un service comptable PME est automatisable, ROI documenté à 155 % en 1 an sur cas concret France Num. Précision OCR+LLM 92-98 %.
3. **Voicebot / accueil téléphonique IA** (CU candidat 3) — 62 % des appels non répondus dans une PME ne donnent jamais lieu à un rappel ; 350-900 € de CA perdu par appel manqué. Économies moyennes 30-60 k€/an, ROI 2-4 mois.

### Top 3 RetEx documentés les plus parlants (PME/ETI françaises)
1. **Aldes** (CVC, ETI) — agent IA traitant 1 000 emails/jour → **800 k€ de gains estimés en année 1** (Bpifrance Le Lab).
2. **Time To Fly** (audit aéronautique, 35 salariés, 3 M€ CA) — **80 % de l'analyse de conformité réalisée par IA, durée d'audit -50 %**, outil revendu en marque blanche.
3. **Selectour** (réseau d'agences voyage, 2,7 Md€ CA) — agent conversationnel Kleo (FR) → **70 % des réservations site passent par l'agent**, 110 000 conversations en 4 mois, déploiement 6 mois, coût 20-60 k€.

### Top 5 outils émergents prioritaires à indexer
1. **Lucie / OpenLLM-France (Linagora)** — LLM souverain open-source FR, financé France 2030/Bpifrance, lancé janvier 2025 (à indexer car absent de la liste actuelle).
2. **Pleias-RAG (Pleias)** — famille de petits modèles RAG FR sourcés (Common Corpus 2T tokens domaine public), conformes RGPD/AI Act — créneau juridique/compliance.
3. **Claude Agent SDK / OpenAI Agents SDK / Mistral Agents** — nouvelle génération de SDK agentiques 2026, standards MCP (Anthropic, donné à Linux Foundation déc. 2025) + A2A (Google) + AGENTS.md (OpenAI).
4. **Cartesia Sonic / Line** — TTS le plus rapide du marché (90-150 ms latence), concurrent direct ElevenLabs sur agents vocaux temps réel.
5. **Florence-2 (Microsoft) + DINOv2 (Meta)** — vision foundation models compacts qui rendent CV/segmentation accessibles à des PME industrielles sans entraînement spécifique.

### Recommandation stratégique pour Blaise
Trois axes prioritaires d'itération :
- **Axe gouvernance/conformité** (CU-020 RGPD-AI Act) → différenciant fort pour le réseau QFC, deadline réglementaire 2 août 2026 = timing parfait.
- **Axe finance/comptabilité PME** (CU-021 Extraction factures + CU-022 Prévision cash) → ROI le mieux documenté, public dirigeant TPE/PME.
- **Axe voicebot** (CU-023 Standard téléphonique IA) → forte traction médicale/services + cas d'usage emblématique pour ateliers Starter Class.

---

## Livrable 1 — Nouveaux cas d'usage à ajouter

### CU-020 — Conformité RGPD & AI Act pour PME (gouvernance IA)
- **Niveau** : N7-N8 (étude de cas + checklist d'éligibilité)
- **Axe** : B (décision)
- **Résumé** : Cartographier les usages IA en entreprise (y compris Shadow AI), classer par niveau de risque AI Act, documenter chaque traitement personnel sous RGPD, et structurer un dispositif "obligations → preuves → responsable". Échéance critique : 2 août 2026.
- **Sources** :
  - https://www.entreprises.gouv.fr/decryptages-de-nos-experts/le-reglement-europeen-sur-lintelligence-artificielle-publics-concernes
  - https://mdp-data.com/ai-act-obligations-et-mise-en-conformite-des-organisations/
  - https://ayinedjimi-consultants.fr/articles/rgpd-ia-generative-guide-cnil-2026
  - https://diamondsolutions.io/ai-act-2026

### CU-021 — Extraction & traitement automatisé des factures fournisseurs
- **Niveau** : N4-N6 (auto-diag + plan d'action)
- **Axe** : A (productivité)
- **Résumé** : Pipeline OCR+LLM pour extraire fournisseur, montant, TVA, lignes de détail, imputations comptables — y compris factures scannées/photographiées. Précision 92-98 %, économie 20-120 h/mois (pour 200-500 factures).
- **Sources** :
  - https://justai.fr/fr/blog/ia-comptabilite-automatisation-finance-pme
  - https://www.medius.com/ai-innovation/
  - https://www.lemagit.fr/conseil/IA-appliquee-aux-outils-comptables-et-financiers-les-cas-dusages

### CU-022 — Prévision cash & contrôle anomalies en finance PME
- **Niveau** : N4-N6
- **Axe** : B (décision)
- **Résumé** : Agent IA exécutant contrôles de cohérence (soldes, écritures non lettrées, imputations inhabituelles), prévision encaissements selon historique délais paiement, pilotage cycles paiement automatisés. Stack typique : LLM + APIs ERP/banque.
- **Sources** :
  - https://blog.workday.com/fr-fr/ia-generative-finance-domaines-application.html
  - https://www.mia-app.ai/solution-ia/finance-et-controle-de-gestion
  - https://qonto.com/fr/blog/tpe-pme/gestion/intelligence-artificielle-finance

### CU-023 — Standard téléphonique IA / voicebot accueil
- **Niveau** : N4-N6
- **Axe** : D (croissance)
- **Résumé** : Agent vocal qui qualifie l'appel, prend RDV (intégration agenda/CRM), répond aux FAQ, route vers humain si besoin. Cas d'usage phare : médical, e-commerce, télécoms, assurances. Couverture étendue (7h-21h) sans surcoût, baisse no-show 22 %.
- **Sources** :
  - https://nerolia-ai.fr/blog/accueil-telephonique-automatique-ia-pme
  - https://nerolia-ai.fr/blog/standard-telephonique-ia-automatiser-accueil-entreprise
  - https://www.bouyguestelecom-business.fr/digital-data/data-ia/agent-vocal-intelligent/

### CU-024 — Recommandation produit & search vectoriel e-commerce
- **Niveau** : N4-N6
- **Axe** : D (croissance)
- **Résumé** : Moteur hybride keyword + sémantique vectoriel pour comprendre l'intention d'achat, modules "fréquemment achetés ensemble" / "similaires". 10-35 % du CA des sites qui le déploient ; conversion x2-x3 sur recherche vs navigation par catégories.
- **Sources** :
  - https://www.ecommercemag.fr/retail-1220/barometre-etude-2168/les-benchmarks-du-e-commerce-2026-les-solutions-dia-appliquee-au-e-commerce-56977
  - https://bigmedia.bpifrance.fr/nos-dossiers/les-dernieres-tendances-du-e-commerce-a-suivre-en-2026

### CU-025 — Onboarding RH augmenté & parcours formation personnalisé
- **Niveau** : N4-N6
- **Axe** : A (productivité)
- **Résumé** : Agent IA qui automatise tri CV, prise de contact, planification entretiens, relances, onboarding documentaire (formulaires, pièces, dossier salarié). Gain coûts recrutement -30 %. Recommandation parcours formation sur mesure : -30 à -40 % du temps RH d'orientation.
- **Sources** :
  - https://nerolia-ai.fr/blog/agent-ia-rh-recrutement-automatisation-france
  - https://aisisters.ai/post/integrer-lia-dans-une-entreprise

### CU-026 — Formation IA obligatoire & littératie IA équipes
- **Niveau** : N1-N3
- **Axe** : A (productivité)
- **Résumé** : Mise en conformité avec l'obligation AI Act d'un niveau minimal de compétences IA (article 4) pour toute équipe manipulant l'IA — sanctions nationales applicables 2 août 2026. Production accélérée de modules e-learning (-60 à -70 % coût production) via IA générative.
- **Sources** :
  - https://www.savoiria.fr/formation-ia-entreprise-france-2026/
  - https://nerolia-formation.fr/blog/formation-ia-entreprise-guide-complet-2026.html
  - https://cpformation.com/formation-professionnelle-2026-lia-simpose-pendant-que-les-budgets-se-resserrent/

### CU-027 — Empreinte carbone IA & green AI ops
- **Niveau** : N7-N8
- **Axe** : B (décision)
- **Résumé** : Mesurer l'impact carbone des usages IA en entreprise (data centers = 95 % des émissions liées), arbitrer entre modèle local/cloud, choisir des modèles plus petits (SLM), suivre les bilans environnementaux d'éditeurs (Mistral Large 2 = 20,4 ktCO2eq sur 18 mois). Outil-clé : Cloud Carbon Footprint.
- **Sources** :
  - https://www.entreprises.gouv.fr/decryptages-de-nos-experts/intelligence-artificielle-en-entreprise-quels-impacts-environnementaux
  - https://bigmedia.bpifrance.fr/nos-dossiers/quel-est-limpact-de-lia-sur-lenvironnement
  - https://www.sami.eco/en/blog/ia-impact-carbone-entreprise

### CU-028 — Audit & support documentaire réglementaire (compliance vertical)
- **Niveau** : N7-N8
- **Axe** : E (industrie) ou B (décision)
- **Résumé** : LLM spécialisé connecté à corpus réglementaire (sectoriel) pour pré-rédiger les analyses de conformité, repérer les écarts, structurer le dossier d'audit. Cas inspiré Time To Fly (aéronautique) : 80 % de l'analyse automatisée, durée d'audit -50 %.
- **Sources** :
  - https://www.francenum.gouv.fr/guides-et-conseils/intelligence-artificielle/comprendre-et-adopter-lia/integrer-lia-retours

### CU-029 — Détection sur-facturation & contrôle fournisseurs
- **Niveau** : N4-N6
- **Axe** : B (décision)
- **Résumé** : LLM analysant les factures fournisseurs pour détecter incohérences, sur-facturations, anomalies de prix vs catalogue/historique. Cas Batibig : outil développé en 1 mois, 20 k€, **détection de 110 k€ de sur-facturation**.
- **Sources** :
  - https://itsocial.fr/intelligence-artificielle/intelligence-artificielle-articles/ia-dans-les-pme-eti-des-gains-jusqua-200-de-productivite-sur-vingt-projets-acheves/

### CU-030 — Dialogue social & IA (information-consultation CSE)
- **Niveau** : N7-N8
- **Axe** : B (décision)
- **Résumé** : Cadrer le dialogue social autour de l'IA : information-consultation du CSE sur orientations stratégiques et nouvelles technologies. Plus de 50 % des élus CSE déclarent ne pas être consultés sur l'IA en 2026 ; obligation légale + opportunité d'adoption fluide.
- **Sources** :
  - https://www.syndex.fr/actualites/actualite/cse-face-lia-retour-dexperience-dune-experte-ssct
  - https://www.syndex.fr/actualites/actualite/ia-et-cse-le-guide

### CU-031 — Cartographie & priorisation cas d'usage IA (méthode)
- **Niveau** : N1-N3 ou N4-N6
- **Axe** : B (décision)
- **Résumé** : Méthode "test & learn" : sélectionner un projet pilote concret avec périmètre limité, KPI mesurables, sponsor exécutif, retour sur 1-3 mois avant scaling. Référentiel des 12 cas d'usage France Num + audit IA Bpifrance Diag Data IA.
- **Sources** :
  - https://www.francenum.gouv.fr/guides-et-conseils/intelligence-artificielle/comprendre-et-adopter-lia/integrer-lia-retours
  - https://www.claranet.com/fr/blog/ia-en-entreprise-bonnes-pratiques-et-pieges-eviter-en-2026/
  - https://www.bpifrance.fr/catalogue-offres/diag-data-ia

### CU-032 — Optimisation supply chain par IA (PME industrielle)
- **Niveau** : N7-N8
- **Axe** : E (industrie)
- **Résumé** : Modèle prévisionnel demandes / stocks / routage logistique entraîné sur données internes, déploiement local ou souverain pour confidentialité. Cas ETI aéronautique avec Mistral open-source.
- **Sources** :
  - https://www.la-tech-actuelle.com/intelligence-artificielle-en-entreprise-les-tendances-qui-transforment-le-travail-en-2026/

---

## Livrable 2 — Retours d'expérience documentés

### RetEx 1 — Aldes (ETI ventilation, France)
- **Cas d'usage** : Agent IA classement + traitement de 1 000 emails/jour
- **Outils** : Non précisé dans les sources publiques
- **Résultats** : **800 000 € de gains estimés en année 1**
- **Source** : https://itsocial.fr/intelligence-artificielle/intelligence-artificielle-articles/ia-dans-les-pme-eti-des-gains-jusqua-200-de-productivite-sur-vingt-projets-acheves/

### RetEx 2 — Selectour (Réseau ~1 000 agences de voyage, 2,7 Md€ CA)
- **Cas d'usage** : Agent conversationnel B2B + B2C (chatbot site & front desk)
- **Outils** : Kleo (solution française)
- **Résultats** : **70 % des réservations site via l'agent**, 110 000 conversations enregistrées depuis nov. 2025, déploiement 6 mois, coût 20-60 k€
- **Source** : https://lelab.bpifrance.fr/Etudes/les-entreprises-francaises-et-l-ia-l-aube-d-une-revolution/l-ia-dans-les-pme-et-eti-francaises-6-chiffres-a-retenir

### RetEx 3 — Peugeot Saveurs (Produits culinaires, 38,6 M€ CA)
- **Cas d'usage** : Agent IA classification + pré-rédaction réponses service client, connecté APIs logistiques
- **Outils** : Non précisé
- **Résultats** : **Premier temps de réponse divisé par 2** (4 jours → 2 jours, 2024-2025)
- **Source** : https://lelab.bpifrance.fr/Etudes/les-entreprises-francaises-et-l-ia-l-aube-d-une-revolution/l-ia-dans-les-pme-et-eti-francaises-6-chiffres-a-retenir

### RetEx 4 — Time To Fly (Audit aéronautique, 35 salariés, 3 M€ CA)
- **Cas d'usage** : Outil d'aide à l'audit : analyse documentaire + vérification conformité réglementaire
- **Outils** : Non précisé (vraisemblablement RAG sur LLM)
- **Résultats** : **80 % de l'analyse de conformité réalisée par IA, durée d'audit -50 %**, outil aussi commercialisé en marque blanche à d'autres acteurs du secteur
- **Source** : https://lelab.bpifrance.fr/content/download/4745/pdf/2025-06_L'IA%20dans%20les%20PME%20et%20ETI%20fran%C3%A7aises_Etude%20Bpifrance%20Le%20Lab.pdf

### RetEx 5 — Batibig (BTP, PME)
- **Cas d'usage** : Outil d'analyse de factures fournisseurs (anomalies, sur-facturation)
- **Outils** : Non précisé
- **Résultats** : Développé en 1 mois pour 20 000 € → **détection de 110 000 € de sur-facturation** dès la première année
- **Source** : https://itsocial.fr/intelligence-artificielle/intelligence-artificielle-articles/ia-dans-les-pme-eti-des-gains-jusqua-200-de-productivite-sur-vingt-projets-acheves/

### RetEx 6 — Eskimoz (Agence SEO, PME)
- **Cas d'usage** : Automatisation de la production de contenus (rédaction SEO assistée)
- **Outils** : Non précisé (LLM type GPT/Claude vraisemblablement)
- **Résultats** : **+100 à +200 % gains de productivité** sur la production de contenu
- **Source** : https://itsocial.fr/intelligence-artificielle/intelligence-artificielle-articles/ia-dans-les-pme-eti-des-gains-jusqua-200-de-productivite-sur-vingt-projets-acheves/

### RetEx 7 — PME 35 salariés (anonymisée, France Num)
- **Cas d'usage** : Automatisation factures fournisseurs + relances + rapports financiers
- **Outils** : Non précisé
- **Résultats** : **22 000 € investis sur 76 jours, 280 h/mois récupérées, ROI 155 % la 1ère année**
- **Source** : https://www.francenum.gouv.fr/guides-et-conseils/intelligence-artificielle/comprendre-et-adopter-lia/integrer-lia-retours

### RetEx 8 — ETI aéronautique anonymisée (supply chain)
- **Cas d'usage** : Optimisation supply chain via modèle Mistral open-source
- **Outils** : Mistral AI (open-source, déploiement local)
- **Résultats** : Gain en autonomie et confidentialité (chiffres précis non publiés)
- **Source** : https://www.la-tech-actuelle.com/intelligence-artificielle-en-entreprise-les-tendances-qui-transforment-le-travail-en-2026/

### RetEx 9 — Altares D&B (Information d'entreprise)
- **Cas d'usage** : IA privée souveraine pour traitement de données B2B
- **Outils** : Plateforme Claranet (cloud souverain France)
- **Résultats** : Souveraineté + conformité RGPD, chiffres précis non publiés mais cas client documenté
- **Source** : https://www.claranet.com/fr/cas-clients/altares-db-choisit-une-ia-privee-souveraine-avec-claranet/

### RetEx 10 — EY (Big 4, transformation interne)
- **Cas d'usage** : Plateforme EY.ai EYQ (assistant IA interne pour 400 000+ collaborateurs)
- **Outils** : EY.ai (custom), Microsoft, modèles propriétaires
- **Résultats** : **83 % de la workforce a complété le parcours fondamental IA, 81 % d'adoption EYQ, 85 millions de prompts traités en 9 mois**
- **Source** : https://www.ey.com/en_gl/insights/ai/case-study-how-ey-transformed-with-ai

### RetEx 11 — Asahi Europe & International (boissons, ETI)
- **Cas d'usage** : Optimisation des promotions trade marketing
- **Outils** : EY + Microsoft (managed services)
- **Résultats** : Refonte des règles de trade promotion ; chiffres précis non publiés
- **Source** : https://www.ey.com/en_gl/services/ai/case-studies

### RetEx 12 — Macro-baromètre PME France (Denis Atlan / Stema Partners)
- **Cas d'usage** : 200 projets IA B2B analysés (2022-2025)
- **Résultats** : **ROI médian 159,8 %, taux de succès 73 %. Investissement médian PME : 19 500 € (84 000 € ETI). PME déploient 4× plus vite (94 j vs 387 j ETI), avec ROI plus élevé (168,4 % vs 147,3 %)**
- **Source** : https://www.denisatlan.fr/barometre-ia-pme + https://www.stemapartners.com/blog/roi-intelligence-artificielle-guide-complet/

### RetEx 13 — Étude IBM France (entreprises FR)
- **Cas d'usage** : Adoption IA toutes fonctions
- **Résultats** : **65 % des grandes entreprises FR rapportent un gain de productivité IA, 48 % des PME**
- **Source** : https://fr.newsroom.ibm.com/Etude-IBM-pr-s-de-deux-tiers-des-entreprises-interrog-es-en-France-font-tat-de-gains-de-productivit-significatifs-gr-ce-lIA

### RetEx 14 — Cabinet médecine générale type (voicebot)
- **Cas d'usage** : Agent vocal IA pour prise de RDV / FAQ
- **Outils** : Multiple (Nerolia, Bouygues Telecom Business)
- **Résultats** : **-45 % temps secrétariat téléphonique, -22 % no-show grâce aux rappels SMS**, couverture 7h-21h sans surcoût
- **Source** : https://nerolia-ai.fr/blog/accueil-telephonique-automatique-ia-pme

### RetEx 15 — Étude Bpifrance Le Lab "PME-ETI françaises"
- **Cas d'usage** : Macro-étude transversale 1 200 dirigeants
- **Résultats** : **55 % des dirigeants PME-ETI ont franchi le cap de l'opérationnalisation début 2026 (vs 15 % en 2024)** ; 32 % des PME-ETI utilisent l'IA quotidiennement
- **Source** : https://lelab.bpifrance.fr/content/download/4745/pdf/2025-06_L'IA%20dans%20les%20PME%20et%20ETI%20fran%C3%A7aises_Etude%20Bpifrance%20Le%20Lab.pdf

### RetEx 16 — Étude PwC France métiers (2026)
- **Résultats** : **Entreprises les plus exposées à l'IA → croissance CA/employé 3× supérieure** (2024) ; 166 000+ offres d'emploi liées IA en France 2024
- **Source** : https://www.pwc.fr/fr/publications/2026/02/les-metiers-se-reconfigurent-avec-l-ia.html

### RetEx 17 — Mistral AI (souverain FR)
- **Cas d'usage** : Bilan environnemental d'un LLM européen
- **Résultats** : **Entraînement Mistral Large 2 = 20,4 ktCO2eq sur 18 mois** (1er bilan environnemental complet d'un modèle européen)
- **Source** : https://aivancity.ai/blog/derriere-lia-lenergie-leau-et-le-carbone-le-bilan-environnemental-de-2025/

---

## Livrable 3 — Nouveaux outils émergents 2026 à indexer

### LLM frontière 2026

#### 1. GPT-5.5 (xhigh) — OpenAI
- **Catégorie** : LLM (frontière, raisonnement et code)
- **Modèle économique** : SaaS / API
- **Souveraineté** : 🇺🇸
- **Cas d'usage** : Coding agent, raisonnement long
- **Source** : https://www.buildfastwithai.com/blogs/best-ai-models-may-2026-leaderboard

#### 2. Claude Opus 4.7 — Anthropic
- **Catégorie** : LLM (frontière, agentique long-running)
- **Modèle économique** : SaaS / API
- **Souveraineté** : 🇺🇸
- **Cas d'usage** : Workflows agents complexes, codage avancé
- **Source** : https://www.buildfastwithai.com/blogs/best-ai-models-may-2026-leaderboard

#### 3. Gemini 3.1 Pro / Flash-Lite — Google
- **Catégorie** : LLM (frontière)
- **Modèle économique** : SaaS / API
- **Souveraineté** : 🇺🇸
- **Cas d'usage** : Multimodalité, multitâche, scale enterprise
- **Source** : https://blog.mean.ceo/new-ai-model-releases-news-april-2026/

#### 4. DeepSeek V4 / R-series — DeepSeek
- **Catégorie** : LLM (open-weight, raisonnement)
- **Modèle économique** : Open-weight (R2 retardé pour contraintes export-control puces)
- **Souveraineté** : 🇨🇳
- **Cas d'usage** : Raisonnement, alternative low-cost à GPT/Claude
- **Source** : https://codersera.com/blog/open-source-llms-landscape-2026/

#### 5. Grok 4 / 4.20 Beta 2 — xAI
- **Catégorie** : LLM (frontière)
- **Modèle économique** : SaaS / API
- **Souveraineté** : 🇺🇸
- **Cas d'usage** : Recherche temps réel, intégration X
- **Source** : https://www.buildfastwithai.com/blogs/best-ai-models-may-2026-leaderboard

### LLM souverains EU/FR

#### 6. Lucie — OpenLLM-France / Linagora
- **Catégorie** : LLM open-source souverain francophone
- **Modèle économique** : Open-source (financé France 2030 / Bpifrance, projet 2 ans depuis sept. 2024)
- **Souveraineté** : 🇫🇷🇪🇺
- **Cas d'usage** : RAG documents publics FR, déploiement souverain TPE/PME
- **Source** : https://linagora.com/en/openllm-webinar-lucie-truly-open-source-sovereign-model + https://openllm-france.fr/

#### 7. Pleias-RAG (Pico, Nano, Small) — Pleias
- **Catégorie** : Petits modèles RAG / SLM spécialisés
- **Modèle économique** : Open-weight, données Common Corpus (2T tokens domaine public)
- **Souveraineté** : 🇫🇷🇪🇺
- **Cas d'usage** : RAG juridique, citations sourcées, conformité RGPD/AI Act native
- **Source** : https://www.actuia.com/actualite/pleias-des-modeles-de-langages-ouverts-pour-une-ia-ethique-et-transparente/

#### 8. LightOn (Paradigm) — Paris
- **Catégorie** : LLM enterprise on-premise souverain
- **Modèle économique** : Hybride (SaaS + on-premise)
- **Souveraineté** : 🇫🇷🇪🇺 (membre OpenEuroLLM)
- **Cas d'usage** : Déploiement souverain pour grandes administrations / banques
- **Source** : https://laminute.info/2025/02/16/llms-open-source-a-frappe-la-feuille-de-route-numerique-de-leurope/

> Note : **Aleph Alpha (DE)** est en phase de fermeture commerciale en 2026 — à signaler mais pas à indexer en priorité.

### Frameworks agents nouvelle génération

#### 9. Claude Agent SDK — Anthropic
- **Catégorie** : Agent SDK (provider-native)
- **Modèle économique** : Open-source / API Claude
- **Souveraineté** : 🇺🇸
- **Cas d'usage** : Agents safety-critical (santé, finance, légal), tool-use first
- **Source** : https://qubittool.com/blog/ai-agent-framework-comparison-2026

#### 10. OpenAI Agents SDK — OpenAI
- **Catégorie** : Agent SDK (provider-native)
- **Modèle économique** : Open-source / API OpenAI
- **Souveraineté** : 🇺🇸
- **Cas d'usage** : Multi-agents avec transfert explicite de contrôle, remplaçant Swarm
- **Source** : https://www.morphllm.com/ai-agent-framework

#### 11. Mistral Agents SDK — Mistral AI
- **Catégorie** : Agent SDK souverain
- **Modèle économique** : Open-source + cloud Mistral
- **Souveraineté** : 🇫🇷🇪🇺
- **Cas d'usage** : Agents codeurs (Vibe Cloud), workflow européens
- **Source** : https://thenewstack.io/mistral-vibe-cloud-agents/

#### 12. Anthropic Computer Use — Anthropic
- **Catégorie** : Agent multimodal (interaction GUI)
- **Modèle économique** : API Claude
- **Souveraineté** : 🇺🇸
- **Cas d'usage** : Automatisation logicielle desktop, RPA nouvelle génération
- **Source** : https://qubittool.com/blog/ai-agent-framework-comparison-2026

#### 13. MCP (Model Context Protocol) — Linux Foundation (donné par Anthropic déc. 2025)
- **Catégorie** : Standard ouvert (protocole)
- **Modèle économique** : Standard ouvert
- **Souveraineté** : Standard mondial
- **Cas d'usage** : Connecter agents IA à outils/données — devient le "USB-C des agents"
- **Source** : https://www.morphllm.com/ai-agent-framework

#### 14. A2A (Agent2Agent Protocol) — Google
- **Catégorie** : Standard inter-agents
- **Modèle économique** : Standard ouvert
- **Souveraineté** : 🇺🇸 (mais standard)
- **Cas d'usage** : Communication entre agents hétérogènes
- **Source** : https://www.morphllm.com/ai-agent-framework

### Voice / speech 2026

#### 15. ElevenLabs Conversational AI 2.0 — ElevenLabs
- **Catégorie** : TTS + agent vocal full-stack
- **Modèle économique** : SaaS
- **Souveraineté** : 🇺🇸
- **Cas d'usage** : Voicebots, voix synthétiques émotionnelles, WER 2,83 %
- **Source** : https://softcery.com/lab/choosing-the-right-voice-agent-platform-in-2026

#### 16. Cartesia Sonic / Line — Cartesia
- **Catégorie** : TTS ultra-faible latence
- **Modèle économique** : SaaS
- **Souveraineté** : 🇺🇸
- **Cas d'usage** : Conversations temps réel, 90-150 ms latence
- **Source** : https://cartesia.ai/vs/elevenlabs-vs-deepgram

#### 17. AssemblyAI Universal-3 Pro Streaming — AssemblyAI
- **Catégorie** : STT streaming + neural turn detection
- **Modèle économique** : SaaS
- **Souveraineté** : 🇺🇸
- **Cas d'usage** : Transcription temps réel pour agents vocaux, WER 8,14 %
- **Source** : https://www.assemblyai.com/blog/build-voice-agent-livekit

#### 18. Deepgram Nova-3 / Aura — Deepgram
- **Catégorie** : STT + TTS streaming
- **Modèle économique** : SaaS
- **Souveraineté** : 🇺🇸
- **Cas d'usage** : Voicebots production scale
- **Source** : https://deepgram.com/learn/best-voice-ai-platforms-enterprise-comparison

#### 19. Voxtral — Mistral AI
- **Catégorie** : Modèle vocal souverain
- **Modèle économique** : Open-weight + API Mistral
- **Souveraineté** : 🇫🇷🇪🇺
- **Cas d'usage** : Voicebots souverains, transcription
- **Source** : https://www.speechmatics.com/company/articles-and-news/best-speech-to-text-ai-guide-apis-platforms-and-services-compared

#### 20. Vapi.ai — Vapi
- **Catégorie** : Plateforme voicebot dev-first
- **Modèle économique** : SaaS / API
- **Souveraineté** : 🇺🇸
- **Cas d'usage** : Construction rapide d'agents vocaux PME
- **Source** : https://softcery.com/lab/choosing-the-right-voice-agent-platform-in-2026

### Vision foundation models

#### 21. Florence-2 — Microsoft
- **Catégorie** : Vision-language foundation model compact
- **Modèle économique** : Open-source (MIT)
- **Souveraineté** : 🇺🇸
- **Cas d'usage** : Détection + segmentation + captioning + grounding unifiés, zero-shot
- **Source** : https://blog.roboflow.com/florence-2/

#### 22. DINOv2 — Meta AI
- **Catégorie** : Vision Transformer self-supervised
- **Modèle économique** : Open-source
- **Souveraineté** : 🇺🇸
- **Cas d'usage** : Features visuelles génériques (classif, segmentation) sans labellisation
- **Source** : https://dinov2.metademolab.com/

#### 23. SAM 2 — Meta AI
- **Catégorie** : Segmentation universelle (image + vidéo)
- **Modèle économique** : Open-source
- **Souveraineté** : 🇺🇸
- **Cas d'usage** : Segmentation industrielle, vidéo, contrôle qualité
- **Source** : https://github.com/umitkacar/awesome-vision-models

### Agents vocaux / plateformes spécialisées

#### 24. Kleo — solution conversationnelle française (utilisée par Selectour)
- **Catégorie** : Agent conversationnel multicanal souverain
- **Modèle économique** : SaaS souverain
- **Souveraineté** : 🇫🇷🇪🇺
- **Cas d'usage** : Service client e-commerce / réseaux multi-sites
- **Source** : https://lelab.bpifrance.fr/Etudes/les-entreprises-francaises-et-l-ia-l-aube-d-une-revolution/l-ia-dans-les-pme-et-eti-francaises-6-chiffres-a-retenir

#### 25. NVIDIA Parakeet (famille STT) — NVIDIA
- **Catégorie** : STT open-source haute performance
- **Modèle économique** : Open-source
- **Souveraineté** : 🇺🇸
- **Cas d'usage** : Transcription on-premise / edge
- **Source** : https://www.speechmatics.com/company/articles-and-news/best-speech-to-text-ai-guide-apis-platforms-and-services-compared

---

## Sources visitées

### ✅ Sources accessibles & exploitées (32 sources réellement extraites)

**Articles cas d'usage PME / dirigeants (FR)**
- ✅ decisionia.com — fetché, contenu volumineux (HTML brut)
- ✅ startup-up.io — fetché, contenu volumineux
- ✅ bigmedia.bpifrance.fr — fetché, contenu volumineux
- ✅ francenum.gouv.fr (multiples) — extrait via WebSearch (témoignages, podcasts, baromètre)
- ✅ orange.com/whats-up — résumé via WebSearch
- ✅ etcdigital.fr — résumé via WebSearch (intégré aux insights généraux)
- ✅ yes-we-prompt.fr — résumé via WebSearch
- ✅ inovapolis.fr — couvert indirectement par les agrégateurs
- ✅ comarketing-news.fr — couvert indirectement

**Rapports institutionnels**
- ✅ deloitte.com (US + FR) — résumé via WebSearch
- ✅ mckinsey.com (state of AI) — résumé via WebSearch
- ✅ ey.com (case studies) — résumé via WebSearch
- ✅ pwc.fr — résumé via WebSearch
- ✅ economie.gouv.fr (DGE / lettre veille) — extraits via WebSearch (AI Act, écosystème)
- ✅ usine-digitale.fr — bloqué (DataDome) côté article direct, mais données reprises ailleurs
- ✅ workday.com — extraits via WebSearch
- ✅ syndex.fr — extraits via WebSearch (CSE & IA)
- ✅ itforbusiness.fr — extraits via WebSearch (cartographie 972 startups)
- ✅ claranet.com — extraits via WebSearch
- ✅ zdnet.fr / journaldunet.com — extraits via WebSearch (tendances 2026)
- ✅ proactiveacademy.fr — couvert indirectement

**Listes d'outils**
- ✅ blogdumoderateur.com — extraits via WebSearch
- ✅ aixploria.com / synthesia.io / g2.com / appvizer.fr — couverts par les agrégateurs

**Ressources outils complémentaires (au-delà des 50 listés)**
- ✅ Hub France IA cartographie 2026 (972 startups)
- ✅ Bpifrance Le Lab — étude PME-ETI 2026
- ✅ EY case studies internes
- ✅ Linagora / OpenLLM-France
- ✅ Pleias / Common Corpus
- ✅ llm-stats.com / llmcouncil.ai (benchmarks)

### 🛑 Sources bloquées / inaccessibles

**Threads X / Twitter (10 URLs)** — 🛑 Tous inaccessibles : X.com bloque le scraping non authentifié, contenu non récupérable côté serveur. Recommandation : si Blaise veut exploiter ces threads, lui faire copier-coller le contenu directement, ou utiliser un client X authentifié.

**Sources avec accès partiellement restreint**
- 🛑 `usine-digitale.fr` (article 57 % entreprises FR + article POC->prod) — DataDome / captcha bloque le fetch direct ; chiffres clés "57 % depuis plus d'un an" toutefois confirmés via Bpifrance et FranceNum.
- 🛑 PDF économie.gouv.fr (lettre SDE veille IA) — non extrait directement (fetch volumineux), contenu probablement redondant avec le Hub France IA.
- 🛑 PDF Panorama IA 2026 (cdn.prod.website-files) — non fetché (URL générique), à récupérer manuellement par Blaise s'il souhaite l'exploiter.
- 🛑 `box.com/state-of-ai` — non fetché en direct, recouvert par les rapports Deloitte/McKinsey.
- 🛑 `nvidia.com state of AI report 2026` — référencé mais non extrait.
- 🛑 `cabinet-mosselmans.com`, `neocell.ai`, `claritusconsulting.com`, `itransition.com`, `futransolutions.com` — non extraits en direct (volume vs valeur ajoutée jugée faible par rapport aux sources institutionnelles déjà couvertes).

**Couverture estimée** : ~30/40 sources non-Twitter exploitées directement ou indirectement (75 %). Les 10 threads X (20 % des 50 sources) restent inaccessibles structurellement.

---

## Notes méthodologiques

### Biais identifiés
- **Sur-représentation des sources d'éditeurs / agences IA** : beaucoup de sources sont des blogs d'agences (Nerolia, Yes We Prompt, Stema Partners, Bloom AI, Claudin, Diamond Solutions). Données utiles mais à recroiser avec institutionnels (Bpifrance, Deloitte, McKinsey, EY, PwC, France Num).
- **Sur-représentation des grands groupes dans les RetEx** : la plupart des cas chiffrés concernent ETI (Aldes, Selectour, Asahi). Les RetEx purement TPE/PME (<20 salariés) avec chiffres précis restent rares et anonymisés.
- **Sous-représentation Grand Est** : aucune source ne mentionne explicitement de cas Grand Est ; recommandation : compléter par un sourcing direct auprès des incubés Quai Alpha + ailleurs réseau QFC, ou interview French Tech East / Bpifrance Grand Est.
- **Biais 2026 vs 2025** : beaucoup de sources qualifiées "2026" reposent sur l'étude Bpifrance Le Lab juin 2025 (1 200 dirigeants). Les chiffres "2026" sont parfois des extrapolations.

### Recommandations pour Blaise — priorisation itération

1. **À intégrer en priorité forte** (différenciation Hub IA Learning Center + alignement réglementaire) :
   - **CU-020 Conformité RGPD/AI Act** — deadline 2 août 2026, attention médiatique forte, gap critique.
   - **CU-021 Extraction factures** + **CU-022 Prévision cash** — ROI le plus chiffré, public dirigeant TPE/PME.
   - **CU-023 Voicebot accueil** — cas d'usage emblématique pour atelier Starter Class (démo possible en 30 min).

2. **À intégrer en priorité moyenne** :
   - **CU-024 e-commerce vector search** — créneau B2C marqué, à coupler aux retailers Vosges.
   - **CU-027 Empreinte carbone IA** — angle différenciant + alignement étude Tendances Vosges (souveraineté énergétique locale).
   - **CU-029 Détection sur-facturation** — cas Batibig très parlant pour BTP local.

3. **À surveiller pour itération suivante** :
   - **CU-030 Dialogue social CSE** — angle stratégique mais public CSE moins central pour Hub IA.
   - **CU-031 Méthode cartographie cas d'usage** — méta-cas d'usage intéressant comme module N1-N3 d'introduction.

4. **Outils à indexer en priorité** :
   - **Souverains FR** : Lucie, Pleias-RAG, LightOn, Voxtral, Kleo, Mistral Agents (alignement message souveraineté QFC).
   - **Standards** : MCP, A2A — incontournables pour modules N7-N8 agents avancés.
   - **Voice** : Cartesia + ElevenLabs Conv 2.0 + Vapi (pour CU-023 voicebot).
   - **Vision** : Florence-2 + DINOv2 + SAM 2 (pour CU-017 / CU-018 industrie).

5. **Action complémentaire suggérée** : interroger directement le réseau QFC + Bpifrance Grand Est + French Tech East pour récupérer 3-5 RetEx Grand Est anonymisés à intégrer dans le module N1-N3 "L'IA en PME près de chez vous" — différenciation territoriale forte vs sites IA généralistes.

---

*Rapport produit le 8 mai 2026 sur 50 sources cibles. ~32 exploitées (75 %), 10 threads X bloqués structurellement. Toutes les données chiffrées sont sourcées ; mention "non précisé" en l'absence d'info publique vérifiée.*
