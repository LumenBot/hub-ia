#!/usr/bin/env python3
"""Dump retrieval top-10 — S2.5 Lot Drer (diagnostic ciblé).

Pour chacune des 4 questions du Lot Drer, calcule l'embedding (OpenAI) et
récupère le top-10 ChromaDB SANS appel Anthropic (génération exclue pour
économiser le budget — seul le rang/similarité des chunks importe ici).

Met en évidence le chunk cible attendu (cu-001 / pr-07 / pr-08) et son rang.

Usage : python -m rag.eval._dump_retrieval_drer
"""
from __future__ import annotations

import importlib.util
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # rag/
QUERY_SCRIPT = os.path.join(ROOT, "code", "backend", "query.py")

# Charge le backend (Embedder + Retriever) comme run_eval.py
spec = importlib.util.spec_from_file_location("query", QUERY_SCRIPT)
query = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = query
spec.loader.exec_module(query)

TARGETS = [
    ("q-002", "Quelles sont les sources fiables pour suivre l'actualité IA générative en 2026 ?", "cu-001"),
    ("q-030", "Quelles sont les obligations réglementaires à anticiper pour un projet IA en PME en 2026 ?", "pr-07"),
    ("q-051", "Quels sont les 7 dispositifs fiscaux mobilisables pour financer un projet IA en PME en 2026 ?", "pr-08"),
    ("q-052", "Quelle est la règle des 5 étapes pour empiler les dispositifs de financement IA en PME ?", "pr-08"),
]

K = 10


def main() -> int:
    embedder = query.Embedder()
    retriever = query.Retriever()

    print("=" * 78)
    print("DUMP RETRIEVAL top-%d — S2.5 Lot Drer (génération Anthropic exclue)" % K)
    print("=" * 78)

    for qid, question, target_code in TARGETS:
        vec = embedder.embed_one(question)
        chunks = retriever.query(vec, k=K)
        target_rank = None
        target_sim = None
        for rank, c in enumerate(chunks, 1):
            if c.metadata.get("code", "") == target_code and target_rank is None:
                target_rank = rank
                target_sim = 1 - c.distance
        in_top5 = "OUI" if (target_rank is not None and target_rank <= 5) else "NON"

        print()
        print("-" * 78)
        print(f"{qid} — cible attendue : [{target_code}]")
        print(f"   Question : {question}")
        if target_rank is not None:
            print(f"   >>> [{target_code}] rang #{target_rank} | sim cosine {target_sim:.4f} "
                  f"| dans top-5 : {in_top5}")
        else:
            print(f"   >>> [{target_code}] ABSENT du top-{K} | dans top-5 : NON")
        print(f"   top-{K} :")
        for rank, c in enumerate(chunks, 1):
            code = c.metadata.get("code", "?")
            h2 = c.metadata.get("h2_title", "")
            sim = 1 - c.distance
            mark = "  <== CIBLE" if code == target_code else ""
            print(f"     #{rank:2d}  [{code:24s}] sim={sim:.4f}  {h2[:48]}{mark}")

    print()
    print("=" * 78)
    return 0


if __name__ == "__main__":
    sys.exit(main())
