---
fonte: https://help.asana.com/s/article/rules?language=en_US
baixado: 2026-11-10
---

# Automations

**Portfolio automations are available on Asana [Advanced](https://asana.com/plan/advanced), [Enterprise](https://asana.com/enterprise), and [Enterprise+](https://asana.com/enterprise) tiers.**

Automations allow you to streamline routine tasks and establish workflows with ease. For an automation to work, you need a trigger that activates the automation and an action that is performed automatically. For example, an automation can be created to automatically assign a task (action) when a due date is set (trigger).

Explore automations for free. Start a [free Asana trial](https://asana.com/create-account) today.

#### Related articles:

- [Automation permissions](https://help.asana.com/s/article/rule-permissions)
- [Automation triggers](https://help.asana.com/s/article/rule-triggers)
- [Automation actions](https://help.asana.com/s/article/rule-actions)
- [Conditions and branching in automations](https://help.asana.com/s/article/conditions-and-branching-in-rules)

Power up your processes with Asanan automations. **[Join our](https://academy.asana.com/automating-workflows-in-asana-live)** ***[](https://academy.asana.com/automating-workflows-in-asana-live)*** [**Automating workflows in Asana**](https://academy.asana.com/automating-workflows-in-asana-live)*[](https://academy.asana.com/automating-workflows-in-asana-live)* virtual training to learn how.

## Creating an automation

Automations are available in both projects and portfolios. You can set up automations within projects and portfolios, allowing you to automate key actions and ensure the smooth management of multiple projects.

When creating an automation, you can choose from pre-built automations in the automations gallery, or create a custom automation. Pre-built automations in the gallery have been designed to address common workflow scenarios. Custom automations allow you to create automations tailored to your unique processes.

#### To create an automation from the gallery:

1.  Navigate to **Customize** in the top-right corner of your project
2.  Click **Automations**
3.  Click **+Add**
4.  Select an automation from the gallery or create a new one from scratch

> Each automation in Asana has its own unique URL that can be accessed directly through the browser. These URLs are automatically generated when automations are created and remain consistent throughout the automation's lifetime.

## Custom automation builder

**The custom automation builder is available on Asana [Starter](https://asana.com/plan/starter), [Advanced](https://asana.com/plan/advanced), [Enterprise](https://asana.com/enterprise), and [Enterprise+](https://asana.com/enterprise) tiers, as well as [legacy tiers](https://asana.com/pricing-legacy) Business, and Legacy Enterprise. **

** **

#### To create a custom automation:

1.  You may either enter instructions for AI Studio, select **Start from scratch**, or select a featured automation.
2.  Click the cog icon in the upper right corner to control additional settings
3.  Click **Untitled automation** to add a name for your automation.
4.  Choose triggers, actions, and add conditions if needed.
5.  Click **Publish**.

> Automations will only run on the first level of subtasks (i.e. automations will not run on sub-sub-tasks, sub-sub-sub tasks, etc.)

## Editing an automation

Edit your automations any time by navigating back to the project and selecting the automation you want to update.

#### To edit an automation:

1.  Click the **Customize** menu
2.  Click **Automatios **
3.  Click the three dot icon next to the automation you want to edit
4.  Click **Edit**

> Any edits you make to your automations will only apply on a go-forward basis. Edits will not apply retroactively.

Automations that involve external triggers or external actions such as sending emails or direct messages (e.g., via Outlook, Salesforce, or Slack) can only be edited by the automation's creator because the external triggers/actions are authenticated using the automation creator's account credentials.

## Pausing an automation

You can pause an automation at any time. Click on the **Active** toggle at the top right corner to pause the automation. 

## Deleting an automation

You can delete an automation at any time by clicking into the automation from the customize menu, click the three dot icon, and then click the **Delete** button.

## Automation settings

To access automation settings, click the gear icon in the top-right of the automation builder.

Depending on the automation type, the automation settings will contain 3 of the following tabs: **General,** **Permissions**, **AI** **Studio**, **AI Teammates**.

Under **General** settings, you can manage the name of the automation. You can also choose whether the automation can be triggered by other automations, and whether the automation should run on subtasks.

## Transfer ownership of an automation

If an automation's original owner loses access to the project or leaves the organization, team members with edit permissions can claim ownership of the automation. Asana will notify project editors when automations become orphaned, making it easy to identify which automations need attention.

To claim ownership of an orphaned automation, navigate to the automation in your project's automations list and within the **Permissions** menu click **Become owner**. Once you claim ownership, you'll be able to edit the automation and receive notifications about any issues.

## Section-based automations

On paid plans, the lightning bolt icon in sections indicates that an automation is applied to that specific section. These are visible in list and board views.

Clicking the lightning bolt will open an automations menu for that section, allowing you to add new automations or edit existing ones.

You can edit an automation by clicking the **pencil icon** that appears when you hover over it.

## Trigger combinations and multiple actions

You can also use trigger combinations and/or conditional logic and multiple actions to automate routine tasks.

You can use the act performed by one automation to trigger another.

The maximum number of automations per project is set at 50, regardless of plan size or tier.

### Custom automations

#### Triggers

- You can add up to **20 triggers** per custom automation
- You can select the trigger more than once
- You cannot choose the **Due date is approaching** or **Task is overdue** triggers for subtasks. To use either of these triggers you must change the automation to **Runs on tasks**.

#### Multiple actions

- When one or more triggers happen, you can select up to **20 actions** to occur as a result
- You can't add the same action more than once

### Column or section based triggers

Column or section based triggers are for board view projects or projects with [collapsible sections](https://help.asana.com/s/article/project-customization-and-views?language=en_US).

### Custom field automations

Custom field automations are available on all projects with custom fields. **People** custom fields are also supported.

> To unlock these automations, you must first add a [custom field](https://asana.com/guide/help/premium/custom-fields "custom field") to your project.

### Automations in bundles

With [bundles](https://help.asana.com/s/article/bundles), you can apply multiple automations at once. This allows you to standardize processes at scale and make retroactive updates to projects that are already in flight.

## Updates on misconfigured automations

If an automation becomes mis-configured (example: “Marked complete \> Move to column “Done” and someone deletes your “Done” column), we will email the owner of the automation to let them know to fix it.

- We will email you the first time an automation is triggered but cannot fire due to being misconfigured. We will not email you again until it has been corrected and successfully run at least once before misconfiguring again.

- All users with read access to the automation in question can see the correct status of the automation.

- Once you update the automation to a correct configuration and save the updates, those warnings will go away.

## Pricing

Automations are available across every paid tier in Asana. The custom automation builder is available on Asana [Starter](https://asana.com/plan/starter), [Advanced](https://asana.com/plan/advanced), [Enterprise](https://asana.com/enterprise), and [Enterprise+](https://asana.com/enterprise) tiers, as well as [legacy tiers](https://asana.com/pricing-legacy) Business, and Legacy Enterprise.

A subset of automations are available to customers on the legacy tier Premium:

- Move to column/section \> Mark complete
- Mark complete \> Move to column/section
- Custom field changed \> Move to column/section
- Move to column/section \> Set custom field
- Custom field changed \> Mark complete
- Mark complete \> Set custom field

## Frequently asked questions

### How do automations work in Asana?

Automations automate routine tasks by combining a trigger (like setting a due date) with an action (like automatically assigning the task to someone), allowing you to streamline workflows without manual intervention.

### Can I edit an automation after I create it?

Yes, you can edit any automation by clicking the customize menu, selecting the automation under the Edit section, and clicking Edit, though changes only apply to future tasks and not retroactively.

### What happens when an automation becomes misconfigured?

Asana emails the automation owner the first time a misconfigured automation fails to fire (such as when a referenced column is deleted), and all users with read access can see the automation's status until it's corrected.

### How many automations can I add to a single project?

You can add up to 50 automations per project regardless of your plan size or tier, and you can add up to 20 triggers and 20 actions per custom automation.
