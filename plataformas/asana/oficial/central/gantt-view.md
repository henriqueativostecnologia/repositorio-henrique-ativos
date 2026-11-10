---
fonte: https://help.asana.com/s/article/gantt-view?language=en_US
baixado: 2026-11-10
---

# Gantt view

**Available on Asana [*Starter*](https://asana.com/plan/starter), [*Advanced*](https://asana.com/plan/advanced), [*Enterprise*](https://asana.com/enterprise), and [*Enterprise+*](https://asana.com/enterprise) tiers, as well as [*legacy tiers*](https://asana.com/pricing-legacy) Premium, Business, and Legacy Enterprise.**

**Visit our [*pricing page*](https://asana.com/pricing) for more information.**

Gantt view equips project managers with the tools to visualize and manage project plans effectively, offering insight into task durations, delivery dates, dependencies, and baseline of your project plan. Gantt view is particularly valuable for large, structured, complex projects that require meticulous planning and comparison of original plans against real-time progress.

#### Related articles

- [Gantt view FAQ](https://help.asana.com/s/article/gantt-view-faq?language=en_US)

## Adding and removing Gantt view

Gantt view is available for both new and existing projects. You can add/remove Gantt view as follows:

1.  Click the **+** icon in the project tabs menu.
2.  Choose **Gantt** from the drop-down menu. Gantt view will be added as a new tab.
3.  To remove Gantt view, click the **Gantt** tab and click **Remove.**

> Removing **Gantt view** from your project will not delete any tasks, this will simply remove the view. The view can be added again at any time.

## Key benefits of Gantt view

**Strategic planning:** Gantt view allows you to plan and estimate essential delivery dates by leveraging task auto-scheduling and duration calculation.

**End-to-end management:** With a clear depiction of work schedules, including subtasks and dependencies, project managers can effectively oversee projects from start to finish, ensuring seamless coordination.

**Progress monitoring:** One of the standout features of Gantt view is its ability to monitor project deviations over time. By comparing current progress against an established baseline, project managers gain insights into how well a project adheres to its original plan.

**Enhancements and new features:** In project management, the complexity of tasks can escalate with the size of the project. Gantt view addresses this challenge by providing an intuitive interface to schedule and manage projects. This view condenses tasks, durations, key dates, and dependencies into a single, accessible location. This is particularly advantageous for larger projects, allowing project managers to gain a holistic perspective and make informed decisions.

**Structured and process-oriented approach:** Gantt view is not only a tool for visualizing projects; it also facilitates structured and process-oriented project management right from the outset. This is especially beneficial for projects that require well-defined workflows and adherence to procedures.

## Using Gantt view

To view a project in Gantt view, you will need to [add the view to your project](https://help.asana.com/s/article/gantt-view#h_01H9TNV17ZEHSG8FTH3G8Z47TJ). Once the view has been added, open your project in Asana and navigate to the **Gantt** tab.

- A list style view is shown on the left, divided into sections identical to your project’s **List view**.
- You can filter your Gantt view to show **All tasks**, **Completed tasks** or **Incomplete tasks**.
- You can choose to view your tasks by **Days**, **Weeks**, **Months**, **Quarters**, **Half-years** and **Years**.
- You can filter your Gantt view to show **All tasks**, **Completed tasks** or **Incomplete tasks**.

More information on the **Color**, **Auto-scheduling** and **Baseline** features can be found below .

> You can create chain dependencies in bulk with Gantt view. To do so, [multi-select](https://help.asana.com/s/article/task-actions?language=en_US#gl-multi-select) the relevant tasks and select the **Chain dependencies** option from the pop-up bar that appears at the bottom of the screen.

## Changing the bar colors in Gantt view

You can map the colors of the bar to a custom field in Gantt view.

  

To this this:

1.  Click on the **Options** button in the upper right-hand corner.
2.  Click **Layout options**
3.  Click the **Color tasks by** drop-down and choose your preferred option
4.  Click **Save view**

Advantages and examples of color mapping to a custom field include:

- If your custom field represents various teams (marketing, product, design and engineering, for example), coloring the bars accordingly allows you to view which team is working on what, at a glance.
- If your custom field represents the status of a task, color mapping to that custom field would give extra visual information on the overall status of your project. The example in the gif above shows a priority custom field, allowing users to identify high and low priority tasks at a glance.

## Compact mode

Compact mode condenses the information shown in the left pane, allowing you to view more tasks at once.

To enable compact mode:

- Click **Options** on the upper right within Gantt view.
- Select **Go to settings** within the tip shown at the top of the **Options** menu.
- The will open the **Display** tab of the settings menu, from here check the box to **Enable compact mode** under **Advanced options**.

## Adding a baseline

Baseline captures a snapshot of the project (including tasks, dates, durations, etc.) at a point in time. It can be used for a visual comparison of the captured vs. current project plans to show how the project has deviated over time.

#### To add a baseline:

1.  Open a project in **Gantt view**
2.  Click **Options**
3.  Click **Dependency settings**
4.  Add a baseline date. This date is the day on which you’d like to view the previous state of the project.
5.  Adding a date will automatically switch on the **Show baseline** toggle. You can click the toggle to switch this off again.

The rectangles with the diagonal hash pattern show the original plan, which you can compare against the current project shown via solid rectangles.

> Each project can only have 1 baseline. Creating additional snapshots override the current snapshot.

## Creating dependencies in Gantt view

[Dependencies](https://help.asana.com/s/article/task-dependencies#h_01HQTB67SZ74DTZ7JH4SYZVZYV) are the relationships among tasks that determine the order in which activities need to be performed. With task dependencies, you can mark a task as blocking another task, or blocked by another task. You can create task dependencies within Gantt view using drag and drop.

To create task dependencies:

- Hover over the task block (pink in the example shown) to make the dependency handle appear.
- Drag the handle to another task to create a dependency.
- Once you’ve created a dependency, the dependency drop-down arrow appears.
- Click the drop-down arrow to choose the dependency type.

## Auto-schedule tasks

To help you quickly create your project structure, Asana will automatically assign dates to new tasks in Gantt view. As you create tasks, they’ll have consecutive date ranges as well as a duration of 1 day by default. If you zoom out to a half-year or year view, the date ranges will be populated as a duration of 5 days by default.

Auto-scheduling is enabled by default. If you wish to turn off auto-scheduling, follow the steps below:

- To turn off auto-scheduling, open a project in **Gantt view**.
- Click **Gant options** in the upper right-hand corner above the Gantt chart.
- Toggle off **Auto-schedule tasks.**

#### Additional notes:

- By default, tasks will be auto-scheduled and sorted by start date.
- If auto-scheduling is on, your first task created will have a start date of the project start date. If there is no project start date, the first task’s start date will be set to today.
- Each subsequent task will be given a due date that is one day afterwards.
- Auto-schedule mode is supported when sorting by both **Start date** and **None**, but has slightly different behavior in each. You can also manually schedule tasks.
- If auto-scheduling is disabled and then re-enabled, it will not overwrite the dates you have already added to the project.

> Need Gantt view guidance? [Ask the Community](https://forum.asana.com/c/forum-en/tips/6).
