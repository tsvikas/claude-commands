# Claude Code Slash Commands Cheatsheet

Categorized reference for built-in slash commands.
Snapshot as of 2026-08 / v2.1.251 (commands are added often) — canonical list: <https://code.claude.com/docs/en/commands.md>

Symbols: ⚡ costs tokens · ☁️ runs in the cloud.

## Where to look

1. [Steer the model](#1-steer-the-model) — model, effort, thinking, plan mode
2. [Manage the context window](#2-manage-the-context-window) — compact, clear, branch, rewind
3. [Act on the code](#3-act-on-the-code) — reviews, verify, simplify, design, reference docs
4. [Delegate & automate](#4-delegate--automate) — subagents, background & scheduled runs
5. [Capture & share output](#5-capture--share-output) — diff, copy, export, recap
6. [Manage the session itself](#6-manage-the-session-itself) — resume, background, move between surfaces
7. [Inspect & diagnose](#7-inspect--diagnose) — cost, status, doctor, feedback
8. [Learn](#8-learn) — help, release notes, lessons
9. [Play](#9-play) — radio, stickers
10. [Project bootstrap](#10-project-bootstrap) — init, onboarding, design sync
11. [Set up & configure](#11-set-up--configure-persistent-survives-sessions) — settings, permissions, MCP, look & feel, accounts

Also in here: [in-message directives](#in-message-directives-not-commands) (`@file`, `!cmd`, `ultrathink`…), [keyboard shortcuts](#keyboard-shortcuts), [what ultracode actually does](#ultracode-the-special-case), and [recently added & changed](#recently-added--changed) — read that one first if you've been away a month.

## 1. Steer the model

### Saved as default (persist across sessions)

- `/model [model]` (`Opt+P`): switch model. `s` in picker to switch for this session only.
- `/effort [level|auto]` (`←`/`→` in the model picker): reasoning effort: low/medium/high/xhigh/max/ultracode (max and ultracode are session-only). The saved default is per model, so each model keeps its own
- `/fast [on|off]` (`Opt+O`): fast mode toggle
- `/advisor [model|off]`: second model for guidance

### Session only

- `ultrathink`: request deeper reasoning (for this turn only)
- `Opt+T`: toggle extended thinking
- `Shift+Tab`: cycle permission modes
- `/plan`: enter plan mode (read/explore only)
- `/plan <task>` ⚡: enter plan mode and start planning the task immediately

## 2. Manage the context window

- `/context [all]`: visualize context usage
- `/compact [instructions]` ⚡: summarize conversation to free context
- `/autocompact [auto|<tokens>]`: how full context gets before auto-compaction kicks in (e.g. `500k`); saved as a default
- `/clear [name]` (`/reset`, `/new`): start fresh (also starts a new session)
- `/branch [name]`: fork the conversation here to try a different direction; return to the original with `/resume`
- `/rewind` (`/checkpoint`, `/undo`, `Esc Esc`): pick a past point, then roll code/conversation back to it or summarize the conversation before or after it

## 3. Act on the code

### Check the work

- `/code-review [effort-level] [--fix] [--comment] [pr#|branch|path]` (`/review`) ⚡: review the local changes, or a PR/branch/path. `--fix` applies findings, `--comment` posts them as inline PR comments. Runs as a background subagent, so findings arrive without eating your context; with no effort level it reuses the last one you typed
- `/code-review ultra` (`/ultrareview`, `ultrareview`) ☁️: deeper review, multi-agent cloud run (usage credits). On a github.com PR target, `--post` preselects posting the findings to the PR
- `/security-review` ⚡: review the local changes for injection / auth / data-exposure risks
- `/simplify [target]` ⚡: simplify the code (runs 4 parallel agents: reuse, simplify, efficiency, abstraction level)
- `/verify` ⚡: run the project e2e and verify its behavior
- `/run` ⚡: launch and drive the project to see a change working

### Design

- `/design [brief]` ⚡ ☁️: draft a canvas of editable UI artboards (published as an Artifact), tweak one by hand, then tell Claude which to implement (research preview, Pro/Max/Team/Enterprise)

### Reference (load expertise into context)

- `/claude-api [migrate|upgrade|managed-agents-onboard|prompt-audit|cost-optimize]` ⚡: Claude API / Managed Agents docs. The subcommands act: migrate code to a newer model, upgrade a Python project from `anthropic` 0.x to 1.x, walk through creating a Managed Agent, audit prompts and skills for older-model instructions, profile and cut API spend one measured change at a time
- `/dataviz [request]` ⚡: chart / dashboard design guidance
- `/workflow-authoring` ⚡: the dynamic-workflow script reference — API, resume behavior, quality patterns. Claude loads it itself before writing a script; run it by hand before editing a saved one

## 4. Delegate & automate

### Start now

- `/btw [question]` ⚡: quick side question, kept out of history (`c` copies the raw markdown answer)
- `/subtask <task>` ⚡: forked subagent — inherits the full conversation, runs in the background, returns its result *here*
- `/fork [prompt]` ⚡: copy the conversation into a separate background session that goes its own way (own worktree, own row in `claude agents`)
- `/batch <instruction>` ⚡: split a codebase-wide change into 5–30 units, one subagent + worktree + PR each
- `ultracode` ⚡: run a single task as a dynamic workflow
- `/deep-research <question>` ⚡: fan out web searches, cross-check sources, synthesize a cited report

### Recurring / conditional

- `/loop [interval] [prompt]` (`/proactive`) ⚡: run a prompt on an interval (or self-paced); with no prompt it runs an autonomous check, or `.claude/loop.md`
- `/goal [condition|clear]` ⚡: keep working until a condition is met
- `/schedule [description]` (`/routines`) ⚡ ☁️: cron-scheduled cloud agents
- `/autofix-pr [prompt]` ⚡ ☁️: watch a PR, push fixes when CI fails

### Monitor & control

- `/tasks` (`/bashes`): view everything running in the background, with the model and effort level each subagent ran on
- `/workflows`: workflow progress view (`p` pause, `x` stop, `s` save as command)
- `/list-agents` (`/peers`): everything Claude can message — subagents, live teammates, other sessions on this machine, your Remote Control sessions elsewhere and cloud sessions (labelled `offline` / `cloud`), with the name to address each one by

## 5. Capture & share output

- `/diff`: interactive diff viewer for uncommitted changes
- `/copy [N]`: copy Nth-latest response (pick code blocks interactively)
- `/export [filename]`: export conversation as plain text
- `/artifacts`: list Artifacts you own or that were shared with you, then attach one to the session (`Enter`), open it in the browser, or copy its link
- `/recap` ⚡: one-line summary of the session

## 6. Manage the session itself

### Lifecycle

- `/resume [session]` (`/continue`): resume a previous conversation
- `/rename [name]`: rename current session
- `/color`: set the prompt bar color for this session (syncs to claude.ai), handy for telling concurrent sessions apart
- `/background [prompt]` (`/bg`) ⚡: detach this session to run as a background agent, freeing the terminal (reattach with `claude attach <id>`; `claude --help` also lists `logs`, `stop`, `respawn`, `rm`)
- `/stop`: stop the attached background session (transcript and worktree kept; to detach and leave it running use `/exit`)
- `/exit` (`/quit`): exit CLI (in an attached background session: detaches and leaves it running)

### Workspace scope

- `/cd <path>`: move session to a new working directory; its project settings, hooks, skills, agents and `.mcp.json` servers take effect right away
- `/add-dir <path>`: add a directory without moving the session

### Move between surfaces

- `/desktop` (`/app`): continue in the desktop app
- `/teleport` (`/tp`): pull a claude.ai web session into the terminal
- `/remote-control` (`/rc`): expose this local session to claude.ai

## 7. Inspect & diagnose

- `/usage` (`/cost`, `/stats`): session cost, plan limits, per-skill/agent breakdown, a per-`/loop` breakdown (runs, tokens, tokens per run, last run), and a prompt-cache line (hit ratio, misses, tokens re-cached, warm/cold)
- `/status`: version, model, account, connectivity, session kind, whether GitHub is connected for Claude Code on the web
- `/doctor` (`/checkup`) ⚡: setup checkup that also fixes — install health, unused skills/MCP/plugins vs their context cost, duplicated or derivable `CLAUDE.md` content, slow hooks. Reports first, asks before changing anything
- `/debug [description]` ⚡: enable debug logging and troubleshoot
- `/heapdump`: heap snapshot for memory diagnosis
- `/feedback [report]` (`/bug`, `/share`): submit feedback, report a bug, or share the conversation. Claude can queue a draft report here when something goes wrong (`feedbackDrafts: false` to turn off)

## 8. Learn

- `/help`: help and available commands
- `/release-notes`: changelog picker
- `/powerup`: interactive lessons
- `/insights` ⚡: cross-session report: project areas, interaction patterns, friction points

## 9. Play

- `/radio`: Claude FM lo-fi radio
- `/stickers`: order Claude Code stickers

## 10. Project bootstrap

- `/init` ⚡: generate CLAUDE.md for a project
- `/run-skill-generator` ⚡: teach `/run` and `/verify` how to build, launch and drive this project
- `/team-onboarding` ⚡: onboarding guide for teammates
- `/design-sync [hint]` ⚡: sync a React design system to Claude Design

## 11. Set up & configure (persistent, survives sessions)

### Behavior & safety

- `/config [key=value ...]` (`/settings`): theme, model default, output style, etc.
- `/permissions` (`/allowed-tools`): manage allow/ask/deny rules (user and project scope); the **Auto mode** tab holds the classifier rules and recent auto-mode denials
- `/fewer-permission-prompts` ⚡: scan transcripts, add a read-only allowlist to project settings
- `/auto-mode-setup` ⚡: draft `autoMode.environment` entries from your project and recent sessions, review, then save them to user settings (Pro/Max/Team)
- `/sandbox`: toggle sandbox mode (supported platforms only)
- `/hooks`: view/edit hook configurations (user and project scope)
- `/memory`: edit CLAUDE.md / rules files, toggle auto-memory (project-scoped)
- `/privacy-settings`: view/update privacy settings

### Capabilities

- `/mcp [reconnect <server>|enable|disable [<server>|all]]`: manage MCP server connections
- `/plugin [subcommand]`: manage plugins (list, install, enable, disable)
- `/reload-plugins [--force]`: reload active plugins
- `/skills`: list skills, toggle visibility
- `/reload-skills`: re-scan skill directories

### Look & input

- `/theme`: color theme
- `/tui [default|fullscreen]`: renderer; relaunches with the conversation intact
- `/focus`: focus view: last prompt + tool summary + response (fullscreen only, persists via `viewMode`)
- `/scroll-speed`: mouse wheel speed (fullscreen only)
- `/statusline` ⚡: configure the status line (describe it, or auto-configure from your shell prompt)
- `/keybindings`: open keyboard shortcuts file
- `/voice [hold|tap|off]`: voice dictation mode

### Accounts & backends

- `/login` / `/logout`: Anthropic account sign in/out
- `/upgrade`: switch to higher plan tier
- `/usage-credits`: configure usage credits for when you hit a limit
- `/rate-limit-options`: what to do when a usage limit blocks a request — wait and continue automatically at reset, add credits, upgrade (hidden from the menu, type the full name)
- `/setup-bedrock`: Amazon Bedrock auth
- `/setup-vertex`: Google Cloud auth
- `/passes`: share a free week with friends

### One-time integrations

- `/import [codex|gemini] [--dry-run] [--yes]`: pull instruction files, MCP servers, commands, subagents and skills over from Codex / Gemini CLI
- `/terminal-setup`: terminal keybindings
- `/ide`: IDE integrations and status
- `/chrome`: Claude in Chrome settings
- `/mobile` (`/ios`, `/android`): QR code to download the mobile app
- `/web-setup`: connect GitHub for Claude Code on the web
- `/remote-env`: default environment for cloud agents
- `/install-github-app`: Claude GitHub App for a repo
- `/install-slack-app`: Claude Slack app
- `/design-login`: authorize design-system access for `/design-sync`

## In-message directives (not commands)

- `@file` / `@dir` / `@server:resource`: inline a file's content, a directory listing, or an MCP resource
- `@session-name`: mention another Claude Code session; Claude then reaches it with `SendMessage`
- `!<cmd>` (message prefix): run a shell command directly. Output lands in the conversation *and* Claude responds to it (costs a turn) — `respondToBashCommands: false` for the old silent behavior
- `/skill-a /skill-b <text>`: stack up to 6 skills at the start of a message, the trailing text goes to each
- `:name:`: emoji shortcode autocomplete in the prompt (`emojiCompletionEnabled` to disable)

## Keyboard shortcuts

defaults, `/keybindings` to customize

### Steering

- `Shift+Tab`: cycle permission modes: auto (classifier-adjudicated, the default for new sessions since 2026-08-14), manual (was "default"), auto-accept edits, plan mode (like `/plan`)
- `Opt+P`: switch model (like `/model`, `←`/`→` in the picker: effort slider)
- `Opt+O`: toggle fast mode (like `/fast`)
- `Opt+T`: toggle extended thinking for the session

### While Claude works

- `Esc`: interrupt the current turn
- `Ctrl+F`: kill running agents
- `Ctrl+X` `Ctrl+K` (twice): stop all background subagents
- `Ctrl+B`: send the running task to the background (like `/background`)
- `Ctrl+O`: toggle verbose transcript (also expands a collapsed `Message from @sender` preview)
- `Ctrl+T`: toggle the todo list (nothing to show on Opus 4.8 / Sonnet 5 / Fable 5 and newer — todo tools are off there unless `CLAUDE_CODE_ENABLE_TODO_TOOLS=1`)
- `Ctrl+]`: reopen the last Artifact
- `Ctrl+E` (in the verbose transcript): expand all content
- `Ctrl+E` (in a permission dialog): toggle explanation

### Prompt editing

- `\` + `Enter`: newline
- `Esc` `Esc` (double tap): clear input
- `Up` / `Down`: prompt history
- `Ctrl+R`: search prompt history
- `Ctrl+W`: delete word back (`keybindingFlavor: "readline"` to stop at whitespace like Bash instead of at punctuation)
- `Ctrl+Shift+-` (or `Ctrl+_`): undo input edit
- `Ctrl+V`: paste images
- `Ctrl+S`: stash prompt
- `Ctrl+G`: edit prompt in `$EDITOR`
- hold `Space` (empty prompt): push-to-talk voice

---

## Ultracode, the special case

`ultracode` opts into *dynamic workflows*: instead of working turn by turn, Claude writes a JavaScript orchestration script and a runtime executes it in the background.
It spawns dozens to hundreds of subagents (16 concurrent, 1000 per run max) while the session stays responsive.
Intermediate results stay in script variables, only the final answer lands in context.

- Keyword form (`ultracode` in a message): run one task as a workflow. Plain "use a workflow" works too.
- Session form (`/effort ultracode`): `xhigh` reasoning + Claude plans a workflow for every substantive task, possibly several per request (understand, change, verify). More tokens and slower per request.
- Skill form (workflows like `/deep-research`): some bundled skills already are workflows, so they fan out without you opting in.
- Watch and manage with `/workflows`; `/workflow-authoring` loads the script-API reference before you hand-edit a saved script.
- Cost: a run can spend far more than the same task in conversation. Gauge on a small slice first, and check `/model` before a large run, agents inherit the session model.
- Workflow subagents always run in acceptEdits mode with your tool allowlist, regardless of session permission mode.

## Notation & notes

Legend used throughout:

- ⚡ invokes the model, costs tokens (the rest are instant UI commands)
- ☁️ runs in the cloud on Anthropic infra, needs a claude.ai account
- `/cmd` (`/alias`): parens right after a command hold its alternative names
- `<arg>` a required argument, `[arg]` an optional one

Two cross-cutting axes worth asking about any command:

- How long the effect lasts: one message, this session, forever (config), or out in the world.
- Scope: some config commands manage both user-level (`~/.claude/`) and project-level (`.claude/`) layers.

How this sheet is ordered: sections by mid-task lookup frequency, one-time setup near the end; within each subsection, commands go from most-used to most-niche.

## Recently added & changed

Newest first. Only what changes how you invoke something — bug fixes and UI polish are left out.
Numbers are the release a change landed in; `claude --version` to compare against your install.

### August 2026 · 2.1.221–251

New: `/workflow-authoring` — the dynamic-workflow script reference (248) · `/claude-api cost-optimize` — profile and cut API spend (247) · `/design` — draft editable UI artboards on a canvas (233) · `/rate-limit-options` — options when a usage limit blocks you (234) · `/auto-mode-setup` — draft auto-mode environment entries (228) · `/autocompact` — set the compaction threshold (221) · `/list-agents` (`/peers`) — sessions Claude can message (224) · `/claude-api prompt-audit` — flag older-model instructions in your prompts and skills (221)

- `/effort` saves your default level per model, so each model keeps its own (251)
- `/cost` gained a per-session prompt-cache line — hit ratio, misses, tokens re-cached, warm/cold — plus a `prompt_cache` object for status line scripts (251)
- `claude --help` now lists `attach`, `logs`, `stop`, `respawn`, `rm`, and `--resume` on a running background session names the exact `claude attach <id>` (251)
- `CLAUDE_CODE_SUBAGENT_MODEL` is a default now, not an override: an agent definition's `model:` and an explicit per-spawn model win over it (251)
- `PreModelSwitch` / `PostModelSwitch` hook events can block, confirm or annotate a model switch (251)
- Claude in Chrome actions go through Claude Code's own permission checks instead of the extension's prompts (251)
- `/loop`'s self-paced dynamic mode and its no-prompt autonomous default are available everywhere now, Bedrock / Vertex / Foundry included (248)
- the Workflow tool's description shrank from ~5.7k to ~1k tokens; the script-writing reference moved into `/workflow-authoring` (248)
- `--restricted` (`CLAUDE_CODE_RESTRICTED=1`) drops the command- and code-running tools plus `WebFetch`, confines file tools to the working directory, and ignores user / project / local settings (248)
- `/ultrareview <PR#>` checks your GitHub account can reach the repo before launching, instead of failing after the cloud session starts (248)
- in the agent view's dispatch input, `Shift+Enter` inserts a newline and `Ctrl+Enter` dispatches and attaches (248)
- Claude can queue a feedback draft when something goes wrong; you review and send it from `/feedback` (`feedbackDrafts: false` to turn off) (247)
- Bash permission prompts gained a one-keystroke "Yes, and switch to auto mode" (247)
- messages from your other sessions collapse to a one-line `Message from @sender:` preview; `Ctrl+O` expands the body (247)
- Sonnet 5's auto-compact threshold now uses its full 1M window — about 967K tokens instead of 934K (247)
- `/permissions` gained an **Auto mode** tab, for the classifier rules and recent auto-mode denials (246)
- Claude can start `/code-review` on its own everywhere now — ask in plain language, or point a scheduled task at it (246)
- `/cd` applies the new directory's project settings, hooks, skills, agents and `.mcp.json` servers right away, instead of at the next `--resume` (246)
- a subagent that hits its `maxTurns` limit returns partial output plus a hint to continue it via `SendMessage`, instead of looking finished (246)
- `/usage` gained a Loops breakdown: per-`/loop` runs, tokens, tokens per run, last run (243)
- `/tasks` and the agent dialogs show the model and effort level each subagent ran on (243)
- `/status` gained rows for GitHub-connected (for Claude Code on the web) and for managed-settings sources skipped by a higher-precedence one (243)
- `/login` can sign in with an Anthropic Console account without minting an API key (243)
- `modelPicker` setting: curate the `/model` picker with your own ordered, labelled list (243)
- `/goal` check-ins on parked background work back off 30 min → 1 h → 2 h, and stop after three per goal; your next message allows three more (239, 246)
- `/claude-api upgrade` migrates a Python project from `anthropic` 0.x to 1.x (239)
- `/list-agents` also lists your live teammates, not just subagents and sessions (239)
- `keybindingFlavor: "readline"` makes `Ctrl+W` and the word-motion keys behave like Bash (238, 239)
- new built-in "Concise" output style — result first, no preamble; pick it under Output style in `/config` (237)
- pressing `Enter` on a slash-command typo now reports Unknown command instead of running the closest fuzzy match; prefixes and aliases still run (236)
- `ANTHROPIC_DEFAULT_MODEL` sets the model new sessions start on; unlike `ANTHROPIC_MODEL`, a `/model` pick still overrides it and persists (236)
- cross-session `SendMessage` gained `notify_when_idle` (one notice when that session next goes idle); native Windows got cross-session messaging at all (236, 239)
- `@` in the prompt now also mentions another *session* by name, and Claude messages it; live sessions on one machine get unique names automatically (232)
- dialogs no longer wait for the turn to end: `/permissions`, `/add-dir`, `/autocompact`, `/theme`, `/help`, `/config`, `/advisor` (234), `/feedback` and `/bug` (232) open mid-turn
- `Ctrl+T`'s todo list is empty on Opus 4.8 / Sonnet 5 / Fable 5 and newer — the todo tools are gone unless `CLAUDE_CODE_ENABLE_TODO_TOOLS=1` (233)
- `/goal` now clears itself when a turn dies unrecoverably, and checks in on background tasks that keep it waiting 30+ min (234)
- `/config` gained "Continue automatically at usage limit" (234) and rows for dialog expiry and inbound messages from your other sessions (232)
- `/code-review` at high/xhigh/max runs in a background agent too, like the lower levels (232)
- subagents fork by default (inheriting the conversation and its prompt cache) and spawn in the background (232)
- `/plugin install plugin@marketplace` refreshes the marketplace first, so a freshly published plugin installs (232)
- `Esc` in fullscreen keeps a mouse text selection instead of clearing it (234)
- `/review` is now *only* an alias of `/code-review` with the same arguments, no longer a separate PR-picker command (223)
- `/code-review` with no effort level reuses the level you typed last (223)
- `/fork` copies get a worktree of their own instead of sharing your checkout (221)
- `/plugin` installs activate in the running session when it's safe, no `/reload-plugins` (221)
- `/status` gained a session-kind row: `interactive`, or background `attached` / `unattended` (221)
- not a command, but it moves what `Shift+Tab` lands on: auto mode became the default permission mode for new sessions on 2026-08-14

### July 2026 · 2.1.198–220

New: `/dataviz` (198) · `/checkup` as an alias of `/doctor` (205) · `/artifacts` — list and attach your Artifacts (208) · `/subtask` (212) · `/import` from Codex / Gemini (213)

- **`/fork` changed meaning** — it now copies the conversation into a separate background session; the old "subagent that reports back here" is `/subtask` (212)
- `/doctor` went from a read-only report to a checkup that also fixes (205)
- `/verify` and `/deep-research` run only when you invoke them; Claude no longer starts them on its own (215, 218) — `/code-review` went back the other way in 246
- `/code-review` runs as a background subagent, so review work stays out of your context (218)
- the `/agents` wizard is gone — ask Claude, or edit `.claude/agents/` directly (198)
- `/fast` dropped Opus 4.7; it applies to Opus 5 and 4.8 (219)
- bare `/btw` reopens the side panel on your last exchange instead of starting a fresh one (212)

### June 2026 · 2.1.160–197

New: `/cd` — move the session's working directory (169) · `/plugin list` inline, with `--enabled` / `--disabled` (163)

- the dynamic-workflow trigger keyword became `ultracode`; the plain word "workflow" no longer fires one (160)
- `/config key=value` sets any setting from the prompt, also under `-p` and Remote Control; `/config --help` lists the keys (181, 183)
- `/rewind` can resume a conversation from before `/clear` was run (191)
- `/install-github-app` can install just the app and skip the Actions workflow and secrets (187)
- `/btw` gained `c` to copy the raw markdown answer (163)
- `/effort` now says when your chosen level will persist as the default for new sessions (162)

<!-- Deliberately not listed:
/agents  - since v2.1.198 it only prints "ask Claude, or edit .claude/agents/"
/ultraplan, /pr-comments, /vim  - removed upstream, the docs table keeps tombstone rows

Refreshing this file - no single source is complete, use all three:
1. curl -sL https://code.claude.com/docs/en/commands.md
   The canonical table. Diff the command names against this file:
     grep -oE '^\| `/[a-z-]+' commands.md | sed 's/| `//' | sort -u
   Do NOT read it via a fetch-and-summarize tool, that silently drops and
   invents rows. Its "Requires vX" clause is the reliable birth date of a
   command - better than the CHANGELOG, which never mentioned /radio,
   /list-agents or /peers at all.
2. https://raw.githubusercontent.com/anthropics/claude-code/refs/heads/main/CHANGELOG.md
   Best source for behaviour changes. Has no dates - join on the docs
   changelog, which carries <Update label="2.1.x" description="date">.
   Skip bullets starting with "Fixed", they are ~half of it and are noise here.
3. https://code.claude.com/docs/en/whats-new/2026-wNN
   Weekly digests, good for framing why a change matters. Some weeks are
   missing entirely (there is no w31) - the index at /whats-new lists the real ones.

Month boundaries so far: June 2.1.160, July 2.1.198, August 2.1.221.
Add a new month block on top; prune blocks older than ~6 months, the body
above already reflects them.
-->
