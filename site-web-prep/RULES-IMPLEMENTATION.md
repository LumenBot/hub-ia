# Règles d'implémentation — Hub IA Learning Center

**Version :** 1.6.2 (refonte simplifiée + chiffres-clés actualisés v3.11 — fiches outils 99 → 104, 15 → 16 catégories)
**Statut :** Référentiel non négociable
**Public :** Claude Code, contributeurs au repo, futurs LLM intervenant sur le site

> Ce fichier est le **référentiel ultime** des règles d'implémentation du Hub IA. Tout ce qui n'y est pas n'est pas une règle ; tout ce qui y est doit être respecté à la lettre. Toute PR qui contredit ce fichier doit être amendée avant merge.

---

## 0. Préambule

Le Hub IA est un site pédagogique destiné à des **dirigeants PME/ETI non-IT** du Grand Est. Trois propriétés en font un outil utile :
1. Il dit la vérité (sourcing rigoureux)
2. Il parle leur langue (pas de jargon technique non explicité)
3. Il est cohérent (chiffres et nav synchronisés partout)

Les LLM ont tendance à dériver sur ces trois axes au fil des itérations — d'où ce fichier.

**Méthode de la v1.6** : refonte consolidée de v1.0 → v1.5.14 en **13 règles essentielles**, avec exemples détaillés et scripts d'audit reportés en annexe (Section 4). Pour la traçabilité, voir `RULES-MIGRATION-v1.5-vers-v1.6.md`.

**Référence visuelle canonique** : `modules/cu-008-knowledge-base-rag.html`. Pour tout doute structurel, consulter ce fichier.

**Garde-fou automatisé** : `site-web-prep/audit-global.py` doit retourner `Total hits : 0` avant toute PR. C'est l'instrument exécutoire de ce référentiel.

---

## 1. Les 13 règles essentielles

### Dimension A — Sourcing & véracité

#### Règle A.1 — Sourcing rigoureux

Toute affirmation chiffrée doit avoir une **source datée et un lien vérifiable**. Format obligatoire : « 95 % des projets GenAI échouent (étude MIT NANDA, août 2025) ». Pas de chiffre orphelin. Pas d'hallucination. Pas d'extrapolation présentée comme fait. Pas de citation fictive.

**Sources prioritaires** : institutions publiques (Bpifrance Le Lab, France Num, INSEE, CNIL, NIST), grandes études (McKinsey, MIT, Microsoft Work Trend, PwC, OECD), références techniques de confiance (Anthropic Engineering, Cloud Security Alliance, OWASP).

**Sources à éviter** : blogs marketing d'éditeurs, contenus sponsorisés, posts LinkedIn anecdotiques, sources sans lien vérifiable.

Détails et exemples : Annexe § 4.A.1.

#### Règle A.2 — RetEx institutionnels uniquement

Les retours d'expérience d'entreprises sont **nommables** uniquement si la source est institutionnelle et publique (Bpifrance Le Lab, presse économique reconnue). Les cas remontés par cabinets de conseil sont **anonymisés** et présentés comme « pattern ».

#### Règle A.3 — Pas de promotion commerciale

Aucun cabinet de conseil intermédiaire, agence ou intégrateur n'est mentionné en promotion. Les fiches outils décrivent factuellement (atouts, limites, prix, souveraineté) sans plaidoyer. Aucun lien d'affiliation.

---

### Dimension B — Cohérence numérique

#### Règle B.1 — Cohérence numérique cross-site et intra-page

Tout chiffre structurel du site (nombre de modules, préalables, fiches outils, entrées de nav, etc.) doit être **identique sur toutes les pages où il apparaît** ET **cohérent intra-page** (les exec-stats ne contredisent pas le hero badge ni la prose).

Avant tout commit modifiant un comptage : exécuter `audit-global.py` qui vérifie les chiffres réels (`grep` des éléments) contre toutes les apparitions cross-site. Mise à jour synchrone obligatoire de **toutes** les occurrences (`exec-stats`, `card-badge`, `hero-stat-num`, `cat-divider-count`, prose narrative, méta-description, takeaways texte, README, glossaire RULES § 1.2.3).

**Glossaire des chiffres-clés courants** : voir Annexe § 4.B.1.

#### Règle B.2 — Pas de versioning interne sur le front

Les mentions « v3.5 », « v3.6 », « itération v3.x » sont des conventions internes (commits, briefs, RULES). Elles **ne doivent jamais apparaître côté UX visible** (badges, accroches, descriptions, méta).

Pour signaler une nouveauté côté front, préférer une formulation neutre : « catégorie récente », « nouveauté 2026 », ou pas de marqueur du tout. Le versioning reste dans `git log` et dans les briefs internes.

---

### Dimension C — Niveau de langue & terminologie

#### Règle C.1 — Public cible PME/ETI non-IT + glose obligatoire

Public cible : dirigeant PME/ETI non-IT (40-65 ans, formation gestion ou technique métier). Vocabulaire de référence : celui d'une CCI ou d'une chambre de métiers.

Aucun jargon technique sans glose explicite à la **première occurrence** dans une page. Liste des termes à expliciter : RAG, MVP, POC, fine-tuning, embeddings, prompt, token, LLM, API, SaaS, cloud souverain, open-source, on-premise (voir Annexe § 4.C.1 pour les gloses canoniques).

Phrases courtes (15-25 mots en moyenne). Paragraphes ≤ 6 lignes. Pas de subordonnées en cascade. Privilégier les termes français quand ils existent. Acronymes QFC (SUM, PM, Starter Class, etc.) à utiliser avec parcimonie sur le site public.

#### Règle C.2 — Pas de codes internes visibles + pas de nomenclature non explicitée

Les codes internes (`PR-01`, `CU-007`, `DEP-03`) **ne doivent pas apparaître dans les titres, cards, badges ou corps de texte visibles**. Ils restent dans les URL et les ancres uniquement. Seul le titre métier est visible en surface.

**Exception unique** : les codes `A1 / A2 / A3 / A4` sont les noms canoniques des patterns d'architecture (`architectures.html` et encarts d'architectures recommandées).

Toute nomenclature ou échelle nouvelle visible côté UX doit être soit **alignée sur les classifications existantes** (échelle ⭐ à ⭐⭐⭐⭐), soit accompagnée d'une **glose immédiate**. Toute légende affichée doit refléter ce qui est réellement utilisé sur la page.

---

### Dimension D — Posture éditoriale

#### Règle D.1 — Pas de biais sectoriel ou territorial dominant

Le Hub IA cible **toutes les PME/ETI** du réseau QFC (principalement Grand Est, ambition plus large). Les modules doivent rester **agnostiques en filière et en territoire** : exemples diversifiés (au moins 3-4 filières comparables), écosystèmes R&D pluriels (plusieurs labos français/européens cités), dispositifs de financement panorama national/européen (pas fléchage régional exclusif).

**Seuils de détection** (hors étude de cas) : aucune filière ne doit saturer > 60-70 % des marqueurs sectoriels d'un module. Aucun écosystème territorial ne doit saturer > 30 % des occurrences territoriales.

Les études de cas peuvent être positionnées dans une filière concrète à condition de **mentionner explicitement la transposabilité** à 2-3 autres filières.

Anti-patterns historiques et script d'audit : Annexe § 4.D.1.

#### Règle D.2 — Card index ↔ contenu réel

Si une card de la home promet « Étude de cas + checklist », le module doit livrer **les deux**. Si le module ne contient qu'une checklist (sans étude de cas formelle), la card doit dire « Checklist projet » ou équivalent. Si le module contient un cas pédagogique (incident documenté, contre-exemple), la card peut dire « Cas pédagogique + checklist ».

**Toute désynchronisation card ↔ contenu détectée est un bug bloquant à corriger immédiatement.**

---

### Dimension E — Harmonisation visuelle

#### Règle E.1 — Cohérence visuelle cross-pages

**Nav** : 5 entrées (Préalables / Architectures / Modules / Déploiement / Ressources), identique sur toutes les pages, dans le même ordre, avec les mêmes libellés. Toute évolution se propage simultanément.

**Head banner** : même gabarit sur toutes les pages (logo, titre, accroche, hauteur, typo, padding, sticky).

**Footer** : identique partout (crédits Quai Alpha / Quest for Change, mention année, lien repo GitHub, lien méthodologie, lien à propos).

**Composants CSS** : centralisés dans `module-v3.css`. Composants spécifiques inline acceptés uniquement si utilisés sur **une seule page**. Dès la 2ème utilisation, migration obligatoire dans `module-v3.css`. Couleurs hardcodées interdites (variables CSS du design system uniquement : `--color-primary`, `--color-surface`, etc.). Espacements en `var(--space-X)`, pas en `rem` absolus.

**Sommaire (`module-toc`)** : format unique **emoji-style** (`<span class="toc-icon">EMOJI</span>Titre court`). Pas de variante numérotée. Bibliothèque d'emojis canoniques par type de section : Annexe § 4.E.1.

**Contraste obligatoire sur fonds foncés** : sur les conteneurs à fond bleu foncé (`.exec-summary`, `.case-deep-final`, `.archi-block`), aucun élément texte ne doit hériter ou recevoir une couleur sombre (paragraphes, listes, cellules, headings h2/h3/h4, `<strong>`, liens). Détails et règles CSS défensives : Annexe § 4.E.2.

#### Règle E.2 — Responsive obligatoire par défaut (mobile-first défensif)

Toute nouvelle section, tout nouveau composant CSS, tout nouveau bloc HTML ajouté à la plateforme **doit intégrer la dimension responsive dès sa conception**. Trois breakpoints actifs sur le site :

- **`< 900px`** : `.module-layout` 2 colonnes → 1 colonne, TOC en accordéon mobile
- **`< 768px`** : padding/marges des sections réduits, icônes section 56 → 44 px, tableaux en scroll horizontal défensif, exec-summary compacte
- **`< 480px`** : nav compressée (logo 56 px, libellé site masqué), titres h1 réduits, grilles secondaires forcées en 1 colonne

**Le contrat opérationnel** :

1. **Padding > `var(--space-5)`** (24 px) → override mobile obligatoire pour ramener à `var(--space-4)` (16 px) ou moins.
2. **Grille > 1 colonne** (`grid-template-columns: repeat(N, ...)` ou `repeat(auto-fit, minmax(Xpx, 1fr))` avec X > 280) → vérifier l'effondrement à 1 colonne en dessous de 480 px.
3. **Police > 1.5 rem** (h1, stat-num, hero) → utiliser `clamp(min, vw, max)` OU prévoir un override `@media (max-width: 480px)`.
4. **Tableau** (`<table>` ou `.tool-table`, `.compare-table`, `.decision-matrix`, `.tech-comparison-table`, `.rules-matrix`, `.trouble-table`) → la règle générale `@media (max-width: 768px) { ... display: block; overflow-x: auto; }` couvre par défaut. Pour les tableaux à largeur fixe (rare), prévoir un wrapper `<div class="table-scroll">`.
5. **SVG schémas** (`.schema-svg-wrap`, `.archi-flow`) → couverts par défaut via `overflow-x: auto` à 768 px. Ne pas définir de `width` fixe en pixels sur les `<svg>` (utiliser `width="100%"` + `viewBox`).
6. **Composant à `padding` en pixels** (rare, à éviter) → utiliser `var(--space-X)` qui s'adapte aux overrides.

**Où ajouter les overrides** :

- Composant **structurel global** (nav, footer, hero home) → `css/style.css` (chargé par toutes les pages, y compris `index.html` et `about.html`)
- Composant **propre aux modules / fiches PR / fiches DEP** → `css/module-v3.css` (chargé sur ces pages uniquement)
- Style **inline** sur une seule page (`<style>` dans le `<head>`) → l'auteur doit inclure son propre `@media` dans le même `<style>`

**Anti-patterns interdits** (cf. J.1 #15) :
- Composant qui pousse un scroll horizontal sur le viewport mobile (≤ 768 px) lors d'un test rapide DevTools.
- Tableau sans `overflow-x: auto` ni wrapper scrollable.
- Police `font-size` en pixels (`12px`) sur du texte de contenu — utiliser `rem` ou `var(...)` pour respecter le scaling utilisateur.

**Validation manuelle attendue à chaque PR éditoriale** : ouvrir la page modifiée dans DevTools Chrome/Firefox aux 3 viewports de référence (375 px, 768 px, 1024 px) et vérifier qu'aucun scroll horizontal involontaire n'apparaît, et que les composants restent lisibles. À ajouter à la checklist de PR ci-après.

**Validation automatisée** : l'audit `audit_responsive_basics()` (rule 15) flagge les styles inline `<style>` qui ajoutent une grille ou un padding > 24 px sans `@media` associé dans le même bloc.

---

### Dimension F — Pattern structurel obligatoire

#### Règle F.1 — Squelette HTML des modules CU, préalables PR, fiches DEP

Tout nouveau module CU, toute fiche PR, toute fiche DEP doit suivre cette ordonnance **non négociable** (9 blocs) :

```html
<body>
  <div class="reading-progress" id="readingProgress"></div>          <!-- 1. Reading progress -->
  <nav class="nav scrolled" id="nav">…</nav>                          <!-- 2. Nav harmonisée -->
  <header class="module-hero">                                        <!-- 3. Hero -->
    <div class="module-hero-inner">
      <a href="…" class="module-back">← Retour</a>
      <div class="module-badges">…</div>
      <h1>EMOJI Titre métier</h1>                                     <!-- h1 emoji ouvrant -->
      <p class="module-subtitle">…</p>
    </div>
  </header>
  <div class="module-layout">                                         <!-- 4. Layout 2 colonnes -->
    <aside class="module-toc">…</aside>                               <!-- TOC sticky emoji-style -->
    <main class="module-main">
      <section class="module-section" id="executive-summary">         <!-- 5. Executive summary -->
        <div class="exec-summary">
          <div class="exec-summary-label">⚡ L'essentiel…</div>
          <h2>…</h2>
          <div class="exec-takeaways">
            <div class="exec-takeaway">
              <div class="exec-takeaway-num">1</div>                  <!-- num pas icon -->
              <p>…</p>
            </div>
            <!-- 4 takeaways au total -->
          </div>
          <div class="exec-stats">…</div>                              <!-- 3-4 stats -->
          <div class="exec-when">…</div>                               <!-- public cible -->
        </div>
      </section>
      <section class="module-section" id="section-1">                  <!-- 6. Sections numérotées -->
        <div class="module-section-header">                            <!-- header structuré -->
          <div class="module-section-icon icon-context">1</div>
          <div class="module-section-title">
            <div class="section-number">Section 1</div>
            <h2>Titre métier</h2>
          </div>
        </div>
        …
      </section>
      …
      <section class="module-section" id="ressources">                  <!-- 7. id="ressources" -->
        <div class="module-section-header">…</div>
        <div class="callout callout-info">
          Pour le panorama complet, voir la
          <a href="../ressources.html#bibliographie">page Ressources</a>.
        </div>
        <div class="resources-cat">
          <h3>📰 Articles de fond</h3>                                 <!-- 4 sous-rubriques externes -->
          <ul>…</ul>
        </div>
        <div class="resources-cat"><h3>🎓 Tutoriels &amp; cas pratiques</h3>…</div>
        <div class="resources-cat"><h3>📚 Documentation officielle &amp; études</h3>…</div>
        <div class="resources-cat"><h3>👥 Communautés &amp; veille</h3>…</div>
      </section>
    </main>
  </div>
  <footer class="footer">…</footer>                                    <!-- 8. Footer harmonisé -->
  <script src="../js/module-v3.js"></script>                           <!-- 9. JS module-v3 -->
</body>
```

**Composants centralisés à utiliser (jamais redéfinir en `<style>` inline)** : voir Annexe § 4.F.1.

**Référence canonique** : `modules/cu-008-knowledge-base-rag.html`. En cas de doute structurel, copier ce fichier comme base.

---

### Dimension G — Spécialisation des rôles

#### Règle G.1 — Cowork = matière MD / Claude Code = construction HTML

**Cowork** produit le contenu éditorial, le sourcing, les gloses, les écueils, les briefs structurés — **en MD uniquement**. Cowork ne produit plus de mockup HTML depuis v3.6.2 (cette règle est née du constat que les mockups Cowork dérivaient systématiquement du pattern de référence).

**Claude Code** construit le HTML des nouveaux modules à partir du gabarit canonique `cu-008-knowledge-base-rag.html` et de la matière MD fournie par Cowork. Claude Code valide la conformité au pattern (Règle F.1) et au CSS centralisé (Règle E.1) avant d'intégrer. Tout commit qui déroge doit le signaler explicitement.

---

### Dimension H — Format auto-diagnostic standard

#### Règle H.1 — Auto-diagnostic interactif obligatoire

Toute section nommée **« Auto-diagnostic »** doit respecter **3 propriétés non négociables** :
1. **Form interactif** (`<form>` avec inputs radio, checkbox, textarea, select) — pas de checklist statique non interactive
2. **Génération d'un plan d'action** dynamique via JS, personnalisé selon les réponses (pas seulement un score)
3. **Export téléchargeable** en `.txt` ou `.md`, avec persistance `localStorage` recommandée

**Si la section ne respecte pas ces 3 propriétés**, elle ne peut PAS être nommée « Auto-diagnostic ». Renommer en « Checklist d'éligibilité », « Checklist projet », « Checklist sécurité » ou équivalent.

Référence d'implémentation : `modules/cu-023-devis-intelligent.html` (pattern auto-diag 8 questions Oui/Non avec verdict 3 niveaux).

---

### Dimension I — Renvois internes contextualisés

#### Règle I.1 — Renvois internes dans le corps, ressources externes en section finale

Les renvois internes (autres modules CU, préalables PR, fiches DEP, fiches outils de `ressources.html`, page Architectures) **vivent dans le corps du module au fil du texte, contextualisés**. Ils **ne doivent PAS être récapitulés** dans la section finale `id="ressources"` (qui est réservée aux **ressources externes** — Schéma A : 4 sous-rubriques externes uniquement).

**Lien obligatoire à la 1re mention significative d'un outil** ayant une fiche dans `ressources.html` : `<a href="../ressources.html#nom-outil" class="tool-link">Nom de l'outil</a>`.

**Précisions opérationnelles (v3.9)** :
- La règle s'applique sur **toute page** du Hub (modules, préalables, déploiement, architectures, index) : chaque page doit linker la **première occurrence non-liée** de chaque outil cité qui possède une fiche `tool-card` dans `ressources.html`.
- Les occurrences suivantes dans la même page ne sont **pas** à linker (évite la surcharge visuelle).
- Le label du lien reprend exactement le nom mentionné dans le texte (alias acceptés : `Mistral Large` → `#mistral`, `Claude Code` → `#claude-code`, `ChatGPT Atlas` → `#atlas`).
- Zones à exclure du wrappage automatique : `<a>`, `<code>`, `<pre>`, `<script>`, `<style>`, `<svg>`, `<aside class="module-toc">`, attributs HTML.
- Outils dont le nom est homographe d'un mot usuel (Make, v0, Comet, Operator, Atlas, Crayon, Whisper) → décision manuelle au cas par cas.

**Liste des ancres à jour** : `grep -oE '<article class="tool-card" id="[^"]+"' ressources.html`. Toute nouvelle fiche outil ajoutée dans `ressources.html` ouvre un cycle de revue cross-site (cf. `site-web-prep/link-tools-to-resources.py` — script idempotent qui ajoute la première mention par page).

**Cross-links obligatoires sur paires sensibles** (voir Annexe § 4.I.1 pour la liste complète) : CU-015 ↔ CU-027, CU-021 ↔ CU-024, triptyque CU-001/011/012, CU-014 ↔ CU-026, etc.

**Audit automatisé** : la fonction `audit_tool_link_first_mention()` de `audit-global.py` détecte les mentions d'outils non-liées sur les pages de contenu (rule I.2).

---

### Dimension J — Anti-patterns interdits

#### Règle J.1 — Liste exhaustive des anti-patterns

Les patterns suivants sont **interdits** dans tout module / fiche PR / fiche DEP :

1. ❌ `<main>` direct sans `module-layout` 2 colonnes
2. ❌ Section finale avec un autre id que `id="ressources"` (jamais `id="section-N"`)
3. ❌ `.exec-takeaway-icon` (emoji texte) au lieu de `.exec-takeaway-num` (numéro 1-2-3-4)
4. ❌ `<style>` inline qui redéfinit `.exec-summary`, `.exec-takeaway`, `.alert-block`, `.checklist-block`, `.stat-block`, `.tool-table`, `.pull-quote`, `.arch-callout`, `.case-deep-actor` (centralisés)
5. ❌ Couleurs hardcodées dans `<style>` inline (`#1e3a8a`, `#dc2626`, etc.) — variables CSS uniquement
6. ❌ Espacements absolus dans `<style>` inline (`padding: 1.5rem`) — `var(--space-X)` uniquement
7. ❌ `<h1>` sans emoji ouvrant
8. ❌ `<a>` imbriqué dans le contenu d'une card cliquable de la home
9. ❌ Sous-rubriques internes (« Modules complémentaires », « Préalables associés ») dans la section finale `id="ressources"`
10. ❌ Section nommée « Auto-diagnostic » sans form interactif + génération plan + export
11. ❌ Codes internes (`CU-XXX`, `PR-XX`, `DEP-XX`) visibles dans titres / cards / badges / corps de texte
12. ❌ Fallback emoji `📌` répété sur > 1 entrée d'un sommaire (chaque section a son emoji contextuel)
13. ❌ Placeholders STASH résiduels post-bulk-patch (`§STASH-XX§`)
14. ❌ NUL bytes résiduels (`\x00`) dans les fichiers HTML
15. ❌ Section ou composant ajouté **sans dimension responsive** (cf. E.2) — pas de scroll horizontal involontaire à ≤ 768 px, pas de tableau sans `overflow-x` défensif, pas de grille fixe > 1 colonne maintenue sous 480 px

Détails et historique de détection : Annexe § 4.J.1.

---

### Dimension K — Audit automatisé obligatoire

#### Règle K.1 — audit-global.py exécuté avant et après chaque PR

`site-web-prep/audit-global.py` couvre les **13 règles automatisées** issues du présent référentiel :

```bash
python3 site-web-prep/audit-global.py
# Sortie attendue : Total hits : 0
# Code retour : 0 (succès) ou 1 (hits détectés)
```

Toute PR doit afficher `Total hits : 0` au démarrage et à la clôture.

Si une nouvelle règle structurelle est introduite dans ce référentiel (RULES.md), **une fonction d'audit correspondante doit être ajoutée à `audit-global.py` dans la même PR**. Pas de règle descriptive sans audit exécutoire — sinon la règle dérive (cf. Annexe § 4.K.1 sur l'historique des 14 sous-versions v1.5.X qui étaient des règles non auditées).

---

## 2. Checklist obligatoire avant tout commit / PR

```
☐ J'ai lu RULES-IMPLEMENTATION.md v1.6 en intégralité avant de commencer.
☐ audit-global.py exécuté au démarrage → Total hits : 0

Sourcing (A.1, A.2, A.3) :
☐ Tous mes chiffres ont une source datée et un lien vérifiable.
☐ Aucune statistique inventée. Aucune citation fictive.
☐ RetEx d'entreprises nommées uniquement si source institutionnelle.
☐ Aucun cabinet de conseil intermédiaire mentionné en promotion.

Cohérence numérique (B.1, B.2) :
☐ Si j'ai modifié un comptage, j'ai mis à jour TOUS les lieux d'apparition (cross-site + intra-page).
☐ Aucune mention « v3.X » visible côté UX.

Niveau de langue (C.1, C.2) :
☐ Aucun jargon technique sans glose à la 1re occurrence.
☐ Aucun code interne (PR-XX, CU-XXX, DEP-XX) visible (hors URL/ancres et A1-A4).

Posture éditoriale (D.1, D.2) :
☐ Pas de biais sectoriel/territorial dominant (audit § 4.D.1).
☐ Card index ↔ contenu réel cohérent.

Harmonisation visuelle (E.1) :
☐ Nav 5 entrées identique cross-pages.
☐ Head banner + footer identiques.
☐ Sticky TOC + scroll-spy + reading progress fonctionnels.
☐ Sommaire format emoji-style.
☐ Aucune couleur hardcodée, aucun espacement absolu en `<style>` inline.
☐ Aucun texte sombre dans conteneur à fond foncé.

Responsive (E.2) :
☐ Toute nouvelle section / composant ajouté → override `@media` mobile prévu (768 px et 480 px).
☐ Aucun scroll horizontal involontaire à 375 px (test DevTools).
☐ Tableaux ajoutés → couverts par `display: block; overflow-x: auto` du breakpoint 768 px.
☐ Grilles ajoutées → effondrement à 1 colonne à 480 px vérifié.
☐ `audit-global.py` règle 15 sans hit.

Pattern structurel (F.1) :
☐ Squelette HTML 9 blocs respecté sur tout nouveau module/PR/DEP.
☐ Référence canonique CU-008 consultée en cas de doute.

Spécialisation des rôles (G.1) :
☐ Cowork = matière MD. Claude Code = HTML.

Auto-diagnostic (H.1) :
☐ Toute section « Auto-diagnostic » a form interactif + plan + export.

Renvois internes (I.1) :
☐ Renvois internes dans le corps, contextualisés.
☐ Section finale id="ressources" en Schéma A (4 sous-rubriques externes).
☐ 1re mention significative d'un outil sur la page → lien `<a href="ressources.html#anchor" class="tool-link">Nom</a>`.
☐ `audit-global.py` règle 14 sans hit (sinon, exécuter `site-web-prep/link-tools-to-resources.py`).

Anti-patterns (J.1) :
☐ Aucun des 14 anti-patterns interdits présent (vérification grep).

Audit final (K.1) :
☐ audit-global.py exécuté en clôture → Total hits : 0
☐ Description de PR pointe vers le brief de l'itération + résume les écarts au RULES s'il y en a (et pourquoi).
```

---

## 3. Cohérence avec audit-global.py

Mapping des **15 règles automatisées** dans `audit-global.py` vers les règles RULES v1.6 :

| Fonction audit | Règle RULES v1.6 |
|---|---|
| `audit_coherence_numerique` | B.1 |
| `audit_coherence_intra_page` | B.1 |
| `audit_versioning_front` | B.2 |
| `audit_biais_sectoriel_territorial` | D.1 |
| `audit_structure_module_section_header` | F.1 |
| `audit_callout_intro_margin` | F.1 |
| `audit_codes_internes_visibles` | C.2 |
| `audit_lien_outil_obligatoire` (legacy) | I.1 |
| `audit_tool_link_first_mention` (rule 14) | I.1 (renvois cross-site) |
| `audit_responsive_basics` (rule 15) | E.2 |
| `audit_coherence_card_contenu` | D.2 |
| `audit_sommaire_canonique` | E.1 |
| `audit_contraste_fonds_fonces` | E.1 |
| `audit_placeholders_stash_residuels` | J.1 (#13) |
| `audit_nul_bytes` | J.1 (#14) |

**Règles RULES v1.6 sans audit automatisé** (à vérifier manuellement ou à automatiser dans une future itération) :
- A.1, A.2, A.3 (sourcing — vérification humaine via revue)
- C.1 (jargon — vérification humaine)
- E.1 partiel (composants CSS inline — à automatiser)
- F.1 partiel (squelette HTML 9 blocs — partiellement automatisé)
- G.1 (rôles Cowork / Claude Code — règle de process, pas auditable)
- H.1 (format auto-diagnostic — à automatiser)
- J.1 (#1 à #12 partiellement automatisés — à compléter)

**Opportunité** : compléter `audit-global.py` pour automatiser les règles manquantes au fil des itérations. Chaque nouvelle règle structurelle codifiée dans RULES doit s'accompagner d'une fonction d'audit dans la même PR (cf. K.1).

---

## 4. Annexes — Compendium d'exemples détaillés

> Cette section regroupe **les exemples concrets, anti-patterns historiques, scripts d'audit et gloses canoniques** issus des 14 sous-versions v1.5.X. Elle complète les 13 règles essentielles ci-dessus sans les alourdir.

### 4.A.1 — Sourcing (exemples)

**Bon exemple** :
> **+270 % de ROI moyen** sur les déploiements IA générative en entreprise (*Microsoft New Future of Work Report 2025*, données 2024 sur 1 200 organisations).

**Mauvais exemple (à proscrire)** :
> Les études montrent que l'IA permet d'augmenter la productivité de manière significative.

**Format HTML obligatoire** :
```html
<p><strong>+270 % de ROI moyen</strong> sur les déploiements IA générative
(<a href="https://aka.ms/AINewFutureOfWork" target="_blank" rel="noopener">
Microsoft New Future of Work Report 2025</a>).</p>
```

### 4.B.1 — Glossaire des chiffres-clés

| Chiffre | Valeur courante (mai 2026, v3.8) | Lieux d'apparition |
|---|---|---|
| Modules CU | **27** (CU-001 → CU-027) | home, page modules, à propos, méta |
| Préalables PR | **8** (PR-01 → PR-08) | prealables.html, home, à propos |
| Fiches Déploiement DEP | **8** (DEP-01 → DEP-08) | deploiement.html, home, à propos |
| Fiches outils | **104** (16 catégories) | ressources.html, à propos, hero ressources |
| Patterns architecture | 4 + 1 hybride | architectures.html, à propos |
| Entrées nav | **5** (Préalables / Architectures / Modules / Déploiement / Ressources) | toutes pages |
| Familles métier (modules) | **6** (Découverte / Marketing & croissance / Décision & gouvernance / Fonctions support / Industrie / Architectures agentiques) | home |
| Échelle complexité | **4** niveaux (⭐ Initiation / ⭐⭐ Opérationnel / ⭐⭐⭐ Avancé / ⭐⭐⭐⭐ Expert) | home (filtre), badges modules |

**Statistiques macro à synchroniser cross-pages** : 95 % MIT NANDA, +270 % Microsoft, 76 % France Num (puis 26 % France Num 2025 + 55 % Bpifrance Le Lab), ×5 productivité PwC, 77 000 offres PwC, 3,7× IDC Copilot, consensus 70-95 % Gartner/McKinsey/Deloitte, 80-95 % causes orga d'échec, 58 % enjeu vital Bpifrance.

### 4.C.1 — Gloses canoniques (jargon)

| Terme | Glose obligatoire à la 1re occurrence |
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
| MCP | « Model Context Protocol : protocole standardisé pour donner aux agents l'accès à des outils et données » |

### 4.D.1 — Biais sectoriel/territorial : exemples et audit

**Anti-pattern observé v3.7.7 sur CU-018** : 277 marqueurs sectoriels/territoriaux dont 110 mentions « bois » (40 %), 92 mentions de l'écosystème R&D Grand Est (ENSTIB / LERMAB / CRAN / ENACT), 34 mentions territoriales. Refondu en v3.7.8 pour réintroduire 3-4 filières comparables (textile, métallurgie, plasturgie, agroalimentaire) et un panorama national/européen.

**Script d'audit** : voir `audit-global.py` fonction `audit_biais_sectoriel_territorial()`.

### 4.E.1 — Bibliothèque d'emojis canoniques pour le sommaire

| Section | Emoji |
|---|---|
| Synthèse rapide / L'essentiel | ⚡ |
| Ce que tu sauras faire | 🎯 |
| Le contexte / Ce qui a changé | 🧭 |
| Comment ça fonctionne / Schéma / Architecture | 🛠️ |
| Étapes en détail | 📋 |
| Stack et outils / Panorama outils | ⚙️ |
| Cas d'étude / Étude de cas / RetEx | 🎯 ou 📊 |
| Pièges à éviter / Écueils / Troubleshooting | ⚠️ |
| Auto-diagnostic / Checklist d'éligibilité | 🔎 |
| Pour aller plus loin / Ressources | 📚 |
| Plan d'action 30 jours | 🚀 |
| Quiz | ✅ |
| Coût / ROI / Financement | 💰 ou 💸 |
| Cadre juridique / Conformité / RGPD / AI Act | ⚖️ |
| Sécurité / Garde-fous | 🛡️ |
| Multi-agents / IA agentique | 🤖 |
| Veille / Signaux / Alertes | 🔭 ou 📡 |
| Vision industrielle / Contrôle qualité | 👁️ |
| Maintenance / Capteurs | 🔧 |
| Newsletter / Email / CRM | ✉️ |
| Pattern Fat Skills / architecture compounding | 🧱 |
| Gouvernance / Identité agents | 🪪 |
| Knowledge management / Vault personnel | 🧠 |

### 4.E.2 — Contraste fonds foncés : règle CSS défensive

Sur les conteneurs `.exec-summary`, `.case-deep-final`, `.archi-block`, aucun texte sombre. Règle CSS défensive obligatoire dans `module-v3.css` :

```css
.exec-summary [style*="color: var(--color-text"],
.exec-summary [style*="color: var(--color-primary"],
.case-deep-final [style*="color: var(--color-text"],
.case-deep-final [style*="color: var(--color-primary"],
.archi-block [style*="color: var(--color-text"],
.archi-block [style*="color: var(--color-primary"] {
  color: rgba(255, 255, 255, 0.88) !important;
}
.exec-summary p, .exec-summary li, .exec-summary td, .exec-summary h2, .exec-summary h3, .exec-summary h4, .exec-summary strong,
.case-deep-final p, .case-deep-final li, .case-deep-final h3, .case-deep-final h4,
.archi-block p, .archi-block li, .archi-block h3, .archi-block h4 {
  color: inherit;
}
```

Origine de la règle : bugs cascade CSS conflictuelle v3.7.10 et v3.7.11.

### 4.F.1 — Composants CSS centralisés à ne pas redéfinir inline

- **Layout** : `.module-layout` · `.module-toc` · `.module-main` · `.module-toc-list`
- **Hero** : `.module-hero` · `.module-hero-inner` · `.module-back` · `.module-badges` · `.module-subtitle`
- **Synthèse** : `.exec-summary` · `.exec-summary-label` · `.exec-takeaways` · `.exec-takeaway` · `.exec-takeaway-num` · `.exec-stats` · `.exec-stat` · `.exec-when`
- **Section** : `.module-section` · `.module-section-header` · `.module-section-icon` · `.module-section-title` · `.section-number`
- **Composants typés** : `.callout` (`.callout-info` / `.callout-warn`) · `.alert-block` · `.alert-ai-act` · `.checklist-block` · `.diagnostic` · `.case-deep-actor` (variantes `.warm`, etc.) · `.pull-quote` · `.resources-cat` · `.stat-block` · `.tool-table` · `.arch-callout`
- **Niveaux** : `.card-badge.n1` · `.n2` · `.n3` · `.n4`
- **Axes métier** : `.card-badge.axe-a` à `axe-e` · classe spéciale agentique

Si un composant nouveau apparaît sur 2+ modules, **migration obligatoire vers `module-v3.css` dans le commit qui l'introduit la 2ème fois**.

### 4.I.1 — Cross-links obligatoires sur paires sensibles

- **CU-015 ↔ CU-027** : asynchronicité agentique managériale vs guide d'achat dev applicatif
- **CU-021 ↔ CU-024** : compta fournisseur entrante vs cycle commercial sortant
- **CU-001 ↔ CU-011 ↔ CU-012** : triptyque veille progressif (réflexe individuel → système permanent → système agentique)
- **CU-005 ↔ CU-023** : propositions B2B complexes vs devis simples (porte d'entrée IA)
- **CU-014 ↔ CU-026** : architecture multi-agents vs gouvernance managériale agents
- **CU-026 ↔ CU-020, PR-05** : gouvernance agents (angle managérial) ↔ conformité RGPD/AI Act + sécurité IA

### 4.I.2 — Renvois outils → `ressources.html#anchor` (mise en pratique)

**Principe** : sur **toute page** du Hub, la **première mention non-liée** de chaque outil disposant d'une `tool-card` dans `ressources.html` doit être wrappée dans un lien vers la fiche.

**Pattern HTML attendu** :

```html
<!-- Première occurrence : linkée -->
<p>Pour le retrieval, on utilise <a href="../ressources.html#qdrant" class="tool-link">Qdrant</a>
   et un LLM type <a href="../ressources.html#claude" class="tool-link">Claude</a>.</p>

<!-- Occurrences suivantes dans la même page : pas linkées -->
<p>Qdrant tient la charge sur les volumétries PME ; Claude reste l'option par défaut.</p>
```

**Outils homographes à NE PAS linker automatiquement** (décision manuelle requise) : `Make`, `v0`, `Comet`, `Operator`, `Atlas`, `Crayon`, `Whisper`. Le contexte décide.

**Aliases acceptés** (label du lien = ce qui est écrit dans le texte) :
- `Mistral Large`, `Mistral 7B`, `Mistral AI`, `Mistral Forge` → tous vers la fiche Mistral (`#mistral`) sauf `Mistral Agents SDK` (`#mistral-agents`) et `Mistral Forge` (`#mistral-forge`)
- `Claude Code` → `#claude-code` (≠ `#claude`)
- `ChatGPT Atlas` → `#atlas` (et non `#gpt`)
- `GPT-4`, `GPT-5`, `GPT-4o`, `ChatGPT` → tous vers `#gpt`
- `pgvector` ou `Postgres pgvector` → `#pgvector`

**Zones à exclure du wrappage** : tout contenu à l'intérieur de `<a>`, `<code>`, `<pre>`, `<script>`, `<style>`, `<svg>`, `<aside class="module-toc">`, `<title>`, `<meta>`, ou un attribut HTML.

**Outils opérationnels** :
- `site-web-prep/link-tools-to-resources.py` — script idempotent qui linke la première mention par page (peut être ré-exécuté après ajout d'un nouvel outil dans `ressources.html`)
- `audit-global.py` règle 14 — flagge tout fichier où un outil mentionné n'a aucun lien vers sa fiche

**Quand exécuter le script** :
- Après ajout d'une nouvelle `tool-card` dans `ressources.html`
- Après création d'un nouveau module / préalable / fiche DEP
- Lors d'une refonte éditoriale élargie (ex : itération v3.X qui touche plusieurs modules)

### 4.J.1 — Anti-patterns historiques de détection

Liste des incidents qui ont motivé chaque entrée de la Règle J.1 :

| # | Anti-pattern | Origine historique |
|---|---|---|
| 1 | `<main>` sans `module-layout` | Mockups Cowork v3.6 (CU-023/024/027 initial, refondu v3.6.1) |
| 2 | `id="section-N"` au lieu de `id="ressources"` | 17 modules détectés v3.6.2 |
| 3 | `.exec-takeaway-icon` au lieu de `.exec-takeaway-num` | 18 modules legacy v3.7.14 |
| 4 | `<style>` inline composants centralisés | 81 lignes CU-023, 71 lignes CU-027 (v3.6.2) |
| 5 | Couleurs hardcodées | CU-002, CU-003, CU-006 `.case-deep-actor` (v3.7.14) |
| 6 | Espacements absolus | Détection v1.4 |
| 7 | h1 sans emoji | PR-07 v3.6.2 corrigé v3.7 |
| 8 | `<a>` dans card cliquable home | Bug CU-020 v3.6 |
| 9 | Sous-rubriques internes section finale | 19 hits sur 6 préalables (v3.7.14) |
| 10 | « Auto-diagnostic » sans interactivité | CU-023 v3.6.0 statique |
| 11 | Codes internes visibles | 45 codes détectés v3.7.2 |
| 12 | Fallback 📌 répété | 31 emojis détectés v3.7.13 |
| 13 | Placeholders STASH | Bug bulk-patch v3.7.4 |
| 14 | NUL bytes | Bug bulk-patch v3.7.4 |

### 4.K.1 — Historique des 14 sous-versions v1.5.X (raison d'être de la refonte v1.6)

Entre v3.5 et v3.8, le référentiel RULES a accumulé 14 sous-versions :
- v1.5.1 (v3.7.1) : Nav 6→5 + § 1.2.5.1 anti-drift cross-bloc
- v1.5.2 (v3.7.2) : § 1.5.6.1 anti-codes-internes + § 1.5.6.2 lien outil obligatoire
- v1.5.3 (v3.7.4) : § 1.4.5 anti-bulk-patch-bug + § 1.4.6 audit contraste
- v1.5.4 (v3.7.5) : § 1.5.1.1 structure canonique `module-section-header`
- v1.5.5 (v3.7.6) : § 1.5.1.2 callout intro margin-bottom
- v1.5.6 (v3.7.7) : § 1.5 audit cohérence card↔contenu
- v1.5.7 (v3.7.8) : § 1.2.7 anti-biais sectoriel/territorial
- v1.5.8 (v3.7.9) : § 1.5.3 anti-`<pre>` text-art
- v1.5.9 (v3.7.10) : § 1.4.7 sommaire emoji + § 1.4.8 contraste élargi
- v1.5.10 (v3.7.11) : post-mortem cascade CSS + regex agressive
- v1.5.11 (v3.7.12) : **Garde-fou `audit-global.py`** (point pivot)
- v1.5.12 (v3.7.13) : § 1.4.7 fallback 📌
- v1.5.13 (v3.7.14) : Lot 4 mise à jour en-tête + .case-deep-actor.warm
- v1.5.14 (v3.8) : Glossaire 27 modules / 99 fiches (CU-026 + 4 nouvelles fiches)

Constat : chaque sous-version a corrigé un écart spécifique, mais l'ensemble a perdu en lisibilité. La refonte v1.6 consolide ces apports en 13 règles essentielles + annexes, sans perte d'information (cf. `RULES-MIGRATION-v1.5-vers-v1.6.md` pour la traçabilité complète).

---

## 5. Décisions éditoriales structurantes (rappel)

- **Pas de pub pour acteurs commerciaux** : pas de fiches sur cabinets de conseil, intégrateurs, agences. Les RetEx mentionnent les cas, pas les prestataires intermédiaires.
- **Distinction CU / PR / DEP / Architectures** : voir Annexe ou briefs historiques v3.4, v3.5, v3.7.
- **Pas de reframing géographique** : le site reste calibré PME/ETI Grand Est en cible primaire, ambition rayonnement large.
- **Pas de refonte du design system** sans validation explicite Blaise.
- **Pas d'ajout de catégorie d'outils** sans validation explicite Blaise.

---

## 6. Évolution de ce fichier

Ce fichier est **vivant**. À chaque itération majeure, Cowork ou Claude Code peut proposer des amendements via PR dédiée. Toute évolution doit faire l'objet d'une discussion explicite avec Blaise avant merge.

**Principe directeur post-refonte v1.6** : **toute nouvelle règle structurelle doit être accompagnée d'une fonction d'audit dans `audit-global.py` dans la même PR**. Sans cela, la règle dérive (cf. constat des 14 sous-versions v1.5.X qui étaient des règles non auditées).

Versionnage : on incrémente la version en tête de fichier. v1.6 → v1.7 (refonte structurelle) ou v1.6.1 (correctif mineur, à éviter).

---

## 7. Historique condensé

- **v1.0** — 9 mai 2026 : création initiale
- **v1.1** — post v3.5.3 : premier audit qualité
- **v1.2** — post v3.6.1 : harmonisation CU-023/024/027
- **v1.3** — v3.6.2 : Schéma A, anti-patterns § 1.5.3, rôles Cowork/Claude Code, format auto-diag
- **v1.4** — post v3.6.2 : checklist statique, card↔contenu, espacements `var(--space-X)`
- **v1.5** — v3.7 : glossaire actualisé (26 modules, 95 fiches, 5 nav)
- **v1.5.1 à v1.5.14** — v3.7.1 → v3.8 : 14 sous-versions de patches cumulés (détail § 4.K.1)
- **v1.6** — refonte simplifiée : 13 règles essentielles + annexes + alignement audit-global.py. Pas de nouvelle règle. Pas de règle abandonnée. Consolidation pure (cf. `RULES-MIGRATION-v1.5-vers-v1.6.md` pour le mapping exhaustif).
- **v1.6.1** — v3.10 : glossaire chiffres-clés actualisé (préalables PR : 7 → 8 suite ajout de PR-08 « Financer son projet IA en 2026 »).
- **v1.6.2** — v3.11 : glossaire chiffres-clés actualisé (fiches outils : 99 → 104, 15 → 16 catégories suite création nouvelle catégorie « Stack agentique Claude / Anthropic » avec 5 nouvelles fiches : ECC, AgentShield, agentmemory, claude-smart, Onyx).

---

## 8. Contact & responsabilité

**Maintainer du référentiel** : Blaise Cavalli — blaise.cavalli@questforchange.eu

**Si tu lis ce fichier en tant que LLM / agent** : ton rôle est de t'y conformer, pas de l'interpréter. En cas de doute, demande à Blaise avant de commit.
