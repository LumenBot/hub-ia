# Garde-fous juridiques Hub v2 — v1

**Version** : v1 — 26 mai 2026 (dépôt anticipé sur jalon vendredi 19 juin)
**Statut** : livrable structurant S3.4 — cartographie des obligations juridiques applicables à Hub v2 + premiers réflexes
**Garant** : Cowork Hub Strat — proposé à Cavalli pour validation
**Modules Vianeo activés** : 3 Acceptabilité + 4 Faisabilité/Viabilité
**Périmètre** : 6 volets — AI Act, RGPD/CNIL, DPA fournisseurs LLM, CGV/CGU freemium SaaS, IP contenus utilisateurs, statut side project Cavalli vs QFC

---

## 0. Posture et limites de ce livrable

**Hub Strat ne donne pas de conseil juridique définitif** (règle 7 des instructions projet QFC : « ne pas donner de conseils juridiques ou fiscaux définitifs aux porteurs, orienter vers les experts du réseau »).

Ce document est une **cartographie d'obligations + checklist de premiers réflexes + identification des zones où l'intervention d'un expert juridique est requise**. Aucune formulation de ce document ne se substitue à une consultation avec un avocat compétent en droit du numérique / IP / droit du travail. Le tag **🟧 EXPERT JURIDIQUE REQUIS** marque explicitement les zones où Cavalli doit consulter avant action.

Sources mobilisées : textes officiels (UE AI Act, RGPD), CNIL (recommandations IA + chatbots juillet 2025), CPI français, jurisprudence accessible, cabinets d'avocats spécialisés en droit du numérique. Recherches documentaires datées 26 mai 2026.

---

## 1. Synthèse exécutive

Hub v2 doit composer avec **six volets juridiques** structurants :

1. **AI Act** — Hub v2 est qualifié **système IA à risque limité** (chatbot interactif) → obligation **principale = transparence (informer l'utilisateur que le contenu est généré par IA)**. Pas d'obligations lourdes type évaluation conformité. **Échéance critique : 2 août 2026** pour les systèmes à haut risque déjà identifiés (Hub v2 non concerné mais à surveiller en cas d'évolution produit).
2. **RGPD / CNIL** — base légale recommandée **intérêt légitime** pour développement + amélioration du modèle. Cinq points clés CNIL : finalité claire, base légale documentée, information visible, données minimisées, sécurité adaptée. Recommandations CNIL spécifiques chatbots publiées juillet 2025.
3. **DPA fournisseurs LLM** — Mistral, Anthropic et OpenAI proposent tous des DPA RGPD-compliant avec hébergement EU. **Mistral La Plateforme Enterprise = option la plus mature** (Zero Data Retention, France hosting, RGPD by design).
4. **CGV/CGU freemium SaaS** — distinction CGU (gratuit) vs CGV (payant), limites engagements version Free, **résiliation en ligne obligatoire** (décret 2023-417 + EU Data Act sept 2025 préavis max 2 mois). Coût template prêt-à-l'emploi : 0-500 €.
5. **IP contenus utilisateurs** — en France, **œuvre 100 % IA sans intervention humaine créative n'est pas protégée** par droit d'auteur (L.111-1 CPI). Hub v2 doit clarifier dans ses CGU qui détient quoi sur les chats, artefacts générés, prompts utilisateurs.
6. **Statut side project Cavalli vs QFC** — préparation du dossier d'arbitrage IP (préalable Étape 4, anticipé module 4 fin juillet). **Trois pistes** : side project 100 % personnel, convention QFC (licence/redevance), bascule projet interne QFC. Trois conditions de la vision Hub v2 v1.0 §2.1 à vérifier : pas de conflit d'intérêt opérationnel, transparence d'implication, diffusion compatible.

**Budget juridique estimé Hub v2 phase d'amorçage (Étapes 1-3)** : 1 500-5 000 € (templates CGV/CGU + consultation avocat spécialisé numérique pour validation des points sensibles + premier audit RGPD).

**Risques majeurs identifiés** :

- **Risque #1 — Position QFC sur le side project** : si la direction QFC contestait *a posteriori* le caractère personnel du projet, Hub v2 pourrait se retrouver bloqué juridiquement. **Mitigation : anticiper le dossier IP en module 4** (arbitrage Cavalli 25 mai validé).
- **Risque #2 — Évolution du périmètre produit** : si Hub v2 intègre à terme des fonctionnalités susceptibles de basculer en « haut risque » au sens AI Act (par ex. évaluation/notation de salariés, sélection candidatures), obligations beaucoup plus lourdes. Surveiller la roadmap.
- **Risque #3 — Conformité résiliation Pro tier** : non-respect du préavis max 2 mois EU Data Act = sanctions. À traiter dès Étape 4 (bascule monétisation).

---

## 2. Volet 1 — AI Act (Règlement UE 2024/1689)

### 2.1 Calendrier d'entrée en vigueur

| Date | Échéance | Concerne Hub v2 ? |
|------|----------|---------------------|
| **1er août 2024** | Entrée en vigueur du règlement | Cadre général applicable |
| **2 février 2025** | Interdiction systèmes IA à risque inacceptable (manipulation subliminale, exploitation vulnérabilités, social scoring, etc.) | Non — Hub v2 n'est pas dans ces catégories |
| **2 août 2025** | Règles modèles IA usage général (GPAI) + désignation autorités nationales | Indirectement (fournisseurs LLM Hub v2 sont concernés en amont) |
| **2 août 2026** ⚠️ | Application aux systèmes IA haut risque déjà identifiés (biométrie, infrastructures critiques, éducation, emploi, justice) | Non — Hub v2 n'est pas dans ces catégories ; **mais l'obligation de transparence chatbot s'applique** |
| Possiblement **2 décembre 2027** | Digital Omnibus du Parlement européen propose de reporter cette échéance | À surveiller |
| **2 août 2027** | Systèmes IA haut risque dans produits réglementés (jouets, dispositifs médicaux, machines) | Non |

### 2.2 Classification probable de Hub v2

Hub v2 est un **système IA à risque limité** au sens de l'AI Act :

- Chatbot conversationnel interactif
- Pas de prise de décision automatisée à effet juridique significatif
- Pas d'usage dans biométrie / infrastructure critique / éducation / emploi / justice / etc.

🟧 **EXPERT JURIDIQUE REQUIS** : la classification définitive doit être validée par un avocat avant lancement Étape 3 (MVP). Risque de bascule en « haut risque » si Hub v2 développe certaines fonctionnalités (par ex. évaluation candidats, scoring de performance employés, accompagnement à décision RH).

### 2.3 Obligations Hub v2 en tant que système à risque limité

**Obligation principale** : transparence — l'utilisateur doit être **clairement informé qu'il interagit avec une IA**.

Premiers réflexes Hub v2 :

- Mention visible dès la première interaction : « Vous interagissez avec une IA générative. Les réponses sont susceptibles d'erreur. »
- Étiquetage des contenus générés par IA si re-partagés en dehors de la plateforme (downloads, exports)
- Information dans les CGU sur la nature IA du service
- Disclaimer dans les emails / newsletters automatisés mentionnant la part de génération IA

**Note** : la Plattform Lernende Systeme allemande indique que dès le 2 août 2026, les chatbots doivent être labellisés IA et le contenu généré par IA doit être transparent (cohérent avec l'application au niveau EU).

### 2.4 Obligations transverses pour tout système IA

- **Documentation technique** minimale (architecture, données d'entraînement, modèles utilisés, limites connues) — à constituer dès Étape 2 (MVP)
- **Suivi post-marketing** : mécanisme de signalement d'incidents par les utilisateurs + traitement
- **Évaluation des biais** : démarche démontrable de réduction des biais (genre, origine, etc.) — particulièrement sur les exemples / persona type abordés dans la matière éditoriale

🟧 **EXPERT JURIDIQUE REQUIS** : niveau précis de documentation requise pour un système à risque limité — l'AI Act ne le fixe pas strictement mais la pratique se construit. Échange recommandé avec un avocat spécialisé IA / numérique avant Étape 3.

---

## 3. Volet 2 — RGPD et recommandations CNIL

### 3.1 Cadre général

Hub v2 traite des données à caractère personnel (a minima : emails utilisateurs, contenus des chats, profils déclaratifs) → **RGPD applicable**.

Cinq points clés CNIL (recommandations IA + chatbots, mises à jour juillet 2025) :

1. **Finalité claire** — formuler explicitement pourquoi les données sont collectées
2. **Base légale documentée** — choisir et justifier la base légale (intérêt légitime probablement pour Hub v2)
3. **Information visible** — politique de confidentialité accessible et compréhensible
4. **Données minimisées** — collecter le strict nécessaire
5. **Sécurité adaptée** — mesures techniques et organisationnelles proportionnées au risque

### 3.2 Base légale recommandée

**Pour le développement et l'amélioration du modèle IA** : la CNIL considère que **l'intérêt légitime** est la base la plus adaptée dans la majorité des cas. Le consentement est rarement praticable lorsque les données proviennent de sources multiples.

Intérêts légitimes explicitement reconnus par la CNIL :

- Proposer un service d'agent conversationnel d'assistance aux utilisateurs ✅ (cœur Hub v2)
- Développer un système d'IA de détection de contenus et comportements frauduleux ✅ (modération éventuelle Hub v2)

**Pour la réutilisation des conversations utilisateurs** (fine-tuning, amélioration RAG) : intérêt légitime possible **sous condition de garanties fortes** :

- Information explicite des personnes sur la réutilisation
- **Droit d'opposition discrétionnaire** (l'utilisateur peut s'opposer sans avoir à justifier)
- Limitation du traitement à des données pseudonymisées ou anonymisées
- Pas de réutilisation des données particulièrement sensibles (santé, données pénales, etc.)

🟧 **EXPERT JURIDIQUE REQUIS** : rédaction de la base légale dans la politique de confidentialité + paramétrage de l'opt-out réutilisation des conversations + analyse d'impact relative à la protection des données (AIPD) si nécessaire — à valider avec avocat avant ouverture publique Étape 1 (POC RAG).

### 3.3 Droits des personnes à garantir

| Droit | Action Hub v2 |
|-------|---------------|
| **Information** | Politique de confidentialité claire + bandeau d'information à l'inscription |
| **Accès** | Mécanisme permettant à l'utilisateur de récupérer ses données |
| **Rectification** | Édition possible des informations de profil |
| **Effacement** | Suppression compte + données associées dans délai raisonnable |
| **Limitation** | Possibilité de suspendre temporairement le traitement |
| **Portabilité** | Export des données dans un format machine-lisible |
| **Opposition** | Notamment sur la réutilisation des conversations pour entraînement |
| **Décision automatisée** | Information sur les éventuelles décisions automatisées (non applicable Hub v2 a priori) |

### 3.4 Registre des traitements (Art. 30 RGPD)

Obligatoire dès qu'on traite des données à caractère personnel. Doit lister :

- Nom du responsable du traitement + DPO le cas échéant
- Finalités des traitements
- Catégories de personnes concernées + données collectées
- Destinataires (internes + sous-traitants type fournisseurs LLM)
- Durées de conservation
- Mesures de sécurité

Pour Hub v2 à l'amorçage : registre minimal viable suffit (template gratuit CNIL disponible). À densifier à mesure que les traitements se complexifient.

🟧 **EXPERT JURIDIQUE REQUIS** : désignation d'un DPO obligatoire ou non pour Hub v2 (en principe non requis sauf traitement à grande échelle de données sensibles, ce qui n'est pas le cas en première phase). À reconfirmer avec avocat.

### 3.5 Sous-traitance fournisseurs LLM

Les fournisseurs LLM (Mistral, Anthropic, OpenAI) sont des **sous-traitants** au sens de l'Art. 28 RGPD → Hub v2 doit signer une **DPA (Data Processing Agreement / Addendum au traitement)** avec chacun, et les mentionner dans le registre des traitements. Détail volet 3.

---

## 4. Volet 3 — DPA fournisseurs LLM

### 4.1 Tableau comparatif des options

| Fournisseur | DPA disponible | Hébergement EU | Zero Data Retention | Self-service | Notation Hub Strat |
|-------------|----------------|-----------------|---------------------|--------------|---------------------|
| **Mistral La Plateforme Enterprise** | ✅ Tous clients Enterprise | ✅ France | ✅ disponible | Sur demande commerciale | **Option recommandée pour Hub v2** (souveraineté + RGPD by design + résidence France) |
| **Anthropic Claude for Work / Enterprise** | ✅ Depuis mars 2023 | ✅ EU depuis juin 2024 | ✅ Zero training on customer data | ✅ Depuis janv 2026 (Dashboard Claude → Settings → Legal & Compliance) | Option robuste, hébergement EU + DPA pré-signé self-service |
| **OpenAI ChatGPT Business / Enterprise** | ✅ Depuis 2024 | ✅ Hébergement EU | ✅ No training Enterprise | Sur demande | Option mature mais éditeur US (juridiction extra-EU) |

### 4.2 Recommandation Hub v2

**Pour cohérence avec le narratif souveraineté EU** porté dans la vision produit, et pour réduire l'exposition juridictionnelle extra-EU :

- **LLM principal Hub v2 envisagé : Mistral La Plateforme Enterprise** ou équivalent (Anthropic Claude EU Enterprise en alternative équivalente sur la résidence des données)
- À arbitrer en fonction des capacités techniques nécessaires (capacité de raisonnement, contexte long, multimodalité) — l'équipe technique Hub RAG (canal pair) instruit l'arbitrage technique, Hub Strat l'arbitrage souveraineté/juridique

🟧 **EXPERT JURIDIQUE REQUIS** : relecture des DPA fournisseurs avant signature, en particulier :

- Modalités de transferts hors EU (sous-sous-traitance des fournisseurs)
- Garanties supplémentaires en cas de transfert (clauses contractuelles types, accords adéquation, etc.)
- Modalités de fin de contrat (effacement des données par le fournisseur)
- Responsabilité en cas de violation de données

### 4.3 Architecture de traitement recommandée

```
Utilisateur Hub v2 (FR/EU)
    │ (chat, requête)
    ▼
Hub v2 — backend hébergé EU (Scaleway / OVH / Supabase EU)
    │ (proxy via Agent Gateway)
    ▼
LLM Fournisseur souverain EU (Mistral La Plateforme ou Anthropic EU)
    │ Zero Data Retention activé
    │ DPA signé
    ▼
Réponse → retour utilisateur
```

À documenter dans le registre des traitements + politique de confidentialité.

---

## 5. Volet 4 — CGV/CGU minimum viable freemium SaaS

### 5.1 Distinction CGU (gratuit) vs CGV (payant)

| Document | Statut Hub v2 | Engagements |
|----------|----------------|-------------|
| **CGU** | Tier Free (utilisateurs sans abonnement) | Conditions d'usage, limitations responsabilité, RGPD, IP. **Pas de SLA, pas de support garanti.** |
| **CGV** | Tier Pro 29 €/mois + tier Équipe 19 €/siège/mois + crédits | Engagements contractuels : SLA (disponibilité), modalités paiement, résiliation, support, garanties, recours |

### 5.2 Clauses obligatoires CGV SaaS

| Clause | Contenu |
|--------|---------|
| Identification | Identité juridique Hub v2 (à fixer — entreprise individuelle ? société dédiée ?), siège social, RCS, capital, contact, DPO le cas échéant |
| Objet | Service offert, périmètre, version (Free / Pro / Équipe) |
| Tarification | Montant, mode de facturation (mensuel / annuel / pré-payé), pro-rata entrée/sortie, conséquences non-paiement |
| **SLA** | Disponibilité (99 % minimum recommandé), délais correction incidents, hotline / support |
| Limitation de responsabilité | Plafond = montants payés sur les 12 derniers mois (pratique courante SaaS) |
| Données personnelles | Renvoi vers politique de confidentialité conforme RGPD |
| **Résiliation** ⚠️ | **Résiliation en ligne obligatoire** (décret 2023-417) + **préavis max 2 mois** (EU Data Act sept 2025) — clauses de 6 mois ou résiliation par lettre recommandée = **non conformes** |
| Propriété intellectuelle | Qui possède quoi (volet 5) |
| Modification | Modalités de modification des CGV (préavis, accord tacite ou exprès) |
| Force majeure | Clause classique |
| Litiges | Médiation préalable + juridiction (Tribunal de commerce français recommandé) + droit applicable (droit français) |

### 5.3 Spécificités modèle freemium

- **Pas de SLA sur le tier Free** : clarifier dans les CGU que le tier Free est fourni « tel quel », sans garantie de disponibilité ni de support
- **Incitations à l'upgrade** légales et transparentes : pas de dark patterns (par ex. mise en avant trompeuse du tier payant)
- **Limites du tier Free claires** : nombre de chats/jour, fonctionnalités, durée
- **Transition Free → Pro fluide** : process d'inscription Pro doit être clair, prix affichés TTC + HT, conditions de prélèvement transparentes

### 5.4 Mise à disposition opérationnelle

Trois options pour produire les CGV/CGU :

| Option | Coût | Délai | Recommandation Hub Strat |
|--------|------|-------|--------------------------|
| **Template gratuit générique** (CNIL, Donnéespersonnelles.fr, Swapn) | 0 € | 1-2 jours | Risquée — pas adaptée IA/SaaS, dispositions à compléter manuellement |
| **Template personnalisé** (Legalplace, LegalStart, Captain Contrat, WebLegal.ai) | 50-300 € | 1 semaine | **Recommandé pour amorçage** Étape 3 (MVP) — bon ratio coût/qualité |
| **Rédaction sur-mesure** par avocat spécialisé numérique | 1 000-2 500 € | 2-4 semaines | Recommandé avant Étape 4 (monétisation Pro) — investissement à amortir sur la commercialisation |

🟧 **EXPERT JURIDIQUE REQUIS** : relecture finale des CGV/CGU avant ouverture Pro tier (Étape 4) — qu'elle que soit l'option retenue. Coût ~500-1 000 € pour une relecture.

---

## 6. Volet 5 — Propriété intellectuelle des contenus utilisateurs

### 6.1 Cadre juridique français

**Article L.111-1 du Code de la Propriété Intellectuelle (CPI)** : seul l'auteur, défini comme **personne physique**, peut revendiquer une protection pour une œuvre de l'esprit.

**Conséquence pour Hub v2** :

- Les **réponses générées à 100 % par l'IA** (sans intervention humaine créative) **ne sont pas protégées** par le droit d'auteur en France
- Les **contenus produits avec intervention humaine créative** (prompts élaborés, retouches, itérations significatives) **peuvent l'être** au nom de l'utilisateur, sous certaines conditions

### 6.2 Trois questions à trancher dans les CGU Hub v2

#### Question A — Qui détient les conversations ?

Trois options :

| Option | Avantages | Inconvénients |
|--------|-----------|---------------|
| Utilisateur détient ses conversations | Confiance utilisateur, conformité RGPD facilitée | Hub v2 ne peut pas réutiliser pour amélioration sans opt-in |
| Hub v2 détient les conversations | Réutilisation facilitée pour amélioration produit | Friction utilisateur, méfiance, freine adoption |
| **Co-titularité avec usage limité Hub v2** (recommandé) | Compromise équilibré | Rédaction CGU plus complexe |

**Recommandation Hub v2** : **l'utilisateur reste titulaire de ses conversations**, et **Hub v2 obtient une licence d'usage limitée** pour : (i) fourniture du service, (ii) amélioration du produit sous condition de pseudonymisation/anonymisation + droit d'opposition discrétionnaire (cf. CNIL §3.2).

#### Question B — Qui détient les artefacts générés (PDFs, livrables Pro) ?

Trois options similaires. **Recommandation Hub v2** : **l'utilisateur détient les artefacts générés au sein de son compte**, Hub v2 conserve un usage interne anonymisé pour amélioration produit. L'utilisateur peut télécharger, partager, réutiliser librement les artefacts générés.

#### Question C — Que faire des prompts utilisateurs élaborés ?

Certains utilisateurs vont passer du temps à élaborer des prompts complexes (en particulier les consultants senior — persona E1). Ces prompts ont une valeur créative.

**Recommandation Hub v2** : **les prompts utilisateurs sont leur propriété**. Hub v2 peut les utiliser de manière anonymisée pour améliorer le produit, mais ne peut pas les partager ou les revendre. Permettre l'export des prompts (« mes prompts » dans le compte).

### 6.3 Contenu source Hub v2 (matière éditoriale)

La matière éditoriale curated Hub Content (base RAG, articles, fiches outils, etc.) est protégée par droit d'auteur au nom des contributeurs (Cavalli et éventuels co-rédacteurs). À documenter dans les CGU Hub v2 :

- Réutilisation des contenus Hub v2 par les utilisateurs : autorisée pour usage interne (entreprise utilisatrice), interdite pour redistribution commerciale
- Citation autorisée avec attribution Hub v2

🟧 **EXPERT JURIDIQUE REQUIS** : rédaction précise des clauses IP CGU + cohérence avec arbitrage statut side project Cavalli vs QFC (volet 6). Coût ~500-1 500 €.

---

## 7. Volet 6 — Statut side project Cavalli vs salariat QFC

⚠️ **Volet le plus structurant pour Hub v2.** Préparation directe du dossier d'arbitrage IP (préalable Étape 4, anticipé module 4 fin juillet — arbitrage Cavalli 25 mai validé).

### 7.1 Cadre juridique français — droits du salarié hors mission

**Principes posés par la jurisprudence et le Code du travail / CPI** :

- **Œuvres de l'esprit créées par un salarié hors mission** : le salarié reste **titulaire initial** du droit d'auteur, **sauf clause contraire** dans le contrat de travail
- **Inventions hors mission** : le salarié reste **propriétaire**, mais l'employeur dispose d'un **droit de préemption** pour acquérir tout ou partie des droits attachés
- **Obligation de loyauté** : même en l'absence de clause expresse, le salarié est tenu à la **non-concurrence active** vis-à-vis de son employeur **pendant la durée du contrat**. Mais cette obligation **n'interdit pas la préparation d'une activité** entrepreneuriale qui pourrait s'exercer après ou en parallèle, tant que pas de concurrence active déloyale
- **Clause de non-concurrence post-contrat** : pour être valable, doit être limitée dans le temps, l'espace, le secteur, et indemnisée financièrement

### 7.2 Cas spécifique Cavalli — premier état des lieux

À vérifier en consultation directe du contrat de travail Cavalli avec QFC / Quai Alpha (que Hub Strat n'a pas en sa possession — ce travail est à mener par Cavalli) :

| Question | Réponse à obtenir |
|----------|--------------------|
| **Q1** — Le contrat de travail Cavalli contient-il une clause de cession des droits d'auteur sur les œuvres créées hors mission ? | À vérifier par Cavalli |
| **Q2** — Le contrat contient-il une clause de non-concurrence (générique ou spécifique IA / accompagnement startups) ? | À vérifier par Cavalli |
| **Q3** — Le contrat ou l'accord QFC contient-il une clause de partage de propriété sur les inventions / innovations créées par les SUM ? | À vérifier par Cavalli |
| **Q4** — Y a-t-il une procédure formelle QFC pour déclarer un projet personnel d'innovation ? | À vérifier auprès de QFC |
| **Q5** — Hub v2 utilise-t-il des matières produites dans le cadre du contrat QFC (Guide Métier SUM, méthodes Vianeo, contenus formation) ? | **Réponse partielle** : la méthodologie Vianeo est sous licence externe ; la matière éditoriale Hub v2 actuelle ([base RAG, modules, fiches outils]) est-elle considérée comme apport personnel Cavalli ou production QFC ? **À arbitrer explicitement avec QFC** (cf. Vision Hub v2 §2.2) |

### 7.3 Trois pistes de structuration

#### Piste A — Side project 100 % personnel Cavalli
**Conditions de viabilité** :

- Contrat de travail Cavalli sans clause de cession IP étendue hors mission ✅ (à vérifier)
- Aucune utilisation de matière produite dans le cadre QFC sans accord ✅ (probable pour la matière originale Hub IA mais à confirmer)
- Activité Hub v2 menée hors temps de travail ✅
- Information transparente à la direction QFC (recommandée mais pas nécessairement obligatoire avant un seuil)

**Avantages** : autonomie maximale Cavalli, agilité produit, fiscalité personnelle simple (micro-entreprise possible jusqu'à 77 700 €/an de CA en BIC services 2026)
**Inconvénients** : si succès commercial, risque de revendication QFC *a posteriori* sur la matière sourcée

#### Piste B — Convention QFC à formaliser (licence / redevance / co-portage)
**Mécanique** :

- Cavalli reste porteur opérationnel Hub v2
- QFC obtient un droit d'usage / partage de revenus sur la matière éditoriale partiellement issue du cadre QFC, en échange d'une licence claire
- Possibilité de co-portage : QFC bénéficie d'un accès Pro Hub v2 pour son réseau d'incubés/alumni

**Avantages** : sécurise juridiquement, permet diffusion écosystème QFC qui est un canal d'acquisition fort (H4 persona)
**Inconvénients** : négociation à mener, dilution potentielle de la liberté produit Cavalli

#### Piste C — Bascule projet interne QFC
**Mécanique** :

- Hub v2 devient un produit interne QFC, Cavalli en est le porteur salarié, propriété QFC

**Avantages** : levée de tous les risques juridiques personnels Cavalli
**Inconvénients** : perte d'autonomie entrepreneuriale, dépendance aux arbitrages internes QFC, fiscalité salariée, valorisation patrimoniale réduite

### 7.4 Recommandation Hub Strat — préparation du dossier d'arbitrage

Le dossier d'arbitrage IP (livrable module 4, anticipé fin juillet) devra comprendre :

1. **Cartographie de la matière Hub v2** : qu'est-ce qui est apport personnel Cavalli (à dater + tracer), qu'est-ce qui pourrait être considéré comme apport QFC (Guide Métier SUM contenus, etc.), qu'est-ce qui est zone grise
2. **Synthèse contrat de travail Cavalli** : extraits des clauses pertinentes (IP, non-concurrence, exclusivité, etc.)
3. **Positionnement des 3 pistes** : avantages / inconvénients quantifiés (charge fiscale, autonomie, sécurité juridique, valorisation)
4. **Recommandation Cavalli + proposition de mécanique** pour la piste retenue
5. **Plan de transmission à la direction QFC** : timing, support, interlocuteurs

🟧 **EXPERT JURIDIQUE REQUIS** : avocat spécialisé droit du travail + droit du numérique, idéalement avec expérience accompagnement de salariés-entrepreneurs (cabinets type Aklea, Bersay, Dunaud-Clarenc-Combles). Coût ~1 500-3 000 € pour analyse + recommandation structurée. **À engager dès juin** si possible — c'est un préalable structurant à toute communication externe Hub v2.

### 7.5 Trois conditions de la vision Hub v2 v1.0 §2.1 — état des lieux

| Condition | État actuel | Action requise |
|-----------|-------------|----------------|
| 1. Pas de conflit d'intérêt opérationnel (Hub v2 ne capte pas les prospects QFC, ne détourne pas les ressources, n'utilise pas le contenu éditorial QFC comme matière commerciale sans accord) | ⚠️ Zone grise sur la matière éditoriale Hub v2 (vs Guide Métier QFC) | Cartographier précisément la matière (dossier IP) + arbitrer cas par cas |
| 2. Transparence d'implication (information direction QFC le moment venu) | ⚠️ Pas encore réalisée | Anticiper l'échange avec direction QFC sur base du dossier IP — calendrier recommandé : août-septembre 2026 |
| 3. Diffusion compatible (version freemium Hub v2 diffusable dans l'écosystème QFC) | ✅ Cohérent vision | À formaliser dans la convention QFC si piste B retenue |

---

## 8. Carnet de questions pour expert juridique (briefing avocat)

Liste consolidée des questions à poser lors de la consultation avocat spécialisé droit du numérique + droit du travail :

### Bloc AI Act
1. Confirmer la classification Hub v2 en système IA à risque limité — quels critères précis ?
2. Quel niveau de documentation technique recommandé pour Hub v2 Étape 3 ?
3. Quelles fonctionnalités produit envisageables pourraient basculer Hub v2 en « haut risque » au sens AI Act ?

### Bloc RGPD / CNIL
4. Hub v2 doit-il désigner un DPO (Data Protection Officer) à l'Étape 3 (MVP) ou Étape 4 (commercialisation) ?
5. Une AIPD (Analyse d'Impact relative à la Protection des Données) est-elle requise avant lancement ?
6. Comment formuler concrètement la base légale « intérêt légitime » dans la politique de confidentialité ?
7. Quel mécanisme technique pour l'opt-out de la réutilisation des conversations conforme aux exigences CNIL ?

### Bloc DPA fournisseurs LLM
8. Relire la DPA Mistral La Plateforme Enterprise et Anthropic Claude — points d'attention ?
9. Quel niveau de garantie nécessaire sur la sous-sous-traitance (cas où le fournisseur LLM utiliserait lui-même des services tiers) ?

### Bloc CGV/CGU
10. Validation des CGV/CGU produites par template + ajustements spécifiques Hub v2 ?
11. Conformité résiliation EU Data Act (préavis max 2 mois, en ligne) — formulation type ?

### Bloc IP utilisateurs
12. Rédaction des clauses IP Hub v2 (qui détient quoi : conversations, artefacts, prompts, contenus source) ?
13. Conformité avec la position française sur IA générative (L.111-1 CPI) ?

### Bloc statut side project (priorité)
14. Analyse du contrat de travail Cavalli — risque sur les œuvres et inventions hors mission ?
15. Y a-t-il un seuil d'activité side project à partir duquel l'information employeur devient impérative ?
16. Quelle structure juridique recommandée pour Hub v2 (micro-entreprise / EURL / SASU) au stade actuel ?
17. Quelles conventions / accords formaliser avec QFC en cas de piste B (licence / redevance) ?
18. Si Hub v2 devient un succès commercial, quelle protection contre une revendication *a posteriori* de QFC sur la matière ?

**Budget consultation recommandé** : 1 500-3 000 € pour une consultation initiale 4-6 heures avec briefing + analyse contrat + recommandations écrites.

---

## 9. Calendrier de mise en conformité par étape Hub v2

| Étape | Échéance | Obligations à respecter | Budget juridique cumulé estimé |
|-------|----------|-------------------------|--------------------------------|
| **Étape 0** | En cours | Néant (POC interne, pas d'utilisateurs externes) | 0 € |
| **Étape 1** — POC RAG | Sem 1-2 juin 2026 | Information utilisateurs sur usage IA + base légale intérêt légitime + DPA fournisseur LLM + mention chatbot IA | ~500-1 000 € (template CGU + audit RGPD léger) |
| **Étape 2** — MVP avec onboarding | Sem 24-26 juin | Politique de confidentialité complète + registre traitements + droits utilisateurs opérationnels + CGU Free tier | +500-1 000 € |
| **Étape 3** — MVP commercialisable | 5-8 mois | CGV Pro tier + résiliation conforme + IP CGU + AIPD si requise + dossier conformité AI Act | +1 500-3 000 € (incluant relecture avocat) |
| **Étape 4** — Bascule Pro | 8-12 mois | **🟧 DOSSIER IP CAVALLI vs QFC** (préalable validé) + relecture finale CGV avocat + structure juridique Hub v2 (entreprise dédiée si justifié) | +2 000-4 000 € (avocat IP + structure juridique) |
| **Étape 5** — Tier Équipe + diffusion QFC | 10-18 mois | Convention QFC formalisée + CGV B2B Équipe + DPA propres à Hub v2 (Hub v2 devient sous-traitant pour ses clients Équipe) | +1 000-2 000 € |

**Total budget juridique estimé sur 18 mois** : **5 500-11 000 €**.

---

## 10. Bloc résumé exécutif transmissible (auto-imposé §8.1.7)

> **À copier-coller pour notification autonome aux canaux pairs ou à DEV IA Head.**
>
> ---
>
> **Garde-fous juridiques Hub v2 v1 — 26 mai 2026 — synthèse**
>
> Six volets juridiques cartographiés pour Hub v2 : **AI Act** (Hub v2 = système IA à risque limité → obligation transparence chatbot, échéance principale 2 août 2026), **RGPD/CNIL** (base légale intérêt légitime recommandée, 5 points clés CNIL chatbots juillet 2025), **DPA fournisseurs LLM** (Mistral La Plateforme Enterprise = option mature souveraine, alternatives Anthropic EU et OpenAI EU), **CGV/CGU freemium SaaS** (conformité résiliation EU Data Act sept 2025 préavis 2 mois, distinction CGU/CGV stricte), **IP contenus utilisateurs** (œuvre 100% IA non protégée L.111-1 CPI, recommandation co-titularité), **statut side project Cavalli vs QFC** (volet le plus structurant, dossier d'arbitrage anticipé module 4 fin juillet).
>
> **Budget juridique estimé Hub v2 sur 18 mois : 5 500-11 000 €** échelonné par étape.
>
> **Trois risques majeurs identifiés** : (1) position QFC sur side project — anticipation dossier IP impérative ; (2) évolution périmètre produit susceptible de basculer en haut risque AI Act ; (3) conformité résiliation Pro tier (EU Data Act). Mitigation actée sur chacun.
>
> **18 questions consolidées pour briefing avocat** spécialisé droit numérique + droit du travail. Consultation recommandée dès juin (~1 500-3 000 €) — préalable structurant à toute communication externe Hub v2.
>
> Source complète : `Canaux/Hub-Strat/outputs/garde-fous-juridiques-hub-v2-v1.md`

---

## 11. Check pré-livrable §8.1 — application

1. **Étanchéité QFC** ✅ — aucune startup réelle nommée. Le volet 6 traite la relation Cavalli ↔ QFC mais ne révèle aucun élément confidentiel QFC (matière publique sur le statut salarié + Vision Hub v2 v1.0 déjà partagée en interne).
2. **Modules Vianeo cohérents** ✅ — module 3 (Acceptabilité, conditions juridiques de l'offre) + module 4 (Faisabilité/Viabilité, structure juridique). Respect règles cohérence inter-modules v1.1.
3. **Sources citées et vérifiables** ✅ — textes officiels UE + CNIL + sites cabinets avocats spécialisés (§13).
4. **Pas de substitution à l'arbitrage Cavalli** ✅ — posture explicitée §0, tag 🟧 EXPERT JURIDIQUE REQUIS sur 7 zones, recommandation finale toujours soumise à validation avocat.
5. **Impacts autres canaux signalés** ✅ — Hub Content (clauses IP sur la matière éditoriale), Hub RAG (architecture de traitement données + fournisseur LLM), Claude Design (UX de l'opt-out réutilisation conversations + bandeau transparence chatbot), DEV IA Head (pattern transverse possible sur P15 — résolution complète du trou produit-commercial).
6. **Versioning explicite** ✅ — v1 + historique §14.
7. **(Auto-imposé) Bloc résumé exécutif transmissible** ✅ — §10.

---

## 12. Zones à creuser (itération v1.1 ou v2)

- **Suivi Digital Omnibus** : confirmation du report éventuel de l'échéance 2 août 2026 vers 2 décembre 2027
- **Suivi recommandations CNIL** : nouvelles publications post-juillet 2025 sur IA et chatbots
- **Veille jurisprudence** : premières décisions sur IP IA générative en France (post-procès NYT vs OpenAI US)
- **Approfondissement convention QFC** (piste B) : modélisation d'une licence / redevance équitable
- **Étude comparée fournisseurs LLM EU émergents** (Mistral, Aleph Alpha post-Cohere, autres) sur leurs DPA et garanties
- **Étude impact du fork EU-IA Act** au cas où le Digital Omnibus modifie significativement le calendrier — implications pour la roadmap Hub v2

---

## 13. Sources mobilisées

### Textes officiels UE
- [Direction générale des Entreprises — Règlement IA UE 2024/1689](https://www.entreprises.gouv.fr/decryptages-de-nos-experts/le-reglement-europeen-sur-lintelligence-artificielle-publics-concernes)
- [Implementation Timeline — EU AI Act service desk](https://ai-act-service-desk.ec.europa.eu/en/ai-act/timeline/timeline-implementation-eu-ai-act)
- [EU AI Act — implementation timeline officiel](https://artificialintelligenceact.eu/implementation-timeline/)
- [WEnvision — AI Act report échéance août 2026](https://www.wenvision.com/fr/articles/ai-act-report-echeance-aout-2026-systemes-ia-haut-risque/)
- [DC NUMERIQUE — AI Act calendrier complet entreprises FR](https://dcnumerique.fr/ai-act-calendrier-entreprise/)

### CNIL — recommandations IA et chatbots
- [CNIL — Développement des systèmes d'IA : recommandations RGPD](https://www.cnil.fr/fr/developpement-des-systemes-dia-les-recommandations-de-la-cnil-pour-respecter-le-rgpd)
- [CNIL — Chatbots : conseils pour respecter les droits des personnes](https://www.cnil.fr/fr/chatbots-les-conseils-de-la-cnil-pour-respecter-les-droits-des-personnes)
- [CNIL — IA et RGPD : nouvelles recommandations 2025](https://www.cnil.fr/fr/ia-et-rgpd-la-cnil-publie-ses-nouvelles-recommandations-pour-accompagner-une-innovation-responsable)
- [CNIL — Recommandations sur l'intérêt légitime développement IA](https://www.cnil.fr/fr/recommandations-developpement-ia-interet-legitime)
- [CNIL + HAS — Guide pratique IA mars 2026](https://www.cnil.fr/sites/default/files/2026-03/guide_has_cnil_recommandations_ia.pdf)

### DPA fournisseurs LLM
- [Tendances IA PME — Zero Data Retention IA entreprise 2026](https://www.tendancesiapme.fr/blog/zero-data-retention-zdr-ia-entreprise-2026/)
- [Leto Legal — ChatGPT et RGPD 2026 DPA](https://www.leto.legal/guides/intelligence-artificielle-chatgpt-et-rgpd)
- [Leto Legal — Claude Anthropic RGPD conformité 2026](https://www.leto.legal/guides/claude-anthropic-rgpd-conformite-2026)
- [Mister IA — IA sécurisée entreprise ChatGPT Claude Mistral](https://www.mister-ia.com/article/ia-la-plus-securisee)

### CGV/CGU SaaS freemium
- [Wilhow — CGV logiciel SaaS structuration](https://wilhow.fr/blog/juridique/cgv-logiciel-saas-licence/)
- [Legalplace — Rédiger CGV logiciel SaaS](https://www.legalplace.fr/guides/cgv-logiciel-saas/)
- [Captain Contrat — CGU Conditions générales utilisation 2026](https://www.captaincontrat.com/contrats-commerciaux-cgv/cgv-cgu-cga/cgu-conditions-generales-utilisation)
- [Données personnelles — CGV modèle gratuit conforme 2026](https://www.donneespersonnelles.fr/conditions-generales-vente)
- [1D-D1 — CGV CGU structure minimale testée 2025](https://www.1d-d1.io/cgv-cgu-modeles-conformes-site/)

### IP contenu IA générative
- [Dreyfus avocats — Propriété contenus IA défi droit auteur](https://www.dreyfus.fr/en/2025/08/13/ownership-of-ai-generated-content-a-challenge-for-copyright-law/)
- [August Debouzy — ChatGPT IA contenu protégé](https://www.august-debouzy.com/fr/blog/1898-chat-gpt-une-ia-peut-elle-donner-naissance-a-un-contenu-protege)
- [Franklin Paris — IP law implications ChatGPT](https://www.franklin-paris.com/en/news-en/a-closer-look-at-the-ip-law-implications-of-chatgpt/)
- [Sigma — IA obligations conformité entreprises 2026](https://www.sigma.fr/publications/blog/data-ia/ia-obligations-reglementation-entreprises/)

### Statut side project / salarié
- [Village Justice — Propriété intellectuelle et non-concurrence du salarié](https://www.village-justice.com/articles/propriete-intellectuelle-non-concurrence-salarie,28641.html)
- [Lexbase — Clauses propriété intellectuelle contrat de travail](https://www.lexbase.fr/article-juridique/105960736-pratique-professionnelle-les-clauses-de-propriete-intellectuelle-dans-le-contrat-de-travail)
- [Coin des entrepreneurs — Création entreprise par salarié](https://www.lecoindesentrepreneurs.fr/creation-entreprise-concurrente-par-salarie-ou-ancien-salarie/)
- [CCI Paris Île-de-France — Salarié peut-il être empêché d'entreprendre](https://www.entreprises.cci-paris-idf.fr/fiches-pratiques/le-salarie-peut-il-etre-empeche-dentreprendre)
- [Pacaud Avocat — Inventions employés propriété intellectuelle](https://www.pacaud-avocat.fr/en/blog/employer-works-inventions-employees-intellectual-property)
- [Assistant juridique — Créer son entreprise en étant salarié](https://www.assistant-juridique.fr/concurrence_employeur.jsp)

---

## 14. Historique de versions

| Date | Version | Modification |
|------|---------|--------------|
| 26 mai 2026 | v1 | Création initiale — 6 volets cartographiés (AI Act, RGPD/CNIL, DPA fournisseurs LLM, CGV/CGU freemium, IP utilisateurs, statut side project Cavalli vs QFC). 18 questions consolidées pour briefing avocat. Budget juridique estimé 5 500-11 000 € sur 18 mois. Dépôt anticipé sur jalon vendredi 19 juin (S3.4). Préparation directe du dossier d'arbitrage IP (module 4 anticipé fin juillet). |

---

*Livrable structurant Hub Strat — version v1, validation Cavalli attendue avant transmission croisée. Posture règle 7 respectée : Hub Strat cartographie, l'expert juridique tranche. Sept zones explicitement marquées 🟧 EXPERT JURIDIQUE REQUIS.*
