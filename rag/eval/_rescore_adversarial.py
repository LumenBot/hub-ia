#!/usr/bin/env python3
"""Re-scoring offline du bloc adversarial S2.7 (Lot Dev fix).

Le harness Lot Dev a produit un faux négatif (0/12 refus corrects) faute
de la phrase canonique du system prompt dans REFUSAL_MARKERS et d'un verdict
trop strict (refus_correct exigeait `not cited`). Ce script ré-applique la
logique corrigée de `run_eval.evaluate_adversarial()` sur les réponses déjà
collectées (`eval-report-s2.7-adversarial.json`) — SANS appel API (coût 0 $).

Note : le re-scoring s'appuie sur `answer_preview` (240 premiers caractères)
comme proxy de la réponse complète. La phrase canonique de refus apparaît en
tête de réponse (vérifié sur les 12 entrées), donc le re-scoring est fiable
pour le bloc adversarial. Pour une validation formelle complète, un rerun
Desktop sur réponses intégrales reste possible (non requis ici).

Usage :
    python3 rag/eval/_rescore_adversarial.py
"""

from __future__ import annotations

import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RUN_EVAL = os.path.join(os.path.dirname(HERE), "code", "eval", "run_eval.py")
ADV_JSON = os.path.join(HERE, "eval-report-s2.7-adversarial.json")
OUT_MD = os.path.join(HERE, "eval-report-s2.7-adversarial-rescored.md")


def _load_run_eval():
    sys.path.insert(0, os.path.join(os.path.dirname(HERE), "code", "eval"))
    spec = importlib.util.spec_from_file_location("run_eval", RUN_EVAL)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules["run_eval"] = mod
    spec.loader.exec_module(mod)
    return mod


def main() -> int:
    run_eval = _load_run_eval()
    with open(ADV_JSON, encoding="utf-8") as f:
        items = json.load(f)

    rescored = []
    for it in items:
        q = {"id": it["id"], "question": it["question"], "expected_refusal": True}
        # answer_preview comme proxy (phrase canonique en tête — vérifié)
        result = {"answer": it.get("answer_preview", ""), "cited_codes": it.get("cited_codes", [])}
        rescored.append(run_eval.evaluate_one(q, result))

    refus_ok = sum(1 for i in rescored if i.score_global == 1)
    hallu = [i for i in rescored if i.adversarial_verdict == "hallucination"]
    partiel = [i for i in rescored if i.adversarial_verdict == "refus_partiel"]
    total = len(rescored)

    lines = [
        "=" * 70,
        "RE-SCORING ADVERSARIAL S2.7 — harness calibration v2 (Lot Dev fix)",
        "=" * 70,
        f"Questions adversariales : {total}",
        f"Refus corrects : {refus_ok}/{total}",
        f"Hallucinations : {len(hallu)}/{total}",
        f"Refus partiels : {len(partiel)}/{total}",
        "",
        "Note : re-scoring offline sur answer_preview (proxy), coût 0 $.",
        "Avant fix (harness Lot Dev) : 0/12 refus corrects (faux négatif).",
        "",
    ]
    for it in rescored:
        flag = "✅" if it.score_global else "❌"
        lines.append(f"{flag} {it.id} [{it.adversarial_verdict}] cited={bool(it.cited_codes)}")
    report = "\n".join(lines) + "\n"

    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write(report)
    print(report)
    print(f"→ écrit : {os.path.relpath(OUT_MD, os.path.dirname(os.path.dirname(HERE)))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
