---
code: outils-llm
titre: "Outils — Modèles LLM"
type: fiche-outil
axe: transverse
niveau: 3
tags: [llm, claude, gpt, mistral, llama, kimi, lucie, pleias-rag, lighton, notebooklm, multimodal, contexte-long, souverainete]
version: 3.12.0
last_updated: 2026-05-25
glosaire_termes: [llm, agent, rag, prompt, embeddings, souverainete]
derives: ["[[cu-001]]", "[[cu-002]]", "[[cu-008]]", "[[cu-013]]", "[[cu-025]]", "[[cu-027]]", "[[dep-02]]", "[[dep-04]]", "[[dep-06]]", "[[pattern-souverainete-eu]]", "[[chiffres-macro-2026]]"]
public_cible: [dirigeant, ops, r&d, tech]
---

# Outils — Modèles LLM

## Quand utiliser un modèle LLM

Un [[glossaire#llm]] est le moteur central de tout usage IA générative en 2026 : génération texte, synthèse, traduction, classification, extraction structurée, raisonnement, code, ou encore moteur d'un [[glossaire#agent]] qui exécute des actions. Le marché 2026 mature offre **11 modèles de référence** structurants : 4 modèles commerciaux US (Claude, GPT, Mixtral, NotebookLM), 1 modèle commercial EU mixte (Mistral), 1 modèle open-weight permissif (Llama), 1 modèle open-weight chinois (Qwen, Kimi K2.6), et 4 modèles souverains FR (Mistral, Lucie, Pleias-RAG, LightOn).

Le choix dépend du cas d'usage (génération texte vs code vs raisonnement vs multimodal), du volume (free tier vs SaaS vs API vs self-host), du niveau de [[glossaire#souverainete]] exigé (cf. [[pattern-souverainete-eu]] 4 niveaux), du contexte fonctionnel (fenêtre de contexte 200 K vs 400 K vs 1 M tokens), et du budget (de 0,80 $/MTok pour les open-source jusqu'à 75 $/MTok pour les modèles raisonnement premium).

Tarifs canoniques 2026 transposés textuellement depuis ressources.html (R10 stricte). Articulation avec [[dep-06]] (arbitrages économiques inférence) et [[chiffres-macro-2026]] (chiffres macro adoption IA).

## Claude (Anthropic) — référence raisonnement et code

Claude est le modèle le plus utilisé en 2026 pour les usages **raisonnement complexe** (analyse stratégique, synthèse documentaire, agents pilotant d'autres outils) et le **développement de code** (via Claude Code, l'IDE intégré natif d'Anthropic). Combo : excellente qualité de génération + suivi d'instructions précis + contexte long natif (200 K standard, 1 M bêta) + multimodalité (texte + images).

**Quand l'utiliser** : raisonnement long-form (notes stratégiques, analyses), génération de code, agents autonomes avec planification, RAG avec longs contextes, tâches sensibles où la qualité prime sur le coût.

**Quand ne pas l'utiliser** : usages haute volumétrie temps réel avec budget serré (préférer GPT-4o ou Mistral), souveraineté EU stricte requise (US-based, voir [[pattern-souverainete-eu]]).

**Modèle économique** : API Sonnet **3 $/MTok input + 15 $/MTok output** · API Opus **15 $/MTok input + 75 $/MTok output** · Free tier limité (claude.ai web) · **Claude Pro 20 $/mois utilisateur**. Multimodal natif. Contexte 200 K standard / 1 M en bêta accès. Souveraineté niveau **Light** (US, hébergement EU optionnel).

**Cas d'usage Hub** : [[cu-001]] (Sources fiables IA), [[cu-002]] (Assistant rédactionnel), [[cu-008]] (Knowledge base RAG), [[cu-025]] (Knowledge management dirigeant), [[cu-027]] (Faire développer une appli métier sans être IT).

**Lien** : claude.com / docs.anthropic.com

## GPT (OpenAI) — référence universelle multimodal

GPT (GPT-4o, GPT-5, GPT-5 mini) reste la référence mainstream du marché LLM 2026. Modèle généraliste de très grande qualité, multimodal natif (texte + image + voix + vidéo en preview), fenêtre de contexte étendue à 400 K (fév-mars 2026, mode raisonnement adaptatif). Premier marché en termes d'écosystème tiers (intégrations, agents, plugins).

**Quand l'utiliser** : usages bureautiques généralistes, ChatGPT pour productivité quotidienne, intégration via API dans des outils tiers (le plus large écosystème), tâches multimodales (vision, voix).

**Quand ne pas l'utiliser** : raisonnement complexe long-form (préférer Claude), souveraineté EU stricte (US-based, voir [[pattern-souverainete-eu]]).

**Modèle économique** : API GPT-4o **~2,50 $/MTok input + 10 $/MTok output** · **ChatGPT Plus 20 $/mois** · **ChatGPT Team 25-30 $/mois** · ChatGPT Enterprise sur devis. Fenêtre 400 K (fév-mars 2026, mode raisonnement adaptatif). Souveraineté niveau **Light** (US).

**Cas d'usage Hub** : [[cu-001]] (Sources fiables IA), [[cu-002]] (Assistant rédactionnel), [[cu-013]] (Workflow email-CRM).

**Lien** : openai.com / platform.openai.com

## Mistral — référence souveraine EU

Mistral (FR) est le **leader européen** des modèles LLM avec Mistral Large 2 (modèle propriétaire dense), Mixtral 8x7B et Mixtral 8x22B (modèles MoE open-weight), Le Chat (chatbot web grand public) et Le Chat Pro (offre PME). Combo : qualité comparable à GPT-4 pour la plupart des tâches + souveraineté EU + écosystème open-weight permissif.

**Quand l'utiliser** : besoin de souveraineté EU (cf. [[pattern-souverainete-eu]] niveau Moderate à Strong), self-hosting via Mixtral open-weight, usages PME générique avec Le Chat Pro, alternative au stack US.

**Quand ne pas l'utiliser** : usages exigeant l'écosystème mainstream ChatGPT/Claude (intégrations tierces moins matures), agents complexes nécessitant Claude-level reasoning.

**Modèle économique** : **API Mistral Large 2 ~3 $/MTok input** · **Le Chat Pro 14,99 €/mois utilisateur** · **Mixtral open-weight gratuit (Apache 2.0)** · Mistral Forge sur devis (enterprise on-premise). Souveraineté niveau **Moderate à Strong** (FR, hébergement EU + open-weight).

**Cas d'usage Hub** : [[cu-001]] (Sources fiables IA souveraines), [[cu-002]] (Assistant rédactionnel EU), [[cu-008]] (RAG souverain), [[pattern-souverainete-eu]] (acteur de référence).

**Lien** : mistral.ai / docs.mistral.ai

## NotebookLM (Google) — RAG conversationnel sur sources uploadées

NotebookLM est un outil **RAG conversationnel** où l'utilisateur uploade des sources (PDF, docs, URLs, vidéos YouTube) et dialogue avec le LLM Google contraint à ces sources. Avantage différenciant : Audio Overviews (podcasts auto-générés à partir des sources), sourçage strict avec citations.

**Quand l'utiliser** : RAG personnel ou équipe sur petits corpus (<100 sources), synthèse documentaire avec sourçage strict, génération audio à partir de documents, dialogue préparatoire à une décision avec littérature de référence.

**Quand ne pas l'utiliser** : RAG production multi-utilisateurs (préférer [[outils-vector-db]] + Claude/GPT API), corpus > 100 documents (limite NotebookLM), souveraineté EU stricte (Google US, voir [[pattern-souverainete-eu]]).

**Modèle économique** : Free tier 50 sources × 100 notebooks · **NotebookLM Plus dans Google AI Pro 19 $/mois utilisateur** · Enterprise via Google Workspace (variable selon plan). Souveraineté niveau **Light** (US).

**Cas d'usage Hub** : [[cu-001]] (Sources fiables IA), [[cu-008]] (alternative SaaS au RAG self-hosted), [[cu-025]] (Knowledge management dirigeant).

**Lien** : notebooklm.google.com

## Mixtral (Mistral) — modèle MoE open-weight

Mixtral (8x7B et 8x22B) est l'architecture **Mixture-of-Experts** (MoE) open-weight de Mistral. Avantage : meilleure efficacité paramètre / qualité que les modèles denses équivalents. Idéal pour le self-hosting EU souverain quand on a la capacité GPU.

**Quand l'utiliser** : self-hosting sur infrastructure GPU EU (souveraineté niveau Strong), arbitrage économique vs API SaaS (cf. [[dep-06]]), besoin d'auditer le code et les poids du modèle.

**Quand ne pas l'utiliser** : pas d'équipe DevOps/MLOps capable d'opérer un cluster d'inférence GPU, volumes très faibles (API SaaS sera moins chère), exigence de modèle premium (préférer Claude Opus).

**Modèle économique** : **Open-weight gratuit (Apache 2.0)** · Via API Mistral La Plateforme **~0,7-2 $/MTok selon variante** · Via Together / Fireworks ~0,5-2 $/MTok · Coût réel infrastructure GPU + MLOps si self-host. Souveraineté niveau **Strong** (FR open-weight + auto-hébergeable).

**Cas d'usage Hub** : [[cu-008]] (RAG souverain self-hosted), [[dep-04]] (Fine-tuning), [[pattern-souverainete-eu]] (acteur de référence).

**Lien** : mistral.ai/news/mixtral-8x7b / huggingface.co/mistralai

## Llama (Meta) — open-weight référence

Llama (Llama 3, Llama 4) est le **modèle open-weight de référence** marché 2026. Combo : qualité comparable aux modèles commerciaux + licence Community permissive + énorme écosystème de variantes fine-tunées. Choix par défaut pour le self-hosting sur infrastructure US ou EU.

**Quand l'utiliser** : self-hosting sur infrastructure GPU, fine-tuning métier (cf. [[dep-04]]), arbitrage économique vs SaaS, recherche et expérimentation.

**Quand ne pas l'utiliser** : équipe sans capacité MLOps GPU, exigence de support enterprise (préférer Claude/GPT/Mistral), souveraineté EU stricte (éditeur US — niveau Light selon hébergement, voir [[pattern-souverainete-eu]]).

**Modèle économique** : **Community License Meta (gratuite)** · Via providers Together / Fireworks / Replicate **~0,2 à 3 $/MTok selon taille modèle** · Coût réel infrastructure GPU + MLOps si self-host. Souveraineté niveau **Light à Moderate** (éditeur US mais open-weight permissif).

**Cas d'usage Hub** : [[cu-008]] (RAG self-hosted), [[dep-04]] (Fine-tuning), [[dep-06]] (Inférence SaaS vs self-hosted).

**Lien** : llama.com / huggingface.co/meta-llama

## Qwen (Alibaba) — open-weight chinois performant

Qwen (séries Qwen 2.5, Qwen 3) est la **famille de modèles open-weight chinoise**, hautement compétitive en 2026 (équivalent ou supérieur à Llama sur de nombreux benchmarks). Disponible en plusieurs tailles (Qwen 7B, 14B, 72B) avec licences ouvertes.

**Quand l'utiliser** : self-hosting alternatif à Llama (souvent meilleurs scores), tâches multilingues incluant le chinois, expérimentation et recherche.

**Quand ne pas l'utiliser** : exigence de souveraineté EU stricte (éditeur CN, niveau Light voire à éviter selon sensibilité données), équipe sans capacité MLOps GPU.

**Modèle économique** : **Open-weight gratuit (Tongyi Qianwen License)** · Via providers cloud (Together, Fireworks) **~0,2-1,50 $/MTok**. Souveraineté niveau **Light** (éditeur CN, hébergement à arbitrer).

**Cas d'usage Hub** : [[cu-008]] (RAG self-hosted multilingue), [[dep-04]] (Fine-tuning), expérimentation et benchmark.

**Lien** : qwenlm.github.io / huggingface.co/Qwen

## Kimi K2 / K2.6 (Moonshot AI) — long contexte premium

Kimi K2 et K2.6 sont des modèles **chinois open-weight** spécialisés dans le **contexte long** (jusqu'à 2 millions de tokens en V2.6) et le raisonnement. Disponibles via Together.ai, Modal Labs, Fireworks AI (hébergement EU possible) ou self-hosting.

**Quand l'utiliser** : raisonnement sur contextes très longs (> 500 K tokens), self-hosting ou inférence cloud EU via Fireworks, alternative économique à Claude Opus pour le raisonnement.

**Quand ne pas l'utiliser** : exigence souveraineté EU stricte (éditeur CN, voir [[pattern-souverainete-eu]] niveau Light), usages mainstream avec besoin d'écosystème intégrations.

**Modèle économique** : **0,80 $/MTok input + 3,60 $/MTok output** (chiffres canoniques cohérents avec [[chiffres-macro-2026#kimi-k26-tarifs]] via I-D-005). API via Together.ai, Modal Labs, Fireworks AI (EU possible), ou self-host. Souveraineté niveau **Light** (éditeur CN, inférence selon provider).

**Cas d'usage Hub** : [[cu-008]] (RAG long contexte), [[cu-025]] (Synthèse documentaire dirigeant volumes importants), [[dep-06]] (Inférence économique cloud EU).

**Lien** : moonshot.ai / together.ai/models/kimi-k2

## Lucie (souverain FR) — open-weight français

Lucie est le **modèle open-weight souverain français** porté par le consortium LINAGORA et financé par BPI France. Trajectoire : équivalent Mistral 7B + extension à des modèles 13B et 70B. Pleinement souverain (éditeur FR, open-weight, hébergeable EU).

**Quand l'utiliser** : souveraineté EU stricte (niveau Strong cf. [[pattern-souverainete-eu]]), self-hosting EU souverain, démarche de soutien à l'écosystème français, expérimentation et recherche académique.

**Quand ne pas l'utiliser** : exigence qualité top-tier équivalent Claude/GPT-4 (Lucie reste en deçà sur les benchmarks complexes), pas d'équipe MLOps GPU.

**Modèle économique** : **Open-weight gratuit** + infrastructure GPU pour self-host. Pas d'API SaaS Lucie native mature à ce jour (mai 2026) — déploiement via OVHcloud, Scaleway, ou self-host. Souveraineté niveau **Strong** (FR open-weight + hébergeable EU).

**Cas d'usage Hub** : [[pattern-souverainete-eu]] (acteur de référence souverain), [[cu-008]] (RAG souverain démonstrateur), expérimentation et tests souverains.

**Lien** : linagora.com/lucie / huggingface.co/OpenLLM-France

## Pleias-RAG (souverain FR) — spécialisé RAG juridique et réglementaire

Pleias-RAG est un **modèle open-weight souverain français spécialisé RAG** (corpus juridique, réglementaire, scientifique). Conçu pour minimiser les hallucinations sur tâches de citation et de sourçage strict, idéal pour les usages où la traçabilité légale prime.

**Quand l'utiliser** : RAG juridique/réglementaire avec sourçage critique, conformité (cf. [[cu-020]]), souveraineté EU stricte, démarche de soutien écosystème FR.

**Quand ne pas l'utiliser** : usages généralistes hors RAG (Mistral Large 2 ou Claude seront meilleurs), pas d'équipe technique pour self-host.

**Modèle économique** : **Open-weight individuel et recherche gratuit** · **API Pleias usage commercial (tarif à la requête)** — indicatif **~10-50 €/mois usage TPE**, **~200-800 €/mois PME juridique active**. Souveraineté niveau **Strong** (FR open-weight + hébergement EU).

**Cas d'usage Hub** : [[cu-008]] (RAG juridique/réglementaire souverain), [[cu-020]] (Conformité RGPD/AI Act), [[pattern-souverainete-eu]] (acteur de référence).

**Lien** : pleias.fr / huggingface.co/pleias

## LightOn (souverain FR) — solution enterprise full souveraine

LightOn est la **solution enterprise full souveraine française**, intégrant modèles LLM propriétaires + plateforme RAG + observabilité + déploiement on-premise ou SecNumCloud. Cible : grands comptes EU avec exigences de souveraineté niveau Sovereign (OIV, OSE, défense, santé).

**Quand l'utiliser** : souveraineté niveau Sovereign requise (cf. [[pattern-souverainete-eu]]), exigence SecNumCloud (ANSSI), grands comptes avec >1 000 utilisateurs, conformité réglementaire stricte (santé HDS, défense, OIV/OSE).

**Quand ne pas l'utiliser** : PME avec budget < 100 K€/an (cible enterprise), POC ou prototypage (cible production critique), besoin de modèle de référence mainstream (préférer Mistral Le Chat Pro).

**Modèle économique** : **Tarification enterprise sur devis** — typiquement **100-500 K€/an pour 1 000 utilisateurs** (licence + déploiement + support + mises à jour). Souveraineté niveau **Sovereign** (FR, on-premise ou SecNumCloud).

**Cas d'usage Hub** : [[pattern-souverainete-eu]] (acteur de référence souverain Sovereign), [[pr-05]] (Sécurité IA cadrage stratégique), [[cu-020]] (Conformité réglementaire stricte).

**Lien** : lighton.ai

## Comparatif synthétique

| Outil | Souveraineté | Tarif référence | Volume cible | Cas Hub principal |
|---|---|---|---|---|
| **Claude** (Sonnet) | Light (US) | 3 $/15 $/MTok | Production raisonnement + code | Knowledge mgmt, agents, code |
| **Claude** (Opus) | Light (US) | 15 $/75 $/MTok | Raisonnement premium | Décision stratégique, analyses |
| **GPT-4o** | Light (US) | 2,50 $/10 $/MTok | Production multimodale | Bureautique, écosystème intégrations |
| **Mistral Large 2** | Moderate (FR) | ~3 $/MTok input | Production souveraine EU | RAG souverain, alternative SaaS US |
| **Le Chat Pro** | Moderate (FR) | 14,99 €/mois | PME productivité | Chatbot bureautique souverain |
| **NotebookLM** | Light (US) | 19 $/mois (Plus) | RAG personnel/équipe | KM dirigeant, sourçage strict |
| **Mixtral open-weight** | Strong (FR self-host) | Gratuit + infra GPU | Self-hosting EU | RAG souverain niveau avancé |
| **Llama** | Light/Moderate | Gratuit + infra GPU | Self-hosting général | Fine-tuning, recherche |
| **Qwen** | Light (CN open-weight) | Gratuit + infra | Self-hosting multilingue | Benchmark, recherche |
| **Kimi K2.6** | Light (CN) | 0,80 $/3,60 $/MTok | Contexte très long | Synthèse documentaire massive |
| **Lucie** | Strong (FR open-weight) | Gratuit + infra GPU | Self-hosting souverain | Démonstrateur souverain |
| **Pleias-RAG** | Strong (FR open-weight) | Gratuit / 10-800 €/mois | RAG juridique souverain | Conformité, juridique |
| **LightOn** | Sovereign (FR enterprise) | 100-500 K€/an | Grands comptes critiques | Souveraineté maximale |

## Recommandations PME par profil

**PME 5-15 salariés non-tech, usage productivité général** : Le Chat Pro (14,99 €/mois) ou Claude Pro (20 $/mois) — choix arbitré sur souveraineté (Le Chat EU) vs fonctionnalités premium (Claude Opus).

**PME 15-50 salariés avec dirigeant data-friendly, usages variés** : Claude (Sonnet API + Pro) pour raisonnement et code + GPT-4o (Plus ou API) pour multimodal et écosystème. Budget ~100-300 €/mois.

**PME 50-150 salariés avec sensibilité souveraineté** : Mistral Le Chat Pro (PME) + Mistral Large 2 API (intégrations) + Mixtral self-host (cas avancés). Niveau Moderate à Strong selon configuration.

**PME 50-500 salariés secteur santé / défense / OIV** : LightOn enterprise + déploiement SecNumCloud + Pleias-RAG pour conformité juridique. Niveau Sovereign, budget significatif.

**Démarche démonstrateur / R&D souverain** : Lucie + Pleias-RAG + Mixtral en self-host EU. Coût : infrastructure GPU + temps MLOps.

## Pour aller plus loin

- **Pattern souveraineté EU des outils IA** ([[pattern-souverainete-eu]]) : 4 critères + 4 niveaux + acteurs de référence par catégorie
- **Arbitrage économique SaaS vs self-hosted** ([[dep-06]]) : calculer le seuil de bascule
- **Fine-tuning** ([[dep-04]]) : quand et comment fine-tuner un modèle open-weight
- **Frameworks RAG** ([[outils-frameworks-rag]]) : intégrer le LLM dans une stack RAG
- **Vector stores** ([[outils-vector-db]]) : la brique embedding-recherche du RAG
- **Chiffres macro 2026** ([[chiffres-macro-2026]]) : adoption marché LLM en PME
