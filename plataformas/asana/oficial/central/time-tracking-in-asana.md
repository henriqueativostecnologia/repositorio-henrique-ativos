---
fonte: https://help.asana.com/s/article/time-tracking-in-asana?language=en_US
baixado: 2026-11-10
---

# Time tracking in Asana

**Available on Asana [Advanced](https://asana.com/plan/advanced), [Enterprise](https://asana.com/enterprise), and [Enterprise+](https://asana.com/enterprise) tiers, as well as [legacy tiers](https://asana.com/pricing-legacy) Business and Legacy Enterprise.**

**Visit our [pricing page](https://asana.com/pricing) for more information.**

Asana’s native time tracking feature allows you to estimate the time needed to complete a task, as well as record the actual time spent. This valuable time data helps inform decisions regarding workload and resourcing, provides better information for real-time estimates on project progress, and can be instrumental for forecasting and budgeting. 

You can manually track time or rely on time logging to automatically calculate total actual time spent, based on different occasions that the task was worked on. It is also possible to report on time tracking data in dashboards, and estimated time can be sorted like other custom fields.

Explore time tracking for free. Start a [free Asana trial](https://asana.com/create-account) today.

Video: https://fast.wistia.net/embed/iframe/bqztuzuhh0?seo=true&videoFoam=false

## Enable time tracking in your project

To enable time tracking in your project:

1.  Click **Customize** in the top right corner
2.  Click **Fields**
3.  Click **+ Add**
4.  Select **Time your work** from the list

## Estimated time and Actual time fields

The custom fields **Estimated time** and **Actual time** will be added to the project. You can also add these fields via the custom field library.

1.  Estimated time
2.  Actual time
3.  Time log can record time for each occasion that the task is worked on
4.  Total time is automatically calculated from the time logs

## Reporting on time tracking data

You can report on time data in projects in much the same way as other custom fields by using dashboards.

### Estimated time by assignee

This example reports on the estimated time to complete tasks in a project based on each assignee. Recreate this chart by selecting the following:

- X-axis: **Assignee**
- Y-axis: **Custom field** \> **Estimated time**

### Estimated time by a group of assignees

You can also report on the total estimated time for tasks based on a select group of assignees within the project.

### Total actual time by section

You can also report on total actual time. This dashboard shows total actual time by section.

Recreate this chart by selecting the following:

- X-axis: **Section**
- Y-axis: **Time entry** \> **Actual time**

### Total actual time by custom field

Report on total actual time by custom field in a project.

Recreate this chart by selecting the following:

- X-axis: **Custom field** \> **Department**
- Y-axis: **Time entry** \> **Actual time**

## Time tracking live timer

You can now record **Actual time** spent on a task by using the start and stop live timer.

When the timer is running, a popup appears in the bottom-right corner of the screen with the running timer and task name. Clicking on the pop up will redirect you to the task which has the timer running. This way you can accurately and seamlessly keep track of the time spent on a task.

Clicking **Actual time** on a task will show each instance that the timer has run while the task is being worked on, as well as which user set the timer running. In the above example, the task was estimated to take 1 hour, and was worked on in two different periods; one of 45 minutes, and one of 15 minutes.

## Time tracking read API support

It is now possible to read time tracking information for tasks in the API. See further information on our [Community Forum](https://forum.asana.com/t/native-time-tracking-read-data/261390/9 "Community Forum").

## Time tracking subtask rollups

Values from **Actual time** and **Estimated time** fields in subtasks roll up to the parent task value.

When subtasks are expanded in list view, the subtask **Actual time** and **Estimated time** values and the parent task **Actual time** and **Estimated time** values are displayed separately.

When subtasks are collapsed in list view, subtask **Actual time** and **Estimated time** values are rolled up and added to the parent task values.

The **Actual time** and **Estimated time** values displayed next to the parent task show the sum of parent task and subtask **Actual time** and **Estimated time** values.

In the above example, the **Actual time** values of two subtasks (45 minutes and 30 minutes) are added to the **Actual time** value of the parent task (1 hour, 0 minutes), totalling 2 hours, 15 minutes. **Estimated time** values are rolled up in the same way.

## Time tracking support in templates

Time tracking fields are supported in templates. **Estimated time** and **Actual time** fields will be carried over to any project created from a template where these fields are present.

## Time tracking import and export support

It is possible to import and export time tracking values via CSV.

### Export time entries (beta)

**Note: This feature is currently in limited availability and may not be visible to all users.**

Easily export comprehensive time tracking data from your projects into CSV format for analysis and reporting. Time tracking export allows you to download detailed time entries organized by person and date. This provides better visibility into how time is being spent across projects. For example, project managers can do a CSV export of a project to identify how much time was spent on working on it by Bob last month.

#### To export time entries as CSV:

1.  Click the drop-down menu next to your project’s name
2.  Click **Sync/Export**
3.  Click **Time entries as CSV**

### Export total time per task

If you’d like the total time logged per task (without dates of when the time was logged or who logged it), you can use the standard CSV export of all project tasks. 

> A value of 1h 30min will be exported as 1:30

### Import

When importing time tracking values, Asana will recognize the following formats:

- *hh:mm*
- \_hr \_min
- \_h \_m

Numbers alone are assumed to be hours. Importing a value of **15** will be recognized as **15 hours**.

## Frequently asked questions

### How do I enable time tracking in Asana?

To enable time tracking, navigate to the customize menu in any project and click "time your work." This adds two custom fields to your project: estimated time and actual time.

### What's the difference between estimated time and actual time in Asana?

Estimated time lets you budget how long you expect a task to take, while actual time records how long you actually spend working on it. You can track actual time using the built-in timer or by entering time manually.

### How does the built-in timer work in Asana?

Click the actual time field on a task to start the timer, which continues running until you pause it. Asana automatically records the time you spent on the task when you stop the timer.

### Do subtasks roll up into the parent task for time tracking?

Yes, time tracked on subtasks automatically rolls up into the parent task. You can see the total of both estimated and actual time for all tasks within each project section.

 

**Want to learn more? Check out all the [features of Asana Time Tracking](https://asana.com/features/resource-management/time-tracking).**

[](https://forum.asana.com/c/forum-en/tips/6)
