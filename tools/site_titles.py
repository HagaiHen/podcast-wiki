"""Site build only: give each page its H1 as the frontmatter title and drop the H1, so Quartz
shows "LLM Evals" (not the slug "llm-evals") in <title>, link previews, and the page heading.

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


if __name__ == "__main__":
    if sys.argv[1] == "--selftest":
        assert retitle("---\ntype: concept\n---\n# LLM Evals\n\nBody") == '---\ntitle: "LLM Evals"\ntype: concept\n---\n\nBody'
        assert retitle("# Ingest log\nx") == '---\ntitle: "Ingest log"\n---\nx'
        assert retitle("---\ntitle: Podcast Wiki\n---\n# Index\n") == "---\ntitle: Podcast Wiki\n---\n# Index\n"
        assert retitle("no heading") == "no heading"
        print("selftest ok")
    else:
        for p in Path(sys.argv[1]).rglob("*.md"):
            p.write_text(retitle(p.read_text(encoding="utf-8")), encoding="utf-8")
