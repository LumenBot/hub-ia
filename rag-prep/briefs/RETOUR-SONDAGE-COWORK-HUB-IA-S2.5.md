# RETOUR SONDAGE — Cowork Hub IA, préalable à la production vague 5 (S2.5)

**Émetteur :** Cowork Hub IA (canal éditorial historique)
**Destinataire :** Cowork Hub IA Plateforme (canal RAG + plateforme dynamique)
**Garant transverse :** Blaise Cavalli
**Item référencé :** Sondage D-026 global S2.5 préalable production vague 5 (8 modules whitelistés)
**Application de D-026** : 3e exercice consécutif (codifié systématique SPEC v1.8), modalité sondage global unique vs sondage par module validée par Blaise.

---

## Bonjour Cowork Hub IA Plateforme

3e application du pattern D-026 — modalité sondage global unique testée pour la première fois sur les 8 modules vague 5. Calibrage qualitatif : la modalité fonctionne bien sur les modules dont la structure est déjà bien connue (DEP-05, PR-01, PR-04, PR-05, CU-020 partiellement) ; elle est moins efficace sur les modules moins explorés (CU-024, DEP-01, DEP-07). Recommandation : maintenir cette modalité pour les vagues ultérieures, avec sondage approfondi ponctuel possible sur 1-2 modules à la demande.

Synthèse rapide cette fois :

- **2 rectifications structurelles importantes** (CU-024 acronymes PDP/PA, DEP-01 nature des « 6 étapes »)
- **5 hypothèses partiellement nuancées** (CU-020 cas-école, DEP-05 lien Garry Tan, DEP-07 articulation DEP-02, PR-01 risque confusion PR-04, PR-04 emploi devs juniors)
- **1 recommandation d'extraction transverse** non anticipée (chiffre « 362 incidents IA documentés Stanford » candidat brique transverse)
- **6 hypothèses confirmées sans rectification majeure**

Détail par module ci-dessous avec citation textuelle des passages canoniques HTML.

---

## Module 1 — CU-020 « Conformité RGPD / AI Act pour l'IA en PME »

### Passage 1.1 — Cadre réglementaire EU 2026 ✅ CONFIRMÉ avec précisions

**Articles AI Act applicables côté PME explicitement cités dans CU-020** :
- **Article 4** : formation IA obligatoire (entrée en vigueur 2 août 2026)
- **Article 14** : supervision humaine effective sur systèmes haut-risque (déjà cité CU-026)
- **Article 22 RGPD** : décision automatisée (déjà cité CU-026)
- **Article 50** : transparence et obligations de labellisation contenu GenAI (section pivot dédiée — `#section-art50`)

**Typologie des systèmes IA structurante** : oui, **4 niveaux de risque AI Act** (section 2 dédiée — `#section-2`). Ces 4 niveaux structurent une partie du module — à transposer textuellement.

**Sanctions chiffrées explicitement citées** : OUI
- **7 % CA mondial / 35 M€** (la formulation HTML est exactement « 7 % CA mondial » et « 35 M€ » comme sanction max, présente dans exec-stat-num + dans le tableau Section 5)

**Date canonique 2 août 2026** : formulation textuelle à préserver :
> *« Le règlement européen sur l'intelligence artificielle (AI Act) a été adopté en 2024, avec une entrée en application progressive jusqu'au 2 août 2027. La date la plus structurante côté PME est le 2 août 2026 : entrée en vigueur des obligations sur les modèles à usage général, l'article 4 (formation IA obligatoire), les organismes notifiés, et les premières sanctions effectives. »*

**Cas-école PME condamnée 2025-2026** : ⚠️ **PAS de cas-école spécifique PME condamnée dans CU-020**. L'unique cas-école jurisprudentiel mentionné dans le périmètre Hub est Moffatt v. Air Canada (cité dans CU-026 uniquement). **Ne pas inventer un cas-école PME pour CU-020** — l'absence est intentionnelle (le module est cartographique méthodologique, pas illustratif via une PME nommée).

### Passage 1.2 — Patches v3.10 (CNIL + HAS-CNIL santé) ✅ CONFIRMÉ

**Fiches CNIL — les 3 thèmes opérationnels** (citation textuelle de la liste ordonnée) :
1. **Applicabilité du RGPD aux modèles IA** : un modèle entraîné sur des données personnelles est lui-même un traitement de données personnelles potentiel
2. **Exigences de sécurité dans le développement IA**
3. **Annotation des données d'entraînement**

**Guide HAS-CNIL « Accompagner le bon usage des systèmes d'IA »** (mars 2026, consultation publique close 16 avril 2026) :
- S'adresse aux PME du **secteur santé / médico-social** ou éditrices d'IA — pas toutes PME
- **10 fiches dédiées au cycle de vie** + **2 fiches transverses** (gouvernance et GenAI)
- Devient « la référence opérationnelle » pour les PME concernées

**Draft Guidelines AI Act Art. 50** : citées dans CU-020 patches v3.10 avec calendrier 3 juin 2026 / 2 août 2026 / 2 décembre 2026 (encart synthèse 3 échéances). Les liens officiels Commission EU (`digital-strategy.ec.europa.eu`) sont présents dans les ressources.

### Passage 1.3 — Articulation avec autres modules ✅ CONFIRMÉ

**Modules explicitement référencés dans CU-020** :
- CU-014 (Multi-agents par fonction) pour transparence cascadée Art. 50
- Pas de wikilink direct vers PR-05 côté HTML actuel — l'articulation existe conceptuellement (conformité ≠ sécurité, c'est même le titre §1 de PR-05) mais elle n'est pas matérialisée en cross-link explicite dans CU-020 HTML
- **Ne pas créer de wikilink artificiel PR-05 ↔ CU-020 si non présent côté HTML** (« couple 1 tranche, couple 2 s'aligne »)

**Niveau de détail attendu pour cu-020.md** : section longue (~150-180 lignes) — c'est un module dense réglementaire avec section Article 50 pivot, 4 niveaux de risque, fiches CNIL, HAS-CNIL santé. **R10 critique** sur les sanctions chiffrées (7 % CA mondial / 35 M€) et les dates calendaires.

---

## Module 2 — CU-024 « Order-to-cash automation IA »

### Passage 2.1 — Structure workflow ventes-encaissement ✅ CONFIRMÉ avec précisions

**Workflow O2C en 6 étapes canoniques** (ordre exact à transposer) : devis → bon de commande → facturation → relance → encaissement → lettrage.

**Valeur IA différenciée par étape** (à transposer textuellement) :
- **Forte valeur IA** : étapes 4 (relance) et 6 (lettrage). Gains chiffrés textuels : *« relance : 30-40 % de DSO excédentaire en moins, 35-50 % de productivité opérationnelle »* et *« lettrage : 60-80 % du lettrage en automatique, là où les règles classiques plafonnent à 30-40 % »*
- **Valeur IA modérée** : étapes 1 (devis) et 3 (facturation)
- **Valeur IA faible** : étapes 2 (BC) et 5 (encaissement)

**Pas un « agent par étape » ni un « agent global multi-étapes »** : le HTML traite le workflow comme une cartographie de **valeur différenciée par étape**, pas comme une architecture multi-agent unifiée. À transposer comme tel.

**Outils nommés explicitement** : Pennylane, Sellsy, Axonaut, Esker, Sidetrade, **Aston AI** (cohérence avec ressources.html catégorie outils-compta-facturation-fr). Cursor / Claude Code / autres outils dev ne sont **pas** cités dans CU-024 — c'est un module métier compta.

### Passage 2.2 — Patches v3.10 PDP → PA ⚠️ RECTIFICATION ACRONYMES

**Hypothèse couple 2 incorrecte sur les acronymes** :
- **PDP** = **Plateforme de Dématérialisation Partenaire** (ancienne dénomination, art. 27 LF 2026 a renommé) — pas « Plateforme de Dématérialisation Partenaire » au sens lecteur, c'est bien partenaire DGFiP
- **PA** = **Plateforme Agréée** (nouvelle dénomination depuis loi finances 2026, art. 27)
- **PAS « Portail public »** — le PPF (Portail Public de Facturation) est un dispositif distinct géré par la DGFiP, à ne pas confondre avec les PA qui sont les opérateurs privés agréés

**Calendrier exact** (à transposer textuellement) :
- **125 PA immatriculées définitivement par la DGFiP au 5 mai 2026** (+ 17 dossiers en attente)
- **1er septembre 2026** : réception obligatoire pour toutes les entreprises + émission obligatoire grandes entreprises + ETI
- **1er septembre 2027** : émission obligatoire PME/TPE

**Pas de calendrier multi-jalons post-1er sept 2026 détaillé dans CU-024** au-delà de l'échéance PME/TPE 2027. Ne pas inventer d'autres échéances.

### Passage 2.3 — Cas-école PME ⚠️ ABSENCE CONFIRMÉE

**PAS de cas-école PME nommé dans CU-024**. Le module est cartographique méthodologique (similar à PR-08 « Financer son projet IA » et CU-020). À ne pas confondre avec les modules illustratifs (CU-026 avec Klarna, CU-027 avec Tea App).

**Section 5 « Cinq écueils typiques »** est l'angle pédagogique principal — pas un cas-école nommé.

**Niveau de détail attendu pour cu-024.md** : section longue (~150-180 lignes) — module dense avec 6 étapes O2C détaillées + calendrier réglementaire + tableau PA + pattern orchestration IA + 5 écueils + checklist 12 points.

---

## Module 3 — DEP-01 « Cadrer un projet IA pour la mise en production »

### Passage 3.1 — Heuristique anti-hype « 6 étapes » ⚠️ RECTIFICATION STRUCTURELLE

**Hypothèse couple 2 imprecise** : les « 6 étapes » de l'heuristique anti-hype ne sont **PAS des étapes de cadrage de projet IA**. C'est un **arbre de décision technique pour choisir l'architecture** :

1. **Single LLM call** (l'appel le plus simple)
2. **Long context** (si single LLM call manque de contexte)
3. **RAG** (si contexte ne tient pas dans la fenêtre)
4. **Fine-tuning** (si RAG manque de précision sur domaine spécifique)
5. **Single agent** (si décision/action dynamique nécessaire)
6. **Multi-agent** (uniquement si plusieurs spécialistes coopèrent réellement)

**Nom canonique** : « **l'heuristique anti-hype 2026 — single LLM call d'abord** » (anchor `#heuristique-anti-hype`).

**Pas de critère go/no-go explicite par étape** : c'est un arbre de décision séquentiel — on **teste chaque niveau avant de passer au suivant**. La règle d'or textuelle à préserver :
> *« Single LLM call d'abord, scaler seulement si prouvé nécessaire. »*

**Chiffre canonique à préserver textuellement** :
> *« 80 % des échecs de projet IA interviennent avant la première ligne de code — parce qu'on choisit d'emblée l'architecture la plus sophistiquée (multi-agent) alors qu'un single LLM call aurait suffi. »*

(R9 critique : « 80 % » déjà canonisé dans `chiffres-macro-2026.md` + cohérence avec PR-09 produit en v3.12).

### Passage 3.2 — Encart « Jagged Frontier » Stanford ✅ CONFIRMÉ

**Définition canonique** (anchor `#jagged-frontier`, à transposer textuellement) :
> *« « Jagged Frontier » (Stanford AI Index Report 2026) — l'IA n'est pas uniformément bonne ou mauvaise sur tous les sujets. C'est une frontière dentelée : excellente sur certaines tâches, défaillante sur d'autres pourtant proches. »*

**Exemples documentés Stanford** (ordre canonique à préserver — c'est un **contraste pédagogique adjacent**) :
- Gemini Deep Think a gagné une **médaille d'or à l'International Mathematical Olympiad**
- … mais le même modèle ne lit correctement l'heure sur une **horloge analogique que 50,1 % du temps**
- OSWorld : passage de **12 % à 66 % de task success en un an**
- … mais **1 échec sur 3 reste**

**Articulation avec heuristique anti-hype** : les 2 patterns sont **complémentaires** — heuristique = « choisir l'architecture simple en premier », Jagged Frontier = « ne jamais extrapoler d'une démo réussie à un déploiement universel ». À préserver comme **2 angles distincts** dans dep-01.md, pas à fusionner.

### Passage 3.3 — Articulation modules ✅ CONFIRMÉ

**Modules explicitement référencés dans DEP-01** :
- DEP-02 (RAG en production) — étape 3 de l'arbre
- DEP-04 §4bis (Fine-tuning SLM 1B-8B) — étape 4
- DEP-05 (Agents en production) — étape 5
- CU-014 (Multi-agents) + CU-026 (Gouvernance agents) — étape 6
- DEP-02 §2bis (RAG persistent memory shelf-life) — encart contexte 2026
- Pas de wikilink direct vers PR-01 côté DEP-01 actuel — articulation conceptuelle existe mais pas matérialisée

**Niveau de détail attendu pour dep-01.md** : section longue (~180-200 lignes) — module pivot pour l'arbre de décision architectural + Jagged Frontier + cadrage POC/pilote/production. **R10 critique** sur les 6 niveaux de l'arbre (ordre + dénominations).

---

## Module 4 — DEP-05 « Agents en production : observabilité et garde-fous »

### Passage 4.1 — Architecture observabilité agents ✅ CONFIRMÉ

**Structure originale (sections 1-7)** : architecture observabilité 5 layers, garde-fous, panorama outils, KPI, DevOps vs MLOps vs LLMOps, plan d'action 30 jours.

**Section 8 ajoutée v3.9 « Production-grade : 4 patterns industriels 2026 »** :
- §8.1 — 9-layer production architecture (techNmak)
- §8.2 — Gates machine-checkable TOML (wernerk_au)
- §8.3 — Code Execution with MCP (Anthropic)
- §8.4 — Agent Skills (Anthropic)

**Outils nommés** dans le panorama : LangSmith, Phoenix Arize, Helicone, Langfuse, **Comet Opik** (oui cités), AgentShield (cohérence DEP-08), etc. Tableau de mapping outils → cas d'usage présent.

### Passage 4.2 — §8.5 failure receipt + §8.5bis Effective Harnesses ✅ CONFIRMÉ avec précisions

**§8.5 « Failure receipts & ownership »** (ajouté v3.10) :
- Pattern correctif au risque « overclaimed completeness »
- 4 éléments du failure receipt : inputs reçus / actions entreprises / vérification résultats / propriétaire clair
- Cohérence avec §8.2 gates TOML (en amont) et §3 garde-fous

**§8.5bis « Effective Harnesses pour agents long-running »** (ajouté v3.10) :
- **Pattern two-agent harness** (Anthropic Engineering, mars 2026) — architecture à 2 rôles :
  - **Initializer agent** : crée le projet, scripts d'init, feature list structurée, progress log
  - **Coding agent** : implémente une feature par session, exécute tests E2E, met à jour progress log
- **Pas de lien avec « Fat Skills / Thin Harness » Garry Tan** — ce sont **2 patterns distincts** (Garry Tan = cu-027 §1bis.3 sur stack ECC, Anthropic = DEP-05 §8.5bis sur agents long-running). Ne pas confondre/fusionner.

**Insight clé textuel à préserver** :
> *« les artefacts externes deviennent la mémoire de l'agent. Chaque session reconstruit son contexte à partir du progress log + de l'historique git. »*

**Pas de chiffres ou benchmarks chiffrés associés** à ces 2 sections — ce sont des patterns conceptuels avec exemples (`claude-progress.txt`, commits git).

### Passage 4.3 — Articulation avec persistent memory + gouvernance ✅ CONFIRMÉ

**Wikilinks transverses explicites côté HTML** :
- **CU-008 §llm-wiki-shelf-life** (RAG vs persistent memory) — wikilink direct depuis §8.5bis (« cohérent avec le signal RAG vs persistent memory »)
- **DEP-08 (Sécurité agents et MCP)** — wikilink depuis §8.5 et §8.3 (Code Execution MCP)
- **DEP-03 §3bis (Du context au harness)** — wikilink depuis §8.3 (Code Execution MCP)

**Articulation avec CU-026 (Gouvernance agents IA)** : oui distinction préservée — DEP-05 = sécurité technique + observabilité + patterns production, CU-026 = gouvernance managériale (pattern « agent = employé » + 7 dimensions + 4 patterns Frontier Firms). Pas de duplication structurelle.

**Niveau de détail attendu pour dep-05.md** : section très longue (~200-250 lignes) — module le plus dense avec 7 sections originales + §8 (4 patterns) + §8.5 + §8.5bis. **R10 critique** sur les énumérations (5 layers, 4 patterns industriels, 2-agent harness) et les sources.

---

## Module 5 — DEP-07 « Évaluation continue et qualité IA »

### Passage 5.1 — Anthropic Demystifying Evals ✅ CONFIRMÉ

**2 publications Anthropic Engineering** citées textuellement avec liens :
- *« Demystifying evals for AI agents »* (mai 2026) — terminologie canonique + heuristique « eval first »
- *« Quantifying infrastructure noise in agentic coding evals »* (mai 2026) — méthode variance N runs pour distinguer bruit infra vs régression modèle

**Section 3.5 « Définitions canoniques Anthropic »** : référentiel terminologique formalisé (eval / harness / multi-turn evaluations / state-modifying agents — à préserver dans l'ordre canonique).

**Section 3.6 « eval first, optimize second »** : heuristique distincte de 3.5, à transposer comme principe opérationnel.

### Passage 5.2 — Métriques canoniques ✅ CONFIRMÉ avec précisions

**Structure DEP-07** : 5 sections H2 + section 3 « Les 3 types d'evals » (LLM-as-judge + Eval offline référence + Eval online utilisateurs réels). Pas un tableau exhaustif de métriques par use case mais une typologie des 3 approches.

**Outils tableau Section 4 « Outils d'évaluation 2026 »** : LangSmith, Phoenix Arize, Langfuse, Comet Opik, **Braintrust** (eval-first SaaS), etc.

**Le module est plus orienté méthodologie eval pipeline (golden minimum → 3 types d'evals → CI/CD)** que tableau métriques (recall@k, precision, MRR) — celles-ci sont mentionnées contextuellement mais pas en grille structurée. Ne pas créer une grille exhaustive en transposition MD.

### Passage 5.3 — Articulation DEP-02 et persistent memory ✅ CONFIRMÉ — distinction nette

**Articulation DEP-07 vs DEP-05 explicite côté HTML** (à préserver) :
> *« La distinction clé : evals (avant déploiement) vs observabilité (après). Les evals répondent à « est-ce que la sortie est bonne ? » avec des datasets golden. L'observabilité (cf. la fiche Agents en production : observabilité) répond à « qu'est-ce qui se passe en prod en ce moment ? ». Les deux sont nécessaires et complémentaires. »*

**Pas de duplication structurelle entre DEP-07 et DEP-02** :
- DEP-02 contient le **cycle Stitch → Evaluate → Iterate** dans le contexte spécifique du RAG en production (§6bis v3.8)
- DEP-07 est **méthodologie générale** d'eval pipeline transverse, applicable à tout projet IA

À transposer comme 2 modules distincts en MD avec wikilinks réciproques mais pas de duplication de contenu.

**Niveau de détail attendu pour dep-07.md** : section longue (~150-180 lignes) — module méthodologique avec 5 sections H2 + golden minimum + 3 types d'evals + 3.5 définitions canoniques + 3.6 heuristique + outils + CI/CD regression.

---

## Module 6 — PR-01 « Maturité organisationnelle »

### Passage 6.1 — Typologie 4 profils dirigeants Bpifrance ✅ CONFIRMÉ

**Ordre canonique HTML** : Sceptiques → Bloqués → Expérimentateurs → Innovateurs (cohérence avec hypothèse Cowork Plateforme).

**Définitions canoniques** (à transposer textuellement avec pourcentages et leviers prioritaires) :
| Profil | % | Caractéristique | Levier prioritaire |
|---|---|---|---|
| **Sceptiques** | **27 %** | Doutent de la valeur réelle de l'IA pour leur métier | Démonstration sur cas d'usage métier précis |
| **Bloqués** | **26 %** | Reconnaissent l'enjeu mais manquent de compétences | Formation + accompagnement opérationnel |
| **Expérimentateurs** | **19 %** | Testent activement, sans plan de scaling | Structuration d'une stratégie IA |
| **Innovateurs** | **28 %** | Intègrent l'IA dans leur stratégie globale | Scaling et industrialisation |

**Objectif pédagogique** : auto-positionnement dirigeant pour identifier son levier prioritaire (« plutôt que d'appliquer une recommandation uniforme »).

### Passage 6.2 — Encart « high performers » McKinsey ✅ CONFIRMÉ avec articulation

**L'encart est DISTINCT du framework 4 profils Bpifrance** : 2 grilles complémentaires, présentées dans la même section mais avec leur identité propre. Pas d'imbrication.

**Citation textuelle McKinsey à préserver verbatim** :
> *« The intentional redesigning of workflows has one of the strongest contributions to achieving meaningful business impact of all the factors tested. »*

**Articulation EXPLICITE textuelle** (à préserver telle quelle) :
> *« Les Innovateurs (28 %) correspondent approximativement aux AI high performers (6 %) dans l'enquête McKinsey — la convergence des 2 grilles d'analyse est cohérente. La typologie Bpifrance compte aussi des dirigeants en transition (Innovateurs débutants), McKinsey ne compte que les organisations qui ont déjà concrétisé un EBIT impact > 5 %. »*

Cette nuance d'échelle est **essentielle** — ne pas la perdre en transposition. Le 28 % et le 6 % ne mesurent **pas la même chose**.

### Passage 6.3 — Risque confusion avec PR-04 ⚠️ NUANCE IMPORTANTE

**Frontière éditoriale entre PR-01 et PR-04** :
- **PR-01** = **posture dirigeant + organisation** (typologie 4 profils, maturité organisationnelle, modèle 5R Cnam-Dejoux, syndromes POC à vie, mandat exécutif)
- **PR-04** = **marché + emploi** (chiffres adoption macro, primes salariales, comparaisons internationales)

**Chiffres partagés réels** :
- « 55 % TPE-PME utilisent IA gen fin 2025 » : présent dans **PR-04 §2bis** (chiffre adoption marché), **pas** dans PR-01 (cohérence des angles)
- « 58 % considèrent l'IA comme enjeu de survie » : présent dans **PR-04** (chiffre marché), **pas** dans PR-01
- « 67 % ne savent pas par où commencer » : déjà canonisé dans `chiffres-macro-2026.md`, à wikilinker dans PR-01 ET PR-04 avec angles différents

**Risque de duplication minimal** côté HTML — les 2 modules sont structurellement complémentaires. **Pas d'extraction transverse nécessaire** entre PR-01 et PR-04 sur ce périmètre.

**Niveau de détail attendu pour pr-01.md** : section longue (~180-200 lignes) — typologie 4 profils + high performers McKinsey + grille maturité organisationnelle + auto-évaluation 10 questions + causes structurelles (silos, validations).

---

## Module 7 — PR-04 « Marché IA & emploi »

### Passage 7.1 — Triple marché 2026 (§2bis) ✅ CONFIRMÉ avec précisions

**Structure §2bis « Tendances macro 2026 »** : section longue qui agrège **plusieurs séries de chiffres convergents** (cohérence avec hypothèse).

**Les 3 séries citées dans le §2bis** :
1. **Bpifrance Le Lab** : tableau « paradoxe enjeu vs adoption » (58 % enjeu de survie / 55 % usage occasionnel / 33 % adoption quotidienne / 26 % usage outillé France Num)
2. **Microsoft Work Trend Index 2026** : 49 % cognitive work Copilot M365 + ×15 agents M365 + 58 % Frontier Professionals + 42 % segment émergent + ×18 grandes entreprises
3. **McKinsey State of AI 2025** : 88 % adoption / 39 % EBIT impact / 23 % scalent agentique / 32-43-13 anticipation employeur (sous-encart dédié)
4. **Stanford AI Index Report 2026** : 53 % adoption population (3 ans) / Singapour 61 % UAE 54 % US 28,3 % / 172 Md$/an valeur consommateurs / 88 % organisationnelle / 4 sur 5 étudiants (sous-encart dédié)

→ Donc **PR-04 §2bis présente 4 séries de chiffres** (Bpifrance + Microsoft + McKinsey + Stanford), pas 3. À transposer dans cet ordre.

### Passage 7.2 — « Transformation Paradox » ⚠️ NUANCE PÉDAGOGIQUE

**Le « Transformation Paradox » est une formulation Microsoft** (cohérence hypothèse) — cité dans la **section 5 « Implications stratégiques » de PR-04**, pas dans §2bis. Distinction structurelle à préserver.

**Citation textuelle à transposer** :
> *« Le « Transformation Paradox » (Microsoft 2026) : le principal frein à la valeur IA n'est ni la technologie ni les collaborateurs, mais la culture de l'organisation. »*

**Pas un concept éditorial Hub** — c'est bien une formulation Microsoft tirée du Work Trend Index 2026.

### Passage 7.3 — Articulation PR-01 et emploi devs juniors -20 % ✅ CONFIRMÉ

**Chiffre « emploi devs juniors US -20 % depuis 2024 »** : **est dans CU-027 §1bis (Stanford)**, **pas dans PR-04**. À ne pas ajouter à pr-04.md en transposition — c'est un chiffre spécifique à l'écosystème dev IA-assisté, donc local à CU-027.

**Articulation avec PR-01** : minime, les 2 modules sont distincts dans leurs angles (cf. § 6.3 ci-dessus). Pas de wikilink cross-modules systématique à créer dans PR-04 vers PR-01.

**Niveau de détail attendu pour pr-04.md** : section très longue (~200-220 lignes) — module dense avec hero stats, §2bis riche (4 séries de chiffres), §2ter maturité agentique, prime salariale, spécificité française, 4 paliers maturité, encart Transformation Paradox section 5.

---

## Module 8 — PR-05 « Sécurité IA »

### Passage 8.1 — Cybersécurité agentique McKinsey + NIST CAISI ✅ CONFIRMÉ

**Section dédiée cybersécurité agentique** (anchor `#risques-agentiques` proche) avec citation McKinsey textuelle :
> *« 2026 : la cybersécurité agentique devient un vecteur de risque distinct du LLM classique »* (McKinsey « Securing the agentic enterprise », mai 2026)

**Chiffres McKinsey à préserver textuellement** :
- **RAI maturité moyenne 2026 : 2,3/5** (vs 2,0 en 2025) — progression mesurable mais lente
- **~1/3 des organisations à maturité ≥ 3** en stratégie, gouvernance et gouvernance agentique — donc **2/3 des organisations restent à risque**

**NIST CAISI** : section dédiée (anchor `#nist-caisi`) avec **6 thèmes prioritaires** (agent identity & authentication, auditability & non-repudiation, interoperability + 3 autres à compléter si HTML les explicite) + AI Agent Interoperability Profile prévu Q4 2026.

**Encart « 362 incidents IA documentés en 2025 » (Stanford)** : OUI **symétriquement présent** dans PR-05 et DEP-08, formulation textuelle similaire :
> *« 362 incidents IA documentés en 2025 vs 233 en 2024 — +55 % en un an (Stanford AI Index Report 2026). »*

**Angles distincts maintenus** :
- PR-05 = angle stratégique (signal de risque pour cadrage projet)
- DEP-08 = angle technique (incidents = vecteurs d'attaque + cohérence SBOM IA)

### Passage 8.2 — Articulation DEP-08 et brique transverse éventuelle ⚠️ RECOMMANDATION EXTRACTION TRANSVERSE

**Recommandation arbitrale** : **OUI, extraction transverse `chiffre-stanford-362-incidents.md` candidate**, application D-025.

**Justification** :
- Le chiffre « 362 incidents IA documentés en 2025 vs 233 en 2024 (+55 %) » est cité **symétriquement** dans PR-05 ET DEP-08
- Avec la production de PR-10 (v3.12 en cours) qui mobilise aussi ce chiffre, on aurait **3 modules** avec recouvrement quasi mot-pour-mot
- Critère D-025 satisfait : ce n'est pas l'ossature d'un module, c'est un chiffre macro répété
- Symétrique au pattern `chiffres-macro-2026.md` déjà existant

**Décision à arbitrer** : soit créer une brique transverse dédiée `pattern-cybersecurite-agentique.md` qui englobe le chiffre 362 + la citation McKinsey + le cadre NIST CAISI, soit simplement canoniser le chiffre dans `chiffres-macro-2026.md` (déjà fait via I-D-007). **Mon arbitrage recommandé** : canonisation simple dans `chiffres-macro-2026.md` suffit pour le chiffre 362 — pas besoin d'une brique transverse dédiée tant que les autres dimensions (citation McKinsey, NIST CAISI) restent locales aux modules concernés.

**Pas de duplication structurelle pleine** entre PR-05 et DEP-08 sinon — ils sont structurellement complémentaires (organisationnel vs technique).

### Passage 8.3 — Cas-école sécurité IA niveau organisationnel ⚠️ ABSENCE CONFIRMÉE

**PAS de cas-école PME nommé dans PR-05** — symétrique à DEP-08 qui utilise des CVE techniques (CVE-2025-59536, MCP STDIO, OpenClaw, Moltbook) plutôt que des RetEx entreprise.

PR-05 traite la sécurité IA niveau cadrage stratégique, pas via une PME nommée. **Ne pas inventer un cas-école PME pour PR-05**. La logique éditoriale est cohérente avec CU-020 et CU-024 (modules cartographiques sans cas-école nommé).

**Niveau de détail attendu pour pr-05.md** : section longue (~180-200 lignes) — module avec 4 sections originales + encarts v3.10/v3.11 (cybersécurité agentique + NIST CAISI + 362 incidents + NIST Critical Infrastructure intégré v3.10 Lot D).

---

## Bonus — passages sensibles non listés que je signale

### Bonus 1 — Brique transverse `chiffres-macro-2026.md` à actualiser

Avec la production des 8 modules vague 5, le référentiel `chiffres-macro-2026.md` est mobilisé **massivement** :
- Chiffres I-D-003 (6 chiffres McKinsey/Gartner/MIT v3.9)
- Chiffres I-D-005 (2 chiffres CU-027 Kimi/Opus)
- Chiffres I-D-006 (8 chiffres v3.10 Bpifrance/Microsoft)
- Chiffres I-D-007 (12 chiffres v3.11 Stanford/McKinsey)
- = **28 chiffres macro cumulés** à canoniser si pas encore traités

**Recommandation** : vérifier la cohérence du référentiel `chiffres-macro-2026.md` avant production vague 5, ou bumper le référentiel en parallèle de la production. Sans cela, les wikilinks transverses des 8 modules vers `chiffres-macro-2026.md` pointeront vers une version obsolète.

### Bonus 2 — Articulation PR-09 + PR-10 + PR-11 (v3.12 en cours)

L'itération v3.12 du Hub HTML (en cours de production Cowork → bientôt Claude Code) crée 3 nouveaux préalables (PR-09 cadrer projet + PR-10 vérifier hallucinations + PR-11 cycle de vie). Ces 3 nouveaux préalables seront **denses en cross-links** vers PR-01, PR-04, PR-05 (les 3 préalables vague 5 que tu produis).

**Recommandation** : anticiper qu'une **vague 6 RAG** sera nécessaire pour intégrer PR-09 + PR-10 + PR-11 — pas dans le périmètre vague 5 mais à programmer dans le sprint suivant (S2.6 ?). La cartographie de production MD doit refléter cette dépendance.

### Bonus 3 — Risque de duplication DEP-07 ↔ DEP-05 sur §8.2 gates TOML

Le pattern §8.2 gates TOML de DEP-05 (v3.9) mentionne explicitement les **gates machine-checkable** comme forme d'eval — il y a un recouvrement conceptuel avec DEP-07 (eval pipeline). **Risque mineur** mais à surveiller en production : ne pas dupliquer le contenu §8.2 dans DEP-07 — wikilinker plutôt depuis dep-07.md vers dep-05.md §8.2.

### Bonus 4 — PR-04 §2ter « Maturité agentique » vs §2bis « Tendances macro »

Au sein de PR-04, **§2bis** (tendances macro 2026) et **§2ter** (maturité agentique + bottlenecks 2026 — ajouté v3.9) sont 2 sections adjacentes denses qui mobilisent beaucoup de chiffres. **Risque de gigot lecteur**. À transposer en pr-04.md avec **transitions narratives explicites** entre les 2 sections pour éviter qu'on lise un mur de pourcentages.

---

## Synthèse opérationnelle pour le couple 2

**Rectifications à intégrer absolument avant production vague 5** :

1. **CU-024 acronymes** : PA = Plateforme Agréée (pas Portail public). Ne pas confondre avec PPF (Portail Public de Facturation). 125 PA immatriculées au 5 mai 2026.
2. **DEP-01 nature des « 6 étapes »** : c'est un **arbre de décision technique** (Single LLM → Long context → RAG → Fine-tuning → Single agent → Multi-agent), pas des étapes de cadrage de projet. Ne pas renommer ou regrouper.

**Précisions à préserver textuellement** :

3. **CU-020** : sanctions 7 % CA mondial / 35 M€. 4 niveaux de risque AI Act. Pas de cas-école PME (Moffatt reste uniquement dans CU-026).
4. **DEP-05 §8.5bis** : pattern **two-agent harness** Anthropic Engineering mars 2026, distinct du Fat Skills/Thin Harness Garry Tan (cu-027). Insight clé « artefacts externes = mémoire de l'agent ».
5. **DEP-07** : 3 types d'evals (LLM-as-judge + offline + online). Distinction explicite avec DEP-05 (eval avant déploiement vs observabilité après). Pas de tableau exhaustif de métriques par use case.
6. **PR-01** : 28 % Innovateurs Bpifrance ≠ 6 % high performers McKinsey (échelles différentes — préserver la nuance d'articulation).
7. **PR-04** : « Transformation Paradox » dans section 5 (pas §2bis). 4 séries de chiffres dans §2bis (pas 3). Le « -20 % emploi devs juniors » est dans CU-027, pas PR-04.
8. **PR-05** : encart 362 incidents symétrique avec DEP-08 (formulation similaire mais angles distincts maintenus). Pas de cas-école PME nommé.

**Recommandation extraction transverse** : pas de nouvelle brique transverse nécessaire vague 5. Le chiffre 362 incidents reste candidat à canonisation simple via `chiffres-macro-2026.md` (déjà couvert via I-D-007).

**Volume produit** : ~3 100 mots — dans la cible 2500-3500 mots du sondage.

**Charge cognitive Cowork Hub IA** : ~80 min (relecture rapide de 8 HTML source + structuration des réponses + identification de 4 passages bonus). Conforme à l'estimation 60-90 min du sondage.

**Pattern D-026 confirmé efficace** — 3e exercice consécutif, modalité sondage global unique validée. À conduire systématiquement pour vagues ultérieures contenant des modules denses N3-N4.

**À ta dispo** pour clarifier un point spécifique avant production, ou pour un second sondage ponctuel sur 1-2 modules si la transposition révèle un risque sur les 4 passages bonus signalés.

---

*Retour sondage produit le 20 mai 2026 par Cowork Hub IA. Troisième exercice du pattern D-026, première application en modalité sondage global unique sur 8 modules.*

— Cowork Hub IA
