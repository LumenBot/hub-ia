======================================================================
ÉVAL GOLDEN SET — rapport
======================================================================
Questions : 30
Sources attendues retrouvées : 30/30
Concepts attendus pleinement couverts : 25/30
Score global (source + ≥50% concepts) : 30/30

----------------------------------------------------------------------
✅ q-001 — Qu'est-ce que la veille IA et comment la structurer dans une PME ?
   Sources attendues : ['cu-001']
   Sources citées    : ['cu-001', 'chiffres-macro-2026', 'cu-011', 'cu-025']
   Concepts trouvés  : ['veille', 'source']
   ⚠ concepts absents: ['méthode']
   Extrait réponse   : ## La veille IA en PME : de quoi parle-t-on et comment la structurer ?  ### Ce qu'est la veille IA augmentée  La **veille IA** désigne l'ensemble des pratiques qui consistent à surveiller en continu s
----------------------------------------------------------------------
✅ q-002 — Quelles sont les sources fiables pour suivre l'actualité IA générative en 2026 ?
   Sources attendues : ['cu-001']
   Sources citées    : ['chiffres-macro-2026', 'pr-07', 'cu-001', 'vigilance-hallucinations']
   Concepts trouvés  : ['source', 'veille']
   Extrait réponse   : ## Sources fiables pour suivre l'actualité IA générative en 2026  Le contexte du Hub IA ne contient pas de module dédié à la **veille des sources médias ou académiques** sur l'IA générative. Je n'ai d
----------------------------------------------------------------------
✅ q-003 — Quelle est la différence entre RAG et fine-tuning ?
   Sources attendues : ['cu-008']
   Sources citées    : ['cu-008', 'chiffres-macro-2026']
   Concepts trouvés  : ['retrieval', 'fine-tuning', 'mise à jour']
   Extrait réponse   : ## RAG vs Fine-tuning : deux façons très différentes d'apprendre à un modèle  **Le RAG (Retrieval-Augmented Generation)** consiste à *connecter* le modèle d'IA à une base documentaire externe : à chaq
----------------------------------------------------------------------
✅ q-004 — Comment fonctionne une knowledge base interne avec RAG ?
   Sources attendues : ['cu-008']
   Sources citées    : ['cu-008', 'chiffres-macro-2026']
   Concepts trouvés  : ['retrieval', 'embedding', 'citation']
   Extrait réponse   : ## Comment fonctionne une knowledge base interne avec RAG ?  ### Le principe général  Le RAG (*Retrieval-Augmented Generation* — littéralement « génération augmentée par récupération ») est une archit
----------------------------------------------------------------------
✅ q-005 — Comment arbitrer entre construire en interne ou acheter une solution IA (build vs buy) ?
   Sources attendues : ['pr-07']
   Sources citées    : ['chiffres-macro-2026', 'pr-07']
   Concepts trouvés  : ['build', 'buy', 'coût']
   Extrait réponse   : ## Arbitrer entre Build et Buy en IA : un cadre en 15 minutes  ### La réalité à intégrer avant tout arbitrage  Avant de choisir, prenez acte d'un chiffre structurant : [[chiffres-macro-2026#95-pourcen
----------------------------------------------------------------------
✅ q-006 — Quels critères considérer pour le build vs buy d'une plateforme IA en PME ?
   Sources attendues : ['pr-07']
   Sources citées    : ['pr-07', 'dep-04', 'chiffres-macro-2026']
   Concepts trouvés  : ['arbitrage', 'critère']
   Extrait réponse   : ## Build vs Buy d'une plateforme IA en PME : les critères clés  ### Une décision structurée en 6 critères  Le module [[pr-07]] propose une grille d'arbitrage applicable en 15 minutes, fondée sur six c
----------------------------------------------------------------------
✅ q-007 — Comment mettre un système RAG en production ?
   Sources attendues : ['dep-02']
   Sources citées    : ['dep-02', 'dep-07']
   Concepts trouvés  : ['production', 'évaluation', 'itération']
   Extrait réponse   : ## Mettre un système RAG en production : mode d'emploi  ### La pipeline technique en 7 étapes  Une architecture RAG (Retrieval-Augmented Generation — système qui connecte un LLM à votre base documenta
----------------------------------------------------------------------
✅ q-008 — Qu'est-ce que le cycle Stitch Evaluate Iterate pour le déploiement RAG ?
   Sources attendues : ['dep-02']
   Sources citées    : ['dep-02', 'dep-07']
   Concepts trouvés  : ['stitch', 'evaluate', 'iterate']
   Extrait réponse   : ## Le cycle Stitch → Evaluate → Iterate  ### Pourquoi ce cycle existe-t-il ?  Le point de départ est un constat documenté : **les benchmarks publics (leaderboards) ne prédisent pas la performance d'un
----------------------------------------------------------------------
✅ q-009 — Quelle vector database choisir pour démarrer un POC RAG ?
   Sources attendues : ['outils-vector-db']
   Sources citées    : ['outils-vector-db', 'cu-008', 'dep-02']
   Concepts trouvés  : ['chromadb', 'vector']
   Extrait réponse   : ## Quelle vector database choisir pour démarrer un POC RAG ?  La réponse dépend avant tout d'une question simple : **avez-vous déjà PostgreSQL dans votre infrastructure ?** Si oui, commencez par **pgv
----------------------------------------------------------------------
✅ q-010 — Pinecone, Qdrant, Weaviate ou ChromaDB : sur quels critères choisir ?
   Sources attendues : ['outils-vector-db']
   Sources citées    : ['dep-02', 'outils-vector-db']
   Concepts trouvés  : ['pinecone', 'qdrant', 'weaviate', 'chromadb']
   Extrait réponse   : ## Choisir son vector store : les bons critères  Avant d'entrer dans les détails de chaque outil, retenez un point clé posé dans la documentation du Hub : **la question "quel vector store choisir ?" e
----------------------------------------------------------------------
✅ q-011 — Quels sont les trois outils pour les trois usages distincts de la recherche augmentée IA ?
   Sources attendues : ['cu-001']
   Sources citées    : ['cu-001', 'glossaire', 'vigilance-hallucinations', 'vigilance-confidentialite']
   Concepts trouvés  : ['perplexity', 'mistral', 'notebooklm']
   Extrait réponse   : ## Les trois outils pour les trois usages distincts de la recherche augmentée IA  Le module [[cu-001]] identifie clairement trois outils, chacun conçu pour un type de besoin précis.  **1. Perplexity —
----------------------------------------------------------------------
✅ q-012 — Comment éviter les hallucinations quand on utilise un outil de recherche augmentée comme Perplexity ?
   Sources attendues : ['cu-001', 'vigilance-hallucinations']
   Sources citées    : ['cu-001', 'vigilance-hallucinations']
   Concepts trouvés  : ['hallucination', 'source']
   ⚠ concepts absents: ['vérification']
   Extrait réponse   : ## Éviter les hallucinations avec Perplexity  Perplexity est conçu pour réduire le risque d'hallucination — c'est-à-dire de réponses inventées par le modèle d'IA — grâce à deux atouts structurels : il
----------------------------------------------------------------------
✅ q-013 — Combien d'heures par semaine peut-on gagner avec la recherche augmentée IA en PME ?
   Sources attendues : ['cu-001']
   Sources citées    : ['cu-001', 'chiffres-macro-2026', 'vigilance-hallucinations', 'vigilance-confidentialite']
   Concepts trouvés  : ['heures', 'semaine', 'gain']
   Extrait réponse   : ## Gain de temps avec la recherche augmentée IA en PME  Selon le module dédié à la recherche et veille augmentée, le gain documenté est de **3 à 5 heures par semaine** [[cu-001#L'essentiel à retenir]]
----------------------------------------------------------------------
✅ q-014 — Quels sont les pièges à éviter lors de la mise en place d'un RAG en entreprise ?
   Sources attendues : ['cu-008']
   Sources citées    : ['cu-008', 'dep-02', 'vigilance-confidentialite', 'vigilance-hallucinations']
   Concepts trouvés  : ['garbage', 'droits', 'maintenance', 'hallucination']
   Extrait réponse   : ## Les pièges à éviter lors de la mise en place d'un RAG en entreprise  La mise en place d'un RAG (Retrieval-Augmented Generation — système qui connecte un modèle d'IA à une base documentaire pour qu'
----------------------------------------------------------------------
✅ q-015 — Quelle architecture choisir pour un RAG sur documentation interne stratégique ?
   Sources attendues : ['cu-008']
   Sources citées    : ['cu-008', 'dep-02', 'vigilance-confidentialite']
   Concepts trouvés  : ['a3', 'a4', 'souveraineté']
   Extrait réponse   : ## Architecture RAG pour documentation interne stratégique  ### Le critère décisif : la sensibilité des données  Pour de la **documentation interne stratégique** — procédures, contrats, savoir-faire p
----------------------------------------------------------------------
✅ q-016 — Combien de temps perd-on en moyenne par jour à chercher de l'information dans une organisation ?
   Sources attendues : ['cu-008', 'chiffres-macro-2026']
   Sources citées    : ['chiffres-macro-2026', 'cu-008', 'cu-001']
   Concepts trouvés  : ['mckinsey']
   ⚠ concepts absents: ['1,8 heures']
   Extrait réponse   : ## Combien de temps perd-on à chercher de l'information ?  Selon les données du Hub IA, **1,8 heure par jour est perdue en moyenne à chercher de l'information dans une organisation**, quelle que soit 
----------------------------------------------------------------------
✅ q-017 — Qu'est-ce que le scaling gap dans les projets IA en entreprise ?
   Sources attendues : ['pr-07']
   Sources citées    : ['chiffres-macro-2026', 'pr-07']
   Concepts trouvés  : ['scaling', 'gap', 'workflow', 'redesign']
   Extrait réponse   : ## Le scaling gap : quand l'IA déçoit massivement en entreprise  Le **scaling gap** désigne le fossé entre les ambitions affichées des projets IA en entreprise et leurs résultats réels une fois déploy
----------------------------------------------------------------------
✅ q-018 — Le fine-tuning de petits modèles SLM est-il une alternative au build vs buy en 2026 ?
   Sources attendues : ['pr-07', 'dep-04']
   Sources citées    : ['pr-07', 'chiffres-macro-2026', 'dep-04']
   Concepts trouvés  : ['slm', 'fine-tuning', 'troisième voie']
   Extrait réponse   : ## Le fine-tuning SLM : une troisième voie entre Build et Buy en 2026  Oui, le fine-tuning de petits modèles SLM constitue bien une alternative émergente à l'arbitrage classique Build vs Buy — et c'es
----------------------------------------------------------------------
✅ q-019 — Pourquoi 95 % des projets GenAI ne génèrent-ils pas de ROI mesurable ?
   Sources attendues : ['pr-07', 'chiffres-macro-2026']
   Sources citées    : ['chiffres-macro-2026', 'pr-07']
   Concepts trouvés  : ['95 %', 'roi', 'gouvernance', 'redesign']
   Extrait réponse   : ## Pourquoi 95 % des projets GenAI ne génèrent-ils pas de ROI mesurable ?  **Le chiffre d'abord** : 95 % des projets GenAI déployés en entreprise ne génèrent pas de ROI mesurable — c'est-à-dire aucun 
----------------------------------------------------------------------
✅ q-020 — Quelles sont les 7 étapes d'une pipeline RAG hybride en production ?
   Sources attendues : ['dep-02']
   Sources citées    : ['dep-02', 'vigilance-confidentialite']
   Concepts trouvés  : ['chunking', 'embedding', 'retrieval', 'reranking', 'generation']
   Extrait réponse   : ## Les 7 étapes d'une pipeline RAG hybride en production  Une pipeline RAG hybride (RAG = *Retrieval-Augmented Generation*, c'est-à-dire un système d'IA qui génère ses réponses en allant chercher des 
----------------------------------------------------------------------
✅ q-021 — Comment évaluer la qualité d'un RAG en production ?
   Sources attendues : ['dep-02']
   Sources citées    : ['dep-02']
   Concepts trouvés  : ['eval', 'golden', 'stitch', 'evaluate', 'iterate']
   Extrait réponse   : ## Évaluer la qualité d'un RAG en production  La règle de base est simple : **sans pipeline d'évaluation, vous pilotez à l'aveugle.** Chaque modification de votre système (changement d'embedding, ajus
----------------------------------------------------------------------
✅ q-022 — Quel est l'impact relatif des choix techniques sur la qualité d'un RAG ?
   Sources attendues : ['dep-02']
   Sources citées    : ['dep-02', 'cu-008']
   Concepts trouvés  : ['embedding', 'reranking', 'chunking', 'vector']
   Extrait réponse   : ## Impact relatif des choix techniques sur la qualité d'un RAG  La première bonne nouvelle pour un dirigeant de PME : tous les choix techniques n'ont **pas le même poids**. Le document de référence [[
----------------------------------------------------------------------
✅ q-023 — Quand choisir pgvector plutôt que Qdrant pour un RAG en PME ?
   Sources attendues : ['outils-vector-db']
   Sources citées    : ['outils-vector-db', 'cu-008', 'cu-013', 'dep-02']
   Concepts trouvés  : ['pgvector', 'postgres', 'qdrant']
   Extrait réponse   : ## pgvector vs Qdrant pour un RAG en PME : le critère décisif est votre stack existante  La règle d'or est simple : **si vous avez déjà PostgreSQL en production dans votre système d'information, comme
----------------------------------------------------------------------
✅ q-024 — Quelle vector database choisir pour un RAG souverain en Europe ?
   Sources attendues : ['outils-vector-db']
   Sources citées    : ['outils-vector-db', 'dep-02', 'cu-008']
   Concepts trouvés  : ['souveraineté', 'qdrant', 'self-host', 'eu']
   Extrait réponse   : ## Quelle vector database choisir pour un RAG souverain en Europe ?  **La réponse courte : Qdrant self-hosted est le choix par défaut** pour un RAG souverain en France et en Europe [[outils-vector-db#
----------------------------------------------------------------------
✅ q-025 — Quelle discipline appliquer face aux hallucinations d'un LLM ?
   Sources attendues : ['vigilance-hallucinations']
   Sources citées    : ['vigilance-hallucinations', 'cu-008', 'dep-02', 'glossaire', 'dep-05', 'dep-07']
   Concepts trouvés  : ['vérifier', 'source', 'challenger']
   Extrait réponse   : ## Faire face aux hallucinations d'un LLM : la discipline à adopter  ### Comprendre le phénomène d'abord  Une **hallucination** est une affirmation fausse présentée avec assurance par le modèle — il n
----------------------------------------------------------------------
✅ q-026 — Quelles données ne jamais coller dans un chatbot grand public ?
   Sources attendues : ['vigilance-confidentialite']
   Sources citées    : ['vigilance-confidentialite', 'cu-020', 'pr-05']
   Concepts trouvés  : ['personnelles', 'contractuelles', 'stratégiques', 'régulées']
   Extrait réponse   : ## Quelles données ne jamais coller dans un chatbot grand public ?  La règle de base est simple : tout ce qui concerne votre entreprise de près ou de loin de manière confidentielle ne doit pas être co
----------------------------------------------------------------------
✅ q-027 — Quel pourcentage des organisations IA ont redesigné leurs workflows ?
   Sources attendues : ['chiffres-macro-2026']
   Sources citées    : ['chiffres-macro-2026', 'pr-07']
   Concepts trouvés  : ['21 %', 'mckinsey', 'workflow']
   Extrait réponse   : ## Seulement 21 % des organisations IA ont redesigné leurs workflows  Selon les données canoniques du Hub IA, **21 % seulement des organisations ayant déployé de l'IA ont effectivement redesigné leurs
----------------------------------------------------------------------
✅ q-028 — Qu'est-ce que le pattern LLM Wiki de Karpathy et quand l'utiliser ?
   Sources attendues : ['pattern-llm-wiki']
   Sources citées    : ['pattern-llm-wiki', 'cu-008', 'dep-02']
   Concepts trouvés  : ['karpathy', 'synthèse', 'markdown']
   ⚠ concepts absents: ['persistant']
   Extrait réponse   : ## Le pattern LLM Wiki de Karpathy  **Ce que c'est**  Le **LLM Wiki** est une alternative architecturale au RAG vectoriel classique, proposée par Andrej Karpathy en avril 2026 dans un gist GitHub (17 
----------------------------------------------------------------------
✅ q-029 — Pour un corpus stable de 50K tokens, dois-je choisir un RAG vectoriel ou un LLM Wiki ?
   Sources attendues : ['pattern-llm-wiki', 'dep-02']
   Sources citées    : ['pattern-llm-wiki', 'dep-02', 'cu-008']
   Concepts trouvés  : ['llm wiki', '50k', 'stable']
   ⚠ concepts absents: ['économie']
   Extrait réponse   : ## Réponse directe  **Votre corpus de 50 000 tokens se situe exactement à la frontière du tableau de décision.** Selon [[pattern-llm-wiki#Quand le LLM Wiki bat le RAG vectoriel — tableau de décision]]
----------------------------------------------------------------------
✅ q-030 — Quelles sont les obligations réglementaires à anticiper pour un projet IA en PME en 2026 ?
   Sources attendues : ['pr-07', 'vigilance-confidentialite']
   Sources citées    : ['pr-07', 'chiffres-macro-2026']
   ⚠ manquantes     : ['vigilance-confidentialite']
   Concepts trouvés  : ['rgpd', 'ai act', 'conformité']
   Extrait réponse   : ## Obligations réglementaires à anticiper pour un projet IA en PME en 2026  Le contexte disponible dans le Hub IA identifie **trois calendriers réglementaires majeurs** qui s'imposent aux PME et qui r

Critère brief §9 : ✅ cible atteinte
