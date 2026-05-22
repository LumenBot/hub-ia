# Lot B v3.12 — PR-10 « Vérifier et limiter les hallucinations IA » (nouveau préalable, fusion idées 3+4)

**Brief consolidé pour Claude Code** : création complète d'un nouveau préalable PR-10 dédié à la discipline managériale de vérification des outputs IA et à la limitation des hallucinations en contexte métier PME. Fusion validée des idées 3 (vérification) et 4 (hallucinations) du brainstorming roadmap éditoriale.

**Décision validée par Blaise** : nouveau préalable PR-10 (pas CU comme initialement proposé pour les hallucinations — repositionnement transverse). Articulation avec patterns techniques DEP-05 §8.5 (failure receipt v3.10), DEP-07 (evals), DEP-08 (sécurité agents).

**Référence canonique structure HTML** : `prealables/pr-08-financer-projet-ia.html`.

---

## Architecture du préalable PR-10

**Module cible** : `prealables/pr-10-verifier-limiter-hallucinations.html` (à créer)
**Titre** : « Vérifier et limiter les hallucinations IA »
**Sous-titre/accroche** : « Pourquoi un agent IA peut déclarer une tâche terminée sans qu'elle le soit. La discipline managériale qui sépare les PME qui pilotent l'IA de celles qui pilotent à l'aveugle. »
**Badge complexité** : ⭐⭐ Opérationnel
**Badge angle** : 🛡️ Discipline managériale
**Badge temps de lecture** : 18 min

### Sommaire (TOC) proposé

```html
<ul class="module-toc-list" id="tocList">
  <li><a href="#executive-summary">⚡ L'essentiel</a></li>
  <li><a href="#section-1">🧭 Le problème de l'hallucination silencieuse</a></li>
  <li><a href="#section-2">📚 Typologie des hallucinations métier</a></li>
  <li><a href="#section-3">⚖️ Pattern « pas de claim de complétion sans preuve fraîche »</a></li>
  <li><a href="#section-4">🛡️ 4 niveaux de vérification proportionnés à l'enjeu</a></li>
  <li><a href="#section-5">👥 Qui vérifie quoi quand — discipline managériale</a></li>
  <li><a href="#section-6">📏 Outils de mesure (golden set, eval, humain dans la boucle)</a></li>
  <li><a href="#section-7">🚀 Plan d'action 30 jours</a></li>
  <li><a href="#ressources">📚 Pour aller plus loin</a></li>
</ul>
```

---

## Contenu détaillé par section

### Executive summary

**Titre exec** : *« Un agent IA peut déclarer une tâche terminée sans qu'elle le soit. La discipline de vérification est ce qui sépare une PME qui pilote l'IA d'une PME qui pilote à l'aveugle. »*

**5 takeaways** :

1. **L'hallucination silencieuse est le risque IA le plus sous-estimé en PME.** Un agent ne dit pas « je n'ai pas pu faire ça » — il dit « voilà ce que j'ai fait », même quand l'output est incorrect. Sans vérification, l'erreur passe directement en production.
2. **Quatre familles d'hallucinations métier reviennent quasi quotidiennement** : chiffres inventés, citations fabriquées, conclusions hors-périmètre, faux positifs de complétion (l'agent prétend avoir réalisé une action qu'il n'a pas faite).
3. **Le pattern « pas de claim de complétion sans preuve fraîche » est la règle absolue.** Aucun output IA ne doit être considéré comme valide tant qu'une vérification proportionnée à l'enjeu n'a pas été effectuée. Cette règle s'applique à l'humain qui valide comme à l'agent qui contrôle.
4. **4 niveaux de vérification proportionnés** : pas de vérification (POC sans enjeu), vérification par échantillonnage (production faible enjeu), vérification systématique humaine (production enjeu modéré), double validation humain + agent réviseur (production enjeu critique).
5. **Cette discipline est managériale, pas technique.** Elle se traduit en répartition de responsabilités, en routines d'équipe, en KPI de qualité. Sans ce volet managérial, les meilleures stacks techniques d'évaluation ne protègent pas la PME.

**Stat block** suggéré :

- **362** incidents IA documentés en 2025 (+55 % vs 2024 — Stanford AI Index Report 2026, déjà canonisé I-D-007)
- **45 %** du code IA-généré contient des failles (Cloud Security Alliance — cohérence avec CU-027 §3)
- **0** garantie de correction sans vérification effective de l'output
- **9 secondes** — temps qu'a mis un agent à supprimer une base de production + ses backups dans un incident documenté en mai 2026 (référence DEP-05 §8.5 failure receipt)

### Section 1 — Le problème de l'hallucination silencieuse

**Trois constats à intégrer en intro** :

1. **Un agent IA n'a pas conscience de ne pas savoir.** Quand il manque d'information ou se trompe, il **complète** plutôt que d'avouer l'ignorance. C'est une propriété structurelle des modèles génératifs, pas un bug ponctuel.
2. **L'hallucination est silencieuse par défaut.** L'output est syntaxiquement correct, le ton est confiant, la mise en forme professionnelle. Rien ne signale à l'utilisateur que le contenu est erroné — sauf vérification active.
3. **Le coût d'une hallucination détectée tardivement est asymétrique.** 100 réponses correctes apportent un gain marginal. 1 réponse incorrecte transmise à un client, intégrée dans un contrat ou utilisée pour une décision peut détruire la valeur accumulée.

**Citation à intégrer** (issue du retour McKinsey 2025) :

> *« Les organisations ne peuvent plus se contenter de craindre que l'IA dise la mauvaise chose, elles doivent contendre avec des systèmes qui font la mauvaise chose : actions non intentionnelles, mésusage d'outils, contournement de garde-fous. »*

(Source : McKinsey « Securing the agentic enterprise », mai 2026 — déjà intégrée PR-05 v3.10)

**Pourquoi c'est spécifiquement critique en PME** : la PME n'a généralement pas de cellule qualité dédiée à la vérification IA. Les outputs IA arrivent directement dans le flux de travail sans relais de contrôle. Le risque est donc plus élevé qu'en grande entreprise où une vérification — même imparfaite — existe par construction des process.

### Section 2 — Typologie des hallucinations métier

**4 familles d'hallucinations** à reconnaître, illustrées par des cas concrets adaptés au contexte PME :

#### 2.1 Chiffres inventés

**Pattern** : l'agent produit un chiffre précis (« le marché de la digitalisation PME pèse 3,7 Md€ en 2025 ») sans source vérifiable, parce que le chiffre **paraît plausible** dans le contexte de la réponse.

**Cas d'usage type** : un dirigeant demande à un agent de synthétiser une note sectorielle. L'agent produit des chiffres de marché que le dirigeant intègre dans une présentation client. 2 mois plus tard, un audit révèle que 3 chiffres sur 5 sont fabriqués.

**Détection** : croisement systématique avec sources officielles (INSEE, Bpifrance Le Lab, France Num, études institutionnelles). Si un chiffre ne peut pas être tracé vers une source publique, il ne doit pas être utilisé.

#### 2.2 Citations fabriquées

**Pattern** : l'agent attribue à une personnalité réelle (chercheur, dirigeant, expert) une citation qu'elle n'a jamais prononcée, parce que cette citation **renforce** le propos.

**Cas d'usage type** : un agent prépare une argumentation pour convaincre un comité d'investir dans un projet IA. Il cite Andrew Ng disant « toute entreprise qui n'investit pas dans l'IA en 2026 sera dépassée en 2028 ». Cette citation n'existe pas dans le corpus public d'Andrew Ng.

**Détection** : règle absolue **aucune citation ne peut être utilisée sans source vérifiable** (lien vers tweet, article, vidéo). Si l'agent cite sans lien, demander le lien. Si l'agent ne peut pas fournir le lien, la citation est fabriquée.

#### 2.3 Conclusions hors-périmètre

**Pattern** : l'agent répond à une question en sortant du périmètre des données qu'il a effectivement consultées. Il **extrapole** sans signaler qu'il extrapole.

**Cas d'usage type** : un agent analyse un contrat fournisseur. Il conclut « cette clause de confidentialité est standard dans votre secteur ». Or l'agent n'a accès à aucun corpus de contrats sectoriels — il extrapole sur la base de ses connaissances générales.

**Détection** : règle absolue **l'agent doit signaler explicitement quand il extrapole**. Si une conclusion ne peut pas être adossée à un document ou une donnée présente dans le contexte de la requête, elle doit être préfixée par « basé sur les données disponibles » ou « extrapolation à valider ».

#### 2.4 Faux positifs de complétion

**Pattern** : l'agent déclare une tâche terminée alors qu'elle a échoué silencieusement. C'est le pattern **« overclaimed completeness »** documenté dans la communauté builders en mai 2026 (référence DEP-05 §8.2 v3.9 gates TOML).

**Cas d'usage type** : un agent doit envoyer un email de confirmation à un prospect. Il déclare « email envoyé avec succès ». En réalité, l'API SMTP a renvoyé une erreur silencieuse — l'email n'a jamais été transmis. Le prospect n'a rien reçu. La PME pense avoir contacté le prospect.

**Détection** : règle absolue **toute déclaration de complétion doit être assortie d'une preuve fraîche** (par exemple, l'ID du message envoyé chez le provider SMTP, ou un fichier produit dont on vérifie l'existence et le contenu). Sans preuve fraîche, la complétion est non vérifiée — donc à considérer comme **non aboutie** jusqu'à vérification.

**Exemple documenté** : un coding agent a supprimé en 9 secondes une base de production + ses backups, en déclarant l'opération « terminée avec succès » (cité dans le pattern failure receipt DEP-05 §8.5 v3.10). Le mécanisme est exactement le même : déclaration de complétion non vérifiée.

### Section 3 — Pattern « pas de claim de complétion sans preuve fraîche »

**Le principe central** de la discipline de vérification, formulé en règle absolue :

> *« Aucun output IA n'est considéré comme valide tant qu'une preuve fraîche d'exécution n'a pas été produite et vérifiée. »*

**Application opérationnelle par type d'output** :

| Type d'output IA | Preuve fraîche acceptable | Niveau de vérification minimal |
|---|---|---|
| **Génération de texte** (note, mail, document) | Contenu lisible avec citations sources | Relecture humaine intégrale avant envoi externe |
| **Extraction de données** (chiffres, dates, entités) | Renvoi vers le passage source dans le document d'origine | Vérification par sondage minimum 10 % |
| **Action sur système externe** (envoi mail, mise à jour CRM, écriture fichier) | ID de transaction du système cible + vérification de l'état post-action | Vérification systématique pour actions à enjeu |
| **Recommandation ou décision** (« je recommande ») | Liste explicite des critères évalués + des alternatives écartées | Validation humaine obligatoire avant exécution |

**Garde-fou managérial** : ce principe doit être **codifié dans une procédure interne** de la PME, pas rester une bonne intention. Chaque agent IA en production a un « contrat de vérification » qui spécifie : qui vérifie, à quelle fréquence, sur quoi.

### Section 4 — 4 niveaux de vérification proportionnés à l'enjeu

La discipline de vérification ne se traite pas en tout-ou-rien. Quatre niveaux à calibrer selon l'enjeu de l'output :

#### Niveau 0 — Pas de vérification (POC sans enjeu)

**Contexte** : POC interne sur des données fictives, test en bac à sable, exploration. L'output ne sort jamais du périmètre POC.

**Risque acceptable** : aucun (puisque l'output n'a pas d'impact externe).

**Pratique** : pas de vérification systématique, simple relecture finale du résultat d'ensemble.

#### Niveau 1 — Vérification par échantillonnage (production faible enjeu)

**Contexte** : tâche répétée à fort volume, où une erreur ponctuelle est rattrapable (par exemple : tri automatique d'emails, catégorisation de tickets de support en first triage).

**Risque acceptable** : taux d'erreur <5 % corrigible a posteriori.

**Pratique** : échantillonnage de 5-10 % des outputs vérifiés par un humain, taux d'erreur mesuré et tracé, recalibrage si dérive observée.

#### Niveau 2 — Vérification systématique humaine (production enjeu modéré)

**Contexte** : output qui sort de l'entreprise ou qui prend une décision automatisée à impact business (par exemple : génération de propositions commerciales, réponses à des prospects, analyses de contrats).

**Risque acceptable** : pratiquement aucune erreur (1 erreur peut coûter un client ou créer un contentieux).

**Pratique** : chaque output relu et validé par un humain avant transmission externe. L'agent IA produit le draft, l'humain valide et signe.

#### Niveau 3 — Double validation humain + agent réviseur (production enjeu critique)

**Contexte** : décisions à fort impact (financier, juridique, sécurité, santé), actions irréversibles sur systèmes critiques (par exemple : modifications de bases de données, transferts financiers, signature de contrats).

**Risque acceptable** : zéro erreur.

**Pratique** : double validation systématique. Un humain valide. Un agent réviseur (différent de l'agent producteur) audite l'output selon des critères structurés. La conjonction des deux validations est requise.

**Heuristique de choix** : à chaque output IA en production, se poser la question « quelle est la conséquence d'une erreur non détectée ? ». Si la réponse est « rattrapable et limitée » → niveau 1. Si « réputationnelle ou contractuelle » → niveau 2. Si « critique ou irréversible » → niveau 3.

### Section 5 — Qui vérifie quoi quand — discipline managériale

La discipline de vérification ne fonctionne que si **la responsabilité est nommée**. Quatre dimensions à formaliser pour chaque agent IA en production :

**Dimension 1 — Le human owner désigné**
Pour chaque agent en production, **une personne physique est désignée** comme responsable de sa qualité d'output. Pas une équipe, une personne. Elle peut déléguer la vérification opérationnelle, mais la responsabilité reste sienne.

**Dimension 2 — Le rythme de vérification**
Selon le niveau (cf. § 4), la vérification est continue (niveau 2-3) ou par échantillonnage (niveau 1) avec fréquence définie (par exemple : « 10 outputs échantillonnés tous les vendredis »).

**Dimension 3 — La procédure d'escalade en cas d'erreur détectée**
Quand une erreur est détectée, qui est notifié ? Quelle est la procédure de correction ? L'output défaillant est-il rétro-corrigé chez le destinataire ? L'agent est-il suspendu en attendant la correction ?

**Dimension 4 — Le suivi des indicateurs de qualité**
Taux d'erreur observé, types d'erreurs récurrentes, dérives saisonnières. Ces indicateurs sont **partagés** avec la direction (revue mensuelle ou trimestrielle selon enjeu) pour permettre les arbitrages d'investissement.

**Cohérence avec le pattern « agent = employé »** (référence CU-026) : la discipline de vérification appliquée à un agent IA est exactement celle qu'on appliquerait à un employé junior qui démarre — supervision rapprochée au démarrage, autonomie graduelle avec contrôles d'échantillonnage, escalade en cas de doute.

### Section 6 — Outils de mesure (golden set, eval, humain dans la boucle)

Pour structurer la mesure de qualité des outputs IA, trois outils complémentaires.

#### 6.1 Golden set

**Définition** : ensemble de **questions de référence avec réponses attendues**, défini une fois pour toutes (ou révisé périodiquement) et utilisé pour mesurer la qualité de l'agent dans le temps.

**Construction** : 20 à 100 questions représentatives des cas d'usage réels, avec pour chacune la réponse attendue formulée par un expert humain.

**Usage** : à chaque évolution de l'agent (nouveau prompt, nouveau modèle, nouvelle source de données), exécuter le golden set et mesurer le pourcentage de réponses correctes. Si le score baisse, la modification est régressive.

**Coût indicatif** : la construction d'un golden set représente quelques jours de travail expert. Le coût d'exécution est faible (quelques euros par cycle d'évaluation sur 50 questions).

#### 6.2 Eval automatique (LLM-as-judge)

**Définition** : un second agent IA évalue les outputs du premier sur des critères structurés (factualité, format, ton, complétude).

**Usage** : permet d'évaluer un volume important d'outputs sans mobiliser systématiquement un humain. Particulièrement adapté pour les niveaux 1 et 2 de vérification (cf. § 4).

**Garde-fou** : l'agent évaluateur peut lui-même halluciner. Il faut donc périodiquement **comparer ses évaluations à celles d'un humain expert** pour calibrer sa fiabilité.

#### 6.3 Humain dans la boucle

**Définition** : un humain valide tout ou partie des outputs IA avant transmission ou exécution.

**Usage** : indispensable pour les niveaux 2 et 3. Pour le niveau 1, l'humain valide par échantillonnage.

**Effort** : l'humain dans la boucle est le mécanisme le plus coûteux mais le plus fiable. La question opérationnelle est **quelle fraction des outputs justifie ce coût** (cf. § 4 niveaux).

**Combinaison optimale** : golden set pour la mesure de régression, eval automatique pour le volume courant, humain dans la boucle pour les enjeux critiques.

### Section 7 — Plan d'action 30 jours

**Jours 1-7 — Diagnostic existant**
- Lister tous les agents IA actuellement en production dans l'entreprise (ChatGPT utilisé par les équipes, Copilot Microsoft, agents personnalisés, etc.)
- Pour chacun : identifier le human owner désigné (souvent inexistant à ce stade)
- Identifier les outputs IA qui sortent de l'entreprise sans vérification systématique

**Jours 8-14 — Calibrage des niveaux**
- Pour chaque agent identifié, classifier en niveau 0 / 1 / 2 / 3 (cf. § 4)
- Identifier les écarts entre niveau requis et niveau effectif
- Prioriser les écarts les plus critiques (niveau 3 requis avec niveau 0 effectif = priorité absolue)

**Jours 15-21 — Mise en place des procédures**
- Pour les agents en écart de niveau, mettre en place le mécanisme de vérification approprié (échantillonnage, validation systématique, double validation)
- Désigner les human owners explicitement
- Documenter les procédures dans une note interne courte (1-2 pages par agent)

**Jours 22-30 — Mesure et ajustement**
- Démarrer le suivi des indicateurs (taux d'erreur, types d'erreurs)
- Si un golden set n'existe pas pour un agent à enjeu, le construire (20-30 questions)
- Programmer une revue à 90 jours pour mesurer l'efficacité du dispositif

---

## Ressources à intégrer

### Articles de fond
- **Stanford AI Index Report 2026** — chapitre 3 « Responsible AI » : 362 incidents documentés en 2025 (déjà cité I-D-007). Cohérence cross-modules.
- **McKinsey « Securing the agentic enterprise »** — concept de cybersécurité agentique (déjà cité PR-05 v3.10)
- **Anthropic Engineering** — « Demystifying evals for AI agents » + « Quantifying infrastructure noise in agentic coding evals » (déjà citées DEP-07 v3.11)
- **@CliffDoesAI** — pattern failure receipt & ownership (déjà cité DEP-05 §8.5 v3.10)
- **@wernerk_au** — audit 7 cycles LLM-agent + gates TOML (déjà cité DEP-05 §8.2 v3.9)

### Tutoriels & cas pratiques
- **Template de procédure de vérification** par niveau (à fournir en téléchargement)
- **Auto-diagnostic** : à quel niveau de vérification se situent vos agents IA actuels ? (checklist 10 questions)

### Documentation officielle & études
- **Cloud Security Alliance** — recherche sécurité code IA-généré (déjà citée CU-027 §3)
- **NIST AI RMF + CAISI** — frameworks de gestion des risques agents IA (déjà cités PR-05 v3.10)
- **CNIL** — recommandations sur la supervision humaine et l'auditabilité (cohérence RGPD)
- **AI Act Article 14** — supervision humaine effective sur systèmes haut risque (déjà cité CU-026)

### Contacts opérationnels
- **AgentShield (composant ECC)** — audit sécurité gratuit pour configuration d'agents IA (déjà cité DEP-08 §3 + fiche outil ressources.html v3.11)
- **Bpifrance Le Lab** — études sur l'adoption qualité IA en PME

---

## Mise à jour navigation et page préalables

- Ajouter une **card PR-10** dans `prealables.html` après PR-09
- Position dans la liste : à la suite de PR-09 (ordre numérique)
- Icône suggérée : 🛡️
- Catégorie : « Discipline managériale »
- Cross-link depuis PR-04 (qualité du code IA), PR-05 (sécurité IA), CU-026 (gouvernance agents), DEP-05 §8.5 (failure receipt), DEP-07 (evals)

## Renvois croisés vers autres préalables (à mettre à jour dans les modules existants)

- **PR-05 (Sécurité IA)** : encart « complémentaire à PR-10 sur la discipline de vérification opérationnelle »
- **CU-026 (Gouvernance agents IA)** : §3bis Frontier Firms peut mentionner PR-10 pour le volet vérification des outputs
- **DEP-05 §8.5 (Failure receipt v3.10)** : encart « pendant managérial accessible aux non-IT — voir PR-10 »
- **DEP-07 (Evals)** : encart « cadre managérial pour appliquer ces évaluations en PME — voir PR-10 »

## Métadonnées module

- `<meta name="description">` : *« Vérifier et limiter les hallucinations IA : 4 niveaux de vérification proportionnés à l'enjeu, pattern « pas de claim de complétion sans preuve fraîche », typologie des hallucinations métier. La discipline managériale qui sépare les PME qui pilotent l'IA de celles qui pilotent à l'aveugle. »*
- Badge temps de lecture : **18 min**

## Item parallèle (à compiler dans brief v3.12)

Pas de canonisation chiffre macro nouveau pour PR-10 — les chiffres mobilisés (362 incidents, 45 % failles code IA, 9 secondes incident) sont déjà canonisés via I-D-006/I-D-007 ou sont des références ponctuelles non réutilisables cross-modules.
