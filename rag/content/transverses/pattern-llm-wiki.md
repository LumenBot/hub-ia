---
code: pattern-llm-wiki
titre: "Pattern LLM Wiki — alternative architecturale au RAG classique"
type: transverse
axe: transverse
niveau: 3
tags: [llm-wiki, karpathy, rag, architecture, persistent-memory, self-maintaining-kb]
version: 3.8.6
last_updated: 2026-05-12
glosaire_termes: [llm-wiki, rag, vector-store, chunk, embeddings]
derives: ["[[cu-008]]", "[[cu-014]]", "[[cu-025]]", "[[dep-02]]"]
public_cible: [dirigeant, ops, r&d, tech]
---

# Pattern LLM Wiki — alternative architecturale au RAG classique

> Brique transverse référencée par les modules qui mobilisent un pattern de [[glossaire#rag]] ou de connaissance organisationnelle. Une seule définition canonique du pattern LLM Wiki et de ses 5 évolutions post-Karpathy. Évite la duplication entre [[cu-008]] (Knowledge base RAG, angle décideur) et [[dep-02]] (RAG en production, angle technique).

## Le pattern en deux phrases

[[glossaire#llm-wiki]] est une alternative architecturale au RAG vectoriel classique, proposée par Andrej Karpathy en avril 2026 (gist GitHub, 17 M de vues, 5 000 stars en quelques jours).

- **RAG classique** : à chaque requête, on cherche dans le [[glossaire#vector-store]] → on récupère des [[glossaire#chunk]]s → on injecte dans le prompt → on génère une réponse → on oublie tout. *Stateless. Pas de mémoire de synthèse.*
- **LLM Wiki** : on maintient une base markdown structurée par un LLM. Quand on ajoute un document, le LLM met à jour les pages markdown affectées (synthèses, entités, contradictions). Quand un utilisateur pose une question, le LLM consulte directement les pages markdown pertinentes. *Synthèse persistante au lieu de retrieval éphémère.*

Le shift conceptuel : **synthèse persistante au lieu de retrieval éphémère**.

## Quand le LLM Wiki bat le RAG vectoriel — tableau de décision

| Volume corpus | Stabilité | Recommandation |
|---|---|---|
| < 50K tokens | Stable (MAJ trimestrielle) | LLM Wiki (~95 % moins cher en tokens vs RAG vectoriel) |
| 50K-100K tokens | Stable | LLM Wiki ou RAG dense léger (Chroma) |
| 100K-1M tokens | Mixte | RAG hybride (cf. [[dep-02]]) |
| > 1M tokens | Quelconque | RAG hybride avec sharding |
| Quelconque | Mises à jour temps réel | RAG vectoriel (LLM Wiki ne convient pas) |

Source des seuils : Karpathy gist (avril 2026) + benchmarks communautaires post-publication (mai 2026).

## Cas types pertinents en PME

- **Manuel produit stable** : documentation technique d'une machine industrielle, manuel d'intégration. Volume 30K-80K tokens, mises à jour trimestrielles.
- **FAQ métier structurée** : questions/réponses standardisées, < 50K tokens.
- **Procédures internes RH** : règlement intérieur, processus de recrutement, parcours d'onboarding.
- **Documentation projet** : cahier des charges, spécifications fonctionnelles, manuel d'intégration.

## Cas où ce n'est PAS pertinent

- **Volume > 200K tokens** : le contexte LLM devient trop coûteux et lent.
- **Mises à jour temps réel** : réindexation continue impossible, le LLM Wiki ne suit pas.
- **Corpus très hétérogène** : la maintenance markdown devient une charge.
- **Besoin de réponses ultra-précises avec citations multiples** : le RAG hybride reste meilleur sur ce cas.

## Coût-bénéfice mesuré

Pour une PME avec un corpus de 50K tokens (calcul typique) :

| Architecture | Coût mensuel typique | Maintenance |
|---|---|---|
| RAG vectoriel (Pinecone + OpenAI + Claude) | ~150-300 €/mois | Modérée (re-indexation manuelle) |
| LLM Wiki (Claude uniquement, base MD) | ~10-50 €/mois | Légère (le LLM auto-maintient) |

**Économie potentielle de 90 %** sur les petits corpus stables. À pondérer par l'effort de mise en place initial (similaire dans les deux cas).

## Les 5 patterns post-Karpathy — écosystème mai 2026

Depuis le gist initial de Karpathy (avril 2026), un écosystème de forks open-source a émergé, introduisant des patterns complémentaires :

**1. Persistent memory** : la mémoire de l'agent persiste entre les sessions et entre les utilisateurs (avec gestion de droits). Permet de capitaliser au fil du temps les interactions sans repartir de zéro.

**2. Self-maintaining KB** : la base de connaissances se met à jour automatiquement quand de nouveaux documents sont ingérés (synthèses regénérées). Réduit drastiquement la charge de maintenance manuelle.

**3. Contradiction detection** : le système identifie automatiquement les contradictions entre nouveaux contenus et synthèses existantes, et alerte. Outil structurant pour les organisations qui ingèrent des sources hétérogènes.

**4. Multi-agent vaults** : plusieurs agents spécialisés partagent et enrichissent un vault commun. Pattern utile pour les organisations où des fonctions distinctes (juridique, technique, commercial) co-construisent la base. Lien avec [[cu-014]] (Multi-agents par fonction).

**5. Sleep consolidation** : pattern inspiré du sommeil humain. La base se consolide « hors ligne » pendant les périodes creuses (regénération de synthèses, déduplication). Optimise les coûts d'inférence en évitant le travail en temps réel sur les opérations lourdes.

Ces 5 patterns représentent la trajectoire architecturale la plus prometteuse pour les RAG d'organisations sur corpus modéré.

## 3 questions à se poser avant de choisir LLM Wiki vs RAG classique

1. **Volume et stabilité du corpus** : < 100K tokens et stable ? → LLM Wiki probablement pertinent. Sinon → RAG hybride.
2. **Cas d'usage temps réel** : besoin de réponses sur des données qui changent en continu ? → RAG vectoriel obligatoire.
3. **Maturité organisationnelle** : capacité à maintenir une base markdown structurée par un LLM ? Si oui → LLM Wiki accessible. Si non → SaaS RAG type NotebookLM en première étape.

## Implication pour les PME qui démarrent un RAG

Ne pas sauter directement sur Pinecone + embeddings + reranking si le corpus est petit et stable. Tester d'abord l'approche LLM Wiki — souvent suffisante, beaucoup moins coûteuse, beaucoup plus simple à maintenir.

C'est la cible architecturale long terme de la **Phase 2 LLM Wiki layer** de la plateforme Hub IA Learning Center (roadmap couple 2).

## Pour aller plus loin

- Module fonctionnel orienté décideur : [[cu-008]] (Knowledge base RAG)
- Module technique orienté production : [[dep-02]] (RAG en production : choisir son architecture)
- Knowledge management dirigeant — pattern proche : [[cu-025]] (Knowledge management IA-augmenté pour dirigeant)
- Multi-agents synergie : [[cu-014]] (Multi-agents par fonction)

**Articles de fond externes** :
- Karpathy A., LLM Wiki — gist GitHub avril 2026 (référence canonique)
- DEP-02 §2 « LLM Wiki Karpathy — alternative crédible pour les petits corpus » (Hub IA Learning Center)
