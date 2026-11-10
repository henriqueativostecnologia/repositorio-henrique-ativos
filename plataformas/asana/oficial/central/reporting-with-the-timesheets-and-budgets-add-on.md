---
fonte: https://help.asana.com/s/article/reporting-with-the-timesheets-and-budgets-add-on?language=en_US
baixado: 2026-11-10
---

# Reporting with the Timesheets and Budgets add-on

With the Timesheets and Budgets add-on, you can report on estimated time, actual time, estimated cost, or actual cost. 

Timesheets and Budgets add-on charts can be created in either project dashboards or portfolio dashboards. 

This article focuses on how to do reporting with the Timesheets and Budgets add-on. If you are interested in understanding what makes it different from reporting in Asana’s core product, see [Understanding the Value of Reporting with the Timesheets and Budgets add-on](https://help.asana.com/s/article/understanding-the-value-of-reporting-with-the-timesheets-and-budgets-add-on).

#### Related articles

- [Setting up timesheets and budgets add-on](https://help.asana.com/s/article/timesheets-and-budgets-add-on)
- [Logging and submitting timesheets](https://help.asana.com/s/article/logging-and-submitting-timesheets)
- [Managing timesheet reviewers and approvals](https://help.asana.com/s/article/managing-timesheet-reviewers-and-approvals)
- [Tracking project budgets and progress with timesheets and budgets add-on](https://help.asana.com/s/article/tracking-project-budgets-and-progress-with-timesheets-and-budgets-add-on)

### Creating a chart

To create a chart:

1.  Navigate to your project
2.  Click on the **Dashboard** tab
3.  Click **+ Add widget**
4.  From **Chart details** select **Time entries**
5.  You can the choose to report on **Time** or **Financials**

### Reporting on time

The time metrics included in timesheets charts are actual and estimated time.

> Timesheet charts can combine estimates and actuals and allow stacked bar charts.

**Actual time**

Aggregates the time entries set at the task level and the project level either using timesheets or directly on tasks.

**Estimated time**

Estimated time can come from two different sources: 

- From capacity plans, used for high-level estimates at the project level
- From tasks, for detailed, task-level estimates.

When reporting using the Timesheets and Budgets Addon, you can select whether the estimates should come from capacity plans, tasks, or both.

**Estimated time distribution**

When estimates come from capacity plans, charts will distribute time evenly across the unit of time you select. 

In the image below, a project has 200 hours of estimated time. The chart using “Working date” as a grouping (or X-axis) with a granularity of “Week”, is showing how those 200 hours are distributed in 4 groups (each group a week) of 50 hours. 

## Reporting on cost

The cost metrics included in timesheets charts are actual cost and estimated cost. Both metrics work by taking time (estimated or actual) and multiplying it by the [project rates](https://help.asana.com/s/article/timesheets-and-budgets-add-on#setting-people-rates-costs-measurement) that correspond to the team member and project.

> Cost data is only available to those who have admin access to the projects from where that data comes from. Specifically, the project from which the rates are being used.

**Actual cost**

Aggregates the time entries set at the task level and the project level and multiplies that time by the corresponding project rates to calculate cost.

For example a chart like the one below shows actual cost by teammate.

**Estimated cost**

Estimate cost aggregates the estimates set from those sources and multiplies them by the corresponding project rates to calculate the cost.

For example a chart like the one below shows estimated cost by teammate.

Estimated time can come from two different sources: 

- Capacity plans, for high-level estimates at the project level
- Tasks, for detailed, task-level estimates.

### Groupings (X-axis)

Grouping organizes metrics across different buckets. The groupings included in timesheets charts are:

**All dashboards**

- Staff: The people associated with the estimates or that logged the time entries.
- Billable / Non-billable: Whether the estimates or the time entries should be billed or not.
- Approval status: In which stage each time entry is in the approval process.
- Working date: The date or date range associated with the estimates of the time entries.

 

Project dashboards

- This project: The total value for a metric across the entire project the chart belongs to.

**Portfolio dashboards**

- Project: The different projects associated with the estimates or the time entries.
- This portfolio: The total value for a metric across the entire portfolio the chart belongs to.

### Filters

Filters narrow down the estimates or the time entries that get aggregated in a chart. The filters included in the timesheets charts are:

**All dashboards**

- Staff: The people associated with the estimates or that logged the time entries.

- Billable / Non-billable: Whether the estimates or the time entries should be billed or not.

- Approval status: In which stage each time entry is in the [approval process](https://help.asana.com/s/article/timesheets-and-budgets-add-on#approve-or-reject-timesheets).

- Working date: The date or date range associated with the estimates or the time entries.

**Portfolio dashboards**

- Project: The different projects associated with the estimates or the time entries.
