---
code: vigilance-hallucinations
titre: "Vigilance — hallucinations des LLM"
type: transverse
axe: transverse
niveau: 2
tags: [vigilance, hallucination, llm, verification, sourcing, qualite, 4-familles]
version: 3.12.0
last_updated: 2026-05-22
glosaire_termes: [hallucination, llm, rag, prompt, agent]
derives: ["[[cu-001]]", "[[cu-002]]", "[[cu-008]]", "[[cu-009]]", "[[cu-011]]", "[[cu-020]]", "[[cu-025]]", "[[pr-05]]", "[[pr-06]]", "[[pr-10]]", "[[dep-05]]", "[[dep-07]]"]
public_cible: [dirigeant, ops, r&d]
---

# Vigilance — hallucinations des LLM

> Brique transverse référencée par les modules qui mobilisent un [[glossaire#llm]] ou un [[glossaire#agent]]. Typologie canonique en **4 familles d'hallucinations** alignée sur [[pr-10]] (refonte v3.12 post-PR-10). Pour la discipline managériale opérationnelle complète (4 niveaux de vérification proportionnés à l'enjeu + 5 dimensions managériales + outils de mesure), voir [[pr-10]].

## Qu'est-ce qu'une hallucination

Une [[glossaire#hallucination]] est une affirmation fausse présentée avec assurance par un modèle d'IA. Le modèle ne « sait » pas qu'il invente — il génère le mot le plus probable étape par étape, et certaines séquences statistiquement plausibles sont factuellement fausses.

Le ton assuré du modèle n'est pas un signal de fiabilité : un LLM affirme tout avec la même conviction qu'il dise vrai ou qu'il invente.

## Les 4 familles d'hallucinations (typologie canonique PME 2026)

Typologie opérationnelle alignée sur [[pr-10]] (v3.12), à utiliser comme grille de lecture systématique des outputs IA en production.

### Famille 1 — Chiffres inventés

**Pattern** : l'agent produit un chiffre précis (statistique, montant, pourcentage, date) sans source vérifiable, ou en attribuant le chiffre à une source qui ne le contient pas.

**Détection** : croisement avec sources officielles primaires (INSEE, Bpifrance Le Lab, France Num, France Stratégie pour les chiffres macro français ; rapports OCDE, McKinsey, Bain, Stanford AI Index pour les chiffres internationaux).

### Famille 2 — Citations fabriquées

**Pattern** : l'agent attribue une citation à une personnalité réelle ou à une étude réelle, sans que cette citation existe textuellement.

**Détection** : règle absolue *« aucune citation sans source vérifiable »*. Cliquer chaque lien donné, vérifier que la citation s'y trouve textuellement.

### Famille 3 — Conclusions hors-périmètre

**Pattern** : l'agent extrapole une conclusion qui ne découle pas réellement des éléments fournis, mais qui « sonne » logiquement. Souvent sur des questions hors scope du contexte fourni.

**Détection** : l'agent doit préfixer explicitement par *« basé sur les données disponibles »* ou *« extrapolation à valider »*. Sinon, traiter comme conclusion à challenger.

### Famille 4 — Faux positifs de complétion

**Pattern** « **overclaimed completeness** » documenté par la communauté builders d'agents 2025-2026 : l'agent affirme avoir accompli une tâche (envoyer un email, créer un fichier, exécuter une transaction) qui n'a en réalité pas eu lieu, ou seulement partiellement.

**Détection** : preuve fraîche obligatoire — ID transaction, fichier vérifié dans le système cible, accusé de réception, etc. Ne jamais croire la confirmation d'exécution d'un agent sans preuve indépendante.

## Pourquoi c'est structurellement présent

Les LLM modernes ont des taux d'hallucination résiduels même avec des techniques de mitigation (RAG, fine-tuning, garde-fous). C'est une **propriété structurelle** des modèles génératifs probabilistes, pas un bug à corriger ponctuellement. La discipline d'usage doit l'intégrer dès le départ.

**362 incidents IA documentés en 2025** vs 233 en 2024 (+55 % en un an, Stanford AI Index Report 2026 — cf. [[chiffres-macro-2026]]). Pour les usages stratégiques (décision, communication externe, conformité), considérer toute affirmation chiffrée ou factuelle comme « à vérifier » par défaut.

## La discipline en 3 règles structurantes

**Règle 1 — Toujours vérifier les éléments factuels critiques.** Pour toute affirmation engageante (chiffres, dates, citations, sources, noms propres), lire au moins une source citée vérifiable. Si le modèle ne cite pas de source vérifiable, considérer la réponse comme une piste à creuser, pas comme un fait.

**Règle 2 — Ne jamais prendre une synthèse pour parole d'évangile.** L'outil va vite. Trop vite. La tentation est de prendre une synthèse pour acquise sans la critiquer. Sur les sujets stratégiques, challenger systématiquement les conclusions du modèle (demander des contre-arguments, des cas d'exception, des sources alternatives).

**Règle 3 — Faire diverger les sources.** Quand le sujet est important, ne pas s'appuyer sur une seule réponse d'un seul modèle. Croiser deux LLM, vérifier sur des sources externes humaines (presse, études, experts). Une concordance multi-sources réduit drastiquement le risque d'hallucination commune.

## Mitigations techniques applicables

Pour les contextes où l'hallucination doit être mitigée structurellement (pas seulement vérifiée a posteriori) :

- **RAG avec citation systématique des sources** : oblige le modèle à appuyer sa réponse sur des passages identifiables. Si aucun passage ne couvre la question, le modèle doit refuser plutôt qu'inventer. Voir [[cu-008]] et [[dep-02]].
- **Prompt engineering** : instructions explicites « si tu ne sais pas, dis "je ne sais pas" plutôt que d'inventer », exemples few-shot de comportement attendu. Voir [[glossaire#prompt]].
- **Garde-fous de validation** : règles métier qui interceptent les sorties avant utilisation (un chiffre hors fourchette plausible, un nom propre non présent dans une whitelist, etc.). Voir [[dep-05]].
- **Failure receipt pour les agents** : pattern où chaque action de l'agent émet un reçu d'exécution vérifiable. Mitigation directe de la famille 4 (faux positifs de complétion). Voir [[dep-05]] §8.5.
- **Eval continue** : golden set de questions test rejoué régulièrement pour détecter les régressions. Voir [[dep-07]].

## Cas d'application typiques

- **Recherche augmentée** ([[cu-001]]) : vérifier au moins une source citée par Perplexity, Le Chat Pro ou NotebookLM avant d'inclure un chiffre dans une note de comité — vigilance familles 1 et 2.
- **Rédactionnel** ([[cu-002]]) : ne jamais publier un contenu écrit par IA sans relecture humaine — un chiffre inventé dans un communiqué de presse engage la responsabilité. Vigilance familles 1 et 3.
- **Veille concurrentielle** ([[cu-011]]) et **veille AAP** ([[cu-012]]) : croiser systématiquement avec les sources officielles (registres, sites institutionnels). Vigilance familles 1, 2 et 3.
- **Workflow agentique** ([[cu-015]], [[cu-013]]) : pattern failure receipt obligatoire pour chaque action externe (email envoyé, paiement déclenché, fichier créé). Vigilance famille 4.
- **Conformité RGPD/AI Act** ([[cu-020]]) : ne jamais s'appuyer sur une interprétation IA d'un texte réglementaire sans vérification du texte officiel. Vigilance familles 1, 2 et 3.
- **Knowledge management dirigeant** ([[cu-025]]) : appliquer les 3 règles à chaque sortie IA destinée à éclairer une décision stratégique.

## Anti-patterns observés

- **Confiance par défaut dans le ton assuré du modèle** : un LLM affirme tout avec la même conviction qu'il dise vrai ou qu'il invente. Le ton n'est pas un signal de fiabilité.
- **Citation de source non vérifiée** : reprendre dans un livrable une référence donnée par l'IA sans cliquer sur le lien. Si le lien ne marche pas ou pointe vers autre chose, la source est probablement hallucinée (famille 2).
- **Délégation totale du fact-checking au modèle** : demander à l'IA « cette information est-elle vraie ? » à la place de la vérifier soi-même. L'IA peut halluciner sa propre auto-évaluation.
- **Croire la confirmation d'exécution d'un agent sans preuve** : ne jamais accepter « j'ai envoyé l'email » ou « j'ai créé le fichier » sans vérifier indépendamment dans le système cible (famille 4).

## Pour aller plus loin

- **Discipline managériale opérationnelle complète** ([[pr-10]]) : 4 familles + 4 niveaux de vérification proportionnés à l'enjeu (0 Pas vérif / 1 Échantillonnage / 2 Systématique humaine / 3 Double validation humain + agent réviseur) + 5 dimensions managériales + outils de mesure.
- Cadrage sécurité IA ([[pr-05]]) : Sécurité IA.
- Qualité du code généré par IA ([[pr-06]]) : Qualité du code IA.
- Évaluation continue qualité ([[dep-07]]) : Évaluation continue et qualité IA.
- Pattern RAG comme mitigation ([[cu-008]] et [[dep-02]]) : Knowledge base RAG et RAG en production.
- Pattern failure receipt agents production ([[dep-05]] §8.5) : reçu d'exécution vérifiable pour chaque action.
