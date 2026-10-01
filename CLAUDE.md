# claude-commands

`claude-commands.md` is a cheatsheet of Claude Code's built-in slash commands and keyboard shortcuts.
Line 4 of the sheet names the Claude Code version it reflects.

## Refreshing the sheet

Work one release at a time, oldest first, from the version on line 4 to the newest release in the CHANGELOG.
A release is done when it has its own commit and line 4 names it.

No single source is complete, so each refresh reads all four:

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

   - A row's "Requires vX" clause is the birth date of a command.
     The CHANGELOG never mentioned `/radio`, `/list-agents` or `/peers` at all.
2. The CHANGELOG: <https://raw.githubusercontent.com/anthropics/claude-code/refs/heads/main/CHANGELOG.md>
   - The source for behaviour changes. Skip bullets starting with "Fixed"; they are about half of it.
   - It has no dates. Take them from the `<Update label="2.1.x" description="date">` tags in <https://code.claude.com/docs/en/changelog.md>.
3. The weekly digests: `https://code.claude.com/docs/en/whats-new/2026-wNN`
   - Good for why a change matters. Some weeks are missing (there is no w31); the index at `/whats-new` lists the real ones.
4. The docs shortcut table: `curl -sL https://code.claude.com/docs/en/interactive-mode.md`
   - The source for the Keyboard shortcuts section. Voice keys are in `voice-dictation.md`.
   - Check what each key does in each state: `Ctrl+C` interrupts, clears the input, or exits depending on what is running, and `Ctrl+B` backgrounds a task, not the session.

Before adding a command, read the "Deliberately not listed" comment at the end of the sheet.

## Commits

The git history is the sheet's changelog: one commit per release, in release order, including the quiet ones.

- `Update for 2.1.NNN`: something in the sheet changed.
- `Reviewed 2.1.NNN, nothing for the sheet`: only line 4 moves.

Release numbers skip. When the previous number was never released, the title says so: `Update for 2.1.257 (253-256 never released)`.

The body lists each behaviour change as a bullet, then everything deliberately left out, so a later pass can tell "not worth a line" from "missed it".
A change that belongs to no release gets its own commit, with a lowercase prefix for its kind:

- `meta:` instructions for maintaining the sheet: this file and the sheet's trailing comment.
- `tidy:` moving or rewording what the sheet already says.
- `add:` content the sheet never had.
- `fix:` correcting a line that is wrong.

An `add:` or `fix:` title ends with the release its content comes from, in parentheses, when that release is known: the release itself when it is later than 2.1.251, the version the sheet started from, and `pre 2.1.252` when it is earlier.

Run `prek run --all-files` before each commit; a fresh clone has no git hook installed.
