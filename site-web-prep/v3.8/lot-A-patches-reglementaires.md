# Lot A v3.8 — Patches réglementaires (AI Act Article 50 + Omnibus VII + facturation électronique)

**Brief consolidé pour Claude Code** : 6 patches éditoriaux à appliquer sur des modules existants. Aucun nouveau module dans ce lot.

**Sources** : veille v3.7.13 (Grok input 4 + Commission EU 8 mai 2026 + economie.gouv.fr).

---

## Patch A.1 — CU-020 (Conformité RGPD & AI Act) — section AI Act Article 50 + Omnibus VII

**Module cible** : `modules/cu-020-conformite-rgpd-ai-act.html`
**Position** : nouvelle section dédiée à intégrer entre la section actuelle « AI Act haut-risque » et la section « Plan d'action conformité ». Titre suggéré : **« AI Act Article 50 — Transparence et obligations de labellisation »**.

### Contenu à intégrer

#### 1. Le principe de l'Article 50 (à expliquer en clair)

L'Article 50 du règlement européen sur l'IA (AI Act) impose **deux obligations de transparence** distinctes, applicables à tous les acteurs (pas seulement aux systèmes haut-risque) :

1. **Informer l'utilisateur qu'il interagit avec un système d'IA** lorsque ce n'est pas évident (chatbot, agent vocal, assistant en ligne, etc.)
2. **Labelliser les contenus générés ou substantiellement modifiés par l'IA** (texte, image, audio, vidéo) afin que le public puisse les identifier comme synthétiques

**Application** : 2 août 2026.

#### 2. Le statut actuel des draft guidelines (mai 2026)

Les **draft guidelines pour l'implémentation de l'Article 50** ont été publiées par la Commission européenne le 8 mai 2026. Elles sont en **consultation publique** : tout acteur concerné peut soumettre des observations (lien dans les sources finales).

> ⚠️ **À vérifier au moment de l'intégration HTML** : la consultation publique a une date de fin. Si elle a évolué entre la rédaction et l'intégration, mettre à jour. Pour information, la date initialement annoncée par la Commission était fixée début juin 2026.

#### 3. Le paquet Omnibus VII (simplification)

Le **paquet de simplification Omnibus VII** a fait l'objet d'un accord politique entre Parlement et Conseil le **7 mai 2026**. Il apporte trois nouveautés :

- **Allègement administratif** pour les acteurs non haut-risque
- **Clarification des interactions** entre l'AI Act et d'autres règlements (notamment Machinery Regulation pour les machines connectées)
- **Interdiction explicite des applications dites de « nudification »** (génération d'images dénudées non consenties)

L'adoption formelle est prévue avant l'application de l'AI Act haut-risque (2 août 2026).

#### 4. Le watermarking reporté

Une nouveauté significative du paquet Omnibus VII : **l'obligation technique de watermarking des contenus générés par IA est reportée au 2 décembre 2026**. La labellisation visuelle/textuelle reste obligatoire au 2 août, mais l'aspect cryptographique du watermarking bénéficie d'un délai supplémentaire.

#### 5. Implication concrète pour les PME

Trois actions à mener avant le 2 août 2026 :

1. **Auditer ses interactions avec l'IA** : tout chatbot, assistant vocal, ou agent doit annoncer clairement qu'il s'agit d'une IA dès la première interaction
2. **Identifier les contenus générés par IA** : tout email rédigé par IA et envoyé à un tiers, tout visuel ou audio généré, doit être labellisé (mention type « contenu généré ou modifié par IA »)
3. **Documenter la conformité** : tenir un registre interne des usages IA en contact avec le public (clients, fournisseurs, candidats)

### Sources à ajouter dans la section finale (Schéma A)

À insérer dans la sous-rubrique « 📚 Documentation officielle & études » :
- [Commission européenne — Draft guidelines Article 50 (8 mai 2026)](https://digital-strategy.ec.europa.eu/en/library/draft-guidelines-implementation-transparency-obligations-certain-ai-systems-under-article-50-ai-act)
- [Conseil de l'UE — Accord Omnibus VII (7 mai 2026)](https://www.consilium.europa.eu/en/press/press-releases/2026/05/07/artificial-intelligence-council-and-parliament-agree-to-simplify-and-streamline-rules/)

### Renvois internes à mettre à jour dans le corps

- Renvoyer vers les modules contenu généré (CU-002, CU-009, CU-010, CU-019) qui sont aussi impactés par l'obligation de labellisation
- Renvoyer vers PR-05 (Sécurité IA) et CU-014 (Multi-agents)

---

## Patch A.2 — CU-002 (Assistant rédactionnel) — encart Article 50 transparence

**Module cible** : `modules/cu-002-assistant-redactionnel.html`
**Position** : encart visible (composant `.alert-block` ou `.callout-info`) à insérer dans la section actuelle « Bonnes pratiques » ou en début de module si la section appropriée n'existe pas.

### Contenu de l'encart

> **⚖️ AI Act Article 50 — applicable au 2 août 2026**
>
> Tout contenu rédigé ou substantiellement modifié par IA et publié auprès d'un tiers (client, fournisseur, candidat, public) doit être **labellisé comme synthétique** au sens de l'article 50 de l'AI Act européen. Pour l'instant la labellisation visuelle/textuelle suffit (mention type « rédigé avec assistance IA »). Le watermarking technique (cryptographique) est reporté au 2 décembre 2026.
>
> Pour le cadre complet, voir le module [Conformité RGPD & AI Act](cu-020-conformite-rgpd-ai-act.html).

### Note Cowork

Encart court à intégrer en haut du module ou dans la section bonnes pratiques. Pas de refonte structurelle. Lien interne vers CU-020 pour aller plus loin.

---

## Patch A.3 — CU-009 (Content repurposing) — encart Article 50 transparence

**Module cible** : `modules/cu-009-content-repurposing.html`
**Position** : encart visible à insérer dans la section pertinente (typiquement « Pour aller plus loin » ou « Bonnes pratiques »).

### Contenu de l'encart

> **⚖️ AI Act Article 50 — applicable au 2 août 2026**
>
> Tout contenu (texte, image, audio, vidéo) repackagé ou généré par IA et diffusé auprès d'un tiers (réseaux sociaux, newsletter, site web public) doit être **labellisé comme synthétique** au sens de l'article 50 de l'AI Act européen. La labellisation visuelle/textuelle suffit pour l'instant. Le watermarking cryptographique est reporté au 2 décembre 2026.
>
> Pour le cadre complet, voir le module [Conformité RGPD & AI Act](cu-020-conformite-rgpd-ai-act.html).

---

## Patch A.4 — CU-010 (Pipeline contenu social) — encart Article 50 transparence

**Module cible** : `modules/cu-010-pipeline-contenu-social.html`
**Position** : même logique que A.3 (encart pertinent dans la section bonnes pratiques).

### Contenu de l'encart

> **⚖️ AI Act Article 50 — applicable au 2 août 2026**
>
> Les contenus générés ou substantiellement modifiés par IA et publiés sur les réseaux sociaux (LinkedIn, X, Facebook, Instagram) entrent dans le champ d'application de l'article 50 de l'AI Act européen. **La labellisation textuelle/visuelle est obligatoire** (mention type « visuel généré par IA », « rédigé avec assistance IA »). Le watermarking technique est reporté au 2 décembre 2026.
>
> Cas particulier des plateformes : LinkedIn, Meta, TikTok ont déjà commencé à déployer leurs propres outils de labellisation automatique. À surveiller selon ta plateforme cible.
>
> Pour le cadre complet, voir [Conformité RGPD & AI Act](cu-020-conformite-rgpd-ai-act.html).

---

## Patch A.5 — CU-019 (Newsletter locale) — encart Article 50 transparence

**Module cible** : `modules/cu-019-newsletter-locale.html`
**Position** : encart en début de module ou dans la section pertinente.

### Contenu de l'encart

> **⚖️ AI Act Article 50 — applicable au 2 août 2026**
>
> Une newsletter dont le contenu est rédigé ou substantiellement modifié par IA doit **labelliser ce caractère synthétique** au sens de l'article 50 de l'AI Act européen. Mention possible : « Cette newsletter est rédigée avec l'aide d'une intelligence artificielle, sous supervision éditoriale humaine ». La labellisation textuelle suffit pour l'instant. Le watermarking cryptographique est reporté au 2 décembre 2026.
>
> Pour le cadre complet, voir [Conformité RGPD & AI Act](cu-020-conformite-rgpd-ai-act.html).

---

## Patch A.6 — CU-024 (Order-to-cash) — actualisation calendrier facturation électronique

**Module cible** : `modules/cu-024-order-to-cash.html`
**Position** : section actuelle sur le calendrier facturation électronique (à actualiser avec données mai 2026).

### Contenu à intégrer

Remplacer ou actualiser le bloc actuel sur le calendrier de la facturation électronique avec les informations précises mai 2026 :

#### Calendrier officiel facturation électronique (mai 2026)

- **Mai 2026** : qualification de **ChorusPro pour la sphère publique** (l'État, les collectivités, les établissements publics utilisent désormais le portail ChorusPro qualifié comme plateforme d'échange).
- **1er septembre 2026** : **réception obligatoire** des factures électroniques pour **toutes les entreprises** (TPE, PME, ETI, grandes entreprises). Concrètement : ton entreprise doit pouvoir réceptionner techniquement une facture électronique de l'un de ses fournisseurs.
- **1er septembre 2027** : **émission obligatoire** des factures électroniques pour **les PME, TPE et micro-entreprises**. Tu devras produire toutes tes factures B2B en format électronique structuré (Factur-X, UBL ou CII), via une plateforme agréée DGFiP ou via le portail public.
- Les ETI et grandes entreprises ont des échéances différentes selon les segments (à vérifier sur economie.gouv.fr selon ton statut).

#### Implications concrètes pour la PME

1. **Avant le 1er septembre 2026** : choisir et configurer ta plateforme agréée DGFiP (cf. fiches outils Pennylane, Sellsy, Axonaut, Esker dans le Hub) pour la **réception** des factures fournisseurs.
2. **Avant le 1er septembre 2027** : configurer la même plateforme (ou une autre) pour l'**émission** de tes factures clients en format électronique structuré.
3. **Audit des connecteurs** : vérifier que ton ERP / outil compta existant peut interfacer avec la plateforme cible (test sandbox documenté indispensable).
4. **Ne pas confondre** : ChorusPro (sphère publique) et les plateformes agréées (sphère B2B privée). Si ta PME facture l'État, tu utilises déjà ChorusPro depuis 2017. Pour le B2B privé, c'est une plateforme agréée.

### Sources à ajouter dans la section finale

À insérer dans la sous-rubrique « 📚 Documentation officielle & études » :
- [economie.gouv.fr — Facturation électronique B2B](https://www.economie.gouv.fr/cedef/facturation-electronique)
- [service-public.fr — Calendrier facturation électronique](https://entreprendre.service-public.fr/vosdroits/F23208)

---

## Synthèse Lot A pour Claude Code

**Volume** : 6 patches éditoriaux ciblés sur 6 modules existants.

**Effort estimé Claude Code** : 2-3 h (intégrations courtes, sans création de nouvelle structure).

**Composants à utiliser** :
- `.alert-block` ou `.callout-info` pour les encarts Article 50 sur CU-002 / CU-009 / CU-010 / CU-019
- Pas de nouveau composant à introduire

**Cohérence numérique** : aucun changement (pas de nouveau module ni fiche outil dans ce lot).

**Référence canonique** : `modules/cu-008-knowledge-base-rag.html` pour les bonnes pratiques d'intégration.

## Note Cowork

Sources prioritaires utilisées : Commission européenne (digital-strategy.ec.europa.eu, consilium.europa.eu), economie.gouv.fr, service-public.fr. Aucune source non institutionnelle. Conforme RULES § 1.1.
