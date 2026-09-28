# Marketplaces to know

Interesting or useful marketplaces, not a full list. Companion to
`claude-commands.md`, which covers only what ships in the binary.

Add a marketplace, then install from it:

```
/plugin marketplace add <owner/repo>
/plugin install <plugin>@<marketplace-name>
```

## Recommended

- `claude-plugins-official` — Anthropic's own; ships with Claude Code, so it is already present and `/plugin` browses it
- `anthropic-agent-skills` (`anthropics/skills`) — Anthropic's example skills. Overlaps what a claude.ai account already syncs
- `trailofbits` (`trailofbits/skills`) — Trail of Bits' own security and tooling skills
- `skills-curated` (`trailofbits/skills-curated`) — community-vetted, deliberately small
- `claude-code-workflows` (`wshobson/agents`) — subagents and workflows by language and domain
- `mattpocock` (`mattpocock/skills`) — Matt Pocock's engineering skills: grilling a plan, TDD, code review, merge conflicts. The official marketplace re-ships it as `mattpocock-skills`; install from one or the other, not both
