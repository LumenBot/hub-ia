#!/usr/bin/env python3
"""
Audit conformité MD du vault RAG — v2
=====================================

Script qui parcourt tous les fichiers .md de `rag/content/` et applique les
règles canoniques définies dans `SPEC-MD-POUR-RAG.md` v1.3.

À lancer avant tout commit qui modifie le vault :
    python3 rag/code/audit/audit-md-rag.py

Options :
    --vault PATH      chemin du vault (défaut : rag/content)
    --report PATH     chemin de sortie du rapport (défaut : stdout)
    --strict          exit 1 dès la première erreur (CI)
    --strict-future   transforme les warnings R4 (wikilinks whitelisted)
                      en erreurs réelles (utile pour bloquer l'élargissement
                      silencieux de la whitelist)
    --whitelist PATH  chemin du whitelist-wikilinks-futurs.md (défaut :
                      rag-prep/whitelist-wikilinks-futurs.md)

Sortie :
    rapport texte structuré, distinguant erreurs et warnings
    code retour 0 si 0 erreur (warnings tolérés), 1 sinon

Couvre 10 règles canoniques SPEC v1.3 (D-016 + D-023 + D-028 + D-029) :
    R1-frontmatter-complet : 10 champs canoniques (exception D-028 pour les
                             fichiers racines transverses : glossaire,
                             chiffres-macro)
    R2-h1-unique           : un seul H1, identique au champ `titre`
    R3-chunking-respecte   : aucune section H2 > 800 tokens sans subdivision H3
    R4-wikilinks-valides   : cibles wikilink présentes dans le vault
                             (D-029 : warnings tolérés pour codes dans
                             whitelist-wikilinks-futurs.md)
    R5-glossaire-wikilink  : termes du glossaire utilisés via [[glossaire#…]]
                             (warning première itération)
    R6-chiffres-sources    : chiffre statistique suivi d'une source proche
                             (markdown, URL, ou wikilink vers brique transverse)
    R7-nommage-fichier     : conformité au schéma kebab-case + famille connue
    R8-versioning-git      : last_updated du frontmatter cohérent avec
                             la dernière modif git (< 7 jours d'écart)
    R9-chiffres-macro      : chiffres canoniques du Hub (chiffres-macro-2026.md)
                             cités via wikilink, pas en clair (warning)
    R10-tableaux-fideles   : valeurs numériques des tableaux MD cohérentes
                             avec le HTML source correspondant (warning,
                             implémentation pragmatique première itération)

Style aligné sur `site-web-prep/audit-global.py` (couple 1).

Réfs : D-016, D-023, D-028, D-029, SPEC-MD-POUR-RAG.md v1.3 §Validation.
"""

from __future__ import annotations

import argparse
import glob
import os
import re
import subprocess
import sys
import unicodedata
from dataclasses import dataclass, field
from datetime import date, datetime, timezone
from typing import Iterable

try:
    import yaml
except ImportError:
    print("[erreur] pyyaml requis : pip install pyyaml", file=sys.stderr)
    sys.exit(2)


ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REPO_ROOT = os.path.dirname(ROOT)
DEFAULT_VAULT = os.path.join(ROOT, "content")
DEFAULT_WHITELIST = os.path.join(REPO_ROOT, "rag-prep", "whitelist-wikilinks-futurs.md")
DEFAULT_CHIFFRES = os.path.join(ROOT, "content", "transverses", "chiffres-macro-2026.md")
DEFAULT_HTML_ROOT = REPO_ROOT  # racine où vivent modules/*.html, prealables/*.html, etc.

FRONTMATTER_FIELDS = [
    "code",
    "titre",
    "type",
    "axe",
    "niveau",
    "tags",
    "version",
    "last_updated",
    "glosaire_termes",
    "derives",
    "public_cible",
]

TYPE_ALLOWED = {"module-cu", "prealable-pr", "deploiement-dep", "architecture", "fiche-outil", "transverse"}
AXE_ALLOWED = {"A", "B", "C", "D", "E", "agentique", "transverse"}
NIVEAU_ALLOWED = {1, 2, 3, 4}
PUBLIC_ALLOWED = {"dirigeant", "ops", "r&d", "tech", "transverse"}

# D-028 : fichiers racines transverses pour lesquels glosaire_termes et derives
# peuvent être vides par construction (le fichier ne dépend d'aucun autre).
# Critère pragmatique : codes commençant par un préfixe canonique de référentiel
# racine ET frontmatter.type == "transverse".
R1_EXCEPTION_CODES = {"glossaire"}
R1_EXCEPTION_CODE_PREFIXES = ("chiffres-macro-",)
R1_EXCEPTION_OPTIONAL_FIELDS = {"glosaire_termes", "derives"}

CHUNK_TOKEN_LIMIT = 800
TOKENS_PER_WORD = 1.3

NUMBER_PATTERNS = [
    re.compile(r"\b\d+\s?%"),
    re.compile(r"\b\d+(?:[.,]\d+)?\s?[x×]\b", re.IGNORECASE),
    re.compile(r"\b\d+(?:[.,]\d+)?\s?[kK]€"),
    re.compile(r"\b\d+(?:[.,]\d+)?\s?M€"),
]
# Source proche : mention textuelle « Source : », URL, lien markdown ou
# wikilink vers une brique transverse (chiffres-macro-*, transverses/*).
# (R6 étendu — Bloc C — proposition 13 SPEC §Validation)
SOURCE_MARKERS = re.compile(
    r"(Source\s*:"
    r"|\[[^\]]+\]\([^)]+\)"
    r"|URL"
    r"|\[\[chiffres-macro-\d{4}[^\]]*\]\]"
    r"|\[\[transverses?/[^\]]+\]\])",
    re.IGNORECASE,
)
WIKILINK_PATTERN = re.compile(r"\[\[([^\]\|#]+)(?:#[^\]\|]+)?(?:\|[^\]]+)?\]\]")

R7_NAME_SCHEMAS = [
    re.compile(r"^(cu|pr|dep)-\d{2,3}\.md$"),      # cu-001, cu-008, pr-07, dep-02
    re.compile(r"^a\d+\.md$"),                     # a1.md, a4.md (architectures)
    re.compile(r"^outils-[a-z0-9][a-z0-9-]*\.md$"),
    re.compile(r"^glossaire\.md$"),
    re.compile(
        r"^("
        r"transverse|vigilance|pattern|methodologie|chiffres-macro|"
        r"cadrage|calendrier|gouvernance|strategie"
        r")-[a-z0-9][a-z0-9-]*\.md$"
    ),
]

R8_LAST_UPDATED_TOLERANCE_DAYS = 7


# ============================================================
# Structures
# ============================================================

@dataclass
class RuleResult:
    """Résultat de l'évaluation d'une règle pour un fichier.

    Distingue les erreurs (blocantes — exit code non-zéro) des warnings
    (signalement informatif — pas de blocage par défaut, sauf --strict-future
    pour R4).
    """

    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def add_error(self, msg: str) -> None:
        self.errors.append(msg)

    def add_warning(self, msg: str) -> None:
        self.warnings.append(msg)

    def merge(self, other: "RuleResult") -> None:
        self.errors.extend(other.errors)
        self.warnings.extend(other.warnings)


@dataclass
class AuditContext:
    """Contexte global de l'audit : vault codes connus, whitelist, chiffres canoniques."""

    vault_codes: set[str] = field(default_factory=set)
    whitelist_codes: set[str] = field(default_factory=set)
    glossaire_terms: list[str] = field(default_factory=list)
    canonical_chiffres: list[dict] = field(default_factory=list)
    repo_root: str = REPO_ROOT
    strict_future: bool = False


# ============================================================
# Helpers
# ============================================================

def list_md_files(vault: str) -> list[str]:
    return sorted(glob.glob(os.path.join(vault, "**", "*.md"), recursive=True))


def rel(fp: str, vault: str) -> str:
    return os.path.relpath(fp, vault)


def read(fp: str) -> str:
    with open(fp, encoding="utf-8") as f:
        return f.read()


def split_frontmatter(text: str) -> tuple[dict | None, str]:
    """Retourne (frontmatter_dict, body). frontmatter_dict=None si absent."""
    if not text.startswith("---\n") and not text.startswith("---\r\n"):
        return None, text
    end = text.find("\n---", 4)
    if end == -1:
        return None, text
    fm_raw = text[4:end]
    body = text[end + 4:].lstrip("\n")
    try:
        data = yaml.safe_load(fm_raw) or {}
        if not isinstance(data, dict):
            return None, body
        return data, body
    except yaml.YAMLError:
        return None, body


def estimate_tokens(text: str) -> int:
    """Estimation grossière du nombre de tokens (~1.3 token/mot)."""
    words = len(text.split())
    return int(words * TOKENS_PER_WORD)


def slugify(text: str) -> str:
    s = unicodedata.normalize("NFKD", text)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower().strip()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-") or "section"


def split_sections(body: str) -> list[tuple[str, str, str]]:
    """Découpe le corps en sections (level, title, body).

    level ∈ {"h1", "h2", "h3"}. body inclut le titre.
    """
    lines = body.splitlines(keepends=True)
    sections: list[tuple[str, str, str]] = []
    current_level = None
    current_title = None
    current_buf: list[str] = []

    for line in lines:
        m = re.match(r"^(#{1,3})\s+(.+?)\s*$", line.rstrip("\n"))
        if m:
            if current_level is not None:
                sections.append((current_level, current_title or "", "".join(current_buf)))
            depth = len(m.group(1))
            current_level = f"h{depth}"
            current_title = m.group(2).strip()
            current_buf = [line]
        else:
            current_buf.append(line)

    if current_level is not None:
        sections.append((current_level, current_title or "", "".join(current_buf)))

    return sections


def vault_codes(files: Iterable[str]) -> set[str]:
    """Indexe les codes de fichiers du vault (basename sans .md + champ `code` du frontmatter)."""
    codes: set[str] = set()
    for fp in files:
        base = os.path.splitext(os.path.basename(fp))[0]
        codes.add(base.lower())
        try:
            text = read(fp)
            fm, _ = split_frontmatter(text)
            if fm and isinstance(fm.get("code"), str):
                codes.add(fm["code"].strip().lower())
        except Exception:
            pass
    codes.add("glossaire")
    return codes


# ============================================================
# Loaders : whitelist + glossaire + chiffres canoniques
# ============================================================

WHITELIST_CODE_PATTERN = re.compile(r"\|\s*`([a-z0-9][a-z0-9-]*)`")


def load_whitelist(path: str) -> set[str]:
    """Parse `rag-prep/whitelist-wikilinks-futurs.md` et retourne les codes.

    Convention : les codes sont en première colonne des tableaux markdown,
    entre backticks (ex. `| ` + "`" + `cu-002` + "`" + ` | ...`). Le parsing
    capture ces backtickés sur les lignes de tableau (commençant par `|`).
    """
    codes: set[str] = set()
    if not os.path.exists(path):
        return codes
    with open(path, encoding="utf-8") as f:
        for line in f:
            if not line.lstrip().startswith("|"):
                continue
            m = WHITELIST_CODE_PATTERN.search(line)
            if m:
                codes.add(m.group(1).lower())
    return codes


def load_glossaire_terms(vault: str) -> list[str]:
    """Charge les termes du glossaire (titres H2 de `glossaire.md`)."""
    glossaire_fp = os.path.join(vault, "glossaire.md")
    if not os.path.exists(glossaire_fp):
        return []
    text = read(glossaire_fp)
    _, body = split_frontmatter(text)
    terms: list[str] = []
    for level, title, _ in split_sections(body):
        if level == "h2":
            terms.append(title.strip().lower())
    return terms


CHIFFRE_TITLE_PATTERN = re.compile(
    r"^("
    r"\+?\d+(?:[.,]\d+)?\s*-\s*\d+(?:[.,]\d+)?\s?%"        # 80-95 %
    r"|\+?\d+(?:[.,]\d+)?\s?%\s*vs\s*\d+(?:[.,]\d+)?\s?%"  # 67 % vs 33 %
    r"|\+?\d+(?:[.,]\d+)?\s?%"                             # 95 %, +270 %
    r"|\+?\d+(?:[.,]\d+)?\s?h/jour"                        # 1,8 h/jour
    r"|\d+(?:[.,]\d+)?\s?h\b"                              # 1,8 h
    r"|×\s?\d+(?:[.,]\d+)?"                                # ×5
    r"|\d+(?:[.,]\d+)?\s?×"                                # 3,7×
    r"|\d+\s+\d{3,}"                                       # 77 000
    r")",
    re.IGNORECASE,
)


def load_canonical_chiffres(path: str) -> list[dict]:
    """Parse `chiffres-macro-2026.md` et retourne la liste des chiffres canoniques.

    Chaque entrée : {"value": "67 %", "title": "67 % — dirigeants PME/TPE…",
                     "slug": "67-pourcent-dirigeants-pme-tpe-…"}.
    Le `value` est extrait du début du titre H2 par regex tolérante aux
    fourchettes, vs, +, ×, espaces séparateurs, etc.
    """
    if not os.path.exists(path):
        return []
    text = read(path)
    _, body = split_frontmatter(text)
    out: list[dict] = []
    for level, title, _ in split_sections(body):
        if level != "h2":
            continue
        m = CHIFFRE_TITLE_PATTERN.match(title.strip())
        if m:
            out.append({
                "value": m.group(1).strip(),
                "title": title.strip(),
                "slug": slugify(title),
            })
    return out


# ============================================================
# Règle R1 — Frontmatter complet (D-028 exception fichiers racines transverses)
# ============================================================

def _is_r1_exception(fm: dict, field_name: str) -> bool:
    """D-028 : autoriser glosaire_termes et derives vides pour les fichiers
    racines transverses (glossaire.md, chiffres-macro-*.md)."""
    if field_name not in R1_EXCEPTION_OPTIONAL_FIELDS:
        return False
    code = str(fm.get("code", "")).strip().lower()
    type_ = str(fm.get("type", "")).strip().lower()
    if type_ != "transverse":
        return False
    if code in R1_EXCEPTION_CODES:
        return True
    return any(code.startswith(prefix) for prefix in R1_EXCEPTION_CODE_PREFIXES)


def check_r1_frontmatter(fp: str, fm: dict | None) -> RuleResult:
    res = RuleResult()
    if fm is None:
        res.add_error("R1: frontmatter YAML absent ou invalide")
        return res

    for fname in FRONTMATTER_FIELDS:
        if fname not in fm:
            if _is_r1_exception(fm, fname):
                continue  # D-028 : champ optionnel pour racine transverse
            res.add_error(f"R1: champ frontmatter manquant `{fname}`")
            continue
        value = fm[fname]
        if value is None or value == "" or value == [] or value == {}:
            if _is_r1_exception(fm, fname):
                continue  # D-028
            res.add_error(f"R1: champ frontmatter vide `{fname}`")

    if "type" in fm and fm["type"] not in TYPE_ALLOWED:
        res.add_error(f"R1: type `{fm['type']}` hors valeurs autorisées {sorted(TYPE_ALLOWED)}")
    if "axe" in fm and fm["axe"] not in AXE_ALLOWED:
        res.add_error(f"R1: axe `{fm['axe']}` hors valeurs autorisées {sorted(AXE_ALLOWED)}")
    if "niveau" in fm and fm["niveau"] not in NIVEAU_ALLOWED:
        res.add_error(f"R1: niveau `{fm['niveau']}` hors {sorted(NIVEAU_ALLOWED)}")
    if "public_cible" in fm and isinstance(fm["public_cible"], list):
        bad = [p for p in fm["public_cible"] if p not in PUBLIC_ALLOWED]
        if bad:
            res.add_error(f"R1: public_cible invalide {bad} (autorisés : {sorted(PUBLIC_ALLOWED)})")

    return res


# ============================================================
# Règle R2 — H1 unique, identique au titre
# ============================================================

def check_r2_h1(fp: str, fm: dict | None, body: str) -> RuleResult:
    res = RuleResult()
    h1s = re.findall(r"^#\s+(.+?)\s*$", body, flags=re.MULTILINE)
    if len(h1s) == 0:
        res.add_error("R2: aucun H1 détecté")
        return res
    if len(h1s) > 1:
        res.add_error(f"R2: {len(h1s)} H1 détectés (un seul autorisé)")

    if fm and "titre" in fm and isinstance(fm["titre"], str):
        titre = fm["titre"].strip().strip('"').strip("'")
        if h1s[0].strip() != titre:
            res.add_error(f"R2: H1 `{h1s[0].strip()}` != frontmatter.titre `{titre}`")

    return res


# ============================================================
# Règle R3 — Chunking : H2 > 800 tokens doit être subdivisé en H3
# ============================================================

def check_r3_chunking(fp: str, body: str) -> RuleResult:
    res = RuleResult()
    sections = split_sections(body)

    i = 0
    while i < len(sections):
        level, title, content = sections[i]
        if level != "h2":
            i += 1
            continue

        children: list[tuple[str, str, str]] = []
        j = i + 1
        while j < len(sections) and sections[j][0] == "h3":
            children.append(sections[j])
            j += 1

        if children:
            for ch_level, ch_title, ch_content in children:
                tokens = estimate_tokens(ch_content)
                if tokens > CHUNK_TOKEN_LIMIT:
                    res.add_error(
                        f"R3: section H3 `{title} > {ch_title}` ≈ {tokens} tokens (> {CHUNK_TOKEN_LIMIT})"
                    )
        else:
            tokens = estimate_tokens(content)
            if tokens > CHUNK_TOKEN_LIMIT:
                res.add_error(
                    f"R3: section H2 `{title}` ≈ {tokens} tokens (> {CHUNK_TOKEN_LIMIT}, à subdiviser en H3)"
                )

        i = j if children else i + 1

    return res


# ============================================================
# Règle R4 — Wikilinks vers cibles existantes (D-029 whitelist tolérée)
# ============================================================

def check_r4_wikilinks(fp: str, body: str, ctx: AuditContext) -> RuleResult:
    res = RuleResult()
    for match in WIKILINK_PATTERN.finditer(body):
        target = match.group(1).strip().lower()
        if not target:
            res.add_error("R4: wikilink vide `[[]]`")
            continue
        if target in ctx.vault_codes:
            continue
        if target in ctx.whitelist_codes:
            # D-029 : MD planifié mais non encore produit — warning, pas erreur.
            msg = f"R4: wikilink `[[{target}]]` → cible non encore produite (whitelist)"
            if ctx.strict_future:
                res.add_error(msg + " [strict-future]")
            else:
                res.add_warning(msg)
            continue
        res.add_error(f"R4: wikilink `[[{target}]]` → cible inexistante dans le vault ni la whitelist")
    return res


# ============================================================
# Règle R5 — Termes du glossaire utilisés via wikilink (warning v2)
# ============================================================

# Termes courts ou polysémiques qu'on exclut de R5 (trop bruyants, ou
# usage générique acceptable en prose).
R5_TERMS_EXCLUDED = {"api"}


def _strip_wikilinks(text: str) -> str:
    """Retire toutes les portées de wikilinks `[[...]]` pour ne chercher
    R5 que dans le texte hors-wikilink."""
    return WIKILINK_PATTERN.sub(" ", text)


def check_r5_glossaire(fp: str, fm: dict | None, body: str, ctx: AuditContext) -> RuleResult:
    """Warning si un terme du glossaire apparaît en clair (hors wikilink)
    dans un module. Déduplication par terme par fichier pour éviter le bruit.

    Première itération en warning seulement (cf. brief §4 Bloc B).
    Le glossaire lui-même est exempté (il définit les termes).
    """
    res = RuleResult()
    if not ctx.glossaire_terms or not fm:
        return res
    if str(fm.get("code", "")).strip().lower() == "glossaire":
        return res

    body_clean = _strip_wikilinks(body)
    flagged: set[str] = set()
    for term in ctx.glossaire_terms:
        term_lower = term.lower()
        if term_lower in R5_TERMS_EXCLUDED:
            continue
        if term_lower in flagged:
            continue
        # word boundary insensible à la casse
        pattern = re.compile(r"\b" + re.escape(term) + r"\b", re.IGNORECASE)
        if pattern.search(body_clean):
            flagged.add(term_lower)
            res.add_warning(
                f"R5: terme `{term}` cité en clair — préférer `[[glossaire#{slugify(term)}]]`"
            )
    return res


# ============================================================
# Règle R7 — Conformité du nom de fichier
# ============================================================

def check_r7_nommage(fp: str) -> RuleResult:
    res = RuleResult()
    base = os.path.basename(fp)
    if not any(pat.match(base) for pat in R7_NAME_SCHEMAS):
        res.add_error(
            f"R7: nom de fichier `{base}` non conforme aux schémas autorisés "
            f"(cu-NNN.md, pr-NN.md, dep-NN.md, aN.md, outils-*.md, glossaire.md, "
            f"transverse-/vigilance-/pattern-/methodologie-/chiffres-macro-/cadrage-/"
            f"calendrier-/gouvernance-/strategie-*.md)"
        )
    return res


# ============================================================
# Règle R8 — Versioning git : last_updated cohérent avec git log
# ============================================================

def get_git_mtime(fp: str, repo_root: str | None = None) -> date | None:
    """Retourne la date Unix de la dernière modif git d'un fichier, ou None
    si git absent, fichier non versionné, ou pas dans un repo.

    Cette fonction est volontairement séparée pour permettre le mockage en test.
    """
    try:
        cmd = ["git", "log", "-1", "--format=%ct", "--", fp]
        kwargs = {}
        if repo_root and os.path.isdir(repo_root):
            kwargs["cwd"] = repo_root
        out = subprocess.check_output(cmd, stderr=subprocess.DEVNULL, **kwargs).decode().strip()
        if not out:
            return None
        ts = int(out)
        return datetime.fromtimestamp(ts, tz=timezone.utc).date()
    except (FileNotFoundError, subprocess.CalledProcessError, ValueError):
        return None


def _parse_last_updated(value) -> date | None:
    """Parse une valeur YAML last_updated en `date`. Tolérant aux types pyyaml
    (datetime.date ou str ISO ou datetime.datetime)."""
    if isinstance(value, date):
        return value if not isinstance(value, datetime) else value.date()
    if isinstance(value, str):
        try:
            return datetime.strptime(value.strip(), "%Y-%m-%d").date()
        except ValueError:
            return None
    return None


def check_r8_versioning(fp: str, fm: dict | None, ctx: AuditContext,
                       git_mtime_func=None) -> RuleResult:
    """Vérifie que last_updated est cohérent avec la dernière modif git
    (écart toléré : 7 jours)."""
    res = RuleResult()
    if not fm or "last_updated" not in fm:
        return res  # R1 signale déjà l'absence du champ
    declared = _parse_last_updated(fm["last_updated"])
    if declared is None:
        res.add_error(
            f"R8: last_updated `{fm['last_updated']}` non parseable (format YYYY-MM-DD attendu)"
        )
        return res

    func = git_mtime_func or get_git_mtime
    git_date = func(fp, ctx.repo_root)
    if git_date is None:
        return res  # git absent ou fichier non versionné — skip silencieux

    delta = abs((git_date - declared).days)
    if delta > R8_LAST_UPDATED_TOLERANCE_DAYS:
        res.add_error(
            f"R8: last_updated `{declared}` vs dernière modif git `{git_date}` "
            f"— écart {delta} jours (> {R8_LAST_UPDATED_TOLERANCE_DAYS})"
        )
    return res


# ============================================================
# Règle R6 — Chiffres sourcés (R6 étendu : reconnaît wikilinks transverses)
# ============================================================

def check_r6_chiffres(fp: str, body: str) -> RuleResult:
    """R6 — chiffre statistique suivi (ou précédé) d'une source proche.

    Fenêtre symétrique de 200 caractères autour du chiffre : la source peut
    apparaître après (mention « Source : », URL, lien markdown) OU avant
    (cas typique d'un wikilink Obsidian `[[chiffres-macro-…|N %]]` où le
    chiffre est dans l'alias).
    """
    res = RuleResult()
    for pat in NUMBER_PATTERNS:
        for m in pat.finditer(body):
            start = m.start()
            end = m.end()
            window = body[max(0, start - 200):end + 200]
            if not SOURCE_MARKERS.search(window):
                snippet = body[max(0, start - 20):start + 40].replace("\n", " ").strip()
                res.add_error(f"R6: chiffre `{m.group(0)}` sans source proche — contexte: «{snippet}»")
    return res


# ============================================================
# Règle R9 — Chiffres macro canoniques cités via wikilink (warning v2)
# ============================================================

# Fenêtre (en caractères) de proximité dans laquelle un wikilink vers
# chiffres-macro-2026 est considéré comme « citant » le chiffre détecté.
R9_PROXIMITY_WINDOW = 200

R9_WIKILINK_PATTERN = re.compile(r"\[\[chiffres-macro-\d{4}[^\]]*\]\]")


def _normalize_chiffre_value(value: str) -> str:
    """Normalise une valeur pour la recherche regex tolérante (espaces,
    casse, séparateurs).  Ex : ``«1,8 h/jour»`` → motif tolérant les
    variations d'espacement."""
    # On échappe les caractères regex, puis on rend les espaces tolérants.
    escaped = re.escape(value.strip())
    return re.sub(r"\\\s+", r"\\s*", escaped)


def check_r9_chiffres_macro(fp: str, fm: dict | None, body: str, ctx: AuditContext) -> RuleResult:
    """Warning si un chiffre canonique du Hub (extrait de chiffres-macro-2026.md)
    apparaît en clair dans un module sans wikilink vers chiffres-macro-2026.md
    à proximité.

    Première itération en warning (cf. brief §4 Bloc C). La détection est
    pragmatique : déduplication par chiffre par fichier pour limiter le bruit.
    """
    res = RuleResult()
    if not ctx.canonical_chiffres or not fm:
        return res
    code = str(fm.get("code", "")).strip().lower()
    if code.startswith("chiffres-macro-") or code == "glossaire":
        return res  # le référentiel lui-même + glossaire

    flagged: set[str] = set()
    for chiffre in ctx.canonical_chiffres:
        value = chiffre["value"]
        if value.lower() in flagged:
            continue
        try:
            value_pattern = re.compile(_normalize_chiffre_value(value), re.IGNORECASE)
        except re.error:
            continue
        for m in value_pattern.finditer(body):
            start = m.start()
            end = m.end()
            window_start = max(0, start - R9_PROXIMITY_WINDOW)
            window_end = end + R9_PROXIMITY_WINDOW
            window = body[window_start:window_end]
            if R9_WIKILINK_PATTERN.search(window):
                continue  # source canonique citée à proximité
            flagged.add(value.lower())
            snippet = body[max(0, start - 20):start + 40].replace("\n", " ").strip()
            res.add_warning(
                f"R9: chiffre macro `{value}` cité en clair — préférer "
                f"`[[chiffres-macro-2026#{chiffre['slug']}]]` (contexte: «{snippet}»)"
            )
            break  # 1 warning par chiffre canonique
    return res


# ============================================================
# Orchestration
# ============================================================

def build_context(files: Iterable[str], vault: str, whitelist_path: str, strict_future: bool = False) -> AuditContext:
    """Construit le contexte d'audit (codes vault + whitelist + glossaire + chiffres)."""
    files = list(files)
    return AuditContext(
        vault_codes=vault_codes(files),
        whitelist_codes=load_whitelist(whitelist_path),
        glossaire_terms=load_glossaire_terms(vault),
        canonical_chiffres=load_canonical_chiffres(
            os.path.join(vault, "transverses", "chiffres-macro-2026.md")
        ),
        repo_root=REPO_ROOT,
        strict_future=strict_future,
    )


def audit_file(fp: str, vault: str, ctx: AuditContext | set[str]) -> dict:
    """Audit complet d'un fichier MD.

    Rétro-compatibilité : si `ctx` est passé comme un `set[str]` (signature v1),
    on l'enveloppe dans un AuditContext minimaliste (sans whitelist ni
    chiffres canoniques — les nouvelles règles ne se déclenchent pas).
    """
    if isinstance(ctx, set):
        ctx = AuditContext(vault_codes=ctx)

    text = read(fp)
    fm, body = split_frontmatter(text)

    total = RuleResult()
    total.merge(check_r1_frontmatter(fp, fm))
    total.merge(check_r2_h1(fp, fm, body))
    total.merge(check_r3_chunking(fp, body))
    total.merge(check_r4_wikilinks(fp, body, ctx))
    total.merge(check_r5_glossaire(fp, fm, body, ctx))
    total.merge(check_r6_chiffres(fp, body))
    total.merge(check_r7_nommage(fp))
    total.merge(check_r8_versioning(fp, fm, ctx))
    total.merge(check_r9_chiffres_macro(fp, fm, body, ctx))

    return {
        "file": rel(fp, vault),
        "hits": total.errors,        # rétro-compatibilité avec tests v1
        "errors": total.errors,
        "warnings": total.warnings,
    }


def format_report(results: list[dict], vault: str) -> str:
    total_files = len(results)
    files_with_errors = [r for r in results if r["errors"]]
    files_with_warnings = [r for r in results if r["warnings"]]
    total_errors = sum(len(r["errors"]) for r in results)
    total_warnings = sum(len(r["warnings"]) for r in results)

    lines: list[str] = []
    lines.append("=" * 70)
    lines.append("AUDIT MD-RAG v2 — rapport (SPEC v1.3, D-028 + D-029)")
    lines.append("=" * 70)
    lines.append(f"Vault                  : {vault}")
    lines.append(f"Fichiers audités       : {total_files}")
    lines.append(f"Fichiers en erreur     : {len(files_with_errors)}")
    lines.append(f"Fichiers avec warnings : {len(files_with_warnings)}")
    lines.append(f"Total erreurs          : {total_errors}")
    lines.append(f"Total warnings         : {total_warnings}")
    lines.append("")

    if not files_with_errors and not files_with_warnings:
        lines.append("✅ CLEAN — aucun écart détecté.")
        return "\n".join(lines) + "\n"

    err_by_rule: dict[str, int] = {}
    warn_by_rule: dict[str, int] = {}
    for r in results:
        for h in r["errors"]:
            rule = h.split(":", 1)[0]
            err_by_rule[rule] = err_by_rule.get(rule, 0) + 1
        for h in r["warnings"]:
            rule = h.split(":", 1)[0]
            warn_by_rule[rule] = warn_by_rule.get(rule, 0) + 1

    if err_by_rule:
        lines.append("Erreurs par règle :")
        for rule in sorted(err_by_rule):
            lines.append(f"  {rule}: {err_by_rule[rule]} erreur(s)")
        lines.append("")
    if warn_by_rule:
        lines.append("Warnings par règle :")
        for rule in sorted(warn_by_rule):
            lines.append(f"  {rule}: {warn_by_rule[rule]} warning(s)")
        lines.append("")

    for r in results:
        if not r["errors"] and not r["warnings"]:
            continue
        lines.append("-" * 70)
        header = f"📄 {r['file']}"
        if r["errors"]:
            header += f" — {len(r['errors'])} erreur(s)"
        if r["warnings"]:
            header += f" — {len(r['warnings'])} warning(s)"
        lines.append(header)
        for h in r["errors"]:
            lines.append(f"  ✗ {h}")
        for h in r["warnings"]:
            lines.append(f"  ⚠ {h}")
    lines.append("")
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Audit conformité MD vault RAG (SPEC v1.3).")
    parser.add_argument("--vault", default=DEFAULT_VAULT, help="chemin du vault (défaut: rag/content)")
    parser.add_argument("--report", default=None, help="chemin de sortie (défaut: stdout)")
    parser.add_argument("--strict", action="store_true", help="exit 1 dès première erreur")
    parser.add_argument("--strict-future", action="store_true",
                        help="transforme les warnings R4 (whitelist) en erreurs")
    parser.add_argument("--whitelist", default=DEFAULT_WHITELIST,
                        help="chemin du whitelist-wikilinks-futurs.md")
    args = parser.parse_args(argv)

    vault = os.path.abspath(args.vault)
    if not os.path.isdir(vault):
        print(f"[erreur] vault introuvable : {vault}", file=sys.stderr)
        return 2

    files = list_md_files(vault)
    if not files:
        report = f"⚠️  Aucun fichier .md trouvé dans {vault}\n"
        if args.report:
            with open(args.report, "w", encoding="utf-8") as f:
                f.write(report)
        else:
            print(report)
        return 0

    ctx = build_context(files, vault, args.whitelist, strict_future=args.strict_future)
    results = [audit_file(fp, vault, ctx) for fp in files]
    report = format_report(results, vault)

    if args.report:
        with open(args.report, "w", encoding="utf-8") as f:
            f.write(report)
    else:
        print(report)

    total_errors = sum(len(r["errors"]) for r in results)
    return 1 if total_errors > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
