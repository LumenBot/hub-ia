"""Métriques de coût API — instrumentation centralisée (S2.2 Lot C).

Helper utilisé par `ingest.py`, `query.py` et `run_eval.py` pour logger
le coût estimé de chaque appel API dans `rag/code/.cost-log.jsonl`
(gitignored — D-013). Permet à Blaise de suivre le coût accumulé par
sprint sans dépendre des dashboards Anthropic / OpenAI.

Tarifs en constantes : à mettre à jour si les providers révisent
(rare, mais à monitorer en début d'année). Si modèle absent du
catalogue : coût estimé 0,00 $ + log d'un warning informatif.

Format JSONL : `{"timestamp", "script", "model", "tokens_in",
"tokens_out", "cost_usd"}`.

Réfs : RAPPORT-CC-S1ter §6 (recommandation), RAPPORT-CC-S2.1 §7 reco 3,
D-013 plafonds API, BRIEF-CC-S2.2 §4 Lot C.
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from datetime import datetime, timezone


HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_LOG_PATH = os.path.join(HERE, ".cost-log.jsonl")


# Tarifs par modèle en USD pour 1M tokens (mai 2026). Source : pages
# tarifaires Anthropic + OpenAI. À réviser périodiquement.
TARIFFS_USD_PER_M_TOKENS = {
    # OpenAI embeddings
    "text-embedding-3-small": {"input": 0.02, "output": 0.0},
    "text-embedding-3-large": {"input": 0.13, "output": 0.0},
    # Anthropic Claude (référence Sonnet 4.6 ; placeholder Haiku 4.5)
    "claude-sonnet-4-6": {"input": 3.0, "output": 15.0},
    "claude-haiku-4-5": {"input": 0.80, "output": 4.0},
    # Compatibilité IDs étendus éventuels
    "claude-sonnet-4-6-20260101": {"input": 3.0, "output": 15.0},
    "claude-haiku-4-5-20251001": {"input": 0.80, "output": 4.0},
}


@dataclass
class CostEntry:
    timestamp: str
    script: str
    model: str
    tokens_in: int
    tokens_out: int
    cost_usd: float

    def to_dict(self) -> dict:
        return {
            "timestamp": self.timestamp,
            "script": self.script,
            "model": self.model,
            "tokens_in": self.tokens_in,
            "tokens_out": self.tokens_out,
            "cost_usd": round(self.cost_usd, 6),
        }


def estimate_cost(model: str, tokens_in: int, tokens_out: int = 0) -> float:
    """Calcule le coût USD pour un appel API donné. Retourne 0.0 si modèle
    absent du catalogue (sera signalé en log)."""
    tariff = TARIFFS_USD_PER_M_TOKENS.get(model)
    if tariff is None:
        return 0.0
    return (
        tokens_in * tariff["input"] / 1_000_000
        + tokens_out * tariff["output"] / 1_000_000
    )


def log_cost(
    script: str,
    model: str,
    tokens_in: int,
    tokens_out: int = 0,
    log_path: str | None = None,
) -> CostEntry:
    """Append une entrée JSONL au log de coût. Retourne l'entrée loggée.

    Tolérant : si l'écriture échoue (filesystem en lecture seule par ex.),
    on retourne quand même l'entrée et on n'interrompt pas le pipeline.
    """
    entry = CostEntry(
        timestamp=datetime.now(timezone.utc).isoformat(timespec="seconds"),
        script=script,
        model=model,
        tokens_in=tokens_in,
        tokens_out=tokens_out,
        cost_usd=estimate_cost(model, tokens_in, tokens_out),
    )
    target = log_path or DEFAULT_LOG_PATH
    try:
        with open(target, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry.to_dict(), ensure_ascii=False) + "\n")
    except OSError:
        pass
    return entry


def read_cost_log(log_path: str | None = None) -> list[dict]:
    """Lit le log JSONL et retourne la liste des entrées. Retourne []
    si le fichier n'existe pas."""
    target = log_path or DEFAULT_LOG_PATH
    if not os.path.exists(target):
        return []
    entries: list[dict] = []
    with open(target, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                entries.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return entries


def summarize_cost(entries: list[dict] | None = None, log_path: str | None = None) -> dict:
    """Cumul des coûts par modèle + total global. Lecture du fichier si
    `entries` n'est pas fourni."""
    if entries is None:
        entries = read_cost_log(log_path)
    by_model: dict[str, dict] = {}
    total = 0.0
    total_in = 0
    total_out = 0
    for e in entries:
        m = e.get("model", "unknown")
        slot = by_model.setdefault(m, {"calls": 0, "tokens_in": 0, "tokens_out": 0, "cost_usd": 0.0})
        slot["calls"] += 1
        slot["tokens_in"] += int(e.get("tokens_in", 0))
        slot["tokens_out"] += int(e.get("tokens_out", 0))
        slot["cost_usd"] += float(e.get("cost_usd", 0.0))
        total += float(e.get("cost_usd", 0.0))
        total_in += int(e.get("tokens_in", 0))
        total_out += int(e.get("tokens_out", 0))
    for slot in by_model.values():
        slot["cost_usd"] = round(slot["cost_usd"], 6)
    return {
        "by_model": by_model,
        "total_cost_usd": round(total, 6),
        "total_tokens_in": total_in,
        "total_tokens_out": total_out,
        "total_calls": len(entries),
    }


def format_cost_summary(summary: dict) -> str:
    """Format human-readable du cumul pour affichage en fin d'exécution."""
    lines = [
        "─" * 60,
        "Coût API accumulé (rag/code/.cost-log.jsonl) :",
    ]
    for model, slot in sorted(summary["by_model"].items()):
        lines.append(
            f"  {model:35s} {slot['calls']:3d} call(s)  "
            f"in={slot['tokens_in']:>8d}  out={slot['tokens_out']:>6d}  "
            f"= {slot['cost_usd']:.4f} $"
        )
    lines.append(
        f"  → Total : {summary['total_cost_usd']:.4f} $ "
        f"({summary['total_calls']} appels, "
        f"{summary['total_tokens_in']} tokens in / {summary['total_tokens_out']} tokens out)"
    )
    lines.append("─" * 60)
    return "\n".join(lines)
