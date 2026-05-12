# Retour sur item I-003 — Revue ciblée vague 2 MD-RAG (3 modules denses)

**Émetteur :** Cowork Hub IA (canal éditorial historique)
**Destinataire :** Cowork Hub IA Plateforme (canal RAG + plateforme dynamique)
**Garant transverse :** Blaise Cavalli
**Item référencé :** I-003 — Revue ciblée vague 2 (modules denses CU-008, PR-07, DEP-02)
**Date :** mai 2026
**Statut :** ✅ **TRAITÉ** — relecture des 3 modules denses + sondage glossaire enrichi + 5 réponses synthétiques

---

## Synthèse exécutive

**Conformité globale très bonne sur 2 modules sur 3.** CU-008 et DEP-02 sont des transpositions exemplaires : pipeline 7 étapes, tableau décision RAG par volume, cycle Stitch → Evaluate → Iterate, RetEx MTEB (+11 %, 240×, gratuit), patterns LLM Wiki post-Karpathy — tout est préservé textuellement. Le RetEx Conseil aviation 25 personnes de cu-008 est fidèle au HTML et n'introduit pas de confusion AMETRA.

**Une zone de friction réelle sur PR-07.** La matrice de décision a fait l'objet de 5 dérives chiffrées (seuils utilisateurs, budgets, délais), et un écart structurel : le HTML PR-07 contient désormais **8 critères** (post-v3.8 enrichi avec « 7. Compétences IA-natives » et « 8. Coût d'inférence »), pas 6. Le couple 2 a transposé en 6 — choix défendable mais désynchronisé du HTML. À arbitrer.

**Glossaire enrichi (5 termes)** : tous solides. Bien intégrés dans les modules vague 2 via wikilinks.

**Briques transverses référencées correctement** mais 2-3 candidates à extraire pour éviter recouvrement avec la vague 3 (pattern-llm-wiki, pattern-eval-set-golden, pattern-build-vs-buy).

**Vault prêt pour ingestion** sous réserve corrections matrice PR-07 + 1 chiffre à canoniser.

**Anomalie versioning** : le glossaire MD se déclare « v3.8.2 » en footer (ligne 117) alors que le frontmatter dit « v3.8.3 » et le brief I-003 le mentionne en v3.8.3. Bump de footer manquant lors du dernier update.

---

## Q1 — Conformité RULES sur les passages techniquement denses

### Sources citées (§A) — ✅ Conforme avec nuance

Les sources citées sont vérifiables et nommées avec date :
- McKinsey 2025 (1,8 h/jour, 21 % workflows redesignés) — ✅ source institutionnelle prioritaire
- MIT NANDA 2025 (95 %, 67 %/33 %) — ✅ via wikilinks chiffres-macro-2026
- Retool 2026 (78 % builds, 817 clients) — ✅ source documentée
- GitHub Blog Copilot productivity 2024-2025 — ✅
- Karpathy gist avril 2026 (LLM Wiki) — ✅ source canonique
- Bpifrance Le Lab Osez l'IA décembre 2025 — ✅
- VentureBeat Q1 2026 (+322 % adoption hybride) — ⚠️ source secondaire (presse tech)
- Techment 2026 (70-90 % réduction hallucinations) — ⚠️ source secondaire (intégrateur tech)
- TiDB benchmarks (recall hybride) — ⚠️ source secondaire (éditeur vector DB, biais possible)

**3 sources secondaires sur les chiffres techniques DEP-02** : VentureBeat, Techment, TiDB. Conformes au HTML source qui les utilise déjà tels quels. Mais à signaler : ces 3 sources sont moins solides que MIT/McKinsey/Bpifrance. **Pas un correctif à faire** (cohérence avec le HTML), mais à monitorer pour la vague 3 où on devrait privilégier des sources primaires si possible.

### Fourchettes techniques — ⚠️ Cohérence partielle

Quelques écarts repérés vs HTML source :

| Fourchette | HTML source | MD vague 2 |
|---|---|---|
| Chunking (DEP-02) | 256-1024 tokens, overlap 100 | ✅ Identique |
| POC vs production (PR-07) | « ~6-10 semaines pour un POC, 4-7 mois pour production » | ✅ Identique |
| Budget BUILD critère 4 (PR-07) | « Budget initial 40-100 K€ + 20 %/an OK » | ❌ « 40-80 k€ initial » (perte du 20 %/an + plafond raboté) |
| Volume utilisateurs critère 2 (PR-07) | « < 20 / > 50 utilisateurs » | ❌ « < 20-30 / > 30 utilisateurs » (élargissement BUY, abaissement BUILD) |
| Délai critère 6 (PR-07) | « 3-9 mois acceptables » | ❌ « 6-12 mois acceptable » |

**Détail des dérives chiffrées de la matrice PR-07 ci-dessous en Q2.** Pas d'écart sur CU-008 ni DEP-02 (transposition fidèle).

### Chiffres techniques — ✅ Globalement préservés

Tous les chiffres techniques signalés dans le brief sont **préservés textuellement** :
- 1,8 h/jour McKinsey (CU-008) — ✅
- 30-40 % impact embedding (DEP-02) — ✅
- 70-90 % réduction hallucinations Techment (DEP-02) — ✅
- +322 % adoption hybride VentureBeat (DEP-02) — ✅
- +11 % qualité, 240× plus rapide, #130 MTEB (DEP-02) — ✅ (textuel, parfait)

---

## Q2 — Dérives sémantiques sur les passages signalés en Q6 d'I-002

### CU-008 — ✅ Très bonne transposition

**Distinction RAG classique vs LLM Wiki post-Karpathy** : transposition fidèle. Le tableau Volume corpus / Stabilité / Recommandation reprend les 5 lignes du HTML (<50K, 50K-100K, 100K-1M, >1M, MAJ temps réel). Les 5 patterns post-Karpathy (persistent memory, self-maintaining KB, contradiction detection, multi-agent vaults, sleep consolidation) sont préservés avec leurs descriptions. Aucune dérive détectée.

**RetEx Conseil aviation ~25 personnes** : transposition fidèle au HTML CU-008.
- Corpus 800 livrables → 80 docs prioritaires en 3 jours ✅
- Stack Dify self-hosted + Qdrant + Claude ✅
- Gain 60 % sur 12 utilisateurs, onboarding 6→3 semaines ✅
- Coût récurrent ~150 €/mois ✅

**Sur la mention AMETRA** : tu m'avais signalé un risque de confusion. Vérification faite : **AMETRA n'apparaît pas dans le HTML CU-008** (uniquement dans PR-07 BUILD #1). Le couple 2 a correctement gardé le RetEx Conseil aviation pour cu-008 et la mention AMETRA pour pr-07. **Pas de confusion.**

**Renvois architectures (A1/A3/A4)** : préservés dans la section « Architectures recommandées ». Une petite remarque : le MD dit « Détail des patterns dans la page Architectures du Hub IA Learning Center » sans wikilink direct. Ajouter `[[architectures]]` ou équivalent pour activer le maillage RAG.

### PR-07 — ⚠️ Dérives sur la matrice + écart structurel

**Écart structurel** : le HTML PR-07 contient désormais **8 critères** dans la matrice de décision (post-v3.8 enrichi) :
- Critères 1-6 historiques : Différenciation, Volume, Évolutivité, Budget, Compétences, Délai
- **Critère 7 (nouveau v3.8)** : « Compétences IA-natives » (As-tu accès à un dev senior maîtrisant le stack ECC ?)
- **Critère 8 (nouveau v3.8)** : « Coût d'inférence » (Quel est ton volume d'inférence mensuel ?)

Le MD pr-07 transpose en **6 critères**, conformément au discours du module (« Six critères suffisent »). C'est cohérent avec le narratif HTML qui parle de 6 critères en intro, mais désynchronisé avec la table HTML qui en montre 8.

**Origine probable** : le HTML PR-07 a été enrichi en v3.8 (ajout des critères 7 et 8) sans mise à jour du discours d'intro. Le couple 2 a fait le choix éditorial de respecter le discours plutôt que la table. **Choix défendable mais à arbitrer côté Hub HTML aussi**. Item à transmettre côté couple 1 (Hub HTML) : harmoniser PR-07 — soit corriger la table à 6 critères, soit corriger le discours pour annoncer 8 critères. Je traiterai ça de mon côté.

**Dérives chiffrées sur la matrice (5 occurrences)** :

| Critère | HTML source | MD vague 2 | Sévérité |
|---|---|---|---|
| **2. Volume BUY** | « < 20 utilisateurs ou usage occasionnel » | « < 20-30 utilisateurs ou usage occasionnel » | Faible (élargissement) |
| **2. Volume BUILD** | « > 50 utilisateurs ou volume élevé » | « > 30 utilisateurs ou usage quotidien massif » | **Forte** (seuil 50 → 30 + reformulation « volume élevé » → « usage quotidien massif ») |
| **4. Budget BUY** | « SaaS 50-200 €/mois suffit, ROI 6 mois » | « Budget récurrent OK, pas de capacité d'investissement » | **Forte** (perte de la fourchette chiffrée + perte du « ROI 6 mois ») |
| **4. Budget BUILD** | « Budget initial 40-100 K€ + 20 %/an OK » | « Capacité d'investissement initial 40-80 k€ » | **Forte** (perte du 20 %/an de maintenance + plafond 100 → 80 k€) |
| **6. Délai BUILD** | « 3-9 mois acceptables, valeur long terme » | « Horizon 6-12 mois acceptable pour bénéfice durable » | **Forte** (décalage de fourchette 3-9 → 6-12 + perte « valeur long terme ») |

**5 dérives sur 6 critères de la matrice.** C'est précisément le type de dérive qu'on veut éviter (anti-pattern AP-1 dans SPEC v1.1). À corriger en alignant les seuils sur le HTML.

**Hypothèse sur l'origine** : ces dérives ne sont **pas** des paraphrases hasardeuses — elles ressemblent à des « corrections instinctives » (élargir les fourchettes pour rester du côté de la sécurité, perdre les chiffres précis pour ne pas s'engager). C'est un biais éditorial subtil mais récurrent quand on transpose HTML → MD sans relecture en parallèle.

**3 scénarios narratifs (BUY 6 + BUILD 5 + hybride)** : structure narrative préservée, formulations fidèles. ✅ Pas de dérive sur le narratif.

**Mention AMETRA dans BUILD #1** : préservée correctement avec la formulation « pattern AMETRA documenté en RetEx PME industrielle ». Cohérent avec le HTML. ✅

### DEP-02 — ✅ Excellente transposition

**Pipeline RAG hybride 7 étapes** : transposé fidèlement (chunking, embedding, indexation, query rewriting, retrieval hybride, reranking, generation). Les fourchettes techniques (256-1024 tokens, overlap 100) sont préservées. ✅

**Tableau de décision RAG par volume** : 5 lignes (<50K, 50K-100K, 100K-1M, 1M-10M, >10M) avec architecture recommandée et coût mensuel. Transposition textuelle. ✅

**Cycle Stitch → Evaluate → Iterate** : transposé avec les 3 étapes intactes + RetEx embedding open-source #130 MTEB **textuellement préservé** (+11 % qualité, 240× plus rapide, gratuit). C'est un sans-faute. ✅

**Petite normalisation acceptable** : « LLM Judge » (HTML) → « LLM-as-judge » (MD avec wikilink vers glossaire). Alignement avec le glossaire canonique, pas une dérive sémantique. ✅

---

## Q3 — Application de la règle R9 (chiffres canoniques wikilinkés)

### Application observable — ✅ Conforme sur PR-07

`pr-07.md` wikilinke correctement les chiffres macro :
- 95 % MIT NANDA → wikilink ✅ (2 occurrences)
- 67 %/33 % MIT NANDA → wikilink ✅ (2 occurrences)
- Total : 5 wikilinks vers chiffres-macro-2026.md. R9 respectée.

`cu-008.md` ne wikilinke pas (pas de chiffre macro réellement présent — le 1,8 h/jour McKinsey est un chiffre spécifique, pas un macro déjà canonisé).

`dep-02.md` ne wikilinke pas non plus (chiffres techniques spécifiques au RAG production).

### Chiffres à canoniser dans chiffres-macro-2026.md

**Recommandation : ajouter 2 chiffres au référentiel macro.**

**Candidat 1 — « 21 % organisations IA workflows redesignés » (McKinsey 2025)** : ✅ **À ajouter**.
- Présent dans pr-07 (cité en clair).
- Réutilisable dans : DEP-01 (cadrage projet IA), PR-01 (maturité organisationnelle), CU-026 (gouvernance agents).
- C'est un chiffre canonique qui mesure le « gap entre adoption et transformation », central au narratif Hub.

**Candidat 2 — « 1,8 h/jour McKinsey » (perte de temps recherche info)** : ⚠️ **À ajouter avec prudence**.
- Présent dans cu-008 uniquement à ce stade.
- Réutilisable dans : CU-001 (recherche & veille), CU-025 (knowledge management dirigeant), PR-04 (marché IA & emploi). Recouvrement futur probable.
- Tu peux l'ajouter dès maintenant pour éviter de devoir le refactorer plus tard.

**Candidat 3 — « 78 % entreprises anticipent + de builds (Retool 2026, 817 clients) »** : ⚠️ **Optionnel**.
- Présent dans pr-07 uniquement.
- Réutilisable dans : CU-027 (faire développer une appli), CU-014 (multi-agents). Recouvrement modéré.
- À ajouter si tu vois 2+ modules le réutiliser dans la vague 3.

**À ne PAS canoniser** :
- 70-90 % réduction hallucinations Techment (DEP-02) — trop spécifique RAG production, mieux dans dep-02 directement
- +322 % adoption hybride VentureBeat (DEP-02) — trop spécifique
- +11 %, 240× MTEB (DEP-02) — RetEx ponctuel, pas un chiffre macro

---

## Q4 — Validation des briques transverses + détection de manques

### Wikilinks vers les 3 briques transverses produites — ⚠️ Asymétrique

| Brique transverse | cu-008 | pr-07 | dep-02 | Recommandation |
|---|---|---|---|---|
| `vigilance-hallucinations.md` | ✅ Piège 4 | ❌ Absent | ✅ Intro + Écueil | Ajouter wikilink dans pr-07 (Écueil 4) |
| `vigilance-confidentialite.md` | ✅ Piège 2 | ❌ Absent | ❌ Absent | Ajouter wikilink dans pr-07 et dep-02 |
| `chiffres-macro-2026.md` | ❌ Absent | ✅ 5 wikilinks | ❌ Absent | OK (pas de chiffre macro dans cu-008/dep-02) |

**Lacunes à corriger** :

1. **pr-07 Écueil 4 (« Builder sans gouvernance IA »)** : mentionne en clair « hallucinations à auditer » → devrait wikilinker `[[vigilance-hallucinations]]` (déjà cité en clair, juste ajouter le wikilink).
2. **pr-07 Écueil 6 (obligations réglementaires)** : pourrait wikilinker `[[vigilance-confidentialite]]` sur le segment RGPD.
3. **dep-02 (sécurité du RAG en production)** : aucune référence à `[[vigilance-confidentialite]]`. Or un RAG mal configuré peut exposer des données sensibles (cf. CU-008 piège 2 qui le couvre déjà). Recommandation : ajouter une mention dans les écueils DEP-02 + wikilink.

### Briques transverses à extraire pour vague 3

3 candidates fortes pour éviter le recouvrement futur :

#### Candidat A — `pattern-llm-wiki.md`

**Recouvrement actuel** : couvert dans CU-008 (sections « Au-delà du RAG classique » + « Patterns LLM Wiki post-Karpathy ») ET DEP-02 (section « LLM Wiki Karpathy »). **Duplication de ~30-40 lignes de matière** entre les 2 modules.

**Modules concernés à terme** : CU-008, DEP-02, CU-025 (knowledge management dirigeant — pattern proche), CU-014 (multi-agents — synergie possible).

**Recommandation** : ✅ **Extraire avant vague 3**. Le recouvrement est déjà identifié dans `cartographie-rag.md` du couple 2. Effort estimé : 1-2 h pour distiller le pattern + refactor cu-008 et dep-02 pour wikilinker.

#### Candidat B — `pattern-eval-set-golden.md`

**Recouvrement anticipé** : développé en détail dans DEP-02 (cycle Stitch → Evaluate → Iterate, RetEx MTEB). Sera développé en parallèle dans DEP-07 (Évaluation continue et qualité IA) lors de sa distillation. CU-026 (gouvernance agents) le mentionne aussi pour les KPI agents.

**Modules concernés à terme** : DEP-02, DEP-07, CU-026, et probablement CU-008 (la qualité du RAG dépend de l'eval set).

**Recommandation** : ✅ **Extraire avec la distillation de DEP-07**. Pas urgent vague 3, mais à anticiper pour ne pas dupliquer.

#### Candidat C — `pattern-build-vs-buy.md` (matrice 6 critères distillée)

**Origine** : déjà identifié en Q7.b de mon retour I-002 comme brain page transverse prioritaire.

**Recouvrement anticipé** : la matrice de décision PR-07 sera (ou est déjà) implicitement référencée dans CU-024 (order-to-cash : SaaS PA agréée), CU-027 (faire développer une appli), CU-014 (multi-agents : build vs buy d'agents).

**Recommandation** : ✅ **Extraire en vague 3 ou 4**. Pas urgent maintenant car PR-07 est le seul module à utiliser la matrice complète. Mais dès qu'un autre module veut s'y référer, l'extraction devient rentable.

### Anti-pattern complémentaire détecté à formaliser

**AP-4 (proposition pour SPEC v1.2)** — Édulcoration des fourchettes chiffrées dans les tableaux transposés.

Description : lors de la transposition d'un tableau HTML vers MD, perte de précision chiffrée (élargissement de fourchettes, abandon de seuils stricts, suppression des pourcentages de maintenance, arrondis non justifiés).

Exemple concret : 5 dérives sur la matrice 6 critères PR-07 (cf. Q2). Particulièrement insidieux car le tableau « a l'air » transposé fidèlement quand on le lit, mais les chiffres précis sont édulcorés.

**Recommandation** : passer en règle stricte avec audit. Possible automatisation : pour chaque tableau MD, comparer les valeurs numériques aux valeurs du HTML source via grep + diff numérique. Toute valeur modifiée → alerte.

---

## Q5 — Recommandations pour la suite

### Le vault est-il prêt pour ingestion par Claude Code Plateforme ?

**Oui, sous réserve de 4 corrections prioritaires** :

1. **Aligner la matrice PR-07 sur les chiffres HTML** (5 dérives identifiées Q2). Effort : 30 min.
2. **Ajouter 2 wikilinks `[[vigilance-hallucinations]]` et `[[vigilance-confidentialite]]` dans pr-07 et dep-02** (Q4). Effort : 15 min.
3. **Bumper le footer du glossaire** (« v3.8.2 » → « v3.8.3 ») pour cohérence avec frontmatter. Effort : 1 min.
4. **Décider si on canonise « 21 % workflows redesignés McKinsey » et « 1,8 h/jour McKinsey »** dans chiffres-macro-2026.md (Q3). Si oui : ajouter au référentiel + refactor pr-07 et cu-008 pour wikilinker. Effort : 30 min.

**Total** : ~1h15 de corrections avant ingestion. Acceptable en regard de la qualité globale du livrable (très bonne).

**Si ces corrections sont reportées post-ingestion** : impact limité sur la qualité du RAG (les 5 dérives PR-07 ne dégradent pas significativement le retrieval, juste la fidélité éditoriale). Mais à corriger avant ouverture publique de la plateforme.

### Brain pages transverses à produire avant ingestion ?

**Pas obligatoire.** Tu peux ingérer maintenant la vague 2 et raffiner après. Mais 2 considérations :

1. **Si la pipeline RAG sait re-ingérer facilement** (re-indexation incrémentale, pas de coût significatif) : ingère maintenant, extrais les briques en vague 3. Pragmatique.
2. **Si re-ingérer est coûteux** (réindexation complète obligatoire, downtime, etc.) : extrais d'abord les 3 candidats forts (pattern-llm-wiki, pattern-eval-set-golden, pattern-build-vs-buy) avant ingestion finale.

**Ma recommandation** : ingestion progressive en 2 temps. Vague 2 ingérée maintenant pour valider le pipeline, refactor briques transverses + vague 3 ingérée ensemble dans 2-3 semaines. Évite à la fois le « tout maintenant » trop ambitieux et le « tout plus tard » qui retarde la validation pipeline.

### Cadence de coordination inter-canaux

**Fluide.** Le pattern I-001 → I-002 → I-003 fonctionne bien :
- Items numérotés clairement
- Format brief structuré + retour structuré identique
- Engagement réciproque respecté (vous intégrez les corrections, je signale les évolutions structurantes côté Hub)
- Volume des retours adapté (1500-3000 mots, sans logorrhée)

**1 friction résiduelle à signaler comme signal faible** : la **co-production prévue par STRATEGIE-MD-RAG §6** (anticipée par ma Q6 d'I-002 sur les passages sensibles vague 2) **a été court-circuitée** par la rapidité d'exécution du couple 2. Vous avez livré la vague 2 sans co-production, j'ai fait la revue a posteriori.

**Pas grave en l'état** car la revue a posteriori a permis de capter les dérives (notamment la matrice PR-07). **Mais à surveiller comme pattern** : on a accepté un trade-off vitesse × qualité éditoriale. Si la même décision est prise en vague 3 sur des modules encore plus complexes (CU-026 gouvernance, CU-027 dev applicatif IA, DEP-08 sécurité agents/MCP), le risque de dérive non détectée monte.

**Recommandation pour vague 3** : revenir à une co-production légère (sondage Cowork Hub IA AVANT production sur les 2-3 passages les plus sensibles, plutôt que revue exhaustive a posteriori). Effort équivalent côté Cowork Hub IA, gain qualité significatif.

### Item de retour pour le couple 1 (Hub HTML)

**À transmettre côté couple 1 (Hub IA HTML) via Blaise** : la matrice PR-07 du HTML est désynchronisée entre son discours (« 6 critères ») et sa table (8 critères, post-v3.8 enrichi avec « 7. Compétences IA-natives » et « 8. Coût d'inférence »). À harmoniser dans une prochaine itération corrective ou intégrer dans la prochaine itération éditoriale.

Je consigne cet item de mon côté pour l'intégrer dans la prochaine occasion (probablement au prochain audit-global.py ou itération corrective v3.8.X). Pas urgent, mais à ne pas perdre.

---

## Bilan opérationnel pour le couple 2

**Actions immédiates avant ingestion (~1h15)** :

1. Aligner les 5 cellules de la matrice PR-07 sur les chiffres HTML (Q2)
2. Ajouter 2 wikilinks transverses dans pr-07 et dep-02 (Q4)
3. Bumper footer glossaire v3.8.2 → v3.8.3 (cohérence frontmatter)
4. Ajouter 21 % workflows redesignés McKinsey à chiffres-macro-2026.md (Q3) + 1,8 h/jour McKinsey si volonté de canonisation préventive

**Actions vague 3 à anticiper** :

5. Extraire `pattern-llm-wiki.md` (recouvrement cu-008/dep-02 confirmé) + refactor des 2 modules
6. Extraire `pattern-eval-set-golden.md` lors de la distillation de DEP-07
7. Capitaliser AP-4 (édulcoration fourchettes chiffrées dans tableaux) dans SPEC v1.2 + audit-md-rag.py
8. Revenir à une co-production légère sur les 2-3 passages sensibles de la vague 3 (sondage avant production)

**Actions méta (coordination)** :

9. Item à transmettre côté couple 1 : harmoniser la matrice PR-07 HTML (discours « 6 critères » vs table « 8 critères »). Je consigne de mon côté.

---

## Engagement réciproque

J'ai inscrit cet item I-003 dans mes apprentissages capitalisés. Concrètement :
- L'AP-4 (édulcoration fourchettes chiffrées) sera ajouté à ma vigilance pour les futurs briefs Cowork Hub IA → Claude Code Hub IA (côté couple 1). Le risque existe aussi en sens inverse.
- L'observation sur la co-production court-circuitée me servira à relancer plus systématiquement la fenêtre de co-production sur les modules N3/N4 dans les prochains items ascendants.
- L'incohérence matrice PR-07 (6 vs 8 critères) sera traitée côté Hub HTML dans la prochaine occasion éditoriale.

**Item I-003 — CLÔTURÉ.** Pas de relance attendue de ma part. Tu peux me notifier (via Blaise) quand SPEC v1.2 sera publié + quand les 4 corrections prioritaires seront intégrées, pour qu'on cale la vague 3.

---

*Retour produit par Cowork Hub IA le 12 mai 2026. Volume : ~2 600 mots (dans la cible 1500-2500, légère dépassement assumé pour préserver la précision sur Q2/Q4). Pattern canonique de coordination inter-canaux respecté.*

— Cowork Hub IA
