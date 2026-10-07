"""Write _site/index.html: the sheet as a web page, one card per section.

Run by the Pages workflow on every push to main or staging, and by hand to look at the result.
The page is generated; edit the sheet, `page.css` or `page.js`, not the page.
Beside it goes _site/badge.json, which the README's badge reads for the sheet's version and date.
With `--staging` the page says it is the staging copy and asks search engines to skip it.
Both copies count their visits with GoatCounter.
Beside it too goes _site/card.png, the picture a pasted link to the page shows.
"""

import html
import json
import re
import shutil
import sys
from pathlib import Path
from string import Template

from outline import SHEET, anchor, short, spans, top_level

HERE = Path(__file__).parent
PAGE = HERE.parent / "_site" / "index.html"
BADGE = PAGE.parent / "badge.json"
REPO = "https://github.com/tsvikas/claude-commands"
# where the page is served; a link preview needs whole addresses, and the staging copy adds staging/
SITE = "https://tsvikas.github.io/claude-commands/"
# a screenshot of card.html, copied beside the page
CARD = HERE / "card.png"
# the GoatCounter site that counts visits; it sets no cookie and keeps nothing that identifies a visitor
GOATCOUNTER = "tsvikas"

# a description is cut at the first of these, and the page shows the rest only on request
BREAKS = [". ", "; ", ": ", " — "]
# arguments longer than this show as […] until the row is opened
LONG_ARGUMENTS = 22
SYMBOLS = {"⚡": ("bolt", "costs tokens"), "☁": ("cloud", "runs in the cloud")}
# a name that starts with a capital or one of these is a key; anything else is typed
KEY_STARTS = "←→↑↓?\\"

TEMPLATE = Template("""\
<!doctype html>
<html lang="en" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>$title</title>
<meta name="description" content="$intro">$robots
<link rel="canonical" href="$url">
<meta property="og:type" content="website">
<meta property="og:title" content="$title">
<meta property="og:description" content="$intro">
<meta property="og:url" content="$url">
<meta property="og:image" content="$url$card">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="$title: two sections of the page, each a list of commands and keys">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&amp;family=IBM+Plex+Sans:wght@400;500;600;700&amp;display=swap">
<style>
$css</style>
<script>try{const t=localStorage.getItem("theme");if(t)document.documentElement.dataset.theme=t}catch{}</script>
</head>
<body>$banner
<svg class="sprite" aria-hidden="true">
<symbol id="bolt" viewBox="0 0 24 24"><path d="M13 2 4 14h7l-1 8 9-12h-7l1-8z"/></symbol>
<symbol id="cloud" viewBox="0 0 24 24"><path d="M17.5 19a4.5 4.5 0 0 0 .5-8.97A6 6 0 0 0 6.34 11.5 3.75 3.75 0 0 0 7 19h10.5z"/></symbol>
<symbol id="sun" viewBox="0 0 24 24"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></symbol>
<symbol id="moon" viewBox="0 0 24 24"><path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z"/></symbol>
</svg>
<div class="page">
<header class="top">
<div class="brand">
<h1>$title</h1>
<p>v$version · $date</p>
</div>
<button id="theme" class="theme" type="button" role="switch" aria-checked="false" aria-label="Dark theme"><svg class="i"><use href="#sun"/></svg><svg class="i"><use href="#moon"/></svg></button>
<label class="filter">Filter <input id="q" type="search" placeholder="a command, a key, or a word" autocomplete="off"></label>
<button id="all" class="ghost" type="button" aria-pressed="false">Expand all details</button>
<ul class="legend">
<li><svg class="i"><use href="#bolt"/></svg> costs tokens</li>
<li><svg class="i"><use href="#cloud"/></svg> runs in the cloud</li>
<li><span class="name key">Key</span> a key, not a command</li>
<li><code>&lt;arg&gt;</code> required, <code>[arg]</code> optional</li>
<li><span class="name key">Alt</span> is Option on macOS</li>
</ul>
</header>
<main id="board">
$cards
</main>
<p id="empty" hidden>No command or key matches that.</p>
<div class="extras">
$prose
</div>
<footer>
Generated from <a href="$repo/blob/main/claude-commands.md">claude-commands.md</a> ·
<a href="$repo">source on GitHub</a> ·
canonical list: <a href="$canonical">$canonical</a>
</footer>
</div>
<script>
$js</script>
<script data-goatcounter="https://$goatcounter.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>
</body>
</html>
""")


def sections(lines):
    """Each `##` section as (title, groups). A group is (label, sentences, bullets); the first has no label."""
    found = []
    for line in lines:
        if line.startswith("## "):
            found.append((line[3:], [(None, [], [])]))
        elif line.startswith("### "):
            found[-1][1].append((line[4:], [], []))
        elif line.startswith("- ") and found:
            found[-1][1][-1][2].append(line[2:])
        elif line.strip() and found:
            found[-1][1][-1][1].append(line)
    return found


def sheet(text):
    """The sheet as its lines above "Where to look", its task sections, and the prose sections after the rule."""
    lines = text.split("\n")
    start = lines.index("## Where to look")
    rule = next(i for i, line in enumerate(lines) if line.startswith("____"))
    end = next((i for i, line in enumerate(lines) if line.startswith("<!--")), len(lines))
    tasks = sections(lines[start:rule])[1:]
    if not tasks:
        raise SystemExit("page.py: no sections found in the sheet")
    return lines[:start], tasks, sections(lines[rule + 1 : end])


def inline(text):
    """Markdown inline text as HTML: code spans, *emphasis*, <links> and [text](links)."""
    out = []
    for i, part in enumerate(text.split("`")):
        part = html.escape(part)
        if i % 2:
            out.append(f"<code>{part}</code>")
            continue
        part = re.sub(r"&lt;(https?://\S+?)&gt;", r'<a href="\1">\1</a>', part)
        part = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r'<a href="\2">\1</a>', part)
        out.append(re.sub(r"\*([^*]+)\*", r"<em>\1</em>", part))
    return "".join(out)


def cut(desc):
    """Where the short part of a description ends.

    At its first break outside code and parentheses, then back over a parenthesis that closes
    the short part: `start fresh (also starts a new session)` is cut before the parenthesis.
    """
    ends = [len(parts[0]) for stop in BREAKS if len(parts := top_level(desc, stop)) > 1]
    end = min(ends, default=len(desc))
    aside = re.search(r" \([^()]*\)$", desc[:end])
    return aside.start() if aside else end


def name(alternative):
    """One name before the colon as (name, arguments, condition, whether it is a key)."""
    label = top_level(alternative, " (")[0]
    found = spans(label)
    if not found or (len(label) < len(alternative) and not alternative.endswith(")")):
        raise SystemExit(f"page.py: cannot read the name in: {alternative[:60]}")
    text = label.replace("`", "")
    bare = short(found[0]) if len(found) == 1 else text
    is_key = text[0].isupper() or text[0] in KEY_STARTS
    return bare, text[len(bare) :].strip(), alternative[len(label) + 2 : -1], is_key


def entry(line):
    """A bullet as its alternatives, its symbols and its description."""
    parts = top_level(line, ": ")
    if len(parts) < 2:
        raise SystemExit(f"page.py: no description in: {line[:60]}")
    symbols = [SYMBOLS[s] for s in SYMBOLS if s in parts[0]]
    head = re.sub("[⚡☁️]", "", parts[0]).strip()
    return [a.strip() for a in top_level(head, " · ")], symbols, ": ".join(parts[1:])


def row(line):
    """A bullet as one run of text: names, then the short part, then the rest for when it is opened."""
    alternatives, symbols, desc = entry(line)
    (bare, args, cond, is_key), others = name(alternatives[0]), [name(a) for a in alternatives[1:]]
    end = cut(desc)
    long_args = len(args) > LONG_ARGUMENTS
    can_open = bool(desc[end:]) or long_args or any(other[2] for other in others)
    key = " key" if is_key else ""

    side = [f'<svg class="i" role="img" aria-label="{label}"><use href="#{icon}"/></svg>' for icon, label in symbols]
    side.append('<span class="mark" aria-hidden="true"></span>')
    if can_open:
        text = [f'<button class="name{key}" type="button" aria-expanded="false">{html.escape(bare)}</button>']
    else:
        text = [f'<span class="name{key}">{html.escape(bare)}</span>']
    if long_args:
        text.append(f'<span class="args"><span class="less">[…]</span><span class="more">{html.escape(args)}</span></span>')
    elif args:
        text.append(f'<span class="args">{html.escape(args)}</span>')
    if cond:
        text.append(f'<span class="cond">({inline(cond)})</span>')
    for other, other_args, other_cond, other_is_key in others:
        shown = html.escape(f"{other} {other_args}".strip())
        text.append(f'<span class="alt{" key" if other_is_key else ""}">{shown}</span>')
        if other_cond:
            text.append(f'<span class="cond more">({inline(other_cond)})</span>')
    rest = f'<span class="rest">{inline(desc[end:])}</span>' if desc[end:] else ""
    text.append(f'<span class="short">{inline(desc[:end])}</span>{rest}')

    # the tooltip repeats the whole line, for a look without opening it
    tip = [f'<div class="use"><b>{html.escape(bare)}</b> {html.escape(args)}</div>']
    if cond:
        tip.append(f'<div class="dim">when: {inline(cond)}</div>')
    if others:
        tip.append(f'<div class="dim">also: {inline(" · ".join(alternatives[1:]))}</div>')
    tip.append(f"<p>{inline(desc)}</p>")
    if symbols:
        tip.append(f'<div class="dim">{" · ".join(label for _, label in symbols)}</div>')

    searchable = html.escape(re.sub("[`*]", "", line).lower())
    return (
        f'<div class="row{" can" if can_open else ""}" data-text="{searchable}">'
        f'<span class="side">{"".join(side)}</span>{" ".join(text)}'
        f'<div class="tip" aria-hidden="true">{"".join(tip)}</div></div>'
    )


def note(sentences):
    return f'<p class="note">{inline(" ".join(sentences))}</p>'


def card(title, groups):
    """A task section: its sentences, then each group of rows under its label."""
    out = [f'<section class="sec" id="{anchor(title)}">', f"<h2>{inline(title)}</h2>"]
    for label, sentences, bullets in groups:
        if label is None and sentences:
            out.append(note(sentences))
        if not bullets:
            continue
        out.append('<div class="grp">')
        if label:
            out.append(f"<h3>{inline(label)}</h3>")
            if sentences:
                out.append(note(sentences))
        out += [row(bullet) for bullet in bullets]
        out.append("</div>")
    return "\n".join(out + ["</section>"])


def prose(title, groups):
    """A section after the rule: paragraphs and plain bullets, nothing to open."""
    out = [f'<section class="sec prose" id="{anchor(title)}">', f"<h2>{inline(title)}</h2>"]
    for _, sentences, bullets in groups:
        if sentences:
            out.append(f"<p>{inline(' '.join(sentences))}</p>")
        if bullets:
            out.append("<ul>" + "".join(f"<li>{inline(bullet)}</li>" for bullet in bullets) + "</ul>")
    return "\n".join(out + ["</section>"])


def snapshot(top):
    """The version, its date and the canonical link that the sheet names above "Where to look"."""
    found = re.search(r"v([\d.]+) \((\d{4}-\d\d-\d\d)\).*<(\S+)>", "\n".join(top))
    if not found:
        raise SystemExit("page.py: no version, date and canonical link above \"Where to look\"")
    return found.groups()


def badge(text):
    """What the README's badge shows, in the shape shields.io's endpoint badge reads."""
    version, date, _ = snapshot(sheet(text)[0])
    # not blue, the colour of the npm badge beside it, and not green or amber, which would read as a verdict
    return json.dumps({"schemaVersion": 1, "label": "updated for", "message": f"v{version} · {date}", "color": "blueviolet"})


STAGING_ROBOTS = '\n<meta name="robots" content="noindex">'
STAGING_BANNER = '\n<p class="staging">Staging copy, for checking a change before it is live. <a href="../">The live page</a></p>'


def render(text, staging=False):
    top, tasks, after = sheet(text)
    version, date, canonical = snapshot(top)
    return TEMPLATE.substitute(
        robots=STAGING_ROBOTS if staging else "",
        banner=STAGING_BANNER if staging else "",
        title=html.escape(top[0].removeprefix("# ")),
        intro=html.escape(top[2]),
        url=SITE + ("staging/" if staging else ""),
        card=CARD.name,
        version=version,
        date=date,
        canonical=html.escape(canonical),
        repo=REPO,
        goatcounter=GOATCOUNTER,
        css=(HERE / "page.css").read_text(),
        js=(HERE / "page.js").read_text(),
        cards="\n".join(card(title, groups) for title, groups in tasks),
        prose="\n".join(prose(title, groups) for title, groups in after),
    )


if __name__ == "__main__":
    PAGE.parent.mkdir(exist_ok=True)
    PAGE.write_text(render(SHEET.read_text(), staging="--staging" in sys.argv[1:]))
    BADGE.write_text(badge(SHEET.read_text()))
    shutil.copy(CARD, PAGE.parent)
