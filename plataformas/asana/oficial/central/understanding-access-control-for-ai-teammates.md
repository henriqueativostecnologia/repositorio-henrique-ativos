---
fonte: https://help.asana.com/s/article/understanding-access-control-for-ai-teammates?language=en_US
baixado: 2026-11-10
---

# Understanding access control, memories, integrations, and approvals for AI Teammates and Dash

Maintaining security and privacy is just as important as the work itself, and AI Teammates and Dash are designed to follow the exact same rules as your colleagues. They operate within the boundaries of your existing permissions, ensuring they only see, search, or summarize the tasks and projects they’ve been explicitly invited to. By mirroring Asana’s standard access levels and using memories that respect your team's privacy, these help scale your productivity without ever overstepping your organization's data guardrails.

#### Related articles

- [AI Teammates](https://help.asana.com/s/article/ai-teammates)
- [Triggering AI Teammates](https://help.asana.com/s/article/triggering-ai-teammates)
- [Chat with Dash](https://help.asana.com/s/article/chat-with-dash)

## Access control for AI Teammates

When first created, AI Teammates can see public tasks and projects in the domain – just like new users. AI Teammates must be explicitly added as members or collaborators on private work graph objects (e.g., tasks, projects, teams) to see and search them. 

AI Teammates respect Asana's standard access levels:

| **Access level** | **What the Teammate can do**                                                           |
|:----------------:|----------------------------------------------------------------------------------------|
|    **Editor**    | Create, edit, and complete tasks; post comments; update custom fields; manage subtasks |
|  **Commenter**   | Post comments on tasks; cannot create or edit tasks                                    |
|    **Viewer**    | Read task information only; cannot comment or edit                                     |

 

> If an AI Teammate is added to a team, it will inherit the team’s access levels.

An AI Teammate cannot elevate its own permissions.

When you assign a task or ask a question to an AI Teammate, the AI Teammate will only respond using information from tasks, projects, and other objects that both you and the AI Teammate can access. AI Teammates can’t reveal information that you, as the “triggering” user, don’t already have permission to view.

For example, if you ask your AI Teammate to answer questions about a particular Asana project, they can only access and respond to you about that project if both of you have access to that project and/or its tasks. In other words, both you and your AI Teammate need to be authorized project members or task collaborators. 

> Keep in mind that AI Teammate comments are visible to everyone with access to that task. Before triggering a request, consider whether the audience in that context is appropriate for the content you're asking for.

### Details about access control

- AI Teammates see public Asana data by default, like any new user in your domain (e.g., tasks in public projects; projects in public teams).
- Requests involving or accessing information from third-party tools, such as Google Drive, use the triggering user’s access tokens.
- When creating or editing an AI Teammate, authorized members may upload key resources (e.g., playbooks, policies, instructions) for the AI Teammate's ongoing reference and access.

In practice, this means an AI Teammate cannot be used to look up information you do not already have access to. It can only work with the same tasks, projects, teams, and third-party files that you and the AI Teammate can both see.

If you want an AI Teammate to help on a private project or team, make sure it has been added as a member or collaborator, just as you would add a new colleague.

## Memories

To stay helpful over time, AI Teammates can remember important details about the work they have done. This section explains how those memories work and how they respect the same access controls as your tasks and projects.

After an interaction, an AI Teammate may store a memory for future reference. Memories are most commonly created during task executions, but can also be created when an AI Teammate reads key resources like documents. Think of memories as private notes that can only be viewed by users who can both see the associated object and trigger the AI Teammate.

### Details about memories

- Memories are stored on tasks as point-in-time recollections or summaries of interactions related to the task.
- A user who loses access to a task will also lose access to its memories.
- When an AI Teammate is removed from a project or task, the AI Teammate will forget the related memories.
- Memories can be viewed by authorized members of the AI Teammate on the AI Teammate’s profile page.
- A memory is only visible to users who already have permission to view the source task. For example, if a Teammate creates a memory from a private task, a colleague who cannot see that task will not be able to see the memory, even if they have full access to the Teammate.

Put simply, memories help an AI Teammate stay consistent with your preferences and past decisions, but they never widen access. Only people who can already see the underlying task and work with the AI Teammate can see its memories.

Over time, this lets teams build shared context with an AI Teammate so it can pick up work where it left off and avoid repeating the same questions, while still following your existing permissions.

## Integrations

In addition to reading your Asana workspace, AI Teammates and Asana Dash can connect to external tools to extend their capabilities.

At this time, all AI Teammate and Asana Dash integrations act on your behalf. When you trigger an [AI Teammate](https://help.asana.com/s/article/ai-teammates), or Asana Dash, it uses your own connected account for that tool, and its actions appear as though you performed them. An AI Teammate or Asana Dash can only see and do what you can already see and do in that tool, so it can never access content or take actions that you do not have permission for yourself. 

> Authorizing an integration for one Teammate grants access to that integration for all of your Teammates.

### Google Drive

AI Teammates and Asana Dash can read, search, edit, and create content in Google Drive, including:

- **Google Docs**: Read existing documents; create new documents; edit documents with content changes
- **Google Sheets**: Read spreadsheet data; create new spreadsheets; edit cell values
- **Google Slides**: Read slide content

### Gmail

AI Teammates Asana Dash can read, search, send, and organize email in Gmail, including:

- **Read and search**: Search your messages and threads using Gmail search syntax, open a full thread, summarize your unread inbox, and view or download attachments.
- **Draft and send**: Compose a new email, save a draft, reply, reply to all, or forward a message.
- **Organize**: Apply or remove labels, archive messages, mark them read or unread, and move messages to the trash.

> Asana's use and transfer of information received from Google APIs adheres to the [Google API Services User Data Policy](https://asana.com/terms/google-api), including the Limited Use requirements.

### Google Calendar

AI Teammates Asana Dash can view your calendar and manage events in Google Calendar, including:

- **View calendars and events**: List your calendars, list events in a date range, open the details of a single event, and suggest meeting times based on attendee availability.
- **Manage events**: Create events (including events with a Google Meet link), update event details such as time and attendees, delete events, and respond to invitations (accept, tentative, or decline) on your behalf.

### Outlook (Mail and Calendar)

AI Teammates Asana Dash can work with both Outlook Mail and Outlook Calendar.

#### Mail

- **Read and search**: Search your messages, open a specific message, and list recently sent items.
- **Draft and send**: Send an email, create or send a draft, reply, or reply to all.
- **Organize**: Set a message's category and importance, and move a message to Deleted Items (recoverable).

#### Calendar

- **View**: List events, view event occurrences across a date range, open a single event, check free/busy availability, and find meeting times.
- **Manage events**: Create events (including Teams online meetings), update events, cancel events (which notifies attendees), delete events you organized that have no attendees, and accept or decline invitations.

### Slack

AI Teammates Asana Dash can search, read, and post in Slack, including:

- **Search**: Search messages and files in public channels, find channels by name or description, and find people in your workspace.
- **Read**: Read messages in a specific channel or thread you have access to (including private channels and direct messages you belong to), read a user's profile, and read a canvas.
- **Post and create**: Send a message, save a draft, schedule a message for later, and create or update a canvas.

### Microsoft Teams

AI Teammates Asana Dash can search and send messages in Microsoft Teams, including:

 

- **Search and browse:** List the teams you've joined and the channels in a team, search messages across the teams and channels you have access to, and find people in your organization by their exact display name.

- **Send:** Post a message to a channel, or send a direct message to a person (a new 1:1 chat is created if one doesn't already exist). Messages can be plain text or formatted, and can @mention people.

### HubSpot

AI Teammates Asana Dash can read and write to your HubSpot CRM through HubSpot's MCP server, including:

- **CRM records**: Read contacts, companies, deals, tickets, products, line items, quotes, invoices, orders, subscriptions, and lists; create and update contacts, companies, deals, tickets, products, and line items.
- **Activities**: Read and log calls, emails, meetings, notes, and tasks tied to your CRM records.
- **Marketing and content**: Read campaigns, landing pages, site pages, blog posts, and marketing events.

Users will be asked to select permissions when they authorize the integration. The AI Teammate can only use the access they grant, and only within that user's own HubSpot permissions.

### Canva

AI Teammates Asana Dash can create, find, and export designs through Canva's MCP server, including:

- **Create and edit**: Generate new designs from a prompt (documents, presentations, social posts, videos, and more), edit existing designs, and autofill brand templates.
- **Find and organize**: Search designs by title, content, or metadata, browse folders, and view design details.
- **Export and comment**: Export designs as PDFs, images, or video, and add comments to a design.

Some capabilities (such as template autofill) depend on the user's Canva plan and on the admin enabling the AI Connector.

### Microsoft Office 365 (beta)

- Read, edit, and create new documents for SharePoint/OneDrive docx, pptx, and xlsx files.

To use SharePoint/OneDrive with an AI Teammate, the Teammate uses the credentials of collaborating users on the task. The collaborating user must have access to the relevant files.

### Web access

AI Teammates Asana Dash can read public web pages when given a URL. This is useful for:

- Researching topics or competitors
- Reading public documentation
- Pulling information from public data sources

## AI Teammate approvals

### Always requires approval

- Remove task collaborators - any removal is always gated
- Remove project members - any removal is always gated

### Requires approval based on conditions

|                             |                                                                                                      |                                                  |
|-----------------------------|------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| **Action**                  | **Approval bypassed when...**                                                                        | **Approval required when...**                    |
| Assign task                 | Assignee is null, or already has task access                                                         | Assignee would gain new read access to the task  |
| Create tasks with assignees | All assignees already have task access                                                               | Any assignee would gain new access               |
| Delete task                 | Teammate itself created the task                                                                     | Deleting a task created by someone else          |
| Add task to project         | Currently bypassed entirely (temporary flag \##TemporarilyAllowAiTeammateMultihomingWithoutApproval) | Would be required if task isn't public to domain |
| Add collaborators to task   | All added people already have task visibility                                                        | Any added person would gain new task visibility  |
| Add members to project      | Project is public to domain                                                                          | Project is private                               |
