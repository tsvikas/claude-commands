"""Write claude-commands-outline.md: every command and key in the sheet, by section and group.

Run by prek whenever the sheet changes. The outline is generated; edit the sheet, not the outline.
"""

import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).parent.parent
SHEET = ROOT / "claude-commands.md"
OUTLINE = ROOT / "claude-commands-outline.md"

HEADER = """\
# Claude Code Commands and Shortcuts: Outline

Every command and key in [the cheatsheet](claude-commands.md), by section and group.
Generated from it by `tools/outline.py`; edit the sheet, not this file.
"""


def anchor(title):
    kept = re.sub(r"[^a-z0-9 \-_]", "", title.lower())
    return kept.replace(" ", "-")


def sections(text):
    """The sheet's sections, between "Where to look" and the rule that ends them."""
    lines = text.split("\n")
    start = lines.index("## Where to look")
    end = next(i for i, line in enumerate(lines) if line.startswith("____"))
    found = []
    for line in lines[start + 1 : end]:
        if line.startswith("## "):
            found.append((line[3:], [(None, [])]))
        elif line.startswith("### "):
            found[-1][1].append((line[4:], []))
        elif line.startswith("- ") and found:
            found[-1][1][-1][1].append(line[2:])
    if not found:
        raise SystemExit("outline.py: no sections found in the sheet")
    return found


def top_level(text, stop):
    """Split text at each `stop` that is outside a code span and outside parentheses."""
    parts, depth, in_code, last, i = [], 0, False, 0, 0
    while i < len(text):
        char = text[i]
        if char == "`":
            in_code = not in_code
        elif not in_code and char == "(":
            depth += 1
        elif not in_code and char == ")":
            depth -= 1
        elif not in_code and depth == 0 and text.startswith(stop, i):
            parts.append(text[last:i])
            last = i + len(stop)
            i = last
            continue
        i += 1
    parts.append(text[last:])
    return parts


def spans(text):
    """The code spans of text that are not inside parentheses."""
    found, depth, i = [], 0, 0
    while i < len(text):
        if text[i] == "`":
            end = text.index("`", i + 1)
            if depth == 0:
                found.append(text[i + 1 : end])
            i = end
        elif text[i] == "(":
            depth += 1
        elif text[i] == ")":
            depth -= 1
        i += 1
    return found


def short(span):
    """A name without its arguments: `/effort ultracode [on|off]` -> `/effort ultracode`."""
    kept = []
    for word in span.split(" "):
        if kept and word[0] in "[<":
            break
        kept.append(word)
    return " ".join(kept)


def condition(alternative):
    """The parenthesis that follows a name before the colon, or an empty string."""
    found = re.search(r"\(.*\)", alternative)
    return found.group(0) if found else ""


def names(line):
    """Split a line's part before the colon into its main name and its other names."""
    before_colon = top_level(line, ":")[0]
    alternatives = [a.strip() for a in top_level(before_colon, " · ")]
    main = alternatives[0]
    if not spans(main):
        raise SystemExit(f"outline.py: no name found in: {line[:60]}")
    return main, alternatives[1:]


def entries(found):
    parsed = [names(line) for _, groups in found for _, lines in groups for line in lines]
    key = lambda main: tuple(short(s) for s in spans(main))
    count = Counter(key(main) for main, _ in parsed)
    full = Counter(tuple(spans(main)) for main, _ in parsed)
    result = {}
    for main, others in parsed:
        shown = spans(main) if count[key(main)] > 1 else list(key(main))
        text = " / ".join(f"`{s}`" for s in shown)
        if full[tuple(spans(main))] > 1 and condition(main):
            text += " " + condition(main)
        # a key that leads a line is followed by the command it stands for
        if not shown[0].startswith("/"):
            command = next((short(spans(o)[0]) for o in others if spans(o) and spans(o)[0].startswith("/")), None)
            if command:
                text += f" · `{command}`"
        result[main] = text
    return result


def render(found):
    shown = entries(found)
    out = [HEADER]
    for title, groups in found:
        out += [f"## [{title}](claude-commands.md#{anchor(title)})", ""]
        for group, lines in groups:
            if not lines:
                continue
            listed = ", ".join(shown[names(line)[0]] for line in lines)
            out.append(f"- **{group}:** {listed}" if group else f"- {listed}")
        out.append("")
    return "\n".join(out)


if __name__ == "__main__":
    OUTLINE.write_text(render(sections(SHEET.read_text())))
