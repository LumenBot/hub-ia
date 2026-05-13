======================================================================
ÉVAL GOLDEN SET — rapport
======================================================================
Questions : 15
Sources attendues retrouvées : 9/15
Concepts attendus pleinement couverts : 11/15
Score global (source + ≥50% concepts) : 9/15

----------------------------------------------------------------------
✅ q-016 — Combien de temps perd-on en moyenne par jour à chercher de l'information dans une organisation ?
   Sources attendues : ['cu-008', 'chiffres-macro-2026']
   Sources citées    : ['cu-008', 'cu-001']
   ⚠ manquantes     : ['chiffres-macro-2026']
   Concepts trouvés  : ['mckinsey']
   ⚠ concepts absents: ['1,8 heures']
   Extrait réponse   : ## Temps perdu à chercher l'information : que dit la recherche ?  Selon McKinsey (2025), **un collaborateur perd en moyenne 1,8 heure par jour à chercher de l'information** dans une organisation moyen
----------------------------------------------------------------------
✅ q-017 — Qu'est-ce que le scaling gap dans les projets IA en entreprise ?
   Sources attendues : ['pr-07']
   Sources citées    : ['pr-07']
   Concepts trouvés  : ['scaling', 'gap', 'workflow', 'redesign']
   Extrait réponse   : ## Le scaling gap : quand la promesse IA se heurte à la réalité opérationnelle  Le **scaling gap** désigne l'écart massif qui existe entre l'adoption de l'IA en entreprise et la capacité à en tirer un
----------------------------------------------------------------------
✅ q-018 — Le fine-tuning de petits modèles SLM est-il une alternative au build vs buy en 2026 ?
   Sources attendues : ['pr-07', 'dep-04']
   Sources citées    : ['dep-04', 'pr-07']
   Concepts trouvés  : ['slm', 'fine-tuning', 'troisième voie']
   Extrait réponse   : ## Le fine-tuning SLM : une troisième voie entre Build et Buy  Oui, en 2026, le fine-tuning de petits modèles SLM s'affirme explicitement comme **une troisième option** dans l'arbitrage Build vs Buy —
----------------------------------------------------------------------
✅ q-019 — Pourquoi 95 % des projets GenAI ne génèrent-ils pas de ROI mesurable ?
   Sources attendues : ['pr-07', 'chiffres-macro-2026']
   Sources citées    : ['pr-07']
   ⚠ manquantes     : ['chiffres-macro-2026']
   Concepts trouvés  : ['95 %', 'roi', 'gouvernance', 'redesign']
   Extrait réponse   : ## Pourquoi 95 % des projets GenAI ne génèrent-ils pas de ROI mesurable ?  La réponse courte : **ce n'est pas un problème de technologie, c'est un problème de méthode et d'organisation.** Selon le MIT
----------------------------------------------------------------------
✅ q-020 — Quelles sont les 7 étapes d'une pipeline RAG hybride en production ?
   Sources attendues : ['dep-02']
   Sources citées    : ['dep-02']
   Concepts trouvés  : ['chunking', 'embedding', 'retrieval', 'reranking', 'generation']
   Extrait réponse   : ## Les 7 étapes d'une pipeline RAG hybride en production  Voici l'anatomie complète telle que définie dans le référentiel Hub IA — « ton prestataire doit te les réciter sans hésiter » [[dep-02#RAG hyb
----------------------------------------------------------------------
❌ q-021 — Comment évaluer la qualité d'un RAG en production ?
   Sources attendues : ['dep-02']
   Sources citées    : []
   ⚠ manquantes     : ['dep-02']
   Concepts trouvés  : ['eval', 'golden', 'stitch', 'evaluate', 'iterate']
   Extrait réponse   : ## Évaluer la qualité d'un RAG en production  La règle de base est simple : **sans pipeline d'évaluation, tu ne sais pas si une modification améliore ou dégrade ton système** — tout choix devient subj
----------------------------------------------------------------------
❌ q-022 — Quel est l'impact relatif des choix techniques sur la qualité d'un RAG ?
   Sources attendues : ['dep-02']
   Sources citées    : []
   ⚠ manquantes     : ['dep-02']
   Concepts trouvés  : ['embedding', 'reranking', 'chunking', 'vector']
   Extrait réponse   : ## Impact relatif des choix techniques sur la qualité d'un RAG  La question centrale n'est pas « quelles briques choisir ? » mais **dans quel ordre concentrer son attention**. Tous les choix technique
----------------------------------------------------------------------
✅ q-023 — Quand choisir pgvector plutôt que Qdrant pour un RAG en PME ?
   Sources attendues : ['outils-vector-db']
   Sources citées    : ['dep-02', 'cu-008', 'outils-vector-db']
   Concepts trouvés  : ['pgvector', 'postgres', 'qdrant']
   Extrait réponse   : ## pgvector ou Qdrant pour votre RAG en PME ?  La réponse courte : **commencez par pgvector si vous avez déjà PostgreSQL, passez à Qdrant dès que vous montez en volume ou en exigence de production.** 
----------------------------------------------------------------------
✅ q-024 — Quelle vector database choisir pour un RAG souverain en Europe ?
   Sources attendues : ['outils-vector-db']
   Sources citées    : ['outils-vector-db']
   Concepts trouvés  : ['souveraineté', 'qdrant', 'self-host', 'eu']
   Extrait réponse   : ## Quelle vector database pour un RAG souverain en Europe ?  **La réponse courte : Qdrant en self-hosting.**  Pour un RAG souverain — c'est-à-dire un système où vos données restent hébergées sur le so
----------------------------------------------------------------------
❌ q-025 — Quelle discipline appliquer face aux hallucinations d'un LLM ?
   Sources attendues : ['vigilance-hallucinations']
   Sources citées    : ['cu-008', 'dep-02', 'dep-05', 'dep-07']
   ⚠ manquantes     : ['vigilance-hallucinations']
   Concepts trouvés  : ['vérifier', 'source']
   ⚠ concepts absents: ['challenger']
   Extrait réponse   : ## Faire face aux hallucinations d'un LLM : la discipline à adopter  ### Comprendre d'abord ce qu'est une hallucination  Une **hallucination** est une affirmation fausse présentée avec assurance par u
----------------------------------------------------------------------
❌ q-026 — Quelles données ne jamais coller dans un chatbot grand public ?
   Sources attendues : ['vigilance-confidentialite']
   Sources citées    : ['cu-007', 'cu-008', 'cu-020', 'cu-024', 'cu-002', 'cu-005', 'pr-05']
   ⚠ manquantes     : ['vigilance-confidentialite']
   Concepts trouvés  : ['personnelles', 'contractuelles', 'stratégiques']
   ⚠ concepts absents: ['régulées']
   Extrait réponse   : ## Données à ne jamais coller dans un chatbot grand public  La règle de base est simple : un chatbot grand public (ChatGPT, Gemini, Perplexity en version gratuite, etc.) envoie toutes vos saisies vers
----------------------------------------------------------------------
❌ q-027 — Quel pourcentage des organisations IA ont redesigné leurs workflows ?
   Sources attendues : ['chiffres-macro-2026']
   Sources citées    : ['pr-07']
   ⚠ manquantes     : ['chiffres-macro-2026']
   Concepts trouvés  : ['21 %', 'mckinsey', 'workflow']
   Extrait réponse   : ## Redesign des workflows IA : où en sont les organisations ?  **21 % seulement des organisations ayant adopté l'IA ont effectivement redesigné leurs workflows.** [[chiffres-macro-2026#21-pourcent-org
----------------------------------------------------------------------
❌ q-028 — Qu'est-ce que le pattern LLM Wiki de Karpathy et quand l'utiliser ?
   Sources attendues : ['pattern-llm-wiki']
   Sources citées    : ['cu-014', 'dep-02', 'cu-008']
   ⚠ manquantes     : ['pattern-llm-wiki']
   Concepts trouvés  : ['karpathy', 'synthèse', 'persistant', 'markdown']
   Extrait réponse   : ## Le pattern LLM Wiki de Karpathy  **Ce que c'est**  Le **LLM Wiki** est une alternative architecturale au RAG vectoriel classique, proposée par Andrej Karpathy en avril 2026 dans un gist GitHub (17 
----------------------------------------------------------------------
✅ q-029 — Pour un corpus stable de 50K tokens, dois-je choisir un RAG vectoriel ou un LLM Wiki ?
   Sources attendues : ['pattern-llm-wiki', 'dep-02']
   Sources citées    : ['cu-008', 'dep-02']
   ⚠ manquantes     : ['pattern-llm-wiki']
   Concepts trouvés  : ['llm wiki', '50k', 'stable']
   ⚠ concepts absents: ['économie']
   Extrait réponse   : ## LLM Wiki ou RAG vectoriel pour 50 000 tokens stables ?  **La réponse est claire : le LLM Wiki est recommandé en priorité.** Pour un corpus de 50 000 tokens avec une stabilité élevée (mises à jour t
----------------------------------------------------------------------
✅ q-030 — Quelles sont les obligations réglementaires à anticiper pour un projet IA en PME en 2026 ?
   Sources attendues : ['pr-07', 'vigilance-confidentialite']
   Sources citées    : ['pr-07']
   ⚠ manquantes     : ['vigilance-confidentialite']
   Concepts trouvés  : ['rgpd', 'ai act', 'conformité']
   Extrait réponse   : ## Obligations réglementaires à anticiper pour un projet IA en PME en 2026  Le contexte disponible dans le Hub IA identifie **trois calendriers réglementaires concrets** qui s'imposent aux PME et qui 

Critère brief §9 : ✅ cible atteinte
