# Lot C v3.8 — Actualisations chiffrées (PR-01, PR-04)

**Brief consolidé pour Claude Code** : 2 actualisations de chiffres macro sur des préalables existants.

**Sources** : veille v3.7.13 (Bpifrance Le Lab + France Num + Grok input 5).

---

## Patch C.1 — PR-01 (Maturité organisationnelle) — chiffre 80-95 % d'échecs imputables aux causes organisationnelles

**Module cible** : `prealables/pr-01-maturite-organisationnelle.html`
**Position** : section actuelle qui parle des causes d'échec des projets IA (typiquement dans l'introduction ou la première section). Si la section n'existe pas, créer un encart `.alert-block` ou `.stat-block` en début de module.

### Contenu à intégrer

#### Le chiffre choc à mettre en avant

> **80 à 95 % des échecs de projets IA en entreprise sont imputables à des causes organisationnelles** (gouvernance floue, sponsor absent, objectifs flous, redesign de workflow oublié), pas à la technologie elle-même. L'IA ne crée pas de nouvelles dysfonctions : elle **amplifie celles qui préexistent**.

#### Articulation avec le chiffre MIT NANDA déjà présent (95 % d'échec)

Le chiffre MIT NANDA est déjà présent dans le Hub (95 % des projets GenAI sans ROI mesurable sur 30-40 milliards de dollars investis). Le nouveau chiffre 80-95 % apporte **la cause structurelle** :

> Le chiffre MIT NANDA dit **combien** de projets échouent. Le chiffre 80-95 % dit **pourquoi**.

#### Implications pratiques pour le dirigeant PME

Trois points à retenir et à expliciter dans le module :

1. **Avant tout POC IA** : auditer la maturité organisationnelle (sponsor identifié ? gouvernance définie ? objectifs mesurables ? redesign workflow planifié ?). C'est précisément le rôle de PR-01.
2. **Pendant le pilote** : ne pas se focaliser sur la « performance IA » seule. Suivre aussi les indicateurs organisationnels (adoption utilisateur, redesign effectif, réorganisation des rôles).
3. **En production** : 80 % du travail post-déploiement n'est pas technique. C'est de la conduite du changement.

#### Mise en contexte v2026

Ce chiffre 80-95 % est documenté par plusieurs sources convergentes en 2026 (Gartner, Deloitte, Bpifrance Le Lab). C'est devenu un **consensus** dans la littérature gouvernance IA. À utiliser comme ancrage pour expliquer pourquoi un préalable comme PR-01 est non négociable avant tout projet IA en PME.

### Format suggéré pour l'intégration HTML

Composant `.stat-block` recommandé (existe dans `module-v3.css`), avec format type :

```
[Chiffre choc 80-95 %]
Causes organisationnelles dans les échecs de projets IA en entreprise
Source : consensus Gartner / Deloitte / Bpifrance Le Lab (2025-2026)
```

Suivi d'un encart `.callout-info` qui développe l'articulation avec le 95 % MIT NANDA et les 3 implications pratiques.

### Sources à ajouter dans la section finale

À insérer dans la sous-rubrique « 📰 Articles de fond » :
- Compte X @OChambelant — analyse causes organisationnelles d'échec IA (mai 2026)

À insérer dans la sous-rubrique « 📚 Documentation officielle & études » :
- Bpifrance Le Lab — études IA PME/ETI 2025 (déjà présent ailleurs dans le Hub, vérifier le lien)

---

## Patch C.2 — PR-04 (Marché IA & emploi) — Baromètre France Num 2025 + étude Bpifrance Le Lab

**Module cible** : `prealables/pr-04-marche-ia-emploi.html`
**Position** : section actuelle sur les chiffres d'adoption IA en France (à actualiser avec données 2025).

### Contenu à intégrer

#### 1. Données Baromètre France Num 2025

À intégrer comme nouveaux chiffres clés du marché français :

> **26 % des TPE-PME françaises utilisent une IA en 2025**, soit **un doublement (×2) par rapport à 2024** (où le taux était de 13 %).
>
> Cette adoption est très inégale selon les secteurs :
> - **41 %** dans le secteur ICT (technologies de l'information et de la communication)
> - **9 %** dans le secteur Agriculture
> - Les autres secteurs se positionnent entre ces deux extrêmes
>
> Source : Baromètre France Num 2025 (publié par france Num, agence d'État pour la transformation numérique des PME).

#### 2. Données Bpifrance Le Lab — paradoxe enjeu vs adoption

À intégrer comme **paradoxe pédagogique central** :

> **58 % des dirigeants de PME et ETI françaises** considèrent l'intelligence artificielle comme un **enjeu de survie** pour leur entreprise.
>
> Pourtant, **seul 1 dirigeant sur 3** déclare l'adopter au quotidien dans son organisation.
>
> Source : étude Bpifrance Le Lab — IA dans les PME et ETI françaises (2025).

#### 3. Articulation pédagogique pour le dirigeant

Le contraste entre ces deux datasets met en évidence un **gap stratégique majeur** :

- **Côté perception** : 58 % des dirigeants reconnaissent l'enjeu vital de l'IA → la prise de conscience est faite.
- **Côté action** : 33 % d'adoption quotidienne → l'écart entre conscience et action est de 25 points.

Ce gap est précisément la zone d'intervention où le Hub IA (et l'accompagnement Quai Alpha) apporte une valeur ajoutée différenciante.

#### 4. Comparaison avec le chiffre Bpifrance Le Lab déjà présent (55 %)

Le Hub mentionne déjà le chiffre « 55 % des TPE-PME utilisent une IA générative fin 2025 » (étude Bpifrance Le Lab Osez l'IA, décembre 2025). Le nouveau chiffre France Num 2025 (26 %) ne contredit pas ce chiffre — les périmètres sont différents :

- **Bpifrance Le Lab Osez l'IA (déc. 2025)** : usage **occasionnel** d'une IA générative (« avez-vous déjà utilisé ChatGPT ou équivalent ? »)
- **Baromètre France Num 2025** : usage **outillé et intégré** dans l'entreprise (« utilisez-vous une IA dans vos processus ? »)
- **Étude Bpifrance Le Lab — adoption quotidienne** : usage **quotidien et opérationnel**

Ces 3 indicateurs racontent ensemble la maturité du marché : prise de conscience massive, adoption ponctuelle large, intégration quotidienne encore minoritaire.

### Format suggéré pour l'intégration HTML

3 `.stat-block` côte-à-côte (composant existant) ou un `.tool-table` comparatif :

| Indicateur | Valeur | Source |
|---|---|---|
| Usage occasionnel IA générative | 55 % | Bpifrance Le Lab — Osez l'IA (déc. 2025) |
| Usage outillé et intégré | 26 % | Baromètre France Num 2025 |
| Adoption quotidienne | 33 % | Bpifrance Le Lab (étude PME/ETI 2025) |
| Considère l'IA comme enjeu de survie | 58 % | Bpifrance Le Lab (idem) |

### Sources à ajouter dans la section finale

À insérer dans la sous-rubrique « 📚 Documentation officielle & études » :
- [France Num — Baromètre France Num 2025](https://www.francenum.gouv.fr/) (vérifier le lien direct au moment de l'intégration)
- [Bpifrance Le Lab — IA dans les PME et ETI françaises](https://lelab.bpifrance.fr/) (chercher l'étude la plus récente disponible publiquement)

---

## Synthèse Lot C pour Claude Code

**Volume** : 2 actualisations chiffrées sur 2 préalables.

**Effort estimé Claude Code** : 30 min - 1 h.

**Composants à utiliser** : `.stat-block` (centralisé), `.tool-table` (centralisé), `.callout-info` (centralisé).

**Cohérence numérique** : pas de changement structurel des comptages Hub. Mais ces nouveaux chiffres macro doivent être cohérents partout où ils apparaissent (RULES § 1.2.4 sur la cohérence des stats macro).

**Vigilance** : ne pas effacer les chiffres précédents (95 % MIT NANDA, +270 % Microsoft, etc.). Les nouveaux chiffres viennent **en complément**.

## Note Cowork

Sources prioritaires utilisées : France Num (institutionnel public), Bpifrance Le Lab (institutionnel public). Conforme RULES § 1.1.5.
