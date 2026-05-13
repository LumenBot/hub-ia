#!/usr/bin/env python3
"""
Audit global du Hub IA — Learning Center
=========================================

Script qui exécute en batch toutes les vérifications structurelles RULES.md sur
l'ensemble du site, et produit un rapport markdown listant tous les écarts.

À lancer à chaque clôture d'itération AVANT push :
    python3 site-web-prep/audit-global.py

Sortie :
    site-web-prep/audit-rapport.md (rapport markdown)
    Code retour : 0 si 0 hit (clean), 1 si hits détectés

Couvre 13 règles RULES (mai 2026) :
    1.  Cohérence numérique cross-site (chiffres glossaire)
    2.  Cohérence intra-page (exec-stats vs prose vs badges)
    3.  Pas de versioning interne front-visible
    4.  Pas de biais sectoriel ou territorial dominant
    5.  Structure canonique module-section-header (callout hors header)
    6.  Callout intro Pour-aller-plus-loin avec margin-bottom
    7.  Pas de codes internes (CU-XXX / PR-XX / DEP-XX) en texte affiché
    8.  Lien outil obligatoire sur première mention significative
    9.  Cohérence card index ↔ contenu réel
    10. Format canonique du sommaire (emoji + titre court)
    11. Contraste lecture sur fonds foncés (inline dark colors)
    12. Pas de placeholders STASH résiduels (post-bulk-patch)
    13. Pas de NUL bytes (post-bulk-patch)
"""

from __future__ import annotations

import os
import re
import sys
import glob
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ============================================================
# Helpers
# ============================================================

def list_module_files():
    return sorted(glob.glob(os.path.join(ROOT, 'modules', 'cu-*.html')))

def list_prealable_files():
    return sorted(glob.glob(os.path.join(ROOT, 'prealables', 'pr-*.html')))

def list_dep_files():
    return sorted(glob.glob(os.path.join(ROOT, 'deploiement', 'dep-*.html')))

def list_root_pages():
    return [
        os.path.join(ROOT, 'index.html'),
        os.path.join(ROOT, 'prealables.html'),
        os.path.join(ROOT, 'architectures.html'),
        os.path.join(ROOT, 'deploiement.html'),
        os.path.join(ROOT, 'ressources.html'),
    ]

def all_html_files():
    return list_module_files() + list_prealable_files() + list_dep_files() + list_root_pages()

def rel(fp):
    return os.path.relpath(fp, ROOT)

def read(fp):
    with open(fp, encoding='utf-8') as f:
        return f.read()


# ============================================================
# Règle 1 — Cohérence numérique cross-site
# ============================================================

def audit_coherence_numerique():
    """Compte les éléments réels et vérifie qu'ils sont reflétés cross-site."""
    hits = []
    real = {
        'modules': len(list_module_files()),
        'prealables': len(list_prealable_files()),
        'fiches_dep': len(list_dep_files()),
        'fiches_outils': 0,  # comptés dans ressources.html
    }
    res = read(os.path.join(ROOT, 'ressources.html'))
    real['fiches_outils'] = len(re.findall(r'tool-card" id="', res))

    # Expected references in front-visible pages
    expectations = [
        # (relative_path, regex_to_find, expected_value)
        ('index.html', r'(\d+) modules cas d.usage', real['modules']),
        ('index.html', r'(\d+) fiches outils', real['fiches_outils']),
        ('prealables.html', r'(\d+) cas d.usage', real['modules']),
        ('prealables.html', r'(\d+) fiches outils', real['fiches_outils']),
        ('ressources.html', r'(\d+) fiches deep-dive', real['fiches_outils']),
        ('ressources.html', r'(\d+) outils essentiels', real['fiches_outils']),
        ('ressources.html', r'(\d+) fiches en \d+ catégories', real['fiches_outils']),
    ]
    for path, pattern, expected in expectations:
        s = read(os.path.join(ROOT, path))
        for m in re.finditer(pattern, s):
            actual = int(m.group(1))
            if actual != expected:
                line = s[:m.start()].count('\n') + 1
                hits.append({
                    'rule': '1 — Cohérence numérique',
                    'file': path,
                    'line': line,
                    'issue': f"« {m.group(0)} » mais réel = {expected}",
                })
    return hits, real


# ============================================================
# Règle 2 — Cohérence intra-page (badges / exec-stats / prose)
# ============================================================

def audit_coherence_intrapage():
    """Détecte les chiffres incohérents au sein d'une même page."""
    hits = []
    # ressources.html : "X fiches · Y catégories" cohérent partout
    res = read(os.path.join(ROOT, 'ressources.html'))
    real_fiches = len(re.findall(r'tool-card" id="', res))
    real_cat = len(re.findall(r'class="cat-divider"', res))

    for m in re.finditer(r'(\d+)\s+fiches?\s+(?:·|en)?\s*(\d+)?\s*catégories?', res):
        f_val = int(m.group(1))
        c_val = int(m.group(2)) if m.group(2) else None
        line = res[:m.start()].count('\n') + 1
        if f_val != real_fiches:
            hits.append({
                'rule': '2 — Cohérence intra-page',
                'file': 'ressources.html',
                'line': line,
                'issue': f"« {f_val} fiches » mais comptage réel = {real_fiches}",
            })
        if c_val is not None and c_val != real_cat:
            hits.append({
                'rule': '2 — Cohérence intra-page',
                'file': 'ressources.html',
                'line': line,
                'issue': f"« {c_val} catégories » mais comptage réel = {real_cat}",
            })

    # Vérifier que toutes les categories ont une entrée dans le sommaire
    real_cats = re.findall(r'cat-divider" id="(cat-[a-z0-9-]+)"', res)
    toc_match = re.search(r'<ul class="module-toc-list"[^>]*>.*?</ul>', res, re.DOTALL)
    if toc_match:
        toc = toc_match.group(0)
        toc_cats = re.findall(r'href="#(cat-[a-z0-9-]+)"', toc)
        missing = [c for c in real_cats if c not in toc_cats]
        for c in missing:
            hits.append({
                'rule': '2 — Cohérence intra-page',
                'file': 'ressources.html',
                'line': 0,
                'issue': f"Catégorie #{c} absente du sommaire (mais présente dans le DOM)",
            })

    return hits


# ============================================================
# Règle 3 — Pas de versioning interne front-visible
# ============================================================

def audit_versioning_front():
    """Détecte « V3.X » ou « v3.x » dans le contenu visible."""
    hits = []
    pat = re.compile(r'\b[Vv]3\.\d+(?:\.\d+)?\b')
    for fp in all_html_files():
        s = read(fp)
        # Strip comments / script / style
        clean = re.sub(r'<!--.*?-->', '', s, flags=re.DOTALL)
        clean = re.sub(r'<script.*?</script>', '', clean, flags=re.DOTALL)
        clean = re.sub(r'<style.*?</style>', '', clean, flags=re.DOTALL)
        for m in pat.finditer(clean):
            line = clean[:m.start()].count('\n') + 1
            ctx = clean[max(0, m.start()-40):min(len(clean), m.end()+40)].replace('\n', ' ').strip()
            hits.append({
                'rule': '3 — Pas de versioning front',
                'file': rel(fp),
                'line': line,
                'issue': f"« {m.group(0)} » en clair — ctx: ...{ctx[:80]}...",
            })
    return hits


# ============================================================
# Règle 4 — Pas de biais sectoriel ou territorial dominant
# ============================================================

def audit_biais_sectoriel():
    """Détecte un module qui sature sur une seule filière ou un seul écosystème territorial."""
    hits = []
    sectors = {
        'bois': r'\b(?:bois|grume|scieri|menuiseri|panneau|charpent|ENSTIB|LERMAB)\b',
        'textile': r'\b(?:textile|tissu|filature|tissage|Lectra)\b',
        'métal': r'\b(?:métallurg|tôle|profilé|forge|fonderi)\b',
        'plasturgie': r'\b(?:plastur|moulage|injection)\b',
        'agroalim': r'\b(?:agroaliment|laiteri|fromager|brasseri|abattoir)\b',
    }
    territories = {
        'Grand_Est': r'\b(?:Grand\sEst|Vosges|Lorraine|Alsace|Champagne-Ardenne|Épinal|Nancy|Strasbourg|Mulhouse)\b',
    }
    for fp in list_module_files() + list_prealable_files() + list_dep_files():
        s = read(fp)
        # Strip comments / scripts / styles
        s_clean = re.sub(r'<script.*?</script>|<style.*?</style>|<!--.*?-->', '', s, flags=re.DOTALL)
        sector_counts = {k: len(re.findall(p, s_clean, re.I)) for k, p in sectors.items()}
        territ_count = sum(len(re.findall(p, s_clean, re.I)) for p in territories.values())
        total_sector = sum(sector_counts.values())
        if total_sector >= 30:
            for sec, n in sector_counts.items():
                share = n / total_sector * 100
                if share > 60:
                    hits.append({
                        'rule': '4 — Biais sectoriel',
                        'file': rel(fp),
                        'line': 0,
                        'issue': f"Filière « {sec} » sature ({n}/{total_sector} = {share:.0f}%, seuil 60%)",
                    })
        if territ_count > 25 and territ_count / max(1, total_sector + territ_count) > 0.30:
            hits.append({
                'rule': '4 — Biais territorial',
                'file': rel(fp),
                'line': 0,
                'issue': f"Mentions Grand Est = {territ_count} (seuil 25 + 30% du total)",
            })
    return hits


# ============================================================
# Règle 5 — Structure canonique module-section-header
# ============================================================

def audit_section_header():
    """Le module-section-header ne doit contenir que icône + titre."""
    hits = []
    pat = re.compile(
        r'<div class="module-section-header">(.*?)</div>\s*(?=<div class="(?!module-section-icon|module-section-title)|<p|<ul|<ol|<h3|<section|<table|</section)',
        re.DOTALL
    )
    for fp in list_module_files() + list_prealable_files() + list_dep_files():
        s = read(fp)
        for m in pat.finditer(s):
            body = m.group(1)
            body_check = re.sub(r'<div class="module-section-icon[^"]*">[^<]*</div>', '', body)
            body_check = re.sub(r'<h2 class="module-section-title">[^<]*</h2>', '', body_check)
            body_check = re.sub(r'<div class="module-section-title">.*?</div>', '', body_check, flags=re.DOTALL)
            body_check = re.sub(r'<h2>[^<]*</h2>', '', body_check)
            body_check = body_check.strip()
            if body_check:
                line = s[:m.start()].count('\n') + 1
                if 'callout' in body_check or '<p' in body_check or '<ul' in body_check:
                    hits.append({
                        'rule': '5 — Structure section-header',
                        'file': rel(fp),
                        'line': line,
                        'issue': f"Contenu non-canonique dans header : {body_check[:60]}...",
                    })
    return hits


# ============================================================
# Règle 6 — Callout intro Pour-aller-plus-loin avec margin
# ============================================================

def audit_callout_intro_margin():
    """Le callout-info avant resources-cat doit avoir un style margin."""
    hits = []
    for fp in list_module_files() + list_prealable_files() + list_dep_files():
        s = read(fp)
        for m in re.finditer(r'<div class="callout callout-info">', s):
            after = s[m.end():m.end() + 1500]
            cb = re.search(r'</div>\s*<div class="resources-cat">', after)
            next_callout = after.find('<div class="callout')
            if cb and (next_callout == -1 or cb.start() < next_callout):
                # This is an intro callout — needs margin
                line = s[:m.start()].count('\n') + 1
                hits.append({
                    'rule': '6 — Callout intro margin',
                    'file': rel(fp),
                    'line': line,
                    'issue': "callout intro sans style margin-bottom",
                })
    return hits


# ============================================================
# Règle 7 — Pas de codes internes (CU/PR/DEP) en texte affiché
# ============================================================

def audit_jargon_codes():
    """Détecte tout label <a>CODE Titre</a> ou texte brut CODE-XX visible."""
    hits = []
    # <a>CODE Titre</a> — strip code prefix from label
    pat_a = re.compile(r'<a [^>]+>(CU-\d+|PR-\d+|DEP-\d+)\b[^<]*</a>')
    # Plain text CODE-XX hors <a> et attributs
    pat_plain = re.compile(r'(?<![/-])\b(CU-\d+|PR-\d+|DEP-\d+)\b(?!-)')

    for fp in all_html_files():
        s = read(fp)
        for m in pat_a.finditer(s):
            line = s[:m.start()].count('\n') + 1
            hits.append({
                'rule': '7 — Jargon codes internes',
                'file': rel(fp),
                'line': line,
                'issue': f"Label <a> commence par code : {m.group(0)[:80]}",
            })
        # Pour plain text, on strippe scripts / styles / a / comments / attrs
        clean = re.sub(r'<a [^>]*>.*?</a>', '', s, flags=re.DOTALL)
        clean = re.sub(r'<script.*?</script>|<style.*?</style>|<!--.*?-->', '', clean, flags=re.DOTALL)
        clean = re.sub(r'<[^>]+>', '', clean)
        for m in pat_plain.finditer(clean):
            ctx_before = clean[max(0, m.start()-40):m.start()].lower()
            if 'module' in ctx_before or 'auto-diag' in ctx_before:
                continue
            line = clean[:m.start()].count('\n') + 1
            hits.append({
                'rule': '7 — Jargon codes en clair',
                'file': rel(fp),
                'line': line,
                'issue': f"Code « {m.group(1)} » en texte brut",
            })
    return hits


# ============================================================
# Règle 9 — Cohérence card index ↔ contenu réel
# ============================================================

def audit_card_content_coherence():
    """Vérifie que les labels card-quiz reflètent le contenu effectif des modules."""
    hits = []
    home = read(os.path.join(ROOT, 'index.html'))
    card_re = re.compile(
        r'<a href="modules/(cu-\d+-[a-z0-9-]+)\.html"[^>]*>.*?<span class="card-quiz">([^<]+)</span>',
        re.DOTALL
    )
    for m in card_re.finditer(home):
        cu_id, label = m.group(1), m.group(2).strip()
        fp = os.path.join(ROOT, 'modules', f'{cu_id}.html')
        if not os.path.exists(fp):
            continue
        s = read(fp)
        flags = set()
        if re.search(r'case-deep-step|case-deep-final|<h2[^>]*>[^<]*(?:[Éé]tude de cas|RetEx|Mise en situation)', s):
            flags.add('CASE')
        if re.search(r'<h2[^>]*>[^<]*Auto-diagnostic', s) or 'id="diagnostic"' in s:
            flags.add('AUTO-DIAG')
        if re.search(r'<h2[^>]*>[^<]*[Qq]uiz', s):
            flags.add('QUIZ')
        if 'checklist-block' in s or re.search(r'<h2[^>]*>[^<]*[Cc]hecklist', s):
            flags.add('CHECKLIST')
        if re.search(r'<h2[^>]*>[^<]*(?:[Pp]lan d.action|[Pp]lan 30 jours)', s):
            flags.add('PLAN')
        if 'incident-card' in s or re.search(r'<h2[^>]*>[^<]*[Ii]ncident', s):
            flags.add('INCIDENT')
        label_l = label.lower()
        expected = set()
        if 'étude de cas' in label_l or 'etude de cas' in label_l:
            expected.add('CASE')
        if 'auto-diagnostic' in label_l:
            expected.add('AUTO-DIAG')
        if 'quiz' in label_l:
            expected.add('QUIZ')
        if 'checklist' in label_l:
            expected.add('CHECKLIST')
        if 'plan' in label_l:
            expected.add('PLAN')
        if 'cas pédagogique' in label_l:
            expected.add('INCIDENT')
        missing = expected - flags
        if missing:
            hits.append({
                'rule': '9 — Card↔contenu',
                'file': 'index.html',
                'line': 0,
                'issue': f"{cu_id}: label « {label} » promet {expected}, contenu réel = {flags}, manque {missing}",
            })
    return hits


# ============================================================
# Règle 10 — Format canonique sommaire (emoji)
# ============================================================

def audit_sommaire_canonique():
    """Tous les sommaires doivent utiliser <ul class='module-toc-list'> avec toc-icon,
    et chaque entrée doit avoir un emoji contextuel (pas le fallback 📌)."""
    hits = []
    for fp in list_module_files() + list_prealable_files() + list_dep_files() + [os.path.join(ROOT, 'architectures.html')]:
        s = read(fp)
        m = re.search(r'<aside class="module-toc">.*?</aside>', s, re.DOTALL)
        if not m:
            continue
        toc = m.group(0)
        if '<ul class="module-toc-list"' not in toc:
            line = s[:m.start()].count('\n') + 1
            hits.append({
                'rule': '10 — Sommaire canonique',
                'file': rel(fp),
                'line': line,
                'issue': "Sommaire non emoji-style (<nav class=\"module-toc-nav\"> au lieu de <ul class=\"module-toc-list\">)",
            })
            continue
        # Détecte l'emoji fallback 📌 (mapping incomplet du convertisseur v3.7.10)
        fallback_count = toc.count('<span class="toc-icon">📌</span>')
        if fallback_count > 0:
            line = s[:m.start()].count('\n') + 1
            hits.append({
                'rule': '10 — Sommaire fallback',
                'file': rel(fp),
                'line': line,
                'issue': f"{fallback_count} entrée(s) avec emoji fallback 📌 — mapping titre→emoji incomplet, remplacer par un emoji contextuel",
            })
        # Détecte la répétition excessive du même emoji (>3 fois dans le même TOC = mapping pauvre)
        icons = re.findall(r'<span class="toc-icon">([^<]+)</span>', toc)
        from collections import Counter
        cnt = Counter(icons)
        for emo, n in cnt.items():
            # Tolérer 🎯 qui est légitimement utilisé pour "Ce que tu sauras faire" ET "Cas d'étude"
            if n >= 4 and emo != '🎯':
                line = s[:m.start()].count('\n') + 1
                hits.append({
                    'rule': '10 — Sommaire répétition emoji',
                    'file': rel(fp),
                    'line': line,
                    'issue': f"Emoji {emo} utilisé {n} fois dans le sommaire — varier pour gain visuel",
                })
    return hits


# ============================================================
# Règle 11 — Contraste lecture sur fonds foncés
# ============================================================

def audit_contraste_dark():
    """Inline color: var(--color-text...) ou var(--color-primary) dans .exec-summary/.case-deep-final/.archi-block."""
    hits = []
    for fp in list_module_files() + list_prealable_files() + list_dep_files():
        s = read(fp)
        for container_class in ['exec-summary', 'case-deep-final', 'archi-block']:
            for m_open in re.finditer(rf'<div class="{container_class}"[^>]*>', s):
                start = m_open.start()
                depth = 1
                i = m_open.end()
                while i < len(s) and depth > 0:
                    no = s.find('<div', i)
                    nc = s.find('</div>', i)
                    if nc == -1:
                        break
                    if no != -1 and no < nc:
                        depth += 1
                        i = no + 4
                    else:
                        depth -= 1
                        i = nc + 6
                container = s[start:i]
                for im in re.finditer(r'style="[^"]*color:\s*(var\(--color-(?:text|primary)[^)]*\))[^"]*"', container):
                    line_in = container[:im.start()].count('\n')
                    abs_line = s[:start].count('\n') + 1 + line_in
                    hits.append({
                        'rule': '11 — Contraste dark bg',
                        'file': rel(fp),
                        'line': abs_line,
                        'issue': f"[{container_class}] inline color {im.group(1)} → illisible sur fond foncé",
                    })
    return hits


# ============================================================
# Règle 12 — Pas de placeholders STASH résiduels
# ============================================================

def audit_stash_residuals():
    hits = []
    for fp in all_html_files():
        s = read(fp)
        if 'STASH' in s and re.search(r'\bSTASH\d+\b', s):
            for m in re.finditer(r'\bSTASH\d+\b', s):
                line = s[:m.start()].count('\n') + 1
                hits.append({
                    'rule': '12 — STASH résiduel',
                    'file': rel(fp),
                    'line': line,
                    'issue': f"Placeholder STASH non restauré : {m.group(0)}",
                })
    return hits


# ============================================================
# Règle 13 — Pas de NUL bytes
# ============================================================

def audit_nul_bytes():
    hits = []
    for fp in all_html_files():
        with open(fp, 'rb') as f:
            data = f.read()
        nuls = data.count(b'\x00')
        if nuls:
            hits.append({
                'rule': '13 — NUL bytes',
                'file': rel(fp),
                'line': 0,
                'issue': f"{nuls} octet(s) NUL (\\x00) — corruption post-bulk-patch",
            })
    return hits


# ============================================================
# Règle 14 — Renvois outils → ressources.html#anchor (Rule I.1 v1.6)
# ============================================================

# Outils ambigus (homographes de mots usuels) — décision manuelle requise,
# l'audit ne flagge PAS leurs mentions
TOOL_AMBIGUOUS = {'Make', 'v0', 'Comet', 'Operator', 'Atlas', 'Crayon', 'Whisper'}

def _build_tool_catalog():
    """Lit ressources.html et extrait (anchor, primary_name) pour chaque tool-card."""
    res_path = os.path.join(ROOT, 'ressources.html')
    if not os.path.exists(res_path):
        return []
    html = read(res_path)
    pat = re.compile(
        r'<article class="tool-card" id="([^"]+)">.*?<h3>([^<]+?)'
        r'(?:<span[^>]*>[^<]*</span>)?</h3>',
        re.DOTALL,
    )
    catalog = []
    for m in pat.finditer(html):
        anchor = m.group(1)
        name = re.sub(r'\s+', ' ', m.group(2)).strip()
        catalog.append((anchor, name))
    return catalog

def audit_tool_link_first_mention():
    """Détecte les pages où le nom d'un outil possédant une tool-card est mentionné
    sans aucun lien vers la fiche ressources.html#anchor correspondante.
    Une seule mention liée par page suffit (la première)."""
    hits = []
    catalog = _build_tool_catalog()
    if not catalog:
        return hits

    # Liste des noms (primary + variantes manuelles connues à ne PAS dupliquer ici —
    # le script link-tools-to-resources.py est la référence pour les alias)
    tools = [(a, n) for a, n in catalog if n not in TOOL_AMBIGUOUS]

    # Zones protégées (identiques au linker)
    protected = [
        re.compile(r'<a\b[^>]*>.*?</a>', re.DOTALL),
        re.compile(r'<code\b[^>]*>.*?</code>', re.DOTALL),
        re.compile(r'<pre\b[^>]*>.*?</pre>', re.DOTALL),
        re.compile(r'<script\b[^>]*>.*?</script>', re.DOTALL),
        re.compile(r'<style\b[^>]*>.*?</style>', re.DOTALL),
        re.compile(r'<svg\b[^>]*>.*?</svg>', re.DOTALL),
        re.compile(r'<aside\b[^>]*class="module-toc"[^>]*>.*?</aside>', re.DOTALL),
        re.compile(r'<title\b[^>]*>.*?</title>', re.DOTALL),
        re.compile(r'<meta\b[^>]*>'),
        re.compile(r'<[^>]+>'),
    ]

    for fp in all_html_files():
        if rel(fp) == 'ressources.html':
            continue
        s = read(fp)
        # mask
        mask = [True] * len(s)
        for p in protected:
            for m in p.finditer(s):
                for i in range(m.start(), m.end()):
                    mask[i] = False
        # Pour chaque outil, vérifier si une mention non-liée existe ET si aucun lien
        # vers cet anchor n'est déjà présent sur la page
        for anchor, name in tools:
            # Lien déjà présent ?
            if re.search(r'href="[^"]*ressources\.html#' + re.escape(anchor) + r'"', s):
                continue
            # Cherche une mention non-liée
            pat = re.compile(r'(?<![\w.\-])' + re.escape(name) + r'(?![\w.\-])')
            for m in pat.finditer(s):
                if all(mask[i] for i in range(m.start(), m.end())):
                    line = s[:m.start()].count('\n') + 1
                    hits.append({
                        'rule': '14 — Renvoi outil manquant',
                        'file': rel(fp),
                        'line': line,
                        'issue': f"Mention « {name} » non liée — manque <a href=\".../ressources.html#{anchor}\">",
                    })
                    break  # une seule occurrence rapportée par fichier par outil
    return hits


# ============================================================
# Règle 15 — Responsive basics (Rule E.2 v1.6)
# ============================================================

def audit_responsive_basics():
    """Détecte les styles inline <style>...</style> qui introduisent un padding
    > var(--space-5) (24 px) OU une grille > 1 colonne SANS @media query
    associée dans le même bloc <style>.
    Heuristique défensive : si on ajoute du design dans un fichier sans
    breakpoint mobile, on signale.
    """
    hits = []
    style_block_re = re.compile(r'<style\b[^>]*>(.*?)</style>', re.DOTALL)
    # Patterns considérés comme "non responsive" sans @media :
    risky_re = re.compile(
        r'(?:'
        r'padding\s*:\s*var\(--space-[6789]\)'      # padding très large
        r'|padding\s*:\s*(?:[3-9]|[1-9]\d+)\s*rem'  # padding pixel/rem absolu >= 3rem
        r'|grid-template-columns\s*:\s*repeat\(\s*[2-9]\s*,'  # grille à 2+ colonnes fixes
        r')',
        re.IGNORECASE,
    )
    media_re = re.compile(r'@media\s*\([^)]*max-width', re.IGNORECASE)

    for fp in all_html_files():
        s = read(fp)
        for m in style_block_re.finditer(s):
            block = m.group(1)
            # Ignorer les blocs minuscules (commentaires migration, etc.)
            if len(block.strip()) < 100:
                continue
            if risky_re.search(block) and not media_re.search(block):
                line = s[:m.start()].count('\n') + 1
                hits.append({
                    'rule': '15 — Responsive manquant',
                    'file': rel(fp),
                    'line': line,
                    'issue': "Bloc <style> avec padding large / grille fixe sans @media query mobile (cf. E.2)",
                })
    return hits


# ============================================================
# Main
# ============================================================

def main():
    print("Audit global Hub IA — Learning Center")
    print("=" * 60)

    all_hits = []
    all_hits += audit_versioning_front()
    coh_hits, real = audit_coherence_numerique()
    all_hits += coh_hits
    all_hits += audit_coherence_intrapage()
    all_hits += audit_biais_sectoriel()
    all_hits += audit_section_header()
    all_hits += audit_callout_intro_margin()
    all_hits += audit_jargon_codes()
    all_hits += audit_card_content_coherence()
    all_hits += audit_sommaire_canonique()
    all_hits += audit_contraste_dark()
    all_hits += audit_stash_residuals()
    all_hits += audit_nul_bytes()
    all_hits += audit_tool_link_first_mention()
    all_hits += audit_responsive_basics()

    # Group by rule
    by_rule = {}
    for h in all_hits:
        by_rule.setdefault(h['rule'], []).append(h)

    # Markdown report
    lines = []
    lines.append("# Audit global — Hub IA Learning Center")
    lines.append("")
    lines.append(f"**Total hits** : {len(all_hits)}")
    lines.append("")
    lines.append("**Comptages réels** :")
    for k, v in real.items():
        lines.append(f"- {k} : {v}")
    lines.append("")

    if not all_hits:
        lines.append("✅ Aucun écart détecté.")
    else:
        for rule, hits in sorted(by_rule.items()):
            lines.append(f"## {rule} ({len(hits)} hits)")
            lines.append("")
            for h in hits:
                loc = f"{h['file']}" + (f":{h['line']}" if h['line'] else '')
                lines.append(f"- `{loc}` — {h['issue']}")
            lines.append("")

    rapport_md = '\n'.join(lines)
    rapport_path = os.path.join(ROOT, 'site-web-prep', 'audit-rapport.md')
    with open(rapport_path, 'w', encoding='utf-8') as f:
        f.write(rapport_md)

    print(f"\nRapport écrit : {rel(rapport_path)}")
    print(f"Total hits : {len(all_hits)}")
    if by_rule:
        for r, hits in sorted(by_rule.items()):
            print(f"  {r}: {len(hits)}")

    return 0 if not all_hits else 1


if __name__ == '__main__':
    sys.exit(main())
