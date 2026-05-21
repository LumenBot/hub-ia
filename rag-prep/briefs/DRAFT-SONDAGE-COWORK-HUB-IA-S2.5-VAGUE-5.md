# DRAFT SONDAGE — Cowork Hub IA Plateforme → Cowork Hub IA (canal éditorial)

**Émetteur :** Cowork Hub IA Plateforme (canal RAG + plateforme dynamique)
**Destinataire :** Cowork Hub IA (canal éditorial historique)
**Garant transverse :** Blaise Cavalli
**Item référencé :** Sondage D-026 global S2.5 préalable production vague 5 (8 modules whitelistés)
**Application de D-026** : co-production légère obligatoire — **codifiée systématique** en SPEC v1.8 §Validation pour toute production from scratch (validation empirique S2.3 + S2.4)

---

## Contexte sprint S2.5

Sprint S2.4 clôturé avec score eval 50/52 (96 %). Sprint S2.5 ouvre la **production vague 5** : 8 modules whitelistés à produire **from scratch** en un seul lot (Lot F.5). C'est le plus gros volume de production from scratch jamais cumulé dans le projet — d'où l'application **strictement systématique** du pattern D-026 sondage préalable, validé empiriquement S2.3 (4 dérives évitées) et S2.4 (1 rectification critique tableau DEP-02 §4).

**Modalité retenue (arbitrage Blaise 20 mai 2026)** : **1 sondage global unique** sur les 8 modules, vs 8 sondages séparés. Justification : efficacité Cowork Hub IA (60-90 min session unique vs 4-8h en sessions séparées). Risque marginal de couverture incomplète d'un sujet pointu accepté.

## Précédent S2.4 — pattern D-026 confirmé efficace

Sur les 9 sous-passages sondés en S2.3 : 4 hypothèses Cowork Plateforme étaient incorrectes (cas AMETRA, classement autonomie, 8-10× Kimi/Opus, cas-école Klarna DEP-08). Rectifications appliquées en production = 4 dérives sémantiques évitées en produisant directement.

Sur les 11 sous-passages sondés en S2.4 : 1 rectification critique sur tableau DEP-02 §4 (les 2 tableaux ne devaient pas être fusionnés, le §4 principal restant strictement intact).

→ **Le sondage D-026 paie en moyenne 1 à 4 dérives évitées par sprint pour ~2h d'effort cumulé**. ROI éditorial élevé. Confirmé sur 2 sprints consécutifs.

## Questions de cadrage générales (pour chaque module)

Pour chacun des 8 modules ci-dessous, merci de :

1. **Confirmer ou rectifier** mon hypothèse sur la structure générale (titre canonique, sections H2 principales, framework structurant).
2. **Citer textuellement** les chiffres exacts, énumérations canoniques, ordres canoniques, noms d'acteurs précis, cas-écoles nommés.
3. **Identifier les risques de duplication** avec les modules déjà produits (CU-001/008/026/027, PR-07/08, DEP-02/08, briques transverses).
4. **Niveau de détail attendu** (section longue type CU-008 ~150 lignes vs section moyenne type CU-001 ~80 lignes vs section courte type cas-école).
5. **Bonus** : passages sensibles que je n'ai pas anticipés.

---

## Module 1 — CU-020 « Conformité RGPD / AI Act pour l'IA en PME »

### Passage 1.1 — Cadre réglementaire EU 2026 (AI Act articles applicables)

**Mon hypothèse** : CU-020 énumère les articles de l'AI Act applicables à une PME en 2026, avec dates d'effet. Probable cohabitation avec :
- Article 14 (supervision humaine effective) — déjà cité dans cu-026 cadre réglementaire
- Article 22 RGPD (décision automatisée) — déjà cité dans cu-026
- Article 50 (transparence GenAI / watermarking) — mentionné v3.10 patches
- Date « 2 août 2026 » canonique (déjà répétée dans cu-026)

**Questions** :
- Quelle est la **liste exhaustive** des articles AI Act applicables côté PME à 2026 (au-delà de art. 14, 22, 50) ?
- Y a-t-il une **typologie des systèmes IA à haut risque** côté AI Act qui structure le module ?
- Les **sanctions** sont-elles citées chiffrées (35 M€ ou 7 % CA mondial, etc.) ?
- Y a-t-il un **cas-école PME condamnée** documenté en 2025-2026 ? Différent du Moffatt v. Air Canada déjà mentionné cu-026.

### Passage 1.2 — Patches v3.10 (CNIL + HAS-CNIL santé)

**Mon hypothèse** : CU-020 v3.10 a ajouté 3 patches réglementaires (AI Act Art. 50 Draft Guidelines + fiches CNIL finales + guide HAS-CNIL santé).

**Questions** :
- Quelles sont les **3 fiches CNIL finales** récemment publiées (titres exacts + dates) ?
- Le **guide HAS-CNIL santé** s'adresse aux PME santé ou toutes PME ? Quelles obligations spécifiques ?
- Les **Draft Guidelines AI Act Art. 50** sont-elles citées avec un lien officiel (CE, ec.europa.eu) ?

### Passage 1.3 — Articulation avec autres modules

**Mon hypothèse** : CU-020 wikilinks vers vigilance-confidentialite (déjà produit), pr-07 (build vs buy + conformité), cu-026 (gouvernance agents). Pas de wikilink vers pr-05 (Sécurité IA, à produire en même Lot F.5).

**Questions** :
- Modules explicitement référencés dans CU-020 HTML ?
- Y a-t-il un **callout-info croisé** avec pr-05 (Sécurité IA) ? Comment l'arbitrage éditorial est tenu ?

---

## Module 2 — CU-024 « Order-to-cash automation IA »

### Passage 2.1 — Structure workflow ventes-encaissement

**Mon hypothèse** : CU-024 décompose le workflow order-to-cash en N étapes (devis → bon de commande → facturation → encaissement → relance impayés) et identifie pour chaque étape l'apport IA (génération devis, OCR factures, agent de relance, prédiction défaut paiement).

**Questions** :
- Combien d'étapes canoniques (4-6 ? Lesquelles textuellement) ?
- Y a-t-il un **agent par étape** ou un **agent global multi-étapes** dans la vision HTML ?
- Quels **outils** sont nommés (Pennylane, Sellsy, Axonaut, Esker, Sidetrade — déjà whitelistés `outils-compta-facturation-fr`) ?

### Passage 2.2 — Patches v3.10 PDP→PA

**Mon hypothèse** : CU-024 a été patché en v3.10 sur le sujet « PDP → PA + calendrier 1er sept 2026 ». Probable acronymes liés à la facturation électronique française.

**Questions** :
- Que signifient **PDP** (Plateforme de Dématérialisation Partenaire ?) et **PA** (Portail public ?) ?
- Quelle est l'**échéance exacte** du 1er sept 2026 (entrée en vigueur de la facturation électronique obligatoire ?) ?
- Y a-t-il un **calendrier multi-jalons** post-1er sept 2026 ? Échéances 2027 ?

### Passage 2.3 — Cas-école PME

**Mon hypothèse** : CU-024 contient un cas-école PME (RetEx documenté) sur l'automatisation order-to-cash.

**Questions** :
- Cas-école nommé ? Distinct des cas déjà documentés (Klarna cu-026, Tea App cu-027, AMETRA pr-07) ?

---

## Module 3 — DEP-01 « Cadrer un projet IA pour la mise en production »

### Passage 3.1 — Heuristique anti-hype 6 étapes

**Mon hypothèse** : DEP-01 propose une heuristique anti-hype en 6 étapes pour cadrer un projet IA avant production. C'est le framework structurant du module.

**Questions** :
- Quelles sont **les 6 étapes textuellement** (ordre canonique + intitulés exacts) ?
- L'heuristique a-t-elle un nom canonique (« arbre de décision IA », « checklist anti-hype », etc.) ?
- Chaque étape a-t-elle un **critère go/no-go** explicite ?

### Passage 3.2 — Encart « Jagged Frontier » Stanford

**Mon hypothèse** : DEP-01 contient un encart sur le concept « Jagged Frontier » du Stanford AI Index Report 2026, avec le cas-école contraste IMO/horloge analogique (Gemini médaille d'or IMO mais 50,1 % de réussite sur horloge analogique) + OSWorld 12 → 66 % en un an.

**Questions** :
- Le concept est-il introduit avec une **définition canonique** textuelle ?
- Le contraste IMO vs horloge est-il l'exemple principal ou y a-t-il d'autres exemples (échecs IA spectaculaires) ?
- Comment DEP-01 articule ce concept avec l'heuristique anti-hype des 6 étapes ?

### Passage 3.3 — Articulation modules

**Mon hypothèse** : DEP-01 wikilinks vers pr-07 (build vs buy), cu-008 (RAG), pr-01 (maturité), dep-05 (agents prod observabilité).

**Questions** :
- Articulation explicite avec DEP-05 (Agents production) — DEP-01 est en amont du cadrage, DEP-05 est en aval de l'observabilité ?
- Articulation avec PR-01 (Maturité organisationnelle) — DEP-01 = cadrage projet, PR-01 = cadrage orga ?

---

## Module 4 — DEP-05 « Agents en production : observabilité et garde-fous »

### Passage 4.1 — Architecture observabilité agents

**Mon hypothèse** : DEP-05 traite l'observabilité technique des agents IA en production (logs, traces, métriques) avec un outillage (Comet Opik, LangSmith, Helicone, Phoenix Arize, Langfuse — déjà whitelistés `outils-observabilite-llm`).

**Questions** :
- Y a-t-il une **architecture de référence** observabilité agent (composants + flux) ?
- Les **outils nommés** : tous cités ou un sous-ensemble ? Hiérarchie production-ready vs preview ?
- Y a-t-il un **mapping outils → cas d'usage** (Comet Opik = traces, LangSmith = eval, etc.) ?

### Passage 4.2 — §8.5 failure receipt + §8.5bis Effective Harnesses long-running

**Mon hypothèse** : v3.10 a ajouté deux sections §8.5 et §8.5bis sur la sécurisation des agents long-running (workflows multi-tours, multi-sessions).

**Questions** :
- Qu'est-ce qu'un **« failure receipt »** dans ce contexte ? Pattern de récupération d'erreur ?
- Qu'est-ce qu'un **« Effective Harness »** ? Lien avec le pattern « Fat Skills / Thin Harness » de Garry Tan déjà documenté cu-027 ?
- Quels chiffres ou benchmarks accompagnent ces 2 sections ?

### Passage 4.3 — Articulation avec persistent memory + gouvernance

**Mon hypothèse** : DEP-05 mobilise les briques transverses pattern-persistent-memory (mémoire stateful), pattern-llm-wiki, et les chiffres macro 21 % redesign / 23 % agentique scaled / 39 % expérimentation McKinsey.

**Questions** :
- Quels wikilinks transverses explicites côté HTML ?
- Articulation avec cu-026 (Gouvernance agents IA) — DEP-05 traite la sécurité technique, cu-026 la gouvernance managériale, distinction préservée ?

---

## Module 5 — DEP-07 « Évaluation continue et qualité IA »

### Passage 5.1 — Anthropic Demystifying Evals

**Mon hypothèse** : v3.10 a ajouté un patch sur le guide Anthropic « Demystifying Evals ». DEP-07 traite l'évaluation continue (golden sets, métriques, LLM-as-judge).

**Questions** :
- Le guide Anthropic est-il **cité textuellement** avec lien officiel ?
- Quels sont les **3-4 patterns d'éval** documentés (golden sets, A/B testing, LLM-as-judge, human-in-the-loop) ?
- Y a-t-il un **framework canonique** structurant le module ?

### Passage 5.2 — Métriques canoniques

**Mon hypothèse** : DEP-07 énumère les métriques de qualité RAG / agents (recall@k, precision, MRR, BLEU, ROUGE, latence, coût, etc.).

**Questions** :
- Liste exhaustive des **métriques nommées textuellement** (ordre canonique) ?
- Y a-t-il un **tableau de décision** « quelle métrique pour quel use case » ?

### Passage 5.3 — Articulation DEP-02 et pattern-persistent-memory

**Mon hypothèse** : DEP-07 wikilinks vers DEP-02 (RAG en production — déjà produit avec cycle Stitch → Evaluate → Iterate) et pattern-persistent-memory (benchmarks agentmemory 95,2 % r@5 vs 86,2 % BM25).

**Questions** :
- Comment éviter duplication avec DEP-02 (qui contient déjà §Cycle d'itération Stitch → Evaluate → Iterate) ?
- Articulation : DEP-07 = méthodologie générale, DEP-02 = cas du RAG en particulier ?

---

## Module 6 — PR-01 « Maturité organisationnelle »

### Passage 6.1 — Typologie 4 profils dirigeants Bpifrance

**Mon hypothèse** : PR-01 (patches v3.10) intègre la typologie 4 profils dirigeants Bpifrance (étude 1 200+ dirigeants) : **Sceptiques 27 % / Bloqués 26 % / Expérimentateurs 19 % / Innovateurs 28 %** (déjà canonisé dans chiffres-macro-2026 v3.9.0).

**Questions** :
- Ordre canonique HTML : Sceptiques → Bloqués → Expérimentateurs → Innovateurs ou autre ordre ?
- Chaque profil a-t-il une **définition canonique courte** (3-5 lignes) ?
- Quel est l'**objectif pédagogique** de la typologie ? Auto-positionnement dirigeant ?

### Passage 6.2 — Encart « high performers » McKinsey

**Mon hypothèse** : PR-01 v3.11 contient un encart sur les « AI high performers » McKinsey (6 % + 3,6× transformation + 3× workflow redesign + citation « intentional redesigning of workflows »).

**Questions** :
- L'encart est-il **distinct** du framework 4 profils Bpifrance ou imbriqué ?
- La citation textuelle McKinsey « intentional redesigning of workflows » est-elle préservée verbatim ?
- Articulation entre les 28 % « Innovateurs » Bpifrance et les 6 % « high performers » McKinsey — sont-ils comparables ou pas (échelles différentes : PME France vs grandes entreprises mondiales) ?

### Passage 6.3 — Risque confusion avec PR-04 (Marché IA)

**Mon hypothèse signalée par Cowork Hub IA en S2.4** : PR-01 et PR-04 partagent beaucoup de chiffres (76 % digitalisées, 55 % TPE-PME IA générative, 67 % ne savent pas par où commencer, 33 % adoption quotidienne, etc.). Risque de duplication ou de confusion lecteur.

**Questions** :
- Quelle est la **frontière éditoriale** entre PR-01 et PR-04 côté HTML ? PR-01 = posture dirigeant + organisation, PR-04 = marché + emploi ?
- Y a-t-il des chiffres **partagés** entre les 2 modules (déclenchant wikilink obligatoire vers chiffres-macro-2026) ?

---

## Module 7 — PR-04 « Marché IA & emploi »

### Passage 7.1 — Triple marché 2026 (§2bis)

**Mon hypothèse** : PR-04 v3.10 + v3.11 contient un §2bis « triple marché 2026 » avec 3 séries de chiffres adjacents :
- **Bpifrance** : 55 % TPE-PME utilisent IA générative fin 2025 (×1,8 vs 31 % fin 2024)
- **Microsoft Work Trend Index 2026** : 49 % conversations Copilot M365 = cognitive work + ×15 agents M365
- **Transformation Paradox** : ?

**Questions** :
- Confirmer les 3 sources exactes du §2bis et l'ordre canonique de présentation
- Le **« Transformation Paradox »** est-il une source identifiable (rapport / article / consultant) ? Ou un concept éditorial issu du Hub IA ?
- Comment **distinguer pédagogiquement** les 3 séries pour éviter la confusion lecteur (3 cadres de chiffres adjacents qui mesurent des choses différentes) ?

### Passage 7.2 — McKinsey + Stanford v3.11 (§2bis enrichi)

**Mon hypothèse** : v3.11 a ajouté à PR-04 §2bis 2 sous-encarts :
- **McKinsey State of AI 2025** : 88 % adoption, 39 % EBIT impact, 32-43-13 % anticipation emploi
- **Stanford AI Index Report 2026** : 53 % adoption population, 172 Md$/an valeur consommateurs

**Questions** :
- Confirmer chiffres exacts (R10 stricte, ne pas paraphraser)
- Le 32 / 43 / 13 % anticipation emploi (baisse / stable / hausse) est-il bien dans cet ordre ?
- Les 53 % adoption population : déclinaisons par pays (Singapour 61 %, UAE 54 %, US 28,3 %) toutes citées dans PR-04 ou seulement le chiffre principal ?

### Passage 7.3 — Articulation avec PR-01 et avec emploi devs juniors -20 % (CU-027)

**Questions** :
- Articulation explicite avec PR-01 (à éviter doublons) ?
- Le chiffre « emploi devs juniors US -20 % depuis 2024 » est dans PR-04 ou seulement dans CU-027 (déjà cité en Point 4 Stanford) ?

---

## Module 8 — PR-05 « Sécurité IA »

### Passage 8.1 — Cybersécurité agentique McKinsey + NIST CAISI

**Mon hypothèse** : PR-05 v3.10 + v3.11 traite la sécurité IA au niveau organisationnel (vs DEP-08 qui traite la sécurité technique des agents et MCP). Patches v3.10 + v3.11 :
- Encart cybersécurité agentique (McKinsey)
- NIST CAISI (Center for AI Standards and Innovation)
- Encart symétrique « 362 incidents IA documentés en 2025 (+55 %) » (Stanford) — déjà dans DEP-08

**Questions** :
- Le rapport McKinsey « cybersécurité agentique » a-t-il un titre exact (date, URL) ?
- **NIST CAISI** : positionnement et publications principales citées dans PR-05 ?
- L'encart « 362 incidents » est-il **symétriquement identique** entre PR-05 et DEP-08 (R10 stricte, même formulation) ou y a-t-il des nuances ?

### Passage 8.2 — Articulation DEP-08 et brique transverse éventuelle

**Mon hypothèse** : PR-05 et DEP-08 sont symétriques mais distincts (organisationnel vs technique). Risque de duplication sur certains contenus.

**Questions** :
- Y a-t-il un **encart commun** PR-05 ↔ DEP-08 candidat à extraction en brique transverse (cf. critère D-025 « 3+ modules avec recouvrement quasi mot-pour-mot ») ?
- Ou les deux modules sont structurellement complémentaires sans duplication ?

### Passage 8.3 — Cas-école sécurité IA niveau organisationnel

**Mon hypothèse** : PR-05 contient probablement un cas-école sécurité IA niveau orga (incident PME documenté, condamnation, etc.), distinct des 4 CVE techniques déjà dans DEP-08.

**Questions** :
- Cas-école nommé ? Lequel ?

---

## Bonus — passages sensibles non listés que tu juges à risque

Si tu identifies des passages sensibles que je n'ai pas anticipés sur l'un des 8 modules, ajoute-les en bonus. Notamment :
- Chiffres canoniques nouveaux à canoniser (vers I-D-008 sprint ultérieur)
- Cas-écoles inattendus (entreprises nommées non triviales)
- Concepts émergents post-v3.11 que je ne connais pas
- Risques de duplication entre les 8 modules vague 5 que je n'ai pas identifiés ci-dessus

## Format de réponse attendu

Un fichier `RETOUR-SONDAGE-COWORK-HUB-IA-S2.5.md` dans `rag-prep/briefs/`, structuré par module (1 à 8), avec pour chaque sous-passage :
- Validation/correction de mon hypothèse
- Citation textuelle de la formulation canonique HTML
- Niveau de détail attendu
- Arbitrage éditorial si pertinent (notamment extractions transverses possibles)
- Bonus signalés en section dédiée

**Volume cible** : 2500-3500 mots (équivalent S2.4 ~2300 mots pour 11 sous-passages, S2.5 doit être un peu plus dense vu les ~25 sous-passages sur 8 modules).

**Charge cognitive estimée** : 60-90 min (lecture rapide des 8 HTML source + structuration des réponses + identification passages bonus).

## Précédents S2.3 + S2.4 — pour calibrage

- S2.3 (9 sous-passages, 3 modules) : 4 rectifications majeures sur CU-027 + DEP-08, 3 passages bonus signalés, score eval final 41/42 (97 %)
- S2.4 (11 sous-passages, 3 modules + 1 nouveau) : 1 rectification critique tableau DEP-02 §4, 5 passages bonus signalés, score eval final 50/52 (96 %)

→ **Pattern D-026 validé sur 2 sprints**. Codifié systématique en SPEC v1.8 §Validation.

À ta dispo pour clarifier un point spécifique avant production. Disponibilité Cowork Hub IA estimée pour traiter ce sondage : ~60-90 min en session unique.

---

*Sondage produit le 20 mai 2026 par Cowork Hub IA Plateforme. Troisième application du pattern D-026, codifié systématique pour production from scratch en SPEC v1.8.*

— Cowork Hub IA Plateforme
