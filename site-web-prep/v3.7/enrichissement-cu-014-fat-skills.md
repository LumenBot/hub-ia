# Enrichissement CU-014 — Patterns Fat Skills / Thin Harness (Garry Tan)

**Module cible** : `modules/cu-014-multi-agents.html`
**Type** : Patch éditorial (ajout de section)
**Volume** : ~350 mots à intégrer

---

## Position de l'enrichissement

Ajouter une **nouvelle section** dans CU-014, idéalement entre la section actuelle « Architecture multi-agents » et la section « Étude de cas ». Titre suggéré : **« Le pattern Fat Skills / Thin Harness (référence 2026) »**.

## Contenu à intégrer

### 1. Le pattern en deux phrases

**Garry Tan** (CEO Y Combinator) a popularisé en 2025-2026 un pattern d'architecture pour les systèmes IA personnels et organisationnels :

> Le **harness** (runtime) reste **mince** : quelques milliers de lignes de code, juste une logique de routage. Toute l'intelligence est dans des **skills réutilisables et composables** : des fichiers markdown qui décrivent des compétences spécifiques, accumulables et améliorables au fil du temps.

### 2. Pourquoi ce pattern domine en 2026

Trois propriétés fortes :

1. **Compounding effect** : chaque skill ajoutée enrichit les suivantes. Garry Tan a documenté 100+ skills accumulées sur 6 mois dans son système personnel. Le système ne devient pas obsolète, il s'enrichit.

2. **Coût d'apprentissage faible** : pas de framework lourd à maîtriser. Les skills sont en markdown, le harness peut être lu en quelques heures. Un dev senior peut prendre la stack en 2 jours.

3. **Composabilité** : une skill « book-mirror » peut appeler « brain-ops » + « enrich » + « cross-modal-eval » + « pdf-generation ». Chaque skill améliore tout le système.

### 3. Application concrète en PME

Pour une PME qui construit un système multi-agents (cf. cas d'usage actuel CU-014) :

- **Ne pas réinventer un framework custom** (LangChain est lourd, suffit rarement)
- **Utiliser un harness léger** : OpenClaw, Hermes Agent, ou ECC (Everything Claude Code)
- **Construire des skills focalisées** : une skill = une compétence claire, testée, documentée
- **Skillify les workflows répétés** : à chaque fois qu'un workflow est repris 3 fois, le transformer en skill réutilisable

### 4. La méta-skill « Skillify »

Le pattern le plus puissant : une **méta-skill qui crée des skills**. Quand tu rencontres un workflow que tu vas répéter, tu lances « skillify ce que je viens de faire ». Le système :
- Examine le workflow récent
- Extrait le pattern repétable
- Écrit un fichier skill avec triggers et edge cases
- L'enregistre dans le résolveur de routage

**Conséquence** : ton système devient plus capable chaque jour, sans intervention dev.

### 5. Stack technique 2026 (compatible Hub IA)

Pour une PME qui veut adopter ce pattern :

- **Harness** : OpenClaw (Hermes Agent en backup) — open-source, léger
- **Brain (mémoire) ** : GBrain (Karpathy LLM Wiki appliqué)
- **Skills par défaut** : ECC stack (38 agents + 156 skills)
- **Audit sécurité** : AgentShield (cf. [DEP-08](../deploiement/dep-08-securite-agents-mcp.html))

→ Setup PME : 1-3 jours pour un dev senior. Maintenance : ~2-5 h/mois.

## Sources à ajouter dans la section finale (Schéma A)

À insérer dans la sous-rubrique « 📰 Articles de fond » :
- [Garry Tan — Fat Skills, Fat Code, Thin Harness (X.com)](https://x.com/garrytan) — Article de référence
- [Garry Tan — Resolvers + Skillify](https://x.com/garrytan) — Architecture détaillée

À insérer dans la sous-rubrique « 🎓 Tutoriels & cas pratiques » :
- [GBrain GitHub (Garry Tan)](https://github.com/garrytan/gbrain) — Implémentation référence open-source
- [OpenClaw](https://openclaw.ai/) — Harness ouvert
- [Hermes Agent](https://github.com/nicobailon/hermes-agent) — Alternative

## Renvois internes à ajouter

- Vers [CU-027 Faire développer une appli métier](cu-027-dev-applicatif-ia.html) (qui mentionne ECC et Garry Tan déjà)
- Vers [DEP-05 Agents en production : observabilité](../deploiement/dep-05-agents-observabilite.html)
- Vers [DEP-08 Sécurité agents et MCP](../deploiement/dep-08-securite-agents-mcp.html)

## Note Cowork
Cet enrichissement actualise CU-014 avec le pattern de référence 2026, sans casser sa structure éditoriale. Positionne CU-014 comme **module avancé multi-agents** avec lien vers la section Déploiement pour la mise en prod.
