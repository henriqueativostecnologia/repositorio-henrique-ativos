---
fonte: https://support.google.com/docs/answer/12822123?hl=en
baixado: 2026-11-10
---

# Get started with Connected Sheets for Looker

**Requirements:** To use Connected Sheets for Looker, you must know the URL of the Looker instance you want to connect to. You can find out what Looker instances are eligible and how to enable Connected Sheets in Looker here: [Using Connected Sheets for Looker](https://cloud.google.com/looker/docs/connected-sheets).

In Sheets, connect to your Looker-modeled data to analyze data from a single source of truth and even integrate other data sources for deeper analysis.

With Connected Sheets for Looker, you can analyze data from more than 60 databases that can be live-connected to Looker. You can also combine your Looker data with Sheets data and you can analyze your data using familiar Sheets features like pivot tables.

[Learn more about Looker](https://www.looker.com).

## Connect to a Look or an Explore

1.  On your computer, open a [spreadsheet in Google Sheets](https://docs.google.com/spreadsheets/u/0/).
2.  At the top, click **Data** and then **Data connectors** and then **Connect to Looker**.
3.  Enter your Looker instance URL or instance ID.
    - To access Looker, you must have a Looker instance. If you don’t have a Looker instance, contact the Looker sales team to [request a demo](https://www.looker.com/).
    - If you’re prompted to allow access to your Looker data, you'll be asked to link your account, if you agree, click **Agree and continue** to link your Google and Looker accounts and allow Google to access your Looker data on your behalf.
4.  Click **Connect to Look** or **Connect to Explore**.
    - **If you select** ”**Connect to Look:**”
      1.  Select a Look.
      2.  Click **Connect**.
      3.  In the “Connect to a Look” window, under “Insert to,” select **New sheet** or **Existing sheet**.
      4.  Click **Create**.
      5.  On the left of the spreadsheet, click **Apply**.
          - In the “Look editor” side panel, you’ll find the Look title and Look URL.
      6.  To refresh the data in the table:
          - At the bottom right, in the “Look editor“ side panel, click **Refresh**.
          - At the bottom left of the table, click **Refresh**.
    - **If you select** ”**Connect to Explore:**”
      1.  Select a model from the list.
      2.  Click **Connect**.

## Learn how to use Connected Sheets for Looker

After you load the Explore from the Looker instance, you can:

- Run live queries based on modeled data and standardized metrics
- Share and collaborate across the org with partners, analysts, or other stakeholders on up-to-date data
- Create new analysis in Google Sheets with built-in Google Sheets functions

## Learn more about Looker

To better understand Looker terminology, please take a look at the Looker documentation:

- [Learn more about “model.”](https://cloud.google.com/looker/docs/model-and-view-files#model_files)
- [Learn more about “Explore.”](https://cloud.google.com/looker/docs/exploring-data)
- [Learn more about “views.”](https://cloud.google.com/looker/docs/model-and-view-files#view_files)
- [Learn more about “measures.”](https://cloud.google.com/looker/docs/exploring-data#explores_are_the_starting_po)
- [Learn how to add dimensions for more details](https://cloud.google.com/looker/docs/exploring-data#adding_more_dimensions_for_more_detail).
- [Learn how to pivot dimensions](https://cloud.google.com/looker/docs/exploring-data#pivoting_dimensions).
- [Learn how to filter data](https://cloud.google.com/looker/docs/filtering-and-limiting#filtering_data).
- [Learn how to save and edit Looks](https://cloud.google.com/looker/docs/saving-and-editing-looks).

## Create a pivot table

At the top left of the spreadsheet that is connected to Looker data, you can easily create a pivot table to analyze large data sets and find relationships between data points.

[Learn how to create and use pivot tables](https://support.google.com/docs/answer/1272900?hl=en&co=GENIE.Platform%3DDesktop#zippy=%2Cchange-or-remove-data%2Csee-cell-details).

1.  To make edits on the pivot table, click Edit .
2.  To add data from dimensions and measures, select an option:
    - Click **Add**.
    - From the right-hand side of the pivot table editor, you can drag and drop:
      - Dimensions as rows, columns, values or filters
      - Measures as values or filters
      - Filter-only fields and parameters as filters

&nbsp;

3.  To apply changes to the pivot table, click **Apply**.

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| In the screenshot:                                                                                                                                            |
|                                                                                                                                                               |
| Rows = Distribution Center - Name                                                                                                                             |
|                                                                                                                                                               |
| Columns = Inventory Items - Created Date                                                                                                                      |
|                                                                                                                                                               |
| Values = Orders - Order Count                                                                                                                                 |
|                                                                                                                                                               |
| Filters = Inventory Items - Created Date between 2023-12-01 and 2023-12-05                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Tips:**

- Looker Explores may contain one or more [always_filters](https://cloud.google.com/looker/docs/reference/param-explore-always-filter) and/or [conditionally_filters](https://cloud.google.com/looker/docs/reference/param-explore-conditionally-filter). These filters are defined in Looker and also apply to Connected Sheets for Looker pivot tables. As shown below, you can go to the "Looker filters" section of the Pivot table editor and see fields with defined filters.
- Pivot tables can currently support up to 100K results.

###

### Add a filter to a pivot table

1.  Click Edit to edit the pivot table.
2.  Under “Filters,” click **Add**.

- You can add Looker [filter-only fields](https://cloud.google.com/looker/docs/reference/param-field-filter) and [parameters](https://cloud.google.com/looker/docs/reference/param-field-parameter) as filters in pivot tables. Learn more about [Using Looker parameters and filter-only fields](https://cloud.google.com/looker/docs/connected-sheets#using_looker_parameters_and_filter-only_fields_added_october_2023).

#### Add a filter by value

You can [filter dimensions or measures by values](https://cloud.google.com/looker/docs/connected-sheets#filter_by_value_added_august_2023).

1.  Select a dimension or measure.
2.  Next to “Showing all items," click the Down arrow Down arrow .
3.  Under “Filter by value,” click **Add filter**.

**Tip:** Looker fetches the top 500 values, which may take a few seconds.

6.  Select values to filter.
7.  Click **OK**.
8.  At the bottom left of the sheet, click **Apply**.

**Tip:** To remove current filters, in the right side panel, under “Filters,” click **Remove** .

## Add a filter expression

You can use [*filter expressions*](https://cloud.google.com/looker/docs/connected-sheets#filters_using_looker_filter_expressions_added_september_2023) to filter with common expressions such as "last day,” "next week,” or "NOT 5”.

1.  Select a dimension or measure.
2.  Under “Filter by condition,” select **“Filter expression.”**
3.  Input your expressions.
4.  Click **OK**.
5.  At the bottom left of the sheet, click **Apply**.

## Refresh your data

Looker data doesn't automatically sync with Connected Sheets. To sync the data, you can refresh a specific item, everything within a data source, or everything within all data sources. Once you’ve connected to a data source, you can refresh Pivot Tables associated with that data.

1.  On your computer, open a spreadsheet in [Google Sheets](https://docs.google.com/spreadsheets/u/0/) that is connected to Looker data.
2.  At the bottom, next to "Refresh" click More More icon and then **Refresh options**.
3.  To the right, under "Refresh options," click the items you want to refresh. To refresh all of the data, at the bottom right, click **Refresh all**.

## Schedule a refresh

**Important:** Scheduled refreshes of Connected Sheets don't propagate any end-user context such as IP address or device information.

A scheduled refresh will update all objects and data sources at a specific, preset time.
**Important:**

A scheduled refresh will run as the user that set up the schedule. If another user adds or updates an existing datasource, the schedule will automatically pause. To unpause, contact the schedule owner or [take over the refresh](#TakeOveraSR).

Objects in the preview or failed state will not refresh with a scheduled refresh.

1.  On your computer, open a spreadsheet in [Google Sheets](https://docs.google.com/spreadsheets/u/0/) that is connected to Looker data.
2.  At the bottom, next to "Refresh" click More More icon and then **Refresh options**.
3.  At the bottom of the sidebar to the right, under “Scheduled refresh,” click Setup now.
4.  Choose your refresh frequency.
5.  Click Save.

#### Take over a scheduled refresh

To run a scheduled refresh as yourself instead of the original owner, you can take over a refresh.

1.  On your computer, open a spreadsheet in [Google Sheets](https://docs.google.com/spreadsheets/u/0/) that is connected to Looker data.
2.  At the bottom, next to "Refresh" click More More icon and then **Refresh options**.
3.  At the bottom of the sidebar to the right, under “Scheduled refresh,” click Edit.
4.  Choose your refresh frequency.
5.  Click Save to transfer the scheduled refresh ownership to you.

## View query details and cancel a query

Editors of a spreadsheet and users with the [*required Looker permissions*](https://cloud.google.com/looker/docs/admin-panel-database-queries#query_killing) can cancel a query that is running.

**To view query details for a pivot table:**

1.  On your computer, open a spreadsheet in Google Sheets that is connected to Looker data.

2.  Create a pivot table.

3.  At the bottom left of the pivot table, click **Apply** to apply any changes.

4.  At the bottom left of the pivot table, hover over the refresh icon Refresh , next to "Refresh", click **Open in Looker** to open the pivot table query in Looker

5.  \[Optional\] Click More More icon

    1.  And click **See your recent Looker queries** to see a list of recently run queries in Looker
    2.  And click **See query in Looker System Activity** to see the details of this execution of the query in System Activity.
        1.  **Note:** You will need Looker's see_system_activity permission to see the data

**To cancel a query**

1.  On your computer, open a spreadsheet in Google Sheets that is connected to Looker data.
2.  When a query is running or pending: At the bottom, next to “Running query” or “Query pending”, click **Cancel** next to the calculated running time.
3.  Click **Confirm**.

You can also cancel a query from Refresh options sidebar:

1.  On your computer, open a spreadsheet in Google Sheets that is connected to Looker data.

2.  At the bottom, hover over the refresh icon Refresh , next to "Refresh" click More More icon and then **Refresh options**.

3.  To cancel running refresh individually, next to each item, click **Cancel**.

4.  Click **Confirm**.

Note:

- If you do not have the required Looker permission, the action to cancel a query cannot be completed.
- A query that failed due to a Sheets timeout may keep running in the database.

## Explore connection settings

If you are currently connected to an Explore and you want to update the connection, you can use Connection settings.

1.  At the top right, click **Connection settings**.
2.  To connect, click a new Explore.
3.  Click **Connect**.

## Admin Audit Logs

**Important:** When you access Looker data in Connected Sheets, entries are recorded in Looker's Audit Logs. The logs show who accessed the data and when. Only people with proper authorization can access log records.

You can find the [spreadsheet ID in the audit log](https://support.google.com/a/answer/9604541). Every spreadsheet has a unique spreadsheet ID value containing letters, numbers, hyphens, or underscores. You can also find the spreadsheet ID in a Google Sheets URL.

[Learn more about Monitoring Connected Sheets](https://cloud.google.com/looker/docs/connected-sheets#monitoring_connected_sheets).
