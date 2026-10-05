# Launch plan

The goal is readers for the sheet.
The case for it: the official docs list commands alphabetically, and nothing else collects every command and key, groups them by task, and tracks them release by release.
Lead with "every command and key, grouped by task, updated every release" rather than "a cheatsheet". Cheatsheets are common; complete and current ones are not.

This branch holds working notes and is not meant to be merged into main.
`drafts.md` has the text for each post.

## Where it started

On 2026-10-04 the repo had 0 stars, 0 forks, and 0 views in GitHub's 14-day traffic graph, with no referrers.
It had 591 clones (197 unique), almost certainly the Pages workflow and bots.

## Done

- 2026-10-04: the repo's homepage points at the page, and it has eight topics: `claude-code`, `claude`, `anthropic`, `cheatsheet`, `slash-commands`, `keyboard-shortcuts`, `cli`, `ai-coding`.
- 2026-10-05: the page counts visits with GoatCounter. The numbers are at https://tsvikas.goatcounter.com.
- 2026-10-05: a pasted link to the page shows a preview: a canonical link, Open Graph tags and a 1200×630 picture.
- 2026-10-05: the repo has an MIT license.

## To do, in order

1. Fill in the Reddit draft's TODO with two or three commands that surprised you.
2. Read the self-promotion and flair rules of r/ClaudeAI and r/ClaudeCode.
3. Post to one subreddit.
4. A few days later, post to the other subreddit or to Hacker News.
5. Post the short line in the Anthropic Discord, after checking the channel's rules.
6. On or after 2026-10-11, fill in the awesome-claude-code form.

After each post, look at the GoatCounter referrers before posting the next, so each post's effect can be told apart.

## Why this order

- awesome-claude-code comes last.
  Its maintainer says plainly that getting listed is not a launch strategy: get users first, the list follows.
  It also requires 14 days since the first commit (2026-09-27, so 2026-10-11) or 100 stars, and closes earlier submissions automatically.
- It takes no pull requests. The only route is its web issue form, filled in by a human; it says a submission through `gh` risks a temporary block. One resource per submission, and its bot reports the repo's license.
- Hacker News gets a regular submission. The Show HN rules put "lists, and other reading material" off topic.
- The two subreddits get the post days apart, since the same text in both on one day reads as spam.

## Reading the numbers

- GoatCounter shows how many came, from which country and from which link, never who.
- Totals undercount, because ad blockers block GoatCounter and Claude Code users are a blocker-heavy crowd. Treat a total as a floor, and use the referrers to compare posts.
- To keep your own visits out, open the page once with `#toggle-goatcounter` at the end of its address, in each browser you use.
- GitHub's own traffic covers the repo, not the page, and keeps 14 days:
  `gh api repos/tsvikas/claude-commands/traffic/views` and `.../traffic/popular/referrers`.

## Ideas, not started

- A short post per notable release, such as "3 things 2.1.288 added that you can use today", linking to the page.
  A launch post is read once; the release cadence is the reason to come back, and the per-release commits already hold the material.
- A "What's new" section on the page, or an RSS feed, generated from the git log, so a visitor sees the release history without opening the repo.
- A footer line on the page saying it counts visits. Not legally needed, since there is no cookie and no personal data.
- Name Claude Code in the page's description. The title names it, but the description comes from the sheet's opening sentence, "Categorized reference for built-in slash commands and keyboard shortcuts, by task.", and that is the text a search result and a link preview show.
- A favicon for the page.
