---
fonte: https://help.asana.com/s/article/salesforce-in-asana-rules?language=en_US
baixado: 2026-11-10
---

# Salesforce in Asana integration

> If you’re looking for the Asana app in Salesforce AppExchange, you can learn more about the deprecation plan in this [FAQ](https://help.asana.com/s/article/salesforce-integration-deprecation-faq). Going forward, customers should use the Salesforce app in Asana integration.

Salesforce in Asana integration extends our rules core components to Salesforce, so that you can automate workflows between Salesforce and Asana, and keep the latest data in sync in Asana.

Asana Rules are automations that streamline routine tasks. A rule consists of a **trigger** and an **action**, an event that activates the rule and an action performed by the rule, respectively. An example of a trigger is **When an opportunity is created in Salesforce**. An example of an action is **Create a task in a specific Asana project**.

## Salesforce trigger conditions to create or update tasks

Salesforce in Asana integration utilizes the trigger **Salesforce record created or updated**, with many customizable conditions available. Rules can be configured with conditions based on Salesforce object types (e.g. Opportunity, Account) and specific field values across numbers, dates, and picklists.

Users can choose from 2 Salesforce triggers:

- **Record is created**: This triggers the rule to run only if a record has been created and meets the conditions that you set. Record is created is a common trigger for intake workflows, such as creating a task when a VOC is created.
- **Record is created or updated**: This triggers the rule to run if a record has been created or updated and the conditions you have set are met. This trigger could be used for hand-offs based on Salesforce updates, such as creating an SE inbox task when an opportunity reaches stage 3.

Note that **Record is created or updated** is the trigger that should be used for the **Create task and keep in sync** action.

When setting your trigger, you can specify certain conditions that should simultaneously be met for the rule to run. If the rule is triggered by an event, but the specified condition is not met, then the rule will not run. For example, for the trigger Salesforce record is created or updated, the following conditions are supported as part of the trigger:

- **Object conditions**: Any object the user has access to is supported, e.g. opportunity, account, case, campaign, and custom objects.
  - Use an object condition without any field condition if you want the rule to be triggered whenever any object is created or updated.
  - *Example: Create a task when opportunity is created or updated. When fields are updated and record is attached to a task, keep fields in sync*
  - *Trigger = “Record created or updated”, Object is “Opportunity”*
  - *Action = "Create task and sync" with number CF with {amount} AND Set text CF with {opportunity name}*
    - *Create opportunity A → Task A is created*
    - *Update opportunity A ARR change to 12,000 → On Task A, ARR field is updated to 12,000*
    - *Update opportunity A name to XYZ → On Task A, Text CF is updated to XYZ*
    - *Update opportunity B with ARR change set to 9,000 → Task B is created*
- **Field conditions**: Any field available to the user on an object across number, date, and picklist types.
  - Use a field condition if you want the rule to be triggered whenever this field changes.
  - *Example: Add a comment when an account has an activity update*
  - *Trigger = “Record created or updated”, Object is “Account”, Field is “Date of last activity”*
  - *Action = "Add comment"*
    - *When the linked account has an update to “Last Activity Date”, add a comment to tasks where the account is attached*
    - *Update field other than “Date of last activity” (eg. Name) → No action taken*
- **Value conditions**: A certain picklist value, for example.
  - Use a value condition if you want the rule to be triggered when this field changes and meets the value condition.

  - *Example: Create a review task when opportunity ARR change is changed to \> \$10,000*

  - *Trigger = “Record created or updated”, Object is “Opportunity”, Field is “ARR change”, Operator is “greater than”, Number is “10,000”*

  - *Action = "Create task"*
    - *Create a new opportunity with ARR change set to 11,000 → Task is created*
    - *Update ARR change to 12,000 → Task is created*
    - *Update ARR change to 9,000 → No action taken (field change doesn’t meet trigger conditions)*
    - *Update field other than ARR change (eg. Name) → No action taken*

Note that conditions are set within the Salesforce trigger, i.e. they are [coupled with the trigger](https://help.asana.com/s/article/conditions-and-branching-in-rules?language=en_US#Coupled_triggers_and_conditions). They cannot be set as a separate condition to the trigger.

See a popular example in action in the "Creating tasks for specific opportunity stages" [section](https://help.asana.com/s/article/salesforce-in-asana-rules#creating-tasks-for-specific-opportunity-stages).

## Salesforce variables in rules

Salesforce builds upon [rule variables](https://help.asana.com/s/article/variables-in-rules?language=en_US). A variable is a way to reference key data from a rule trigger in the rule action.

For example, if a Salesforce trigger is chosen, rule actions can reference the Salesforce opportunity ARR. In rule actions like **Create task**, fields from the Salesforce record can be mapped using dynamic variables to populate the task name, description, and custom fields. When the rule is triggered by an event in Salesforce, the rule action will pull the value of the variable from Salesforce.

When setting up a rule action, the following Salesforce field types are available as variables to be pulled into Asana task fields:

|                           |                                                       |
|:-------------------------:|:-----------------------------------------------------:|
| **Salesforce field type** |                 **Asana field type**                  |
|          String           | Text (task title, description, custom field, comment) |
|         Textarea          |                         Text                          |
|         Picklist          |                         Text                          |
|      Date, Datetime       |                    Date/time, text                    |
|         Currency          |                     Number, text                      |
|            Int            |                     Number, text                      |
|           Long            |                     Number, text                      |
|          Percent          |                  Number (1%=1), text                  |
|       Rich textarea       |                   Unformatted text                    |

## Create task and keep in sync action

The **Create a task and keep in sync** action pairs with the **Salesforce record is created or updated** trigger to enable automatic updates from fields in Salesforce to Asana fields through rule actions that map Salesforce variables. When Salesforce fields change, corresponding Asana tasks are automatically updated, ensuring teams always have the latest information without the need for manual updates.

When using the create task and keep in sync action, a Salesforce field will be mapped 1-to-1 with an Asana field. For example, "Account Name" can be mapped 1-to-1 to a text field like "Task Name". However, the create task and keep in sync action will not update a concatenation of text and variables, like "Account: {Account Name}".

## Setting up two rules for stage-specific opportunity sync

When you want to create and sync tasks only when an opportunity reaches a specific stage, such as "Proposal" or "Negotiation," you must set up two separate rules instead of using the preset **Create task and keep in sync** action. Using the standard preset action will not sync fields correctly for individual stages.

### Rule 1: The creation rule

This rule watches for the specific stage change and creates the Asana task. You configure this rule to trigger when an opportunity record reaches your target stage, ensuring a task is only created at the right moment in your pipeline.

### Rule 2: The sync rule

This rule runs in the background for all opportunities to keep fields updated once a task is already linked, regardless of what stage the opportunity moves to next. Without this rule, field data will not remain current after the initial task creation.

Together, these two rules replicate the behavior of the preset action while giving you the stage-specific control you need. Setting up both rules is required for the field sync to work properly when triggering tasks at specific opportunity stages.

## How to set up the Create a task and keep in sync action

Salesforce admins have the required permissions to set up the sync action rule in Asana.

1.  In your project, click the **Customize** menu
2.  Click + Add rule
3.  Select the Salesforce trigger Salesforce record created or updated. See the section **Salesforce trigger conditions to create or update** above for more detail.
4.  Select the action **Create a task and keep in sync**
5.  Map Salesforce fields to Asana task fields and custom fields
6.  When field mapping is complete, click **Publish**

Consider a rule which is designed to create a new task in Asana whenever a new opportunity is created in Salesforce, and to sync the values of the Salesforce opportunity's fields with their corresponding Asana task fields.

The Salesforce opportunity's **Name** and **ARR Change** fields would be mapped to the Asana task's **Task name** and **Amount** fields, respectively. If the opportunity's name is changed to XYZ, the Asana task's title changes to XYZ automatically. Likewise, any modification of the **ARR Change** value within Salesforce will automatically be reflected in the **Amount** field in the Asana task.

## Creating tasks for specific opportunity stages

While the **Create task and keep in sync** action is useful for creating tasks for all opportunities, you may want to create and sync tasks only when an opportunity reaches a specific stage (such as "Proposal" or "Negotiation"). This requires setting up two separate rules instead of using the preset action.

Use the two rule approach when you want to:

- Create Asana tasks only for opportunities that reach a certain stage
- Keep task fields synchronized with Salesforce data
- Avoid creating tasks for early-stage opportunities that may not convert

Important: Single-select and multi-select custom fields are not supported in Salesforce-Asana field syncing.

### Rule 1: Create task for specific stage

This rule creates the initial task when an opportunity reaches your target stage.

1.  When: **Record is created or updated** (Salesforce)
2.  In: **Opportunity, Stage** is set to \[Your target stage\] (e.g., Proposal, Negotiation)
3.  Do this: **Create a task** (select **Create a task**, do not select **Create a task and keep in sync**)
4.  Configure your task details (project, assignee, task name, etc.)
5.  Do not add any **Check if** conditions for this rule

### Rule 2: Sync fields between Salesforce and Asana

This rule keeps the task fields synchronized with Salesforce data

1.  When: **Record is created or updated** (Salesforce)
2.  In: **Opportunity** (do not specify a stage condition here)
3.  Do this: Set up fields mappings
    1.  Set SFDC Field 1 to Asana Field 1
    2.  Set SFDC Field 2 to Asana Field 2
    3.  Add additional mappings as needed

### Example setup

For opportunities in the Proposal stage.

Rule 1:

- When Record is created or updated (Salesforce)
- Opportunity, Stage is set to Proposal
- Do this: Create a task in Sales Pipeline project, assign to Account Owner

Rule 2:

- When: Record is created or updated (Salesforce)
- In: Opportunity
- Do this: Set Opportunity Amount to Task Custom Fields "Deal Value", Set Close Date to Task Due Date

This setup ensures tasks are only created when opportunities reach the "Proposal" stage, while keeping all relevant fields synchronized throughout the opportunity lifecycle.

## Setup requirements

We recommend working with your Salesforce admin on installation steps and referring to this more detailed [installation guide documentation](https://docs.google.com/document/d/1ibLvMvB4zjCdOlXu12P9WbiJxd8lzfF1i5hCTVv_SJo/edit?usp=sharing). 

### Creating a rule

An Asana user can create and save the rule if the following conditions are satisfied:

1.  The user has authorized via OAuth into their Salesforce account.

2.  The user has the following Salesforce permissions. We recommend working with your Salesforce admin to set up these permissions:

    1.  Customize Application

    2.  Run flows

    3.  Manage flows

    4.  Modify Metadata Through Metadata API Functions

    5.  Enable System Mode Flow Activation

### Linking Salesforce records to Asana tasks

An Asana user can link Salesforce records to an Asana task if the following conditions are satisfied:

1.  The user has authorized via OAuth into their Salesforce account.

2.  The user has access to those specific records in Salesforce.

Data is communicated securely through the Salesforce API integration. User permissions for accessing linked Salesforce data follow Asana's standard permissions model based on task access.

 

[ ](https://forum.asana.com/c/forum-en/tips/6)
