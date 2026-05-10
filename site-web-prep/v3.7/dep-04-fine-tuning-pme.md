# DEP-04 — Fine-tuning : quand y aller, quand ne pas

**Public cible :** dirigeant qui pilote un projet IA + équipe technique tentée par le fine-tuning

---

## Métadonnées (pour Claude Code)

- **Section** : Déploiement
- **Niveau** : ⭐⭐⭐ Avancé
- **Type** : Cadrage stratégique
- **Durée lecture** : 15 min
- **Emoji h1** : 🎓
- **Titre métier visible** : « Fine-tuning : quand y aller, quand ne pas »
- **Sous-titre hero** : Le fine-tuning est devenu accessible (LoRA / QLoRA sur 1 GPU). Mais pour 80 % des cas PME, un bon prompt + RAG suffit largement. Voici quand le fine-tuning est vraiment justifié.
- **Card index promesse** : « Cadrage stratégique »

## Synthèse exécutive

### Pourquoi cette page ?

Le fine-tuning (ajustement d'un modèle IA sur tes propres données) est devenu **techniquement accessible** depuis 2023 grâce aux techniques LoRA et QLoRA qui permettent d'entraîner un modèle sur **un seul GPU**. La promesse est séduisante : un modèle « qui parle ton métier ». La réalité est plus nuancée. **Pour 80 % des cas d'usage PME, le fine-tuning n'est pas la bonne réponse** — un bon prompt engineering + un RAG bien conçu (cf. [DEP-02](dep-02-rag-architecture-prod.html)) couvrent l'essentiel des besoins, à un coût et un délai bien moindres.

Cette fiche te donne le cadre de décision : **quand le fine-tuning est justifié**, quand c'est un piège qui consomme du temps et du budget pour un gain marginal.

### 4 takeaways

1. **Pour 80 % des cas PME, le fine-tuning n'est pas la bonne réponse.** Avant de fine-tuner, demande-toi si un bon prompt + RAG couvre déjà 90 % du besoin. Dans la majorité des cas, oui. Le fine-tuning ne devient justifié que quand prompt + RAG plafonnent à < 80 % de qualité sur un cas d'usage critique.

2. **Le fine-tuning a 3 cas d'usage légitimes en PME.** (a) Adapter le **format de sortie** (générer toujours du JSON valide selon ton schéma propre), (b) capturer un **style/voix de marque** très spécifique (généralement difficile par prompt), (c) **réduire le coût d'inférence** (un petit modèle fine-tuné peut surpasser un gros modèle générique sur ton cas, à 10× moins cher).

3. **La qualité des données prime sur le volume.** Ce qui sépare un fine-tuning réussi d'un raté n'est pas la quantité de données mais leur qualité : annotations cohérentes, déduplication, instruction formatting propre, filtrage. **Sweet spot PME : 500 à 5 000 exemples bien préparés**, pas 100 000 mal préparés.

4. **LoRA / QLoRA = standard pratique 2026.** Plutôt que de fine-tuner les milliards de paramètres d'un modèle, on entraîne uniquement de petites matrices d'adaptation (LoRA = Low-Rank Adaptation). Coût typique : 50 à 500 € de GPU + 1-3 semaines de travail data + entraînement. Délai total raisonnable : 1-2 mois.

### Stats (3-4)

- **80 %** des cas PME ne nécessitent pas de fine-tuning (consensus pratique 2026 : prompt + RAG suffisent)
- **Sweet spot PME** : 500-5 000 exemples bien annotés (qualité > volume)
- **Coût LoRA/QLoRA** : 50-500 € de GPU pour fine-tuner un modèle 7B-13B sur tes données
- **1-3 % de perplexité** perdue avec quantization 4-bit après fine-tuning (ratio coût/qualité excellent)

### Quand cette page est utile

Tu as déployé un prompt engineering + RAG et tu **plafonnes à < 80 % de qualité** sur un cas d'usage critique. Tu veux savoir si le fine-tuning vaut l'investissement. Tu as un cas d'usage à très haut volume où l'inférence coûte cher. Tu cherches à capturer un style/voix difficile à transmettre par prompt.

## Section 1 — Le fine-tuning est-il vraiment nécessaire ?

### 1.1 La hiérarchie des leviers (avant de fine-tuner)

Avant de fine-tuner, parcourir cette hiérarchie dans l'ordre :

1. **Prompt engineering basique** : instructions claires, few-shot examples, format de sortie spécifié → 50-70 % de qualité atteinte gratuitement
2. **Prompt engineering avancé** : chain-of-thought, prompt caching (cf. [DEP-03](dep-03-context-engineering-couts.html)), structured output → +10-15 % qualité
3. **RAG** sur ta base de connaissance (cf. [DEP-02](dep-02-rag-architecture-prod.html)) → +10-20 % qualité sur cas où le contexte métier compte
4. **Fine-tuning** → +5-15 % qualité sur cas spécifiques

→ Si les étapes 1-3 atteignent 90 %, le fine-tuning n'apporte rien d'opérationnellement utile.

### 1.2 Le test du « 80 % qui suffit »

Pour beaucoup de cas d'usage PME, atteindre 80 % de qualité avec prompt + RAG est suffisant pour générer de la valeur. Le passage de 80 % à 92 % via fine-tuning :
- Coût : +50-500 € GPU + 1-2 mois de travail
- Gain : 12 % de qualité supplémentaire
- ROI : souvent négatif sur le court terme

**À mesurer sur ton cas avant de décider.**

## Section 2 — Les 3 cas où le fine-tuning est vraiment justifié

### 2.1 Format de sortie strict (le plus fréquent en PME)

Si tu as besoin de **toujours générer un format précis** (JSON conforme à ton schéma, XML métier, format de fichier propriétaire) avec **0 % d'erreur de format**, le fine-tuning est plus fiable que le prompt engineering.

**Exemple type** : génération automatique de fiches produit dans un schéma JSON spécifique pour ton ERP. Avec prompt = 95 % de format valide. Avec fine-tuning = 99,8 % de format valide. Sur 10 000 fiches/jour, la différence est significative.

### 2.2 Capture d'un style ou voix de marque très spécifique

Si tu produis du contenu (mails, articles, posts) qui doit avoir une **voix très spécifique** difficile à transmettre par prompt (humour particulier, ton sectoriel, vocabulaire métier), le fine-tuning capture ce style mieux qu'un prompt long.

**Exemple type** : un éditeur de contenus juridiques qui veut un ton « expert mais accessible », avec ses propres formules de transition. 200-500 articles annotés peuvent suffire.

### 2.3 Réduction du coût d'inférence

Pour un cas d'usage à **très haut volume** (millions de requêtes/mois), fine-tuner un petit modèle (7B-13B) peut **surpasser un gros modèle générique** sur ton cas spécifique, à un coût d'inférence 10× moindre.

**Exemple type** : classification automatique de tickets support (10 catégories métier). Un Mistral 7B fine-tuné peut atteindre 95 % de précision contre 92 % pour Claude Sonnet, à 10× moins cher en inférence.

## Section 3 — Les 5 cas où le fine-tuning n'est PAS la bonne réponse

À l'inverse, ces cas indiquent qu'il faut **rester sur prompt + RAG** :

1. **Tu veux que le modèle « connaisse » des informations métier**. C'est le rôle du RAG, pas du fine-tuning. Le fine-tuning n'apprend pas des faits, il apprend des patterns. Pour les faits → RAG.
2. **Les informations changent souvent.** Re-fine-tuner à chaque mise à jour est insoutenable. RAG réindexe en quelques minutes.
3. **Le besoin n'est pas encore stable.** Fine-tuner sur un besoin qui va évoluer = perte sèche.
4. **Tu n'as pas 500+ exemples de qualité.** En dessous, le risque d'overfitting est élevé pour un gain marginal.
5. **Tu n'as pas mesuré ton baseline prompt + RAG.** Sans baseline, impossible de justifier le ROI du fine-tuning.

## Section 4 — LoRA et QLoRA en pratique

### 4.1 Le principe (en 2 phrases)

**LoRA (Low-Rank Adaptation)** : au lieu d'entraîner les milliards de paramètres d'un modèle, on entraîne uniquement de **petites matrices d'adaptation** ajoutées au modèle. Résultat : on garde 99 % de la connaissance générale du modèle + on ajoute notre adaptation spécifique, sur **un seul GPU grand public**.

**QLoRA** : variante qui ajoute une quantization (compression 4-bit) du modèle de base, divisant encore par 4 la mémoire requise.

### 4.2 Coût et délai typiques pour une PME

Pour fine-tuner un Mistral 7B ou Llama 8B en LoRA sur tes données :
- **Préparation données** : 1-3 semaines (le plus long en PME)
- **Entraînement** : 2-12 heures sur une GPU A100/H100 (Vast.ai, Runpod, Lambda Labs)
- **Coût GPU** : 50-500 € total
- **Évaluation** : 1 semaine

**Délai total réaliste** : 1-2 mois calendaires.

### 4.3 Outils 2026

- **Unsloth** : framework open-source qui rend LoRA/QLoRA 2-5x plus rapide
- **Hugging Face PEFT** : bibliothèque officielle LoRA
- **Hugging Face TRL** : entraînement supervisé + RLHF
- **Axolotl** : framework wrapper pour fine-tuning à l'échelle
- **Together.ai, Modal Labs, Lambda Labs** : plateformes managed pour fine-tuning sans gérer l'infra

## Section 5 — La discipline data : le vrai sujet du fine-tuning

### 5.1 Qualité > Volume

Le fine-tuning échoue 9 fois sur 10 à cause des données, pas de la technique. Quatre disciplines essentielles :

1. **Annotations cohérentes** : si tu as 5 annotateurs, ils doivent avoir des guidelines strictes (kappa de Cohen > 0,7)
2. **Déduplication** : les doublons gonflent artificiellement le volume sans apporter de signal
3. **Instruction formatting propre** : format input/output strict (Alpaca, ShareGPT, ChatML)
4. **Filtrage** : enlever les exemples ambigus, contradictoires, ou mal annotés

### 5.2 Sweet spot PME

- **< 100 exemples** : fine-tuning généralement non viable, rester sur prompt
- **100-500 exemples** : viable pour cas très spécifiques (format strict)
- **500-5 000 exemples** : sweet spot PME — qualité optimale si bien préparés
- **5 000-50 000 exemples** : pour cas à fort enjeu, demande processus d'annotation industrialisé
- **> 50 000 exemples** : très rare en PME, généralement sur datasets synthétiques générés

## Section 6 — Plan d'action 60 jours pour décider

### Jours 1-15 — Mesure du baseline
- Définir le cas d'usage candidat au fine-tuning
- Construire un dataset golden de 100-200 cas test
- Mesurer la qualité actuelle prompt + RAG sur ce golden

### Jours 16-30 — Décision Go/No-Go fine-tuning
- Si baseline > 90 % : pas de fine-tuning, optimiser prompt
- Si baseline 80-90 % : analyser les erreurs, voir si patterns récurrents
- Si baseline < 80 % : fine-tuning probablement justifié, passer à la suite

### Jours 31-45 — Préparation des données
- Constituer 500-2 000 exemples annotés de qualité
- Format input/output strict
- Split train/validation/test (70/15/15)

### Jours 46-60 — Entraînement et évaluation
- LoRA/QLoRA sur Mistral 7B ou Llama 8B (selon licence)
- Évaluation sur le golden vs baseline prompt + RAG
- Décision déploiement si gain mesurable > 5 % qualité

## Section 7 — Pour aller plus loin (Schéma A)

### Callout d'aiguillage

> Pour le panorama complet des outils de fine-tuning et frameworks LLM, retrouve les fiches détaillées sur la [page Ressources du Hub](../ressources.html#bibliographie).

### 📰 Articles de fond
- [Avi Chawla — 5 must-know LLM fine-tuning techniques](https://blog.dailydoseofds.com/p/foundations-of-ai-engineering-and-0a6) — Pilier 4 LLM Engineering Roadmap
- [Hugging Face Blog — PEFT Methods](https://huggingface.co/blog/peft) — Référence pédagogique LoRA
- [Sebastian Raschka — Practical fine-tuning](https://magazine.sebastianraschka.com/) — Newsletter technique de référence

### 🎓 Tutoriels & cas pratiques
- [Unsloth Notebooks](https://github.com/unslothai/unsloth) — Notebooks Colab gratuits LoRA/QLoRA rapides
- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course) — Cours communautaire end-to-end
- [Sebastian Raschka — Build a LLM from scratch](https://github.com/rasbt/LLMs-from-scratch) — Repo référence pretraining + fine-tuning + LoRA

### 📚 Documentation officielle & études
- [Hugging Face PEFT Docs](https://huggingface.co/docs/peft) — Documentation officielle LoRA/QLoRA
- [Hugging Face TRL Docs](https://huggingface.co/docs/trl) — Supervised fine-tuning + RLHF
- [Axolotl GitHub](https://github.com/OpenAccess-AI-Collective/axolotl) — Framework wrapper

### 👥 Communautés & veille
- [Hugging Face Forum](https://discuss.huggingface.co/) — Communauté technique
- [r/LocalLLaMA](https://reddit.com/r/LocalLLaMA) — Communauté open-source LLM

## Renvois internes pour Claude Code

- **Section 1.1 (étape 2)** : lien `<a href="dep-03-context-engineering-couts.html">DEP-03 Context engineering et coûts</a>`
- **Section 1.1 (étape 3)** : lien `<a href="dep-02-rag-architecture-prod.html">DEP-02 RAG en production</a>`
- **Section corps** : si fiche Unsloth créée → lien `<a href="../ressources.html#unsloth">Unsloth</a>`

## Composants visuels suggérés

- **Section 1.1** : pyramide des leviers (prompt → RAG → fine-tuning) en SVG ou bloc visuel
- **Section 4.2** : `.stat-block` pour les 50-500 € GPU
- **Section 5.2** : tableau « volume vs viabilité » en `.tool-table`
- **Section 6** : `.timeline-block` pour le plan d'action 60 jours

## Note Cowork
Sources prioritaires : Avi Chawla, Hugging Face, Sebastian Raschka, Unsloth. Conforme RULES § 1.1. Public cible bien différencié de DEP-02 (RAG) et DEP-03 (Context).
