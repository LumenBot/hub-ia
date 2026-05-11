# CU-026 — Gouvernance des agents IA

**Public cible** : dirigeant PME/ETI + manager d'équipe qui doit « manager » des agents IA comme on manage des humains.

---

## Métadonnées (pour Claude Code)

- **Section** : Modules CU
- **Niveau** : ⭐⭐⭐ Avancé
- **Type** : Étude de cas + framework opérationnel + auto-diagnostic
- **Durée lecture** : 25 min
- **Emoji h1** : 🪪
- **Axe métier** : `axe-b` (Décision) avec `axe-secondaire="agentique"`
- **Filière** : `transverse`
- **Agentique** : `true`
- **Titre métier visible** : « Gouvernance des agents IA »
- **Sous-titre hero** : « 91 % des organisations utilisent des agents IA. 10 % seulement ont une gouvernance dédiée. Traiter les agents comme des employés débutants : tâche bornée, droits explicites, escalade documentée, évaluation périodique. Le pattern managérial qui sépare les 5 % qui réussissent des 95 % qui échouent. »
- **Card index** :
  - Emoji : 🪪
  - Titre : « Gouvernance des agents IA »
  - Sous-titre : « Manager un agent IA comme un employé débutant. 7 dimensions à formaliser, l'auto-diagnostic, et le cas Klarna comme leçon. »
  - Type : « Étude de cas + framework + auto-diagnostic »
  - Niveau : ⭐⭐⭐ Avancé · 25 min

## Synthèse exécutive

### Pourquoi cette page ?

Tu as déployé (ou tu envisages de déployer) un agent IA en production : assistant client, agent commercial, automatisation de tâches récurrentes. **Le défi n'est plus de construire l'agent — c'est de le gouverner.** Selon Okta (Fortune, avril 2026), **91 % des organisations utilisent déjà des agents IA, mais seulement 10 % ont mis en place une gouvernance dédiée**. Gartner prévoit que **plus de 40 % des projets agentic seront annulés d'ici fin 2027** pour cause de coûts incontrôlés, valeur métier floue, ou contrôles de risque insuffisants.

Le framing managérial qui s'impose en 2026 : **traiter l'agent IA comme un employé débutant**. Mission unique et bornée, droits de décision explicites, points d'escalade documentés, évaluation périodique. Cette page te donne le framework opérationnel, le cas Klarna comme leçon fondatrice, et un auto-diagnostic interactif pour positionner ta propre gouvernance.

### 4 takeaways

1. **L'écart entre usage et gouvernance est aujourd'hui béant.** 91 % des organisations utilisent des agents IA, 10 % seulement ont une gouvernance dédiée (Okta, avril 2026). Gartner prévoit que plus de 40 % des projets agentic seront annulés d'ici fin 2027. La gouvernance n'est plus un nice-to-have, c'est le facteur de survie du projet.

2. **Le cas Klarna est la leçon fondatrice.** Février 2024 : Klarna annonce que son agent IA fait le travail de 700 ETP (gestion 2,3 millions de chats/mois, CSAT au niveau humain). 2025 : Klarna réembauche publiquement des humains pour traiter les cas complexes. **Pattern documenté** : l'agent matche les humains sur les tâches simples, mais s'effondre sur les cas nuancés à forte exposition.

3. **Le pattern « agent = employé » est le bon framing 2026.** Identité dédiée (pas un service account partagé), périmètre de mission unique et borné, permissions least-privilege + just-in-time, manager humain identifié, kill switch instantané, évaluation périodique sur KPI agent (containment rate, escalation accuracy, cost per interaction). Sept dimensions à formaliser pour chaque agent en production.

4. **La jurisprudence rend l'entreprise responsable des décisions de ses agents.** L'arrêt Moffatt v. Air Canada (BC Civil Resolution Tribunal, février 2024) a tranché : un chatbot n'est pas une entité légale séparée, l'entreprise est responsable de ce qu'il dit. En France, l'article 22 RGPD impose une intervention humaine « significative ». L'AI Act (article 14) exige une supervision humaine effective sur les systèmes haut-risque dès le 2 août 2026.

### Stats (3-4)

- **91 % vs 10 %** : organisations utilisant des agents IA vs organisations ayant une gouvernance dédiée (Okta, Fortune, avril 2026)
- **>40 %** des projets agentic seront annulés d'ici fin 2027 pour cause de coûts/valeur/risque (Gartner, juin 2025)
- **23 %** des organisations passent un système agentique à l'échelle, 39 % expérimentent (McKinsey State of AI 2025, novembre 2025)
- **40 %** des RFP IA en UE (25 % en Amérique du Nord) mentionnent ISO/IEC 42001 mi-2026 (devient standard contractuel)

### Quand cette page est utile

Tu as déployé un agent IA en production (chatbot, agent commercial, automatisation), ou tu t'apprêtes à le faire. Tu te poses des questions sur **qui est responsable si l'agent fait une erreur**, **comment évaluer sa performance**, **quand l'agent doit escalader à un humain**, **comment l'auditer**. Tu cherches un framework opérationnel et applicable en PME, pas une doctrine théorique.

## Section 1 — Le shift de framing 2026 — l'agent comme employé

### 1.1 Pourquoi le framing techno-centré ne suffit plus

Jusqu'en 2025, le discours dominant sur les agents IA était **techno-centré** : « comment construire ? quelle architecture ? quel framework (LangGraph, CrewAI, Hermes Agent) ? quel modèle backend ? ». Cette vision était nécessaire pour démarrer, elle ne suffit plus en production.

**Le constat 2026** : les organisations qui réussissent leurs déploiements d'agents IA ont en commun un changement de posture. Elles ne pilotent pas leurs agents comme des logiciels. Elles les pilotent **comme des employés débutants** :
- À qui on confie une mission claire
- À qui on accorde des droits limités au démarrage, élargis avec la confiance
- Qu'on briefe avec des exemples et des contre-exemples
- Qu'on supervise et qu'on évalue
- Qu'on peut « licencier » (désactiver, archiver) si nécessaire

### 1.2 Trois raisons documentées qui font fonctionner ce framing

1. **Il rend la gouvernance lisible pour les non-IT.** Un dirigeant non-technique comprend immédiatement « cet agent fait le travail d'un junior commercial » plutôt que « ce système est un graphe LangGraph avec des nœuds tool-call asynchrones ». La conversation devient possible avec les RH, les juristes, les opérationnels.

2. **Il force la discipline managériale.** Si tu traites un agent comme un employé, tu dois lui définir un périmètre, des objectifs, des KPI. Cela évite le « projet IA flou » qui finit en abandon dans 40 % des cas (Gartner, 2025).

3. **Il prépare la conformité réglementaire.** L'AI Act exige une supervision humaine effective (article 14, applicable au 2 août 2026 sur les systèmes haut-risque). L'article 22 RGPD impose qu'une décision significative ne soit pas 100 % automatisée. Le pattern « agent = employé » colle naturellement à ces obligations.

### 1.3 Ce que ça veut dire concrètement

Le framing « agent = employé » se traduit en **7 dimensions à formaliser pour chaque agent en production**. C'est l'objet de la section 3 de ce module.

## Section 2 — La leçon Klarna — étude de cas fondatrice

### 2.1 Février 2024 — l'annonce qui a marqué le marché

En février 2024, Klarna (fintech suédoise spécialisée dans le « buy now, pay later ») publie un communiqué qui fait le tour du monde : son agent IA déployé en partenariat avec OpenAI gère désormais **deux tiers du support client**, soit **2,3 millions de conversations en un mois**, équivalent au travail de **700 ETP**, avec un score de satisfaction client (CSAT) **au niveau des agents humains**. Klarna chiffre le gain à 40 millions de dollars par an.

Le récit séduit : voici la preuve que l'IA peut remplacer massivement le support client humain. Le marché s'enflamme.

### 2.2 2025 — le retour de bâton

En 2025, Klarna communique discrètement un changement de stratégie : l'entreprise **réembauche publiquement des humains** pour le service client. Le chatbot reste actif sur les requêtes simples (recherche de commande, modification d'adresse, questions FAQ), mais les cas complexes — litiges, soupçons de fraude, négociations commerciales, situations émotionnelles — sont **systématiquement réorientés vers des humains**.

Le PDG Sebastian Siemiatkowski explique le revirement : la dégradation de la qualité sur les cas nuancés a affecté la réputation de la marque, et le coût caché (clients mécontents qui partent, contentieux qui gonflent) a finalement dépassé les économies réalisées.

**Bilan factuel** : le temps moyen de résolution reste réduit de 82 % vs avant l'agent. Mais le pattern de déploiement a changé : l'agent ne remplace plus, il **assiste et trie**, et l'humain reprend la main sur les cas à forte exposition.

### 2.3 Les 4 leçons fondatrices du cas Klarna

1. **L'agent matche les humains sur les tâches simples, s'effondre sur les cas nuancés.** Le test de production révèle un seuil de complexité au-delà duquel la performance s'effondre, alors que les benchmarks initiaux étaient impressionnants. Sans gouvernance qui anticipe ce seuil (par escalade automatique), tu paies en réputation.

2. **Le coût caché de l'erreur d'un agent est asymétrique.** Sur 100 tickets traités correctement, l'agent te fait gagner du temps. Sur 1 ticket traité catastrophiquement (insulte client, mauvaise information juridique, traitement inéquitable), tu perds en réputation, en contentieux, en confiance. La balance n'est pas linéaire.

3. **Le « 700 ETP remplacés » était une vanity metric.** Le bon KPI n'est pas « combien d'humains ai-je remplacés », c'est « quel est le gain net (économies − coûts cachés) sur 12 mois ». Klarna a appris la leçon publiquement.

4. **Le retour en arrière est honorable.** Klarna a communiqué ouvertement sur son revirement. C'est devenu un cas pédagogique de référence en 2026, plutôt qu'un échec caché. La transparence sur les ajustements protège la crédibilité long terme.

### 2.4 Ce que tu retiens en tant que dirigeant

Avant tout déploiement d'agent IA en production, **anticipe le seuil de complexité au-delà duquel l'agent doit escalader**. Définis les KPI de coût net (pas seulement les économies brutes). Prévois un mécanisme de retour en arrière sans perte de face. Le cas Klarna n'est pas un cas d'échec — c'est un cas de gouvernance ajustée en cours de route, ce qui est précisément ce que demande la production.

## Section 3 — Le framework opérationnel — 7 dimensions à formaliser par agent

Pour chaque agent en production, formaliser ces 7 dimensions. C'est ton **contrat agent ↔ entreprise**, l'équivalent d'une fiche de poste.

| # | Dimension | Question à formaliser |
|---|---|---|
| 1 | **Tâche** | Quelle est la mission unique de cet agent ? Périmètre fonctionnel borné, pas multi-rôles. |
| 2 | **Droits de décision** | Que peut-il décider seul ? Quelles décisions doivent être validées par un humain ? |
| 3 | **Points d'escalade** | À qui adresse-t-il les cas qui sortent de son périmètre ? Quel SLA d'escalade ? |
| 4 | **KPI** | Comment mesure-t-on sa performance ? À quelle fréquence ? Avec quel seuil d'alerte ? |
| 5 | **Audit** | Qui revoit ses décisions ? À quelle fréquence ? Sur quel échantillon ? |
| 6 | **Versions** | Comment gère-t-on l'évolution de son prompt / modèle / outils ? Tests de non-régression ? |
| 7 | **Onboarding / Offboarding** | Quel briefing initial (système prompt, exemples, contraintes) ? Comment archiver son travail si l'agent est désactivé ? |

### 3.1 Détail dimension par dimension

#### Dimension 1 — Tâche

Une mission **unique et bornée**, formulée comme on rédigerait une fiche de poste pour un employé débutant. Mauvais exemple : « assistant commercial polyvalent ». Bon exemple : « qualification des leads entrants via formulaire web, scoring sur 5 critères définis, transmission au commercial humain pour les leads scorés ≥ 4/5 ».

Le test : si tu peux résumer la mission en une phrase claire, c'est bon. Si tu hésites entre 3 missions, l'agent va dériver.

#### Dimension 2 — Droits de décision

Trois niveaux à distinguer :
- **Décisions autonomes** : l'agent décide et agit sans validation. Réservées aux décisions à faible enjeu et à fort volume (ex : envoyer un accusé de réception, marquer un ticket comme « résolu » après confirmation utilisateur).
- **Décisions avec garde-fous** : l'agent décide mais avec des règles strictes (ex : peut accorder une remise jusqu'à X %, au-delà = validation manager).
- **Décisions à valider** : l'agent prépare une recommandation, un humain valide avant action (ex : envoyer une réponse de litige, supprimer un compte client).

Principe de **moindre privilège** : commencer restrictif, élargir progressivement avec la preuve de la performance.

#### Dimension 3 — Points d'escalade

Pour chaque cas où l'agent atteint sa limite (manque de confiance, cas non prévu, demande hors périmètre), définir explicitement :
- **À qui** il escalade (un humain identifié, un autre agent spécialisé, une file d'attente)
- **Quel SLA** est attendu (sous 5 min ? 1 h ? 24 h ?)
- **Quel format de transmission** (résumé du contexte, historique de la conversation, raison de l'escalade)

L'escalade silencieuse (l'agent renvoie « je ne peux pas vous aider » sans transmission) est le pire des cas — c'est l'utilisateur qui doit recommencer son parcours.

#### Dimension 4 — KPI agent

Trois familles de KPI à suivre :

- **Performance opérationnelle** : containment rate (% de cas résolus sans escalade), temps moyen de résolution, taux d'escalade
- **Qualité** : taux de satisfaction utilisateur, taux de modification post-hoc des décisions de l'agent (signal de mauvaise calibration), taux d'erreur détecté en audit
- **Coût** : coût par interaction, coût total mensuel, coût par cas escaladé

Cible opérationnelle pratique 2026 : **10-15 % de cas en revue humaine**. Si moins, l'agent est probablement trop autonome (risque d'erreurs cachées). Si plus, l'agent est mal calibré (à reformer ou redéployer).

> 💡 **Signal rouge** : taux de modification chronique > 20 % des décisions de l'agent. Cela signifie que les humains corrigent systématiquement l'agent — il faut le reformer (nouveaux exemples, prompt revu, modèle changé).

#### Dimension 5 — Audit

Qui revoit les décisions de l'agent ? À quelle fréquence ? Sur quel échantillon ? Trois patterns d'audit :

- **Audit continu** : revue de chaque décision (pour les cas haut-risque uniquement, ex : décisions financières > X €)
- **Audit échantillonné** : revue d'un échantillon représentatif (10-20 % des décisions, par exemple chaque semaine)
- **Audit déclenché** : revue à la demande (sur réclamation utilisateur, sur signal anormal détecté en monitoring)

L'audit n'est pas optionnel. Il est exigé par l'AI Act (article 14) sur les systèmes haut-risque, et par la jurisprudence (cf. arrêt Moffatt v. Air Canada).

#### Dimension 6 — Versions

Un agent évolue : tu changes son prompt, tu changes le modèle backend (de Claude Sonnet 4.6 à Sonnet 4.7), tu ajoutes un outil. **Chaque changement est une nouvelle version**. À documenter :

- Numéro de version (v1.0, v1.1, etc.)
- Date de mise en production
- Description du changement
- Test de non-régression sur un dataset golden (cf. DEP-07 Évaluation continue)
- Plan de rollback si la nouvelle version dégrade la performance

Sans ce versioning, tu ne sais pas pourquoi ton agent a brutalement changé de comportement. Avec, tu peux revenir en arrière en quelques minutes.

#### Dimension 7 — Onboarding et offboarding

**Onboarding** : briefing initial de l'agent avant mise en production. Inclut :
- Système prompt complet
- Exemples positifs (« voici une bonne réponse à cette question »)
- Contre-exemples (« voici une réponse à ne pas donner »)
- Contraintes explicites (« tu ne donnes jamais de conseil juridique sans renvoyer à notre service juridique »)

**Offboarding** : si l'agent est désactivé (changement de mission, abandon du projet), comment archiver proprement ? Que devient l'historique de ses décisions ? Comment les utilisateurs sont-ils informés ?

Souvent négligé. C'est pourtant ce qui distingue une organisation mature d'une organisation qui empile des agents fantômes en production.

## Section 4 — Le cadre réglementaire à connaître

### 4.1 EU AI Act — Article 14 (supervision humaine)

L'AI Act exige une **supervision humaine effective** sur les systèmes d'IA haut-risque (recrutement, scoring crédit, biométrie, infrastructures critiques, etc.). Applicable au **2 août 2026**.

« Supervision humaine effective » signifie concrètement :
- Une personne physique identifiée capable d'intervenir
- Une compréhension suffisante du fonctionnement du système pour détecter les anomalies
- Un mécanisme d'arrêt rapide
- Des contrôles documentés

Pas de validation-réflexe (un humain qui clique « OK » sans lire) : la supervision doit être **significative**.

### 4.2 RGPD — Article 22 (décision automatisée)

L'article 22 du RGPD interdit qu'une **décision produisant des effets juridiques** ou des **effets significatifs similaires** sur une personne soit prise **uniquement** sur la base d'un traitement automatisé.

Cas concret : un agent IA qui rejette automatiquement une candidature, qui refuse un crédit, qui suspend un compte utilisateur, sans intervention humaine, est en infraction. Une intervention humaine **significative** est requise.

### 4.3 Jurisprudence — Moffatt v. Air Canada (BC Civil Resolution Tribunal, février 2024)

Le tribunal a tranché : **un chatbot n'est pas une entité légale séparée**. L'entreprise est responsable de ce que dit son chatbot. Air Canada a été condamnée à honorer les engagements pris par son chatbot, même si ces engagements contredisaient sa politique tarifaire officielle.

Implication : tout ce que ton agent dit ou décide engage ton entreprise, comme si c'était dit ou décidé par un employé. La défense « c'est l'IA qui a dit ça » n'est pas recevable.

### 4.4 Frameworks de référence à connaître

| Framework | Émetteur | Apport pour ta gouvernance |
|---|---|---|
| **NIST AI RMF + GenAI Profile** | NIST (gouvernement américain) | Référentiel risques + 4 fonctions Govern / Map / Measure / Manage. Gratuit, public. |
| **NIST Agentic AI Profile** | CSA Labs (en lien NIST) | Spécifique aux agents autonomes. Public draft 2026. |
| **ISO/IEC 42001** | ISO/IEC | 38 contrôles certifiables. Devient standard contractuel : 40 % des RFP IA en UE le mentionnent mi-2026. |
| **Recommandations CNIL IA** | CNIL (France) | Application du RGPD au développement IA + chaîne de responsabilités. |

## Section 5 — Le pattern d'escalade — confidence-based routing

### 5.1 Le pattern qui s'impose en 2026

Le pattern managérial le plus mature qui émerge en 2026 : **confidence-based routing + tiered escalation**. Plutôt que d'opposer « agent autonome » et « agent supervisé », l'agent **mesure sa propre confiance** sur chaque décision et **route automatiquement** selon le niveau de confiance.

### 5.2 Trois zones de confiance

| Zone | Confiance | Action |
|---|---|---|
| **Zone verte** | Haute (> 80 %) | L'agent agit en autonomie, log de la décision pour audit |
| **Zone jaune** | Moyenne (50-80 %) | L'agent prépare la décision, validation humaine rapide (sous 1 h) |
| **Zone rouge** | Basse (< 50 %) | L'agent escalade immédiatement, formule la question pour le bon humain |

Cible opérationnelle : 70-85 % zone verte, 10-15 % zone jaune, 5-15 % zone rouge.

### 5.3 Mesurer la confiance — comment faire en pratique

Plusieurs approches concrètes :
- **Self-reported confidence** : demander à l'agent de scorer sa propre réponse (l'agent donne sa réponse + un score 1-10 + une justification)
- **Multi-model voting** : faire générer plusieurs versions par plusieurs modèles, mesurer la cohérence
- **Rule-based triggers** : escalade automatique si certains mots-clés apparaissent (ex : « litige », « urgent », « réclamation », « avocat »)
- **External signals** : si l'utilisateur a déjà eu des escalades précédentes ou est sur un compte sensible, escalade par défaut

### 5.4 Outils 2026

- **LangGraph `interrupt()`** : permet à un agent LangGraph de demander une intervention humaine au milieu de son exécution
- **Anthropic patterns d'orchestration** : documentés dans les Claude Engineering blog posts
- **Hermes Agent (NousResearch)** : agent open-source avec gestion native de l'escalade (cf. fiche outil)

## Section 6 — Auto-diagnostic : où en es-tu sur la gouvernance de tes agents ?

> **Format pour Claude Code** : auto-diagnostic interactif conforme RULES § 1.5.5 (form interactif + génération d'un plan d'action + export `.txt` + persistance localStorage). Reprendre le pattern de CU-023 / CU-008 / CU-013.

### Les 8 questions

Pour chaque agent en production (ou en projet), réponds Oui / Non / Partiel :

1. **Tâche bornée** : la mission de mon agent tient-elle en une phrase claire, sans ambiguïté ?
2. **Droits explicites** : ai-je formalisé les 3 niveaux de décision (autonome / avec garde-fous / à valider) pour cet agent ?
3. **Escalade documentée** : ai-je défini à qui l'agent escalade, sous quel SLA, dans quel format ?
4. **KPI agent** : est-ce que je mesure containment rate, taux d'escalade, satisfaction utilisateur, coût par interaction ?
5. **Audit régulier** : ai-je planifié un audit échantillonné des décisions de l'agent (au minimum mensuel) ?
6. **Versioning** : tiens-je un registre des versions de l'agent (prompt, modèle, outils), avec tests de non-régression ?
7. **Manager humain identifié** : y a-t-il une personne nommée (pas une équipe vague) qui « manage » cet agent au quotidien ?
8. **Conformité** : ma gouvernance respecte-t-elle l'article 14 AI Act (supervision humaine effective) et l'article 22 RGPD (intervention humaine significative) ?

### Le verdict en 3 niveaux

- **🟢 GOUVERNANCE MATURE** (7-8 OUI) : ton agent est en production avec un cadre opérationnel solide. Maintiens la rigueur, audite trimestriellement.
- **🟡 GOUVERNANCE EN CONSTRUCTION** (4-6 OUI) : ton agent fonctionne mais des angles morts existent. Priorise les dimensions manquantes avant de scaler.
- **🔴 GOUVERNANCE INSUFFISANTE** (< 4 OUI) : risque significatif (réputationnel, juridique, financier). Suspends l'extension du périmètre de l'agent et formalise les dimensions manquantes en urgence.

### Plan d'action généré par le diagnostic

Pour chaque dimension où la réponse est NON ou PARTIEL, générer une recommandation concrète issue de la section 3 du module.

### Export

Bouton « 📥 Exporter en .txt » qui produit un livrable contenant le verdict, les réponses, et le plan d'action personnalisé.

## Section 7 — Plan d'action 30 jours pour structurer la gouvernance

### Jours 1-7 — Inventaire

- Lister tous les agents IA déployés ou en projet dans l'entreprise
- Pour chaque agent : qui est responsable ? quel périmètre ? quels KPI suivis (s'ils existent) ?
- Identifier les agents prioritaires (impact business le plus fort, exposition réglementaire la plus élevée)

### Jours 8-14 — Formalisation des 7 dimensions

- Pour chaque agent prioritaire, remplir le contrat « agent ↔ entreprise » (cf. section 3)
- Nommer un manager humain identifié pour chaque agent
- Documenter les points d'escalade

### Jours 15-21 — Mise en place du suivi

- Définir les KPI de chaque agent et les mettre en monitoring
- Construire un dataset golden pour l'évaluation continue (cf. DEP-07)
- Planifier le rythme d'audit (mensuel minimum)

### Jours 22-30 — Audit et ajustement

- Premier audit échantillonné des décisions de chaque agent
- Identifier les écarts (taux de modification > 20 %, escalades manquées, biais détectés)
- Plan d'ajustement (reformer l'agent, revoir les droits, élargir le périmètre d'escalade)

## Section 8 — Pour aller plus loin (Schéma A)

### Callout d'aiguillage

> Pour le panorama complet des outils agents IA et frameworks de gouvernance, retrouve les fiches détaillées sur la [page Ressources du Hub](../ressources.html#bibliographie).

### 📰 Articles de fond

- [Fortune — AI agents are acting like employees, but company structures still treat them like software (avril 2026)](https://fortune.com/2026/04/13/ai-agents-governance-identity-risk-okta/) — Le constat 91 % usage / 10 % gouvernance
- [Raconteur — Autonomous AI agents 2026: the new rules for business governance](https://www.raconteur.net/technology/autonomous-ai-agents-2026-the-new-rules-for-business-governance) — Synthèse des règles émergentes
- [CX Dive — Klarna reinvests in human talent for customer service](https://www.customerexperiencedive.com/news/klarna-reinvests-human-talent-customer-service-AI-chatbot/747586/) — Cas pédagogique fondateur
- [McKinsey — The State of AI 2025 (novembre 2025)](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai) — Données scaling agents

### 🎓 Tutoriels & cas pratiques

- [Snowflake — The AI Agent Identity Problem](https://www.snowflake.com/en/blog/ai-agent-identity-governance-enterprise-trust/) — Pattern identité dédiée pour agents
- [Anthropic Engineering — Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) — Patterns techniques de production
- [LangGraph — Human-in-the-loop with `interrupt()`](https://langchain-ai.github.io/langgraph/) — Documentation du pattern d'escalade

### 📚 Documentation officielle & études

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — Référentiel gouvernement américain
- [NIST AI 600-1 Generative AI Profile (PDF)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) — 12 risques GenAI documentés
- [CSA Labs — NIST AI RMF Agentic Profile](https://labs.cloudsecurityalliance.org/agentic/agentic-nist-ai-rmf-profile-v1/) — Spécifique agents
- [Bpifrance Le Lab — IA dans les PME et ETI françaises](https://lelab.bpifrance.fr/) — Données PME 2025
- [CNIL — Recommandations IA et RGPD](https://www.cnil.fr/) — Application française
- [Moffatt v. Air Canada — Civil Resolution Tribunal (février 2024)](https://decisions.civilresolutionbc.ca/) — Jurisprudence fondatrice

### 👥 Communautés & veille

- [Anthropic Discord](https://www.anthropic.com/discord) — Échanges patterns d'agents production
- [LangChain Forum](https://forum.langchain.com/) — Communauté technique active
- [r/LocalLLaMA](https://reddit.com/r/LocalLLaMA) — Communauté self-host LLM et agents

## Renvois internes pour Claude Code

- **Section 1.3 et Section 3** : lien `<a href="cu-014-multi-agents.html">CU-014 Multi-agents par fonction</a>` (architecture)
- **Section 4** : liens `<a href="cu-020-conformite-rgpd-ai-act.html">CU-020 Conformité RGPD &amp; AI Act</a>` et `<a href="../prealables/pr-05-securite-ia.html">PR-05 Sécurité IA</a>`
- **Section 5.4** : liens vers les fiches outils `<a href="../ressources.html#hermes-agent">Hermes Agent</a>` (créée Lot D), Anthropic, LangGraph
- **Section 7** : lien `<a href="../deploiement/dep-07-evaluation-qualite.html">DEP-07 Évaluation continue et qualité IA</a>` (dataset golden)
- **Section 7** : lien `<a href="../deploiement/dep-05-agents-observabilite.html">DEP-05 Agents en production</a>` (monitoring)

## Composants visuels suggérés

- **Section 1** : encart `.stat-block` pour le « 91 % vs 10 % »
- **Section 2** : `.case-deep-actor` pour le cas Klarna (variante warm pour mise en relief)
- **Section 3** : `.tool-table` pour le tableau des 7 dimensions
- **Section 4.4** : `.tool-table` pour les frameworks de référence
- **Section 5.2** : grille 3 cards pour les 3 zones de confiance (vert / jaune / rouge)
- **Section 6** : `<form id="govDiagForm">` interactif conforme RULES § 1.5.5
- **Section 7** : `.timeline-block` pour le plan d'action 30 jours

## Cohérence numérique (RULES § 1.2.3)

CU-026 ajouté → **passage de 26 à 27 modules CU**. Mise à jour cross-site obligatoire (cf. brief Claude Code v3.8).

## Note Cowork

Module construit à partir de la veille `veille-cu-026-gouvernance-agents.md` (11 mai 2026), elle-même appuyée sur Okta, Fortune, McKinsey, Bpifrance Le Lab, NIST, CSA Labs, ISO/IEC, CNIL, jurisprudence Moffatt v. Air Canada. Aucune mention d'éditeur en promotion. Conforme RULES § 1.1.

L'angle « agent = employé » est bien différencié des modules adjacents (CU-014 architecture, CU-020 conformité, PR-05 sécurité technique). Validé arbitrage Blaise.
