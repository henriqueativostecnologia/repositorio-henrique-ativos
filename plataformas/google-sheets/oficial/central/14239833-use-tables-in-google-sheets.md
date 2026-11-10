---
fonte: https://support.google.com/docs/answer/14239833?hl=en
baixado: 2026-11-10
---

# Use tables in Google Sheets

In Google Sheets, tables can simplify data creation and reduce the need to repeatedly format, input, and update data by automatically applying format and structure to ranges of data.

Tables are well suited to track and organize information like:

- Project tracking
- Event planning
- Inventory management

There are 2 main parts of a table:

- For each column, you can set the appropriate column type. Your table ensures all data you enter aligns.
- You have access to a unified menu. You can manage table-level settings and perform actions like create a filter view for your table.

This article includes information on how to:

- [Convert existing data to a table](https://support.google.com/docs/answer/14239833#convert)
- [Insert a pre-built table](https://support.google.com/docs/answer/14239833#get-started)
- [Set up your table](https://support.google.com/docs/answer/14239833#setup)
- [Use the table menu](https://support.google.com/docs/answer/14239833#use-table-menu)
- [Use table references](https://support.google.com/docs/answer/14239833#use-table-references)
- [Use table views](https://support.google.com/docs/answer/14239833#use-table-views)
- [Use group by view](https://support.google.com/docs/answer/14239833#group)
- [Give feedback on tables](https://support.google.com/docs/answer/14239833#feedback)

## Convert existing data to a table

1.  Open a spreadsheet in [Google Sheets](https://docs.google.com/spreadsheets).
2.  Select a range of cells, either empty or with data.
3.  On the Menu Bar, click **Format** and then **Convert to table**.
4.  Select the appropriate column type for each column.

[Learn more about column types](#column).

For some column types, placeholder chips are auto populated to allow for easy data entry. To turn off placeholder chips for a column:

1.  On your computer, open a Sheet with a table.
2.  Next to each column header, open the **Column menu**.
3.  Click **Edit column type.**
    - **Tip:** If any column is filtered, the filter menu will show up. To edit the column type, click **Column menu**.
4.  Uncheck **Show placeholders**.

## Get started by inserting a pre-built table

You can insert a new table with a predefined structure through templates that cover common use cases.

You can select a template that matches your use case. Go to the:

- Insert menu:
  - Click **Insert** and then **Pre-built table**.

A sidebar opens for both menu options where you can browse, preview, and insert one or multiple pre-built blocks.

## Set up your table

#### Create table names

Table names must follow certain rules and format requirements, they can’t:

- Be named TRUE or FALSE.
- Use "A1" or "R1C1" syntax, like "A1” or “AA11."
- Start with a number.
- Exceed 255 characters.
- Have special characters, except for underscores.

**Tip:** Spaces in table name changes to underscores in formulas. For example, “Table 1” becomes “Table_1.”

Examples of valid table names:

- Table1
- Project roadmap
- Q3_Sales

#### Set column types

Table column types help you organize, format your column data, and prevent errors as they report incorrect data types. For example, if you select “Date” as your column type, it shows a warning for cells within the column that don’t follow this type.

You can choose from any of the following types:

- Number
  - Number
  - Percentage
  - Currency
- Text
- Date
  - Date
  - Date and time
  - Time
- Dropdown
- Checkbox
- Smart chips
  - People chip
  - File chip
  - Finance chip
  - Place chip
  - Rating chip
- None: If you select this option, we don’t apply a column type to your column. Choose this option if you want a flexible column that can support mixed data types.

## Use table menu

**Tip:** When you convert your data to a table, we automatically apply basic formatting. To further customize your table, you can either use the table menu or, in the menu bar, click **Format** and then **Table formatting**. In the “Table formatting” sidebar, you can:

- Readjust the row height
- Remove the alternating colors
- Change alternating colors
- Change header and footer style
- Select another default style

You can control your table settings and further customize it through the table menu. To use the table menu, at the top of your table, next to the table name, click Table menu Down arrow .

In the table menu, you can find these options:

- Rename table
- Adjust table range Select data range
- Table header color
  - You can select a table header color or add a custom color.
- Table formatting : You can select different formatting options:
  - Show gridlines
  - Show alternating colors
  - Show condensed view
  - Show table footer
  - View advanced options
    - In the “Table formatting” sidebar, you can create a custom style and find all table formatting options.
- Revert to unformatted data : Removes the table’s style but the table data remains unchanged.
- Delete table Delete : Removes the table and its data.
- Send feedback Feedback Icon

**Tip:** This feature is only available to certain work or school accounts. Next to the table menu, click Conditional notification . Select either:

- To set rules: Click **Create a new conditional notification**. [Learn more about conditional notifications](https://support.google.com/docs/answer/14099459).
- To use pre-built tables: To help get you started, Google Sheets automatically attaches pre-built conditional notification rules such as “Send email when project task owner changes.” By default, the pre-built conditional notification rules are disabled until you edit or enable it.

## Use table references

Table references are a special way to refer to a table or parts of a table in a formula. When you convert your data to a table, we give it a name, as well as each column header. You can then use those names to reference cells in the table. For example: Instead of explicit cell references: `=Sum(C2:C7)`, you can use table references: `=SUM(DeptSales[Sales Amount])`.

When you reference table elements by name, the references update whenever you add or remove data from the table.

[Learn about table references](https://support.google.com/docs/answer/15637642).

## Use table views

With views, you can find the data you care about without impacting what others see on the sheet. You can use views to show or hide specific rows and apply other configurations to manage how to visualize data.

Each view can have its own unique configurations to filter and sort.

- To create new views, click Views , and then select one of the following:
  - Create group by view
    - This allows you to see rows grouped together based on the field of your choice.
  - Create filter view

**Tip:** A temporary view is created by default. If you have edit access to the spreadsheet, you can save this view to access it later from the Table menu. Temporary views disappear after the spreadsheet refreshes.

- To apply existing views, click **Table menu ** and then existing view name.
- To save a temporary view, at the top right, click **Save view**.
  - Or, you can click Views and then **View options** and then **Save view**. [Learn how to sort and filter your data](https://support.google.com/docs/answer/3540681).
- To refresh the view, click Views and then **View options** and then **Refresh view**.

## Use group by view

You can apply column-level aggregations. When you create a new group by view, aggregation is automatically applied. Your first column from the left is grouped by “Count.”

Other column types may have aggregations already applied. You can apply the following per column aggregations:

- Average
- Count
- Empty
- Filled
- Maximum
- Minimum
- Percent empty
- Percent filled
- Percent unique
- Sum
- Unique

**To add a group by view:**

1.  Open a spreadsheet in [Google Sheets](https://docs.google.com/spreadsheets).
2.  In the menu bar, click **Insert** and then **Tables**.
3.  In the column header, select a column you want to group by view.
4.  Beside the heading name, click the Down arrow Down arrow and then **Group by column**.
5.  In each category’s row, click the Down arrow Down arrow .
    - Select an aggregation type.

**Tip:** To hide the aggregation type and results, click Views and then **View options** and then **Hide group by aggregation**.

## Give feedback on tables

If you have any issues or want to change this feature and help us improve, you can submit feedback to us.

To submit feedback:

- Use the “Send feedback” option on the tables menu.
- At the top of your sheet, click **Help** and then **Help Sheets improve**.

## Related resource

- [Learn about table references](https://support.google.com/docs/answer/15637642)
