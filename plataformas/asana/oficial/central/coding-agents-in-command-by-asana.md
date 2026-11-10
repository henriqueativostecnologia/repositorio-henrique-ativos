---
fonte: https://help.asana.com/s/article/coding-agents-in-command-by-asana?language=en_US
baixado: 2026-11-10
---

# Coding agents in Command by Asana

> **This feature is in Early Access and is only available to select customers.**

Coding agents in Command by Asana help you delegate well-scoped coding tasks to an AI-powered agent — Cursor or Copilot — directly from a ticket. Setting up a coding agent happens in three stages: a domain admin enables the integration, each user connects their own account, and teamspaces set defaults. Delegating a ticket and managing the resulting session work the same way across agents, with one exception noted below.

## Set up the integration

A domain admin enables coding agent integrations for the whole org.

1.  Switch to Command mode.
2.  In the side panel, select **Admin**. This option only appears for domain admins.
3.  Enable the integrations you want to make available: **Cursor** and/or **Copilot**.

## Connect your account

**Available for: Cursor, Copilot**

Once an integration is enabled, each user needs to connect their own account before they can run sessions — for example, by being assigned a ticket or @mentioned in a comment.

1.  Click your user avatar, then select **Settings**.
2.  Select **Apps**.
3.  Find the integration you want to connect (**Cursor** or **Copilot**) and configure it with a personal access token (PAT) or API key, depending on the agent provider.
4.  Repeat for each coding agent you plan to use.

## Set teamspace defaults

**Available for: Cursor, Copilot**

Teamspace settings control the default model and repository used when a session starts from a ticket in that teamspace.

1.  Click the three-dot icon at the top-right corner.
2.  Select **Teamspace settings**, then select **Integrations**.
3.  Find the integration you want to configure (**Cursor** or **Copilot**).
4.  Select a **Default model** from the picker. You can keep the default model if it meets your needs.
5.  Select a **Default repository** from the picker. For example, choose the repository that contains the code you want the agent to work with.
6.  Specify a branch if needed

## Delegate a ticket to a coding agent

**Available for: Cursor, Copilot**

You can delegate a ticket to any connected coding agent by assigning the ticket to the agent, by @mentioning the agent in a comment with your instructions, or by clicking **Start session** on the **AI Agents widget** on the ticket.. Use a focused request, such as asking the agent to fix a straightforward bug.

> The widget shows that the session is launching and indicates which agent the ticket was delegated to. Session startup may take some time.

To delegate from a comment, open the ticket, add your instructions, and @mention the agent — for example, **@Cursor** or **@Copilot**. For example, write "@Copilot, work on this" after describing the requested change. You can also use the direct delegation option (assigning the ticket to the agent) if it's available on the ticket.

## Open the session

**Available for: Cursor**

Opening the resulting session directly from Command is currently only available for Cursor.

When a Cursor session starts, the ticket displays a message that your session is ready. You can open the session in either of two ways:

1.  In the **AI Agents widget**, select the session, then click **Continue in Cursor**.
2.  In the comment that confirms the session is ready, click **Continue in Cursor**.

Both options open the Cursor session associated with the ticket.
