"""
Wrap first unlinked mention per file of each tool name with a link
to ressources.html#anchor.

Fixed: track consumed ranges to avoid overlapping replacements
(prevents 'Claude' matching inside 'Claude Code').
Also: skip occurrences inside SVG <text> elements.
"""
import re
from pathlib import Path

ROOT = Path('/home/user/hub-ia')

# (anchor, name) — order doesn't matter for correctness now, but
# putting longer-name variants first per anchor gives nicer link labels.
TOOLS = [
    ('claude-code', 'Claude Code'),
    ('claude-chrome', 'Claude pour Chrome'),
    ('claude', 'Claude'),
    ('gpt', 'GPT-4o'),
    ('gpt', 'GPT-4 Turbo'),
    ('gpt', 'GPT-4 mini'),
    ('gpt', 'GPT-4'),
    ('gpt', 'GPT-5'),
    ('atlas', 'ChatGPT Atlas'),
    ('gpt', 'ChatGPT'),
    ('mistral-agents', 'Mistral Agents SDK'),
    ('mistral-forge', 'Mistral Forge'),
    ('mistral', 'Mistral Large'),
    ('mistral', 'Mistral Medium'),
    ('mistral', 'Mistral Small'),
    ('mistral', 'Mistral 7B'),
    ('mistral', 'Mistral AI'),
    ('mistral', 'Mistral'),
    ('notebooklm', 'NotebookLM'),
    ('mixtral', 'Mixtral'),
    ('llama', 'Llama 3'),
    ('llama', 'Llama 7B'),
    ('llama', 'Llama 8B'),
    ('llama', 'Llama'),
    ('qwen', 'Qwen'),
    ('kimi', 'Kimi K2.6'),
    ('kimi', 'Kimi K2'),
    ('kimi', 'Kimi'),
    ('lucie', 'Lucie'),
    ('pleias-rag', 'Pleias-RAG'),
    ('pleias-rag', 'Pleias RAG'),
    ('pleias-rag', 'Pleias'),
    ('lighton', 'LightOn'),
    ('n8n', 'n8n'),
    ('dify', 'Dify'),
    ('flowise', 'Flowise'),
    ('composio', 'Composio'),
    ('beever-atlas', 'Beever Atlas'),
    ('langgraph', 'LangGraph'),
    ('crewai', 'CrewAI'),
    ('autogen', 'AutoGen'),
    ('openclaw', 'OpenClaw'),
    ('pytorch', 'PyTorch'),
    ('computer-use', 'Anthropic Computer Use'),
    ('computer-use', 'Computer Use'),
    ('mcp', 'Model Context Protocol'),
    ('mcp', 'MCP'),
    ('a2a', 'A2A'),
    ('lindy', 'Lindy'),
    ('manus', 'Manus'),
    ('hermes-agent', 'Hermes Agent'),
    ('aaflow', 'AAFLOW'),
    ('cursor', 'Cursor'),
    ('copilot-workspace', 'GitHub Copilot Workspace'),
    ('copilot-workspace', 'Copilot Workspace'),
    ('aider', 'Aider'),
    ('devin', 'Devin'),
    ('lovable', 'Lovable'),
    ('bolt-new', 'Bolt.new'),
    ('replit-agent', 'Replit Agent'),
    ('windsurf', 'Windsurf'),
    ('qdrant', 'Qdrant'),
    ('pgvector', 'Postgres pgvector'),
    ('pgvector', 'pgvector'),
    ('pinecone', 'Pinecone'),
    ('chromadb', 'ChromaDB'),
    ('apify', 'Apify'),
    ('agentmail', 'AgentMail'),
    ('voxtral', 'Voxtral'),
    ('cartesia', 'Cartesia'),
    ('elevenlabs', 'ElevenLabs Conv 2.0'),
    ('elevenlabs', 'ElevenLabs'),
    ('vapi', 'Vapi.ai'),
    ('vapi', 'Vapi'),
    ('brand24', 'Brand24'),
    ('klue', 'Klue'),
    ('perplexity', 'Perplexity'),
    ('otter', 'Otter.ai'),
    ('otter', 'Otter'),
    ('fireflies', 'Fireflies.ai'),
    ('fireflies', 'Fireflies'),
    ('tldv', 'tl;dv'),
    ('beehiiv', 'Beehiiv'),
    ('deepl', 'DeepL Pro'),
    ('deepl', 'DeepL'),
    ('clickup-brain', 'ClickUp Brain'),
    ('clickup-brain', 'ClickUp'),
    ('supersplat', 'SuperSplat'),
    ('hubspot', 'HubSpot'),
    ('pipedrive', 'Pipedrive'),
    ('attio', 'Attio'),
    ('salesforce', 'Salesforce'),
    ('dynamics', 'Microsoft Dynamics 365'),
    ('dynamics', 'Dynamics 365'),
    ('zoho', 'Zoho CRM'),
    ('zoho', 'Zoho'),
    ('pennylane', 'Pennylane'),
    ('sellsy', 'Sellsy'),
    ('axonaut', 'Axonaut'),
    ('pandadoc', 'PandaDoc'),
    ('esker', 'Esker'),
    ('sidetrade', 'Sidetrade'),
    ('tacton', 'Tacton'),
    ('yolo-opencv', 'YOLO + OpenCV'),
    ('yolo-opencv', 'YOLO'),
    ('yolo-opencv', 'OpenCV'),
    ('roboflow', 'Roboflow'),
    ('cognex', 'Cognex'),
    ('keyence', 'Keyence'),
    ('landing-ai', 'Landing AI'),
    ('mask-rcnn', 'Mask R-CNN'),
    ('florence-2', 'Florence-2'),
    ('sam-2', 'SAM 2'),
    ('or-tools', 'OR-Tools'),
    ('cadwork', 'Cadwork'),
    ('topsolid', 'TopSolid'),
    ('lectra', 'Lectra'),
    ('gurobi', 'Gurobi'),
    ('cplex', 'IBM CPLEX'),
    ('cplex', 'CPLEX'),
    ('xpress', 'FICO Xpress'),
    ('xpress', 'Xpress'),
    ('goodweek', 'Goodweek'),
    ('nin-ia', 'NIN-IA'),
    ('ethiqais', 'EthiqAIS'),
    ('spinalia', 'Spinalia'),
]

def res_url(path: Path, anchor: str) -> str:
    rel = path.relative_to(ROOT)
    parts = rel.parts
    if len(parts) == 1:
        return f"ressources.html#{anchor}"
    return "../" * (len(parts)-1) + f"ressources.html#{anchor}"

PROTECTED_PATTERNS = [
    re.compile(r'<a\b[^>]*>.*?</a>', re.DOTALL),
    re.compile(r'<code\b[^>]*>.*?</code>', re.DOTALL),
    re.compile(r'<pre\b[^>]*>.*?</pre>', re.DOTALL),
    re.compile(r'<script\b[^>]*>.*?</script>', re.DOTALL),
    re.compile(r'<style\b[^>]*>.*?</style>', re.DOTALL),
    re.compile(r'<!--.*?-->', re.DOTALL),
    re.compile(r'<svg\b[^>]*>.*?</svg>', re.DOTALL),   # entire SVG
    re.compile(r'<aside\b[^>]*class="module-toc"[^>]*>.*?</aside>', re.DOTALL),
    re.compile(r'<title\b[^>]*>.*?</title>', re.DOTALL),
    re.compile(r'<meta\b[^>]*>'),
    re.compile(r'<[^>]+>'),  # all HTML tag attributes
]

def build_mask(html: str):
    mask = [True] * len(html)
    for pat in PROTECTED_PATTERNS:
        for m in pat.finditer(html):
            for i in range(m.start(), m.end()):
                mask[i] = False
    return mask

def process_file(path: Path) -> int:
    text = path.read_text()
    mask = build_mask(text)
    consumed = []   # list of (start, end) already-chosen edits
    edits = []
    seen_anchors = set()

    def overlaps(a, b, c, d):
        return not (b <= c or d <= a)

    for anchor, name in TOOLS:
        if anchor in seen_anchors:
            continue
        pat = re.compile(r'(?<![\w.\-])' + re.escape(name) + r'(?![\w.\-])')
        for m in pat.finditer(text):
            s, e = m.start(), m.end()
            # Must be entirely in editable mask
            if not all(mask[i] for i in range(s, e)):
                continue
            # Must not overlap an already-chosen edit
            if any(overlaps(s, e, cs, ce) for cs, ce in consumed):
                continue
            edits.append((s, e, anchor, name))
            consumed.append((s, e))
            seen_anchors.add(anchor)
            break

    if not edits:
        return 0
    edits.sort(key=lambda x: -x[0])
    out = text
    for s, e, anchor, name in edits:
        url = res_url(path, anchor)
        rep = f'<a href="{url}" class="tool-link">{name}</a>'
        out = out[:s] + rep + out[e:]
    path.write_text(out)
    return len(edits)

total = 0
files_modified = 0
for path in sorted(ROOT.rglob('*.html')):
    rel = str(path.relative_to(ROOT))
    if rel == 'ressources.html': continue
    if rel.endswith('_template-etude-de-cas.html'): continue
    if 'site-web-prep' in rel or 'mockup' in rel or 'archives' in rel: continue
    n = process_file(path)
    if n > 0:
        files_modified += 1
        total += n
        print(f"{rel}: {n}")
print(f"\nTotal: {total} links across {files_modified} files")
