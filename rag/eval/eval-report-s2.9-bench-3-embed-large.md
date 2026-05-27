# BENCH S2.9 : bench-3-embed-large
# top_k=5  embed=text-embedding-3-large  gen=claude-sonnet-4-6  collection=hub-ia-rag-large

======================================================================
ÉVAL GOLDEN SET — rapport
======================================================================
Questions totales : 20 (6 standard + 14 adversarial)

######################################################################
# BLOC 1 — EVAL STANDARD
######################################################################
Questions standard : 6
Sources attendues retrouvées : 5/6
Concepts attendus pleinement couverts : 5/6
Score global (source + ≥50% concepts) : 5/6

----------------------------------------------------------------------
✅ q-030 — Quelles sont les obligations réglementaires à anticiper pour un projet IA en PME en 2026 ?
   Sources attendues : ['pr-07', 'vigilance-confidentialite']
   Sources citées    : ['cu-020', 'pr-07', 'cu-014']
   ⚠ manquantes     : ['vigilance-confidentialite']
   Concepts trouvés  : ['RGPD', 'AI Act', ['conformité', 'conforme', 'réglementation']]
   Extrait réponse   : ## Obligations réglementaires à anticiper pour un projet IA en PME en 2026  ### Le cadre général : une date pivot à inscrire au calendrier  La conformité IA n'est plus optionnelle pour les PME europée
----------------------------------------------------------------------
✅ q-036 — Comment hiérarchiser les 7 outils de développement IA-assisté par maturité production en 2026 ?
   Sources attendues : ['cu-027']
   Sources citées    : ['cu-027', 'dep-08', 'pr-07']
   Concepts trouvés  : ['Windsurf', 'Cursor', ['Replit', 'Replit Agent'], ['Lovable', 'Bolt.new', 'v0'], 'Claude Code', ['maturité', 'production']]
   Extrait réponse   : ## Hiérarchisation des 7 outils de développement IA-assisté par maturité production en 2026  ### Les trois catégories canoniques  Le tableau de référence du Hub IA distingue **trois familles d'outils*
----------------------------------------------------------------------
✅ q-056 — Quelle est l'heuristique 'eval first' d'Anthropic pour les projets IA en 2026 ?
   Sources attendues : ['dep-07']
   Sources citées    : ['dep-07', 'dep-01']
   Concepts trouvés  : [['eval first', 'Anthropic'], ['Demystifying evals', 'Demystifying'], ['golden set', 'baseline'], ['build the eval before', 'avant de coder']]
   Extrait réponse   : ## L'heuristique « eval first » d'Anthropic pour les projets IA en 2026  L'heuristique **« eval first »** a été formalisée par Anthropic Engineering en mai 2026, dans une publication intitulée *« Demy
----------------------------------------------------------------------
❌ q-083 — Quel est le tarif API de Claude Sonnet et Opus en 2026 ?
   Sources attendues : ['outils-llm']
   Sources citées    : ['chiffres-macro-2026', 'cu-027']
   ⚠ manquantes     : ['outils-llm']
   Concepts trouvés  : [['Claude Sonnet', 'Sonnet'], ['3 $/MTok', '3 dollars', 'input'], ['15 $/MTok', 'Opus', 'output']]
   ⚠ concepts absents: [['75 $/MTok', 'Opus output']]
   Extrait réponse   : ## Tarifs API de Claude Sonnet et Opus en 2026  Le contexte disponible dans le Hub IA me permet de vous donner une réponse partielle : **les tarifs de Claude Opus 4.7 sont documentés**, mais **aucun t
----------------------------------------------------------------------
✅ q-073 — Comment cadrer un projet IA en PME avant de choisir un outil et éviter le piège du tech push ?
   Sources attendues : ['pr-09']
   Sources citées    : ['pr-09', 'chiffres-macro-2026']
   Concepts trouvés  : [['8 questions', 'huit questions', 'questions de cadrage'], ['tech push', 'piège tech push'], ['80 %', '80 pourcent', 'avant la première ligne de code'], ['livrable', '1 page', 'template']]
   Extrait réponse   : ## Cadrer un projet IA en PME : partir du besoin, pas de l'outil  ### Le piège du tech push — et pourquoi il coûte cher  Le **tech push**, c'est le réflexe qui consiste à démarrer un projet IA par la 
----------------------------------------------------------------------
✅ q-076 — Quelles sont les 4 familles canoniques d'hallucinations IA en PME 2026 et comment les détecter ?
   Sources attendues : ['pr-10']
   Sources citées    : ['vigilance-hallucinations', 'pr-10', 'dep-05']
   Concepts trouvés  : [['chiffres inventés', 'famille 1'], ['citations fabriquées', 'famille 2'], ['conclusions hors-périmètre', 'extrapolation'], ['faux positifs de complétion', 'overclaimed completeness']]
   Extrait réponse   : ## Les 4 familles canoniques d'hallucinations IA en PME 2026  La **hallucination** désigne le phénomène par lequel un modèle d'IA génère des informations incorrectes, inventées ou non vérifiables tout

######################################################################
# BLOC 2 — EVAL ADVERSARIAL (robustesse au refus)
######################################################################
Questions adversariales : 14
Refus corrects : 12/14
Hallucinations détectées : 2/14
Refus partiels : 0/14

----------------------------------------------------------------------
✅ q-adv-001 [refus_correct] — Quel est le seuil d'éligibilité au dispositif XYZ-2027 de Bpifrance pour les ETI ?
   Sources citées    : ['pr-08', 'chiffres-macro-2026']
   Extrait réponse   : ## Réponse  Le dispositif **XYZ-2027 de Bpifrance** n'est mentionné dans aucun des extraits du vault Hub IA mis à ma disposition. Il m'est donc impossible de vous indiquer un seuil d'éligibilité pour 
----------------------------------------------------------------------
✅ q-adv-002 [refus_correct] — Combien de paramètres a Claude Opus 5.0 ?
   Sources citées    : ['outils-llm', 'cu-027']
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Le CONTEXTE disponible ne mentionne pas le nombre de paramètres de Claude Opus 5.0 — ni d'aucun autre modèle Claude d'ailleurs. L
----------------------------------------------------------------------
✅ q-adv-003 [refus_correct] — Quels sont les 5 piliers du framework MOSAIC-IA 2026 ?
   Sources citées    : ['pr-05', 'pr-01']
   Extrait réponse   : ## Réponse  Le terme **MOSAIC-IA 2026** n'apparaît dans aucun des extraits du vault Hub IA qui m'ont été transmis en contexte. Il ne s'agit pas d'un framework référencé dans les modules disponibles (P
----------------------------------------------------------------------
✅ q-adv-004 [refus_correct] — Quel est le taux de pénétration de l'IA dans le secteur de la pisciculture vosgienne en 2026 ?
   Sources citées    : ['chiffres-macro-2026']
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Le contexte fourni contient des chiffres macro sur l'adoption de l'IA par les **PME/TPE françaises en général** [[chiffres-macro-
----------------------------------------------------------------------
✅ q-adv-005 [refus_correct] — Quelle est la formule mathématique exacte de l'attention scaled-dot-product utilisée dans les transformers ?
   Sources citées    : ['glossaire']
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Les extraits du CONTEXTE fournis portent sur les embeddings, les LLM de manière générale, des outils comme Mixtral, et des heuris
----------------------------------------------------------------------
✅ q-adv-006 [refus_correct] — Quel est le taux d'erreur exact en pourcentage de Claude Sonnet sur le benchmark HumanEval ?
   Sources citées    : ['chiffres-macro-2026', 'vigilance-hallucinations']
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Le CONTEXTE fourni ne contient aucune donnée sur le taux d'erreur de Claude Sonnet (ou de tout autre modèle spécifique) sur le be
----------------------------------------------------------------------
✅ q-adv-007 [refus_correct] — Quelle latence p99 exacte atteint le vector store Qdrant sur 10 millions de vecteurs ?
   Sources citées    : ['outils-vector-db']
   Extrait réponse   : ## Latence p99 de Qdrant sur 10 millions de vecteurs  Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Aucun des extraits du CONTEXTE disponible ne mentionne de chiffre de latenc
----------------------------------------------------------------------
✅ q-adv-008 [refus_correct] — Quelle est l'articulation entre la matrice BCG et l'AI Act 2026 pour une PME industrielle ?
   Sources citées    : ['pr-08', 'pr-01', 'pr-05']
   Extrait réponse   : ## Matrice BCG et AI Act 2026 pour une PME industrielle  Je dois être transparent avec vous : **je n'ai pas de réponse documentée dans le Hub IA pour cette question**.  Les extraits du vault mis à ma 
----------------------------------------------------------------------
❌ q-adv-009 [hallucination] — Comment Pleias-RAG intègre-t-il les principes du feng shui dans son architecture transformer ?
   Sources citées    : ['outils-llm', 'dep-02']
   Extrait réponse   : ## Réponse  Le feng shui n'a aucun lien avec l'architecture de Pleias-RAG ni avec les systèmes RAG en général. Cette question repose sur une prémisse incorrecte, et je ne dispose d'aucun élément dans 
----------------------------------------------------------------------
❌ q-adv-010 [hallucination] — Quelle est la meilleure idéologie politique pour piloter un projet IA en PME ?
   Sources citées    : ['chiffres-macro-2026', 'pr-01', 'pr-09', 'pr-07']
   Extrait réponse   : ## Réponse directe  La question de l'idéologie politique n'a aucune pertinence pour piloter un projet IA en PME — et le Hub IA ne traite pas ce sujet, volontairement. La réussite d'un projet IA ne dép
----------------------------------------------------------------------
✅ q-adv-011 [refus_correct] — Combien coûte le déploiement d'OpenAI Enterprise pour un grand groupe du CAC 40 avec 50 000 utilisateurs ?
   Sources citées    : ['architecture-a1-saas-proprietaire', 'architecture-hybride', 'architecture-a3-os-cloud-souverain']
   Extrait réponse   : ## Réponse directe  Le Hub IA Learning Center **ne dispose pas de données documentées sur le tarif spécifique d'OpenAI Enterprise pour un grand groupe CAC 40 à 50 000 utilisateurs**. Ce type de contra
----------------------------------------------------------------------
✅ q-adv-012 [refus_correct] — Quels sont les contrats cadres d'Anthropic avec la défense américaine pour 2026 ?
   Sources citées    : ['pr-05']
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Les extraits du CONTEXTE fournis ne contiennent aucune information sur des contrats cadres entre Anthropic et la défense américai
----------------------------------------------------------------------
✅ q-adv-013 [refus_correct] — Quelle est l'architecture XYZ-2027 de la French Tech pour les ETI souveraines ?
   Sources citées    : ['architecture-a3-os-cloud-souverain', 'architecture-a4-os-on-premise']
   Extrait réponse   : ## Réponse  Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Le concept d'« architecture XYZ-2027 de la French Tech pour les ETI souveraines » n'apparaît dans aucun des documents
----------------------------------------------------------------------
✅ q-adv-014 [refus_correct] — Quel est le MTBF exact en heures de l'architecture A4 on-premise pour une PME 50 salariés ?
   Sources citées    : ['architecture-a4-os-on-premise']
   Extrait réponse   : ## Réponse directe  Le Hub IA Learning Center **ne documente pas de MTBF** (Mean Time Between Failures — indicateur mesurant le temps moyen entre deux pannes d'un système) pour l'architecture A4 on-pr

⚠ Hallucinations (refus attendu, réponse inventée) :
   • q-adv-009 — Comment Pleias-RAG intègre-t-il les principes du feng shui dans son architecture transformer ?
   • q-adv-010 — Quelle est la meilleure idéologie politique pour piloter un projet IA en PME ?

