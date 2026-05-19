# whitelist-wikilinks-futurs.md — Liste des MD planifiés mais non encore produits

**Statut :** v2 (post-S2.3 Lot B — 3 modules vague 3 produits)
**Dernière mise à jour :** 13 mai 2026
**Maintainer :** Cowork Hub IA Plateforme

> **Rôle (D-029) :** liste des codes de fichiers MD planifiés dans la roadmap du vault mais pas encore produits. Lue par `audit-md-rag.py` v2 au démarrage. Les wikilinks pointant vers ces codes sont signalés comme **warnings** (anticipations légitimes), pas comme erreurs (wikilinks cassés).

> **Politique de maintenance :** à chaque nouveau MD produit, retirer son code de la whitelist. Si un wikilink pointe vers un code **ni dans le vault ni dans la whitelist** → erreur réelle (wikilink cassé) à corriger.

---

## Modules CU planifiés (à produire vagues 3 à 5)

| Code | Titre métier (rappel cartographie HTML couple 1) | Vague cible |
|---|---|---|
| `cu-002` | Assistant rédactionnel | 3-4 |
| `cu-003` | CR de réunion | 4 |
| `cu-004` | Traduction | 4 |
| `cu-005` | Propositions commerciales B2B complexes | 3-4 |
| `cu-006` | Leads & chatbot | 4 |
| `cu-007` | RH (CV, entretiens) | 3-4 |
| `cu-009` | Content repurposing | 4 |
| `cu-010` | Pipeline contenu social | 4 |
| `cu-011` | Veille concurrentielle | 3-4 |
| `cu-012` | Veille AAP & drafting | 4 |
| `cu-013` | Workflow email-CRM | 4 |
| `cu-014` | Multi-agents par fonction | 3 |
| `cu-015` | Asynchronicité agentique — cas Stripe Minions | 4 |
| `cu-016` | Maintenance prédictive | 4-5 |
| `cu-017` | Contrôle qualité par vision IA | 4-5 |
| `cu-018` | Optimisation production / nesting | 4-5 |
| `cu-019` | Newsletter locale | 4 |
| `cu-020` | Conformité RGPD & AI Act | 3-4 |
| `cu-021` | Finance & comptabilité augmentées | 4 |
| `cu-022` | Voicebot accueil téléphonique | 4 |
| `cu-023` | Devis simples — porte d'entrée IA | 4 |
| `cu-024` | Order-to-cash automation | 4 |
| `cu-025` | Knowledge management IA-augmenté pour dirigeant | 3 |
| ~~`cu-026`~~ | ~~Gouvernance des agents IA~~ | ✅ **Produit S2.3 Lot B — retiré whitelist le 13 mai 2026** |
| ~~`cu-027`~~ | ~~Faire développer une appli métier (sans être IT)~~ | ✅ **Produit S2.3 Lot B — retiré whitelist le 13 mai 2026** |

## Préalables PR planifiés (à produire vagues 3 à 4)

| Code | Titre métier | Vague cible |
|---|---|---|
| `pr-01` | Maturité organisationnelle | 3-4 |
| `pr-02` | Préalables data & SI | 3-4 |
| `pr-03` | Maturité humaine & formation | 3-4 |
| `pr-04` | Marché IA & emploi | 3-4 |
| `pr-05` | Sécurité IA | 3-4 |
| `pr-06` | Qualité du code IA | 3-4 |

## Fiches déploiement DEP planifiées (à produire vagues 3 à 5)

| Code | Titre métier | Vague cible |
|---|---|---|
| `dep-01` | Cadrer un projet IA pour la mise en production | 3-4 |
| `dep-03` | Context engineering et coût par requête | 4 |
| `dep-04` | Fine-tuning : quand y aller, quand ne pas | 4 |
| `dep-05` | Agents en production : observabilité et garde-fous | 3-4 |
| `dep-06` | Inférence et coûts : SaaS vs self-hosted | 3-4 |
| `dep-07` | Évaluation continue et qualité IA | 3-4 |
| ~~`dep-08`~~ | ~~Sécurité agents et MCP servers~~ | ✅ **Produit S2.3 Lot B — retiré whitelist le 13 mai 2026** |

## Architectures planifiées

| Code | Titre | Vague cible |
|---|---|---|
| `a1` | SaaS propriétaire | 4 |
| `a2` | Propriétaire managé EU | 4 |
| `a3` | Open-source cloud souverain | 4 |
| `a4` | Open-source on-premise | 4 |

## Briques transverses planifiées (priorisées dans STATUS-RAG §Vague 3)

| Code | Portée (rappel) | Priorité |
|---|---|---|
| ~~`pattern-llm-wiki`~~ | ~~Pattern LLM Wiki Karpathy distillé + 5 patterns post-Karpathy~~ | ✅ **Produit S2.2 Lot A — retiré whitelist le 12 mai 2026** |
| ~~`pattern-persistent-memory`~~ | ~~Pattern Persistent memory 4 signaux + agentmemory benchmarks~~ | ✅ **Produit S2.4 Phase 2 Lot F.1 — 13 mai 2026** (post-RETOUR-SONDAGE-S2.4, validation D-025 SPEC v1.6 — symétrique pattern-llm-wiki) |
| `pattern-eval-set-golden` | Méthodologie golden set + Stitch → Evaluate → Iterate + LLM-as-judge | 🟡 Moyenne (à coupler avec dep-07) |
| `pattern-build-vs-buy` | Matrice 6 critères + 3 scénarios distillés | 🟢 Basse (à coupler avec module appelant) |
| `methodologie-prompt-engineering` | 4 étapes universelles (question, contexte, vérification, itération) | 🟡 Moyenne |
| `cadrage-ai-act-2026` | Article 50 + Omnibus VII + watermarking + calendrier | 🟡 Moyenne |
| `calendrier-facturation-electronique` | Dates précises 2026-2027 | 🟢 Basse |
| `gouvernance-agents-ia` | Framework 7 dimensions CU-026 distillé | 🟡 Moyenne |
| `strategie-souverainete-eu` | Choix SaaS US vs souverain EU | 🟢 Basse |

## Fiches outils par catégorie planifiées (issu cartographie HTML couple 1)

À produire au fil des modules qui les nécessitent — pas urgent en vague 3.

- `outils-llm` (modèles LLM : Claude, GPT, Gemini, Mistral, Llama, Kimi K2.6, DeepSeek)
- `outils-frameworks-rag` (LangChain, LlamaIndex, Dify, Flowise)
- `outils-ide-dev-ia` (Cursor, Claude Code, Windsurf, GitHub Copilot Workspace)
- `outils-app-builders-no-code` (Lovable, Bolt.new, v0, Replit Agent)
- `outils-workflow-automation` (n8n, Make, Zapier, LangFlow, AAFLOW)
- `outils-llm-gateway` (LiteLLM, OpenRouter, Helicone)
- `outils-observabilite-llm` (Comet Opik, LangSmith, Helicone, Phoenix Arize, Langfuse)
- `outils-gardefous-prompt-injection` (NeMo Guardrails, Lakera Guard, Rebuff)
- `outils-audit-securite-agents` (AgentShield, Snyk, Semgrep)
- `outils-inference-open-source` (vLLM, llama.cpp, Unsloth, Triton, Ollama)
- `outils-voice` (Whisper, ElevenLabs)
- `outils-knowledge-management` (Obsidian, GBrain, Readwise, Airr, NotebookLM, Beever Atlas, SuperSplat)
- `outils-compta-facturation-fr` (Pennylane, Sellsy, Axonaut, Esker, Sidetrade, Tacton)
- `outils-crm-propositions` (HubSpot, Salesforce, PandaDoc)
- `outils-navigateurs-agentiques` (Atlas, Comet, Claude pour Chrome, Operator)
- `outils-agents-frameworks-multi-agents` (Lindy, Manus, ClickUp Brain, Hermes Agent)

## Notes de maintenance

- **Total codes whitelistés** : 27 modules CU + 6 préalables PR + 7 DEP + 5 architectures + 8 brain pages transverses + 16 catégories outils = **69 codes**
- **À jour au 12 mai 2026** : seuls les codes effectivement produits dans `rag/content/` sont à retirer (à ce stade : `glossaire`, `cu-001`, `cu-008`, `pr-07`, `dep-02`, `outils-vector-db`, `chiffres-macro-2026`, `vigilance-hallucinations`, `vigilance-confidentialite` — non listés ci-dessus car dans le vault)
- **Procédure** : à chaque production MD, vérifier que le code disparaît de cette whitelist (sinon erreur de maintenance)

## Historique des versions

| Version | Date | Modification |
|---|---|---|
| v1 | 12 mai 2026 | Initialisation post-S1bis (D-029), 69 codes whitelistés couvrant vagues 3 à 5 |
| v2 | 13 mai 2026 | S2.3 Lot B — retrait de `cu-026`, `cu-027`, `dep-08` (produits dans le vault). 66 codes restant whitelistés. |
