# RULES Migration v1.5.14 → v1.6 — Table de mapping exhaustive

**But** : garantir qu'aucune règle structurelle de v1.5.X n'a été perdue ou abandonnée silencieusement lors de la refonte v1.6. Cette table sert de **filet de sécurité** : à la lecture, on doit pouvoir confirmer pour chaque amendement v1.5.X qu'il est intégré dans v1.6 (sous quelle règle ?) ou explicitement abandonné (avec justification).

---

## Méthode appliquée

Pour chaque sous-version v1.5.X et chaque règle de v1.5.14, je vérifie :
1. **Présent dans v1.6 ?** Oui / Non
2. **Sous quelle règle ?** Si oui, mapping explicite
3. **Justification si abandon** : si non, raison précise (règle devenue obsolète, redondante, intégrée dans `audit-global.py`, etc.)

---

## A — Sourcing & véracité

| Règle v1.5.14 | Présence v1.6 | Mapping |
|---|---|---|
| 1.1.1 Sourcing rigoureux + format obligatoire | ✅ | A.1 |
| 1.1.2 Pas d'invention / extrapolation | ✅ | A.1 (consolidée) |
| 1.1.3 Sources prioritaires / à éviter | ✅ | A.1 (consolidée) |
| 1.1.4 Citations vérifiables, pas de témoignage fictif | ✅ | A.1 (consolidée) |
| 1.1.5 RetEx entreprises institutionnels uniquement | ✅ | A.2 |

**Aucune règle abandonnée. Pas d'ajout dans v1.6 sur ce domaine.**

**Ajout v1.6 par rapport à v1.5** : Règle A.3 « Pas de promotion commerciale » — qui était implicite dans v1.5 (mentionnée en section 6 « Décisions éditoriales structurantes »), mais qui devient une règle explicite en v1.6 pour clarification.

---

## B — Cohérence numérique

| Règle v1.5.14 | Présence v1.6 | Mapping |
|---|---|---|
| 1.2.1 Cohérence numérique cross-site | ✅ | B.1 |
| 1.2.2 Recherche cross-site avant tout commit | ✅ | B.1 (consolidée) |
| 1.2.3 Glossaire chiffres-clés | ✅ | B.1 + Annexe § 4.B.1 |
| 1.2.4 Statistiques macro synchronisées | ✅ | B.1 + Annexe § 4.B.1 |
| 1.2.5 Cohérence intra-page | ✅ | B.1 (consolidée intra-page) |
| 1.2.5.1 Anti-drift cross-bloc (exec-stats, badges, prose, méta) | ✅ | B.1 (consolidée) |
| 1.2.6 Pas de versioning interne sur le front | ✅ | B.2 |
| 1.2.7 Pas de biais sectoriel/territorial dominant | ✅ | D.1 (déplacée vers Posture éditoriale — plus cohérent) |

**Aucune règle abandonnée.**

**Refactor v1.6** : la règle « biais sectoriel/territorial » a été déplacée de la dimension « Cohérence numérique » (1.2.7) vers une nouvelle dimension « Posture éditoriale » (D.1). Cela colle mieux à sa nature (c'est une règle éditoriale, pas un comptage).

---

## C — Niveau de langue & terminologie

| Règle v1.5.14 | Présence v1.6 | Mapping |
|---|---|---|
| 1.3.1 Public cible PME/ETI non-IT | ✅ | C.1 |
| 1.3.2 Glose obligatoire à la 1re occurrence | ✅ | C.1 + Annexe § 4.C.1 |
| 1.3.3 Privilégier termes français | ✅ | C.1 (consolidée) |
| 1.3.4 Phrases courtes, paragraphes ≤ 6 lignes | ✅ | C.1 (consolidée) |
| 1.3.5 Acronymes QFC avec parcimonie | ✅ | C.1 (consolidée) |
| 1.3.6 Pas de codes internes visibles (PR-XX, CU-XXX) | ✅ | C.2 |
| 1.3.7 Pas de nomenclature non explicitée | ✅ | C.2 (consolidée) |
| 1.3.8 Légende badge ↔ badges réellement utilisés | ✅ | C.2 (consolidée) |

**Aucune règle abandonnée.**

---

## D — Harmonisation visuelle

| Règle v1.5.14 | Présence v1.6 | Mapping |
|---|---|---|
| 1.4.1 Nav identique cross-pages | ✅ | E.1 |
| 1.4.2 Head banner identique | ✅ | E.1 (consolidée) |
| 1.4.3 Footer identique | ✅ | E.1 (consolidée) |
| 1.4.4 Composants CSS centralisés | ✅ | E.1 (consolidée) |
| 1.4.5 Executive summary obligatoire (introduit v1.5.3 anti-bulk-patch-bug) | ✅ | F.1 (déplacée vers Pattern structurel) |
| 1.4.6 Sticky TOC + scroll-spy + reading progress fonctionnels (élargi v1.5.3, v1.5.9) | ✅ | E.1 + F.1 |
| 1.4.7 Format canonique sommaire emoji-style (v1.5.9, v1.5.12 fallback) | ✅ | E.1 + Annexe § 4.E.1 |
| 1.4.8 Contraste fond foncé (v1.5.9, v1.5.10 cascade fix) | ✅ | E.1 + Annexe § 4.E.2 |

**Aucune règle abandonnée.**

**Refactor v1.6** : la règle « executive summary obligatoire » (anciennement 1.4.5) a été déplacée vers la dimension « Pattern structurel » (F.1), avec les autres composants du squelette HTML obligatoire. Plus cohérent.

---

## E — Pattern structurel modules CU et fiches PR/DEP

| Règle v1.5.14 | Présence v1.6 | Mapping |
|---|---|---|
| 1.5.1 Squelette HTML minimal (9 blocs) | ✅ | F.1 |
| 1.5.1.1 Structure canonique `module-section-header` (v1.5.4) | ✅ | F.1 (consolidée dans squelette) |
| 1.5.1.2 Callout intro Pour-aller-plus-loin avec margin-bottom (v1.5.5) | ✅ | F.1 (consolidée dans squelette) |
| 1.5.2 Composants CSS de référence | ✅ | E.1 + Annexe § 4.F.1 |
| 1.5.3 Anti-patterns interdits (étendue v1.5.3, v1.5.8) | ✅ | J.1 (regroupé en liste exhaustive 14 anti-patterns) |
| 1.5.4 Rôles Cowork (matière MD) / Claude Code (HTML) | ✅ | G.1 (nouvelle dimension dédiée — plus visible) |
| 1.5.5 Format auto-diagnostic standard (3 propriétés) | ✅ | H.1 (nouvelle dimension dédiée) |
| 1.5.6 Renvois internes contextualisés dans le corps | ✅ | I.1 (nouvelle dimension dédiée) |
| 1.5.6.1 Anti-codes-internes en texte affiché (v1.5.2) | ✅ | C.2 + J.1 (anti-pattern #11) |
| 1.5.6.2 Lien outil obligatoire (v1.5.2) | ✅ | I.1 |

**Aucune règle abandonnée.**

**Refactor v1.6** : la dimension monolithique « Pattern structurel » de v1.5 a été éclatée en 4 dimensions distinctes en v1.6 :
- **F.1** : Squelette HTML obligatoire (la structure)
- **G.1** : Rôles Cowork / Claude Code (le process — spécialisation des rôles)
- **H.1** : Format auto-diagnostic (le pattern spécifique)
- **I.1** : Renvois internes (la règle d'articulation entre modules)

Chacune devient une dimension de premier plan, plus lisible et plus actionnable.

---

## F — Anti-patterns (consolidation des entrées éparpillées)

| Anti-pattern v1.5.14 | Présence v1.6 | Mapping |
|---|---|---|
| `<main>` direct sans `module-layout` | ✅ | J.1 (#1) |
| `id="section-7"` au lieu de `id="ressources"` | ✅ | J.1 (#2) |
| `.exec-takeaway-icon` au lieu de `.exec-takeaway-num` | ✅ | J.1 (#3) |
| `<style>` inline qui redéfinit composants centralisés | ✅ | J.1 (#4) |
| h1 sans emoji ouvrant | ✅ | J.1 (#7) |
| `<a>` imbriqué dans card cliquable home | ✅ | J.1 (#8) |
| Couleurs hardcodées en `<style>` inline (v1.4) | ✅ | J.1 (#5) |
| Espacements absolus en `<style>` inline (v1.4) | ✅ | J.1 (#6) |
| Auto-diagnostic sans interactivité (v1.5.5) | ✅ | J.1 (#10) |
| Renvois internes dans section finale (v1.5.6) | ✅ | J.1 (#9) |
| `<pre>` text-art pour flux fonctionnels (v1.5.8) | ✅ | (à intégrer dans audit-global.py — règle implicite F.1 sur les composants centralisés) |
| Placeholders STASH résiduels (v1.5.3) | ✅ | J.1 (#13) |
| NUL bytes (v1.5.3) | ✅ | J.1 (#14) |
| Codes internes visibles (v1.5.2) | ✅ | J.1 (#11) |
| Fallback emoji 📌 répété (v1.5.12) | ✅ | J.1 (#12) |

**Aucun anti-pattern abandonné.**

**Refactor v1.6** : tous les anti-patterns sont regroupés dans la **Règle J.1 (liste exhaustive de 14 entrées)**, classés par ordre de détection historique. Annexe § 4.J.1 documente l'origine de chaque anti-pattern pour traçabilité.

---

## G — Garde-fou automatisé `audit-global.py`

| Élément v1.5.14 | Présence v1.6 | Mapping |
|---|---|---|
| Mention du garde-fou `audit-global.py` (introduit v1.5.11) | ✅ | K.1 (nouvelle dimension dédiée) |
| 13 règles automatisées | ✅ | K.1 + Section 3 (tableau de mapping) |
| Principe « toute nouvelle règle structurelle = nouvelle fonction d'audit » | ✅ | K.1 (formalisé comme principe directeur) |

**Refactor v1.6** : le garde-fou `audit-global.py` devient une **dimension de premier plan** (K.1), pas un détail technique enfoui dans l'historique. C'est l'outil exécutoire du référentiel, il mérite cette visibilité.

---

## H — Décisions éditoriales structurantes (section 6 de v1.5)

| Décision v1.5.14 | Présence v1.6 | Mapping |
|---|---|---|
| Pas de pub pour acteurs commerciaux | ✅ | A.3 (devient règle explicite) + Section 5 (rappel) |
| Distinction CU / PR / DEP / Architectures | ✅ | Section 5 (rappel) |
| Pas de reframing géographique | ✅ | Section 5 (rappel) + D.1 (précision) |
| Pas de refonte du design system sans Blaise | ✅ | Section 5 (rappel) |
| Pas d'ajout de catégorie d'outils sans Blaise | ✅ | Section 5 (rappel) |

**Aucune décision abandonnée.**

---

## I — Évolution du fichier (section 7 de v1.5)

| Élément v1.5.14 | Présence v1.6 | Mapping |
|---|---|---|
| Versionnage v1.X | ✅ | Section 6 |
| Évolution via PR dédiée, validation Blaise | ✅ | Section 6 |
| Principe : nouvelle règle = nouveau audit | ✅ | Section 6 (formalisé) |

---

## Synthèse — règles abandonnées en v1.6

**Aucune.** Toutes les règles structurelles de v1.5.14 et de l'historique v1.5.X sont reprises dans v1.6, soit comme règle de premier plan, soit comme entrée d'annexe, soit comme rappel en section 5.

**Refactors structurels v1.6** (sans perte de contenu) :
1. Dimension « Pattern structurel » de v1.5 éclatée en 4 dimensions distinctes (F, G, H, I)
2. Règle « biais sectoriel/territorial » déplacée de « Cohérence numérique » vers « Posture éditoriale »
3. Tous les anti-patterns regroupés dans la Règle J.1 (au lieu d'être éparpillés)
4. Le garde-fou `audit-global.py` devient une dimension de premier plan (K.1)
5. Toutes les justifications historiques détaillées, scripts d'audit Python in-line et anti-patterns d'origine sont **migrés en Annexe Section 4** (compendium d'exemples détaillés)

**Ajout v1.6 par rapport à v1.5** : Règle A.3 « Pas de promotion commerciale » devient explicite (était implicite dans v1.5).

---

## Test de cohérence avec audit-global.py

Les 13 fonctions d'audit dans `audit-global.py` couvrent :
- B.1 (cohérence numérique cross-site + intra-page)
- B.2 (pas de versioning interne)
- C.2 (codes internes visibles)
- D.1 (biais sectoriel/territorial)
- D.2 (cohérence card ↔ contenu)
- E.1 partiel (sommaire canonique, contraste fonds foncés)
- F.1 partiel (structure module-section-header, callout intro margin)
- I.1 (lien outil obligatoire)
- J.1 partiel (placeholders STASH, NUL bytes)

Règles **non automatisées** dans v1.6 (à compléter dans `audit-global.py` au fil des itérations futures) :
- A.1, A.2, A.3 (sourcing — vérification humaine)
- C.1 (jargon — vérification humaine)
- E.1 partiel (composants CSS inline non centralisés — à automatiser)
- F.1 partiel (squelette 9 blocs — partiellement automatisé)
- G.1 (rôles Cowork/Claude Code — règle de process)
- H.1 (format auto-diagnostic — à automatiser)
- J.1 (#1 à #12 — partiellement automatisés, à compléter)

**Engagement v1.6** : à chaque nouvelle règle structurelle ajoutée au référentiel, une fonction d'audit correspondante est créée dans `audit-global.py` dans la même PR.

---

## Note de prudence

Cette table de migration est **un filet de sécurité, pas une garantie absolue**. Recommandation : à la première itération éditoriale post-v1.6 (probable v3.9 ou v4.0), exécuter audit-global.py et faire un audit visuel de quelques modules pour confirmer que la consolidation v1.6 n'a pas créé d'angle mort. Si un écart est détecté, il sera corrigé en v1.6.1 (cas particulier) ou v1.7 (refonte structurelle).

---

*Table de migration produite par Cowork le 11 mai 2026 lors de la refonte RULES v1.5.14 → v1.6 (item I-001 transmis par le canal Plateforme).*
