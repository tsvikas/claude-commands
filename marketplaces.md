# Marketplaces to know

These places hold interesting or useful plugins. Not a full list. Companion to
`claude-commands.md`, which covers only what ships in the binary.

Add a marketplace, then install from it:

```
/plugin marketplace add <owner/repo>
/plugin install <plugin>@<marketplace-name>
```

## Recommended

- `claude-plugins-official` — Anthropic's own; ships with Claude Code, so it is already present and `/plugin` browses it. Try: `frontend-design`, `pr-review-toolkit`, `pyright-lsp`
- `anthropic-agent-skills` (`anthropics/skills`) — Anthropic's example skills. Overlaps what a claude.ai account already syncs, see below. Try: `document-skills` (xlsx, docx, pptx, pdf), `example-skills` (skill-creator, mcp-builder, …)
- `trailofbits` (`trailofbits/skills`) — Trail of Bits' own security and tooling skills. Try: `static-analysis`, `differential-review`, `modern-python`
- `skills-curated` (`trailofbits/skills-curated`) — community-vetted, deliberately small. Try: `humanizer`, `planning-with-files`, `last30days`
- `claude-code-workflows` (`wshobson/agents`) — subagents and workflows by language and domain. Try: `python-development`, `comprehensive-review`, `tdd-workflows`
- `mattpocock` (`mattpocock/skills`) — Matt Pocock's engineering skills: grilling a plan, TDD, code review, merge conflicts. The official marketplace re-ships it as `mattpocock-skills`; install from one or the other, not both

## Reference, not installable

- `asgeirtj/system_prompts_leaks` — `Anthropic/claude-code/` holds `skills/`, `agents/`, `commands/`, `output-styles/` and a system prompt per model. Unofficial and unaffiliated, so treat it as a reading copy that may be stale, never as a source of truth. Useful for seeing a bundled or synced skill's full text without gating it behind your own account.

## Skills that arrive without a marketplace

Two paths deliver skills that no `/plugin` command manages:

- **Bundled** — inside the binary, listed in `claude-commands.md`. The docs mark them **Skill** in <https://code.claude.com/docs/en/commands>
- **Synced from claude.ai** — written to `~/.claude/skills/synced/<uuid>_<uuid>/`, one folder per skill plus a `manifest.json` that records each skill's `source` and `updatedAt`. Off with `syncClaudeAiSkills: false`

The synced set follows the account, not the install, so it differs per person.

## Reading a skill's full text

There is no public catalogue — most of these skills are published nowhere. Two
places hold the full text.

Your account's skills, the ones that sync, are readable in full at
<https://claude.ai/new#customize/skills/yours>. That page does not cover skills
installed from a marketplace, or bundled ones.

Everything you install is also plain markdown on disk, which is the copy to grep,
diff across syncs, or read offline:

| kind | where |
| --- | --- |
| synced from claude.ai, including the skills of a plugin you added there | `~/.claude/skills/synced/<uuid>_<uuid>/<name>/SKILL.md` |
| installed from a marketplace | `~/.claude/plugins/cache/<marketplace>/<plugin>/.../skills/<name>/SKILL.md` |
| your own | `~/.claude/skills/<name>/SKILL.md`, or a project's `.claude/skills/` |
| bundled | not on disk — it lives inside the binary. The docs table describes it, `asgeirtj/system_prompts_leaks` mirrors the text |

The official marketplace is worth reading as an index in its own right: its
`.claude-plugin/marketplace.json` lists every plugin, most as `git-subdir`
pointers at the vendor's own repo, so it says where each one really comes from.
It does not carry the plugins in the claude.ai directory — those reach you only
by syncing, and several are published nowhere else.

To review your own, read the folder directly, or copy it out and commit it so each sync shows as a diff:

```
jq -r '.skills[] | "\(.updatedAt)  \(.source)  \(.name)"' ~/.claude/skills/synced/*/manifest.json | sort
rsync -a ~/.claude/skills/synced/*/ ~/code/synced-skills/
```
