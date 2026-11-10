---
fonte: https://support.google.com/appsheet/answer/11445386?hl=en
baixado: 2026-11-10
---

# Processes: The Essentials

Run a set of activities in your bot using a *process* as described in the following sections:

- [What is a process?](#what-is)
- [Add a process to a bot](#add-process-to-bot)
- [Create a process](#create-process)
- [View processes](#view-processes)
- [Edit a process](#edit-process)
- [Delete a process](#delete-process)

## What is a process?

A *process* combines tasks into composite activities. A process represents a typical business process, such as an order approval.

A process may run a simple set of [tasks](https://support.google.com/appsheet/answer/11445301) sequentially, such as send an email or create a file. A more complex process might take hours or days to complete if it includes more time-consuming activities, such as:

- Loop over many records and call a task for each of them
- Call other processes
- Wait for a human to respond to something

Process in a bot with tasks

A process contains the following elements:

- An input (a row in a table this process will work on)
- A sequence of **[steps](https://support.google.com/appsheet/answer/11463007)**

For example, in the screenshot below you can see a sample **Confirmed appointment** process that contains the following elements:

- Table: A row in the **Appointments** table.
- Step: **Send an email**

Process that sends a daily email

## Add a process to a bot

Add a process to a bot using AppSheet in one of the following ways:

- **Create a new process**
  See [Create a new process](#create-process).
- **Reuse an existing process **(if a linkable process is available)
  In the **Then run...** drop-down select a linkable process. See [Reuse automation components](https://support.google.com/appsheet/answer/12193489).

## Create a new process

AppSheet Automation enables you to build processes once and reuse them in various automations to save time and accelerate development. See also [About component reusability with AppSheet Automation](https://support.google.com/appsheet/answer/11431791#bot-component-reusability).

To create a new process:

- To create a new process within a bot, simply [add steps](https://support.google.com/appsheet/answer/11463007) to the process in the **Then run...** section.
- To create a reusable process, select **Automation** Automation icon ** \> Processes** and click **+ **in the **Processes** panel.

## If you are using the legacy editor

To create a new process:

- When creating or editing a bot, select **Create new process** in the **Run this Process** drop-down list.
- Select **Automation \> Processes** and click **New Process**.

To copy an existing process:

1.  Select **Automation** Automation icon ** \> Processes**.
2.  Select the process you want to copy in the **Processes** panel.
3.  Click **More**  Three-dot menu vertical   **\> Duplicate** in the process heading.

The existing process is copied. The name of the new process defaults to the name of the current process followed by a unique number (starting with 1 and incrementing), such as **Onboard new employees 1**.

## If you are using the legacy editor

To copy an existing process:

1.  Select **Automation \> Processes**.
2.  Select the process you want to copy.
3.  Click **Copy** in the process heading.

The existing process is copied. The name of the new process defaults to the name of the current process followed by a unique number (starting with 1 and incrementing), such as **Onboard new employees 1**.

## View processes

To view all processes, select **Automation ** Automation icon **\> Processes**. Processes are organized by their table association or under `Other` if there is no table association.

By default, only [reusable (linkable) processes](https://support.google.com/appsheet/answer/12193489) are shown. To view all processes, turn on **Show all automation components**, as described in [Configure app editor settings](https://support.google.com/appsheet/answer/13396480).

If a reusable process is used by one or more bots, it displays a reusability indicator (number in the process header) to indicate the number of bots using the process. Click the number to view the list of bots that are using the process. For more information, see [Reuse automation components](https://support.google.com/appsheet/answer/12193489).

## Edit a process

**Note**: If a process is reused, consider the impact to all bots before editing the process.

To edit a process, [view the process](#view-processes) in the editor, edit the steps, and save your changes.

## Delete a process

**Note**: If a [reusable process](https://support.google.com/appsheet/answer/12193489) is used in multiple bots, consider the impact to all bots before deleting the process. If you try to delete a process that is used by one or more bots, AppSheet will prompt you to confirm the operation.

Warning displayed for reusable component when attempting to delete

To delete a reusable process:

1.  Select **Automation** Automation icon ** \> Processes**.
2.  Select the process you want to delete in the **Processes** panel.
3.  Click **More**  Three-dot menu vertical   **\> Delete** in the process heading.

 

## If you are using the legacy editor

 

To delete a process:

1.  Select **Automation \> Processes**.
2.  Select the process you want to delete.
3.  Click **Delete** in the process heading.
4.  To delete a process used in a bot:
5.  Select **Automation \> Bots**.
6.  Select **Remove** from the **Then run...** process drop-down.
