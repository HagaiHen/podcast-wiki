"""Mechanical health checks for wiki/. Prints one issue per line; exit 1 if any.

  uv run tools/lint_wiki.py             # lint the repo's wiki
  uv run tools/lint_wiki.py --selftest
"""
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")
CONCEPT_SECTIONS = ["**Summary:**", "## Key ideas", "## Disagreements & open questions", "## Takeaways", "## Related"]
HUB_MIN = 5


def field(text, name):
    m = re.search(rf"^{name}:\s*(.*)$", text, re.M)
    return m.group(1).strip().strip('"') if m else None


def lint(root):
    wiki = root / "wiki"
    pages = {p.relative_to(wiki).with_suffix("").as_posix(): p.read_text() for p in wiki.rglob("*.md")
             if ".obsidian" not in p.parts}
    issues = []
    inbound = Counter()
    for name, text in pages.items():
        for target in set(LINK.findall(text)):
            if target not in pages:
                issues.append(f"broken-link {name} -> {target}")
            elif name != "index":
                inbound[target] += 1
    index = pages.get("index", "")
    for name in pages:
        if name.split("/")[0] in {"concepts", "people", "shows", "episodes", "hubs"} and f"[[{name}]]" not in index:
            issues.append(f"not-in-index {name}")
    hub_counts = Counter()
    for name, text in pages.items():
        kind = name.split("/")[0]
        if kind == "concepts":
            if not inbound[name]:
                issues.append(f"orphan {name}")
            for s in CONCEPT_SECTIONS:
                if s not in text:
                    issues.append(f"missing-section {name}: {s}")
            eps = {t for t in LINK.findall(text) if t.startswith("episodes/")}
            declared = field(text, "sources")
            if declared and declared.isdigit() and int(declared) != len(eps):
                issues.append(f"sources-mismatch {name}: says {declared}, links {len(eps)} episodes")
            hubs = re.findall(r"[\w-]+", field(text, "hubs") or "")
            if not hubs:
                issues.append(f"no-hub {name}")
            hub_counts.update(hubs)
        elif kind == "episodes":
            raw = field(text, "raw")
            raw_path = root / raw if raw else None
            if not raw_path or not raw_path.exists():
                issues.append(f"missing-raw {name}: {raw}")
            elif field(text, "spotify_url") != field(raw_path.read_text(), "spotify_url"):
                issues.append(f"url-mismatch {name}")
    for hub, n in sorted(hub_counts.items()):
        if n >= HUB_MIN and f"hubs/{hub}" not in pages:
            issues.append(f"needs-hub {hub}: {n} concepts")
    return issues


def selftest():
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        (root / "raw").mkdir()
        (root / "raw/a.md").write_text('---\nspotify_url: "u1"\n---\n')
        w = root / "wiki"
        for sub in ("concepts", "episodes"):
            (w / sub).mkdir(parents=True)
        (w / "episodes/e.md").write_text("---\nraw: raw/a.md\nspotify_url: u2\n---\n[[concepts/c]]")
        (w / "concepts/c.md").write_text("---\nhubs: [health]\nsources: 2\n---\n**Summary:** x\n## Key ideas\n- y ([[episodes/e]])\n"
                                         "## Disagreements & open questions\n## Takeaways\n## Related\n[[concepts/gone]]")
        (w / "concepts/lone.md").write_text("---\nhubs: []\nsources: 0\n---\n**Summary:** x")
        (w / "index.md").write_text("[[concepts/c]] [[episodes/e]]")
        got = set(lint(root))
    want = {"broken-link concepts/c -> concepts/gone", "not-in-index concepts/lone", "orphan concepts/lone",
            "no-hub concepts/lone", "url-mismatch episodes/e", "sources-mismatch concepts/c: says 2, links 1 episodes"}
    assert want <= got, want - got
    assert not any(i.startswith("orphan concepts/c") for i in got), got
    assert sum(i.startswith("missing-section concepts/lone") for i in got) == 4, got
    print("selftest ok")


if __name__ == "__main__":
    if sys.argv[1:] == ["--selftest"]:
        selftest()
    else:
        found = lint(ROOT)
        print("\n".join(found) or "clean")
        sys.exit(1 if found else 0)
