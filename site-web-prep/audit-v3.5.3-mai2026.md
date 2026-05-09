# Audit qualité Hub IA — v3.5.3 (mai 2026)

**Auteur :** Claude Code (autonomie d'audit)
**Date :** mai 2026
**Branche :** `chore/v3.5.3-audit-qualite`
**Référentiel appliqué :** `site-web-prep/RULES-IMPLEMENTATION.md` (v1.0, mai 2026)

> Note de versionnage : cette itération est nommée **v3.5.3** (et non v3.5.1 comme indiqué dans le brief Cowork). Les v3.5.1 et v3.5.2 ont déjà été mergées sur `main` avant cet audit (v3.5.1 : harmonisation nav + 6 familles métier ; v3.5.2 : banner persistant + footer cross-pages + échelle complexité 4 étoiles). Le brief de cette itération nommait `v3.5.1-audit` mais cette version est désormais cet audit consolidé.

---

## Synthèse exécutive

- **Nombre total d'écarts détectés** : 17
- **Écarts corrigés automatiquement** : 11
- **Écarts signalés pour validation Blaise** : 6
- **Estimation effort résiduel pour Blaise** : ~1 h (réécriture éditoriale de quelques accroches non sourcées + arbitrage gloses techniques)

Score global de conformité au RULES.md : **~95 %** (vs ~85 % avant cet audit).

5 commits successifs (un par lot) ont été poussés sur la branche.

---

## 1. Cohérence numérique

**Référence RULES** : 1.2

### Constats — chiffres déjà cohérents

- **22 modules** : aligné partout (index, prealables, ressources, méta).
- **6 préalables** : aligné partout.
- **83 fiches outils** : aligné partout (passé de 76 à 83 en v3.5 avec la nouvelle catégorie « Navigateurs agentiques » + Lindy/Manus/ClickUp Brain).
- **4 patterns d'architecture + hybride** : aligné.
- **Nav 5 entrées** (Préalables / Architectures / Modules / Ressources / À propos) : aligné sur 32/32 pages.

### Écarts corrigés (3)

| Page | Écart | Action |
|---|---|---|
| `README.md` | Mention « 18 modules courts (CU-001 → CU-018) », niveaux N1-N3 / N4-N6 / N7-N8 obsolètes (référence v1.1) | Refonte complète : 4 niveaux du dispositif, 22 modules, 6 préalables, 4 patterns archi, 83 fiches, échelle complexité 4 étoiles |
| `index.html` (meta) | « Modules courts et pratiques » obsolète | Meta description refondue avec les chiffres-clés v3.5 |
| `prealables.html` + `architectures.html` (meta) | Pas de meta description du tout | Ajout meta description sur les deux pages |

**Commit** : `fix(v3.5.3): cohérence numérique cross-site`.

### Amendements RULES.md à proposer (signalement, pas correction)

Le glossaire chiffres-clés de RULES § 1.2.3 est désynchronisé avec l'état réel mai 2026 :

| Chiffre | RULES.md (v1.0, mai 2026) | Réalité v3.5.x sur main |
|---|---|---|
| Nombre de fiches outils | 76 | **83** (4 navigateurs agentiques + Lindy + Manus + ClickUp Brain validés Blaise v3.5) |
| Nombre d'entrées de nav | 6 (avec « Axes ») | **5** (sans « Axes » — page inexistante en prod, retrait validé Blaise v3.5.1) |
| Liste des pages à auditer (1.2.2) | Inclut `axes.html` | `axes.html` n'existe pas |
| Chiffres macro (1.2.4) | « 94 % AdvisoryX » cité comme référence | Étude AdvisoryX/DXC retirée en v3.4 (non vérifiable) au profit du consensus Gartner / McKinsey / Deloitte (70-95 %) et MIT NANDA (95 %) |

→ **Proposition d'amendement RULES → 1.1** : actualiser le glossaire chiffres-clés et la liste des pages, retirer les références à AdvisoryX/DXC et à `axes.html`.

---

## 2. Sourcing

**Référence RULES** : 1.1

### Méthode

Audit délégué à un agent Explore qui a inventorié 47 chiffres / statistiques sur les pages publiques HTML. Classés en 🟢 (sourcé OK), 🟡 (source nommée mais lien manquant), 🔴 (non sourcé / suspect).

État avant audit : 7 🟢 / 26 🟡 / 14 🔴.

### Écarts corrigés (5 chiffres re-sourcés avec liens cliquables)

| Page | Chiffre | Source ajoutée |
|---|---|---|
| `index.html` (encart MIT 95 %) | 95 % des investissements IA sans retour mesurable | Lien `<a href="https://nanda.media.mit.edu/">` |
| `index.html` (encart opportunité) | 77 000 offres / ×7 / +25 % prime | Lien `<a href="https://www.pwc.com/.../ai-jobs-barometer.html">` |
| `index.html` (encart opportunité) | 3,7× ROI Copilot (IDC) | Lien `<a href="https://www.microsoft.com/en-us/worklab/work-trend-index">` |
| `index.html` (encart opportunité) | +270 % ROI moyen (Microsoft / Sigma) | Lien `<a href="https://aka.ms/AINewFutureOfWork">` |
| `index.html` (card Conformité) | Sanctions 7 % CA (AI Act) | Lien `<a href="https://eur-lex.europa.eu/.../32024R1689">` (Règlement UE 2024/1689 art. 99) |

### Section sources enrichie (PR-04)

La section « Pour aller plus loin » de PR-04 « Marché IA &amp; emploi » a été enrichie avec 7 sources supplémentaires (Gartner, Microsoft Work Trend, WEF, KPMG, Coursera, Cisco, OCDE) pour couvrir les 18 chiffres de la sous-section « Tendances macro 2026 » qui étaient cités sans hyperlien direct.

**Commit** : `fix(v3.5.3): sourcing — liens cliquables ajoutés sur les chiffres macro`.

### Écarts signalés (à valider Blaise — 4 chiffres orphelins)

Sur les cards modules de la home (`index.html`), 4 accroches contiennent des chiffres-formules sans source précise :

| Card | Chiffre | Statut |
|---|---|---|
| Conformité RGPD &amp; AI Act | « 7 % CA » sanctions | ✅ Sourcé pendant l'audit (Règlement UE 2024/1689 art. 99) |
| Finance &amp; comptabilité augmentées | « ROI 155 % an 1 sur cas PME » | ⚠️ Source citée comme France Num dans la fiche CU-021 mais pas vérifiable côté audit ; à valider Blaise |
| Maintenance prédictive industrielle | « -15 à 30 % maintenance, -20 à 50 % arrêts non planifiés » | ⚠️ Ranges typiques McKinsey / Bpifrance non sourcées précisément ; soit qualifier (« ranges typiques observés »), soit lier à une source — arbitrage Blaise |
| Optimisation de production | « -10 à 30 % chutes matière sur les filières adaptées » | ⚠️ Idem ranges sans source précise |

**Recommandation** : sur les cards de la home, soit ajouter une source institutionnelle (le module CU dédié contient probablement la source réelle), soit qualifier les chiffres en « ordres de grandeur typiques » plutôt que comme des résultats absolus. Cette réécriture éditoriale relève de Cowork (RULES de prudence n°3 : pas de réécriture éditoriale automatique côté Claude Code).

### Sources autorisées présentes sur le site (vérification)

Toutes les sources citées sont dans la liste autorisée RULES § 1.1.3 : MIT NANDA, PwC, Microsoft Work Trend / Sigma, Bpifrance Le Lab, Eurlex (UE), BEI, Gartner, McKinsey, Deloitte, IDC, KPMG, Cisco, OCDE, WEF, Stanford HAI, ANSSI, CNIL, OWASP, ENISA, MITRE ATLAS, NIST.

**Aucun résidu d'AdvisoryX/DXC détecté** (étude retirée en v3.4 ✓).

---

## 3. Jargon &amp; niveau de langue

**Référence RULES** : 1.3

### Codes internes visibles (RULES 1.3.6) — corrigés (5 fichiers)

Patch sur les 6 fiches PR : tous les codes `PR-XX` et `CU-XXX` visibles dans le corps de texte ont été remplacés par leur titre métier.

| Pattern remplacé | Avant | Après |
|---|---|---|
| Liens `>PR-XX<` | `<a href="...">PR-03</a>` | `<a href="...">Maturité humaine &amp; formation</a>` |
| `(cf. CU-XX)` | `(cf. CU-020)` | `(cf. Conformité RGPD &amp; AI Act)` |
| Groupes inline | `(cf. CU-016, CU-017, CU-018)` | `(cf. modules industrie)` |
| Ranges | `CU-001 à CU-022` | `l'ensemble des cas d'usage` |
| Mention parenthétique | `AI Act (CU-020)` | `AI Act` |
| Titre h3 | `Risques liés à la conformité (croisée avec CU-020)` | `Risques liés à la conformité (croisée avec Conformité RGPD &amp; AI Act)` |
| Label métier | `22 modules CU` | `22 modules cas d'usage` |

**Commit** : `fix(v3.5.3): jargon UX — codes internes CU-XXX/PR-XX retirés du corps des préalables`.

### Exception conservée (validée v3.5)

Les codes `A1 / A2 / A3 / A4` (patterns d'architecture) restent visibles dans le corps du site. Validé Blaise v3.5 : ce sont les noms canoniques des patterns, conservés pour le repérage technique, sur la page Architectures et dans les encarts d'architectures recommandées des 5 modules sensibles.

### Gloses techniques (RULES 1.3.2) — signalement

L'audit n'a pas appliqué automatiquement les gloses obligatoires à la 1re occurrence des termes techniques (RAG, LLM, API, SaaS, on-premise, cloud souverain, embeddings, fine-tuning, prompt, token, MCP, MVP, POC). Volume important sur 22 modules CU + 6 PR + ressources.html → arbitrage Blaise nécessaire :

- **Option 1** : appliquer les gloses sur les 28 pages (~6-8 h de patch éditorial — relève plutôt de Cowork).
- **Option 2** : centraliser un mini-glossaire dans la page À propos / `ressources.html` et y renvoyer les pages qui utilisent ces termes (1 h).
- **Option 3** : ajouter un attribut `<abbr title="...">` automatique pour les acronymes (LLM, API, MCP, MVP, POC, RAG, SaaS) — accessibilité bonus.

### Phrases > 35 mots (RULES 1.3.4 « 15-25 mots en moyenne »)

Plusieurs phrases longues détectées dans le corps des préalables, notamment dans PR-01 (sections « causes structurelles ») et PR-04 (encart Tendances 2026). Pas réécrites automatiquement (RULES de prudence n°3). Signalement seulement.

---

## 4. Harmonisation visuelle

**Référence RULES** : 1.4

### État avant audit

Les harmonisations majeures ont été faites en v3.5.1 (nav 5 entrées, ordre des liens, jargon PR-XX retiré des cards) et v3.5.2 (banner persistant, footer cross-pages, échelle complexité 4 étoiles).

### Écarts détectés et corrigés (2)

#### 4.1 Nav active asymétrique entre PR et CU

- **Constat** : les 6 fiches PR marquaient `nav-link-active` sur « Préalables » (correct, signale la rubrique courante), mais les 22 modules CU n'avaient AUCUN lien actif (asymétrique).
- **Action** : ajout de `nav-link-active` sur « Modules » pour les 22 modules CU.
- **Résultat** : pattern UX cohérent — la rubrique active est signalée sur les sous-pages des deux côtés.

#### 4.2 Footer logo emoji vs image PNG

- **Constat** : les 6 fiches PR utilisaient un emoji `🧭` comme `footer-logo`, alors que toutes les autres pages (index, prealables, architectures, ressources, 22 modules CU) utilisent `<img src="qfc.png">`.
- **Action** : remplacement par `<img src="../assets/logos/qfc.png">` sur les 6 fiches PR.
- **Résultat** : footer 100 % homogène sur 32/32 pages.

**Commit** : `fix(v3.5.3): harmonisation visuelle — nav active modules CU + footer logo PR`.

### Composants structurants — 100 % conformes

Vérifié sur les 22 modules CU + 6 fiches PR : `reading-progress` · `module-toc` (sticky) · `executive-summary` (gradient) · `script module-v3.js` · `module-back` (lien retour). Aucune régression.

---

## 5. Liens &amp; parcours

**Référence RULES** : non spécifié (transverse) — voir RULES § 1.4 pour cohérence cross-pages.

### Méthode

Crawl interne délégué à un agent Explore qui a scanné l'intégralité des `href="..."` et `src="..."` locaux sur les 32 pages, vérifié les ancres internes, audité les liens croisés critiques.

### Résultats

| Métrique | Résultat |
|---|---|
| Pages auditées | 32 / 32 (100 %) |
| Liens internes scannés | 79+ |
| Liens internes morts | **0** ✅ |
| Ancres internes vérifiées | 35+ (#modules, #a-propos, #section-1 à #section-10 sur architectures, 13 ancres `#cat-*` sur ressources) |
| Ancres manquantes | **0** ✅ |
| Liens externes (sources) | 401 |
| Liens externes mal formés | **0** ✅ (structure URL valide) |
| Assets CSS / JS / images | 3 / 3 + 6 logos — 100 % présents ✅ |

### Liens croisés critiques — confirmés présents

| Parcours | État |
|---|---|
| Les 5 modules sensibles (CU-007 / CU-008 / CU-013 / CU-020 / CU-021) → encart « Architectures recommandées » + lien vers `architectures.html` | ✅ 5 / 5 |
| Les 6 fiches PR → liens croisés vers index, architectures, ressources, modules | ✅ 6 / 6 |
| Home (index.html) → CTAs vers Préalables (×5) + Architectures (×5) | ✅ multiples |
| Page Préalables → 6 sous-pages | ✅ 6 / 6 |
| Page Ressources → 22 modules + 6 préalables | ✅ 100 % |

### Écart corrigé pendant l'audit

`prealables.html` ligne 137 (card de PR-05 « Sécurité IA &amp; risques opérationnels ») : la description courte contenait deux résidus historiques d'avant la v3.4 :

- `(CU-020)` (code interne visible — RULES 1.3.6)
- « 3 cas DGSI documentés » (régression de v3.4 où on avait reformulé en « 3 patterns d'incidents type » dans la fiche PR-05 elle-même mais pas dans la card de l'index Préalables)

→ Phrase reformulée pour refléter la rédaction actuelle de PR-05 et retirer le code interne.

**Commit** : `fix(v3.5.3): liens & parcours — résidu DGSI / CU-020 sur card prealables.html`.

### Aucune autre régression

Aucun lien mort, aucune ancre orpheline. Le maillage CU ↔ PR ↔ Architectures établi en v3.5 fonctionne. Les 401 liens externes (sources institutionnelles) sont bien formés — pas d'audit HTTP pour vérifier les 200 OK (hors périmètre de l'audit selon RULES de prudence n°5).

**Recommandation** : intégrer une vérification mensuelle automatique des liens externes (script de crawl côté CI/CD) à proposer pour v3.6+.

---

## 6. Propositions d'amendement à RULES.md

Cinq points imprécis ou désynchronisés détectés pendant l'audit. À discuter avec Blaise puis amender en v1.1 du référentiel :

### 6.1 Glossaire chiffres-clés (§ 1.2.3) — désynchronisé

Voir section 1 du présent rapport. Actualiser :
- 76 fiches outils → **83 fiches**
- 6 entrées de nav (avec Axes) → **5 entrées (sans Axes)**
- Retirer `axes.html` de la liste des pages à vérifier (§ 1.2.2)

### 6.2 Chiffres macro (§ 1.2.4) — référence obsolète

Retirer la mention « 94 % AdvisoryX » qui n'est plus utilisée sur le site (étude non vérifiable retirée en v3.4). Mettre à jour avec : 95 % MIT NANDA, +270 % Microsoft / Sigma, 76 % France Num, ×5 PwC, 77 000 offres PwC, 3,7× IDC Copilot.

### 6.3 Pattern executive summary (§ 1.4.5) — précision attendue

Le RULES indique « gradient bleu marine + 4 takeaways + stats grid + callout when ». Préciser :
- Quelle classe CSS exacte est attendue (`.exec-summary`) ?
- Le « callout when » est-il l'élément `.exec-when` ?
- Les stats peuvent-elles être 3 ou 4 (variabilité actuelle) ?

### 6.4 Page À propos en page séparée (§ 1.4.3) ?

Le RULES mentionne « lien à propos » comme constituant du footer mais le site a actuellement la section « À propos » comme ancre `#a-propos` sur `index.html`, pas en page séparée. À clarifier : page séparée nécessaire ou ancre suffit ?

### 6.5 Codes A1-A4 visibles (§ 1.3.6) — exception à formaliser

Le cas particulier validé v3.5 (les A1-A4 restent visibles sur architectures.html et dans les encarts d'archi recommandées des 5 modules sensibles) mérite d'être inscrit explicitement dans RULES § 1.3.6 pour éviter qu'un futur audit les supprime par erreur.

---

## 7. Recommandations pour v3.6

À propager dans le brief v3.6 (CU-023 / CU-024 / CU-027 / PR-07) :

1. **Avant ajout** : exécuter le grep cross-site (RULES § 5) sur tous les chiffres impactés (« 22 modules » → « 24 modules », « 6 préalables » → « 7 préalables », etc.).
2. **Sourcing dès création** : tout nouveau chiffre dans CU-023 / CU-024 / CU-027 / PR-07 doit avoir son lien `<a href>` cliquable dès la 1re version.
3. **Glossaire dans ressources.html** : si l'option 2 du § 3 est validée, le mini-glossaire des termes techniques doit être créé en v3.6 pour limiter la dette d'explicitation.
4. **Réorganisation home modules** : prévoir d'ajouter les 3 nouveaux modules dans une des 6 familles métier existantes (Découverte / Marketing &amp; Croissance / Décision &amp; Gouvernance / Fonctions support / Industrie / Architectures agentiques avancées) ou créer une 7e famille. Décision Cowork.
5. **Échelle complexité** : assigner un niveau ⭐ à ⭐⭐⭐⭐ aux 3 nouveaux CU dès le brief de leur création.
6. **Distribution famille / niveau** : actuelle 4 / 6 / 6 / 6 (par niveau). Vérifier l'équilibrage après ajout des 3 CU + 1 PR.

---

*Rapport produit par Claude Code dans le cadre de l'audit autonome v3.5.3, mai 2026.*
