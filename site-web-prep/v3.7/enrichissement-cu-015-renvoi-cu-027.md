# Enrichissement CU-015 — Renvoi enrichi vers CU-025 + précisions cas Stripe

**Module cible** : `modules/cu-015-stripe-minions.html`
**Type** : Patch éditorial léger (renvois + actualisation chiffre)
**Volume** : ~150 mots à intégrer

---

## Position de l'enrichissement

Patch léger sur CU-015 (« Asynchronicité agentique — cas Stripe Minions »). Pas de nouvelle section ; juste deux ajouts ciblés dans des sections existantes.

## Contenu à intégrer

### 1. Renvoi vers CU-025 dans la section « Pour aller plus loin »

CU-025 (nouveau module v3.7 sur le Knowledge Management IA-augmenté pour dirigeant) applique le pattern d'asynchronicité agentique à un usage personnel/dirigeant. Le renvoi est naturel.

À ajouter dans le corps du module (section conclusion ou « transposabilité ») :

> Le pattern d'asynchronicité agentique illustré par les Stripe Minions est transposable bien au-delà du code. Pour son application à un cas d'usage personnel/dirigeant — la construction d'un knowledge management auto-apprenant — voir [CU-025 Knowledge management IA-augmenté pour dirigeant](cu-025-knowledge-management-dirigeant.html).

### 2. Actualisation des outils dans la section panorama

Les outils mentionnés dans CU-015 (Cursor, Claude Code, Devin, Aider, Copilot Workspace) sont à compléter par les outils 2026 :

> En 2026, le pattern d'asynchronicité agentique a continué d'évoluer avec l'arrivée de **Kimi K2.6** (Moonshot AI, open-source, ~10 % du coût d'Opus pour 75 % de la qualité), de **ECC stack** (38 agents spécialisés + AgentShield) et des patterns Garry Tan « Fat Skills / Thin Harness » (cf. [CU-014 Multi-agents par fonction](cu-014-multi-agents.html) enrichi en parallèle).

### 3. Renvoi vers DEP-08 dans la section sécurité

À ajouter dans la section actuelle qui mentionne la sécurité du code agentique :

> Pour la sécurité des agents et MCP servers en production (audit AgentShield, garde-fous prompt injection, CVE 2026), voir [DEP-08 Sécurité agents et MCP servers](../deploiement/dep-08-securite-agents-mcp.html).

## Sources à ajouter dans la section finale (Schéma A)

À insérer dans la sous-rubrique « 📰 Articles de fond » :
- [Garry Tan — Meta-Meta-Prompting + Fat Skills Thin Harness](https://x.com/garrytan) — Référence pattern asynchronicité
- [Kirill — Kimi K2.6 Complete A-Z Guide](https://kimi.com/blog/kimi-k2-6) — Évolution du marché coding agentique

## Renvois internes à ajouter

- Vers [CU-025 Knowledge management IA-augmenté pour dirigeant](cu-025-knowledge-management-dirigeant.html) (transposition)
- Vers [CU-014 Multi-agents par fonction](cu-014-multi-agents.html) (patterns Fat Skills)
- Vers [DEP-08 Sécurité agents et MCP](../deploiement/dep-08-securite-agents-mcp.html) (sécurité prod)

## Note Cowork
Patch léger (~150 mots) qui maintient l'identité éditoriale de CU-015 (cas-école managérial, transposable) tout en l'articulant avec les nouveautés v3.7. Aucun changement structurel.
