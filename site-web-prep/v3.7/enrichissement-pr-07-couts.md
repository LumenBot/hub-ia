# Enrichissement PR-07 — Chiffres compression coûts MIT NANDA

**Module cible** : `prealables/pr-07-build-vs-buy.html`
**Type** : Patch éditorial (mise à jour chiffres + ajout encart)
**Volume** : ~250 mots à intégrer

---

## Position de l'enrichissement

Compléter la section actuelle « 95 % d'échec MIT NANDA » avec les **chiffres précis du Build vs Buy** et un encart sur la **compression des coûts du build IA-assisté en 2026**.

## Contenu à intégrer

### 1. Chiffres précis Build vs Buy (à intégrer dans la section décision)

**MIT NANDA — State of AI in Business 2025** (août 2025, étude sur 30-40 milliards $ investis, 153 leaders sondés, 300 déploiements analysés) :

> Les stratégies **Buy + partenariat** réussissent dans **~67 % des cas**. Les stratégies **Build interne** réussissent dans **~33 % des cas seulement**. Soit un **rapport 2:1** en faveur du Buy.

Ce chiffre doit être affiché en bonne place comme **stat-block** ou **callout** dans la section décision.

### 2. Encart sur la compression des coûts du build (nouveau)

> **La compression des coûts du build IA-assisté en 2026**
>
> Le coût d'un build IA-assisté a été divisé par 3 à 5 entre 2023 et 2026, sans compromis sur la qualité finale, grâce à 3 facteurs :
>
> - **Modèles open-source compétitifs** : Kimi K2.6 (sortie 2026) propose ~75 % de la qualité de Claude Opus 4.7 pour 10 % du coût d'inférence.
> - **Frameworks d'agents matures** : ECC (Everything Claude Code) avec 38 agents spécialisés + AgentShield = équivalent d'une équipe de 3-4 devs juniors pour ~$20-200/mois.
> - **Patterns Fat Skills / Thin Harness** (Garry Tan) : architecture compounding où chaque skill réutilisable réduit le coût de la suivante.
>
> Conséquence : le **seuil de rentabilité du Build s'est abaissé** par rapport à 2023. Le « Buy » reste statistiquement supérieur (67 % vs 33 % de réussite), mais les cas où le Build est justifié deviennent plus accessibles aux PME ambitieuses.

### 3. Mise à jour de la matrice de décision

Dans la matrice Build vs Buy existante, ajouter une **5e ligne** :

| Critère | Build justifié si... |
|---|---|
| Volume mensuel élevé | > 5 M tokens/mois récurrents (cf. [DEP-06](../deploiement/dep-06-inference-saas-self-hosted.html)) |
| Souveraineté critique | Données ultra-sensibles, secret industriel |
| Différenciation compétitive | Le système IA fait ton avantage durable |
| **NEW : Compétences IA-natives accessibles** | Tu as un dev senior + Cursor + Kimi K2.6 + ECC stack |
| **NEW : Coût d'inférence Opus prohibitif** | Tu peux switcher 75 % du volume vers Kimi sans perte |

## Sources à ajouter dans la section finale (Schéma A)

À insérer dans la sous-rubrique « 📚 Documentation officielle & études » :
- [MIT NANDA — State of AI in Business 2025 (synthèse)](https://www.aigl.blog/state-of-ai-in-business-2025/) — Chiffres 67 % vs 33 %
- [Together.ai — Kimi K2.6 économie](https://www.together.ai/) — Analyse coût comparé
- [Garry Tan — Personal AI compounding](https://x.com/garrytan) — Patterns architecture

## Renvois internes à ajouter

- Vers [DEP-01 Cadrer un projet IA](../deploiement/dep-01-cadrer-projet-prod.html)
- Vers [DEP-06 Inférence SaaS vs self-hosted](../deploiement/dep-06-inference-saas-self-hosted.html)
- Vers [CU-027 Faire développer une appli métier](../modules/cu-027-dev-applicatif-ia.html) (déjà présent, vérifier)

## Note Cowork
Patch léger qui actualise les chiffres MIT NANDA avec précision (67 % / 33 %) et ajoute la dimension compression coûts 2026. Préserve la structure éditoriale existante de PR-07.
