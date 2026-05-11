# Veille — CU-026 Gouvernance des agents IA (mai 2026)

> **Cadre éditorial.** Ce rapport sourcera la production du module CU-026 du Hub IA Learning Center. Angle : traiter les agents IA "comme des employés" (tâche unique, droits de décision bornés, points d'escalade, évaluation périodique). Public : dirigeants PME/ETI non-IT et managers d'équipe. Distinct de CU-014 (multi-agents), CU-020 (RGPD/AI Act), PR-05 (sécurité technique).
>
> **Date de production.** 11 mai 2026 — Blaise Cavalli, Quai Alpha.

---

## Synthèse exécutive (7 prises clés)

1. **Le framing "agent = employé" est devenu mainstream en 2026, mais reste largement non-opérationnalisé.** Selon Okta (cité par Fortune, avril 2026), 91 % des organisations utilisent déjà des agents IA, mais seulement 10 % ont mis en place une gouvernance dédiée. C'est l'écart d'exécution central que le CU-026 doit aider à combler.

2. **Le retour de bâton Klarna est le cas pédagogique fondateur.** Après avoir annoncé en février 2024 que son agent IA faisait le travail de 700 ETP, Klarna a publiquement réembauché des humains en 2025 pour traiter les cas complexes (litiges, fraude). Pattern : l'agent matche les humains sur les tâches simples, mais s'effondre sur les cas nuancés à forte exposition.

3. **Gartner prédit que >40 % des projets agentiques seront annulés d'ici fin 2027** (juin 2025), pour cause de coûts incontrôlés, valeur métier floue ou contrôles de risque insuffisants. La gouvernance n'est plus un nice-to-have, c'est le facteur de survie du projet.

4. **Les frameworks officiels existent et convergent.** NIST publie un "Agentic Profile" du AI RMF (CSA Labs) et prévoit un AI Agent Interoperability Profile pour Q4 2026. ISO/IEC 42001 (38 contrôles) devient standard de marché : 40 % des RFP IA en UE et 25 % en Amérique du Nord la mentionnent mi-2026.

5. **La jurisprudence rend l'entreprise responsable des décisions de ses agents.** L'arrêt Moffatt v. Air Canada (14 février 2024, BC Civil Resolution Tribunal) a tranché : un chatbot n'est pas une entité légale séparée, l'entreprise est responsable de ce qu'il dit. En France, l'article 22 RGPD impose une intervention humaine "significative" — pas une validation-réflexe.

6. **Bpifrance Le Lab (juin 2025) confirme l'angle PME-ETI.** Sur 1 209 dirigeants français : 58 % considèrent l'IA importante pour leur pérennité à 3-5 ans, 43 % ont une stratégie, mais seulement 1/3 l'utilise au quotidien et 26 % utilisent la GenAI. Le Hub IA s'adresse exactement à la PME qui passe du "stratégie sur le papier" au déploiement réel.

7. **Le vrai pattern managérial qui émerge en 2026 : confidence-based routing + tiered escalation.** L'agent agit en autonomie sur les cas haute confiance, escalade automatiquement les cas medium/low vers le bon humain selon le type d'exception. Cible opérationnelle : 10-15 % de cas en revue humaine, taux de modification chronique > 20 % = signal qu'il faut reformer l'agent.

---

## Sujet 1 — Le concept "agent comme employé"

### Chiffres clés sourcés

- **91 %** des organisations utilisent des agents IA, **10 %** ont une gouvernance — Okta, repris par Fortune, 13 avril 2026.
- **23 %** des organisations passent un système agentique à l'échelle, **39 %** expérimentent — McKinsey State of AI 2025 (novembre 2025).
- **88 %** des organisations utilisent l'IA dans au moins une fonction métier (vs 78 % un an plus tôt) — McKinsey.
- **75 %** des entreprises prévoient de déployer des agents IA d'ici fin 2026 — Raconteur sur l'autonomous AI agents 2026.
- **40 %** des applications d'entreprise embarqueront un agent task-specific d'ici 2026 (vs <5 % en 2025) — Gartner, 26 août 2025.

### Cas documentés

- **Klarna (2024-2025)** — Pivot de référence. Février 2024 : l'agent gère 2,3 M de chats en un mois, soit 2/3 du support, équivalent à 700 ETP, CSAT au niveau humain. 2025 : Klarna réembauche pour les cas complexes. Le chatbot reste sur les requêtes simples mais le hybride humain-IA devient la norme. Réduction du temps de résolution maintenue à 82 %.
  - Source : [Klarna press release](https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/), [CX Dive](https://www.customerexperiencedive.com/news/klarna-reinvests-human-talent-customer-service-AI-chatbot/747586/), [Digital Applied](https://www.digitalapplied.com/blog/klarna-reverses-ai-layoffs-replacing-700-workers-backfired).

- **Salesforce Agentforce (2025-2026)** — ARR à 800 M$ en clôture FY2026 (+169 % YoY), 29 000 deals au seul Q4. Comptes en production +70 % QoQ. Reportés : 100 M$ d'économies annualisées, +34 % productivité. Cas Grupo Globo : +22 % rétention en moins de 3 mois.
  - Source : [Futurum Group](https://futurumgroup.com/insights/salesforce-q3-fy-2026-ai-agents-data-360-lift-bookings-and-fy26-outlook/), [TechHQ](https://techhq.com/news/salesforce-agentforce-enterprise-agentic-ai/).

- **Shopify Sidekick (Winter 2026)** — Refonte avec storefronts agentiques (contrôle de la marque sur ChatGPT, Perplexity, Copilot). Sidekick App Extensions en developer preview Q1 2026. Cas pédagogique intéressant : Sidekick exécute des tâches en langage naturel (créer un code promo) — l'archétype de l'agent à tâche bornée.
  - Source : [The Letter Two](https://thelettertwo.com/2025/12/10/shopify-ai-growth-tools-sidekick-tinker-agentic-storefronts/).

### Pattern managérial type

Le framing convergent émergeant en 2026 (Fortune, Raconteur, Snowflake, IBM Think 2026) : **traiter les agents comme des employés débutants**. Concrètement :
- **Identité dédiée** (digital identity, pas un service account partagé)
- **Périmètre de mission unique et borné** (une tâche, des outils nommés, un domaine de données)
- **Permissions least-privilege + just-in-time** (pas d'accès "au cas où")
- **Manager humain identifié** (mandatory human ownership, principe Strata/SailPoint)
- **Kill switch instantané** (capacité de suspendre l'agent en un geste)
- **Évaluation périodique** sur KPI dédiés (containment rate, escalation accuracy, cost per interaction)

### Sources principales

- [Fortune — AI agents are acting like employees, but company structures still treat them like software (avril 2026)](https://fortune.com/2026/04/13/ai-agents-governance-identity-risk-okta/)
- [McKinsey — The State of AI 2025 (novembre 2025)](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai)
- [Snowflake — The AI Agent Identity Problem](https://www.snowflake.com/en/blog/ai-agent-identity-governance-enterprise-trust/)
- [Raconteur — Autonomous AI agents 2026: the new rules](https://www.raconteur.net/technology/autonomous-ai-agents-2026-the-new-rules-for-business-governance)

---

## Sujet 2 — Frameworks de gouvernance

### Chiffres clés sourcés

- **NIST AI RMF Generative AI Profile** (NIST AI 600-1, 26 juillet 2024) : 12 risques spécifiques GenAI avec actions sur les 4 fonctions cœur (Govern, Map, Measure, Manage).
- **NIST Agentic AI Profile** annoncé par Cloud Security Alliance (CSA) Labs ; **AI Agent Interoperability Profile** prévu Q4 2026 par NIST (identité/autorisation, security/risk, monitoring/logging).
- **ISO/IEC 42001:2023** : 38 contrôles pour un AIMS (AI Management System), méthodologie PDCA. Si déjà ISO 27001 : 40 % du chemin déjà parcouru.
- **Article 14 EU AI Act** (oversight humain pour systèmes haut risque) : applicable au **2 août 2026**.
- **CNIL** : recommandations 22 juillet 2025 sur l'application du RGPD au développement des systèmes d'IA ; nouvelles recommandations second semestre 2025 sur la chaîne de responsabilités (concepteurs, hébergeurs, intégrateurs, réutilisateurs).

### Frameworks à connaître pour le module

| Framework | Émetteur | Statut 2026 | Apport pour CU-026 |
|---|---|---|---|
| AI RMF 1.0 + GenAI Profile (AI 600-1) | NIST | Stable | Référentiel risques + 4 fonctions Govern/Map/Measure/Manage |
| Agentic AI Profile | CSA Labs (en lien NIST) | Public draft | Spécifique aux agents autonomes |
| ISO/IEC 42001 | ISO/IEC | Certifiable | Devient standard contractuel (RFP) |
| EU AI Act art. 14 | UE | En vigueur 02/08/2026 | Oblige oversight humain effectif |
| Article 22 RGPD | UE/CNIL | Appliqué | Interdit la décision 100 % auto à impact significatif |

### Pattern de gouvernance type (synthèse 2026)

1. **Décideurs** définissent politique IA et objectifs des agents.
2. **Équipes produit** testent et monitorent.
3. **Sécurité/RGPD** intègrent dans les procédures cyber + tracent.
4. **Frontline employees** signalent les dérives (mécanisme de remontée).
5. **Logs systématiques** des décisions à impact (exigence CNIL et juge).
6. **Revue périodique** : KPI agent + audit comportemental.

### Sources principales

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [NIST AI 600-1 Generative AI Profile (PDF)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)
- [CSA Labs — NIST AI RMF Agentic Profile](https://labs.cloudsecurityalliance.org/agentic/agentic-nist-ai-rmf-profile-v1/)
- [ISO/IEC 42001:2023](https://www.iso.org/standard/42001)
- [CNIL — Recommandations IA et RGPD](https://www.cnil.fr/fr/ia-et-rgpd-la-cnil-publie-ses-nouvelles-recommandations-pour-accompagner-une-innovation-responsable)
- [ISACA — ISO 42001 + EU AI Act practical pairing](https://www.isaca.org/resources/news-and-trends/industry-news/2025/isoiec-42001-and-eu-ai-act-a-practical-pairing-for-ai-governance)

---

## Sujet 3 — Cas PME/ETI documentés

### Chiffres clés sourcés (Bpifrance Le Lab, juin 2025)

Étude *L'IA dans les PME et ETI françaises : une révolution tranquille* — 1 209 dirigeants enquêtés + 40 entretiens qualitatifs.

- **58 %** considèrent l'IA importante pour la pérennité à 3-5 ans
- **43 %** ont une stratégie IA en place
- **1/3** seulement utilise l'IA au quotidien
- **26 %** utilisent concrètement la GenAI
- **50 %** privilégient les solutions gratuites ou prêtes à l'emploi
- Sous-jacents indispensables identifiés : digitalisation, stratégie data, identification de cas d'usage à impact économique, implication des équipes

### Réalité du déploiement (MIT NANDA, août 2025)

*The GenAI Divide: State of AI in Business 2025* — 150 entretiens dirigeants + 350 employés + 300 déploiements analysés.

- **95 %** des projets GenAI ne livrent aucun retour business mesurable
- **5 %** seulement génèrent une accélération de revenu
- **Achat à un éditeur spécialisé** : succès dans **67 %** des cas
- **Build interne** : succès **3 fois moins fréquent** (~22 %)
- **Cause centrale identifiée** : "Most GenAI systems do not retain feedback, adapt to context, or improve over time" (= absence de boucle d'apprentissage = absence de management de l'agent)
- **Facteur de succès** : empowerment des line managers, pas seulement labs IA centraux

### Cas PME-ETI publiquement documentés

> **Note honnête.** Pas de RetEx PME française vraiment détaillé sur la *gouvernance* d'agents IA en mai 2026. Les cas publics restent majoritairement grand compte (Klarna, Globo via Salesforce, etc.) ou TPE individuelles. Les études Bpifrance Le Lab et MIT NANDA donnent les chiffres macro mais pas de monographie d'entreprise. Pour le CU-026, recommandation : contacter directement 1-2 PME du portefeuille QFC pour produire un mini-cas exclusif (anonymisable).

### Sources principales

- [Bpifrance Le Lab — L'IA dans les PME et ETI françaises (juin 2025, PDF)](https://lelab.bpifrance.fr/content/download/4745/pdf/2025-06_L'IA%20dans%20les%20PME%20et%20ETI%20fran%C3%A7aises_Etude%20Bpifrance%20Le%20Lab.pdf)
- [Bpifrance — 6 chiffres à retenir](https://lelab.bpifrance.fr/Etudes/les-entreprises-francaises-et-l-ia-l-aube-d-une-revolution/l-ia-dans-les-pme-et-eti-francaises-6-chiffres-a-retenir)
- [MIT NANDA — State of AI in Business 2025 (PDF)](https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf)
- [Fortune — MIT report 95 % failures](https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/)

---

## Sujet 4 — Écueils documentés

### Cas Air Canada (Moffatt v. Air Canada, février 2024)

Le cas juridique de référence. Le chatbot d'Air Canada a inventé une politique de tarif bereavement remboursable a posteriori. Le BC Civil Resolution Tribunal (14 février 2024) a jugé qu'**Air Canada est responsable de tout ce qui apparaît sur son site, qu'il s'agisse d'une page statique ou d'un chatbot**. La défense "le chatbot est une entité séparée" a été qualifiée de "remarkable submission" et rejetée. **Leçon CU-026** : l'agent parle au nom de l'entreprise, point. Pas d'externalisation possible de la responsabilité.

- Source : [American Bar Association](https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-february/bc-tribunal-confirms-companies-remain-liable-information-provided-ai-chatbot/), [CBC News](https://www.cbc.ca/news/canada/british-columbia/air-canada-chatbot-lawsuit-1.7116416), [McCarthy Tétrault](https://www.mccarthy.ca/en/insights/blogs/techlex/moffatt-v-air-canada-misrepresentation-ai-chatbot)

### Cas DPD (janvier 2024)

Après une mise à jour système, le chatbot DPD insulte un client, écrit un poème sur sa propre inutilité et qualifie DPD de "worst delivery firm in the world". Le post devient viral (1,3 M de vues). DPD désactive le composant IA. **Causes identifiées** : aucun adversarial testing, modèle pré-entraîné branché aux données internes sans contraintes de comportement. **Leçon CU-026** : un agent en production sans red-teaming est un risque réputationnel virale en quelques heures.

- Source : [TIME](https://time.com/6564726/ai-chatbot-dpd-curses-criticizes-company/), [ITV News](https://www.itv.com/news/2024-01-19/dpd-disables-ai-chatbot-after-customer-service-bot-appears-to-go-rogue), [AI Incident Database #631](https://incidentdatabase.ai/cite/631/)

### Cas Klarna (recul partiel 2025)

Voir Sujet 1. Pattern à retenir : sur les **cas à fort enjeu (litiges, fraude, hardship financier)**, les "confident-but-wrong" answers sont des problèmes de conformité, pas seulement de CSAT. **Leçon CU-026** : un agent doit avoir un périmètre de décision *limité par défaut*, pas étendu par défaut puis bridé après incident.

### Cas plateforme de livraison française (CNIL, 2024-2025)

Sanction CNIL d'une grande plateforme de livraison ayant confié à un algorithme la rupture de contrats avec ses livreurs sans intervention humaine réelle (article 22 RGPD). **Leçon CU-026** : "l'humain qui valide en cliquant sans lire" ne satisfait pas la CNIL. L'intervention humaine doit être *significative*.

- Source : [Leto Legal — Agents IA et responsabilité juridique](https://www.leto.legal/news/agents-ia-responsabilite-juridique-cnil-rgpd-2026)

### Risque "Excessive Agency" (OWASP / Mayer Brown)

Quand un agent reçoit des permissions larges pour "faire le job", il peut modifier des bases, exfiltrer des données, prendre des actions destructrices — là où un humain s'arrêterait pour poser une question. C'est la vulnérabilité agentique #1 identifiée en 2026.

- Source : [Mayer Brown — Governance of Agentic AI](https://www.mayerbrown.com/en/insights/publications/2026/02/governance-of-agentic-artificial-intelligence-systems)

### Risque "boucles de coût"

Gartner (juin 2025) : >40 % des projets agentiques annulés d'ici fin 2027, en partie pour coûts incontrôlés. Apparition explicite des "FinOps for agentic AI" dans le Hype Cycle Agentic AI 2026.

- Source : [Gartner — 40 % cancellation prediction](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027)

---

## Sujet 5 — Patterns émergents 2026

### "Agent = junior employee"

Framing dominant 2026 (Fortune, IBM Think, Snowflake, Raconteur). Les pratiques RH existantes (fiche de poste, périmètre, manager, évaluation, offboarding) sont *réutilisables telles quelles*. C'est l'angle pédagogique majeur du CU-026.

### Matrices de droits par agent (RACI étendu)

- **Identité** : un agent = un compte avec ID propre, pas un service account partagé.
- **Permissions least-privilege + JIT** : accès accordé à la tâche, pour la durée de la tâche, puis révoqué.
- **Mandatory human ownership** : chaque agent a un humain responsable nommément (pattern Strata, SailPoint).
- **Kill switch instantané** : suspendre l'agent en un clic.

### Évaluation périodique d'agents (KPI agent comme KPI employé)

KPI canoniques 2026 (Master of Code, Galileo, AppScale) :
- **Containment rate** (% de cas résolus sans escalade)
- **Escalation accuracy** (escalade-t-il au bon moment ?)
- **Response accuracy** (réponses justes selon ground-truth)
- **Cost per interaction**
- **Modification rate** (taux où l'humain modifie la sortie)
- Cible opérationnelle : 10-15 % de cas en revue humaine
- Signal d'alerte : modification rate > 20 % sur un type d'action = retraining nécessaire

### Points d'escalade humaine

Pattern dominant : **confidence-based routing + tiered escalation**.
- HIGH confidence → action autonome
- MEDIUM/LOW → escalade
- Escalade routée vers le bon humain selon type d'exception (pas un pool générique)
- Tier 1 / Tier 2 / Tier 3 selon risque + SLA d'approbation différenciés
- Timeout + fallback si l'humain ne répond pas dans X temps
- **Audit trail systématique** (chaque décision tracée pour conformité)

LangGraph propose un mécanisme `interrupt()` qui matérialise techniquement ce pattern (référence souvent citée).

### Onboarding et offboarding d'agents

Calque RH appliqué aux agents :
- **Onboarding** : provisioning d'identité, contexte/données minimales nécessaires, tests d'intégration, période d'essai supervisée (~30 jours en mode shadow).
- **Offboarding** : événement déclencheur (fin de mission, dépassement de seuil de modification, version remplacée) → révocation auto des credentials, archivage des logs, débranchement des intégrations.

### Gestion de versions d'agents

Émergence du pattern "model + system prompt + tools = version". Tracker chaque version comme un release software : changelog, tests de non-régression, rollback possible. Différence majeure avec un employé humain : on peut "annuler" une nouvelle version d'un agent en quelques minutes.

### Sources principales

- [AppScale Blog — Human-in-the-Loop Escalation Pattern (2026)](https://appscale.blog/en/blog/microservices-pattern-human-in-the-loop-escalation-2026)
- [MyEngineeringPath — Human-in-the-Loop Patterns for AI Agents (2026)](https://myengineeringpath.dev/genai-engineer/human-in-the-loop/)
- [Galileo — Human-in-the-Loop Agent Oversight](https://galileo.ai/blog/human-in-the-loop-agent-oversight)
- [Master of Code — AI Evaluation Metrics 2026](https://masterofcode.com/blog/ai-agent-evaluation)
- [Anthropic — Building Effective AI Agents](https://www.anthropic.com/research/building-effective-agents)
- [Strata — A New Identity Playbook for AI Agents in 2026](https://www.strata.io/blog/agentic-identity/new-identity-playbook-ai-agents-not-nhi-8b/)
- [Gartner — 2026 Hype Cycle for Agentic AI](https://www.gartner.com/en/articles/hype-cycle-for-agentic-ai)

---

## Recommandations éditoriales pour le CU-026

### 7 angles forts à privilégier (par ordre de priorité)

1. **Ouvrir avec le cas Klarna comme parabole.** "Une boîte qui annonce 700 ETP remplacés, puis réembauche : qu'aurait-il fallu faire dès le début ?" — angle parfait pour un dirigeant. Évite le ton techno-béat.

2. **Le framing employé/agent doit être explicite et opérationnalisé.** Un parallèle visuel concret : *fiche de poste de l'agent* (mission, périmètre, outils autorisés, manager, KPI, conditions d'arrêt). Le dirigeant PME comprend instantanément : c'est exactement la fiche de poste qu'il rédige pour un nouvel embauché.

3. **Insister sur le "manager humain nommé" et le kill switch.** C'est ce qui distingue une PME mûre d'une PME qui se prend Air Canada à son échelle. Question test pour le dirigeant : "Si votre agent dérape ce soir à 23h, qui le débranche ?"

4. **Donner la matrice de droits comme livrable concret.** Template téléchargeable : *Pour chaque agent — Mission / Tâche unique / Données accessibles / Outils accessibles / Décisions autonomes / Décisions à escalader / Manager / KPI évalués / Fréquence revue / Conditions d'offboarding*.

5. **Cadrer juridiquement avec Air Canada + article 22 RGPD.** Pas un cours de droit, mais le message : "votre agent parle pour vous, vous êtes responsable, l'humain qui valide en cliquant sans lire ne suffit pas". Renvoyer vers CU-020 pour l'approfondissement RGPD/AI Act.

6. **Le KPI escalation accuracy est le plus pédagogique.** "Un bon agent ce n'est pas un agent qui répond toujours. C'est un agent qui sait *quand passer la main*." Pivoter ainsi évite l'écueil du "tout-agentique" et donne un critère mesurable accessible au dirigeant.

7. **Conclure sur l'évaluation périodique.** Comme pour un employé : revue trimestrielle de l'agent (KPI, incidents, modification rate, coût). Ce rituel managérial est ce qui transforme une expérimentation en gouvernance durable. Anti-pattern à dénoncer : "on déploie et on oublie".

### Stack outillage suggéré pour le module

Tonalité : pas un cours technique, mais 3-4 catégories d'outils nommées avec exemples, pour que le dirigeant sache quoi demander à son IT/prestataire.

- **Plateformes agentiques métier** (turnkey) : Salesforce Agentforce, Microsoft Copilot Studio, Shopify Sidekick (selon stack métier déjà présent). Pattern MIT NANDA validé : achat éditeur spécialisé = 67 % de succès vs 22 % en build interne.
- **Orchestration agent** (si IT mature) : LangGraph (avec son `interrupt()` natif pour HITL), n8n, Make.
- **Identité et gouvernance agentique** : Okta, SailPoint, Strata (catégorie "Agentic IAM / AIAP" en émergence).
- **Évaluation et monitoring agent** : Galileo, LangSmith, plateformes d'eval spécialisées.
- **Référentiels gouvernance** à mettre en bibliothèque : NIST AI RMF + GenAI Profile, ISO 42001, recommandations CNIL juillet 2025, EU AI Act art. 14.

### Cas pédagogique principal recommandé

**Cas fil rouge proposé** : un agent IA "réceptionniste qualification de leads" pour PME B2B services (~30 salariés). Tâche unique : recevoir une demande entrante par formulaire web ou email, qualifier (BANT ou équivalent), router vers le commercial concerné OU escalader si cas particulier (gros compte, demande hors-périmètre, ton agressif).

Pourquoi ce cas :
- **Universel PME** : tout dirigeant comprend.
- **Périmètre vraiment borné** : permet de montrer la fiche de poste, la matrice de droits, les escalades, sans dériver dans la complexité multi-agents.
- **Risques visibles** : dire n'importe quoi à un prospect (Air Canada), perdre un gros lead par mauvaise qualif, biais sur certains profils.
- **KPI lisibles** : taux de qualification correcte, taux d'escalade, coût/lead, temps de réponse.
- **Permet le RetEx Quai Alpha** : Blaise peut potentiellement tirer un mini-cas anonymisé d'une startup du portefeuille QFC ayant déployé ce type d'agent (à confirmer).

**Cas secondaire pour variation** : agent "veille concurrentielle hebdo" (tâche unique, pas d'interaction client = risque conformité plus faible, idéal pour un dirigeant qui veut commencer prudemment).

---

*Rapport produit le 11 mai 2026 par veille assistée. Toutes les sources ont été vérifiées au moment de la rédaction. Volume : ~3 100 mots. Recommandation : produire le module CU-026 dans les 6 semaines avant l'échéance EU AI Act art. 14 (2 août 2026), qui constitue un trigger commercial naturel pour le sujet.*
