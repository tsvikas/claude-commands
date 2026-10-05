# Launch drafts

Texts for announcing the sheet, one per place, in posting order.
They are drafts: reword them before posting, and submit each one by hand.
They say "v2.1.289"; update the number if a release lands first.
`plan.md` has the order, the rules behind each choice, and what is still open.

## Reddit: r/ClaudeAI and r/ClaudeCode

The rules of both subreddits are unread (Reddit refused the request), so read each sidebar for self-promotion and flair rules first.
Post to one, wait a few days, then the other. The same text in both on one day reads as spam.

Title: `I grouped every built-in Claude Code slash command and shortcut by task, and update it each release`

Body:

> The docs list commands alphabetically, which is fine for looking one up and useless for finding out what exists. I wanted a page I could read once and learn what the tool can do.
>
> So this is one sheet, ordered by what you are doing: set how Claude runs → write the prompt → while it works → check the work → manage the conversation → sessions → delegate and automate → configure.
>
> - Page (filter box, press a row for the details): https://tsvikas.github.io/claude-commands/
> - The same thing as one Markdown file: https://github.com/tsvikas/claude-commands
>
> Things I learned while building it that I had not seen anywhere:
>
> - TODO: two or three lines from the sheet that surprised you. A concrete command is what gets the post read.
>
> It currently reflects v2.1.289. Every release gets its own commit, so the git history is a list of what each version added. Each refresh reads the docs, the changelog and the binary, since each one misses things the others have.
>
> If a line is wrong or something is missing, tell me here or open an issue.

## Hacker News

A regular submission, not a Show HN: the Show HN rules put "lists, and other reading material" off topic and say to make a regular submission instead.
Do not ask anyone to upvote; the rules forbid it.

- Title: `Claude Code's slash commands and shortcuts, grouped by task`
- URL: https://tsvikas.github.io/claude-commands/

First comment, from you:

> I made this because I kept finding out about Claude Code commands by accident. The official command table is alphabetical, and a new release lands almost every week, so I never knew what I was missing.
>
> The sheet orders everything by what you are doing at that moment: setting how Claude runs, writing the prompt, watching it work, checking the result, then the conversation, sessions, delegation and configuration. Each row is one line; press it for the rest.
>
> For every release I re-read the docs command table, the changelog, the shortcut table and the installed binary, because no one of them is complete: some commands never appeared in the changelog at all. Each release is one commit, so `git log` doubles as a "what's new that I can use" feed.
>
> It is one Markdown file; the page and an outline are generated from it. Corrections are welcome, especially a command or key I have wrong.

## Anthropic Discord

Check the channel's rules on sharing your own work first.

> I keep a cheatsheet of Claude Code's built-in slash commands and keys, grouped by task instead of alphabetically, and refresh it for each release: https://tsvikas.github.io/claude-commands/ . Corrections welcome.

## awesome-claude-code

On or after 2026-10-11, through the web form only, filled in by hand:
https://github.com/hesreallyhim/awesome-claude-code/issues/new?template=recommend-resource.yml

| Field | Value |
| ------------ | ------------------------------------------ |
| Title | `[Resource]: claude-commands` |
| Display Name | claude-commands |
| Category | Documentation, Knowledge & Learning |
| Link | https://github.com/tsvikas/claude-commands |
| Author Name | Tsvika Shapira |
| Author Link | https://github.com/tsvikas |

Description (365 characters; the form allows 10 to 500, on one line, descriptive and not promotional, not addressing the reader, no emojis):

> A cheatsheet of Claude Code's built-in slash commands, bundled skills, keyboard shortcuts and message syntax, grouped by the task they serve rather than alphabetically. Each release is checked against the docs, the changelog and the installed binary and gets its own commit, so the git history shows what each version added. Also published as a filterable web page.

Before ticking the checklist:

- "Visited this repo with my own eyes, and the resource is sufficiently distinct": look at the two nearest entries and decide for yourself.
  Anthropic's own "Claude Code Cheatsheet" (support.claude.com) has about 36 slash commands plus core vocabulary.
  zebbern's "Claude Code Guide" is a single-page reference covering install, env vars, commands, MCP and hooks.
  This sheet has about 136 command names, is ordered by task, and has a per-release history.
- The last box says "Do not check the following box". Leave it unchecked.
