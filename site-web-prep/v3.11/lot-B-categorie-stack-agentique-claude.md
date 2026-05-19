# Lot B v3.11 — Catégorie ressources « Stack agentique Claude/Anthropic » (option resserrée + fusion Lot C)

**Brief consolidé pour Claude Code** : création d'une **nouvelle catégorie** dans `ressources.html` regroupant 10 fiches outils (9 nouvelles ou officialisées + 1 actualisation) structurées en **3 sous-catégories**. Catégorie labellisée explicitement « niveau prestataire / expert » pour ne pas perdre le lecteur dirigeant non-IT.

**Sources** : runs veille 12-19 mai 2026 (Grok screeners 1, 2, 3, 6) + analyse intuition Blaise validée sur l'écosystème Claude/Anthropic + recoupement avec modules existants (CU-027, DEP-08, DEP-05).

**Fusion Lot C** : la piste Onyx (reportée v3.10) et l'actualisation Hermes Agent (reportée v3.10) sont absorbées dans le Lot B — pas de Lot C séparé v3.11.

**Décision validée** : option resserrée (10 fiches) plutôt qu'option élargie (15+). LangSmith / Phoenix / Langfuse / BMad Method / Lyra-Dev restent en surveillance jusqu'à recroisement seconde source.

---

## Architecture de la nouvelle catégorie

**Position dans `ressources.html`** : nouvelle catégorie distincte, à insérer après les catégories existantes (Modèles LLM, RAG, Agents IA, Knowledge management, etc.).

**Nom de la catégorie** : « **Stack agentique Claude / Anthropic** »

**Label explicite à intégrer en intro de catégorie** :

> 🛠️ **Cette catégorie regroupe les briques de l'écosystème agentique Claude/Anthropic — niveau prestataire / expert.**
>
> Ces outils sont conçus pour des développeurs senior ou des prestataires IA-natifs qui pilotent des projets PME. Si vous êtes un dirigeant non-IT, **vous n'avez pas à choisir ces outils vous-même** — vous devez vérifier que votre prestataire les maîtrise (cf. questions à poser à votre prestataire, [CU-027 §1bis](modules/cu-027-dev-applicatif-ia.html#section-1bis)).
>
> L'écosystème agentique Claude/Anthropic a en 2026 une **avance structurelle** sur les écosystèmes concurrents : MCP standard adopté par OpenAI / GitHub / Microsoft / Cursor, Agent Skills comme pattern structurel, ECC stack open-source qui rassemble une communauté active. Cette catégorie cartographie les briques principales.

---

## Sous-catégorie 1 — Frameworks ECC & écosystème Anthropic (7 fiches)

### Fiche 1 — Everything Claude Code (ECC)

**Anchor id** : `everything-claude-code`
**Catégorie principale** : Stack agentique Claude/Anthropic > Frameworks ECC
**Description courte** : Méta-framework open-source qui rassemble 38 agents spécialisés + 156 skills réutilisables + 72 commandes slash + AgentShield (audit sécurité gratuit). Standard de fait pour piloter un projet de dev applicatif IA-assisté en 2026.
**URL officielle** : github.com/affaan-m/everything-claude-code
**Mainteneur** : @affaan-m (Affaan Mustafa)
**Licence** : open-source
**Coût** : gratuit + abonnement Claude Pro (~20 $/mois) recommandé
**Souveraineté** : local-first, peut tourner on-premise
**Cas d'usage PME** : remplacer une équipe de 3-4 dev juniors (~8-10 K$/mois) par 1 dev senior + ECC stack pour un projet de dev applicatif IA-assisté
**Cross-link Hub** : déjà cité dans **CU-027 §1bis** (état de l'art 2026) et **DEP-08 §3** (AgentShield)

### Fiche 2 — AgentShield

**Anchor id** : `agentshield`
**Catégorie principale** : Stack agentique Claude/Anthropic > Frameworks ECC
**Description courte** : Audit sécurité automatique gratuit pour configurations agents IA. Composant d'ECC. **1 282 tests automatiques, 102 règles de sécurité**. Mode `--opus` lance un pipeline 3 agents Claude Opus en red-team / blue-team / auditor.
**URL officielle** : github.com/affaan-m/everything-claude-code (composant d'ECC)
**Commande d'exécution** : `npx ecc-agentshield scan`
**Coût** : gratuit
**Cas d'usage PME** : à lancer **avant tout déploiement production** d'un agent qui utilise des MCP servers tiers. Détecte hardcoded API keys, configs surdimensionnées, MCP servers à risque CVE connues, patterns d'injection.
**Cross-link Hub** : **DEP-08 §3.2 et §3.3** (déjà documenté en détail)

### Fiche 3 — Claude Code (officiel Anthropic)

**Anchor id** : `claude-code`
**Catégorie principale** : Stack agentique Claude/Anthropic > Frameworks ECC
**Description courte** : CLI agentique officiel d'Anthropic pour le coding. Référence du marché en 2026. Support natif MCP, hooks personnalisables, Agent Skills.
**URL officielle** : github.com/anthropics/claude-code + claude.ai/code
**Mainteneur** : Anthropic
**Licence** : propriétaire (CLI gratuit, modèle Claude facturé à l'usage)
**Coût** : ~20 $/mois (Claude Pro) à plusieurs centaines/mois selon volume API
**Souveraineté** : CLI local, mais inférence chez Anthropic (cf. **DEP-06** pour arbitrage SaaS vs self-hosted)
**Cas d'usage PME** : CLI de base pour tout projet de dev IA-assisté sérieux en 2026. À utiliser via un prestataire qui maîtrise l'écosystème ECC en surplomb.
**Note CVE** : **CVE-2025-59536** (CVSS 8.7) corrigée — RCE via MCP servers manipulés. Toujours auditer les MCP tiers avant intégration (cf. **DEP-08 §3.1**).
**Cross-link Hub** : **CU-027 §1.1**, **DEP-08 §1.3**, **DEP-05 §8.3** (Code Execution with MCP)

### Fiche 4 — Cursor

**Anchor id** : `cursor`
**Catégorie principale** : Stack agentique Claude/Anthropic > Frameworks ECC
**Description courte** : IDE IA fork de VS Code. Production-ready en 2026 selon le benchmark Aqua Voice / DEV.to (7,5/10 production-ready).
**URL officielle** : cursor.com
**Coût** : freemium puis ~20 $/mois Pro, abonnements équipe au-delà
**Souveraineté** : IDE local, inférence chez Cursor (privacy mode disponible)
**Cas d'usage PME** : IDE de référence pour dev senior interne ou prestataire IA-natif. Alternative à VS Code + extensions.
**Cross-link Hub** : **CU-027 §1.1** (tableau outils)

### Fiche 5 — Windsurf

**Anchor id** : `windsurf`
**Catégorie principale** : Stack agentique Claude/Anthropic > Frameworks ECC
**Description courte** : IDE agentique production-ready avec tests intégrés. Top du benchmark Aqua Voice / DEV.to (**8,5/10 production-ready** — devant Cursor 7,5 et Replit 7).
**URL officielle** : codeium.com/windsurf
**Coût** : freemium puis abonnement Pro
**Cas d'usage PME** : IDE recommandé pour code « shippable » avec tests intégrés. Alternative à Cursor pour les équipes qui privilégient l'autonomie agent.
**Cross-link Hub** : **CU-027 §1.1**

### Fiche 6 — agentmemory ⭐ nouveau v3.11

**Anchor id** : `agentmemory`
**Catégorie principale** : Stack agentique Claude/Anthropic > Frameworks ECC
**Description courte** : Couche de **persistent memory mutualisable cross-agents** (Claude Code, Hermes Agent, OpenClaw, Codex CLI, Cursor, Gemini CLI). Serveur **local SQLite + FAISS**. Premier projet à fournir une implémentation production-ready du pattern persistent memory.
**URL officielle** : github.com/rohitg00/agentmemory
**Mainteneur** : @ghumare64 (Rohit Ghumare)
**Stars GitHub** : **13 200+** (mai 2026, croissance rapide)
**Licence** : open-source
**Coût** : gratuit
**Souveraineté** : 100 % local-first (SQLite + FAISS), aucune dépendance SaaS — compatible architectures A3/A4 souveraineté
**Benchmarks publiés** : **95,2 % r@5 (recall at 5) vs 86,2 % BM25 fallback** + **coût token ÷ 100+ vs full context injection**
**Cas d'usage PME** : transforme un coding agent ponctuel en système qui « se souvient » du codebase, des décisions passées, des corrections d'erreur. Pertinent pour PME utilisant Claude Code / Cursor de manière régulière sur un même projet.
**Cross-link Hub** : **CU-008 §llm-wiki-shelf-life** (v3.11 Lot D enrichi) et **DEP-02 §section-2bis** (v3.11 Lot D enrichi). Implémentation concrète du pattern « persistent memory > RAG stateless » documenté dans ces 2 modules.

### Fiche 7 — claude-smart ⭐ nouveau v3.11

**Anchor id** : `claude-smart`
**Catégorie principale** : Stack agentique Claude/Anthropic > Frameworks ECC
**Description courte** : Plugin self-improving open-source pour Claude Code. **Analyse chaque session, extrait les leçons des échecs/corrections et crée automatiquement des Agent Skills réutilisables.** Réduit les boucles de planning et la consommation de tokens de **70 %+**.
**URL officielle** : github.com/ReflexioAI/claude-smart
**Mainteneur** : Yi Lu (Tech Lead Meta AI, ReflexioAI)
**Date de lancement** : 18 mai 2026 (récent — laisser mûrir avant adoption critique)
**Licence** : open-source
**Coût** : gratuit
**Souveraineté** : local-first, dashboard de review en local
**Cas d'usage PME** : pour les équipes qui utilisent Claude Code intensivement et veulent automatiser la capitalisation des apprentissages. Cohérent avec le pattern Anthropic Agent Skills (cf. **DEP-05 §8.4**) — c'est l'**automatisation de la création de skills**.
**Note de maturité** : dépôt récent (mai 2026), croissance initiale forte via relais Meta AI mais à surveiller sur 2-3 mois avant adoption production critique.
**Cross-link Hub** : **DEP-05 §8.4** (Agent Skills v3.9), **CU-008 §llm-wiki-shelf-life** (Lot D v3.11)

---

## Sous-catégorie 2 — MCP servers & orchestrateurs (2 fiches)

### Fiche 8 — Onyx ⭐ nouveau v3.11

**Anchor id** : `onyx`
**Catégorie principale** : Stack agentique Claude/Anthropic > MCP servers & orchestrateurs
**Description courte** : Plateforme open-source self-hostable RAG + agents + MCP. **40+ connectors natifs** vers les principales sources de données entreprise. Présentée par certains builders comme une alternative open-source à des suites SaaS d'agents.
**URL officielle** : github.com/onyx-dot-app/onyx
**Stars GitHub** : **18 000+** (mai 2026)
**Licence** : open-source
**Coût** : gratuit (self-hosting) + coûts infra
**Souveraineté** : self-hostable on-premise — pertinent pour PME RGPD-sensibles ou avec secrets industriels
**Cas d'usage PME** : PME souhaitant garder la maîtrise de ses données (RGPD, secrets industriels) tout en disposant d'une plateforme agentique complète. Alternative aux suites SaaS propriétaires.
**Note de maturité** : 18k stars, communauté active. Recroisement seconde source institutionnelle en cours mais fichage validé en v3.11 sur la base de la viralité GitHub + cohérence pédagogique avec la trajectoire souveraineté Hub.
**Cross-link Hub** : **DEP-02** (RAG en production), **DEP-08** (sécurité agents et MCP), **architectures.html** (pattern A3 souveraineté contrôlée)

### Fiche 9 — MCP STDIO standard (concept)

**Anchor id** : `mcp`
**Catégorie principale** : Stack agentique Claude/Anthropic > MCP servers & orchestrateurs
**Description courte** : **Model Context Protocol** — standard ouvert introduit fin 2024 par Anthropic, adopté en 2025-2026 par OpenAI, GitHub, Microsoft, Cursor. Permet à un agent IA de connecter de manière standardisée à des outils, des sources de données et des actions externes.
**URL officielle** : modelcontextprotocol.io + github.com/modelcontextprotocol
**Mainteneur** : Anthropic + écosystème ouvert
**Licence** : open standard (spec publique)
**Coût** : gratuit (spec ouverte)
**Cas d'usage PME** : standard de fait pour intégrer un agent IA à un écosystème d'outils (CRM, ERP, fichiers, APIs). Permet d'éviter le verrouillage propriétaire.
**Vulnérabilité connue** : **MCP STDIO vulnerability** (avril 2026) a affecté > 7 000 serveurs et > 150 M téléchargements. Audit AgentShield obligatoire avant intégration de tout MCP server tiers.
**Cross-link Hub** : **DEP-08 §1.2** (vecteurs d'attaque), **DEP-08 §3** (audit MCP), **DEP-05 §8.3** (Code Execution with MCP)

---

## Sous-catégorie 3 — Actualisation fiche existante (1 fiche)

### Fiche 10 — Hermes Agent (actualisation majeure)

**Anchor id** : `hermes-agent` (existant)
**Catégorie principale** : reclassement dans Stack agentique Claude/Anthropic > MCP servers & orchestrateurs (cohérence narrative — la fiche existante était dans Agents IA / frameworks multi-agents en v3.8, à déplacer ou à dupliquer)

**Actualisations à apporter** (cf. piste reportée v3.10) :
- **Codex est désormais runtime officiel pour les outils core** (activable par simple switch — cf. relais X ~2300 likes mai 2026)
- **Nouvelle vague d'intégrations MCP** : Obsidian / Reddit / GitHub / Stripe (mai 2026 — cohérence avec la tendance « MCP & memory layers comme nouveau standard agentique »)
- **Cohérence renforcée avec agentmemory** : Hermes Agent fait partie des coding agents supportés par les hooks agentmemory (cf. Fiche 6) — pattern persistent memory partagé

**Cross-link Hub** : **CU-008 §llm-wiki-shelf-life** (Lot D v3.11), **DEP-05 §8.4** (Agent Skills v3.9), **CU-014** (Multi-agents)

---

## Mise à jour RULES / glossaire chiffres-clés

Le **glossaire des chiffres-clés** RULES § 1.2.3 doit être actualisé :
- Nombre de fiches outils : **99 → ~107** (9 nouvelles fiches + 1 actualisation ne compte pas)
  - +7 fiches sous-catégorie ECC : ECC, AgentShield, Claude Code, Cursor, Windsurf, agentmemory, claude-smart
  - +2 fiches sous-catégorie MCP : Onyx, MCP STDIO
  - Hermes Agent = actualisation, pas nouvelle fiche
- Si certaines fiches existent déjà sous d'autres catégories (Claude Code, Cursor, Windsurf, Hermes Agent peuvent déjà être dans une catégorie « IDE et outils dev IA » ou « Agents IA »), trois options :
  1. **Déplacer** vers la nouvelle catégorie Stack agentique Claude/Anthropic (perte de visibilité ailleurs)
  2. **Dupliquer** dans la nouvelle catégorie (le compte de fiches reste cohérent — chaque fiche n'est comptée qu'une fois dans le glossaire RULES)
  3. **Conserver dans l'existant + lien transversal** depuis la nouvelle catégorie

**Mon arbitrage recommandé** : option 3 — conserver les fiches Claude Code, Cursor, Windsurf, Hermes Agent dans leur catégorie d'origine, et **ajouter des liens transversaux explicites** depuis la nouvelle catégorie Stack agentique Claude/Anthropic. Cela préserve la cohérence numérique RULES et évite la duplication tout en mettant en avant la cartographie.

Avec l'option 3 : nombre réel de NOUVELLES fiches créées = **5** (ECC + AgentShield + agentmemory + claude-smart + Onyx + MCP STDIO selon dédoublonnage)
→ Nombre de fiches outils : **99 → 104 ou 105**

À arbitrer par Claude Code lors de l'implémentation HTML selon l'état actuel de `ressources.html`.

## Lieux à mettre à jour pour la cohérence numérique (rule 1.2.x)

- `index.html` : meta + hero stats + filter count + section À propos → mention « ~107 fiches outils » (selon arbitrage)
- `ressources.html` : badge V·outils·catégories, accroche synthèse, exec-stats, intitulés des sections
- `README.md` : mention « ~107 fiches outils »
- `architectures.html` : badges éventuels
- Méta-descriptions de toutes les pages mentionnant le compte de fiches
- Lieux où la liste des catégories ressources apparaît (mention de la nouvelle catégorie « Stack agentique Claude/Anthropic »)

## Mise à jour RULES § 1.2.3

Entrée historique à ajouter :

```markdown
- **v1.6.2** — itération v3.11 (page ressources écosystème Claude + chiffres macro Stanford/McKinsey) :
  - Glossaire § 1.2.3 : 99 → ~105 fiches outils (5-7 nouvelles fiches selon dédoublonnage)
  - Nouvelle catégorie « Stack agentique Claude / Anthropic » dans ressources.html
  - Aucune nouvelle règle structurelle. RULES reste à 1.6.X.
```

## Item parallèle (à compiler dans brief v3.11)

Pas de canonisation chiffre macro spécifique au Lot B (les chiffres des fiches outils — 13 200 stars, 95,2 % r@5, 1 282 tests AgentShield, etc. — sont **locaux aux fiches**, pas réutilisables cross-modules comme chiffres macro IA). Le Lot A v3.11 (chiffres Stanford + McKinsey) reste la seule source d'I-D-007.

## Cohérence narrative finale du Lot B

La nouvelle catégorie répond à l'**intuition Blaise validée** : l'écosystème agentique Claude/Anthropic a aujourd'hui une avance structurelle qui mérite d'être cartographiée. Plutôt que de créer un nouveau module CU pédagogique (qui demanderait une production lourde et alourdirait le compteur CU), on opte pour une **cartographie ressources** clairement labellisée niveau prestataire/expert.

Si cette cartographie révèle dans les 3 mois post-publication un **besoin pédagogique fort** (questions visiteurs récurrentes, feedback prestataires), création éventuelle d'un **CU-029 « L'écosystème agentique Claude/Anthropic 2026 »** en v3.12 ou v3.13. Pour l'instant, la cartographie ressources suffit.
