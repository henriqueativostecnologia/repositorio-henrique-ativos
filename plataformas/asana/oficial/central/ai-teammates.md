---
fonte: https://help.asana.com/s/article/ai-teammates?language=en_US
baixado: 2026-11-10
---

# AI Teammates

AI Teammates bring intelligent, context-aware support directly into your workflows. This article covers the basics of what AI Teammates can do and its elements.

#### Related articles

- [Triggering AI Teammates](https://help.asana.com/s/article/triggering-ai-teammates)
- [Understanding access control for AI Teammates](https://help.asana.com/s/article/understanding-access-control-for-ai-teammates)

## What are AI Teammates?

AI Teammates are collaborative, AI-powered agents built directly into Asana. AI Teammates are designed for teams, not just one person at a time. They build a shared memory of your organization’s language and processes, allowing multiple colleagues to assign them work, ask questions, and review their output. 

Here are some of the key ways AI Teammates work:

**Context:** AI Teammates navigate the Asana Work Graph to understand the relationships between your projects, tasks, goals, and portfolios. They can also read external content, such as Google Drive or SharePoint files. 

**Checkpoints:** They break complex work into subtasks and leave comments as they go, so your team can review drafts or request changes at any point.

**Control:** They follow the same access permissions as any other user in your domain. They can only see and use information for which they have explicit permission to access. See the [Access control for AI Teammates article](https://help.asana.com/s/article/understanding-access-control-for-ai-teammates) for more details.

Once set up, an AI Teammate can:

- Read and act on tasks, projects, goals, and portfolios
- Create, update, and complete tasks and subtasks
- Draft and edit documents in Google Drive and SharePoint
- Post comments and communicate with your team
- Search across your workspace for relevant information
- Follow the instructions you define to handle recurring workflows

## Anatomy of an AI Teammate and terminology

- **Name:** Your AI Teammate’s name.

- **Description:** Describes what your AI Teammate does. 

  - 💡*Tip: Your Teammate doesn’t read its own description; this field is for human colleagues. Use it to explain to your organization exactly how and when to use this Teammate. *

- **Behavior guidance:** Your AI Teammate’s personality: how it speaks (e.g., "favor concise bullet points"), thinks (e.g., "always flag when an assumption is being made"), and delivers work (e.g., "always draft long-form content directly in Google Docs").

  - 💡*Tip:* Don't worry about getting this right on day one. Teammates are designed to make smart inferences based on your goals. You can refine these instructions over time as you observe how your Teammate works.

- **Access:** What your AI Teammate can read/edit. Includes:

  - **Work:** Specific Asana projects and teams

  - **Attachments:** Public URLs or individual attachments selected from Google Drive or OneDrive/SharePoint.

  - **Apps:** General permissions to search and update across your linked Google Drive and OneDrive/SharePoint accounts.

  - *Note: During initial setup, you can grant your Teammate access to Asana data. To connect external sources like Google Drive, visit the Profile Page after your Teammate is created. *

  - **Memory:** Your AI Teammate’s persistent knowledge base that grows through every interaction. While you define behavior, the Teammate builds memory automatically to learn your preferences and retain context over time. You cannot manually create memories, but you can review and delete them to ensure your Teammate’s information remains accurate and relevant.

  - **💡 Privacy Note:** Memory visibility is strictly tied to Asana permissions. A user can only access a specific memory if they already have permission to view the source task it was created from.

- **Sharing:** Who can use your AI Teammate.

  - **💡Note:** The AI Teammate creator decides who can access it and at what level (admin, editor, user)

## Sharing AI Teammates

You can share AI teammates with your team or specific people. Only invited members can use the AI Teammate.

 

To share an AI Teammate:

1.  Click the **Share button** at the top right corner
2.  Type the name of the team or person
3.  Choose their access level
    - AI Teammate admin: Full access to change settings, modify, or delete the AI Teammate
    - Editor: Can modify and apply the AI Teammate to work
    - User: Can find and apply the AI Teammate to work
4.  Click **Invite**

To remove a team or person from the list of people with access, click the **Share button**, click the drop-down next to the name, and select **Remove from AI Teammate**.

## AI Studio and AI Teammates

AI Studio and AI Teammates are designed to work together. AI Studio helps you build automated workflows for high-volume, repeatable tasks. AI Teammates focus on collaborative work that requires context, judgment, and back-and-forth interaction.

One common pattern is to use AI Studio to collect and route requests into Asana as structured tasks, then involve an AI Teammate to handle the more complex work inside those tasks. For example, AI Studio might create and triage incoming campaign requests for a marketing team. A marketing AI Teammate can then draft briefs, summarize research, and prepare updates for those campaigns.

To learn more about AI Studio and how to build workflows, see the [AI Studio articles](https://help.asana.com/s/topic/0TOPc0000001Kw9OAE/asana-ai) in the Asana Help Center.

## What AI Teammates can and can't do today

### Invoking an AI Teammate

+----------------------------------------------------------+---------------------------------------+----------------------------------------------------------+
| **Capability**                                           | **Can an AI Teammate do this today?** | **Notes**                                                |
+----------------------------------------------------------+---------------------------------------+----------------------------------------------------------+
| Trigger on task assignment                               | ✅                                    |                                                          |
+----------------------------------------------------------+---------------------------------------+----------------------------------------------------------+
| Trigger on \@mention                                     | ✅                                    |                                                          |
+----------------------------------------------------------+---------------------------------------+----------------------------------------------------------+
| Trigger on updates to objects that the Teammate is a     | ✅                                    | If an AI Teammate is already a collaborator on a task or |
| collaborator on.                                         |                                       | project, updates to that work (like task completion or   |
|                                                          |                                       | key custom field changes) can trigger it to run again    |
|                                                          |                                       | and decide what follow‑up actions to take.               |
+----------------------------------------------------------+---------------------------------------+----------------------------------------------------------+
| Trigger via rule                                         | ✅                                    | If a Teammate is triggered via a rule, the Teammate runs |
|                                                          |                                       | on the access control of the rule owner unless otherwise |
|                                                          |                                       | specified at time of rule creation.                      |
+----------------------------------------------------------+---------------------------------------+----------------------------------------------------------+
| Trigger upon form submission                             | ✅                                    | Set your AI Teammate as the default assignee.            |
|                                                          |                                       |                                                          |
|                                                          |                                       | In this scenario, the AI Teammate uses the access        |
|                                                          |                                       | control of the form creator, or optionally the form      |
|                                                          |                                       | submitter for logged-in forms. This is customizable by   |
|                                                          |                                       | the form creator.                                        |
+----------------------------------------------------------+---------------------------------------+----------------------------------------------------------+
| Trigger via a recurring task                             | ✅                                    |                                                          |
+----------------------------------------------------------+---------------------------------------+----------------------------------------------------------+

### Searching the Work Graph

> For best results, tell your AI Teammate where and what to search for in its behavior guidance or in your prompts.

|                                                                                     |                                       |                                                                                                                                                                                                                                 |
|-------------------------------------------------------------------------------------|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Capability**                                                                      | **Can an AI Teammate do this today?** | **Notes**                                                                                                                                                                                                                       |
| Search public workspace data                                                        | ✅                                    |                                                                                                                                                                                                                                 |
| Search tasks                                                                        | ✅ - when it has access               |                                                                                                                                                                                                                                 |
| Search subtasks                                                                     | ✅ - when it has access               |                                                                                                                                                                                                                                 |
| Search projects and project updates                                                 | ✅ - when it has access               |                                                                                                                                                                                                                                 |
| Search milestones                                                                   | ✅ - when it has access               |                                                                                                                                                                                                                                 |
| Search portfolios                                                                   | ✅ - when it has access               |                                                                                                                                                                                                                                 |
| Search messages                                                                     | ✅ - when it has access               |                                                                                                                                                                                                                                 |
| Search comments                                                                     | ✅ - when it has access               |                                                                                                                                                                                                                                 |
| Search attachments                                                                  | ✅ - when it has access               |                                                                                                                                                                                                                                 |
| Search custom fields                                                                | ✅ - when it has access               |                                                                                                                                                                                                                                 |
| Search status updates                                                               | ✅ - when it has access               |                                                                                                                                                                                                                                 |
| Search goals and goal updates                                                       | ✅ - when it has access               |                                                                                                                                                                                                                                 |
| Search Reporting objects (dashboards)                                               | ✅                                    |                                                                                                                                                                                                                                 |
| Search Resourcing objects (capacity plans and workload views) that it has access to | ✅                                    |                                                                                                                                                                                                                                 |
| Search for objects it doesn't explicitly have access to within an interaction       | ❌                                    | AI Teammates can only interact with information if both the AI Teammate and the running user have access. See [Access control for AI Teammates](https://help.asana.com/s/article/ai-teammates#access-control-for-ai-teammates). |

### Updating the Work Graph

+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Capability**                                     | **Can an AI Teammate do this today?**              | **Notes**                                          |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Set name of task                                   | ✅                                                 | Can do for both existing tasks and tasks it        |
|                                                    |                                                    | created.                                           |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Mark a task complete                               | ✅                                                 | Can do for both existing tasks and tasks it        |
|                                                    |                                                    | created.                                           |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Set description of task                            | ✅                                                 | Can do for both existing tasks and tasks it        |
|                                                    |                                                    | created.                                           |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Add comments to a task                             | ✅                                                 | Can do for both existing tasks and tasks it        |
|                                                    |                                                    | created.                                           |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Create tasks and subtasks                          | ✅                                                 | AI Teammates can create tasks including titles,    |
|                                                    |                                                    | descriptions, assignees, and due dates.            |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Create subtasks                                    | ✅                                                 |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Edit tasks and subtasks                            | ✅                                                 | Edit titles, descriptions, assignees, and due      |
|                                                    |                                                    | dates on tasks it’s working with.                  |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | Start dates, task type, and approval status,       |
|                                                    |                                                    | cannot be updated on existing tasks.               |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Add comments to tasks and subtasks                 | ✅                                                 | AI Teammates use comments to summarize work,       |
|                                                    |                                                    | propose next steps, and draft plans/status         |
|                                                    |                                                    | updates.                                           |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | AI Teammates can edit and delete comments they     |
|                                                    |                                                    | wrote.                                             |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Delete tasks                                       | ✅ - requires approval if it was not the task      |                                                    |
|                                                    | creator                                            |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Assign tasks or subtasks to a user                 | ✅ - requires approval if the user is not already  | The AI Teammate can assign a task to a user on its |
|                                                    | a task collaborator or assignee                    | own if the user already has access to the task. If |
|                                                    |                                                    | the user does not have access to the task, the AI  |
|                                                    |                                                    | Teammate will ask the running user for approval.   |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Update value of an existing project custom field   | ✅                                                 |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Add task to a project                              | ✅ - requires approval if AI Teammate is not an    |                                                    |
|                                                    | editor in the project                              |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Add or remove task collaborators                   | ✅ - requires approval                             |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Create projects                                    | ✅                                                 |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Create or update sections                          | ✅                                                 | AI Teammates can create or reorder sections, but   |
|                                                    |                                                    | not rename or delete them.                         |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Bulk update tasks                                  | ✅                                                 |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Create dependencies                                | ✅                                                 |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Create milestones                                  | ✅                                                 |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Merge duplicate tasks                              | ✅                                                 |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Create Asana Pages                                 | ✅                                                 |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Create, update, and delete record items in Asana   | ✅                                                 |                                                    |
| Tables                                             |                                                    |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Create capacity plans and workloads; read effort   | ✅                                                 |                                                    |
| graph data; create, update, delete allocations     |                                                    |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Create goals                                       | ❌                                                 |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Create a custom field                              | ❌                                                 |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Remove task from a project                         | ❌                                                 |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Send messages or status updates                    | ❌                                                 |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Create dashboards or charts                        | ❌                                                 |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Add or remove users from Work Graph objects        | ❌                                                 | Approval required for non-public projects;         |
|                                                    |                                                    | removing members always requires approval.         |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+

### External tools and files

Learn more about [AI Teammate integrations](https://help.asana.com/s/article/understanding-access-control-for-ai-teammates?language=en_US#integrations).

+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Capability**                                     | **Can an AI Teammate do this today?**              | **Notes**                                          |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Generate external files                            | ✅, except Google Slides                           | AI Teammates can create new documents for Google   |
|                                                    |                                                    | Docs and Sheets, as well as for                    |
|                                                    |                                                    | Sharepoint/OneDrive files (docx, pptx, and xlsx).  |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Search external files (images, PDFs, documents,    | ✅ - if both the acting user and the AI Teammate   | AI Teammates can read Google Drive files (docs,    |
| slides, and sheets)                                | have access                                        | sheets, and slides), as well as                    |
|                                                    |                                                    | Sharepoint/OneDrive files (docx, pptx, and         |
|                                                    |                                                    | xlsx).                                             |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | The AI Teammate uses the running user’s            |
|                                                    |                                                    | authentication to access external tools. The       |
|                                                    |                                                    | running user must grant the AI Teammate access on  |
|                                                    |                                                    | the Profile page or when the request is triggered. |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Read images and attachments on a task              | ✅                                                 |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Attach a file to a task                            | ✅                                                 |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Gmail                                              | ✅                                                 | Search, read, draft, send (w/ approval), reply,    |
|                                                    |                                                    | forward, labels, trash                             |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Google Calendar                                    | ✅                                                 | Read, suggest times, create/update events, RSVP,   |
|                                                    |                                                    | delete (w/ approval)                               |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Microsoft Outlook Mail                             | ✅                                                 | Read, search, draft, send (w/ approval), reply,    |
|                                                    |                                                    | delete (w/ approval)                               |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Microsoft Outlook Calendar                         | ✅                                                 | Read, create/update, delete (w/ approval)          |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Slack                                              | ✅                                                 | Search/read messages, send/schedule messages,      |
|                                                    |                                                    | manage canvases                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| HubSpot                                            | ✅                                                 | Read/write CRM records (contacts, companies,       |
|                                                    |                                                    | deals, etc.)                                       |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Canva                                              | ✅                                                 | Create/search/edit designs                         |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Microsoft Teams                                    | ✅                                                 | Search messages, send channel/direct messages      |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Web search & browsing                              | ✅                                                 | Public web search, read public URLs                |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Generate images or PDFs                            | ❌                                                 |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+

### Access, safety, and usage

|                    |                                       |           |
|--------------------|---------------------------------------|-----------|
| **Capability**     | **Can an AI Teammate do this today?** | **Notes** |
| Bypass permissions | ❌                                    |           |

## How do I turn off AI Teammates?

Who can use AI Teammates is determined at the individual user level. Users who have access to consume AI requests will be able to use AI Teammates, while users who have this permission disabled will not.

To update this setting for a specific user, navigate to the admin console, select **Users**, and click into the **Licenses** column. Under the **AI spending** subheading, you will be able to toggle on or off the user's ability to consume AI requests, which will control the user's ability to use AI Teammates.

If you wish to update this control for multiple users at once, you can use the Import/Export CSV functionality to update users in bulk.
