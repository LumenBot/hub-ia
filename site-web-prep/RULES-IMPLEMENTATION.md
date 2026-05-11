# Règles d'implémentation — Hub IA Learning Center

**Version :** 1.5 (mai 2026)
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

| Chiffre | Valeur courante (mai 2026, v3.7) | Lieux d'apparition |
|---|---|---|
| Nombre de modules CU | 26 (CU-001 → CU-025 + CU-027 ; CU-026 réservé v3.8) | home, page modules, à propos, méta |
| Nombre de préalables PR | 7 (PR-01 → PR-07) | prealables.html, home, à propos |
| Nombre de fiches Déploiement DEP | 8 (DEP-01 → DEP-08, nouvelle section v3.7) | deploiement.html, home, à propos |
| Nombre de fiches outils | 95 (83 + 12 nouvelles + 2 mises à jour v3.7) | ressources.html, à propos, hero ressources |
| Nombre de patterns d'architecture | 4 + 1 hybride | architectures.html, à propos |
| Nombre d'entrées nav | 5 (Préalables / Architectures / Modules / Déploiement / Ressources) — ordre depuis v3.7.1 ; « À propos » retiré du navbar (la section reste accessible via le footer ou par scroll de la home) | toutes pages |
| Nombre de familles métier (modules) | 6 (Découverte / Marketing &amp; croissance / Décision &amp; gouvernance / Fonctions support / Industrie / Architectures agentiques avancées) | home |
| Échelle complexité | 4 niveaux (⭐ Initiation / ⭐⭐ Opérationnel / ⭐⭐⭐ Avancé / ⭐⭐⭐⭐ Expert) | home (filtre), badges modules |

**Règle 1.2.4** — Les statistiques macro (95 % MIT NANDA, +270 % Microsoft / Sigma, 76 % France Num, ×5 productivité PwC, 77 000 offres PwC, 3,7× IDC Copilot, consensus 70-95 % Gartner / McKinsey / Deloitte) sont synchronisées sur leurs lieux d'apparition (home + PR-01 + PR-02 + PR-04). Toute modification d'un chiffre macro déclenche une vérification cross-pages.

**Règle 1.2.5** — **Cohérence intra-page des chiffres affichés**. Sur une même page, les chiffres déclarés doivent être cohérents entre eux. Ex : si l'accroche dit « catalogue étendu à 83 fiches en 14 catégories », la grille de stats juste en dessous ne peut pas afficher « 76 Deep-dives · 90+ Outils indexés · 13 Catégories ». Toute stat affichée doit être identique aux comptages réels (vérifier par grep le nombre d'éléments avant de figer une stat).

**Règle 1.2.5.1 — Tous les blocs chiffrés d'une page doivent être patchés ensemble (anti-drift)**. Erreur récurrente identifiée v3.6, v3.7 et v3.7.1 : sur `ressources.html`, le hero badge et le h2 du catalogue sont mis à jour (`95 fiches · 15 catégories`), mais la grille `<div class="exec-stats">` de la section Synthèse conserve les anciens nombres en clair (`<div class="exec-stat-num">83</div>` + `14`). Les chiffres dans `exec-stats`, `card-badge`, `hero-stat-num`, `cat-divider-count`, prose narrative, méta description, takeaways texte sont **tous des points d'apparition à patcher** lorsqu'un total change. Avant de figer une itération :
- Lancer `grep -n '<chiffre-courant>\b' page.html` pour repérer **toutes** les occurrences ;
- Ne jamais supposer qu'une mise à jour ponctuelle (badge, h2, meta) suffit — les `exec-stat-num` et `cat-divider-count` sont des anti-patterns récurrents oubliés ;
- Cross-checker via `grep -c 'tool-card" id='` (ou équivalent par type d'entité) le comptage réel et l'aligner partout.

**Règle 1.2.6** — **Pas de versioning interne sur le front**. Les mentions « V3.5 », « v3.6 », « itération v3.x » sont des conventions internes (commits, briefs, RULES). Elles **ne doivent jamais apparaître côté UX visible** (badges, accroches, descriptions). Le site est un produit publié, pas un changelog. Pour signaler une nouveauté côté front, préférer une formulation neutre : « catégorie récente », « nouveauté 2026 », ou pas de marqueur du tout. Le versioning reste dans `git log` et dans les briefs internes.

**Règle 1.2.7 — Pas de biais sectoriel ou territorial dominant** (NOUVELLE v1.5.7). Le Hub IA cible **les dirigeants PME/ETI du réseau Quest for Change**, qui opère principalement sur le Grand Est mais cherche à rayonner plus largement. Les modules doivent rester **agnostiques en termes de filière et de territoire** : on cite des exemples diversifiés sans pousser un secteur ou un écosystème territorial spécifique comme cas dominant.

**Seuils de détection** : sur un module donné (hors étude de cas qui peut légitimement ancrer un cas client), un compte par grep des marqueurs sectoriels/territoriaux ne doit pas saturer sur **une seule filière** (> 60-70 % du total des marqueurs) ni sur **un seul écosystème territorial** (> 30 % des occurrences territoriales).

❌ **Anti-pattern observé v3.7.7 sur CU-018** : 277 marqueurs sectoriels/territoriaux dont 110 mentions « bois » (40 %), 92 mentions de l'écosystème R&D Grand Est (ENSTIB / LERMAB / CRAN / ENACT), 34 mentions territoriales (Vosges / Grand Est / Lorraine). Un industriel hors filière bois ou hors Grand Est ne se reconnaissait pas dans le module.

✅ **Pattern correct** :
- Pour les exemples sectoriels : citer **au moins 3-4 filières** comparables (bois, textile, métallurgie, plasturgie, agroalimentaire selon le sujet) en parallèle.
- Pour les écosystèmes R&D : citer **plusieurs laboratoires français/européens** par filière (ENSTIB / LERMAB pour le bois, Mines ParisTech / Centrale pour la mécanique, INSA Lyon pour la plasturgie, CEA Tech transverse, IRT SystemX / Saint Exupéry / Jules Verne, etc.). Le Grand Est peut rester cité comme **un exemple parmi d'autres**, jamais comme « atout territorial unique » ou « avantage compétitif structurant ».
- Pour les dispositifs de financement : citer un panorama national/européen (France 2030, CIR/JEI, BPI Build Up, EIC Accelerator, Horizon Europe) plutôt qu'un fléchage régional exclusif (Climaxion, Région Grand Est seuls).
- L'étude de cas peut être positionnée dans une filière concrète (cohérence narrative) mais doit **mentionner explicitement la transposabilité** à 2-3 autres filières via une phrase du type : « Pattern comparable à ce qu'on observe en fonderie, plasturgie ou textile ».

**Procédure de vérification** :
```bash
# Audit biais sectoriel/territorial — à lancer sur tout module avant clôture
python3 -c "
import re
sectors = {
    'bois': r'\b(?:bois|grume|scieri|menuiseri|panneau|charpent|ENSTIB|LERMAB)\b',
    'textile': r'\b(?:textile|tissu|filature|tissage|Lectra)\b',
    'métal': r'\b(?:métallurg|tôle|profilé|forge|fonderi)\b',
    'plasturgie': r'\b(?:plastur|moulage|injection)\b',
    'agroalim': r'\b(?:agroaliment|laiteri|fromager|brasseri|abattoir)\b',
}
import sys
s = open(sys.argv[1]).read()
counts = {k: len(re.findall(p, s, re.I)) for k, p in sectors.items()}
total = sum(counts.values())
if total > 30:
    for k, n in counts.items():
        share = n/total*100
        flag = '⚠️' if share > 60 else ''
        print(f'{k}: {n} ({share:.0f}%) {flag}')
" modules/cu-018-...html
```

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

### 1.5 Pattern structurel obligatoire pour tout module CU et toute fiche PR

Cette section formalise le pattern HTML / CSS / JS attendu pour **tout nouveau module CU et toute nouvelle fiche PR**. Toute production Cowork (mockup) ou Claude Code (intégration) doit s'y conformer. Ce pattern est non négociable — il garantit la cohérence visuelle et la maintenabilité du site.

**Règle 1.5.1 — Squelette HTML minimal**. Tout module CU et toute fiche PR doit suivre cette ordonnance :

```html
<body>
  <!-- 1. Reading progress (avant le hero, en dehors du main) -->
  <div class="reading-progress" id="readingProgress"></div>

  <!-- 2. Nav harmonisée (cf. règles 1.4.1-1.4.2) -->
  <nav class="nav scrolled" id="nav">…</nav>

  <!-- 3. Hero du module -->
  <header class="module-hero">
    <div class="module-hero-inner">
      <a href="…" class="module-back">← Retour aux modules</a>
      <div class="module-badges">
        <a href="…" class="card-badge axe-X">…</a>          <!-- axe métier obligatoire -->
        <a href="…" class="card-badge nX">⭐… Niveau X</a>   <!-- niveau de complexité -->
        <span class="card-badge">📋 Type</span>              <!-- type de format -->
        <span class="card-badge">… min de lecture</span>     <!-- temps de lecture -->
      </div>
      <h1>EMOJI Titre métier</h1>                            <!-- emoji ouvrant obligatoire -->
      <p class="module-subtitle">…</p>                        <!-- 2-3 phrases -->
    </div>
  </header>

  <!-- 4. Layout 2 colonnes (sidebar + main) -->
  <div class="module-layout">

    <aside class="module-toc">                               <!-- TOC sticky obligatoire -->
      <button class="module-toc-mobile-toggle">📋 Sommaire</button>
      <div class="module-toc-label">Sommaire</div>
      <ul class="module-toc-list" id="tocList">
        <li><a href="#executive-summary">…</a></li>
        <li><a href="#section-1">…</a></li>
        …
        <li><a href="#ressources">…</a></li>
      </ul>
    </aside>

    <main class="module-main">

      <!-- 5. Executive summary (gradient bleu marine, obligatoire) -->
      <section class="module-section" id="executive-summary">
        <div class="exec-summary">
          <div class="exec-summary-label">⚡ L'essentiel à retenir en 90 secondes</div>
          <h2>…</h2>
          <div class="exec-takeaways">
            <div class="exec-takeaway">
              <div class="exec-takeaway-num">1</div>           <!-- num pas icon -->
              <p>…</p>
            </div>
            <!-- 4 takeaways au total -->
          </div>
          <div class="exec-stats">…</div>                       <!-- 3-4 stats -->
          <div class="exec-when">                               <!-- public cible -->
            <h3>Ce module est pour toi si…</h3>
            <ul>…</ul>
          </div>
        </div>
      </section>

      <!-- 6. Sections numérotées (header avec section-number obligatoire) -->
      <section class="module-section" id="section-1">
        <div class="module-section-header">
          <div class="module-section-icon icon-context">1</div>
          <div class="module-section-title">
            <div class="section-number">Section 1</div>
            <h2>Titre métier</h2>
          </div>
        </div>
        …
      </section>
      …

      <!-- 7. Pour aller plus loin (id="ressources" obligatoire — pas "section-7") -->
      <!-- Schéma A — externes UNIQUEMENT (cf. règle 1.5.5) -->
      <section class="module-section" id="ressources">
        <div class="module-section-header">…</div>
        <!-- Callout d'aiguillage vers la bibliographie transverse -->
        <div class="callout callout-info">
          Pour le panorama complet des outils, retrouve les fiches détaillées sur la
          <a href="../ressources.html#bibliographie">page Ressources du Hub</a>.
        </div>
        <div class="resources-cat">
          <h3>📰 Articles de fond</h3>
          <ul>
            <li><a href="…" target="_blank" rel="noopener">…</a><span class="resources-meta">…</span></li>
          </ul>
        </div>
        <div class="resources-cat">
          <h3>🎓 Tutoriels &amp; cas pratiques</h3>
          <ul>…</ul>
        </div>
        <div class="resources-cat">
          <h3>📚 Documentation officielle &amp; études</h3>
          <ul>…</ul>
        </div>
        <div class="resources-cat">
          <h3>👥 Communautés &amp; veille</h3>
          <ul>…</ul>
        </div>
      </section>
      <!-- Les renvois INTERNES (modules complémentaires, préalables, fiches outils, architectures)
           vivent dans le CORPS du module au fil du texte (cf. règle 1.5.6),
           PAS dans cette section finale. -->


    </main>
  </div>

  <!-- 8. Footer harmonisé (cf. règle 1.4.3) -->
  <footer class="footer">…</footer>

  <!-- 9. JS module-v3 (active TOC sticky + scroll-spy + reading progress) -->
  <script src="../js/module-v3.js"></script>
</body>
```

**Règle 1.5.2 — Composants CSS de référence**. Ne jamais redéfinir les composants suivants en `<style>` inline. Ils sont dans `module-v3.css` ou `style.css` et doivent être référencés tels quels :

- Layout : `.module-layout` · `.module-toc` · `.module-main` · `.module-toc-list`
- Hero : `.module-hero` · `.module-hero-inner` · `.module-back` · `.module-badges` · `.module-subtitle`
- Synthèse : `.exec-summary` · `.exec-summary-label` · `.exec-takeaways` · `.exec-takeaway` · `.exec-takeaway-num` · `.exec-stats` · `.exec-stat` · `.exec-when`
- Section : `.module-section` · `.module-section-header` · `.module-section-icon` · `.module-section-title` · `.section-number`
- Composants typés (à utiliser, pas à réinventer) : `.callout` (`.callout-info` / `.callout-warn`) · `.alert-block` · `.alert-ai-act` · `.checklist-block` · `.diagnostic` · `.case-deep-actor` · `.pull-quote` · `.resources-cat`
- Niveaux : `.card-badge.n1` · `.n2` · `.n3` · `.n4`
- Axes métier : `.card-badge.axe-a` à `axe-e` · classe spéciale agentique

Si une page introduit un composant nouveau (ex : `.timeline-block`, `.tool-table`, `.legal-grid`), il peut rester inline **uniquement s'il est utilisé sur une seule page**. Dès qu'il est utilisé sur 2+ pages, il doit migrer dans `module-v3.css` ou `style.css`.

**Règle 1.5.3 — Anti-patterns interdits sur les modules / fiches PR** :

- ❌ **Pas de `<main>` direct sans `module-layout`** : tout module / fiche doit avoir la sidebar TOC sticky.
- ❌ **Pas d'`id="section-7"` pour la dernière section** : utiliser `id="ressources"` (cohérent avec le pattern et les renvois inter-pages).
- ❌ **Pas de `.exec-takeaway-icon` (emoji texte) au lieu de `.exec-takeaway-num`** : le pattern de référence utilise des numéros 1-2-3-4, pas des icônes émoji.
- ❌ **Pas de `<style>` inline qui redéfinit `.exec-summary`, `.exec-takeaway`, `.alert-block`, `.checklist-block`, `.stat-block`, `.tool-table`, `.pull-quote`, `.arch-callout`** : ces composants sont centralisés (ou doivent l'être). Si un composant nouveau apparaît sur 2+ modules, **migration obligatoire vers `module-v3.css`** dans le commit qui l'introduit la 2ème fois (renforcé v1.3 suite v3.6.2).
- ❌ **Pas de h1 sans emoji ouvrant** sur les modules / fiches PR (ex : `<h1>Order-to-cash automation</h1>` doit devenir `<h1>💸 Order-to-cash automation</h1>`).
- ❌ **Pas de balise `<a>` dans le contenu d'une card cliquable de la home** (le navigateur ferme la card prématurément). Si une source doit être citée, la mettre sur la page CU dédiée.
- ❌ **Pas de couleurs hardcodées** dans les `<style>` inline (`#1e3a8a`, `#dc2626`, etc.) : utiliser exclusivement les variables CSS du design system (`--color-primary`, `--color-surface`, `--color-warning`, `--color-success`, etc.). Sinon, le design system perd sa cohérence (ajout v1.3).
- ❌ **Pas d'espacements en valeurs absolues** (`padding: 1.5rem`, `margin: 2rem`, etc.) dans les `<style>` inline : utiliser les variables `var(--space-1)` à `var(--space-9)` du design system. Cohérence avec la grille d'espacement et facilité de refactorisation future (ajout v1.4 suite à proposition Claude Code v3.6.2).
- ❌ **Pas de section nommée « Auto-diagnostic » sans form interactif + génération de plan + export** (cf. règle 1.5.5). Si la section ne respecte pas ces 3 propriétés, la nommer autrement (« Checklist d'éligibilité », « Récapitulatif »).
- ❌ **Pas de récapitulatif des renvois internes (modules, préalables, fiches outils, architectures) dans la section finale `id="ressources"`** : ces renvois vivent dans le corps du module, contextualisés (cf. règle 1.5.6). La section finale est réservée aux ressources externes (Schéma A : Articles / Tutoriels / Documentation / Communautés + callout vers `ressources.html#bibliographie`).
- ❌ **Pas de `<pre>` text-art pour représenter un flux fonctionnel** (étapes liées par flèches → / ↓ / ⬇). Le `<pre>` impose une police monospace et un rendu « code brut » qui ressemble à un terminal — alors qu'il s'agit en réalité d'un **schéma fonctionnel**, qui mérite une représentation visuelle structurée. Ajout v1.5.8 suite à v3.7.9 (2 schémas mal rendus dans `dep-07-evaluation-qualite.html`).
  Pattern correct : utiliser un composant **pipeline visuel** avec étapes numérotées, branches Yes/No colorées et flèches CSS — un `<div class="pipeline-flow">` avec des `<div class="pipeline-step">` enchaînés et des `<div class="pipeline-arrow">↓</div>` entre les étapes. Si le composant n'est utilisé qu'une ou deux fois sur une page, il peut rester scopé en `<style>` local de la fiche (RULES § 1.4.4 single-use autorisé). Au-delà, migrer vers `module-v3.css`.

**Règle 1.5.4 — Rôle de Cowork vs Claude Code (mise à jour v1.3, suite à v3.6.2)**. Pour éliminer définitivement les désynchronisations de canal :

- **Cowork = matière éditoriale en MD structuré uniquement.** Cowork produit le contenu éditorial, le sourcing, les gloses, les structures narratives, les écueils, les checklists métier, les instructions précises sur les composants à utiliser (« ici un `.alert-block`, ici un `.diagnostic` 8 questions »). **Cowork ne produit PLUS de mockup HTML** depuis v3.6.2. Cette règle est née du constat que les mockups Cowork dérivaient systématiquement du pattern de référence (v3.6 → v3.6.1 → v3.6.2).
- **Claude Code = construction HTML conforme.** Claude Code construit le HTML des nouveaux modules à partir du gabarit canonique `modules/cu-008-knowledge-base-rag.html` et de la matière éditoriale MD fournie par Cowork. Claude Code valide la conformité au pattern 1.5.1 et au CSS centralisé (1.5.2) avant d'intégrer. Tout commit qui déroge doit le signaler explicitement.
- **Référence visuelle commune** : `modules/cu-008-knowledge-base-rag.html` est le module canonique de référence pour la structure complète (TOC + executive summary + sections numérotées + auto-diagnostic JS + Pour aller plus loin avec `.resources-cat` Schéma A). Tout nouveau module doit s'aligner sur sa structure.

**Règle 1.5.5 — Format auto-diagnostic standard (NOUVELLE v1.3)**. La section auto-diagnostic d'un module CU peut être personnalisée selon le sujet (échelle de positionnement, prérequis bloquants, scoring de maturité, verdict GO/NO-GO, etc.) — mais doit respecter **3 propriétés non négociables** :

1. **Form interactif** : `<form>` avec inputs (radio, checkbox, textarea, select) — pas de checklist statique non interactive.
2. **Génération d'un plan d'action** : un bouton qui produit dynamiquement (en JS) un plan personnalisé sur la base des réponses de l'utilisateur. Pas seulement un score.
3. **Export téléchargeable** : un bouton qui exporte le plan en `.txt` ou `.md` — l'utilisateur doit pouvoir partir avec son livrable. Sauvegarde en `localStorage` recommandée pour la persistance entre visites.

Le template de référence (`modules/_template-auto-diagnostic.html`) propose un format normalisé en 5 questions (positionnement / cas concret / frein / premier pas / indicateur), utilisable tel quel pour les modules N1-N3. Pour les modules N3-N4 plus avancés (CU-008, CU-013), un format custom est acceptable tant que les 3 propriétés ci-dessus sont respectées.

**Anti-pattern à proscrire** : checklist statique en `<ul>` à compter manuellement, sans interactivité ni export, **nommée « Auto-diagnostic »** (cas CU-023 v3.6.0 — corrigé en v3.6.2).

**Si la section ne respecte pas les 3 propriétés**, elle ne doit PAS être nommée « Auto-diagnostic ». Choisir un nom plus juste : « Checklist d'éligibilité », « Checklist projet », « Récapitulatif ». L'utilisateur doit savoir ce qu'il obtient.

**Précision (ajout v1.4)** : le **format checklist statique** reste un format valide pour le Hub, à condition d'être **nommé en cohérence** avec ce qu'il livre (« Checklist d'éligibilité », « Checklist projet », « Checklist sécurité prestataire »). Il a sa valeur en format imprimable / référentiel contractuel. **MAIS** pour les modules N4 (Expert) où l'utilisateur attend un livrable actionnable et personnalisé, le format interactif (form + verdict + export) reste fortement recommandé pour cohérence UX avec les modules récents (CU-008, CU-013, CU-023). Cas limites traités au cas par cas par Cowork éditorial.

**Précision (ajout v1.4) — cohérence card index ↔ contenu réel** : si une card de la home promet « Étude de cas + checklist », le module doit livrer **les deux**. Si le module ne contient qu'une checklist (sans étude de cas formelle), la card doit dire « Checklist projet » ou équivalent. Si le module contient un cas pédagogique (incident documenté, contre-exemple), la card peut dire « Cas pédagogique + checklist ». Toute désynchronisation card ↔ contenu détectée est un bug bloquant à corriger immédiatement.

**Précision (ajout v1.5.6) — audit de cohérence card ↔ contenu automatisé**. Le bug récurrent observé sur CU-024 / CU-027 (v3.6.3) puis CU-025 (v3.7.7) suit toujours le même schéma : la card promet un livrable nominal (étude de cas, auto-diag) qui n'est pas effectivement présent dans le module. Pour prévenir la récurrence, **lancer le script d'audit suivant à chaque clôture d'itération** :

```python
import re, glob, os
with open('index.html') as f: home = f.read()
card_re = re.compile(
    r'<a href="modules/(cu-\d+-[a-z0-9-]+)\.html"[^>]*>.*?<span class="card-quiz">([^<]+)</span>',
    re.DOTALL
)
for m in card_re.finditer(home):
    cu_id, label = m.group(1), m.group(2).strip()
    fp = f'modules/{cu_id}.html'
    if not os.path.exists(fp): continue
    s = open(fp).read()
    flags = []
    if re.search(r'case-deep-step|case-deep-final|<h2[^>]*>[^<]*(?:[Éé]tude de cas|RetEx|Mise en situation)', s):
        flags.append('CASE')
    if re.search(r'<h2[^>]*>[^<]*Auto-diagnostic', s) or 'id="diagnostic"' in s:
        flags.append('AUTO-DIAG')
    if re.search(r'<h2[^>]*>[^<]*[Qq]uiz', s):
        flags.append('QUIZ')
    if 'checklist-block' in s or re.search(r'<h2[^>]*>[^<]*[Cc]hecklist', s):
        flags.append('CHECKLIST')
    if re.search(r'<h2[^>]*>[^<]*(?:[Pp]lan d.action|[Pp]lan 30 jours)', s):
        flags.append('PLAN')
    if 'incident-card' in s or re.search(r'<h2[^>]*>[^<]*[Ii]ncident', s):
        flags.append('INCIDENT')
    label_l = label.lower()
    expected = []
    if 'étude de cas' in label_l or 'etude de cas' in label_l: expected.append('CASE')
    if 'auto-diagnostic' in label_l: expected.append('AUTO-DIAG')
    if 'quiz' in label_l: expected.append('QUIZ')
    if 'checklist' in label_l: expected.append('CHECKLIST')
    if 'plan' in label_l: expected.append('PLAN')
    if 'cas pédagogique' in label_l: expected.append('INCIDENT')
    missing = [e for e in expected if e not in flags]
    if missing:
        print(f'MISMATCH {cu_id}: label="{label}" missing={missing} actual={flags}')
```

Si le script retourne une ligne `MISMATCH`, soit (a) renommer la card pour qu'elle reflète le contenu réel, soit (b) ajouter le contenu manquant au module. **Jamais laisser tel quel** : la card est la promesse, le module est la livraison — un dirigeant trompé deux fois ne revient plus.

**Pour CU-025 (v3.7.7)** : la card promettait « Étude de cas + plan d'action » mais le module contient en réalité une **architecture détaillée en 4 layers** + un **plan d'action 30 jours** + des **retours communautaires convergents** (5 retours croisés cités), pas une étude de cas formelle. Label corrigé en « **Architecture + plan d'action** » (sur la card home + le badge hero du module) — descriptif et précis. Les retours communautaires restent un bloc de validation pédagogique, pas un cas d'étude au sens canonique du Hub (cf. CU-008, CU-014, CU-015 qui ont chacun une étude de cas formelle structurée en `case-deep-step` / `case-deep-final`).

**Règle 1.5.6 — Renvois internes contextualisés (NOUVELLE v1.3)**. Les renvois vers d'autres ressources internes du Hub (autres modules CU, préalables PR, fiches outils de `ressources.html`, page Architectures) **vivent dans le CORPS du module**, au fil du texte, contextualisés à l'endroit où ils sont pertinents. Ils **ne doivent PAS** être récapitulés dans la section finale `id="ressources"` (qui est réservée aux ressources externes — cf. règle 1.5.5 et squelette HTML 1.5.1 mis à jour v1.3).

**Patterns de renvoi obligatoires** :

- **Vers une fiche outil de `ressources.html`** : à la première mention en `<strong>` d'un outil ayant une fiche dans la page Ressources, ajouter un lien vers son ancre :
  ```html
  L'écosystème <a href="../ressources.html#cursor"><strong>Cursor</strong></a> permet…
  ```
  **Liste à jour des ancres outils** : à générer dynamiquement par grep avant chaque écriture (la liste indicative ci-dessous se désynchronise vite — préfère la commande live, ajout v1.4 suite à proposition Claude Code v3.6.2) :
  ```bash
  grep -oE '<article class="tool-card" id="[^"]+"' ressources.html | grep -oE 'id="[^"]+"' | sort -u
  ```
  Liste indicative au moment de v1.4 (~84 fiches) : `#cursor`, `#claude-code`, `#claude`, `#pinecone`, `#n8n`, `#dify`, `#mistral`, `#perplexity`, `#notebooklm`, `#hubspot`, `#salesforce`, `#copilot-workspace`, etc. À ne **pas** considérer comme exhaustive — toujours regreper avant écriture.

- **Vers un préalable** : quand un module mentionne un cadrage transverse (organisation, data, sécurité, formation), renvoyer au préalable correspondant :
  ```html
  Pour cadrer ta maturité organisationnelle avant de te lancer, lis
  <a href="../prealables/pr-01-maturite-organisationnelle.html">le préalable Maturité organisationnelle</a>.
  ```

- **Vers la page Architectures** : pour les modules sensibles (RH, juridique, financier, sécurité), renvoyer aux patterns d'architecture pertinents :
  ```html
  Architecture recommandée : <a href="../architectures.html#a3">A3 (open-source cloud souverain)</a>
  ou <a href="../architectures.html#a4">A4 (on-premise)</a>.
  ```

- **Vers un module complémentaire** : dans le sous-titre hero ou dans le corps :
  ```html
  Pour le cycle commercial sortant, voir <a href="cu-024-order-to-cash.html">Order-to-cash automation</a>.
  ```

**Règle 1.5.6.1 — Pas de codes internes (CU-XXX, PR-XX, DEP-XX) en texte affiché** (NOUVELLE v1.5.2, post-audit jargon v3.7.2). Les codes `CU-001` à `CU-027`, `PR-01` à `PR-07`, `DEP-01` à `DEP-08` sont des **conventions internes** (briefs, RULES, file paths, commits, ids HTML). Ils **ne doivent jamais apparaître en clair côté lecteur** : ni en libellé de lien, ni dans le corps du texte, ni dans un `desc` JS injecté dans l'auto-diag, ni dans une cellule de tableau.

  **Le lecteur cible (dirigeant PME/ETI non-IT) ne sait pas ce qu'est un « CU-020 » ou un « DEP-06 ».** Il a besoin de **noms parlants**.

  ❌ **À proscrire** :
  ```html
  <a href="../deploiement/dep-06-inference-saas-self-hosted.html">DEP-06</a>
  <a href="../deploiement/dep-06-inference-saas-self-hosted.html">DEP-06 Inférence SaaS vs self-hosted</a>
  (cf. CU-017)
  (cf. CU-020 méthode audit)
  rester sur du multi-prompt classique (CU-001 à CU-011)
  ```

  ✅ **Pattern correct** : utiliser le **titre éditorial** de la cible avec lien intégré (et un dénominateur de navigation : « le module », « la fiche », « le préalable ») :
  ```html
  Voir la fiche <a href="../deploiement/dep-06-inference-saas-self-hosted.html">Inférence SaaS vs self-hosted</a>.
  Voir le module <a href="../modules/cu-020-conformite-rgpd-ai-act.html">Conformité RGPD &amp; AI Act</a>.
  Voir le préalable <a href="../prealables/pr-07-build-vs-buy.html">Build vs Buy à l'ère de l'IA</a>.
  (cf. <a href="cu-017-controle-qualite-vision.html">Contrôle qualité par vision</a>)
  ```

  **Exceptions tolérées** (codes restent admis car invisibles ou conventionnels) :
  - Attributs HTML : `data-module="cu-027"`, `id="section-1bis"`
  - Chemins de fichiers : `cu-020-conformite-rgpd-ai-act.html`
  - Commentaires HTML / CSS / JS : `/* Bloc — spécifique CU-015 */`
  - Signatures de fichiers exportés : `Plan généré par le module CU-008 du Hub IA`
  - Titres administratifs internes (briefs, rapports de mission, historique RULES, commits)

  **Procédure de vérification** avant clôture d'itération :
  ```bash
  # Codes en clair en dehors des liens et attributs (devrait être quasi-vide) :
  grep -rEn '\b(CU|PR|DEP)-[0-9]+\b' modules/cu-*.html prealables/pr-*.html deploiement/dep-*.html \
    | grep -vE 'href=|data-module|<style|<script|/\*|"CU-|cu-0[0-9]|dep-0[0-9]|pr-0[0-9]|onclick|content \+=|filename|id="|module CU-|"Auto-diagnostic'
  ```

**Règle 1.5.6.2 — Lien outil obligatoire sur la première mention significative par section** (NOUVELLE v1.5.2, post-audit renvois v3.7.2). Tout outil ayant une fiche dans `ressources.html` doit être lié à sa première mention significative dans chaque grande section (`module-section`) où il apparaît. Une « mention significative » est une mise en `<strong>`, une phrase de présentation/comparaison/recommandation, ou une mention d'architecture (« RAG sur Pinecone », « fine-tuning Mistral »).

  **Pas besoin de lier toutes les occurrences** (sinon saturation visuelle) — la règle est : **1 lien par outil par section**, sur la mention la plus significative.

  **Cas pratiques** :
  - Énumération comparative (« Cursor, Claude Code, Windsurf ») : lier les 3 outils si c'est leur 1re apparition sur la page.
  - Architecture technique (« stack RAG Pinecone + Cohere ») : lier Pinecone et Cohere s'ils ont une fiche.
  - Cas client (« la PME utilise HubSpot ») : lier HubSpot à sa première occurrence pédagogique.
  - Outils accessoires hors-sujet : laisser non lié (ex: une URL technique mentionnée en passant).

  **Audit recommandé** : périodiquement, lancer un grep sur les noms commerciaux des fiches outils dans les modules pour détecter les mentions non liées et les corriger.

**Cross-links obligatoires sur les paires/triplets sensibles** (codifiés v3.6.2) :
- CU-015 ↔ CU-027 (asynchronicité agentique vs guide d'achat dev)
- CU-021 ↔ CU-024 (compta fournisseur entrante vs cycle commercial sortant)
- CU-001 ↔ CU-011 ↔ CU-012 (triptyque veille progressif)
- CU-005 ↔ CU-023 (déjà en place, à préserver)

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
- **v1.5.8** — mai 2026, suite à v3.7.9 (jargon DEP-XX résiduel + 2 schémas `<pre>` text-art peu lisibles dans `dep-07-evaluation-qualite.html`, signalés par Cowork) :
  - § 1.5.3 enrichie : interdiction des `<pre>` text-art pour représenter un flux fonctionnel. Pattern correct = composant pipeline visuel `<div class="pipeline-flow">` avec étapes numérotées, branches colorées, flèches CSS.
  - Correctif appliqué v3.7.9 :
    - dep-07 : 2 `<pre>` text-art (cycle prompt-eval-improve + workflow CI/CD) refondus en composants `pipeline-flow` lisibles.
    - 11 jargons DEP-XX / CU-XXX / PR-XX résiduels patchés (label-seul, en clair) dans dep-06, dep-07, dep-08, cu-021, pr-06, pr-07. Audit v3.7.2 n'avait pas tout ratissé — la vérif grep documentée en § 1.5.6.1 doit être lancée plus largement.
    - 1 lien cassé corrigé : `cu-014-veille-strategique.html` (n'existe pas) → `cu-014-multi-agents.html` dans pr-07.
- **v1.5.7** — mai 2026, suite à v3.7.8 (biais sectoriel/territorial massif sur CU-018, signalé par Cowork) :
  - § 1.2.7 (NOUVELLE) : interdiction du biais sectoriel ou territorial dominant. Le Hub IA cible le réseau QFC qui rayonne au-delà du Grand Est ; un module doit rester agnostique en termes de filière (citer 3-4 filières comparables en parallèle) et de territoire (panorama national/européen des écosystèmes R&D et dispositifs de financement). Seuils : > 60-70 % des marqueurs sectoriels sur une seule filière, ou > 30 % sur un seul écosystème territorial = bug bloquant. Procédure de vérification grep documentée.
  - Correctif appliqué v3.7.8 : CU-018 « Optimisation production » refondue éditorialement. Avant : 110 mentions bois (40 % des marqueurs), 92 mentions ENSTIB/LERMAB/CRAN, 34 mentions Grand Est/Vosges, étude de cas exclusive BoisCo scierie Vosges. Après : équilibrage multi-filière (bois, textile, métallurgie, plasturgie, agroalim), élargissement à un panorama d'écosystèmes R&D français/européens, étude de cas repositionnée en cas industriel transverse.
- **v1.5.6** — mai 2026, suite à v3.7.7 (mismatch card ↔ contenu sur CU-025, signalé par Cowork) :
  - § 1.5 enrichie (audit cohérence automatisé) — script Python documenté pour détecter les mismatches card / contenu sur l'ensemble des modules. Couvre 6 livrables canoniques : CASE (étude de cas formelle), AUTO-DIAG (auto-diagnostic interactif), QUIZ, CHECKLIST, PLAN (plan d'action), INCIDENT (cas pédagogique). Le script doit retourner 0 ligne MISMATCH à chaque clôture d'itération.
  - Correctif appliqué v3.7.7 : CU-025 « Knowledge management IA-augmenté pour dirigeant » — label card et badge hero mis à jour de « Étude de cas + plan d'action » → « **Architecture + plan d'action** ». Le module n'a pas d'étude de cas formelle (`case-deep-step` / `case-deep-final`) mais une architecture détaillée en 4 layers + un plan d'action 30 jours + des retours communautaires convergents (5 retours croisés cités). Le nouveau label est descriptif et précis.
- **v1.5.5** — mai 2026, suite à v3.7.6 (callout intro de la section « Pour aller plus loin » sans `margin-bottom`, signalé par Cowork sur cu-023 « Devis simples ») :
  - § 1.5.1.2 (NOUVELLE) — **Le callout intro de la section finale `id="ressources"` doit toujours porter le style `margin-bottom: var(--space-5)`**. Ce callout sert de pont visuel entre le titre de la section (« Pour aller plus loin ») et la première sous-rubrique (`📰 Articles de fond`, `🎓 Tutoriels`, etc.). Sans `margin-bottom`, le callout est collé au titre h3 suivant — pas de respiration, le tout devient illisible.

    ❌ **Anti-pattern observé en v3.7.6** (12 fichiers concernés : cu-023, cu-024, cu-027, pr-07, dep-01 à dep-08 sauf dep-04 inclus) :
    ```html
    <div class="callout callout-info">
      Pour le panorama complet des outils, retrouve les fiches détaillées sur la <a href="...">page Ressources du Hub</a>.
    </div>
    <div class="resources-cat">
      <h3>📰 Articles de fond</h3>
      …
    </div>
    ```

    ✅ **Pattern correct** :
    ```html
    <div class="callout callout-info" style="margin-bottom: var(--space-5);">
      <p style="margin:0;">📚 <strong>Bibliographie transverse&nbsp;:</strong> …</p>
    </div>
    <div class="resources-cat">
      <h3>📰 Articles de fond</h3>
      …
    </div>
    ```

    **Pourquoi `style` inline ?** Le bloc `.callout` du design system n'a pas de `margin-bottom` standard (les espacements sont définis par le contexte). Sur la section finale, l'espacement avant `resources-cat` est nécessaire ; le style inline `var(--space-5)` est tolérable car single-use et utilise une variable du design system (RULES § 1.5.3 admet `style="..."` ponctuel qui utilise les `var(--space-X)`).

    **Règle de prévention** : vérifier par grep que **tout `<div class="callout callout-info">` qui précède directement un `<div class="resources-cat">`** porte un attribut `style` avec `margin-bottom` :
    ```bash
    python3 -c "
    import re, glob
    for fp in glob.glob('modules/cu-*.html') + glob.glob('prealables/pr-*.html') + glob.glob('deploiement/dep-*.html'):
        s = open(fp).read()
        for m in re.finditer(r'<div class=\"callout callout-info\"([^>]*)>', s):
            after = s[m.end():m.end()+1500]
            if re.search(r'</div>\s*<div class=\"resources-cat\">', after):
                if 'margin' not in m.group(1):
                    print(f'{fp}: callout intro sans margin')
    "
    ```
  - Correctif appliqué v3.7.6 : 12 callouts patchés (cu-023, cu-024, cu-027, pr-07, dep-01, dep-02, dep-03, dep-04, dep-05, dep-06, dep-07, dep-08) — ajout de `style="margin-bottom: var(--space-5);"` au tag d'ouverture.
- **v1.5.4** — mai 2026, suite à v3.7.5 (callout `Bibliographie transverse` mal imbriqué dans le `module-section-header` sur 8 modules, signalé par Cowork) :
  - § 1.5.1.1 (NOUVELLE) — **Structure canonique stricte du `<div class="module-section-header">`**. Le `module-section-header` est un conteneur de **mise en page horizontale** (flex / grid) qui aligne **l'icône à gauche et le titre à droite**. Il accepte **uniquement** les enfants suivants, dans cet ordre :
    1. `<div class="module-section-icon ...">…</div>` — icône numérotée ou thématique
    2. **Une seule de ces variantes** pour le titre :
       - `<h2 class="module-section-title">…</h2>` — variante compacte
       - `<div class="module-section-title"><div class="section-number">Section N</div><h2>…</h2></div>` — variante avec numéro de section
    Tout autre contenu (paragraphes, callouts, listes, tables, blocs introductifs) **doit être placé APRÈS** la balise `</div>` qui ferme le `module-section-header`, comme enfant direct du `<section class="module-section">`.

    ❌ **Anti-pattern observé en v3.7.5** (8 modules concernés) :
    ```html
    <section class="module-section" id="ressources">
      <div class="module-section-header">
        <div class="module-section-icon icon-resources">9</div>
        <h2 class="module-section-title">Pour aller plus loin</h2>
        <div class="callout callout-info">…Bibliographie transverse…</div>  <!-- ❌ -->
      </div>
      …
    </section>
    ```
    Le callout aspiré dans la grille horizontale du header se retrouve sur la même ligne que le titre, créant un layout illisible (callout sur la 3e colonne du grid).

    ✅ **Pattern correct** :
    ```html
    <section class="module-section" id="ressources">
      <div class="module-section-header">
        <div class="module-section-icon icon-resources">9</div>
        <h2 class="module-section-title">Pour aller plus loin</h2>
      </div>

      <div class="callout callout-info" style="margin-bottom: var(--space-5);">…</div>

      <div class="resources-cat">…</div>
    </section>
    ```

    **Règle de prévention** : à chaque création / patch d'une section, vérifier par grep que **rien d'autre** que l'icône et le titre n'est imbriqué dans `module-section-header` :
    ```bash
    # Détecte les enfants suspects dans module-section-header :
    python3 -c "
    import re, glob
    pat = re.compile(r'<div class=\"module-section-header\">(.*?)</div>\s*(?=<)', re.DOTALL)
    for fp in glob.glob('modules/cu-*.html') + glob.glob('prealables/pr-*.html') + glob.glob('deploiement/dep-*.html'):
        s = open(fp).read()
        for m in pat.finditer(s):
            body = re.sub(r'<div class=\"module-section-icon[^\"]*\">[^<]*</div>', '', m.group(1))
            body = re.sub(r'<(h2|div) class=\"module-section-title\".*?</\1>', '', body, flags=re.DOTALL)
            body = re.sub(r'<h2>[^<]*</h2>', '', body)
            if body.strip():
                print(f'{fp} : leftover = {body.strip()[:80]}')
    "
    ```
  - Correctif appliqué v3.7.5 : 8 modules patchés (cu-011, cu-012, cu-013, cu-014, cu-015, cu-017, cu-018, cu-019). Callout `Bibliographie transverse` déplacé hors du header avec style normalisé `margin-bottom: var(--space-5)`.
- **v1.5.3** — mai 2026, suite à v3.7.4 (deux bugs critiques post-v3.7.3 signalés par Cowork) :
  - § 1.4.5 (NOUVELLE) — **Tout script qui patche en bulk plusieurs fichiers HTML est interdit s'il s'appuie sur des placeholders textuels (`STASH0`, `STASH1`, etc.) sans contrôle d'intégrité post-écriture**. Bug observé en v3.7.3 : un script Python ajoutait `class="tool-link"` à des liens internes en stashant temporairement les régions `<nav>`, `<footer>`, `<aside>`, `<header>` pour les exclure du patch. Le pattern `<aside class="module-toc">` d'`architectures.html` et de 17 autres pages contient un `<nav class="module-toc-nav">` imbriqué. Le `<nav>` interne a été stashé en premier (placeholder `\x00STASH1\x00`), puis le `<aside>` entier (contenant déjà ce placeholder) a été stashé à son tour. À la restauration (boucle `for key, val in placeholders.items()`), le placeholder STASH1 du nav interne a été restauré AVANT le STASH du aside qui le contenait textuellement — résultat : le `<aside>` restauré contenait `<aside ...> ...\x00STASH1\x00... </aside>` que la boucle ne pouvait plus remplacer (la clé avait déjà été consommée). Les octets nuls ont en outre survécu à l'écriture, corrompant 18 fichiers.
    **Règle de prévention obligatoire** :
    1. Tout script bulk qui stash des régions HTML imbriquées (`<nav>` ↔ `<aside>`, `<header>` ↔ `<section>`, etc.) doit utiliser un parseur HTML (BeautifulSoup, lxml) plutôt que des regex.
    2. Si un script regex doit être utilisé, **restaurer les placeholders dans l'ordre inverse de stash** (LIFO) pour éviter la cascade.
    3. **Test obligatoire post-écriture** : `grep -l $'\x00' [files]` + `grep -l 'STASH[0-9]' [files]` doit renvoyer vide avant clôture du patch. Cf. snippet de vérif :
       ```python
       for fp in files:
           with open(fp, 'rb') as f:
               data = f.read()
           assert b'\x00' not in data, f"NUL bytes in {fp}"
           assert b'STASH' not in data, f"Stash residual in {fp}"
       ```
    4. Toujours **prévisualiser le diff sur 1-2 fichiers** avant d'appliquer en bulk sur 40+ fichiers.
  - § 1.4.6 (NOUVELLE) — **Tout nouveau style de lien (`a.tool-link`, `.crit-build a`, etc.) doit être audité contre tous les conteneurs à fond foncé du design system**. Bug observé en v3.7.3 : la classe `a.tool-link` (couleur `var(--color-primary)` = #1F3864 bleu foncé) a été ajoutée à 344 liens internes — y compris à l'intérieur de `.exec-summary` (gradient #1F3864 → #2E5395, fond bleu foncé) — créant un contraste **bleu sur bleu illisible**. Mêmes conteneurs à risque : `.case-deep-final`, `.archi-block`, `.compare-table th`, `.trouble-table th`.
    **Règle de prévention obligatoire** :
    1. Avant de finaliser un nouveau style de lien (ou de couleur de texte), **lister tous les conteneurs à fond foncé** du design system : `grep -nE 'background:.*(#1F3864\|#2E5395\|#1F2937\|#1E3A8A\|gradient.*135deg)' css/*.css`.
    2. **Définir une surcharge explicite** pour chacun (color jaune accent `#FFD600` ou blanc selon le pattern). Pattern canonique appliqué en v3.7.4 :
       ```css
       .exec-summary a, .exec-summary a.tool-link,
       .case-deep-final a, .case-deep-final a.tool-link,
       .archi-block a, .archi-block a.tool-link {
         color: #FFD600;
         text-decoration-color: rgba(255, 214, 0, 0.45);
       }
       ```
    3. **Test visuel manuel** : ouvrir au moins un module avec exec-summary et vérifier que les liens internes sont lisibles avant de cliquer « commit ».
  - Correctifs appliqués v3.7.4 :
    - 18 sommaires (TOC) restaurés à leur contenu d'origine depuis `HEAD~1` (`architectures.html` + 11 modules CU + 6 préalables PR concernés par le pattern `<nav>` imbriqué dans `<aside class="module-toc">`).
    - Surcharge CSS contraste ajoutée dans `module-v3.css` § 322+ couvrant `.exec-summary`, `.case-deep-final`, `.archi-block`.
- **v1.5.2** — mai 2026, suite à v3.7.2 (audit jargon codes internes + audit renvois outils manquants, signalés par Cowork) :
  - § 1.5.6.1 (NOUVELLE) : interdiction des **codes internes (CU-XXX, PR-XX, DEP-XX) en texte affiché**. Le lecteur cible (dirigeant PME/ETI non-IT) ne sait pas ce qu'est un « DEP-06 » ou un « CU-020 » : ces codes sont du jargon technique interne qui ne doit jamais sortir des fichiers. Pattern correct = titre éditorial avec lien intégré et dénominateur de navigation (« le module », « la fiche », « le préalable »). 45 occurrences de ce type corrigées en v3.7.2 (cu-008, cu-014, cu-015, cu-018, cu-021, cu-022, cu-023, cu-025, cu-027, pr-01, pr-02, pr-03, pr-05, pr-07, dep-01, dep-07). Procédure de vérification grep documentée.
  - § 1.5.6.2 (NOUVELLE) : règle explicite **lien outil obligatoire sur la première mention significative par section**. Audit v3.7.2 a identifié 378 occurrences d'outils en clair non liées vers leur fiche `ressources.html#xxx`. Top 5 fichiers concentraient 128 hits (cu-013, pr-07, cu-021, cu-023, cu-027). Patches appliqués sur ces 5 fichiers. La règle codifie la pratique : 1 lien par outil par section sur la mention la plus significative — pas saturation.
  - Bug fix collatéral : le module CU-023 pointait vers un fichier inexistant `cu-007-ia-rh.html` (lien cassé) — corrigé vers `cu-007-rh-cv-entretiens.html`.
- **v1.5.1** — mai 2026, suite à v3.7.1 (correctifs post-merge v3.7) :
  - § 1.2.3 mis à jour : nav passe de 6 → **5 entrées** (Préalables / Architectures / **Modules** / **Déploiement** / Ressources). « À propos » retiré du navbar (la section reste accessible via le footer ou par scroll de la home). Modules et Déploiement intervertis pour mettre en avant le cœur de valeur (modules cas d'usage) avant la couche technique (déploiement). Décision Cowork v3.7.1 motivée par (a) le wrap visuel d'« À propos » sur deux lignes après ajout de Déploiement, (b) la priorité éditoriale sur les rubriques à forte densité de contenu.
  - § 1.2.5.1 (NOUVELLE) : règle anti-drift sur les blocs chiffrés multi-emplacements (`exec-stats`, `cat-divider-count`, `hero-stat-num`, badges, méta description, prose, takeaways). Erreur récurrente identifiée v3.6 / v3.7 / v3.7.1 : la grille `<div class="exec-stats">` de `ressources.html` § Synthèse a conservé `83 / 14` après que le hero badge et le h2 catalogue avaient été passés à `95 / 15`. Procédure obligatoire : `grep -n` exhaustif du chiffre courant **avant** clôture d'itération + cross-check du comptage réel via `grep -c`.
- **v1.5** — mai 2026, suite à v3.7 (expansion éditoriale majeure : nouvelle section Déploiement + CU-025 + 5 enrichissements + 14 fiches outils) :
  - § 1.2.3 (glossaire chiffres-clés) actualisé v3.7 : 25 → 26 modules CU (CU-025 ajouté, CU-026 réservé v3.8) ; 83 → 95 fiches outils (12 nouvelles : Pennylane, Sellsy, Axonaut, PandaDoc, Esker, Sidetrade, Tacton, Lovable, Bolt.new, v0, Replit Agent, Windsurf ; 2 mises à jour : Kimi K2 → K2.6 et GitHub Copilot Workspace) ; 5 → 6 entrées de nav (ajout « Déploiement » entre Architectures et Modules) ; ajout d'une nouvelle ligne « Nombre de fiches Déploiement DEP : 8 (DEP-01 → DEP-08) ».
  - Le pattern HTML obligatoire RULES § 1.5.1 s'applique aux fiches DEP avec les mêmes principes que les PR (cadrage transverse). Les fiches DEP suivent le squelette des préalables (sections numérotées, executive summary, sticky TOC, Schéma A pour les ressources finales).
- **v1.4** — mai 2026, suite à audit visuel post-v3.6.2 (incohérences résiduelles CU-024/CU-027 + 3 amendements proposés par Claude Code dans rapport v3.6.2) :
  - § 1.5.5 enrichie : précision que le format checklist statique reste valide sous un autre nom (« Checklist d'éligibilité », « Checklist projet », « Checklist sécurité prestataire »). Format interactif fortement recommandé pour cohérence UX sur les modules N4.
  - § 1.5 enrichie : règle explicite de **cohérence card index ↔ contenu réel** (si card promet « Étude de cas + checklist », le module doit livrer les deux ; sinon renommer la card). Toute désynchronisation détectée = bug bloquant.
  - § 1.5.3 enrichie : interdiction des **espacements en valeurs absolues** (`padding: 1.5rem`, etc.) dans les `<style>` inline — utilisation obligatoire de `var(--space-X)`.
  - § 1.5.6 enrichie : **commande grep dynamique** pour générer la liste à jour des ancres outils (la liste indicative se désynchronise vite, préférer la commande live).
- **v1.3** — mai 2026, suite à l'audit éditorial conjoint Cowork + Claude Code et à l'itération corrective v3.6.2 :
  - § 1.5.1 (squelette HTML) : section finale `id="ressources"` refondue en **Schéma A** — 4 sous-rubriques **toutes externes uniquement** (Articles de fond / Tutoriels / Documentation officielle / Communautés) + callout vers `ressources.html#bibliographie`. Suppression des sous-rubriques internes (Modules complémentaires, Préalables associés) qui mélangeaient les niveaux.
  - § 1.5.3 (anti-patterns) renforcée : ajout de `.stat-block`, `.tool-table`, `.pull-quote`, `.arch-callout` à la liste des composants centralisés à ne pas redéfinir ; règle de **migration obligatoire vers `module-v3.css` dès la 2ème utilisation** ; interdiction des **couleurs hardcodées** ; interdiction de nommer « Auto-diagnostic » une section qui n'est pas interactive ; interdiction des **renvois internes dans la section finale ressources** (qui restent dans le corps).
  - § 1.5.4 (rôles Cowork/Claude Code) clarifiée : **Cowork ne produit plus de mockup HTML**, uniquement de la matière éditoriale en MD structuré. Claude Code construit le HTML à partir de la canonique CU-008 + matière MD Cowork. Cette règle clôt définitivement le cycle de désynchronisation v3.6 → v3.6.1 → v3.6.2.
  - § 1.5.5 (NOUVELLE) : Format auto-diagnostic standard — 3 propriétés non négociables (form interactif + génération plan + export). Format custom toléré sous ces conditions.
  - § 1.5.6 (NOUVELLE) : Renvois internes contextualisés dans le corps — patterns obligatoires vers fiches outils (`ressources.html#xxx`), préalables, architectures, modules complémentaires. Cross-links codifiés sur paires sensibles (CU-015↔CU-027, CU-021↔CU-024, triptyque veille).
- **v1.2** — mai 2026, suite à v3.6.1 (harmonisation des modules CU-023/024/027 produits par Cowork qui déviaient du pattern de référence) :
  - § 1.5 ajoutée : pattern structurel obligatoire pour tout module CU et toute fiche PR (squelette HTML, composants CSS de référence, anti-patterns interdits, rôles Cowork ↔ Claude Code).
  - Nouvelle référence canonique : `modules/cu-008-knowledge-base-rag.html` est le gabarit visuel.
  - § 1.5.3 codifie 6 anti-patterns à bannir (dont `<a>` imbriqué dans card cliquable, `id="section-7"` au lieu de `id="ressources"`, `<style>` inline qui redéfinit les composants centralisés, h1 sans emoji ouvrant).
  - § 1.5.4 clarifie la responsabilité de Cowork (mockup conforme au pattern dès la production) et celle de Claude Code (validation conformité avant intégration, correction sinon).
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
