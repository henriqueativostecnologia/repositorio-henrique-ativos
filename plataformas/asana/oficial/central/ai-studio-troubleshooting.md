---
fonte: https://help.asana.com/s/article/ai-studio-troubleshooting?language=en_US
baixado: 2026-11-10
---

# Troubleshooting in AI Studio

AI Studio is available for [Starter](https://asana.com/plan/starter), [Advanced](https://asana.com/plan/advanced), [Enterprise](https://asana.com/enterprise), and [Enterprise+](https://asana.com/enterprise) customers. Visit [asana.com/ai](https://asana.com/product/ai) to learn more about the launch of Asana AI Studio.

This article will help you troubleshoot common AI Studio issues and keep your Smart workflows running smoothly. To deepen your skills, you can also earn the [AI Studio Foundations skill badge](https://academy.asana.com/ai-studio-foundations-skill-badge) in the Asana Academy, where you’ll learn how to write effective prompts, plan workflows, and handle errors with confidence.

#### Related articles

- [Introduction to Asana AI Studio](https://help.asana.com/s/article/ai-studio)
- [Create Smart workflows with AI Studio](https://help.asana.com/s/article/ai-studio-smart-workflows)
- [Writing instructions in AI Studio](https://help.asana.com/s/article/writing-ai-studio-instructions)
- [AI Studio add-on and pricing](https://help.asana.com/s/article/ai-studio-pricing)
- [AI Studio FAQ](https://help.asana.com/s/article/ai-studio-faq)

## Workflow execution issues

### When I @mention many projects, and ask AI to read their task contents, Asana AI doesn’t seem to be reading all the data from them

If you @mention multiple projects, the system will include as many tasks from those projects as can fit within the context window, up to a maximum of 200 tasks. The included tasks are sorted by last modified date. So if the data exceeds the limit, some tasks from the @mentioned projects may not be sent to Asana AI.

### I received a warning that the Smart workflow couldn't run an action

This usually indicates Asana AI does not have sufficient context to take the requested action clearly. Viewing Asana AI’s reasoning will explain the specific issue and suggest how to resolve it. You can learn how to do this in the “Check Asana AI's reasoning” section below. Often the solution is providing additional instructions so Asana AI has the necessary information to proceed confidently. Sometimes the instructions given to Asana AI need to provide additional context.

### Check Asana AI's reasoning

Asana AI’s reasoning gives a valuable insight into how Asana AI is processing information. Check Asana AI’s reasoning in each task’s history to understand how AI is interpreting your instructions.

The reasoning can show you things like:

1.  Asana AI might not have access to the work you think it does (check if the work is mentioned in the instructions you’ve provided).
2.  The instructions provided to Asana AI might not be clear enough or may have some ambiguity that results in Asana AI interpreting the instructions differently to how you expected.

To find Asana AI’s reasoning, open a task where Asana AI has taken action, scroll down to the task history/comments section and click **Show reasoning** as shown in the gif above.

### Asana AI is not performing the action specified in my instructions

To ensure your workflow functions as intended, it's important to set up your Smart workflow so it can perform the desired action. A common mistake is assuming that telling Asana AI what action you want it to perform in the instructions is enough, but remember that AI Studio is built on top of Asana's rules engine, meaning you will still need to create an action when building the rule before anything can happen.

For example, you might write instructions for Asana AI to comment on incoming requests that don't have enough information, asking the requester specific follow up questions. While these instructions explain **how** you want the action executed, Asana AI can't carry them out unless you also create an **Add** **Comment** action in the rule. Additionally, you must include the **Use AI variable** in the comment field when creating the action for the process to be completed successfully. Without these steps, Asana AI won't be able to follow through, no matter how clear your instructions are.

Think of the instructions as guidance for Asana AI on *how* to perform the action. However, creating the action in the rule and adding the **Use AI** variable specifies *what* the rule needs to do. Both elements are essential to make the workflow function smoothly.

## Attachment handling

### Attachments are not working in Smart workflows

An issue with attachments may be due to one of the following:

- It’s possible that the Smart workflow cannot access task attachments. Make sure you have the **Include attachments added to tasks** checkbox enabled in AI Studio.
- The attachment may be too large. There are size limits that will prevent the rule from working if the limit is exceeded. Asana AI can read images up to 5MB, and attachments up to 25MB. There is no hard limit to the number of attachments you can add, but the AI will only read as much as it can fit into its context window.
- For PDFs, only text information is extracted by Asana AI. Images in PDFs are ignored. This also applies to Claude models (which can read images, but not images from PDFs).
- Images are only currently supported for Claude models. There is a limit of 100 images per task and each individual image must be under 5MB in size. GPT models cannot read images at this time.
- If using incognito mode in Chrome, you may need to allow third-party cookies in your browser settings.
- The attachment type may not be supported. See a list of supported file types below.
- AI can't access attachments on parent or subtasks of the input task (the task that triggers the rule). The only current workaround for this is mentioning those parent or subtasks directly in Asana AI instructions.

### Supported file types

|                                                                    |                   |                  |                  |                    |             |         |
|:------------------------------------------------------------------:|:-----------------:|:----------------:|:----------------:|:------------------:|:-----------:|:-------:|
|                        **Attachment type**                         | **Direct upload** | **Google Drive** | **OneDrive\*\*** | **SharePoint\*\*** | **Dropbox** | **Box** |
|                  Cloud folder (Google docs, etc.)                  |        n/a        |        ✅        |       n/a        |        n/a         |     n/a     |   n/a   |
|                   Cloud doc (Google docs, etc.)                    |        n/a        |        ✅        |       n/a        |        n/a         |     n/a     |   n/a   |
|                 Cloud sheet (Google sheets, etc.)                  |        n/a        |        ✅        |       n/a        |        n/a         |     n/a     |   n/a   |
|              Cloud presentation (Google slides, etc.)              |        n/a        |        ✅        |       n/a        |        n/a         |     n/a     |   n/a   |
| Images (.jpg, .png, .apng, .tiff, .svg, .bmp, .gif, .webp, etc.)\* |        ✅         |        ✅        |        ✅        |         ✅         |     ✅      |   ✅    |
|                               .docx                                |        ✅         |        ✅        |        ✅        |         ✅         |     ✅      |   ✅    |
|                     .xlsx/.csv (spreadsheets)                      |        ✅         |        ✅        |        ✅        |         ✅         |     ✅      |   ✅    |
|               .pptx (Microsoft PowerPoint slideshow)               |        ✅         |        ✅        |        ✅        |         ✅         |     ✅      |   ✅    |
|                                .pdf                                |        ✅         |        ✅        |        ✅        |         ✅         |     ✅      |   ✅    |
|                                .txt                                |        ✅         |        ✅        |        ✅        |         ✅         |     ✅      |   ✅    |
|                      .vtt (video text tracks)                      |        ✅         |        ✅        |        ✅        |         ✅         |     ✅      |   ✅    |
|                           .json / .yaml                            |        ✅         |        ✅        |        ✅        |         ✅         |     ✅      |   ✅    |

\*Images can be read only by Anthropic's Claude models, not OpenAI's GPT models.

\*\*If you disconnect a OneDrive or SharePoint account from **Settings \> Apps**, you may still remain signed in on the Microsoft side. To fully switch to a different account, you may need to clear your browser cookies to remove the previous Microsoft login session.

> Dropbox is not currently supported.

 

## Access issues

### Asana AI can't access the work I expect

You must explicitly mention other projects or tasks in order for Asana AI to get access to them. If Asana AI is not accessing the work that you expect:

1.  Be aware that work must be mentioned explicitly in the instructions when building the rule.
2.  Smart workflows can't currently access portfolios.
3.  Check the bottom part of the Asana AI instructions pane where it calls out which work Asana AI has access to.
4.  Check Asana AI's reasoning as shown in the section above.
5.  Check the model you're using - are you trying to use a GPT model to analyze an image? Only Claude models support this currently.

See our article on [Connecting your Smart workflow to the right data sources](https://help.asana.com/s/article/ai-studio-connect-your-smart-workflow) for more detailed information and tips to ensure Asana AI can access the work it needs.

### My Smart workflow can't see parent/subtask information

If your Smart workflow is unable to see parent and subtask information, there are a few key settings to check. First, ensure you have chosen **Task data, comments, activity, linked tasks** under **Data to use from tasks** in the **Data and permissions** section of the instructions. If you've already enabled this setting but still experience issues, try explicitly @mentioning the parent or subtask in your workflow instructions. It's important to understand that these relationships aren't automatically visible to Asana AI without the proper permissions being in place.

### My Smart workflow can't see other tasks in the same project

Smart workflows don't automatically have visibility to all tasks within the same project, even when working with related items. To ensure proper access, you should always explicitly @mention the specific project in your workflow instructions. It's also crucial to verify your project data access settings are properly configured - these can be set to Project names only, Similar tasks, or Recent tasks. Remember that simply being in the same project doesn't automatically grant Asana AI access to other tasks.

## Data permission settings

### My Smart workflow has limited access to tasks within a project

When working with a project’s tasks in Smart workflows, the level of access is determined by your **Data to use from projects** setting. This setting has three options that provide different levels of visibility: **Project names only** provides minimal access and only allows the workflow to see project names; **Similar tasks** grants access to up to 10 tasks that are similar to the one being processed; and **Recent tasks** provides the broadest access, allowing visibility of up to 200 recently modified tasks. Understanding these settings is crucial for ensuring your workflow has the appropriate level of access to tasks within a project.

### My Smart workflow can't add certain collaborators

If your Smart workflow is having trouble adding collaborators, you'll need to check the **Who can be added as a collaborator** setting.

In the example below, the setting chosen only allows those @mentioned in the instructions to be added as collaborators when the rule creates a comment on the task.

This setting has three permission levels:

1.  **@Mentioned**: This is the most restrictive option and only allows explicitly mentioned users to be added. In this case you would need to provide Asana AI with a list of users it can mention in Asana AI instructions. In the example shown in the screenshot above, only Jamie, Yvette, Alan and Hannah can be added to tasks as collaborators. Other members of the legal team not @mentioned here cannot be added as collaborators.
2.  **Members and @mentioned guests**: provides a balanced level of access. This allows anyone in your organization and any guests @mentioned in the instructions, to be added as collaborators.
3.  **Anyone**: is the most permissive setting, allowing the workflow to add any user as a collaborator. 

Selecting the appropriate setting will ensure your workflow can add the intended collaborators while maintaining your desired security level.

[](https://forum.asana.com/c/forum-en/tips/6)
