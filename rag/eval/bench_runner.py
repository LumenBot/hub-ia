#!/usr/bin/env python3
"""Bench runner S2.9 — wrapper paramétrable autour de `run_eval`.

Permet d'évaluer le golden set avec des variations de configuration (top_k,
modèle d'embedding, modèle de génération, collection ChromaDB) sans modifier
le code de production (`query.py`, `run_eval.py`, `ingest.py`).

Réutilise :
- `query.Embedder`, `query.Retriever`, `query.Generator`, `query.answer_question`
- `run_eval.run_eval()`, `run_eval.format_report()`, `run_eval.EvalItem`

Sortie : rapport texte + JSON au même format que `run_eval` natif.

Utilisé pour les Lots Bench-2/3/4/5 S2.9 (optimisations latence/qualité). Le
Bench-1 (reranking Cohere/cross-encoder) nécessite une clé API ou un install
lourd et n'est pas couvert ici (à scorer hors de ce wrapper si activé).
"""
from __future__ import annotations

import argparse
import dataclasses
import importlib.util
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # rag/
QUERY = os.path.join(ROOT, "code", "backend", "query.py")
RUN_EVAL = os.path.join(ROOT, "code", "eval", "run_eval.py")

# Charge le .env via _env (clés API)
sys.path.insert(0, os.path.join(ROOT, "code"))
import _env  # noqa: F401

try:
    import yaml
except ImportError:
    print("[erreur] pyyaml requis", file=sys.stderr); sys.exit(2)


def _load(name: str, path: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Bench runner S2.9 (variations conf retrieval/gen).")
    p.add_argument("--questions", required=True)
    p.add_argument("--report", required=True)
    p.add_argument("--json", dest="json_path", required=True)
    p.add_argument("--top-k", type=int, default=5)
    p.add_argument("--embed-model", default="text-embedding-3-small")
    p.add_argument("--gen-model", default="claude-sonnet-4-6")
    p.add_argument("--collection", default="hub-ia-rag")
    p.add_argument("--store", default=os.path.join(ROOT, "code", "vector_store"))
    p.add_argument("--bench-name", default="bench", help="étiquette dans l'en-tête du rapport")
    args = p.parse_args(argv)

    query = _load("query", QUERY)
    run_eval = _load("run_eval", RUN_EVAL)

    print(f"[bench] {args.bench_name} | top_k={args.top_k} embed={args.embed_model} "
          f"gen={args.gen_model} coll={args.collection}", flush=True)

    embedder = query.Embedder(model=args.embed_model)
    retriever = query.Retriever(persist_path=args.store, collection=args.collection)
    generator = query.Generator(model=args.gen_model)

    def runner(q: str) -> dict:
        return query.answer_question(q, embedder, retriever, generator, k=args.top_k).to_dict()

    with open(args.questions, encoding="utf-8") as f:
        questions = yaml.safe_load(f) or []

    items = run_eval.run_eval(questions, runner)

    header = (
        f"# BENCH S2.9 : {args.bench_name}\n"
        f"# top_k={args.top_k}  embed={args.embed_model}  gen={args.gen_model}  collection={args.collection}\n\n"
    )
    with open(args.report, "w", encoding="utf-8") as f:
        f.write(header + run_eval.format_report(items))
    with open(args.json_path, "w", encoding="utf-8") as f:
        json.dump([dataclasses.asdict(it) for it in items], f, ensure_ascii=False, indent=2)

    # Récap coût (S2.2 Lot C)
    try:
        import _cost
        s = _cost.summarize_cost()
        if s["total_calls"] > 0:
            print(_cost.format_cost_summary(s))
    except Exception:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
