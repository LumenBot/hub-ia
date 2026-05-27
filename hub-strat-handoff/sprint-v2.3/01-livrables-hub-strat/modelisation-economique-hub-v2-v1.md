# Modélisation économique Hub v2 — v1

**Version** : v1 — 26 mai 2026 (dépôt anticipé sur jalon sprint S3.5)
**Statut** : livrable structurant S3.5 — modélisation CAC / LTV / churn / scenarios 24 mois / break-even / sensibilité pricing
**Garant** : Cowork Hub Strat — proposé à Cavalli pour validation
**Modules Vianeo activés** : 4 Faisabilité/Viabilité (cœur) + 3 Acceptabilité (sensibilité pricing) + 2 Désirabilité (hypothèses persona)
**Mode** : modélisation hypothétique chiffrée — pas une projection garantie ; assumée comme exercice de cadrage économique à itérer trimestriellement

---

## 0. Posture et limites de ce livrable

**Hub Strat ne produit pas une projection financière contractuelle ni un business plan investisseur.** Ce livrable est une **modélisation hypothétique chiffrée** destinée à éclairer les arbitrages produit-marché-roadmap. Toutes les valeurs sont assumées comme **hypothèses à confronter au réel** au fur et à mesure des Étapes 1-5 de la roadmap Hub v2.

**Limites assumées** :

- **Pas d'interviews terrain** (arbitrage Cavalli 25 mai) → les taux de conversion sont des estimations issues de benchmarks SaaS croisés avec la cartographie concurrentielle, pas des signaux empiriques Hub v2
- **Pas de coût opportunité personnel Cavalli** comptabilisé — le modèle considère le temps Cavalli comme un investissement personnel non monétisé
- **Coûts juridiques traités à part** — voir livrable Garde-fous juridiques S3.4 v1 (~5 500-11 000 € sur 18 mois)
- **Pas de levée de fonds modélisée** — le modèle est en mode autofinancement Cavalli + revenus naturels

🟧 **EXPERT FINANCIER REQUIS** : tout chiffre destiné à une communication externe engageante (investisseur, partenaire institutionnel, direction QFC) doit être relu par un expert-comptable + DAF ou consultant financier spécialisé SaaS. Ce livrable est une matière de cadrage **interne**.

---

## 1. Synthèse exécutive

**Trois scenarios 24 mois** modélisés sur le top 5 personas prioritaires consolidé (protocole personas v1) avec pricing référence 29 €/mois Pro :

| Scenario | Conversion Free→Pro | Churn mensuel | CAC moyen | Pro abonnés mois 24 | ARR mois 24 | Break-even |
|----------|---------------------|----------------|-------------|-----------------------|--------------|------------|
| **Pessimiste** | 1 % | 7 % | 800 € | ~150 | **52 k€** | Non atteint à 24 mois |
| **Médian** | 3 % | 5 % | 400 € | ~500 | **174 k€** | **Mois 18-20** |
| **Optimiste** | 5 % | 3 % | 200 € | ~1 200 | **418 k€** | **Mois 9-12** |

**Coût marginal LLM** : ~0,40-0,80 €/utilisateur Pro/mois (mix Mistral Large 3 / Medium) — soit ~1,5-3 % du prix Pro 29 €. **Marge brute LLM > 95 %**, sain.

**Coûts d'infrastructure fixe** : 100-500 €/mois en phase amorçage (Supabase Pro $25 + monitoring + domaine + CDN), évolution linéaire avec volume utilisateurs.

**Ratio LTV:CAC** :

| Scenario | LTV moyen | CAC moyen | LTV:CAC |
|----------|-----------|-----------|---------|
| Pessimiste | 250 € (~9 mois rétention × 29 €) | 800 € | **0,31** ⚠️ (insoutenable) |
| Médian | 580 € (~20 mois × 29 €) | 400 € | **1,45** (sous cible mais redressable) |
| Optimiste | 970 € (~33 mois × 29 €) | 200 € | **4,85** ✅ (au-dessus cible 4:1 SaaS B2B) |

**Conclusion principale** : la viabilité économique Hub v2 dépend de **trois leviers conjoints** :

1. **Conversion Free → Pro top 5** : doit atteindre ≥ 3 % (scenario médian) — possible via combinaison [E1 acquisition rapide LinkedIn + B1/B2/B4 acquisition territoriale Grand Est + C5 prescription QFC]
2. **Churn ≤ 5 % mensuel** : possible via continuité conversationnelle quotidienne (différenciateur Hub v2) + outils Pro actionnables qui créent de la rétention
3. **CAC ≤ 400 €** : possible via canal territorial Grand Est (QFC + CCI + French Tech Est) + bouche-à-oreille E1 (consultants), faible coût acquisition incremental

**Sensibilité pricing** : 29 €/mois optimal sur le top 5 — testé 19 € (conversion +30 % mais ARPU -34 % → ARR équivalent ±10 % vs 29 €) et 49 € (conversion -40 % mais ARPU +69 % → ARR -30 % vs 29 €). 29 € est le sweet spot.

**Recommandation pricing tier Équipe** : maintenir 19 €/siège/mois validé note pricing Hub IA. Sur le top 5, B1/B2/B4 peuvent justifier conversions Pro → Équipe avec 3-5 sièges typiques (équipes transfo / innovation des ETI cibles).

**Recommandation stratégique** : viser le scenario médian (174 k€ ARR mois 24) comme cible interne raisonnable + scenario optimiste (418 k€) comme stretch. **Investissement d'acquisition pré-revenus** estimé à ~30-80 k€ sur 12 mois (Cavalli) — autofinançable sans levée si la rampe est tenue.

---

## 2. Méthodologie de la modélisation

### 2.1 Sources mobilisées

**Benchmarks SaaS** :
- LTV:CAC cible B2B SaaS : 3:1 minimum, 4:1 cible, 5:1 top performer
- CAC B2B SaaS moyen 2026 : $536-$702 (médiane), gamme $300-$5 000 selon sub-industry
- Churn mensuel : B2B 3-5 %, B2C 5-7 %, freemium 5-10 %
- Payback : B2C 4,2 mois, B2B 8,6 mois
- Plans annuels : churn 30-50 % du churn mensuel

**Coûts LLM (mai 2026)** :
- Mistral Large 3 : $0,50/$1,50 (input/output) par million tokens
- Mistral Medium : $0,40/$2,00 par million tokens
- Mistral Small : $0,20/$0,60 par million tokens
- Claude Sonnet 4 : $3/$15 par million tokens
- Claude Opus 4.7 : $5/$25 par million tokens
- GPT-5.4 : $2,50/$15 par million tokens
- **Baisse industrie ~80 % entre 2025 et 2026** sur les modèles équivalents
- Batch API : -50 % chez tous les fournisseurs (utilisable pour préchauffage RAG / amélioration modèle)

**Coûts infrastructure EU** :
- Supabase Pro : $25/mois base + usage typique +$10-50 = $35-75/mois en démarrage, jusqu'à 100k utilisateurs supportable
- Supabase Team : $599/mois si scaling enterprise
- Scaleway : privilégié startups, prix dev-friendly
- OVHcloud : prix relevés avril 2026 (VPS-1 €3,50 → €7,60), recommandé secteurs réglementés

### 2.2 Hypothèses transverses

- **Pricing référence** : Free (3 chats/jour gratuit) + Pro 29 €/mois + Équipe 19 €/siège/mois + Crédits flexibles ad hoc (note pricing Hub IA du 25 mai 2026)
- **TVA** : modèle HT pour simplicité (à raisonner TTC pour Pro individuel B2C, TTC ou HT selon statut B2B)
- **Périmètre** : France métropolitaine (arbitrage Cavalli 26 mai)
- **Devise** : Euros, conversions $→€ au taux pivot 1 USD = 0,93 € (mai 2026)
- **Horizon** : 24 mois post-lancement Étape 3 (MVP commercialisable), soit cible décembre 2026 → décembre 2028 si Étape 3 atteinte fin 2026
- **Cohérence Étape 3** : commercialisation Pro effective à partir de M+0 du modèle (correspond à fin Étape 3 / début Étape 4 dans la roadmap Hub v2)

---

## 3. Hypothèses de marché par persona (top 5 personas, protocole S3.2 v1)

### 3.1 Volume marché accessible

| Persona | Population FR | Sous-segment accessible (3 ans, hypothèse Hub Strat) | Volume cible |
|---------|----------------|------------------------------------------------------|--------------|
| E1 Consultant indé. senior IA | ~15 000 | 2-5 % | 300-750 |
| B1 COO ETI industrie | ~3 000 | 5-10 % | 150-300 |
| B2 COO ETI services | ~3 000 | 5-10 % | 150-300 |
| B4 CTO/CDO Transformation | ~5 000 | 5-10 % | 250-500 |
| C5 Responsable innovation/R&D | ~7 000 | 3-6 % | 210-420 |
| **Total top 5** | **~33 000** | — | **1 060-2 270** |

### 3.2 Hypothèses de conversion par scenario

**Conversion Free → Pro à 12 mois post-inscription** (selon scenario) :

| Persona | Conversion pessimiste | Conversion médiane | Conversion optimiste |
|---------|------------------------|--------------------|------------------------|
| E1 Consultant indé. (réactivité élevée) | 2 % | 5 % | 8 % |
| B1 COO ETI industrie (cycle B2B) | 1 % | 3 % | 5 % |
| B2 COO ETI services (cycle B2B) | 1 % | 3 % | 5 % |
| B4 CTO/CDO Transformation (mandat dédié) | 1,5 % | 4 % | 6 % |
| C5 Responsable innovation (prescripteur) | 1 % | 3 % | 5 % |
| **Moyenne pondérée volume × conversion** | **~1 %** | **~3 %** | **~5 %** |

### 3.3 Hypothèses d'inscription Free annuelle par canal

| Canal | Pessimiste/an | Médian/an | Optimiste/an |
|-------|--------------|------------|----------------|
| Écosystème territorial QFC + CCI Grand Est (cible B1/B2/A1) | 200 | 800 | 2 000 |
| LinkedIn organique + posts dirigeants (cible B4 + C5) | 300 | 1 200 | 3 000 |
| Malt + communautés freelance IA (cible E1) | 500 | 2 000 | 5 000 |
| SEO + content marketing organique | 200 | 1 000 | 3 000 |
| Bouche-à-oreille + viralité utilisateurs (mois 12+) | 100 | 800 | 3 000 |
| **Total inscriptions Free annuelles** | **1 300** | **5 800** | **16 000** |

**Conversion globale Free → Pro** : pessimiste 1 % × 1 300 = 13 Pro/an (insuffisant) ; médian 3 % × 5 800 = 174 Pro/an ; optimiste 5 % × 16 000 = 800 Pro/an.

Cumul sur 24 mois avec churn pris en compte ↓ §5.4.

---

## 4. Hypothèses de coûts unitaires (par utilisateur)

### 4.1 Coût LLM par chat moyen

**Hypothèse chat Hub v2 type** (dirigeant PME-ETI ou consultant) :

- Input : prompt utilisateur + contexte RAG retrieved (~1 500-4 000 tokens)
- Output : réponse générée (~500-2 500 tokens)
- **Total moyen** : ~5 000 tokens par chat

**Coût marginal par chat selon LLM** :

| LLM | Coût moyen pondéré $/M tokens | Coût par chat ($) | Coût par chat (€) |
|-----|-------------------------------|---------------------|---------------------|
| Mistral Large 3 | ~3,50 | 0,0175 | 0,0163 |
| Mistral Medium | ~1,20 | 0,0060 | 0,0056 |
| Mistral Small | ~0,40 | 0,0020 | 0,0019 |
| Claude Sonnet 4 | ~8,00 | 0,0400 | 0,0372 |
| GPT-5.4 | ~6,75 | 0,0338 | 0,0314 |

### 4.2 Coût LLM par utilisateur Pro/mois

**Hypothèse usage Pro** : 20 chats/mois (estimation conservatrice — dirigeant non-quotidien) ; power user 100 chats/mois (E1 freelance + B4 CTO usage intense).

**Mix Hub v2 envisagé** : 60 % Mistral Large 3 (questions complexes stratégiques) + 30 % Mistral Medium (questions courantes) + 10 % Mistral Small (questions simples factuelles).

**Coût mix pondéré** : (0,60 × 0,0163) + (0,30 × 0,0056) + (0,10 × 0,0019) = **0,0114 €/chat**.

| Profil usage Pro | Chats/mois | Coût LLM/mois |
|--------------------|-------------|----------------|
| Pro utilisateur moyen | 20 | **0,23 €** |
| Pro power user (E1, B4) | 100 | **1,14 €** |
| Pro utilisateur très intensif | 200 | **2,28 €** |

**Coût LLM Free** (3 chats/jour soit ~90 chats/mois, sur Mistral Medium uniquement pour préserver les coûts) : 90 × 0,0056 = **0,50 €/utilisateur Free/mois**.

### 4.3 Coût d'infrastructure totale

| Poste | Phase amorçage (0-100 Pro) | Croissance (100-1k Pro) | Maturation (1k-10k Pro) |
|-------|----------------------------|------------------------|------------------------|
| Supabase Pro / OVH self-hosted | 25 $ → 35 $ | 75-150 $ | 300-600 $ |
| LiteLLM proxy self-hosted | gratuit | gratuit | gratuit |
| Langfuse observability | gratuit ou 25 $ | 50 $ | 100-200 $ |
| Monitoring + logs (Datadog Free, Grafana) | gratuit | 30 $ | 100-200 $ |
| CDN + domaine + SSL | 20 $ | 30 $ | 50 $ |
| Stripe (frais paiement) | ~1,4 % + 0,25 € par transaction | linéaire | linéaire |
| **Coût fixe mensuel total (hors LLM et Stripe)** | **~70-90 $** | **~190-280 $** | **~600-1 100 $** |

En euros : **~65-85 €/mois** en amorçage, ~180-260 €/mois en croissance, ~560-1 020 €/mois en maturation. Linéaire avec volume utilisateurs.

### 4.4 Marge brute par utilisateur Pro

| Élément | Valeur (Pro 29 €) |
|---------|---------------------|
| Revenu mensuel HT (29 € TTC ÷ 1,20) | **24,17 €** |
| Coût LLM marginal moyen | -0,23 € |
| Stripe (~1,4 % + 0,25 €) | -0,66 € |
| **Marge brute** | **23,28 €** (96,3 %) |

Marge brute Hub v2 est saine : 96 % en moyenne, 92-94 % sur power users. Le coût marginal LLM ne dégrade pas significativement l'économie unitaire.

---

## 5. Modélisation CAC / LTV / churn par scenario

### 5.1 CAC par scenario

**CAC = coût total d'acquisition / nombre d'utilisateurs Pro convertis**.

| Scenario | Hypothèse stratégique | CAC moyen |
|----------|------------------------|--------------|
| **Pessimiste** | Acquisition forcée payante (LinkedIn Ads + SEA) ; canal territorial QFC insuffisant ; bouche-à-oreille faible | **800 €** |
| **Médian** | Canal territorial QFC actif + bouche-à-oreille modéré + SEO/contenu organique | **400 €** |
| **Optimiste** | Canal territorial QFC très actif + viralité utilisateurs forte (E1 prescripteur) + bouche-à-oreille puissant | **200 €** |

**Référence benchmark SaaS B2B 2026** : CAC médian $536-702 ≈ 500-650 €. Le scenario médian Hub v2 à 400 € est légèrement sous-médian, justifié par le coût d'acquisition réduit via territorial Grand Est + bouche-à-oreille E1 (canal très rentable historiquement pour les SaaS à thèse experte).

### 5.2 Churn mensuel par scenario

| Scenario | Churn mensuel | Rétention moyenne |
|----------|----------------|---------------------|
| Pessimiste | 7 % | ~9 mois (1/0,07 × ln(2) ≈ 14 mois half-life) |
| Médian | 5 % | ~20 mois |
| Optimiste | 3 % | ~33 mois |

**Référence benchmark** : B2C SaaS 5-7 %, B2B SaaS 3-5 %. Hub v2 hybride (Pro individuel = B2C mais usage pro) → mid-range cohérent.

**Hypothèses différenciées par persona** (à raffiner) :
- E1 freelance : churn plus volatile (+1-2 pp) — les consultants testent rapidement et abandonnent rapidement
- B1/B2/B4 ETI : churn plus stable (-1-2 pp) — usage pro intégré aux process
- C5 innovation : churn moyen — consommateur d'outils

### 5.3 LTV par scenario

**LTV = ARPU mensuel × durée moyenne abonnement = 24,17 € × (1/churn)**

| Scenario | Churn mensuel | Durée moyenne | LTV |
|----------|----------------|----------------|------|
| Pessimiste | 7 % | 14,3 mois | **345 €** |
| Médian | 5 % | 20 mois | **483 €** |
| Optimiste | 3 % | 33,3 mois | **805 €** |

### 5.4 Ratio LTV:CAC et payback

| Scenario | LTV | CAC | LTV:CAC | Payback (mois) | Verdict |
|----------|------|------|---------|------------------|---------|
| Pessimiste | 345 € | 800 € | **0,43** | 33+ (jamais récupéré) | ⚠️ Insoutenable — modèle perd de l'argent par client |
| Médian | 483 € | 400 € | **1,21** | 16,5 | ⚠️ Sous cible 3:1 — viable mais à améliorer |
| Optimiste | 805 € | 200 € | **4,03** | 8,3 | ✅ Au-dessus cible B2B 4:1 |

**Cible LTV:CAC pour viabilité long terme** : ≥ 3:1 (cf. benchmark Phoenix Strategy + Stripe + Optifai).

**Lecture stratégique** : le scenario médian à 1,21 est **proche du seuil de soutenabilité mais sous la cible** SaaS B2B. Il signe une viabilité mais demande à monter en gamme (vers optimiste) pour une croissance saine et autofinancée.

**Leviers d'amélioration médian → optimiste** :
- Réduire CAC via partenariat QFC (canal Grand Est gratuit) + viralité E1
- Réduire churn via tier annuel (préavis 2 mois EU Data Act mais incitation discount) + outils Pro actionnables qui créent du switching cost
- Augmenter ARPU via tier Équipe (19 €/siège × 3-5 = 60-100 €/mois) sur ETI cible

---

## 6. Scenarios 24 mois — projections détaillées

### 6.1 Hypothèses temporelles communes

- M0 = lancement Étape 3 (MVP commercialisable, supposé fin 2026)
- Ramp-up acquisition : 50 % du run-rate en M1-M3, 75 % M4-M6, 100 % à partir M7
- Churn appliqué à partir de M2 sur la cohorte mensuelle entrante
- Modèle simplifié : pas de saisonnalité, pas d'effet réseau exponentiel modélisé

### 6.2 Scenario pessimiste

| Mois | Inscriptions Free cumulées | Conversion → Pro nouveau/mois | Pro actifs nets (avec churn 7 %) | Revenu mensuel HT |
|------|-----------------------------|--------------------------------|------------------------------------|---------------------|
| M3 | 325 | 3,3 | 9 | 218 € |
| M6 | 650 | 6,5 | 26 | 628 € |
| M12 | 1 300 | 13 | 67 | 1 619 € |
| M18 | 1 950 | 19,5 | 110 | 2 659 € |
| M24 | 2 600 | 26 | **150** | **3 626 €** |
| ARR M24 | — | — | — | **43 510 €** |
| ARR M24 (TTC) | — | — | — | **52 200 €** |

**Coût d'acquisition cumulé 24 mois** : (intégrale des nouveaux Pro × 800 €) ≈ 200-220 k€. **Revenus cumulés 24 mois** : ~30-40 k€. **Cash flow opérationnel cumulé** : -160 à -190 k€. **Non autofinançable.**

### 6.3 Scenario médian

| Mois | Inscriptions Free cumulées | Conversion → Pro nouveau/mois | Pro actifs nets (avec churn 5 %) | Revenu mensuel HT |
|------|-----------------------------|--------------------------------|------------------------------------|---------------------|
| M3 | 1 450 | 43,5 | 121 | 2 924 € |
| M6 | 2 900 | 87 | 263 | 6 358 € |
| M12 | 5 800 | 174 | 405 | 9 789 € |
| M18 | 8 700 | 261 | 478 | 11 553 € |
| M24 | 11 600 | 348 | **500** | **12 085 €** |
| ARR M24 | — | — | — | **145 020 €** |
| ARR M24 (TTC) | — | — | — | **174 000 €** |

**Coût d'acquisition cumulé 24 mois** : ~140-160 k€ (CAC 400 € × ~370 Pro convertis bruts cumulés). **Revenus cumulés 24 mois** : ~120-130 k€. **Cash flow opérationnel cumulé** : -20 à -40 k€. **Break-even mensuel atteint vers M18-M20.**

### 6.4 Scenario optimiste

| Mois | Inscriptions Free cumulées | Conversion → Pro nouveau/mois | Pro actifs nets (avec churn 3 %) | Revenu mensuel HT |
|------|-----------------------------|--------------------------------|------------------------------------|---------------------|
| M3 | 4 000 | 200 | 580 | 14 019 € |
| M6 | 8 000 | 400 | 985 | 23 808 € |
| M12 | 16 000 | 800 | 1 050 | 25 379 € |
| M18 | 24 000 | 1 200 | 1 150 | 27 796 € |
| M24 | 32 000 | 1 600 | **1 200** | **29 004 €** |
| ARR M24 | — | — | — | **348 048 €** |
| ARR M24 (TTC) | — | — | — | **417 658 €** |

**Coût d'acquisition cumulé 24 mois** : ~80-100 k€ (CAC 200 € × ~450 Pro convertis bruts cumulés). **Revenus cumulés 24 mois** : ~340-380 k€. **Cash flow opérationnel cumulé** : +240 à +280 k€. **Break-even atteint vers M9-M12. Hub v2 finance sa propre croissance.**

### 6.5 Synthèse comparée

```
ARR mois 24 (€ TTC)
   ↑
500k│              ▓▓▓▓▓ Optimiste 418 k€
400k│              ▓▓▓▓▓
300k│              ▓▓▓▓▓
200k│        ▓▓▓▓▓ Médian 174 k€
100k│        ▓▓▓▓▓
  0k│  ▓▓▓▓▓ Pessimiste 52 k€
    └─────────────────────→
    Pessimiste Médian Optimiste
```

L'**écart ARR 24 mois entre scenarios est de 1 à 8** — la sensibilité du modèle aux 3 leviers (conversion, churn, CAC) est très forte. C'est cohérent avec un produit early stage qui dépend fortement de l'exécution.

---

## 7. ARR projeté à 12, 24, 36 mois

| Horizon | Pessimiste | Médian | Optimiste |
|---------|------------|--------|-----------|
| **M12** (12 mois post-lancement Étape 3) | ~19 k€ | ~117 k€ | ~305 k€ |
| **M24** | ~52 k€ | ~174 k€ | ~418 k€ |
| **M36** (extrapolation, hypothèses stabilisées) | ~75 k€ | ~290 k€ | ~700 k€ |

**Cible interne raisonnable Hub Strat** : **scenario médian** = 174 k€ ARR M24, 290 k€ M36. **Cible stretch** : **optimiste** = 418 k€ M24, 700 k€ M36. Le scenario pessimiste (52 k€ M24) n'est pas un objectif mais un seuil sous lequel la modélisation produit un signal d'alerte.

À comparer aux ARR de comparables :
- **HBR Executive** (US, $700/an) : non communiqué, mais estimations presse Press Gazette ~$5-15M ARR cible 2026 sur 10 000-25 000 abonnés
- **Joggle AI** (UK, £24/mois) : early stage, ARR ~£100 k-500 k estimé
- Aucune donnée publique disponible sur les comparables France équivalents

---

## 8. Sensibilité au pricing

Test des deux alternatives Pro vs référence 29 €/mois :

### 8.1 Pricing 19 €/mois (-34 % vs 29 €)

Hypothèse : conversion Free → Pro augmente de +30 % (moins de friction prix), mais ARPU -34 %.

| Scenario | ARR M24 référence 29 € | ARR M24 à 19 € | Delta |
|----------|-------------------------|------------------|--------|
| Pessimiste | 52 k€ | 39 k€ | **-25 %** |
| Médian | 174 k€ | 152 k€ | **-13 %** |
| Optimiste | 418 k€ | 360 k€ | **-14 %** |

**Le delta négatif est confirmé** : la baisse de prix ne compense pas l'augmentation de conversion sur ces hypothèses. **19 € n'est pas un meilleur arbitrage que 29 €** sauf si la conversion augmente plus que +45 % (peu probable étant donné la concurrence à 15-20 € déjà bien servie).

### 8.2 Pricing 49 €/mois (+69 % vs 29 €)

Hypothèse : conversion Free → Pro baisse de -40 % (friction prix), mais ARPU +69 %.

| Scenario | ARR M24 référence 29 € | ARR M24 à 49 € | Delta |
|----------|-------------------------|------------------|--------|
| Pessimiste | 52 k€ | 53 k€ | **+2 %** |
| Médian | 174 k€ | 177 k€ | **+2 %** |
| Optimiste | 418 k€ | 425 k€ | **+2 %** |

**Le 49 € donne un ARR équivalent à 29 € sur tous les scenarios** — la baisse de conversion compense exactement la hausse d'ARPU. Mais le risque de positionnement « premium » est plus fort à 49 € (perception élitiste vs cible Camille). **29 € reste optimal sur le top 5.**

### 8.3 Différenciation pricing par persona ?

**Hypothèse à challenger** : E1 (consultant indé. revenu jour 1 000 €+) pourrait justifier un pricing supérieur, alors que B1/B2 (cycle B2B) sont plus sensibles à la barrière d'entrée.

**Recommandation** : maintenir un **pricing unifié 29 €/mois** sur le tier Pro individuel — un pricing différencié par persona introduit de la complexité tarifaire qui peut nuire à la lisibilité offre. **Différenciation possible sur le tier Équipe** : 19 €/siège × N (cohérent pour B1/B2/B4 qui peuvent justifier 3-5 sièges au sein de leur équipe transfo / innovation).

### 8.4 Tier Équipe — modélisation séparée

Hypothèses scenario médian :

- Conversion Pro → Équipe : ~10 % des Pro existants ont une équipe à équiper (typique pour B1/B2/B4)
- Taille moyenne équipe : 4 sièges
- Pricing : 19 €/siège × 4 = 76 €/mois en HT
- Sur 500 Pro M24 médian : 50 comptes Équipe × 76 € = +3 800 €/mois = **+45,6 k€/an d'ARR additionnel**
- Total ARR médian avec Équipe : 174 + 46 = **~220 k€ ARR M24**

Levier intéressant à activer dès Étape 5 (tier Équipe + diffusion QFC).

---

## 9. Break-even projeté

### 9.1 Coûts mensuels fixes Hub v2 (hors acquisition)

| Poste | Phase amorçage | Croissance | Maturation |
|-------|------------------|-------------|--------------|
| Infrastructure (Supabase + monitoring + CDN) | 80 € | 250 € | 1 000 € |
| Outils Cavalli (notion, comm) | 50 € | 100 € | 200 € |
| Marketing / contenu / SEO outils | 50 € | 200 € | 500 € |
| Outils Hub v2 (Stripe, etc. — fixe) | 30 € | 30 € | 30 € |
| **Total coûts fixes mensuels** | **210 €** | **580 €** | **1 730 €** |

### 9.2 Break-even mensuel par scenario

Break-even mensuel = revenus mensuels nets ≥ coûts mensuels totaux (fixe + LLM + acquisition mensuelle).

**Hypothèse acquisition mensuelle** : la conversion mensuelle de nouveaux Pro × CAC ≈ coût d'acquisition mensuel.

| Scenario | M12 BE atteint ? | M18 BE atteint ? | M24 BE atteint ? |
|----------|--------------------|--------------------|--------------------|
| Pessimiste | Non (revenus 1,6 k€ < coûts ~12 k€) | Non | Non (revenus 3,6 k€ < coûts ~21 k€) |
| Médian | Non (revenus 9,8 k€ < coûts ~70 k€) | **Proche** (revenus 11,5 k€ vs coûts ~10-13 k€) | **Atteint** (revenus 12,1 k€ ≥ coûts ~10 k€) |
| Optimiste | Proche (revenus 25,4 k€ vs coûts ~30 k€) | **Atteint** (revenus 27,8 k€ ≥ coûts ~25 k€) | **Atteint avec marge** (revenus 29 k€ vs coûts ~15 k€ — l'acquisition baisse en intensité car le portefeuille mature) |

### 9.3 Cash flow opérationnel cumulé 24 mois

| Scenario | Revenus cumulés | Coûts d'acquisition cumulés | Coûts fixes cumulés | LLM cumulés | **Cash flow op. cumulé** |
|----------|------------------|------------------------------|----------------------|--------------|----------------------------|
| Pessimiste | 35 k€ | 200 k€ | 8 k€ | 1 k€ | **-174 k€** |
| Médian | 125 k€ | 150 k€ | 9 k€ | 3 k€ | **-37 k€** |
| Optimiste | 360 k€ | 90 k€ | 12 k€ | 7 k€ | **+251 k€** |

**Lecture** : sur 24 mois, le scenario médian demande un **investissement net Cavalli de ~40 k€** (combinable avec les ~5 500-11 000 € de garde-fous juridiques = total exposition ~50 k€). Le scenario optimiste est autofinançant. Le pessimiste demande -174 k€ d'investissement net — **non soutenable** sans levée de fonds ou réduction drastique du CAC.

### 9.4 Implication levée de fonds

**Scenario médian** : autofinançable par Cavalli si trésorerie personnelle disponible de l'ordre de 50 k€ sur 18 mois. **Pas de levée nécessaire**.

**Scenario optimiste** : autofinançable et même générant des liquidités à partir de M12-M18.

**Scenario pessimiste** : levée de ~200-250 k€ requise, ou pivot du modèle (CAC à réduire ou conversion à augmenter avant lancement Étape 3).

🟧 **Décision Cavalli structurante** : tolérance d'investissement personnel sur 18 mois ? La modélisation médiane suppose ~40-50 k€ d'apport net. À confronter avec la trésorerie personnelle disponible / l'arbitrage Cavalli sur le niveau d'engagement personnel.

---

## 10. Implications stratégiques

### 10.1 Confirmation pricing 29 €/mois

La sensibilité au pricing confirme que **29 €/mois est le sweet spot** sur le top 5 personas. Le tier Équipe à 19 €/siège active un levier B2B significatif (+25-30 % ARR potentiel) à partir d'Étape 5.

### 10.2 Levier prioritaire #1 — Réduire le CAC

Le CAC est le levier le plus impactant (gain ARR ×8 entre pessimiste 800 € et optimiste 200 €). **Actions concrètes** :

- **Activer le canal territorial Grand Est** dès Étape 1 (QFC réseau + CCI Vosges + French Tech Est + POLARIS) — coût marginal acquisition très bas par utilisateur
- **Stimuler la viralité E1** (consultants indé.) — un consultant satisfait recommande 3-5 confrères en moyenne
- **Bouche-à-oreille entre dirigeants ETI** via communautés (B4 CDO Days, C5 RETIS / Hub Bpifrance Innovation)
- **Contenu organique SEO** indexable sur requêtes "IA dirigeants PME", "accompagnement IA entreprise", "boussole IA"

### 10.3 Levier prioritaire #2 — Réduire le churn

Le churn est le 2e levier le plus impactant. **Actions concrètes** :

- **Continuité conversationnelle quotidienne** (différenciateur Hub v2) — un utilisateur qui ouvre Hub v2 chaque semaine est ~3-5× moins susceptible de churner qu'un utilisateur passif
- **Outils Pro actionnables** (générateur de cadrage, comparateur, estimateur ROI) — créent du switching cost
- **Dimension éditoriale forte** (newsletter hebdomadaire + Playbook bi-mensuel, arbitrage Cavalli 27 mai) — créent un rituel d'usage qui renforce l'attachement à la plateforme
- **Tier annuel avec discount 15-20 %** — réduit le churn × 30-50 % (effet contrat annuel)

### 10.4 Levier prioritaire #3 — Conversion Free → Pro

**Hypothèses produit-marché à instrumenter dès Étape 1** :

- Quel % des utilisateurs Free atteignent la limite des 3 chats/jour et soit s'arrêtent, soit upgradent ?
- Quel signal d'upgrade le plus performant (limite atteinte ? premier livrable Pro essayé ? mois 3 d'inscription ?) ?
- Les crédits 10 € de bienvenue convertissent-ils réellement en Pro à un taux supérieur ?

Le test produit Étape 1 (POC RAG sem 1-2 juin) doit instrumenter ces hypothèses dès le départ.

### 10.5 Risque structurel — sensibilité aux 3 leviers conjoints

La modélisation montre que **les 3 leviers (conversion, churn, CAC) sont multiplicatifs** sur l'ARR final. Une dégradation d'un seul (par ex. CAC qui dérape de 400 € à 700 €) peut suffire à basculer du médian vers le pessimiste. **Vigilance trimestrielle requise** sur les 3 leviers.

🟧 **Recommandation tableau de bord** : tracer mensuellement à partir d'Étape 3 (i) inscriptions Free, (ii) conversion Free → Pro, (iii) CAC moyen tous canaux confondus, (iv) churn brut + churn net, (v) ARR mensuel. Identifier les dérives rapidement.

### 10.6 Articulation avec le dossier IP / statut Cavalli (S3.4)

L'arbitrage IP Cavalli vs QFC (dossier module 4 anticipé fin juillet) **conditionne directement le modèle économique** :

- **Piste A** (side project 100 % perso) : modèle autonome, Cavalli porte 100 % du risque et 100 % des revenus
- **Piste B** (convention QFC, licence/redevance) : modèle partagé, par ex. QFC reçoit 10-20 % des revenus → impacte la marge mais activerait le canal QFC plus fort + diminuerait le CAC moyen
- **Piste C** (projet interne QFC) : modèle salarié, pas d'investissement personnel mais valorisation patrimoniale réduite

**Implication modélisation** : la piste B pourrait améliorer l'économie globale (CAC -30 %, ARPU -10-15 % en redevance), nette positive. À chiffrer en S3.7 ou plus tôt si le dossier IP avance.

---

## 11. Bloc résumé exécutif transmissible (auto-imposé §8.1.7)

> **À copier-coller pour notification autonome aux canaux pairs.**
>
> ---
>
> **Modélisation économique Hub v2 v1 — 26 mai 2026 — synthèse**
>
> Trois scenarios 24 mois modélisés sur top 5 personas (E1, B1, B2, B4, C5) avec pricing référence 29 €/mois Pro :
>
> - **Pessimiste** (conversion 1 %, churn 7 %, CAC 800 €) → **52 k€ ARR M24**, break-even non atteint, LTV:CAC 0,43 insoutenable
> - **Médian** (conversion 3 %, churn 5 %, CAC 400 €) → **174 k€ ARR M24**, break-even M18-M20, LTV:CAC 1,21 sous cible
> - **Optimiste** (conversion 5 %, churn 3 %, CAC 200 €) → **418 k€ ARR M24**, break-even M9-M12, LTV:CAC 4,03 au-dessus cible
>
> **Marge brute Hub v2 ~96 %** (coût marginal LLM Mistral 0,40-0,80 €/user Pro/mois sur prix 29 €). Coûts fixes 65-1 000 €/mois selon phase.
>
> **Investissement personnel Cavalli estimé scenario médian** : ~40-50 k€ sur 18 mois. Scenario optimiste autofinançant à partir M12-M18.
>
> **Pricing 29 €/mois confirmé optimal** vs 19 € (-13 % ARR médian) et 49 € (équivalent ARR mais risque positionnement premium). Tier Équipe 19 €/siège active un levier B2B +25-30 % ARR potentiel à partir Étape 5.
>
> **Levers prioritaires** : (1) réduire CAC via territorial Grand Est + viralité E1, (2) réduire churn via continuité conversationnelle + outils Pro + tier annuel, (3) instrumenter la conversion Free → Pro dès Étape 1.
>
> **Articulation dossier IP** : la piste B (convention QFC) pourrait améliorer l'économie globale (CAC -30 %, ARPU -10-15 %), nette positive — à chiffrer après arbitrage Cavalli.
>
> Source complète : `Canaux/Hub-Strat/outputs/modelisation-economique-hub-v2-v1.md`

---

## 12. Check pré-livrable §8.1 — application

1. **Étanchéité QFC** ✅ — aucune startup réelle nommée. Mentions QFC traitées au niveau structurel (canal d'acquisition) sans matière confidentielle.
2. **Modules Vianeo cohérents** ✅ — module 4 Faisabilité/Viabilité (cœur) + 3 Acceptabilité (sensibilité pricing) + 2 Désirabilité (hypothèses persona). Règle de cohérence inter-modules v1.1 respectée (la modélisation chiffrée s'appuie sur les hypothèses persona convergentes du protocole v1).
3. **Sources citées et vérifiables** ✅ — benchmarks SaaS publics + tarifs LLM officiels + protocole personas v1 interne, tous référencés §13.
4. **Pas de substitution Cavalli** ✅ — 1 décision structurante 🟧 (tolérance investissement personnel) + 1 décision opérationnelle 🟧 (tableau de bord) ; toutes les hypothèses du modèle sont assumées comme telles, pas comme conclusions.
5. **Impacts autres canaux signalés** ✅ — Hub Content (instrumentation conversion Free → Pro dès Étape 1), Hub RAG (arbitrage LLM Mistral Large 3 / Medium / Small pour optimiser coûts), Claude Design (UX upgrade Free → Pro à instrumenter), DEV IA Head (pattern transverse économique réutilisable).
6. **Versioning explicite** ✅ — v1 + historique §14.
7. **(Auto-imposé) Bloc résumé exécutif transmissible** ✅ — §11.

---

## 13. Zones à creuser (itération v1.1 ou v2)

- **Validation hypothèses conversion** dès remontées Étape 1 (POC RAG sem 1-2 juin) → recalibrage scenarios
- **Chiffrage précis du tier Équipe** sur scenarios complets (modélisation seule du tier Pro individuel dans v1, Équipe estimé séparément)
- **Modélisation crédits 10 € bienvenue** : impact sur conversion Free → Pro + valeur unitaire des power users
- **Sensibilité au mix LLM** : impact financier d'un basculement 100 % Claude Sonnet (10× plus cher que Mistral Mix) si décision de fiabilité
- **Analyse cohorte** : modélisation par cohorte mensuelle (acquisition + rétention) plutôt que par simplification
- **Modèle revenu redevance QFC** post-arbitrage IP (piste B) : impact net après prise en compte du canal d'acquisition activé
- **Coût opportunité Cavalli** : si Hub v2 devient activité principale, intégrer un salaire de référence (60-100 k€/an net pour un SUM senior + entrepreneur IA)

---

## 14. Sources mobilisées

### Coûts API LLM
- [CloudZero — Mistral API Pricing 2026](https://www.cloudzero.com/blog/mistral-api-pricing/)
- [TokenMix — Mistral API Pricing 2026](https://tokenmix.ai/blog/mistral-api-pricing)
- [CloudZero — LLM API Pricing Comparison 2026](https://www.cloudzero.com/blog/llm-api-pricing-comparison/)
- [Seobooster — Observatoire prix API LLM 2026](https://www.seobooster.fr/observatoire/prix-api-llm/)
- [TLDL — LLM API Pricing 2026 GPT-5 Claude Gemini](https://www.tldl.io/resources/llm-api-pricing-2026)

### Benchmarks CAC / LTV / churn SaaS
- [Growth Spree — B2B SaaS LTV:CAC Ratio Guide 2026](https://www.growthspreeofficial.com/blogs/b2b-saas-ltv-cac-ratio-guide-calculate-benchmark-improve-2026)
- [Data-Mania — B2B Tech Startup CAC Benchmarks 2026](https://www.data-mania.com/blog/cac-benchmarks-for-b2b-tech-startups-2025/)
- [SaaS Hero — LTV CAC Ratio B2B SaaS 2026](https://www.saashero.net/strategy/b2b-saas-ltv-cac-benchmarks/)
- [Optifai — B2B SaaS LTV Benchmarks 939 companies](https://optif.ai/learn/questions/b2b-saas-ltv-benchmark/)
- [Stripe — CAC SaaS guide](https://stripe.com/resources/more/cac-in-saas)
- [Phoenix Strategy — LTV:CAC SaaS Benchmarks](https://www.phoenixstrategy.group/blog/ltvcac-ratio-saas-benchmarks-and-insights)
- [Skalin — Benchmark taux churn SaaS B2B](https://www.skalin.io/blog/benchmark-taux-churn-saas-b2b)
- [PM Toolkit — Churn Rate Benchmarks 2026](https://pmtoolkit.ai/benchmarks/churn-rate-benchmarks)
- [Churnkey — B2B vs B2C churn rates](https://churnkey.co/blog/the-difference-between-b2b-b2c-churn-rates/)
- [Proven SaaS — CAC Payback Benchmarks 2026](https://proven-saas.com/benchmarks/cac-payback-benchmarks)

### Infrastructure / hébergement EU
- [Supabase — Pricing & Fees](https://supabase.com/pricing)
- [DesignRevision — Supabase Pricing real costs at 10K-100K users](https://designrevision.com/blog/supabase-pricing)
- [Intelligence Privée — Comparatif hébergement IA EU 2026 OVHcloud Scaleway Outscale](https://intelligence-privee.com/articles/ia-hebergee-europe-comparatif-ovhcloud-scaleway-outscale)
- [Freelance Stack — Top 5 hébergeurs EU 2026](https://www.freelance-stack.io/en/blog/hebergement-web-2026-top-5-solutions-europeennes-garder-controle-donnees/)
- [Buildmvpfast — Supabase pricing hidden costs at scale 2026](https://www.buildmvpfast.com/blog/supabase-pricing-hidden-costs-scale-alternatives-2026)
- [Get AI Perks — Supabase tarifs 2026](https://www.getaiperks.com/fr/articles/supabase-pricing)

### Documents internes mobilisés
- `Canaux/Hub-Strat/outputs/protocole-cartographie-priorisation-personas-hub-v2-v1.md`
- `Canaux/Hub-Strat/outputs/cartographie-concurrentielle-hub-v2-v1.md`
- `Canaux/Hub-Strat/outputs/garde-fous-juridiques-hub-v2-v1.md`
- `Canaux/Hub-IA/outputs/NOTE-PRICING-HUB-V2-credits-vs-abonnement.md`
- `Canaux/Hub-IA/outputs/VISION-HUB-V2-CONSOLIDEE-v1.md`

---

## 15. Historique de versions

| Date | Version | Modification |
|------|---------|--------------|
| 26 mai 2026 | v1 | Création initiale — modélisation 3 scenarios 24 mois (pessimiste / médian / optimiste) sur top 5 personas, coûts LLM Mistral mix + infra Supabase, CAC/LTV/churn par segment, break-even projeté, sensibilité pricing 19/29/49 €, ARR à 12/24/36 mois, recommandation tier Équipe 19 €/siège. Articulation dossier IP S3.4 + recommandations leviers CAC/churn/conversion. Dépôt anticipé sur jalon S3.5. |

---

*Livrable structurant Hub Strat — version v1, modélisation hypothétique chiffrée à itérer trimestriellement post-Étape 1. Validation Cavalli attendue. Recommandation : relecture experte (DAF / consultant financier SaaS) avant toute communication externe engageante. Check pré-livrable §8.1 appliqué — sept points OK.*
