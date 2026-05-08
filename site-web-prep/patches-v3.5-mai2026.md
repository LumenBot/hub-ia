# Patches v3.5 — Hub IA Learning Center (mai 2026)

> Matière éditoriale consolidée pour intégration par Claude Code en v3.5. Liste tous les patches : refresh chiffres macro, intégration 5 RetEx Bpifrance Le Lab, ajout 4 fiches outils + nouvelle catégorie « Navigateurs agentiques », tagging architectures sur 5 modules sensibles, update PR-01 avec checklist diagnostic projet en cours, fixes UX.

**Note d'intégration** : la page `architectures.html` est livrée séparément en HTML complet dans `mockup/architectures.html`. Les autres patches sont à appliquer sur les pages existantes selon les indications ci-dessous.

---

## 0. Fixes UX prioritaires (à traiter avant le reste)

### 0.1 Harmonisation du head banner sur toutes les pages
**Problème** : la page `prealables.html` et les sous-pages PR utilisent un head banner différent du reste du site.

**Action** : appliquer sur toutes les pages le **layout du `nav` de `index.html`** :
- Titre « Hub IA — Learning Center » aligné à gauche
- Logo QFC centré (zone centrale)
- Menu de navigation aligné à droite

Conserver l'ordre des liens : **Préalables → Architectures → Modules → Ressources → À propos**.

### 0.2 Padding head banner sur la page Préalables
**Problème** : le head banner masque partiellement le titre principal de `prealables.html`.

**Action** : ajouter un `padding-top` cohérent sur le hero `.prealables-hero` (au moins équivalent à la hauteur du nav fixé). Vérifier que le même problème n'existe pas sur `architectures.html` et corriger si besoin.

### 0.3 Reformulation du titre de la section Préalables
**Avant** :
```html
<h1>Préalables / Pré-requis à l'intégration de l'IA</h1>
```

**Après** :
```html
<h1>Avant de te lancer dans un projet IA</h1>
```

À mettre à jour sur :
- `prealables.html` (h1 du hero)
- Toutes les références dans la nav, le footer, l'index.html, les autres pages préalables (titre `<title>` + breadcrumb « Retour aux préalables »)

### 0.4 Suppression du jargon « PR-XX » côté UX visible
**Problème** : la numérotation PR-01 → PR-06 est affichée dans les cards d'index, dans les hero des sous-pages, dans les sommaires. C'est du jargon technique qui n'apporte rien à l'utilisateur.

**Action** :
- **Conserver** les noms de fichiers `pr-01-*.html` à `pr-06-*.html` (pour la traçabilité technique et les liens internes existants)
- **Supprimer** les badges visibles « ⚡ Préalable PR-01 », « ⚡ Préalable PR-02 », etc. dans les hero des 6 sous-pages
- **Remplacer dans `prealables.html`** les tags `<div class="pr-card-num">PR-01</div>` à `<div class="pr-card-num">PR-06</div>` par le nom de la rubrique (ex : « Maturité organisationnelle ») ou simplement par un emoji/icône cohérent
- **Adapter les sommaires internes** des PR (ex : « 1. Le constat 94 % d'échec ») pour qu'ils n'utilisent plus le préfixe « PR-01 » nulle part

Pour les badges hero, possibilité de remplacer par `⚡ Cadrage` ou `⚡ Préalable` simple sans numéro.

### 0.5 Mise à jour de la rubrique « À propos »
**Problème** : la rubrique parle de « 2 niveaux complémentaires » (Modules + Ressources) alors qu'on en a maintenant **4** (Préalables + Architectures + Modules + Ressources).

**Action** : reformuler le paragraphe de présentation sur la home (`index.html#a-propos`) et la page À propos si elle existe en page séparée. Format suggéré :

> Le Hub IA — Learning Center est une initiative portée par Quest for Change, à destination de ses incubateurs territoriaux, des startups accompagnées et de leurs alumni, des partenaires institutionnels, et des entreprises du territoire au sens large.
>
> L'objectif : disséminer les connaissances autour des enjeux et applications de l'IA, au service du développement économique territorial et de la compétitivité de nos entreprises.
>
> Le site s'organise en **4 niveaux complémentaires** :
> 1. **Préalables** — qu'est-ce que je dois maîtriser avant de me lancer ?
> 2. **Architectures** — quel pattern d'implémentation choisir pour mon cas d'usage ?
> 3. **Modules** — comment résoudre concrètement mon problème métier avec l'IA ?
> 4. **Ressources** — quels outils utiliser pour ma stack ?
>
> Le savoir ne devrait pas être une ressource exclusive. Seule l'exécution compte.
>
> **Contact** : [blaise.cavalli@questforchange.eu](mailto:blaise.cavalli@questforchange.eu)

---

## 1. Refresh chiffres macro

### 1.1 Page d'accueil (`index.html`) — chiffre choc principal

**Action** : remplacer le chiffre AdvisoryX/DXC actuel (94 %) par la version MIT mieux sourcée.

**Avant** :
> 94 % des projets IA échouent malgré 77 % de priorité dirigeants (étude AdvisoryX/DXC).

**Après** :
> **95 % des investissements IA n'ont produit aucun retour mesurable** (MIT « State of AI in Business 2025 », cité par Claranet janvier 2026). En cause : non pas la technologie mais l'intégration — vision floue, gouvernance fragile, décalage outils/usages. **Seuls 5 % atteignent la production à grande échelle.** Avant de te lancer, parcours les [Préalables](prealables.html) et choisis ton [pattern d'architecture](architectures.html).

**Source** : Claranet janvier 2026 — https://www.claranet.com/fr/blog/ia-en-entreprise-bonnes-pratiques-et-pieges-eviter-en-2026/

### 1.2 Page d'accueil — second chiffre choc complémentaire

**Action** : ajouter un second encart juste après ou en alternance, mettant en avant l'opportunité.

**Contenu** :
> **Productivité ×5** dans les secteurs très exposés à l'IA, **77 000 offres d'emploi** exigeant des compétences IA en France en 2023 (×7 vs 2018), **prime salariale +25 %** en moyenne. **+270 % de ROI moyen** documenté sur les projets IA bien exécutés (étude Microsoft / Sigma 2025), **3,7×** sur Copilot (étude IDC 31 000 collaborateurs / 31 pays).
>
> Le marché ne va pas attendre — le Hub IA donne les clés concrètes pour s'y mettre.

**Sources** : PwC AI Jobs Barometer 2024, Sigma livre blanc 2025 (Microsoft), IDC.

### 1.3 PR-04 « Marché IA & emploi » — encart « Tendances 2026 »

**Action** : ajouter une section ou un encart « Tendances macro 2026 » dans `prealables/pr-04-marche-ia-emploi.html`, idéalement juste après la section 2 « Le marché de l'emploi IA explose ».

**Contenu suggéré** :
```html
<section class="module-section">
  <div class="module-section-header">
    <div class="module-section-icon icon-flow">2bis</div>
    <h2 class="module-section-title">Tendances macro 2026 — la dynamique s'accélère</h2>
  </div>

  <p>Synthèse de chiffres convergents (Bpifrance Le Lab juin 2025, PwC, Deloitte, KPMG, Statworx, Vention) qui cadrent l'ampleur du mouvement IA en 2026.</p>

  <h3>Marché et adoption</h3>
  <ul>
    <li><strong>Marché IA software</strong> : 174 Md$ en 2025 → <strong>467 Md$ en 2030</strong> (CAGR ~22 %, ABI Research)</li>
    <li><strong>Spend total IA mondial</strong> : 1,5 T$ en 2025 → <strong>2 T$ en 2026</strong> → 3,3 T$ en 2029 (Gartner)</li>
    <li><strong>93 % des entreprises mondiales</strong> utilisent l'IA (80 % directement, 13 % via vendor) — Vention 2026</li>
    <li><strong>France spécifiquement</strong> : 25 % entreprises FR utilisent IA gen vs <strong>37 % EU moyenne</strong> (BEI déc 2025) ; <strong>26 %</strong> PME/ETI FR (Bpifrance Le Lab juin 2025)</li>
  </ul>

  <h3>ROI et valeur économique</h3>
  <ul>
    <li><strong>+270 % ROI moyen</strong> sur projets IA bien exécutés (étude Microsoft / Sigma 2025)</li>
    <li><strong>3,7× ROI</strong> sur Copilot (étude IDC nov 2024 sur 31 000 collaborateurs / 31 pays)</li>
    <li><strong>+1,3 point de PIB par an d'ici 2034</strong> en France grâce à l'automatisation IA (Bpifrance Le Lab juin 2025, étude OCDE)</li>
    <li><strong>+11 à +37 % de productivité en Europe d'ici 2030</strong> (Commission AIDA UE)</li>
    <li>Mais <strong>seulement 19 %</strong> des organisations Vention 2025 ont vu un ROI IA &gt; 5 % à court terme — confirmant l'enjeu d'exécution</li>
  </ul>

  <h3>Workforce et formation</h3>
  <ul>
    <li><strong>WEF Future of Jobs 2025</strong> : net-positif global, 2 des 3 jobs en plus forte croissance sont IA-related</li>
    <li><strong>Coursera</strong> : enrollments cours GenAI <strong>+195 % YoY</strong> en juin 2025, 8 M+ apprenants dans le monde</li>
    <li><strong>KPMG</strong> : <strong>83 %</strong> des professionnels intéressés par formation IA, mais seulement <strong>21 %</strong> s'évaluent comme « high knowledge » — gap massif</li>
  </ul>

  <h3>Agents IA et agentique</h3>
  <ul>
    <li><strong>96 %</strong> des entreprises EU prévoient d'accroître leurs usages des agents IA dans 12 mois (ActuIA)</li>
    <li><strong>Gartner</strong> : <strong>&lt; 1 % d'apps agentiques en 2024 → 33 % d'ici 2028</strong></li>
    <li><strong>Cisco</strong> : <strong>68 % des interactions service client</strong> seront gérées de bout en bout par IA agentique d'ici 2028</li>
    <li><strong>Marché agents IA</strong> : 7 Md$ en 2025 → <strong>93 Md$ en 2032</strong></li>
  </ul>
</section>
```

**Sources** :
- Bpifrance Le Lab juin 2025 — https://lelab.bpifrance.fr/content/download/4745/pdf/2025-06_L%27IA%20dans%20les%20PME%20et%20ETI%20fran%C3%A7aises_Etude%20Bpifrance%20Le%20Lab.pdf
- Sigma livre blanc 2025 — https://www.informatiquenews.fr/wp-content/uploads/2025/06/Livre_Blanc_Embarquer_IA_entreprise.pdf
- Vention State of AI 2026 — https://ventionteams.com/solutions/ai/report

### 1.4 Section À propos — encart digitalisation

**Action** : ajouter dans la rubrique À propos (ou en encart sur PR-02 Préalables data & SI) le chiffre Bpifrance Le Lab sur la séquence digitalisation → data → IA.

**Contenu suggéré** :
> **76 % des PME et ETI françaises ont engagé leur transformation digitale en 2024** (Bpifrance Le Lab juin 2025), contre 72 % en 2017 — soit un rythme de digitalisation de **+1 % par an seulement**. **43 % n'analysent toujours pas leurs données** pour piloter leur activité. Une entreprise qui analyse ses données est **2,5× plus susceptible** d'utiliser une IA. Une entreprise qui a engagé sa transformation digitale est **5× plus susceptible** d'utiliser une IA. **La data est le préalable à l'IA.**

**Source** : Bpifrance Le Lab juin 2025, p. 32-35.

---

## 2. Intégration des 5 RetEx Bpifrance Le Lab juin 2025

Pour chaque RetEx, ajouter un encart dans la section appropriée du module concerné. Format suggéré : `case-deep-actor` existant ou nouvelle classe `retex-bpifrance` selon ton choix architectural.

### 2.1 CU-016 Maintenance prédictive industrielle — RetEx Alfi Technologies

**Action** : ajouter dans `modules/cu-016-maintenance-predictive.html`, idéalement dans une section RetEx existante ou en nouvelle section.

**Contenu** :
```html
<div class="case-deep-actor">
  <div class="case-deep-actor-label">Cas type — Industrie française</div>
  <p style="margin: 0;">
    <strong>Alfi Technologies</strong> (200 employés, ~30 M€ de CA, Pin-en-Mauges) — fabricant de chaînes logistiques industrielles. A intégré une couche LLM (Mistral) à sa brique servicielle de maintenance prédictive sur ses machines déployées chez ses clients. Stack : capteurs IoT + machine learning prédictif + couche LLM RAG sur la documentation technique propre à chaque installation client.
  </p>
  <div class="case-deep-actor-meta">
    <div class="case-deep-actor-meta-item">
      <div class="case-deep-actor-meta-label">Effectif</div>
      <strong>200 personnes</strong>
    </div>
    <div class="case-deep-actor-meta-item">
      <div class="case-deep-actor-meta-label">Réduction appels clients</div>
      <strong>−30 %</strong>
    </div>
    <div class="case-deep-actor-meta-item">
      <div class="case-deep-actor-meta-label">Temps redémarrage</div>
      <strong>Largement amélioré</strong>
    </div>
    <div class="case-deep-actor-meta-item">
      <div class="case-deep-actor-meta-label">Business model</div>
      <strong>Serviciel revu</strong>
    </div>
  </div>
  <p style="margin-top: var(--space-3); font-size: 0.9375rem;">
    Résultats : <strong>−30 % d'appels entrants clients</strong> pour questions techniques, augmentation de la disponibilité machine, temps de redémarrage largement amélioré, business model serviciel revu comme avantage compétitif. Coût mutualisé via partenariat technologique de 10 ans avec InUse, formation 1 ingénieure IA temps partiel pour développer et calibrer le modèle.
  </p>
  <p style="margin: 0; font-size: 0.8125rem; color: var(--color-text-soft); font-style: italic;">
    Source : Bpifrance Le Lab, « L'IA dans les PME et ETI françaises », juin 2025, p. 110-113.
  </p>
</div>
```

### 2.2 CU-018 Optimisation production / nesting — RetEx Transarc

**Action** : ajouter dans `modules/cu-018-optimisation-production.html`.

**Contenu** :
```html
<div class="case-deep-actor">
  <div class="case-deep-actor-label">Cas type — Transport & logistique</div>
  <p style="margin: 0;">
    <strong>Transarc</strong> (1 600 employés, 90 M€ de CA, Dijon) — société d'autocars. Solution sur mesure développée avec Neovision pour optimiser les trajets à vide entre dépôts et tournées. Stack : machine learning sur données internes + OpenStreetMap + interface web cartographique.
  </p>
  <div class="case-deep-actor-meta">
    <div class="case-deep-actor-meta-item">
      <div class="case-deep-actor-meta-label">Coût projet</div>
      <strong>100 K€ + maintenance</strong>
    </div>
    <div class="case-deep-actor-meta-item">
      <div class="case-deep-actor-meta-label">ROI atteint</div>
      <strong>3 mois</strong>
    </div>
    <div class="case-deep-actor-meta-item">
      <div class="case-deep-actor-meta-label">Km à vide évités</div>
      <strong>Centaines de milliers</strong>
    </div>
    <div class="case-deep-actor-meta-item">
      <div class="case-deep-actor-meta-label">CO2 évité (6 mois)</div>
      <strong>17 t</strong>
    </div>
  </div>
  <p style="margin-top: var(--space-3); font-size: 0.9375rem;">
    Sur les 6 premiers mois : plusieurs centaines de milliers de kilomètres à vide évités, 17 tonnes de CO2 évitées, satisfaction conducteurs en hausse. <strong>Étape suivante</strong> : génération automatique de devis personnalisés via RAG sur 1 M+ de devis historiques. Cas-école triple impact (économique, environnemental, social).
  </p>
  <p style="margin: 0; font-size: 0.8125rem; color: var(--color-text-soft); font-style: italic;">
    Source : Bpifrance Le Lab, « L'IA dans les PME et ETI françaises », juin 2025, p. 102-105.
  </p>
</div>
```

### 2.3 CU-006 Qualification leads et CU-013 Workflow email-CRM — RetEx société de géolocalisation

**Action** : ajouter à la fois dans `modules/cu-006-leads-chatbot.html` ET dans `modules/cu-013-workflow-email-crm.html` (cas transverse aux deux modules).

**Contenu** :
```html
<div class="case-deep-actor">
  <div class="case-deep-actor-label">Cas type — TPE Tech, ~25 personnes</div>
  <p style="margin: 0;">
    <strong>Société de géolocalisation</strong> (25 employés, &lt; 5 M€ CA, Paris — anonymisée). Automatisation complète de la gestion des leads entrants par formulaire web et email. Agent IA connecté à la boîte mail via API, classification anti-spam puis génération de brouillon de réponse personnalisée + proposition de RDV agenda + enregistrement automatique dans le CRM Pipedrive.
  </p>
  <div class="case-deep-actor-meta">
    <div class="case-deep-actor-meta-item">
      <div class="case-deep-actor-meta-label">Coût développement</div>
      <strong>~10 j/h interne</strong>
    </div>
    <div class="case-deep-actor-meta-item">
      <div class="case-deep-actor-meta-label">Coût récurrent</div>
      <strong>200 €/mois OpenAI</strong>
    </div>
    <div class="case-deep-actor-meta-item">
      <div class="case-deep-actor-meta-label">Réduction temps</div>
      <strong>−99 %</strong>
    </div>
    <div class="case-deep-actor-meta-item">
      <div class="case-deep-actor-meta-label">Réalisé par</div>
      <strong>Le dirigeant seul</strong>
    </div>
  </div>
  <p style="margin-top: var(--space-3); font-size: 0.9375rem;">
    <strong>40 leads qu'un stagiaire aurait traités en 1 semaine sont désormais traités en 30 minutes</strong> — réduction du temps de traitement de <strong>−99 %</strong>. Développement réalisé seul par le dirigeant avec assistance IA générative (Claude Code / ChatGPT). Stack : API OpenAI GPT-4.1 + RAG sur base FAQ et manuels internes + Pipedrive. Démontre que la mise en production est désormais accessible à une TPE sans équipe technique dédiée.
  </p>
  <p style="margin: 0; font-size: 0.8125rem; color: var(--color-text-soft); font-style: italic;">
    Source : Bpifrance Le Lab, « L'IA dans les PME et ETI françaises », juin 2025, p. 106-109.
  </p>
</div>
```

### 2.4 CU-008 Knowledge base RAG — RetEx Time to Fly + chiffre Cisco

**Action** : ajouter dans `modules/cu-008-knowledge-base-rag.html`.

**Contenu RetEx** :
```html
<div class="case-deep-actor">
  <div class="case-deep-actor-label">Cas type — Conseil aviation, ~25 personnes</div>
  <p style="margin: 0;">
    <strong>Time to Fly</strong> (25 employés, 2,6 M€ CA, Roissy) — conseil aviation. Algorithme RAG (GPT-4) pour analyse documentaire de conformité réglementaire, jusqu'à 1 000 pages par audit.
  </p>
  <div class="case-deep-actor-meta">
    <div class="case-deep-actor-meta-item">
      <div class="case-deep-actor-meta-label">Coût prototype</div>
      <strong>100 K€ subv. ~50 %</strong>
    </div>
    <div class="case-deep-actor-meta-item">
      <div class="case-deep-actor-meta-label">Précision identification</div>
      <strong>80 %</strong>
    </div>
    <div class="case-deep-actor-meta-item">
      <div class="case-deep-actor-meta-label">Gain temps audit</div>
      <strong>−50 %</strong>
    </div>
    <div class="case-deep-actor-meta-item">
      <div class="case-deep-actor-meta-label">ROI estimé</div>
      <strong>2 ans</strong>
    </div>
  </div>
  <p style="margin-top: var(--space-3); font-size: 0.9375rem;">
    <strong>Précision démontrée 80 %</strong> sur identification des passages pertinents et conformité, <strong>gain temps −50 %</strong> par audit. Coût prototype 100 K€ subventionné ~50 % via IA Booster + Pack IA région IDF. <strong>Limite documentée</strong> : prototype encore sans interface utilisateur, blocage à 300 K€ pour la phase 2 d'industrialisation. Cas illustratif des freins financiers sur le passage POC → production.
  </p>
  <p style="margin: 0; font-size: 0.8125rem; color: var(--color-text-soft); font-style: italic;">
    Source : Bpifrance Le Lab, « L'IA dans les PME et ETI françaises », juin 2025, p. 114-119.
  </p>
</div>
```

**Contenu chiffre tendance Cisco** (à ajouter dans la section « Pour aller plus loin » ou en encart) :
> **Cisco prévoit qu'en 2028, 68 % des interactions de service client seront gérées de bout en bout par l'IA agentique sans intervention humaine** (relayé par Apizee, avril 2026). Le pattern RAG est l'une des briques fondatrices de cette évolution.

### 2.5 CU-009 Content repurposing et CU-002 Assistant rédactionnel — RetEx Meero

**Action** : ajouter en encart court dans `modules/cu-009-content-repurposing.html` ET `modules/cu-002-assistant-redactionnel.html`.

**Contenu** :
```html
<div class="callout callout-info">
  <p>
    <strong>Cas type — Meero (TPE FR, photographie pro)</strong>. IA déployée pour automatiser la retouche d'images professionnelles. <strong>Près de 60 % des employés gagnent jusqu'à 5 heures de travail par semaine</strong>, réinvesties en tâches à plus forte valeur ajoutée. Coûts de production réduits → prix plus compétitifs sur le marché. Cas démonstratif des gains massifs possibles sur des tâches à fort caractère répétitif.
  </p>
  <p style="margin: 0; font-size: 0.8125rem; font-style: italic;">
    Source : Bpifrance Big Media « 8 cas d'usage de l'IA en entreprise », février 2026.
  </p>
</div>
```

---

## 3. Update CU-007 RH — chiffres frais + encart anti-pattern

**Action** : enrichir `modules/cu-007-rh-cv-entretiens.html`.

### 3.1 Chiffres clés à intégrer (en exec-summary ou stats)

À insérer dans une section « Chiffres clés 2026 » ou enrichir les stats existantes :
- **70 % des professionnels RH** utilisent déjà une IA générative (ParlonsRH 2024)
- **80 % des collaborateurs** voient l'IA RH comme un levier d'évolution professionnelle (Liaisons Sociales 2024)
- Bénéfices documentés : **−30 % coûts de recrutement, +25 % satisfaction employés, +30-40 % productivité fonction RH** (Neobrain, sources Liaisons Sociales et Culture RH 2024)
- Cas PwC US/Mexique avec Neobrain + Microsoft Copilot : passage de **2 % à 15 % de profils atypiques** dans la talent marketplace grâce à la combinaison IA matching + IA générative
- RetEx complémentaire : **ETI BTP Occitanie 300p** — pré-sélection CV par IA → −60 % temps lecture CV + meilleure diversité profils (source : Bpifrance Big Media)

### 3.2 Encart anti-pattern RH IA — distinction acceptable / interdit

**Action** : ajouter une section dédiée « Anti-patterns à éviter » avec encart visuel rouge.

**Contenu** :
```html
<div class="alert-ai-act">
  <div class="alert-ai-act-icon">⚠️</div>
  <div class="alert-ai-act-content">
    <h3>Anti-pattern RH IA — distinction critique</h3>
    <p><strong>Acceptable</strong> : usages d'aide à la rédaction, reformulation, synthèse factuelle, traduction multilingue (descriptif de poste, mail candidat, compte-rendu d'entretien).</p>
    <p><strong>INTERDIT ou très encadré</strong> : évaluation de candidat, scoring, classement, prédiction sur les personnes — ces usages relèvent du <strong>haut risque AI Act</strong> et sont également exposés à un risque RGPD + risque de discrimination algorithmique. Ils nécessitent un dispositif lourd (AIPD renforcée, contrôle humain documenté, transparence vis-à-vis des candidats, architecture A2/A3/A4 obligatoire — cf. <a href="../architectures.html" class="tool-link">Architectures</a>).</p>
    <p>Pour ces usages haut risque, ne jamais utiliser un SaaS propriétaire (A1) en cloud public sans garanties contractuelles spécifiques. Privilégier <strong>Mistral en cloud souverain EU</strong>, <strong>Pleias-RAG</strong>, ou solution on-premise selon sensibilité.</p>
  </div>
</div>
```

**Source** : Atela Conseil — https://atelaconseil.com/debut-2026-quels-outils-ia-utiliser/ + Neobrain — https://www.neobrain.io/blog/7-cas-usage-lia-equipes-rh

---

## 4. Tagging architectures sur 5 modules sensibles

**Action** : pour chaque module sensible, ajouter en tête (juste après le hero ou en synthèse rapide) un encart « Architectures recommandées » qui pointe vers la page Architectures.

### 4.1 CU-007 RH (haut risque AI Act)
```html
<div class="callout callout-warn">
  <p>
    <strong>🏗️ Architectures recommandées pour ce cas d'usage</strong> : <strong>A2 minimum</strong> (cloud privé / data residency EU), <strong>A3 ou A4 préférable</strong> pour les sous-cas de scoring / évaluation. <strong>A1 (SaaS propriétaire en cloud public) déconseillé</strong> sur les flux candidats — usage haut risque AI Act, exposition RGPD forte. Voir <a href="../architectures.html" class="tool-link">Architectures</a> pour le détail des patterns.
  </p>
</div>
```

### 4.2 CU-020 Conformité RGPD & AI Act
```html
<div class="callout callout-info">
  <p>
    <strong>🏗️ Architectures recommandées pour ce dispositif gouvernance</strong> : la cartographie elle-même peut s'appuyer sur n'importe quel pattern (le contenu n'est pas sensible). En revanche, les <strong>flux IA cartographiés doivent être classés par sensibilité</strong> et orientés vers le pattern adapté. Pour les usages haut risque, <strong>A3 (cloud souverain EU)</strong> ou <strong>A4 (on-premise)</strong> sont la cible. Voir <a href="../architectures.html" class="tool-link">Architectures</a>.
  </p>
</div>
```

### 4.3 CU-021 Finance & comptabilité augmentées
```html
<div class="callout callout-warn">
  <p>
    <strong>🏗️ Architectures recommandées pour ce cas d'usage</strong> : <strong>A2 ou A3 recommandés</strong> — les factures fournisseurs incluent des données personnelles (RIB, contacts, contrats). <strong>A1 (SaaS public) sous condition stricte</strong> avec engagement no-training et data residency EU. <strong>Mistral Cloud EU</strong> ou <strong>Pennylane / Qonto intégrés</strong> sont les options pragmatiques. Voir <a href="../architectures.html" class="tool-link">Architectures</a>.
  </p>
</div>
```

### 4.4 CU-013 Workflow email-CRM
```html
<div class="callout callout-info">
  <p>
    <strong>🏗️ Architectures recommandées pour ce cas d'usage</strong> : <strong>architecture hybride typique</strong>. <strong>A1</strong> acceptable pour les flux non sensibles (FAQ génériques, accusés de réception). <strong>A3 recommandé</strong> pour les flux contenant des données client personnelles (réclamations, négociations, demandes commerciales nominatives). Discipline : matrice de classification des emails par sensibilité, orientation vers le pattern adapté. Voir <a href="../architectures.html" class="tool-link">Architectures</a>.
  </p>
</div>
```

### 4.5 CU-008 Knowledge base RAG
```html
<div class="callout callout-info">
  <p>
    <strong>🏗️ Architectures recommandées pour ce cas d'usage</strong> : dépend totalement de la sensibilité du corpus indexé. Documentation publique → <strong>A1 OK</strong>. Documentation interne stratégique (procédures, contrats, savoir-faire) → <strong>A3 ou A4</strong>. RAG juridique / compliance → <strong>Pleias-RAG</strong> (open-weight souverain) en A3 / A4. Voir <a href="../architectures.html" class="tool-link">Architectures</a>.
  </p>
</div>
```

---

## 5. Update PR-01 Maturité organisationnelle — checklist diagnostic projet en cours

**Action** : ajouter dans `prealables/pr-01-maturite-organisationnelle.html` une **section supplémentaire** (ex : section 5bis ou nouvelle section 6, à placer avant « Pour aller plus loin ») dédiée au **diagnostic d'un projet IA déjà lancé** (en complément de l'auto-éval « projet à lancer » existante).

**Note** : cette section absorbe l'angle CU-023 anti-patterns identifié par la veille v3.5, sans créer un nouveau module.

**Contenu suggéré** :

```html
<section class="module-section" id="section-diag-projet-en-cours">
  <div class="module-section-header">
    <div class="module-section-icon icon-warning">5bis</div>
    <h2 class="module-section-title">Diagnostic d'un projet IA déjà lancé — 12 anti-patterns</h2>
  </div>

  <p>
    L'auto-évaluation précédente cadre la maturité <strong>avant</strong> de lancer un projet. Cette section couvre le cas complémentaire : un projet IA est <strong>déjà en cours</strong> (POC, pilote, début de production) et tu veux poser un diagnostic objectif sur sa trajectoire. 12 anti-patterns documentés par MIT Sloan, AdvisoryX-DXC, Gartner, S&amp;P Global et Bpifrance Le Lab — chacun augmente significativement la probabilité que le projet rejoigne les 95 % qui n'atteignent jamais la production à grande échelle (MIT « State of AI in Business 2025 »).
  </p>

  <div class="diagnostic">
    <div class="diagnostic-header">
      <h3 style="color: #B86E1A; margin: 0 0 var(--space-3);">Check-list 12 anti-patterns — coche ceux qui s'appliquent à ton projet</h3>
      <p class="diagnostic-intro">Plus tu coches, plus le risque d'échec est élevé. ≥ 4 anti-patterns détectés = signal d'alerte fort, considérer une remise à plat avant de poursuivre.</p>
    </div>

    <form id="antipatternForm">

      <div class="diag-question">
        <label class="diag-question-label">
          <input type="checkbox" name="ap1" style="margin-right: 8px;">
          <strong>1. Sponsor exécutif faible ou absent.</strong> Personne au COMEX ne porte vraiment le projet, le pilote est un middle-manager isolé.
        </label>
      </div>

      <div class="diag-question">
        <label class="diag-question-label">
          <input type="checkbox" name="ap2" style="margin-right: 8px;">
          <strong>2. ROI non chiffré ou non mesurable.</strong> Le projet ne sait pas dire quel KPI il doit faire bouger ni de combien.
        </label>
      </div>

      <div class="diag-question">
        <label class="diag-question-label">
          <input type="checkbox" name="ap3" style="margin-right: 8px;">
          <strong>3. Données du périmètre cible non préparées.</strong> Pas de nettoyage préalable, données en silos, schéma non documenté (cf. <a href="pr-02-preables-data-si.html" class="tool-link">PR-02</a>).
        </label>
      </div>

      <div class="diag-question">
        <label class="diag-question-label">
          <input type="checkbox" name="ap4" style="margin-right: 8px;">
          <strong>4. Pattern d'architecture non choisi explicitement.</strong> Le projet utilise par défaut un SaaS propriétaire sans avoir évalué les patterns A2/A3/A4 (cf. <a href="../architectures.html" class="tool-link">Architectures</a>).
        </label>
      </div>

      <div class="diag-question">
        <label class="diag-question-label">
          <input type="checkbox" name="ap5" style="margin-right: 8px;">
          <strong>5. Aucun audit Shadow AI.</strong> Personne ne sait ce que les collaborateurs utilisent déjà — risque de doublons et de Shadow AI persistante (cf. <a href="../modules/cu-020-conformite-rgpd-ai-act.html" class="tool-link">CU-020</a>).
        </label>
      </div>

      <div class="diag-question">
        <label class="diag-question-label">
          <input type="checkbox" name="ap6" style="margin-right: 8px;">
          <strong>6. Périmètre métier flou ou trop large.</strong> Le projet veut tout transformer en même temps au lieu de cibler 1-2 cas d'usage prioritaires.
        </label>
      </div>

      <div class="diag-question">
        <label class="diag-question-label">
          <input type="checkbox" name="ap7" style="margin-right: 8px;">
          <strong>7. Plan de formation IA absent ou générique.</strong> Pas de plan article 4 AI Act adapté aux fonctions impactées (cf. <a href="pr-03-maturite-humaine-formation.html" class="tool-link">PR-03</a>).
        </label>
      </div>

      <div class="diag-question">
        <label class="diag-question-label">
          <input type="checkbox" name="ap8" style="margin-right: 8px;">
          <strong>8. Validation humaine non documentée.</strong> Sur les actions externes (envoi, paiement, contrat), pas de matrice claire « auto / draft / humain ».
        </label>
      </div>

      <div class="diag-question">
        <label class="diag-question-label">
          <input type="checkbox" name="ap9" style="margin-right: 8px;">
          <strong>9. Comité de pilotage IA inexistant ou ad-hoc.</strong> Pas de point régulier (mensuel min) pour suivre l'avancement, arbitrer, calibrer.
        </label>
      </div>

      <div class="diag-question">
        <label class="diag-question-label">
          <input type="checkbox" name="ap10" style="margin-right: 8px;">
          <strong>10. POC sans plan de bascule production.</strong> Le projet vit en POC depuis 6+ mois sans calendrier ni budget pour la mise à l'échelle. Le « POC orphelin » est l'anti-pattern n°1 documenté MIT et Gartner.
        </label>
      </div>

      <div class="diag-question">
        <label class="diag-question-label">
          <input type="checkbox" name="ap11" style="margin-right: 8px;">
          <strong>11. Absence de procédure d'incident IA.</strong> Si l'agent fait une erreur préjudiciable demain, personne ne sait quoi faire.
        </label>
      </div>

      <div class="diag-question">
        <label class="diag-question-label">
          <input type="checkbox" name="ap12" style="margin-right: 8px;">
          <strong>12. Vendor lock-in sans plan B.</strong> Toute la chaîne dépend d'un seul fournisseur (Anthropic OU OpenAI OU autre) sans alternative documentée si le service ferme ou modifie ses CGU.
        </label>
      </div>

      <button type="button" class="diag-submit" onclick="evaluateAntiPatterns()">Évaluer le risque d'échec</button>
    </form>

    <div class="diag-result" id="antipatternResult"></div>
  </div>

  <p style="margin-top: var(--space-5);">
    <strong>Pourquoi c'est important</strong> : les études convergent — MIT (95 %), AdvisoryX-DXC (94 %), Rand Corp (&gt; 80 %), Gartner (30 % de projets abandonnés en 2026), S&amp;P Global (46 % des POCs abandonnés). Ce n'est pas la technologie qui échoue, c'est l'exécution. Les anti-patterns ci-dessus sont les <strong>causes structurelles documentées</strong> de cet échec.
  </p>
</section>
```

**Et ajouter le script JS associé** (à placer avant `</script>` du bas de page) :

```javascript
function evaluateAntiPatterns() {
  const form = document.getElementById('antipatternForm');
  const result = document.getElementById('antipatternResult');
  let count = 0;
  for (let i = 1; i <= 12; i++) {
    if (form.querySelector(`input[name="ap${i}"]`).checked) count++;
  }

  let level, color, msg;
  if (count === 0) {
    level = '✅ Aucun anti-pattern détecté';
    color = '#2E5C2E';
    msg = 'Trajectoire saine. Maintenir les rituels de pilotage et la discipline qualité.';
  } else if (count <= 3) {
    level = '🟡 Quelques signaux faibles (' + count + '/12)';
    color = '#B86E1A';
    msg = 'Anti-patterns ciblés à corriger sans urgence absolue. Prioriser ceux qui touchent au sponsor exécutif, à l\'ROI et au plan de bascule production — ce sont les causes les plus déterminantes selon MIT.';
  } else if (count <= 6) {
    level = '🟠 Risque élevé (' + count + '/12)';
    color = '#C82A2A';
    msg = 'Plusieurs anti-patterns structurels détectés. Probabilité d\'abandon ou d\'échec significatif. Recommandation : pause de 2-4 semaines pour remettre à plat avant de poursuivre l\'investissement.';
  } else {
    level = '🛑 Risque critique (' + count + '/12)';
    color = '#8C1A1A';
    msg = 'Le projet est dans la zone des 95 % qui n\'atteignent jamais la production à grande échelle (MIT). Recommandation forte : arrêter ou suspendre, refaire le cadrage organisationnel (cf. auto-éval section 5), repartir sur des bases plus solides.';
  }

  result.innerHTML = `
    <div style="text-align:center; padding: var(--space-5) 0;">
      <div style="font-size: 3rem; font-weight: 800; color: ${color}; line-height: 1;">${count}<span style="font-size: 1.5rem; color: var(--color-text-soft);">/12</span></div>
      <div style="font-size: 1.0625rem; font-weight: 700; color: ${color}; margin: var(--space-2) 0;">${level}</div>
    </div>
    <div class="diag-action" style="border-left-color: ${color};">
      <p style="margin: 0;">${msg}</p>
    </div>
  `;
  result.classList.add('show');
  result.scrollIntoView({ behavior: 'smooth', block: 'center' });
}
```

**Sources de la matière** :
- MIT « State of AI in Business 2025 » via Claranet — https://www.claranet.com/fr/blog/ia-en-entreprise-bonnes-pratiques-et-pieges-eviter-en-2026/
- Sigma livre blanc juin 2025 — https://www.informatiquenews.fr/wp-content/uploads/2025/06/Livre_Blanc_Embarquer_IA_entreprise.pdf
- Bpifrance Le Lab juin 2025
- Unow article mars 2026 — https://www.unow.fr/blog/le-coin-des-experts/adoption-ia-entreprise-tendances-2026/

---

## 6. Page Ressources — nouvelle catégorie « Navigateurs agentiques » + 4 fiches outils

### 6.1 Création de la nouvelle catégorie

**Action** : ajouter dans `ressources.html` une nouvelle catégorie au sommaire principal et une section correspondante dans le contenu.

**Position dans le sommaire** : entre « 🎙️ Voice & speech » et « 👁️ Vision industrielle » (ou autre position cohérente avec la logique du sommaire actuel).

**Format de la section catégorie** :

```html
<section class="module-section" id="navigateurs-agentiques">
  <div class="module-section-header">
    <div class="module-section-icon">🌐</div>
    <h2 class="module-section-title">Navigateurs agentiques</h2>
  </div>

  <p>
    Catégorie nouvelle 2026 — les navigateurs intégrant un agent IA capable de naviguer le web, remplir des formulaires, exécuter des actions à la place de l'utilisateur. Rupture de paradigme par rapport aux assistants conversationnels classiques. Émergence forte fin 2025 avec OpenAI, Perplexity, Anthropic et Atlassian.
  </p>

  <div class="callout callout-warn">
    <p>
      <strong>⚠️ Avertissement sécurité.</strong> Ces outils combinent automation web + LLM, exposant à des risques nouveaux : <strong>prompt injection</strong> via des pages web malveillantes, <strong>collecte silencieuse</strong> de la navigation utilisateur (selon CGU), <strong>actions involontaires</strong> sur comptes sensibles (banque, médical, RH). Recommandation : <strong>ne pas utiliser pour comptes sensibles</strong>, isoler dans un profil de navigation dédié, surveiller les CGU sur la rétention de l'historique. Voir <a href="prealables/pr-05-securite-ia.html" class="tool-link">Sécurité IA &amp; risques opérationnels</a>.
    </p>
  </div>

  <!-- 4 fiches outils -->
  [Insertion ChatGPT Atlas, Comet, Claude pour Chrome, Operator — voir 6.2 ci-dessous]
</section>
```

### 6.2 Les 4 fiches outils de la catégorie

#### Fiche A — ChatGPT Atlas (OpenAI)
- **Vendor** : OpenAI
- **Catégorie** : Navigateur agentique
- **Type** : SaaS propriétaire
- **Souveraineté** : 🇺🇸
- **Maturité** : N4-N6 (lancement fin 2025, montée en charge 2026)
- **Coût** : 🟠 Payant (inclus ChatGPT Pro 200 $/mois) ou 🟡 Freemium selon plan
- **Complexité** : 🛠️ Plug-and-play (extension Chrome)

**Tagline** : Extension navigateur OpenAI qui mémorise les interactions et exécute des actions web (réservations, formulaires, achats) à la place de l'utilisateur. Architecture agentique grand public lancée fin 2025.

**Description** : ChatGPT Atlas est l'arrivée d'OpenAI sur le segment des navigateurs agentiques. L'extension transforme Chrome en environnement d'orchestration où l'agent ChatGPT peut prendre la main pour exécuter des tâches multi-étapes (recherche d'info, comparaison, achat, prise de RDV). Inclus dans ChatGPT Pro à partir de fin 2025.

**Cas d'usage typiques** : recherche comparative complexe, automatisation tâches répétitives web, synthèse multi-sources avec exécution.

**Limites importantes** : ne pas utiliser sur comptes sensibles (banque, santé, RH). Risque de prompt injection via pages web malveillantes documenté.

**Source** : https://openai.com/atlas (à vérifier URL exacte au moment de l'intégration)

#### Fiche B — Comet (Perplexity)
- **Vendor** : Perplexity AI
- **Catégorie** : Navigateur agentique
- **Type** : SaaS propriétaire
- **Souveraineté** : 🇺🇸
- **Maturité** : N4-N6
- **Coût** : 🟡 Freemium (intégré aux plans Perplexity Pro)
- **Complexité** : 🛠️ Plug-and-play

**Tagline** : Pendant Perplexity du navigateur agentique, intégré à la recherche augmentée de Perplexity. Combine recherche temps réel + actions web dans une même expérience.

**Description** : Comet capitalise sur la force de Perplexity en recherche augmentée pour offrir un navigateur agentique orienté découverte d'information et action. Différenciant principal : l'agent peut citer ses sources avec attribution claire (héritage Perplexity).

**Cas d'usage typiques** : veille active sur sujets complexes, recherche structurée + action, comparaisons de produits / services.

**Source** : https://www.perplexity.ai/comet (à vérifier)

#### Fiche C — Claude pour Chrome (Anthropic)
- **Vendor** : Anthropic
- **Catégorie** : Navigateur agentique
- **Type** : SaaS propriétaire
- **Souveraineté** : 🇺🇸
- **Maturité** : N4-N6
- **Coût** : 🟠 Payant (inclus Claude Max)
- **Complexité** : 🛠️ Plug-and-play

**Tagline** : Extension Chrome qui permet à Claude de lire, comprendre et interagir avec les pages web ouvertes. Disponible dans les plans Claude Max.

**Description** : Claude pour Chrome est la réponse d'Anthropic sur le segment des navigateurs agentiques. L'extension donne à Claude un accès contextuel aux pages web visitées, permettant des actions multi-étapes orchestrées par l'agent. Approche prudente sur les actions externes engageantes (validation humaine systématique sur formulaires de paiement, contrats, etc.).

**Cas d'usage typiques** : analyse documentaire web (rapports, articles longs), assistance shopping comparatif, synthèse de plusieurs onglets.

**Source** : https://www.anthropic.com/claude-for-chrome (à vérifier)

#### Fiche D — Operator (OpenAI)
- **Vendor** : OpenAI
- **Catégorie** : Navigateur agentique (variant)
- **Type** : SaaS propriétaire
- **Souveraineté** : 🇺🇸
- **Maturité** : N7-N8 (early access pro)
- **Coût** : 🔴 Entreprise / Pro (200 $/mois minimum)
- **Complexité** : 🛠️🛠️ Setup léger

**Tagline** : Agent IA OpenAI qui pilote un navigateur dédié dans le cloud pour exécuter des tâches multi-étapes complexes. Plus puissant qu'une extension navigateur classique.

**Description** : Operator est le « grand frère » d'Atlas. Au lieu d'une extension dans Chrome local, Operator dispose d'un navigateur cloud isolé qu'il pilote intégralement. Permet des automations complexes (ex : remplir 50 formulaires, scraper un site avec navigation conditionnelle, exécuter des tâches métier répétitives). Disponibilité : early access dans ChatGPT Pro (200 $/mois).

**Cas d'usage typiques** : automatisation back-office (saisie multi-systèmes), recherche web exhaustive, scraping web piloté.

**Limites** : coût élevé, encore en early access, risques sécurité documentés (Vention State of AI 2026).

**Source** : https://openai.com/operator (à vérifier)

### 6.3 Mise à jour des fiches outils existantes — versions des modèles

**Action** : actualiser les versions citées dans les fiches existantes aux versions mai 2026.

| Fiche | Mise à jour |
|---|---|
| Claude (Anthropic) | Mentionner **Claude Opus 4.6** et **Sonnet 4.6** (fév-mars 2026), SWE-Bench 80,8-80,9 %, contexte 1 M tokens en bêta |
| GPT (OpenAI) | Mentionner **GPT-5.2 → 5.4** (fév-mars 2026), fenêtre 400 K tokens, mode raisonnement adaptatif |
| Gemini (Google) | Mentionner **Gemini 3 Pro / Flash** (déc 2025), **Nano Banana Pro** images, **Veo 3.1** vidéo |
| Mistral | Mentionner **Mistral Large 2** + **Le Chat** (gratuit illimité grand public), utilisé par BNP, Orange, Capgemini |
| (Nouvelle mention) | **Sora 2** (OpenAI, inclus ChatGPT Pro) — vidéo 20s avec audio synchronisé |

### 6.4 Outils complémentaires à ajouter (3 fiches)

#### Lindy
- **Catégorie** : Agents IA / Orchestration
- **Type** : SaaS no-code
- **Tagline** : Plateforme no-code de création d'agents IA personnalisés. À partir de 49 $/mois. Concurrent direct de CrewAI / Manus pour les utilisateurs métiers non-tech.
- **Pertinence** : un des rares outils no-code à monter, pertinent pour PME qui veulent créer des agents sans dev.

#### Manus
- **Catégorie** : Agents IA autonomes
- **Type** : SaaS
- **Tagline** : Agent autonome capable de tâches complexes multi-étapes. Représente la nouvelle vague d'agents 100 % autonomes émergents fin 2025.
- **Pertinence** : à indexer même en early-stage car cité partout dans la littérature de référence 2026.

#### ClickUp Brain
- **Catégorie** : Productivité / Gestion projet
- **Type** : SaaS
- **Tagline** : IA intégrée native dans ClickUp pour résumés, rédaction, recherche, automatisations. Tarif 7-12 $/utilisateur/mois.
- **Pertinence** : alternative tout-en-un à Notion AI / Asana Intelligence pour les PME serrées sur les outils.

---

## 7. Récapitulatif des fichiers à modifier par Claude Code

| Fichier | Type d'action |
|---|---|
| `index.html` | Refresh chiffres macro hero + ajout 2 chiffres complémentaires + mise à jour À propos (4 niveaux) + mise à jour nav (5 entrées) |
| `prealables.html` | Refonte head banner (layout index) + padding hero + reformulation titre + suppression PR-XX + nav 5 entrées |
| `prealables/pr-01-*.html` à `pr-06-*.html` | Suppression badges PR-XX + harmonisation head banner + mise à jour nav 5 entrées |
| `prealables/pr-01-*.html` (spécifique) | Ajout section « Diagnostic projet en cours » avec 12 anti-patterns + script JS |
| `prealables/pr-04-*.html` (spécifique) | Ajout section « Tendances macro 2026 » |
| `architectures.html` | Nouveau fichier (livré dans `mockup/architectures.html`) |
| `modules/cu-002-*.html` | Encart RetEx Meero |
| `modules/cu-006-*.html` | Encart RetEx société géoloc |
| `modules/cu-007-*.html` | Chiffres frais + encart anti-pattern + tagging architectures |
| `modules/cu-008-*.html` | Encart RetEx Time to Fly + chiffre Cisco + tagging architectures |
| `modules/cu-009-*.html` | Encart RetEx Meero |
| `modules/cu-013-*.html` | Encart RetEx société géoloc + tagging architectures |
| `modules/cu-016-*.html` | Encart RetEx Alfi Technologies |
| `modules/cu-018-*.html` | Encart RetEx Transarc |
| `modules/cu-020-*.html` | Tagging architectures |
| `modules/cu-021-*.html` | Tagging architectures |
| `ressources.html` | Nouvelle catégorie Navigateurs agentiques + 4 fiches + 3 fiches complémentaires (Lindy, Manus, ClickUp Brain) + maj versions modèles |
| **Toutes les pages** | Mise à jour nav principale (Préalables → Architectures → Modules → Ressources → À propos) |

---

*Patches v3.5 — Hub IA Learning Center — mai 2026 — Cowork (Claude desktop)*
