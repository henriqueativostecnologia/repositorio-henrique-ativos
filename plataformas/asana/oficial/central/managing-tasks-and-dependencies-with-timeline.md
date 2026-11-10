---
fonte: https://help.asana.com/s/article/managing-tasks-and-dependencies-with-timeline?language=en_US
baixado: 2026-11-10
---

# Managing tasks and dependencies with timeline

**Timeline is available on Asana [*Starter*](https://asana.com/plan/starter), [*Advanced*](https://asana.com/plan/advanced), [*Enterprise*](https://asana.com/enterprise), and [*Enterprise+*](https://asana.com/enterprise) tiers, as well as [*legacy tiers*](https://asana.com/pricing-legacy) Premium, Business, and Legacy Enterprise.**

**Visit our [*pricing page*](https://asana.com/pricing) for more information.**

This article delves into the nuances of setting dependencies, adjusting timelines, sharing your project's timeline, and exploring dependency date shifting options like maintaining, consuming, or ignoring due date buffers.

#### Related articles

- [Timeline](https://help.asana.com/s/article/timeline?language=en_US)
- [Critical path on timeline](https://help.asana.com/s/article/critical-path-on-timeline?language=en_US)

## Dependencies on your timeline

You can set dependencies directly on your timeline by clicking the **connector** icon that appears when hovering over a task and then dragging it to another task.

 

#### To draw dependencies on your timeline:

1.  Click on the **connector** icon when hovering over a task
2.  Drag the connector over to the task you wish to mark as **Dependent on**.

If the tasks in your project are [dependent on](https://help.asana.com/s/article/task-dependencies?language=en_US "dependent on") others, they will show as connected on your timeline.

If there are no date conflicts, a task will be connected to the task it’s dependent on via a grey line on your timeline.

If dependent tasks overlap on your timeline, for example, if one task has a start date that starts before a task it is dependent on is completed, a red dependency line will show up on your timeline to indicate a potential conflict.

### Zooming on your timeline

You can zoom on your timeline and view it by Hours, Days, Weeks, Months, Quarters, Half-year, or Years.

### Sharing your timeline

Anyone with access to your project will have access to the project’s timeline. If you’d like to share a timeline with someone in your company, you can send them the link to your project’s timeline if the project is public by copying the URL. Alternatively, add them as a [collaborator](https://asana.com/guide/help/tasks/understanding-tasks#gl-collaborators "collaborator") to tasks in your project if the project privacy settings are set to [private to members](https://help.asana.com/s/article/project-permissions?language=en_US).

## Dependency date shifting

### Dependency management options

There are three different dependency date shifting options to choose from.

To access the different date shifting options, click the drop-down menu next to your project’s name and select **Manage dependencies**, or click the **Project dependency settings** icon from the date picker.

From your timeline view, you can click **Options** in the top right corner of your project’s timeline view, then select **Project dependency settings**. The options are explained further below.

Note the requirements for auto-shifting due dates to work properly are as follows:

- A task has been **marked as dependent** on another, either **blocking** or **blocked by** another task.
- The blocking and blocked tasks both have due dates set. Start dates do not interfere with this process.
- Tasks are not marked as complete. Changes in dates will not have an impact on completed tasks

From your list view, you can add **Blocked by** and **Blocking** columns.

1.  Click **Options**
2.  Select **Show/Hide columns**
3.  Toggle on the **Blocked by** and **Blocking** columns
4.  Click **Save view**
5.  You can also click the **+** button next to the  last column

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

1.  **Choose party venue**, due on June 1
2.  **Organize catering**, due on June 3
3.  **Send out invites**, due on June 10

**Choose party venue** is blocking **Organize catering**, which itself is blocking **Send out invites**.

 

With slack shifting, moving the due date of **Organize catering** to June 7 will have no impact on either of the other tasks, since it does not cause a due date conflict. Similarly, the buffer between **Organize catering** and **Send out invites** is not maintained - the 7-day gap becomes a 3-day gap.

In the second phase of the example, **Organize catering** is still blocked by **Choose party venue**. Moving the due date of **Organize catering** forward in time to May 31 will result in a dependency due date conflict. Therefore, the due date of **Choose party venue** must move forward in time to accommodate this. The due date of **Choose party venue** moves forward one day in order to respect the dependency, and receives a new due date of May 30.

### Ignore due date buffer

Select **None** to ignore the amount of time between dependent tasks, even if there's a conflict. With this option, the buffer will neither be maintained or consumed. Conflicts between due dates of dependents tasks will also not be considered.

Consider the 3 tasks in the screenshot example provided.

1.  **Choose party venue**, due on June 1
2.  **Organize catering**, due on June 3
3.  **Send out invites**, due on June 10

**Choose party venue** is blocking **Organize catering**, which itself is blocking **Send out invites**.

 

With **None** selected, the amount of time between due dates is ignored entirely. In the example, the due dates change and do not respect the dependencies between the tasks. Blocked tasks can still be slated to be completed before tasks that they are dependent on.

## Work schedules

Use **work schedules** to automatically avoid scheduling tasks on weekends when shifting the due dates of dependent tasks.

### To define a project’s schedule: 

1.  Navigate to the **Customize menu**
2.  Click the **Project** **settings icon**
3.  Turn on the **Choose work hours toggle**
4.  Set your timezone, work days, and hours

> Project schedules will affect [tasks with dependencies](https://help.asana.com/s/article/task-dependencies?language=en_US) and timer custom fields.

[](https://forum.asana.com/c/forum-en/tips/6)
