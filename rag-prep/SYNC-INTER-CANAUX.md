# SYNC-INTER-CANAUX.md — Coordination couple 1 ↔ couple 2

**Statut :** v0 (initial)
**Dernière mise à jour :** 11 mai 2026
**Garant transverse :** Blaise Cavalli

> **Rôle :** matérialiser les flux de coordination entre le couple 1 (Cowork Hub IA + Claude Code Hub IA — production éditoriale) et le couple 2 (Cowork Hub IA Plateforme + Claude Code Hub IA Plateforme — développement RAG).

> **Principe :** ce fichier est **léger par construction**. Toute décision structurante interne à un couple reste dans ses propres registres. Ne remontent ici que les éléments qui demandent une action de l'autre couple ou qui informent son mode de travail.

---

## Triggers de coordination

### Couple 1 → Couple 2 (descendants)

Le couple 2 doit être informé quand :

1. **Nouvelle itération éditoriale majeure** (v3.9, v4.0…) est planifiée → permet la préparation de la production MD RAG en parallèle
2. **Nouveau contenu HTML produit et mergé** (modules CU/PR/DEP créés ou modifiés) → déclenche production MD associée par couple 2
3. **Évolution de RULES-IMPLEMENTATION.md** qui impacte la structure éditoriale → peut nécessiter alignement de `SPEC-MD-POUR-RAG.md`
4. **Évolution de la cartographie d'ancrage couple 1** (`veille/cartographie-hub-ia.md`) → peut nécessiter alignement de `cartographie-rag.md`

**Mécanisme** : Blaise relaie via une mention courte dans une session Cowork Hub IA Plateforme : *« nouveau contenu côté couple 1 : [liste], priorité [niveau] »*. Le couple 2 inscrit le déclencheur dans `STATUS-RAG.md` ou ouvre une nouvelle tâche.

### Couple 2 → Couple 1 (montants)

Le couple 1 doit être informé quand :

1. **Évolution de `SPEC-MD-POUR-RAG.md`** qui impacte la production de contenu côté couple 1 → notamment si un nouveau champ frontmatter ou une nouvelle convention apparaît qui doit être appliqué dès la prochaine itération éditoriale
2. **Évolution du glossaire canonique** (`rag/content/glossaire.md`) → doit s'aligner avec les gloses de RULES couple 1 §1.3.2 (et vice-versa)
3. **Demande d'assistance contextuelle** sur un module dense (co-production MD) → demande de bande passante
4. **Apprentissage du RAG remontant des questions visiteurs** : si la capture feedback Phase 1 révèle un gap de contenu (question récurrente sans bonne réponse dans le Hub) → signaler au couple 1 comme piste éditoriale potentielle

**Mécanisme** : Blaise relaie. Items consignés ci-dessous dans la section « Items en attente ».

---

## Items en attente

### Items montants (couple 2 → couple 1)

*Aucun en attente.*

---

### Items descendants (couple 1 → couple 2)

#### I-D-001 — Harmonisation matrice PR-07 HTML (6 critères discours vs 8 critères table)

**Émetteur :** couple 1 (Cowork Hub IA)
**Destinataire :** couple 2 (Cowork Hub IA Plateforme)
**Date d'inscription :** 12 mai 2026 (signalé en Q2 du retour I-003)
**Statut :** ouvert (à traiter par couple 1 dans une prochaine itération éditoriale Hub HTML)

**Contenu (résumé) :**
La matrice de décision PR-07 dans le HTML du Hub est désynchronisée entre son discours (« Six critères suffisent ») et sa table (8 critères depuis v3.8 enrichi : critère 7 « Compétences IA-natives » + critère 8 « Coût d'inférence »). À harmoniser dans une prochaine itération corrective ou intégrer dans la prochaine itération éditoriale.

**Action attendue côté couple 1 :** soit corriger la table à 6 critères (revenir à l'état d'avant v3.8), soit corriger le discours pour annoncer 8 critères. Couple 1 consigne cet item de son côté.

**Impact côté couple 2 :** convention « le couple 1 tranche, le couple 2 s'aligne ». Le MD pr-07 reste à 6 critères en attendant. Dès que la décision côté HTML est mergée, refactor du MD pr-07 pour s'aligner (ajout des critères 7 et 8 ou pas).

**Suivi :** à la prochaine notification de merge côté couple 1 sur PR-07, refactor pr-07.md en miroir.

---

---

## Items résolus / archivés

### I-003 — Revue ciblée vague 2 (modules denses CU-008, PR-07, DEP-02) — ✅ CLÔTURÉ

**Émetteur :** couple 2
**Destinataire :** couple 1
**Date d'inscription :** 12 mai 2026
**Date de transmission :** 12 mai 2026
**Date de clôture :** 12 mai 2026 (même jour, traité par couple 1)
**Statut :** ✅ CLÔTURÉ

**Résolution :** Cowork Hub IA a produit le `RETOUR-I-003-REVUE-VAGUE-2.md` (~2600 mots). Verdict : conformité très bonne sur 2 modules sur 3 (CU-008 et DEP-02 = transpositions exemplaires). 1 zone de friction réelle sur PR-07 (5 dérives chiffrées sur la matrice 6 critères + écart structurel 6 vs 8 critères dans HTML v3.8 enrichi). Glossaire OK avec incohérence footer/frontmatter détectée et corrigée.

**Apprentissages capitalisés côté couple 2 :**

1. **Corrections vague 2 effectuées** (4 actions immédiates ~1h15) :
   - Matrice PR-07 : 5 cellules réalignées sur le HTML (volume BUY/BUILD, budget BUY/BUILD, délai BUILD)
   - Wikilinks transverses : `[[vigilance-hallucinations]]` ajouté dans pr-07 Écueil 4 ; `[[vigilance-confidentialite]]` ajouté dans pr-07 Écueil 6 et dans dep-02 (nouvel Écueil 6 transverse)
   - Glossaire footer bumpé v3.8.2 → v3.8.3 (cohérence avec frontmatter)
   - 2 nouveaux chiffres macro canonisés dans `chiffres-macro-2026.md` : 21 % organisations IA workflows redesignés (McKinsey 2025) + 1,8 h/jour temps perdu à chercher l'information (McKinsey 2025). Wikilinks créés depuis pr-07 et cu-008.

2. **SPEC v1.2 publiée** :
   - **R10 nouvelle règle stricte** : transposition fidèle des valeurs numériques dans les tableaux (issue AP-4 du couple 1, promu en règle plutôt qu'anti-pattern documenté). Roadmap audit R10 ajoutée.

3. **D-026 actée** : co-production légère obligatoire sur modules N3/N4 vague 3+ (sondage AVANT production sur 2-3 passages sensibles, plutôt que revue exhaustive a posteriori).

4. **Briques transverses anticipées vague 3** :
   - `pattern-llm-wiki.md` : urgent, recouvrement cu-008/dep-02 confirmé (~30-40 lignes dupliquées)
   - `pattern-eval-set-golden.md` : à produire avec DEP-07
   - `pattern-build-vs-buy.md` : à produire avec module suivant qui s'y réfère

5. **Item descendant inscrit** : I-D-001 (harmonisation matrice PR-07 HTML 6 vs 8 critères, à traiter par couple 1 dans une prochaine itération). Convention « couple 1 tranche, couple 2 s'aligne ».

**Suivi post-clôture :**
- Vault prêt pour ingestion par Claude Code Plateforme (Lots S1 du brief CC-S1)
- Recommandation Cowork Hub IA : ingestion progressive en 2 temps (vague 2 maintenant pour valider pipeline, refactor briques transverses + vague 3 ingérées ensemble dans 2-3 semaines)
- Au prochain module N3/N4 produit (vague 3 — CU-026, CU-027, DEP-08), application de D-026 : sondage préalable Cowork Hub IA sur 2-3 passages sensibles

**Trace temporelle :**
- 12 mai 2026 — inscription dans SYNC-INTER-CANAUX
- 12 mai 2026 — transmission par Blaise au canal Cowork Hub IA
- 12 mai 2026 — réception du retour I-003 (~2600 mots, 5 questions répondues)
- 12 mai 2026 — intégration complète : SPEC v1.2, D-026, chiffres-macro étendu, matrice PR-07 alignée, wikilinks transverses ajoutés, item I-D-001 descendant ouvert

---

### I-002 — Revue de conformité vague 1 + arbitrage architectural découpage sémantique — ✅ CLÔTURÉ

**Émetteur :** couple 2
**Destinataire :** couple 1
**Date d'inscription :** 11 mai 2026
**Date de transmission :** 11 mai 2026
**Date de clôture :** 11 mai 2026 (même jour, traité par couple 1)
**Statut :** ✅ CLÔTURÉ

**Résolution :** Cowork Hub IA a produit le `RETOUR-I-002-REVUE-VAGUE-1.md` (~3100 mots) avec relecture des 3 fichiers vague 1 + 7 réponses structurées. Verdict global : « Conformité globale très bonne ». 4 points de friction identifiés (5 dérives détaillées) + architecture validée pour le compromis « module + transverses sélectifs ».

**Apprentissages capitalisés côté couple 2 :**

1. **Dérives détectées et corrigées** sur cu-001.md (commit séparé) :
   - Chiffre « 67 % » remis en formulation canonique « ne savent pas par où commencer » (vs « n'ont pas commencé »)
   - Conversion monétaire Perplexity Pro $ → € alignée sur HTML
   - Citation MIT 2025 réintégrée dans l'essentiel
   - Certifications ISO 27001 / SOC 2 du Chat Pro restaurées
   - Formulation « 5 minutes du réflexe humain à la matière exploitable » reprise du HTML
   - Phrases trop longues aérées (vigilances passées en liste)

2. **3 anti-patterns intégrés dans SPEC v1.1** :
   - R9 nouvelle règle stricte : citation textuelle des chiffres canoniques (AP-1)
   - AP-2 anti-pattern documenté : conversion monétaire ad-hoc
   - AP-3 anti-pattern documenté : édulcoration éléments contextuels secondaires

3. **3 briques transverses prioritaires produites avant vague 2** (recommandation Q7.a actée immédiatement) :
   - `transverses/chiffres-macro-2026.md` (référentiel canonique de 13 chiffres macro)
   - `transverses/vigilance-hallucinations.md` (~10 modules concernés)
   - `transverses/vigilance-confidentialite.md` (~8 modules concernés)
   - cu-001.md refactorisé pour wikilinker ces 3 briques

4. **D-025 actée** : pattern architectural « unité = module + extraction sélective de transverses » (réponse Q7 couple 1).

5. **On-premise ajouté au glossaire** (13e glose obligatoire RULES §C.2 absente initialement).

**Suivi post-clôture :**
- 7 brain pages transverses prioritaires identifiées (Q7.b) à produire sur 6-12 mois : `pattern-rag-vs-fine-tuning.md`, `pattern-build-vs-buy.md`, `methodologie-prompt-engineering.md`, `cadrage-ai-act-2026.md`, `calendrier-facturation-electronique.md`, `gouvernance-agents-ia.md`, `strategie-souverainete-eu.md`. À produire au fil des modules qui les nécessitent.
- Protocole de double-relecture HTML ↔ MD systématique sur modules denses N3/N4 (recommandation couple 1).
- Glossaire à enrichir pour vague 2 : `eval-set`, `LLM-as-judge`, `reranker`, `retrieval-hybride`, `MTEB`.

**Trace temporelle :**
- 11 mai 2026 — inscription dans SYNC-INTER-CANAUX (item ouvert)
- 11 mai 2026 — transmission par Blaise au canal Cowork Hub IA
- 11 mai 2026 — réception du retour I-002 (3100 mots, 7 questions répondues)
- 11 mai 2026 — intégration complète : SPEC v1.1, D-025, 3 briques transverses produites, vague 1 corrigée, item archivé

---

### I-001 — Opportunité refonte RULES-IMPLEMENTATION.md v1.6 simplifiée — ✅ CLÔTURÉ

**Émetteur :** couple 2 (post-RetEx)
**Destinataire :** couple 1
**Date d'inscription :** 11 mai 2026
**Date de transmission :** 11 mai 2026
**Date de clôture :** 11 mai 2026 (même jour, traité immédiatement par couple 1)
**Statut :** ✅ CLÔTURÉ

**Résolution :** le couple 1 a acknowledgé et traité immédiatement, la fenêtre étant propice (post-v3.8, pas d'itération majeure planifiée) et la dette technique reconnue. 3 livrables produits côté Cowork Hub IA :
- `RULES-IMPLEMENTATION-v1.6.md` (13 règles essentielles en 11 dimensions A.1 à K.1 + annexes)
- `RULES-MIGRATION-v1.5-vers-v1.6.md` (table de mapping exhaustive, filet de sécurité)
- `BRIEF-CLAUDE-CODE-RULES-v1.6.md` (intégration par Claude Code Hub IA sur branche `refactor/rules-v1.6-consolidation`, effort ~1h30)

**Apprentissages partagés vers couple 2 :**
1. Démarrer minimaliste (10-15 règles) — déjà appliqué dans `SPEC-MD-POUR-RAG.md` v1 (8 règles)
2. **Codifier dès la v1 le principe « nouvelle règle = nouvelle fonction d'audit »** → acté par D-023 côté couple 2
3. Distinguer référentiel principal court vs annexes longues — déjà appliqué côté couple 2

**Suivi post-clôture :** attendre notification de merge de la branche v1.6 par couple 1, puis substituer la référence à `RULES-IMPLEMENTATION.md` v1.5.14 par v1.6 dans `_instructions-rag.md` et `BRIEF-CC-S1`.

**Trace temporelle :**
- 11 mai 2026 — inscription dans SYNC-INTER-CANAUX (item ouvert)
- 11 mai 2026 — transmission par Blaise au canal Cowork Hub IA
- 11 mai 2026 — traitement et clôture par couple 1
- 11 mai 2026 — retour reçu, item archivé ici

---

## Conventions de coordination

### Pattern canonique de coordination (codifié post-clôture I-001)

Le pattern suivant, validé empiriquement sur I-001, est désormais la convention canonique de coordination inter-canaux :

```
Item identifié dans un canal (couple 1 ou couple 2)
  ↓
Item structuré et inscrit dans SYNC-INTER-CANAUX.md (numéro + contenu + recommandation + action attendue + statut)
  ↓
Transmis via Blaise vers le canal cible (Blaise relaie le contenu de l'item)
  ↓
Canal cible arbitre, traite ou reporte (acknowledgement explicite obligatoire)
  ↓
Retour structuré vers canal émetteur (livrables + statut + apprentissages partagés le cas échéant)
  ↓
Mise à jour SYNC-INTER-CANAUX.md côté canal émetteur (clôture + archivage)
```

### Règles de fonctionnement des items

1. **Numérotation continue** : I-001, I-002… quel que soit le sens (montant ou descendant).
2. **Format léger** : un item = max 200 mots dans son inscription initiale. Plus dense → brief dédié, pas item.
3. **Pas de date d'échéance interne** (D-020). Items traités selon disponibilité.
4. **Trace temporelle systématique** : inscription, transmission, acknowledgement, traitement, clôture — chaque étape datée.
5. **Apprentissages partagés** : tout traitement d'item peut produire des apprentissages capitalisables pour l'autre canal. Inscrits dans la section « Apprentissages partagés » de la résolution.
6. **Acknowledgement explicite obligatoire** : un item transmis sans retour structuré dans un délai raisonnable est un signal faible (RetEx Q5) — Blaise relance.
7. **Archivage à clôture** : items résolus déplacés dans la section « Items résolus / archivés » avec horodatage complet.

---

## Historique des versions

| Version | Date | Modification |
|---|---|---|
| v0 | 11 mai 2026 | Initialisation + I-001 (opportunité refonte RULES v1.6 couple 1) |
