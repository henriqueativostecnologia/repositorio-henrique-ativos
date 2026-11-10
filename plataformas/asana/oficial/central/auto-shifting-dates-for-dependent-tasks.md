---
fonte: https://help.asana.com/s/article/auto-shifting-dates-for-dependent-tasks?language=en_US
baixado: 2026-11-10
---

# Auto-shifting dates for dependent tasks

**Available on Asana [Starter](https://asana.com/plan/starter), [Advanced](https://asana.com/plan/advanced), [Enterprise](https://asana.com/enterprise), and [Enterprise+](https://asana.com/enterprise) tiers, as well as [legacy tiers](https://asana.com/pricing-legacy) Premium, Business, and Legacy Enterprise.**

**Visit our [pricing page](https://asana.com/pricing) for more information.**

When changing the due dates of tasks with dependencies results in a due date overlap, this feature can auto-shift the due dates based on your preferences. Auto-shifting dates for dependent tasks is now available in list, board, calendar, timeline, and Gantt view.

There are three different dependency date shifting options to choose from in the project’s list, board, calendar, timeline, and Gantt view. To access project dependency settings, click the drop-down next to your project’s name and click **Manage dependencies**

You can choose to maintain the buffer between dependent tasks, consume the buffer or ignore the buffer. **None** is the default setting for dependency date shifting. Only new projects with a Gantt tab will be set to **Consume buffer**.

#### Related articles

- [Task dependencies](https://help.asana.com/s/article/task-dependencies?language=en_US)

## Requirements for auto-shifting dates

For auto-shifting to work, the following criteria must be met:

- A task has been marked as dependent on another
- The precedent and dependent tasks have due dates set. This also works when a start date and a due date are set.
- The dependency setting is set to maintain or consume buffer.
- Tasks are not marked as complete. Auto-shifting dates will not impact completed tasks.
- For consume buffer only: the change in any of the tasks causes an overlap in the dates.

This functionality does not apply to subtasks by default. You can mark subtasks as dependent on the parent task if you want to use auto-shifting for subtasks.

## Using the auto-shifting dates feature in list view

You can use auto-shifting while updating dates in list view.

If the **Consume buffer** setting is enabled, a change on a precedent task’s due date will update the date of the dependent task when the change causes an overlap and a change on a dependent task’s due date will update the date of the precedent task when the change causes an overlap.

Any change to the start date as a result of the auto-shifting dependency dates feature also changes the due date of that same task (and vice-versa).

The auto-shifting dependency dates feature automatically skips weekends. You can also edit this from the **Project settings** in the **Customize menu**.

In addition, it works for changes that move the dates backward or forward. When a precedent task’s date is pushed forward in the future, this precedent task can move dependent tasks forward as well. However, when "consume buffer" is enabled, if the date of a dependent task is postponed, it will not affect the preceding tasks since there will be no overlap.

When a dependent task’s date is pushed back in the past, the precedent task will remain the same. However, when "consume buffer" is enabled, if the date of a dependent task is pushed back, the dependent task can also push back the precedent task.

## Auto-shifting due dates in action

When a task with dependencies has its dates changed in any view except Timeline and Gantt, a modal will appear displaying all the resulting date changes for dependent tasks. You can adjust the new dates within the modal and confirm the changes, after which all dependent task dates will be updated accordingly.

The date picker shows what dependency settings the project is set to. 

You can click on the project dependency settings icon at the top right of the date picker to open the project’s dependency settings.

You can play around with dates for the parent task and see the new due dates for dependent tasks on the right side. Once the changes are saved, you can see the new due dates reflected in the list view.

## Using the auto-shifting dates feature in board and calendar view

1.  In either board or calendar view you will need to click on the task to open the task details pane.
2.  Click on the due date to open the date picker.
3.  Click on **Preview** to review dependent tasks.
4.  Add your new due date or date range on the left-hand side to see how this will affect dependent tasks.
5.  The new date range for dependent tasks will be populated on the right.
6.  Click **Save changes** to save your new due date and auto-shift the dates of any dependent tasks.

## Autoshifting on board and calendar view

### Board view

Click on the due date to open the date picker and add your new due date or date range.

### Calendar view

In calendar view, dragging the task from one date to another will show the same confirmation modal, as well as changing the dates from the task pane.

Click [here](https://asana.com/guide/help/tasks/dependencies#gl-auto-shifting-dates) to see examples of auto-shifting in action in timeline view.

## Dependency management options

There are three different dependency date shifting options to choose from.

To access the different date shifting options, click the drop-down menu next to your project’s name and select **Manage dependencies**, or click the **Project dependency settings** icon from the date picker.

From your timeline view, you can click **Options** in the top right corner of your project’s timeline view, then select **Project dependency settings**. The options are explained further below.

Note the requirements for auto-shifting due dates to work properly are as follows:

- A task has been **marked as dependent** on another, either **blocking** or **blocked by** another task.
- The blocking and blocked tasks both have due dates set. Start dates do not interfere with this process.
- Tasks are not marked as complete. Changes in dates will not have an impact on completed tasks

### Maintain due date buffer with lag shifting

Select **Maintain buffer** to maintain the amount of time between dependent tasks. This process is known as lag shifting.

You can choose to maintain a buffer for all dependent tasks, or only for downstream dependent tasks.

#### Maintain buffer for all dependent tasks

All the tasks in the dependency chain will move, including the precedent task. The due date of the precedent task and the dependent task will move relative to the shifted task’s due date.

#### Maintain buffer for downstream dependent tasks

The precedent task won’t move and only the downstream tasks in the dependency chain will shift.

Consider the 3 tasks in the screenshot example provided. For this example, we’ll maintain the buffer for all dependent tasks.

1.  **Choose party venue**, due on May 30.
2.  **Organize catering**, due on June 1.
3.  **Send out invites**, due on June 13.

**Choose party venue** is blocking **Organize catering**, which itself is blocking **Send out invites**.

With lag shifting, moving the due date of **Organize catering** back by one week to June 8 means that the due date of **Send out invites** will shift by one week to preserve the gap. The gap between **Choose party venue** and **Organize catering** will change if the due date of **Organize catering** changes.

### Consume due date buffer with slack shifting

Select **Consume buffer** to consume the amount of time between dependent tasks unless there's a conflict. This is also known as slack shifting.

In consuming the buffer between two dependent tasks, the due date of one task will not move relative to the shifted task’s due date.

Consider the 3 tasks in the screenshot example provided.

1.  **Choose party venue**, due on June 1.
2.  **Organize catering**, due on June 3.
3.  **Send out invites**, due on June 10.

**Choose party venue** is blocking **Organize catering**, which itself is blocking **Send out invites**.

 

With slack shifting, moving the due date of **Organize catering** to June 7 will have no impact on either of the other tasks, since it does not cause a due date conflict. Similarly, the buffer between **Organize catering** and **Send out invites** is not maintained - the 7-day gap becomes a 3-day gap.

In the second phase of the example, **Organize catering** is still blocked by **Choose party venue**. Moving the due date of **Organize catering** forward in time to May 31 will result in a dependency due date conflict. Therefore, the due date of **Choose party venue** must move forward in time to accommodate this. The due date of **Choose party venue** moves forward one day in order to respect the dependency, and receives a new due date of May 30.

### Ignore due date buffer

Select **None** to ignore the amount of time between dependent tasks, even if there's a conflict. With this option, the buffer will neither be maintained or consumed. Conflicts between due dates of dependents tasks will also not be considered.

Consider the 3 tasks in the screenshot example provided.

1.  **Choose party venue**, due on June 1.
2.  **Organize catering**, due on June 3.
3.  **Send out invites**, due on June 10.

**Choose party venue** is blocking **Organize catering**, which itself is blocking **Send out invites**.

With **None** selected, the amount of time between due dates is ignored entirely. In the example, the due dates change and do not respect the dependencies between the tasks. Blocked tasks can still be slated to be completed before tasks that they are dependent on.

> Questions about auto-shifting dates? [Ask the Community](https://forum.asana.com/c/forum-en/tips/6).

[](https://forum.asana.com/c/forum-en/tips/6)
