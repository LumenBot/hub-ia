# Lot B v3.10 — Réglementaire & conformité (CU-020 ×3, CU-024)

**Brief consolidé pour Claude Code** : 4 patches réglementaires à dates serrées. CU-020 reçoit 3 actualisations majeures (AI Act Art. 50 Draft Guidelines + fiches CNIL finales + guide HAS-CNIL). CU-024 reçoit un patch terminologique (PDP → PA) + actualisation calendrier.

**Sources** : run veille 13 mai + 18 mai 2026 (Commission EU, CNIL, HAS-CNIL, DGFiP, economie.gouv.fr).

**Urgence** : applicabilité AI Act Art. 50 au **2 août 2026**, consultation publique close **3 juin 2026**, calendrier facturation électronique au **1er septembre 2026**. Patches à intégrer rapidement.

---

## Patch B.1 — CU-020 — AI Act Art. 50 Draft Guidelines (publiées 8 mai 2026)

**Module cible** : `modules/cu-020-conformite-rgpd-ai-act.html`
**Position** : actualisation de la section AI Act Article 50 existante (depuis v3.8). Pas de nouvelle section.

### Contenu à intégrer

**Cadrage de la publication** :

Le 8 mai 2026, la Commission européenne a publié les **premières lignes directrices (non contraignantes) couvrant l'intégralité du périmètre de l'article 50 AI Act** : transparence pour interactions IA, deepfakes, contenus IA-générés, reconnaissance émotionnelle, catégorisation biométrique.

**Calendrier à actualiser dans la section** :

- **8 mai 2026** : publication des Draft Guidelines
- **3 juin 2026** : clôture de la consultation publique ciblée
- **2 août 2026** : applicabilité confirmée des obligations Art. 50

**Obligations confirmées au 2 août 2026** :

Pour les **fournisseurs de systèmes IA** :
- Informer les utilisateurs lorsqu'ils interagissent avec une IA (interfaces conversationnelles)
- Implémenter des **marques machine-readable dans les systèmes d'IA générative** pour permettre la détection automatique de contenu synthétique

Pour les **déployeurs (entreprises utilisatrices)** :
- Informer les personnes exposées à des deepfakes
- Informer en cas de publications IA-générées sur sujets d'intérêt public
- Informer en cas d'usage de systèmes de reconnaissance émotionnelle ou catégorisation biométrique

**Précisions importantes à intégrer** :

- Le caractère **non contraignant** des Draft Guidelines (orientation pour les opérateurs, pas obligation juridique en tant que telles — l'obligation vient de l'AI Act lui-même)
- La publication en parallèle du **Code of Practice on Transparency of AI-Generated Content** (2e draft publié le 5 mars 2026)
- L'importance pratique pour les PME : ces Draft Guidelines précisent **comment** appliquer les obligations Art. 50, pas seulement quoi appliquer.

### Sources à ajouter

- **Commission européenne** — Draft Guidelines on transparency obligations under Article 50 AI Act (digital-strategy.ec.europa.eu, 8 mai 2026)
- **Commission européenne** — Public consultation (clôture 3 juin 2026)
- **Inside Global Tech** — 10 takeaways European Commission Draft Guidelines on AI transparency (insideglobaltech.com, 12 mai 2026)

### Renvois croisés

- Garder cohérence avec les encarts existants CU-002, CU-009, CU-010, CU-019 (renvoyer vers CU-020 actualisé)
- Cohérence avec **Code of Practice on Transparency of AI-Generated Content** — mention explicite

---

## Patch B.2 — CU-020 — Fiches IA finales CNIL + Guide HAS-CNIL

**Module cible** : `modules/cu-020-conformite-rgpd-ai-act.html`
**Position** : nouvelle sous-section ou encart à intégrer dans la section consacrée à la CNIL (selon état actuel du module).

### Contenu à intégrer

**Fiches IA finales CNIL (publication 2026)** :

La CNIL a publié ses recommandations finales sur l'IA et le RGPD, couvrant 3 thèmes opérationnels :

1. **Applicabilité du RGPD aux modèles IA** : un modèle entraîné sur des données personnelles est lui-même un traitement de données personnelles potentiel
2. **Exigences de sécurité dans le développement IA** : security-by-design + tests de robustesse + traçabilité des données d'entraînement
3. **Conditions d'annotation des données d'entraînement** : information des annotateurs + bases légales applicables + droits d'accès et rectification

**Guide HAS-CNIL « Accompagner le bon usage des systèmes d'IA »** (mars 2026, consultation publique close 16 avril 2026) :

- **10 fiches dédiées au cycle de vie** des systèmes IA (cadrage → conception → développement → déploiement → suivi)
- **2 fiches transverses** : gouvernance et GenAI

**Impact pour la PME** :
- Pour toute PME secteur santé / médico-social / éditrice d'IA traitant des données personnelles : le guide HAS-CNIL devient la référence opérationnelle.
- Pour les PME tertiaires : les fiches IA finales CNIL doivent être consultées avant tout projet IA exploitant des données personnelles (clients, candidats, employés).

### Sources à ajouter

- **CNIL** — IA et RGPD : recommandations finales (cnil.fr/fr/ia-et-rgpd-la-cnil-publie-ses-nouvelles-recommandations, 2026)
- **CNIL × HAS** — Guide « Accompagner le bon usage des systèmes d'IA » (cnil.fr/sites/default/files/2026-03/guide_has_cnil_recommandations_ia.pdf, mars 2026)

### Renvois croisés

- **CU-007 (RH/CV)** : encart « annotation des données candidats » avec renvoi vers CU-020 fiche CNIL annotation.
- **PR-05 (Sécurité IA)** : signalement des « exigences de sécurité dans le développement IA » CNIL.

---

## Patch B.3 — CU-020 — Encart de synthèse 2026

**Module cible** : `modules/cu-020-conformite-rgpd-ai-act.html`
**Position** : nouvel encart en tête de module ou en synthèse de section AI Act.

### Contenu à intégrer

**Encart de synthèse — calendrier 2026 à anticiper** :

> 📅 **3 échéances réglementaires PME 2026 à anticiper** :
>
> - **3 juin 2026** : clôture consultation publique Draft Guidelines Art. 50 AI Act
> - **2 août 2026** : applicabilité Art. 50 AI Act (transparence interactions IA, deepfakes, contenus IA-générés)
> - **2 décembre 2026** : watermarking obligatoire (reporté par Omnibus VII)
>
> En parallèle, les **fiches IA finales CNIL** (applicabilité RGPD aux modèles, exigences sécurité, annotation données) et le **guide HAS-CNIL santé** (12 fiches) deviennent des références opérationnelles applicables maintenant.

### Métadonnées module

- `<meta name="description">` : actualiser pour mentionner les 3 échéances 2026 (suggestion : *« 3 échéances réglementaires IA à anticiper en 2026 : juin (consultation Art. 50), août (applicabilité), décembre (watermarking). Comprendre AI Act, RGPD, fiches CNIL et guide HAS-CNIL. »*)
- Badge temps de lecture : passer à **+4 min** (estimation cumulée des 3 patches B.1+B.2+B.3).

---

## Patch B.4 — CU-024 — Terminologie PDP → PA + actualisation calendrier

**Module cible** : `modules/cu-024-order-to-cash.html`
**Position** : patch terminologique transverse sur l'ensemble du module + actualisation de l'encart calendrier.

### Contenu à intégrer

**Patch terminologique** :

La **loi de finances 2026 (art. 27)** a officiellement renommé les **« plateformes de dématérialisation partenaires » (PDP)** en **« plateformes agréées » (PA)**.

À effectuer dans le module :
- **Remplacer toutes les occurrences** de « PDP », « plateformes PDP », « plateformes de dématérialisation partenaires » par « PA », « plateformes agréées »
- Ajouter en première occurrence une note historique : *« anciennement PDP (plateformes de dématérialisation partenaires), renommées PA par l'art. 27 LF 2026 »*

**Actualisation chiffrée** :

- **125 plateformes agréées immatriculées définitivement** par la DGFiP au 5 mai 2026
- + 17 dossiers en attente d'immatriculation
- Liste évoluant chaque semaine sur impots.gouv.fr

**Actualisation calendrier** :

- **1er septembre 2026** : réception obligatoire pour **toutes** les entreprises (toutes tailles confondues)
- **1er septembre 2026** : émission obligatoire **grandes entreprises + ETI**
- **1er septembre 2027** : émission obligatoire **PME/TPE**

### Sources à ajouter

- **DGFiP — Facturation électronique et plateformes agréées** (impots.gouv.fr/facturation-electronique-et-plateformes-agreees)
- **Economie.gouv.fr** — Liste des 101 premières plateformes agréées (mai 2026)
- **Service public entreprises** — Actualité PA (entreprendre.service-public.gouv.fr/actualites/A18759)

### Renvois internes

- Encart « calendrier 2026 » en tête de module à actualiser avec les 3 dates précises
- Liste DGFiP en lien externe direct dans la section « Choisir sa plateforme »

### Métadonnées module

- `<meta name="description">` : actualiser pour intégrer la terminologie PA et le calendrier 1er septembre 2026/2027.
- Badge temps de lecture : pas de changement significatif (patch terminologique).

---

## Synthèse cohérence Lot B

Les 4 patches forment un bloc réglementaire **temporel cohérent** centré sur le 2e semestre 2026 :
- **3 juin 2026** : consultation Art. 50 (B.1)
- **2 août 2026** : applicabilité Art. 50 (B.1 + B.3)
- **1er septembre 2026** : facturation électronique réception (B.4)
- **2 décembre 2026** : watermarking (B.3 rappel — déjà intégré v3.8)

Cohérence narrative : 2026 est l'année où la **conformité IA devient opérationnelle** pour les PME — pas seulement théorique. Cette narration peut être renforcée dans l'encart B.3.

## Item parallèle (à compiler dans brief v3.10)

Aucun nouveau chiffre macro à canoniser pour ce Lot B (les dates et calendriers sont contextuels, pas des chiffres macro réutilisables cross-modules).
