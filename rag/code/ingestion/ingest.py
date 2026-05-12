#!/usr/bin/env python3
"""
Pipeline d'ingestion ChromaDB — v1
==================================

Parcourt `rag/content/**/*.md`, découpe chaque fichier en chunks selon D-011
(section H2 = chunk, subdivision H3 si > 800 tokens), calcule les embeddings
via OpenAI text-embedding-3-small (D-007), et insère dans ChromaDB local
(D-006) avec re-indexation incrémentale (hash + version).

Usage :
    python3 rag/code/ingestion/ingest.py [--vault PATH] [--store PATH] [--dry-run]

Variables d'env attendues :
    OPENAI_API_KEY            (sauf --dry-run)
    RAG_EMBEDDING_MODEL       (défaut : text-embedding-3-small)
    RAG_VECTOR_STORE_PATH     (défaut : rag/code/vector_store)
    RAG_CONTENT_PATH          (défaut : rag/content)

Réfs : D-006, D-007, D-011, D-019.
"""

from __future__ import annotations

import argparse
import glob
import hashlib
import os
import re
import sys
import unicodedata
from dataclasses import dataclass, field
from typing import Iterable

# Chargement automatique de rag/code/.env (S1ter Lot S1c.1)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import _env  # noqa: F401  # side-effect: load_env() au moment de l'import

try:
    import yaml
except ImportError:
    print("[erreur] pyyaml requis : pip install pyyaml", file=sys.stderr)
    sys.exit(2)


ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DEFAULT_VAULT = os.path.join(ROOT, "content")
DEFAULT_STORE = os.path.join(ROOT, "code", "vector_store")
DEFAULT_COLLECTION = "hub-ia-rag"

CHUNK_TOKEN_LIMIT = 800
TOKENS_PER_WORD = 1.3


# ============================================================
# Structures
# ============================================================

@dataclass
class Chunk:
    chunk_id: str
    text: str
    metadata: dict
    content_hash: str = field(init=False)

    def __post_init__(self) -> None:
        self.content_hash = hashlib.sha256(self.text.encode("utf-8")).hexdigest()


# ============================================================
# Parsing : frontmatter + sections
# ============================================================

def split_frontmatter(text: str) -> tuple[dict, str]:
    if not (text.startswith("---\n") or text.startswith("---\r\n")):
        return {}, text
    end = text.find("\n---", 4)
    if end == -1:
        return {}, text
    fm_raw = text[4:end]
    body = text[end + 4:].lstrip("\n")
    try:
        data = yaml.safe_load(fm_raw) or {}
        if not isinstance(data, dict):
            return {}, body
        return data, body
    except yaml.YAMLError:
        return {}, body


def estimate_tokens(text: str) -> int:
    return int(len(text.split()) * TOKENS_PER_WORD)


def slugify(text: str) -> str:
    s = unicodedata.normalize("NFKD", text)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower().strip()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-") or "section"


def split_sections(body: str) -> list[tuple[str, str, str]]:
    """Retourne [(level, title, content_with_heading), ...] pour h1/h2/h3."""
    lines = body.splitlines(keepends=True)
    sections: list[tuple[str, str, str]] = []
    cur_level: str | None = None
    cur_title: str | None = None
    cur_buf: list[str] = []

    for line in lines:
        m = re.match(r"^(#{1,3})\s+(.+?)\s*$", line.rstrip("\n"))
        if m:
            if cur_level is not None:
                sections.append((cur_level, cur_title or "", "".join(cur_buf)))
            cur_level = f"h{len(m.group(1))}"
            cur_title = m.group(2).strip()
            cur_buf = [line]
        else:
            cur_buf.append(line)

    if cur_level is not None:
        sections.append((cur_level, cur_title or "", "".join(cur_buf)))

    return sections


def serialize_frontmatter_header(fm: dict) -> str:
    """Bloc de métadonnées injecté en tête de chaque chunk (D-011)."""
    lines = ["[METADATA]"]
    for key in ("code", "titre", "type", "axe", "niveau", "version", "tags", "public_cible"):
        if key in fm:
            value = fm[key]
            if isinstance(value, list):
                value = ", ".join(str(v) for v in value)
            lines.append(f"{key}: {value}")
    lines.append("[CONTENT]")
    return "\n".join(lines) + "\n"


def _metadata_for_chunk(fm: dict, source_file: str, chunk_id: str, h2_title: str) -> dict:
    def _join(value) -> str:
        if isinstance(value, list):
            return ", ".join(str(v) for v in value)
        return str(value) if value is not None else ""

    return {
        "code": _join(fm.get("code", "")),
        "titre": _join(fm.get("titre", "")),
        "type": _join(fm.get("type", "")),
        "axe": _join(fm.get("axe", "")),
        "niveau": _join(fm.get("niveau", "")),
        "tags": _join(fm.get("tags", [])),
        "version": _join(fm.get("version", "")),
        "public_cible": _join(fm.get("public_cible", [])),
        "source_file": source_file,
        "chunk_id": chunk_id,
        "h2_title": h2_title,
    }


def build_chunks(fp: str, vault: str) -> list[Chunk]:
    """Produit les chunks d'un fichier MD selon D-011."""
    with open(fp, encoding="utf-8") as f:
        text = f.read()

    fm, body = split_frontmatter(text)
    if not fm:
        return []

    code = str(fm.get("code", "")).strip().lower() or os.path.splitext(os.path.basename(fp))[0]
    source_file = os.path.relpath(fp, vault)
    header = serialize_frontmatter_header(fm)

    sections = split_sections(body)
    chunks: list[Chunk] = []

    i = 0
    while i < len(sections):
        level, title, content = sections[i]
        if level != "h2":
            i += 1
            continue

        # H3 enfants éventuels
        children: list[tuple[str, str, str]] = []
        j = i + 1
        while j < len(sections) and sections[j][0] == "h3":
            children.append(sections[j])
            j += 1

        h2_slug = slugify(title)

        if children and any(estimate_tokens(c[2]) > CHUNK_TOKEN_LIMIT for c in children) or (
            children and estimate_tokens(content + "".join(c[2] for c in children)) > CHUNK_TOKEN_LIMIT
        ):
            # Subdivision : chaque H3 devient un chunk
            for _, ch_title, ch_content in children:
                ch_slug = slugify(ch_title)
                chunk_id = f"{code}#{h2_slug}#{ch_slug}"
                chunks.append(Chunk(
                    chunk_id=chunk_id,
                    text=header + content.split("\n", 1)[0] + "\n\n" + ch_content,
                    metadata=_metadata_for_chunk(fm, source_file, chunk_id, title),
                ))
        else:
            full = content + "".join(c[2] for c in children)
            chunk_id = f"{code}#{h2_slug}"
            chunks.append(Chunk(
                chunk_id=chunk_id,
                text=header + full,
                metadata=_metadata_for_chunk(fm, source_file, chunk_id, title),
            ))

        i = j if children else i + 1

    return chunks


def collect_chunks(vault: str) -> list[Chunk]:
    files = sorted(glob.glob(os.path.join(vault, "**", "*.md"), recursive=True))
    all_chunks: list[Chunk] = []
    for fp in files:
        all_chunks.extend(build_chunks(fp, vault))
    return all_chunks


# ============================================================
# Embeddings : abstraction (mockable en test)
# ============================================================

class Embedder:
    """Abstraction d'un client d'embeddings. Override en test."""

    def __init__(self, model: str = "text-embedding-3-small", api_key: str | None = None):
        self.model = model
        self._client = None
        self._api_key = api_key or os.environ.get("OPENAI_API_KEY")

    def _ensure_client(self):
        if self._client is None:
            if not self._api_key:
                raise RuntimeError("OPENAI_API_KEY manquante (sinon utiliser --dry-run)")
            from openai import OpenAI  # type: ignore
            self._client = OpenAI(api_key=self._api_key)
        return self._client

    def embed(self, texts: list[str]) -> list[list[float]]:
        if not texts:
            return []
        client = self._ensure_client()
        resp = client.embeddings.create(model=self.model, input=texts)
        return [d.embedding for d in resp.data]


# ============================================================
# Store : abstraction ChromaDB
# ============================================================

class ChromaStore:
    """Wrapper minimal sur ChromaDB. Injection possible pour tests (client custom)."""

    def __init__(self, persist_path: str | None = DEFAULT_STORE, collection: str = DEFAULT_COLLECTION, client=None):
        if client is not None:
            self._client = client
        else:
            import chromadb  # type: ignore
            if persist_path is None:
                self._client = chromadb.EphemeralClient()
            else:
                os.makedirs(persist_path, exist_ok=True)
                self._client = chromadb.PersistentClient(path=persist_path)
        self.collection_name = collection
        self.collection = self._client.get_or_create_collection(name=collection)

    def existing_hashes(self) -> dict[str, str]:
        """{chunk_id: content_hash} pour les chunks déjà stockés."""
        try:
            data = self.collection.get(include=["metadatas"])
        except Exception:
            return {}
        result: dict[str, str] = {}
        for cid, meta in zip(data.get("ids", []), data.get("metadatas", []) or []):
            if meta and "content_hash" in meta:
                result[cid] = meta["content_hash"]
        return result

    def upsert(self, chunk: Chunk, embedding: list[float]) -> None:
        meta = dict(chunk.metadata)
        meta["content_hash"] = chunk.content_hash
        self.collection.upsert(
            ids=[chunk.chunk_id],
            embeddings=[embedding],
            documents=[chunk.text],
            metadatas=[meta],
        )

    def delete(self, chunk_ids: Iterable[str]) -> None:
        ids = list(chunk_ids)
        if ids:
            self.collection.delete(ids=ids)

    def count(self) -> int:
        try:
            return self.collection.count()
        except Exception:
            return 0


# ============================================================
# Orchestration : re-indexation incrémentale
# ============================================================

@dataclass
class IngestionReport:
    files_seen: int = 0
    chunks_total: int = 0
    chunks_new: int = 0
    chunks_updated: int = 0
    chunks_skipped: int = 0
    chunks_deleted: int = 0
    errors: list[str] = field(default_factory=list)

    def summary(self) -> str:
        return (
            f"files={self.files_seen}  chunks={self.chunks_total}  "
            f"new={self.chunks_new}  updated={self.chunks_updated}  "
            f"skipped={self.chunks_skipped}  deleted={self.chunks_deleted}  "
            f"errors={len(self.errors)}"
        )


def ingest(vault: str, store: ChromaStore, embedder: Embedder | None, dry_run: bool = False) -> IngestionReport:
    report = IngestionReport()
    files = sorted(glob.glob(os.path.join(vault, "**", "*.md"), recursive=True))
    report.files_seen = len(files)

    all_chunks: list[Chunk] = []
    for fp in files:
        try:
            all_chunks.extend(build_chunks(fp, vault))
        except Exception as e:
            report.errors.append(f"{fp}: {e}")
    report.chunks_total = len(all_chunks)

    existing = store.existing_hashes()
    to_embed: list[Chunk] = []
    ids_in_vault: set[str] = set()

    for chunk in all_chunks:
        ids_in_vault.add(chunk.chunk_id)
        prev_hash = existing.get(chunk.chunk_id)
        if prev_hash is None:
            to_embed.append(chunk)
            report.chunks_new += 1
        elif prev_hash != chunk.content_hash:
            to_embed.append(chunk)
            report.chunks_updated += 1
        else:
            report.chunks_skipped += 1

    obsolete = [cid for cid in existing if cid not in ids_in_vault]
    if obsolete and not dry_run:
        store.delete(obsolete)
    report.chunks_deleted = len(obsolete)

    if dry_run or not to_embed:
        return report

    if embedder is None:
        raise RuntimeError("Embedder requis hors dry-run")

    embeddings = embedder.embed([c.text for c in to_embed])
    if len(embeddings) != len(to_embed):
        raise RuntimeError(f"taille embeddings inattendue : {len(embeddings)} vs {len(to_embed)}")

    for chunk, vec in zip(to_embed, embeddings):
        store.upsert(chunk, vec)

    return report


# ============================================================
# CLI
# ============================================================

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Ingestion ChromaDB du vault RAG (D-011, D-019).")
    parser.add_argument("--vault", default=os.environ.get("RAG_CONTENT_PATH", DEFAULT_VAULT))
    parser.add_argument("--store", default=os.environ.get("RAG_VECTOR_STORE_PATH", DEFAULT_STORE))
    parser.add_argument("--collection", default=DEFAULT_COLLECTION)
    parser.add_argument("--model", default=os.environ.get("RAG_EMBEDDING_MODEL", "text-embedding-3-small"))
    parser.add_argument("--dry-run", action="store_true", help="aucune embedding/écriture, juste un diff")
    args = parser.parse_args(argv)

    vault = os.path.abspath(args.vault)
    if not os.path.isdir(vault):
        print(f"[erreur] vault introuvable : {vault}", file=sys.stderr)
        return 2

    if args.dry_run:
        # Store en mémoire pour le dry-run (jamais d'écriture disque ni d'embedding)
        try:
            import chromadb  # type: ignore  # noqa: F401
            store = ChromaStore(persist_path=None, collection=args.collection)
        except ImportError:
            print("[info] chromadb absent, dry-run sur le diff de chunks seul.")
            chunks = collect_chunks(vault)
            print(f"chunks détectés : {len(chunks)}")
            return 0
        embedder = None
    else:
        store = ChromaStore(persist_path=args.store, collection=args.collection)
        embedder = Embedder(model=args.model)

    report = ingest(vault, store, embedder, dry_run=args.dry_run)
    print(report.summary())
    if report.errors:
        for err in report.errors:
            print(f"  ! {err}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
