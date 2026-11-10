---
fonte: https://www.notion.com/help/guides/build-a-custom-agent-that-delivers-weekly-market-insights
baixado: 2026-11-10
---

# Build a Custom Agent that delivers weekly market insights

## Learn how to build a Custom Agent that delivers a weekly brief of what changed in your market, what's at risk, and what to do about it.

6 min read

Vídeo: https://www.youtube.com/watch?v=Tsr_O5Gp5Iw

------------------------------------------------------------------------

## [What you'll build](https://www.notion.com/help/guides/build-a-custom-agent-that-delivers-weekly-market-insights#what-you'll-build)

A Custom Agent that scans the sites you trust each week for competitor launches, pricing shifts, and category news, saves a full brief to your Market Briefs database, and posts a short summary to Slack. The team gets a regular read on what's changing in your market.

### [Who this is for](https://www.notion.com/help/guides/build-a-custom-agent-that-delivers-weekly-market-insights#who-this-is-for)

Product marketing, product, and strategy teams who own a recurring competitive or market update.

PromptI need a weekly market brief that tracks competitor launches, pricing changes, and important category news so we can spot anything that might impact our next launch.[Try it\!→](https://app.notion.com/?target=new_custom_agent&prefill=I%20need%20a%20weekly%20market%20brief%20that%20tracks%20competitor%20launches%2C%20pricing%20changes%2C%20and%20important%20category%20news%20so%20we%20can%20spot%20anything%20that%20might%20impact%20our%20next%20launch.)

## [1. Prompt the agent](https://www.notion.com/help/guides/build-a-custom-agent-that-delivers-weekly-market-insights#1.-prompt-the-agent)

In this step, you'll prompt the agent to draft an initial setup, including Instructions, Triggers, and the Tools and access it needs. You'll fine-tune each of these in the next steps.

1.  Open `Agents` from your sidebar and click `New agent`.

2.  In the chat, describe what you want the agent to do. You can use the *Try this prompt* callout above as a starting point.

3.  The agent will draft `Instructions`, suggest `Triggers`, and flag the `Tools and access` it needs.

4.  Answer any quick follow-ups, like which database or Slack channel to connect.

Vídeo: https://www.youtube.com/watch?v=Tsr_O5Gp5Iw&t=31s

Helpful tips

## [2. Enable trusted URLs](https://www.notion.com/help/guides/build-a-custom-agent-that-delivers-weekly-market-insights#2.-enable-trusted-urls)

The agent runs on its own each week, so it needs an explicit list of sites it's allowed to scan. Trusted URLs is how you set that scope.

1.  Open `Instructions` in your agent and scroll to `Trusted URLs`.

2.  Add the sites you want the agent to scan each week, such as:

    - Competitor news pages and product blogs.

    - Industry publications relevant to your market.

    - Any data providers or analyst sites you already trust.

3.  In `Tools and access`, you can also enable `Web Search` so the agent can scan across the web.

Vídeo: https://www.youtube.com/watch?v=Tsr_O5Gp5Iw&t=86s

Helpful tips

## [3. Set up triggers and access](https://www.notion.com/help/guides/build-a-custom-agent-that-delivers-weekly-market-insights#3.-set-up-triggers-and-access)

For the agent to run on its own each week and publish where the team will see it, you need to set the schedule and grant access to a few sources.

1.  **Set the weekly trigger:** Open `Triggers` and confirm there's a Monday 9:00 AM scheduled run that creates a new page in Market Briefs.

2.  **Connect Slack:** In `Tools and access`, connect your channel (e.g.,

    \#all-competition-market-intel) with `write` access so the agent can post the summary.

3.  **Give read access to context sources:** Still in `Tools and access`, give the agent read access to anything that helps ground its takeaways, like competitive one-pagers or Gong transcripts.

4.  Hit `Save`.

Vídeo: https://www.youtube.com/watch?v=Tsr_O5Gp5Iw&t=99s

Helpful tips

## [4. Establish scope](https://www.notion.com/help/guides/build-a-custom-agent-that-delivers-weekly-market-insights#4.-establish-scope)

In this step, you'll set guardrails on what the agent pulls and what it does when something is uncertain.

1.  In the chat, give the agent three guardrails:

    - **Recency:** Only look at updates from the last 7 days.

    - **Volume:** Cap summaries at 2 to 3 items per competitor.

    - **Sourcing:** Only include claims it can link to. If a source is missing or unclear, flag it instead of guessing.

2.  When prompted, click `Show changes` to review what the agent updated in `Instructions`, then hit `Save`.

Vídeo: https://www.youtube.com/watch?v=Tsr_O5Gp5Iw&t=224s

Helpful tips

## [5. Set formatting guidelines](https://www.notion.com/help/guides/build-a-custom-agent-that-delivers-weekly-market-insights#5.-set-formatting-guidelines)

A good weekly brief is consistent. In this step, you'll define the sections your agent uses so every brief is easy to scan and share.

1.  In the chat, tell the agent to format each brief with these sections:

    - **Highlights:** 3 to 5 bullets covering the most important changes.

    - **Risks:** What could impact your positioning or roadmap.

    - **Opportunities:** Openings the team could act on.

    - **Positioning tweaks:** Messaging or narrative adjustments to consider.

    - **Recommended actions:** Concrete next steps for Product and Marketing.

    - **Sources:** Links to every claim made in the brief.

2.  When prompted, click `Show changes` to review what the agent updated in `Instructions`, then hit `Save`.

Vídeo: https://www.youtube.com/watch?v=Tsr_O5Gp5Iw&t=287s

Helpful tips

## [6. Test your agent](https://www.notion.com/help/guides/build-a-custom-agent-that-delivers-weekly-market-insights#6.-test-your-agent)

Before the first scheduled run, kick off the agent manually. A test pass surfaces the small things, like wrong sources, missing links, or a Slack channel that didn't connect, while there's still time to fix them.

1.  Open `Triggers`, click `Run agent`, and select the Monday 9:00 AM scheduled run.

2.  Review the brief the agent creates and confirm:

    - Section headings match what you set in the previous step.

    - Takeaways are specific (a named competitor + dated event), not generic ("the market shifted").

    - Every claim links back to a source.

3.  Check \#all-competition-market-intel in Slack to confirm the summary posted with 2 to 3 highlights and a link to the full brief.

Vídeo: https://www.youtube.com/watch?v=Tsr_O5Gp5Iw&t=344s

Helpful tips

## [How to roll out your Custom Agent](https://www.notion.com/help/guides/build-a-custom-agent-that-delivers-weekly-market-insights#how-to-roll-out-your-custom-agent)

Once the agent is running reliably, share it with the team and put a light maintenance routine in place so the brief stays useful as your market shifts.

- **Set expectations with the team:** Tell stakeholders where the briefs live (the Market Briefs database), when they publish (Monday at 9:00 AM), and what the Slack post includes.

- **Be intentional about sharing:** Sharing the agent also shares what it has access to. Double-check the sources and integrations look right for the audience before adding new collaborators.

- **Test after any meaningful change:** If you add or remove sources, adjust scope, or change formatting, run a manual test before the next scheduled run.

- **Keep your source list focused:** A smaller, curated set of trusted URLs tends to produce more relevant briefs than a long, noisy one.

More resources

- For tips on keeping your agent sharp over time, check out our [Custom Agent best practices guide](https://www.notion.com/help/guides/best-practices-for-improving-your-custom-agent).

- For a deeper dive into Custom Agents, take our [course](https://academy.notion.com/page/notion-ai-catalogue) on Notion Academy.

Share this guide

------------------------------------------------------------------------
