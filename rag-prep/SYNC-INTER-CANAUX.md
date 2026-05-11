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

### Items descendants (couple 1 → couple 2)

*Aucun en attente. Premier item probable : signal de nouvelle itération éditoriale v3.9 ou v4.0 par couple 1, ou notification de merge de la branche `refactor/rules-v1.6-consolidation` (suite item I-001).*

---

## Items résolus / archivés

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
