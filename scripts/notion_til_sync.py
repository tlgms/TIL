"""Notion TIL page -> markdown files.

Convention: on the root TIL page, each callout with a 📁 emoji icon is a
folder (wherever it is — inside columns too). A 📁 callout nested in
another 📁 callout is a subfolder. Pages inside a callout (nested child
pages or links to Notion pages) become <folder>/.../<title>.md.
Only 📁 folders are managed; other files in the repo are never touched.
"""
import json
import os
import re
import shutil
import sys
import urllib.request
from pathlib import Path

TOKEN = os.environ["NOTION_TOKEN"]
ROOT_PAGE = "39f2cdd741ac81269110e55addbc9396"
REPO_DIR = Path(__file__).resolve().parents[1]
FOLDER_EMOJI = "\U0001F4C1"


def api(path):
    req = urllib.request.Request(
        "https://api.notion.com/v1" + path,
        headers={"Authorization": f"Bearer {TOKEN}", "Notion-Version": "2022-06-28"},
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


def block_md(b, indent=0):
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
        lines.append(f"![image]({url})")
    elif t == "child_page":
        return []
    elif txt:
        lines.append(pre + txt)
    if b.get("has_children") and t not in ("code", "child_page"):
        for c in children(b["id"]):
            lines += block_md(c, indent + 1)
    return lines


def page_title(pid):
    p = api(f"/pages/{pid}")
    for prop in p["properties"].values():
        if prop["type"] == "title":
            return "".join(t.get("plain_text", "") for t in prop["title"]) or "Untitled"
    return "Untitled"


def page_md(pid, title):
    body = []
    for b in children(pid):
        md = block_md(b)
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
            f.write_text(page_md(pid, title), encoding="utf-8")
            changed.append(str(f.relative_to(REPO_DIR)))
    print(f"Folders: {[' / '.join(p) for p, _ in folders]}")
    print("Synced files:")
    for c in changed:
        print(" -", c)


if __name__ == "__main__":
    sys.exit(main())
