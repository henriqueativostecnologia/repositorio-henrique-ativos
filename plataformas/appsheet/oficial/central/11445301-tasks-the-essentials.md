---
fonte: https://support.google.com/appsheet/answer/11445301?hl=en
baixado: 2026-11-10
---

# Tasks: The Essentials

Define the tasks you want to run in a process in your bot:

- [What is a task?](#what-is-task)
- [Supported task types](#supported-task-types)
- [Add a task to a bot](#add-task)
- [Copy an existing task](#copy-existing-task)
- [View tasks](#view-tasks)
- [Edit a task](#edit-task)
- [Delete a task](#delete-task)

## What is a task?

A task is a simple activity that runs quickly. For example, you can send someone a message (email, SMS), change data, or call an external service.

You [add a task as a step in a process](#add-task). Tasks can be reused across processes.

Tasks in a process in a bot.

## Supported task types

AppSheet supports the following types of tasks:

- [Use AI](https://support.google.com/appsheet/answer/16045284) to extract information from a file or photo, or categorize information using predefined categories
- [Send an email](https://support.google.com/appsheet/answer/11447614)
- [Send a notification](https://support.google.com/appsheet/answer/11513089)
- [Send an SMS message](https://support.google.com/appsheet/answer/11509435)
- [Call a webhook](https://support.google.com/appsheet/answer/11511244)
- [Create and save a file](https://support.google.com/appsheet/answer/11512511)
- [Call a script](https://support.google.com/appsheet/answer/11997142)
- [Send a chat message](https://support.google.com/appsheet/answer/12981549)

## Add a task to a bot

Add a task to a bot as a [step](https://support.google.com/appsheet/answer/11463007) in a [process](https://support.google.com/appsheet/answer/11445386) using AppSheet:

1.  Click **Add a step** in the process flow
2.  Select **Run a task**.
3.  Optionally, do one of the following:
    - **Choose from the list of suggestions.** AppSheet Automation is an intent-aware platform. The platform understands user intent and recommends configuration options that align with what you are trying to achieve. For example, selecting the following bot suggestion would configure a basic **Send an email** task for you:

      When a new **NationalParks** record is created, send an email
    - **Reuse an existing task**. Click **Custom** **task** and select an existing task from the list.
4.  Select the [task type](#supported-task-types) and configure the task.

We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

## If you are using the legacy editor

Add a task to a bot as a [step](https://support.google.com/appsheet/answer/11463007) in a [process](https://support.google.com/appsheet/answer/11445386) using AppSheet in one of the following ways:

- **Choose from the list of suggestions.** AppSheet Automation is an intent-aware platform. The platform understands user intent and recommends configuration options that align with what you are trying to achieve. For example, selecting the following bot suggestion would configure a basic **Send an email** task for you:

  `When a new `**`NationalParks`**` record is created, send an email`
- **Reuse an existing task.** When creating a custom [step](https://support.google.com/appsheet/answer/11463007) in a process, click **Run a task** and select an existing task from the list.
- **Create a custom task.**
  - When creating a custom [step](https://support.google.com/appsheet/answer/11463007) in a process, click **Run a task**, then select **Create new task** in the **Task to run** list to create a reusable task and include it in the existing process.
  - Select **Automation \> Tasks** and click **+ New Task** to create a reusable task that can be used in any bot process.

## ****Copy an existing task

Copy an existing task. The name of the new tasks defaults to the name of the current task followed by a unique number (starting with 1 and incrementing), such as **My Task 1**.

To copy an existing reusable task:

1.  Select **Automation \> Tasks**.
2.  Select the task you want to copy.
3.  Click **Copy** in the task heading.

We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

## If you are using the legacy editor

 

To copy a task:

1.  Select **Automation \> Tasks**.
2.  Select the task you want to copy.
3.  Click **Copy **in the task heading.

## ****View tasks

 To view all tasks, select **Automation ** Automation icon **\> Tasks**. Tasks are organized by table.

By default, only [reusable (linkable) tasks](https://support.google.com/appsheet/answer/12193489) are shown. To view all tasks, turn on **Show all automation components**, as described in [Configure app editor settings](https://support.google.com/appsheet/answer/13396480).

If a reusable task is used by one or more bots, it displays a reusability indicator (number in the task header) to indicate the number of bots using the task. Click the number to view the list of bots that are using the task. For more information, see [Reuse automation components](https://support.google.com/appsheet/answer/12193489).

## ****Edit a task

**Note**: If editing a [reusable task](https://support.google.com/appsheet/answer/12193489), consider the impact to all processes before editing the task.

To edit a task, [view the task](#view-task) in the app editor, edit the configuration, and save your changes.

## ****Delete a task

 Deleting a [reusable task](https://support.google.com/appsheet/answer/12193489) that is used in one or more processes may negatively impact the execution of those processes. If you try to delete a task that is used by one or more processes, AppSheet will prompt you to confirm the operation, as shown:

Warning displayed for reusable component when attempting to delete

To delete a reusable task:

1.  Select **Automation \> Tasks**.
2.  Select the task you want to delete.
3.   Click **More**  Three-dot menu vertical   **\> Delete** in the task heading.

To delete a task used in a bot:

1.  Select **Automation \> Bots**.
2.  Select the task in the process flow in the center pane.
3.  Click **More**  Three-dot menu vertical   **\> Delete**.

We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

 

## If you are using the legacy editor

 

To delete a resuable task:

1.  Select **Automation \> Tasks**.
2.  Select the task you want to delete.
3.  Click **Delete** in the task heading.

 To delete a task used in a bot:

1.  Select **Automation \> Bots**.
2.  Locate the task in the process flow in the center pane.
3.  Click **More**  Three-dot menu vertical   **\> Delete**.
