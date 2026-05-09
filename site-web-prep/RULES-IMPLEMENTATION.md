# Règles d'implémentation — Hub IA Learning Center

**Version :** 1.1 (mai 2026)
**Statut :** Référentiel non négociable
**Public :** Claude Code, contributeurs au repo, futurs LLM intervenant sur le site

> Ce fichier est le **référentiel ultime** des règles d'implémentation du Hub IA. Tout ce qui n'y est pas n'est pas une règle ; tout ce qui y est doit être respecté à la lettre. Toute PR qui contredit ce fichier doit être amendée avant merge.

---

## 0. Préambule — pourquoi ce fichier existe

Le Hub IA est un site pédagogique destiné à des **dirigeants PME/ETI non-IT** du Grand Est. Trois propriétés en font un outil utile : (i) il dit la vérité (sourcing rigoureux, pas d'hallucination), (ii) il parle leur langue (pas de jargon technique non explicité), (iii) il est cohérent (les chiffres et la nav sont synchronisés partout). Sans ces trois propriétés, c'est juste un blog de plus.

Les LLM (Claude Code, Cowork, autres) ont tendance à dériver sur ces trois axes au fil des itérations — d'où ce fichier.

---

## 1. Règles non négociables — 4 dimensions

### 1.1 Sourcing & véracité

**Règle 1.1.1** — Aucune affirmation chiffrée sans source datée, vérifiable, et publique. Format obligatoire : *« 95 % des projets GenAI échouent (étude MIT Sloan / NANDA, août 2025) »*. Pas de chiffre orphelin.

**Règle 1.1.2** — Aucune statistique inventée, aucune extrapolation présentée comme fait. Si la donnée n'existe pas, on ne l'écrit pas. Préférer une qualification prudente (« la majorité des PME observent… ») à un chiffre fabriqué.

**Règle 1.1.3** — Sources prioritaires : Bpifrance Le Lab, France Num, INSEE, Pôle emploi, McKinsey, MIT Sloan, Microsoft Work Trend, PwC, OECD, études institutionnelles FR/UE. Sources à éviter : blogs marketing d'éditeurs, contenus sponsorisés, posts LinkedIn anecdotiques, IA ayant cité une source sans lien vérifiable.

**Règle 1.1.4** — Toute citation directe de personne (dirigeant, expert) doit être publique et vérifiable. Pas de témoignage fictif, même pour illustrer.

**Règle 1.1.5** — Les RetEx d'entreprises ne sont nommables que si la source est institutionnelle et publique (Bpifrance Le Lab, presse économique reconnue). Les cas remontés par cabinets de conseil sont **anonymisés** (présentés comme « pattern »).

### 1.2 Cohérence numérique cross-site

**Règle 1.2.1** — Chaque chiffre structurel du site (« 22 modules », « 6 préalables », « 76 fiches outils », nombre d'axes, etc.) doit être identique sur **toutes** les pages où il apparaît. Si un de ces nombres bouge, **tous** doivent bouger en même temps dans le même commit.

**Règle 1.2.2** — Avant tout commit qui ajoute/retire un module, un préalable ou une fiche outil, exécuter une recherche cross-site sur l'ancien nombre et lister tous les hits à mettre à jour. Liste minimale à vérifier : `index.html` (meta, hero stats, filter count haut + bas, section À propos), `prealables.html` (meta, accroche, footer-cta), `architectures.html`, `ressources.html` (badge V·outils·catégories, accroche synthèse, exec-stats, intitulés des sections), `README.md`, footers de tous les modules CU et PR, méta-descriptions de toutes les pages.

**Règle 1.2.3** — Glossaire des chiffres-clés à maintenir cohérent (à actualiser à chaque itération) :

| Chiffre | Valeur courante (mai 2026, v3.6) | Lieux d'apparition |
|---|---|---|
| Nombre de modules CU | 25 (CU-001 → CU-024 + CU-027 ; CU-025 et CU-026 réservés v3.7) | home, page modules, à propos, méta |
| Nombre de préalables PR | 7 (PR-01 → PR-07) | prealables.html, home, à propos |
| Nombre de fiches outils | 83 | ressources.html, à propos, hero ressources |
| Nombre de patterns d'architecture | 4 + 1 hybride | architectures.html, à propos |
| Nombre d'entrées nav | 5 (Préalables / Architectures / Modules / Ressources / À propos) | toutes pages |
| Nombre de familles métier (modules) | 6 (Découverte / Marketing &amp; croissance / Décision &amp; gouvernance / Fonctions support / Industrie / Architectures agentiques avancées) | home |
| Échelle complexité | 4 niveaux (⭐ Initiation / ⭐⭐ Opérationnel / ⭐⭐⭐ Avancé / ⭐⭐⭐⭐ Expert) | home (filtre), badges modules |

**Règle 1.2.4** — Les statistiques macro (95 % MIT NANDA, +270 % Microsoft / Sigma, 76 % France Num, ×5 productivité PwC, 77 000 offres PwC, 3,7× IDC Copilot, consensus 70-95 % Gartner / McKinsey / Deloitte) sont synchronisées sur leurs lieux d'apparition (home + PR-01 + PR-02 + PR-04). Toute modification d'un chiffre macro déclenche une vérification cross-pages.

**Règle 1.2.5** — **Cohérence intra-page des chiffres affichés**. Sur une même page, les chiffres déclarés doivent être cohérents entre eux. Ex : si l'accroche dit « catalogue étendu à 83 fiches en 14 catégories », la grille de stats juste en dessous ne peut pas afficher « 76 Deep-dives · 90+ Outils indexés · 13 Catégories ». Toute stat affichée doit être identique aux comptages réels (vérifier par grep le nombre d'éléments avant de figer une stat).

**Règle 1.2.6** — **Pas de versioning interne sur le front**. Les mentions « V3.5 », « v3.6 », « itération v3.x » sont des conventions internes (commits, briefs, RULES). Elles **ne doivent jamais apparaître côté UX visible** (badges, accroches, descriptions). Le site est un produit publié, pas un changelog. Pour signaler une nouveauté côté front, préférer une formulation neutre : « catégorie récente », « nouveauté 2026 », ou pas de marqueur du tout. Le versioning reste dans `git log` et dans les briefs internes.

### 1.3 Niveau de langue & terminologie

**Règle 1.3.1** — Public cible : dirigeant PME/ETI **non-IT**, profil 40-65 ans, formation gestion ou technique métier. Vocabulaire de référence : celui qu'on entend dans une CCI ou une chambre de métiers, pas dans une conférence DevOps.

**Règle 1.3.2** — Aucun jargon technique sans glose explicite à la première occurrence dans une page. Liste indicative de termes à expliciter (non exhaustive) :

| Terme | Glose obligatoire la 1re fois |
|---|---|
| RAG | « Retrieval-Augmented Generation : un agent IA qui consulte ta documentation interne avant de répondre » |
| MVP | « Minimum Viable Product : la version la plus simple d'un produit qu'on peut déjà mettre dans les mains d'un client » |
| POC | « Proof of Concept : prototype pour valider une faisabilité avant d'industrialiser » |
| Fine-tuning | « ajustement d'un modèle IA sur tes propres données » |
| Embeddings | « représentation numérique d'un texte que l'IA peut comparer » |
| Prompt | « instruction donnée à l'IA en langage naturel » |
| Token | « unité de texte traitée par l'IA, ~3-4 caractères en moyenne » |
| LLM | « Large Language Model : modèle d'IA générative type ChatGPT, Claude, Gemini » |
| API | « interface de programmation qui permet à un logiciel d'en appeler un autre » |
| SaaS | « Software as a Service : logiciel hébergé chez l'éditeur, accessible par navigateur » |
| Cloud souverain | « hébergement cloud opéré sous juridiction européenne, certifié SecNumCloud le cas échéant » |
| Open-source | « logiciel dont le code source est public et modifiable » |
| On-premise | « hébergement sur tes propres serveurs, dans ton infrastructure » |

**Règle 1.3.3** — Privilégier les termes français quand ils existent (« veille concurrentielle » plutôt que « competitive intelligence », « tableau de bord » plutôt que « dashboard »). Anglicismes acceptés : ceux entrés dans le langage courant gestion (ROI, KPI, scaling, pipeline commercial).

**Règle 1.3.4** — Phrases courtes en moyenne (15-25 mots). Pas de paragraphes de plus de 6 lignes. Pas de subordonnées en cascade.

**Règle 1.3.5** — Les acronymes propres au réseau QFC / Quai Alpha (SUM, PM, Starter Class, Comité d'Engagement) sont à utiliser avec parcimonie sur le site public — il ne s'adresse pas aux porteurs de l'écosystème mais à des dirigeants externes.

**Règle 1.3.6** — Pas de jargon de référencement éditorial visible côté UX. Les codes internes (`PR-01`, `CU-007`) **ne doivent pas apparaître dans les titres, cards, badges ou corps de texte visibles** (ils peuvent rester dans l'URL et les ancres). Seul le titre métier est visible en surface.

**Exception** : les codes `A1 / A2 / A3 / A4` sont les noms canoniques des patterns d'architecture (validés v3.5). Ils restent visibles sur `architectures.html` et dans les encarts d'architectures recommandées des modules sensibles. Cette exception ne s'étend à aucun autre code interne.

**Règle 1.3.7** — **Pas d'introduction de nomenclatures internes non explicitées sur le front**. Toute échelle, codification ou taxonomie nouvelle visible côté UX doit être :
- soit alignée sur les classifications existantes du site (ex : échelle de complexité ⭐ à ⭐⭐⭐⭐ déjà déployée sur les modules) ;
- soit accompagnée d'une glose immédiate.

Anti-exemple historique : le bloc « Maturité opérationnelle — N1-N3 quiz / N4-N6 pilote / N7-N8 mise à l'échelle » sur `ressources.html` (jargon non explicité, hors scope outils, désaligné de l'échelle ⭐ à ⭐⭐⭐⭐ utilisée sur les modules). Retiré en v3.6.

**Règle 1.3.8** — **Toute légende de badge / nomenclature affichée doit refléter ce qui est réellement utilisé sur la page**. Si la légende décrit des badges « N1-N3 / N4-N6 / N7-N8 » mais que les fiches outils affichent des badges « Établi / Émergent / Early access », il y a incohérence à corriger.

### 1.4 Harmonisation visuelle cross-pages

**Règle 1.4.1** — La nav principale est **identique sur toutes les pages**, dans le même ordre, avec les mêmes libellés. Toute évolution de la nav se propage simultanément sur toutes les pages dans le même commit.

**Règle 1.4.2** — Le head banner (logo, titre, accroche) suit le même gabarit sur toutes les pages : même hauteur, même typo, même padding, même comportement sticky.

**Règle 1.4.3** — Le footer est identique partout : crédits Quai Alpha / Quest for Change, mention année, lien repo GitHub, lien méthodologie, lien à propos.

**Règle 1.4.4** — Les composants CSS structurants sont mutualisés dans `module-v3.css`. Les composants spécifiques à une page peuvent rester inline si utilisés à un seul endroit ; sinon, factorisation obligatoire.

**Règle 1.4.5** — Le pattern executive summary (gradient bleu marine + 4 takeaways + stats grid + callout « when ») est **obligatoire** en tête de chaque module CU et préalable PR. Pas d'exception.

**Règle 1.4.6** — La sticky TOC + scroll-spy + reading progress bar sont actifs sur tous les modules CU, tous les PR, et la page Architectures. Si un de ces composants ne fonctionne pas sur une page, c'est un bug bloquant.

---

## 2. Checklist obligatoire avant tout commit / PR

À exécuter **avant** push. Une PR qui n'a pas validé cette checklist doit être amendée.

```
☐ J'ai lu RULES-IMPLEMENTATION.md en intégralité avant de commencer.

☐ Sourcing : tous mes nouveaux chiffres ont une source datée et vérifiable.
☐ Sourcing : aucune statistique inventée, aucune citation fictive.

☐ Cohérence numérique : si j'ai modifié le nombre de modules / préalables / outils,
  j'ai mis à jour TOUS les lieux listés en règle 1.2.2 dans le même commit.
☐ Cohérence numérique : grep cross-site exécuté sur les chiffres impactés.

☐ Niveau de langue : aucun nouveau terme technique sans glose à sa 1re occurrence.
☐ Niveau de langue : pas de PR-XX / CU-XX / A1-A4 visible dans les titres ou cards.

☐ Harmonisation : nav identique sur toutes les pages touchées.
☐ Harmonisation : head banner et footer identiques.
☐ Harmonisation : sticky TOC + scroll-spy + progress bar fonctionnels sur les pages avec contenu long.

☐ Tests croisés : Chrome / Firefox / Safari, mobile + desktop.
☐ Liens : aucun lien mort, tous les liens cross-pages fonctionnent.

☐ Description PR : pointe vers le brief de l'itération + résume les écarts au RULES s'il y en a (et pourquoi).
```

---

## 3. Pattern de sourcing — exemples

### Bon exemple

> **+270 % de ROI moyen** sur les déploiements IA générative en entreprise (*Microsoft New Future of Work Report 2025*, données 2024 sur 1 200 organisations).

### Mauvais exemple (à proscrire)

> Les études montrent que l'IA permet d'augmenter la productivité de manière significative.

### Format en HTML

```html
<p><strong>+270 % de ROI moyen</strong> sur les déploiements IA générative
(<a href="https://aka.ms/AINewFutureOfWork" target="_blank" rel="noopener">
Microsoft New Future of Work Report 2025</a>).</p>
```

Toujours un `<a>` cliquable vers la source. Si la source n'a pas d'URL publique stable, citer la référence complète (titre + auteur + date + éditeur).

---

## 4. Pattern de glose terminologique — exemples

### Bon exemple

> Un agent **RAG** (Retrieval-Augmented Generation : un assistant IA qui consulte d'abord ta documentation interne avant de formuler sa réponse) permet de répondre aux questions techniques de tes équipes en s'appuyant sur tes manuels, procédures et historiques projets.

### Mauvais exemple (à proscrire)

> Le RAG permet d'augmenter la pertinence des LLM sur des verticales métier en réduisant les hallucinations.

(Trois termes techniques non explicités en une phrase = lecteur perdu)

---

## 5. Pattern d'harmonisation numérique

### Scénario : ajout d'un module CU-023

Avant push, exécuter :

```bash
# Lister tous les hits "22 modules" (à mettre à jour vers "23 modules")
grep -rn "22 modules" .
grep -rn "22 cas d'usage" .
grep -rn "CU-001 → CU-022" .
grep -rn "CU-001 à CU-022" .

# Vérifier que la mise à jour est cohérente
grep -rn "23 modules" .
grep -rn "23 cas d'usage" .
grep -rn "CU-001 → CU-023" .
```

Tous les hits anciens doivent avoir disparu, tous les nouveaux doivent être présents. Sinon, le commit n'est pas prêt.

---

## 6. Décisions éditoriales structurantes (rappel)

- **Pas de pub pour acteurs commerciaux** : pas de fiches sur cabinets de conseil, intégrateurs, agences. Les RetEx mentionnent les cas, pas les prestataires intermédiaires.
- **Distinction CU / PR / Architectures** : voir brief v3.4 et v3.5 pour le détail. Ne pas mélanger.
- **Pas de reframing géographique** : le site reste calibré PME/ETI Grand Est, pas national, pas international.
- **Pas de refonte du design system** sans validation explicite Blaise.
- **Pas d'ajout de catégorie d'outils** sans validation explicite Blaise.

---

## 7. Évolution de ce fichier

Ce fichier est **vivant**. À chaque itération majeure (v3.6, v3.7, etc.), Cowork (côté Blaise) ou Claude Code peut proposer des amendements via PR dédiée. Toute évolution doit faire l'objet d'une discussion explicite avec Blaise avant merge.

Versionnage : on incrémente la version en tête de fichier (1.0 → 1.1 → 2.0 selon ampleur).

---

## 8. Contact & responsabilité

Maintainer du référentiel : Blaise Cavalli — blaise.cavalli@questforchange.eu

Historique :
- **v1.0** — 9 mai 2026 : création.
- **v1.1** — mai 2026, en complément de l'audit v3.5.3 et de l'itération v3.6 :
  - Glossaire chiffres-clés (§ 1.2.3) actualisé : 25 modules / 7 préalables / 83 fiches / 5 entrées de nav (sans Axes) / 6 familles métier / échelle 4 étoiles.
  - § 1.2.2 : liste des lieux d'apparition cross-site précisée (badge ressources, exec-stats, README, etc.).
  - § 1.2.5 ajoutée : cohérence intra-page des chiffres affichés (anti-pattern : 76 deep-dives vs 83 fiches sur la même page).
  - § 1.2.6 ajoutée : pas de versioning interne (V3.5, v3.6) sur le front.
  - § 1.3.6 : exception A1-A4 formalisée (validée v3.5).
  - § 1.3.7 ajoutée : pas d'introduction de nomenclatures internes non explicitées (anti-pattern : N1-N3/N4-N6/N7-N8).
  - § 1.3.8 ajoutée : cohérence légende ↔ badges réellement utilisés.
  - § 1.2.4 : suppression de la mention « 94 % AdvisoryX » (étude retirée v3.4) ; ajout du consensus 70-95 % et du 3,7× IDC.

**Si tu lis ce fichier en tant que LLM / agent : ton rôle est de t'y conformer, pas de l'interpréter. En cas de doute, demande à Blaise avant de commit.**
