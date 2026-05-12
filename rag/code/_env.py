"""Chargement automatique de `rag/code/.env` au démarrage des scripts.

Importé en tête de `ingest.py`, `query.py` et `run_eval.py` (avant les imports
openai / anthropic). Charge silencieusement les paires `KEY=value` du fichier
`.env` situé à la racine de `rag/code/` (gitignored — D-013). Si le fichier
est absent ou si la dépendance `python-dotenv` n'est pas installée, fallback
sur les variables d'environnement déjà exportées (compatibilité CI, tests).

Réf : S1ter Lot S1c.1, BRIEF-CC-S1ter-validation-end-to-end-avec-cles §4.
"""

from __future__ import annotations

import os

ENV_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    ".env",
)


def load_env(path: str | None = None) -> bool:
    """Charge le `.env` situé dans `rag/code/.env` (ou `path` si fourni).

    Retourne True si un fichier a été chargé, False sinon (fichier absent ou
    `python-dotenv` indisponible). Ne lève jamais d'exception : les scripts
    qui n'ont pas besoin des clés API doivent continuer à fonctionner.
    """
    target = path or ENV_PATH
    if not os.path.exists(target):
        return False
    try:
        from dotenv import load_dotenv  # type: ignore
    except ImportError:
        return False
    load_dotenv(target, override=False)
    return True


# Chargement immédiat à l'import — comportement par défaut attendu par les
# scripts d'ingestion / query / eval. Les tests peuvent invoquer load_env()
# explicitement avec un path différent.
load_env()
