# claude-commands

`claude-commands.md` is a cheatsheet of Claude Code's built-in slash commands and keyboard shortcuts.
Line 4 of the sheet names the Claude Code version it reflects and that version's release date.

## What belongs in the sheet

The sheet covers what ships in the binary and that a user types or presses: slash commands, bundled skills, keyboard shortcuts.

- A bundled skill belongs when the docs command table lists it. One the table omits is for Claude to load, and stays out.
- A setting stays out. An opt-in that unlocks something stays in.
- Behaviour tied to no command or key stays out, such as a time limit on background commands.
- CLI flags and subcommands stay out; "Beyond slash commands" links to their reference.
- A command that behaves differently in two situations gets one line per situation, as `/resume` and `/verify` do.
- Context that is not a command goes as a plain sentence under its heading, above the bullets.
- Other names and keys for the same thing follow it, separated by `·`: `/cmd` · `/alias` · `Key`.
- Before the colon, parentheses hold only a condition on the name they follow: `Key` (on an empty prompt).
- After the colon, in the description, parentheses are free for an aside: `/clear`: start fresh (also starts a new session).
- A requirement, such as a plan, a mode or an opt-in, goes in parentheses at the end of the description: `/scroll-speed`: mouse wheel speed (fullscreen only).
- The main name comes first, then its aliases, then keys. A key leads only when it is the usual way to do the thing, as `Esc Esc` is for rewinding.
- A chord or a repeated key is one code span with a space, as the keybindings file writes it: `Ctrl+X Ctrl+K`, `Esc Esc`.
- Write `Alt` for the Alt or Option key. The legend says once that it is `Option` on macOS.
- A line with an optional argument says what the bare command does only when that is something other than running with no input or opening a picker.
- Describe a command or key in the docs' own short words where they have them: the shortcut table, the keybindings actions table, the first sentence of a command's row.
- Before writing a line, find how the sheet already says that kind of thing and fit the pattern, such as "(fullscreen only)" for a requirement or "newer models" for a note about models.
- A long line that packs several cases is a candidate for one line per case. Suggest the split.
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

## Commits

The git history is the sheet's changelog: one commit per release, in release order, including the quiet ones.

- `Update for 2.1.NNN`: something in the sheet changed.
- `Reviewed 2.1.NNN, nothing for the sheet`: only line 4 moves.

Release numbers skip. When the previous number was never released, the title says so: `Update for 2.1.257 (253-256 never released)`.

The body of a release commit has one bullet per change in that release that reached the sheet, in the changelog's own words where they fit, then everything deliberately left out, so a later pass can tell "not worth a line" from "missed it".
A change that belongs to no release gets its own commit, with a lowercase prefix for its kind:

- `meta:` instructions for maintaining the sheet: this file and the sheet's trailing comment.
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
