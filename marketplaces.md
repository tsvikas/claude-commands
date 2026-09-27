# Marketplaces worth adding

The plugin marketplaces I recommend, and why each earns its place. Companion to
`claude-commands.md`, which covers only what ships in the binary.

Add a marketplace, then install from it:

```
/plugin marketplace add <owner/repo>
/plugin install <plugin>@<marketplace-name>
```

## Recommended

| marketplace | source | plugins | what it is |
| --- | --- | --- | --- |
| `claude-plugins-official` | ships with Claude Code, fetched over GCS — no GitHub URL | 314 | Anthropic's own. Already present; `/plugin` browses it |
| `anthropic-agent-skills` | `anthropics/skills` | 2 | Anthropic's example skills, as `document-skills` (xlsx, docx, pptx, pdf) and `example-skills` (skill-creator, mcp-builder, algorithmic-art, canvas-design, …). 19 skills in the repo. Overlaps what a claude.ai account already syncs — see below |
| `trailofbits` | `trailofbits/skills` | 44 | Trail of Bits' own security and tooling skills |
| `skills-curated` | `trailofbits/skills-curated` | 29 | Community-vetted, deliberately small. Vetting is the point |
| `claude-code-workflows` | `wshobson/agents` | 94 | Subagents and workflows by language and domain |

## Reference, not installable

- `asgeirtj/system_prompts_leaks` — `Anthropic/claude-code/` holds `skills/`, `agents/`, `commands/`, `output-styles/` and a system prompt per model. Unofficial and unaffiliated, so treat it as a reading copy that may be stale, never as a source of truth. Useful for seeing a bundled or synced skill's full text without gating it behind your own account.

## Skills that arrive without a marketplace

Two paths deliver skills that no `/plugin` command manages:

- **Bundled** — inside the binary, listed in `claude-commands.md`. The docs mark them **Skill** in <https://code.claude.com/docs/en/commands>
- **Synced from claude.ai** — written to `~/.claude/skills/synced/<uuid>_<uuid>/`, one folder per skill plus a `manifest.json` that records each skill's `source` and `updatedAt`. Off with `syncClaudeAiSkills: false`

The synced set follows the account, not the install, so it differs per person. Sampling twelve accounts' committed manifests, five are universal — `docx`, `pdf`, `pptx`, `xlsx`, `skill-creator` — and `morning` and `import-memory` appear in eleven. The rest track which surfaces an account uses: `computer-use`, `built-in-browser`, `chrome-browser` and `deep-research` in roughly a third, then per-account custom skills.

To review your own, read the folder directly, or copy it out and commit it so each sync shows as a diff:

```
jq -r '.skills[] | "\(.updatedAt)  \(.source)  \(.name)"' ~/.claude/skills/synced/*/manifest.json | sort
rsync -a ~/.claude/skills/synced/*/ ~/code/synced-skills/
```

Edit the files in place and Claude Code will tell you the change is not saved to your account; the next sync overwrites them.
