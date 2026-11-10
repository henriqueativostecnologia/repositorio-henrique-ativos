---
fonte: https://help.asana.com/s/article/google-sheets-asana?language=en_US
baixado: 2026-11-10
---

# Google Sheets & Asana

**Available on Asana [*Advanced*](https://asana.com/plan/advanced), [*Enterprise*](https://asana.com/enterprise), and [*Enterprise+*](https://asana.com/enterprise) tiers, as well as [*legacy tiers*](https://asana.com/pricing-legacy) Business and Legacy Enterprise.**

**Visit our [*pricing page*](https://asana.com/pricing) for more information.**

With reporting in Google Sheets, you can use project data to create custom reports and visualizations to see what’s on track and what needs attention. Google sheet exports are available for [portfolios](https://help.asana.com/s/article/portfolios-overview?language=en_US), [projects](https://help.asana.com/s/article/understanding-projects?language=en_US) and [advanced search](https://help.asana.com/s/article/search-and-search-views?language=en_US) results. This article will help you get started and provide inspiration for creating reports.

## Using Google Sheet reporting

Before opening a Google Sheet from your [portfolio](https://asana.com/guide/help/premium/portfolios "Portfolio"), ensure you have added the appropriate projects. We recommend consulting Google’s [Help Center](https://support.google.com/docs?docs_site_home#topic=2811806 "Help Center") and [Google Sheets](https://productforums.google.com/forum/#!topicsearchin/docs/category$3Aspreadsheets%7Csort:relevance%7Cspell:false "Google Sheets") Help Forum if you are new to Google sheets.

#### Getting started

1.  Install the **Asana Exports** add on in Google Drive using [this link](https://workspace.google.com/marketplace/app/asana_exports/766596199153).
2.  Copy your Asana export link to sync with Google Sheets.
    - In Asana, click **Export/Print** from the drop down menu next to your project/portfolio header and select **Sync to Google Sheets**. Your Google Sheet will open in a new tab.

    - Copy the URL provided in the modal that follows.

3. Sync your Asana data to a new sheet

- Create a new, blank Google sheet
- Navigate to the **Extensions **tab \> **Asana Exports **\> **Sync with Asana**
- Paste the URL from step 2 into the input box and click **Ok**. Your sheet will be synced with your Asana data.

> The current limit for syncing and exporting data is 500 rows.

## Portfolio reporting

First time users will need to authorize Asana to connect with their Google account.

> The data in your Google Sheet will automatically update every 6 hours.

The Google Sheet report includes three tabs:

1.  **Overview**— a reference on how to use the Sheet with two example charts created from your data.
2.  **Asana project data**—shows the most important data from each project. Explore this data by sorting or filtering by the columns.
3.  **Live source data**—pulls live data directly from Asana. This tab is locked to protect the connection to Asana.

> Hover over column headers to learn more about the data in that column.

## Building custom reports

Sample reports to create in your Google Sheet:

1.  **Which projects are at risk and due soon?** A scatter chart of due date and status color.
2.  **Which project owners are pushing work forward quickly?** A bar chart of recent tasks completed, by project owner.
3.  **What portion of your projects are on track?** A pie chart of status colors.
4.  **Is work focused or spread across projects?** A histogram of tasks completed in the past week in each project.
5.  **Which teams have projects that are close to completion?** A stacked bar chart of projects at % completion, by team.

### Example: At risk projects that are due soon

This example shows how to build a report to find the individual projects that need your attention.

#### Create a new tab

- 1.  Click the **+** icon on the bottom left of your sheet to create a new tab.
  2.  Choose a name for your report.

#### Add columns to your report by referencing the **Live source data** tab

1.  Select the top left cell of your new blank tab and type `=`.
2.  Navigate to the **Live source data** tab. Click the header of the column you want to copy. In this example, we will reference the **Name** column.
3.  Press `Enter`. This will take you back to your report tab.

4.  Select the next cell to the right, and repeat steps 2 to 4 for the **Due Date** and **Status Color** columns.
5.  Once the header cell of each column has been referenced, the data itself can be copied across. Select all three headers, and use the autofill handle on the bottom right corner of your selection to drag down.

> We’ve referenced the data in the **Live source data** tab, rather than just copying it. That means when the data in the **Live source data** tab automatically updates every hour, your report will also automatically update.

#### Use a formula to calculate the time remaining until the deadline for each project

1.  Type `DAYS TILL DUE` as a header in the fourth column
2.  Enter the formula `=DATEDIF(NOW(), B2, "D")` underneath. This calculates the number of days between now and the value in the **Due Date** column.

3.  Drag the autofill handle to populate the rest of your new column.

#### Create a scatter chart

1.  Sort the report by **Status Color** by opening the **Data** menu and choosing **Filter**. Use the menu on the **Status Color** column header to **Sort A → Z**.

2.  Select the **Status Color**, **Days Till Due**, and **Name** columns, in that order, by holding `⌘` (on Mac) or `CTRL` (on PC) and clicking the letter above each column (C, D and A). These three columns are needed in the scatter chart, and the **Name** column must be chosen last as it will act as the label for each datapoint.

3.  Create a chart, by opening the **Insert** menu and choosing **Chart.**
4.  Choose a **Scatter chart** and uncheck **Aggregate column C**.

Use this chart to identify which projects are at risk. In the screenshot below “danger zone” projects are any projects that are red and due in less than 60 days. As the data is updated hourly, you can reference this chart frequently to understand where to focus team efforts.

### Example: Task completion rate by project owner

This example shows how to build a report where projects are grouped according to a property, in this case by project owner. Use this report to identify the number of tasks completed this week in projects driven by each project owner.

#### Create a pivot table to group the projects by owner

1.  Navigate to the **Live source data** tab.
2.  Select rows. Skip row 1 because a pivot table works best when the first row contains the headers.

3.  Open the **Data** menu and choose **Pivot table**. This will open a new tab titled Pivot table.
4.  From the Pivot table tab, in the **Report Editor** sidebar, under **Rows**, choose **Add field**. Select the column you wish to group your projects by, in this case **Owner**. Uncheck **Show totals**, this data is not needed in this example.

5.  Under **Values**, choose **Add field**. Select the column you’d like to understand for each group of projects—in this case, **Tasks Completed**.

6.  Check that the values for the group are summarized as needed. In this example, we want to see the total task completion rate for each group of projects, so we choose **Sum**.

#### Visualize the data

Use the **Explore** sidebar in Google Sheets, which generates relevant charts using artificial intelligence.

1.  Click **Explore** in the bottom right hand of the Sheet. In this example, a bar chart is a useful visualization of the task completion rate.
2.  To see a larger version of the chart, you can drag it into the main area of the sheet. Right click the chart to customize it.

Reports you create are saved automatically, and will appear the next time you open the sheet from Asana.

> Questions about Google Sheets integration? [Ask the Community](https://forum.asana.com/c/forum-en/integrations/9).

[](https://forum.asana.com/c/forum-en/tips/6)
