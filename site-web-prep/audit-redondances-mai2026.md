# Audit redondances éditoriales — Hub IA (mai 2026)

> Audit ciblé sur 5 paires/triplets de modules suspects. Méthode : lecture hero + executive summary + section 1 + card index pour chaque module concerné. Audit des 25 modules du catalogue v3.6.

## Synthèse exécutive

- **1 vraie redondance résiduelle (point chaud Blaise) :** CU-015 et CU-027 partagent 50 % de leur surface (vibe coding, outils Cursor/Claude Code, panorama 2026). La frontière éditoriale existe (cas-école Stripe / dirigeant PME non-IT) mais n'est pas tenue dans les hero, ni dans les cards index, ni dans l'angle pédagogique.
- **2 paires bien différenciées avec cross-link explicite :** CU-005 vs CU-023 (les hero se renvoient mutuellement, niveau et cible distincts) et CU-013 vs CU-024 (workflow agentique générique vs cycle O2C réglementaire). Pas d'action structurelle à prévoir.
- **1 chevauchement partiel à clarifier :** CU-021 (finance augmentée) et CU-024 (O2C) se croisent sur la facturation, sans cross-link et sans frontière explicitée. Ni redondance ni indépendance claire — les deux modules se complètent mais l'utilisateur ne le sait pas.
- **1 trio à réarticuler en triptyque :** CU-001 / CU-011 / CU-012 (recherche, veille concurrentielle, veille AAP) couvrent des objets très distincts mais aucun cross-link ne le matérialise. Pas de redondance, mais un manque d'aiguillage (lecteur ne sait pas par où commencer).
- **Recommandation globale :** 1 fusion partielle / refonte (CU-015 + CU-027), 1 amendement de hero (CU-021/CU-024), 1 ajout de cross-links (trio veille). Aucune suppression de module n'est justifiée.

---

## 1. CU-015 vs CU-027 (point chaud Blaise)

### Périmètres comparés

| Critère | CU-015 — Stripe Minions | CU-027 — Dev applicatif IA-assisté |
|---|---|---|
| **Card index** | « 1000+ PRs/semaine produits par agents. Le passage de l'IA assistant à l'IA autonome sur cycle court » | « Comment piloter un dev IA-assisté (Cursor, Claude Code, Lovable, Bolt) sans être IT — angle dirigeant PME non-tech » |
| **Sous-titre hero** | « Asynchronicité comme principe de pilotage transposable bien au-delà du dev » | « Ce qui demandait 3 développeurs et 6 mois se prototype en 2-3 semaines avec Cursor, Claude Code, Lovable, Windsurf » |
| **Public cible déclaré** | Pilotes équipe tech avec backlog ; veulent transposer l'asynchronicité à des fonctions non-tech | Dirigeants PME/ETI non-IT qui ont fait le diag build vs buy |
| **Périmètre fonctionnel** | Pattern « one-shot end-to-end », asynchronicité, prérequis tests 75 %, code review obligatoire, étude de cas Stripe | Panorama outils 2026 (Lovable, Bolt, v0, Replit, Cursor, Claude Code, Windsurf), incident Tea App, 6 écueils, checklist sécurité, cadre juridique |
| **Outils mentionnés** | Claude Code, Devin, Cursor Composer, Aider | Lovable, Bolt, v0, Replit Agent, Cursor, Claude Code, Windsurf, GitHub Copilot |
| **Angle pédagogique** | Cas-école + leçon générique d'asynchronicité (badge « cas-école ») | Étude de cas + checklist prestataire + cadre juridique (badge « Étude de cas + checklist ») |
| **Niveau / lecture** | N4, 40 min | N4, 25 min |

### Diagnostic

**Chevauchement réel et inconfortable.** Les deux modules :
- partagent l'axe agentique, le niveau N4, l'emoji 🛠️
- listent en partie les mêmes outils (Cursor, Claude Code)
- s'adressent au même type de lecteur (dirigeant)

Mais ils visent en réalité deux questions distinctes :
- **CU-015 = pattern d'orchestration** (« comment pense-t-on quand un agent fait du travail à ma place ? ») — c'est un cas-école managérial qui se trouve illustré par le code Stripe mais qui se transpose au support, à l'admin, au contenu.
- **CU-027 = guide d'achat / cadrage projet** (« je veux faire développer une appli, comment je m'y prends ? ») — c'est un module utilitaire de pilotage projet pour dirigeant non-IT.

Le problème éditorial : **les hero ne disent pas cette différence**. Un lecteur qui voit deux cards N4 axe agentique avec emoji 🛠️ et qui entend parler de Cursor + Claude Code dans les deux ne sait pas pourquoi il y en a deux.

### Recommandation

**Garder les deux modules — clarifier radicalement la frontière**, dans cet ordre :
1. **Renommer CU-015** sur la card et le hero pour effacer toute ambiguïté côté « guide d'achat » : passer de « Agents codeurs internes » à « Asynchronicité agentique — cas Stripe Minions ». Le mot « codeur » est ce qui crée la confusion ; or l'enseignement est managérial, pas technique.
2. **Renommer CU-027** sur la card pour effacer l'allusion aux agents : passer de « Développement applicatif métier IA-assisté » à « Faire développer une appli métier (sans être IT) ». Reformuler la card index pour mettre l'accent sur le pilotage projet (cadrage, choix prestataire, sécurité) plutôt que sur le panorama d'outils.
3. **Ajouter un cross-link mutuel** dans les sous-titres hero (comme CU-005/CU-023), du type : « Pour comprendre ce que change le pattern agentique côté pilotage cognitif → CU-015 » et « Pour cadrer un projet de dev concret → CU-027 ».
4. **Diversifier les outils mis en avant** : retirer Cursor / Claude Code de la première impression visuelle de CU-015 (les pousser plus bas dans le module) ; garder le panorama complet sur CU-027 où il a sa place.

---

## 2. CU-005 vs CU-023

### Périmètres comparés

| Critère | CU-005 — Propositions B2B complexes | CU-023 — Devis simples (porte d'entrée IA) |
|---|---|---|
| **Card index** | « RFP, bid management, mémoires techniques, propal > 20 pages. Couplage assistant IA + base de connaissance interne » | « Devis catalogue, forfaits, services standardisés. Brouillon contextualisé en quelques minutes (1 h → 36 min). Cible TPE/PME qui démarrent l'IA » |
| **Sous-titre hero** | Mentionne **explicitement** : « Pour les devis simples, voir CU-023 » | Mentionne **explicitement** : « Pour les propositions B2B complexes, voir CU-005 » |
| **Public cible** | Équipe produit 5-15 propositions/mois consommant 1h30-2h chacune ; corpus historique exploitable | Commercial 30 devis/mois ; pas de migration ERP ; ROI 3-6 mois ; premier cas d'usage IA |
| **Périmètre fonctionnel** | Architecture RAG sur base interne (catalogue + tarifs + historique), voix de marque, NotebookLM/Dify/Flowise | Activation couche IA d'un CRM/ERP existant (Pennylane, Sellsy, Axonaut, HubSpot, PandaDoc) |
| **Outils mentionnés** | Claude, GPT-4/5, Mistral, NotebookLM, Dify, Flowise, Goodweek, EthiqAIS | Pennylane, Sellsy, Axonaut, HubSpot, Salesforce, PandaDoc, Esker |
| **Angle pédagogique** | Auto-diagnostic + plan d'action séquencé | Auto-diagnostic + cas chiffré HPC/PandaDoc + plan d'action 90 jours |
| **Niveau / lecture** | N3, 25 min | N2, 15 min |

### Diagnostic

**Pas de redondance — différenciation claire et déjà matérialisée.** Le clivage est net sur 3 dimensions :
- **Volume / complexité du livrable** : RFP > 20 pages vs devis catalogue
- **Stack** : assistant IA + RAG sur corpus interne vs couche IA native d'un outil SaaS
- **Niveau de maturité IA du lecteur** : N2 (premier cas) vs N3 (chantier organisationnel structurant)

Les deux hero se renvoient explicitement l'un à l'autre, ce qui résout le risque de confusion. Les outils ne se recoupent pas (NotebookLM/Dify côté CU-005, CRM/ERP intégrés côté CU-023).

### Recommandation

**Status quo.** Modules à conserver tels quels. Le seul micro-amendement possible : harmoniser la terminologie « devis » vs « proposition » sur la home (la card CU-005 dit « Propositions », la card CU-023 dit « Devis »), ce qui est déjà le cas. RAS.

---

## 3. CU-021 vs CU-024

### Périmètres comparés

| Critère | CU-021 — Finance & comptabilité augmentées | CU-024 — Order-to-cash automation |
|---|---|---|
| **Card index** | « Extraction factures, rapprochement bancaire, prévision cash, détection anomalies. ROI 155 % an 1 » | « Cycle complet devis → commande → livraison → facture → encaissement, calé sur facturation électronique 2026-2027. -30 % de délai paiement » |
| **Sous-titre hero** | Automatiser extraction factures **fournisseurs**, rapprochement bancaire, prévision cash, détection anomalies | Cycle commercial complet sortant — devis, BC, **facturation**, relance, encaissement, lettrage |
| **Public cible** | PME/ETI ≥ 100 factures fournisseurs/mois ; service comptable saturé ; DAF qui reconstruit le cash hebdo | Émet > 100 factures/mois ; DSO > 50 jours ; pas encore choisi sa Plateforme Agréée DGFiP |
| **Périmètre fonctionnel** | 4 sous-cas **comptabilité fournisseur + pilotage cash interne** | 6 maillons **cycle commercial sortant**, calendrier réglementaire (e-facturation 2026, AI Act scoring), choix PA agréée |
| **Outils mentionnés** | Claude/GPT + n8n/Make + ERP (Sage, Cegid, EBP, Pennylane, Qonto, Odoo) | Plateformes Agréées DGFiP — Pennylane, Sellsy, Axonaut, Esker, Sidetrade |
| **Angle pédagogique** | Étude de cas Batibig (110 K€ détectés / 20 K€ investis), 4 sous-cas séquentiels | Calendrier réglementaire + 6 maillons + checklist 12 points |
| **Niveau / lecture** | N3, 35 min | N4, 22 min |

### Diagnostic

**Chevauchement partiel à clarifier — pas de redondance.** Les frontières existent mais ne sont pas dites :
- **CU-021 = côté fournisseur entrant (achats) + pilotage interne** : factures fournisseurs, rapprochement, anomalies, cash forecast
- **CU-024 = côté client sortant (ventes)** : devis, BC, facture émise, relance, encaissement

Les deux croisent la facturation et la prévision cash mais ne traitent ni le même flux ni le même service métier (compta fournisseur vs ADV/recouvrement). **Aucun cross-link** dans les hero ni les exec summary, ce qui laisse planer un doute. Pire : CU-024 mentionne CU-021 et CU-013 dans son module mais l'inverse n'est pas vrai dans CU-021.

Risque concret : un dirigeant qui veut « automatiser sa compta » va lire CU-021 et croira avoir tout couvert ; il manquera tout l'enjeu réglementaire e-facturation 2026 qui est dans CU-024.

### Recommandation

**Réarticuler par cross-links explicites + amendement hero.**
1. Ajouter dans le hero CU-021 une phrase : « Pour le cycle commercial sortant (facturation client, relance, recouvrement, e-facturation 2026), voir CU-024. »
2. Ajouter dans le hero CU-024 une phrase symétrique : « Pour la fonction comptable fournisseur (extraction factures entrantes, prévision cash, anomalies), voir CU-021. »
3. Optionnellement : ajouter un mini-schéma « cartographie du cycle financier » qui place les deux modules côte à côte (fournisseurs / clients) et les positionne explicitement.

---

## 4. CU-013 vs CU-024

### Périmètres comparés

| Critère | CU-013 — Workflow email → CRM | CU-024 — Order-to-cash automation |
|---|---|---|
| **Card index** | « Workflow de référence pour franchir le pas de l'IA agentique : 30-60 min/jour libérées sur le tri d'emails » | « Cycle complet devis → encaissement, calé sur facturation électronique 2026-2027 » |
| **Sous-titre hero** | Agent IA qui lit emails, classifie, extrait info, met à jour CRM, rédige réponse contextualisée | Cycle complet O2C automatisé par IA, contexte DSO 65 jours et e-facturation obligatoire |
| **Public cible** | Boîte avec 50+ emails/jour ; CRM (HubSpot, Pipedrive, Salesforce) sous-utilisé pour le logging | Émet > 100 factures/mois, DSO > 50 jours, choix Plateforme Agréée à faire |
| **Périmètre fonctionnel** | Pattern agentique générique de traitement entrant : classification AUTO/DRAFT/HUMAIN, mise à jour CRM, rédaction réponse | Cycle commercial réglementé : devis, BC, facturation, relance, encaissement, lettrage |
| **Outils mentionnés** | HubSpot, Pipedrive, Salesforce ; Mistral pour souveraineté | Pennylane, Sellsy, Axonaut, Esker, Sidetrade ; PA agréées DGFiP |
| **Angle pédagogique** | Matrice de règles + étude de cas ServicesCo + checklist d'éligibilité | Calendrier réglementaire + checklist 12 points + sélection PA agréée |
| **Niveau / lecture** | N4 axe agentique, 40 min | N4 axe productivité, 22 min |

### Diagnostic

**Pas de redondance — frontière claire mais implicite.** Les deux modules ne se rencontrent que sur un point très étroit (la mise à jour CRM post-email peut concerner une opportunité commerciale qui finira en devis). Le clivage est net :
- CU-013 = pattern agentique sur **flux email entrant**, transversal à tous les services
- CU-024 = chaîne **commerciale et financière sortante** sous contrainte réglementaire

Aucun risque de confusion réelle pour un lecteur. Mais aucun cross-link non plus.

### Recommandation

**Status quo + 1 cross-link mineur.** Optionnellement, ajouter dans CU-024 une mention type « pour la pré-qualification des emails entrants (devis, demandes), voir CU-013 ». Sans urgence — la frontière éditoriale tient toute seule.

---

## 5. CU-001 vs CU-011 vs CU-012

### Périmètres comparés

| Critère | CU-001 Recherche & veille | CU-011 Veille concurrentielle | CU-012 Veille AAP & drafting |
|---|---|---|---|
| **Card index** | « Remplacer Google par des outils de recherche IA pour produire des synthèses sourcées en quelques minutes » | « Surveillance permanente d'un panel de concurrents, alerte sur les évolutions significatives » | « Auto-discovery des AAP, matching profil, pré-rédaction des dossiers. Cas pivot pour les startups » |
| **Sous-titre hero** | « Le réflexe le plus rentable à acquérir, applicable dès aujourd'hui sans aucune compétence technique » | « Système qui scrute en continu un panel de concurrents (sites, communications, brevets, recrutements, levées) et alerte » | « Système agentique qui découvre les nouveaux AAP, les rapproche du profil entreprise, génère un draft » |
| **Public cible** | Tout dirigeant qui passe plusieurs heures/sem à chercher de l'info ; n'a jamais utilisé Perplexity/NotebookLM/Le Chat Pro | Apprend les mouvements concurrents avec retard ; reçoit 50 alertes/sem ignorées ; 8-12 concurrents directs | Startup deeptech/biotech/industrielle avec 6+ candidatures/an ; ou SUM qui outille un portefeuille |
| **Périmètre fonctionnel** | Usage ponctuel : question → synthèse sourcée. Outils chatbot/research | Système permanent : panel + signaux + matrice + synthèse hebdo | Système agentique 4 agents (veille + matching + drafting + submission) + 2 validations humaines |
| **Outils mentionnés** | Perplexity, Le Chat Pro Mistral, NotebookLM | Outils dédiés veille (mention Perplexity ponctuelle) + n8n, alertes structurées | Mistral EU, EthiqAIS, Goodweek, n8n, frameworks multi-agents Python |
| **Angle pédagogique** | Quiz 5 questions + cas d'étude guidé (15 min de mise en pratique) | Étude de cas + signaux types + auto-diagnostic | Étude de cas DeepTechCo + checklist d'éligibilité + architecture multi-agents |
| **Niveau / lecture** | N1, 15 min | N2, 25 min | N3 axe agentique, 45 min |

### Diagnostic

**Pas de redondance — triptyque progressif bien différencié, mais aucune articulation visible.** Les trois modules forment naturellement un parcours :
- **CU-001** = premier réflexe individuel (un humain pose une question, l'outil répond)
- **CU-011** = système permanent ciblé sur un objet précis (concurrents)
- **CU-012** = système agentique sur cas pivot startup (AAP)

Aucun chevauchement de périmètre fonctionnel. Aucun outil n'est mentionné dans les trois modules de façon centrale (Perplexity est central CU-001, périphérique CU-011 ; n8n et Mistral apparaissent surtout sur CU-011 et CU-012).

**Mais : aucun cross-link** entre les trois modules dans les hero. Un lecteur qui découvre la home avec « Recherche & veille augmentée » (CU-001) ne sait pas qu'il existe deux applications industrialisées plus loin (CU-011, CU-012).

### Recommandation

**Status quo sur le périmètre + ajouter un encart de parcours.**
1. Dans le hero ou l'exec summary de CU-001, ajouter une phrase : « Pour passer du réflexe ponctuel à un système permanent : CU-011 (veille concurrentielle) ou CU-012 (veille AAP). »
2. Symétriquement, dans CU-011 et CU-012, mentionner CU-001 comme prérequis « si tu n'as pas encore le réflexe individuel ».
3. Optionnel : créer une visualisation « parcours veille » sur la home (3 jalons N1 → N2 → N3) qui matérialise la progression.

---

## 6. Autres redondances détectées

Lecture rapide des autres modules — **aucune autre redondance signalée** sur la liste de 25. Quelques points périphériques relevés sans conséquence :

- **CU-008 (KB RAG) / CU-005 (Propositions B2B)** : les deux mobilisent du RAG mais sur objets distincts (RAG général d'entreprise vs RAG spécialisé sur corpus propositions). CU-005 cite CU-008 comme prérequis implicite. Frontière claire.
- **CU-009 (Content repurposing) / CU-010 (Pipeline contenu social)** : non audités en détail mais à vérifier sur une prochaine itération — leurs cards index pourraient se chevaucher.
- **CU-002 (Assistant rédactionnel) / CU-008 (KB RAG)** : CU-002 est un usage individuel chatbot, CU-008 est une infrastructure organisationnelle. Pas de chevauchement.

---

## Recommandations consolidées pour Cowork + Claude Code

Ordre de priorité pour la prochaine itération d'harmonisation :

### Priorité 1 — résolution du point chaud (CU-015 vs CU-027)
- **Tâche Claude Code** : éditer hero + card index des deux modules pour clarifier la frontière (asynchronicité managériale vs guide d'achat dev applicatif). Ajouter cross-links mutuels. Estimation 30 min.
- **Tâche éditoriale Blaise** : valider les nouveaux titres et sous-titres avant publication.

### Priorité 2 — clarification finance (CU-021 vs CU-024)
- **Tâche Claude Code** : ajouter cross-link bidirectionnel dans les hero. Optionnel : insérer un mini-schéma « cartographie cycle financier ». Estimation 20 min.

### Priorité 3 — articulation triptyque veille (CU-001 / CU-011 / CU-012)
- **Tâche Claude Code** : ajouter une mention de parcours dans chacun des trois exec summary. Estimation 15 min.

### Priorité 4 — micro-amendements (CU-013 vs CU-024)
- **Tâche Claude Code** : 1 ligne de cross-link dans CU-024. Estimation 5 min.

### Action différée — audit complémentaire
- **À ouvrir au prochain sprint** : audit ciblé CU-009 vs CU-010 (pipeline contenu) qui n'était pas dans la liste prioritaire mais mérite une lecture rapide.

**Aucun module ne doit être supprimé ni fusionné intégralement.** L'ensemble des recommandations relève de l'amendement éditorial (titres, sous-titres, cross-links), pas d'une refonte structurelle.
