---
fonte: https://support.google.com/docs/answer/9703214?hl=en
baixado: 2026-11-10
---

# Analyze & refresh BigQuery data in Google Sheets using Connected Sheets

You can use Gemini in Sheets, functions, charts, extracts, and pivot tables to analyze and refresh BigQuery data in Google Sheets.

**Important:** To access BigQuery data in Google Sheets, you need access to BigQuery. [Learn how to get started with BigQuery](https://support.google.com/docs/answer/9702507).

## Add a chart

1.  On your computer, open a spreadsheet in [Google Sheets](https://docs.google.com/spreadsheets/u/0/) that is connected to BigQuery data.
2.  At the top, click **Chart**.
3.  Choose where to place it.
4.  Click **Create**.
5.  At the right, choose your other settings.
6.  At the bottom right, click **Apply**.

[Learn more about charts in Google Sheets](https://support.google.com/docs/answer/63824?hl=en&ref_topic=9055207).

**Tip:** To update the chart based on the latest BigQuery data, at the bottom of the chart, click **Refresh**.

 

To group numeric values in charts into a histogram, under X-axis, you can check **Aggregate** and click **Edit**.

- In the "Grouping rule" pop-up, specify any of Minimum value, Maximum value, or Interval size, then click OK to apply those parameters for data aggregation.

#### Add a pivot table

1.  On your computer, open a spreadsheet in [Google Sheets](https://docs.google.com/spreadsheets/u/0/) that is connected to BigQuery data.
2.  At the top, click **Pivot table**.
3.  Choose where to place it.
4.  Click **Create**.
5.  At the right, choose your settings.
6.  At the bottom right, click **Apply**.

**Tips:**

- Pivot tables can currently support up to 200,000 rows.
- To limit the amount of data you see in your pivot table, specify the number of rows or columns to return. Update "sort by" and "order" to specify which rows or columns are returned.
- To add calculated fields with a SUM or custom formula, in the side panel, next to "Values," click **Add** and then **Calculated field**. [Learn how to add Calculated fields in pivot tables](https://support.google.com/docs/answer/1272900#calculated_fields).
- To update to the latest BigQuery data, at the bottom of the pivot table, click **Refresh**.
- To view values at intervals within a range, use histogram grouping. Values that are higher than the maximum and lower than the minimum are grouped together.
- You can double-click on a cell in pivot table to open a new tab with extract editor.

#### Use a function

You can use some functions with BigQuery data.

1.  On your computer, open a spreadsheet in [Google Sheets](https://docs.google.com/spreadsheets/u/0/) that is connected to BigQuery data.
2.  At the top, click **Function**.
3.  Choose a function from the list.
4.  Select where to place the function.
5.  Click **Create**.
6.  Choose your reference column and add any other required parameters.
7.  Press **Enter**.
8.  Put your mouse over a cell that contains the formula, and click **Apply changes**.

**Tip:** You can also type functions inside any cell. 

#### Pull data into an extract

You can analyze data offline, or reference individual values and ranges within functions. You can pull up to 500k rows or 10MB of your BigQuery data. If you try to pull more than this limit, only the first 500k rows will appear.

If the number of rows are:

- Less than or equal to 50k, then there’s no cell limit.
- Greater than 50k but less than or equal to 500k, then the number of cells must be less than or equal to 5m.
- Greater than 500k, then the data pull isn’t supported.

1.  On your computer, open a spreadsheet in [Google Sheets](https://docs.google.com/spreadsheets/u/0/) that is connected to BigQuery data.
2.  Select an option:
    1.  At the top, click **Extract**.
3.  Choose where to put it.
4.  Click **Create**.
5.  At the right, under "Extract editor," add columns, filters, and sort settings.
6.  At the bottom left of the extract, click **Apply changes**.

#### Add a calculation to all rows in a data set and view column stats

You can apply a calculation to all rows by adding a calculated column.

1.  On your computer, open a spreadsheet in [Google Sheets](https://docs.google.com/spreadsheets/u/0/) that is connected to BigQuery data.
2.  At the top, click **Calculated column**.
3.  Enter a formula using column names and supported Sheets functions. You can use basic math operations like *=price \* quantity* or manipulate text with *=RIGHT(orderId, 4)*. 
4.  Click **Add**.
5.  On the bottom left of the Sheet, click **Apply.**

**Tip:** To view column stats, at the top right of a column, click Down arrow Down arrow   and then  **View Column Stats**.

#### Supported functions

**Logic Functions**

- IF (can be used to detect potential errors, such as division by zero)
- AND
- OR
- NOT

**Lookup Functions**

- ROWS 
- VLOOKUP: [Learn how to use VLOOKUP in Connected Sheets](https://support.google.com/docs/answer/3093318).
- XLOOKUP: [Learn how to use XLOOKUP in Connected Sheets](https://support.google.com/docs/answer/12405947).

**Filter Functions**

- FILTER

**Text Functions**

- LEFT, RIGHT, MID
- UPPER, LOWER
- LEN
- CONCAT (&)

**Basic Math**

- +, -, \*, /
- The negative sign (-) and the percent sign (%)

**Math Functions**

- ROUND
- POW/POWER (^)
- SQRT
- ABS
- LOG, LN, LOG10

**Dates and Times**

- DATE, TIME
- YEAR, MONTH, DAY
- HOUR, MINUTE, SECOND

**Comparison**

- =, \<\>
- \>, \>=, \<, \<=

**Aggregations**

- SUM
- SUMIF
- SUMIFS
- COUNT
- COUNTBLANK
- COUNTIF
- COUNTIFS
- COUNTUNIQUE
- COUNTUNIQUEIFS
- MIN
- MINIFS
- MAX
- MAXIFS
- AVERAGE
- AVERAGEIF
- AVERAGEIFS
- VAR
- VARP
- STDEV
- STDEVP

**Other**

- ISBLANK (returns whether or not the given argument is NULL)

#### Analyze data with Gemini in Connected Sheets

You can use Gemini in Sheets to ask questions, analyze and explore data trends, and build live, connected charts, pivot tables, formulas and more across your full BigQuery dataset. [Learn more about Gemini in Sheets](https://support.google.com/docs/answer/14356410).

**Important:**

- This feature requires an eligible Google Workspace or Google AI plan. [Learn about Gemini features and plans](https://support.google.com/docs/answer/13952129).
- To run queries with Gemini, you need standard BigQuery permissions (BigQuery Job User and BigQuery Data Viewer) Collaborators who have view access to the spreadsheet without BigQuery permissions can still view saved results, charts, and dashboards in the sheet. [Learn more about BigQuery permissions](https://support.google.com/a/answer/9604541).
- Gemini runs read-only queries on your connected BigQuery data source and doesn't modify or delete data in BigQuery.

### **Get started with Gemini on BigQuery data**

1.  Open [Google Sheets](https://docs.google.com/spreadsheets).
2.  Open a spreadsheet connected to BigQuery data.
    1.  [Learn how to open a BigQuery project in Google Sheets](https://support.google.com/docs/answer/9702507#addproject).
3.  At the top right, click **Ask Gemini** .
4.  In the side panel, select a prompt or create your own. Examples of prompts:
    1.  "Compare our top 5 marketing campaigns month over month."
    2.  "Make a bar chart of clicks by campaign."
    3.  "Build an executive dashboard tab with revenue by region, a monthly trend chart, and an extract of urgent tickets."
    4.  "Check current stock levels in BigQuery for the Product IDs listed in Column A."
5.  Press **Enter**.
    1.  **Note:** If you’re using this feature for the first time, you may need to follow steps in the side panel to authenticate your account.
6.  **Optional:** You can ask follow-up questions to explore further, or ask Gemini to create or update items in your spreadsheet.
7.  When you’re done prompting, review the plan card in the side panel and click **Apply**.

**Tip:** Charts, pivot tables, formulas, and extracts created by Gemini stay connected to BigQuery. You can update them anytime manually or with a scheduled refresh. [Learn more about refreshing your BigQuery data](https://support.google.com/docs/answer/9703214#refresh).

## Refresh your data

BigQuery data doesn't automatically sync with Connected Sheets. To sync the data, you can refresh a specific item, everything within a data source, or everything within all data sources. Once you’ve connected to a data source, you can refresh that data and all of the objects like Charts, Functions, Extracts, and Pivot Tables associated with that data. 

1.  On your computer, open a spreadsheet in [Google Sheets](https://docs.google.com/spreadsheets/u/0/) that is connected to BigQuery data.
2.  At the bottom, next to "Refresh" click More More   and then  **Refresh options**.
3.  To the right, under "Refresh options," click the items you want to refresh. To refresh all of the data, at the bottom right, click **Refresh all**.

#### Schedule a refresh

**Important: **Scheduled refreshes of Connected Sheets don't propagate any end-user context such as IP address or device information. Virtual Private Cloud Service Controls (VPC-SC) perimeters that use end-user context to restrict access will cause scheduled refreshes to fail.

A scheduled refresh will update all objects and data sources at a specific, preset time.
**Important:**

- A scheduled refresh will run as the user that set up the schedule. If another user adds or updates an existing datasource, the schedule will automatically pause. To unpause, contact the schedule owner or [take over the refresh](#takeover).
- Objects in the preview or failed state will not refresh with a scheduled refresh. 

1.  On your computer, open a spreadsheet in [Google Sheets](https://docs.google.com/spreadsheets/u/0/) that is connected to BigQuery data.
2.  At the bottom, next to "Refresh" click More More   and then **Refresh options**.
3.  At the bottom of the sidebar to the right, under “Scheduled refresh,” click **Setup now**.
4.  Choose your refresh frequency.
5.  Click **Save**.

#### Take over a scheduled refresh

To run a scheduled refresh as yourself instead of the original owner, you can take over a refresh. 

1.  On your computer, open a spreadsheet in [Google Sheets](https://docs.google.com/spreadsheets/u/0/) that is connected to BigQuery data.
2.  At the bottom, next to "Refresh" click More More   and then  **Refresh options**.
3.  At the bottom of the sidebar to the right, under “Scheduled refresh,” click **Edit**.
4.  Choose your refresh frequency. 
5.  Click **Save** to transfer the scheduled refresh ownership to you.
     

#### View query details and cancel a query

Editors of a spreadsheet and users with the [*required BigQuery permissions*](https://cloud.google.com/bigquery/docs/managing-jobs#required_permissions_3) can cancel a query that is running. 

**To view query details for any database objects:**

1.  On your computer, open a spreadsheet in Google Sheets that is connected to BigQuery data.
2.  At the bottom pop-up Refresh button, click info The info icon. to see query details in BigQuery.
    - **Note:** The info icon. won’t show up if the data can be obtained without running a query. [*Learn more about exploring table data without running a query*](https://cloud.google.com/bigquery/docs/best-practices-costs#preview-data).
    - When you refresh, similar formulas may be combined into one query that computes results for all combined formulas.

**To cancel a query for any database objects:**

1.  On your computer, open a spreadsheet in Google Sheets that is connected to BigQuery data.
2.  When a query is running or pending: At the bottom pop-up Refresh button, next to “Running query” or “Query pending”, click **Cancel** next to the calculated running time.
3.  Click **Confirm**.

You can also cancel a query from Refresh options sidebar:

1.  On your computer, open a spreadsheet in Google Sheets that is connected to BigQuery data.
2.  At the bottom, hover over the refresh icon Refresh , next to "Refresh" click More More and then **Refresh options**.
3.  To cancel running refresh individually, next to each item, click **Cancel.**
4.  Click **Confirm**.

**Note:**

- If you do not have the [*required BigQuery permission*](https://cloud.google.com/bigquery/docs/managing-jobs#required_permissions_3) for a BigQuery dataset, the action to cancel a query cannot be completed.
- A query that failed due to a Sheets timeout may keep running in the database.
- If you cancel a query that has multiple formulas, all of the other formulas in the query are also canceled.

[Next: Write & edit a query with BigQuery data in Sheets](https://support.google.com/docs/answer/9703000)

## Related articles

- [Collaborate with Gemini in Google Sheets](https://support.google.com/docs/answer/14356410)
- [Get started with BigQuery data in Sheets](https://support.google.com/docs/answer/9702507)
- [Sort & filter your BigQuery data in Sheets](https://support.google.com/docs/answer/9702999)
- [Write & edit a query with BigQuery data in Sheets](https://support.google.com/docs/answer/9703000)
- [Fix problems with BigQuery data in Sheets](https://support.google.com/docs/answer/9703001)
