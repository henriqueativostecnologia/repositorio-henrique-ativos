---
fonte: https://www.notion.com/help/connect-cursor-to-notion
baixado: 2026-11-10
---

# Use Cursor in Notion (beta)

In this help doc

## Connect Cursor to your Notion workspace and use it as an AI coding and productivity assistant.

[Jump to FAQs](https://www.notion.com/help/connect-cursor-to-notion#faq)

------------------------------------------------------------------------

**Note:** Cursor agents in Notion is currently in beta and subject to the beta terms of your agreement.

Cursor is a coding agent. When you connect it to Notion, you can use your workspace content as context for coding tasks without switching apps.

Cursor agents are different from [Custom Agents.](https://www.notion.com/help/custom-agents) They run on Cursor's infrastructure, but your work and results stay in Notion.

## [Who can use Cursor with Notion](https://www.notion.com/help/connect-cursor-to-notion#who-can-use-cursor-with-notion)

- This is available to all Cursor users with Notion Business and Enterprise plans.

- You must have a Cursor account and access to user API keys to use it.

- We're rolling this out gradually, so you might not see it right away.

## [What to know before you start](https://www.notion.com/help/connect-cursor-to-notion#what-to-know-before-you-start)

- Cursor runs the agent. Sessions happen entirely on Cursor's infrastructure.

- Cursor in Notion is available on desktop only.

- You'll need a Cursor account and a personal API key. If you can't create API keys, ask your workspace admin.

## [How billing works](https://www.notion.com/help/connect-cursor-to-notion#how-billing-works)

- Connecting Cursor to Notion is currently in beta and included in Business and Enterprise plans at no extra cost.

- Your Cursor usage is billed directly by Cursor through your own Cursor account.

## [Connect Cursor to Notion](https://www.notion.com/help/connect-cursor-to-notion#connect-cursor-to-notion)

1.  In Notion, go to `Agents` in the sidebar → `New Agent` → `Cursor`.

2.  Pick a starting point:

    - **Start with a default template:** Templates for common tasks (like Code Q&A and Bug Triage) can help you get started faster.

    - **Start from scratch:** Set up your own instructions, triggers, and connections.

3.  Enter your Cursor API key when prompted. Find it in your [Cursor account settings](https://cursor.com/settings).

4.  Set up triggers and schedules. [Learn more →](https://www.notion.com/help/custom-agents#configure-triggers-and-schedules)

## [What Cursor can do in Notion](https://www.notion.com/help/connect-cursor-to-notion#what-cursor-can-do-in-notion)

Once connected, Cursor can:

- **Find information in your workspace.** For example, pull up specs, meeting notes, or project docs while you work.

- **Create and update pages for you.** For example, write a new troubleshooting page or update an existing guide after you ship a change.

- **Answer questions about your work.** For example, ask "What's blocked?", "What's due this week?", or "Which tasks mention this project?"

- **Keep your workspace in sync as you code.** Store decisions, requirements, and notes in Notion so nothing gets lost between your code and your team.

## [How permissions work](https://www.notion.com/help/connect-cursor-to-notion#how-permissions-work)

- The connection is tied to your personal API key. This means Cursor access and activity are linked to your individual Cursor account, not the whole workspace. [Learn more →](https://cursor.com/docs/cli/reference/authentication#browser-authentication-recommended)

- Repos, environment, and connections come from your Cursor agent setup. Configure these in your [Cursor dashboard](https://cursor.com/dashboard/).

- Each Cursor agent can only access content it’s been shared on. Permissions are set per agent and aren’t inherited from whoever starts a run.

- Cursor agent permissions work the same way as Custom Agents. [Learn how agent permissions work →](https://www.notion.com/help/custom-agents-sharing-and-permissions#how-custom-agent-permissions-work)

- You can give different groups different levels of access. This includes can view and interact, can edit, or full access. [Learn more about access →](https://www.notion.com/help/custom-agents-sharing-and-permissions#who-can-access-your-custom-agent-and-its-resources)

## [Workspace admin controls](https://www.notion.com/help/connect-cursor-to-notion#workspace-admin-controls)

Workspace admins can switch off Cursor agents by going to `Settings` → `Notion AI` → `Agents` → `Manage external agents`.

------------------------------------------------------------------------

## FAQs

How is Cursor different from a Custom Agent?

Custom Agents are built and run entirely in Notion. Cursor agents run on Cursor's infrastructure, but you interact with them in Notion.

How does billing work? Does Cursor use Notion credits?

No. Cursor is billed through your own Cursor account. It doesn't use Notion credits.

Can I use my own billing?

Yes. Cursor billing always runs through your own Cursor account.

Where can I view my Cursor activity?

Results appear in Notion on the page or task where the agent ran. You can also find your chat sessions in the agent view in Notion, or in your Cursor dashboard. In your dashboard you can Filter → Source → API to see your chats.

Does Cursor in Notion support zero data retention (ZDR)?

Notion's own ZDR commitments don't cover Cursor agents. You configure your ZDR policy and relationship with Cursor. Sessions run on Cursor's infrastructure under Cursor's data handling policies.

## Contents

- [Who can use Cursor with Notion](#who-can-use-cursor-with-notion)
- [What to know before you start](#what-to-know-before-you-start)
- [How billing works](#how-billing-works)
- [Connect Cursor to Notion](#connect-cursor-to-notion)
- [What Cursor can do in Notion](#what-cursor-can-do-in-notion)
- [How permissions work](#how-permissions-work)
- [Workspace admin controls](#workspace-admin-controls)
