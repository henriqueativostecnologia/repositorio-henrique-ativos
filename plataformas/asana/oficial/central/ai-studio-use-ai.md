---
fonte: https://help.asana.com/s/article/ai-studio-use-ai?language=en_US
baixado: 2026-11-10
---

# How the Use AI variable works

AI Studio is available for [Starter](https://asana.com/plan/starter), [Advanced](https://asana.com/plan/advanced), [Enterprise](https://asana.com/enterprise), and [Enterprise+](https://asana.com/enterprise) customers. Visit [asana.com/ai](https://asana.com/product/ai) to learn more about the launch of Asana AI Studio.

The **Use AI** variable allows Asana AI to generate context-aware outputs in your smart workflows. This article will help you understand how the Use AI variable works and how to apply it effectively in your Smart workflows. If you’d like to go further, you can also earn the [AI Studio Foundations skill badge](https://academy.asana.com/ai-studio-foundations-skill-badge) in the Asana Academy. You’ll learn how to write effective prompts, plan Smart workflows, and troubleshoot common issues.

Video: https://fast.wistia.net/embed/iframe/0c8wgrkt63?web_component=true&seo=true&videoFoam=false

#### Related articles

- [Create Smart workflows with AI Studio](https://help.asana.com/s/article/ai-studio-smart-workflows)
- [Writing instructions in AI Studio](https://help.asana.com/s/article/writing-ai-studio-instructions)
- [AI Studio FAQ](https://help.asana.com/s/article/ai-studio-faq)
- [Troubleshooting in AI Studio](https://help.asana.com/s/article/ai-studio-troubleshooting)
- [AI Studio add-on and pricing](https://help.asana.com/s/article/ai-studio-pricing)

## What is a variable?

To understand the Use AI variable, let’s first define a variable. In the context of Asana workflows, a variable is a placeholder that dynamically pulls information from your tasks or projects. It’s used to personalize automation by inserting specific data, such as task names, assignees, or due dates, into rule actions.

## What is the Use AI variable?

The Use AI variable goes beyond static placeholder variables. It enables AI Studio to actively generate content or make decisions within a Smart workflow based on the context provided in the instructions pane. Instead of simply pulling existing information, Asana AI dynamically creates outputs guided by your instructions and the workflow’s context.

### How the Use AI variable works:

- **Dynamic content generation**: The Use AI variable allows AI Studio to do things like draft emails and campaign briefs, add and respond to comments, analyze Asana data, documents, sheets, PDFs, and images.
- **Context-aware adaptation**: The Use AI variable allows AI Studio to consider the specific details of the task or project to provide intelligent and relevant outputs.

For example, instead of specifying a static assignee in a rule action, you can input the Use AI variable to assign the task to the most appropriate person based on the context provided in your AI instructions.

## Differences between standard variables and the Use AI variable

While both standard variables and the Use AI variable are used to enhance workflows, they serve distinct purposes. A standard variable uses existing task or project data. The Use AI variable uses Asana AI to create content based on instructions and context.

For example, you can use the people variable to assign the task in a specific section to a particular team member. However, you can add the Use AI variable to determine the most suitable person for the task based on the context and instructions the rule builder has provided.

## Where to add the Use AI variable in your Smart workflows

The Use AI variable is designed to be used in the **action** part of a rule. Actions determine what happens after a trigger is activated in a workflow. Adding the Use AI variable to actions allows Asana AI to contribute outputs that align with the workflow’s goals.

### Examples:

Here are a few examples of when you can add the Use AI variable. Please note that this isn’t an exhaustive list and there are many more scenarios where you can use this variable.

1.  **Dynamic assignees**: Instead of assigning a task to a fixed team member, use the Use AI variable to let Asana AI select the most relevant assignee based on the rule builder’s detailed instructions.

2.  **Automated comments**: Set your rule to add a comment like “*Recommended next steps:* **Use AI**” and let Asana AI generate actionable recommendations in place of the Use AI variable when the comment is added.

3.  **Task descriptions**: Add the Use AI variable to automatically generate detailed task descriptions based on the task name and project context.

## Adding the Use AI variable to your workflow

When creating or editing a rule in Asana, navigate to the **Action** section.

You can add the Use AI variable when:

- Adding comments
- Moving to a section
- Moving or adding to project
- Setting task description
- Setting custom fields
- Creating a task
- Creating a subtask
- Creating approvals
- Setting assignees
- Setting due dates
- Adding collaborators

In this example, we will add the Use AI variable to choose the appropriate option for the **Approval status** custom field.

You’ll then need to provide instructions for Asana AI. If the **Add instructions** box isn’t visible, it will appear once you select **Use AI**.

Click **+ Add instructions** to provide instructions and context for Asana AI. These instructions will allow it to choose the appropriate option when filling out the custom field, which in this example is named *Approval Status*. Once you’ve finished providing instructions and setting permissions, click **Publish rule** in the top right corner. Since the approval status has been chosen as the Use AI variable,  Asana AI can choose the most appropriate custom field value based on the instructions provided, rather than a static value.

## Use AI with assignee

For task assignment, **Use AI** is designed to assign tasks to users based in objective instructions. Asana AI is not designed to assign tasks via AI-based assessments of a user's skills or traits.

To publish your workflow, please either:

1.  Revise your user assignment instructions to focus on objective factors, or
2.  Remove the **Use AI** option from the assignee field.

For example, your workflow instructions could incorporate objective criteria like:

1.  Operational conditions (e.g., availability, on-call status, office location)
2.  Role-based assignments (e.g., team membership, job function)
3.  Scheduling rules (e.g., rotation systems, predetermined schedules)
4.  Workload metrics (e.g., current task count)

**Examples:**

- ✅ "Assign to the on-call engineer according to our weekly rotation"
- ✅ "Route to members of the Marketing team"
- ✅ "Distribute to team members with fewer than 5 active tasks"
- ⚠️ "Assign to the person who's best at design work"
- ⚠️ "Route to team members based on their performance history"

[](https://forum.asana.com/c/forum-en/tips/6)
