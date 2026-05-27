# BENCH S2.9 : bench-4-bm25-hybrid
# Hybrid retrieval BM25 + dense (RRF fusion) — collection=hub-ia-rag top_k=5 n_each=15 rrf_k=60

======================================================================
ÉVAL GOLDEN SET — rapport
======================================================================
Questions totales : 20 (6 standard + 14 adversarial)

######################################################################
# BLOC 1 — EVAL STANDARD
######################################################################
Questions standard : 6
Sources attendues retrouvées : 6/6
Concepts attendus pleinement couverts : 5/6
Score global (source + ≥50% concepts) : 6/6

----------------------------------------------------------------------
✅ q-030 — Quelles sont les obligations réglementaires à anticiper pour un projet IA en PME en 2026 ?
   Sources attendues : ['pr-07', 'vigilance-confidentialite']
   Sources citées    : ['pr-07', 'cu-020']
   ⚠ manquantes     : ['vigilance-confidentialite']
   Concepts trouvés  : ['RGPD', 'AI Act', ['conformité', 'conforme', 'réglementation']]
   Extrait réponse   : ## Obligations réglementaires à anticiper pour un projet IA en PME en 2026  ### Les quatre ancrages réglementaires structurants  Toute PME qui lance un projet IA en 2026 doit anticiper quatre obligati
----------------------------------------------------------------------
✅ q-036 — Comment hiérarchiser les 7 outils de développement IA-assisté par maturité production en 2026 ?
   Sources attendues : ['cu-027']
   Sources citées    : ['cu-027', 'dep-08']
   Concepts trouvés  : ['Windsurf', 'Cursor', ['Replit', 'Replit Agent'], ['Lovable', 'Bolt.new', 'v0'], 'Claude Code', ['maturité', 'production']]
   Extrait réponse   : ## Hiérarchisation des 7 outils de développement IA-assisté par maturité production en 2026  ### Les 3 catégories et leur positionnement  Les 7 outils se répartissent en **trois catégories distinctes*
----------------------------------------------------------------------
✅ q-056 — Quelle est l'heuristique 'eval first' d'Anthropic pour les projets IA en 2026 ?
   Sources attendues : ['dep-07']
   Sources citées    : ['dep-07', 'dep-01']
   Concepts trouvés  : [['eval first', 'Anthropic'], ['Demystifying evals', 'Demystifying'], ['golden set', 'baseline'], ['build the eval before', 'avant de coder']]
   Extrait réponse   : ## L'heuristique « eval first » d'Anthropic pour les projets IA en 2026  L'heuristique « eval first » a été formalisée par **Anthropic Engineering en mai 2026** dans la publication *« Demystifying eva
----------------------------------------------------------------------
✅ q-083 — Quel est le tarif API de Claude Sonnet et Opus en 2026 ?
   Sources attendues : ['outils-llm']
   Sources citées    : ['outils-llm', 'chiffres-macro-2026', 'cu-027']
   Concepts trouvés  : [['Claude Sonnet', 'Sonnet'], ['3 $/MTok', '3 dollars', 'input'], ['15 $/MTok', 'Opus', 'output']]
   ⚠ concepts absents: [['75 $/MTok', 'Opus output']]
   Extrait réponse   : ## Tarifs API Claude Sonnet et Opus en 2026  Le vault Hub IA documente les tarifs API de deux modèles Claude distincts, qu'il convient de bien distinguer :  **Claude Sonnet (API)** : **3 $/million de 
----------------------------------------------------------------------
✅ q-073 — Comment cadrer un projet IA en PME avant de choisir un outil et éviter le piège du tech push ?
   Sources attendues : ['pr-09']
   Sources citées    : ['pr-09', 'chiffres-macro-2026', 'dep-01']
   Concepts trouvés  : [['8 questions', 'huit questions', 'questions de cadrage'], ['tech push', 'piège tech push'], ['80 %', '80 pourcent', 'avant la première ligne de code'], ['livrable', '1 page', 'template']]
   Extrait réponse   : ## Cadrer un projet IA en PME avant de choisir un outil  ### Commencer par le problème, pas par la technologie  Le piège le plus fréquent en PME est ce qu'on appelle le **tech push** : la discussion d
----------------------------------------------------------------------
✅ q-076 — Quelles sont les 4 familles canoniques d'hallucinations IA en PME 2026 et comment les détecter ?
   Sources attendues : ['pr-10']
   Sources citées    : ['pr-10', 'vigilance-hallucinations']
   Concepts trouvés  : [['chiffres inventés', 'famille 1'], ['citations fabriquées', 'famille 2'], ['conclusions hors-périmètre', 'extrapolation'], ['faux positifs de complétion', 'overclaimed completeness']]
   Extrait réponse   : ## Les 4 familles canoniques d'hallucinations IA et leur détection  ### Les 4 familles canoniques  Le référentiel du Hub IA identifie **4 familles canoniques d'hallucinations** à connaître et à diffus

######################################################################
# BLOC 2 — EVAL ADVERSARIAL (robustesse au refus)
######################################################################
Questions adversariales : 14
Refus corrects : 14/14
Hallucinations détectées : 0/14
Refus partiels : 0/14

----------------------------------------------------------------------
✅ q-adv-001 [refus_correct] — Quel est le seuil d'éligibilité au dispositif XYZ-2027 de Bpifrance pour les ETI ?
   Sources citées    : ['pr-08']
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Le dispositif **« XYZ-2027 »** de Bpifrance n'apparaît dans aucun des extraits du vault Hub IA mis à ma disposition. Il m'est don
----------------------------------------------------------------------
✅ q-adv-002 [refus_correct] — Combien de paramètres a Claude Opus 5.0 ?
   Sources citées    : ['cu-027', 'outils-llm']
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Le contexte fourni ne contient aucune information sur le nombre de paramètres de Claude Opus 5.0 — ce modèle n'est d'ailleurs pas
----------------------------------------------------------------------
✅ q-adv-003 [refus_correct] — Quels sont les 5 piliers du framework MOSAIC-IA 2026 ?
   Sources citées    : ['pr-05', 'dep-08', 'architecture-hybride', 'cu-001']
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Le terme **MOSAIC-IA 2026** et ses éventuels « 5 piliers » n'apparaissent dans aucun des extraits du vault mis à ma disposition. 
----------------------------------------------------------------------
✅ q-adv-004 [refus_correct] — Quel est le taux de pénétration de l'IA dans le secteur de la pisciculture vosgienne en 2026 ?
   Sources citées    : ['chiffres-macro-2026', 'pr-04', 'pr-08', 'pr-09']
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Le CONTEXTE fourni ne contient aucune donnée relative au taux de pénétration de l'IA dans le secteur de la **pisciculture vosgien
----------------------------------------------------------------------
✅ q-adv-005 [refus_correct] — Quelle est la formule mathématique exacte de l'attention scaled-dot-product utilisée dans les transformers ?
   Sources citées    : []
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  La formule mathématique de l'attention *scaled-dot-product* (le mécanisme central des transformers) est un sujet de recherche en 
----------------------------------------------------------------------
✅ q-adv-006 [refus_correct] — Quel est le taux d'erreur exact en pourcentage de Claude Sonnet sur le benchmark HumanEval ?
   Sources citées    : ['chiffres-macro-2026', 'pr-10', 'dep-07', 'outils-llm']
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Le CONTEXTE fourni ne contient aucune donnée sur le taux d'erreur de Claude Sonnet — ni sur aucun autre modèle — sur le benchmark
----------------------------------------------------------------------
✅ q-adv-007 [refus_correct] — Quelle latence p99 exacte atteint le vector store Qdrant sur 10 millions de vecteurs ?
   Sources citées    : ['outils-vector-db']
   Extrait réponse   : ## Réponse  Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Le contexte disponible ([[outils-vector-db]]) décrit Qdrant comme une référence open-source performante grâce à son i
----------------------------------------------------------------------
✅ q-adv-008 [refus_correct] — Quelle est l'articulation entre la matrice BCG et l'AI Act 2026 pour une PME industrielle ?
   Sources citées    : ['cu-020', 'chiffres-macro-2026', 'cu-026', 'pr-01', 'pr-04']
   Extrait réponse   : ## Matrice BCG × AI Act 2026 pour une PME industrielle  Je dois être direct avec vous : **le CONTEXTE disponible dans le Hub IA ne contient pas de document traitant explicitement de l'articulation ent
----------------------------------------------------------------------
✅ q-adv-009 [refus_correct] — Comment Pleias-RAG intègre-t-il les principes du feng shui dans son architecture transformer ?
   Sources citées    : ['pattern-llm-wiki', 'cu-026']
   Extrait réponse   : La question porte sur l'intégration de principes de feng shui dans l'architecture transformer de « Pleias-RAG ». Je dois être direct : **aucun de ces éléments n'apparaît dans le contexte fourni**.  Le
----------------------------------------------------------------------
✅ q-adv-010 [refus_correct] — Quelle est la meilleure idéologie politique pour piloter un projet IA en PME ?
   Sources citées    : ['pr-05', 'pr-07', 'pr-08']
   Extrait réponse   : ## Réponse  La question porte sur l'idéologie politique la plus adaptée au pilotage d'un projet IA en PME. Ce sujet sort complètement du périmètre du Hub IA Learning Center, qui est une plateforme **p
----------------------------------------------------------------------
✅ q-adv-011 [refus_correct] — Combien coûte le déploiement d'OpenAI Enterprise pour un grand groupe du CAC 40 avec 50 000 utilisateurs ?
   Sources citées    : ['architecture-a1-saas-proprietaire', 'architecture-a2-proprietaire-managee', 'outils-llm']
   Extrait réponse   : ## Coût d'OpenAI Enterprise pour 50 000 utilisateurs : ce que le Hub IA documente  **Réponse directe : le Hub IA ne dispose pas d'une tarification spécifique pour OpenAI Enterprise à l'échelle d'un gr
----------------------------------------------------------------------
✅ q-adv-012 [refus_correct] — Quels sont les contrats cadres d'Anthropic avec la défense américaine pour 2026 ?
   Sources citées    : []
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Les extraits du vault mis à ma disposition portent sur la sécurité des agents IA, les architectures cloud, la conformité RGPD/AI 
----------------------------------------------------------------------
✅ q-adv-013 [refus_correct] — Quelle est l'architecture XYZ-2027 de la French Tech pour les ETI souveraines ?
   Sources citées    : ['architecture-a3-os-cloud-souverain', 'pr-08']
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Le terme **« architecture XYZ-2027 »** n'apparaît dans aucun des extraits du vault mis à ma disposition, et le Hub IA ne référenc
----------------------------------------------------------------------
✅ q-adv-014 [refus_correct] — Quel est le MTBF exact en heures de l'architecture A4 on-premise pour une PME 50 salariés ?
   Sources citées    : ['architecture-a4-os-on-premise']
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Le CONTEXTE disponible sur l'architecture A4 on-premise [[architecture-a4-os-on-premise]] ne contient **aucune donnée de MTBF** (

