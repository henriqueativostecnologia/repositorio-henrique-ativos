---
fonte: https://www.notion.com/help/guides/automate-project-updates-and-reporting-with-custom-agents
baixado: 2026-11-10
---

# Automate project updates and reporting with Custom Agents

## Learn how to build a Custom Agent that handles the busywork of weekly project updates, from triaging new bugs and requests to drafting a report that's ready to share.

5 min read

Vídeo: https://www.youtube.com/watch?v=fcfbAAczSJg

------------------------------------------------------------------------

## [What you’ll build](https://www.notion.com/help/guides/automate-project-updates-and-reporting-with-custom-agents#what-you%E2%80%99ll-build)

A Custom Agent that handles two recurring jobs. First, it watches your feedback channel and files new bugs and feature requests as tasks in your project database. Then each week, it drafts a project update from that same database, saves it to your Weekly Updates database, and posts a short Slack summary. You spend less time stitching together updates and more time moving the project forward.

### [Who this is for](https://www.notion.com/help/guides/automate-project-updates-and-reporting-with-custom-agents#who-this-is-for)

Project and program managers, product leads, and team leads who own a recurring status update.

PromptCreate a weekly project update for my team, add each report to the Weekly Updates database, and post a short Slack summary to \#project-bolt whenever a new report is published. Each update should include highlights, progress, risks and blockers, next week priorities, and any relevant links.[Try it\!→](https://app.notion.com/?target=new_custom_agent&prefill=Create%20a%20weekly%20project%20update%20for%20my%20team%2C%20add%20each%20report%20to%20the%20Weekly%20Updates%20database%2C%20and%20post%20a%20short%20Slack%20summary%20to%20%23project-bolt%20whenever%20a%20new%20report%20is%20published.%20Each%20update%20should%20include%20highlights%2C%20progress%2C%20risks%20and%20blockers%2C%20next%20week%20priorities%2C%20and%20any%20relevant%20links.)

## [1. Prompt the agent](https://www.notion.com/help/guides/automate-project-updates-and-reporting-with-custom-agents#1.-prompt-the-agent)

In this step, you'll set the agent's foundation: where to watch for incoming requests, what to do with them, and the guardrails that keep things consistent.

1.  In your sidebar, open `Agents` and click `New agent` to start a new chat.

2.  Describe what you want the agent to do (the *Try this prompt* callout above is a good starting point). @-mention your project database and your \#user-feedback Slack channel so the agent knows where to read from and where to file new tasks.

3.  Answer any follow-up questions the agent asks in chat, like confirming which database is your project tracker.

4.  The agent will draft `Instructions`, suggest `Triggers`, and flag the `Tools and access` it needs. You'll fine-tune each of these in the next steps.

Vídeo: https://www.youtube.com/watch?v=fcfbAAczSJg&t=31s

Helpful tips

## [2. Automate task assignments](https://www.notion.com/help/guides/automate-project-updates-and-reporting-with-custom-agents#2.-automate-task-assignments)

In this step, you’ll teach the agent what to do with each new task: who owns it and what status it lands in.

1.  In the same chat, tell the agent to set you as the assignee on any new task it files from \#user-feedback.

2.  Then tell it to move the status from `New` to `Assigned` so the rest of the team knows the task has been picked up.

3.  Click `Save` once the agent has updated its instructions. This way when you post a new message in \#user-feedback, a matching task appears in your project database, assigned to you, with status set to `Assigned`.

Vídeo: https://www.youtube.com/watch?v=fcfbAAczSJg&t=108s

Helpful tips

## [3. Draft the weekly update](https://www.notion.com/help/guides/automate-project-updates-and-reporting-with-custom-agents#3.-draft-the-weekly-update)

With triage handled, the next part is the weekly update itself: where the agent drafts it, where it saves it, and when it shares it.

1.  In the same chat, tell the agent to draft a weekly project update for your team using the work in your project database.

2.  Tell it to save each draft to the Weekly Updates database as a new page.

3.  Tell it to post a short summary to \#project-bolt when a report’s status changes to `Published`, so you can review and edit each draft before it goes out.

4.  Click `Save` once the agent has updated its instructions. From now on, the agent will draft a new report each week and post a Slack summary to \#project-bolt the moment you change its status to `Published`.

Vídeo: https://www.youtube.com/watch?v=fcfbAAczSJg&t=226s

Helpful tips

## [4. Set formatting guidelines](https://www.notion.com/help/guides/automate-project-updates-and-reporting-with-custom-agents#4.-set-formatting-guidelines)

Without a set structure, the agent may improvise and every weekly update will look a little different. Define the sections once so each report comes out predictable and easy to skim.

1.  In the same chat, tell the agent to format each weekly report with these sections:

    - **Current status** so your team can quickly see where things stand.

    - **Open action items** to call out what's still in flight.

    - **Blockers** so risks don't get buried.

    - **Next milestones** to keep everyone looking ahead.

2.  Then tell it to format each Slack summary as 2–3 highlights with a link back to the full update in Notion.

3.  Click `Save` once the agent has updated its instructions.

Vídeo: https://www.youtube.com/watch?v=fcfbAAczSJg&t=310s

Helpful tips

## [5. Test your agent](https://www.notion.com/help/guides/automate-project-updates-and-reporting-with-custom-agents#5.-test-your-agent)

Before going live, run a quick end-to-end test on both workflows: bug-to-task and weekly update. This way you catch any wiring issues before the agent runs on its own schedule.

1.  Open your agent's `Triggers` panel and confirm both triggers are toggled `on`. If either is off, turn it on now. A saved agent won't run if its triggers are disabled.

2.  Test the bug-to-task workflow:

    - Post a test message in \#user-feedback (e.g., "Bug: settings page won't load on mobile").

    - Open your project database and confirm a matching task appears, assigned to you, with status

      `Assigned`.

3.  Test the weekly update workflow:

    - Open your Weekly Updates database and find a draft the agent has created. (If there isn't one yet, ask the agent in chat to generate one.)

    - Change its status to `Published`.

    - Check \#project-bolt for a Slack summary with a link back to the full update.

Vídeo: https://www.youtube.com/watch?v=fcfbAAczSJg&t=372s

Helpful tips

## [How to maintain your Custom Agent](https://www.notion.com/help/guides/automate-project-updates-and-reporting-with-custom-agents#how-to-maintain-your-custom-agent)

Here are a few best practices to keep your agent reliable as your project evolves:

- **Share access intentionally:** Sharing the agent can also share what it has access to. Review the `Tools and access` panel before adding new viewers.

- **Set expectations with your team:** Let stakeholders know when to expect updates and where to find them.

- **Layer in new behavior:** Add to the agent's setup instead of swapping pieces out. If your execs sit in a different Slack channel, add a second posting destination alongside the existing one.

- **Refine instructions over time:** The agent gets better through conversation, not rewrites. If bug reports lose detail, ask it to tighten its instructions rather than starting over.

- **Re-test after database changes:** A renamed property or new status option can quietly break the agent's logic. Run a quick test on both triggers before the next real run.

More resources

- For tips on keeping your agent sharp over time, check out our [Custom Agent best practices guide](https://www.notion.com/help/guides/best-practices-for-improving-your-custom-agent).

- For a deeper dive into Custom Agents, take our [course](https://academy.notion.com/page/notion-ai-catalogue) on Notion Academy.

Share this guide

------------------------------------------------------------------------
