# Brief Claude Code — Hub IA Learning Center (passation v3.3)

**Auteur :** Blaise Cavalli — Startup Manager Quai Alpha (Quest for Change)
**Date :** mai 2026
**Repo :** https://github.com/LumenBot/hub-ia
**Branche cible :** main
**Hébergement :** GitHub Pages
**Itération précédente :** v3.2 (PR #14 — Lots A1, A2, A3, A5, A6 + bonus Hero)

---

## 0. Contexte court

Le Hub IA Learning Center continue son extension. Cette itération **v3.3** ajoute :
- **3 nouveaux modules pédagogiques** (CU-020 Conformité RGPD/AI Act, CU-021 Finance augmentée, CU-022 Voicebot accueil) → portant le total de 19 à **22 modules**
- **13 nouvelles fiches outils émergents** sur la page Ressources → portant le total de 63 à **76 fiches deep-dive**
- **1 nouvelle catégorie d'outils** dans le sommaire Ressources : « 🎙️ Voice & speech »
- **Cross-mises à jour** des modules existants (5 modules) avec liens vers les nouvelles fiches outils

**Préalable bloquant** : merger la PR #14 (v3.2) sur `feat/v3.1-corrections-globales` AVANT d'attaquer cette nouvelle itération (sauf si déjà fait — je n'ai pas la confirmation).

**Tous les fichiers sources de cette itération sont prêts dans `site-web-prep/` du repo** :
- `mockup/modules/cu-020-conformite-rgpd-ai-act.html` — module HTML V3 complet
- `mockup/modules/cu-021-finance-augmentee.html` — module HTML V3 complet
- `mockup/modules/cu-022-voicebot-accueil.html` — module HTML V3 complet
- `fiches-outils-phase3-mai2026.md` — matière éditoriale 13 fiches outils
- `revue-v3.1-mai2026.md` — note de revue critique (déjà majoritairement intégrée en v3.2, fournie ici pour contexte)

---

## 1. Lot 1 — Intégration des 3 nouveaux modules

### 1.1 Source

Les 3 modules sont **déjà au format V3 standard** (architecture mutualisée `module-v3.css` / `module-v3.js`, sticky TOC, executive summary, sections numérotées avec icônes, étude de cas / cas d'étude, auto-diagnostic ou checklist d'éligibilité, plan d'action exportable MD/TXT, footer normalisé).

### 1.2 Action

**Copier les 3 fichiers HTML** depuis `site-web-prep/mockup/modules/` vers `modules/` (racine du repo, là où sont les autres modules). Cohérence visuelle automatique grâce à l'architecture mutualisée. Aucune adaptation structurelle nécessaire.

### 1.3 Spécificités à signaler

#### CU-020 — Conformité RGPD & AI Act pour PME

- **Niveau** : N7-N8 (étude de cas + checklist d'éligibilité)
- **Axe** : B Décision (badge cliquable sur l'index)
- **Badge spécifique** : `⚖️ Conformité réglementaire` (à styler en rouge similaire à `card-warning` mais variant violet)
- **Bandeau spécifique** : `.alert-deadline` (rouge urgence — rappel deadline 2 août 2026, sanctions 7 % CA)
- **Composant CSS nouveau** : `.risk-matrix` (4 cartes colorées interdit/élevé/limité/minimal). À mutualiser dans `module-v3.css` car potentiellement réutilisable.
- **Étude de cas** : ManufactCo (ETI mécanique 80p Grand Est) — 4 mois, 23 usages cartographiés, ~31 K€ externes, conformité avant 2 août 2026

#### CU-021 — Finance & comptabilité augmentées

- **Niveau** : N4-N6 (auto-diagnostic + plan d'action)
- **Axe** : A Productivité + B Décision (double axe avec 2ᵉ en opacité 0.7)
- **Module fusionné** : couvre 4 sous-cas (extraction factures + rapprochement bancaire + prévision cash + détection anomalies)
- **Composant CSS nouveau** : `.usecase-grid` + `.usecase-card` (4 cartes cas d'usage avec ROI typique). Peut être mutualisé avec `.signals-grid` ou `.filieres-grid` existants.
- **Cas d'étude guidé** : PME services 35 salariés (calé sur RetEx France Num documenté), ROI 155 % la 1ʳᵉ année

#### CU-022 — Voicebot accueil téléphonique IA

- **Niveau** : N4-N6
- **Axe** : D Croissance
- **Composant CSS** : réutilise `.usecase-grid` / `.usecase-card` du CU-021 (à mutualiser une fois)
- **Cas d'étude guidé** : cabinet de kinésithérapie 6 praticiens, bilan 4 mois → ~110 K€ valeur cumulée 1ʳᵉ année pour 4,8 K€ setup + 3,4 K€/an récurrents
- **Stack documentée** : Vapi.ai, Cartesia, ElevenLabs Conv 2.0, Voxtral, Deepgram Nova-3

### 1.4 Liens placeholder à vérifier dans les 3 modules

Les 3 modules contiennent des `<a href="../ressources.html#xxx" class="tool-link">` vers les fiches outils. **Vérifier que les ancres correspondent à celles que tu vas créer en Lot 2** (notamment pour `#lucie`, `#pleias-rag`, `#voxtral`, `#cartesia`, `#elevenlabs`, `#vapi`, `#mistral-agents`).

---

## 2. Lot 2 — Page Ressources : 13 nouvelles fiches outils + nouvelle catégorie

### 2.1 Source

Matière éditoriale complète dans `site-web-prep/fiches-outils-phase3-mai2026.md`. Format identique aux 63 fiches existantes en v3.2 (structure `.tool-card` avec `.tool-card-header` / `.tool-body` / `.tool-grid` / `.tool-block`).

### 2.2 13 fiches à intégrer

| # | Outil | Catégorie cible | Souveraineté | Anchor suggérée |
|---|---|---|---|---|
| 1 | Lucie / OpenLLM-France | 🧠 LLM | 🇫🇷🇪🇺 | `#lucie` |
| 2 | Pleias-RAG | 🧠 LLM (SLM RAG) | 🇫🇷🇪🇺 | `#pleias-rag` |
| 3 | LightOn (Paradigm) | 🧠 LLM enterprise | 🇫🇷🇪🇺 | `#lighton` |
| 4 | Voxtral | 🎙️ **Voice & speech** | 🇫🇷🇪🇺 | `#voxtral` |
| 5 | Cartesia (Sonic / Line) | 🎙️ **Voice & speech** | 🇺🇸 | `#cartesia` |
| 6 | ElevenLabs Conv 2.0 | 🎙️ **Voice & speech** | 🇺🇸 | `#elevenlabs` |
| 7 | Vapi.ai | 🎙️ **Voice & speech** | 🇺🇸 | `#vapi` |
| 8 | Mistral Agents SDK | 🤖 Multi-agents | 🇫🇷🇪🇺 | `#mistral-agents` |
| 9 | Anthropic Computer Use | 🤖 Multi-agents | 🇺🇸 | `#computer-use` |
| 10 | MCP (Model Context Protocol) | 🤖 Multi-agents (standard) | 🌍 | `#mcp` |
| 11 | A2A (Agent2Agent) | 🤖 Multi-agents (standard) | 🇺🇸 (ouvert) | `#a2a` |
| 12 | Florence-2 | 👁️ Vision | 🇺🇸 | `#florence-2` |
| 13 | SAM 2 | 👁️ Vision | 🇺🇸 | `#sam-2` |

### 2.3 Nouvelle catégorie 17 — « 🎙️ Voice & speech »

À créer dans le sommaire Ressources, **entre les catégories existantes** (la position naturelle est entre « 📨 Email & scraping » et « 👁️ Vision industrielle » selon la logique technique du pipeline). Contiendra initialement les 4 fiches Voxtral / Cartesia / ElevenLabs / Vapi.

**Logique extension future** (Lot 3+ optionnel) : Deepgram, AssemblyAI, Whisper (déplacement depuis Productivité), NVIDIA Parakeet, Speechmatics. Mais **pas dans cette itération**.

### 2.4 Application des 6 dimensions de badges

Toutes les fiches sont livrées avec les **6 dimensions de badges** documentées dans le MD source :
1. **Type** (SaaS / Open-source / Open-weight / Hybride / Standard)
2. **Catégorie d'usage** (LLM / Voice / Agents / Vision / etc.)
3. **Maturité** (N1-N3 / N4-N6 / N7-N8)
4. **Souveraineté** (🇪🇺 / 🇫🇷🇪🇺 / 🇺🇸 / 🌍)
5. **Coût d'entrée** (🟢 Gratuit / 🟡 Freemium / 🟠 Payant / 🔴 Entreprise)
6. **Complexité de mise en œuvre** (🛠️ Plug-and-play / 🛠️🛠️ Setup léger / 🛠️🛠️🛠️ Intégration / 🛠️🛠️🛠️🛠️ Projet)

### 2.5 Renforcement souveraineté

**6 nouvelles fiches 🇫🇷🇪🇺** (Lucie, Pleias-RAG, LightOn, Voxtral, Mistral Agents) → total souverains badgés passe de 12 à **18 fiches**. À mettre en avant dans la légende des badges et la synthèse de la page Ressources.

---

## 3. Lot 3 — Cross-mises à jour des modules existants

### 3.1 Modules à mettre à jour avec liens `tool-link` vers les nouvelles fiches

| Module existant | Nouvelles fiches à lier |
|---|---|
| **CU-008 Knowledge base RAG** | Lucie, Pleias-RAG (RAG souverain) |
| **CU-014 Multi-agents par fonction métier** | Mistral Agents SDK, Anthropic Computer Use, MCP, A2A |
| **CU-015 Stripe Minions / agents codeurs** | Mistral Agents SDK, Anthropic Computer Use, MCP |
| **CU-017 Contrôle qualité par vision IA** | Florence-2, SAM 2 |
| **CU-018 Optimisation production / nesting** | Florence-2, SAM 2 |

**Format suggéré** : remplacer les mentions `<strong>Outil</strong>` par `<a href="../ressources.html#anchor" class="tool-link">Outil</a>` dans les sections Stack & outils des modules concernés. Conserver le `<strong>` ailleurs (mises en avant éditoriales).

### 3.2 Mise à jour annexe — CU-014, CU-015 (mention MCP / A2A)

Le debrief Claude Code v3.1 mentionnait que CU-014 et CU-015 méritaient un **update mineur pour mentionner les standards MCP et A2A**. C'est l'occasion de l'intégrer dans cette itération : ajouter 1-2 paragraphes dans la section « Stack & outils » de chaque module pour mentionner ces standards.

---

## 4. Lot 4 — Mises à jour structurelles

### 4.1 Index (page d'accueil)

- **Compteur de modules** : passer de « 19 modules » à « 22 modules » dans le hero
- **Ajout de 3 nouvelles cartes module** sur la grille des modules :
  - CU-020 (axe-b Décision · n3 · ⚖️ Conformité réglementaire) → position naturelle : rubrique « Décision », à côté ou avant CU-007 (RH AI Act)
  - CU-021 (axe-a Productivité + axe-b Décision · n2) → rubrique « Productivité » ou « Décision » selon ton choix éditorial
  - CU-022 (axe-d Croissance · n2) → rubrique « Croissance », à côté de CU-006 (chatbot leads)

### 4.2 Page Ressources

- **Compteur fiches outils** : passer de 63 à 76 dans la synthèse
- **Compteur catégories** : passer de 16 à 17 (avec ajout « 🎙️ Voice & speech »)
- **Compteur souverains EU** : passer de 12 à 18 dans la légende badges et synthèse

### 4.3 Navigation et footer

Aucun changement structurel sur la nav (déjà à 4 entrées : Modules, Ressources, Axes, À propos). Footer reste inchangé. Email contact reste `blaise.cavalli@questforchange.eu`.

### 4.4 Page À propos (encart « QFC en chiffres » de la v3.2)

L'encart « Réseau QFC en chiffres » créé en v3.2 mentionne probablement les chiffres globaux du réseau. À ré-évaluer avec Blaise si une mise à jour est nécessaire (pas dans cette itération).

---

## 5. Notes additionnelles

### 5.1 Composants CSS à mutualiser

Plusieurs composants apparaissent dans les modules livrés et mériteraient d'être consolidés dans `module-v3.css` plutôt que dupliqués :
- `.risk-matrix` (CU-020) — réutilisable pour matrices de classification (déjà partiellement présente avec `.eligibility-section.bloquant` et autres)
- `.usecase-grid` / `.usecase-card` (CU-021, CU-022) — duplique partiellement `.signals-grid` (CU-011), `.filieres-grid` (CU-017), `.axes-grid` (CU-018), `.agents-grid` (CU-014). **Idée pour v3.4** : refondre tous ces composants en un seul `.cards-grid` paramétrable. Pas dans cette itération.
- `.alert-deadline` (CU-020) — variante de `.alert-ai-act` existante. À factoriser ensemble.

### 5.2 Vérifications post-déploiement

Une fois la PR de cette itération mergée, vérifier sur le site live :
- Les 3 nouveaux modules s'affichent correctement avec architecture V3 (sticky TOC, exec summary, etc.)
- Les liens `../ressources.html#xxx` depuis les modules pointent bien vers les nouvelles fiches
- Le sommaire de la page Ressources affiche bien les 17 catégories
- Les badges souveraineté EU s'affichent correctement sur les 18 fiches concernées

### 5.3 Décisions explicites de NE PAS faire dans cette itération

- **Pas de nouveaux modules** au-delà des 3 livrés
- **Pas d'extension de la page Ressources** au-delà des 13 fiches livrées (les outils du Lot 3+ comme Deepgram, Phi-4, etc. attendront une prochaine itération)
- **Pas de refonte du système de cards** (suggestion v3.4 mentionnée plus haut)
- **Pas de modification du reframing géographique** (validé en v3.1 + v3.2)

---

## 6. Estimation effort Claude Code

| Lot | Sujet | Effort estimé |
|---|---|---|
| Lot 1 | Intégration 3 modules HTML | 2-3 h (copie + ajustements visuels mineurs + tests) |
| Lot 2 | 13 fiches outils + nouvelle catégorie | 5-7 h (HTML structuré, badges, ancrages) |
| Lot 3 | Cross-mises à jour 5 modules existants | 2-3 h (find-replace + paragraphes annexes pour CU-014/015) |
| Lot 4 | Index + compteurs + navigation | 1-2 h |
| **Total** | | **10-15 h** |

---

## 7. Workflow recommandé

1. **Vérifier que la PR #14 (v3.2) est bien mergée** sur main avant de commencer
2. **Créer une branche `feat/v3.3-cu-020-021-022-fiches-outils`**
3. **Lot 1 d'abord** (3 modules) pour livrable intermédiaire visible
4. **Lot 2 ensuite** (Ressources) — gros morceau, à tester en preview GitHub Pages
5. **Lot 3 et 4** en parallèle (cross-mises à jour + structurel)
6. **Tests croisés** sur Chrome/Firefox/Safari, mobile + desktop
7. **PR avec description structurée** pointant vers ce brief pour traçabilité

---

## 8. Fichiers de référence

- **Brief de cette itération** : `site-web-prep/BRIEF-CLAUDE-CODE-v3.3-passation.md` (ce fichier)
- **Modules à intégrer** : `site-web-prep/mockup/modules/cu-020-*.html`, `cu-021-*.html`, `cu-022-*.html`
- **Matière fiches outils** : `site-web-prep/fiches-outils-phase3-mai2026.md`
- **Note de revue v3.1** (référence) : `site-web-prep/revue-v3.1-mai2026.md`

---

## 9. Notes de positionnement éditorial

- **Ton du Hub IA Learning Center** : pragmatique, opérationnel, direct. Vocabulaire QFC respecté quand pertinent.
- **Public cible** : SUMs et PMs des incubateurs Quest for Change, startups accompagnées et alumni, PME et ETI du Grand Est et au-delà, partenaires institutionnels.
- **Avantage différenciant** : ancrage QFC + souveraineté EU + accompagnement pédagogique progressif (3 niveaux N1-N3 / N4-N6 / N7-N8).

---

## 10. Contact

Pour toute question pendant l'intégration : Blaise Cavalli — blaise.cavalli@questforchange.eu

**Bonne mission, et merci pour le travail !**

---

*Brief produit par Cowork (Claude desktop) le 8 mai 2026. Cette itération v3.3 fait suite à la v3.2 livrée par Claude Code (PR #14).*
