# Phase 3 — Matière éditoriale 13 fiches outils émergents 2026

**Auteur** : Cowork (Claude desktop)
**Pour** : Blaise Cavalli — Startup Manager Quai Alpha
**À transmettre à** : Claude Code pour intégration dans `ressources.html`
**Date** : mai 2026

---

## Contexte

Cette matière éditoriale couvre 13 outils émergents identifiés par la veille pré-itération comme prioritaires pour la page Ressources du Hub IA Learning Center. Format inspiré des 63 fiches deep-dive existantes (`.tool-card`, badges, blocks, etc.).

**Note d'intégration pour Claude Code** :
- Réutiliser le format `.tool-card` existant (cf. ressources.html v3.2)
- Appliquer les **5 dimensions de badges** (Type / Catégorie / Maturité / Souveraineté + Coût / Complexité ajoutées en patch v3.2)
- Si la **catégorie 17ᵉ « 🎙️ Voice & speech »** n'existe pas encore, la créer dans le sommaire (entre « 📨 Email & scraping » et « 👁️ Vision industrielle » par exemple)
- 4 fiches souveraines FR/EU 🇪🇺 (Lucie, Pleias-RAG, LightOn, Voxtral, Kleo, Mistral Agents) renforcent l'équilibre souveraineté du site

---

## 🧠 Catégorie : LLM & modèles génératifs (3 nouvelles fiches souveraines)

### 1. Lucie / OpenLLM-France

- **Vendor** : Linagora + OpenLLM-France (consortium)
- **Catégorie** : LLM open-source souverain francophone
- **Type** : Open-source
- **Souveraineté** : 🇫🇷🇪🇺
- **Maturité** : N4-N6 (pilote)
- **Coût** : 🟢 Gratuit (auto-hébergé)
- **Complexité** : 🛠️🛠️🛠️ Intégration

**Tagline**
LLM open-source francophone porté par un consortium académique et industriel français. Financé France 2030 / Bpifrance. Lancé janvier 2025, projet sur 2 ans depuis septembre 2024. Alternative souveraine pour les déploiements RAG sur documents publics français et les usages PME sensibles.

**Description**
Lucie est l'aboutissement du projet OpenLLM-France lancé par Linagora et un consortium d'acteurs académiques et industriels français en 2024. Objectif : produire un modèle de langage open-source totalement transparent (poids + corpus + méthode d'entraînement) avec une qualité francophone supérieure aux modèles US généralistes. Financement France 2030 / Bpifrance. La V1 a été lancée en janvier 2025, avec des itérations régulières en 2026.

**À quoi ça sert**
- RAG sur documents publics français (administrations, archives, code, jurisprudence)
- Déploiement souverain TPE/PME pour usages traitant des données stratégiques ou personnelles
- Cas d'usage où l'AI Act impose une transparence totale sur le modèle (Article 4 + lignes directrices haut risque)
- Recherche académique sur LLM francophones

**Quand l'utiliser**
- Tu as un cas d'usage avec données sensibles ou stratégiques que tu ne veux pas exposer à OpenAI/Anthropic
- Tu veux un modèle 100 % auditable (transparence corpus + poids + entraînement)
- Tu disposes d'un GPU local ou d'un budget cloud souverain pour l'inférence

**Quand NE PAS l'utiliser**
- Cas d'usage qui demande la performance frontière (GPT-5, Claude Opus 4.7) : Lucie est positionnée pertinente mais pas frontière
- Tu n'as pas de compétence DevOps pour déployer (préférer Mistral managed dans ce cas)

**Stack & intégrations**
- Hébergement : auto-hébergé GPU (NVIDIA A100/H100), ou cloud souverain Outscale, OVHcloud, Scaleway
- Frameworks : compatible Hugging Face Transformers, vLLM, llama.cpp
- Articulation : peut être utilisé comme backend LLM dans n8n / LangGraph / CrewAI

**Modèle économique**
- Modèle open-source sous licence permissive
- Coût = uniquement infrastructure (GPU + bande passante)
- Indicatif : ~80-200 €/mois pour un déploiement TPE-PME en cloud souverain (modèle moyen, charges modestes)

**Cas d'usage dans nos modules**
- [CU-008 Knowledge base RAG](modules/cu-008-knowledge-base-rag.html) — RAG souverain sur corpus interne
- [CU-020 Conformité RGPD & AI Act](modules/cu-020-conformite-rgpd-ai-act.html) — option souveraine pour usages sensibles
- [CU-021 Finance augmentée](modules/cu-021-finance-augmentee.html) — alternative à Claude/GPT sur données financières

**Alternatives**
- Mistral (souverain EU, plus mature)
- Mixtral (open-weight, alternative)
- Llama (Meta, anglophone par défaut)

**Pour aller plus loin**
- [Site officiel Lucie / OpenLLM-France](https://openllm-france.fr/)
- [Linagora — webinar Lucie](https://linagora.com/en/openllm-webinar-lucie-truly-open-source-sovereign-model)
- [HuggingFace Hub — modèles Lucie](https://huggingface.co/OpenLLM-France)

---

### 2. Pleias-RAG (Pico, Nano, Small)

- **Vendor** : Pleias
- **Catégorie** : Petits modèles RAG / SLM spécialisés
- **Type** : Open-weight
- **Souveraineté** : 🇫🇷🇪🇺
- **Maturité** : N4-N6 (pilote validé sur cas juridique / compliance)
- **Coût** : 🟢 Gratuit (auto-hébergé) ou 🟡 Freemium (API hébergée)
- **Complexité** : 🛠️🛠️ Setup léger (modèles compacts)

**Tagline**
Famille de petits modèles spécialisés pour le RAG (Retrieval-Augmented Generation) en français, entraînés sur le Common Corpus (2 trillions de tokens 100 % domaine public). Conformité RGPD/AI Act native, créneau juridique et compliance. Modèles compacts adaptés à l'on-premise et l'edge.

**Description**
Pleias est une startup française qui développe une famille de petits modèles (Pico, Nano, Small) optimisés pour le RAG, sourcés de manière 100 % transparente sur le Common Corpus — un corpus de 2T tokens uniquement issus du domaine public (Wikipedia, archives, codes, jurisprudence libre, etc.). C'est une réponse directe aux enjeux de souveraineté et de transparence imposés par l'AI Act, particulièrement adapté aux secteurs juridique, compliance et administration publique.

**À quoi ça sert**
- RAG juridique avec citations sourcées (chaque réponse précise la source du Common Corpus)
- Compliance et audit réglementaire (transparence corpus = preuve d'absence de biais commerciaux)
- Déploiement edge / on-premise (modèles compacts 1-3B paramètres)
- Cas d'usage avec contraintes très fortes sur la traçabilité des données d'entraînement

**Quand l'utiliser**
- Cabinet d'avocats, expertise comptable, audit, conformité
- Administrations publiques avec exigences de transparence
- Cas d'usage où la « source attribution » est critique (chaque réponse doit citer ses sources)

**Quand NE PAS l'utiliser**
- Tâches généralistes ou créatives (préférer Claude/Mistral)
- Volumes massifs de tokens (les petits modèles ne battent pas les grands sur la finesse de raisonnement)

**Stack & intégrations**
- Hébergement : auto-hébergé (CPU pour Pico, GPU léger pour Nano/Small) ou API Pleias hébergée
- Frameworks : compatible Hugging Face Transformers, llama.cpp pour edge
- Articulation : intègre nativement avec vector stores (Qdrant, pgvector)

**Modèle économique**
- Open-weight pour usage individuel et recherche
- API hébergée Pleias pour usage commercial (tarification à la requête)
- Indicatif : ~10-50 €/mois pour usage TPE, ~200-800 €/mois pour PME juridique active

**Cas d'usage dans nos modules**
- [CU-008 Knowledge base RAG](modules/cu-008-knowledge-base-rag.html) — RAG juridique souverain
- [CU-020 Conformité RGPD & AI Act](modules/cu-020-conformite-rgpd-ai-act.html) — recommandé pour secteurs juridiques/compliance
- [CU-012 Veille AAP & drafting](modules/cu-012-veille-aap-drafting.html) — drafting de candidatures avec citations sourcées

**Alternatives**
- Lucie (Linagora, open-source FR plus généraliste)
- Mistral (souverain EU, plus mature mais moins spécialisé compliance)
- Solutions juridiques propriétaires (Lexis+ AI, Doctrine, Predictice — mais SaaS US)

**Pour aller plus loin**
- [Pleias — site officiel](https://pleias.fr/)
- [ActuIA — Pleias et l'IA éthique](https://www.actuia.com/actualite/pleias-des-modeles-de-langages-ouverts-pour-une-ia-ethique-et-transparente/)
- [HuggingFace Hub — modèles Pleias](https://huggingface.co/PleIAs)

---

### 3. LightOn (Paradigm)

- **Vendor** : LightOn (Paris)
- **Catégorie** : LLM enterprise on-premise souverain
- **Type** : Hybride (SaaS + on-premise)
- **Souveraineté** : 🇫🇷🇪🇺 (membre OpenEuroLLM)
- **Maturité** : N7-N8 (enterprise-grade)
- **Coût** : 🔴 Entreprise (devis sur mesure)
- **Complexité** : 🛠️🛠️🛠️🛠️ Projet (déploiement enterprise)

**Tagline**
LLM enterprise français spécialisé dans les déploiements on-premise pour grandes administrations, banques et industries critiques. Membre du consortium OpenEuroLLM. Positionnement souveraineté maximale + capacités enterprise-grade (RAG, fine-tuning, monitoring, support).

**Description**
LightOn est une startup parisienne fondée en 2016, originellement dans le hardware optique pour ML, repositionnée 2023-2026 sur les LLM enterprise européens. Sa plateforme **Paradigm** est une solution complète (LLM + RAG + fine-tuning + monitoring + support) déployable en mode SaaS, mais surtout **on-premise** pour les structures avec exigences souveraineté maximale (ministères, banques, défense, santé).

**À quoi ça sert**
- Déploiement LLM enterprise sur infrastructure cliente (on-premise ou cloud privé)
- Fine-tuning sur corpus propriétaire avec garanties de non-dissémination
- RAG enterprise avec gouvernance et audit poussés
- Cas d'usage haut risque AI Act avec exigences de souveraineté

**Quand l'utiliser**
- Grandes administrations (ministères, collectivités majeures)
- Banques, assurances, secteurs régulés
- Industries critiques (défense, énergie, santé hospitalière)
- ETI 1000+ avec contraintes RGPD/AI Act très fortes

**Quand NE PAS l'utiliser**
- TPE / PME (overkill, surcoût important)
- Usage à coût marginal (préférer Mistral managed)
- Besoin de modèle frontière qualité (LightOn est correct mais pas frontière)

**Stack & intégrations**
- Hébergement : on-premise (déploiement par LightOn sur infrastructure cliente) ou cloud privé Paradigm
- Frameworks : intégrations entreprise (SAML, AD, Kerberos, audit), connecteurs CRM/ERP
- Support : équipe dédiée, SLA enterprise

**Modèle économique**
- Tarification enterprise sur devis (typiquement 100-500 K€/an pour un déploiement 1000 utilisateurs)
- Inclut licence + déploiement + support + mises à jour

**Cas d'usage dans nos modules**
- [CU-020 Conformité RGPD & AI Act](modules/cu-020-conformite-rgpd-ai-act.html) — option pour structures publiques et grandes ETI
- [CU-012 Veille AAP & drafting](modules/cu-012-veille-aap-drafting.html) — drafting confidentiel avec souveraineté maximale

**Alternatives**
- Mistral on-premise (Mistral Forge)
- Goodweek (gouvernance multi-LLM avec auditabilité)
- Aleph Alpha (DE, en phase de fermeture commerciale 2026)
- Solutions IBM watsonx (US, mais déploiement EU possible)

**Pour aller plus loin**
- [LightOn — site officiel](https://www.lighton.ai/)
- [Paradigm by LightOn](https://www.lighton.ai/paradigm)
- [OpenEuroLLM consortium](https://openeurollm.eu/)

---

## 🎙️ Catégorie 17 (à créer) : Voice & speech (4 fiches)

### 4. Voxtral

- **Vendor** : Mistral AI
- **Catégorie** : Modèle vocal souverain (STT + TTS)
- **Type** : Open-weight + API Mistral
- **Souveraineté** : 🇫🇷🇪🇺
- **Maturité** : N4-N6 (pilote validé)
- **Coût** : 🟡 Freemium (open-weight gratuit, API tarifée)
- **Complexité** : 🛠️🛠️ Setup léger (API) ou 🛠️🛠️🛠️ Intégration (auto-hébergé)

**Tagline**
Modèle de speech-to-text et text-to-speech open-weight développé par Mistral AI. Alternative souveraine européenne à Whisper, Deepgram, ElevenLabs et Cartesia, particulièrement pertinent pour les voicebots traitant des données sensibles ou les structures avec exigences AI Act renforcées.

**Description**
Voxtral est la réponse de Mistral AI au besoin croissant de souveraineté sur la chaîne voice. Modèle open-weight publié sous licence Apache 2.0, performant en français et dans les langues européennes. Couvre STT (transcription temps réel et batch) et TTS (synthèse vocale). Disponible en mode auto-hébergé ou via l'API Mistral hébergée en EU.

**À quoi ça sert**
- Voicebots souverains pour secteurs sensibles (santé, finance, public)
- Transcription de réunions confidentielles (juridique, RH, M&A)
- Pipeline voice complet en stack 100 % EU (Voxtral STT + Mistral LLM + Voxtral TTS)
- Alternative open-source à Whisper pour déploiements on-premise

**Quand l'utiliser**
- Cas d'usage voicebot avec exigence souveraineté EU forte
- Déploiement on-premise nécessaire
- Stack 100 % Mistral pour cohérence et négociation enterprise

**Quand NE PAS l'utiliser**
- Latence ultra-critique (préférer Cartesia Sonic 90-150 ms)
- Qualité vocale émotionnelle premium (préférer ElevenLabs Conv 2.0)

**Stack & intégrations**
- Hébergement : auto-hébergé (GPU) ou API Mistral hébergée EU
- Frameworks : compatible Hugging Face Transformers, vLLM, integration Vapi (en cours 2026)
- Articulation : pipeline voice complet avec Mistral LLM

**Modèle économique**
- Open-weight gratuit pour auto-hébergement
- API Mistral : tarification au token / minute (compétitive avec Deepgram et ElevenLabs)

**Cas d'usage dans nos modules**
- [CU-022 Voicebot accueil téléphonique IA](modules/cu-022-voicebot-accueil.html) — option souveraine recommandée
- [CU-003 Comptes-rendus de réunion](modules/cu-003-cr-reunion.html) — alternative souveraine à Whisper

**Alternatives**
- Whisper (OpenAI, open-source, anglais > français)
- Deepgram Nova-3 (US, premium qualité streaming)
- Cartesia (US, leader latence TTS)
- ElevenLabs (US, leader qualité émotionnelle TTS)

**Pour aller plus loin**
- [Voxtral — annonce Mistral](https://mistral.ai/news/voxtral) (URL prévisionnelle)
- [HuggingFace — Voxtral models](https://huggingface.co/mistralai)
- [Speechmatics — comparatif STT 2026](https://www.speechmatics.com/company/articles-and-news/best-speech-to-text-ai-guide-apis-platforms-and-services-compared)

---

### 5. Cartesia (Sonic / Line)

- **Vendor** : Cartesia
- **Catégorie** : TTS ultra-faible latence + plateforme voice
- **Type** : SaaS
- **Souveraineté** : 🇺🇸
- **Maturité** : N4-N6 (production-ready)
- **Coût** : 🟡 Freemium (free tier généreux pour tests)
- **Complexité** : 🛠️ Plug-and-play (API simple)

**Tagline**
TTS le plus rapide du marché en 2026 (90-150 ms latence), avec qualité naturelle élevée. Concurrent direct ElevenLabs sur le créneau agents vocaux temps réel. Voix françaises naturelles, tarif accessible PME, intégrations Vapi / Twilio / WebSocket natives.

**Description**
Cartesia a percé en 2025 avec son modèle Sonic, qui a établi un nouveau standard de latence TTS sub-150 ms — faisant tomber le seuil psychologique de la « pause robotique » dans les conversations agent vocal. Le produit Line ajoute une plateforme complète de gestion d'agent vocal (orchestration STT + LLM + TTS). La qualité vocale française est désormais excellente, particulièrement sur les voix neutres et professionnelles.

**À quoi ça sert**
- Voicebots avec exigence latence (médical, e-commerce, support client)
- Agents vocaux conversationnels temps réel
- Synthèse vocale pour podcasts, vidéos, formations e-learning

**Quand l'utiliser**
- Voicebots production avec besoin de fluidité conversationnelle (la latence Sonic fait la différence)
- Agents vocaux multi-tour avec interruptions du locuteur
- Tu veux une plateforme complète gérée (Cartesia Line)

**Quand NE PAS l'utiliser**
- Voix très émotionnelles ou créatives premium (préférer ElevenLabs)
- Souveraineté EU stricte (préférer Voxtral)

**Stack & intégrations**
- API REST + WebSocket pour streaming temps réel
- Intégrations natives : Vapi, Twilio, LiveKit, Pipecat
- SDK Python, JavaScript, Go

**Modèle économique**
- Free tier généreux (~10-20 minutes/mois pour tests)
- Plan PME ~50-200 €/mois selon volume
- Plan enterprise sur devis

**Cas d'usage dans nos modules**
- [CU-022 Voicebot accueil téléphonique IA](modules/cu-022-voicebot-accueil.html) — recommandé pour latence
- [CU-009 Content repurposing](modules/cu-009-content-repurposing.html) — synthèse vocale podcasts / formations

**Alternatives**
- ElevenLabs Conv 2.0 (qualité émotionnelle premium)
- Voxtral (souverain EU)
- Deepgram Aura (TTS streaming alternatif)
- Azure Neural TTS (Microsoft, qualité solide mais moins rapide)

**Pour aller plus loin**
- [Cartesia — site officiel](https://cartesia.ai/)
- [Documentation Cartesia](https://docs.cartesia.ai/)
- [Cartesia vs ElevenLabs vs Deepgram](https://cartesia.ai/vs/elevenlabs-vs-deepgram)

---

### 6. ElevenLabs Conversational AI 2.0

- **Vendor** : ElevenLabs
- **Catégorie** : TTS premium + agent vocal full-stack
- **Type** : SaaS
- **Souveraineté** : 🇺🇸
- **Maturité** : N7-N8 (industrie mature)
- **Coût** : 🟡 Freemium (tier gratuit limité) → 🟠 Payant (plans PME)
- **Complexité** : 🛠️🛠️ Setup léger

**Tagline**
Référence qualité émotionnelle TTS en 2026. Voix synthétiques indiscernables de l'humain, gamme étendue de styles (formel, chaleureux, jeune, autoritaire). La V2 Conversational AI ajoute une couche complète d'agent vocal (LLM + tools + workflows) en plus du TTS pur.

**Description**
ElevenLabs s'est imposé en 2024-2025 comme la référence qualité TTS premium, particulièrement sur les voix émotionnelles. La V2 Conversational AI ajoute une plateforme complète qui gère l'agent vocal end-to-end (STT + LLM + tools + TTS), permettant de construire des voicebots de qualité production en quelques heures. Le produit est aussi très utilisé pour la synthèse audio dans le marketing, les podcasts, les jeux vidéo, et la création de contenu.

**À quoi ça sert**
- Voicebots haut de gamme où la voix est un élément différenciant marque
- Synthèse audio pour podcasts, vidéos, e-learning, jeux vidéo
- Doublage et localisation multilingue
- Voix de marque cohérente sur tous les points de contact (web, app, vocal)

**Quand l'utiliser**
- Cible premium ou luxe où la voix est un élément de marque fort
- Cas créatifs (podcasts, formations vidéo, narration)
- Tu veux la plateforme complète sans assemblage custom

**Quand NE PAS l'utiliser**
- Latence ultra-critique (Cartesia Sonic devance ElevenLabs sur ce point)
- Souveraineté EU stricte (préférer Voxtral)
- Budget limité TPE (free tier vite saturé)

**Stack & intégrations**
- API REST, WebSocket, SDK Python/JavaScript
- Intégrations natives : Vapi, Twilio, Make, Zapier, Bubble
- Catalogue de 1000+ voix dont une cinquantaine françaises

**Modèle économique**
- Free tier (~10 000 caractères/mois)
- Starter ~5 €/mois (30 000 caractères)
- Creator ~22 €/mois (100 000 caractères)
- Pro ~99 €/mois (500 000 caractères)
- Enterprise sur devis

**Cas d'usage dans nos modules**
- [CU-022 Voicebot accueil téléphonique IA](modules/cu-022-voicebot-accueil.html) — option qualité premium
- [CU-009 Content repurposing](modules/cu-009-content-repurposing.html) — synthèse audio multi-formats

**Alternatives**
- Cartesia (latence > qualité)
- Voxtral (souveraineté > tout)
- Deepgram Aura (alternative US plus orientée streaming)
- OpenAI TTS (basique mais accessible)

**Pour aller plus loin**
- [ElevenLabs — site officiel](https://elevenlabs.io/)
- [Documentation Conversational AI 2.0](https://elevenlabs.io/docs/conversational-ai)
- [Softcery — comparatif voicebot platforms 2026](https://softcery.com/lab/choosing-the-right-voice-agent-platform-in-2026)

---

### 7. Vapi.ai

- **Vendor** : Vapi
- **Catégorie** : Plateforme voicebot dev-first (full-stack)
- **Type** : SaaS
- **Souveraineté** : 🇺🇸
- **Maturité** : N4-N6 (production-ready, communauté active)
- **Coût** : 🟡 Freemium (~0,10-0,20 € par minute en variable)
- **Complexité** : 🛠️🛠️ Setup léger (1-2 semaines pour cas standard)

**Tagline**
Plateforme dev-first qui couvre l'intégralité du pipeline voicebot (téléphonie + STT + LLM + TTS + intégrations CRM/agenda). Agnostique sur les briques (compatible Twilio, Deepgram/Voxtral, Claude/GPT/Mistral, Cartesia/ElevenLabs). Devenue référence 2026 pour les déploiements PME rapides.

**Description**
Vapi a émergé en 2024 et s'est imposé en 2025-2026 comme la plateforme dev-first de référence pour les voicebots. La proposition de valeur : couvrir l'orchestration complète du pipeline voice (téléphonie, STT, LLM, TTS, intégrations) tout en restant agnostique sur les briques (tu choisis ta téléphonie, ton STT, ton LLM, ton TTS). Setup type : 1-2 semaines pour un voicebot PME standard, déploiement scalable.

**À quoi ça sert**
- Déploiement rapide de voicebots PME (médical, e-commerce, services)
- Prototype rapide d'agent vocal pour validation produit
- Orchestration end-to-end avec briques au choix
- Multi-canal voice : téléphonie, web call, mobile

**Quand l'utiliser**
- Time-to-value critique (lancement < 1 mois)
- Tu veux la flexibilité du choix des briques (Cartesia + Claude + Voxtral, par exemple)
- Volume PME-ETI (jusqu'à ~10 000 minutes/mois)

**Quand NE PAS l'utiliser**
- Souveraineté EU stricte sur l'orchestration (Vapi héberge aux US)
- Volume très massif (>100 000 min/mois) — préférer setup custom
- Cas très spécifiques nécessitant contrôle bas-niveau

**Stack & intégrations**
- Téléphonie : Twilio, Vonage, et plus
- STT : Deepgram, Whisper, AssemblyAI, Voxtral (en cours)
- LLM : OpenAI, Anthropic, Mistral, custom endpoints
- TTS : Cartesia, ElevenLabs, OpenAI, PlayHT
- CRM/agenda : HubSpot, Calendly, Cal.com, custom webhooks

**Modèle économique**
- Pay-as-you-go ~0,10-0,20 € par minute selon stack choisie
- Plan PME ~150-500 €/mois selon volume
- Plan enterprise sur devis

**Cas d'usage dans nos modules**
- [CU-022 Voicebot accueil téléphonique IA](modules/cu-022-voicebot-accueil.html) — recommandation principale pour PME

**Alternatives**
- Retell AI (concurrent direct, similaire)
- Bland AI (alternative US)
- Pipecat (open-source, plus DIY)
- Setup custom Twilio + STT + LLM + TTS (plus de contrôle, plus d'effort)

**Pour aller plus loin**
- [Vapi.ai — site officiel](https://vapi.ai/)
- [Documentation Vapi](https://docs.vapi.ai/)
- [Reddit r/vapi](https://www.reddit.com/r/vapi/)

---

## 🤖 Catégorie : Multi-agents & frameworks (3 nouvelles fiches)

### 8. Mistral Agents SDK

- **Vendor** : Mistral AI
- **Catégorie** : Agent SDK souverain (Vibe Cloud)
- **Type** : Open-source + cloud Mistral
- **Souveraineté** : 🇫🇷🇪🇺
- **Maturité** : N4-N6 (lancement 2026, communauté en croissance)
- **Coût** : 🟢 Gratuit (SDK) + 🟡 API Mistral
- **Complexité** : 🛠️🛠️🛠️ Intégration

**Tagline**
SDK agentique souverain de Mistral AI, alternative européenne à Claude Agent SDK et OpenAI Agents SDK. Couvre les patterns multi-agents avec mémoire partagée, tool-use, handoff inter-agents. Articulation native avec la stack Mistral (Mistral Large, Mistral Document AI, Voxtral).

**Description**
Mistral a publié en 2026 son SDK agentique propriétaire, intégré à sa plateforme Vibe Cloud. C'est la réponse souveraine européenne aux SDK Anthropic et OpenAI sortis fin 2025 - début 2026. Le SDK couvre les patterns canoniques : mémoire partagée, tool-use structuré, handoff explicites entre agents, observability native.

**À quoi ça sert**
- Construction d'agents codeurs ou métier souverains EU
- Workflows multi-agents pour structures avec exigences AI Act renforcées
- Cas d'usage sensibles où la stack 100 % EU est un critère

**Quand l'utiliser**
- Tu travailles sur des données sensibles (santé, finance, public, défense)
- Tu veux la cohérence Mistral end-to-end (LLM + agent + voice)
- Tu négocies un déploiement enterprise et la souveraineté EU est levier commercial

**Quand NE PAS l'utiliser**
- Tu as déjà investi sur LangGraph / CrewAI et l'effort de migration n'est pas justifié
- Tu as besoin de la communauté la plus large et la doc la plus mature (préférer LangGraph)

**Stack & intégrations**
- Hébergement : cloud Mistral (Vibe Cloud) ou auto-hébergé
- Compatible MCP (Model Context Protocol) pour interopérabilité
- SDK Python (et JavaScript en cours)

**Modèle économique**
- SDK open-source gratuit
- Coûts d'inférence sur API Mistral (tarif compétitif, ~$3-15 / 1M tokens selon modèle)

**Cas d'usage dans nos modules**
- [CU-014 Multi-agents par fonction métier](modules/cu-014-multi-agents.html) — option souveraine recommandée
- [CU-015 Stripe Minions / agents codeurs](modules/cu-015-stripe-minions.html) — alternative à Claude Agent SDK
- [CU-020 Conformité RGPD & AI Act](modules/cu-020-conformite-rgpd-ai-act.html) — pour structures avec exigences AI Act

**Alternatives**
- Claude Agent SDK (US, qualité référence)
- OpenAI Agents SDK (US, écosystème large)
- LangGraph (open-source, communauté la plus large)
- CrewAI (open-source, accessible)

**Pour aller plus loin**
- [Mistral Agents SDK — annonce](https://thenewstack.io/mistral-vibe-cloud-agents/)
- [Documentation Mistral Agents](https://docs.mistral.ai/agents)

---

### 9. Anthropic Computer Use

- **Vendor** : Anthropic
- **Catégorie** : Agent multimodal (interaction GUI)
- **Type** : SaaS (API Claude)
- **Souveraineté** : 🇺🇸
- **Maturité** : N4-N6 (production en 2026, beta solide depuis fin 2024)
- **Coût** : 🟠 Payant (tarification API Claude standard)
- **Complexité** : 🛠️🛠️🛠️ Intégration (sandbox sécurité requise)

**Tagline**
Capacité de Claude à interagir directement avec une interface graphique (cliquer, taper, naviguer) — l'évolution naturelle de la RPA traditionnelle vers une RPA pilotée par LLM, plus flexible et plus contextuelle. Production-grade en 2026, déjà déployé sur des cas concrets (administratif, support, automatisation desktop).

**Description**
Lancé par Anthropic en bêta fin 2024, **Claude Computer Use** permet à Claude d'interagir directement avec une interface graphique (capture d'écran → identification des éléments → action). Production-grade en 2026, c'est la version IA générative de la RPA traditionnelle — beaucoup plus flexible (pas besoin de scripter chaque interaction), avec une compréhension contextuelle. Cas d'usage prioritaires : automatisation tâches administratives répétitives, navigation web, scripting GUI.

**À quoi ça sert**
- Automatisation de tâches GUI répétitives (saisie de formulaires, extraction de données, navigation web)
- Remplacement progressif de la RPA traditionnelle (UiPath, Automation Anywhere)
- Workflows hybrides où certaines interactions ne sont accessibles que par GUI (sites legacy sans API)

**Quand l'utiliser**
- Tu as des tâches répétitives sur GUI sans API exposée
- Tu cherches un remplacement souple à la RPA classique
- Tu veux tester l'automatisation sur des process administratifs (saisie multi-systèmes)

**Quand NE PAS l'utiliser**
- Tâches critiques avec exigence de fiabilité 99.9 %+ (Computer Use est encore stochastique)
- Volume très élevé (le coût par action reste significatif)
- Données très sensibles sans sandbox sécurisé

**Stack & intégrations**
- API Anthropic Claude
- Nécessite un environnement sandbox (machine virtuelle dédiée, image Docker)
- Compatible avec MCP pour orchestration

**Modèle économique**
- Tarification API Claude standard (Sonnet ou Opus)
- Coût typique : $0,30-2 par tâche complète selon complexité

**Cas d'usage dans nos modules**
- [CU-014 Multi-agents par fonction métier](modules/cu-014-multi-agents.html) — agent administratif autonome
- [CU-015 Stripe Minions / agents codeurs](modules/cu-015-stripe-minions.html) — automation tâches développeur
- [CU-013 Workflow email-CRM](modules/cu-013-workflow-email-crm.html) — automatisation cas où API CRM absente

**Alternatives**
- UiPath / Automation Anywhere (RPA traditionnelle)
- Browser-use (open-source, agent Playwright)
- Adept ACT-1 (concurrent US)
- Manus AI (Chinois, alternatif)

**Pour aller plus loin**
- [Claude Computer Use — Anthropic](https://www.anthropic.com/news/computer-use)
- [Documentation officielle](https://docs.anthropic.com/en/docs/build-with-claude/computer-use)

---

### 10. MCP (Model Context Protocol)

- **Vendor** : Linux Foundation (donné par Anthropic en décembre 2025)
- **Catégorie** : Standard ouvert (protocole)
- **Type** : Standard ouvert
- **Souveraineté** : Standard mondial
- **Maturité** : N7-N8 (devenu standard de fait 2026)
- **Coût** : 🟢 Gratuit (standard ouvert)
- **Complexité** : 🛠️🛠️ Setup léger (intégration via SDKs existants)

**Tagline**
Standard ouvert pour connecter les agents IA aux outils et données. Devient « le USB-C des agents » en 2026 — Anthropic a donné le protocole à la Linux Foundation en décembre 2025, ce qui en fait un standard cross-vendor adopté par Claude, OpenAI, Mistral, et la plupart des frameworks agentiques.

**Description**
MCP est un protocole ouvert publié par Anthropic en 2024, donné à la Linux Foundation fin 2025. Il standardise la manière dont un agent IA appelle des outils externes (APIs, bases de données, applications) : un serveur MCP expose des « tools » (capabilities) que n'importe quel client MCP peut consommer. Adoption massive en 2026 : Anthropic, OpenAI, Mistral, mais aussi LangGraph, CrewAI, AutoGen et la plupart des frameworks intègrent désormais MCP nativement.

**À quoi ça sert**
- Connecter un agent IA à des outils externes sans réinventer le wheel à chaque fois
- Construire des serveurs MCP spécifiques (intégrations d'entreprise, ERP custom)
- Découpler l'agent du LLM sous-jacent (changement de modèle sans réécrire les intégrations)
- Mutualiser les connecteurs entre projets

**Quand l'utiliser**
- Tu construis un système agentique avec besoin d'intégrer plusieurs outils
- Tu veux la flexibilité de changer de LLM sans tout réécrire
- Tu participes à un écosystème (interopérabilité avec partenaires)

**Quand NE PAS l'utiliser**
- Cas ultra-simple avec 1 seul tool d'intégration (overkill)
- Tu as déjà un standard maison validé sur des dizaines d'intégrations existantes

**Stack & intégrations**
- SDK officiels : Python, TypeScript, Java, Kotlin
- Compatible Claude, OpenAI, Mistral, LangGraph, CrewAI, AutoGen
- Marketplace de serveurs MCP open-source (Filesystem, GitHub, Slack, Postgres, etc.)

**Modèle économique**
- Standard ouvert gratuit
- Coûts uniquement liés à ton infrastructure (serveurs MCP custom à héberger)

**Cas d'usage dans nos modules**
- [CU-014 Multi-agents par fonction métier](modules/cu-014-multi-agents.html) — standard d'intégration recommandé
- [CU-015 Stripe Minions / agents codeurs](modules/cu-015-stripe-minions.html) — connecteurs MCP pour outils dev
- [CU-013 Workflow email-CRM](modules/cu-013-workflow-email-crm.html) — serveur MCP pour CRM custom

**Alternatives**
- A2A (Agent2Agent Protocol — Google, complémentaire pour communication inter-agents)
- AGENTS.md (OpenAI, plus fin sur la spécification d'agent)
- Connecteurs custom (l'option historique, vouée à disparaître)

**Pour aller plus loin**
- [Model Context Protocol — site officiel](https://modelcontextprotocol.io/)
- [GitHub — implémentations officielles](https://github.com/modelcontextprotocol)
- [Linux Foundation MCP — annonce](https://www.linuxfoundation.org/press/mcp)

---

### 11. A2A (Agent2Agent Protocol)

- **Vendor** : Google (initialement)
- **Catégorie** : Standard inter-agents
- **Type** : Standard ouvert
- **Souveraineté** : 🇺🇸 (mais standard ouvert)
- **Maturité** : N7-N8 (en émergence 2026, complémentaire à MCP)
- **Coût** : 🟢 Gratuit (standard ouvert)
- **Complexité** : 🛠️🛠️🛠️ Intégration

**Tagline**
Standard ouvert pour la communication entre agents hétérogènes (de différents vendors / frameworks). Complémentaire à MCP : MCP standardise l'appel d'outils, A2A standardise la communication agent-agent. Émergeant en 2026 avec adoption croissante chez Google, mais aussi acceptation cross-vendor.

**Description**
A2A est un protocole publié par Google en 2025-2026, focalisé sur la communication entre agents IA hétérogènes — par exemple, un agent Claude qui doit collaborer avec un agent Mistral ou un agent custom. Là où MCP standardise l'appel d'outils, A2A standardise les échanges agent-agent (handoff, négociation, consensus). Encore jeune mais adoption croissante en 2026.

**À quoi ça sert**
- Faire collaborer des agents de vendors différents (multi-cloud, multi-LLM)
- Construire des écosystèmes agentiques distribués
- Préparer l'avenir où chaque organisation expose ses propres agents accessibles à des partenaires

**Quand l'utiliser**
- Tu construis un système multi-agents avec briques hétérogènes
- Tu veux préparer l'interopérabilité avec partenaires (B2B agentique)
- Tu travailles dans un écosystème complexe (places de marché, marketplaces de services)

**Quand NE PAS l'utiliser**
- Système monolithique avec 1 seul vendor (overkill)
- Cas d'usage où MCP suffit

**Stack & intégrations**
- SDK Google + open-source emerging
- Compatible avec MCP (les 2 standards se complètent)
- Adoption en cours sur LangGraph, CrewAI

**Modèle économique**
- Standard ouvert gratuit
- Coûts liés à infrastructure de communication

**Cas d'usage dans nos modules**
- [CU-014 Multi-agents par fonction métier](modules/cu-014-multi-agents.html) — pour les setups multi-vendor

**Alternatives**
- MCP (qui couvre une couche différente — appel d'outils vs communication agent-agent)
- Standards maison (à éviter, voués à disparaître)

**Pour aller plus loin**
- [A2A — annonce Google](https://blog.google/technology/ai/agent2agent-protocol)
- [Documentation A2A](https://a2a-protocol.org)

---

## 👁️ Catégorie : Vision foundation models (2 nouvelles fiches)

### 12. Florence-2

- **Vendor** : Microsoft
- **Catégorie** : Vision-language foundation model compact
- **Type** : Open-source (MIT)
- **Souveraineté** : 🇺🇸 (open-source mondial)
- **Maturité** : N4-N6 (production-ready 2025-2026)
- **Coût** : 🟢 Gratuit (auto-hébergé)
- **Complexité** : 🛠️🛠️🛠️ Intégration

**Tagline**
Vision-language foundation model compact (0,7B paramètres) qui unifie détection, segmentation, captioning et grounding en un seul modèle. Zero-shot sur les tâches courantes, fine-tunable rapidement sur datasets spécialisés. Rend la vision industrielle accessible aux PME sans équipe ML dédiée.

**Description**
Florence-2 est sorti par Microsoft Research en 2024, devenu standard de fait en 2025-2026 pour la vision unifiée. Modèle compact (0,7B paramètres en version base) qui regroupe en un seul réseau neuronal : détection d'objets, segmentation, captioning, grounding (relier texte et zones de l'image). Performant en zero-shot sur les tâches classiques, fine-tunable en quelques heures pour des cas spécialisés.

**À quoi ça sert**
- Vision industrielle (contrôle qualité, comptage, identification produits) sans équipe ML lourde
- Annotation automatique de datasets visuels
- Captioning et description d'images pour accessibilité ou indexation
- Pré-traitement avant fine-tuning sur cas custom

**Quand l'utiliser**
- PME / ETI industrielles avec besoins vision sans data scientist dédié
- Cas d'usage où la combinaison détection + segmentation + caption est utile
- Edge computing (modèle compact → déployable sur Jetson, edge devices)

**Quand NE PAS l'utiliser**
- Performance frontière sur tâches très spécialisées (préférer modèles dédiés type YOLO + Mask R-CNN spécialisés)
- Cas avec datasets très grands où un modèle plus gros ferait mieux

**Stack & intégrations**
- Hugging Face Transformers
- Compatible PyTorch, ONNX
- Déploiement edge possible (NVIDIA Jetson, ARM)

**Modèle économique**
- Open-source MIT — usage commercial autorisé sans royalty
- Coûts uniquement infra (GPU pour training/inférence)

**Cas d'usage dans nos modules**
- [CU-017 Contrôle qualité par vision IA](modules/cu-017-controle-qualite-vision.html) — option compact pour PME
- [CU-018 Optimisation production / nesting](modules/cu-018-optimisation-production.html) — caractérisation matière

**Alternatives**
- DINOv2 (Meta, self-supervised, plus généraliste)
- SAM 2 (Meta, segmentation dédiée)
- YOLO 11+ (détection dédiée)
- CLIP / OpenCLIP (vision-language sans détection structurée)

**Pour aller plus loin**
- [Florence-2 — Hugging Face](https://huggingface.co/microsoft/Florence-2-base)
- [Roboflow Blog — Florence-2 deep dive](https://blog.roboflow.com/florence-2/)
- [GitHub Microsoft Florence](https://github.com/microsoft/Florence-2)

---

### 13. SAM 2 (Segment Anything 2)

- **Vendor** : Meta AI
- **Catégorie** : Segmentation universelle (image + vidéo)
- **Type** : Open-source
- **Souveraineté** : 🇺🇸 (open-source mondial)
- **Maturité** : N4-N6 (production-ready)
- **Coût** : 🟢 Gratuit (auto-hébergé)
- **Complexité** : 🛠️🛠️🛠️ Intégration

**Tagline**
Modèle de segmentation universelle de Meta — étend SAM 1 (image) à la vidéo. Zero-shot sur quasiment tous les objets, segmentation pixel-perfect en temps réel. Standard de fait 2026 pour les cas d'usage industriels et créatifs nécessitant une segmentation fine.

**Description**
SAM 2 est la suite de Segment Anything (SAM 1, 2023), publié par Meta en 2024. La V2 ajoute la dimension temporelle — segmentation vidéo cohérente frame par frame. Zero-shot sur quasiment tous les objets (pas besoin de fine-tuning pour la majorité des cas), segmentation pixel-perfect, temps réel sur GPU moderne. Standard de fait 2026 pour annotation de datasets, contrôle qualité industrielle, traitement vidéo.

**À quoi ça sert**
- Contrôle qualité industriel par segmentation (défauts, bavures, contaminations)
- Annotation automatique de datasets pour fine-tuning de modèles spécialisés
- Traitement vidéo (suivi d'objets, segmentation temps réel)
- Vision robotique (segmentation des éléments à manipuler)

**Quand l'utiliser**
- Cas industriel avec besoin de segmentation pixel-perfect
- Annotation rapide de larges datasets visuels
- Traitement vidéo en temps réel

**Quand NE PAS l'utiliser**
- Cas où la classification suffit (pas besoin de segmentation pixel)
- Edge computing très contraint (modèle plus gros que Florence-2)

**Stack & intégrations**
- PyTorch, ONNX
- Intégration Roboflow, CVAT pour annotation
- Compatible Florence-2 en pipeline (Florence-2 détection + SAM 2 segmentation)

**Modèle économique**
- Open-source (Apache 2.0) — usage commercial autorisé
- Coûts uniquement infra (GPU pour training/inférence)

**Cas d'usage dans nos modules**
- [CU-017 Contrôle qualité par vision IA](modules/cu-017-controle-qualite-vision.html) — segmentation défauts pixel-perfect
- [CU-018 Optimisation production / nesting](modules/cu-018-optimisation-production.html) — caractérisation matière fine

**Alternatives**
- Mask R-CNN (segmentation classique)
- Florence-2 (vision unifiée mais segmentation moins fine)
- YOLOv11-seg (détection + segmentation rapide)

**Pour aller plus loin**
- [SAM 2 — site officiel Meta](https://ai.meta.com/sam2/)
- [GitHub Meta SAM 2](https://github.com/facebookresearch/sam2)
- [Roboflow — SAM 2 démos](https://blog.roboflow.com/sam-2/)

---

## Récapitulatif de l'intégration

### 13 fiches livrées

| # | Outil | Catégorie | Souveraineté | Coût |
|---|---|---|---|---|
| 1 | Lucie / OpenLLM-France | LLM | 🇫🇷🇪🇺 | 🟢 |
| 2 | Pleias-RAG | LLM (SLM RAG) | 🇫🇷🇪🇺 | 🟢/🟡 |
| 3 | LightOn (Paradigm) | LLM enterprise | 🇫🇷🇪🇺 | 🔴 |
| 4 | Voxtral | Voice (STT + TTS) | 🇫🇷🇪🇺 | 🟡 |
| 5 | Cartesia (Sonic / Line) | Voice (TTS premium) | 🇺🇸 | 🟡 |
| 6 | ElevenLabs Conv 2.0 | Voice (TTS premium) | 🇺🇸 | 🟡/🟠 |
| 7 | Vapi.ai | Voice (plateforme) | 🇺🇸 | 🟡 |
| 8 | Mistral Agents SDK | Multi-agents | 🇫🇷🇪🇺 | 🟢/🟡 |
| 9 | Anthropic Computer Use | Agent multimodal | 🇺🇸 | 🟠 |
| 10 | MCP | Standard | Standard mondial | 🟢 |
| 11 | A2A | Standard | 🇺🇸 (ouvert) | 🟢 |
| 12 | Florence-2 | Vision (foundation) | 🇺🇸 (open-source) | 🟢 |
| 13 | SAM 2 | Vision (segmentation) | 🇺🇸 (open-source) | 🟢 |

### Renforcement souveraineté EU/FR

**6 nouvelles fiches 🇫🇷🇪🇺** (Lucie, Pleias-RAG, LightOn, Voxtral, Mistral Agents) — passe le total souverains à **18 fiches** dans la page Ressources (vs 12 en v3.2).

### Nouvelle catégorie à créer

**Catégorie 17 — 🎙️ Voice & speech** (entre `📨 Email & scraping` et `👁️ Vision industrielle` dans le sommaire). Contiendra : Voxtral, Cartesia, ElevenLabs Conv 2.0, Vapi.ai (4 outils minimum, + extension future possible avec Deepgram, AssemblyAI, etc.).

### Modules existants à mettre à jour avec liens vers ces nouvelles fiches

- **CU-008 Knowledge base RAG** : ajouter liens vers Lucie, Pleias-RAG (RAG souverain)
- **CU-014 Multi-agents par fonction métier** : ajouter liens vers Mistral Agents, Computer Use, MCP, A2A
- **CU-015 Stripe Minions / agents codeurs** : ajouter liens vers Mistral Agents, Computer Use, MCP
- **CU-017 Contrôle qualité par vision IA** : ajouter liens vers Florence-2, SAM 2
- **CU-018 Optimisation production / nesting** : ajouter liens vers Florence-2, SAM 2
- **CU-020 Conformité RGPD & AI Act** : ajouter liens vers Lucie, Pleias-RAG, LightOn (déjà présents en placeholders dans le HTML livré)
- **CU-022 Voicebot accueil** : ajouter liens vers Voxtral, Cartesia, ElevenLabs, Vapi (déjà présents en placeholders)
- **CU-021 Finance augmentée** : ajouter lien vers Mistral si pas déjà fait

### Métadonnées à ajouter aux 13 fiches

Pour chaque fiche, Claude Code doit appliquer les **6 dimensions de badges** harmonisées avec la patch v3.2 :
1. **Type** (SaaS / Open-source / Open-weight / Hybride / Standard)
2. **Catégorie d'usage** (LLM / Voice / Agents / Vision / etc.)
3. **Maturité** (N1-N3 / N4-N6 / N7-N8)
4. **Souveraineté** (🇪🇺 si applicable)
5. **Coût d'entrée** (🟢 Gratuit / 🟡 Freemium / 🟠 Payant / 🔴 Entreprise)
6. **Complexité de mise en œuvre** (🛠️ Plug-and-play / 🛠️🛠️ Setup léger / 🛠️🛠️🛠️ Intégration / 🛠️🛠️🛠️🛠️ Projet)

Les badges sont déjà mentionnés en début de chaque fiche dans ce document.

---

*Matière éditoriale produite le 8 mai 2026 par Cowork. Sources principales : veille pré-itération mai 2026, debrief Claude Code post-v3.1, recherche Web ciblée sur les outils émergents.*
