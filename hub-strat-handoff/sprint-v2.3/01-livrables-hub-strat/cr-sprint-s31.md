# CR sprint S3.1 — fin de sprint + ordre du jour S3.2

**Date de clôture S3.1** : vendredi 29 mai 2026 (dépôt anticipé mardi 26 mai en session active)
**Période S3.1** : 25-29 mai 2026
**Garant** : Cowork Hub Strat
**Destinataire** : Cavalli — pour arbitrages et ouverture S3.2 lundi 1er juin

---

## 1. Livrables produits en S3.1

| # | Livrable | Type | Localisation | Statut |
|---|----------|------|--------------|--------|
| 1 | Note de cadrage Hub Strat v1 | Structurant | `outputs/note-cadrage-hub-strat-v1.md` | ✅ Livré, validé Cavalli |
| 2 | Notification canal head Initiative IA | Structurant (notification) | `outputs/NOTIFICATION-CANAL-HEAD-INITIATIVE-IA.md` | ✅ Préexistant, lu et intégré |
| 3 | Avenant `_instructions.md` v1.1 (règle 3 réécrite) | Structurant | `_instructions.md` (versionné) | ✅ Livré, validé Cavalli |
| 4 | Scoping espace persona Hub v2 v0 | Intermédiaire | `travail/personas/scoping-espace-persona-v0.md` | ✅ Déposé |
| 5 | Préparation protocole S3.2 v0 (grille 6 critères + cartographie sources) | Intermédiaire | `travail/personas/preparation-protocole-s32-v0.md` | ✅ Déposé |
| 6 | CR sprint S3.1 (ce document) | Gouvernance | `outputs/cr-sprint-s31.md` | ✅ En cours de livraison |

Sprint S3.1 livré **en avance** sur le planning initial (4 livrables + le CR, là où le sprint nominal prévoyait 1 livrable structurant). La fenêtre 27-29 mai reste disponible pour itération sur retours Cavalli ou amorçage S3.2 / S3.3.

---

## 2. Observations critiques portées en S3.1

### 2.1 Trois tensions résolues

- **Tension Vianeo séquentielle vs lean itératif parallèle** → résolue par réécriture règle 3 du `_instructions.md` en v1.1 (grille à 4 dimensions itérée en parallèle + 4 règles de cohérence inter-modules).
- **Tension StarterClass canonique vs mode désirabilité documentaire** → résolue par clause explicite ajoutée à la règle 3 v1.1 (écart méthodologique assumé, bascule vers interviews légères activable si signaux insuffisants).
- **Tension architecture 5 acteurs vs 10 acteurs** → résolue par intégration de la cartographie d'orchestration v1.0 dans la note de cadrage (section 2) et par adoption de la contrainte de design « bloc résumé exécutif transmissible » sur chaque livrable structurant (mitigation risque méta-gouvernance #1).

### 2.2 Un point structurant nouveau

L'arbitrage Cavalli du 26 mai sur l'**élargissement de l'espace persona au-delà de Camille** (Camille = un exemple, pas la persona unique) a élargi le scope du module 2 Désirabilité. Conséquences portées : reformulation H1 (espace persona à cartographier puis prioriser), reformulation livrable S3.2 (« protocole de cartographie et priorisation personas » au lieu de « protocole d'analyse documentaire persona Camille »), volet quantitatif ajouté (sources INSEE / Bpifrance / DGE / Apec).

Scoping ouvert produit : **14 profils** en 5 familles (généralistes, opérationnels-transverses, fonctionnels, techniques accidentels, porteurs indirects).

### 2.3 Une zone d'inconnu à clarifier rapidement

L'**approche sectorielle vs transverse** n'est pas tranchée. La vision Hub v2 est transverse, mais la grille StarterClass J4 (Pain DUR vs Vitamine) suggère que la douleur IA est probablement plus aiguë dans certains secteurs (industrie + services BtoB) que dans d'autres. À arbitrer en S3.2 — ne peut pas rester implicite.

---

## 3. Points à arbitrer pour ouverture S3.2 sereine — 10 questions consolidées

Reprise des 5 questions ouvertes du scoping v0 + 5 questions ouvertes du document préparation protocole. Toutes peuvent être arbitrées en bloc ou différées — pas de blocage absolu pour démarrer S3.2, mais plus elles sont arbitrées tôt, moins on perd de temps en allers-retours.

### Bloc A — Scope persona

1. **Inclusion / exclusion du profil E1** (consultant indépendant senior accompagnant PME-ETI) ? Choix structurant pour la stratégie d'acquisition — early adopter rentable mais rupture vs cible dirigeants en entreprise.
2. **Approche sectorielle ou transverse** ? Confirmation de la vision transverse, ou identification d'un secteur prioritaire en première itération (probable : industrie + services BtoB) ?
3. **Plafond du nombre de personas prioritaires** retenus en sortie de S3.2 : 1 / 2-3 / 4-5 ? Trade-off profondeur vs largeur.

### Bloc B — Méthodologie de priorisation

4. **Pondération des 6 critères** (proposition : C2 Pain 25 %, C3 DàP 20 %, C5 différenciation 20 %, C1 taille 15 %, C4 canal 15 %, C6 alignement 5 %) : OK telle quelle ou ajustements ?
5. **Règle de bloquant** (note ≤ 1 sur C1/C2/C3/C5 ou note = 0 sur C6 → persona éliminé quelle que soit la moyenne) : OK ?
6. **Seuils de priorisation** (note ≥ 4,0 top, 3,0-3,9 watching, 2,0-2,9 à surveiller, < 2,0 écarté) : OK ?
7. **Plancher de taille de population** sous lequel un profil est éliminé (par ex. < 1 000 individus en France) ? Ou pas de plancher, tout profil défendable conservé ?

### Bloc C — Outils et format

8. **Budget LinkedIn Sales Navigator (~90 €/mois)** autorisé en outil Hub Strat ? Influe sur la qualité d'objectivation C1 et C4 (qualification des canaux d'acquisition).
9. **Format de stockage des signaux** extraits (markdown structuré dans `travail/personas/signaux/` vs base Airtable / Notion) : préférence ?
10. **Transmissions croisées différées** (réponse Cavalli du 26 mai) : confirmation que les notifications aux canaux pairs (Hub Content, Hub RAG, Claude Design, DEV IA Head) restent en attente jusqu'à demande explicite ?

---

## 4. Ordre du jour S3.2 proposé (1-5 juin)

Sous réserve des arbitrages bloc A, B, C ci-dessus. Plan de charge indicatif :

| Jour | Travail | Livrable de fin de journée |
|------|---------|----------------------------|
| **Lun 1 juin** | Rédaction protocole v1 — sections 1 à 4 (objet, espace persona consolidé, grille critères validée, échelles) | Brouillon protocole 50 % |
| **Mar 2 juin** | Rédaction protocole v1 — sections 5 à 7 (cartographie sources validée, grille extraction, workflow) | Brouillon protocole 90 % |
| **Mer 3 juin** | Test pilote sur 2-3 personas (B1 Camille / E1 Consultant / A1 Fondateur PME) | Note test pilote |
| **Jeu 4 juin** | Itération protocole post-test + amorçage cartographie concurrentielle S3.3 (gain de temps) | Protocole v1 finalisé |
| **Ven 5 juin** | Check pré-livrable + transmission + CR sprint S3.2 + plan S3.3 | **Livrable structurant : Protocole de cartographie et priorisation personas Hub v2 v1** + CR S3.2 |

---

## 5. Risques identifiés pour S3.2 (à surveiller)

- **Si arbitrages Cavalli différés > mer 3 juin** : risque sur l'application pilote (qui dépend de la grille validée). Mitigation : test pilote sur grille « best guess Hub Strat » avec mention explicite « sous réserve d'ajustements ».
- **Si LinkedIn Sales Nav non autorisé** : qualité d'objectivation C1 dégradée → note C1 portée à intervalle de confiance plus large, à signaler dans le protocole.
- **Si approche transverse confirmée et plafond personas = 1** : tension à arbitrer (le persona unique ne peut pas être transverse sans dilution). Mitigation : proposer 2 personas minimum dans ce cas.

---

## 6. Avance et bandwidth disponible

Sprint S3.1 livré en 2 jours sur 5. Bandwidth disponible 27-29 mai pour :
- Itérations sur retours Cavalli sur les livrables produits
- Amorçage anticipé de la cartographie concurrentielle S3.3 (premiers crawls sites concurrents Bpifrance Hub IA / French AI Lab / Diagnostic IA Numeum)
- Ou pause / attente arbitrages — selon ta préférence.

Question fermée : **tu préfères que je continue à pousser en avance (S3.2 ou S3.3 anticipé), ou j'attends ton retour sur les 10 arbitrages avant de reprendre ?**

---

*CR de sprint Hub Strat — gouvernance interne canal. Versioning du CR : un par sprint, nommé `cr-sprint-sX.Y.md`.*
