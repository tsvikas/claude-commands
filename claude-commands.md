# Claude Code Commands and Shortcuts Cheatsheet

Categorized reference for built-in slash commands and keyboard shortcuts, by task.
Snapshot as of v2.1.287 (2026-10-01) — canonical list: <https://code.claude.com/docs/en/commands.md>

Symbols: ⚡ costs tokens · ☁️ runs in the cloud.
`<arg>` is required, `[arg]` is optional: without it a command runs with no input or opens a picker, unless its line says otherwise.
`·` separates other names and keys for the same thing; parentheses hold a condition.
`Alt` is `Option` on macOS.

## Where to look

- [Set how Claude runs](#set-how-claude-runs) — model, fast mode, thinking, effort, output style, permission mode, plan mode, working directory
- [Write the prompt](#write-the-prompt) — `@file`, `!cmd`, `ultrathink`, newline, history, paste, voice
- [While Claude works](#while-claude-works) — stop, background, send now, side question, transcript, diff, focus view
- [Check the work](#check-the-work) — reviews, simplify, run, verify, browser tasks
- [Manage the conversation](#manage-the-conversation) — context, compact, clear, branch, rewind, copy, export
- [Manage sessions](#manage-sessions) — recap, rename, resume, teleport, background, desktop, Remote Control, exit
- [Delegate & automate](#delegate--automate) — subagents, forks, workflows, goals, loops, scheduled runs
- [Artifacts](#artifacts) — artifacts, design, slides
- [Specialist skills](#specialist-skills) — reference docs, Claude API
- [Project knowledge](#project-knowledge) — CLAUDE.md, init, memory, design sync
- [Inspect & diagnose](#inspect--diagnose) — cost, status, doctor, feedback
- [Configure](#configure) — settings, permissions, sandbox, MCP, plugins, skills, look & feel, account, integrations
- [Learn](#learn) — help, release notes, lessons
- [Extras](#extras) — radio, stickers, passes

Also in here: [what ultracode actually does](#what-ultracode-does).

## Set how Claude runs

### Set at the start

Changing one of these mid-conversation makes the next turn slower.
Switching model, or turning fast mode on for the first time, also re-reads the whole conversation with no prompt-cache hits, so that turn costs more.

- `/model [model]` · `Alt+P`: switch model. In the picker, `←`/`→` set the effort and `s` keeps the choice to this session
- `/fast [on|off]` · `Alt+O`: fast mode toggle
- `Alt+T`: toggle extended thinking (always on for newer models)

### Change any time

`/advisor` and `/output-style` keep the prompt cache, and so does `/effort` on newer models.
On older models and on third-party providers, a change of effort costs one uncached turn.

- `/effort [level|auto|status]` · `←`/`→` (in the model picker): set the effort level for the current model: low/medium/high/xhigh/max (max is session-only). `status` prints it. `s` in the picker: this session only
- `/effort ultracode [on|off]` · `Tab` (in the `/effort` slider): plan a workflow for every substantive task, at the current effort level (session-only)
- `/advisor [model|off]`: second model for guidance
- `/output-style [style]`: switch output style: default, proactive, concise, explanatory, learning; saved for this project, in `.claude/settings.local.json`

### What Claude may do, and where

- `Shift+Tab`: cycle permission modes: auto (the default), manual, auto-accept edits, plan (like `/plan`)
- `/plan`: enter plan mode (read/explore only)
- `/plan <task>` ⚡: enter plan mode and start planning the task immediately
- `/cd <path>`: move the session to a new working directory; its project config takes effect
- `/add-dir <path>`: add a directory without moving the session

## Write the prompt

### In the message

- `@file` / `@dir` / `@server:resource`: inline a file's content, a directory listing, or an MCP resource
- `@session-name`: mention another Claude Code session; Claude then reaches it with `SendMessage`
- `!<cmd>` (message prefix): run a shell command directly. Output lands in the conversation *and* Claude responds to it (costs a turn)
- `/skill-a /skill-b <text>`: stack up to 6 skills at the start of a message; the trailing text goes to each
- `ultrathink`: request deeper reasoning (for this turn only)
- `:name:`: emoji shortcode autocomplete in the prompt

### Editing

The usual Bash line-editing keys work: `Ctrl+A`/`Ctrl+E`, `Alt+B`/`Alt+F`, `Ctrl+K`/`Ctrl+U`, `Ctrl+W`/`Alt+D`, `Ctrl+Y`/`Alt+Y`.

- `Shift+Enter` · `Ctrl+J` · `\ Enter`: newline (`Shift+Enter` needs `/terminal-setup` in some terminals)
- `Tab` (after a `/` typed mid-prompt): list the matching commands
- `Space` (hold or tap): dictate a prompt (needs `/voice` on)
- `Ctrl+Shift+-`: undo input edit
- `Ctrl+V` · `Alt+V` (Windows and WSL) · `Cmd+V` (iTerm2): paste images
- `Ctrl+S`: stash or restore prompt
- `Up` / `Down`: prompt history
- `Ctrl+R`: search prompt history
- `Esc Esc` (with text in the prompt, nothing running) · `Ctrl+C` (nothing running): clear input
- `Ctrl+G`: edit prompt in `$EDITOR`

## While Claude works

### Act on the running turn

- `Esc` · `Ctrl+C`: interrupt Claude
- `Ctrl+B` · `Ctrl+X Ctrl+B`: background running tasks
- `Ctrl+Enter` · `Ctrl+X Ctrl+S`: send queued messages now; running tasks move to the background
- `/btw [question]` ⚡: ask a side question without adding to the conversation. With no argument, opens previous answers (`Shift+←`/`Shift+→` browse, `c` copies, `f` forks)

### See what it is doing

- `/diff`: interactive diff viewer for uncommitted changes; in fullscreen, a live panel beside the conversation
- `/focus`: focus view: last prompt + tool summary + response (fullscreen only, persists via `viewMode`)
- `Ctrl+O`: toggle the verbose transcript
- `Ctrl+E` (in the verbose transcript): expand all content
- `Ctrl+E` (in a permission dialog): toggle explanation (not in Bash / PowerShell prompts)
- `Ctrl+T`: toggle the todo list (off for newer models unless `CLAUDE_CODE_ENABLE_TODO_TOOLS=1`)
- `Ctrl+L`: redraw the screen

## Check the work

### Review the change

- `/code-review [effort-level] [--fix] [--comment] [pr#|branch|path]` · `/review` ⚡: review the current diff, or a PR/branch/path, for bugs. Runs as a background subagent. `--fix` applies findings, `--comment` posts them on the PR. With no effort level it reuses the last one you typed
- `/code-review ultra` · `/ultrareview` · `ultrareview` ☁️: deeper review, multi-agent cloud run (usage credits). On a github.com PR target, `--post` preselects posting the findings to the PR
- `/simplify [target]` ⚡: simplify the code (runs 4 parallel agents: reuse, simplify, efficiency, abstraction level)
- `/security-review` ⚡: review the local changes for injection / auth / data-exposure risks

### Run it

- `/run` ⚡: launch and drive the project to see a change working
- `/verify` (no project `verify` skill) ⚡: run the project e2e and verify its behavior; then save what worked as a project `verify` skill. Runs only when you call it
- `/verify` (with a project `verify` skill) ⚡: verify by following the saved recipe. Claude also runs it before committing code changes
- `/claude-in-chrome [task]` ⚡: have Claude carry out a task in your browser — test a web app, read console logs, fill forms, extract data from pages

## Manage the conversation

- `/context [all]`: visualize context usage
- `/compact [instructions]` ⚡: summarize conversation to free context
- `/autocompact [auto|<tokens>]`: how full context gets before auto-compaction kicks in (e.g. `500k`); saved as a default
- `/clear [name]` · `/reset` · `/new`: start fresh (also starts a new session)
- `/branch [name]`: branch the conversation: you switch to a new session (with that name); the original is preserved (return to it with `/resume`)
- `Esc Esc` (on an empty prompt, nothing running) · `/rewind` · `/checkpoint` · `/undo`: rewind the conversation/code to a previous point, or summarize from or up to it
- `/copy [N]`: copy Nth-latest response (pick code blocks interactively)
- `/export [filename]`: export conversation as plain text

## Manage sessions

### Recognize this one

- `/recap` ⚡: one-line summary of the session
- `/rename [name]`: rename current session
- `/color`: set the prompt bar color for this session; syncs to claude.ai, handy for telling concurrent sessions apart

### Pick up another

- `/resume [ended-session]` · `/continue`: switch to a past conversation; the current one is saved and can be resumed later
- `/resume [background-session]` · `/continue`: attach to a background session that is still running; the current conversation moves to the background
- `/teleport` · `/tp`: copy a claude.ai web session into the terminal (not synced)

### Move or mirror this one

Background sessions run without a terminal, so they keep working after you close it.
From the shell, `claude attach <id>` reattaches to one; `claude --help` also lists `logs`, `stop`, `respawn`, `rm`.

- `←` (on an empty prompt): background or detach the session, then open agent view (your background sessions)
- `/background [prompt]` · `/bg` ⚡: detach this session to run as a background agent, freeing the terminal
- `/desktop` · `/app`: continue in the desktop app
- `/remote-control [name]` · `/rc`: expose this local session to claude.ai; it runs here and the conversation is mirrored both ways

### End it

- `Ctrl+C` (twice, nothing running) · `Ctrl+D` (twice, on an empty prompt) · `/exit` · `/quit`: exit CLI (in an attached background session: detaches and leaves it running)
- `/stop`: stop the current background session (keeps the worktree)

## Delegate & automate

### Hand a task to a copy of this conversation

- `/subtask <task>` ⚡: forked subagent — inherits the full conversation, runs in the background, returns its result *here*
- `/fork [prompt]` ⚡: copy the conversation into a new background session and keep working here; the copy edits in its own worktree

### Run agents in parallel

- `ultracode` ⚡: run a single task as a dynamic workflow
- `/batch <instruction>` ⚡: split a codebase-wide change into 5–30 units; once you approve the plan, one subagent + worktree per unit
- `/deep-research <question>` ⚡: fan out web searches, cross-check sources, synthesize a cited report

### Keep Claude working unattended

- `/goal [condition|clear]` ⚡: keep working until a condition is met. With no argument, shows the current goal
- `/loop [interval] [prompt]` · `/proactive` ⚡: run a prompt on an interval (or self-paced); with no prompt it runs an autonomous check, or `.claude/loop.md`
- `/schedule [description]` · `/routines` ⚡ ☁️: cron-scheduled cloud agents
- `/autofix-pr [prompt]` ⚡ ☁️: watch a PR, push fixes when CI fails

### See what is running, and control it

- `/tasks` · `/bashes`: view everything running in the background; shows the model and effort level each subagent ran on
- `Ctrl+X Ctrl+K` (twice): stop all background subagents; also turns off artifact auto-replies for the rest of the session
- `/workflows`: workflow progress view (`p` pauses or resumes, `x` stops, `r` restarts an agent, `s` saves as a command, `Enter` opens an agent)
- `/list-agents` · `/peers`: list names for everything Claude can message (subagents, teammates, other sessions)

## Artifacts

- `/artifacts`: list Artifacts you own or that were shared with you; then attach one to the session (`Enter`), open it in the browser, or copy its link
- `Ctrl+]`: reopen the last Artifact
- `/design [brief]` ⚡ ☁️: draft a canvas of editable UI artboards, published as an Artifact; tweak one by hand, then tell Claude which to implement (research preview, Pro/Max/Team/Enterprise)
- `/slides [brief]` ⚡ ☁️: turn a brief into a slide deck, published as an Artifact; you edit and present it in the browser

## Specialist skills

### Reference

Claude loads these on its own when a task calls for them; type one to load it up front.

- `/dataviz [request]` ⚡: chart / dashboard design guidance
- `/workflow-authoring` ⚡: the dynamic-workflow script reference — API, resume behavior, quality patterns. Run it by hand before editing a saved one
- `/artifact-diagramming` ⚡: diagramming guidance for artifacts — when a diagram helps, and inline SVG that reads in light and dark themes
- `/artifact-capabilities` ⚡: what a published artifact can do at runtime: call your connectors, offer a file download; also which of those your account has

### Claude API projects

- `/claude-api` ⚡: load Claude API / Managed Agents docs for your project's language; also loads on its own when your code imports `anthropic`
- `/claude-api migrate` ⚡: move existing API code to a newer model
- `/claude-api upgrade` ⚡: take the SDK across a major version (Python `anthropic` 0.x to 1.x)
- `/claude-api managed-agents-onboard` ⚡: walk through creating a Managed Agent
- `/claude-api prompt-audit` ⚡: flag instructions written for older models in prompts, skills and tool descriptions
- `/claude-api cost-optimize` ⚡: profile API spend and cut it one measured change at a time
- `/claude-api build-eval` ⚡: build an eval set for your Claude-powered app
- `/claude-api hillclimb` ⚡: improve the app step by step against an existing eval
- `/claude-api preserved-thinking-migration` ⚡: find edits that drop preserved thinking, and fix them one at a time; covers edits to earlier turns, system prompt or tools

## Project knowledge

`CLAUDE.md` is read at launch from the working directory and every directory above it, plus `~/.claude/CLAUDE.md`; a subdirectory's loads when Claude reads a file there.
`AGENTS.md` is read the same way, but only when no `CLAUDE.md` exists in the working directory or above; Project instructions in `/config` can make Claude read both.

- `/init` ⚡: generate CLAUDE.md for a project
- `/memory`: edit CLAUDE.md / rules files, toggle auto-memory (project-scoped)
- `/run-skill-generator` ⚡: teach `/run` and `/verify` how to build, launch and drive this project
- `/team-onboarding` ⚡: onboarding guide for teammates
- `/design-sync [hint]` ⚡: sync a React design system to Claude Design

## Inspect & diagnose

- `/usage` · `/cost` · `/stats`: session cost and plan limits; also breakdowns per skill, agent and `/loop`, plus prompt-cache hit ratio
- `/status`: version, model, account, connectivity; also session kind and whether GitHub is connected for cloud sessions
- `/doctor` · `/checkup` ⚡: setup checkup that diagnoses issues and can fix them; they include unused skills/MCP/plugins, redundant `CLAUDE.md` content and slow hooks
- `/doctor prompt-audit` ⚡: audit CLAUDE.md files, skills, agents and commands for prompting written for older models
- `/skill-doctor`: which of your loaded skills go unused and what each costs in context, so you can prune them (needs feature-flag fetching)
- `/debug [description]` ⚡: enable debug logging and troubleshoot
- `/heapdump`: heap snapshot for memory diagnosis
- `/feedback [report]` · `/bug` · `/share`: send product feedback about Claude Code

## Configure

What you set here is persistent between sessions.

### Settings

- `/config [key=value ...]` · `/settings`: theme, model default, output style, etc.
- `/update-config [request]` ⚡: edit `settings.json` in free language ("allow npm test", "add a hook that…")

### Permissions

- `/permissions` · `/allowed-tools`: manage allow, ask and deny rules for tool permissions
- `/fewer-permission-prompts` ⚡: scan transcripts, add a read-only allowlist to project settings
- `/auto-mode-setup` ⚡: draft `autoMode.environment` entries from your project and recent sessions; review, then save them to user settings (Pro/Max/Team)
- `/sandbox`: set up sandbox mode; saved for this project, in `.claude/settings.local.json`

### Extensions

Skills and plugins you enable on claude.ai also load in your terminal sessions.

- `/plugin [subcommand]`: manage plugins (list, install, enable, disable)
- `/reload-plugins [--force]`: reload active plugins, when a change didn't take effect on its own
- `/skills`: list skills, toggle visibility
- `/reload-skills`: re-scan skill directories
- `/mcp [reconnect|enable|disable [<server>|all]]`: manage MCP server connections
- `/hooks`: view/edit hook configurations (user and project scope)

### Look & input

- `/statusline` ⚡: configure the status line (describe it, or auto-configure from your shell prompt)
- `/theme`: color theme
- `/tui [default|fullscreen]`: renderer; relaunches with the conversation intact. With no argument, prints the active one
- `/scroll-speed`: mouse wheel speed (fullscreen only)
- `/keybindings`: open keyboard shortcuts file
- `/voice [hold|tap|off]`: voice dictation mode; once on, use `Space` to dictate. With no argument, toggles it

### Account & plan

- `/login` / `/logout`: Anthropic account sign in/out
- `/upgrade`: switch to higher plan tier
- `/usage-credits`: configure usage credits for when you hit a limit
- `/rate-limit-options`: what to do when a usage limit blocks a request — wait and continue automatically at reset, add credits, upgrade
- `/privacy-settings`: view/update privacy settings

### One-time integrations

- `/import [codex|gemini|cursor] [--dry-run] [--yes]`: bring configuration over from Codex / Gemini CLI / Cursor: instruction files, MCP servers, commands, subagents and skills
- `/terminal-setup`: terminal keybindings
- `/ide`: IDE integrations and status
- `/chrome`: Claude in Chrome settings
- `/mobile` · `/ios` · `/android`: QR code to download the mobile app
- `/web-setup`: connect GitHub for Claude Code on the web
- `/remote-env`: default environment for cloud agents
- `/install-github-app`: Claude GitHub App for a repo
- `/install-slack-app`: Claude Slack app
- `/design-login`: authorize design-system access for `/design-sync`
- `/setup-bedrock`: Amazon Bedrock auth
- `/setup-vertex`: Google Cloud auth

## Learn

- `?` (on an empty prompt): toggle the shortcut help panel
- `/help`: help and available commands
- `/release-notes`: changelog picker
- `/powerup`: interactive lessons
- `/insights` ⚡: cross-session report across all projects: project areas, interaction patterns, friction points, prompts auto mode could have spared you

## Extras

- `/radio`: Claude FM lo-fi radio
- `/stickers`: order Claude Code stickers
- `/passes`: share a free week with friends

______________________________________________________________________

## What ultracode does

`ultracode` opts into *dynamic workflows*: instead of working turn by turn, Claude writes a JavaScript orchestration script and a runtime executes it in the background.
It spawns dozens to hundreds of subagents (16 concurrent, 1000 per run max) while the session stays responsive.
Intermediate results stay in script variables, only the final answer lands in context.

- Keyword form (`ultracode` in a message): run one task as a workflow. Plain "use a workflow" works too.
- Session form (`/effort ultracode`, or `Tab` in the `/effort` slider): Claude plans a workflow for every substantive task, possibly several per request (understand, change, verify). More tokens and slower per request.
- Skill form (workflows like `/deep-research`): some bundled skills already are workflows, so they fan out without you opting in.
- Watch and manage with `/workflows`; `/workflow-authoring` loads the script-API reference before you hand-edit a saved script.
- Size: a guideline caps the agents per run — small on Pro plans, medium elsewhere (~10 agents, down from 15); change it with Dynamic workflow size in `/config`.
- Cost: a run can spend far more than the same task in conversation. Gauge on a small slice first, and check `/model` before a large run, agents inherit the session model.
- Usage limit: a run that hits it pauses and resumes at reset.
- Workflow subagents always run in acceptEdits mode with your tool allowlist, regardless of session permission mode.

## Beyond slash commands

Other parts of Claude Code worth getting to know, each with its own reference:

- the `claude` CLI (flags and subcommands): <https://code.claude.com/docs/en/cli-reference>
- permission rules (wildcards, `domain:` and MCP forms, what is auto-allowed): <https://code.claude.com/docs/en/permissions>
- hooks: recipes in <https://code.claude.com/docs/en/hooks-guide>, all the events in <https://code.claude.com/docs/en/hooks>
- environment variables: <https://code.claude.com/docs/en/env-vars>

<!-- Deliberately not listed:
/agents  - since v2.1.198 it only prints "ask Claude, or edit .claude/agents/", and
   since 2.1.281 it is gone from the / menu and /help; typing it still explains
/ultraplan, /pr-comments, /vim  - removed upstream, the docs table keeps tombstone rows

Registered as bundled skills at 2.1.251, but no user can type them:
/explain-usage, /setup-cowork  - isEnabled demands CLAUDE_CODE_ENTRYPOINT=remote_cowork
/plan-artifact  - isEnabled is hardwired to false in that build
/artifact-components  - gated on the tengu_gable_onyx_sluice flag, off by default
Re-check by grepping the binary for name:"..." near userInvocable:!0 and isEnabled.

/artifact-design, /keybindings-help  - bundled skills registered userInvocable:!1
   at 2.1.286: reference for Claude to load, absent from the docs table and from
   the / menu until the full name is typed. Ask in plain words instead.

This file has no changelog section - the git history is the changelog.
Line 4 always names the version the file reflects, so git log alone answers
which releases have been read.
  git log --oneline                 what versions are covered
  git show <commit>                 the notes for one version
  git log -p -- claude-commands.md  when a line last changed, and why
-->
