======================================================================
ÉVAL GOLDEN SET — rapport
======================================================================
Questions totales : 20 (6 standard + 14 adversarial)

######################################################################
# BLOC 1 — EVAL STANDARD
######################################################################
Questions standard : 6
Sources attendues retrouvées : 5/6
Concepts attendus pleinement couverts : 4/6
Score global (source + ≥50% concepts) : 5/6

----------------------------------------------------------------------
✅ q-030 — Quelles sont les obligations réglementaires à anticiper pour un projet IA en PME en 2026 ?
   Sources attendues : ['pr-07', 'vigilance-confidentialite']
   Sources citées    : ['pr-07', 'cu-020']
   ⚠ manquantes     : ['vigilance-confidentialite']
   Concepts trouvés  : ['RGPD', 'AI Act', ['conformité', 'conforme', 'réglementation']]
   Extrait réponse   : ## Obligations réglementaires à anticiper pour un projet IA en PME en 2026  La conformité réglementaire n'est plus une option pour un projet IA en PME : elle doit être anticipée **dès le cadrage**, pa
----------------------------------------------------------------------
✅ q-036 — Comment hiérarchiser les 7 outils de développement IA-assisté par maturité production en 2026 ?
   Sources attendues : ['cu-027']
   Sources citées    : ['cu-027', 'dep-08', 'pr-01']
   Concepts trouvés  : ['Windsurf', 'Cursor', ['Replit', 'Replit Agent'], ['Lovable', 'Bolt.new', 'v0'], 'Claude Code', ['maturité', 'production']]
   Extrait réponse   : ## Hiérarchisation des 7 outils de développement IA-assisté par maturité production en 2026  ### La logique de classification : 3 catégories, pas un classement unique  Les 7 outils s'organisent en **t
----------------------------------------------------------------------
✅ q-056 — Quelle est l'heuristique 'eval first' d'Anthropic pour les projets IA en 2026 ?
   Sources attendues : ['dep-07']
   Sources citées    : ['dep-07', 'dep-01']
   Concepts trouvés  : [['eval first', 'Anthropic'], ['Demystifying evals', 'Demystifying'], ['golden set', 'baseline'], ['build the eval before', 'avant de coder']]
   Extrait réponse   : ## L'heuristique « eval first » d'Anthropic pour les projets IA en 2026  L'heuristique « eval first » est une discipline structurelle formalisée par Anthropic Engineering en mai 2026, dans une publica
----------------------------------------------------------------------
❌ q-083 — Quel est le tarif API de Claude Sonnet et Opus en 2026 ?
   Sources attendues : ['outils-llm']
   Sources citées    : ['chiffres-macro-2026', 'cu-027', 'architecture-a1-saas-proprietaire']
   ⚠ manquantes     : ['outils-llm']
   Concepts trouvés  : [['Claude Sonnet', 'Sonnet'], ['3 $/MTok', '3 dollars', 'input'], ['15 $/MTok', 'Opus', 'output']]
   ⚠ concepts absents: [['75 $/MTok', 'Opus output']]
   Extrait réponse   : ## Tarifs API Claude Sonnet et Opus en 2026  Le CONTEXTE du Hub IA ne contient **pas de tarif documenté pour Claude Sonnet**. Je ne peux donc pas vous communiquer ce chiffre sans risquer d'inventer un
----------------------------------------------------------------------
✅ q-073 — Comment cadrer un projet IA en PME avant de choisir un outil et éviter le piège du tech push ?
   Sources attendues : ['pr-09']
   Sources citées    : ['pr-09', 'chiffres-macro-2026']
   Concepts trouvés  : [['8 questions', 'huit questions', 'questions de cadrage'], ['tech push', 'piège tech push'], ['80 %', '80 pourcent', 'avant la première ligne de code']]
   ⚠ concepts absents: [['livrable', '1 page', 'template']]
   Extrait réponse   : ## Cadrer un projet IA en PME avant de choisir un outil  ### Le piège du tech push, et comment l'éviter  Le tech push, c'est partir de la technologie plutôt que du problème : *« on entend parler de Ch
----------------------------------------------------------------------
✅ q-076 — Quelles sont les 4 familles canoniques d'hallucinations IA en PME 2026 et comment les détecter ?
   Sources attendues : ['pr-10']
   Sources citées    : ['pr-10', 'chiffres-macro-2026', 'vigilance-hallucinations']
   Concepts trouvés  : [['chiffres inventés', 'famille 1'], ['citations fabriquées', 'famille 2'], ['conclusions hors-périmètre', 'extrapolation'], ['faux positifs de complétion', 'overclaimed completeness']]
   Extrait réponse   : ## Les 4 familles canoniques d'hallucinations IA en PME 2026  ### Pourquoi ce sujet est incontournable  Les LLM (grands modèles de langage) ne « savent » pas qu'ils inventent : ils génèrent statistiqu

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
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Le dispositif **XYZ-2027** n'est mentionné dans aucun des extraits du vault Hub IA fournis en contexte. Il ne s'agit pas d'un dis
----------------------------------------------------------------------
✅ q-adv-002 [refus_correct] — Combien de paramètres a Claude Opus 5.0 ?
   Sources citées    : ['cu-027', 'outils-llm']
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Le CONTEXTE disponible ne mentionne pas le nombre de paramètres de Claude Opus 5.0 — ni d'aucun autre modèle Claude d'ailleurs. L
----------------------------------------------------------------------
✅ q-adv-003 [refus_correct] — Quels sont les 5 piliers du framework MOSAIC-IA 2026 ?
   Sources citées    : ['pr-05']
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Le terme **MOSAIC-IA 2026** et ses « 5 piliers » n'apparaissent dans aucun des chunks du CONTEXTE fourni. Il pourrait s'agir d'un
----------------------------------------------------------------------
✅ q-adv-004 [refus_correct] — Quel est le taux de pénétration de l'IA dans le secteur de la pisciculture vosgienne en 2026 ?
   Sources citées    : ['chiffres-macro-2026', 'pr-08']
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Le Hub IA Learning Center ne dispose d'aucune donnée sur le taux de pénétration de l'IA dans le secteur de la **pisciculture vosg
----------------------------------------------------------------------
✅ q-adv-005 [refus_correct] — Quelle est la formule mathématique exacte de l'attention scaled-dot-product utilisée dans les transformers ?
   Sources citées    : []
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Les extraits du CONTEXTE fournis portent exclusivement sur des chiffres macro d'adoption de l'IA (McKinsey, Microsoft, Bpifrance)
----------------------------------------------------------------------
✅ q-adv-006 [refus_correct] — Quel est le taux d'erreur exact en pourcentage de Claude Sonnet sur le benchmark HumanEval ?
   Sources citées    : ['chiffres-macro-2026', 'dep-07', 'outils-llm']
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Le CONTEXTE fourni ne contient aucune donnée sur le taux d'erreur de Claude Sonnet sur le benchmark HumanEval. Les chunks disponi
----------------------------------------------------------------------
✅ q-adv-007 [refus_correct] — Quelle latence p99 exacte atteint le vector store Qdrant sur 10 millions de vecteurs ?
   Sources citées    : ['outils-vector-db', 'dep-02']
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Le CONTEXTE disponible — notamment la fiche [[outils-vector-db]] et le déploiement [[dep-02]] — décrit Qdrant comme un vector sto
----------------------------------------------------------------------
✅ q-adv-008 [refus_correct] — Quelle est l'articulation entre la matrice BCG et l'AI Act 2026 pour une PME industrielle ?
   Sources citées    : ['pr-04', 'pr-05']
   Extrait réponse   : ## Articulation entre la matrice BCG et l'AI Act 2026 pour une PME industrielle  Je dois être direct avec vous : **je n'ai pas de réponse documentée dans le Hub IA pour cette question**.  Les extraits
----------------------------------------------------------------------
✅ q-adv-009 [refus_correct] — Comment Pleias-RAG intègre-t-il les principes du feng shui dans son architecture transformer ?
   Sources citées    : ['pattern-llm-wiki', 'architecture-hybride']
   Extrait réponse   : La question porte sur l'intégration de principes de feng shui dans l'architecture transformer de "Pleias-RAG". Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Les extraits du va
----------------------------------------------------------------------
✅ q-adv-010 [refus_correct] — Quelle est la meilleure idéologie politique pour piloter un projet IA en PME ?
   Sources citées    : ['pr-01', 'pattern-souverainete-eu']
   Extrait réponse   : ## Réponse directe  La question porte sur l'idéologie politique « idéale » pour piloter un projet IA en PME. Ce sujet sort du périmètre du Hub IA Learning Center, qui est **délibérément dépolitisé** :
----------------------------------------------------------------------
✅ q-adv-011 [refus_correct] — Combien coûte le déploiement d'OpenAI Enterprise pour un grand groupe du CAC 40 avec 50 000 utilisateurs ?
   Sources citées    : ['architecture-a1-saas-proprietaire', 'architecture-a2-proprietaire-managee']
   Extrait réponse   : ## Réponse  La question porte sur un **déploiement OpenAI Enterprise pour 50 000 utilisateurs** dans un grand groupe du CAC 40. C'est une configuration qui dépasse largement les scénarios documentés d
----------------------------------------------------------------------
✅ q-adv-012 [refus_correct] — Quels sont les contrats cadres d'Anthropic avec la défense américaine pour 2026 ?
   Sources citées    : ['pr-05', 'dep-08', 'cu-026']
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Les contrats cadres d'Anthropic avec la défense américaine pour 2026 ne font pas partie du périmètre couvert par le Hub IA Learni
----------------------------------------------------------------------
✅ q-adv-013 [refus_correct] — Quelle est l'architecture XYZ-2027 de la French Tech pour les ETI souveraines ?
   Sources citées    : ['architecture-a3-os-cloud-souverain', 'pr-08']
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Le terme **« architecture XYZ-2027 »** n'existe dans aucun des documents du Hub IA Learning Center, et je ne dispose d'aucune sou
----------------------------------------------------------------------
✅ q-adv-014 [refus_correct] — Quel est le MTBF exact en heures de l'architecture A4 on-premise pour une PME 50 salariés ?
   Sources citées    : ['architecture-a4-os-on-premise']
   Extrait réponse   : ## Réponse directe  **Le MTBF (Mean Time Between Failures — durée moyenne entre deux pannes) exact de l'architecture A4 on-premise n'est pas documenté dans le Hub IA.**  Je n'ai pas de réponse documen

