# DEP-06 — Inférence et coûts : SaaS vs self-hosted

**Public cible :** dirigeant + CTO arbitrant entre API SaaS et self-host

---

## Métadonnées (pour Claude Code)

- **Section** : Déploiement
- **Niveau** : ⭐⭐⭐⭐ Expert
- **Type** : Cadrage stratégique
- **Durée lecture** : 18 min
- **Emoji h1** : ⚙️
- **Titre métier visible** : « Inférence et coûts : SaaS vs self-hosted »
- **Sous-titre hero** : Kimi K2.6 = 8-10× moins cher que Claude Opus 4.7. vLLM = 2-4× plus de débit que les serveurs naïfs. Quantization Q4_K_M = ~1 % de qualité perdue, 4× moins de mémoire. Le self-host n'est plus réservé aux ETI.
- **Card index promesse** : « Cadrage stratégique »

## Synthèse exécutive

### Pourquoi cette page ?

Tu as commencé à utiliser des API LLM (Anthropic, OpenAI, Mistral). Les factures grimpent. Tu te demandes : **« est-ce que je devrais self-host ? »**. La réponse n'est ni oui ni non. C'est un arbitrage entre **coût récurrent**, **latence**, **souveraineté**, **complexité ops**, et **flexibilité**.

Cette fiche te donne le tableau de décision, les outils 2026 (vLLM, LiteLLM, llama.cpp, Unsloth, Kimi K2.6), les seuils où le self-host devient rentable, et les écueils typiques.

### 4 takeaways

1. **Le self-host devient rentable au-delà d'un seuil de volume mensuel.** Seuil approximatif : **> 5 M de tokens/mois** pour un modèle moyen. En dessous, l'API SaaS reste économiquement et opérationnellement supérieure. Au-delà, le self-host commence à valoir son investissement initial.

2. **vLLM est le standard d'inférence open-source.** Avec son innovation **PagedAttention**, vLLM réduit le gaspillage de mémoire KV cache de 60-80 % à < 4 %, soit **2-4× plus de débit** que les serveurs naïfs (TGI, Text Generation Inference). Si tu self-hostes un modèle open-source, vLLM est le choix par défaut.

3. **La quantization 4-bit est le levier coût n°1 du self-host.** Q4_K_M (le format llama.cpp standard) compresse les poids du modèle d'un facteur 4 (FP16 → 4-bit) avec **~1 % de perplexité perdue** seulement. Conséquence : un modèle 70B fine-tuné peut tourner sur **1 seul GPU 24GB** (RTX 4090, RTX 5090).

4. **Kimi K2.6 change l'équation économique du SaaS lui-même.** Open-source chinois performant (proche Claude Opus 4.7 sur SWE-Bench), proposé en API à **0,80 $/M input et 3,60 $/M output** soit 8-10× moins cher qu'Opus. Pour 75 % des cas d'usage agentic coding, c'est suffisant. Question : self-host Kimi ou utiliser son API ?

### Stats (3-4)

- **2-4×** plus de débit avec vLLM PagedAttention vs serveurs naïfs (60-80 % → < 4 % de gaspillage KV cache)
- **~1 % de perplexité perdue** avec quantization 4-bit (Q4_K_M)
- **8-10×** moins cher : Kimi K2.6 vs Claude Opus 4.7
- **> 5 M tokens/mois** : seuil approximatif où le self-host devient rentable

### Quand cette page est utile

Tu as une facture LLM mensuelle qui dépasse 500-1000 €/mois et tu te demandes si tu peux la réduire. Tu as une contrainte de souveraineté (données ultra-sensibles, secret industriel). Tu veux tester un modèle spécifique non disponible en SaaS. Tu veux comprendre les ordres de grandeur avant de discuter avec ton CTO ou prestataire.

## Section 1 — Le cadre de décision SaaS vs self-hosted

### 1.1 Cinq critères à pondérer

| Critère | Favorise SaaS | Favorise self-hosted |
|---|---|---|
| **Volume mensuel** | < 5 M tokens | > 5 M tokens |
| **Latence** | 200ms acceptable | < 50ms requis (temps réel) |
| **Souveraineté** | EU + RGPD suffisant | SecNumCloud / cloud souverain strict |
| **Complexité ops** | Pas d'équipe ops | Équipe IT en place |
| **Flexibilité** | Modèle standard OK | Besoin spécifique (fine-tuning, modèles non standards) |

→ Si > 3 critères favorisent self-host : envisage. Sinon, reste SaaS.

### 1.2 La règle « default SaaS » pour la plupart des PME

Pour la majorité des cas d'usage PME, **l'API SaaS est meilleure**. Raisons :
- Maintenance externalisée (mises à jour modèles, sécurité, conformité)
- Pas de Capex GPU (10-30 K€ pour un GPU H100/A100)
- Time-to-value rapide
- Modèles régulièrement mis à jour (Claude Sonnet 4.6 → 4.7 → ... transparent)

→ Le self-host devient pertinent **après** avoir prouvé la valeur en SaaS et atteint un volume significatif.

## Section 2 — vLLM et l'optimisation d'inférence

### 2.1 Le problème : le gaspillage du KV cache

Les serveurs LLM naïfs (TGI, FastAPI custom) gaspillent **60 à 80 % de la mémoire allouée au KV cache** (key-value cache, qui stocke les états intermédiaires des tokens déjà traités). Conséquence : peu de requêtes parallèles possibles, sous-utilisation du GPU.

### 2.2 La solution vLLM : PagedAttention

vLLM a inventé **PagedAttention** (2023, Berkeley), inspiré de la pagination mémoire OS. Au lieu d'allouer un bloc contigu de KV cache par requête, vLLM alloue par **petites pages** allouées dynamiquement.

**Résultat** : gaspillage tombe à < 4 %, soit **2-4× plus de débit** sur le même GPU.

→ Si tu self-hostes un modèle open-source, vLLM est devenu le standard 2024-2026.

### 2.3 Les autres serveurs d'inférence

| Serveur | Profil | Quand l'utiliser |
|---|---|---|
| **vLLM** | Open-source, PagedAttention, débit max | Cas par défaut self-host |
| **TGI (Hugging Face)** | Open-source, plus simple, intégration HF native | Si déjà sur écosystème HF |
| **Triton Inference Server (Nvidia)** | Production-grade enterprise, multi-modèles | Stack Nvidia complet |
| **llama.cpp** | C++ pur, supporte CPU + GPU, ultra-léger | Inférence on-device, edge, dev local |
| **Ollama** | Wrapper llama.cpp pour dev | Dev local et POC, pas pour prod |

## Section 3 — La quantization, levier coût n°1

### 3.1 Le principe

La **quantization** réduit la précision numérique des poids du modèle (FP16 16-bit → INT8 8-bit → INT4 4-bit). Effet : moins de mémoire requise, plus de tokens/seconde, **avec une perte de qualité minime** si bien fait.

### 3.2 Les formats de quantization courants

| Format | Mémoire | Perte qualité | Quand l'utiliser |
|---|---|---|---|
| **FP16** | Référence (1×) | 0 % | Modèle production critique |
| **INT8** | 0,5× | < 0,5 % | Bonne option par défaut |
| **Q4_K_M (llama.cpp)** | 0,25× (4×) | ~1 % | Self-host budget contraint |
| **Q3_K_M** | 0,2× | 2-3 % | Cas extrêmes |
| **Q2_K** | 0,15× | 5-10 % | Démo / dev seulement |

→ Sweet spot 2026 : **Q4_K_M** pour le self-host PME. Permet de faire tourner un Llama 70B sur un seul GPU 24GB.

### 3.3 Les outils de quantization

- **llama.cpp** : référence open-source, supporte 1.5-bit à 8-bit
- **Hugging Face Optimum** : kit pour quantization + ONNX export + hardware optim
- **bitsandbytes** : librairie 8-bit / 4-bit utilisée par Transformers / Unsloth
- **Unsloth** : 2× plus rapide pour fine-tuning + inférence quantizée

## Section 4 — Le LLM gateway, brique transverse essentielle

### 4.1 Pourquoi un LLM gateway

Si tu utilises plusieurs modèles (Claude, OpenAI, Mistral, Kimi, modèle self-hosted), tu veux :
- Un seul code à maintenir (interface unifiée)
- Routage intelligent (selon coût, qualité, disponibilité)
- Fallback automatique (si un modèle est down)
- Cost tracking centralisé
- Cache transparent

→ C'est le rôle du **LLM gateway**.

### 4.2 LiteLLM, le standard open-source 2026

**LiteLLM** unifie 100+ APIs LLM derrière une interface OpenAI-compatible. Open-source, self-hostable, gratuit.

Fonctions clés :
- Routage par modèle, coût, latence
- Fallback automatique
- Cost tracking par utilisateur / projet
- Cache transparent
- Rate limiting

→ Setup PME : 1-3 jours pour basculer ton code de « API directe Anthropic » vers « via LiteLLM gateway ».

### 4.3 Alternatives commerciales

- **OpenRouter** : SaaS multi-LLM avec routing
- **Helicone** : LLM gateway + observabilité (cf. [DEP-05](dep-05-agents-observabilite.html))
- **Portkey** : SaaS gateway + caching

## Section 5 — Le cas Kimi K2.6 — la rupture économique 2026

### 5.1 Les faits

**Kimi K2.6** (Moonshot AI, sortie 2026, open-source) :
- **0,80 $/M input, 3,60 $/M output** (vs Claude Opus 4.7 : 5 $/M input, 25 $/M output)
- **Open-source** : self-hostable
- **Performance** : proche Claude Opus 4.7 sur SWE-Bench, Terminal-Bench, agentic coding (~75-90 % de la qualité)
- API disponible chez Together.ai, Modal Labs, Fireworks AI

### 5.2 Implication pour la PME

Pour 75 % des cas d'usage agentic coding (cf. [CU-027 Faire développer une appli métier](../modules/cu-027-dev-applicatif-ia.html)), Kimi K2.6 est suffisant. Économie typique : **80-90 % de la facture** vs Opus.

→ Question stratégique : **garder Opus pour les 25 % vraiment complexes, basculer 75 % sur Kimi**.

### 5.3 Self-host Kimi K2.6 ?

Si tu as les compétences, oui. Kimi K2.6 est self-hostable sur GPU H100 cluster. Mais à ce niveau, comparer avec utiliser l'API Together.ai ou Fireworks AI hébergeant Kimi en EU. Le self-host n'est rentable qu'à partir de **plusieurs millions de tokens/jour**.

## Section 6 — Tableau de décision rapide

| Cas d'usage | Volume mensuel | Recommandation 2026 |
|---|---|---|
| Démarrage IA, exploration | < 1 M tokens | API SaaS (Anthropic, OpenAI, Mistral) |
| PME en croissance, multi-cas | 1-5 M tokens | API SaaS via **LiteLLM gateway** + caching |
| PME avec exigence souveraineté | Quelconque | API EU (Mistral, Anthropic EU, OpenAI EU) ou self-host |
| Volume significatif, cas standards | 5-50 M tokens | LLM gateway + dispatch modèle pas cher (Kimi, Mistral) |
| Volume très significatif | > 50 M tokens | Self-host vLLM avec quantization Q4_K_M |
| Souveraineté + volume | > 50 M tokens + secret | Self-host on-premise ou cloud souverain |
| Ultra basse latence (< 50ms) | Quelconque | Self-host avec llama.cpp ou vLLM proche utilisateurs |

## Section 7 — Plan d'action 60 jours pour optimiser ton inférence

### Jours 1-15 — Audit
- Mesure facture mensuelle par cas d'usage
- Identifier le coût par requête / coût par utilisateur
- Mesurer la latence p95

### Jours 16-30 — Quick wins SaaS
- Déployer un LLM gateway (LiteLLM)
- Implémenter prompt caching (cf. [DEP-03](dep-03-context-engineering-couts.html))
- Tester routage Kimi K2.6 sur 75 % des cas d'usage simples

### Jours 31-45 — Évaluer self-host
- Si volume > 5 M tokens/mois : POC vLLM avec un modèle open-source (Llama 8B ou Mistral 7B)
- Calcul TCO 12 mois : Capex GPU + ops + énergie vs API mensuelle

### Jours 46-60 — Décision
- Si TCO self-host < 50 % du SaaS sur 12 mois : migration progressive
- Sinon : rester SaaS, optimiser caching et routage

## Section 8 — Pour aller plus loin (Schéma A)

### Callout d'aiguillage

> Pour le panorama complet des serveurs d'inférence et outils self-host, retrouve les fiches détaillées sur la [page Ressources du Hub](../ressources.html#bibliographie).

### 📰 Articles de fond
- [Avi Chawla — DevOps vs MLOps vs LLMOps](https://blog.dailydoseofds.com/p/foundations-of-ai-engineering-and-0a6) — Pilier 6 LLM Engineering Roadmap
- [vLLM blog — PagedAttention announcement](https://blog.vllm.ai/) — Innovation technique de référence
- [Together.ai — Kimi K2.6 hosting analysis](https://www.together.ai/) — Analyse économique modèle vs API

### 🎓 Tutoriels & cas pratiques
- [vLLM Quickstart](https://docs.vllm.ai/en/latest/getting_started/quickstart.html) — Lancer un serveur en 10 min
- [llama.cpp tutorials](https://github.com/ggerganov/llama.cpp) — Inférence locale optimisée
- [Unsloth Notebooks](https://github.com/unslothai/unsloth) — Fine-tuning + inférence accélérés

### 📚 Documentation officielle & études
- [vLLM GitHub](https://github.com/vllm-project/vllm) — Référence inférence open-source
- [LiteLLM Docs](https://docs.litellm.ai/) — Gateway open-source
- [llama.cpp GitHub](https://github.com/ggerganov/llama.cpp) — Quantization 1.5-bit à 8-bit
- [Hugging Face Optimum](https://github.com/huggingface/optimum) — Quantization, ONNX, hardware optim
- [bitsandbytes GitHub](https://github.com/bitsandbytes-foundation/bitsandbytes) — Lib 8-bit / 4-bit

### 👥 Communautés & veille
- [r/LocalLLaMA](https://reddit.com/r/LocalLLaMA) — Communauté self-host LLM
- [vLLM Discord](https://discord.com/invite/jz7wjKhh6g) — Échanges techniques

## Renvois internes pour Claude Code

- **Section 4.3 (Helicone)** : lien `<a href="dep-05-agents-observabilite.html">DEP-05</a>`
- **Section 5.2** : lien `<a href="../modules/cu-027-dev-applicatif-ia.html">CU-027</a>`
- **Section 7 (caching)** : lien `<a href="dep-03-context-engineering-couts.html">DEP-03</a>`

## Composants visuels suggérés

- **Section 1.1** : `.tool-table` pour les 5 critères
- **Section 3.2** : `.tool-table` pour les formats quantization
- **Section 6** : `.tool-table` pour le tableau de décision
- **Section 7** : `.timeline-block` pour le plan d'action 60 jours

## Note Cowork
Sources prioritaires : Avi Chawla, vLLM, llama.cpp, Together.ai. Conforme RULES § 1.1.
