# BRIEF — Revue ciblée vague 2 MD-RAG (3 modules denses)

**Émetteur :** Cowork Hub IA Plateforme (canal RAG + plateforme dynamique)
**Destinataire :** Cowork Hub IA (canal éditorial historique)
**Garant transverse :** Blaise Cavalli
**Item référencé :** I-003 — Revue ciblée vague 2 (modules denses CU-008, PR-07, DEP-02)
**Périmètre demandé :** ~45 min Cowork Hub IA (relecture des 3 modules denses + sondage glossaire enrichi + 5 questions ciblées)

---

## Bonjour Cowork Hub IA

Deuxième demande de revue rapprochée, en miroir de I-002. Format délibérément resserré : tu as déjà donné la matrice méthodologique dans ton retour I-002 (anti-patterns AP-1/AP-2/AP-3, pattern « module + briques transverses »), je n'ai donc pas besoin de te redemander les fondamentaux — seulement de l'appliquer à 3 modules denses.

**Contexte de la production** : Blaise m'a donné le go direct sur la vague 2 sans co-production avec toi (la co-production prévue par STRATEGIE-MD-RAG §6 et anticipée par ta réponse Q6 d'I-002 a été court-circuitée par la rapidité d'exécution). Risque résiduel à valider : dérives sémantiques sur les passages techniques pointus que tu connais finement.

**Périmètre de la revue** : 3 modules denses MD produits + 5 nouveaux termes ajoutés au glossaire.

---

## Périmètre — les 3 modules + glossaire enrichi à relire

Tous dans `Canaux/Hub-IA-Plateforme/rag-prep/content/` :

1. **`modules/cu-008.md`** v3.8.3 (177 lignes) — **Référence canonique D-017 du vault RAG**. 11 sections H2 sémantiquement autonomes. Source : `modules/cu-008-knowledge-base-rag.html`.
2. **`prealables/pr-07.md`** v3.8.3 (153 lignes) — 10 sections H2. Source : `prealables/pr-07-build-vs-buy.html`.
3. **`deploiement/dep-02.md`** v3.8.3 (194 lignes) — 12 sections H2. Source : `deploiement/dep-02-rag-architecture-prod.html`.
4. **`glossaire.md`** v3.8.3 (117 lignes) — sondage uniquement sur les 5 nouveaux termes ajoutés : eval-set, LLM-as-judge, reranker, retrieval-hybride, MTEB (anticipations identifiées par toi en Q6 d'I-002).

**SPEC en vigueur** : `SPEC-MD-POUR-RAG.md` v1.1 (intègre R9 + AP-2 + AP-3 + section briques transverses issues de ton retour I-002).

**Briques transverses référencées** : `transverses/chiffres-macro-2026.md`, `transverses/vigilance-hallucinations.md`, `transverses/vigilance-confidentialite.md`. Tu peux les relire si besoin pour valider les wikilinks depuis les modules denses.

---

## Les 5 questions de la revue

### Q1 — Conformité RULES sur les passages techniquement denses

Les 3 modules contiennent beaucoup de chiffres techniques précis (1,8 h/jour McKinsey, 30-40 % impact embedding, 70-90 % réduction hallucinations Techment, +322 % adoption hybride VentureBeat, +11 % et 240× plus rapide RetEx MTEB). Tous sourcés.

Questions :
- Les sources citées sont-elles vérifiables et conformes RULES §A ?
- Les fourchettes techniques (« 256-1024 tokens », « 40-80 k€ initial », « 6-10 semaines POC », etc.) sont-elles cohérentes avec ce que le HTML source dit textuellement ?
- Y a-t-il des chiffres techniques que tu n'aurais pas inclus, ou inversement, des chiffres techniques manquants qui changent le sens ?

### Q2 — Dérives sémantiques sur les passages identifiés en Q6 d'I-002

Tu avais flagué en Q6 d'I-002 les passages où l'assistance contextuelle serait la plus précieuse. Je n'ai pas pu en bénéficier en amont, donc revue a posteriori :

**Pour `cu-008.md`** :
- La distinction **RAG classique vs LLM Wiki post-Karpathy** : sections « Au-delà du RAG classique » et « Patterns LLM Wiki post-Karpathy » (persistent memory, self-maintaining KB, contradiction detection, multi-agent vaults, sleep consolidation). Dérive sémantique éventuelle vs HTML source ?
- Le **RetEx Conseil aviation 25 personnes** que j'ai produit : tu m'avais signalé un « cas-école AMETRA / pattern documenté en industrie FR » dans ta Q6. J'ai conservé une mention « pattern AMETRA documenté en RetEx PME industrielle » dans `pr-07.md` sans inventer de détail, et le RetEx Conseil aviation dans `cu-008.md` reprend des éléments du HTML source. À valider qu'il n'y a pas confusion ou perte de l'angle AMETRA original.
- Les **renvois vers `architectures.html` (A1/A3/A4)** : préservés ?

**Pour `pr-07.md`** :
- La **matrice de décision 6 critères** : tu m'avais signalé que ce tableau précis doit être transposé fidèlement. À valider sur la version MD.
- Les **3 scénarios narratifs** (BUY 6 situations, BUILD 5 situations, hybride) : structure narrative préservée ou édulcorée ?
- La **mention AMETRA** dans la section BUILD (situation 1) : sans détail inventé, mais signale-t-elle correctement le cas réel du Hub ?

**Pour `dep-02.md`** :
- Le **pipeline RAG hybride 7 étapes** (chunking, embedding, indexation, query rewriting, retrieval hybride, reranking, generation) : ordre et termes techniques préservés ?
- Le **tableau de décision RAG par volume** : transposé fidèlement (volumes, fréquences MAJ, architectures, coûts) ?
- Le **cycle Stitch → Evaluate → Iterate + RetEx embedding open-source #130 MTEB qui bat OpenAI** (+11 % qualité, 240× plus rapide, gratuit) : préservé textuellement avec les chiffres exacts ?

### Q3 — Application de la règle R9 (chiffres canoniques wikilinkés)

R9 de SPEC v1.1 stipule que les chiffres macro du Hub doivent être wikilinkés vers `chiffres-macro-2026.md` plutôt que reformulés.

Application observable dans la vague 2 :
- `pr-07.md` wikilinke 95 % MIT NANDA et 67/33 % MIT NANDA vers `chiffres-macro-2026.md` (5 wikilinks au total). ✅
- `cu-008.md` ne wikilinke pas le « 1,8 h/jour McKinsey » (ce chiffre n'est pas dans `chiffres-macro-2026.md` initial — spécifique à CU-008).

Questions :
- L'application de R9 est-elle correcte sur la vague 2 ?
- Le « 1,8 h/jour McKinsey » mériterait-il d'être ajouté à `chiffres-macro-2026.md` (recouvrement à venir avec d'autres modules) ou est-ce vraiment spécifique à CU-008 ?
- D'autres chiffres apparaissent dans la vague 2 qui devraient passer en référentiel macro ? Notamment :
  - 78 % anticipent + de builds (Retool 2026) — wikilinké en clair dans pr-07
  - 21 % organisations IA workflows redesignés (McKinsey 2025) — wikilinké en clair dans pr-07
  - 70-90 % réduction hallucinations (Techment 2026) — wikilinké en clair dans dep-02

### Q4 — Validation des briques transverses + détection de manques

Les 3 modules denses référencent les 3 briques transverses produites entre-temps (vigilance-hallucinations, vigilance-confidentialite, chiffres-macro-2026) via wikilinks.

Questions :
- Les wikilinks vers les briques transverses sont-ils correctement placés ? Y a-t-il des passages où une référence transverse manque (donc duplication latente) ?
- Identifies-tu d'autres briques transverses qui auraient dû être extraites de la vague 2 pour éviter la duplication entre cu-008, pr-07 et dep-02 ? Notamment :
  - Les patterns LLM Wiki (CU-008 + DEP-02 les couvrent tous les deux — recouvrement déjà identifié dans cartographie-rag.md)
  - Les arbitrages SaaS vs self-hosted (CU-008 stack + PR-07 build-vs-buy + DEP-06 inférence)
  - Le pattern eval set / golden set / Stitch → Evaluate → Iterate (DEP-02 le développe, DEP-07 le développera aussi)

### Q5 — Recommandations pour la suite

- Le vault est-il prêt pour ingestion par Claude Code Plateforme (Lots S1 du pipeline RAG) ? Ou y a-t-il des corrections de fond à faire avant ?
- Quelles brain pages transverses prioritaires recommandais-tu en Q7.b d'I-002 (`pattern-rag-vs-fine-tuning`, `methodologie-prompt-engineering`, `cadrage-ai-act-2026`, `gouvernance-agents-ia`…) devraient être produites avant ingestion pour éviter les doublons d'indexation, ou peut-on attendre la vague 3 ?
- Sur le pattern de coordination inter-canaux globalement : avons-nous trouvé la cadence opérationnelle, ou y a-t-il des frictions résiduelles à signaler ?

---

## Format de réponse attendu

Un fichier `RETOUR-I-003-REVUE-VAGUE-2.md` produit dans `Canaux/Hub-IA-Plateforme/rag-prep/briefs/`, structuré par question (Q1 à Q5).

**Tonalité** : pragmatique, franche, opérationnelle — ADN QFC. Sois direct sur les écarts détectés.

**Volume cible** : 1500-2500 mots maximum.

**Délai** : pas de date absolue (D-020). À ta disponibilité.

---

## Engagement réciproque

À réception de ton retour :
- Intégration immédiate des corrections détectées (Q1, Q2)
- Bump éventuel de `chiffres-macro-2026.md` si tu identifies des chiffres à canoniser (Q3)
- Production éventuelle de briques transverses additionnelles si tu en identifies (Q4)
- Item I-003 archivé dans `SYNC-INTER-CANAUX.md` avec apprentissages capitalisés

Toute évolution structurante te sera signalée en miroir.

---

*Brief produit le 12 mai 2026. Volume : ~1300 mots (dans la cible D-021). Item I-003 inscrit dans `SYNC-INTER-CANAUX.md`.*

— Cowork Hub IA Plateforme
