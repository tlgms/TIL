"""Notion TIL page -> markdown files.

Convention: on the root TIL page, each callout with a 📁 emoji icon is a
folder (anywhere on the page, including columns). A 📁 callout nested in
another 📁 callout is a subfolder. Pages inside a callout become
<folder>/.../<title>.md. Notion-hosted images/files are downloaded to
assets/ with stable names (block id) so re-runs produce no diff.
Only 📁 folders and assets/ are managed; other repo files are untouched.
"""
import json
import os
import re
import shutil
import sys
import urllib.parse
import urllib.request
from pathlib import Path

TOKEN = os.environ["NOTION_TOKEN"]
ROOT_PAGE = "39f2cdd741ac81269110e55addbc9396"
REPO_DIR = Path(__file__).resolve().parents[1]
ASSETS_DIR = REPO_DIR / "assets"
FOLDER_EMOJI = "\U0001F4C1"
USED_ASSETS = set()


def api(path, payload=None):
    req = urllib.request.Request(
        "https://api.notion.com/v1" + path,
        data=json.dumps(payload).encode() if payload is not None else None,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json",
        },
        method="POST" if payload is not None else "GET",
    )
    with urllib.request.urlopen(req) as r:
        return json.load(r)


def children(block_id):
    results, cursor = [], None
    while True:
        q = f"/blocks/{block_id}/children?page_size=100"
        if cursor:
            q += f"&start_cursor={cursor}"
        data = api(q)
        results += data["results"]
        if not data.get("has_more"):
            break
        cursor = data["next_cursor"]
    return results


def rt(rich):
    out = ""
    for t in rich:
        s = t.get("plain_text", "")
        a = t.get("annotations", {})
        if a.get("code"):
            s = f"`{s}`"
        if a.get("bold"):
            s = f"**{s}**"
        if a.get("italic"):
            s = f"*{s}*"
        if a.get("strikethrough"):
            s = f"~~{s}~~"
        href = t.get("href")
        if href and "notion" not in (href or ""):
            s = f"[{s}]({href})"
        out += s
    return out


def is_notion_hosted(url):
    return "X-Amz-" in url or "notion-static" in url or "prod-files-secure" in url


def asset_url(url, block_id, out_dir):
    """Download a Notion-hosted file once, return a stable relative path."""
    if not url:
        return url
    if not is_notion_hosted(url):
        return url
    ext = Path(urllib.parse.urlparse(url).path).suffix or ".bin"
    name = block_id.replace("-", "") + ext.lower()
    target = ASSETS_DIR / name
    USED_ASSETS.add(name)
    if not target.exists():
        try:
            ASSETS_DIR.mkdir(exist_ok=True)
            with urllib.request.urlopen(url) as r:
                target.write_bytes(r.read())
        except Exception:
            return url
    rel = os.path.relpath(target, out_dir)
    return urllib.parse.quote(rel.replace(os.sep, "/"))


def block_md(b, indent=0, out_dir=REPO_DIR):
    t = b["type"]
    d = b.get(t, {})
    pre = "  " * indent
    rich = d.get("rich_text", [])
    txt = rt(rich)
    lines = []
    if t == "paragraph":
        if txt:
            lines.append(pre + txt)
    elif t in ("heading_1", "heading_2", "heading_3"):
        lines.append(pre + "#" * int(t[-1]) + " " + txt)
    elif t == "bulleted_list_item":
        lines.append(pre + "- " + txt)
    elif t == "numbered_list_item":
        lines.append(pre + "1. " + txt)
    elif t == "to_do":
        box = "[x]" if d.get("checked") else "[ ]"
        lines.append(pre + "- " + box + " " + txt)
    elif t == "code":
        lang = d.get("language", "")
        code = "".join(x.get("plain_text", "") for x in rich)
        lines.append(f"```{lang}\n{code}\n```")
    elif t in ("quote", "callout"):
        lines.append(pre + "> " + txt)
    elif t == "divider":
        lines.append("---")
    elif t == "image":
        url = d.get("file", {}).get("url") or d.get("external", {}).get("url", "")
        lines.append(f"![image]({asset_url(url, b['id'], out_dir)})")
    elif t in ("bookmark", "embed", "link_preview"):
        url = d.get("url", "")
        cap = rt(d.get("caption", []))
        if url:
            lines.append(pre + f"[{cap or url}]({url})")
    elif t in ("file", "pdf", "video"):
        url = d.get("file", {}).get("url") or d.get("external", {}).get("url", "")
        cap = rt(d.get("caption", []))
        if url:
            lines.append(pre + f"[{cap or url}]({asset_url(url, b['id'], out_dir)})")
    elif t == "child_database":
        lines += database_md(b["id"])
    elif t == "child_page":
        lines.append(pre + "## " + b["child_page"].get("title", "Untitled"))
        for c in children(b["id"]):
            lines += block_md(c, indent, out_dir)
        return lines
    elif txt:
        lines.append(pre + txt)
    if b.get("has_children") and t not in ("code", "child_page"):
        for c in children(b["id"]):
            lines += block_md(c, indent + 1, out_dir)
    return lines


def database_md(db_id):
    try:
        db = api(f"/databases/{db_id}")
    except Exception:
        return []
    props = db.get("properties", {})
    names = [n for n, p in props.items() if p["type"] == "title"]
    names += sorted(n for n, p in props.items() if p["type"] != "title")
    rows, cursor = [], None
    while True:
        payload = {"page_size": 100}
        if cursor:
            payload["start_cursor"] = cursor
        data = api(f"/databases/{db_id}/query", payload)
        rows += data["results"]
        if not data.get("has_more"):
            break
        cursor = data["next_cursor"]

    def cell(p):
        t = p.get("type", "")
        v = p.get(t)
        if t in ("title", "rich_text"):
            return rt(v or [])
        if t == "select":
            return (v or {}).get("name", "")
        if t == "multi_select":
            return ", ".join(x.get("name", "") for x in (v or []))
        if t == "number":
            return "" if v is None else str(v)
        if t == "checkbox":
            return "O" if v else ""
        if t == "date":
            return (v or {}).get("start", "") or ""
        if t == "url":
            return v or ""
        return ""

    lines = []
    dbtitle = rt(db.get("title", []))
    if dbtitle:
        lines.append(f"**{dbtitle}**")
    lines.append("| " + " | ".join(names) + " |")
    lines.append("|" + "---|" * len(names))
    for r in rows:
        cells = []
        for n in names:
            c = cell(r.get("properties", {}).get(n, {}))
            cells.append(c.replace("|", "\\|").replace("\n", " "))
        lines.append("| " + " | ".join(cells) + " |")
    return lines


def page_title(pid):
    p = api(f"/pages/{pid}")
    for prop in p["properties"].values():
        if prop["type"] == "title":
            return "".join(t.get("plain_text", "") for t in prop["title"]) or "Untitled"
    return "Untitled"


def page_md(pid, title, out_dir):
    body = []
    for b in children(pid):
        md = block_md(b, 0, out_dir)
        if md:
            body += md + [""]
    return (
        f"<!-- notion-page-id: {pid} -->\n\n# {title}\n\n"
        + "\n".join(body).strip()
        + "\n"
    )


def sanitize(name):
    return re.sub(r'[\\/:*?"<>|]', "-", name).strip() or "Untitled"


def is_folder_callout(b):
    if b.get("type") != "callout":
        return False
    icon = b["callout"].get("icon") or {}
    return icon.get("type") == "emoji" and icon.get("emoji") == FOLDER_EMOJI


def callout_name(b):
    plain = "".join(t.get("plain_text", "") for t in b["callout"].get("rich_text", []))
    if not plain.strip():
        return ""
    return sanitize(plain.strip().splitlines()[0].strip())


def collect_page_ids(blocks):
    ids = {}
    for k in blocks:
        if k["type"] == "child_page":
            ids[k["id"].replace("-", "")] = k["child_page"]["title"]
            continue
        d = k.get(k["type"], {})
        for t in d.get("rich_text", []):
            href = (t.get("href") or "").replace("-", "")
            m = re.search(r"([0-9a-f]{32})", href)
            if m:
                ids.setdefault(m.group(1), None)
            if t.get("type") == "mention" and t.get("mention", {}).get("type") == "page":
                ids.setdefault(t["mention"]["page"]["id"].replace("-", ""), None)
    return ids


def walk(blocks, prefix, out):
    """Find 📁 callouts anywhere (columns, toggles, nested callouts)."""
    for b in blocks:
        if is_folder_callout(b):
            name = callout_name(b)
            if not name:
                continue
            path = prefix + [name]
            kids = children(b["id"]) if b.get("has_children") else []
            out.append((path, collect_page_ids([k for k in kids if not is_folder_callout(k)])))
            walk([k for k in kids if is_folder_callout(k)], path, out)
        elif b["type"] == "child_page":
            continue
        elif b.get("has_children"):
            walk(children(b["id"]), prefix, out)


def main():
    folders = []
    walk(children(ROOT_PAGE), [], folders)
    for top in {p[0] for p, _ in folders}:
        target = REPO_DIR / top
        if target.exists():
            shutil.rmtree(target)
    changed = []
    for path, ids in folders:
        out_dir = REPO_DIR.joinpath(*path)
        out_dir.mkdir(parents=True, exist_ok=True)
        for pid, title in ids.items():
            title = title or page_title(pid)
            f = out_dir / (sanitize(title) + ".md")
            f.write_text(page_md(pid, title, out_dir), encoding="utf-8")
            changed.append(str(f.relative_to(REPO_DIR)))
    if ASSETS_DIR.exists():
        for f in ASSETS_DIR.iterdir():
            if f.is_file() and re.fullmatch(r"[0-9a-f]{32}\.\w+", f.name) and f.name not in USED_ASSETS:
                f.unlink()
        if not any(ASSETS_DIR.iterdir()):
            ASSETS_DIR.rmdir()
    print(f"Folders: {[' / '.join(p) for p, _ in folders]}")
    print("Synced files:")
    for c in changed:
        print(" -", c)


if __name__ == "__main__":
    sys.exit(main())
