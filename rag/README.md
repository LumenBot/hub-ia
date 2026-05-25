# `rag/` — Pipeline RAG du Hub IA Learning Center (couple 2)

Dossier racine du pipeline Retrieval-Augmented Generation. Vit en parallèle du site HTML (couche pédagogique du couple 1), qu'il ne touche jamais (D-002, D-022).

## Arborescence

```
rag/
├── content/          # vault Obsidian (MD optimisés RAG, écrits par Cowork)
│   ├── modules/      # cu-001.md, cu-008.md, ...
│   ├── prealables/   # pr-01.md, ...
│   ├── deploiement/  # dep-01.md, ...
│   ├── architectures/
│   ├── ressources/   # outils-vector-db.md, ...
│   ├── transverses/  # brain pages
│   └── glossaire.md  # canonique (produit par Cowork)
├── code/
│   ├── ingestion/    # ingest.py — chunking + embeddings + ChromaDB
│   ├── backend/      # query.py — retrieval + Claude (CLI S1, Worker S3)
│   ├── audit/        # audit-md-rag.py — conformité MD vs SPEC v1
│   └── eval/         # run_eval.py — rejoue le golden set
├── eval/
│   ├── questions.yaml      # 10 questions pilote
│   └── golden-answers.yaml # réponses/critères attendus
└── docs/             # doc technique additionnelle
```

## Conventions clés

- **Format MD** : voir `rag-prep/SPEC-MD-POUR-RAG.md` (frontmatter 10 champs, H1 unique, sections H2 autonomes 400-700 tokens).
- **Chunking** : section H2 = chunk, frontmatter injecté en tête, subdivision H3 si > 800 tokens (D-011).
- **Embeddings** : OpenAI `text-embedding-3-small` (D-007).
- **Vector DB** : ChromaDB local (`rag/code/vector_store/`, .gitignored) — D-006.
- **LLM** : Claude Sonnet 4.6 principal, Haiku 4.5 pour tâches simples (D-005).

## Installation locale

```bash
cd rag/code
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # puis remplir ANTHROPIC_API_KEY et OPENAI_API_KEY
```

## Cycle pilote (S1)

```bash
# 1. Audit conformité MD
python code/audit/audit-md-rag.py

# 2. Ingestion (re-indexation incrémentale)
python code/ingestion/ingest.py

# 3. Interroger
python code/backend/query.py "Quelle différence entre RAG et fine-tuning ?"

# 4. Évaluation golden set
python code/eval/run_eval.py
```

## Évaluation — modes standard et adversarial (S2.7)

`run_eval.py` distingue deux modes de question dans `eval/questions.yaml` :

- **Standard** : `expected_sources` non vide + `expected_concepts`. Scoring sur sources retrouvées (citées par le RAG) + concepts couverts (≥ 50 %, matching synonymes option B — S2.3).
- **Adversarial** (question piège) : `expected_refusal: true` OU `expected_sources: []`. Le RAG doit **refuser** de répondre. Scoring :
  - **refus correct** (score 1) : la réponse contient ≥ 1 marqueur canonique de refus ET ne cite aucune source.
  - **refus partiel** (score 0) : marqueur de refus présent MAIS sources citées (doute exprimé + tentative de réponse).
  - **hallucination** (score 0) : aucun marqueur, le RAG cite des sources et invente une réponse plausible.

Marqueurs canoniques de refus (insensible à la casse) : `pas dans le corpus`, `hors scope`, `je ne dispose pas`, `aucune information`, `ne figure pas dans les documents`, `pas d'élément`, `je ne peux pas répondre`.

Exemple de question adversariale :

```yaml
- id: q-adv-001
  question: "Quel est le seuil d'éligibilité au dispositif XYZ-2027 de Bpifrance ?"
  expected_refusal: true
  refusal_reason: "Dispositif XYZ-2027 inexistant (question piège)"
  unit: adversarial
```

Le rapport `eval-report-*.md` sépare les résultats en **2 blocs** : Bloc 1 (eval standard) + Bloc 2 (eval adversarial — refus corrects, hallucinations détectées, refus partiels avec liste nominative).

## Gouvernance

Les fichiers vivants (`JOURNAL-POC-RAG.md`, `STATUS-RAG.md`, `DECISIONS-RAG.md`, `SPEC-MD-POUR-RAG.md`) restent dans `rag-prep/` à la racine du repo (source de vérité unique du couple 2 — D-024).
