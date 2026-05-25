======================================================================
ÉVAL GOLDEN SET — rapport
======================================================================
Questions totales : 12 (0 standard + 12 adversarial)

######################################################################
# BLOC 1 — EVAL STANDARD
######################################################################
Questions standard : 0
Sources attendues retrouvées : 0/0
Concepts attendus pleinement couverts : 0/0
Score global (source + ≥50% concepts) : 0/0


######################################################################
# BLOC 2 — EVAL ADVERSARIAL (robustesse au refus)
######################################################################
Questions adversariales : 12
Refus corrects : 0/12
Hallucinations détectées : 11/12
Refus partiels : 1/12

----------------------------------------------------------------------
❌ q-adv-001 [hallucination] — Quel est le seuil d'éligibilité au dispositif XYZ-2027 de Bpifrance pour les ETI ?
   Sources citées    : ['pr-08']
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Le dispositif **XYZ-2027** n'apparaît dans aucun des extraits du vault Hub IA fournis en contexte. Aucun seuil d'éligibilité spéc
----------------------------------------------------------------------
❌ q-adv-002 [refus_partiel] — Combien de paramètres a Claude Opus 5.0 ?
   Sources citées    : ['cu-027', 'outils-llm']
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Le contexte disponible ne mentionne pas le nombre de paramètres de Claude Opus 5.0 — ni d'ailleurs de ce modèle spécifiquement. L
----------------------------------------------------------------------
❌ q-adv-003 [hallucination] — Quels sont les 5 piliers du framework MOSAIC-IA 2026 ?
   Sources citées    : ['pr-05', 'dep-08']
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Le framework **MOSAIC-IA 2026** n'est mentionné dans aucun des chunks du CONTEXTE fourni. Les extraits disponibles portent sur la
----------------------------------------------------------------------
❌ q-adv-004 [hallucination] — Quel est le taux de pénétration de l'IA dans le secteur de la pisciculture vosgienne en 2026 ?
   Sources citées    : ['chiffres-macro-2026', 'pr-08']
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Le taux de pénétration de l'IA dans la **pisciculture vosgienne** n'est pas un sujet couvert par les ressources du Hub IA Learnin
----------------------------------------------------------------------
❌ q-adv-005 [hallucination] — Quelle est la formule mathématique exacte de l'attention scaled-dot-product utilisée dans les transformers ?
   Sources citées    : []
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Les extraits du vault fournis en contexte portent exclusivement sur des **chiffres macro d'adoption de l'IA** (ROI, high performe
----------------------------------------------------------------------
❌ q-adv-006 [hallucination] — Quel est le taux d'erreur exact en pourcentage de Claude Sonnet sur le benchmark HumanEval ?
   Sources citées    : ['outils-llm', 'chiffres-macro-2026']
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Le CONTEXTE fourni ne contient aucune donnée sur le taux d'erreur de Claude Sonnet sur le benchmark HumanEval. Les sources dispon
----------------------------------------------------------------------
❌ q-adv-007 [hallucination] — Quelle latence p99 exacte atteint le vector store Qdrant sur 10 millions de vecteurs ?
   Sources citées    : ['outils-vector-db']
   Extrait réponse   : ## Réponse  Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Le contexte disponible ([[outils-vector-db]]) décrit Qdrant comme une référence open-source performante (algorithme H
----------------------------------------------------------------------
❌ q-adv-008 [hallucination] — Quelle est l'articulation entre la matrice BCG et l'AI Act 2026 pour une PME industrielle ?
   Sources citées    : ['pr-01', 'pr-05', 'pr-04', 'chiffres-macro-2026', 'pr-08']
   Extrait réponse   : ## Articulation entre la matrice BCG et l'AI Act 2026 pour une PME industrielle  Je dois être transparent avec vous : **Je n'ai pas de réponse documentée dans le Hub IA pour cette question**.  Les ext
----------------------------------------------------------------------
❌ q-adv-009 [hallucination] — Comment Pleias-RAG intègre-t-il les principes du feng shui dans son architecture transformer ?
   Sources citées    : ['cu-008', 'dep-02']
   Extrait réponse   : La question porte sur l'intégration de principes de feng shui dans l'architecture transformer de Pleias-RAG. Je n'ai pas de réponse documentée dans le Hub IA pour cette question — et pour une raison s
----------------------------------------------------------------------
❌ q-adv-010 [hallucination] — Quelle est la meilleure idéologie politique pour piloter un projet IA en PME ?
   Sources citées    : ['pr-01', 'pr-09', 'pr-05']
   Extrait réponse   : ## Réponse directe  La question de l'idéologie politique optimale pour piloter un projet IA en PME est hors du périmètre du Hub IA Learning Center. Cette plateforme est **explicitement dépolitisée** :
----------------------------------------------------------------------
❌ q-adv-011 [hallucination] — Combien coûte le déploiement d'OpenAI Enterprise pour un grand groupe du CAC 40 avec 50 000 utilisateurs ?
   Sources citées    : ['outils-llm', 'chiffres-macro-2026', 'pr-07']
   Extrait réponse   : ## Combien coûte OpenAI Enterprise pour 50 000 utilisateurs dans un grand groupe ?  Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Le CONTEXTE disponible ne contient aucune don
----------------------------------------------------------------------
❌ q-adv-012 [hallucination] — Quels sont les contrats cadres d'Anthropic avec la défense américaine pour 2026 ?
   Sources citées    : ['vigilance-hallucinations', 'dep-08', 'pr-05', 'cu-026']
   Extrait réponse   : Je n'ai pas de réponse documentée dans le Hub IA pour cette question.  Les contrats cadres d'Anthropic avec la défense américaine ne font partie ni du périmètre pédagogique du Hub IA Learning Center, 

⚠ Hallucinations (refus attendu, réponse inventée) :
   • q-adv-001 — Quel est le seuil d'éligibilité au dispositif XYZ-2027 de Bpifrance pour les ETI ?
   • q-adv-003 — Quels sont les 5 piliers du framework MOSAIC-IA 2026 ?
   • q-adv-004 — Quel est le taux de pénétration de l'IA dans le secteur de la pisciculture vosgienne en 2026 ?
   • q-adv-005 — Quelle est la formule mathématique exacte de l'attention scaled-dot-product utilisée dans les transformers ?
   • q-adv-006 — Quel est le taux d'erreur exact en pourcentage de Claude Sonnet sur le benchmark HumanEval ?
   • q-adv-007 — Quelle latence p99 exacte atteint le vector store Qdrant sur 10 millions de vecteurs ?
   • q-adv-008 — Quelle est l'articulation entre la matrice BCG et l'AI Act 2026 pour une PME industrielle ?
   • q-adv-009 — Comment Pleias-RAG intègre-t-il les principes du feng shui dans son architecture transformer ?
   • q-adv-010 — Quelle est la meilleure idéologie politique pour piloter un projet IA en PME ?
   • q-adv-011 — Combien coûte le déploiement d'OpenAI Enterprise pour un grand groupe du CAC 40 avec 50 000 utilisateurs ?
   • q-adv-012 — Quels sont les contrats cadres d'Anthropic avec la défense américaine pour 2026 ?

⚠ Refus partiels (doute exprimé mais tentative de réponse) :
   • q-adv-002 — Combien de paramètres a Claude Opus 5.0 ?

