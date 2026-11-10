---
fonte: https://support.google.com/appsheet/answer/12726685?hl=en
baixado: 2026-11-10
---

# Configure and save the view configuration

View configurations provide you and other database collaborators the flexibility to visualize and work with the data in the way that you prefer. You can configure and save the view configurations with your table [layout](#configure-table-layout), [group](#group-data-by-column), [filter](#filter-data-by-column), [sort](#sort-data-by-column), and [row density](#change-row-density) selections, and then switch between different view configurations to optimize your view of the data.

View configuration tools

Changes to a view configuration are not saved automatically. You must [save the view configuration](#save-changes-view-configuration) to persist your changes and make them available to other collaborators.

 

Configure and save the view configuration for a table in the database editor as described in the following sections:

- [Configure the layout](#configure-table-layout)
- [Group data by column](#group-data-by-column)
- [Filter data](#filter-data-by-column)
- [Sort data by column](#sort-data-by-column)
- [Change the row density](#change-row-density)
- [Manage the view configuration](#manage-view-configuration)

**Note**: The view configuration features described in this section have no impact on the table when viewed in the app editor or used in an app. They are available only when editing the app in the database editor.

## Configure the layout

A *layout* allows you to change the visual format in which the data is displayed in a view. A table can have one or more custom views, and each view has a configurable layout, which determines how the table rows are shown, and how you can interact with it (for example: in a spreadsheet-like grid, or a kanban board, or a map).Configure one of the following table layouts:

|                                     |                                                                                                                 |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| **Layout**                          | **Description**                                                                                                 |
| [Grid layout](#grid-layout)         | Shows table rows in a standard grid with rows and column, similar to a spreadsheet. This is the default layout. |
| [Kanban layout](#kanban-layout)     | Groups table rows into columns that represent workflow stages.                                                  |
| [Calendar layout](#calendar-layout) | Shows table rows in a calendar.                                                                                 |
| [Queue layout](#queue-layout)       | Lists table rows in a queue with details on the side.                                                           |
| [Map layout](#map-layout)           | Shows table rows on a map based on a location column.                                                           |

**Note**: Layouts that are not relevant to the column data types in a table are greyed out.

#### Configure the grid layout

The grid layout shows table rows in a standard grid with rows and columns, similar to a spreadsheet. 

Grid layout example

To configure the grid layout:

1.  [Open the database in the database editor](https://support.google.com/appsheet/answer/12632559).

2.  Select the table tab.

3.  Select **Grid Layout** in the layout drop-down in the toolbar.

4.   Click **Config** to configure the following grid layout settings or click **reset to default** to reset settings to their defaults:

    +-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Column visibility                                                             | Select the columns to display or hide in the table. All columns are displayed |
|                                                                               | by default.                                                                   |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Summary rows                                                                  | Select the columns for which you want summary information displayed below the |
|                                                                               | column header.                                                                |
|                                                                               |                                                                               |
|                                                                               | Summary rows allow you to show a summary of the data in your table columns    |
|                                                                               | using a number of summarization/aggregation functions, depending on the       |
|                                                                               | column type.                                                                  |
|                                                                               |                                                                               |
|                                                                               | For example:\                                                                 |
|                                                                               | Summary of data in your columns                                               |
|                                                                               |                                                                               |
|                                                                               | Some example use cases for summary rows include:                              |
|                                                                               |                                                                               |
|                                                                               | -   Count the number of rows assigned for each "Assignee" so you can balance  |
|                                                                               |     the workload.                                                             |
|                                                                               | -   Count the % of rows that have "Review notes" filled in so you know which  |
|                                                                               |     items still need review.                                                  |
|                                                                               | -   Show the latest date in a "Target Date" column so you know the latest     |
|                                                                               |     date for all tasks to be completed.                                       |
|                                                                               | -   Count the number of tasks by status while grouped by project so you know  |
|                                                                               |     the progress of the work per project.                                     |
|                                                                               |                                                                               |
|                                                                               | Depending on the type of summary, you can hover and select the summary cells  |
|                                                                               | to see additional context and details.                                        |
|                                                                               |                                                                               |
|                                                                               | -   For Count, Avg, Min, Max, and Sum, you can hover over or select the cell  |
|                                                                               |     to see the label for the type of summary.                                 |
|                                                                               | -   For Count by Value, you can select the cell to see a breakdown of unique  |
|                                                                               |     values, sorted by how frequently they occur.                              |
|                                                                               |                                                                               |
|                                                                               | You can also click directly into the summary row cell to select a new         |
|                                                                               | function for summarization.                                                   |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

5.  Click **OK**.

#### Configure the kanban layout

**Note**: The kanban layout requires a [drop-down column data type](https://support.google.com/appsheet/answer/10106435#enumerated) in your table. 

The kanban layout groups table rows into columns that represent workflow stages.

Kanban layout example

To configure the kanban layout:

1.  [Open the database in the database editor](https://support.google.com/appsheet/answer/12632559).

2.  Select the table tab.

3.  Select **Kanban Layout** in the layout drop-down in the toolbar.

4.  Click **Config** to configure the following kanban layout settings or click **reset to default** to reset settings to their defaults:

    |                   |                                                                                   |
|-------------------|-----------------------------------------------------------------------------------|
| **Setting**       | **Description**                                                                   |
| Column visibility | Select the columns to display in the table. All columns are displayed by default. |

5.  Click **OK**.

#### Configure a calendar layout

**Note**: The calendar layout requires a [Date column data type](https://support.google.com/appsheet/answer/101064350#temporal) in your table. 

The calendar layout shows table rows in a calendar.

Calendar layout example

To configure the calendar layout:

1.  [Open the database in the database editor](https://support.google.com/appsheet/answer/12632559).

2.  Select the table tab.

3.  Select **Calendar Layout** in the layout drop-down in the toolbar.

4.  Click **Config** to configure the following calendar layout settings or click **reset to default** to reset settings to their defaults:

    |              |                                                                    |
|--------------|--------------------------------------------------------------------|
| **Setting**  | **Description**                                                    |
| Date column  | Select the column to use for the date in the drop-down list.       |
| Title column | Select the column to use as the title label in the drop-down list. |

5.  Click **OK**.

#### Configure a queue layout

The queue layout shows a ticketing-queue view with each row expanded on the right side, where you can easily see who created or updated the row, and comment on rows.

Queue layout example

To configure the queue layout:

1.  [Open the database in the database editor](https://support.google.com/appsheet/answer/12632559).

2.  Select the table tab.

3.  Select **Queue Layout** in the layout drop-down in the toolbar.

4.  Click **Config** to configure the following queue layout settings or click **reset to default** to reset settings to their defaults:

    |                   |                                                                                   |
|-------------------|-----------------------------------------------------------------------------------|
| **Setting**       | **Description**                                                                   |
| Column visibility | Select the columns to display in the table. All columns are displayed by default. |

5.  Click **OK**.

#### Configure a map layout

**Note**: The map layout is available only if there are [mappable data types](https://support.google.com/appsheet/answer/10106435) in the table.

The map layout shows locations as pins on a Google Maps map, you can [group](#group-data-by-column) on a dropdown-type column to group and color the pins.

To configure the map layout:

1.  [Open the database in the database editor](https://support.google.com/appsheet/answer/12632559).
2.  Select the table tab.
3.  Select **Map Layout** in the layout drop-down in the toolbar.

## Group data by column

Visually group together data. 

When you group data by a column, AppSheet shows a header row for each group. For a drop-down column, AppSheet shows show a header row for each option.

For example, the following shows a grid layout that is grouped by the **Status** values:

Group by column the data in a table

To group data by column:

1.  [Open the database in the database editor](https://support.google.com/appsheet/answer/12632559).
2.  Select the table tab.
3.  Do one of the following:
    - Select a column in the **Group** drop-down
    - Select **More**  Three-dot menu vertical **\> Group by column **adjacent to the column name

## Filter data

Filters allow you to show only a subset of data data based on one or more conditions.

For example, you can create a filter to show only "rows where Status is Complete" , save the view configuration, and switch to the view configuration to see all completed work.

### Filter on multiple conditions

When you filter on multiple conditions:

- You can only define one filter per column at this time.
- When filtering on multiple columns, AppSheet uses a **logical AND**, meaning all conditions have to be true for a row to meet the criteria to be shown.
- When filtering on **Dropdown** type columns, you can select multiple options to match against. The options you select uses a **logical OR**. For example, if you select Option A and Option B in the filter for a Dropdown column, then all rows with either Option A or Option B are displayed.

### Relative filters

Relative filters allow you to filter your rows by comparing them to:

- A relative value in another column
- A relative date from today

For example, you can create a filter to "show rows where ETA is past the Deadline".

Relative filters are supported by the following column types:

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Column type                                                                   | Relative filters                                                              |
+===============================================================================+===============================================================================+
| **Text**                                                                      | -   Contains                                                                  |
|                                                                               | -   Does not contain                                                          |
|                                                                               | -   Starts with                                                               |
|                                                                               | -   Does not start with                                                       |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Number**                                                                    | -   Is greater than                                                           |
|                                                                               | -   Is less than                                                              |
|                                                                               | -   Is in between                                                             |
|                                                                               | -   Is not between                                                            |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Date**                                                                      | -   Is after                                                                  |
|                                                                               | -   Is before                                                                 |
|                                                                               | -   Is between                                                                |
|                                                                               | -   Is not in between                                                         |
|                                                                               | -   Is today                                                                  |
|                                                                               | -   Is in the next x days                                                     |
|                                                                               | -   Is in the past x days                                                     |
|                                                                               | -   Is further than x days                                                    |
|                                                                               | -   Is older than x days                                                      |
|                                                                               | -   Is exactly x days                                                         |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

### Add a filter

To add a filter:

1.  [Open the database in the database editor](https://support.google.com/appsheet/answer/12632559).
2.  Select the table tab.
3.  Click **Filter** in the toolbar to display the filter bar.

    Filter by column in a table
4.  Click **Add filter**.
5.  Select a column from the **Column** drop-down list.
6.  Configure the filter. Options vary based on the column data type.
7.  Click **Add**.
    The filter is applied.
8.  Repeat to add additional filters.

To update a filter, click the filter name, modify its configuration, and click **Update**.  To remove a filter, click the filter name and click **Remove**.

## Sort data by column

Sort row data based on the contents of a column. You can sort on multiple columns with multiple sort directions.

When sorting is in effect:

- New rows that get added or rows that get edited will be resorted immediately.
- You will not be able to manually reorder rows.

To sort data by column:

1.  [Open the database in the database editor](https://support.google.com/appsheet/answer/12632559).
2.  Select the table tab.
3.  Click **Sort** in the toolbar.
4.  Select a column from the drop-down list.
5.  Click **Asc** or **Desc** to sort in ascending or descending order, respectively.
6.  Optionally click **Add sort column** to add another sort column or click x to delete an existing sort column.
7.  Click **Apply**.

Alternatively, select **More**  Three-dot menu vertical **\> Sort on column **adjacent to the column name.

## Change the row density

Change the row density to allow more space within each row and allow text and content to wrap across multiple lines.

1.  [Open the database in the database editor](https://support.google.com/appsheet/answer/12632559).
2.  Select the table tab.
3.  Click  in the toolbar.
4.  Select one of the following row density settings: Default, Comfortable, Spacious

## Manage the view configurations

When you create a new table, a default view configuration is created for you called **Saved View 1**. You can delete or customize the view configuration or add new view configurations, as described in the following sections.

- [Add a view configuration](#add-view-configuration)
- [Save changes to a view configuration](#save-changes-view-configuration)
- [Change the default view configuration](#change-default-view-configuration)
- [Clear all view configuration selections](#clear-configuration)
- [Copy the link to a view configuration](#copy-link-view-configuration)
- [Rename a view configuration](#rename-view-configuration)
- [Duplicate a view configuration](#duplicate-view-configuration)
- [Delete a view configuration](#delete-view-configuration)

### Add a view configuration

To add a view configuration:

1.  [Open the database in the database editor](https://support.google.com/appsheet/answer/12632559).
2.  Select the table tab.
3.  Click the view configuration to display the Saved views in this table dialog.
4.  Click **+Add new view.**
5.  Click **Save new view**.

### Save changes to a view configuration

As you change the table [layout](#configure-table-layout), [group](#group-data-by-column), [filter](#filter-data-by-column), [sort](#sort-data-by-column), and [row density](#change-row-density) selections, an orange dot appears next to the view name to indicate that you have unsaved changes. Changes that you make to a view configuration do not affect other users until you save them. 

Save changes to view configuration

To save changes to a view configuration:

1.  [Open the database in the database editor](https://support.google.com/appsheet/answer/12632559).
2.  Select the table tab.
3.  Click the view configuration to display the Saved views in this table dialog.
4.  Click **Save **adjacent to the view configuration name.

### Change the default view configuration

The default view configuration is the one that is open when you initially view the table. The default view configuration is the first view configuration in the list,=.

To change the default view configuration:

1.  [Open the database in the database editor](https://support.google.com/appsheet/answer/12632559).
2.  Select the table tab.
3.  Click the view configuration to display the Saved views in this table dialog.
4.  Do one of the following:
    - Press and hold the drag handle to drag the view configuration to the top of the list.
    - Select **More**  Three-dot menu vertical **\> Make default **adjacent to the view configuration name.
      **Note**: This option is greyed out if the view configuration is already set as the default.

###  Clear all view configuration selections

To clear all [table layout](#configure-table-layout), [group](#group-data-by-column), [filter](#filter-data-by-column), and [sort](#sort-data-by-column) selections and revert back to the original default configuration, click **X** in the toolbar.

Clear all configuration selections

**Note**: X appears in the toolbar only after you have made a change to the view configuration.

### Copy a link to a view configuration

Copy the link to a view configuration to share with a collaborator.

To copy the link to a view configuration:

1.  [Open the database in the database editor](https://support.google.com/appsheet/answer/12632559).
2.  Select the table tab.
3.  Click the view configuration to display the Saved views in this table dialog.
4.  Select **More**  Three-dot menu vertical **\> Copy link to view **adjacent to the view configuration name.
5.  Share the link with collaborators.

### Rename a view configuration

To rename a view configuration:

1.  [Open the database in the database editor](https://support.google.com/appsheet/answer/12632559).
2.  Select the table tab.
3.  Click the view configuration to display the Saved views in this table dialog.
4.  Select **More**  Three-dot menu vertical **\> Rename **adjacent to the view configuration name.
5.  Edit the name.
6.  Click OK.

### Duplicate a view configuration

To duplicate a view configuration:

1.  [Open the database in the database editor](https://support.google.com/appsheet/answer/12632559).
2.  Select the table tab.
3.  Click the view configuration to display the Saved views in this table dialog.
4.  Select **More**  Three-dot menu vertical **\> Duplicate view **adjacent to the view configuration name.

A new view configuration is added and named as follows: `Copy of `*`view-config-name` *

[Rename the view configuration](#rename-view-configuration), if desired.

### Delete a view configuration

**Note**: You cannot delete the default view configuration. You must first [change the default](#change-default-view-configuration).

To delete a view configuration:

1.  [Open the database in the database editor](https://support.google.com/appsheet/answer/12632559).
2.  Select the table tab.
3.  Click the view configuration to display the Saved views in this table dialog.
4.  Select **More**  Three-dot menu vertical **\> Delete **adjacent to the view configuration name.
