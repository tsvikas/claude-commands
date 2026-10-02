# Claude Code Commands and Shortcuts: Outline

Every command and key in [the cheatsheet](claude-commands.md), by section and group.
Generated from it by `tools/outline.py`; edit the sheet, not this file.

## [Set how Claude runs](claude-commands.md#set-how-claude-runs)

- **Set at the start:** `/model`, `/fast`, `Alt+T`
- **Change any time:** `/effort`, `/effort ultracode`, `/advisor`, `/output-style`
- **What Claude may do, and where:** `Shift+Tab`, `/plan`, `/plan <task>`, `/cd`, `/add-dir`

## [Write the prompt](claude-commands.md#write-the-prompt)

- **In the message:** `@file` / `@dir` / `@server:resource`, `@session-name`, `!<cmd>`, `/skill-a /skill-b`, `ultrathink`, `:name:`
- **Editing:** `Shift+Enter`, `Tab`, `Space`, `Ctrl+Shift+-`, `Ctrl+V`, `Ctrl+S`, `Up` / `Down`, `Ctrl+R`, `Esc Esc` (with text in the prompt, nothing running), `Ctrl+G`

## [While Claude works](claude-commands.md#while-claude-works)

- **Act on the running turn:** `Esc`, `Ctrl+B`, `Ctrl+Enter`, `/btw`
- **See what it is doing:** `/diff`, `/focus`, `Ctrl+O`, `Ctrl+E` (in the verbose transcript), `Ctrl+E` (in a permission dialog), `Ctrl+T`, `Ctrl+L`

## [Check the work](claude-commands.md#check-the-work)

- **Review the change:** `/code-review`, `/code-review ultra`, `/simplify`, `/security-review`
- **Run it:** `/run`, `/verify` (no project `verify` skill), `/verify` (with a project `verify` skill), `/claude-in-chrome`

## [Manage the conversation](claude-commands.md#manage-the-conversation)

- `/context`, `/compact`, `/autocompact`, `/clear`, `/branch`, `Esc Esc` (on an empty prompt, nothing running) · `/rewind`, `/copy`, `/export`

## [Manage sessions](claude-commands.md#manage-sessions)

- **Recognize this one:** `/recap`, `/rename`, `/color`
- **Pick up another:** `/resume [ended-session]`, `/resume [background-session]`, `/teleport`
- **Move or mirror this one:** `←`, `/background`, `/desktop`, `/remote-control`
- **End it:** `Ctrl+C` · `/exit`, `/stop`

## [Delegate & automate](claude-commands.md#delegate--automate)

- **Hand a task to a copy of this conversation:** `/subtask`, `/fork`
- **Run agents in parallel:** `ultracode`, `/batch`, `/deep-research`
- **Keep Claude working unattended:** `/goal`, `/loop`, `/schedule`, `/autofix-pr`
- **See what is running, and control it:** `/tasks`, `Ctrl+X Ctrl+K`, `/workflows`, `/list-agents`

## [Artifacts](claude-commands.md#artifacts)

- `/artifacts`, `Ctrl+]`, `/design`, `/slides`

## [Specialist skills](claude-commands.md#specialist-skills)

- **Reference:** `/dataviz`, `/workflow-authoring`, `/artifact-diagramming`, `/artifact-capabilities`
- **Claude API projects:** `/claude-api`, `/claude-api migrate`, `/claude-api upgrade`, `/claude-api managed-agents-onboard`, `/claude-api prompt-audit`, `/claude-api cost-optimize`, `/claude-api build-eval`, `/claude-api hillclimb`, `/claude-api preserved-thinking-migration`

## [Project knowledge](claude-commands.md#project-knowledge)

- `/init`, `/memory`, `/run-skill-generator`, `/team-onboarding`, `/design-sync`

## [Inspect & diagnose](claude-commands.md#inspect--diagnose)

- `/usage`, `/status`, `/doctor`, `/doctor prompt-audit`, `/skill-doctor`, `/debug`, `/heapdump`, `/feedback`

## [Configure](claude-commands.md#configure)

- **Settings:** `/config`, `/update-config`
- **Permissions:** `/permissions`, `/fewer-permission-prompts`, `/auto-mode-setup`, `/sandbox`
- **Extensions:** `/plugin`, `/reload-plugins`, `/skills`, `/reload-skills`, `/mcp`, `/hooks`
- **Look & input:** `/statusline`, `/theme`, `/tui`, `/scroll-speed`, `/keybindings`, `/voice`
- **Account & plan:** `/login` / `/logout`, `/upgrade`, `/usage-credits`, `/rate-limit-options`, `/privacy-settings`
- **One-time integrations:** `/import`, `/terminal-setup`, `/ide`, `/chrome`, `/mobile`, `/web-setup`, `/remote-env`, `/install-github-app`, `/install-slack-app`, `/design-login`, `/setup-bedrock`, `/setup-vertex`

## [Learn](claude-commands.md#learn)

- `?`, `/help`, `/release-notes`, `/powerup`, `/insights`

## [Extras](claude-commands.md#extras)

- `/radio`, `/stickers`, `/passes`
