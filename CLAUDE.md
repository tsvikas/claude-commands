# claude-commands

`claude-commands.md` is a cheatsheet of Claude Code's built-in slash commands and keyboard shortcuts.
Line 4 of the sheet names the Claude Code version it reflects and that version's release date.
`claude-commands-outline.md` lists every command and key by section and group. `tools/outline.py` generates it from the sheet and `prek` runs it, so edit the sheet and never the outline.
`tools/page.py` generates a web page from the sheet; see "The web page" below.
`README.md` points a reader to the sheet, the page and the outline.
The root holds what a reader opens; the scripts that generate from the sheet live in `tools/`.

## Mission

Make Claude Code's day-to-day surface visible, so you learn what the tool can do and keep learning as new pieces ship almost weekly. Mostly it's read to learn; sometimes it's a reference while you work. The release-by-release history is the second way in: a diff of what's new that's worth learning.

What gets a line:

- **Complete:** every slash command, every key (except the ones every text box has), and every piece of message syntax. These are what you touch while working, and they expose the most UI.
- **Curated, a taste of the most useful:** surfaces too big to list in full, such as `claude` launch flags (`-c`, `-r`, `-w`, `-p`, `claude agents`, starting with a first request) and what you can ask Claude to do through its built-in tools (watch a log, remind you later, message another session).
- **One line and a pointer:** a mode with its own key set, such as vim mode ("turn it on with ...").
- **Linked, not listed:** what you set once and forget: settings, env vars, and subsystem internals like hooks and permissions.

Keep lines short so the whole sheet stays readable.

## What belongs in the sheet

The sheet covers what ships in the binary and that a user types, presses or asks for: slash commands, bundled skills, keyboard shortcuts, message syntax, and the curated tastes the mission names.

- A bundled skill belongs when the docs command table lists it. One the table omits is for Claude to load, and stays out.
- A setting stays out, and so does UI the screen already explains. An opt-in that unlocks something stays in.
- Behaviour tied to no command or key stays out, such as a time limit on background commands. A built-in tool you can ask Claude to use is a capability, not behaviour, and belongs in the mission's curated taste.
- Of the CLI, only the launch flags the mission names belong; "Beyond slash commands" links to the rest.
- Telemetry, gateway and enterprise administration, performance work, and changelog entries tagged `[VSCode]`, `[Claude Tag]` or cloud-session stay out. They go in the release commit's list of what was left out.
- A documented behaviour change that leaves a line still true goes in the commit body only.
- A command that behaves differently in two situations gets one line per situation, as `/resume` and `/verify` do.
- Context that is not a command goes as a plain sentence under its heading, above the bullets.
- Other names and keys for the same thing follow it, separated by `·`: `/cmd` · `/alias` · `Key`.
- Before the colon, parentheses hold only a condition on the name they follow: `Key` (on an empty prompt).
- After the colon, in the description, parentheses are free for an aside: `/clear`: start fresh (also starts a new session).
- A requirement, such as a plan, a mode or an opt-in, goes in parentheses at the end of the description: `/scroll-speed`: mouse wheel speed (fullscreen only).
- A description opens with a phrase that stands on its own, in about 70 characters or fewer. The web page shows that phrase and keeps the rest until the row is pressed.
  When more follows, end the phrase at a `;`, `:` or `.` that a space follows, or at an em dash with a space on each side: `/cd <path>`: move the session to a new working directory; its project config takes effect.
  A parenthesis that closes the phrase counts as the rest. One in the middle of it hides the break from the page, so put that aside after the break.
  Leave a longer phrase whole when a break would cut a single thought in two.
- The main name comes first, then its aliases, then keys. A key leads only when it is the usual way to do the thing, as `Esc Esc` is for rewinding.
- A chord or a repeated key is one code span with a space, as the keybindings file writes it: `Ctrl+X Ctrl+K`, `Esc Esc`.
- Write `Alt` for the Alt or Option key. The legend says once that it is `Option` on macOS.
- A line with an optional argument says what the bare command does only when that is something other than running with no input or opening a picker.
- Describe a command or key in the docs' own short words where they have them: the shortcut table, the keybindings actions table, the first sentence of a command's row.
- A description says what the thing does, not why it is useful or how it works inside.
- Name a command's options and mark the default, rather than giving an example.
- Before writing a line, find how the sheet already says that kind of thing and fit the pattern, such as "(fullscreen only)" for a requirement or "newer models" for a note about models.
- A long line that packs several cases is a candidate for one line per case. Suggest the split.
- A substantial addition gets its own line, stated as its gist, rather than a clause on an existing line.
- A key gets a line for each thing it does, in the section for that task. Most have one, or two next to each other; `Ctrl+C` has three, in three sections. When it does what a command does, it shares that command's line, after a `·`. A command's line may also name the key you press right after running it.
- Sections follow one task and then widen: set how Claude runs, write the prompt, watch it work, check the result; then the conversation and the sessions around it; then other kinds of work; then the project and the tool itself; last what is read once. Within a subsection, the most-used line comes first.
- Headings carry no numbers, so a section can move without changing any other heading or link.
- A line says how long an effect lasts (one message, this session, saved, out in the world) and its scope (user `~/.claude/` or project `.claude/`) wherever that is not obvious.

Before adding a command, read the "Deliberately not listed" comment at the end of the sheet.

## Refreshing the sheet

Work one release at a time, oldest first, from the version on line 4 to the newest release in the CHANGELOG.
A release is done when it has its own commit and line 4 names it.

No single source is complete, so each refresh reads all five:

1. The docs command table: `curl -sL https://code.claude.com/docs/en/commands.md`
   - Fetch it raw. A fetch-and-summarize tool silently drops and invents rows.

   - Diff the command names against the sheet:

     ```sh
     grep -oE '^\| `/[a-z-]+' commands.md | sed 's/| `//' | sort -u
     ```

   - Diff the signatures against the sheet's line for each command:

     ```sh
     grep -oE '^\| `/[a-z-]+[^`]*`' commands.md | sed 's/^| //'
     ```

     New arguments and subcommands reach the table without a CHANGELOG line.
     Subcommand tables live on other pages; `/claude-api`'s is in `skills.md`.

   - Diff the bundled skills, which the table marks **Skill** or **Workflow**, against the sheet:

     ```sh
     grep -E '\*\*\[(Skill|Workflow)\]' commands.md | grep -oE '^\| `/[a-z-]+' | sed 's/| `//'
     ```

   - A row's "Requires vX" clause is the birth date of a command.
     The CHANGELOG never mentioned `/radio`, `/list-agents` or `/peers` at all.
2. The CHANGELOG: <https://raw.githubusercontent.com/anthropics/claude-code/refs/heads/main/CHANGELOG.md>
   - The source for behaviour changes. Skip bullets starting with "Fixed"; they are about half of it.
   - It has no dates. Take them from the `<Update label="2.1.x" description="date">` tags in <https://code.claude.com/docs/en/changelog.md>.
3. The weekly digests: `https://code.claude.com/docs/en/whats-new/2026-wNN`
   - Good for why a change matters. They trail the releases by a few weeks, and some weeks are missing (there is no w31); the index at `/whats-new` lists the real ones.
4. The docs shortcut table: `curl -sL https://code.claude.com/docs/en/interactive-mode.md`
   - The source for every key in the sheet. Voice keys are in `voice-dictation.md`.
   - Check what each key does in each state: `Ctrl+C` interrupts, clears the input, or exits depending on what is running, and `Ctrl+B` backgrounds a task, not the session.
5. The installed binary: `readlink -f "$(which claude)"`
   - The tie-breaker when the docs and the CHANGELOG are vague: a command's usage string, which context a key is bound in, whether a skill is registered `userInvocable`.
   - It is about 240 MB. Search it with `/usr/bin/grep -a -o` and a short context, or with `bytes.find` in Python. Inside a Claude Code session plain `grep` is a wrapper that fails on it, and a regex with wide context times out.
   - It shows what this version does, not the documented workflow. When the two disagree, say so in the commit body.

## The web page

`tools/page.py` writes `_site/index.html` from the sheet, with `tools/page.css` and `tools/page.js` inlined. The Pages workflow runs it on every push to main.
To look at it, run `python3 tools/page.py` and open the file. `_site/` is not committed.
To look at a change on a phone before it is live, push it to the `staging` branch. The workflow publishes that branch under `/staging/` on the same site, with a bar that says so. When it is right, fast-forward main to it. The branch stays; between rounds it equals main.
It also writes `_site/badge.json` from line 4 of the sheet. The first badge in the README reads it, so that badge changes when the page is deployed, not when the README is edited. The second badge reads the latest Claude Code release from npm.
Change the look in `page.css` and the behaviour in `page.js`; the content comes only from the sheet.
The page counts its visits with GoatCounter, which sets no cookie and shows how many came, from which country and from which link, never who. The site's code is `GOATCOUNTER` in `page.py`, and the numbers are at `https://<code>.goatcounter.com`.
The staging copy counts too, under the path `/claude-commands/staging/`. A deployed copy is the only place to check the counter: GoatCounter ignores a page opened from a file or from localhost. To keep your own visits out, open the page once with `#toggle-goatcounter` at the end of its address, in each browser you use.

How a sheet line reaches the page:

- A row shows the names and the short part of the description, and a press opens the rest.
  The short part ends at the first `.`, `;` or `:` that a space follows, or the first em dash with a space on each side, outside code spans and parentheses. A parenthesis that closes the short part goes with the rest.
- A name that starts with a capital letter, an arrow, `?` or `\` is drawn as a key. Any other name is drawn as typed text.
- Arguments longer than 22 characters show as `[…]` until the row is opened.
- A sentence under a heading shows in full above the rows of that heading.
- The sections after the rule show as plain text, with nothing to open.

`page.py` stops with a message when it cannot read a line, and the workflow builds the page on every pull request, so such a line fails there.

## Commits

The git history is the sheet's changelog: one commit per release, in release order, including the quiet ones.

- `Update for 2.1.NNN`: something in the sheet changed.
- `Reviewed 2.1.NNN, nothing for the sheet`: only line 4 moves.

Release numbers skip. When the previous number was never released, the title says so: `Update for 2.1.257 (253-256 never released)`.

The body of a release commit has one bullet per change in that release that reached the sheet, in the changelog's own words where they fit, then everything deliberately left out, so a later pass can tell "not worth a line" from "missed it".
A change that belongs to no release gets its own commit, with a lowercase prefix for its kind:

- `meta:` instructions for maintaining the sheet: this file and the sheet's trailing comment. Also the tooling around the sheet: the scripts, the hooks, the workflow.
- `look:` how the web page looks: its colours, type, spacing and layout. What the page shows and how it is built is `meta:`.
- `tidy:` moving or rewording what the sheet already says.
- `add:` content the sheet never had.
- `fix:` correcting a line that is wrong.

The body of these says why, what was decided and what was left out. It does not list the lines changed or quote them before and after; the diff shows that.

One kind of change per commit. A release commit holds only what that release changed, and a `tidy:` that moves lines rewords nothing.
On a large change it can help to put the commits in order: release commits, then `tidy:`, then `fix:`, then `add:`. Suggest it then; it is not a rule.
An `add:` or a `fix:` holds one fact. Many facts of one kind found together, such as a set of missing keys, may share a commit.

Make each change its own commit, so it can be reviewed alone. Once it is approved, fold it into the commit it corrects or belongs with, so the branch ends with no line written and then rewritten. Ask before rewriting history that is already pushed.

An `add:` or `fix:` title ends with the release its content comes from, in parentheses, when that release is known: the release itself when it is later than 2.1.251, the version the sheet started from, and `pre 2.1.252` when it is earlier.

Run `prek run --all-files` before each commit; a fresh clone has no git hook installed.
It regenerates the outline and formats the Markdown. When it reports a file as modified, stage that file and run it again.
