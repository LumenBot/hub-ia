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

## Gouvernance

Les fichiers vivants (`JOURNAL-POC-RAG.md`, `STATUS-RAG.md`, `DECISIONS-RAG.md`, `SPEC-MD-POUR-RAG.md`) restent dans `rag-prep/` à la racine du repo (source de vérité unique du couple 2 — D-024).
