---
fonte: https://help.asana.com/s/article/ai-studio-connect-your-smart-workflow?language=en_US
baixado: 2026-11-10
---

# Connect your Smart workflow with the right data sources

**AI Studio is available on [Starter](https://asana.com/plan/starter), [Advanced,](https://asana.com/plan/advanced) [Enterprise](https://asana.com/enterprise), and [Enterprise+](https://asana.com/enterprise) plans**. **Visit [asana.com/ai](https://asana.com/ai) to learn more about the launch of Asana AI Studio. **

Understanding what data is available to Asana AI helps you create more effective and transparent Smart workflows. This article explains how to give your Smart workflows access to the right data using @mentions, attachments, and permissions settings in AI Studio. If you’d like to go further, you can also earn the [AI Studio Foundations skill badge](https://academy.asana.com/ai-studio-foundations-skill-badge) in the Asana Academy. You’ll learn how to write effective prompts, plan Smart workflows, and troubleshoot common issues.

By default, Asana AI has access to the task that triggers the rule and the project in which the rule lives. Beyond that, AI Studio creators have control over which additional information their Smart workflow can access, such as tasks, projects, portfolios, goals and attachments. The information below explains how to manage that access effectively.

#### Related articles

- [Introduction to Asana AI Studio](https://help.asana.com/s/article/ai-studio)
- [Create Smart workflows with AI Studio](https://help.asana.com/s/article/ai-studio-smart-workflows)
- [Writing instructions in AI Studio](https://help.asana.com/s/article/writing-ai-studio-instructions)
- [AI Studio - Human in the loop](https://help.asana.com/s/article/ai-studio-human-in-the-loop)
- [How the Use AI variable works](https://help.asana.com/s/article/ai-studio-use-ai)
- [Troubleshooting in AI Studio](https://help.asana.com/s/article/ai-studio-troubleshooting)

## How to @mention work when writing prompts

When we talk about @mentioning work in the instructions of your Smart workflow, we're referring to the process of @mentioning, whereby builders type the @ symbol followed by the name of any of the following work items: a task, project, team, portfolio, goal, universal workload, or person.

@mentioning work in the instructions will give the Smart workflow access to read the information contained within the @mentioned work item. You have control over how much data can be accessed by Smart workflows built using AI Studio; the **Data and permissions** section of the AI Settings pane, explained later in this article, contains various settings which help you give your Smart workflow access to the information it needs, and nothing more.

Reminder: By default, a Smart workflow has access to only two things:

- The information contained in the task which triggers the rule
- Information from the project that the rule lives in and the tasks in that project

Any other information (tasks, projects, etc.) must be explicitly @mentioned in the AI instructions.

### @mentioning tasks

When you @mention tasks in your instructions, you allow the workflow to read the information contained within that task, including task data and user-generated content (title, description, assignee, etc.). You have further control over task data in the **Data and permissions** section of the AI settings pane.

Check the section titled **AI will be able to see these contents** at the bottom of the instructions pane to make sure your Smart workflow can access the desired tasks.

### @mentioning projects

When you @mention a project in your instructions, the Smart workflow is allowed to read tasks from that project based on the setting you choose under the **Data and permissions** section of the AI settings. This is discussed in further detail later in this article, but you can choose your Smart workflow's level of access to the tasks contained in those projects, or restrict it to project names only, and no task information.

Check the section titled **AI will be able to see these contents** at the bottom of the instructions pane to make sure your Smart workflow can access the project information you want it to.

### @mentioning teams or users

AI Studio supports the @mentioning of teams in a Smart workflow's instructions. When you @mention a team in your instructions, you provide access to the following:

- The names of up to 200 team members
- The names of the team admins
- Job title
- Custom fields on team members 

This makes it possible to use a Smart workflow to add members of a team as collaborators on a task, or assign a task to a team admin based on specific instructions.

### @mentioning portfolios

When you @mention a portfolio in your instructions, your Smart workflow can access portfolio information,information about the projects contained within the portfolio, and the tasks contained within those projects. Portfolio information refers to 

- Name 
- Owner 
- Members 
- Last Status Update 
- Project-level custom fields added to the portfolio

@mentioning a portfolio will provide access to the tasks within the portfolio's projects by default, but you can reduce access to include task information by selecting **Project names** from the **Data to use from projects @mentioned in instructions** dropdown within the AI Studio settings when creating your rule. If only **Project names** is selected, no task data is read by the Smart workflow from within those projects.

@mention a portfolio to allow AI Studio to multi-home a task into the correct project within a portfolio, or find tasks across multiple projects in a portfolio.

### @mentioning goals

When you @mention a goal in your instructions, your Smart workflow can access goal information including:

- Name
- Owner
- Date range 
- Description
- Status
- Time period 
- Status updates 
- Sub goals
- Some information from linked projects (name, team, owner, last status update) 

This allows AI Studio to check if the input task is related to a specific goal and can make use of goal information as part of its overall context.

### Referencing universal workload

Universal workload does not currently support @mentioning in AI Studio instructions, but universal workload can still be referenced by pasting the workload URL into the instructions window. This allows AI Studio to reference the workload information and assign the input task to the right person, based on their capacity and workload.

Note that it is possible to reference universal workload specifically, and not project or portfolio workload

## Adding attachments and providing context

There are a few ways to provide your Smart workflow with additional context, so that it has all the information needed to perform its tasks:

- Simply write the context directly into the AI instructions
- Attach files directly to the Smart workflow's AI instructions
- Attach files to the task which triggers the rule
- Attach files to tasks within @mentioned projects and portfolios 

Each approach has its merits, and the best choice depends on the specific requirements of your Smart workflow.

### Writing context directly into AI instructions

Writing context into AI instructions directly is suitable for brief, unchanging guidelines.

Sometimes the simplest approach is to include reference information directly in your instructions. This works well for shorter guidelines, criteria, or examples that can be explained well in text format.

For example, you could write a list of predefined ticket categories such as **Billing**, **Technical**, or **Feature request** directly into the AI instructions, providing brief descriptions for each. The descriptions of these categories will not change, and so a Smart workflow can reference this context when categorizing tickets.

##

### Attaching files directly to AI instructions

Attaching files to a Smart workflow's AI instructions is the ideal approach when using consistent reference materials.

Files attached directly to your AI instructions are available every time the workflow runs, regardless of which task triggers it. Use this approach for reference materials, guidelines, or examples that should inform every execution of the workflow.

For example, consider attaching your brand guidelines PDF directly to the AI instructions so that every time the workflow runs, it references consistent rules for tone, style, and content creation standards.

### Attaching files to tasks

Useful context often lives in documents and files that originate outside of Asana. Attaching these files directly to a task ensures the most relevant context stays with the work.

When a Smart workflow runs on a task with attachments, it can access those files to inform its decisions. This is ideal for workflows that need to analyze documents specific to each task.

For example, if weekly meeting notes are attached to a task, the workflow can extract key details such as action items from that specific meeting. This ensures the workflow tailors its output to the unique context of each meeting, each week.

### Attaching files to tasks within @mentioned projects and portfolios

Useful context often lives in documents and files that originate outside of Asana. Attaching these files directly to a task ensures the most relevant context stays with the work. 

When a project or portfolio is @mentioned in a Smart Workflow, these objects are searched for tasks that are relevant to the rule instructions. See **Data to use from projects @mentioned in instructions** section below. If the attachment appears to be relevant to the rule guidance, the document will be summarized and included as context for the LLM model. 

## Asana AI features can read attachments from Google Drive, OneDrive, SharePoint, Dropbox, and Box

This feature is currently available within AI Studio, allowing Asana AI to read attachments from Google Drive, OneDrive, Sharepoint, Dropbox, and Box. Attachments can be read by Asana AI when attached to the input task (the task which triggers the rule) or when attached directly to the Smart workflow instructions.

Access controls are detailed as follows:

- When you attach a file to a task via one of these cloud storage platforms, the AI workflow which runs on the input task has access to the specific files attached, and does not have access to the entire drive or folder.
- Attaching a file via a cloud storage platform to a task in Asana does not change the access controls that have been set within the platform. For example, if you attach a private document to the task via Google Drive, other task collaborators will still not be able to see the contents of the document.
- Asana supports attaching folders for some cloud storage platforms like Google Drive. When attaching a folder, the contents of the folder will be searched based on the rule guidance and only the relevant files will be used when running the AI workflow.
- If you have attached a file to a task but do not want an AI workflow to be able to read it, you can remove AI access for the file as shown in the image below. Removing AI access to the file does not remove the attachment from the task.

### Attachment types supported by app

For a detailed list of attachment types supported, broken down by cloud storage apps, see the attachment handling section of our [Troubleshooting in AI Studio](https://help.asana.com/s/article/ai-studio-troubleshooting#attachment-handling) article.

## Data and permissions in AI Settings

You can configure which data is included when you @mention projects and tasks in the AI Settings via the **Data and permissions** settings. Changing these settings may affect the overall cost and quality of output, as these settings determine the scope of data that Asana AI should process.

### Data to use from tasks

Choose between two levels of task information that the Smart workflow can access:

- **Task data and comments** provides basic task information like title, description, assignee, and comments.
- **Task data, comments, activity and linked tasks** expands access to include task history and relationships between tasks such as parent tasks and subtasks.

If your Smart workflow fails, and Asana AI's reasoning explains that it does not have access to the parent or subtask, check that the correct data setting is selected.

It's a common assumption that the workflow can automatically access parent tasks or subtasks, but this must be explicitly allowed either via the appropriate data setting (**task data, comments, activity and linked tasks**), or by being @mentioned directly in the AI instructions.

### Include attachments added to tasks

This small but important setting determines whether the Smart workflow has permission to view the contents of a task's attachments.

Asana AI can read images up to 5MB, and attachments up to 25MB. There is no hard limit to the number of attachments you can add to a task, but Asana AI will only read as much as it can fit into its context window.

Again, if a Smart workflow fails and Asana AI's reasoning indicates that it cannot access an attachment, make sure that this box is checked.

### Data to use from projects @mentioned in instructions

This setting allows you to control how the Smart workflow accesses tasks from projects that have been @mentioned in your AI instructions.

You can customize the level of access in 3 different ways:

- **Let AI Decide:** Asana AI will search for tasks within the @mentioned projects(s) and return relevant results. Based on the rule guidance, this will return between 0 to 150 tasks. 
- **Project names** only provides access to the names of the @mentioned projects, and no tasks.
- **Similar tasks** provides access to up to 10 tasks that are most similar to the task the AI is working on.
- **Recent tasks** provides access to the most recently modified tasks in the @mentioned projects. Up to 200 tasks can be accessed, depending on task size.

### Who can be added as a collaborator

This setting allows you to control who the Smart workflow can add as collaborators on tasks, based on your requirements.

You can customize the level of access in 3 different ways:

- **@mentioned** only includes people explicitly @mentioned, or member of teams @mentioned in the instructions. This is ideal for protecting sensitive information by ensuring only specific individuals may be added as collaborators.
- **Members and @mentioned guests** includes everyone in your organization and any guests who are @mentioned in the instructions. This strikes a balance between internal collaboration and external involvement when needed.
- **Any** includes all organization members and guests without restrictions. This setting is best for workflows that require open and unrestricted collaboration.

### AI will be able to see these contents

This section is found at the very bottom of the AI instructions pane, and lists the @mentioned projects, tasks, and teams that the Smart workflow can access. Files attached to AI instructions will also appear here. You may need to scroll down to see it.

In the below example, the builder has @mentioned 2 projects and 2 individual tasks, as well as attaching a budget tracking spreadsheet to the AI instructions.

Note below how the tasks, projects, and attachments appear in this section.

It's a quick way to confirm the workflow's inputs and to make sure the necessary context is available. If a workflow isn't working as expected, reviewing this list is an excellent first step for troubleshooting.

 

[](https://forum.asana.com/c/forum-en/tips/6)
