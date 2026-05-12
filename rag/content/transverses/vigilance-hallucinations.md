---
code: vigilance-hallucinations
titre: "Vigilance — hallucinations des LLM"
type: transverse
axe: transverse
niveau: 2
tags: [vigilance, hallucination, llm, verification, sourcing, qualite]
version: 3.8.2
last_updated: 2026-05-11
glosaire_termes: [hallucination, llm, rag, prompt]
derives: ["[[cu-001]]", "[[cu-002]]", "[[cu-008]]", "[[cu-009]]", "[[cu-011]]", "[[cu-020]]", "[[cu-025]]", "[[pr-05]]", "[[pr-06]]", "[[dep-07]]"]
public_cible: [dirigeant, ops, r&d]
---

# Vigilance — hallucinations des LLM

> Brique transverse référencée par les modules qui mobilisent un [[glossaire#llm]]. Une seule définition canonique, des recommandations opérationnelles applicables à tout contexte d'usage IA.

## Qu'est-ce qu'une hallucination

Une [[glossaire#hallucination]] est une affirmation fausse présentée avec assurance par un modèle d'IA. Le modèle ne « sait » pas qu'il invente — il génère le mot le plus probable étape par étape, et certaines séquences statistiquement plausibles sont factuellement fausses.

Trois types d'hallucinations fréquentes à connaître :
1. **Hallucinations factuelles** : un fait précis inventé (date, chiffre, nom, événement historique). Particulièrement fréquentes sur les détails chiffrés.
2. **Hallucinations de sources** : un article, une étude, un auteur cité qui n'existe pas. Le modèle compose un nom et une URL plausibles à partir des patterns de ses données d'entraînement.
3. **Hallucinations d'inférence** : une conclusion qui ne découle pas réellement des éléments fournis, mais qui « sonne » logiquement.

## Pourquoi c'est structurellement présent

Les LLM modernes ont des taux d'hallucination résiduels même avec des techniques de mitigation (RAG, fine-tuning, garde-fous). C'est une **propriété structurelle** des modèles génératifs probabilistes, pas un bug à corriger ponctuellement. La discipline d'usage doit l'intégrer dès le départ.

Pour les usages stratégiques (décision, communication externe, conformité), considérer toute affirmation chiffrée ou factuelle comme « à vérifier » par défaut.

## La discipline en 3 règles

**Règle 1 — Toujours vérifier les éléments factuels critiques.** Pour toute affirmation engageante (chiffres, dates, citations, sources, noms propres), lire au moins une source citée vérifiable. Si le modèle ne cite pas de source vérifiable, considérer la réponse comme une piste à creuser, pas comme un fait.

**Règle 2 — Ne jamais prendre une synthèse pour parole d'évangile.** L'outil va vite. Trop vite. La tentation est de prendre une synthèse pour acquise sans la critiquer. Sur les sujets stratégiques, challenger systématiquement les conclusions du modèle (demander des contre-arguments, des cas d'exception, des sources alternatives).

**Règle 3 — Faire diverger les sources.** Quand le sujet est important, ne pas s'appuyer sur une seule réponse d'un seul modèle. Croiser deux LLM, vérifier sur des sources externes humaines (presse, études, experts). Une concordance multi-sources réduit drastiquement le risque d'hallucination commune.

## Mitigations techniques applicables

Pour les contextes où l'hallucination doit être mitigée structurellement (pas seulement vérifiée a posteriori) :

- **RAG avec citation systématique des sources** : oblige le modèle à appuyer sa réponse sur des passages identifiables. Si aucun passage ne couvre la question, le modèle doit refuser plutôt qu'inventer. Voir [[cu-008]] et [[dep-02]].
- **Prompt engineering** : instructions explicites « si tu ne sais pas, dis "je ne sais pas" plutôt que d'inventer », exemples few-shot de comportement attendu. Voir [[glossaire#prompt]].
- **Garde-fous de validation** : règles métier qui interceptent les sorties avant utilisation (un chiffre hors fourchette plausible, un nom propre non présent dans une whitelist, etc.). Voir [[dep-05]].
- **Eval continue** : golden set de questions test rejoué régulièrement pour détecter les régressions. Voir [[dep-07]].

## Cas d'application typiques

- **Recherche augmentée** ([[cu-001]]) : vérifier au moins une source citée par Perplexity, Le Chat Pro ou NotebookLM avant d'inclure un chiffre dans une note de comité.
- **Rédactionnel** ([[cu-002]]) : ne jamais publier un contenu écrit par IA sans relecture humaine — un chiffre inventé dans un communiqué de presse engage la responsabilité.
- **Veille concurrentielle** ([[cu-011]]) et **veille AAP** ([[cu-012]]) : croiser systématiquement avec les sources officielles (registres, sites institutionnels).
- **Conformité RGPD/AI Act** ([[cu-020]]) : ne jamais s'appuyer sur une interprétation IA d'un texte réglementaire sans vérification du texte officiel.
- **Knowledge management dirigeant** ([[cu-025]]) : appliquer les 3 règles à chaque sortie IA destinée à éclairer une décision stratégique.

## Anti-patterns observés

- **Confiance par défaut dans le ton assuré du modèle** : un LLM affirme tout avec la même conviction qu'il dise vrai ou qu'il invente. Le ton n'est pas un signal de fiabilité.
- **Citation de source non vérifiée** : reprendre dans un livrable une référence donnée par l'IA sans cliquer sur le lien. Si le lien ne marche pas ou pointe vers autre chose, la source est probablement hallucinée.
- **Délégation totale du fact-checking au modèle** : demander à l'IA « cette information est-elle vraie ? » à la place de la vérifier soi-même. L'IA peut halluciner sa propre auto-évaluation.

## Pour aller plus loin

- Cadrage sécurité IA : [[pr-05]] (Sécurité IA)
- Qualité du code généré par IA : [[pr-06]] (Qualité du code IA)
- Évaluation continue qualité : [[dep-07]] (Évaluation continue et qualité IA)
- Pattern RAG comme mitigation : [[cu-008]] (Knowledge base RAG) et [[dep-02]] (RAG en production)
