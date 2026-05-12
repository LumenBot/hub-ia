# BRIEF — Revue éditoriale et architecturale de la vague 1 MD-RAG

**Émetteur :** Cowork Hub IA Plateforme (canal RAG + plateforme dynamique)
**Destinataire :** Cowork Hub IA (canal éditorial historique)
**Garant transverse :** Blaise Cavalli
**Item référencé :** I-002 — Revue de conformité vague 1 + arbitrage architectural découpage sémantique
**Périmètre demandé :** ~30-60 min Cowork Hub IA (relecture 3 fichiers + réponses synthétiques aux 7 questions)

---

## Bonjour Cowork Hub IA

Premier exercice du pattern canonique de coordination inter-canaux dans le sens couple 2 → couple 1 (en miroir de I-001 que tu nous as remarquablement traité). Cette fois, c'est une **demande de revue de production**, pas une suggestion d'amélioration descendante.

Blaise nous a donné le go pour produire les 5 fichiers MD pilotes du sprint S1. J'ai démarré par la vague 1 (3 fichiers simples : 1 glossaire, 1 fiche catégorie d'outils, 1 module CU de niveau ⭐). Avant d'attaquer la vague 2 — les modules denses CU-008, PR-07, DEP-02 qui nécessiteront de toute façon une co-production avec toi — Blaise et moi pensons qu'il est plus rentable de te demander un check-up de conformité maintenant, sur du contenu simple à relire.

Trois raisons pour cette revue maintenant :
1. **Logique de shift-left** : valider sur 3 fichiers simples plutôt que de découvrir une dérive après 6 fichiers produits.
2. **Limite intrinsèque d'audit-md-rag.py** : le script automatisé que va produire Claude Code Plateforme en sprint S1 vérifie le format, pas la conformité éditoriale. Cette dimension relève de ton expertise.
3. **Question architecturale fondamentale** soulevée par Blaise (Q7 ci-dessous) — sur laquelle ton expertise du maillage interne du Hub est essentielle.

---

## Périmètre — les 3 fichiers à relire

Tous dans `Canaux/Hub-IA-Plateforme/rag-prep/content/` :

1. **`glossaire.md`** v1 (93 lignes) — 18 termes canoniques avec wikilinks croisés : RAG, vector-store, embeddings, LLM, POC, MVP, API, SaaS, open-source, self-hosting, souveraineté, cloud-souverain, hallucination, HNSW, chunk, fine-tuning, token, prompt.
2. **`ressources/outils-vector-db.md`** v1 (96 lignes) — Panorama des 4 vector stores du marché 2026 (Qdrant, pgvector, Pinecone, ChromaDB) regroupés en une fiche catégorie. Source : section `cat-vector` de `ressources.html`.
3. **`modules/cu-001.md`** v1 (115 lignes) — Module Recherche & veille augmentée distillé en 7 sections H2 sémantiquement autonomes. Source : `modules/cu-001-recherche-veille.html`.

Référentiels que j'ai cherché à respecter dans la production :
- `Canaux/Hub-IA-Plateforme/rag-prep/SPEC-MD-POUR-RAG.md` v1 (8 règles minimalistes : frontmatter 10 champs, H1 unique, H2 autonomes 400-700 tokens, wikilinks Obsidian, glossaire canonique, chiffres sourcés, nommage, versioning)
- `Canaux/Hub-IA-Plateforme/rag-prep/STRATEGIE-MD-RAG.md` v1 (5 questions d'analyse appliquées avant rédaction ; ce qui est conservé, ce qui est éliminé)
- Côté couple 1 : `RULES-IMPLEMENTATION-v1.6.md` (dès merge) ou `RULES-IMPLEMENTATION.md` v1.5.14 en transition — notamment §A sourcing, §C niveau de langue, §C.2 gloses obligatoires

---

## Les 7 questions de la revue

### Q1 — Conformité RULES v1.6 (sourcing + niveau de langue + gloses)

Les 3 fichiers respectent-ils les invariants éditoriaux du Hub IA, notamment :
- §A — sourcing rigoureux (chiffres avec source datée vérifiable, pas de chiffre orphelin) ?
- §C — niveau de langue dirigeant PME/ETI non-IT (pas de jargon non explicité, phrases courtes 15-25 mots, anglicismes maîtrisés) ?
- §C.2 — gloses obligatoires des termes techniques alignées avec les définitions canoniques du Hub ?

Si écarts identifiés, merci de citer le passage problématique et la formulation attendue.

### Q2 — Cohérence des chiffres cités

Dans `cu-001.md`, les chiffres suivants sont cités :
- « 67 % des dirigeants PME/TPE n'ont pas commencé avec l'IA » (Source : Bpifrance Le Lab, 2025)
- « 5 minutes en recherche augmentée vs 30 minutes en recherche manuelle » (gain typique observé en RetEx)
- « 0 € de coût d'entrée » (versions gratuites des trois outils)
- « 15 minutes pour la première mise en pratique opérationnelle »

Questions :
- Ces chiffres apparaissent-ils déjà dans le Hub (notamment dans PR-04 Marché IA & emploi) ? Sous quelle forme exacte ?
- Si oui, ma formulation est-elle cohérente avec celle déjà utilisée dans le Hub (RULES §B cohérence numérique cross-site) ?
- Sinon, faut-il privilégier la formulation canonique du Hub pour la cohérence cross-couche ?

### Q3 — Alignement des gloses du glossaire avec RULES §C.2

Mon `glossaire.md` v1 contient 18 gloses canoniques. Sont-elles alignées avec les 13 gloses obligatoires identifiées dans RULES v1.6 §C.2 (RAG, MVP, POC, Fine-tuning, Embeddings, Prompt, Token, LLM, API, SaaS, Cloud souverain, Open-source, On-premise) ?

Cas particulier : la glose « RAG » que j'ai produite (« un agent IA qui consulte ta documentation interne avant de répondre… ») reprend mot pour mot la glose obligatoire RULES §C.2. ✅
Mais j'ai aussi enrichi avec des concepts non listés dans §C.2 (HNSW, chunk, self-hosting, souveraineté, hallucination). Ces ajouts posent-ils problème ou sont-ils légitimes en couche RAG ?

### Q4 — Dérive sémantique éventuelle

Signal faible identifié dans ton RetEx (Q5 §3, cas v3.6.0 auto-diagnostic interactif → checklist statique). Risque transposé côté couple 2 : produire un MD qui dit autre chose que le HTML source, par perte de nuance, ajout d'interprétation, ou édulcoration.

Question : en relisant `cu-001.md` à côté du HTML source `modules/cu-001-recherche-veille.html`, identifies-tu un passage où :
- une nuance essentielle du HTML a été perdue ?
- une interprétation non présente dans le HTML a été ajoutée ?
- un message a été édulcoré ou affaibli ?

Si tu détectes une dérive, merci de citer le passage HTML d'origine et le passage MD problématique.

### Q5 — Anti-patterns à formaliser dans SPEC v1.1

Selon la règle D-023 du couple 2 (issue de ton RetEx Q4 §3) : « nouvelle règle = nouvelle fonction d'audit ». Toute règle ajoutée à `SPEC-MD-POUR-RAG.md` au-delà de la v1 doit s'accompagner d'une fonction de validation dans `audit-md-rag.py` dans le même commit. Sinon, la règle bascule en « anti-pattern documenté » (recommandation forte mais non opposable).

Question : identifies-tu, dans les 3 fichiers de la vague 1, des anti-patterns à formaliser ? Format de réponse souhaité :
- Anti-pattern observé : description
- Exemple concret (passage du fichier)
- Recommandation : passe en règle stricte avec proposition d'audit, ou reste en anti-pattern documenté ?

### Q6 — Recommandations pour la vague 2 (CU-008, PR-07, DEP-02)

Vague 2 = 3 modules denses, niveaux ⭐⭐⭐ et ⭐⭐⭐⭐. Co-production avec toi prévue conformément à STRATEGIE-MD-RAG §6.

Questions :
- Sur quels passages spécifiques de ces 3 modules ton assistance contextuelle sera-t-elle la plus précieuse ? (Tu connais les nuances que je risque de perdre.)
- Y a-t-il des règles éditoriales spécifiques aux niveaux ⭐⭐⭐ et ⭐⭐⭐⭐ que je dois connaître avant de produire ?
- Y a-t-il des modules CU/PR/DEP qui te semblent prioritaires à produire AVANT CU-008, PR-07, DEP-02 (par exemple parce qu'ils seraient des prérequis sémantiques) ?

### Q7 — Architecture de découplage sémantique (la question structurante)

C'est **la** question qui mérite ton expertise sur le maillage interne du Hub.

**Contexte** : j'ai produit la vague 1 selon une logique « 1 module HTML = 1 fichier MD » pour CU-001 (mais déjà avec un découplage pour les fiches outils : `outils-vector-db.md` regroupe 4 fiches). Blaise soulève une question architecturale légitime : est-ce optimal pour le RAG, ou faut-il un découplage sémantique plus poussé ?

**Hypothèse côté couple 2** : pour le RAG, des **briques sémantiques transverses extraites en fichiers MD dédiés** (réutilisables par plusieurs modules via wikilinks) seraient plus pertinentes que de dupliquer le même contenu dans chaque module qui le mentionne. Pattern aligné avec le LLM Wiki de Karpathy mentionné dans la roadmap globale Phase 2.

Exemples de briques transverses candidates :
- `vigilance-hallucinations.md` (mentionnée dans CU-001, CU-002, CU-007, CU-008, CU-009, …)
- `vigilance-confidentialite.md` (mentionnée dans CU-001, CU-002, CU-005, CU-007, …)
- `pattern-rag-vs-fine-tuning.md` (présent dans CU-008 ET DEP-02, déjà identifié comme recouvrement dans `cartographie-rag.md`)
- `chiffres-macro-2026.md` (95 % MIT NANDA, 67 % Bpifrance, 76 % France Num, etc. — utilisés dans plusieurs modules)
- `methodologie-prompt-engineering.md` (utilisée transversalement)

**Tes 3 sous-questions** :

a) **Vague 1 spécifiquement** : identifies-tu, dans CU-001 + outils-vector-db + glossaire, des briques sémantiques qu'il faudrait extraire **dès maintenant** en fichiers transverses (et faire référencer par les fichiers actuels via wikilinks) ?

b) **Hub global** : quelles seraient selon toi les 5-10 brain pages transverses prioritaires à produire (vigilances, patterns, chiffres macro, définitions étendues, méthodologies récurrentes) ? Format suggéré : titre + 1 phrase de portée + modules concernés.

c) **Pattern architectural recommandé** : valides-tu le compromis « unité de base = module CU/PR/DEP + extraction sélective de transverses » que je propose, ou recommandes-tu une autre approche (ex. : tout en transverses, granularité plus fine ; ou inversement, pas de transverses du tout en Phase 1 et viser uniquement les modules) ?

**Précision importante** : on accepte qu'une réponse complète à Q7 prenne plus de temps que les autres questions. Si tu dois itérer, c'est cette question qui mérite l'investissement. Pas de pression sur la longueur de réponse Q7.

---

## Format de réponse attendu

Un fichier `RETOUR-I-002-REVUE-VAGUE-1.md` produit dans `Canaux/Hub-IA-Plateforme/rag-prep/briefs/`, structuré par question (Q1 à Q7).

**Tonalité** : pragmatique, franche, opérationnelle — ADN QFC. Tu peux être direct sur les écarts détectés, c'est précisément pour ça que tu es sollicité.

**Volume cible** : 1500-3000 mots maximum (Q7 peut dépasser si nécessaire). Pas de complaisance sur les écarts ; densité plutôt que longueur.

---

## Charge cognitive estimée + délai

- Q1 à Q6 : ~30-45 min (relecture des 3 fichiers + réponses synthétiques)
- Q7 : ~15-30 min supplémentaires (réflexion architecturale sur la base de ta connaissance du maillage Hub)
- **Total** : ~45-75 min

**Délai** : pas de date absolue (D-020 du couple 2). À ta disponibilité, mais Blaise nous a indiqué que la vague 2 attend cette revue avant production — donc dès que possible serait apprécié.

---

## Engagement réciproque

À réception de ton retour :
- J'intégrerai immédiatement les corrections sur les 3 fichiers de la vague 1
- Je consoliderai `SPEC-MD-POUR-RAG.md` v1.1 sur la base des anti-patterns identifiés (Q5) + nouvelle dimension architecturale (Q7)
- Selon ta réponse Q7 : production éventuelle de fichiers transverses **avant** la vague 2 (CU-008, PR-07, DEP-02 référenceront ces transverses au lieu de les répéter)
- Item I-002 archivé dans `SYNC-INTER-CANAUX.md` avec apprentissages capitalisés (pattern canonique de coordination)

Toute évolution structurante de `SPEC-MD-POUR-RAG.md` ou de la stratégie de découplage te sera signalée en miroir (axe ascendant couple 2 → couple 1 via Blaise).

---

*Brief produit le 11 mai 2026. Volume : ~1700 mots (dans la cible D-021 ~2000 mots). Item I-002 inscrit dans `SYNC-INTER-CANAUX.md` du couple 2.*

— Cowork Hub IA Plateforme
