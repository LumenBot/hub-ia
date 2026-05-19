# Lot D v3.10 — Sécurité agentique (DEP-08 + PR-05)

**Brief consolidé pour Claude Code** : 2 patches sécurité convergents sur le bloc agentique 2026. DEP-08 reçoit une nouvelle section dédiée SBOM IA (cadre international ANSSI/G7). PR-05 reçoit 2 encarts — McKinsey Securing Agentic Enterprise + signalement NIST CAISI.

**Sources** : run veille 18 mai 2026 (3e passage Grok 4 réglementaire) + 13 mai (McKinsey, NIST CAISI).

**Cohérence narrative** : 2026 = année de convergence internationale sur la **traçabilité et la sécurisation des composants IA**. NIST (US) + ANSSI/G7 + Commission EU (AI Act) + McKinsey (industrie) pointent vers le même cadre.

---

## Patch D.1 — DEP-08 (Sécurité agents et MCP servers) — nouvelle section SBOM IA

**Module cible** : `deploiement/dep-08-securite-agents-mcp.html`
**Position** : insérer en **nouvelle section 7bis** entre la section 7 (« Conformité à anticiper ») et `#ressources`.
**Anchor id** : `section-7bis`
**Icône TOC** : 📦
**Label TOC** : « SBOM IA & supply chain »

### Contenu à intégrer

#### Intro de section

> **SBOM for AI** : la **Software Bill of Materials** appliquée aux systèmes IA — un cadre de traçabilité qui devient standard international en 2026.

Le groupe de travail cybersécurité du **G7** a publié en mai 2026 un document de référence : **« Software Bill of Materials (SBOM) for Artificial Intelligence »**. Relayé par l'**ANSSI le 13 mai 2026**. Cadre **non contraignant** mais **aligné NIS2** et futures exigences européennes. À surveiller : la convergence avec le NIST AI Agent Standards Initiative (CAISI) signalé en PR-05.

#### Qu'est-ce qu'un SBOM IA ?

Un SBOM IA est un **inventaire structuré** des composants qui constituent un système IA :

| Composant | Exemples | Pourquoi le tracer |
|---|---|---|
| **Modèles IA** | GPT-4, Claude Opus, Mistral Large, Llama 3 fine-tuné | Vulnérabilités modèle, mise à jour fournisseur |
| **Datasets** | Données d'entraînement, données de fine-tuning, RAG corpus | Conformité RGPD, biais documentés |
| **Fournisseurs** | OpenAI, Anthropic, Mistral, fournisseurs cloud | Risque concentration, défaillance fournisseur |
| **Dépendances logicielles** | LangChain, vector DBs, MCP servers tiers | CVE applicables, supply chain attack |
| **Configuration agents** | Skills, hooks, prompts système, CLAUDE.md | Compromission supply chain, audit trail |

#### Pourquoi c'est important pour une PME en 2026

Trois raisons opérationnelles :

1. **Convergence réglementaire imminente** : NIS2 + AI Act + initiatives NIST → la documentation des composants IA devient un attendu (pas encore une obligation, mais le sera dans 12-24 mois).
2. **Gestion des incidents de production** : sans SBOM, en cas d'incident agent, le délai de diagnostic explose. Avec SBOM, on identifie immédiatement quel modèle / dataset / MCP est impliqué.
3. **Sécurisation supply chain** : 2025-2026 a vu **341 skills malveillants détectés sur OpenClaw Marketplace** (12 %), **MCP STDIO vulnerability** sur 7 000+ serveurs. Le SBOM permet de réagir vite face à ces alertes (« est-ce que je suis exposé ? »).

#### Comment commencer en pratique

**Approche minimaliste (PME découverte)** :
- Documenter dans un simple tableau Excel : liste des modèles IA utilisés + fournisseurs + cas d'usage + données traitées
- Mettre à jour à chaque évolution stack (trimestriel max)
- Stockage simple, partagé entre DSI/RSSI/responsable IA

**Approche structurée (PME en industrialisation)** :
- Outils : SPDX (format standard) + outils de génération automatique de SBOM
- Intégration CI/CD pour automatiser la mise à jour
- Couplage avec la chaîne d'observabilité agent (cf. DEP-05)

**Approche conforme (PME secteur réglementé)** :
- Format SBOM aligné aux recommandations G7/ANSSI
- Audit annuel + procédure de réponse incident liée au SBOM
- Cohérence avec NIS2 et préparation aux futures exigences AI Act

#### Lien avec les autres dimensions sécurité du Hub

- **Section 2 (5 défenses prompt injection)** : le SBOM aide à identifier rapidement quels composants sont impactés par une CVE de modèle ou de MCP.
- **Section 3 (AgentShield)** : AgentShield scanne la configuration agent ; le SBOM documente cette configuration et son évolution.
- **Section 4 (Sécuriser CLAUDE.md)** : le SBOM intègre les CLAUDE.md versionnés comme composant traçable.
- **CU-020 (Conformité)** : volet conformité — le SBOM IA est une brique opérationnelle pour démontrer une diligence raisonnable.
- **PR-05 (Sécurité IA)** : volet stratégique — l'encart D.2 ci-dessous renvoie vers cette section.

### Sources à ajouter (sous-rubrique 📰 Articles de fond)

- **ANSSI / G7** — Software Bill of Materials (SBOM) for Artificial Intelligence (cyber.gouv.fr/nous-connaitre/publications/publications-internationales/software-bill-of-materials-sbom-for-artificial-intelligence/, 13 mai 2026)
- **ANSSI Twitter** — Annonce relais (x.com/ANSSI_FR/status/2054525097969344862)

### Mise à jour TOC

```html
<li><a href="#section-7bis"><span class="toc-icon">📦</span>SBOM IA & supply chain</a></li>
```

### Renvois croisés

- En executive summary de DEP-08 : nouveau takeaway « SBOM IA — l'inventaire des composants devient un standard international en 2026 (ANSSI/G7) »
- Cross-link réciproque depuis PR-05 (Patch D.2) vers DEP-08 §7bis

### Métadonnées module

- `<meta name="description">` : aucune modification majeure.
- Badge temps de lecture : passer à **+4 min**.

---

## Patch D.2 — PR-05 (Sécurité IA) — encarts McKinsey + NIST CAISI

**Module cible** : `prealables/pr-05-securite-ia.html`
**Position** : 2 encarts à intégrer — l'un dans la section 3 « Typologie des risques », l'autre en nouvelle sous-section dans la section 1 ou en section 4.

### Encart D.2.a — Cybersécurité agentique ≠ LLM classique (McKinsey)

**Position** : sous-section ou encart dans la section 3 « Typologie des risques »
**Anchor id** suggéré : `risques-agentiques`

#### Contenu à intégrer

> **2026 : la cybersécurité agentique devient un vecteur de risque distinct du LLM classique.**

Citation de référence (McKinsey « Securing the agentic enterprise », mai 2026) à transposer textuellement :

> *« Les organisations ne peuvent plus se contenter de craindre que l'IA dise la mauvaise chose, elles doivent contendre avec des systèmes qui font la mauvaise chose : actions non intentionnelles, mésusage d'outils, contournement de garde-fous. »*

**Implications pour la PME** :

- **Risque LLM classique** : hallucination, biais, fuite de données via prompt → relativement bien couvert par la stack 2025 (filtrage, sandbox)
- **Risque agentique 2026** : un agent peut **agir** sur un système (envoi de mail, modification fichier, transfert d'argent, accès API). Le risque devient celui de **l'action incorrecte**, pas seulement de l'output incorrect.

**Chiffres McKinsey à intégrer** :

- **RAI maturité moyenne 2026 : 2,3/5** (vs 2,0 en 2025) — progression mesurable mais lente
- **~1/3 des organisations à maturité ≥ 3** en stratégie, gouvernance et gouvernance agentique — donc 2/3 des organisations restent à risque

**Action attendue pour la PME** : si l'entreprise déploie un agent IA en production avec accès à des systèmes opérationnels (CRM, ERP, mail), elle doit appliquer **les patterns de DEP-05 §8 (v3.9 — production-grade) + §8.5 (failure receipt, Lot E v3.10)** et inscrire le projet à un **niveau de gouvernance ≥ 3** (auto-diag CU-026).

### Encart D.2.b — NIST CAISI : cadre US complémentaire AI Act

**Position** : encart en section 4 « Classification & checklist » ou nouvelle sous-section
**Anchor id** suggéré : `nist-caisi`

#### Contenu à intégrer

> 🔄 **NIST AI Agent Standards Initiative (CAISI)** — un cadre US complémentaire de l'AI Act EU à anticiper pour 2026-2027.

**Lancement** : février 2026, via le Center for AI Standards and Innovation (NIST)

**6 thèmes prioritaires** :

1. Agent identity & authentication
2. **Auditability & non-repudiation** (records des décisions agents + approbations humaines — cohérence directe avec le pattern failure receipt v3.10 Lot E)
3. Interoperability
4. (3 autres thèmes à compléter dans le HTML — relire la source NIST si nécessaire pour la liste exhaustive)

**Calendrier** :
- **RFI agent security threats & vulnerabilities** : clos le 9 mars 2026
- **NCCoE concept paper agents authorization** : clos le 2 avril 2026
- **Sector listening sessions** : tenues en avril 2026 (healthcare, finance, education)
- **AI Agent Interoperability Profile** prévu **Q4 2026**

**Implication PME** : le NIST CAISI est un **soft framework** (pas obligatoire en France/EU) mais il **structure les pratiques internationales**. Les PME qui exportent vers les US ou travaillent avec des grandes entreprises US auront à s'aligner. À surveiller pour 2027.

**Couple naturel avec** :
- **NIST AI RMF Profile Trustworthy AI in Critical Infrastructure** (avril 2026) — reporté éventuellement v3.11 si capacité v3.10 saturée
- **SBOM for AI G7/ANSSI** (Patch D.1 ci-dessus) — convergence internationale traçabilité
- **AI Act Art. 50** (Lot B v3.10) — convergence transparence

### Sources à ajouter dans PR-05

À insérer dans la section finale `#ressources` :

- **McKinsey** — Securing the agentic enterprise: opportunities for cybersecurity providers (mckinsey.com/capabilities/risk-and-resilience/our-insights/securing-the-agentic-enterprise-opportunities-for-cybersecurity-providers, mai 2026)
- **NIST** — AI Agent Standards Initiative (CAISI) (nist.gov + metricstream.com/blog/nists-ai-agent-standards-initiative.html, fév.-avril 2026)

### Renvois croisés depuis PR-05

- Vers **DEP-08 §7bis** (SBOM IA) : encart « cadre opérationnel supply chain » dans la section 4.
- Vers **DEP-05 §8 + §8.5** (Production-grade + Failure receipt v3.10) : encart « patterns techniques de mitigation ».
- Vers **CU-026** : encart « gouvernance managériale des agents » (le pattern « agent = employé »).
- Vers **CU-020** : volet conformité (RGPD + AI Act + fiches CNIL).

### Métadonnées module

- `<meta name="description">` : actualiser pour mentionner la cybersécurité agentique. Suggestion : *« Sécurité IA en PME : du LLM classique à l'agentique 2026. Risques, typologie, NIST CAISI, SBOM IA, McKinsey RAI maturité 2,3/5. »*
- Badge temps de lecture : passer à **+3 min**.

---

## Synthèse cohérence Lot D

Les 2 patches forment un bloc **« convergence internationale sur la sécurisation agentique 2026 »** :

- **Niveau opérationnel** (DEP-08) : SBOM IA — outil technique
- **Niveau stratégique** (PR-05) : McKinsey (constat) + NIST CAISI (cadre futur)

Les 2 patches **se renforcent mutuellement** via cross-link et via le rappel constant de la convergence NIST + ANSSI/G7 + AI Act + McKinsey.

## Item parallèle (à compiler dans brief v3.10)

Chiffre macro à canoniser dans `chiffres-macro-2026.md` (item I-D-005) :

- **RAI maturité moyenne 2,3/5 en 2026 (McKinsey)** — recouvrement attendu avec CU-026, PR-01, DEP-05 (modules gouvernance et production agents).

## Note sur NIST Critical Infrastructure (reportée éventuellement v3.11)

Si la capacité v3.10 sature, le patch NIST AI RMF Profile Critical Infrastructure (avril 2026) peut être reporté en v3.11. Sinon, intégrer en encart léger dans PR-05 section 3 (Typologie des risques) avec mention « pertinent pour PME industrielles vosgiennes (OIV/OSE) ».

Mon arbitrage en cas de capacité disponible : **intégrer** car (1) ça reste un patch léger, (2) c'est cohérent avec le bloc sécurité agentique du Lot D, (3) angle territorial PME industrielles vosgiennes pertinent pour Quai Alpha.
