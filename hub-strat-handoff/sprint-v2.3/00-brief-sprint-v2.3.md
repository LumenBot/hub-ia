# Brief Claude Design — Sprint v2.3 (officiel — arbitrages Cavalli intégrés)

**Version** : officielle — 27 mai 2026
**Statut** : sprint v2.3 ouvert
**Émetteur** : Cowork Hub Strat (sur la base des arbitrages Cavalli du 27 mai 2026)
**Destinataire** : Claude Design
**Transmission** : via Cavalli + push repo `LumenBot/hub-ia` dans `hub-strat-handoff/sprint-v2.3/`
**Périmètre** : mise en forme professionnelle des livrables stratégiques Hub Strat + déclinaison commerciale (one-pager prospect, brochure partenaires, deck de vente, templates email, landing soft launch)
**Cadence cible** : 3 packs livrés sur 3-4 semaines (juin 2026) — calendrier indicatif, vélocité observée habituellement plus rapide

---

## 0. Ouverture du sprint et matériau préalable

Cavalli a validé les 6 points d'alignement structurants (§1). Le sprint v2.3 est ouvert sur la base de cette validation.

**Matériau Hub Strat accessible dans ce dossier de handoff** (`hub-strat-handoff/sprint-v2.3/` du repo `LumenBot/hub-ia`) :

| Document | Apport pour sprint v2.3 | Chemin |
|----------|---------------------------|---------|
| Note de cadrage Hub Strat v1 | Cadre méthodologique + 5 hypothèses marché | [`01-livrables-hub-strat/note-cadrage-hub-strat-v1.md`](./01-livrables-hub-strat/note-cadrage-hub-strat-v1.md) |
| Protocole personas v1 | Top 5 personas avec notes (référence narratif) | [`01-livrables-hub-strat/protocole-cartographie-priorisation-personas-hub-v2-v1.md`](./01-livrables-hub-strat/protocole-cartographie-priorisation-personas-hub-v2-v1.md) |
| Cartographie concurrentielle v1 | 31 acteurs, carte positionnement, 3 différenciateurs défendables | [`01-livrables-hub-strat/cartographie-concurrentielle-hub-v2-v1.md`](./01-livrables-hub-strat/cartographie-concurrentielle-hub-v2-v1.md) |
| VPM v2 | Value Proposition Map par persona top 5 | [`01-livrables-hub-strat/vpm-cartographie-concurrentielle-v2.md`](./01-livrables-hub-strat/vpm-cartographie-concurrentielle-v2.md) |
| Garde-fous juridiques v1 | RGPD, AI Act, CGV/CGU, IP, statut side project | [`01-livrables-hub-strat/garde-fous-juridiques-hub-v2-v1.md`](./01-livrables-hub-strat/garde-fous-juridiques-hub-v2-v1.md) |
| Modélisation économique v1 | CAC / LTV / churn + 3 scenarios | [`01-livrables-hub-strat/modelisation-economique-hub-v2-v1.md`](./01-livrables-hub-strat/modelisation-economique-hub-v2-v1.md) |
| Prévisionnel financier xlsx | P&L mensuel 36 mois (visuels à reprendre) | [`01-livrables-hub-strat/previsionnel-financier-hub-v2-v1.xlsx`](./01-livrables-hub-strat/previsionnel-financier-hub-v2-v1.xlsx) |
| Plan acquisition 10 premiers users v1 | Canaux acquisition par persona + funnel | [`01-livrables-hub-strat/plan-acquisition-10-premiers-utilisateurs-hub-v2-v1.md`](./01-livrables-hub-strat/plan-acquisition-10-premiers-utilisateurs-hub-v2-v1.md) |
| Statut juridique (résumé public) | Statut side project + variantes audiences | [`01-livrables-hub-strat/statut-juridique-cavalli-vs-qfc-resume-public.md`](./01-livrables-hub-strat/statut-juridique-cavalli-vs-qfc-resume-public.md) |
| Roadmap v1 | 5 étapes × 6 dimensions + 3 jalons structurants | [`01-livrables-hub-strat/roadmap-hub-v2-v1.md`](./01-livrables-hub-strat/roadmap-hub-v2-v1.md) |
| Business plan v1 | Texte source du pack F | [`01-livrables-hub-strat/business-plan-hub-v2-v1.md`](./01-livrables-hub-strat/business-plan-hub-v2-v1.md) |
| Pitch deck v1 | Structure source du pack G (à habiller) | [`01-livrables-hub-strat/pitch-deck-hub-v2-v1.pptx`](./01-livrables-hub-strat/pitch-deck-hub-v2-v1.pptx) |
| Instructions Hub Strat v1.1 | Règle parallèle itérée + 4 règles cohérence inter-modules | [`02-references-internes/_instructions-hub-strat-v1.1.md`](./02-references-internes/_instructions-hub-strat-v1.1.md) |
| Cartographie orchestration v1.0 | 10 acteurs Cowork (pour slide équipe pack G) | [`02-references-internes/cartographie-orchestration-v1.0.md`](./02-references-internes/cartographie-orchestration-v1.0.md) |

⚠️ **Dossier d'arbitrage IP complet** non publié dans ce handoff (confidentiel — conservé en interne Hub Strat). Remplacé par le **résumé public** [`statut-juridique-cavalli-vs-qfc-resume-public.md`](./01-livrables-hub-strat/statut-juridique-cavalli-vs-qfc-resume-public.md) qui contient le strict nécessaire pour produire les 2 variantes audiences des packs F et G.

**Matériau Claude Design à réutiliser directement** :
- Brand system v2.1 (palette Navy + Indigo, logo *Stratégie ● IA*, Geist + Newsreader + Geist Mono, voix *« en connaissance de cause »*)
- Tokens v2.2 (`handoff/css/tokens.css` canonique)
- Iconographie monoline pack (e) v2.2
- Prototype v2 (captures écran à intégrer comme proof-points)

---

## 1. Six décisions Cavalli intégrées

### 1.1 Naming produit
- **« Stratégie IA »** = naming commercial sur tous les livrables visibles externes (business plan transmis, pitch deck transmis, one-pager prospect, brochure partenaires, deck de vente, templates email, landing soft launch, logo)
- **« Hub v2 »** = nomenclature interne (référence Cowork + canaux pairs + documentation technique handoff Claude Code)
- Logo wordmark *Stratégie ● IA* avec point indigo (Direction B verrouillée v2.1) confirmé

### 1.2 Persona narratif — top 5 (et non Camille seule)
- **Évolution actée** : Camille reste un cas d'usage UX/UI illustratif (parcours onboarding du prototype), mais le **narratif commercial** mobilise les **5 personas top tier** (cf. protocole personas v1) :

| Code | Persona narratif | Pain DUR principal |
|------|------------------|-----------------------|
| E1 | Consultant indépendant senior IA (TJM 800-1 500 €) | Veille fraîche + outiller missions client sans dépendre d'OpenAI/Mistral génériques |
| B1 | COO ETI industrielle (Camille type) | Transformer les process industriels sous pression compétitive |
| B2 | COO ETI services / tertiaire | Cadrer GenAI productivité knowledge workers face à adoption désorganisée |
| B4 | Directeur / CTO/CDO Transformation | Mandat IA explicite — démontrer le ROI en COMEX |
| C5 | Responsable innovation / R&D | Anticiper les bons paris IA + concentrer la veille signaux faibles |

→ Implication pour les livrables commerciaux : **5 cas d'usage parallèles** racontés dans les supports (one-pager verso, brochure partenaires §2-3, deck de vente light), **5 templates email cold outreach** différenciés (pack H §4), **5 cohortes d'acquisition** indiquées dans le pitch deck.

### 1.3 Pricing UX — option C validée
- **Structure** : 3 colonnes côte à côte (Free / Pro 29 € / Équipe 19 €/siège) + **section crédits 10 € bienvenue déclinée en bas de page** (sans casser la hiérarchie « Pro = pivot commercial »)
- À appliquer dans : pitch deck (slide pricing), business plan (§5), one-pager prospect (recto), brochure partenaires, deck de vente, landing soft launch

### 1.4 Stack souveraine — variante A en MVP, migration variante B post-Étape 4
- **Étape 1 → Étape 4** (juin 2026 → janvier 2027) : **variante A — stack US (Vercel + Supabase EU regions) avec mentions RGPD renforcées**. Cohérence avec le sprint v2.2 pack (d) — vélocité MVP préservée.
- **Post-Étape 4** : possibilité de migration en variante B (Scaleway / OVH souverain) si le narratif souveraineté devient un levier commercial actif (cf. modélisation économique v1 §10.6 — pas de gain économique structurel).
- **Communication commerciale** : la souveraineté est traitée comme **condition implicite respectée** (badge subtle, mention footer, page « tes données » dédiée), **pas comme proposition de valeur primaire**. La proposition de valeur primaire reste les 3 différenciateurs (continuité conversationnelle + curation expert dirigeant + outils Pro actionnables).

### 1.5 Articulation des 9 hypothèses — page récap unifiée
- Une page de synthèse unifiée à créer dans la documentation commerciale interne (pack H, à positionner soit en page dédiée du business plan annexe, soit en document séparé selon ton choix de composition) :

| # | Hypothèse | Type | Porteur | Instrumentation | KPI cible |
|---|------------|------|----------|-------------------|-----------|
| H1 | Friction onboarding 5 questions ≤ 60 % d'abandon | Produit | Claude Design (pack b v2.2) | POC RAG Étape 1 + Langfuse | Completion > 60 % |
| H2 | Valeur perçue 29 €/mois justifiée | Produit | Claude Design (pack b v2.2) | POC RAG Étape 1 + observation 5-10 users | Disposition à payer documentée |
| H3 | Chat suggestions vs libre — comparaison | Produit | Claude Design (pack b v2.2) | POC RAG Étape 1 — A/B variants | Engagement chat > 3/sem |
| H4 | Citation source dépliable utilisée | Produit | Claude Design (pack b v2.2) | POC RAG Étape 1 — interaction tracking | Taux d'expansion > 30 % |
| H5 | Persona Camille / top 5 existe et résiste | Marché | Hub Strat | Désirabilité documentaire + signaux LinkedIn | Pain DUR convergent (5+ sources) |
| H6 | Différenciateur Hub v2 défendable | Marché | Hub Strat | Cartographie concurrentielle v1+v2 | 3 différenciateurs validés |
| H7 | Pricing hybride 3 leviers tient | Marché | Hub Strat | Benchmark + signaux DàP top 5 | Conversion Free→Pro ≥ 3 % à 12 mois |
| H8 | Canal acquisition territorial fonctionne | Marché | Hub Strat | Plan acquisition 10 premiers users | 4-5 E1 + 1-2 B1/B2/B4 acquis en 6-10 sem |
| H9 | Statut side project / convention QFC jouable | Marché | Hub Strat | Dossier arbitrage IP v1 + consultation avocat | Convention signée d'ici déc 2026 |

→ **9 hypothèses à confronter au réel** : 4 produit (Claude Design) + 5 marché (Hub Strat). Cohérence transverse Hub v2.

### 1.6 Calendrier de référence — Hub Strat (prudent) avec mention vélocité observée
- Reprendre la timeline **roadmap Hub Strat v1** dans les livrables commerciaux comme calendrier engagement
- Mentionner explicitement en pied de page calendrier : *« Calendrier indicatif — vélocité observée habituellement plus rapide »*
- Cohérent avec la position prudente vis-à-vis direction QFC et investisseurs potentiels

---

## 2. Pack F — Business plan habillé (échéance souhaitable 12 juin 2026)

### 2.1 Matériau source
- [`01-livrables-hub-strat/business-plan-hub-v2-v1.md`](./01-livrables-hub-strat/business-plan-hub-v2-v1.md) (Hub Strat — ~7 000 mots, 14 sections)
- [`01-livrables-hub-strat/previsionnel-financier-hub-v2-v1.xlsx`](./01-livrables-hub-strat/previsionnel-financier-hub-v2-v1.xlsx) (tables financières à intégrer en visuels)
- [`01-livrables-hub-strat/statut-juridique-cavalli-vs-qfc-resume-public.md`](./01-livrables-hub-strat/statut-juridique-cavalli-vs-qfc-resume-public.md) (pour le §11 — 2 variantes audiences)
- Brand system v2.1 + tokens v2.2 + voix éditoriale (tes propres bundles)

### 2.2 Livrables attendus
1. **Business plan PDF print-ready** (~25-30 pages format A4 portrait) avec :
   - Couverture brandée : logo *Stratégie ● IA* + tagline + version + date
   - Sommaire interactif (PDF avec liens internes)
   - Mise en page éditoriale Geist + Newsreader pour pull quotes
   - **8-12 visuels structurants** intégrés :
     - Carte de positionnement 2D concurrentielle (réutilisation du dessin Hub Strat avec habillage v2.2)
     - Matrice top 5 personas (notes 4,15 / 3,90 / 3,90 / 3,85 / 3,65)
     - Schéma 3 différenciateurs Hub v2
     - Schéma pricing 3 leviers (option C — Free / Pro / Équipe + section crédits)
     - Graphe ARR scenarios 36 mois (extraction xlsx)
     - Roadmap 18 mois (5 étapes × 6 dimensions transverses)
     - Architecture multi-canaux Cowork 10 acteurs (référence cartographie d'orchestration)
     - 9 hypothèses à confronter au réel (page récap §1.5)
   - Sidebar récurrente avec navigation rapide (numéro section, dernière mise à jour, version)
   - Pied de page systématique : *Stratégie IA / business plan v1.1 / 12 juin 2026 / page X / Y*

2. **Business plan Web HTML auto-hébergeable** — version cliquable navigable, mêmes contenus, articulée comme le DOC·01 `strategie.html` v2 (sections + nav latérale + sticky scroll)

### 2.3 Direction artistique
- **Ton documentaire mature** — pas startup hype, pas slide deck simplifié. Le business plan se lit, se feuillette, se consulte plusieurs fois.
- **Pull quotes Newsreader italic** pour les insights structurants (1-2 par section) — reprendre les formulations fortes du business plan source (par ex. *« Hub v2 unifie ce que les dirigeants ne trouvent qu'éclaté »*, *« La valeur n'est pas dans l'heure de formation consommée — elle est dans la décision évitée, éclairée ou accélérée »*)
- **Encadrés sémantiques** : `⌖ Insight central`, `⌖ Décision Cavalli requise`, `⌖ Hypothèse à challenger`, `⌖ Expert juridique requis` (pattern repris de DOC·01 v2)
- **Tableaux structurés** plutôt que listes à puces pour les données comparatives
- Niveau de **précision préservée** — ne pas simplifier les chiffres (3 scenarios, ratios LTV:CAC précis, règles cohérence inter-modules Vianeo)

### 2.4 Variantes audience
- **Version "direction QFC"** : conserver le §11 statut juridique en version intégrale (utiliser [`statut-juridique-cavalli-vs-qfc-resume-public.md`](./01-livrables-hub-strat/statut-juridique-cavalli-vs-qfc-resume-public.md) §1-§3 + §3.1)
- **Version "investisseur / partenaire"** : §11 traité en version "light" (cf. [`statut-juridique-cavalli-vs-qfc-resume-public.md`](./01-livrables-hub-strat/statut-juridique-cavalli-vs-qfc-resume-public.md) §3.2)
- Cavalli arbitre quelle version produire selon le cas d'usage (peut être les deux)

---

## 3. Pack G — Pitch deck premium (échéance souhaitable 19 juin 2026)

### 3.1 Matériau source
- [`01-livrables-hub-strat/pitch-deck-hub-v2-v1.pptx`](./01-livrables-hub-strat/pitch-deck-hub-v2-v1.pptx) (15 slides Hub Strat — version structure + contenu, design basique à habiller)
- Brand system v2.1 + tokens v2.2 + voix éditoriale (tes bundles antérieurs)
- Prototype Hub v2 v2 (`prototype.html` de ton sprint v2 / v2.1) — captures d'écran à intégrer comme proof-points
- [`01-livrables-hub-strat/statut-juridique-cavalli-vs-qfc-resume-public.md`](./01-livrables-hub-strat/statut-juridique-cavalli-vs-qfc-resume-public.md) (pour slide n°11 + 3 variantes audiences)

### 3.2 Livrables attendus
1. **Pitch deck PPTX premium** (12-15 slides format 16:9) — version mise en forme professionnelle, intégrant :
   - Couverture brandée avec point indigo signature
   - Slides traitées en **alternance Navy dominant / Indigo dominant / Papier dominant** (variabilité visuelle)
   - **2-3 slides avec captures du prototype interactif** (onboarding diagnostic 5 questions + home adaptative + module + chat) — proof-point produit
   - 1 slide carte de positionnement 2D habillée
   - 1 slide chart ARR scenarios habillé (Recharts-style, sans 3D)
   - 1 slide équipe avec wordmark + photos / icônes Cavalli + 5 canaux Cowork (style Linear / Notion)
   - Slide finale CTA avec coordonnées Cavalli (blaise.cavalli.pro@gmail.com) + tagline + URL landing si dispo

2. **Pitch deck PDF print-ready** (export du PPTX, pour transmission email + impression A4)

3. **Speaker notes PPTX** (1 paragraphe par slide, pour driver Cavalli en présentation orale)

### 3.3 Direction artistique
- **Format premium proche HBR Executive / Linear / Notion** — pas slide deck startup générique
- **Titres en Geist Medium 36-48pt** + body Geist Regular 14-16pt + pull quote Newsreader italic occasionnel
- **Charts propres** (Recharts-style, sans 3D, sans dégradés)
- **Iconographie monoline v2.2** (pack e) pour illustrer les concepts
- **Footer minimal** : numéro de slide + *Stratégie IA* + date version
- **Pas plus de 1-2 idées par slide** — privilégier blancs + respiration

### 3.4 Variantes audience
3 variantes mineures **slide n°15 (« Et maintenant »)** selon audience :

- **A — Direction QFC** : focus sur les 3 décisions structurantes Cavalli (consult avocat juin, transmission QFC août-sept, signature convention déc 2026-janv 2027)
- **B — Investisseurs early stage potentiels** : focus sur les 3 jalons opérationnels (POC RAG juin, MVP commercialisable Étape 3, T0 acquisition janvier 2027)
- **C — Partenaires institutionnels (CCI / French Tech Est / POLARIS / RETIS)** : focus sur les modalités de partenariat (référencement, intégration parcours accompagnement, sièges Pro offerts au réseau)

→ Slide n°11 « Statut juridique convention QFC » à **doubler en version "light"** pour audiences B et C (sans révéler la mécanique convention).

---

## 4. Pack H — Documentation commerciale (échéance souhaitable 26 juin 2026)

### 4.1 Périmètre

Cinq livrables coordonnés visant à doter Cavalli d'une **boîte à outils commerciale cohérente** pour activer les 10 premiers utilisateurs Pro (plan acquisition v1) :

#### 4.1.1 One-pager prospect Pro (A4 recto-verso, lecture en 60 sec)

**Recto** :
- Hero : tagline *Stratégie IA — le copilote de décision IA des dirigeants PME-ETI*
- Promesse client (3-4 lignes)
- 3 différenciateurs (continuité + curation expert + outils Pro)
- Screenshot prototype (1 visuel)
- Tarif clair (Pro 29 €/mois + mention Free + crédits 10 € bienvenue)
- CTA inscription (URL + QR code)

**Verso** :
- **5 cas d'usage par persona top 5** (formulés comme « Si vous êtes [persona], vous trouverez chez Stratégie IA... »)
- Mention RGPD / EU implicite (footer subtle)
- 2-3 espaces vides « témoignage early adopter » (à remplir post-T0)
- Mentions légales (chatbot IA labellisé, statut beta early adopter)

#### 4.1.2 Brochure partenaires institutionnels (4-8 pages A4)

Cible : CCI, French Tech Est, POLARIS, Bpifrance Innovation, RETIS, Conseil Régional Grand Est.

- Page 1 — *Stratégie IA en bref* (qu'est-ce que c'est, qu'y trouvez-vous en tant qu'incubateur/CCI/réseau)
- Page 2-3 — Cas d'usage et bénéfices pour le réseau partenaire (orientation B2B2C / B2B2B)
- Page 4 — Mécanique de partenariat possible (référencement, intégration dans parcours d'accompagnement, sièges Pro offerts au réseau)
- Page 5 — Économie du partenariat (narratif valeur, sans chiffres engageants)
- Page 6-7 — FAQ partenaire (juridique, RGPD, AI Act, modalités, contact)
- Page 8 — Couverture / CTA

#### 4.1.3 Deck de vente light (8-10 slides PPTX, version réduite du pitch deck premium)

Cible : Cavalli en RDV 1-to-1 prospect type top 5 personas.

- Focus 3 slides solution + 2 slides tarif + 1 slide CTA early adopter
- Sans contenu sensible (pricing détaillé Équipe, convention QFC, modélisation économique détaillée)

#### 4.1.4 Templates email (6 versions courtes — HTML responsive + Markdown lisible)

| # | Email | Cible | Variants |
|---|-------|-------|----------|
| 1 | Cold outreach LinkedIn | 5 personas top tier | 5 versions (E1 / B1 / B2 / B4 / C5) |
| 2 | Demande d'introduction réseau 2e degré | Contacts Cavalli 1er degré | 1 version générique |
| 3 | Post-démo (relance avec crédits 10 €) | Prospects ayant fait un RDV | 1 version |
| 4 | Early adopter welcome (onboarding 3 mois Pro offerts) | Nouveaux early adopters | 1 version |
| 5 | Checkout abandonné (relance Stripe) | Free → Pro hésitants | 1 version |
| 6 | Newsletter Hub v2 v1 (première issue) | Pre-liste + early adopters | 1 version |

Pour les emails 1 (cold outreach LinkedIn), prévoir explicitement les 5 variantes adaptées à chaque persona du top 5 — Cavalli les utilisera directement dans l'activation phase 1 de l'acquisition (S+1 à S+4 du plan acquisition v1).

#### 4.1.5 Landing soft launch — capture email pré-liste (1 page HTML)

- Hero avec tagline + countdown POC RAG Étape 1 (semaines 1-2 juin)
- Formulaire email + persona déclaratif (sélection dans le top 5 : « Je suis... »)
- Promesse early adopter (10 places, 3 mois Pro offerts, accès roadmap)
- Mentions RGPD + AI Act + statut beta

### 4.2 Direction artistique transverse pack H
- **Cohérence stricte avec brand system v2.1 / tokens v2.2** — pas de glissement vers du marketing générique
- **Hiérarchie visuelle forte** sur le one-pager (lecture en 60 secondes maximum)
- **Voix éditoriale « en connaissance de cause »** maintenue — pas de superlatifs, pas de buzz, factualité
- **Iconographie monoline v2.2** systématique (pas de stock photo)
- **Mentions légales explicites** dans tous les supports (chatbot IA labellisé selon AI Act, RGPD, conditions early adopter)

### 4.3 Coordination avec Hub Strat
- Validation Cavalli préalable sur chaque template avant déploiement
- Pas de communication externe massive avant arbitrage IP convention QFC (signature décembre 2026 - janvier 2027)
- Versioning par audience (one-pager Pro freelance E1 ≠ one-pager Pro COO ETI B1) — prévoir variantes mineures coordonnées avec le pack G

---

## 5. Modalités de transmission et coordination

### 5.1 Articulation avec les canaux pairs

| Canal pair | Apport vers Sprint v2.3 |
|------------|----------------------------|
| **Hub Strat** | Matière stratégique consolidée (12 livrables) + brief détaillé (ce document) |
| **Hub Content** | Matière éditoriale curated (base RAG) pour newsletter Hub v2 (template #6) + content marketing |
| **Hub RAG** | Statut Étape 1 POC RAG = proof-point fonctionnel pour captures prototype dans le pitch deck |
| **Claude Code** | Implémentation potentielle de la landing soft launch (pack H §4.1.5) |
| **Cavalli** | Validation des livrables, transmission croisée, arbitrages au fil du sprint |
| **DEV IA Head** | Pattern transverse de mise en forme livrables stratégiques (réutilisable pour autres canaux head) |

### 5.2 Cadence cible (indicative, vélocité observée habituellement plus rapide)

| Échéance souhaitable | Livraison |
|------------------------|------------|
| Jeudi 12 juin 2026 | Pack F — Business plan habillé (PDF + Web) + variantes audiences |
| Jeudi 19 juin 2026 | Pack G — Pitch deck premium (PPTX + PDF + speaker notes) + 3 variantes slide n°15 |
| Jeudi 26 juin 2026 | Pack H — Documentation commerciale complète (5 livrables coordonnés) |

### 5.3 Note de retour v2.3 attendue en sortie de sprint

Comme pour les sprints v2.1 et v2.2, produire une **note de retour Claude Design v2.3 structurée** à transmettre à Cavalli + Hub Strat + Hub Content + DEV IA Head, avec :

- Rappel des arbitrages pris en cours de sprint (le cas échéant)
- 3 packs livrés détaillés + check pré-livrable
- Hypothèses à instrumenter post-Étape 1 (continuité avec pack b v2.2)
- Zones non couvertes / à itérer en v2.4

### 5.4 Format de remontée

Modalités de remontée des livrables Sprint v2.3 :
- **Option A (recommandée)** : push dans le même repo `LumenBot/hub-ia` dans un dossier `claude-design-sprint-v2.3/` (cohérence cross-canal — mêmes URLs raw accessibles à Hub Strat pour relecture et à Cavalli pour récupération)
- **Option B** : transmission via bundle ZIP à Cavalli (modèle des sprints précédents v2.1 / v2.2)
- À arbitrer au démarrage du sprint avec Cavalli

---

## 6. Synthèse — état attendu fin sprint v2.3

À la clôture du sprint v2.3 (26 juin 2026 souhaitable), Cavalli + Cowork disposeront d'un **kit commercial Stratégie IA cohérent et déployable** :

- **Pack F** — Business plan v1.1 habillé (PDF + Web) en 2 variantes audiences
- **Pack G** — Pitch deck v1.1 premium (PPTX + PDF + speaker notes) en 3 variantes audiences
- **Pack H** — Documentation commerciale (one-pager prospect + brochure partenaires + deck de vente light + 6 templates email dont 5 cold outreach LinkedIn différenciés par persona + landing soft launch)

**Cohérence end-to-end** : un prospect qui découvre Stratégie IA via le one-pager (pack H) retrouve la même signature visuelle, le même ton, les mêmes promesses dans le pitch deck (pack G), puis dans le business plan (pack F), puis dans le produit lui-même (prototype v2 + tokens v2.2). Test de la cohérence multi-acteurs Cowork passé.

**Prêt pour** :
- Transmission direction QFC (août-septembre 2026 — business plan version "direction QFC" + pitch deck variante A)
- Activation acquisition early adopters dès ouverture MVP Étape 2 fin juin / mi-juillet 2026 (pack H complet)
- Briefing investisseurs early stage potentiels en cas de pivot levée (business plan version "investisseur" + pitch deck variante B)
- Sourcing partenariats institutionnels (brochure partenaires + pitch deck variante C)

---

## 7. Annexe — points d'attention transverses

### 7.1 Étanchéité QFC
Aucun nom de startup réelle accompagnée à Quai Alpha ne doit apparaître dans les livrables. Le canal QFC est mobilisé au niveau structurel uniquement (mention du réseau d'incubateurs, alumni, partenaires institutionnels).

### 7.2 Mentions légales obligatoires
- **Chatbot IA labellisé** (AI Act — obligation transparence systèmes à risque limité, échéance 2 août 2026)
- **RGPD** : politique de confidentialité accessible, droit d'effacement / opposition, base légale intérêt légitime
- **CGU / CGV** : version minimum viable freemium SaaS pour le tier Pro (CGV résiliation en ligne max 2 mois préavis — EU Data Act septembre 2025)
- **Statut beta early adopter** : mention transparente sur les conditions des 3 mois Pro offerts

### 7.3 Hypothèses à confronter au réel (rappel des 9 §1.5)

Les livrables produits sont conçus pour **être confrontés au réel** dès l'ouverture Étape 1 (POC RAG semaines 1-2 juin) et Étape 2 (MVP onboarding fin juin) — chaque retour utilisateur réel doit pouvoir alimenter l'itération v1.2 du business plan, du pitch deck, de la documentation commerciale.

### 7.4 Validation Cavalli préalable au déploiement

Aucun livrable du pack H n'est diffusé en externe avant **validation Cavalli explicite + arbitrage du calendrier de communication** (cohérent avec la position prudente vis-à-vis QFC tant que la convention n'est pas signée).

---

## 8. Sources Hub Strat de référence

Tous les livrables Hub Strat sont accessibles dans `Canaux/Hub-Strat/outputs/` :

- Documents stratégiques (12) — cités §0
- Matière éditoriale (Hub Content) — `Canaux/Hub-IA/outputs/`
- Vision Hub v2 v1.0 (22 mai 2026) — `Canaux/Hub-IA/outputs/VISION-HUB-V2-CONSOLIDEE-v1.md`
- Note pricing Hub IA (25 mai 2026) — `Canaux/Hub-IA/outputs/NOTE-PRICING-HUB-V2-credits-vs-abonnement.md`

Tous les livrables Claude Design (sprints v2 / v2.1 / v2.2) sont accessibles dans `Canaux/Hub-IA/outputs/` également.

---

## 9. Historique

| Date | Version | Modification |
|------|---------|--------------|
| 27 mai 2026 | officielle | Création — sprint v2.3 ouvert sur la base des 6 arbitrages Cavalli (naming Stratégie IA / Hub v2, persona narratif top 5, pricing option C, stack variante A puis B, articulation 9 hypothèses, calendrier indicatif). 3 packs F/G/H cadrés. |

---

*Brief sprint v2.3 — version officielle 27 mai 2026, à transmettre par Cavalli au canal Claude Design pour ouverture immédiate. Note de retour v2.3 attendue en sortie de sprint.*
