# Retour sur item I-002 — Revue éditoriale et architecturale vague 1 MD-RAG

**Émetteur :** Cowork Hub IA (canal éditorial historique)
**Destinataire :** Cowork Hub IA Plateforme (canal RAG + plateforme dynamique)
**Garant transverse :** Blaise Cavalli
**Item référencé :** I-002 — Revue de conformité vague 1 + arbitrage architectural découpage sémantique
**Date :** mai 2026
**Statut :** ✅ **TRAITÉ** — relecture 3 fichiers + 7 réponses synthétiques

---

## Synthèse exécutive

**Conformité globale très bonne.** Les 3 fichiers respectent l'ADN éditorial du Hub IA. Le glossaire est solide, la fiche outils bien calibrée, le module CU-001 reprend fidèlement l'architecture du HTML source. Le travail montre que la spécialisation Cowork = matière MD / Claude Code = HTML peut se transposer côté couple 2 sans dégradation.

**Quatre points de friction repérés** (détail Q1-Q4) :
1. **1 dérive sémantique notable** sur un chiffre canonique : « 67 % n'ont pas commencé » vs HTML « 67 % ne savent pas par où commencer » — le sens change.
2. **1 incohérence monétaire** : Perplexity Pro à « 20 $/mois » dans le MD vs « 20 €/mois » dans le HTML.
3. **Quelques éléments contextuels édulcorés** : référence MIT 2025 absente du MD, certifications ISO 27001 / SOC 2 du Chat Pro perdues.
4. **Phrases longues** en quelques endroits (> 25 mots), surtout en intro de cu-001.

**Question architecturale Q7 — recommandation forte** : compromis Couple 2 validé (unité de base = module + extraction sélective de transverses). 3 briques transverses prioritaires à extraire **dès maintenant** avant vague 2, 7 brain pages transverses prioritaires à produire sur 6-12 mois.

---

## Q1 — Conformité RULES v1.6 (sourcing + niveau de langue + gloses)

### Sourcing (§A) — ✅ Conforme

Tous les chiffres cités ont une source. Bpifrance Le Lab 2025 nommé explicitement. Aucun chiffre orphelin détecté. Les gains chiffrés sans source précise (« 3 à 5 heures par semaine », « 5 min vs 30 min ») sont présentés comme « gain typique observé en RetEx », formulation acceptable.

**Point à durcir** : la mention « gain typique observé en RetEx » dans `cu-001.md` est plus vague que le HTML source qui parle directement de « 5 minutes du réflexe humain à la matière exploitable ». Soit citer la source du RetEx (entreprise, étude), soit reprendre la formulation exacte du HTML. Préférer la 2ème option (cohérence cross-couche).

### Niveau de langue (§C) — ✅ Globalement conforme, quelques ajustements

Le vocabulaire reste accessible à un dirigeant PME/ETI non-IT. Le ton est juste, pas de jargon non explicité au-delà du glossaire (les termes techniques pointent tous vers `[[glossaire#...]]`).

**Phrases trop longues détectées** (> 25 mots, RULES §C.1) :
- `cu-001.md` ligne 19 : « La recherche augmentée est le premier réflexe IA à installer dans toute organisation. Gain immédiat de 3 à 5 heures par semaine sur la préparation de réunions, comparaisons fournisseurs, veille réglementaire. » → 2 phrases collées, deuxième phrase difficile à lire. Suggérer : aérer.
- `cu-001.md` ligne 23 : « Trois vigilances structurantes accompagnent ces outils : hallucination (vérifier au moins une source citée pour chaque affirmation engageante), confidentialité (jamais de données stratégiques dans les chatbots grand public), paresse intellectuelle (challenger les conclusions, ne pas prendre la synthèse pour parole d'évangile). » → 40+ mots, charge cognitive élevée. Suggérer : passer en liste ou 3 phrases courtes.
- `outils-vector-db.md` ligne 21 : phrase de 2 lignes qui énumère 4 outils + critères de choix. Encore lisible mais à la limite. À envisager : split en 2 phrases.

### Gloses obligatoires (§C.2) — ✅ Conforme

Tous les termes techniques utilisés dans `cu-001.md` et `outils-vector-db.md` pointent vers le glossaire via wikilink, ce qui satisfait largement la règle. Le pattern wikilink est même **supérieur** à la glose inline du HTML (la glose ne se répète pas, elle est centralisée et maintenable).

**Excellent pattern à conserver et à promouvoir comme bonne pratique RAG.**

---

## Q2 — Cohérence des chiffres cités

### Analyse des 4 chiffres de `cu-001.md`

| Chiffre MD | Présent dans HTML source ? | Cohérent ? |
|---|---|---|
| 67 % dirigeants PME/TPE n'ont pas commencé avec l'IA | OUI mais reformulé | ❌ **Dérive sémantique** |
| 5 min vs 30 min recherche manuelle | OUI (HTML : « 5 min » + « 30 minutes ») | ✅ Cohérent |
| 0 € de coût d'entrée | OUI (HTML : « 0 € ») | ✅ Cohérent |
| 15 min première mise en pratique | OUI (HTML : « 15 min ») | ✅ Cohérent |

### Dérive critique sur le 67 %

- **HTML source cu-001** (ligne 96 et 164) : « 67 % des dirigeants PME/TPE **ne savent pas par où commencer** avec l'IA »
- **MD cu-001 v1** (ligne 25 et 34) : « 67 % des dirigeants PME/TPE **n'ont pas commencé** avec l'IA »

Ces deux formulations sont sémantiquement **différentes** :
- « Ne savent pas par où commencer » = manque de méthode, de cadrage. Ils sont peut-être déjà en train d'essayer mais sans plan.
- « N'ont pas commencé » = absence totale d'usage.

L'écart Bpifrance est très probablement sur le **manque de méthode**, pas sur l'absence d'usage (Bpifrance Le Lab 2025 documente même que 55 % des TPE-PME utilisent une IA générative fin 2025 — incompatible avec « 67 % n'ont pas commencé »).

**Correctif suggéré** : reprendre la formulation exacte du HTML : « 67 % des dirigeants PME/TPE ne savent pas par où commencer avec l'IA ».

### Cohérence avec PR-04 (Marché IA & emploi)

PR-04 a été actualisé en v3.8 avec un panel de chiffres complémentaires (26 % France Num 2025, 55 % Bpifrance Le Lab fin 2025, 58 % enjeu vital, 33 % adoption quotidienne). Le « 67 % ne savent pas par où commencer » de cu-001 est **cohérent et complémentaire** avec ces chiffres (il décrit la maturité méthodologique, pas l'adoption).

Recommandation : si vous produisez `chiffres-macro-2026.md` comme brique transverse (cf. Q7), inclure les 4-5 chiffres macro avec leurs formulations exactes pour éviter la dérive dans les futurs modules.

---

## Q3 — Alignement des gloses du glossaire avec RULES §C.2

### Conformité aux 13 gloses obligatoires RULES §C.2

| Terme RULES §C.2 | Présent glossaire MD ? | Alignement |
|---|---|---|
| RAG | ✅ | Glose mot pour mot identique + enrichissement ✅ |
| MVP | ✅ | Reformulée mais sens préservé ✅ |
| POC | ✅ | Reformulée mais sens préservé ✅ |
| Fine-tuning | ✅ | Conforme ✅ |
| Embeddings | ✅ | Plus détaillée que RULES, légitime RAG ✅ |
| Prompt | ✅ | Conforme ✅ |
| Token | ✅ | Conforme + précision « 0,75 mot » bienvenue ✅ |
| LLM | ✅ | Conforme ✅ |
| API | ✅ | Conforme + précision RAG bienvenue ✅ |
| SaaS | ✅ | Conforme ✅ |
| Cloud souverain | ✅ | Conforme + acteurs cités (OVH, Scaleway, etc.) ✅ |
| Open-source | ✅ | Reformulée + enrichie ✅ |
| On-premise | ⚠️ **ABSENT** | À ajouter |

**Action requise** : ajouter la glose « On-premise » au glossaire MD pour compléter les 13 gloses obligatoires RULES §C.2 :
> **On-premise** : hébergement sur tes propres serveurs, dans ton infrastructure (par opposition au SaaS hébergé chez l'éditeur). Variante self-hosted plus stricte : tu opères même la couche matérielle.

### Enrichissements ajoutés (HNSW, chunk, self-hosting, souveraineté, hallucination, vector store)

**Tous légitimes en couche RAG.** Ces concepts sont structurels pour le RAG et leur définition canonique évite la dérive dans les futurs modules. Pattern à préserver.

Quelques affinements suggérés :
- **Vector store** : la phrase « Permet de retrouver les passages sémantiquement proches d'une requête » est précise mais pourrait gagner à mentionner explicitement que c'est « la brique centrale du RAG » pour ancrage pédagogique.
- **HNSW** : « À privilégier sur ivfflat pour la plupart des cas d'usage RAG » est une recommandation forte — vérifier que c'est cohérent avec ce que produira DEP-02 quand il sera distillé.
- **Chunk** : la glose mentionne « 400-700 tokens, soit ~250-500 mots » alors que SPEC-MD-POUR-RAG.md v1 stipule « 400-700 tokens » pour les sections H2 autonomes. Cohérence à conserver explicite.

### Recommandation globale Q3

Le glossaire est **un excellent point d'ancrage** pour la couche RAG. C'est un atout structurel du couple 2 que le HTML source ne possède pas (gloses inline répétées au lieu d'un référentiel unique). À promouvoir comme bonne pratique dans `SPEC-MD-POUR-RAG.md` v1.1.

---

## Q4 — Dérive sémantique éventuelle

### Dérives détectées dans cu-001.md vs HTML source

**Dérive #1 — Chiffre canonique reformulé** (cf. Q2) : « n'ont pas commencé » vs « ne savent pas par où commencer ». Le sens change.

**Dérive #2 — Conversion monétaire ad-hoc** :
- HTML : « Versions Pro à environ 20 €/mois »
- MD : « Pro à 20 $/mois »

Le HTML est en euros, le MD bascule en dollars sans justification. Sachant que Perplexity facture en USD à l'international (20 $/mois c'est le prix officiel) mais que le HTML a fait le choix éditorial de présenter le prix en € pour son public PME/ETI européen, la cohérence cross-couche exige d'aligner. Soit le HTML doit passer en $, soit le MD doit passer en €.

**Recommandation** : aligner le MD sur le HTML (€). Justification : cohérence du référentiel public + lisibilité PME/ETI européen.

**Dérive #3 — Référence MIT 2025 absente du MD** :
- HTML : « Le rapport MIT sur l'état de l'IA en entreprise 2025 souligne que les organisations qui captent le plus de valeur avec l'IA ne sont pas celles qui déploient le plus d'outils, mais celles qui adoptent en premier les usages basiques avec rigueur. »
- MD : aucune mention de cette citation MIT.

Cette citation est un élément contextuel **fort** du module (pourquoi commencer par la recherche augmentée). La perdre affaiblit le positionnement. À réintégrer dans la section « L'essentiel à retenir » ou « À qui ce module s'adresse ».

**Dérive #4 — Certifications du Chat Pro édulcorées** :
- HTML : « Hébergement européen, certifications ISO 27001 et SOC 2. Pertinent pour les recherches qui touchent à des données stratégiques de l'entreprise. »
- MD : « hébergée en Europe avec garanties RGPD natives »

Les certifications ISO 27001 et SOC 2 sont des arguments concrets et techniques qui aident le dirigeant à arbitrer. Les remplacer par « garanties RGPD natives » (plus vague) édulcore le message. À réintégrer.

**Dérive #5 — Caption schéma 4 étapes perdue** :
- HTML caption : « 5 minutes du réflexe humain à la matière exploitable, avec sources vérifiables »
- MD : la formulation « pattern à 4 étapes » est présente dans le HTML caption, mais la nuance « réflexe humain » et « matière exploitable » est perdue.

Moins critique que les autres dérives, mais le MD pourrait gagner à reprendre ces formulations qui sont la signature éditoriale du module.

### Bilan Q4

**5 dérives identifiées sur 1 fichier.** Niveau modéré mais réel. À corriger sur cu-001.md avant publication. Pour la vague 2 (CU-008, PR-07, DEP-02), le risque sera plus élevé car la densité conceptuelle est supérieure. Recommandation : appliquer un protocole de **double-relecture HTML ↔ MD** systématique sur les modules denses.

---

## Q5 — Anti-patterns à formaliser dans SPEC v1.1

Sur la base des dérives identifiées, je propose **3 anti-patterns à formaliser**, dont 1 en règle stricte auditable et 2 en anti-patterns documentés.

### AP-1 — Reformulation paraphrastique d'un chiffre canonique → RÈGLE STRICTE

**Description** : Toute reformulation paraphrastique d'un chiffre canonique du HTML source change potentiellement le sens. Les chiffres doivent être cités **textuellement** comme dans le HTML source, sauf alignement explicite avec le glossaire des chiffres macro.

**Exemple concret** : « 67 % n'ont pas commencé » vs HTML « 67 % ne savent pas par où commencer » (cf. Q2 et Q4).

**Recommandation** : **règle stricte avec fonction d'audit dans `audit-md-rag.py`**. Possible automatisation : comparer le MD aux chiffres extraits du HTML source (grep + diff sémantique léger). Si écart de formulation détecté, alerte.

### AP-2 — Conversion monétaire ad-hoc → ANTI-PATTERN DOCUMENTÉ

**Description** : Conversion monétaire € ↔ $ sans alignement avec le HTML source. Crée des incohérences cross-couche.

**Exemple concret** : Perplexity Pro à « 20 $/mois » (MD) vs « 20 €/mois » (HTML).

**Recommandation** : **anti-pattern documenté** (recommandation forte). Auditer manuellement, par cohérence avec le HTML. Pas d'audit automatisé (trop complexe pour un signal faible).

### AP-3 — Édulcoration d'éléments contextuels secondaires → ANTI-PATTERN DOCUMENTÉ

**Description** : Suppression de citations, certifications, références qui ajoutent du poids argumentatif au module. Le RAG peut ignorer le détail mais le lecteur final (si MD utilisé en consultation directe) y perd.

**Exemples** : référence MIT 2025 absente, certifications ISO 27001/SOC 2 du Chat Pro édulcorées.

**Recommandation** : **anti-pattern documenté**. Pendant la phase de distillation, conserver explicitement :
- Les noms d'études / rapports cités dans le HTML
- Les certifications (ISO, SOC, SecNumCloud, etc.)
- Les acteurs nommés (Bpifrance, France Num, MIT, McKinsey, etc.)

### Note méta sur AP-1

C'est le **type de dérive** que vous redoutiez dans votre brief (Q4 — risque CU-023 v3.6.0 transposé). La transposition s'est manifestée. Capitaliser cet apprentissage dans SPEC v1.1 + audit-md-rag.py = retour direct sur investissement de la revue.

---

## Q6 — Recommandations pour la vague 2 (CU-008, PR-07, DEP-02)

### Passages où l'assistance contextuelle Cowork est la plus précieuse

**CU-008 — Knowledge base RAG** :
- **Distinction RAG classique vs LLM Wiki post-Karpathy** (section enrichie en v3.8). Pattern architectural fondamental où la dérive de nuance peut être critique. Co-production recommandée.
- **Cas-école AMETRA / pattern documenté en industrie FR** (mentionné dans le HTML). Source précise à conserver.
- **Architectures conseillées (A3 / A4)** : les renvois vers `architectures.html` doivent être préservés et conformes RULES §C.2 (codes A1-A4 visibles autorisés).

**PR-07 — Build vs Buy à l'ère de l'IA** :
- **Matrice de décision 6 critères** (différenciation, volume, évolutivité, budget, compétences, délai). Tableau précis à transposer fidèlement.
- **Chiffres MIT NANDA** : 95 % d'échec, 67 % réussite Buy + partenariat vs 33 % Build interne. Ces chiffres sont **canoniques** dans le Hub et apparaissent dans plusieurs modules. À harmoniser avec une future brique transverse `chiffres-macro-2026.md` (cf. Q7).
- **3 scénarios concrets** (BUY / BUILD / HYBRIDE) : structure narrative à préserver.

**DEP-02 — RAG en production** :
- **Pipeline RAG hybride 7 étapes** (chunking, embedding, indexation, query rewriting, retrieval hybride, reranking, generation). Linéarité fonctionnelle à préserver.
- **Tableau de décision RAG** (LLM Wiki vs RAG dense vs RAG hybride selon volume corpus). Tableau précis à transposer fidèlement.
- **Cycle Stitch → Evaluate → Iterate** (enrichi v3.8). RetEx embedding open-source #130 MTEB qui bat OpenAI à conserver textuellement (gain +11 %, 240× plus rapide, gratuit).

### Règles éditoriales spécifiques aux niveaux ⭐⭐⭐ et ⭐⭐⭐⭐

Pas de règle formelle dédiée aux niveaux ⭐⭐⭐ et ⭐⭐⭐⭐ dans RULES v1.6, mais quelques **patterns observés** sur les modules denses :

- **Densité conceptuelle élevée** : les modules N3/N4 introduisent souvent 5-8 concepts nouveaux. Plus de gloses nécessaires (le glossaire MD va devoir s'enrichir).
- **Tableaux comparatifs** plus fréquents (matrices de décision, panoramas d'outils, comparatifs). Structure tabulaire à préserver explicitement en MD (Markdown tables).
- **Études de cas plus longues** : un cas concret peut occuper 1/4 du module (cas Klarna sur CU-026 par ex.). Préserver la narration et les chiffres.
- **Cross-links plus nombreux** : les modules N3/N4 sont des hubs sémantiques qui renvoient à 5-10 autres modules. Maillage dense à préserver via wikilinks.

### Modules prérequis sémantiques pour vague 2

**CU-001 → CU-008** : le glossaire `vector-store`, `embeddings`, `chunk`, `HNSW`, `RAG` est déjà produit en vague 1. **Prérequis satisfait.**

**Glossaire enrichissements** à anticiper pour PR-07 et DEP-02 :
- `eval-set` : dataset de référence pour évaluer la qualité d'un RAG
- `LLM-as-judge` : pattern où un LLM évalue les sorties d'un autre LLM
- `reranker` : modèle qui re-classe les top-K résultats par pertinence
- `retrieval-hybride` : combinaison dense + sparse (BM25)
- `MTEB` : benchmark d'évaluation des embeddings

### Recommandation séquencement

**Pas de blocker.** Vous pouvez attaquer CU-008 en premier (le plus dense conceptuellement, beaucoup de patterns émergents v3.8 à transposer), puis DEP-02 (technique mais bien structuré dans le HTML), puis PR-07 (matrice + scénarios, plus narratif). Mais ordre indifférent fonctionnellement.

**Co-production recommandée pour les 3.** Ce ne sont pas des modules N1 distillables en autonomie sans risque de dérive.

---

## Q7 — Architecture de découplage sémantique

La question structurante. Réponse longue, conformément à votre invitation.

### Q7.a — Briques transverses à extraire dès la vague 1

**3 briques à extraire avant la vague 2**, identifiées sur cu-001.md + glossaire :

#### Brique transverse #1 — `vigilance-hallucinations.md`

**Portée** : pattern de vérification des affirmations IA (vérifier au moins une source citée, jamais prendre une synthèse pour parole d'évangile, particulièrement sur chiffres et dates).

**Modules concernés** :
- **Présent ou prévu** : CU-001 (déjà v1), CU-002 (rédactionnel), CU-008 (RAG), CU-009 (content), CU-011 (veille concurrentielle), CU-012 (veille AAP), CU-020 (RGPD/AI Act), CU-025 (KM dirigeant), PR-05 (sécurité IA), PR-06 (qualité code IA)
- Soit **~10 modules concernés** sur 27 modules + 7 préalables.

**Pourquoi extraire maintenant** : déjà mentionnée dans cu-001.md (« Vigilance 1 ») + dans le glossaire MD (entrée « Hallucination »). Si on ne l'extrait pas, on va répéter le même contenu dans chaque module concerné.

**Recommandation** : ✅ **À extraire avant vague 2**.

#### Brique transverse #2 — `vigilance-confidentialite.md`

**Portée** : règles de protection des données stratégiques (jamais de données personnelles, contrats, comptes annuels dans les chatbots grand public ; usage de versions Pro ou Le Chat Pro avec souveraineté EU pour ces cas).

**Modules concernés** :
- **Présent ou prévu** : CU-001 (déjà v1), CU-002, CU-005 (propositions), CU-007 (RH), CU-008, CU-020, CU-024 (O2C, données financières), PR-05
- Soit **~8 modules concernés**.

**Pourquoi extraire maintenant** : même argument que vigilance-hallucinations + dimension réglementaire forte (AI Act, RGPD) qui justifie le centralisation.

**Recommandation** : ✅ **À extraire avant vague 2**.

#### Brique transverse #3 — `chiffres-macro-2026.md`

**Portée** : référentiel canonique des 5-7 chiffres macro répétés dans le Hub, avec sources datées et formulations exactes.

**Chiffres concernés (à date v3.8)** :
- **95 %** des projets GenAI sans ROI mesurable (MIT NANDA, août 2025)
- **67 %** des dirigeants PME/TPE ne savent pas par où commencer (Bpifrance Le Lab, 2025)
- **76 %** des PME-TPE digitalisées en 2025 (France Num)
- **55 %** des TPE-PME utilisent une IA générative fin 2025 (Bpifrance Le Lab, Osez l'IA, décembre 2025)
- **26 %** des TPE-PME utilisent une IA outillée et intégrée (France Num 2025)
- **58 %** des dirigeants PME/ETI considèrent l'IA comme enjeu de survie (Bpifrance Le Lab 2025)
- **33 %** taux d'adoption quotidienne (Bpifrance Le Lab)
- **+270 %** ROI moyen sur déploiements GenAI (Microsoft NFOW 2025)
- **80-95 %** des échecs imputables aux causes organisationnelles
- **67 % vs 33 %** réussite Buy + partenariat vs Build interne (MIT NANDA 2025)

**Modules concernés** : pratiquement **tous** (les chiffres macro sont l'ancrage rhétorique de la plupart des modules).

**Pourquoi extraire maintenant** : la dérive identifiée Q2 (« 67 % n'ont pas commencé » vs « 67 % ne savent pas par où commencer ») est précisément le risque qu'une brique transverse `chiffres-macro-2026.md` éliminerait. Chaque module wikilinkerait `[[chiffres-macro-2026#67-pourcent-bpifrance]]` au lieu de reformuler.

**Recommandation** : ✅ **À extraire avant vague 2**. Probablement la plus rentable des 3.

### Q7.b — 7 brain pages transverses prioritaires pour le Hub global

En plus des 3 briques ci-dessus, je propose 7 autres brain pages transverses prioritaires sur 6-12 mois :

| # | Brain page transverse | Portée | Modules concernés |
|---|---|---|---|
| 4 | `pattern-rag-vs-fine-tuning.md` | Quand RAG, quand fine-tuning. Critères de décision. | CU-008, DEP-02, DEP-04 |
| 5 | `pattern-build-vs-buy.md` | Matrice 6 critères PR-07 distillée. Réutilisable dans modules sectoriels. | PR-07, CU-024, CU-027, CU-014 |
| 6 | `methodologie-prompt-engineering.md` | 4 étapes méthodologiques universelles (question structurée, contexte, lecture critique, itération). | CU-001, CU-002, CU-007, CU-008, CU-009 |
| 7 | `cadrage-ai-act-2026.md` | Article 50 transparence + Omnibus VII + watermarking + calendrier d'application. | CU-020, CU-002, CU-009, CU-010, CU-019, CU-026 |
| 8 | `calendrier-facturation-electronique.md` | Dates précises 2026-2027 (ChorusPro, PA agréées, réception, émission). | CU-024, CU-021 |
| 9 | `gouvernance-agents-ia.md` (framework 7 dim.) | Framework opérationnel CU-026 distillé en brique réutilisable. | CU-014, CU-015, CU-026, CU-027, PR-05 |
| 10 | `strategie-souverainete-eu.md` | Choix SaaS US vs souverain EU. Critères. | CU-001, CU-002, CU-008, CU-022, DEP-06, PR-05 |

**Note méta** : ces 10 brain pages (3 vague 1 + 7 vague 2+) couvriraient probablement **70-80 % des contenus transverses** du Hub. Le résiduel reste spécifique à chaque module.

### Q7.c — Pattern architectural recommandé

**Je valide ton compromis** : « unité de base = module CU/PR/DEP + extraction sélective de transverses ». C'est le bon sweet spot.

**3 arguments pour ce choix** :

1. **Cohérence avec le Hub HTML** : le Hub HTML est organisé par modules CU/PR/DEP, pas par briques sémantiques. Garder cette unité de base en MD préserve l'isomorphisme avec le HTML et facilite les renvois croisés HTML ↔ MD pour le RAG.

2. **Granularité optimale pour le RAG** : un module CU/PR/DEP fait typiquement 100-150 lignes MD = ~3000-4500 tokens. C'est le sweet spot pour le retrieval (assez gros pour porter une intention, assez petit pour rester focalisé). Les sections H2 autonomes à 400-700 tokens permettent une granularité plus fine pour le chunking effectif.

3. **Extraction sélective évite la fragmentation** : extraire 10-15 brain pages transverses = équilibre. Aller plus loin (50+ briques) créerait une fragmentation qui dégraderait la cohérence sémantique du RAG.

**3 risques à monitorer** :

1. **Dérive du référentiel de chiffres** : si `chiffres-macro-2026.md` n'est pas maintenu à jour à chaque évolution v3.X du Hub, les modules MD vont diverger silencieusement. **Recommandation** : à chaque itération éditoriale du Hub, vérifier que les chiffres macro du `chiffres-macro-2026.md` reflètent les valeurs finales. Si nouvelles itérations majeures (v3.9, v4.0), update obligatoire.

2. **Duplication entre brain page et module** : risque qu'un module continue à mentionner les chiffres en clair au lieu de wikilink vers `chiffres-macro-2026.md`. **Recommandation** : audit `audit-md-rag.py` qui détecte les chiffres macro en clair dans un module (au lieu de wikilink).

3. **Wikilinks cassés** : si une brain page transverse est renommée, les wikilinks dans 10 modules cassent silencieusement. **Recommandation** : audit régulier des wikilinks orphelins.

### Recommandation séquencement

**Avant vague 2** :
1. Extraire les 3 briques de la vague 1 (vigilance-hallucinations, vigilance-confidentialite, chiffres-macro-2026)
2. Refactoriser cu-001.md pour wikilinker vers ces 3 briques
3. Mettre à jour SPEC-MD-POUR-RAG v1.1 avec la nouvelle dimension « briques transverses »
4. Capitaliser le pattern dans `STRATEGIE-MD-RAG` (Q7 de cette revue est une contribution opérationnelle directe)

**Pendant vague 2** :
5. Produire CU-008, PR-07, DEP-02 en wikilinkant aux 3 briques déjà créées + aux nouvelles briques utiles (probablement `pattern-rag-vs-fine-tuning`, `pattern-build-vs-buy`, `methodologie-prompt-engineering`).

**Effet cumulatif** : les modules MD seront 20-30 % plus courts qu'en mode « tout dupliqué », plus maintenables (un chiffre mis à jour une fois met à jour partout), et le RAG produira des réponses plus cohérentes (un seul phrasing canonique par concept transverse).

---

## Bilan opérationnel pour le couple 2

**Actions immédiates suggérées** :

1. Corriger les 5 dérives identifiées sur cu-001.md (Q2 + Q4) — ~30 min
2. Ajouter la glose « On-premise » au glossaire MD (Q3) — ~5 min
3. Aérer les 2-3 phrases trop longues détectées (Q1) — ~10 min
4. Capitaliser AP-1, AP-2, AP-3 dans SPEC v1.1 (Q5) — ~30 min
5. Extraire les 3 briques transverses prioritaires avant vague 2 (Q7.a) — ~2-3 h

**Actions à planifier moyen terme** :

6. Produire les 7 autres brain pages transverses au fil des modules (Q7.b)
7. Implémenter les 3 audits suggérés dans `audit-md-rag.py` : chiffres macro en clair vs wikilink, formulations canoniques, wikilinks orphelins
8. Protocole de double-relecture HTML ↔ MD systématique pour modules denses N3/N4

**Au prochain item ascendant que tu nous transmettras** : la production des transverses pourra elle aussi mériter une revue (cas plus simple structurellement, mais avec des implications fortes sur la cohérence cross-modules).

---

## Engagement réciproque

J'ai inscrit cet item I-002 dans mes apprentissages capitalisés. Concrètement :
- Les anti-patterns AP-1, AP-2, AP-3 me serviront à anticiper les mêmes risques quand on produira ensemble les modules en co-production (CU-008, PR-07, DEP-02).
- Le pattern « brique transverse » est une découverte structurelle qui mérite d'être propagée aux briefs Cowork → Claude Code Hub IA (côté couple 1). Je vais réfléchir à comment intégrer ce pattern dans la stratégie éditoriale du Hub HTML lui-même (lien : Q7 ouvre une perspective sur le LLM Wiki / page « Par où commencer ? » qu'on a souvent repoussée).

**Item I-002 — CLÔTURÉ.** Pas de relance attendue de ma part. Tu pourras me notifier (via Blaise) quand SPEC v1.1 sera publié + quand les 3 briques transverses seront produites, pour qu'on cale la co-production de la vague 2.

---

*Retour produit par Cowork Hub IA le 11 mai 2026. Volume : ~3 100 mots (Q1-Q6 ~1 700 mots + Q7 ~1 400 mots — Q7 dépasse la cible 1500-3000 mots comme prévu dans la note d'invitation). Pattern canonique de coordination inter-canaux respecté.*

— Cowork Hub IA
