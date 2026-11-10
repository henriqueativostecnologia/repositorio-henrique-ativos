---
fonte: https://www.notion.com/help/guides/manage-your-inbox-and-calendar-with-custom-agents
baixado: 2026-11-10
---

# Manage your inbox and calendar automatically with Custom Agents

## Custom Agents can manage your mail and calendar automatically, so you spend less time on coordination and more time on the work that matters.

- Notion Calendar
- Notion Mail

8 min read

------------------------------------------------------------------------

Between email and meetings, there’s a lot of coordination that falls through the cracks. You meant to send that follow-up. You forgot to block time for deep work. The prep doc never got shared before the call.

Custom Agents can connect to your email and calendar to handle these workflows automatically.

**In this guide, you’ll learn how to:**

- Set up an Inbox Organizer Agent to triage and organize your inbox

- Create a Calendar Optimizer Agent to protect your time and focus

- Set up a Team Scheduler Agent to coordinate meetings across people

- Connect agents together to create end-to-end workflows

New to Custom Agents?

## [Connect your email and calendar accounts](https://www.notion.com/help/guides/manage-your-inbox-and-calendar-with-custom-agents#connect-your-email-and-calendar-accounts)

Custom Agents work with email (Gmail, iCloud, Notion Mail, or Outlook) and calendar (Google Calendar, iCloud, or Notion Calendar) to read and send emails, view and create calendar events, and take actions based on your schedule.

When an agent requires email or calendar access, you’ll see options to `connect` Mail or Calendar under `Tools and access`, and sometimes directly within the chat.

Want to learn more about Notion Mail and Notion Calendar?

## [Manage your emails with an Inbox Organizer agent](https://www.notion.com/help/guides/manage-your-inbox-and-calendar-with-custom-agents#manage-your-emails-with-an-inbox-organizer-agent)

An Inbox Organizer Agent helps you stay on top of email without living in your inbox. It can sort and label messages, draft replies for your review, and even turn important emails into Notion database entries.

You can use one of our [pre-built templates](https://www.notion.so/agent/2e7efdeead0580d9ac1b0092b49f2f06?wfv=settings) or build an agent from scratch. Head to the `Agents` section in your workspace sidebar and click `+ New agent`. Tell it what you want in simple language:

*“Check my email every morning. Sort messages using my labels, draft replies for anything that needs a response, and flag anything sensitive for my review.”*

### [1) Choose when it runs (trigger)](https://www.notion.com/help/guides/manage-your-inbox-and-calendar-with-custom-agents#1)-choose-when-it-runs-(trigger))

By default, an Inbox Organizer works best on a schedule so you start the day with a clean inbox. You can also set it to run when new emails arrive if you want real-time triage.

How to set the right trigger

### [2) Triage and organize](https://www.notion.com/help/guides/manage-your-inbox-and-calendar-with-custom-agents#2)-triage-and-organize)

Start by telling your agent what to do with common categories of emails. For example: *“Archive newsletters and promotional emails automatically. Flag anything from my direct reports as high priority. If an email looks like a request that needs a reply, label it for me.”*

Here’s one simple labeling system you can use:

- Needs a response: Label as **01. Reply**

- Waiting on someone else: Label as **02. Follow up**

- Important notifications that require action: Label as **03. Important notifications**

- Automated/system alerts: Label as **04. Notifications**

- Newsletters/promotions: Label as **05. Marketing**

### [3) Draft replies](https://www.notion.com/help/guides/manage-your-inbox-and-calendar-with-custom-agents#3)-draft-replies)

Once triage is working, ask your agent to draft responses for anything labeled **01. Reply**—so you can scan, tweak, and send replies if needed.

For example: *“For any email labeled 01. Reply, draft a response. Keep it concise, include a quick recap of what I’m responding to, and end with a clear next step. Leave anything sensitive as a draft for my review.”*

Drafts will appear in your connected email client.

You can also add style guidelines, like:

- Keep paragraphs short and scannable

- Personalize with names/companies when available

- Follow a linked tone/voice guide

### [4) Import to Notion](https://www.notion.com/help/guides/manage-your-inbox-and-calendar-with-custom-agents#4)-import-to-notion)

If you want your inbox to feed directly into your workflows, you can have your agent turn certain emails into database entries. For example, automatically update your CRM with new prospect information or add project requests straight into your task tracker.

Ask, *“When someone emails me a project request, add it to my @Project Requests database with the sender, deadline, and key requirements from the email.”*

When you’re finished configuring the agent in chat, save the agent instructions to apply your changes.

## [Create a Custom Agent that manages your calendar](https://www.notion.com/help/guides/manage-your-inbox-and-calendar-with-custom-agents#create-a-custom-agent-that-manages-your-calendar)

A Calendar Optimizer Agent helps you stay ahead of your schedule—catching conflicts, protecting focus time, and keeping busy weeks from spiraling.

Start with a pre-built template \<deep-link\>, or simply describe what you want in chat. For example:

*“Create a Calendar Optimizer that checks for conflicts and overloaded days, recommends what to keep or move, and suggests a few alternate time slots when something needs rescheduling.”*

From there, shape it around how you actually work. Your agent can:

### [1) Spot conflicts and fix them fast](https://www.notion.com/help/guides/manage-your-inbox-and-calendar-with-custom-agents#1)-spot-conflicts-and-fix-them-fast)

Instead of reacting to meetings one by one, your agent can scan ahead and surface what needs attention.

It can:

- Flag real conflicts (not focus blocks or reminders)

- Highlight what matters most—like external calls, manager meetings, or priority projects

- Recommend which meetings to move first when days get overloaded

- Suggest a few realistic alternate time slots when something needs to shift

### [2) Handle meeting-heavy days](https://www.notion.com/help/guides/manage-your-inbox-and-calendar-with-custom-agents#2)-handle-meeting-heavy-days)

Once your calendar is lighter, your agent can help you use that space intentionally.

Ask it to:

- Find meaningful focus blocks (30–120 minutes, not tiny gaps)

- Pull in high-priority tasks from where you track work

- Propose a realistic plan for the week before making any changes

### [3) Turn open time into a real plan](https://www.notion.com/help/guides/manage-your-inbox-and-calendar-with-custom-agents#3)-turn-open-time-into-a-real-plan)

Once the basics feel right, layer in simple preferences that guide how your agent makes decisions:

- **Use meaningful time blocks:** Ask it to look for existing focus blocks first, then open gaps of at least 30 minutes—ideally one to two hours.

- **Plan from real priorities:** Tell your agent where you track tasks (like @My Tasks or @Project Tracker) so it schedules high-priority work into your best focus windows.

- **Suggest before changing:** Propose time slots and due dates, but wait for approval before updating meetings or tasks.

### [4) Use filters to keep triggers focused](https://www.notion.com/help/guides/manage-your-inbox-and-calendar-with-custom-agents#4)-use-filters-to-keep-triggers-focused)

Once your agent knows what to look for, the next step is deciding *when* it should run.

In most cases, calendar agents work best when they scan ahead in batches, such as daily or over the next few days, instead of reacting to every small calendar change. This keeps recommendations helpful rather than noisy.

When you use event-based triggers like **Event created** or **Event updated**, adding a few simple filters can make a big difference.

Here are the most useful ones to start with:

- **Title:** Run only for specific meeting types

  *Example: contains “1:1”, “Interview”, or “Customer”*

- **Organizer email:** Trigger only for events created by you or a coordinator you trust

- **Participant emails:** Act when certain teammates or clients are included

- **Participant RSVP status:** Wait until key attendees accept before running

- **All-day events:** Exclude PTO and holidays to avoid unnecessary runs

- **Busy status:** Focus on real commitments instead of “Free” placeholders

## [Set up a Custom Agent to coordinate meetings](https://www.notion.com/help/guides/manage-your-inbox-and-calendar-with-custom-agents#set-up-a-custom-agent-to-coordinate-meetings)

A Team Scheduler Agent can find times for meetings across multiple participants by checking availability, respecting working hours and time zones, and handling the coordination.

This works best when you have access to participant calendars (like in Google Workspace) and give your agent permission to view team calendars. Without calendar access, your agent can make general recommendations but won’t be able to see actual availability to confirm meeting times.

For example, ask your agent to:

*“Build a scheduling agent that finds time for meetings across my team, respects everyone’s working hours, and adds confirmed meetings to my @Team Meetings database.”*

As you refine it, get specific about your preferences. Your agent can help to:

- **Find the best slots:** Propose 2–3 options that work across attendees (and time zones), rather than a single time.

- **Respect boundaries:** Only suggest times within working hours, and add buffer time before/after meetings when possible.

- **Handle conflicts:** If there’s no perfect time, pick the lightest-conflict option and explain what it would interrupt.

### [Choose when your agent runs with triggers](https://www.notion.com/help/guides/manage-your-inbox-and-calendar-with-custom-agents#choose-when-your-agent-runs-with-triggers)

A Team Scheduler is most useful when it can react to scheduling changes as they happen.

- **Event-driven triggers** run when meetings are created or updated, which is ideal for real-time scheduling and coordination.

- **Daily or weekly schedules** work best when you want a batch view of upcoming scheduling needs.

If there are scheduling conflicts and you need to coordinate with others, have the agent help you move things forward:

- **Draft a message you can send** (email or chat) with 2–3 proposed time options and a clear next step.

- **Create the calendar event** once a time is confirmed by adding it to everyone’s calendars.

You can also layer on automations: *“When a meeting is confirmed, create a page in my @Team Meetings database with the attendees and agenda.”*

## [Stack your Custom Agents together](https://www.notion.com/help/guides/manage-your-inbox-and-calendar-with-custom-agents#stack-your-custom-agents-together)

Once each Custom Agent is working on its own, they become more powerful together. For example:

- An email comes in asking for a meeting → **Inbox Organizer** flags it as “needs scheduling.”

- You ask **Team Scheduler** to find a time → it checks everyone’s availability and proposes options.

- **Calendar Optimizer** notices you’re overbooked that week → it suggests moving a lower-priority meeting to make room for this call.

Each Custom Agent handles its part of the workflow, and together they keep your inbox and calendar under control without constant manual effort.

More resources

- Check out our help article on using [Custom Agents with Mail](https://www.notion.com/help/connect-mail-to-custom-agents)

- Explore our help article on using [Custom Agents with Calendar](https://www.notion.com/help/connect-calendar-to-custom-agents)

- Learn more about sharing [Custom Agents and managing permissions](http://notion.com/help/custom-agents-sharing-and-permissions)

Share this guide

------------------------------------------------------------------------
