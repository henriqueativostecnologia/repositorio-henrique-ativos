---
fonte: https://www.notion.com/help/guides/how-to-automate-sales-prospecting-in-notion-with-custom-agents
baixado: 2026-11-10
---

# How to automate sales prospecting in Notion with Custom Agents

## Learn how to build two Custom Agents that brief you on prospect accounts each morning, help you turn the signal into a sharp point of view (POV), and draft a ready-to-send outreach sequence (with a quick human-in-the-loop step in between to keep your judgment in the mix).

- Sales

10 min read

Vídeo: https://www.youtube.com/watch?v=g1XSdDiBPvE

------------------------------------------------------------------------

## [What you'll build](https://www.notion.com/help/guides/how-to-automate-sales-prospecting-in-notion-with-custom-agents#what-you'll-build)

1.  **Account Briefing Scout, a Custom Agent** that runs every weekday morning and posts a fresh briefing on your target accounts: recent news (last 7, 30, and 90 days), the top five to focus on today, and recurring themes worth a POV.

2.  **A quick check-in with your Notion agent** that turns one of those themes into a structured POV doc and files it in your Prospecting POVs database.

3.  **Outreach Sequencer, a second Custom Agent** that triggers the moment a new POV lands and drafts a full multi-channel sequence (emails, cold call scripts, LinkedIn messages) into your Outbound Sequences database, ready to paste into your sales engagement tool.

### [Who this is for](https://www.notion.com/help/guides/how-to-automate-sales-prospecting-in-notion-with-custom-agents#who-this-is-for)

Account executives, SDRs, and sales leaders who run their own outbound and want to spend less time researching and writing, and more time talking to prospects.

Have these ready before you build

- A list of target accounts in Salesforce (or wherever your CRM lives) for the briefing agent to pull from.

- A Notion database for daily account briefings (one page per day works well).

- A Notion database for prospecting POVs.

- A Notion database for outbound sequences, with a relation property back to your POV database.

- Your sales methodology saved as a Notion page the agents can reference (Henry uses

  *Fanatical Prospecting*).

- **\[Optional\]** Slack connected under `Tools and access`, if you want the agent to post notifications there.

## [1. Build the account briefing agent](https://www.notion.com/help/guides/how-to-automate-sales-prospecting-in-notion-with-custom-agents#1.-build-the-account-briefing-agent)

This is the agent that does your morning research for you. Instead of opening five tabs, scanning Google Alerts, and stitching together a list of who to reach out to, you start your day with a Notion page that already has the top accounts, the news behind them, and the themes worth pulling on.

PromptYou are an Account Briefing Scout for an AE/SDR team covering \[INDUSTRY/SEGMENT\]. Every weekday morning, pull recent news (last 7, 30, and 90 days) across my target accounts in Salesforce (or my CRM / accounts list database). Identify the top five accounts to prioritize for outreach today and explain why, with links to sources. For each top account, suggest a next action (call/email/LinkedIn) and the angle to lead with. Flag any themes showing up across multiple accounts. Publish the briefing as a new page in my Daily Account Briefings database (one page per day) so I can act on it first thing.[Try it\!→](https://app.notion.com/?target=new_custom_agent&prefill=You%20are%20an%20Account%20Briefing%20Scout%20for%20an%20AE%2FSDR%20team%20covering%20%5BINDUSTRY%2FSEGMENT%5D.%20Every%20weekday%20morning%2C%20pull%20recent%20news%20(last%207%2C%2030%2C%20and%2090%20days)%20across%20my%20target%20accounts%20in%20Salesforce%20(or%20my%20CRM%20%2F%20accounts%20list%20database).%20Identify%20the%20top%20five%20accounts%20to%20prioritize%20for%20outreach%20today%20and%20explain%20why%2C%20with%20links%20to%20sources.%20For%20each%20top%20account%2C%20suggest%20a%20next%20action%20(call%2Femail%2FLinkedIn)%20and%20the%20angle%20to%20lead%20with.%20Flag%20any%20themes%20showing%20up%20across%20multiple%20accounts.%20Publish%20the%20briefing%20as%20a%20new%20page%20in%20my%20Daily%20Account%20Briefings%20database%20(one%20page%20per%20day)%20so%20I%20can%20act%20on%20it%20first%20thing.)

### [1.1 Prompt the agent](https://www.notion.com/help/guides/how-to-automate-sales-prospecting-in-notion-with-custom-agents#1.1-prompt-the-agent)

In this step, you'll set the agent's foundation: what to look at each morning, what to produce, and the guardrails that keep the briefing consistent day-to-day.

1.  Open `Agents` from your sidebar and click `+` to start a new chat.

2.  Describe what you want the agent to do (the *Try this prompt* callout above is a good starting point).

3.  The agent will draft `instructions`, suggest `triggers`, and flag the `Tools and access` it needs. You'll fine-tune each of these in the next steps.

4.  Answer any quick follow-ups, like which accounts to monitor (e.g., your AE Target Accounts view), the news window (7, 30, and 90 days is a good default), and which database the daily briefing should land in.

Vídeo: https://www.youtube.com/watch?v=g1XSdDiBPvE&t=52s

Helpful tips

### [1.2 Check tools and access](https://www.notion.com/help/guides/how-to-automate-sales-prospecting-in-notion-with-custom-agents#1.2-check-tools-and-access)

This agent needs read access to your CRM and reference pages, and write access to your briefings database. Connecting Slack is optional, but useful if you want a morning summary posted to your channel.

Open `Tools and access` in your agent's settings and set permissions for each:

1.  **Salesforce** or your CRM (`read access`): to pull your target account list and recent activity.

2.  **Sales methodology page and brand style guide** (`read access`): so the briefing follows your team's frameworks and tone.

3.  **Daily Account Briefings database** (`edit access`): to create a new briefing page each morning.

4.  **Web search** (`enabled`): to pull recent news beyond what's in Salesforce.

5.  **\[Optional\] Slack** (`read and write access`): to post a short summary in your sales channel.

Vídeo: https://www.youtube.com/watch?v=g1XSdDiBPvE&t=75s

Helpful tips

### [1.3 Set the trigger](https://www.notion.com/help/guides/how-to-automate-sales-prospecting-in-notion-with-custom-agents#1.3-set-the-trigger)

Triggers tell your agent when to run automatically. Set a scheduled trigger here so your briefing is ready first thing in the morning, before you start outbound.

1.  Click `Add trigger`.

2.  Under `Recurring`, choose `On a schedule` and set it to run weekdays at 6:00 AM in your local timezone.

3.  Click `Add trigger` to save.

Vídeo: https://www.youtube.com/watch?v=g1XSdDiBPvE&t=114s

Helpful tips

### [1.4 Review the briefing format](https://www.notion.com/help/guides/how-to-automate-sales-prospecting-in-notion-with-custom-agents#1.4-review-the-briefing-format)

Your agent's instructions determine what lands in every briefing. A useful briefing is fast to scan and specific enough to act on.

Add these four sections to the briefing format:

1.  **Top five accounts for today:** one-sentence reason each (trigger event, news, or signal).

2.  **Recent news per account:** grouped by timeframe (7, 30, 90 days) with source links.

3.  **Persistent themes:** patterns showing up across multiple accounts (M&A, platform shifts, regulatory changes).

4.  **Suggested next action** for each top account (call, email, or POV draft).

Then ask the agent to update its instructions and click `Save`.

### [1.5 Test the agent](https://www.notion.com/help/guides/how-to-automate-sales-prospecting-in-notion-with-custom-agents#1.5-test-the-agent)

Before the agent runs on schedule, trigger it manually once to make sure everything is connected and the briefing looks right.

1.  Click `Run agent` under Triggers.

2.  Open the briefing and check: are the top five accounts ones you'd actually reach out to? Are the news items recent and relevant? If you set up Slack notifications, is the summary useful?

3.  If anything looks off, chat with the agent and ask it to update its instructions.

Vídeo: https://www.youtube.com/watch?v=g1XSdDiBPvE&t=131s

Helpful tips

------------------------------------------------------------------------

## [2. Shape a POV with your Notion agent](https://www.notion.com/help/guides/how-to-automate-sales-prospecting-in-notion-with-custom-agents#2.-shape-a-pov-with-your-notion-agent)

Here, you'll bring Notion agent into the mix. Custom Agents are built for repeatable work that runs on its own; Notion agent is built for one-off tasks like brainstorming, drafting, and thinking out loud, which is exactly what shaping a POV calls for. You'll draft and refine it in chat, then save the final version to your database.

PromptCan you research and formulate a point of view on \[ACCOUNT NAME\] for \[THEME OR USE CASE\]. Make sure this is a well-researched and defendable point of view. If it’s not defendable, tell me why. Use \[BRAND STYLE GUIDE\] as a template for how the information should look. Once I confirm it’s ready, save it as a new page in my Prospecting POVs database with the persona, theme, and source accounts as properties.[Try it\!→](https://app.notion.com/?target=new_custom_agent&prefill=Can%20you%20research%20and%20formulate%20a%20point%20of%20view%20on%20%5BACCOUNT%20NAME%5D%20for%20%5BTHEME%20OR%20USE%20CASE%5D.%20Make%20sure%20this%20is%20a%20well-researched%20and%20defendable%20point%20of%20view.%20If%20it%E2%80%99s%20not%20defendable%2C%20tell%20me%20why.%20Use%20%5BBRAND%20STYLE%20GUIDE%5D%20as%20a%20template%20for%20how%20the%20information%20should%20look.%20Once%20I%20confirm%20it%E2%80%99s%20ready%2C%20save%20it%20as%20a%20new%20page%20in%20my%20Prospecting%20POVs%20database%20with%20the%20persona%2C%20theme%2C%20and%20source%20accounts%20as%20properties.)

Open today's briefing in your Daily Account Briefings database and review the Persistent Themes section. Choose a theme that stands out (for example, post-merger integration, cost reduction, or platform consolidation), then identify which of your top accounts are experiencing it. Those accounts will become the focus of your POV.

### [2.1 Chat with your Notion agent](https://www.notion.com/help/guides/how-to-automate-sales-prospecting-in-notion-with-custom-agents#2.1-chat-with-your-notion-agent)

1.  Open your Notion agent and @-mention today's briefing so it has the full context.

2.  Ask the agent to draft a POV doc on the theme you picked.

    - Be specific about the audience, for example "Chief Transformation Officers at large enterprises post-acquisition."

    - Then sharpen the angle: what you believe and why it matters now, for example "platform consolidation fails without a shared source of truth."

3.  Iterate in chat, pushing for a sharper hook, stronger proof points, and tighter language.

4.  When the draft feels right, ask the agent to save it to your Prospecting POVs database.

Vídeo: https://www.youtube.com/watch?v=g1XSdDiBPvE&t=157s

Helpful tips

------------------------------------------------------------------------

## [3. Build the Outreach Sequencer agent](https://www.notion.com/help/guides/how-to-automate-sales-prospecting-in-notion-with-custom-agents#3.-build-the-outreach-sequencer-agent)

This agent runs when a new POV is added to your database. Each time it triggers, it reads the POV and generates a full multi-channel sequence (emails, cold call scripts, LinkedIn messages) in your Outbound Sequences database, ready for you to review and paste into your sales engagement tool.

To get started, create a new agent chat and describe your goal. The agent will draft `instructions`, suggest a `trigger`, and flag the access it needs.

PromptYou are an Outreach Sequencer for an AE/SDR team. When a new page is created in my Prospecting POVs database, read the POV, research the persona and topic, and create a new page in my Outbound Sequences database with a 9-step, 10-day multi-channel sequence (emails, cold call scripts, and LinkedIn messages), ready to paste into \[SALES ENGAGEMENT TOOL\]. Ground the writing in \[SALES METHODOLOGY\] and the example sequences already in the database. Use the persona’s language, not generic SaaS buzzwords. When the sequence is done, link it back to the original POV via the Outbound Sequences relation property.[Try it\!→](https://app.notion.com/?target=new_custom_agent&prefill=You%20are%20an%20Outreach%20Sequencer%20for%20an%20AE%2FSDR%20team.%20When%20a%20new%20page%20is%20created%20in%20my%20Prospecting%20POVs%20database%2C%20read%20the%20POV%2C%20research%20the%20persona%20and%20topic%2C%20and%20create%20a%20new%20page%20in%20my%20Outbound%20Sequences%20database%20with%20a%209-step%2C%2010-day%20multi-channel%20sequence%20(emails%2C%20cold%20call%20scripts%2C%20and%20LinkedIn%20messages)%2C%20ready%20to%20paste%20into%20%5BSALES%20ENGAGEMENT%20TOOL%5D.%20Ground%20the%20writing%20in%20%5BSALES%20METHODOLOGY%5D%20and%20the%20example%20sequences%20already%20in%20the%20database.%20Use%20the%20persona%E2%80%99s%20language%2C%20not%20generic%20SaaS%20buzzwords.%20When%20the%20sequence%20is%20done%2C%20link%20it%20back%20to%20the%20original%20POV%20via%20the%20Outbound%20Sequences%20relation%20property.)

### [3.1 Set the trigger](https://www.notion.com/help/guides/how-to-automate-sales-prospecting-in-notion-with-custom-agents#3.1-set-the-trigger)

This agent runs on a database event, not a schedule. The moment a POV is added to your Prospecting POVs database, the agent automatically kicks off.

1.  In your agent's settings, click `Add trigger`.

2.  Choose `Page added to database` and select your Prospecting POVs database.

3.  **\[Optional\]** Add a second trigger for `Page moved into database` so the agent also runs when you move an existing draft into the POV database.

4.  Click `Add trigger` to save.

Vídeo: https://www.youtube.com/watch?v=g1XSdDiBPvE&t=200s

Helpful tips

### [3.2 Check tools and access](https://www.notion.com/help/guides/how-to-automate-sales-prospecting-in-notion-with-custom-agents#3.2-check-tools-and-access)

Open `Tools and access` and connect the following:

1.  **Prospecting POVs database** (`read access`): so the agent can read each new POV when it triggers.

2.  **Sales methodology page and example sequences** (`read access`): to ground the writing in your team's frameworks and style.

3.  **Outbound Sequences database** (`edit access`): to create sequence pages and set properties like audience, persona, and status.

4.  **Prospecting POVs database** (`edit access`): to write back to the relation property once the sequence is created.

5.  **Web search** (`enabled`): to pull current context on the persona and topic.

Vídeo: https://www.youtube.com/watch?v=g1XSdDiBPvE&t=222s

Helpful tips

### [3.3 Test the agent](https://www.notion.com/help/guides/how-to-automate-sales-prospecting-in-notion-with-custom-agents#3.3-test-the-agent)

1.  Open one of the POV docs from Section 2 and start a test run: duplicate the POV into the database if your trigger is "page added," or set the status to `Ready for sequence` if you used a status trigger.

2.  Watch for the new sequence to appear in your Outbound Sequences database.

3.  Open it and review: does step 1 sound like the persona’s voice? Does each step add a new angle instead of restating the last one? Is the cold call script tight enough to read in 30 seconds? Is the breakup email respectful and final, not guilt-trippy?

4.  If anything is off, chat with the agent and ask it to update its instructions, then re-test.

Vídeo: https://www.youtube.com/watch?v=g1XSdDiBPvE&t=252s

As your product, audience, and messaging evolve, refresh your example sequences every quarter. The Outreach Sequencer learns from the strongest examples in your database, so adding new high-quality sequences helps keep its recommendations relevant and effective.

Most importantly, review the output regularly to catch signs that the agents are becoming generic, missing context, or drifting from your goals. A little maintenance goes a long way toward keeping the pipeline useful and trustworthy.

More resources

- For tips on keeping your agent sharp over time, check out our [Custom Agent best practices guide](https://www.notion.com/help/guides/best-practices-for-improving-your-custom-agent).

- For a deeper dive into Custom Agents, take our [course](https://academy.notion.com/page/notion-ai-catalogue) on Notion Academy.

- If you're connecting a custom MCP, review our help doc on [MCP connections for Custom Agents](https://www.notion.com/help/mcp-connections-for-custom-agents) to get it set up correctly.

Share this guide

------------------------------------------------------------------------
