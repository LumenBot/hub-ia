# Enrichissement CU-027 — État de l'art outils 2026

**Module cible** : `modules/cu-027-dev-applicatif-ia.html`
**Type** : Patch éditorial (ajout de section)
**Volume** : ~400 mots à intégrer

---

## Position de l'enrichissement

Ajouter une **nouvelle section après la section actuelle « Panorama des outils en 2026 »** (qui devient l'aperçu général). La nouvelle section approfondit l'évolution rapide du marché en 2026.

Titre suggéré : **« État de l'art 2026 : la rupture économique Kimi K2.6 + ECC stack »**

## Contenu à intégrer

### 1. La rupture Kimi K2.6 (2026)

**Kimi K2.6** (Moonshot AI, sortie 2026, open-source) bouleverse l'économie du coding agentique :
- **0,80 $/M input, 3,60 $/M output** (vs Claude Opus 4.7 à 5 $/M input, 25 $/M output)
- **Performance proche d'Opus 4.7** sur SWE-Bench, Terminal-Bench, agentic coding (~75-90 %)
- **Open-source** (self-hostable)
- API disponible chez Together.ai, Modal Labs, Fireworks AI, Groq

→ **Implication PME** : pour 75-80 % des cas d'usage de dev applicatif IA-assisté, Kimi K2.6 est suffisant. Économie typique : **80-90 % de la facture** vs Opus. Garder Opus pour les 20-25 % vraiment complexes.

### 2. ECC (Everything Claude Code) — l'écosystème open-source qui remplace une équipe de devs

**ECC** est devenu le standard 2026 pour qui pilote un projet de dev applicatif IA-assisté :
- 38 agents spécialisés (planner, security-reviewer, typescript-reviewer, etc.)
- 156 skills réutilisables
- 72 commandes slash
- **AgentShield** : audit sécurité gratuit (1282 tests, 102 règles)

→ **Implication PME** : ce qui demandait 8-10 K$/mois pour une équipe de 3-4 devs juniors peut être pris en charge par 1 dev senior + ECC stack. Coût direct : ~$20/mois Claude Pro + ~50-200 €/mois infra.

### 3. Patterns Garry Tan — Fat Skills / Thin Harness

**Garry Tan** (CEO Y Combinator) a popularisé le pattern « Fat Skills / Thin Harness » : architecture où le runtime est minimal (quelques milliers de lignes) et toute l'intelligence est dans des **skills réutilisables et composables** (markdown + scripts).

Bénéfices documentés :
- 100+ skills accumulables sur 6 mois
- Compounding effect : chaque skill améliore le suivant
- Coût d'apprentissage faible (markdown, pas de framework)

→ Voir aussi : [CU-014 Multi-agents par fonction](cu-014-multi-agents.html) qui sera enrichi en parallèle (v3.7).

### 4. Implications stratégiques pour le pilotage

Trois questions à poser à ton prestataire IA-assisté en 2026 :

1. **« Tu utilises quoi comme modèle de base ? »** — Si la réponse est « Opus uniquement », demander pourquoi pas Kimi K2.6 sur les cas non complexes (économie 80-90 %).
2. **« Tu utilises ECC ou un équivalent ? »** — Si non, demander quel framework de skills/agents est utilisé. Sans framework, ton coût de maintenance va exploser.
3. **« Tu lances AgentShield avant chaque mise en prod ? »** — Si non, exiger qu'un audit sécurité soit fait. Cf. [DEP-08 Sécurité agents](../deploiement/dep-08-securite-agents-mcp.html).

## Sources à ajouter dans la section finale (Schéma A)

À insérer dans la sous-rubrique « 📰 Articles de fond » existante :
- [Kirill — Kimi K2.6 Complete A-Z Guide](https://kimi.com/blog/kimi-k2-6) — Analyse économique et technique
- [Garry Tan — Meta-Meta-Prompting + Fat Skills Thin Harness](https://x.com/garrytan) — Pattern d'architecture compounding
- [Affaan / ECC GitHub](https://github.com/affaan-m/everything-claude-code) — Stack open-source de référence

## Renvois internes à ajouter

- Vers [DEP-06 Inférence SaaS vs self-hosted](../deploiement/dep-06-inference-saas-self-hosted.html) (sur Kimi K2.6 et coûts)
- Vers [DEP-08 Sécurité agents et MCP](../deploiement/dep-08-securite-agents-mcp.html) (AgentShield)
- Vers [CU-014 Multi-agents par fonction](cu-014-multi-agents.html) (patterns Garry Tan)

## Note Cowork
Cet enrichissement peut faire ~600-800 mots côté HTML final (avec mise en forme + composants visuels). Maintient la posture éditoriale CU-027 : pédagogique pour dirigeant non-IT, pas tutoriel d'ingénieur.
