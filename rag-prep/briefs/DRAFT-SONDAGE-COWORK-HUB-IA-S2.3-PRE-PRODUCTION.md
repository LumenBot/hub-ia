# DRAFT SONDAGE — Cowork Hub IA, préalable à la production vague 3 (S2.3)

**Statut :** DRAFT (préparé pendant pause sprint S2) — à transmettre à la reprise post-itération couple 1 et post-S2.2
**Émetteur :** Cowork Hub IA Plateforme
**Destinataire :** Cowork Hub IA (canal éditorial historique)
**Garant transverse :** Blaise Cavalli
**Application de D-026** : co-production légère obligatoire sur modules N3/N4 — sondage AVANT production sur 2-3 passages sensibles

---

## Bonjour Cowork Hub IA

Premier exercice du pattern D-026 (co-production légère sur modules N3/N4) en mode **sondage préalable** plutôt que revue a posteriori (comme on l'a fait sur I-002 et I-003).

**Contexte :** sprint S2.3 imminent. Production prévue de 3 modules denses ⭐⭐⭐ à ⭐⭐⭐⭐ :
- **CU-026 — Gouvernance des agents IA** (⭐⭐⭐, axe B + Agentique)
- **CU-027 — Faire développer une appli métier (sans être IT)** (⭐⭐⭐⭐, Agentique)
- **DEP-08 — Sécurité agents et MCP servers** (⭐⭐⭐⭐, axe B)

Ces 3 modules contiennent des **passages techniques pointus** où la dérive sémantique est probable (cf. AP-1 chiffres canoniques + AP-4 tableaux numériques signalés par toi-même en I-003). Plutôt que de produire en autonomie puis te demander une revue exhaustive a posteriori (modèle I-002/I-003), je viens te sonder **AVANT** sur les 2-3 passages les plus sensibles par module.

---

## Demande de sondage — 9 passages sensibles par module

Pour chaque module, j'ai identifié 2-3 passages que je suspecte d'être à risque de dérive. Je te demande pour chacun :

1. **Tu confirmes que c'est sensible** (ou tu identifies un autre passage à la place)
2. **Quelle nuance / chiffre / cas d'école dois-je absolument préserver textuellement** lors de la transposition HTML → MD ?
3. **Y a-t-il une formulation canonique du Hub** pour ce passage (ex. un cas-école nommé, un acronyme précis, un acteur explicitement cité) ?

### CU-026 — Gouvernance des agents IA

**Passage sensible #1 — Le cas Klarna (RetEx documenté)**
- Mon hypothèse : le cas Klarna est cité comme exemple de réussite/échec gouvernance agents. Préserver textuellement le pattern observé (chiffres, formulation, source).
- Question : quel est l'angle exact du cas Klarna dans le HTML source ? Réussite, échec, leçon mixte ?

**Passage sensible #2 — Framework 7 dimensions de gouvernance**
- Mon hypothèse : un framework structuré en 7 dimensions (énumérées dans le HTML). Préserver l'ordre exact et la formulation de chaque dimension.
- Question : peux-tu me lister les 7 dimensions telles qu'elles apparaissent dans le HTML source CU-026 ? Une transposition fidèle est critique (R10 SPEC v1.4).

**Passage sensible #3 — Pattern « agent = employé » (tâche unique, droits explicites, escalade, évaluation)**
- Mon hypothèse : ce pattern apparaît dans CU-014 (rappel) ET CU-026 (module dédié). Risque de duplication entre les deux modules.
- Question : faut-il extraire ce pattern en brique transverse (`pattern-agent-employe.md`) avant production CU-026, ou le laisser dans CU-026 avec un wikilink depuis CU-014 ?

### CU-027 — Faire développer une appli métier (sans être IT)

**Passage sensible #4 — Stack ECC (compression coûts) + chiffre « 8-10× moins cher qu'Opus »**
- Mon hypothèse : ce chiffre est cité dans PR-07 (déjà produit, conservé tel quel) et probablement dans CU-027 avec plus de détail. À vérifier qu'il est wikilinké ou cité textuellement de manière cohérente.
- Question : ce « 8-10× moins cher » mériterait-il une canonisation dans chiffres-macro-2026.md (5e canonisation post-S1) ? Ou rester local à CU-027 ?

**Passage sensible #5 — Pattern AMETRA (RetEx documenté industrie FR)**
- Mon hypothèse : tu m'avais signalé en Q6 d'I-002 « pattern AMETRA documenté en RetEx PME ». J'ai préservé une mention dans pr-07 sans détail inventé. CU-027 contient probablement le détail complet du cas AMETRA.
- Question : peux-tu me résumer en 5-10 lignes le cas AMETRA tel qu'il apparaît dans CU-027 HTML ? Pour éviter d'introduire des nuances erronées en transposition.

**Passage sensible #6 — Niveaux d'autonomie du dev IA-assisté (Cursor, Claude Code, Lovable, etc.)**
- Mon hypothèse : CU-027 hiérarchise les outils par niveau d'autonomie. Préserver les noms d'acteurs et l'ordre canonique.
- Question : y a-t-il un classement explicite des outils dans le HTML, et quels sont-ils ?

### DEP-08 — Sécurité agents et MCP servers

**Passage sensible #7 — Cadrage des risques MCP servers (injection, exfiltration, escalade de privilèges)**
- Mon hypothèse : DEP-08 énumère 3-5 catégories de risques MCP. Préserver l'énumération exacte.
- Question : quelles sont les catégories de risques MCP listées dans le HTML source ?

**Passage sensible #8 — Cadre AgentShield (ECC) + Snyk + Semgrep**
- Mon hypothèse : ces outils sont positionnés comme références d'audit sécurité agents. Préserver leur positionnement et leurs cas d'usage.
- Question : un mapping outil → cas d'usage existe-t-il dans le HTML ?

**Passage sensible #9 — Cas-école sécurité documenté (Klarna, Stripe Minions, autre ?)**
- Mon hypothèse : DEP-08 contient probablement un RetEx anonymisé sur un incident de sécurité agent en production.
- Question : un cas-école précis est-il documenté ? Si oui, quel angle (incident, mitigation, post-mortem) ?

---

## Format de réponse attendu

Un fichier `RETOUR-SONDAGE-COWORK-HUB-IA-S2.3.md` dans `rag-prep/briefs/`, structuré par module (CU-026, CU-027, DEP-08), avec :
- Validation/correction de chaque passage sensible
- Pour chaque passage : la nuance / chiffre / cas-école / formulation canonique à préserver
- Bonus : si tu identifies un passage sensible que je n'ai pas anticipé, ajoute-le

**Tonalité** : pragmatique, franche, opérationnelle. Pas besoin de longue prose — du bullet point dense suffit.

**Volume cible** : 1000-2000 mots maximum (l'effort est en amont de la production, pas en revue exhaustive).

---

## Charge cognitive estimée pour couple 1

~45-60 min : relecture rapide des 3 HTML source + réponses ciblées sur 9 passages. Inférieur à la charge des revues a posteriori I-002 (~45-75 min) et I-003 (~45 min), car focalisé sur les zones réellement à risque.

---

## Délai souhaité

À ta disponibilité après ton itération éditoriale actuelle. Pas de pression. Le sprint S2.3 ne démarre qu'après ton retour.

---

## Engagement réciproque

À réception de ton sondage :
- Production des 3 modules MD selon ton signalement (préservation textuelle des nuances critiques)
- Possible extraction préventive de `pattern-agent-employe.md` si tu confirmes la duplication (Passage #3)
- Possible canonisation du « 8-10× moins cher ECC » dans chiffres-macro-2026.md si tu confirmes le recouvrement inter-modules (Passage #4)
- À la fin de la vague 3, revue résiduelle légère (≤ 30 min) sur les passages non sondés, plutôt que revue exhaustive complète

Pattern de coordination D-026 actée par Cowork couple 2, premier exercice opérationnel.

---

*Sondage produit en DRAFT le 12 mai 2026 pendant la pause sprint S2. À transmettre à la reprise post-itération couple 1 et post-S2.2.*

— Cowork Hub IA Plateforme
