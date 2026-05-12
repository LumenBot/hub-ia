# Architecture technique du pipeline RAG — S1

Document interne au code RAG. Pour la gouvernance (décisions, conventions, briefs), voir `rag-prep/` à la racine du repo.

## Vue d'ensemble

```
[rag/content/*.md]
       │
       │  (1) audit-md-rag.py — conformité SPEC v1
       ▼
[ingest.py] ─── parse frontmatter ─── chunk par H2 (D-011)
       │       
       │  (2) OpenAI text-embedding-3-small
       ▼
[ChromaDB local — rag/code/vector_store/]
       │
       │  (3) query.py reçoit une question (CLI)
       ▼
[Embedding question] → top-k=5 retrieval → contexte
       │
       │  (4) Claude Sonnet 4.6 + system prompt structuré
       ▼
[Réponse + citations sources]
```

## Re-indexation incrémentale (D-019)

Chaque chunk porte trois métadonnées discriminantes :
- `source_file` : chemin relatif du MD source
- `chunk_id` : `{code}#{h2-slug}` ou `{code}#{h2-slug}#{h3-slug}` si subdivisé
- `content_hash` : SHA-256 du contenu du chunk (frontmatter injecté + corps)
- `source_version` : champ `version` du frontmatter source

À chaque run d'`ingest.py` :
1. On calcule le hash de chaque chunk produit
2. Si un chunk avec même `chunk_id` existe avec le même `content_hash` → skip
3. Si différent → upsert (remplace l'ancienne entrée)
4. Si un `chunk_id` dans le store n'apparaît plus dans le vault → delete (purge)

## Modèle de chunking (D-011)

- **Unité** : une section H2 = un chunk.
- **Cible** : 400-700 tokens (mesurés via tiktoken `cl100k_base`).
- **Subdivision** : si une section H2 > 800 tokens, on subdivise par H3 (chaque H3 devient un sous-chunk avec son propre `chunk_id`).
- **Injection** : le frontmatter YAML est injecté en tête de chaque chunk (préfixe `[METADATA]\n...\n[CONTENT]\n`) pour préserver le contexte métadonnées au retrieval.

## Métadonnées indexées

Chaque entrée ChromaDB porte :

| Champ | Source | Usage |
|---|---|---|
| `code` | frontmatter `code` | citation source |
| `titre` | frontmatter `titre` | citation source |
| `type` | frontmatter `type` | filtrage |
| `axe` | frontmatter `axe` | filtrage par profil |
| `niveau` | frontmatter `niveau` | filtrage |
| `tags` | frontmatter `tags` (joined) | filtrage |
| `version` | frontmatter `version` | versioning chunk |
| `public_cible` | frontmatter `public_cible` (joined) | filtrage par profil |
| `source_file` | chemin relatif | citation + purge |
| `chunk_id` | `{code}#{slug}` | upsert + dedup |
| `content_hash` | sha256 | détection modif |
| `h2_title` | titre H2 source | citation précise |

## Prompt système (S1)

Le prompt système de `query.py` est volontairement court (S1 = pilote). Apprentissages remontés vers `SPEC-MD-POUR-RAG.md` v2 et vers un `prompts/system.md` dédié en S2.

Cible :
- Ton pédagogique aligné Hub IA (RULES couple 1 v1.6, dimension B "expressivité").
- Citations sources obligatoires : `[CODE]` en fin de paragraphe pour chaque assertion.
- Refuser de répondre si aucun chunk pertinent (similarity score < seuil).
- Pas d'invention de chiffres ou sources.

## Coûts estimés (S1 pilote, ~5 MD)

| Opération | Coût estimé |
|---|---|
| Embedding initial 5 MD (~10k tokens) | < 0,01 $ |
| Re-indexation incrémentale (par chunk modifié) | négligeable |
| 10 questions × 1 embedding + 1 génération Sonnet | ~0,05 $ |
| **Total S1** | **< 0,10 $** |

Plafond Anthropic 50 $/mois (alerte 30 $), OpenAI 10 $/mois (alerte 5 $) — D-013.

## Hors scope S1 (rappel)

- Pas de backend Cloudflare Worker (S3).
- Pas de widget HTML (S3).
- Pas de capture feedback Supabase (S3).
- Pas de portage TypeScript (S3).
