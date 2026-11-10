---
fonte: https://support.google.com/appsheet/answer/10105821?hl=en
baixado: 2026-11-10
---

# Tables: The Essentials

Explore and manage your tables as described in the following sections:

- [Explore the Data pane](#explore-data-pane)
- [Explore the Table pane](#explore-table-pane)
- [Add a table](#add)
- [About table suggestions](#add-multiple)
- [Configure table settings](#configure-table)
- [Preview data in a table](#preview-table)
- [Create a report for a table in Looker Studio](#create-report)
- [Delete a table](#delete-table)

See also: [About tables](https://support.google.com/appsheet/answer/13829970)

## Explore the Data pane

**Note**: **The Data pane is available in the new editor  only. **The Data pane does not appear in the legacy editor.

Go to **Data ** .

The Data pane is displayed and the first table in the primary navigation is opened in the editor.

Data secondary navigation

As highlighted in the previous figure, you can use the Data pane to:

- Edit columns in the table, as described in [View and edit columns](https://support.google.com/appsheet/answer/10106674#view-edit-column)
- [Add a table](#add)
- Add a table slice, as described in [Add a slice](https://support.google.com/appsheet/answer/10106592#add-slice)
- Manage a table, including:
  - View the data source (in a new tab)
  - Regenerate the table schema, as described in [Add, remove, or rearrange columns](https://support.google.com/appsheet/answer/10106675)
  - [Rename a table](#rename-table)
  - [Delete a table](#delete-table)
- Manage a table slice, including:
  - Preview data in a slice, as described in [View a sample of the data in a slice](https://support.google.com/appsheet/answer/10106592#view-data)
  - Rename a slice, as described in [Rename a slice](https://support.google.com/appsheet/answer/10106592#rename-slice-slice)
  - Duplicate slice, as described in [Copy a slice](https://support.google.com/appsheet/answer/10106592#copy-slice)
  - Delete a slice, as described in [Delete slice](https://support.google.com/appsheet/answer/10106592#delete-slice)
- Configure user settings, as described in [User settings: The Essentials ](https://support.google.com/appsheet/answer/10106760)
- Search all data
- Expand or collapse all items in the navigation bar

## Explore the Table pane

Go to **Data **  and select a table in the list.

The Table pane is displayed, as shown:

Tables panel with callouts

As highlighted in the previous figure, you can use the Table pane to:

- Edit columns in the table, as described in [View and edit columns](https://support.google.com/appsheet/answer/10106674#view-edit-column)
- View the data source (in a new tab)
- [Configure the table settings](#configure-table)
- Regenerate the table schema, as described in [Add, remove, or rearrange columns](https://support.google.com/appsheet/answer/10106675)
- Add a virtual column to the table, as described in [Use virtual columns](https://support.google.com/appsheet/answer/10106758)
- Manage the table, including:
  - [Preview the data in a table](#preview-table)
  - [Create a report for a table in Looker Studio](#create-report)
  - [Delete the table](#delete-table)
  - Show the standard or expanded view of the Data pane
    Select **Show expanded view** to more easily view and edit your expressions in the Data pane, as shown:

    Expanded view in Data pane
- Expand or scroll the table to display more settings

We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

## If you are using the legacy editor

In the title bar, you can click:

- **View Columns** to view the table columns (open the **Data \> Columns** tab)
- **View Source** to open your spreadsheet in another tab.
- **View Data** to open data in the table in another tab - not the original source, but the same information
- **Delete** to remove the table from the editor

##  Add a table

To add a table:

1.  Open the app in the editor.
2.  Go to **Data **.
    The [Data pane](https://support.google.com/appsheet/answer/10106580#explore-data-panel) opens.
3.  Click **+** in the top header of the Data pane.
    We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

    ## If you are using the legacy navigation

    Go to **Data \> Tables **and click **+ New Table**.  
4.  When prompted, choose your data source.
5.  Navigate to and select the data to be added.
    If you select a Google Sheet, you can select multiple worksheets to be added as tables in your app.
6.  Choose how data is accessed in the app.
    You can allow people to Add, Update, and Delete rows, or any combination of the three.
7.  Click **Add to app**.

The tables are added to the app. See [Explore the Table pane](#explore-table-pane).

## About table suggestions

When you [add a table](#add), if you're already using a table source that has multiple worksheets or tabs, AppSheet will suggest unused worksheets from which to create a table and additional suggestions in the dialog.

When adding a suggested table, you select a different table source in the drop-down menu, then choose an unused worksheet to create a new table. If you want to add an entirely new table source--a new spreadsheet, for example--just select **Browse for new source** from the table source drop-down menu. AppSheet will ask you to select a new file; if you have multiple data sources, it will prompt you to select a new data source. You may select the same spreadsheet, or a different one from a different data source.

## Configure table settings

To configure a table:

1.  Open the app in the app editor.

2.  Go to **Data **, select the table you want to configure in the list, and click **Table settings**  Table settings icon  in the table header.
    We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

    ## If you are using the legacy editor

    Go to **Data \> Tables** and expand the table that you want to configure.

3.  Configure the table settings.

    +-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Table name                                                                    | Name of the table.                                                            |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Are updates allowed?                                                          | Control whether app users can add, delete, or edit rows in a table. You can   |
|                                                                               | specify combinations of these options for each table. See [Control, add,      |
|                                                                               | update, and delete                                                            |
|                                                                               | operations](https://support.google.com/appsheet/answer/10106345).             |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Source path                                                                   | Path to the data source for the table.                                        |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Worksheet Name/Qualifier                                                      | Additional qualifier that is used to identify the data source for the table,  |
|                                                                               | such as. the name of the worksheet in a spreadsheet.                          |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Data source                                                                   | Name of the data source for the table.                                        |
|                                                                               |                                                                               |
|                                                                               | Optionally, you can copy the data to another data source:                     |
|                                                                               |                                                                               |
|                                                                               | 1.  Click **Copy Data to New Source**.                                        |
|                                                                               | 2.  Select the data source from the **Save data to** drop-down.               |
|                                                                               | 3.  To include file data, such as images, turn on **Include file data**.      |
|                                                                               | 4.  Click **Copy data**.                                                      |
|                                                                               |                                                                               |
|                                                                               | The data is copied to the new data source. A confirmation dialog is displayed |
|                                                                               | that provides the source path.                                                |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Source Id                                                                     | Provider-specific path to the table data. This information is not visible to  |
|                                                                               | the app user.                                                                 |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Store for image and file capture                                              | Storage location where images and files that are captured by the app are      |
|                                                                               | stored. See [Image storage in the                                             |
|                                                                               | cloud]                                                                        |
|                                                                               | (https://support.google.com/appsheet/answer/10106529#image-storage-in-cloud). |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Filter out all existing rows?                                                 | Turn on to capture new data (that is, allow adds) in forms but do not show    |
|                                                                               | any existing data.                                                            |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Security filter                                                               | Define a security filter condition to restrict the rows that are displayed in |
|                                                                               | the table. For example, to display only items assigned to the current         |
|                                                                               | user: `[AssignedTo]=USEREMAIL()`                                              |
|                                                                               |                                                                               |
|                                                                               | While security filters are primarily meant to be a security feature, they can |
|                                                                               | also be used as a scalability feature, as described in [Scale using security  |
|                                                                               | filters](https://support.google.com/appsheet/answer/10104706)                 |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Access mode                                                                   | Select the credentials to use when accessing the spreadsheet. Valid values    |
|                                                                               | are **as app creator** or **as app user**. See [Set access mode as app        |
|                                                                               | creator or app user](https://support.google.com/appsheet/answer/10105756).    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Shared?                                                                       | Turn on to share the table with all app users. Before turning off this        |
|                                                                               | setting, see [Private                                                         |
|                                                                               | tables](https://support.google.com/appsheet/answer/10106508).                 |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Partitioned across many files/sources?                                        | Partition (or divide) the rows of the table into multiple table sources. See  |
|                                                                               | [Scale using data                                                             |
|                                                                               | partitions](https://support.google.com/appsheet/answer/10105383).             |
|                                                                               |                                                                               |
|                                                                               | **Note**: All partitions must belong to the same data source at this time.    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Partitioned across many worksheets?                                           | Partition (or divide) the rows of the table across multiple worksheets. See   |
|                                                                               | [Scale using data                                                             |
|                                                                               | partitions](https://support.google.com/appsheet/answer/10105383).             |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Data locale                                                                   | Locale used to read the table. For guidance on setting this value,            |
|                                                                               | see [Locale support in                                                        |
|                                                                               | AppSheet](https://support.google.com/appsheet/answer/10106525).               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Descriptive comments                                                          | Description of the table.                                                     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

     

4.  Save the app by selecting one of the following:
    - **Save** - Save the app.
    - **Save & verify data** - Save the app and verify that it is runnable based on external dependencies.

## Preview the data in a table

To preview the data in a table:

1.  Open the app in the app editor.
2.  Go to **Data ** .
3.  Select the table in the list that you want to preview.
4.  Select **More \> Preview data** in the table header.

A separate tab is opened with a preview of the data. Select the number of rows you'd like to show in the drop-down.

We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

## If you are using the legacy editor

To preview the data in a table:

1.  Open the app in the app editor.
2.  Go to **Data \> Tables**.
3.  Expand the table that you want to preview.
4.  Click **View Data **in the table header.

A separate tab is opened with a preview of the data. Select the number of rows you'd like to show in the drop-down.

##  Create a report for a table in Looker Studio

To create a report for a table in Looker Studio:

1.  Open the app in the app editor.
2.  Go to **Data ** .
3.  Select the table in the list that you want to preview.
4.  Select **More \> Create report ** in the table header.

Looker Studio is opened in a separate tab with the generated report. See also [Visualize your app data using Looker Studio](https://support.google.com/appsheet/answer/11911810).

## Rename a table

 To rename a table:

1.   Open the app in the app editor.
2.  Go to **Data ** .
3.  Position your cursor over the data in the Data panel and select **More ********************************************************\> Rename**.
    Alternatively, you can double-click on the name in the Data panel.
4.   Edit the name and press **Enter**.
5.  Save the app by selecting one of the following:
    - **Save** - Save the app.
    - **Save & verify data** - Save the app and verify that it is runnable based on external dependencies.

We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

## If you are using the legacy editor

 To rename data:

1.   Open the app in the app editor.
2.  Go to **Data**.
3.  Expand the data you want to rename.
4.  Edit the **Table name** field.
5.  Save the app by selecting one of the following:
    - **Save** - Save the app.
    - **Save & verify data** - Save the app and verify that it is runnable based on external dependencies.

## Delete a table

To delete a table:

1.  Open the app in the app editor.
2.  Go to **Data ** .
3.  Do one of the following:
    - Position your cursor over the data in the Data pane and select **More** **\> Delete**.
    - Select a table in the list and select **More** **\> Delete** in the table header.
4.  Save the app by selecting one of the following:
    - **Save** - Save the app.
    - **Save & verify data** - Save the app and verify that it is runnable based on external dependencies.

We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

## If you are using the legacy editor

To delete a table:

1.  Open the app in the app editor.
2.  Go to **Data \> Tables**.
3.  Expand the table that you want to delete.
4.  Click **Delete **in the table header.
5.  Save the app by selecting one of the following:
    - **Save** - Save the app.
    - **Save & verify data** - Save the app and verify that it is runnable based on external dependencies.
