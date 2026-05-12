#!/usr/bin/env python3
"""
Backend RAG — CLI Python S1 (Cloudflare Worker reporté à S3)
=============================================================

Reçoit une question en CLI, calcule son embedding (OpenAI), récupère le top-k=5
dans ChromaDB, construit un contexte (chunks + métadonnées), appelle Claude
Sonnet 4.6 (D-005) avec un system prompt structuré, retourne la réponse + les
codes sources citées.

Usage :
    python3 rag/code/backend/query.py "Quelle différence entre RAG et fine-tuning ?"
    python3 rag/code/backend/query.py -k 3 --json "ma question"

Variables d'env attendues :
    OPENAI_API_KEY            (embedding question)
    ANTHROPIC_API_KEY         (génération)
    RAG_EMBEDDING_MODEL       (défaut : text-embedding-3-small)
    RAG_GEN_MODEL             (défaut : claude-sonnet-4-6)
    RAG_VECTOR_STORE_PATH     (défaut : rag/code/vector_store)

Réfs : D-005, D-006, D-007, D-008 (S3).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass
from typing import Any


ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DEFAULT_STORE = os.path.join(ROOT, "code", "vector_store")
DEFAULT_COLLECTION = "hub-ia-rag"
DEFAULT_K = 5

SYSTEM_PROMPT = """Tu es l'assistant du Hub IA Learning Center, plateforme \
pédagogique destinée aux dirigeants de PME/ETI françaises non-IT. Tu réponds à \
leurs questions sur l'IA générative, l'agentique, le RAG, et leurs prérequis.

Ton et style :
- Pédagogique, concret, dépolitisé.
- Pas de jargon non défini ; quand un terme technique est utilisé, on le \
glose en une phrase.
- Pas d'invention de chiffres ou de sources : seules les données présentes \
dans le CONTEXTE ci-dessous sont valides.
- Citations obligatoires : chaque assertion factuelle doit être suivie du \
code source entre crochets, par exemple [CU-008] ou [DEP-02].
- Si le CONTEXTE ne couvre pas la question, dis explicitement « Je n'ai pas \
de réponse documentée dans le Hub IA pour cette question » plutôt que d'extrapoler.

Format de réponse :
1. Réponse directe en 2-4 paragraphes.
2. Ligne « Sources : » à la fin listant les codes utilisés (ex. : CU-001, DEP-02).
"""


@dataclass
class RetrievedChunk:
    chunk_id: str
    document: str
    metadata: dict
    distance: float


@dataclass
class QueryResult:
    question: str
    answer: str
    chunks: list[RetrievedChunk]
    cited_codes: list[str]

    def to_dict(self) -> dict:
        return {
            "question": self.question,
            "answer": self.answer,
            "cited_codes": self.cited_codes,
            "chunks": [
                {
                    "chunk_id": c.chunk_id,
                    "code": c.metadata.get("code", ""),
                    "titre": c.metadata.get("titre", ""),
                    "h2_title": c.metadata.get("h2_title", ""),
                    "source_file": c.metadata.get("source_file", ""),
                    "distance": c.distance,
                }
                for c in self.chunks
            ],
        }


# ============================================================
# Abstractions (mockables en test)
# ============================================================

class Embedder:
    def __init__(self, model: str = "text-embedding-3-small", api_key: str | None = None):
        self.model = model
        self._client = None
        self._api_key = api_key or os.environ.get("OPENAI_API_KEY")

    def _ensure(self):
        if self._client is None:
            if not self._api_key:
                raise RuntimeError("OPENAI_API_KEY manquante")
            from openai import OpenAI  # type: ignore
            self._client = OpenAI(api_key=self._api_key)
        return self._client

    def embed_one(self, text: str) -> list[float]:
        client = self._ensure()
        resp = client.embeddings.create(model=self.model, input=[text])
        return resp.data[0].embedding


class Retriever:
    """Wrapper minimal sur ChromaDB pour récupérer les top-k chunks."""

    def __init__(self, persist_path: str = DEFAULT_STORE, collection: str = DEFAULT_COLLECTION, client=None):
        if client is not None:
            self._client = client
        else:
            import chromadb  # type: ignore
            self._client = chromadb.PersistentClient(path=persist_path)
        self.collection = self._client.get_or_create_collection(name=collection)

    def query(self, embedding: list[float], k: int = DEFAULT_K) -> list[RetrievedChunk]:
        res = self.collection.query(
            query_embeddings=[embedding],
            n_results=k,
            include=["documents", "metadatas", "distances"],
        )
        ids = (res.get("ids") or [[]])[0]
        docs = (res.get("documents") or [[]])[0]
        metas = (res.get("metadatas") or [[]])[0]
        dists = (res.get("distances") or [[]])[0]
        return [
            RetrievedChunk(chunk_id=i, document=d, metadata=m or {}, distance=float(dist))
            for i, d, m, dist in zip(ids, docs, metas, dists)
        ]


class Generator:
    def __init__(self, model: str = "claude-sonnet-4-6", api_key: str | None = None):
        self.model = model
        self._client = None
        self._api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")

    def _ensure(self):
        if self._client is None:
            if not self._api_key:
                raise RuntimeError("ANTHROPIC_API_KEY manquante")
            import anthropic  # type: ignore
            self._client = anthropic.Anthropic(api_key=self._api_key)
        return self._client

    def generate(self, system: str, user: str, max_tokens: int = 1024) -> str:
        client = self._ensure()
        msg = client.messages.create(
            model=self.model,
            max_tokens=max_tokens,
            system=system,
            messages=[{"role": "user", "content": user}],
        )
        return "".join(block.text for block in msg.content if getattr(block, "type", None) == "text")


# ============================================================
# Construction du contexte + extraction des citations
# ============================================================

def build_context(chunks: list[RetrievedChunk]) -> str:
    """Concatène les chunks récupérés pour le prompt utilisateur."""
    blocks: list[str] = []
    for i, c in enumerate(chunks, 1):
        code = c.metadata.get("code", "?")
        titre = c.metadata.get("titre", "")
        h2 = c.metadata.get("h2_title", "")
        blocks.append(
            f"--- Chunk #{i} | code={code} | titre={titre} | section={h2} "
            f"| similarity={1 - c.distance:.3f} ---\n{c.document}"
        )
    return "\n\n".join(blocks)


def build_user_prompt(question: str, chunks: list[RetrievedChunk]) -> str:
    if not chunks:
        return (
            f"QUESTION : {question}\n\n"
            "CONTEXTE : (aucun chunk pertinent trouvé dans le vault)\n\n"
            "Réponds en indiquant que la question n'est pas couverte par le Hub IA."
        )
    return (
        f"QUESTION :\n{question}\n\n"
        f"CONTEXTE — extraits du vault Hub IA :\n\n{build_context(chunks)}\n\n"
        "Réponds à la question en t'appuyant strictement sur le CONTEXTE ci-dessus. "
        "Cite les codes sources entre crochets après chaque assertion factuelle. "
        "Termine par une ligne « Sources : ... »."
    )


CODE_PATTERN = re.compile(r"\[(CU-\d+|PR-\d+|DEP-\d+|A\d+|OUTILS-[A-Z0-9-]+|TRANSVERSE-[A-Z0-9-]+)\]", re.IGNORECASE)


def extract_cited_codes(answer: str) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for m in CODE_PATTERN.finditer(answer):
        code = m.group(1).upper()
        if code not in seen:
            seen.add(code)
            out.append(code)
    return out


# ============================================================
# Orchestration
# ============================================================

def answer_question(
    question: str,
    embedder: Embedder,
    retriever: Retriever,
    generator: Generator,
    k: int = DEFAULT_K,
    system_prompt: str = SYSTEM_PROMPT,
) -> QueryResult:
    q_vec = embedder.embed_one(question)
    chunks = retriever.query(q_vec, k=k)
    user_prompt = build_user_prompt(question, chunks)
    answer = generator.generate(system_prompt, user_prompt)
    return QueryResult(
        question=question,
        answer=answer,
        chunks=chunks,
        cited_codes=extract_cited_codes(answer),
    )


# ============================================================
# CLI
# ============================================================

def format_human(result: QueryResult) -> str:
    lines: list[str] = []
    lines.append("=" * 70)
    lines.append(f"Q: {result.question}")
    lines.append("=" * 70)
    lines.append(result.answer.strip())
    lines.append("")
    lines.append("-" * 70)
    lines.append(f"Top-{len(result.chunks)} chunks récupérés :")
    for c in result.chunks:
        code = c.metadata.get("code", "?")
        h2 = c.metadata.get("h2_title", "")
        lines.append(f"  • [{code.upper()}] {h2}  (sim={1 - c.distance:.3f})")
    if result.cited_codes:
        lines.append(f"Codes cités dans la réponse : {', '.join(result.cited_codes)}")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Backend RAG CLI — question → réponse Claude avec citations.")
    parser.add_argument("question", help="question à poser au Hub IA")
    parser.add_argument("-k", "--top-k", type=int, default=DEFAULT_K)
    parser.add_argument("--store", default=os.environ.get("RAG_VECTOR_STORE_PATH", DEFAULT_STORE))
    parser.add_argument("--collection", default=DEFAULT_COLLECTION)
    parser.add_argument("--embedding-model", default=os.environ.get("RAG_EMBEDDING_MODEL", "text-embedding-3-small"))
    parser.add_argument("--gen-model", default=os.environ.get("RAG_GEN_MODEL", "claude-sonnet-4-6"))
    parser.add_argument("--json", action="store_true", help="sortie JSON pour pipeline (eval)")
    args = parser.parse_args(argv)

    embedder = Embedder(model=args.embedding_model)
    retriever = Retriever(persist_path=args.store, collection=args.collection)
    generator = Generator(model=args.gen_model)

    result = answer_question(args.question, embedder, retriever, generator, k=args.top_k)

    if args.json:
        print(json.dumps(result.to_dict(), ensure_ascii=False, indent=2))
    else:
        print(format_human(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
