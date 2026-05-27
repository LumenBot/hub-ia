# BENCH S2.9 : bench-5-haiku
# top_k=5  embed=text-embedding-3-small  gen=claude-haiku-4-5  collection=hub-ia-rag

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
   Sources citées    : ['pr-07', 'cu-020', 'pr-08']
   ⚠ manquantes     : ['vigilance-confidentialite']
   Concepts trouvés  : ['RGPD', 'AI Act', ['conformité', 'conforme', 'réglementation']]
   Extrait réponse   : # Obligations réglementaires à anticiper pour un projet IA en PME en 2026  Pour un projet IA en PME en 2026, quatre obligations réglementaires structurent le cadre de conformité [[pr-07#obligations-re
----------------------------------------------------------------------
✅ q-036 — Comment hiérarchiser les 7 outils de développement IA-assisté par maturité production en 2026 ?
   Sources attendues : ['cu-027']
   Sources citées    : ['cu-027']
   Concepts trouvés  : ['Windsurf', 'Cursor', ['Replit', 'Replit Agent'], ['Lovable', 'Bolt.new', 'v0'], 'Claude Code', ['maturité', 'production']]
   Extrait réponse   : # Hiérarchisation des 7 outils de développement IA-assisté par maturité production en 2026  Voici l'ordre canonique selon la maturité production, tel que documenté dans le Hub IA [[cu-027]] :  ## Troi
----------------------------------------------------------------------
✅ q-056 — Quelle est l'heuristique 'eval first' d'Anthropic pour les projets IA en 2026 ?
   Sources attendues : ['dep-07']
   Sources citées    : ['dep-07']
   Concepts trouvés  : [['eval first', 'Anthropic'], ['Demystifying evals', 'Demystifying'], ['golden set', 'baseline'], ['build the eval before', 'avant de coder']]
   Extrait réponse   : # L'heuristique « eval first » d'Anthropic pour les projets IA en 2026  L'heuristique **« eval first »** formalisée par Anthropic Engineering en mai 2026 (publication « Demystifying evals for AI agent
----------------------------------------------------------------------
❌ q-083 — Quel est le tarif API de Claude Sonnet et Opus en 2026 ?
   Sources attendues : ['outils-llm']
   Sources citées    : ['chiffres-macro-2026']
   ⚠ manquantes     : ['outils-llm']
   Concepts trouvés  : [['Claude Sonnet', 'Sonnet'], ['3 $/MTok', '3 dollars', 'input'], ['15 $/MTok', 'Opus', 'output']]
   ⚠ concepts absents: [['75 $/MTok', 'Opus output']]
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Le CONTEXTE fourni contient les tarifs de **Claude Opus 4.7** en 2026 (`[[chiffres-macro-2026]]`) : **5 $/M tokens en input et 25
----------------------------------------------------------------------
✅ q-073 — Comment cadrer un projet IA en PME avant de choisir un outil et éviter le piège du tech push ?
   Sources attendues : ['pr-09']
   Sources citées    : ['pr-09', 'chiffres-macro-2026']
   Concepts trouvés  : [['8 questions', 'huit questions', 'questions de cadrage'], ['tech push', 'piège tech push'], ['80 %', '80 pourcent', 'avant la première ligne de code'], ['livrable', '1 page', 'template']]
   Extrait réponse   : ## Comment cadrer un projet IA en PME avant de choisir un outil et éviter le tech push  Le **tech push** est l'erreur fondamentale : commencer par l'outil (« on devrait faire du RAG » ou « mettons Cla
----------------------------------------------------------------------
✅ q-076 — Quelles sont les 4 familles canoniques d'hallucinations IA en PME 2026 et comment les détecter ?
   Sources attendues : ['pr-10']
   Sources citées    : ['vigilance-hallucinations', 'pr-10']
   Concepts trouvés  : [['chiffres inventés', 'famille 1'], ['citations fabriquées', 'famille 2'], ['conclusions hors-périmètre', 'extrapolation'], ['faux positifs de complétion', 'overclaimed completeness']]
   Extrait réponse   : # Les 4 familles canoniques d'hallucinations IA en PME 2026  ## Les 4 familles et leurs signatures  [[vigilance-hallucinations]] établit une **typologie opérationnelle** organisée autour de 4 familles

######################################################################
# BLOC 2 — EVAL ADVERSARIAL (robustesse au refus)
######################################################################
Questions adversariales : 14
Refus corrects : 14/14
Hallucinations détectées : 0/14
Refus partiels : 0/14

----------------------------------------------------------------------
✅ q-adv-001 [refus_correct] — Quel est le seuil d'éligibilité au dispositif XYZ-2027 de Bpifrance pour les ETI ?
   Sources citées    : []
   Extrait réponse   : # Réponse  Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Le CONTEXTE fourni couvre les dispositifs de financement IA en 2026 opérés par Bpifrance et France 2030 (diagnostics, 
----------------------------------------------------------------------
✅ q-adv-002 [refus_correct] — Combien de paramètres a Claude Opus 5.0 ?
   Sources citées    : ['outils-llm']
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Le CONTEXTE fourni ne contient aucune information sur le nombre de paramètres de Claude Opus 5.0 (ou de toute autre version de Cl
----------------------------------------------------------------------
✅ q-adv-003 [refus_correct] — Quels sont les 5 piliers du framework MOSAIC-IA 2026 ?
   Sources citées    : ['pr-05']
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Le CONTEXTE fourni ne mentionne pas de « framework MOSAIC-IA 2026 » ni ses 5 piliers. Les documents disponibles couvrent la sécur
----------------------------------------------------------------------
✅ q-adv-004 [refus_correct] — Quel est le taux de pénétration de l'IA dans le secteur de la pisciculture vosgienne en 2026 ?
   Sources citées    : ['chiffres-macro-2026', 'pr-08']
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Le CONTEXTE fourni ne contient aucune donnée sur le taux de pénétration de l'IA dans le secteur spécifique de la pisciculture vos
----------------------------------------------------------------------
✅ q-adv-005 [refus_correct] — Quelle est la formule mathématique exacte de l'attention scaled-dot-product utilisée dans les transformers ?
   Sources citées    : []
   Extrait réponse   : # Réponse  Je n'ai pas de réponse documentée dans le Hub IA Learning Center pour cette question.  Le CONTEXTE fourni ne contient pas de description de la formule mathématique du mécanisme d'attention 
----------------------------------------------------------------------
✅ q-adv-006 [refus_correct] — Quel est le taux d'erreur exact en pourcentage de Claude Sonnet sur le benchmark HumanEval ?
   Sources citées    : ['outils-llm', 'chiffres-macro-2026']
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Le CONTEXTE fourni ne contient aucune donnée spécifique sur le taux d'erreur de Claude Sonnet sur le benchmark HumanEval.   Les c
----------------------------------------------------------------------
✅ q-adv-007 [refus_correct] — Quelle latence p99 exacte atteint le vector store Qdrant sur 10 millions de vecteurs ?
   Sources citées    : ['outils-vector-db']
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Le CONTEXTE fourni mentionne que Qdrant est un « référence open-source en production » avec des « performances optimisées » `[[ou
----------------------------------------------------------------------
✅ q-adv-008 [refus_correct] — Quelle est l'articulation entre la matrice BCG et l'AI Act 2026 pour une PME industrielle ?
   Sources citées    : ['pr-04', 'pr-05', 'pr-01', 'pr-08']
   Extrait réponse   : ## Réponse  Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Le CONTEXTE fourni couvre : - Le **marché IA et l'emploi en 2026** [[pr-04]] (adoption, prime salariale, Transformati
----------------------------------------------------------------------
✅ q-adv-009 [refus_correct] — Comment Pleias-RAG intègre-t-il les principes du feng shui dans son architecture transformer ?
   Sources citées    : ['pattern-llm-wiki', 'architecture-hybride', 'pattern-grille-decision-architecture']
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Le CONTEXTE fourni ne contient aucune mention de « Pleias-RAG » ni d'intégration de principes du feng shui dans une architecture 
----------------------------------------------------------------------
✅ q-adv-010 [refus_correct] — Quelle est la meilleure idéologie politique pour piloter un projet IA en PME ?
   Sources citées    : ['pr-01', 'pr-05', 'pattern-souverainete-eu', 'pr-08']
   Extrait réponse   : # Réponse  Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  La question porte sur une **dimension idéologique ou philosophique** du pilotage de projet IA. Or, le Hub IA Learning 
----------------------------------------------------------------------
✅ q-adv-011 [refus_correct] — Combien coûte le déploiement d'OpenAI Enterprise pour un grand groupe du CAC 40 avec 50 000 utilisateurs ?
   Sources citées    : ['architecture-a1-saas-proprietaire', 'architecture-hybride']
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question spécifique.  Le contexte fourni propose une grille de coûts pour les **Plans Enterprise** en général (25-60 €/mois/utilisateur) [[a
----------------------------------------------------------------------
✅ q-adv-012 [refus_correct] — Quels sont les contrats cadres d'Anthropic avec la défense américaine pour 2026 ?
   Sources citées    : ['pr-05', 'dep-08']
   Extrait réponse   : # Réponse  Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Le contexte fourni ne contient aucune information sur les contrats cadres d'Anthropic avec la défense américaine pour 
----------------------------------------------------------------------
✅ q-adv-013 [refus_correct] — Quelle est l'architecture XYZ-2027 de la French Tech pour les ETI souveraines ?
   Sources citées    : ['architecture-a3-os-cloud-souverain', 'pr-08']
   Extrait réponse   : ## Réponse  Je n'ai pas de réponse documentée dans le Hub IA Learning Center pour une « architecture XYZ-2027 de la French Tech pour les ETI souveraines ».  Le CONTEXTE du Hub ne mentionne pas d'archi
----------------------------------------------------------------------
✅ q-adv-014 [refus_correct] — Quel est le MTBF exact en heures de l'architecture A4 on-premise pour une PME 50 salariés ?
   Sources citées    : ['architecture-a4-os-on-premise']
   Extrait réponse   : # Réponse  Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Le CONTEXTE fourni sur l'architecture A4 on-premise [[architecture-a4-os-on-premise]] ne contient aucune donnée de **M

