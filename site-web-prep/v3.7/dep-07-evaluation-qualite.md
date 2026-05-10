# DEP-07 — Évaluation continue et qualité IA

**Public cible :** dirigeant qui pilote la qualité IA + équipe technique en charge des evals

---

## Métadonnées (pour Claude Code)

- **Section** : Déploiement
- **Niveau** : ⭐⭐⭐⭐ Expert
- **Type** : Cadrage stratégique
- **Durée lecture** : 17 min
- **Emoji h1** : ✅
- **Titre métier visible** : « Évaluation continue et qualité IA »
- **Sous-titre hero** : Tu ne peux pas piloter ce que tu ne mesures pas. Une eval pipeline, c'est ce qui distingue le projet IA amateur du projet IA production. Voici comment la construire en PME, sans être FAANG.
- **Card index promesse** : « Cadrage stratégique »

## Synthèse exécutive

### Pourquoi cette page ?

Tu as un système IA en production. Tu changes un prompt, un modèle, ou la pipeline RAG. **Comment sais-tu que la qualité s'améliore et ne se dégrade pas ?** Si tu ne peux pas répondre, tu pilotes à l'aveugle. Cette fiche te donne le cadre minimum d'une **eval pipeline** : golden datasets, evals automatiques, regression checks.

L'enjeu est documenté : **la qualité est le blocker n°1 pour 32 % des organisations** déployant des agents IA (LangChain *State of Agent Engineering 2026*). Sans eval pipeline, tu détectes les dégradations par les plaintes utilisateurs — trop tard.

### 4 takeaways

1. **Une eval pipeline distingue les projets IA amateurs des projets en production.** C'est obligatoire dès que tu as une vraie utilisation. Coût d'entrée raisonnable (1-2 semaines de setup pour une PME), gain massif (détection précoce des dégradations, justification des changements de modèle, ROI mesurable).

2. **La distinction clé : evals (avant déploiement) vs observabilité (après).** Les evals répondent à « est-ce que la sortie est bonne ? » avec des datasets golden. L'observabilité (cf. [DEP-05](dep-05-agents-observabilite.html)) répond à « qu'est-ce qui se passe en prod en ce moment ? ». Les deux sont nécessaires et complémentaires.

3. **3 types d'evals à combiner.** (a) Evals **règle-based** (format JSON valide, longueur de réponse, mots-clés interdits) — rapides et déterministes. (b) Evals **sémantiques** (similarité avec réponse de référence) — pour fact-checking. (c) Evals **LLM-as-judge** (un LLM juge la qualité d'une autre sortie) — pour qualité narrative.

4. **Sweet spot dataset golden PME : 50-200 cas.** Suffit pour détecter les régressions majeures (gap > 5 %). Aller au-delà (1000+ cas) demande processus d'annotation industrialisé, généralement disproportionné en PME.

### Stats (3-4)

- **32 %** : qualité = blocker n°1 pour les organisations déployant des agents (LangChain 2026)
- **Sweet spot PME** : 50-200 cas dans le dataset golden
- **Gain typique** d'une eval pipeline : détection précoce de **80-90 % des régressions** avant que les utilisateurs ne les remontent
- **Délai de mise en place** : 1-2 semaines pour une PME

### Quand cette page est utile

Tu as un système IA en production sans eval pipeline et tu te poses la question. Tu changes régulièrement de modèle ou de prompt et tu veux savoir si ça améliore ou dégrade. Tu as eu des incidents qualité que tu n'avais pas anticipés. Tu veux convaincre ta direction du ROI d'une eval pipeline.

## Section 1 — Pourquoi tu ne peux pas piloter sans evals

### 1.1 Les 4 questions auxquelles seule une eval pipeline répond

1. **Est-ce que mon prompt v2 est meilleur que mon prompt v1 ?** (Sans eval : impossible de savoir, on devine)
2. **Est-ce que basculer de Claude Sonnet à Kimi K2.6 dégrade la qualité ?** (Sans eval : pari aveugle)
3. **Est-ce que mon RAG s'est dégradé après l'ajout de 1000 nouveaux documents ?** (Sans eval : on découvre par les plaintes)
4. **Est-ce que ma nouvelle fonctionnalité agent maintient le niveau qualité antérieur ?** (Sans eval : on fait confiance)

### 1.2 Le cycle « prompt → eval → improve → repeat »

C'est le cycle de référence du LLMOps moderne :

```
Prompt v1 → Run sur golden → Score
   ↓
Analyse erreurs → Identification patterns
   ↓
Prompt v2 → Run sur golden → Score
   ↓
Comparer Score v2 vs v1 → Garder si amélioration
```

→ Sans dataset golden et scoring automatique, ce cycle est impossible.

## Section 2 — Construire le dataset golden minimum

### 2.1 Le format type

Pour chaque cas du golden :
- **Input** : le prompt utilisateur réel ou représentatif
- **Contexte** (si applicable) : documents RAG, historique conversation
- **Expected output** : la réponse idéale (ou les caractéristiques d'une bonne réponse)
- **Tags** : catégorie de cas (facile/moyen/difficile, type de question, etc.)
- **Source** : d'où vient le cas (utilisateur réel anonymisé, cas synthétique, edge case)

### 2.2 Les 4 sources de cas pour ton golden

1. **Cas réels anonymisés** : extraits de tes logs production (anonymise les PII). Reflète la distribution réelle des usages.
2. **Cas edge** : situations rares mais critiques (questions ambiguës, cas limites, erreurs typiques).
3. **Cas adverses** : prompts de stress test (jailbreak attempts, prompt injection, requêtes hors scope).
4. **Cas synthétiques** : générés par LLM puis revus humain — pour étendre la couverture.

### 2.3 Sweet spot PME : 50-200 cas

- **< 30 cas** : insuffisant, statistiques non représentatives
- **30-50 cas** : minimum viable pour démarrer
- **50-200 cas** : sweet spot PME, équilibre coût annotation vs représentativité
- **200-1000 cas** : pour cas à fort enjeu, demande processus d'annotation industriel
- **> 1000 cas** : généralement proportionné aux ETI / scale-ups

## Section 3 — Les 3 types d'evals à combiner

### 3.1 Evals règle-based (rapides, déterministes)

Vérifications automatiques sans LLM :
- **Format** : JSON valide selon schéma, XML conforme, longueur
- **Mots-clés** : présence obligatoire, mots interdits (data leak, vulgarité)
- **Patterns regex** : numéros au bon format, dates valides
- **Latence** : temps de réponse sous SLA

→ Coût : quasi-nul. Vitesse : milliseconde. À automatiser systématiquement.

### 3.2 Evals sémantiques (similarity scoring)

Comparaison entre la sortie générée et une référence :
- **BLEU / ROUGE** : métriques classiques (utiles mais imparfaites)
- **Embedding similarity** : cosine similarity entre embedding de la sortie et de la référence
- **BERTScore** : variante avancée

→ Coût : faible. Vitesse : 100ms-1s. Utile pour fact-checking et tâches structurées.

### 3.3 Evals LLM-as-judge (qualité narrative)

Un LLM juge la qualité d'une sortie d'un autre LLM, selon des critères définis :
- **Critères** : précision, cohérence, ton, complétude, absence d'hallucination
- **Échelle** : 1-5 ou 1-10, avec rationale obligatoire
- **Modèle juge** : généralement plus puissant que le modèle évalué (ex : Claude Opus juge Claude Sonnet)

→ Coût : significatif (chaque eval = 1 appel LLM puissant). À utiliser parcimonieusement, en complément des règle-based.

### 3.4 Stratégie type PME

- **Règle-based** sur 100 % des cas (rapide, gratuit)
- **Sémantique** sur 100 % des cas où une référence existe (fact-checking)
- **LLM-as-judge** sur 20-30 % des cas (échantillonnage qualité narrative, coût maîtrisé)

## Section 4 — Outils d'évaluation 2026

### 4.1 Stack open-source self-hosted

| Outil | Rôle | Notes |
|---|---|---|
| **Phoenix Arize** | Eval + tracing OSS, open-source | Référence open-source 2026 |
| **Langfuse** | Eval + observabilité (cf. DEP-05) | Eval intégrée à l'observabilité |
| **DeepEval** | Bibliothèque Python eval pure | Bien pour tests automatisés CI |
| **PromptBench (Microsoft)** | Eval suite robustness | Pour stress test |
| **Eleuther LM Eval Harness** | Standard eval communauté open | Pour benchmarks modèles |

### 4.2 Stack SaaS

| Outil | Rôle | Coût typique PME |
|---|---|---|
| **Comet Opik** | Eval + observabilité (déjà cité DEP-05) | Free tier puis ~50-200 €/mois |
| **LangSmith** | Eval intégrée à LangChain | ~30-200 €/mois |
| **Patronus AI** | Eval enterprise spécialisé | Devis |
| **Braintrust** | Eval-first SaaS | Free tier puis variable |

### 4.3 Recommandation pratique

Pour démarrer en PME : **Phoenix Arize self-hosted** + **DeepEval** pour tests CI. Stack gratuit, contrôle, EU.

Si manque de bandwidth ops : **Comet Opik free tier** + **DeepEval pour CI**.

## Section 5 — Mettre en place les regression checks

### 5.1 Le principe

À chaque modification (nouveau prompt, nouveau modèle, nouvelle pipeline RAG) : **run automatique sur le golden** + comparaison avec la baseline. Si dégradation > seuil défini → bloquer le déploiement.

### 5.2 Workflow type CI/CD pour LLM

```
Modification (PR) → Trigger CI
   ↓
Run golden eval (50-200 cas)
   ↓
Comparer scores vs main branch
   ↓
Si dégradation > 5% → bloquer merge
Si amélioration ≥ 0% → autoriser merge
   ↓
Deploy
   ↓
Monitor en prod (cf. DEP-05)
```

### 5.3 Outils CI/CD compatibles

- **GitHub Actions** : runners gratuits pour OSS, payants à grand volume
- **GitLab CI** : équivalent
- **Argo Workflows** : pour pipelines plus complexes self-hosted

→ Setup PME : 1-3 jours pour wirer une PR avec un run d'eval automatique.

## Section 6 — A/B testing en production

### 6.1 Pourquoi A/B tester

Pour valider l'impact réel d'une amélioration sur les utilisateurs (vs amélioration mesurée sur le golden, qui peut être un overfitting).

### 6.2 Pattern type

- 50 % des sessions → variante A (baseline)
- 50 % des sessions → variante B (nouvelle)
- Mesure des KPI : satisfaction explicite (👍/👎), conversion, drop-off, NPS
- Durée minimum : 1-2 semaines pour signal statistique

### 6.3 Outils

- **LiteLLM gateway** (cf. [DEP-06](dep-06-inference-saas-self-hosted.html)) supporte le routage A/B nativement
- **Statsig**, **Eppo**, **Optimizely** : plateformes A/B testing établies

## Section 7 — Plan d'action 30 jours pour une eval pipeline minimale

### Jours 1-7 — Préparation
- Identifier les cas d'usage à mesurer (le cas critique en priorité)
- Construire le golden initial : 50 cas (mix réels anonymisés + edge cases)
- Définir les KPI cibles (score précision, latence p95, coût/requête)

### Jours 8-15 — Setup outillage
- Choisir stack (Phoenix Arize self-hosted ou Comet Opik free tier)
- Implémenter evals règle-based (format, mots-clés, patterns)
- Implémenter evals sémantiques sur cas avec référence

### Jours 16-23 — Intégration CI/CD
- Wirer une PR à un run d'eval automatique
- Définir seuil de blocage (ex : -5 % qualité = bloque le merge)
- Communiquer le workflow à l'équipe

### Jours 24-30 — LLM-as-judge échantillonné
- Déployer LLM-as-judge sur 20 % des cas (qualité narrative)
- Calibrer les prompts juges sur 10-20 cas annotés humain
- Run quotidien automatique avec alerte sur dégradation

## Section 8 — Pour aller plus loin (Schéma A)

### Callout d'aiguillage

> Pour le panorama complet des outils d'eval et observabilité LLM, retrouve les fiches détaillées sur la [page Ressources du Hub](../ressources.html#bibliographie).

### 📰 Articles de fond
- [Avi Chawla — Eval & observability layers](https://blog.dailydoseofds.com/p/foundations-of-ai-engineering-and-0a6) — Pilier 8 LLM Engineering Roadmap
- [Anthropic Engineering — Building evaluations](https://www.anthropic.com/engineering) — Pratiques de référence
- [LangChain — State of Agent Engineering 2026](https://blog.langchain.dev/) — Étude annuelle, qualité = blocker n°1

### 🎓 Tutoriels & cas pratiques
- [Phoenix Arize Docs](https://phoenix.arize.com/) — Eval + tracing open-source
- [DeepEval GitHub](https://github.com/confident-ai/deepeval) — Bibliothèque eval Python
- [PromptBench (Microsoft)](https://github.com/microsoft/promptbench) — Stress test prompts

### 📚 Documentation officielle & études
- [Comet Opik docs](https://www.comet.com/docs/opik/) — Pratique eval + observabilité
- [LangSmith — Evaluation guide](https://docs.smith.langchain.com/) — Référence LangChain ecosystem
- [Eleuther LM Eval Harness](https://github.com/EleutherAI/lm-evaluation-harness) — Standard communauté open

### 👥 Communautés & veille
- [Phoenix Arize Slack](https://arize-ai.slack.com/) — Communauté open-source
- [LangChain Discord](https://discord.gg/langchain) — Échanges eval pratique

## Renvois internes pour Claude Code

- **Section 1.2 (cycle)** : lien `<a href="dep-03-context-engineering-couts.html">DEP-03</a>` (gouvernance prompts)
- **Section 5.1** : lien `<a href="dep-05-agents-observabilite.html">DEP-05</a>` (observabilité prod)
- **Section 6.3** : lien `<a href="dep-06-inference-saas-self-hosted.html">DEP-06</a>` (LiteLLM gateway)

## Composants visuels suggérés

- **Section 1.2** : schéma SVG du cycle « prompt → eval → improve »
- **Section 3** : tableau comparatif des 3 types d'evals en `.tool-table`
- **Section 4** : 2 `.tool-table` côte-à-côte (open-source / SaaS)
- **Section 5.2** : schéma SVG du workflow CI/CD
- **Section 7** : `.timeline-block` pour le plan d'action 30 jours

## Note Cowork
Sources prioritaires : LangChain 2026, Avi Chawla, Anthropic Engineering, Phoenix Arize. Pas de RetEx PME française institutionnel public trouvé sur ce sujet précis (signalé honnêtement). Conforme RULES § 1.1.
