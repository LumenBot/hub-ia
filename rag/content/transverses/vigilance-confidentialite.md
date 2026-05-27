---
code: vigilance-confidentialite
titre: "Vigilance — confidentialité des données dans les outils IA"
type: transverse
axe: transverse
niveau: 2
tags: [vigilance, confidentialite, rgpd, souverainete, donnees-sensibles, ai-act]
version: 3.8.2
last_updated: 2026-05-11
glosaire_termes: [llm, saas, souverainete, cloud-souverain, on-premise]
derives: ["[[cu-001]]", "[[cu-002]]", "[[cu-005]]", "[[cu-007]]", "[[cu-008]]", "[[cu-020]]", "[[cu-024]]", "[[pr-05]]"]
public_cible: [dirigeant, ops, r&d]
---

# Vigilance — confidentialité des données dans les outils IA

> Brique transverse référencée par les modules qui manipulent des données potentiellement sensibles. Une seule définition canonique des règles de protection, des recommandations opérationnelles applicables à tout contexte d'usage IA.

## Le risque structurel

Les chatbots grand public envoient toutes les requêtes à leurs serveurs et peuvent les utiliser pour entraîner leurs modèles. Cela signifie concrètement que toute donnée collée dans une interface IA grand public peut potentiellement :
- être stockée durablement chez l'éditeur
- être consultée par des employés humains de l'éditeur dans le cadre du contrôle qualité ou de l'amélioration produit
- contribuer à entraîner les modèles futurs (ressurgir potentiellement dans des réponses à d'autres utilisateurs)
- être soumise à la juridiction de l'hébergeur (notamment le Cloud Act pour les acteurs américains)

Le risque ne dépend pas de la sensibilité subjective qu'on attribue à la donnée — il dépend du cadre juridique applicable à l'hébergeur et du contrat d'usage signé.

## Les 4 catégories à ne JAMAIS coller dans un chatbot grand public

**Catégorie 1 — Données personnelles identifiables.** Noms, prénoms, adresses, numéros de téléphone, emails de personnes physiques identifiables ou identifiables indirectement. Le RGPD s'applique : tout transfert de ces données vers un hébergeur tiers nécessite une base légale et un encadrement contractuel.

**Catégorie 2 — Données contractuelles et commerciales.** Contrats clients ou fournisseurs, propositions commerciales en cours de négociation, conditions tarifaires, comptes annuels non publiés. Risque de fuite concurrentielle et de violation des clauses de confidentialité.

**Catégorie 3 — Données stratégiques internes.** Plans stratégiques, projets de R&D, brevets en cours, candidatures à des appels d'offres, données financières prévisionnelles. Risque d'exfiltration de la propriété intellectuelle et de l'avantage concurrentiel.

**Catégorie 4 — Données régulées.** Données de santé, données bancaires, données défense, données soumises à des règlements sectoriels (NIS2, DORA, secrets bancaires, secret médical). Le cadre légal applicable interdit le transfert hors environnement contrôlé.

## Les 3 options pour traiter les données sensibles avec l'IA

**Option 1 — Versions Pro et Enterprise des LLM majeurs.** ChatGPT Team/Enterprise, [[outils-llm|Claude]] pour les entreprises, Gemini Workspace : engagent contractuellement à ne pas utiliser les données pour entraînement. Vérifier les Data Processing Agreements (DPA). Reste un transfert hors UE pour la plupart des acteurs.

**Option 2 — Acteurs européens avec [[glossaire#souverainete]] EU.** [[outils-llm|Mistral]] Le Chat Pro (hébergement EU, certifications ISO 27001 et SOC 2 pour le Chat Pro), Mistral La Plateforme via partenaires EU, OpenAI via Azure Europe avec configuration adéquate. Garanties RGPD natives, juridiction européenne applicable. À privilégier pour les organisations soumises à des contraintes RGPD strictes.

**Option 3 — Modèles open-source en self-hosted ou [[glossaire#on-premise]].** [[outils-llm|Llama]], Mistral, [[outils-llm|Qwen]], Phi déployés sur infrastructure interne ou cloud souverain (OVH, Scaleway, 3DS Outscale, Cloud Temple). [[glossaire#souverainete]] maximale, contrôle total des données. Compromis : compétences techniques requises pour opérer en production.

Le choix entre ces 3 options dépend du niveau de sensibilité, du cadre réglementaire, des compétences disponibles et du budget. Cadrage détaillé dans [[pr-05]] (Sécurité IA) et [[cu-020]] (Conformité RGPD & AI Act).

## La discipline en 4 règles

**Règle 1 — Catégoriser avant de coller.** Avant chaque requête IA, se poser explicitement : est-ce que ce contenu relève des 4 catégories ci-dessus ? Si oui, basculer sur une option compatible (Pro, EU, self-hosted) avant de coller. Si non, l'usage grand public reste acceptable.

**Règle 2 — Documenter les usages autorisés en interne.** Politique IA de l'organisation qui précise quelles données peuvent aller dans quels outils. Sans cette politique écrite, les collaborateurs naviguent à l'aveugle et les fuites sont quasi certaines à moyen terme.

**Règle 3 — Privilégier l'anonymisation à la source.** Si le besoin métier est de traiter de l'information sans manipulation de données identifiantes (ex. analyse d'une masse de tickets support), anonymiser le contenu avant de le passer à l'IA. Permet d'utiliser des outils plus larges sans risque.

**Règle 4 — Vérifier les certifications de l'éditeur pour les usages structurants.** Pour les déploiements IA qui structurent un processus métier (au-delà de l'usage ponctuel), exiger ISO 27001, SOC 2 Type II, et idéalement SecNumCloud si données très sensibles.

## Cas d'application typiques

- **Recherche augmentée** ([[cu-001]]) : pour les recherches sur des sujets sensibles internes (M&A, restructurations, contentieux), utiliser Le Chat Pro plutôt que Perplexity grand public.
- **Rédactionnel** ([[cu-002]]) : ne pas coller de contrats clients dans ChatGPT pour reformulation ; passer par Claude Enterprise ou Mistral Pro.
- **Propositions commerciales B2B** ([[cu-005]]) : les avant-vente complexes contiennent souvent des éléments stratégiques — usage outil Pro avec DPA signé.
- **RH** ([[cu-007]]) : les CV et entretiens contiennent des données personnelles — RGPD applicable, usage strictement encadré.
- **Knowledge base RAG** ([[cu-008]]) : par construction, le RAG manipule du corpus interne. Le vector store et le LLM doivent être en accord avec la sensibilité du corpus (privilégier Mistral EU ou self-hosted pour corpus stratégique).
- **Order-to-cash automation** ([[cu-024]]) : données de facturation, conditions de paiement — données contractuelles + données personnelles.
- **Conformité RGPD/AI Act** ([[cu-020]]) : ce module détaille les obligations légales applicables.

## Anti-patterns observés

- **« Je vais juste tester rapidement »** : la donnée collée pour un test reste durablement chez l'éditeur. Pas de retour en arrière possible une fois envoyée.
- **Anonymisation cosmétique** : remplacer les noms propres par « X » et « Y » ne suffit pas si le contexte permet la réidentification (taille de l'entreprise, secteur, géographie, dates précises…).
- **Confiance dans les engagements verbaux** : si la DPA ne mentionne pas explicitement la non-utilisation pour entraînement et la non-rétention au-delà de la prestation, considérer que la donnée peut être conservée.
- **Politique IA d'usage ignorée** : avoir rédigé une politique IA et ne pas l'appliquer (ou ne pas former les collaborateurs) crée un faux sentiment de sécurité plus dangereux que l'absence de politique.

## Pour aller plus loin

- Cadrage sécurité IA approfondi : [[pr-05]] (Sécurité IA)
- Conformité réglementaire RGPD et AI Act : [[cu-020]] (Conformité RGPD & AI Act)
- Souveraineté à l'échelle d'une infrastructure : page Architectures du Hub (A2 propriétaire managé EU, A3 open-source cloud souverain, A4 open-source on-premise)
