# Protocole de cartographie et priorisation personas Hub v2 — v1

**Version** : v1 — 26 mai 2026 (dépôt anticipé sur jalon vendredi 5 juin)
**Statut** : livrable structurant S3.2 — protocole opérationnel + application complète sur les 14 profils de l'espace persona + top 5 personas prioritaires consolidé
**Garant** : Cowork Hub Strat — proposé à Cavalli pour validation
**Modules Vianeo activés** : 2 Désirabilité (cœur) + transverse acceptabilité / faisabilité
**Mode** : désirabilité documentaire (arbitrage Cavalli 25 mai — pas d'interviews terrain en première phase)

---

## 1. Synthèse exécutive

Application de la grille des 6 critères de priorisation validée Cavalli (arbitrages 4-7 du 26 mai) à l'ensemble des **14 profils** identifiés en scoping ouvert. **Cinq personas prioritaires (top tier)** émergent avec notes ≥ 3,65 :

| Rang | Code | Persona | Note | Famille |
|------|------|---------|------|---------|
| **1** | **E1** | Consultant indépendant senior IA | **4,15** | Porteur indirect — double registre cible + canal d'évangélisation |
| **2=** | **B1** | COO ETI industrielle (Camille type) | **3,90** | Opérationnel-transverse — cœur vision Hub v2 |
| **2=** | **B2** | COO ETI services / tertiaire | **3,90** | Opérationnel-transverse — élargissement secteur |
| **4** | **B4** | Directeur / Chief Transformation Officer | **3,85** | Opérationnel-transverse — rôle dédié transfo |
| **5** | **C5** | Responsable innovation / R&D | **3,65** | Fonctionnel — prescripteur d'outils |

Six personas en **watching** (notes 3,00-3,55) — A1 fondateur PME, D1 DSI accidentel, D2 DPO/juridique, B3 Dir Ops PME, et deux ex aequo techniques. Quatre personas **à surveiller mais non prioritaires** (notes < 3,00). **Un persona écarté par règle de bloquant** : C3 Directeur marketing (note 3,05 mais C5 différenciation = 1 — concurrence frontale outils marketing IA spécialisés type Jasper, Copy.ai, Joggle UK).

**Trois observations structurelles** :

1. **Le Pain (C2) est le critère le plus discriminant** — les 4 premiers personas ont tous C2 ≥ 4. Hub v2 doit prioritairement adresser des profils où le Pain DUR est documenté.
2. **La disposition à payer (C3) n'est pas un frein sur le top tier** — les 5 premiers personas ont tous C3 ≥ 4. Le pricing 29 €/mois est compatible avec leur capacité d'achat.
3. **B1 (industrie) + B2 (services) émergent ex aequo** — signal en faveur d'une **double vertical sectorielle** plutôt qu'une approche purement transverse. À arbitrer Cavalli (point 16 réouvert).

**Trois recommandations actées** pour les sprints suivants :

- **S3.5 modélisation économique** : chiffrer les segments [E1 + B1 + B2 + B4 + C5] avec hypothèses de conversion différenciées (E1 = freelance → réactivité achat élevée, B1/B2/B4 = ETI → cycle B2B plus long mais ticket plus élevé via tier Équipe potentiel).
- **S3.6 plan d'acquisition** : E1 mobilisable via Malt + LinkedIn + communautés freelance dès Étape 1 ; B1/B2 via écosystème Grand Est (CCI, France Industrie, French Tech Est) sur cycle 6-12 mois ; B4 via communautés CDO/CTO (CIO Forum, CDO Days).
- **S3.7 itération produit** : différenciation E1 vs B1/B2/B4 sur la matière éditoriale — E1 a besoin de profondeur veille + outils Pro pour outiller ses missions ; B1/B2/B4 ont besoin de cadrage stratégique + accompagnement décision.

---

## 2. Objet du protocole

Ce document formalise le **protocole opérationnel de cartographie et priorisation des personas Hub v2** appliqué aux 14 profils identifiés en scoping ouvert (cf. `travail/personas/scoping-espace-persona-v0.md`). Il consigne :

1. La méthodologie (mode désirabilité documentaire, arbitrage Cavalli 25 mai)
2. La grille des 6 critères de priorisation (validée Cavalli arbitrages 4-7 du 26 mai)
3. L'application complète sur les 14 profils
4. La consolidation top 5 personas prioritaires + watching + écartés
5. Les inflexions méthodologiques actées
6. L'articulation avec la cartographie concurrentielle v1 (S3.3)
7. Les préconisations pour les sprints suivants

Le protocole est **versionné et reproductible** : la grille peut être réappliquée en S3.7 (cartographie concurrentielle v2 → réajustement scores C5) ou après remontée de signaux contraires (bascule interviews légères §10.4 de la note de cadrage v1).

---

## 3. Méthodologie — mode désirabilité documentaire

Conformément à l'arbitrage Cavalli 25 mai et à la règle 3 du `_instructions.md` v1.1 (clause mode désirabilité documentaire), le protocole opère **sans interviews terrain en première phase**. Les hypothèses produites sont des **hypothèses non encore réfutées par confrontation terrain**, pas des conclusions validées.

Sources documentaires mobilisées (détail dans `travail/personas/preparation-protocole-s32-v0.md` §B) :

- **F1** — Benchmark concurrentiel direct (cf. cartographie concurrentielle v1)
- **F2** — Reviews et plateformes d'avis (G2, Capterra, Trustpilot)
- **F3** — Forums et LinkedIn (groupes pros, communautés)
- **F4** — Presse spécialisée et études (Les Échos, Maddyness, BCG, France Industrie, baromètres Bpifrance Le Lab)
- **F5** — Veille existante Hub Content (cumulatifs sectoriels, financements, événements, acteurs-clés)
- **F6** — Sources quantitatives (INSEE, Bpifrance, DGE, Apec, Malt, Comet)

**Bascule activable** vers interviews légères (5-8 entretiens 30 min) si signaux documentaires trop faibles ou trop divergents sur un persona prioritaire — point d'arbitrage différé (jalon fin S3.4 / 19 juin).

---

## 4. Grille des 6 critères de priorisation

Rappel synthétique — détail opérationnel dans `travail/personas/preparation-protocole-s32-v0.md`.

| Code | Critère | Type | Pondération | Bloquant si |
|------|---------|------|-------------|-------------|
| C1 | Taille population accessible en France | Quantitatif | 15 % | Note ≤ 1 |
| **C2** | Intensité du Pain (DUR vs Vitamine) | Qualitatif | **25 %** | Note ≤ 1 |
| C3 | Disposition à payer 29 €/mois | Mixte | 20 % | Note ≤ 1 |
| C4 | Accessibilité du canal d'acquisition | Qualitatif | 15 % | — (faible accessibilité ralentit) |
| **C5** | Différenciation Hub v2 défendable | Qualitatif | **20 %** | Note ≤ 1 |
| C6 | Alignement vision Cavalli | Qualitatif | 5 % | Note = 0 |

**Échelles de notation** : 0-5 par critère, justification documentée pour chaque score.

**Note finale persona** = Σ (note critère × pondération), arrondie à 0,01 près.

**Seuils de priorisation validés Cavalli** :
- Note ≥ 4,0 → top tier (prioritaire de premier rang)
- Note 3,0-3,9 → watching (prioritaire de second rang)
- Note 2,0-2,9 → à surveiller, non prioritaire
- Note < 2,0 → écarté
- **Règle de bloquant** : un seul critère C1/C2/C3/C5 noté ≤ 1 → exclusion, même si moyenne pondérée correcte

**Plafond personas retenus en sortie** : 4-5 personas top tier (arbitrage Cavalli 3 du 26 mai).

---

## 5. Application complète — 14 profils scorés

Six profils ont été scorés en test pilote (cf. `travail/personas/test-pilote-priorisation-v0.md`). Application complétée ici sur les 9 profils non testés (A2, A3, B2, B3, B4, C2 persona, C3 persona, C4 persona, D2 persona).

### 5.1 Famille A — Dirigeants généralistes (vue stratégique)

#### A1 — Fondateur PME structurée (50-250 sal.) — pilote
| Critère | Note | Justification synthétique |
|---|---|---|
| C1 Population | 4 | ~40 000 PME structurées 50-250 sal. ; fondateur dirigeant dans ~100 % |
| C2 Pain | 3 | Pain D fort (sujet sur son bureau) mais U + R modérés |
| C3 DàP | 3 | Budget pro mais arbitrage serré |
| C4 Canal | 5 | Écosystème QFC élargi très fort sur ce profil |
| C5 Différenciation | 3 | Concurrence Bpifrance + cabinets émergents accessibles |
| C6 Alignement | 5 | Persona vision Hub v2 |
| **Note finale** | **3,55** | Watching |

#### A2 — DG ETI consolidé (250-4999 sal.)
| Critère | Note | Justification synthétique |
|---|---|---|
| C1 Population | 1 | ~6 000 DG ETI France (1 par ETI) |
| C2 Pain | 3 | Pain transformation stratégique mais consomme déjà HBR / cabinets / formations exec |
| C3 DàP | 5 | Budget IA large, 29 € trivial |
| C4 Canal | 2 | Hors écosystème Cavalli direct ; accessible via événements premium (Forum Économique, France Industrie, AFEP) ou cabinets prescripteurs |
| C5 Différenciation | 2 | Concurrence frontale HBR Executive (~58 $) + cabinets BCG/X + formations HEC. Hub v2 à 29 € peut sembler bas de gamme pour ce profil |
| C6 Alignement | 3 | Niveau au-dessus de la cible originelle, mais cohérent |
| **Note finale** | **2,75** | À surveiller |

#### A3 — Cadre dirigeant filiale française d'ETI internationale
| Critère | Note | Justification synthétique |
|---|---|---|
| C1 Population | 1 | ~3 000 filiales françaises d'ETI internationales |
| C2 Pain | 3 | Sujet IA souvent dicté par le groupe, à arbitrer localement |
| C3 DàP | 4 | Budget pro acquis (cascade groupe) |
| C4 Canal | 2 | Difficile via QFC, accessible LinkedIn |
| C5 Différenciation | 2 | Concurrence cabinets internationaux + formations HEC/Cambridge qui maîtrisent l'angle filiale |
| C6 Alignement | 3 | Aligné partiel |
| **Note finale** | **2,55** | À surveiller (peu pertinent) |

### 5.2 Famille B — Opérationnels-transverses (vue exécution)

#### B1 — COO ETI industrielle (Camille type) — pilote
| Critère | Note | Justification synthétique |
|---|---|---|
| C1 Population | 1 | ~3 000 COO ETI industrielles (50 % du total ETI) |
| C2 Pain | 5 | Pain DUR explicite — transformation process indus + pression compétitive + reconnu par baromètres |
| C3 DàP | 5 | Budget pro acquis, 29 € sous le seuil d'arbitrage |
| C4 Canal | 3 | Accessible QFC élargi + LinkedIn + CCI / France Industrie |
| C5 Différenciation | 4 | Concurrence frontale IA Booster + Mistral, mais 3 angles défendables |
| C6 Alignement | 5 | Persona exact vision Hub v2 |
| **Note finale** | **3,90** | Top tier |

#### B2 — COO ETI services / tertiaire (100-1000 sal.)
| Critère | Note | Justification synthétique |
|---|---|---|
| C1 Population | 1 | ~3 000 COO ETI services (50 % du total ETI) |
| C2 Pain | 5 | Pain DUR fort sur productivité knowledge workers + GenAI transforme tertiaire BtoB |
| C3 DàP | 5 | Budget pro acquis, 29 € trivial |
| C4 Canal | 3 | QFC élargi + CCI services + French Tech (services BtoB représente une part importante des startups incubées) |
| C5 Différenciation | 4 | Similaire B1, défendable |
| C6 Alignement | 5 | Persona vision Hub v2 (élargissement secteur) |
| **Note finale** | **3,90** | Top tier (ex aequo B1) |

#### B3 — Directeur des opérations PME (50-250 sal.)
| Critère | Note | Justification synthétique |
|---|---|---|
| C1 Population | 2 | ~10 000 Dir Ops dans PME 50-250 (présent ~30 %) |
| C2 Pain | 3 | Sujet IA tactique (outils concrets équipes), pas vue stratégique |
| C3 DàP | 3 | Budget pro moyen, 29 € passe sur ligne SaaS |
| C4 Canal | 4 | Écosystème QFC élargi + CCI |
| C5 Différenciation | 3 | Concurrence cabinets émergents + Bpifrance + Mistral |
| C6 Alignement | 4 | Cohérent vision mais profil tactique |
| **Note finale** | **3,05** | Watching marginal |

#### B4 — Directeur / Chief Transformation Officer (CTO/CDO Transfo)
| Critère | Note | Justification synthétique |
|---|---|---|
| C1 Population | 1 | ~5 000 rôles dédiés transfo ETI 250-4999 + grandes PME |
| C2 Pain | 5 | Pain DUR très fort — mandat explicite transfo IA, U+D+R explicites |
| C3 DàP | 5 | Budget large, IA = sa ligne directe |
| C4 Canal | 3 | Communautés CIO Forum, CDO Days, French Tech, événements transfo |
| C5 Différenciation | 4 | Concurrence cabinets transfo (Capgemini Invent, Wavestone, Onepoint, Numa) + médias spécialisés ; différenciation curated + outils + ton défendable |
| C6 Alignement | 4 | Très aligné — profil cœur vision (Faisabilité) |
| **Note finale** | **3,85** | Top tier |

### 5.3 Famille C — Fonctionnels (vue métier)

#### C1 (persona) — DAF PME-ETI — pilote
| Critère | Note | Justification synthétique |
|---|---|---|
| C1 Population | 3 | ~59 000 DAF en PME-ETI |
| C2 Pain | 3 | Pain mixte — D moyen, U faible, R sceptique tant que ROI |
| C3 DàP | 4 | Budget pro maîtrisé, ligne IA en gestation |
| C4 Canal | 2 | DAF peu présent dans écosystème Cavalli ; réseau DFCG accessible mais effort significatif |
| C5 Différenciation | 2 | Concurrence outils SaaS DAF intégrant IA (Pennylane, Indy) + cabinets finance |
| C6 Alignement | 3 | DAF = fonctionnel pas transverse |
| **Note finale** | **2,85** | À surveiller |

#### C2 — DRH PME-ETI
| Critère | Note | Justification synthétique |
|---|---|---|
| C1 Population | 3 | ~25 000 DRH PME-ETI |
| C2 Pain | 3 | Pain moyen — pression mais pas immédiate, sujet souvent au DSI ou DG |
| C3 DàP | 3 | Budget HR plus serré que budget transfo |
| C4 Canal | 3 | ANDRH, HRTech, LinkedIn |
| C5 Différenciation | 2 | Concurrence outils HR SaaS qui intègrent IA (Workday, Lucca, Eurécia, Welcome to the Jungle) + cabinets spécialisés |
| C6 Alignement | 3 | DRH = fonctionnel |
| **Note finale** | **2,80** | À surveiller |

#### C3 — Directeur marketing / communication PME-ETI
| Critère | Note | Justification synthétique |
|---|---|---|
| C1 Population | 3 | ~30 000 |
| C2 Pain | 4 | Déjà utilisateur IA (ChatGPT/Mistral pour contenu) + pression compétitive |
| C3 DàP | 4 | Budget marketing pro + abonnements SaaS marketing déjà acquis |
| C4 Canal | 3 | B2B Marketing France, Adetem, HubSpot communautés |
| **C5 Différenciation** | **1** | **Concurrence FRONTALE outils marketing IA spécialisés** : Jasper, Copy.ai, Joggle AI £24/mois UK, agences IA marketing → différenciation Hub v2 introuvable sur ce profil |
| C6 Alignement | 3 | Aligné partiel |
| **Note finale** | **3,05 mais BLOQUANT C5** | **ÉCARTÉ par règle de bloquant** |

#### C4 — Directeur commercial PME-ETI
| Critère | Note | Justification synthétique |
|---|---|---|
| C1 Population | 3 | ~30 000 |
| C2 Pain | 3 | IA vente émergente mais pas critique, sujet souvent CRM/sales ops |
| C3 DàP | 3 | Budget commercial pro + outils SaaS déjà acquis |
| C4 Canal | 3 | Sales Hacking, communautés commerciales |
| C5 Différenciation | 2 | Concurrence outils sales AI (Gong, Modjo, MeetRecord, Salesforce Einstein) |
| C6 Alignement | 3 | Aligné partiel |
| **Note finale** | **2,80** | À surveiller |

#### C5 (persona) — Responsable innovation / R&D — pilote
| Critère | Note | Justification synthétique |
|---|---|---|
| C1 Population | 2 | ~7 000 responsables innovation/R&D dédiés |
| C2 Pain | 4 | Prescripteur d'outils, pression compétitive innovation |
| C3 DàP | 4 | Budget innovation pro autonome |
| C4 Canal | 4 | Hub Bpifrance Innovation, RETIS, French Tech, écosystème QFC |
| C5 Différenciation | 4 | Concurrence veilles spécialisées + agences innovation ; défendable |
| C6 Alignement | 3 | Aligné partiel — dirigeant fonctionnel |
| **Note finale** | **3,65** | Top tier (rang 5) |

### 5.4 Famille D — Techniques accidentels et gardes-fous

#### D1 — DSI accidentel PME — pilote
| Critère | Note | Justification synthétique |
|---|---|---|
| C1 Population | 2 | ~10 000 DSI PME 50-250 dont sous-segment "accidentel" |
| C2 Pain | 5 | Pain DUR explicite — gouvernance IA sans expertise initiale ; témoignages multiples Reddit / forums |
| C3 DàP | 3 | Budget IT/IA souvent serré PME ; validation parfois supérieure |
| C4 Canal | 3 | CTO France, sysadmin, communautés Slack tech FR |
| C5 Différenciation | 4 | Aucun produit dédié "gouvernance IA pour DSI non-experts IA" identifié |
| C6 Alignement | 2 | Profil technique-accidentel, périphérie cible vision |
| **Note finale** | **3,50** | Watching |

#### D2 — Responsable juridique / DPO PME-ETI
| Critère | Note | Justification synthétique |
|---|---|---|
| C1 Population | 2 | ~15 000 DPO + juridiques PME-ETI |
| C2 Pain | 5 | Pain DUR très fort — AI Act entre en vigueur 2 août 2026, RGPD à appliquer aux outils IA, IP utilisateurs à arbitrer |
| C3 DàP | 5 | Budget juridique disponible, 29 € insignifiant |
| C4 Canal | 3 | AFCDP, CNCC, événements RGPD/IA |
| C5 Différenciation | 2 | Concurrence forte — Leto, Privacy by Design, Dastra (SaaS RGPD/DPO) + cabinets avocats numériques |
| C6 Alignement | 2 | Profil très technique, pas dirigeant transverse |
| **Note finale** | **3,50** | Watching (alignement vision faible) |

### 5.5 Famille E — Porteur indirect

#### E1 — Consultant indépendant senior IA — pilote
| Critère | Note | Justification synthétique |
|---|---|---|
| C1 Population | 3 | ~15 000 consultants IA/transfo (Malt 7 292 + hors plateforme estimé équivalent) |
| C2 Pain | 4 | Pain pression pertinence permanente (cabinet) + croissance GenAI +300 % depuis 2022 sur Malt |
| C3 DàP | 5 | Trésorerie pro trivial vs revenu jour 1 000 €+ ; comportement freelance teste/adopte rapidement |
| C4 Canal | 4 | LinkedIn très actif + Malt filtre IA + communautés Slack/Discord IA France + podcasts métier |
| C5 Différenciation | 5 | **Aucun produit identifié spécifiquement positionné « hub savoir IA curated pour consultants indépendants »** — position pionnière |
| C6 Alignement | 3 | Aligné partiel — pas cible originelle vision mais arbitrage Cavalli 1 du 26 mai inclut comme double registre |
| **Note finale** | **4,15** | **Top tier rang 1** |

---

## 6. Consolidation top 5 — synthèse priorisation

### 6.1 Tableau récapitulatif des 14 profils

| Rang | Code | Persona | Note | Verdict |
|------|------|---------|------|---------|
| **1** | E1 | Consultant indé. senior IA | **4,15** | **Top tier #1** |
| **2** | B1 | COO ETI industrielle (Camille type) | **3,90** | **Top tier #2** (ex aequo B2) |
| **2** | B2 | COO ETI services / tertiaire | **3,90** | **Top tier #2** (ex aequo B1) |
| **4** | B4 | Directeur / Chief Transformation Officer | **3,85** | **Top tier #4** |
| **5** | C5 (persona) | Responsable innovation / R&D | **3,65** | **Top tier #5** |
| 6 | A1 | Fondateur PME structurée | 3,55 | Watching |
| 7 | D1 | DSI accidentel PME | 3,50 | Watching |
| 7 | D2 | DPO/juridique PME-ETI | 3,50 | Watching (alignement faible) |
| 9 | B3 | Directeur des opérations PME | 3,05 | Watching marginal |
| 10 | C1 (persona) | DAF PME-ETI | 2,85 | À surveiller |
| 11 | C2 | DRH PME-ETI | 2,80 | À surveiller |
| 11 | C4 | Directeur commercial PME-ETI | 2,80 | À surveiller |
| 13 | A2 | DG ETI consolidé | 2,75 | À surveiller |
| 14 | A3 | Cadre dirigeant filiale ETI internationale | 2,55 | À surveiller |
| **Écarté** | **C3** | **Directeur marketing PME-ETI** | 3,05 mais **C5 = 1** | **Écarté par règle de bloquant** |

### 6.2 Le top 5 — profil mixte cohérent

Le top 5 personas prioritaires couvre quatre angles complémentaires :

- **1 cible directe rentable + canal d'amplification** (E1 consultant) — utilisateur direct + vecteur de prescription vers les autres personas
- **2 personas opérationnels-transverses ETI** (B1 industrie + B2 services) — couvre les deux principaux secteurs où le Pain DUR est documenté
- **1 persona instigateur de transformation** (B4 CTO/CDO) — rôle dédié transfo, mandat explicite IA
- **1 persona prescripteur fonctionnel** (C5 responsable innovation) — détecteur d'outils + amplification interne

Cette diversité est **stratégiquement saine** : Hub v2 ne se rend pas dépendant d'un seul canal d'acquisition ni d'un seul angle de proposition de valeur.

### 6.3 Le persona écarté — C3 Marketing

Le directeur marketing PME-ETI est écarté **non par manque de Pain ou de DàP** (3,05 note finale correcte) mais par **différenciation impossible à défendre** (C5 = 1). La concurrence frontale Jasper / Copy.ai / Joggle AI / agences IA marketing rend Hub v2 inadéquat pour ce profil — il faudrait un module marketing IA dédié, ce qui n'est pas le positionnement Hub v2.

**Cas d'école méthodologique** : la règle de bloquant a effectivement protégé contre une priorisation par moyenne trompeuse. Validation rétrospective de la grille.

---

## 7. Observations structurelles

### 7.1 Le Pain (C2) est le critère le plus discriminant

Sur le top 5 personas, **les 4 premiers ont C2 ≥ 4** (E1 = 4, B1 = 5, B2 = 5, B4 = 5, C5 = 4). À l'inverse, sur les 4 derniers (notes < 2,9), **3 ont C2 = 3** (A2, A3, C2 DRH, C4 commercial) — Pain mais pas DUR.

**Implication produit** : Hub v2 doit prioritairement adresser des profils où le Pain est **documenté comme DUR** (Douloureux + Urgent + Reconnu), pas juste « pertinent ». La communication produit + acquisition doit s'appuyer sur ces signaux DUR.

### 7.2 La disposition à payer (C3) n'est pas un frein sur le top tier

Sur le top 5, **C3 ≥ 4 sur tous** (E1=5, B1=5, B2=5, B4=5, C5=4). Hub v2 à 29 €/mois est compatible avec leur capacité d'achat. Le pricing n'est pas le frein principal — **la valeur perçue l'est**.

### 7.3 La différenciation (C5) bloque certains profils par concurrence frontale

C3 marketing écarté ; C2 DRH / C4 commercial / D2 DPO ont des notes C5 = 2 (concurrence forte outils spécialisés). **Pattern observable** : sur les profils fonctionnels avec une couche métier dédiée (HR, sales, finance, juridique), des outils SaaS IA spécialisés existent et fragilisent la différenciation Hub v2. **Implication** : Hub v2 doit éviter de se positionner sur du fonctionnel spécialisé tant que la matière éditoriale n'est pas profondément verticalisée.

### 7.4 La taille de population (C1) restreint les personas ETI

B1, B2, B4 ont tous C1 = 1 (population ~3 000-6 000). Mais leurs autres scores compensent largement. **Implication** : la pondération C1 à 15 % est bien calibrée — elle limite mais n'écrase pas un persona avec un Pain DUR fort et une DàP solide.

### 7.5 Signal sectoriel — double vertical industrie + services

B1 (industrie) + B2 (services) émergent **ex aequo à 3,90**. Cela ré-ouvre l'arbitrage Cavalli 2 (approche transverse) :

- **Option transverse** : la matière éditoriale Hub v2 cible « le COO ETI » sans distinction sectorielle
- **Option double vertical** : la matière éditoriale propose des modules sectorialisés (« COO industrie » + « COO services BtoB »), avec parcours différenciés

🟧 **Point d'arbitrage Cavalli réouvert** — question 16 du CR S3.1 (focus sectoriel). Recommandation Hub Strat : **double vertical industrie + services** plutôt qu'option transverse, justifiée par la convergence des signaux documentaires sur ces deux secteurs ; la verticalisation fine arrive en S3.7 (cartographie concurrentielle v2) ou plus tard si signal renforcé.

---

## 8. Inflexions méthodologiques actées

Sur la base du test pilote (cf. `test-pilote-priorisation-v0.md` §5) + application complète, trois inflexions intégrées dans ce protocole v1 :

### 8.1 Colonne « niveau de confiance C1 »

Sans LinkedIn Sales Nav (arbitrage Cavalli 8), les estimations C1 sont à ±30 % d'incertitude. Le protocole v1 intègre cette incertitude en marquant explicitement les scores C1 sur les profils retenus prioritaires (B1, B2, B4 = niveau de confiance moyen — ratios fonctionnels Hub Strat ; E1 = niveau de confiance élevé — données Malt directes ; C5 = niveau de confiance faible — ratio R&D dédié estimé).

### 8.2 Score C5 marqué « provisoire » jusqu'à clôture cartographie concurrentielle v1

La cartographie concurrentielle Hub v2 v1 (S3.3, livrée 26 mai) est désormais close. Donc les scores C5 du protocole v1 sont **définitifs** (plus de « provisoire »). Une réitération sera possible à la cartographie v2 (S3.7) si l'univers concurrentiel évolue significativement.

### 8.3 Échelle C6 maintenue 0-5 avec note explicative

C6 prend en pratique les valeurs 2, 3, 4, 5 (pas 0 ni 1 sur les 14 profils — aucun n'est en rupture explicite avec la vision). Le protocole v1 documente que C6 joue surtout comme **filtre binaire** (note 0 = exclusion) et marginalement comme différenciateur granulaire. Pondération maintenue à 5 %.

---

## 9. Articulation avec la cartographie concurrentielle v1

Le top 5 personas peut être croisé avec l'intensité concurrentielle par catégorie (cf. cartographie concurrentielle v1 §10) :

| Persona | Concurrence dominante | Différenciation Hub v2 | Risque |
|---------|-----------------------|--------------------------|--------|
| E1 Consultant indé. | Newsletters premium (AI Weekly for Leaders, etc.), communautés payantes | **Forte** (pas de produit dédié hub savoir IA consultants) | Faible |
| B1 COO ETI industrie | IA Booster + Mistral Le Chat + cabinets émergents | Moyenne (curation + persona-spécificité) | Moyen (concurrence intense) |
| B2 COO ETI services | Idem B1 + outils sectoriels services (Notion AI, etc.) | Moyenne (curation + persona-spécificité) | Moyen |
| B4 CTO/CDO Transfo | Cabinets transfo (Capgemini Invent, Wavestone) + médias spécialisés | **Forte** (combinaison conversationnel + outils Pro) | Faible |
| C5 Responsable innovation | Veilles spécialisées + agences innovation | **Forte** (curated + outils actionnables intégrés) | Faible |

**Pattern** : E1, B4, C5 ont une **différenciation forte** ; B1 et B2 ont une **différenciation moyenne** sous forte concurrence. Implication produit : Hub v2 doit redoubler d'attention sur B1/B2 (cœur historique vision) en démontrant explicitement la valeur ajoutée vs Bpifrance Université + Mistral Le Chat.

---

## 10. Préconisations pour les sprints suivants

### 10.1 S3.5 — Modélisation économique (préconisations)

Chiffrer les **5 segments du top tier** avec hypothèses différenciées par persona :

| Persona | Taille marché accessible (3 ans) | Conversion Free → Pro espérée | Ticket Pro |
|---------|----------------------------------|---------------------------------|--------------|
| E1 Consultant indé. | ~15 000 → 2-5 % accessibles ~300-750 | Élevée (5-8 %) — réactivité freelance | 29 €/mois individuel |
| B1 COO ETI industrie | ~3 000 → 5-10 % ~150-300 | Moyenne (3-5 %) — cycle B2B | 29 € individuel ou tier Équipe |
| B2 COO ETI services | ~3 000 → 5-10 % ~150-300 | Moyenne (3-5 %) — cycle B2B | 29 € individuel ou tier Équipe |
| B4 CTO/CDO Transfo | ~5 000 → 5-10 % ~250-500 | Moyenne-haute (4-6 %) — mandat dédié | 29 € individuel + tier Équipe potentiel |
| C5 Responsable innovation | ~7 000 → 3-6 % ~210-420 | Moyenne (3-5 %) | 29 € individuel |

Hypothèses à challenger en S3.5. **Volume cumulé top 5 (3 ans, conversion 3-5 %)** : ~1 100-2 300 abonnés Pro. ARR cible si stabilisation 2 ans = 380 k€-800 k€. À chiffrer en scenarios pessimiste / médian / optimiste.

### 10.2 S3.6 — Plan d'acquisition 10 premiers utilisateurs (préconisations)

Cible Étape 1-2 (POC RAG juin + MVP onboarding fin juin) : recruter **10 premiers utilisateurs early adopters**. Recommandation profil mixte :

| Profil | # cibles initiales | Canal d'acquisition primaire | Cycle |
|--------|---------------------|------------------------------|-------|
| E1 Consultant indé. | 4-5 | LinkedIn direct (1er degré Cavalli) + Malt featured + post LinkedIn ciblé | 2-4 semaines |
| B1 COO ETI industrie | 1-2 | QFC réseau ETI industrielles vosgiennes + CCI Vosges + France Industrie Lorraine | 4-8 semaines |
| B2 COO ETI services | 1-2 | QFC alumni services BtoB + French Tech Est | 4-8 semaines |
| B4 CTO/CDO Transfo | 1-2 | LinkedIn ciblé + communauté CDO Days FR | 4-8 semaines |
| C5 Responsable innovation | 1-2 | RETIS / Hub Bpifrance Innovation + QFC réseau | 4-8 semaines |

E1 est le segment d'amorçage le plus rapide (conversion espérée 2-4 semaines vs 4-8 pour B1/B2/B4/C5). Cohérent avec la priorisation top tier #1.

### 10.3 S3.7 — Itération produit (préconisations)

Différenciation matière éditoriale par persona prioritaire :

- **E1** : profondeur veille IA + outils Pro (générateur cadrage, comparateur multicritères pour ses missions client)
- **B1/B2** : cadrage stratégique + accompagnement décision + cas sectoriels industrie/services
- **B4** : feuilles de route transfo IA + outils Pro de pilotage (jalons, KPI)
- **C5** : veille technologique + identification signaux faibles + outils benchmark

À transmettre via Cavalli au canal Hub Content pour réflexion sur l'organisation de la matière éditoriale Hub v2 (modules sectoriels ? modules persona-spécifiques ?).

---

## 11. Carnet de questions Cavalli ouvertes

Questions résiduelles à arbitrer pour la suite :

18. **Double vertical industrie + services** (réouverture point 2) : OK pour Hub Strat de structurer la matière selon ces deux secteurs principaux + transverse, ou maintien strictement transverse en première phase ?
19. **Verticalisation matière éditoriale par persona** (préconisation §10.3) : à transmettre à Hub Content en notification croisée, ou maintenir transmissions différées jusqu'à validation Cavalli ?
20. **B2 ex aequo B1** : OK pour les traiter sur pied d'égalité dans S3.5 et S3.6 ?
21. **D1 DSI accidentel (watching, 3,50) et D2 DPO juridique (watching, 3,50)** : maintenus en watching ou opportunités de modules fonctionnels dédiés à explorer dans la roadmap ?

---

## 12. Bloc résumé exécutif transmissible (auto-imposé §8.1.7)

> **À copier-coller pour notification autonome aux canaux pairs.**
>
> ---
>
> **Protocole personas Hub v2 v1 — 26 mai 2026 — synthèse**
>
> Application complète de la grille des 6 critères de priorisation (validée Cavalli arbitrages 4-7 du 26 mai) aux **14 profils** de l'espace persona Hub v2. **5 personas prioritaires (top tier)** émergent :
>
> 1. **E1 Consultant indépendant senior IA** — 4,15 (cible directe + canal d'évangélisation)
> 2. **B1 COO ETI industrielle (Camille)** — 3,90
> 3. **B2 COO ETI services / tertiaire** — 3,90 (ex aequo B1)
> 4. **B4 Directeur / Chief Transformation Officer** — 3,85
> 5. **C5 Responsable innovation / R&D** — 3,65
>
> **1 persona écarté par règle de bloquant** : C3 Directeur marketing (concurrence frontale Jasper / Copy.ai / Joggle / agences IA marketing — C5 différenciation = 1). 8 personas en watching (rangs 6-13), 1 hors priorité (rang 14).
>
> **3 observations structurelles** : (1) le Pain DUR est le critère le plus discriminant ; (2) le pricing 29 € n'est pas le frein sur le top tier ; (3) les profils fonctionnels avec couche métier dédiée (HR, sales, finance) ont une différenciation Hub v2 plus difficile à défendre face aux SaaS spécialisés.
>
> **Signal sectoriel** : B1 industrie et B2 services émergent ex aequo → recommandation **double vertical industrie + services** plutôt qu'approche purement transverse (réouverture arbitrage Cavalli 2 du 26 mai).
>
> **Préconisations sprints suivants** : S3.5 modélisation économique sur 5 segments (volume ARR cible ~380 k€-800 k€ sur 3 ans) / S3.6 plan acquisition 10 premiers users (4-5 E1 amorçage rapide + 1-2 par autre persona top tier) / S3.7 itération produit (différenciation matière éditoriale par persona).
>
> Source complète : `Canaux/Hub-Strat/outputs/protocole-cartographie-priorisation-personas-hub-v2-v1.md`

---

## 13. Check pré-livrable §8.1 — application

1. **Étanchéité QFC** ✅ — aucune startup réelle accompagnée nommée, méthodologie publique uniquement.
2. **Modules Vianeo cohérents** ✅ — module 2 Désirabilité (cœur) + ouvertures transverse acceptabilité / faisabilité. Respect règle 3 v1.1 (grille parallèle itérée).
3. **Sources citées et vérifiables** ✅ — INSEE, Apec, Malt, Comet, cartographie concurrentielle v1 internes ; sources externes hyperlinkées §15.
4. **Pas de substitution Cavalli** ✅ — 4 nouvelles questions à arbitrer §11, jalons d'arbitrage Cavalli identifiés, posture règle des 5 doigts respectée.
5. **Impacts autres canaux signalés** ✅ — Hub Content (verticalisation matière éditoriale §10.3), Claude Design (parcours différenciés par persona prioritaire), DEV IA Head (résolution P15 et patterns de priorisation transverses).
6. **Versioning explicite** ✅ — v1 + historique §16.
7. **(Auto-imposé) Bloc résumé exécutif transmissible** ✅ — §12.

---

## 14. Zones à creuser (itération v1.1 ou v2)

- **Confiance C1** : objectivation des ratios fonctionnels Hub Strat par croisement INSEE × Apec × études sectorielles si décision d'aller plus loin sur un persona top tier
- **Bascule interviews légères** sur 1-2 personas top tier (E1 + B1 ou E1 + B4) si signaux documentaires divergents — point d'arbitrage fin S3.4 / 19 juin
- **Itération post-Étape 1 POC RAG** (sem 1-2 juin) : remontée des premiers feedbacks utilisateurs réels → réajustement priorisation
- **Réitération grille avec cartographie concurrentielle v2** (S3.7 / 6-10 juillet) si l'univers concurrentiel évolue significativement
- **Veille E1 spécifique** : si une plateforme se positionne « hub savoir IA pour consultants indé. », réévaluation urgente C5 sur E1

---

## 15. Sources mobilisées

### Sources quantitatives volet C1
- [INSEE — Tissu productif par catégorie d'entreprises 2023](https://www.insee.fr/fr/statistiques/8675639)
- [INSEE — L'essentiel sur les entreprises](https://www.insee.fr/fr/statistiques/5424748)
- [Haut-commissariat stratégie et plan — ETI fer de lance](https://www.strategie-plan.gouv.fr/publications/les-eti-fer-de-lance-de-leconomie-francaise)
- [Apec — Fiches métier cadres dirigeants](https://www.apec.fr/tous-nos-metiers.html?t=all)
- [Malt — Freelances IA](https://www.malt.fr/s/tags/intelligence-artificielle-602fdd438754972435c21501)
- [Comet — Réseau 120 k consultants tech](https://www.welcometothejungle.com/fr/companies/comet/team)

### Sources qualitatives volet C2 / C3 / C4 / C5
- [France Num — Baromètre 2025 numérique IA TPE PME](https://www.francenum.gouv.fr/guides-et-conseils/strategie-numerique/comprendre-le-numerique/barometre-france-num-2025-le)
- [BCG — Nordic AI Inflection Point](https://www.bcg.com/publications/2026/nordic-ai-value-creation-or-bubble) (proxy adoption EU SME)
- [EY — How Nordic leaders can drive responsible AI](https://www.ey.com/en_fi/insights/ai/how-nordic-leaders-can-drive-responsible-ai)
- [Cartographie concurrentielle Hub v2 v1](../outputs/cartographie-concurrentielle-hub-v2-v1.md) (interne canal)

### Documents internes mobilisés
- `Canaux/Hub-Strat/_instructions.md` v1.1
- `Canaux/Hub-Strat/outputs/note-cadrage-hub-strat-v1.md`
- `Canaux/Hub-Strat/travail/personas/scoping-espace-persona-v0.md`
- `Canaux/Hub-Strat/travail/personas/preparation-protocole-s32-v0.md`
- `Canaux/Hub-Strat/travail/personas/test-pilote-priorisation-v0.md`
- `Canaux/Hub-Strat/outputs/cartographie-concurrentielle-hub-v2-v1.md`
- `Canaux/Hub-IA/outputs/VISION-HUB-V2-CONSOLIDEE-v1.md`

---

## 16. Historique de versions

| Date | Version | Modification |
|------|---------|--------------|
| 26 mai 2026 | v1 | Création initiale — protocole opérationnel + application complète aux 14 profils + top 5 personas consolidé (E1, B1, B2, B4, C5) + 1 persona écarté par règle de bloquant (C3 Marketing). Inflexions méthodologiques actées (confiance C1, C5 définitif, C6 maintenu 0-5). Signal sectoriel double vertical industrie + services émergent. Préconisations sprints S3.5-S3.6-S3.7. 4 nouvelles questions Cavalli ouvertes (réouverture point 2 sectoriel + 3 nouveaux). Dépôt anticipé sur jalon vendredi 5 juin (S3.2). |

---

*Livrable structurant Hub Strat — version v1, validation Cavalli attendue. Application complète de la grille validée. Check pré-livrable §8.1 appliqué — sept points OK.*
