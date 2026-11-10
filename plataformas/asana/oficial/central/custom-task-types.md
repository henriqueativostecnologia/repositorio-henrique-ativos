---
fonte: https://help.asana.com/s/article/custom-task-types?language=en_US
baixado: 2026-11-10
---

# Custom task types and statuses

Custom task types allow you to standardize tasks and better reflect your unique workflows in Asana. This feature helps teams create more consistent workflows by giving more control over which status options are available for certain tasks.

## What are custom task types?

Custom task types are similar to milestones and approvals in Asana. They can be created within the task templates menu.

You can use a custom task type to do the following:

- Standardize tasks so they better suit your workflow.
- Define custom task status options.
- Control how task status changes affect task completion.

Note: This feature is only available to users with **Project admin** or **Editor** permissions.

## How to create custom task types

1.  In your project, navigate to the **Customize** menu
2.  Select **Task templates** and click **+Add**
3.  Click **+ New type**
4.  Name your task type, e.g. "Marketing request status"
5.  Define custom status options, e.g. Submitted, In review, Sent for translation, Published
6.  Set colors for each status
7.  Configure which statuses mark the tasks as complete or incomplete
8.  Add any further details to the task template
9.  Click **Create type** to save your custom task template

## Using custom task types in rules

You can make use of custom task types when creating rules. Use a custom status change such as "In review" as the trigger or as a condition when building a rule, much like you might use a custom field status or an approval status change.

In the example above, we are able to have the rule fire on the condition that the status of the custom task type (Marketing request status) is set to a particular value.

## Using custom task types in AI Studio

You can also make use of custom task types when creating Smart workflows with AI Studio. Just as the status of a task can be used with rule triggers, conditions, or in actions, they can also be used when creating AI-powered rules. In the below example, we instruct Asana AI to review any work that has commenced on the task when it has been added to the project, and ask the AI to update the Marketing request status accordingly.

The custom task type **Marketing request status** is being checked in the condition of this rule, as well as updated in the action of the rule.

## How to use custom task types in bundles

When you add custom task types to a bundle and then apply that bundle to a project, the task types from the bundle become available in that project. This helps your team use the same task types and statuses everywhere that bundle is applied.

To add custom task types to a bundle, start from a project where the bundle is defined. Then follow these steps:

1.  In your project, click **Customize** in the top-right corner.
2.  Click **Bundles**.
3.  Open an existing bundle or click **Create bundle**.
4.  In the bundle editor, go to **Task types and templates**.
5.  Click **Add task types**.
6.  Choose the custom task types you want to include.
7.  Click **Continue** and then **Apply changes**.

The task types you add to the bundle are now part of that bundle. Any project that uses this bundle can surface those task types.

## Set a custom task type as the default task type for your project

Set your custom task template (Marketing request) as the default task type for your project by following the steps below. This will change usual user interface of the **+ Add task** button to **+ Add Marketing request** in this example. You can still add regular tasks and milestones to your project by clicking the dropdown menu beside the **+ Add Marketing request** button if needed.

1.  Click **Customize** in the top-right corner of your project
2.  Open **Project settings**
3.  Click the dropdown menu under **Set the default type**
4.  Choose your custom task template from the list 
5.  Note how the **+ Add task** button now displays **+ Add \[custom task type\]** instead

## Sort, group, and filter by custom task type and status

You can sort, group, and filter a project by custom task type or custom task status. Click **Filter**, **Sort**, or **Group**, then choose your custom task type from the dropdown menu. The example below shows how to filter the project to only show tasks which are Marketing requests, and only those which have the custom task status of **Approved**.

## Tasks maintain custom status when multi-homed

Tasks can only ever have one task type. This means that if you mark a task in your project as a custom task type, such as a Marketing request, the task will maintain its custom task type and status even when multi-homed into another project. The same custom task status options still appear in the task details, even when viewing the task outside of its original project.

## Task type character options

Custom task types include the ability to select custom characters and icons to represent your task type statuses. You can choose from various characters and icons that match each status in your workflow.

To use this feature:

1.   Click **Customize**, then **Project settings** at the bottom of the list
2.  Open your custom task type settings by selecting **+ New template** from the **Type** dropdown
3.  Create a new task type or edit an existing one
4.  Select characters, icons, or even emojis for each status
5.  Save the changes by clicking **Save** in the bottom-right corner

## Sharing custom task types

You can share custom task types you've created with others in your organization through the access control mode.

To share a custom task type:

1.  Click on your custom task type
2.  Select **Edit task type**
3.  Click **Manage access**
4.  You can select from four access levels for members in your organization or add users individually and set their access level

You can also add task types you have access to, to any project from the customize menu.

[](https://forum.asana.com/c/forum-en/tips/6)
