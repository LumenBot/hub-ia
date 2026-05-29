"""Tests pour `_env.load_env()` (S1ter Lot S1c.1).

Vérifie :
- chargement d'un `.env` valide (valeurs propagées dans `os.environ`)
- absence silencieuse (return False) si fichier inexistant
- comportement non destructif (les vars d'env déjà définies ne sont pas
  écrasées — `override=False`)
- import de `_env` ne lève pas d'erreur même sans `.env` réel

Exécution : `pytest rag/code/test_env.py -v`.
"""

from __future__ import annotations

import importlib
import importlib.util
import os
import sys
import textwrap


HERE = os.path.dirname(os.path.abspath(__file__))
MODULE_PATH = os.path.join(HERE, "_env.py")


def _load_env_module():
    """Recharge le module `_env` à neuf (utile entre tests)."""
    sys.modules.pop("_env", None)
    spec = importlib.util.spec_from_file_location("_env", MODULE_PATH)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules["_env"] = mod
    spec.loader.exec_module(mod)
    return mod


def test_load_env_charge_fichier_valide(tmp_path, monkeypatch):
    env_file = tmp_path / ".env"
    env_file.write_text(textwrap.dedent("""\
        TEST_S1TER_FOO=bar
        TEST_S1TER_BAZ=qux
    """), encoding="utf-8")

    monkeypatch.delenv("TEST_S1TER_FOO", raising=False)
    monkeypatch.delenv("TEST_S1TER_BAZ", raising=False)

    mod = _load_env_module()
    loaded = mod.load_env(str(env_file))

    assert loaded is True
    assert os.environ["TEST_S1TER_FOO"] == "bar"
    assert os.environ["TEST_S1TER_BAZ"] == "qux"


def test_load_env_silent_si_fichier_absent(tmp_path):
    mod = _load_env_module()
    loaded = mod.load_env(str(tmp_path / "introuvable.env"))
    assert loaded is False


def test_load_env_override_false_protege_vars_existantes(tmp_path, monkeypatch):
    env_file = tmp_path / ".env"
    env_file.write_text("TEST_S1TER_PROTECTED=from_file\n", encoding="utf-8")

    monkeypatch.setenv("TEST_S1TER_PROTECTED", "from_env_real")
    mod = _load_env_module()
    mod.load_env(str(env_file))

    assert os.environ["TEST_S1TER_PROTECTED"] == "from_env_real"


def test_import_module_ne_leve_pas_erreur():
    """Le chargement au moment de l'import doit être tolérant à tout."""
    mod = _load_env_module()
    # ENV_PATH pointe sur rag/code/.env (peut exister ou non)
    assert mod.ENV_PATH.endswith(".env")
    assert "rag/code" in mod.ENV_PATH or "rag\\code" in mod.ENV_PATH


def test_scripts_principaux_importent_dotenv():
    """Sanity : ingest, query, run_eval importent bien _env en tête."""
    for rel in ("ingestion/ingest.py", "backend/query.py", "eval/run_eval.py"):
        path = os.path.join(HERE, rel)
        with open(path, encoding="utf-8") as f:
            content = f.read()
        assert "import _env" in content, f"_env non importé dans {rel}"
