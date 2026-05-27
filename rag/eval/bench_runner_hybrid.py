#!/usr/bin/env python3
"""Bench S2.9 #4 — Hybrid retrieval BM25 + dense + RRF fusion.

Récupère top-N (=15) en dense (embedding 3-small + ChromaDB) ET top-N en BM25
(sur les documents bruts indexés en mémoire), puis fusionne par Reciprocal
Rank Fusion (RRF, k=60) et garde les top-k=5 finaux pour la génération.

Vise les questions à vocabulaire spécifique (acronymes, chiffres, noms
propres) que la similarité dense purement sémantique peut rater (cf. cas
q-083 S2.8 où outils-llm est manqué sur « tarif API Sonnet/Opus »).

Réutilise `query.Embedder`/`Generator`/`build_user_prompt`/`extract_cited_codes`/
`SYSTEM_PROMPT`/`QueryResult` et `run_eval.run_eval`/`format_report`.
"""
from __future__ import annotations

import argparse
import dataclasses
import importlib.util
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # rag/
sys.path.insert(0, os.path.join(ROOT, "code"))
import _env  # noqa: F401

import yaml
import chromadb
from rank_bm25 import BM25Okapi


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec); sys.modules[name] = mod
    spec.loader.exec_module(mod); return mod


_TOKEN_RE = re.compile(r"\w+", re.UNICODE)


def tokenize(text: str) -> list[str]:
    return _TOKEN_RE.findall((text or "").lower())


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("--questions", required=True)
    p.add_argument("--report", required=True)
    p.add_argument("--json", dest="json_path", required=True)
    p.add_argument("--top-k", type=int, default=5)
    p.add_argument("--n-each", type=int, default=15, help="top-N par méthode avant fusion")
    p.add_argument("--rrf-k", type=int, default=60)
    p.add_argument("--collection", default="hub-ia-rag")
    p.add_argument("--store", default=os.path.join(ROOT, "code", "vector_store"))
    p.add_argument("--bench-name", default="bench-4-bm25-hybrid")
    args = p.parse_args(argv)

    query = _load("query", os.path.join(ROOT, "code", "backend", "query.py"))
    run_eval = _load("run_eval", os.path.join(ROOT, "code", "eval", "run_eval.py"))

    print(f"[{args.bench_name}] chargement collection {args.collection}...", flush=True)
    client = chromadb.PersistentClient(path=args.store)
    col = client.get_or_create_collection(name=args.collection)
    data = col.get(include=["documents", "metadatas"])
    ids = data["ids"]
    docs = data["documents"] or []
    metas = data["metadatas"] or [{}] * len(ids)

    print(f"[{args.bench_name}] BM25 sur {len(docs)} chunks...", flush=True)
    tokenized = [tokenize(d) for d in docs]
    bm25 = BM25Okapi(tokenized)
    id2idx = {cid: i for i, cid in enumerate(ids)}

    embedder = query.Embedder()
    generator = query.Generator()

    def hybrid_retrieve(question: str):
        emb = embedder.embed_one(question)
        dres = col.query(
            query_embeddings=[emb], n_results=args.n_each,
            include=["documents", "metadatas", "distances"],
        )
        d_ids = (dres.get("ids") or [[]])[0]
        d_dists = (dres.get("distances") or [[]])[0]
        d_docs = (dres.get("documents") or [[]])[0]
        d_metas = (dres.get("metadatas") or [[]])[0]
        id2dense = {cid: (d_dists[r], d_docs[r], d_metas[r] or {}) for r, cid in enumerate(d_ids)}

        bm_scores = bm25.get_scores(tokenize(question))
        bm_top_idx = sorted(range(len(bm_scores)), key=lambda i: -bm_scores[i])[:args.n_each]
        bm_top_ids = [ids[i] for i in bm_top_idx]

        # RRF fusion
        score = {}
        for r, cid in enumerate(d_ids):
            score[cid] = score.get(cid, 0.0) + 1.0 / (args.rrf_k + r + 1)
        for r, cid in enumerate(bm_top_ids):
            score[cid] = score.get(cid, 0.0) + 1.0 / (args.rrf_k + r + 1)
        fused = sorted(score.items(), key=lambda x: -x[1])[:args.top_k]

        chunks = []
        for cid, sc in fused:
            if cid in id2dense:
                dist, doc, meta = id2dense[cid]
            else:
                i = id2idx[cid]
                dist = max(0.0, 1.0 - sc * 20)  # proxy similarité
                doc = docs[i]; meta = metas[i] or {}
            chunks.append(query.RetrievedChunk(
                chunk_id=cid, document=doc, metadata=meta, distance=float(dist),
            ))
        return chunks

    def runner(question: str) -> dict:
        chunks = hybrid_retrieve(question)
        user_prompt = query.build_user_prompt(question, chunks)
        answer = generator.generate(query.SYSTEM_PROMPT, user_prompt)
        return query.QueryResult(
            question=question, answer=answer, chunks=chunks,
            cited_codes=query.extract_cited_codes(answer),
        ).to_dict()

    with open(args.questions, encoding="utf-8") as f:
        questions = yaml.safe_load(f) or []

    items = run_eval.run_eval(questions, runner)

    header = (
        f"# BENCH S2.9 : {args.bench_name}\n"
        f"# Hybrid retrieval BM25 + dense (RRF fusion) — collection={args.collection} "
        f"top_k={args.top_k} n_each={args.n_each} rrf_k={args.rrf_k}\n\n"
    )
    with open(args.report, "w", encoding="utf-8") as f:
        f.write(header + run_eval.format_report(items))
    with open(args.json_path, "w", encoding="utf-8") as f:
        json.dump([dataclasses.asdict(it) for it in items], f, ensure_ascii=False, indent=2)

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
