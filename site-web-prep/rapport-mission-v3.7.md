# Rapport mission v3.7 — Expansion éditoriale majeure

**Date** : mai 2026
**Branche** : `claude/implement-hub-ia-site-TsegT`
**RULES** : v1.4 → v1.5

---

## Synthèse

L'itération v3.7 est la plus volumineuse depuis le lancement du Hub IA :
- **Nouvelle section transverse « Déploiement »** (1 page index + 8 fiches DEP)
- **1 nouveau module CU-025** (Knowledge management IA-augmenté pour dirigeant)
- **5 enrichissements ciblés** sur modules existants (CU-027, PR-07, CU-008, CU-014, CU-015)
- **12 nouvelles fiches outils** + 2 mises à jour majeures dans `ressources.html`
- **Cohérence numérique** propagée cross-site (25 → 26 modules ; 83 → 95 fiches outils ; 5 → 6 entrées de nav)
- **RULES amendée** v1.4 → v1.5 (glossaire chiffres-clés actualisé, historique enrichi)

Le Hub IA passe ainsi de **4 niveaux** (Préalables / Architectures / Modules / Ressources) à **5 niveaux** (insertion de Déploiement entre Architectures et Modules).

---

## Inventaire détaillé

### Lot 1 — RULES v1.4 → v1.5 ✓
- `site-web-prep/RULES-IMPLEMENTATION.md` : § 1.2.3 glossaire actualisé v3.7, ligne « Nombre de fiches Déploiement DEP » ajoutée (8), historique v1.5 documenté, valeurs corrigées au comptage réel (95 fiches outils, pas 97).

### Lot 2 — Section Déploiement ✓
- `deploiement.html` : page index créée (mirror de `prealables.html`), hero + 8 dep-cards + 3 parcours + footer. Nav 6 entrées avec « Déploiement » actif.
- `deploiement/dep-01-cadrer-projet-prod.html` (~26.5 KB)
- `deploiement/dep-02-rag-architecture-prod.html` (~26.8 KB)
- `deploiement/dep-03-context-engineering-couts.html` (~26.1 KB)
- `deploiement/dep-04-fine-tuning-pme.html` (~24.6 KB)
- `deploiement/dep-05-agents-observabilite.html` (~27.7 KB)
- `deploiement/dep-06-inference-saas-self-hosted.html` (~27.0 KB)
- `deploiement/dep-07-evaluation-qualite.html` (~27.1 KB)
- `deploiement/dep-08-securite-agents-mcp.html` (~29.9 KB)

Chaque fiche DEP suit le squelette RULES § 1.5.1 (reading-progress + nav + hero + module-layout + executive-summary + 5-7 sections + section finale `id="ressources"` Schéma A + footer + script). Anti-patterns vérifiés (RULES § 1.5.3) : aucun `<style>` inline redondant, h1 emoji, dernière section = `id="ressources"`.

### Lot 3 — Navigation cross-pages 5 → 6 ✓
- 36 pages HTML mises à jour (toutes les `modules/*.html`, `prealables/*.html`, root, plus les nouvelles pages DEP) : ajout `<a href="../deploiement.html">Déploiement</a>` entre Architectures et Modules dans la nav et le footer.
- 46 / 49 pages totales contiennent le lien (les 3 manquantes sont les `_template-*.html`, hors prod).

### Lot 4 — Module CU-025 ✓
- `modules/cu-025-knowledge-management-dirigeant.html` (~40.5 KB) : 9 sections, niveau ⭐⭐⭐ Avancé, axe-b Décision, type « Étude de cas + plan d'action », emoji 🧠.
- Architecture en 4 layers (briefing matinal, synthèse hebdo, archive contextualisée, plan 30 jours). Renvois internes : CU-008 (variante orga), CU-014 (Fat Skills), CU-015 (asynchronicité), DEP-01 et DEP-08.
- Ajout sur la home dans la section « Décision & gouvernance ».

### Lot 5 — 5 enrichissements ✓
- **CU-027** : nouvelle section `id="section-1bis"` « État de l'art 2026 : la rupture économique Kimi K2.6 + ECC stack » (Kimi K2.6, ECC, Garry Tan Fat Skills, 3 questions au prestataire). TOC entry ajoutée.
- **PR-07** : matrice de décision étendue de 6 → 8 critères (compétences IA-natives + coût d'inférence) ; encart `callout-warning` « Compression des coûts du build IA-assisté en 2026 » ; 3 sources ajoutées (MIT NANDA, Together.ai, Garry Tan).
- **CU-008** : nouvelle Section 4 (et renumérotation 4→5, 5→6, …, 9→10) « Au-delà du RAG : l'approche LLM Wiki (Karpathy, 2026) » avec matrice 5 lignes + cas types + sources Karpathy gist / MindStudio / Suryansh Tiwari.
- **CU-014** : nouvelle section `id="section-3bis"` « Le pattern Fat Skills / Thin Harness (référence 2026) » avec matrice stack technique 2026 (harness, brain, skills, observabilité, sécurité) + sources Garry Tan / GBrain / OpenClaw / Hermes Agent.
- **CU-015** : 3 patches ciblés — nouveau h3 « Évolutions 2026 — Kimi K2.6, ECC stack et Fat Skills » dans la section Stack ; renvois CU-025 (transposition perso/dirigeant) et DEP-08 (sécurité agents) dans les sections existantes ; 2 sources ajoutées.

### Lot 6 — Fiches outils v3.7 ✓
**Nouvelle catégorie « Compta, facturation & order-to-cash »** (7 fiches insérée après CRM, avant Vision industrielle) :
- Pennylane (id=`pennylane`)
- Sellsy (id=`sellsy`)
- Axonaut (id=`axonaut`)
- PandaDoc (id=`pandadoc`)
- Esker (id=`esker`)
- Sidetrade (id=`sidetrade`)
- Tacton (id=`tacton`)

**Catégorie « IDE & agents codeurs » étendue** (5 → 10 fiches) :
- Lovable (id=`lovable`)
- Bolt.new (id=`bolt-new`)
- v0 (id=`v0`)
- Replit Agent (id=`replit-agent`)
- Windsurf (id=`windsurf`)

**2 mises à jour majeures** (refresh content sur fiches existantes) :
- Kimi K2 → **Kimi K2 / K2.6** : tagline, badges, body refresh (focus agentic coding, prix 0,80 / 3,60 $, swap 75 % du volume Opus → Kimi, renvois CU-027 / DEP-06 / PR-07 ajoutés).
- GitHub Copilot Workspace : tagline et badge maturité actualisés 2026.

**Net** : +12 nouvelles fiches → catalogue passe de **83 → 95 fiches** dans **15 catégories**. Aucun id dupliqué.

### Lot 7 — Cohérence numérique ✓
- `site-web-prep/RULES-IMPLEMENTATION.md` : valeurs alignées (95 fiches, 26 modules, 8 DEP, 6 nav).
- `index.html` : meta description, hero stats (3 cartes : 26 modules / 8 fiches Déploiement / 95 fiches outils), filtres modules (`<strong>26</strong> sur 26`), section À propos passée à 5 niveaux avec ajout du niveau Déploiement.
- `prealables.html` : « 26 cas d'usage » + « 8 fiches Déploiement » + « 95 fiches outils » intégrés.
- `ressources.html` : meta description, hero badge `95 fiches · 15 catégories`, takeaway 4, h2 catalogue, alerte fin de page.
- `prealables/pr-01`, `pr-02`, `pr-04` : « 25 modules » → « 26 modules ».
- `modules/cu-023-devis-intelligent.html` : « 25 cas d'usage » → « 26 cas d'usage ».

### Lot 8 — Callout home Déploiement ✓
- `index.html` encart « Avant de te lancer » : description complétée (« cadre ta mise en production avec les fiches Déploiement »), 3<sup>e</sup> CTA `🚀 Déploiement` ajouté à côté de Préalables et Architectures.

### Lot 9 — Audit final ✓
- Comptages finaux vérifiés par grep / ls (cf. ci-dessus).
- Aucune duplication d'id sur `ressources.html`.
- Tous les nouveaux fichiers ont la nav 6 entrées et le footer 8 liens harmonisés (vérifié sur 8 DEP + CU-025 + deploiement.html).

---

## Écarts assumés vs brief Cowork

| Brief v3.7 | Réalisation | Justification |
|---|---|---|
| « 14 fiches outils v3.7 → 97 total » | 12 nouvelles + 2 refresh = **95 total** | Les fiches Kimi K2.6 et GitHub Copilot Workspace existaient déjà sous des ids `kimi` / `copilot-workspace`. Plutôt que créer des doublons, j'ai refresh le contenu existant. RULES § 1.2.3 mise à jour en conséquence. |
| « Pas de récap renvois internes en fin de fiche » (RULES § 1.5.3) | Respecté sur toutes les nouvelles pages | Vérifié sur les 8 DEP, CU-025, et tous les enrichissements. |
| « Renvois contextualisés dans le corps » (RULES § 1.5.6) | Appliqué | Les 5 enrichissements et les fiches outils nouvelles ont leurs renvois dans le corps, jamais dans la section finale `ressources`. |

---

## État courant du Hub IA

| Niveau | Volume |
|---|---|
| Préalables PR | 7 |
| Architectures | 4 + 1 hybride |
| **Déploiement DEP** | **8 (NOUVEAU v3.7)** |
| Modules CU | 26 (CU-001 → CU-025 + CU-027 ; CU-026 réservé v3.8) |
| Fiches outils | 95 en 15 catégories |
| Pages HTML totales | 49 (+ 3 templates) |
| Entrées de navigation | 6 |

---

## Prochain commit suggéré

```
v3.7 — Expansion éditoriale majeure : Déploiement + CU-025 + 5 enrichissements + 12 fiches outils

Nouvelle section transverse Déploiement (page index + 8 fiches DEP) ; nouveau module
CU-025 Knowledge management IA-augmenté pour dirigeant ; 5 enrichissements ciblés
(CU-027 Kimi K2.6 + ECC, PR-07 compression coûts build, CU-008 LLM Wiki Karpathy,
CU-014 Fat Skills/Thin Harness, CU-015 renvois 2026) ; 12 nouvelles fiches outils
(7 compta/O2C : Pennylane, Sellsy, Axonaut, PandaDoc, Esker, Sidetrade, Tacton ;
5 IDE agentique : Lovable, Bolt.new, v0, Replit Agent, Windsurf) + refresh
Kimi K2.6 et GitHub Copilot Workspace ; nav 5 → 6 entrées (ajout Déploiement) ;
RULES v1.4 → v1.5 ; cohérence numérique cross-site (25 → 26 modules, 83 → 95
fiches outils, 5 → 6 nav).
```
