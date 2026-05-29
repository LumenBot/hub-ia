"""Tests pour ingest.py (chunking + re-indexation incrémentale).

Exécution :
    pytest rag/code/ingestion/test_ingest.py -v

Pas d'appel API réel : on stubbe `Embedder` et on utilise un store en mémoire
(via un FakeStore qui imite l'interface ChromaStore minimale).
"""

from __future__ import annotations

import importlib.util
import os
import sys
import textwrap

import pytest


HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT_PATH = os.path.join(HERE, "ingest.py")


def _load_ingest():
    spec = importlib.util.spec_from_file_location("ingest", SCRIPT_PATH)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


ingest_mod = _load_ingest()


# ============================================================
# Fixtures
# ============================================================

MD_SHORT = textwrap.dedent("""\
---
code: cu-001
titre: "Recherche & veille"
type: module-cu
axe: B
niveau: 1
tags: [veille]
version: 3.8.2
last_updated: 2026-05-11
glosaire_termes: [veille]
derives: ["[[cu-008]]"]
public_cible: [dirigeant]
---

# Recherche & veille

## Vue d'ensemble

Présentation courte. Mots simples.

## Méthodologie

Trois étapes claires. Texte autonome.
""")

MD_WITH_LONG_H2 = textwrap.dedent("""\
---
code: cu-008
titre: "Knowledge base RAG"
type: module-cu
axe: B
niveau: 3
tags: [rag]
version: 3.8.2
last_updated: 2026-05-11
glosaire_termes: [rag]
derives: ["[[dep-02]]"]
public_cible: [tech]
---

# Knowledge base RAG

## Concepts clés

Intro de la section.

### Définition RAG

""") + ("mot " * 700) + textwrap.dedent("""

### Architecture

Architecture courte.
""")


@pytest.fixture
def vault_two_files(tmp_path):
    (tmp_path / "cu-001.md").write_text(MD_SHORT, encoding="utf-8")
    (tmp_path / "cu-008.md").write_text(MD_WITH_LONG_H2, encoding="utf-8")
    return str(tmp_path)


# ============================================================
# Store factice (interface compatible avec ChromaStore)
# ============================================================

class FakeStore:
    def __init__(self):
        self.entries: dict[str, dict] = {}  # id -> {hash, meta, doc, embedding}

    def existing_hashes(self) -> dict[str, str]:
        return {cid: e["hash"] for cid, e in self.entries.items()}

    def upsert(self, chunk, embedding):
        self.entries[chunk.chunk_id] = {
            "hash": chunk.content_hash,
            "meta": dict(chunk.metadata),
            "doc": chunk.text,
            "embedding": embedding,
        }

    def delete(self, ids):
        for cid in ids:
            self.entries.pop(cid, None)

    def count(self):
        return len(self.entries)


class FakeEmbedder:
    def __init__(self):
        self.calls = 0

    def embed(self, texts):
        self.calls += 1
        return [[0.1] * 8 for _ in texts]


# ============================================================
# Tests : chunking
# ============================================================

class TestChunking:
    def test_short_file_one_chunk_per_h2(self, vault_two_files):
        fp = os.path.join(vault_two_files, "cu-001.md")
        chunks = ingest_mod.build_chunks(fp, vault_two_files)
        assert len(chunks) == 2
        ids = [c.chunk_id for c in chunks]
        assert "cu-001#vue-d-ensemble" in ids
        assert "cu-001#methodologie" in ids

    def test_long_h2_subdivides_by_h3(self, vault_two_files):
        fp = os.path.join(vault_two_files, "cu-008.md")
        chunks = ingest_mod.build_chunks(fp, vault_two_files)
        # H2 "Concepts clés" doit être éclatée par H3
        ids = [c.chunk_id for c in chunks]
        assert "cu-008#concepts-cles#definition-rag" in ids
        assert "cu-008#concepts-cles#architecture" in ids

    def test_metadata_includes_frontmatter(self, vault_two_files):
        fp = os.path.join(vault_two_files, "cu-001.md")
        chunks = ingest_mod.build_chunks(fp, vault_two_files)
        meta = chunks[0].metadata
        assert meta["code"] == "cu-001"
        assert meta["type"] == "module-cu"
        assert meta["axe"] == "B"
        assert meta["version"] == "3.8.2"
        assert meta["source_file"].endswith("cu-001.md")
        assert "[METADATA]" in chunks[0].text
        assert "[CONTENT]" in chunks[0].text

    def test_skip_file_sans_frontmatter(self, tmp_path):
        fp = tmp_path / "broken.md"
        fp.write_text("# Sans frontmatter\n\n## Section\n\nContenu.", encoding="utf-8")
        assert ingest_mod.build_chunks(str(fp), str(tmp_path)) == []

    def test_content_hash_change_si_contenu_modifie(self, vault_two_files):
        fp = os.path.join(vault_two_files, "cu-001.md")
        chunks_before = ingest_mod.build_chunks(fp, vault_two_files)
        with open(fp, "a", encoding="utf-8") as f:
            f.write("\nAjout final dans la dernière section.\n")
        chunks_after = ingest_mod.build_chunks(fp, vault_two_files)
        # La dernière section a changé
        assert chunks_before[-1].content_hash != chunks_after[-1].content_hash
        # Les précédentes restent stables (utile pour la re-indexation incrémentale)
        assert chunks_before[0].content_hash == chunks_after[0].content_hash


# ============================================================
# Tests : ingestion incrémentale
# ============================================================

class TestIngestionIncrementale:
    def test_premier_run_indexe_tous_les_chunks(self, vault_two_files):
        store = FakeStore()
        emb = FakeEmbedder()
        report = ingest_mod.ingest(vault_two_files, store, emb)
        assert report.chunks_new == report.chunks_total
        assert report.chunks_updated == 0
        assert report.chunks_skipped == 0
        assert store.count() == report.chunks_total
        assert emb.calls == 1

    def test_second_run_skip_tout_si_inchange(self, vault_two_files):
        store = FakeStore()
        emb = FakeEmbedder()
        ingest_mod.ingest(vault_two_files, store, emb)
        emb.calls = 0
        report2 = ingest_mod.ingest(vault_two_files, store, emb)
        assert report2.chunks_skipped == report2.chunks_total
        assert report2.chunks_new == 0
        assert report2.chunks_updated == 0
        assert emb.calls == 0

    def test_modification_md_declenche_update(self, vault_two_files):
        store = FakeStore()
        emb = FakeEmbedder()
        ingest_mod.ingest(vault_two_files, store, emb)

        fp = os.path.join(vault_two_files, "cu-001.md")
        text = open(fp, encoding="utf-8").read()
        text = text.replace("Trois étapes claires.", "Trois étapes claires et révisées.")
        open(fp, "w", encoding="utf-8").write(text)

        report2 = ingest_mod.ingest(vault_two_files, store, emb)
        assert report2.chunks_updated == 1
        assert report2.chunks_skipped == report2.chunks_total - 1

    def test_suppression_md_purge_chunks(self, vault_two_files):
        store = FakeStore()
        emb = FakeEmbedder()
        ingest_mod.ingest(vault_two_files, store, emb)
        count_initial = store.count()

        os.remove(os.path.join(vault_two_files, "cu-001.md"))
        report2 = ingest_mod.ingest(vault_two_files, store, emb)
        assert report2.chunks_deleted > 0
        assert store.count() < count_initial

    def test_dry_run_ne_modifie_rien(self, vault_two_files):
        store = FakeStore()
        emb = FakeEmbedder()
        report = ingest_mod.ingest(vault_two_files, store, emb, dry_run=True)
        assert store.count() == 0
        assert emb.calls == 0
        assert report.chunks_total > 0


# ============================================================
# Tests : helpers
# ============================================================

class TestHelpers:
    def test_split_frontmatter(self):
        fm, body = ingest_mod.split_frontmatter(MD_SHORT)
        assert fm["code"] == "cu-001"
        assert body.startswith("# Recherche")

    def test_slugify_accent(self):
        assert ingest_mod.slugify("Vue d'ensemble") == "vue-d-ensemble"

    def test_serialize_frontmatter_header(self):
        fm = {"code": "cu-001", "titre": "X", "tags": ["a", "b"]}
        h = ingest_mod.serialize_frontmatter_header(fm)
        assert "[METADATA]" in h and "[CONTENT]" in h
        assert "tags: a, b" in h


# ============================================================
# Tests : critères de succès brief (chunks attendus pour 5 MD)
# ============================================================

def test_volume_chunks_5_unites_pilotes_estim_acceptable(tmp_path):
    """Sanity check : 5 MD courts produisent un volume cohérent avec ~25-40 chunks attendus."""
    for code in ["cu-001", "cu-008", "pr-07", "dep-02", "outils-vector-db"]:
        md = MD_SHORT.replace("cu-001", code).replace("Recherche & veille", code)
        # On enrichit un peu pour simuler 5-8 H2 par fichier
        extra = "\n\n## " + "\n\nTexte.\n\n## ".join([f"Section {i}" for i in range(1, 6)])
        (tmp_path / f"{code}.md").write_text(md + extra + "\n\nTexte final.\n", encoding="utf-8")
    chunks = ingest_mod.collect_chunks(str(tmp_path))
    # 5 fichiers × ~7 H2 (2 d'origine + 5 ajoutées) = ~35 chunks
    assert 25 <= len(chunks) <= 50
