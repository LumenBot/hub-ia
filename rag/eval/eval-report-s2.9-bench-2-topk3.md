# BENCH S2.9 : bench-2-topk3
# top_k=3  embed=text-embedding-3-small  gen=claude-sonnet-4-6  collection=hub-ia-rag

======================================================================
ÉVAL GOLDEN SET — rapport
======================================================================
Questions totales : 20 (6 standard + 14 adversarial)

######################################################################
# BLOC 1 — EVAL STANDARD
######################################################################
Questions standard : 6
Sources attendues retrouvées : 4/6
Concepts attendus pleinement couverts : 4/6
Score global (source + ≥50% concepts) : 4/6

----------------------------------------------------------------------
✅ q-030 — Quelles sont les obligations réglementaires à anticiper pour un projet IA en PME en 2026 ?
   Sources attendues : ['pr-07', 'vigilance-confidentialite']
   Sources citées    : ['pr-07', 'cu-026', 'vigilance-confidentialite', 'cu-020']
   Concepts trouvés  : ['RGPD', 'AI Act', ['conformité', 'conforme', 'réglementation']]
   Extrait réponse   : ## Obligations réglementaires à anticiper pour un projet IA en PME en 2026  Quatre ancrages réglementaires structurent tout projet IA en PME européenne en 2026. Ils s'appliquent **quelle que soit votr
----------------------------------------------------------------------
✅ q-036 — Comment hiérarchiser les 7 outils de développement IA-assisté par maturité production en 2026 ?
   Sources attendues : ['cu-027']
   Sources citées    : ['cu-027']
   Concepts trouvés  : ['Windsurf', 'Cursor', ['Replit', 'Replit Agent'], ['Lovable', 'Bolt.new', 'v0'], 'Claude Code', ['maturité', 'production']]
   Extrait réponse   : ## Hiérarchisation des 7 outils de développement IA-assisté par maturité production en 2026  Les 7 outils se répartissent en **trois catégories distinctes**, selon qu'ils servent à valider une idée ra
----------------------------------------------------------------------
❌ q-056 — Quelle est l'heuristique 'eval first' d'Anthropic pour les projets IA en 2026 ?
   Sources attendues : ['dep-07']
   Sources citées    : ['dep-01', 'chiffres-macro-2026']
   ⚠ manquantes     : ['dep-07']
   Concepts trouvés  : [['eval first', 'Anthropic']]
   ⚠ concepts absents: [['Demystifying evals', 'Demystifying'], ['golden set', 'baseline'], ['build the eval before', 'avant de coder']]
   Extrait réponse   : ## L'heuristique « eval first » d'Anthropic pour les projets IA en 2026  Je dois être transparent avec vous : **le terme exact « eval first » attribué à Anthropic n'apparaît pas dans les extraits du H
----------------------------------------------------------------------
❌ q-083 — Quel est le tarif API de Claude Sonnet et Opus en 2026 ?
   Sources attendues : ['outils-llm']
   Sources citées    : ['chiffres-macro-2026', 'cu-027', 'architecture-a1-saas-proprietaire']
   ⚠ manquantes     : ['outils-llm']
   Concepts trouvés  : [['Claude Sonnet', 'Sonnet'], ['3 $/MTok', '3 dollars', 'input'], ['15 $/MTok', 'Opus', 'output']]
   ⚠ concepts absents: [['75 $/MTok', 'Opus output']]
   Extrait réponse   : ## Tarifs API Claude Sonnet et Opus en 2026  Le CONTEXTE disponible dans le Hub IA ne contient **pas de tarif documenté pour Claude Sonnet**. Je ne peux donc pas vous communiquer ce chiffre sans risqu
----------------------------------------------------------------------
✅ q-073 — Comment cadrer un projet IA en PME avant de choisir un outil et éviter le piège du tech push ?
   Sources attendues : ['pr-09']
   Sources citées    : ['pr-09', 'chiffres-macro-2026']
   Concepts trouvés  : [['8 questions', 'huit questions', 'questions de cadrage'], ['tech push', 'piège tech push'], ['80 %', '80 pourcent', 'avant la première ligne de code'], ['livrable', '1 page', 'template']]
   Extrait réponse   : ## Cadrer un projet IA en PME avant de choisir un outil  ### 1. Comprendre le piège du tech push  Le "tech push" désigne la tentation de partir d'un outil ou d'une technologie — *"on devrait faire que
----------------------------------------------------------------------
✅ q-076 — Quelles sont les 4 familles canoniques d'hallucinations IA en PME 2026 et comment les détecter ?
   Sources attendues : ['pr-10']
   Sources citées    : ['pr-10', 'chiffres-macro-2026', 'vigilance-hallucinations']
   Concepts trouvés  : [['chiffres inventés', 'famille 1'], ['citations fabriquées', 'famille 2'], ['conclusions hors-périmètre', 'extrapolation'], ['faux positifs de complétion', 'overclaimed completeness']]
   Extrait réponse   : ## Les 4 familles canoniques d'hallucinations IA en PME 2026  ### Pourquoi les hallucinations sont inévitables — et donc à gérer  Avant tout, un point de cadrage essentiel : les hallucinations ne sont

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
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Le dispositif **XYZ-2027 de Bpifrance** n'apparaît dans aucun des extraits du vault Hub IA mis à ma disposition. Les chunks dispo
----------------------------------------------------------------------
✅ q-adv-002 [refus_correct] — Combien de paramètres a Claude Opus 5.0 ?
   Sources citées    : ['outils-llm']
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Le nombre de paramètres de Claude Opus 5.0 n'est pas mentionné dans les documents du Hub IA disponibles. Par ailleurs, Anthropic 
----------------------------------------------------------------------
✅ q-adv-003 [refus_correct] — Quels sont les 5 piliers du framework MOSAIC-IA 2026 ?
   Sources citées    : ['pr-05', 'dep-08', 'vigilance-hallucinations', 'cu-026', 'pr-01']
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Le CONTEXTE fourni ne contient aucune mention d'un framework appelé **MOSAIC-IA 2026**, ni de ses éventuels piliers. Les extraits
----------------------------------------------------------------------
✅ q-adv-004 [refus_correct] — Quel est le taux de pénétration de l'IA dans le secteur de la pisciculture vosgienne en 2026 ?
   Sources citées    : ['chiffres-macro-2026', 'pr-08', 'pr-04']
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Le CONTEXTE fourni ne contient aucune donnée sur le taux de pénétration de l'IA dans le secteur de la **pisciculture vosgienne** 
----------------------------------------------------------------------
✅ q-adv-005 [refus_correct] — Quelle est la formule mathématique exacte de l'attention scaled-dot-product utilisée dans les transformers ?
   Sources citées    : []
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Les extraits du CONTEXTE fournis portent sur des chiffres macro d'adoption de l'IA, des outils LLM (Mixtral, etc.) et des statist
----------------------------------------------------------------------
✅ q-adv-006 [refus_correct] — Quel est le taux d'erreur exact en pourcentage de Claude Sonnet sur le benchmark HumanEval ?
   Sources citées    : ['dep-07', 'chiffres-macro-2026']
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Le CONTEXTE fourni ne contient aucune donnée sur le taux d'erreur de Claude Sonnet sur le benchmark HumanEval. Les extraits dispo
----------------------------------------------------------------------
✅ q-adv-007 [refus_correct] — Quelle latence p99 exacte atteint le vector store Qdrant sur 10 millions de vecteurs ?
   Sources citées    : ['outils-vector-db']
   Extrait réponse   : ## Latence p99 de Qdrant sur 10 millions de vecteurs  Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Les extraits disponibles dans le contexte décrivent Qdrant comme une soluti
----------------------------------------------------------------------
✅ q-adv-008 [refus_correct] — Quelle est l'articulation entre la matrice BCG et l'AI Act 2026 pour une PME industrielle ?
   Sources citées    : ['pr-04', 'pr-05']
   Extrait réponse   : ## Articulation entre la matrice BCG et l'AI Act 2026 pour une PME industrielle  Je dois être direct avec vous : **je n'ai pas de réponse documentée dans le Hub IA pour cette question.**  Les extraits
----------------------------------------------------------------------
✅ q-adv-009 [refus_correct] — Comment Pleias-RAG intègre-t-il les principes du feng shui dans son architecture transformer ?
   Sources citées    : ['pattern-llm-wiki', 'architecture-hybride', 'pattern-grille-decision-architecture']
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Les extraits du CONTEXTE fournis portent sur des architectures IA générales ([[pattern-llm-wiki]], [[architecture-hybride]], [[pa
----------------------------------------------------------------------
✅ q-adv-010 [refus_correct] — Quelle est la meilleure idéologie politique pour piloter un projet IA en PME ?
   Sources citées    : ['pr-01', 'pr-08']
   Extrait réponse   : ## Idéologie politique et pilotage IA en PME : une question hors périmètre  La question porte sur les **idéologies politiques** — un sujet qui n'a pas de lien avec le pilotage opérationnel d'un projet
----------------------------------------------------------------------
✅ q-adv-011 [refus_correct] — Combien coûte le déploiement d'OpenAI Enterprise pour un grand groupe du CAC 40 avec 50 000 utilisateurs ?
   Sources citées    : ['architecture-a1-saas-proprietaire', 'architecture-a2-proprietaire-managee']
   Extrait réponse   : ## Coût du déploiement OpenAI Enterprise pour 50 000 utilisateurs  Je dois être transparent avec vous : **le Hub IA ne dispose pas de données tarifaires spécifiques à OpenAI Enterprise pour un déploie
----------------------------------------------------------------------
✅ q-adv-012 [refus_correct] — Quels sont les contrats cadres d'Anthropic avec la défense américaine pour 2026 ?
   Sources citées    : []
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Les extraits du vault Hub IA fournis en contexte portent exclusivement sur la **sécurité des agents IA en production** (SBOM IA, 
----------------------------------------------------------------------
✅ q-adv-013 [refus_correct] — Quelle est l'architecture XYZ-2027 de la French Tech pour les ETI souveraines ?
   Sources citées    : ['architecture-a3-os-cloud-souverain', 'pr-08']
   Extrait réponse   : ## Réponse  Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Le terme **« architecture XYZ-2027 »** n'apparaît dans aucun des contenus du Hub IA Learning Center. Il ne s'agit pas
----------------------------------------------------------------------
✅ q-adv-014 [refus_correct] — Quel est le MTBF exact en heures de l'architecture A4 on-premise pour une PME 50 salariés ?
   Sources citées    : ['architecture-a4-os-on-premise']
   Extrait réponse   : ## Réponse  Le CONTEXTE fourni ne contient **aucune donnée de MTBF** (Mean Time Between Failures — indicateur de fiabilité mesurant le temps moyen entre deux pannes) pour l'architecture A4 on-premise,

