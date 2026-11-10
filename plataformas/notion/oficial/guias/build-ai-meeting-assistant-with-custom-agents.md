---
fonte: https://www.notion.com/help/guides/build-ai-meeting-assistant-with-custom-agents
baixado: 2026-11-10
---

# How to build a Meeting Assistant in Notion with Custom Agents

## Learn how to build a Custom Agent that gathers context from your project docs, drafts meeting agendas, and creates post-meeting summaries.

6 min read

Vídeo: https://www.youtube.com/watch?v=l6GIpD0s0_M

------------------------------------------------------------------------

## [**What you'll build**](https://www.notion.com/help/guides/build-ai-meeting-assistant-with-custom-agents#what-you'll-build)

A personalized Meeting Assistant agent that preps you for weekly project syncs by pulling the latest status, risks, and action items from your project docs, decision log, and the previous week’s recaps. After the meeting, it publishes a recap with action items and shares a quick update in Slack.

### [**Who this is for**](https://www.notion.com/help/guides/build-ai-meeting-assistant-with-custom-agents#who-this-is-for)

Project or program managers running a weekly cross-functional project sync.

PromptYou’re a Meeting Assistant for a PM running weekly launch syncs (like Project Bolt) with Engineering and Design. Before each meeting, create a prep brief and agenda by pulling the latest status, risks, and open action items from the project tracker plus the most recent meeting notes. After the meeting, turn the transcript into a recap with decisions and action items, then share a short summary in Slack so the whole team knows what’s next.[Try it\!→](https://app.notion.com/?target=new_custom_agent&prefill=You%E2%80%99re%20a%20Meeting%20Assistant%20for%20a%20PM%20running%20weekly%20launch%20syncs%20(like%20Project%20Bolt)%20with%20Engineering%20and%20Design.%20Before%20each%20meeting%2C%20create%20a%20prep%20brief%20and%20agenda%20by%20pulling%20the%20latest%20status%2C%20risks%2C%20and%20open%20action%20items%20from%20the%20project%20tracker%20plus%20the%20most%20recent%20meeting%20notes.%20After%20the%20meeting%2C%20turn%20the%20transcript%20into%20a%20recap%20with%20decisions%20and%20action%20items%2C%20then%20share%20a%20short%20summary%20in%20Slack%20so%20the%20whole%20team%20knows%20what%E2%80%99s%20next.)

## [1. Prompt the agent](https://www.notion.com/help/guides/build-ai-meeting-assistant-with-custom-agents#1.-prompt-the-agent)

In this step, you’ll define the agent’s core behavior: what it should review, what it should produce, and the guardrails that keep the output consistent each week.

1.  Open `Agents` from your sidebar and click `+` to start a new chat.

2.  Describe what you want the agent to do (the *Try this prompt* callout above is a good starting point).

3.  The agent will draft `instructions`, suggest `triggers`, and flag the `Tools and access` it needs. You'll fine-tune each of these in the next steps.

4.  Answer any quick follow-ups, like which meeting (e.g., Project Bolt Weekly) or Slack channel (e.g., \#project-bolt) to connect.

Vídeo: https://www.youtube.com/watch?v=l6GIpD0s0_M&t=37s

Helpful tips

## [2. Check tools and access](https://www.notion.com/help/guides/build-ai-meeting-assistant-with-custom-agents#2.-check-tools-and-access)

To prep an agenda before the sync and write a recap after, your agent needs the right level of access to a few sources.

Open `Tools and access` in your agent's settings and set permissions for each:

1.  **Projects database** (`read access`): to pull the latest statuses and risks into the prep brief.

2.  **Calendar** (`read access`): to find the next Project Bolt Weekly event.

3.  **Meeting Notes database** (`edit access`): to draft the agenda before the sync and write the recap after.

4.  **Slack** (`read and write access`): to post the recap to \#project-bolt.

Vídeo: https://www.youtube.com/watch?v=l6GIpD0s0_M&t=96s

Helpful tips

## [3. Refine triggers](https://www.notion.com/help/guides/build-ai-meeting-assistant-with-custom-agents#3.-refine-triggers)

Your agent likely suggested triggers based on your calendar. Review and adjust them here so you get an agenda before the meeting and a recap afterward.

Your agent has likely already suggested both triggers based on your calendar. Open Triggers in your agent's settings to review them, or follow the steps below to set them up from scratch.

Here's the setup for a Thursday 3 PM sync:

**Pre-meeting agenda** (so you have a day to review the prep before the sync):

1.  Click `Add trigger`.

2.  Set the schedule to weekly on Wednesdays at 11 AM.

3.  Click `Add trigger` to save.

**Post-meeting recap** (so the team gets the wrap-up while it's still fresh):

1.  Click `Add trigger`.

2.  Set the schedule to weekly on Thursdays at 4:45 PM.

3.  Click `Add trigger` to save.

Vídeo: https://www.youtube.com/watch?v=l6GIpD0s0_M&t=151s

Helpful tips

## [4. Check instructions](https://www.notion.com/help/guides/build-ai-meeting-assistant-with-custom-agents#4.-check-instructions)

Your agent's instructions are its blueprint, where all the logic lives. The agent builds them out as you chat, but it's worth a quick read-through to make sure it understood the assignment.

Open `Instructions` in your agent's settings and skim for:

1.  A quick overview of what your agent does week to week.

2.  How it preps the agenda before the sync (which sources it pulls from and what the format looks like).

3.  How it writes the recap after the sync, including the style and tone.

4.  How it handles your project context, like Project Bolt details, key people, and recurring themes.

5.  What it does when something's missing, like an owner or a due date.

If anything looks off, just tell your agent in chat and it'll update the instructions for you.

Vídeo: https://www.youtube.com/watch?v=l6GIpD0s0_M&t=194s

## [5. Provide examples](https://www.notion.com/help/guides/build-ai-meeting-assistant-with-custom-agents#5.-provide-examples)

Showing your agent what “good” looks like helps it be more consistent in every run. Examples of what to avoid are just as useful.

In the agent chat, share your format preferences:

1.  For the prep brief and recap, ask your agent to:

    - Keep it tight with 5–8 bullets.

    - Lead with open action items.

    - End with decisions needed.

2.  In the same chat, share what you want the Slack recap to look like:

    - 2–3 takeaways.

    - A quick action item summary.

    - A link back to the full notes page in Notion.

3.  Ask the agent to update its instructions to match. If, it asks for the go-ahead, click `Continue`.

4.  Click `Save` in your agent’s settings.

Vídeo: https://www.youtube.com/watch?v=l6GIpD0s0_M&t=227s

Helpful tips

## [6. Test your agent](https://www.notion.com/help/guides/build-ai-meeting-assistant-with-custom-agents#6.-test-your-agent)

Before you rely on this in a real meeting, run a quick test to make sure the agent is accurate, consistent, and doesn’t invent details.

1.  Click `Run agent` to kick off a test run.

2.  Your agent will ask which trigger to test. Start with the pre-meeting prep.

3.  Review the agenda. If anything’s off, tell your agent in chat and ask it to try again.

4.  Once the prep looks good, ask your agent to test the recap trigger.

5.  Click `Continue` when prompted so your agent can post a test message in Slack.

6.  Open the Slack post and review it. Same drill: if something’s off, just tell your agent.

Vídeo: https://www.youtube.com/watch?v=l6GIpD0s0_M&t=330s

Once both triggers check out, your agent is ready to run on its own.

Helpful tips

## [**How to roll out your Custom Agent**](https://www.notion.com/help/guides/build-ai-meeting-assistant-with-custom-agents#how-to-roll-out-your-custom-agent)

Once your agent's working the way you want, here's how to get it into your team's flow.

- **Start with one meeting, then scale:** Get your agent running reliably for one recurring meeting first, like your weekly project sync. Once it's consistent, duplicate it and adapt it for other meetings (retros, stakeholder updates, cross-functional syncs).

- **Swap Slack for whatever your team actually uses:** If Slack isn't part of your workflow, replace the recap step with a shared Notion page, an email summary, or any other tool your team checks.

- **Set expectations with your team:** Let them know when the agent runs, what it posts, and where to find the agendas and recaps. A quick heads-up goes a long way.

More resources

- For tips on keeping your agent sharp over time, check out our [Custom Agent best practices guide](https://www.notion.com/help/guides/best-practices-for-improving-your-custom-agent).

- For a deeper dive into Custom Agents, take our [course](https://academy.notion.com/page/notion-ai-catalogue) on Notion Academy.

Share this guide

------------------------------------------------------------------------
