# Lot C v3.10 — PR-08 nouveau préalable « Financer son projet IA en 2026 »

**Brief consolidé pour Claude Code** : création d'un **nouveau préalable PR-08** dédié au financement des projets IA pour les PME/ETI. Bloc cohérent issu de 6 dispositifs convergents (loi de finances 2026 + France 2030 + Bpifrance + Hub France IA).

**Sources** : run veille 13 mai + 18 mai 2026 (BOFIP, financeinnovation.fr, economie.gouv.fr, presse.economie.gouv.fr, entreprises.gouv.fr).

**Urgence** : 2 dispositifs à deadline imminente (5 juin 2026 AMI Solutions souveraines, 9 juin 2026 AAP Pionniers IA). Le préalable doit être publié avant ces deadlines pour avoir une utilité actionnable.

**Décision validée par Blaise** : nouveau préalable PR-08 dédié plutôt qu'enrichissement de PR-04 — sujet trop dense pour une sous-section, manque structurel à combler.

---

## Architecture du préalable PR-08

**Module cible** : `prealables/pr-08-financer-projet-ia.html` (à créer)
**Référence canonique pour la structure HTML** : `prealables/pr-07-build-vs-buy.html` (squelette 9 blocs, exec summary, sections numérotées, ressources)

**Titre du module** : « Financer son projet IA en 2026 »
**Sous-titre/accroche** : « Dispositifs fiscaux 2026, aides France 2030, financements Bpifrance — la carte complète pour un dirigeant non-IT qui veut savoir où chercher 50, 100 ou 500 K€. »
**Badge complexité** : ⭐⭐ Opérationnel
**Badge angle** : 💼 Cadrage stratégique
**Badge temps de lecture** : 18 min

### Sommaire (TOC) proposé

```html
<ul class="module-toc-list" id="tocList">
  <li><a href="#executive-summary">⚡ L'essentiel</a></li>
  <li><a href="#section-1">🧭 Pourquoi financer en 2026 change tout</a></li>
  <li><a href="#section-2">💰 Fiscalité IA 2026 — CIR, CII, nouveau CII-IA, JEI, JEII</a></li>
  <li><a href="#section-3">🚀 France 2030 — Plan « Osez l'IA » et ses dispositifs</a></li>
  <li><a href="#section-4">⏰ Deux deadlines à ne pas manquer juin 2026</a></li>
  <li><a href="#section-5">🏦 Financements Bpifrance — diagnostics, prêts, capital</a></li>
  <li><a href="#section-6">🛠️ Méthode — empiler les dispositifs sans erreur</a></li>
  <li><a href="#section-7">🚀 Plan d'action 30 jours</a></li>
  <li><a href="#ressources">📚 Pour aller plus loin</a></li>
</ul>
```

---

## Contenu détaillé par section

### Executive summary (à transposer en `.exec-summary`)

**Titre exec** : *« 2026 est la meilleure année depuis 10 ans pour financer un projet IA en PME — à condition de connaître la carte »*

**5 takeaways** (à transposer en `.exec-takeaway`) :

1. **La loi de finances 2026 crée un nouveau Crédit d'Impôt Innovation IA (CII-IA)** qui intègre les dépenses de calcul intensif (GPU, CPU) — un dispositif inédit qui peut couvrir une part significative des coûts d'inférence pour les PME ayant des projets agentiques.
2. **CIR, CII, JEI sont maintenus et prorogés jusqu'en 2028 minimum.** Le CICO (Crédit Impôt Recherche Collaborative) et le C3IV (Crédit Impôt Industrie Verte) sont prorogés jusqu'au 31 décembre 2028.
3. **Le plan France 2030 « Osez l'IA »** finance les diagnostics Data IA à hauteur de **40 % de leur coût** + prêts garantis État via Bpifrance + programme d'accélération 18 mois. Cible prioritaire : PME 10-2000 salariés, CA > 250 K€.
4. **Deux deadlines à ne pas manquer en juin 2026** : AMI Solutions souveraines IA (5 juin) + AAP « Pionniers de l'IA » (9 juin). Enveloppes France 2030.
5. **L'empilement des dispositifs** (CIR + CII-IA + JEII + diagnostic Bpifrance + AAP régional) peut financer 40 à 60 % d'un projet IA PME — à condition de respecter la séquence et les critères d'éligibilité.

**Stat block** suggéré (à transposer en `.exec-stats`) :

- **25 M€** — enveloppe France 2030 IA Booster initiale
- **40 %** — taux de prise en charge des diagnostics Data IA
- **15 M** — professionnels formés visés d'ici 2030
- **240 M€** — investis par Bpifrance en capital développement IA en 2025 (vs 17 M€ en 2024, ×14)

### Section 1 — Pourquoi financer en 2026 change tout

**3 ruptures de l'année 2026** :

1. **Création d'un dispositif fiscal dédié IA** : le **CII-IA** intègre explicitement les dépenses de calcul intensif. Avant 2026, ces coûts étaient mal couverts par les dispositifs classiques.
2. **France 2030 entre dans sa phase « diffusion »** : après avoir financé les startups, le plan vise désormais la **généralisation IA dans les PME** via le programme « Osez l'IA ».
3. **Convergence Bpifrance + DGE + Hub France IA** : trois opérateurs publics coordonnent leur action en 2026 (ce n'était pas le cas en 2024-2025).

**Implication pour le dirigeant PME** : il y a aujourd'hui **plus d'argent public disponible pour les projets IA PME qu'à aucun moment depuis 2015** — mais la cartographie est complexe et les guichets multiples. Ce préalable donne la carte.

### Section 2 — Fiscalité IA 2026 — CIR, CII, nouveau CII-IA, JEI, JEII

**Loi de finances 2026** (loi n° 2026-103 du 19 février 2026) — récapitulatif des 6 dispositifs fiscaux pertinents :

| Dispositif | Statut 2026 | Cible | Spécificité IA |
|---|---|---|---|
| **CIR (Crédit Impôt Recherche)** | Maintenu sans changement, prorogé jusqu'en 2028 minimum | Toutes entreprises (R&D) | Applicable aux projets IA en R&D |
| **CII (Crédit Impôt Innovation)** | Maintenu sans changement | PME au sens européen | Applicable aux projets IA d'innovation produit |
| **🆕 CII-IA (Crédit Impôt Innovation IA)** | **Nouveau dispositif 2026** | PME au sens européen | **Intègre les dépenses de calcul intensif (GPU, CPU)** pour soutenir les projets IA et infrastructures numériques de recherche |
| **JEI (Jeune Entreprise Innovante)** | Statut prolongé | Startups <8 ans, ≥15 % R&D | Avantages fiscaux + sociaux |
| **🆕 JEII (Jeune Entreprise d'Innovation à Impact)** | **Nouvelle catégorie créée par art. 23 LF 2026** | Startups réalisant 5-20 % R&D **ET** critères ESS (économie sociale et solidaire) | Ouvre des dispositifs aux startups à impact |
| **CICO (Crédit Impôt Recherche Collaborative)** | Prorogé jusqu'au 31 décembre 2028 | Partenariats public-privé | Renforce les collaborations laboratoires |
| **C3IV (Crédit Impôt Industrie Verte)** | Prorogé jusqu'au 31 décembre 2028 | Industries vertes | Applicable aux projets IA pour l'environnement |

**Implication PME** :
- Une PME avec un projet IA classique (CRM augmenté, automatisation) → **CII** (et CII-IA si dépenses GPU/CPU significatives)
- Une PME en R&D IA (modèle interne, fine-tuning) → **CIR** (et CIR + CII-IA cumulables sur dépenses distinctes)
- Une startup IA <8 ans → **JEI** (et JEII si critères ESS)

### Section 3 — France 2030 — Plan « Osez l'IA » et ses dispositifs

**Plan « Osez l'IA » + IA Booster France 2030** :

- **Diagnostics Data IA** : 40 % du coût pris en charge, expertise technique + identification de cas d'usage concrets
- **Prêts garantis État via Bpifrance** pour gros projets
- **Programme d'accélération 18 mois** : formation collective + immersion (ouvert fin 2025)
- **Objectif 15 M professionnels formés d'ici 2030** via Compétences & Métiers d'Avenir
- **Enveloppe initiale IA Booster** : 25 M€
- **Cible prioritaire** : PME 10-2000 salariés, CA > 250 K€

**Implication PME** : le diagnostic Data IA est le **premier guichet à actionner** pour une PME qui démarre — il identifie les cas d'usage et qualifie l'éligibilité aux autres dispositifs.

### Section 4 — Deux deadlines à ne pas manquer juin 2026

> ⏰ **Échéances proches** — deux AAP/AMI complémentaires France 2030 avec des deadlines en juin 2026

**Dispositif 1 — AMI Solutions souveraines IA pour PME/ETI** :
- Émetteur : DGE + SGPI, appui Hub France IA
- Objectif : constitution d'un **annuaire d'acteurs IA souveraines**
- **1re deadline : 5 juin 2026** (puis dépôt au fil de l'eau)
- Cible : PME/ETI éditrices ou intégratrices de solutions IA souveraines
- Source : presse.economie.gouv.fr

**Dispositif 2 — AAP « Pionniers de l'Intelligence Artificielle »** :
- Émetteur : Plan France 2030
- Objectif : projets IA breakthrough
- **Deadline : 9 juin 2026**
- Cible : startups et PME avec projets IA de rupture
- Source : entreprises.gouv.fr

**Action attendue d'un dirigeant PME concerné** : vérifier l'éligibilité **dans les 7 jours** suivant la lecture de ce module si projet existant ; sinon prendre contact avec un conseiller Bpifrance pour qualification rapide.

### Section 5 — Financements Bpifrance — diagnostics, prêts, capital

**Bpifrance — 4 leviers IA 2025-2026** :

1. **Diagnostics Data IA** (intégré au plan Osez l'IA, 40 % de prise en charge)
2. **460 Data AI Diagnostics réalisés** en 2025 (référence de volume)
3. **9 403 dirigeants formés** à l'IA via Bpifrance Université (Curriculum IA)
4. **240 M€ investis** en capital développement IA en 2025 (vs 17 M€ en 2024)
5. **15 000+ PME formées/sensibilisées** à l'IA en 2025

**Implication PME** : Bpifrance est le **guichet unique d'entrée** pour qualifier son projet IA et identifier les dispositifs adaptés. Le diagnostic Data IA est gratuit ou cofinancé (40 % via Osez l'IA).

### Section 6 — Méthode — empiler les dispositifs sans erreur

**Règle des 5 étapes** :

1. **Faire le diagnostic Data IA Bpifrance** (point d'entrée — qualifie le projet, identifie cas d'usage, oriente vers dispositifs)
2. **Identifier les dépenses éligibles CIR ou CII** (R&D vs innovation produit — pas le même formulaire ni la même administration)
3. **Si dépenses GPU/CPU significatives** : ajouter le **CII-IA** (cumulable avec CII classique sur dépenses distinctes)
4. **Si éligible JEI ou JEII** : valoriser les avantages fiscaux et sociaux (réduction charges)
5. **Candidater aux AAP régionaux ou France 2030** si projet de rupture (AMI souveraine + AAP Pionniers en cours)

**Pièges à éviter** :

- ⚠️ Confondre CIR (R&D) et CII (innovation produit) — formulaires et administrations différentes
- ⚠️ Demander le CII-IA sans dépenses GPU/CPU documentées — risque de redressement
- ⚠️ Candidater à un AAP sans avoir le diagnostic Bpifrance préalable — taux de succès très bas
- ⚠️ Cumuler des dispositifs sans vérification d'éligibilité croisée — risque de récupération a posteriori
- ⚠️ Oublier les **AAP régionaux** — la Région Grand Est a ses propres dispositifs IA complémentaires (vérifier sur grandest.fr)

### Section 7 — Plan d'action 30 jours

**Jours 1-7 — Cadrage**
- Identifier le ou les projets IA candidats au financement
- Estimer les dépenses prévisionnelles (calcul, RH, prestataires)
- Vérifier si l'entreprise est éligible JEI / JEII / PME au sens européen

**Jours 8-14 — Diagnostic**
- Contacter Bpifrance pour demander un **diagnostic Data IA**
- Préparer les éléments du diagnostic : description du projet, données disponibles, équipe, budget

**Jours 15-21 — Cartographie des dispositifs**
- Lister les dispositifs éligibles (CIR, CII, CII-IA, JEI/JEII, AAP)
- Identifier les éventuels recoupements avec les dispositifs régionaux Grand Est
- Vérifier les deadlines (notamment juin 2026 si urgence AMI/AAP)

**Jours 22-30 — Activation**
- Préparer les dossiers fiscaux (CIR/CII en amont de la déclaration de résultats)
- Si AAP en cours : monter le dossier de candidature
- Si demande de prêt Bpifrance : préparer business plan + plan de trésorerie

---

## Ressources à intégrer

### Articles de fond
- **BOFIP** — Actualités fiscales IA 2026 (bofip.impots.gouv.fr/bofip/15020-PGP.html/ACTU-2026-00067)
- **Finance Innovation** — CIR, CICO et C3IV : LF 2026 promulguée (financeinnovation.fr/2026/02/23/cir-cico-et-c3iv-la-loi-de-finances-2026-a-ete-promulguee-au-journal-officiel)
- **Zabala** — Loi finances 2026 CIR (zabala.fr/actualites/loi-finances-2026-cir)
- **Exoqua** — PLF 2026 fiscalité innovation (exoqua.com/post/plf-26-fiscalite-de-l-innovation-2026)

### Tutoriels & cas pratiques
- **Economie.gouv.fr** — Plan « Osez l'IA » (economie.gouv.fr/actualites/osez-lia-un-plan-pour-diffuser-lia-dans-toutes-les-entreprises)
- **Presse.economie.gouv.fr** — AMI Solutions souveraines IA 2026
- **Entreprises.gouv.fr** — AAP Pionniers de l'IA (deadline 9 juin 2026)
- **Bpifrance Le Lab** — Etudes IA 2025-2026 (lelab.bpifrance.fr)

### Documentation officielle & études
- **DGFiP** — Page officielle CIR / CII / CII-IA
- **Bpifrance** — Page diagnostics Data IA
- **France 2030** — Page IA Booster

### Contacts opérationnels
- **Bpifrance Grand Est** — interlocuteurs régionaux (à enrichir avec coordonnées)
- **Hub France IA** — pour AMI Solutions souveraines
- **Région Grand Est** — dispositifs IA complémentaires (grandest.fr)

---

## Mise à jour RULES / glossaire chiffres-clés

Le **glossaire des chiffres-clés** RULES § 1.2.3 doit être actualisé :
- Nombre de préalables PR : **7 → 8** (PR-08 ajouté)

Lieux à mettre à jour :
- `index.html` (meta, hero stats, filter count haut + bas, section À propos)
- `prealables.html` (meta, accroche, footer-cta, nouvelle card PR-08)
- `architectures.html`, `ressources.html` (badges si pertinent)
- `README.md`
- Footers de tous les modules CU et PR (mention « 8 préalables »)
- Méta-descriptions de toutes les pages

## Mise à jour navigation et page préalables

- Ajouter une **card PR-08** dans `prealables.html` (suivre le template des cards existantes PR-01 à PR-07)
- Position dans la liste : à la suite de PR-07 (ordre numérique)
- Icône suggérée : 💰 ou 🏦
- Catégorie : « Financement & dispositifs »
- Cross-link depuis PR-04 (Marché IA & emploi) en encart : « Pour le détail des dispositifs de financement IA 2026, voir PR-08 »

## Métadonnées module

- `<meta name="description">` : *« Financer son projet IA en 2026 : CIR, CII, nouveau CII-IA, JEI/JEII, plan Osez l'IA, AAP France 2030. La carte complète pour une PME non-IT qui veut savoir où chercher 50, 100 ou 500 K€. »*
- Badge temps de lecture : **18 min**

## Item parallèle (à compiler dans brief v3.10)

Pas de canonisation chiffre macro spécifique — les chiffres de ce préalable sont contextuels au financement, pas réutilisables ailleurs comme chiffres macro IA. **Exception possible** : le « 240 M€ Bpifrance capital développement IA 2025 vs 17 M€ en 2024 (×14) » pourrait être canonisé dans `chiffres-macro-2026.md` car réutilisable dans PR-04. À arbitrer côté couple 2.
