---
fonte: https://help.asana.com/s/article/chart-styles?language=en_US
baixado: 2026-11-10
---

# Chart styles

Charts provide a graphic overview of data associated with tasks, projects, portfolios, and goals. You can have up to 20 charts on a single dashboard.

To add a chart to a dashboard, click **Add chart**.

## Bar chart

Customize a simple bar chart by adding filters, or choosing different fields for the X- and Y-axes.

## Stacked bar chart

Gain an understanding of both the quantity and status of tasks at once with a stacked bar chart. Stacked bar charts allow you to compare totals and the categories that contribute to them over time or across groups. Each bar shows a total value, divided into segments representing individual categories, making it easy for you to see both the full picture and the specific contributions of each part.

Example: Total tasks by region of request and task status

## Grouped bar charts

Use grouped bar charts to visualize and compare a primary field grouped by a secondary field along a single Y-axis metric. This allows you to easily break data into groups and compare key data points over a metric.

To create a grouped bar chart:

1.  Navigate to **Dashboard** tab of your project
2.  Click **+ Add chart** or edit an existing chart
3.  Select **Grouped bar** as the chart type
4.  Choose your primary field for the X-axis and the field to group by
5.  Select the Y-axis metric to measure and compare
6.  Customize your chart settings and click **Add**

The resulting grouped bar chart will display your primary field grouped by your secondary field, enabling you to compare the Y-axis metric across groups at a glance.

## Line chart

Line charts help you illustrate trends over time and understand which processes are more effective within your team. 

You can use manual benchmark lines, allowing you to add a user-defined reference line directly within your line charts. This provides a clear visual way to compare actual performance against targets, thresholds, or goals. Whether you're tracking project budgets, team velocity, or campaign metrics, benchmark lines help you contextualize your data at a glance and make more informed decisions about your work.

## Burnup charts

This chart helps you track your team’s velocity over time and how quickly your team is completing work.

Example: Task completion over an amount of time.

## Burndown chart

**Available on Asana** [**Starter**](https://asana.com/plan/starter)**,** [** Advanced**](https://asana.com/plan/advanced)**,** [ **Enterprise**](https://asana.com/enterprise)**, and** [ **Enterprise+**](https://asana.com/enterprise) **tiers, as well as** [ **legacy tiers**](https://asana.com/pricing-legacy) **Premium,** **Business, and Legacy Enterprise.**

Burndown charts are a visual representation of work left to do versus time. They help teams track progress, predict completion dates, and identify potential delays in projects. Burndown charts provide a clear overview of project status, enabling teams to make data-driven decisions and adjust their strategies as needed.

### Benefits of using burndown charts:

- Visualize project progress at a glance
- Predict project completion dates more accurately
- Identify potential delays or roadblocks early
- Improve team accountability and transparency
- Facilitate data-driven decision-making
- Enhance sprint and project planning

### Using burndown charts

Burndown charts in Asana provide a graphical representation of work remaining over time. The chart displays two key elements:

1.  **Total task count:** This line represents the total number of tasks in the project.
2.  **Burndown line**: This line shows the work completed over time, allowing teams to compare their progress against the ideal scenario.

### To create a burndown chart:

1.  Navigate to your project in Asana and open the **Dashboard** tab
2.  Click on **+ Add chart** in the top left corner
3.  Select **Burndown** from the available options under **Chart style**
4.  Adjust the details under **X-axis** to suit your needs and click **Add**.

When you click on the chart while the tooltip is visible, it will take you to the Advanced Search for that specific area. This makes it easier to follow up on any tasks that are still pending.

The chart automatically updates as tasks are completed, providing real-time insights into project progress.

> Ensure all tasks in your project have accurate due dates and completion statuses for the most precise burndown data. For large projects, consider breaking down work into smaller, manageable chunks to get more granular burndown data.

### Burndown charts and Jira data sync 

You can sync data from Jira Issues into Asana projects and create burndown charts from synced data from [Jira Cloud](https://help.asana.com/s/article/asana-for-jira-cloud?language=en_US). For example, you can sync story points from Jira Cloud, and build a burndown chart with story points in Asana.

## Donut charts

Donut charts cannot use averages as their measure, as they are designed to show the proportions or percentages of a whole. Each data point in a donut chart represents a part of the total, and the chart is divided into segments to illustrate these parts. Since averages represent a central tendency or an arithmetic mean, they don't inherently represent parts of a whole.

If a task is [multi-homed](https://asana.com/guide/examples/workflow-basics/adding-movement-to-your-workflow#sts=Multi-homing) across multiple projects and a chart is then grouped by project, the task will be counted separately for each associated project. This means the task will be double-counted, as it will contribute to the count of each project it belongs to.

The task count shown in a donut chart (the number in the middle) will include these duplicate tasks, as multi-homed tasks will be accounted for more than once in this number.

With donut charts you can:

- Get a quick pulse on how big each of your work slices is. For example, are your incomplete tasks a tiny or large piece of the pie?

- Visually represent tasks by completion status or tasks by section custom field by swapping out one for the other or clicking the Pencil icon to customize your chart.

## Number chart

You can add a number field to your project to see its value in this chart.

Enhance your data report with a sum total of your existing numeric custom fields in a particular project. Whatever your individual custom fields are, they will populate the chart to create a roll-up summary. 

We recommend using this chart when comparing estimates to actuals, such as budget to actual costs, or if you want to quickly sum up the hours your team has spent on the project.

> If you have numeric custom fields, we will automatically pull those onto the dashboard.

## Lollipop chart

Example: Task count by assignee.

You can:

- Understand how work is distributed across your team. At a quick glance, you can gauge who is performing and who might be overloaded.

- Click the **Pencil** icon to customize your chart.

> If you hover over the assignee lollipop, you can see how many tasks they have upcoming.

## Editing a chart

#### When editing a chart, you can:

- Choose the chart style.
- Decide if you want to show or hide data labels on your chart by toggling on or off.
- Decide how to group your chart data (x-axis). For example, by assignee.
- Choose how to measure your data ( y-axis). For example, time to complete. Donut charts cannot use average as their measure since the numbers need to be parts of a whole.
- Layer filters on a single chart or numeric roll-up.

### How to edit your chart

To edit your chart, click on the **Pencil** icon next to the selected chart.

From the next window, you can customize your chart to your specifications. Once you’ve finished making your edits, click **Save**.

## Reordering your charts

You can reorder the layout of your charts by dragging and dropping them.

## Expand your chart view

Click the expand icon to display more data and view your chart in a larger format.

You can also click the three dot icon and choose to resize your chart to a half or full size view.

## Chart actions

You can export each one of the charts to an image (png) individually. You cannot export the whole dashboard as one.

In addition to exporting charts as images, you can copy charts directly to your clipboard. This allows you to quickly paste charts into external documents such as PowerPoint presentations or Google Docs, streamlining the process of sharing insights outside of Asana.

If you want to add charts to your status update, download the chart and simply add it as an attachment in the status builder. You can then drag it into an email, a Slack message, or a presentation slide to report on team progress.

#### Click the three dot icon to:

- Resize your charts to half or full size
- Duplicate your chart
- Copy your chart and paste them into other surfaces. For example, slides.
- Download image
- Remove chart

## How to customize your chart by color

Color customizing charts and graphs can help you instantly identify and differentiate any potential road blockers for your team at a glance. Applying a unique color to different charts helps to visually represent **tasks by completion** status or **tasks by section** custom fields. Custom colors can be pulled in for both filtered and grouped charts.

#### How to edit your chart

- Click on the **Pencil** icon next to the selected chart.
- Select your desired color using the color picker and click **Save**

## Multi-metric charts

Multi-metric charts allow you to add multiple numeric and time metrics on the same chart to compare different performance measurements. Multi-metric charts enhance your reporting capabilities by allowing you to add up to four different metrics on a single chart. 

This functionality is available in line charts, bar charts, and lollipop charts used in Universal reporting, portfolio dashboards, and project dashboards.

How to add multiple metrics to a chart:

1.  Navigate to an existing **dashboard** or create a new one
2.  You can edit an existing **chart** within the dashboard or create a new one from scratch
3.  Remember to choose a **line** chart, **bar** chart, or **lollipop** chart
4.  Under **Chart data**, below the **Y-axis** value, click **+ Add metric**
5.  You may add up to four different metrics to one chart
6.  For time metrics, choose the **Unit of time** also.

Each metric will be displayed in a different color on the chart, making it easy to distinguish between them. You can hover over data points to see specific values for each metric.

Multi-metric charts are particularly useful for:

- Comparing estimated time versus actual time spent on tasks
- Monitoring budget metrics like **changed amount**, **estimated amount**, and **total amount**
- Tracking completion rates alongside time metrics to understand team efficiency
- Analyzing relationships between different performance indicators

## FAQ

### What's the difference between stacked and grouped bar charts?

Stacked bar charts combine groups into single stacked bars for each primary field value. Grouped bar charts display groups as separate adjacent bars for easier comparison.

### Are there any limits to the number of groupings in a grouped bar chart?

Yes, currently only four groups are shown.

[](https://forum.asana.com/c/forum-en/tips/6)
