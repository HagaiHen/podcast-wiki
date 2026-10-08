"""Site build only: give each page its H1 as the frontmatter title and drop the H1, so Quartz
shows "LLM Evals" (not the slug "llm-evals") in <title>, link previews, and the page heading.
Also give concept/hub pages a clean ~155-char description from their **Summary:** line, so
search results and link previews don't start with "Summary:".

  python3 tools/site_titles.py <content-dir>
  python3 tools/site_titles.py --selftest
"""
import re
import sys
from pathlib import Path


def retitle(text):
    m = re.match(r"(---\n.*?\n---\n)(.*)", text, re.S)
    front, body = (m.group(1), m.group(2)) if m else ("", text)
    if re.search(r"^title:", front, re.M):
        return text
    h1 = re.search(r"^# (.+)\n?", body, re.M)
    if not h1:
        return text
    title = h1.group(1).strip().replace('"', '\\"')
    body = body[:h1.start()] + body[h1.end():]
    front = front.replace("---\n", f'---\ntitle: "{title}"\n', 1) if front else f'---\ntitle: "{title}"\n---\n'
    return front + body


def plain(md):
    md = re.sub(r"\[\[[^]|]*\|([^]]+)\]\]", r"\1", md)  # [[a|b]] -> b
    md = re.sub(r"\[\[(?:[^]]*/)?([^]/]+)\]\]", lambda m: m.group(1).replace("-", " "), md)  # [[x/y-z]] -> y z
    md = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", md)  # [t](u) -> t
    return re.sub(r"\s+", " ", md.replace("**", "").replace("*", "").replace("`", "")).strip()


def shorten(text, limit=155):
    out = ""
    for sentence in re.findall(r"[^.!?]+[.!?]+(?:\s|$)|[^.!?]+$", text):
        if len(out) + len(sentence) > limit:
            break
        out += sentence
    if not out:  # ponytail: first sentence alone is too long; cut at a word
        out = text[:limit].rsplit(" ", 1)[0].rstrip(",;:") + "…"
    return out.strip()


def describe(text):
    m = re.match(r"(---\n.*?\n---\n)(.*)", text, re.S)
    if not m or re.search(r"^description:", m.group(1), re.M):
        return text
    summary = re.search(r"^\*\*Summary:\*\*\s*(.+)$", m.group(2), re.M)
    if not summary:
        return text
    desc = shorten(plain(summary.group(1))).replace('"', '\\"')
    return m.group(1).replace("---\n", f'---\ndescription: "{desc}"\n', 1) + m.group(2)


if __name__ == "__main__":
    if sys.argv[1] == "--selftest":
        assert retitle("---\ntype: concept\n---\n# LLM Evals\n\nBody") == '---\ntitle: "LLM Evals"\ntype: concept\n---\n\nBody'
        assert retitle("# Ingest log\nx") == '---\ntitle: "Ingest log"\n---\nx'
        assert retitle("---\ntitle: Podcast Wiki\n---\n# Index\n") == "---\ntitle: Podcast Wiki\n---\n# Index\n"
        assert retitle("no heading") == "no heading"
        page = '---\ntype: concept\n---\n**Summary:** How you know an *AI feature* works. Uses [[concepts/llm-evals|evals]] and [[people/x-y]]. ' + "More. " * 40
        d = re.search(r'description: "(.*)"', describe(page)).group(1)
        assert d.startswith("How you know an AI feature works. Uses evals and x y.") and len(d) <= 155 and "Summary" not in d, d
        assert len(shorten("word " * 80)) <= 156 and shorten("word " * 80).endswith("…")
        assert describe("---\ndescription: keep\n---\n**Summary:** x.") == "---\ndescription: keep\n---\n**Summary:** x."
        print("selftest ok")
    else:
        for p in Path(sys.argv[1]).rglob("*.md"):
            p.write_text(describe(retitle(p.read_text(encoding="utf-8"))), encoding="utf-8")
