# Veille v3.7 — Hub IA section Déploiement (mai 2026)

> Veille de cadrage pour la production des 8 fiches DEP.
> Public cible : dirigeant PME/ETI non-IT pilotant un projet IA en mise en prod, avec son interface technique (CTO, presta, IT interne).
> Approche : pédagogique, stratégique, avec renvois vers les ressources techniques.

---

## Synthèse exécutive

1. **Le mur des 95 % est désormais documenté avec rigueur**. Le rapport MIT NANDA *State of AI in Business 2025* (52 entretiens dirigeants, 153 leaders sondés, 300 déploiements analysés) établit que 95 % des projets GenAI en entreprise n'ont aucun impact P&L mesurable, malgré 30 à 40 milliards de dollars investis. Cause racine : organisationnelle, pas technologique. C'est l'ancrage narratif obligatoire de toute la section Déploiement.

2. **Build vs Buy : le partenariat externe gagne 2 à 3 fois plus souvent**. Toujours selon MIT NANDA, l'achat à un éditeur spécialisé + partenariat réussit dans ~67 % des cas, contre ~33 % pour les builds internes. Message clé pour le dirigeant PME : ne pas chercher à tout faire en interne, sauf cas justifié (souveraineté, données sensibles, ROI massif).

3. **Le RAG hybride est devenu le standard production en 2026**. L'intention d'adoption du retrieval hybride (dense + sparse + reranking) est passée de 10,3 % à 33,3 % en un trimestre Q1 2026. Le débat n'est plus "RAG ou pas", mais "quelle architecture de RAG selon mon volume et la nature de mes données". Pour < 100 000 tokens, le pattern LLM Wiki de Karpathy (avril 2026) devient une alternative crédible et 95 % moins coûteuse en tokens que le RAG vectoriel pur.

4. **Le coût par requête est désormais le KPI dirigeant**. Prompt caching Anthropic = -90 % sur input tokens cachés (0,1× le prix standard). Kimi K2.6 est 8 à 10× moins cher que Claude Opus 4.7 pour 75 % de la qualité. Le choix de modèle n'est plus binaire : il devient un arbitrage stratégique par cas d'usage.

5. **Workslop : le coût caché de l'IA mal cadrée**. Étude BetterUp x Stanford (sept. 2025) : 40 % des employés ont reçu du "workslop" (contenu IA poli mais inutile/inexact) sur 30 jours. Coût moyen : 1h56 par incident, 186 $/employé/mois, 9 M$/an pour une entreprise de 10 000 personnes. Argument central pour vendre la gouvernance prompts comme du code.

6. **La sécurité des agents et MCP est en crise ouverte (2026)**. CVE-2025-59536 (CVSS 8.7) sur Claude Code, vulnérabilité MCP STDIO touchant > 7 000 serveurs et > 150 M de téléchargements (avril 2026), 12 % de skills malveillants sur OpenClaw (341/2 857 en janvier 2026), breach Moltbook (1,5 M de clés API exposées en plaintext, février 2026). La sécurité n'est plus un sujet d'expert, c'est un sujet de pilotage.

7. **L'observabilité est devenue obligatoire en production**. LangChain *State of Agent Engineering 2026* : 57 % des organisations ont des agents en prod, 89 % ont une forme d'observabilité, 94 % parmi celles en prod. La qualité reste le blocker n°1 (32 %), la sécurité monte au n°2 dans les grandes entreprises (24,9 %).

---

## DEP-01 — Cadrer un projet IA pour la mise en prod

### Chiffres clés

- **95 % des pilotes GenAI en entreprise n'ont aucun impact P&L mesurable** (MIT NANDA, *The GenAI Divide: State of AI in Business 2025*, août 2025) — [Fortune](https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/)
- **Build vs Buy : 67 % de réussite via achat + partenariat vs ~33 % en build interne** (même rapport MIT NANDA) — [Legal.io](https://www.legal.io/articles/5719519/MIT-Report-Finds-95-of-AI-Pilots-Fail-to-Deliver-ROI-Exposing-GenAI-Divide)
- **78 % des entreprises utilisent l'IA dans au moins une fonction métier** mais seules ~33 % la déploient à l'échelle, et seulement ~6 % atteignent > 5 % d'EBIT attribué à l'IA (McKinsey, *The State of AI in 2025*, mars 2025) — [McKinsey](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai)
- **23 % des organisations scalent un système agentique** dans au moins une fonction (McKinsey, novembre 2025) — [McKinsey PDF](https://www.mckinsey.com/~/media/mckinsey/business%20functions/quantumblack/our%20insights/the%20state%20of%20ai/november%202025/the-state-of-ai-2025-agents-innovation_cmyk-v1.pdf)
- **France : 55 % des TPE-PME utilisent l'IA générative fin 2025**, contre 31 % fin 2024 (Bpifrance, baromètre Osez l'IA, déc. 2025) — [IT Social](https://itsocial.fr/contenus/actualites/intelligence-artificielle-actualites-contenus/bpifrance-constate-un-basculement-des-usages-avec-55-des-tpe-pme-utilisatrices-dia-generative-fin-2025/)

### Outils émergents

- **NIST AI Risk Management Framework** (référentiel public, gratuit) : grille de gouvernance pour critères Go/No-Go.
- **Vianeo** (référence interne QFC) pour cadrer la désirabilité/acceptabilité avant tout sprint technique.
- **AWS Prescriptive Guidance — Generative AI Lifecycle** : framework architecture POC → prod (très pédagogique pour interlocuteur technique). [Lien](https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/dev-architecting.html)
- **Bpifrance Diagnostic IA** ("Osez l'IA", financé) : 700 missions conseil IA réalisées en 2024.
- **Plan Bpifrance "Pionniers de l'IA"** : AAP avec dotation France 2030, ouvert aux PME.

### RetEx documentés

- **Bpifrance Conseil "Osez l'IA"** : 700 diagnostics IA en PME (2024), 9 403 dirigeants formés via Bpifrance University en 2025, 1 084 auto-diagnostics IA. Source institutionnelle datée. [Bpifrance Presse](https://presse.bpifrance.fr/bpifrance-deploie-10-milliards-deuros-pour-developper-lecosysteme-ia-et-soutenir-lappropriation-de-lintelligence-artificielle-par-les-entreprises-francaises)
- **MIT NANDA — la "GenAI Divide"** : sur les 5 % qui réussissent, ce sont presque tous des projets achetés à un éditeur spécialisé + intégrés via partenariat, pas des builds internes.

### Écueils typiques

- **Le "learning gap"** (terme MIT NANDA) : incapacité à intégrer l'IA dans les workflows, structures et culture. Cause racine ≠ technique, mais organisationnelle.
- **Skip de la gouvernance pendant le pilote** → impossibilité de scaler ensuite (audit trails, compliance, reproductibilité absents).
- **Lancer le POC avant d'avoir validé désirabilité/usage** : 95 % d'échec quasi-mécanique.
- **Confondre "adoption" et "transformation"** : usage individuel élevé, transformation organisationnelle nulle.
- **Tout vouloir builder en interne** : ratio de réussite 1/3 contre 2/3 en achat + partenariat.

### Sources principales

- MIT NANDA — *State of AI in Business 2025* — [synthèse](https://www.aigl.blog/state-of-ai-in-business-2025/)
- McKinsey — *The State of AI in 2025* (mars + novembre) — [PDF officiel](https://www.mckinsey.com/~/media/mckinsey/business%20functions/quantumblack/our%20insights/the%20state%20of%20ai/2025/the-state-of-ai-how-organizations-are-rewiring-to-capture-value_final.pdf)
- France Num — Baromètre 2025 — [francenum.gouv.fr](https://www.francenum.gouv.fr/guides-et-conseils/strategie-numerique/comprendre-le-numerique/barometre-france-num-2025-le)
- NIST AI RMF — référentiel gouvernance gratuit

---

## DEP-02 — RAG en production : choisir son architecture

### Chiffres clés

- **L'intention d'adoption du retrieval hybride a triplé en Q1 2026** (10,3 % → 33,3 % en un trimestre) chez les entreprises qui rebâtissent leur RAG (VentureBeat, mars 2026) — [VentureBeat](https://venturebeat.com/data/the-retrieval-rebuild-why-hybrid-retrieval-intent-tripled-as-enterprise-rag-programs-hit-the-scale-wall)
- **Une pipeline de retrieval bien faite réduit les hallucinations de 70 à 90 %** (Techment, RAG in 2026) — [Techment](https://www.techment.com/blogs/rag-in-2026/)
- **Le pattern LLM Wiki de Karpathy** (gist GitHub avril 2026) : 17 M de vues, 5 000 stars, 4 282 forks en quelques jours ; promet 95 % de tokens en moins que le RAG vectoriel pour des bases < 100 000 tokens — [MindStudio](https://www.mindstudio.ai/blog/llm-wiki-vs-rag-markdown-knowledge-base-comparison)
- **Le retrieval hybride améliore le recall de 1 à 9 %** par rapport au vectoriel pur (selon implémentation et corpus) — [TiDB](https://www.pingcap.com/compare/best-vector-database/)

### Outils émergents

- **Pinecone** : managed serverless, zéro ops, premium pricing — référence enterprise.
- **Qdrant** : open-source, performant, contrôle des coûts, devient le challenger n°1 en self-host.
- **Weaviate** : excellence sur hybrid search natif et multi-tenant.
- **Chroma** : prototypage / petits volumes, simple à déployer.
- **MongoDB Atlas Vector Search** : intéressant si l'opérationnel est déjà sur Mongo (pas de nouvelle brique).
- **Cohere Rerank** / **BGE-reranker** (open) : reranking cross-encoder pour la deuxième passe.
- **LLM Wiki pattern (Karpathy)** : alternative gratuite pour bases < 100 000 tokens, knowledge stable.

### RetEx documentés

- **Cas pédagogique Karpathy LLM Wiki** : démontre qu'avant de payer un vector DB, il faut quantifier le volume et la fréquence de mise à jour. Pour beaucoup de PME, une base markdown maintenue par LLM peut suffire.
- **VentureBeat — Q1 2026** : la bascule massive vers le hybride n'est pas une mode, c'est la conséquence du fait que le RAG dense pur plafonne en production sur des corpus métier (acronymes, références produit, codes ATC, etc.).

### Écueils typiques

- **Mauvais chunking = mauvais résultats**, indépendamment du modèle utilisé. Sweet spot Q&A factuel : 256-512 tokens. Tâches analytiques : 512-1 024 tokens.
- **Croire que le choix du vector DB est la décision principale** : c'est en réalité l'embedding model qui pèse le plus sur la qualité.
- **Oublier le reranking** : sauter cette étape sacrifie 10 à 30 % de précision.
- **RAG dense pur sur corpus métier** : rate les acronymes, numéros, codes structurés. Hybride obligatoire.
- **Construire un RAG sans eval pipeline** : impossible de mesurer si une modif prompt/embedding améliore ou dégrade.

### Sources principales

- Avi Chawla — *Daily Dose of DS*, série 8 piliers — [Foundations](https://blog.dailydoseofds.com/p/foundations-of-ai-engineering-and-0a6)
- Karpathy LLM Wiki — [Gist GitHub](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- VentureBeat — *Hybrid retrieval tripled* (mars 2026) — [Lien](https://venturebeat.com/data/the-retrieval-rebuild-why-hybrid-retrieval-intent-tripled-as-enterprise-rag-programs-hit-the-scale-wall)

---

## DEP-03 — Context engineering et coût par requête

### Chiffres clés

- **Prompt caching Anthropic = -90 % sur les tokens input cachés** (0,1× le prix standard sur cache hit) — [Anthropic Docs](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
- **Coût d'écriture du cache : 1,25× standard pour TTL 5 min, 2× pour TTL 1h** — [Anthropic News](https://www.anthropic.com/news/prompt-caching)
- **Workslop : 40 % des employés en ont reçu sur 30 jours**, 1h56 perdues par incident, 186 $/employé/mois, 9 M$/an pour 10 000 employés (BetterUp x Stanford, sept. 2025) — [HBR](https://hbr.org/2025/09/ai-generated-workslop-is-destroying-productivity)
- **Reasoning des LLM commence à se dégrader autour de 3 000 tokens** ; sweet spot pratique : 150-300 mots (état de l'art context engineering 2026) — [Aurimas Griciūnas / SwirlAI](https://www.newsletter.swirlai.com/p/state-of-context-engineering-in-2026)
- **Une JSON schema complexe consomme 500+ tokens** ; 90 outils disponibles = 50 000+ tokens avant la première interaction utilisateur (token economics 2026) — [Maxim AI](https://www.getmaxim.ai/articles/context-engineering-for-ai-agents-production-optimization-strategies/)

### Outils émergents

- **Anthropic Prompt Caching** (TTL 5 min ou 1h) : standard de fait.
- **AWS Bedrock Prompt Caching** : équivalent multi-éditeur.
- **OpenAI prompt caching** : automatique sur les nouveaux modèles, transparent.
- **PromptHub / Helicone / LangSmith** : versioning et A/B test des prompts comme du code.
- **Pydantic** : validation de schémas de sortie structurée (devenu standard).
- **Context products** : nouveau concept (versioned, tested context bundles), intéressant pour la gouvernance de l'IA en équipe métier.

### RetEx documentés

- **HBR — Workslop** : étude conjointe BetterUp Labs + Stanford Social Media Lab, septembre 2025. Un des rares articles institutionnels qui chiffre le coût caché de l'IA mal pilotée.
- **Anthropic — Prompt caching cas client RCA** : un déploiement passe de coût plein à 1/10 sur cache hit > 90 %. Source Anthropic + retour pratique. [Lien](https://www.anthropic.com/news/prompt-caching)
- **DEV Community** — "Anthropic prompt caching cut our RCA cost by 90 %" — illustration concrète mono-organisation. [Lien](https://dev.to/stella_lin_82914c71e25769/anthropic-prompt-caching-cut-our-rca-cost-by-90-5gmb)

### Écueils typiques

- **Démarrer sans prompt caching** alors que le system prompt est stable : surcoût immédiat de 5 à 10×.
- **Charger 50+ outils par défaut "au cas où"** : explosion de la facture avant la première requête.
- **Prompt non versionné, non testé** : régressions invisibles à chaque modification.
- **"Workslop" non détecté** : les employés perdent 2h par incident, le ROI affiché est fictif.
- **Penser "tout balancer dans le contexte" plutôt que sélectionner** : reasoning dégradé au-delà de 3 000 tokens utiles.

### Sources principales

- Anthropic — Prompt Caching docs et news — [Anthropic.com](https://www.anthropic.com/news/prompt-caching)
- HBR — *AI-Generated Workslop Is Destroying Productivity* (sept. 2025) — [Lien](https://hbr.org/2025/09/ai-generated-workslop-is-destroying-productivity)
- Microsoft Research — *New Future of Work Report 2025* — [PDF](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/12/New-Future-Of-Work-Report-2025.pdf)

---

## DEP-04 — Quand fine-tuner et quand ne pas

### Chiffres clés

- **LoRA atteint 90-95 % de la qualité du full fine-tuning pour ~10 % du coût** (Index.dev, 2026) — [Index.dev](https://www.index.dev/skill-vs-skill/ai-lora-vs-qlora-vs-full-finetuning)
- **QLoRA = 33 % d'économie mémoire vs LoRA, +39 % de temps de training** (même source)
- **Full fine-tuning d'un modèle 7B requiert 100-120 GB VRAM** (~50 000 $ de H100 par run) ; **QLoRA fait tourner ce même 7B sur une RTX 4090 à 1 500 $** — [Stratagem Systems](https://www.stratagem-systems.com/blog/lora-fine-tuning-cost-analysis-2026)
- **LoRA fine-tuning Llama 3.2 8B sur 1 000 exemples ≈ 5-15 $ de cloud GPU** — [Stratagem Systems](https://www.stratagem-systems.com/blog/lora-fine-tuning-cost-analysis-2026)
- **QLoRA fait tourner du 70B sur du matériel qui peinerait sur du 7B en full FT** (1× A100 80 GB suffit là où 4 à 8 GPUs seraient nécessaires) — [Introl](https://introl.com/blog/fine-tuning-infrastructure-lora-qlora-peft-scale-guide-2025)

### Outils émergents

- **Unsloth** : framework open-source, 2-5× plus rapide qu'à mains nues, GitHub très actif.
- **Hugging Face PEFT** : librairie standard pour LoRA / QLoRA / DoRA.
- **Axolotl** : configuration YAML déclarative pour fine-tuning.
- **OpenAI Fine-Tuning API** / **Anthropic FT** : si on veut éviter l'infrastructure.
- **Together AI / Modal / Replicate** : plateformes managées pour exécuter du LoRA sans gérer le GPU.
- **Premai / Predibase** : plateformes enterprise pour LoRA en prod.

### RetEx documentés

- **B2B SaaS avec doc technique spécialisée** : LoRA = sweet spot. 24-48 GB VRAM suffisent, training 2-6h.
- **Secteurs réglementés (santé, finance, juridique)** : full fine-tuning peut se justifier malgré 5-10× le coût, pour 1-3 % d'accuracy en plus.
- **PME généraliste** : prompt + RAG suffit dans la grande majorité des cas. Le fine-tuning n'est PAS la première option.

### Écueils typiques

- **Fine-tuner avant d'avoir épuisé prompt + RAG** : pertes de temps et d'argent quasi-systématiques.
- **Croire que "plus de données = mieux"** : qualité > volume. 1 000 exemples bien curés battent 100 000 médiocres.
- **Fine-tuner sur LLM qui change** : tout est à refaire au prochain modèle. Privilégier prompt + RAG si la base évolue vite.
- **Sous-estimer les coûts d'infra cachés** : H100, stockage, monitoring, A/B test post-FT.
- **Pas d'eval set avant FT** : impossible de prouver que ça améliore quoi que ce soit.

### Sources principales

- Hugging Face — docs PEFT / LoRA officielles
- Unsloth GitHub — référence open-source
- Index.dev — *LoRA vs QLoRA vs Full Fine-tuning 2026* — [Lien](https://www.index.dev/skill-vs-skill/ai-lora-vs-qlora-vs-full-finetuning)
- Stratagem Systems — *LoRA Fine-Tuning Cost 2026* — [Lien](https://www.stratagem-systems.com/blog/lora-fine-tuning-cost-analysis-2026)

---

## DEP-05 — Agents en production : observabilité et garde-fous

### Chiffres clés

- **57 % des organisations ont des agents en production** (LangChain, *State of Agent Engineering 2026*) — [LangChain](https://www.langchain.com/state-of-agent-engineering)
- **89 % des organisations ont une forme d'observabilité** sur leurs agents ; **94 % parmi celles ayant des agents en prod**. **62 % font du tracing détaillé** (71,5 % en prod) — même source
- **32 % citent la qualité comme blocker n°1** ; **20 % la latence** ; **24,9 % la sécurité dans les grandes entreprises (2k+ employés)** — même source
- **12 % de skills malveillants détectés sur OpenClaw en janvier 2026** (341/2 857 skills communautaires) — [Cyberdesserts](https://blog.cyberdesserts.com/ai-agent-security-risks/)
- **43 % des serveurs MCP publics vulnérables aux attaques d'exécution de commandes** (audit février 2026) — même source

### Outils émergents

- **LangSmith** : managed cloud + BYOC + self-hosted. Tracing complet, dashboards (P50, P99, cost, error rates). Référence chez les utilisateurs LangChain.
- **Comet Opik** : open-source (auto-hébergeable), tracing + eval + online evaluation par LLM-as-Judge en temps réel. Alternative crédible et libre. [GitHub](https://github.com/comet-ml/opik)
- **LangFuse** : open-source, monté en gamme rapide en 2026.
- **Helicone** : observabilité légère et rapide à déployer, pricing PME-friendly.
- **AgentShield** : scanner de configs agents (CLAUDE.md, MCP, hooks). Né au Cerebral Valley x Anthropic Hackathon (fév. 2026) — [GitHub](https://github.com/affaan-m/agentshield)
- **Ragas** : eval RAG pipelines (faithfulness, context recall).
- **Pydantic + Argilla** : validation schémas + human-in-the-loop.

### RetEx documentés

- **LangChain — State of Agent Engineering 2026** : 89 % d'observabilité côté organisations ayant déployé. Devenu un standard de fait, plus optionnel.
- **OWASP Agentic Skills Top 10** (publié 2026) : référentiel public désormais utilisable comme grille d'audit. [OWASP](https://owasp.org/www-project-agentic-skills-top-10/)

### Écueils typiques

- **Mettre un agent en prod sans tracing** : impossible de comprendre les erreurs et d'itérer.
- **Pas de retry/fail-safe** sur les outils externes (timeouts, rate limits) → cascade de pannes.
- **Sur-permission des outils** ("write to disk", "exec shell") sans audit régulier.
- **Pas de kill-switch budget** : agent qui boucle = facture qui explose en heures.
- **Confondre logs applicatifs et tracing LLM** : besoin de capturer prompt + tool call + raisonnement étape par étape.
- **Skills/MCP non audités** : 12 % de malware sur OpenClaw, 43 % de MCP vulnérables. La supply chain agentique est compromise.

### Sources principales

- LangChain — *State of Agent Engineering 2026* — [Lien](https://www.langchain.com/state-of-agent-engineering)
- Comet Opik docs — [Lien](https://www.comet.com/docs/opik/)
- OWASP Agentic Skills Top 10 — [Lien](https://owasp.org/www-project-agentic-skills-top-10/)

---

## DEP-06 — Inférence et coûts : SaaS vs self-hosted

### Chiffres clés

- **vLLM atteint jusqu'à 24× plus de throughput que TGI en haute concurrence** ; sur LLaMA-2-7B, **15 243 tokens/s à 100 requêtes concurrentes vs 4 156 pour TGI** (arXiv 2511.17593, novembre 2025) — [arXiv](https://arxiv.org/abs/2511.17593)
- **PagedAttention réduit la consommation mémoire de 19-27 %** ; **GPU utilization 85-92 % vs 68-74 % pour TGI** — même source
- **Décembre 2025 : Hugging Face met TGI en mode maintenance**, recommande vLLM ou SGLang pour les nouveaux déploiements — [MarkTechPost](https://www.marktechpost.com/2025/11/19/vllm-vs-tensorrt-llm-vs-hf-tgi-vs-lmdeploy-a-deep-technical-comparison-for-production-llm-inference/)
- **Quantization Q4_K_M = ~70 % VRAM en moins pour 1-3 % de qualité perdue** ; +0,18 ppl sur Llama-3-8B — [Will It Run AI](https://willitrunai.com/blog/quantization-guide-gguf-explained)
- **Kimi K2.6 vs Claude Opus 4.7 : 8 à 10× moins cher** (0,60 $ / 2,50 $ vs 5 $ / 25 $ par million de tokens), **75 % de la qualité** — [Composio](https://composio.dev/content/kimi-k2.6-vs-opus-4.7)

### Outils émergents

- **vLLM** (UC Berkeley, OSS) : référence inférence open-source haute performance.
- **SGLang** : alternative montante, recommandée par HF avec vLLM.
- **TensorRT-LLM** (NVIDIA) : top performance sur GPU NVIDIA, plus complexe.
- **LMDeploy** : challenger récent à surveiller.
- **LiteLLM Gateway** : proxy unifié vers 100+ providers, 40k+ stars GitHub. Standard de fait pour faire de la fallback / loadbalancing entre éditeurs. [GitHub](https://github.com/BerriAI/litellm)
- **llama.cpp** : référence inférence CPU/GPU local, GGUF format, Q4_K_M par défaut.
- **Ollama** : couche au-dessus de llama.cpp, "Docker du LLM", parfait pour tester en local.
- **Modal / Replicate / Together / Fireworks** : alternatives serverless pour ne pas gérer le GPU.

### RetEx documentés

- **arXiv 2511.17593** (nov. 2025) : étude académique formelle vLLM vs TGI. Source la plus solide actuellement disponible pour le débat.
- **Pricing public Kimi K2.6 vs Claude Opus 4.7** : illustration parfaite du gradient de coût. Pour un workload de 10M tokens output/mois, ~280 $/jour sur K2.6 vs ~2 500 $/jour sur Opus 4.7.

### Écueils typiques

- **Self-hoster trop tôt** : sous-estimation du TCO (GPU, monitoring, équipe MLOps, redondance, sécurité). Rentable typiquement > 100k requêtes/jour ou contrainte de souveraineté forte.
- **Choisir un modèle premium "par défaut"** : surcoût 10× quand un Kimi/Mistral/Llama feraient l'affaire.
- **Quantization sans eval** : passer de FP16 à Q4 sans mesurer la dégradation business.
- **Ne pas mettre de gateway** (LiteLLM ou équivalent) : impossible de switcher de modèle, pas de fallback, pas de cost tracking unifié.
- **Oublier le coût caché du context window** : doubler le contexte = doubler la facture, pas seulement la latence.

### Sources principales

- vLLM GitHub officiel — [vllm-project/vllm](https://github.com/vllm-project/vllm)
- arXiv 2511.17593 — *Comparative Analysis of LLM Inference Serving Systems* — [Lien](https://arxiv.org/abs/2511.17593)
- LiteLLM docs — [docs.litellm.ai](https://docs.litellm.ai/)
- llama.cpp GitHub — [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)

---

## DEP-07 — Évaluation continue et qualité IA

### Chiffres clés

- **Un Gold Set de production contient typiquement 100 à 300 paires prompt-réponse** mutuellement exclusives, suffisantes pour la significativité statistique en CI/CD — [TestQuality](https://testquality.com/llm-regression-testing-pipeline/)
- **89 % des organisations ont une forme d'observabilité agent**, dont **62 % avec tracing détaillé** (LangChain 2026) — [LangChain](https://www.langchain.com/state-of-agent-engineering)
- **Quality = blocker n°1 (32 % des répondants)** pour passer un agent en prod — même source
- **Ragas, LLM-as-Judge, schema validation** : trio recommandé en 2026 pour couverture maximale à effort minimum (consensus blogs LLMOps)

### Outils émergents

- **Ragas** : eval RAG (faithfulness, context recall, answer relevancy). OSS de référence.
- **DeepEval / Confident AI** : framework eval avec regression suites hostées et A/B testing.
- **LangSmith / Comet Opik / LangFuse** : tracing + eval intégrés, déjà cités DEP-05.
- **MLflow** : suivi d'expérimentations, version 2.x bien adaptée aux LLMs.
- **Pydantic** : validation schémas de sortie (devenu obligatoire).
- **Argilla** : human-in-the-loop pour curer les golden datasets.
- **PromptArmor** (ICLR 2026) : eval anti-injection à intégrer dans la pipeline.

### RetEx documentés

- **Pas de RetEx institutionnel public** trouvé sur PME. Les meilleures pratiques 2026 viennent de blogs LLMOps qui convergent : Gold Set 100-300 prompts + Ragas + LLM-as-Judge sur major version + human eval en sign-off final.
- **MLOps vs LLMOps** : convergence en 2026, mais évaluation reste fondamentalement différente (déterministe vs probabiliste).

### Écueils typiques

- **Pas de golden dataset** : impossible de prouver une amélioration ou détecter une régression.
- **Eval uniquement par LLM-as-Judge** : biais et coût élevés. À réserver aux changements majeurs.
- **Ignorer la dérive (drift)** : le modèle change (mises à jour éditeur), les performances bougent silencieusement.
- **Coupler trop fort eval et CI/CD initialement** : commencer par des batches manuels hebdo, puis automatiser.
- **Mêmes prompts dans Gold Set et entraînement** : leak qui invalide la mesure.
- **Pas de schema validation Pydantic** : sortie LLM cassée = pipeline aval cassée silencieusement.

### Sources principales

- Confident AI / DeepEval docs — [Lien](https://www.confident-ai.com/docs/llm-evaluation/core-concepts/test-cases-goldens-datasets)
- TestQuality — *LLM Regression Testing Pipeline 2026* — [Lien](https://testquality.com/llm-regression-testing-pipeline/)
- LangChain — *State of Agent Engineering 2026* — [Lien](https://www.langchain.com/state-of-agent-engineering)
- Avi Chawla — *MLOps and LLMOps Case Studies* — [Lien](https://blog.dailydoseofds.com/p/mlops-and-llmops-case-studies)

---

## DEP-08 — Sécurité agents et MCP servers

### Chiffres clés

- **CVE-2025-59536 (CVSS 8.7)** : deux failles d'injection de configuration dans Claude Code, divulguées par Check Point Research le 25 février 2026 — [Cyberdesserts](https://blog.cyberdesserts.com/ai-agent-security-risks/)
- **CVE-2026-21852 (CVSS 5.3)** : vol de clés API par redirection des requêtes Claude Code vers un proxy malveillant — même source
- **CVE-2026-30623** : Command Injection via Anthropic MCP SDK (avril 2026, divulgué par OX Security), affectant > 7 000 serveurs MCP publics et > 150 M de téléchargements de packages — [OX Security](https://www.ox.security/blog/the-mother-of-all-ai-supply-chains-critical-systemic-vulnerability-at-the-core-of-the-mcp/) ; [The Hacker News](https://thehackernews.com/2026/04/anthropic-mcp-design-vulnerability.html)
- **CVE-2026-30615** : prompt injection dans Windsurf 1.9544.26 → exécution de commandes à distance via HTML attaquant — [Computing.co.uk](https://www.computing.co.uk/news/2026/security/flaw-in-anthropic-s-mcp-putting-200k-servers-at-risk)
- **Janvier 2026 : 12 % des skills communautaires d'OpenClaw sont malveillants** (341/2 857) — [Cyberdesserts](https://blog.cyberdesserts.com/ai-agent-security-risks/)
- **Février 2026 — Breach Moltbook** : 1,5 M de clés API en plaintext exposées (OpenAI, Anthropic, AWS, GitHub, GCP), 35 000 emails, messages privés. Cause : misconfiguration Supabase RLS — [Wiz](https://www.wiz.io/blog/exposed-moltbook-database-reveals-millions-of-api-keys)
- **OWASP LLM Top 10 — Prompt Injection #1 pour la 3e année consécutive** en 2026 — [TokenMix](https://tokenmix.ai/blog/prompt-injection-defense-techniques-2026)

### Outils émergents

- **AgentShield** (OSS, fév. 2026) : scanner CLAUDE.md, MCP configs, hooks, permissions. [GitHub](https://github.com/affaan-m/agentshield)
- **PromptArmor** (ICLR 2026) : LLM-as-filter en pré-traitement, < 1 % de FP/FN sur AgentDojo benchmark — référence académique.
- **Dual-LLM pattern** : architecture "privileged LLM" (outils, pas de contenu non-trusté) + "quarantined LLM" (lit du non-trusté, pas d'outils). Référence sécurité agentique.
- **OWASP Agentic Skills Top 10** : référentiel public d'audit. [OWASP](https://owasp.org/www-project-agentic-skills-top-10/)
- **NIST AI RMF** : framework américain de référence (utilisé en miroir avec ANSSI / ENISA en Europe).
- **ENISA** : recommandations européennes sur l'IA générative.

### RetEx documentés

- **Moltbook (Wiz, février 2026)** : cas pédagogique parfait. Misconfiguration triviale (Supabase RLS désactivée) → 1,5 M de clés API exposées. À utiliser comme cas d'école dirigeant. [Wiz Blog](https://www.wiz.io/blog/exposed-moltbook-database-reveals-millions-of-api-keys)
- **OX Security — MCP "design flaw"** : Anthropic a refusé de patcher la racine ("expected behavior"). Démontre que la sécurité agentique est encore en gestation et que le pilote PME doit auditer en interne.
- **Check Point Research — CVE Claude Code** : démonstration que même les outils des éditeurs leaders ont des failles critiques en 2026.

### Écueils typiques (5 défenses prompt injection à empiler)

1. **Layer 1 — Structured prompt formatting** : séparer system / user / tool clairement.
2. **Layer 2 — Output schema validation** (Pydantic) : aucune sortie non typée n'est acceptée.
3. **Layer 3 — Rate limit + reputation** : bloquer les patterns d'abus connus.
4. **Layer 4 — PromptArmor / LLM filter en preprocessing** : filtrer les prompts entrants par un LLM dédié.
5. **Layer 5 — Behavioral tool-call monitoring** : alerter sur toute séquence d'outils anormale.

Autres écueils typiques :
- **Stocker des clés API en plaintext** (cas Moltbook) ou commit accidentel sur GitHub.
- **Installer des skills/MCP communautaires sans audit** : 12 % de malware constatés.
- **Pas de kill-switch budget** : un agent compromis peut générer des milliers de $ en heures.
- **Confondre "filter prompt" et "isolate exécution"** : l'isolement (sandbox, dual-LLM) est ce qui protège vraiment.

### Sources principales

- OX Security — *MCP critical vulnerability* (avril 2026) — [Lien](https://www.ox.security/blog/the-mother-of-all-ai-supply-chains-critical-systemic-vulnerability-at-the-core-of-the-mcp/)
- Wiz — *Hacking Moltbook* (février 2026) — [Lien](https://www.wiz.io/blog/exposed-moltbook-database-reveals-millions-of-api-keys)
- OWASP Agentic Skills Top 10 — [Lien](https://owasp.org/www-project-agentic-skills-top-10/)
- Cloud Security Alliance — recommandations IA agentique 2026
- ANSSI / ENISA — recommandations européennes IA

---

## Recommandations éditoriales pour Cowork

**Par ordre de priorité décroissante pour la production des 8 fiches DEP :**

1. **Ancrer toute la section Déploiement sur la statistique MIT NANDA des 95 %** (et son corollaire build vs buy 67 % vs 33 %). C'est le fait qui parle à un dirigeant en 30 secondes. À mettre en exergue dans l'introduction de la section, puis rappeler dans DEP-01 et DEP-04 (ne pas builder = ne pas fine-tuner par défaut).

2. **Construire chaque fiche autour d'une décision binaire que le dirigeant doit trancher**, pas autour d'une description technique. Exemples : DEP-02 = "Vector DB ou LLM Wiki ?", DEP-04 = "Fine-tuner ou pas ?", DEP-06 = "SaaS premium ou self-host ?". Le dirigeant ne lit pas pour apprendre, il lit pour décider.

3. **Systématiser la grille "Quand c'est justifié / Quand ce ne l'est pas / Comment auditer le presta"**. C'est le format qui donne le bon niveau d'exigence à l'interface technique sans la technifier soi-même. Particulièrement vrai pour DEP-04 (fine-tuning), DEP-06 (self-host), DEP-08 (sécurité).

4. **Mettre en avant les coûts cachés** sur chaque fiche : workslop pour DEP-03, surcoût Opus vs Kimi pour DEP-06, breach Moltbook pour DEP-08, factures agent runaway pour DEP-05. Le langage du dirigeant, c'est le P&L.

5. **Citer systématiquement 1 à 2 sources francophones institutionnelles** (Bpifrance, France Num, ANSSI) en plus des sources techniques internationales. Crédibilité + actionnabilité pour l'écosystème Grand Est.

6. **Réserver une encadré "Pour aller plus loin (CTO/presta)"** dans chaque fiche, avec 2-3 liens techniques (GitHub officiels, papers arXiv, Avi Chawla). Cela permet de garder le corps pédagogique court et de servir aussi l'interlocuteur technique sans surcharger.

7. **Adopter une trame visuelle commune** : (a) Le constat chiffré 2026, (b) La décision à trancher, (c) Les 3 options, (d) La grille de choix, (e) Les 3 questions à poser au presta, (f) Les ressources. C'est répétitif volontairement : le dirigeant qui lit la fiche 5 reconnaît la grille de la fiche 1.
