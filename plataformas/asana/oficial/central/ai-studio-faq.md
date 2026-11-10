---
fonte: https://help.asana.com/s/article/ai-studio-faq?language=en_US
baixado: 2026-11-10
---

# AI Studio FAQ

**AI Studio is available on** **[Starter](https://asana.com/plan/starter), [Advanced,](https://asana.com/plan/advanced) [Enterprise](https://asana.com/enterprise), and [Enterprise+](https://asana.com/enterprise)  plans**. **Visit [asana.com/ai](https://asana.com/ai) to learn more about the launch of Asana AI Studio. **

This article answers frequently asked questions about AI Studio - from how to get started to how permissions, data access, and model selection work. If you’d like to go further, you can also earn the [AI Studio Foundations skill badge](https://academy.asana.com/ai-studio-foundations-skill-badge) in the Asana Academy. You’ll learn how to write effective prompts, plan smart workflows, and troubleshoot common issues.

#### Related articles

- [Introduction to Asana AI Studio](https://help.asana.com/s/article/ai-studio)
- [Create smart workflows with AI Studio](https://help.asana.com/s/article/ai-studio-smart-workflows)
- [Writing instructions in AI Studio](https://help.asana.com/s/article/writing-ai-studio-instructions)
- [AI Studio add-on and pricing](https://help.asana.com/s/article/ai-studio-pricing)
- [Asana AI FAQ](https://help.asana.com/s/article/asana-ai-faq)
- [Troubleshooting in AI Studio](https://help.asana.com/s/article/ai-studio-troubleshooting)

## Getting started with AI Studio

### How do I access AI Studio?

To access Asana AI Studio, follow the steps detailed in [this article](https://help.asana.com/s/article/ai-studio).

### Is there an Asana Academy course available for AI Studio?

Yes. You can take the [AI Studio Foundations skill badge](https://academy.asana.com/ai-studio-foundations-skill-badge) in the Asana Academy to learn how to build smart workflows and write effective instructions.

### How can I connect with other creators using AI Studio? 

We have a dedicated [AI Studio Forum section](https://forum.asana.com/c/forum-en/ai-studio/207). This is a space designed for discussing AI Studio, sharing tips and use cases, and asking questions.

## AI Studio features and functionality

### How does @mentioning teams work?

You can @mention a team in Asana in the same way as you would mention a task or project. This allows the LLM to see the names of up to 200 members of the team and to see who the team admins are. This means it's possible to use AI to add members of a team as collaborators on a task, or assign a task to a team admin.

### What’s the difference between instructions and conditions?

Instructions and conditions serve different purposes in a smart workflow:

- **Instructions** are essential—they tell Asana AI how to perform a task by providing context, goals, and guidelines.

- **Conditions** are optional—they determine whether an action should happen based on certain criteria.

### What are instructions?

Instructions guide Asana AI’s behavior in a smart workflow. They provide necessary context, goals, and details on how Asana AI should complete a task. Every AI-powered workflow must have instructions.

### What are conditions?

Conditions work like "if-then" statements. After a trigger event, the rule checks if a condition is met before proceeding with an action. If the condition isn’t met, the action won’t occur. However, not all workflows require conditions.

### What is a conditional check by AI, and how is it different from regular conditions?

A conditional check by AI is similar to a regular condition, but instead of using fixed criteria, Asana AI evaluates the condition itself. This allows for greater flexibility, as Asana AI can assess more complex or nuanced situations.

## AI Studio models

### Which model should I choose for my smart workflow?

AI Studio currently offers a choice of six large language models for use in your smart workflow. The right model to use depends on the type of work to be done and the potential cost.

#### **Claude Sonnet 4.5**

High cost. Great at writing documents and most tasks.

#### **Claude Opus 4.1**

Very high cost. Best at writing documents and following complex guidance.

#### **Claude Sonnet 4**

High cost. Good at writing documents and most tasks.

#### **GPT-5**

Medium cost. Best for complex tasks and following detailed guidance.

#### **GPT-5 mini**

Very low cost. Best for most tasks.****

#### **Claude 3.5 Haiku**

Medium cost. Good at summarizing and classifying information.****

## Recent changes to AI Studio models

We’ve recently made updates to the models available in AI Studio. To ensure better performance and a consistent experience, we have upgraded all rules using older models. The following models are no longer available for rules: **Claude Sonnet 3.5**, **Claude Opus 4**, **o1**, **o3-mini**, **GPT-4o**, **GPT-4o mini**. On October 20, 2025, rules using legacy models were automatically migrated as described below:

- Claude Sonnet 3.5 → Claude Sonnet 4.5
- Claude Opus 4 → Claude Opus 4.1
- o1 → GPT-5
- o3-mini → GPT-5
- GPT-4o → GPT-5
- GPT-4o mini → GPT-5 mini

**Improved performance, same cost**: The upgraded models are more intelligent and also consume the same or fewer credits, so your overall credit usage will not increase.

**Automatic transition**: You do not need to do anything to enable this transition. On October 20, 2025, rules using legacy models were automatically migrated for you as described above.

## Permissions and user roles

### Is there a limit on the number of builders?

No, there isn’t a limit.

### How do the builder’s permissions affect the smart workflow’s access?

The smart workflow can only access projects and tasks that the builder has permission to see. If the builder doesn’t have access to a project, they can’t set up Asana AI to interact with it. Likewise, if the builder can't view certain tasks, Asana AI won’t be able to see or analyze them when the smart workflow runs.

### Can guests be builders?

No, guests can’t be builders.

## Data and security

### Is AI Studio HIPAA compliant?

Yes, customers on Asana’s HIPAA offering can enable AI Studio. For more information on Asana AI and its data protections, please see [Asana AI FAQ](https://help.asana.com/s/article/asana-ai-faq?language=en_US).

### When a rule is run on a task, what data can the AI access?

When building a smart workflow in AI Studio, you can dictate the data that Asana AI has access to. This gives you control over exactly what data is handled by Asana AI. By default, an AI-powered rule can access two things:

- The data from the task that triggers it.
- Data from the project that the rule lives in and the tasks in that project.

If a task is multi-homed in several projects, the rule cannot identify the other projects unless they are explicitly mentioned in the instructions.

You can give Asana AI access to additional data in AI Studio by configuring instructions in the following ways:

- Specifically @mentioning tasks, projects, portfolios, goals, teams, workloads, or users to provide access to those objects.
- Attaching documents or third-party attachments to the instructions.

For more information, visit the article: [Create smart workflows with AI Studio](https://help.asana.com/s/article/ai-studio-smart-workflows?language=en_US).

#### **Task data to access from input tasks**

An **input task** refers to the task that directly triggers a rule. You have two options under the **Data to use from tasks** section of the AI instructions:

- Task data, comments
- Task data, comments, activity, linked tasks

Task data is the default, non-configurable set of data that may be referenced along with any task. InThis data includes:

- Title
- Description
- Assignee
- Due date
- Start date
- Custom fields (only those with values)
- Type (e.g., approval, milestone)
- Approval or completion status
- Creation time
- Last modified time
- Projects
- Sections
- Creator
- Comments
- Custom fields 
- Collaborators 
- Project Section 
- Health Score
- Attachments on the input task\*

\*For Asana AI to see attachments, you must check the **Include attachments added to tasks** checkbox.

If you choose to include activity and linked tasks in addition to the task data and comments, the following are sent to Asana AI:

- Task activity
- Task data for parent tasks
- Task data for dependent and blocking tasks
- Task data for all subtasks

## AI Studio and web access

Web access is currently in early access and only available for Advanced (annual), Enterprise, and Enterprise+ customers.

### What is web access in Asana AI Studio?

Web access is a feature that allows Asana AI to gather real-time information from public websites. This includes both conducting web searches and reading content from specific user-provided links.

### What kind of links can AI Studio read?

Asana AI will read:

- URLs included in the guidance of a smart workflow rule
- URLs present in the task which triggers the workflow

### Where do I enable web access?

Admins can enable web access from the Asana AI section in the admin console. Once enabled, users can customize access per workflow in AI Studio.

### Does it support all AI models?

Yes, both Anthropic and OpenAI models support web access.

### Is web access HIPAA-compliant?

No. This feature is not available in HIPAA-compliant workspaces due to limitations set by Asana's AI providers.

 

[](https://forum.asana.com/c/forum-en/tips/6)
