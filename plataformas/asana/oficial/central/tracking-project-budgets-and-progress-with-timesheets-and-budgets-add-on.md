---
fonte: https://help.asana.com/s/article/tracking-project-budgets-and-progress-with-timesheets-and-budgets-add-on?language=en_US
baixado: 2026-11-10
---

# Tracking project budgets and progress with timesheets and budgets add-on

**Available as an add-on for [Starter](https://asana.com/plan/starter), [Advanced](https://asana.com/plan/advanced), [Enterprise](https://asana.com/enterprise), and [Enterprise+](https://asana.com/enterprise) tiers.**

Timesheets help you account for where your time is spent across multiple workstreams in Asana. As a time submitter, you can log hours against specific tasks or general project work and submit your weekly entries for review. In this article, you’ll learn how to access your timesheet, use the pre-populate feature, and log time.

#### Related articles

- [Logging and submitting timesheets](https://help.asana.com/s/article/logging-and-submitting-timesheets)
- [Setting up timesheets and budgets add-on](https://help.asana.com/s/article/timesheets-and-budgets-add-on)
- [Managing timesheet reviewers and approvals](https://help.asana.com/s/article/managing-timesheet-reviewers-and-approvals)
- [Reporting with the Timesheets and Budgets add-on](https://help.asana.com/s/article/reporting-with-the-timesheets-and-budgets-add-on)

## Project budgets

With project budgets, you can plan and forecast budgets.

### Accessing project budgets

You can access project budgets in two ways:

1.  Click the drop-down next to your project’s name and select **Set project budget**
2.  Navigate to the **Overview** tab of your project, scroll down to the **budget bar,** and click the settings button  on the bar

> You’ll need to be a project admin to access project budgets.

## Project budgets progress bar

The progress bar will show you how much of the actual work is tracking against the planned work, and the remaining amount.

## Choosing a budget type

You can track your budget through hours or costs. You can also toggle between the two measurement types.

## Setting threshold notifications for budgets

A user can indicate a threshold where they want to be notified about budget progress. 

To enable budget notification:

1.  Open the budget modal in a project with a budget set up
2.  Turn on the setting for threshold notifications
3.  Indicate which value actual costs should be compared against and at what percent the user would like to be notified at.

## Project budget rollups in portfolios

Users can view budgets of multiple projects at the portfolio level to understand aggregations of cost or time, depending on the type of budget a project has.

1.  Navigate to the list view of the portfolio.
2.  Ensure projects with set budgets have been added. (Note: Use 'Add work' to add projects.)
3.  Click the **+** icon on the right corner of the list view to add a new field.
4.  Select one of the budget options to add rollups:
    1.  **Budget (Time):** Adds rollups for Estimated Time (total), Actual Time (total), and Budgeted Time.
    2.  **Budget (Costs):** Adds rollups for Estimated Costs (total), Actual Costs (total), and Budgeted Costs.

> Cost aggregations are only visible to those appropriate permissions.

## Estimated costs or time

For estimated costs, you can choose from two sources; capacity plans or tasks.

### Capacity plans

**Available on** [**Enterprise**](https://asana.com/enterprise) **and** [**Enterprise+**](https://asana.com/enterprise) **tiers.**

As team members are allocated into the project, you’ll be able to see the cost breakdown in the capacity plan view, based on the rates.

The total cost per person will show up on the capacity plan, and the summation will be visible on the project budget.

### Tasks

If allocation is done by estimated times on tasks, this will tie directly to the project to provide that project budget, either in hours or costs, depending on what you’ve selected.

## Actual costs or time

Actual costs will be calculated using actual time from [time tracking](https://help.asana.com/s/article/time-tracking-in-asana) or from timesheets, as they are being submitted. You can break down actual costs by their billable or non-billable, or all time. This will depend on how you’ve configured actual costs.

## Costs in resource management

Once rates are set, you can view costs in [capacity planning](https://help.asana.com/s/article/capacity-planning) and [workload](https://help.asana.com/s/article/portfolio-workload-and-universal-workload) views.

1.  Navigate to a **Workload** or **Capacity planning** view.
2.  In the effort drop-down menu select **Estimated time** or **Actual time**. Then switch the **Cost toggle** on. 

Cost data is designed to ensure it's only editable and visible to the right people.

- **Rate management:** Only **Project admins** have the ability to set the hourly rates for users within that specific project.
- **Cost visibility:** Only  **Project admins** on a given project will be able to see the cost data associated with that project in workload and capacity planning views.

## Setting people rates (Costs measurement)

If you’ve chosen **Costs** as your measurement type, you can designate hourly rates for people working on the project. This rate can also be maintained in their **Capacity plan** view.

To set a rate for a person or placeholder:

1.  Scroll down to the **People and rates** section in the project budget settings.
2.  Click inside of the **Add people** search bar and select people or placeholders.
3.  Type in or select people and click **Add** to add them to your resource pool.
4.  Click on the Rate box and input a number. 
5.  Click **X** to remove the rate from the budget
6.  Click **Save rates** to save any new changes made to the people and rates section.

A few additional notes:

- Placeholders and capacity plans are available on Enterprise and Enterprise+ tiers, so users must have a base Enterprise or Enterprise+ license to use these features with the Timesheets and Budgets add-on.
- Users can set up to 500 people or placeholders in each project’s resource pool.
- Individuals do not need to be a project member to be in the rates list. If a person leaves the project halfway, their rate will still appear in the resource pool and would need to be manually removed. 

## Bulk adding teams and rates to projects

If you’re a project admin, you can bulk add entire Asana teams to a project, allowing you to staff projects quickly, consistently, and with the correct, standardized rates every time.

To add teams to projects:

1.  Start typing the name of the team
2.  The search will find teams you have access to, including teams you belong to and public teams
3.  Select a team from the search results by clicking on it or using your keyboard

> Teams with more than 200 members cannot be added in bulk and will appear grayed out in search results. A single project cannot have more than 500 people staffed to it. The system will prevent you from adding teams that would exceed this limit.

When you click to add a selected team, the system takes a **one-time snapshot** of the team's current membership. It adds each person from that team to your project budget setting list individually. If a person is already on the project list, or if they are a member of multiple teams you've selected, they will only appear once.

> This is not a dynamic sync. If new people are added to the Asana Team later, they will not be automatically added to this project. You would need to add them separately.

### Importing rates along with people

 If your teams have rates defined in a number-based custom field, you can import them directly.

To import rates:

1.  Next to each selected team pill, a drop-down menu will appear. This menu will list all the number-based custom fields from that team that you have permission to see.
2.  Select the desired custom field

> All numbers will be automatically rounded to two decimal places. If the field format is a percentage, it will be converted to a number.

To prevent accidental data loss, the system will not automatically overwrite rates. Instead, it will import all rates and require you to resolve them manually.
