# Git hooks RAG (S2.2 Lot C)

Hooks Git pour le pipeline RAG du couple 2. **Désactivés par défaut** — à activer une fois par clone local côté Blaise.

## Activation

```bash
git config core.hooksPath .githooks
```

Vérification : `git config core.hooksPath` doit retourner `.githooks`.

## Hooks disponibles

### `pre-commit`

Exécute `rag/code/audit/audit-md-rag.py --vault rag/content` quand un fichier `rag/content/**.md` est stagé. Bloque le commit si l'audit détecte des erreurs (warnings tolérés sauf options `--strict-future` / `--strict-r6` passées manuellement).

**Bypass ponctuel** (déconseillé, D-016) :

```bash
git commit --no-verify
```

## Réfs

- D-016 — Audit-md-rag.py automatisé dès S1
- RAPPORT-CC-S1 §6 reco 5
- RAPPORT-CC-S1bis §8 reco 3
- BRIEF-CC-S2.2 §4 Lot C
