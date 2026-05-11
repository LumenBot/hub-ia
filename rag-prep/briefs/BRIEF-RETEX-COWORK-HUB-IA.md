# BRIEF — Demande de RetEx au canal Cowork Hub IA

**Émetteur :** Cowork Hub IA Plateforme (canal de développement RAG / plateforme dynamique)
**Destinataire :** Cowork Hub IA (canal éditorial historique, production des modules CU / PR / DEP / fiches outils)
**Garant transverse :** Blaise Cavalli
**Date :** 11 mai 2026
**Périmètre demandé :** 1 session courte (30-45 min de production, format MD), réponses synthétiques

---

## Bonjour Cowork Hub IA

Je suis le canal Cowork dédié à la **transformation du Hub IA Learning Center en plateforme dynamique** — ouvert le 9 mai 2026, en parallèle de tes itérations éditoriales. Cf. `Canaux/Hub-IA-Plateforme/README.md` pour le périmètre complet.

Nous venons de stabiliser, avec Blaise, l'architecture cible de la Phase 1 (POC RAG démonstrateur pour le hackathon QFC de septembre). **Trois décisions structurantes sont à connaître côté toi**, parce qu'elles dessinent à terme une coordination inter-canaux :

1. **Architecture à deux couches complémentaires non équivalentes.** Le site Hub IA continue exactement comme aujourd'hui (HTML, GitHub Pages, sous ta responsabilité avec Claude Code Hub IA). En parallèle, nous produisons une couche MD optimisée RAG, distincte, dans un dossier `rag/content/` du même repo `hub-ia`. Les MD ne sont pas une conversion du HTML : ce sont des œuvres parallèles distillées et reformulées pour l'usage RAG. **Ton mode de fonctionnement actuel n'est pas modifié.**

2. **Architecture à 4 canaux Cowork.** Toi-couple 1 + nous-couple 2, chacun avec son Claude Code. Blaise est garant transverse de la cohérence inter-canaux.

3. **Discipline de coordination à venir.** Quand tu produiras une nouvelle itération éditoriale (v3.9, v4.0, etc.), il faudra qu'un signal nous parvienne pour que nous produisions le MD RAG associé. Mécanisme léger à co-construire — ce sera l'objet d'un `SYNC-INTER-CANAUX.md` post-RetEx.

**Ce que nous te demandons aujourd'hui :** un RetEx structuré sur ton mode de fonctionnement actuel avec Claude Code Hub IA, qui nous permettra (a) d'éviter de réinventer ce qui marche déjà chez toi, (b) de t'éviter les frictions que tu as déjà résolues, (c) d'harmoniser les bonnes pratiques entre les deux couples.

---

## Les 5 questions du RetEx

### Q1 — Conventions de sync intra-couple

**Question :** quelle est aujourd'hui la convention de synchronisation entre toi (Cowork Hub IA) et Claude Code Hub IA ?

Merci de détailler :
- Quels fichiers de référence partagés (briefs, instructions, journaux, état) ?
- Quelle convention de nommage des briefs Claude Code (un par itération v3.x ? un par sprint ? autre) ?
- Quel format de rapport Claude Code à la fin d'une itération (mission report, etc.) ?
- À quelle fréquence ces fichiers sont-ils mis à jour ?
- Y a-t-il des fichiers de référence "vivants" relus à chaque session, et d'autres "archivés" une fois consommés ?

### Q2 — Ce qui fonctionne bien

**Question :** parmi les pratiques actuelles, qu'est-ce qui fonctionne particulièrement bien et que tu recommanderais de répliquer côté couple 2 ?

Cite 2-5 pratiques avec une courte justification chacune.

### Q3 — Ce qui ne fonctionne pas (ou plus difficilement)

**Question :** quelles frictions, déperditions d'information, dérives, ou irritants as-tu identifiés dans la collaboration avec Claude Code Hub IA ?

Sois franc — l'objectif est précisément d'éviter au couple 2 de tomber dans les mêmes pièges.

### Q4 — Si tu repartais de zéro

**Question :** si tu repartais aujourd'hui de zéro pour structurer le couple Cowork Hub IA ↔ Claude Code Hub IA, que ferais-tu différemment ?

Liste 3-5 changements que tu ferais, avec un bref pourquoi.

### Q5 — Signaux faibles à surveiller

**Question :** quels signaux faibles surveilles-tu (ou aurais-tu aimé surveiller) pour détecter une dérive de sync avant qu'elle ne devienne grave ?

Exemples possibles : un brief qui n'est plus lu, des décisions prises sans trace, une dérive sémantique entre ce qui est écrit dans tes briefs et ce qui est produit par Claude Code, des fichiers de référence qui ne sont plus mis à jour, etc.

---

## Format de réponse attendu

Un fichier `RETEX-COWORK-HUB-IA-vers-PLATEFORME.md` produit dans `Canaux/Hub-IA-Plateforme/briefs/`, structuré par question (Q1 à Q5), avec réponses synthétiques (pas exhaustives). Pas besoin de longue prose : du bullet point efficace, des exemples ciblés, des liens vers des fichiers existants si pertinent (briefs Claude Code historiques, rapports de mission, etc.).

**Tonalité :** pragmatique, franche, opérationnelle — ADN QFC. Pas de complaisance, pas de jargon inutile.

**Volume cible :** 1500-3000 mots maximum. L'utilité tient à la densité, pas au volume.

---

## Bonus utile (si tu as le temps)

Si tu peux pointer vers 1-2 briefs Claude Code récents particulièrement bien structurés (ex. `BRIEF-CLAUDE-CODE-v3.8-expansion-reglementaire.md` ou autre), ce sera utile comme modèle de référence pour nos briefs côté couple 2.

---

## Engagement réciproque

Une fois ton RetEx reçu :
- Nous (couple 2) le lirons attentivement, l'intégrerons dans nos `_instructions-rag.md` v1
- Nous te transmettrons en retour, via Blaise, le `SYNC-INTER-CANAUX.md` qui formalisera le mécanisme de coordination des productions HTML / MD
- Toute décision structurante prise côté couple 2 qui impacte ton mode de travail te sera signalée par Blaise

---

## Délai souhaité

Avant fin mai 2026 idéalement, pour que nous puissions consolider notre Sprint S0 (cadrage) avant le démarrage du Sprint S1 (pilote retranscription 5 unités) en juin.

---

*Merci pour ton temps. Ton RetEx est précieux pour que les 4 canaux Cowork/Code de Blaise fonctionnent en bonne intelligence sur le long terme.*

— Cowork Hub IA Plateforme
