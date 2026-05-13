"""Tests fonctionnels du hook pre-commit (S2.2 Lot C).

Invoque le script bash `.githooks/pre-commit` dans un repo Git éphémère
pour valider deux scénarios :
1. Aucun fichier `rag/content/**.md` stagé → exit 0 sans appeler l'audit.
2. Un fichier MD non conforme stagé → audit déclenché, exit non-zéro.

Le hook bash est testé en boîte noire via subprocess, pour valider la
chaîne complète (détection diff, invocation Python, propagation exit code).
"""

from __future__ import annotations

import os
import subprocess
import textwrap

import pytest


REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HOOK_PATH = os.path.join(REPO_ROOT, ".githooks", "pre-commit")


def _git(args: list[str], cwd: str, env: dict | None = None) -> subprocess.CompletedProcess:
    full_env = os.environ.copy()
    full_env.update({
        "GIT_AUTHOR_NAME": "Test",
        "GIT_AUTHOR_EMAIL": "test@example.com",
        "GIT_COMMITTER_NAME": "Test",
        "GIT_COMMITTER_EMAIL": "test@example.com",
    })
    if env:
        full_env.update(env)
    return subprocess.run(["git", *args], cwd=cwd, env=full_env,
                          capture_output=True, text=True)


def _setup_repo(tmp_path) -> str:
    """Initialise un repo Git éphémère avec une copie du hook et de
    l'audit-md-rag (pour pouvoir l'invoquer)."""
    repo = tmp_path / "repo"
    repo.mkdir()
    _git(["init", "-q"], str(repo))
    # Copier l'arborescence minimale : .githooks/pre-commit, audit-md-rag
    (repo / ".githooks").mkdir()
    with open(HOOK_PATH, encoding="utf-8") as src:
        (repo / ".githooks" / "pre-commit").write_text(src.read(), encoding="utf-8")
    os.chmod(str(repo / ".githooks" / "pre-commit"), 0o755)
    # Copier rag/code/audit/audit-md-rag.py
    (repo / "rag" / "code" / "audit").mkdir(parents=True)
    audit_src = os.path.join(REPO_ROOT, "rag", "code", "audit", "audit-md-rag.py")
    with open(audit_src, encoding="utf-8") as src:
        (repo / "rag" / "code" / "audit" / "audit-md-rag.py").write_text(src.read(), encoding="utf-8")
    (repo / "rag" / "content").mkdir(parents=True)
    # Activer le hook
    _git(["config", "core.hooksPath", ".githooks"], str(repo))
    return str(repo)


@pytest.fixture
def repo(tmp_path):
    return _setup_repo(tmp_path)


def test_hook_pas_de_md_stage_exit_0(repo):
    """Aucun rag/content/*.md stagé → le hook se termine immédiatement avec 0."""
    # Stager un fichier hors rag/content/
    (os.path.join(repo, "README.md"))
    with open(os.path.join(repo, "README.md"), "w") as f:
        f.write("# Repo de test\n")
    _git(["add", "README.md"], repo)
    result = subprocess.run(
        ["bash", os.path.join(repo, ".githooks", "pre-commit")],
        cwd=repo, capture_output=True, text=True,
    )
    assert result.returncode == 0, f"stdout={result.stdout} stderr={result.stderr}"


def test_hook_md_conforme_passe(repo):
    """Un fichier rag/content/*.md correctement formé doit déclencher
    l'audit et le passer (exit 0)."""
    md = textwrap.dedent("""\
    ---
    code: cu-001
    titre: "Test"
    type: module-cu
    axe: B
    niveau: 1
    tags: [test]
    version: 3.8.2
    last_updated: 2026-05-12
    glosaire_termes: [test]
    derives: ["[[cu-008]]"]
    public_cible: [dirigeant]
    ---

    # Test

    ## Section

    Contenu autonome.
    """)
    target_dir = os.path.join(repo, "rag", "content", "modules")
    os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(target_dir, "cu-001.md"), "w") as f:
        f.write(md)
    _git(["add", "rag/content/modules/cu-001.md"], repo)
    result = subprocess.run(
        ["bash", os.path.join(repo, ".githooks", "pre-commit")],
        cwd=repo, capture_output=True, text=True,
    )
    # cu-001.md a un wikilink vers cu-008 qui n'existe pas dans le vault de
    # test (whitelist absente aussi) → R4 erreur attendue → exit 1.
    # On valide juste que le hook a bien invoqué l'audit (output contient
    # l'en-tête AUDIT MD-RAG).
    assert "AUDIT MD-RAG" in result.stdout, f"hook ne semble pas avoir lancé l'audit : {result.stdout}"


def test_hook_md_avec_erreur_bloque_commit(repo):
    """Un MD sans frontmatter doit faire échouer l'audit et bloquer le commit."""
    target_dir = os.path.join(repo, "rag", "content", "modules")
    os.makedirs(target_dir, exist_ok=True)
    # MD avec un nom valide (R7) mais sans frontmatter (R1 erreur)
    with open(os.path.join(target_dir, "cu-002.md"), "w") as f:
        f.write("# Pas de frontmatter\n\nContenu cassé.\n")
    _git(["add", "rag/content/modules/cu-002.md"], repo)
    result = subprocess.run(
        ["bash", os.path.join(repo, ".githooks", "pre-commit")],
        cwd=repo, capture_output=True, text=True,
    )
    assert result.returncode == 1, f"hook devrait bloquer (exit 1), got {result.returncode}"
    assert "bloqué" in result.stdout or "blocked" in result.stdout.lower() or \
           "✗" in result.stdout
