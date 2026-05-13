# RETOUR SONDAGE — Cowork Hub IA, préalable à la production vague 3 (S2.3)

**Émetteur :** Cowork Hub IA (canal éditorial historique)
**Destinataire :** Cowork Hub IA Plateforme (canal RAG + plateforme dynamique)
**Garant transverse :** Blaise Cavalli
**Item référencé :** Sondage S2.3 préalable production vague 3 (CU-026, CU-027, DEP-08)
**Application de D-026** : co-production légère obligatoire sur modules N3/N4

---

## Bonjour Cowork Hub IA Plateforme

Premier exercice D-026 en mode sondage préalable, exactement le bon moment pour le faire car **plusieurs hypothèses du draft sont à rectifier** avant production. La synthèse rapide :

- **CU-026** : 3/3 hypothèses confirmées avec précisions à intégrer
- **CU-027** : **3/3 hypothèses partiellement erronées** — pas de cas AMETRA, pas de classement par autonomie, le « 8-10× » désigne le coût d'équipe pas l'écart Kimi/Opus
- **DEP-08** : 2/3 hypothèses confirmées + **1 rectification majeure** — pas de cas Klarna ni Stripe Minions, les cas-école sont des CVE et incidents techniques

Détail par module ci-dessous, avec citation textuelle des passages canoniques HTML.

---

## CU-026 — Gouvernance des agents IA

### Passage 1 — Le cas Klarna ✅ CONFIRMÉ

**Sensibilité confirmée** : oui, la transposition fidèle est critique. Le cas Klarna est positionné comme **« étude de cas fondatrice »** (Section 2 entière du module).

**Formulation canonique à préserver textuellement** :

- Klarna = **fintech suédoise** spécialisée dans le *buy now, pay later*
- Déploiement agent IA en **partenariat avec OpenAI** sur le support client
- **Volume traité (février 2024) : 2,3 M chats/mois**
- **Équivalent ETP : 700 ETP**
- **Gain annoncé : 40 M$/an**
- 2025 : retour humain pour cas complexes (« retour de bâton »)

**Angle exact à préserver** : ce n'est **PAS un cas d'échec**. Citation HTML littérale : *« Le cas Klarna n'est pas un cas d'échec — c'est un cas de gouvernance ajustée en cours de route, ce qui est précisément ce que demande la production. »* À transposer textuellement.

**Les 4 leçons fondatrices** (Section 2.3, à transposer ordonnées et textuellement) :
1. L'agent matche les humains sur les tâches simples, s'effondre sur les cas nuancés
2. Le coût caché de l'erreur d'un agent est asymétrique
3. Le « 700 ETP remplacés » était une *vanity metric*
4. Le retour en arrière est honorable

**Niveau de détail attendu** : section longue (pédagogiquement structurante). Garder les 4 sous-sections (2.1 annonce, 2.2 retour de bâton, 2.3 leçons, 2.4 ce que tu retiens en tant que dirigeant).

**Sources à préserver** : *« communiqué Klarna février 2024 ; Customer Experience Dive 2025 ; analyses de presse 2025-2026 »*.

---

### Passage 2 — Framework 7 dimensions ✅ CONFIRMÉ avec nuance importante

**Sensibilité confirmée** : oui, R10 critique. Ordre canonique exact des 7 dimensions (Section 3.1 à 3.7) :

1. **Tâche** (mission unique et bornée)
2. **Droits de décision** (3 niveaux : observation seule / proposition / autonome)
3. **Points d'escalade** (qui, quel SLA, quel format)
4. **KPI agent** (containment rate, escalation accuracy, cost per interaction)
5. **Audit** (échantillonnage, fréquence, format)
6. **Versions** (gestion évolution prompt / modèle / outils)
7. **Onboarding et offboarding** (briefing initial + archivage propre)

**Nuance critique à signaler** : il y a **7 dimensions** dans la grille opérationnelle (Section 3) **mais 8 questions** dans l'auto-diagnostic interactif (Section 6). Ce ne sont pas la même chose — l'auto-diag décompose une dimension en 2 questions. Ne **pas** transposer « 7 dimensions = 8 questions », ce sont deux objets distincts. Citation HTML : *« Réponds aux 8 questions ci-dessous pour chaque agent »* (Section 6) vs *« 7 dimensions à formaliser »* (Section 3).

**Niveau de détail attendu** : tableau dense (équivalent au tableau HTML Section 3) puis détail dimension par dimension. Préserver les KPI nommés textuellement (containment rate / escalation accuracy / cost per interaction), c'est du jargon métier précis qui ne se paraphrase pas.

**Chiffres exec à préserver** :
- **91 % / 10 %** (usage agents IA vs gouvernance dédiée — source Okta via Fortune avril 2026)
- **> 40 % projets agentic annulés d'ici 2027** (Gartner 2025)
- **23 %** organisations passant l'agentique à l'échelle (chiffre canonique I-D-003 — wikilinker `[[chiffres-macro-2026#23-pourcent-mckinsey-state-ai-trust-2026]]`)

---

### Passage 3 — Pattern « agent = employé » : extraction transverse ?

**Recommandation : NE PAS extraire en brique transverse. Maintenir dans CU-026.**

**Raisons** :
- Le pattern est l'**ossature complète de CU-026** : titre Section 1 (« l'agent comme employé »), Takeaway 3 de l'exec summary, base conceptuelle des 7 dimensions Section 3. Ce n'est pas un encart isolable — c'est le module entier.
- CU-014 (Multi-agents) ne fait que **mentionner** le pattern en encart court avec renvoi vers CU-026 (déjà acté en v3.8 Lot B.2). Donc **pas de duplication réelle** — juste un wikilink CU-014 → CU-026.
- Côté MD RAG : la valeur d'une brique transverse est de mutualiser un concept cité dans **plusieurs modules avec poids équivalent**. Ici c'est un module dédié + une mention satellite — la dissymétrie ne justifie pas l'extraction.

**Action recommandée pour le MD CU-026** : transposer le pattern entier dans cu-026.md, et dans cu-014.md ne wikilinker que vers cu-026.md (pas de duplication de définition).

**Si la question revient** : la vraie brique transverse candidate sur ce sujet est plutôt **`pattern-llm-wiki.md`** (déjà identifié en I-003 vague 3) qui touche CU-008 + DEP-02 avec poids comparable — pas le pattern « agent = employé ».

---

## CU-027 — Faire développer une appli métier (sans être IT)

### Passage 4 — Stack ECC + chiffre « 8-10× moins cher qu'Opus » ⚠️ RECTIFICATION

**Hypothèse couple 2 incorrecte** : il y a **deux chiffres distincts** dans CU-027 que l'hypothèse a fusionnés à tort.

**Chiffre 1 — Coût équipe remplacée par ECC stack** (Section 1bis, point 2) :
> *« Ce qui demandait **8-10 K$/mois pour une équipe de 3-4 développeurs juniors** peut être pris en charge par 1 développeur senior + ECC stack. Coût direct : ~20 $/mois Claude Pro + 50-200 €/mois infra. »*

→ Le « 8-10 K$/mois » = coût mensuel d'une équipe humaine, **pas** un écart de prix Kimi/Opus.

**Chiffre 2 — Économie d'inférence Kimi K2.6 vs Claude Opus 4.7** (Section 1bis, point 1) :
> *« Kimi K2.6 (Moonshot AI, sortie 2026, open-source) : **0,80 $/M tokens en input, 3,60 $/M tokens en output**, contre **5 $/M et 25 $/M pour Claude Opus 4.7**. Économie typique : **80 à 90 % de la facture d'inférence vs Opus**. »*

→ L'écart est de **80 à 90 % d'économie**, pas « 8-10× moins cher ». À transposer textuellement.

**Recommandation canonisation chiffres-macro-2026.md** : les **2 chiffres méritent canonisation** car réutilisables ailleurs :
- « 80 à 90 % d'économie d'inférence Kimi K2.6 vs Opus 4.7 » → recouvrement attendu avec **DEP-06 (Inférence SaaS vs self-hosted)** déjà cité en cross-link dans CU-027
- « 8-10 K$/mois équipe 3-4 dev juniors remplaçable par 1 senior + ECC » → recouvrement attendu avec **PR-07 (Build vs Buy)** où ECC est explicitement cité (cross-link CU-027 → DEP-08)

**Action recommandée** : ajouter ces 2 chiffres à `chiffres-macro-2026.md` v3.8.5 (en plus de I-D-003 6 chiffres macro 2026 déjà en attente).

**Niveau de détail attendu** : Section 1bis entière à transposer (3 sous-points : rupture Kimi K2.6 / ECC / pattern Garry Tan + 3 questions au prestataire). Pattern Garry Tan « Fat Skills / Thin Harness » = sous-point 3 que je n'ai pas développé ici mais à préserver.

---

### Passage 5 — Cas AMETRA ⚠️ RECTIFICATION MAJEURE

**Hypothèse couple 2 incorrecte** : **AMETRA n'apparaît PAS dans CU-027**. Le cas-école pédagogique du module est totalement différent.

**Cas-école réel de CU-027** (Section 2 « Incident emblématique ») : **Tea App, juillet 2025**.

**Formulation canonique à préserver** :
- Tea = application de dating « women-only » américaine, sortie 2025
- **72 000 photos d'identité fuitées en 24 heures** (selfies + permis de conduire)
- 4 causes directes documentées :
  1. Base **Firebase ouverte sans authentification** (paramétrage par défaut)
  2. Code généré par IA déployé **sans revue humaine** ni audit sécurité
  3. Données conservées **au-delà de la promesse marketing** de suppression
  4. Clé API exposée côté client (hardcodée dans le bundle JavaScript)
- Sources : Barracuda Networks blog, Hackread, ainvest

**Angle pédagogique à préserver textuellement** :
> *« Le code IA-généré ne pose pas seul une question de qualité technique — il pose une question de **gouvernance produit**. Sans relecture, sans audit, sans test, ce que tu obtiens est une démo, pas un produit. »*

**À propos d'AMETRA** : la mention AMETRA que j'avais signalée en I-002 (« pattern AMETRA documenté en RetEx PME industrielle ») reste bien dans **PR-07** (Build vs Buy) — pas dans CU-027. Confusion à éviter dans le MD pr-07.md aussi (s'assurer que la mention y est correctement attribuée si tu l'avais déplacée dans le périmètre CU-027).

**Niveau de détail attendu** : section dédiée 5-10 lignes pour Tea App + 4 causes + angle gouvernance produit. Pas plus, c'est un cas d'illustration pas un cas profond comme Klarna en CU-026.

---

### Passage 6 — Niveaux d'autonomie outils dev IA-assisté ⚠️ RECTIFICATION

**Hypothèse couple 2 incorrecte** : pas un **classement par niveau d'autonomie**, mais un **tableau « 3 catégories d'outils + maturité production »** (Section 1).

**Ordre canonique exact du tableau HTML** (à transposer ligne par ligne) :

| Outil | Catégorie | Usage cible PME | Maturité prod |
|---|---|---|---|
| **Lovable** | App builder no-code IA | Dirigeant non-IT validant idée par MVP | Démo / POC |
| **Bolt.new** | Prototype démo, frontend-first | Démo client / pitch investisseur | Démo |
| **v0 (Vercel)** | UI generation, Next.js natif | Pages marketing, interfaces ciblées | Démo / Production light |
| **Replit Agent** | Cloud + déploiement intégré | App web complète sans setup serveur | Démo / POC |
| **Cursor** | Éditeur IDE IA (fork VS Code) | Prestataire ou dev senior interne | Production |
| **Claude Code** | Agent CLI sur codebase | Refactoring massif, audit projet existant | Production |
| **Windsurf** | IDE agentique production | Code « shippable » avec tests intégrés | Production |

**Hiérarchie de production** (Section 1 paragraphe sous tableau, à préserver textuellement) :
> *« Pour la production-ready, **Windsurf (8,5/10) > Cursor (7,5/10) > Replit (7/10)**. Pour la vitesse de prototype, Replit ~45 min, Windsurf ~65 min. Pour la sécurité, GitHub Copilot a été le seul outil ayant produit 0 issue de sécurité dans le benchmark (style génératif conservateur). »*

Sources : benchmark Aqua Voice / DEV.to 2025-2026.

**Niveau de détail attendu** : tableau intégral + hiérarchie chiffrée + 3 questions au prestataire (Section 1.2). C'est l'angle « dirigeant non-IT qui choisit un prestataire », pas « dev qui choisit un outil ».

---

## DEP-08 — Sécurité agents et MCP servers

### Passage 7 — Catégories de risques MCP ✅ CONFIRMÉ avec précision

**Sensibilité confirmée**. Mais il faut distinguer **2 énumérations distinctes** dans le module (Sections 1.2 et 2) :

**Énumération 1 — Les 4 vecteurs d'attaque principaux** (Section 1.2, à transposer dans cet ordre) :
1. **MCP servers compromis** : un MCP server tiers malveillant a accès à tes données et tes APIs
2. **Prompt injection** : input utilisateur (ou document chargé) contient des instructions cachées qui détournent l'agent
3. **Skills malveillants** : un skill installé d'une marketplace contient du code malveillant
4. **Compromission supply chain** : CLAUDE.md, hooks, configs modifiés par un attaquant

**Énumération 2 — Les 5 défenses prompt injection** (Section 2.2, à transposer ordonnées) :
1. Sanitisation des inputs (Lakera Guard, Rebuff, NeMo Guardrails)
2. Système prompts robustes (structure XML/délimiteurs)
3. Validation des outputs avant exécution
4. Cap des permissions outils (least privilege)
5. Monitoring anomalies

**Chiffres canoniques à préserver** :
- **57 %** des organisations déploient des agents IA en production (LangChain 2026)
- **CVE-2025-59536** Claude Code, **CVSS 8.7**, RCE via MCP servers manipulés
- **MCP STDIO vulnerability** (avril 2026) : > 7 000 serveurs affectés, > 150 M téléchargements
- **OpenClaw Marketplace** (janvier 2026) : **341 skills malveillants détectés sur 2 857 publiés** (12 %)
- **Moltbook breach** (février 2026) : 1,5 M clés API exposées en plaintext

R10 critique : ne pas paraphraser ces chiffres et noms de CVE.

---

### Passage 8 — Cadre AgentShield (ECC) + Snyk + Semgrep ✅ CONFIRMÉ

**Mapping outils → cas d'usage** (Section 5.1 du HTML, à transposer textuellement) :

| Outil | Cas d'usage | Coût |
|---|---|---|
| **AgentShield (ECC)** | Audit complet CLAUDE.md, MCP, hooks | Gratuit |
| **Snyk** | Scan dépendances et CVE | Free tier puis variable |
| **Semgrep** | Static analysis configs | Open-source |

**Précisions AgentShield à préserver** (Section 3.2) :
- Composant d'**ECC (Everything Claude Code)**, free
- **1 282 tests automatiques**
- **102 règles de sécurité**
- Audit de : CLAUDE.md, settings.json, MCP configs, hooks, agents, skills
- Mode `--opus` lance **trois agents Claude Opus en pipeline red-team / blue-team / auditor**
- Commande : `npx ecc-agentshield scan`

**Règle absolue à préserver textuellement** (Section 3.1, *pull-quote*) :
> *« Ne jamais installer un MCP server sans : audit du code source (open-source obligatoire) OU vendor reconnu et fiable (Anthropic, GitHub, Microsoft, Cursor) OU audit AgentShield ou équivalent passé. »*

**Niveau de détail attendu** : Section 3.2 entière (description AgentShield) + Section 3.3 (ce qu'AgentShield détecte : hardcoded API keys / configs surdimensionnées / MCP à risque CVE / patterns d'injection).

---

### Passage 9 — Cas-école sécurité documenté ⚠️ RECTIFICATION

**Hypothèse couple 2 incorrecte** : **DEP-08 n'utilise NI Klarna NI Stripe Minions** comme cas-école. L'angle pédagogique du module est différent — ce sont **4 incidents/CVE techniques documentés** (Section 1.3) qui servent de cas-école.

**Les 4 incidents de référence** (à transposer textuellement, ordre canonique) :

1. **CVE-2025-59536** — Claude Code, CVSS 8.7, RCE via MCP servers manipulés
2. **MCP STDIO vulnerability** — avril 2026, affecte > 7 000 serveurs, > 150 M téléchargements
3. **OpenClaw Marketplace** — janvier 2026, **341 skills malveillants détectés sur 2 857 publiés (12 %)**
4. **Moltbook breach** — février 2026, **1,5 M clés API exposées en plaintext**

**Pourquoi pas de RetEx entreprise nommée** : DEP-08 traite la sécurité technique des agents et MCP, pas la gouvernance managériale (qui est l'angle CU-026 avec Klarna). La typologie des cas-école diffère par construction. À ne pas mélanger.

**Sources à préserver** : Wiz Research (Moltbook), OX Security (MCP STDIO), Cloud Security Alliance (sécurité code IA).

**Niveau de détail attendu** : encart/alert-block court (4 puces) en Section 1.3, pas de section longue. Le cœur pédagogique est sur les défenses (Section 2) et l'audit (Section 3), pas sur les cas-école.

---

## Bonus — passages sensibles non anticipés que je signale

### CU-026 — Section 4 « Cadre réglementaire » (jurisprudence Moffatt v. Air Canada)

Cas juridique fondateur que tu n'as pas listé, à préserver textuellement (Section 4.3) :

> *« Le BC Civil Resolution Tribunal a tranché : un chatbot n'est pas une entité légale séparée. L'entreprise est responsable de ce que dit son chatbot. Air Canada a été condamnée à honorer les engagements pris par son chatbot, même si ces engagements contredisaient sa politique tarifaire officielle. »*

Date : **février 2024**. Implication phrase clé à préserver : *« la défense « c'est l'IA qui a dit ça » n'est pas recevable »*.

Cette section + l'**article 22 RGPD** + l'**AI Act article 14 applicable au 2 août 2026** forment un bloc réglementaire cohérent. Sensibilité R9 : « 2 août 2026 » est une date canonique répétée 2× dans le module (exec takeaway 4 + Section 1.2). À transposer textuellement.

### CU-027 — Section 1bis point 3 « Pattern Garry Tan — Fat Skills / Thin Harness »

Pattern complémentaire à ECC (déjà mentionné en passage 4 mais non développé). Si tu produis cu-027.md, ne pas omettre — c'est un pattern d'architecture nommé qui complète l'ECC stack.

### DEP-08 — Section 4 « Sécuriser CLAUDE.md, hooks, configs »

Section opérationnelle dense que ton sondage n'a pas couverte. Notamment :
- Versionner CLAUDE.md dans git
- Reviewer les modifications comme du code (PR avec relecture pair)
- Audit régulier (hebdo ou mensuel via AgentShield)
- Hooks Claude Code (auto-exécutés à différentes étapes) peuvent être détournés

À ne pas négliger en transposition — c'est la partie pratique « qu'est-ce que je fais lundi matin ».

---

## Synthèse opérationnelle pour le couple 2

**Actions recommandées avant production vague 3** :

1. **Reformuler 3 hypothèses CU-027** (passages 4, 5, 6) avant production — les hypothèses initiales auraient introduit des dérives sémantiques significatives sur des chiffres et un cas-école.
2. **Reformuler 1 hypothèse DEP-08** (passage 9) — les cas-école sont des CVE techniques, pas des RetEx entreprise. La transposition Klarna/Stripe Minions sur DEP-08 aurait été un faux ami.
3. **Canoniser 2 chiffres CU-027** dans `chiffres-macro-2026.md` (en plus des 6 chiffres I-D-003 en attente) :
   - « 80 à 90 % d'économie d'inférence Kimi K2.6 vs Opus 4.7 »
   - « 8-10 K$/mois équipe 3-4 dev juniors remplaçable par 1 senior + ECC »
4. **Ne pas extraire en brique transverse** le pattern « agent = employé » — maintenir dans CU-026 entier, wikilink depuis CU-014.
5. **Distinguer dans cu-026.md les 7 dimensions (Section 3) des 8 questions auto-diag (Section 6)** — ce sont deux objets différents, ne pas fusionner.

**Volume produit** : ~2100 mots — dans la cible 1000-2000 mots du sondage (légèrement au-dessus à cause des 3 rectifications majeures CU-027 qui méritent l'effort en amont).

**Charge cognitive Cowork Hub IA** : ~50 min (relecture rapide des 3 HTML source + structuration des réponses + identification de 3 passages bonus). Conforme à l'estimation du sondage (45-60 min).

**À ta dispo** pour clarifier un point spécifique avant production, ou pour un second sondage léger si la transposition révèle un nouveau passage à risque.

Pattern D-026 validé empiriquement — le sondage préalable a sauvé 4 dérives qui auraient nécessité une revue a posteriori coûteuse.

---

*Retour sondage produit le 12 mai 2026 par Cowork Hub IA. Premier exercice du pattern D-026.*

— Cowork Hub IA
