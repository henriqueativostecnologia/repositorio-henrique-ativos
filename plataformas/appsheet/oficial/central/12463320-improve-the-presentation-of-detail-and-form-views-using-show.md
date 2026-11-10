---
fonte: https://support.google.com/appsheet/answer/12463320?hl=en
baixado: 2026-11-10
---

# Improve the presentation of detail and form views using Show types

Improve the presentation of detail and form views using `Show` types as described in this section.

- [What are Show types?](#what-are-show-types)
- [Use a virtual column as a Show type column](#virtual-column)
- [Use an empty column in your spreadsheet as a Show type column](#empty-column)
- [Configure the column as a Show type](#configure)

For examples using `Show` types:

- [Create multi-page forms](https://support.google.com/appsheet/answer/10107388)
- [Create multi-page forms with conditional branching](https://support.google.com/appsheet/answer/10107390)
- [Configure card blocks in detail views](https://support.google.com/appsheet/answer/12407883#configure-card-blocks) for the new desktop layout

## What are Show types?

`Show` types correspond to table columns whose sole purpose is to improve the presentation of data in forms and detail views.

By default, `Show` type columns are only permitted in form views. To include `Show` type columns in detail views, enable **Include Show columns in detail views** on the **UX \> Options** pane in the **Detail View** section.

There are six categories of `Show` types that you can create based on the improvements you want to make, as summarized in the following table.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Category**                                                                  | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Page_Header                                                                   | Creates a new page. For an example, see:                                      |
|                                                                               |                                                                               |
|                                                                               | -   Form view: [Create multi-page                                             |
|                                                                               |     forms](https://support.google.com/appsheet/answer/10107388)               |
|                                                                               | -   Detail view: [Configure card blocks in detail                             |
|                                                                               |     view                                                                      |
|                                                                               | s](https://support.google.com/appsheet/answer/12407883#configure-card-blocks) |
|                                                                               |     for the new desktop layout                                                |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Section_Header                                                                | Creates a new section within the same page.                                   |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Text                                                                          | Displays a description.                                                       |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| URL                                                                           | Displays a clickable URL.                                                     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Image                                                                         | Displays a static image that is not stored in your table.                     |
|                                                                               |                                                                               |
|                                                                               | For an example, see the [Images in                                            |
|                                                                               | forms                                                                         |
|                                                                               | ](https://www.appsheet.com/template/showdef?appId=Imagesinforms-71626) sample |
|                                                                               | app.                                                                          |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Video                                                                         | Displays an MP4 video.                                                        |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

There are two ways that you can implement `Show` type columns:

- [Use a virtual column in a table as a Show type column](#virtual-column)
- [Use an empty column in a spreadsheet as a Show type column](#empty-column)

## Use a virtual column as a Show type column

To use a virtual column as a Show type column:

1.  [Add a virtual column to the table](https://support.google.com/appsheet/answer/10106758#add).
2.  Set **App formula** to **""** (empty value). This value is not applicable for `Show` type columns and will be ignored. However, it's a required field when configuring a virtual column, so you need to set it to some value.
3.  Select **Show** in the Type drop-down for the virtual column.
4.  Click **Edit**  to view the full set of properties for a specific column.
5.  [Configure the column as a Show type](#configure) and click **Done**. 
    For example:

      Configure virtual column as a Show type column
6.  Create the [detail](https://support.google.com/appsheet/answer/10106385) or [form](https://support.google.com/appsheet/answer/10107846) view.
    Explicitly include the `Show` column in your view. See [Control the order of the virtual column](https://support.google.com/appsheet/answer/10106758#order).
7.  If you are using the Show column in a detail view, enable **Include Show columns in detail views** on the **UX \> Options** pane in the **Detail View** section.
8.  Save your changes by selecting one of the following:
    - **Save** - Save the app.
    - **Save & verify data** - Save the app and verify that it is runnable based on external dependencies.

## Use an empty column in your spreadsheet as a Show type column

To use an empty column in your spreadsheet as a `Show` type column:

1.  Open your source spreadsheet for the table and insert one or more **empty columns**.

    For example, the following example shows a column structure for a Contact Us form. Columns `Page 1`, `Page 2`, and `Page 3` designate the empty columns that will be set as page breaks in the form.

    Contact Us Forms sheet showing Page 1, Page 2, and Page 3 columns

    **Note**:
    - You will configure the empty column as a `Show` type column in the app editor.
    - You can enter a header name for the empty column, if desired, such as `Page 1`. If the header column is left blank, a default name will be added to the table using the following format: `Column_`*`n`*, where *`n`* indicates its position in relation to the visible columns. The column name is visible only to the app creator; it will not be visible in the app.

2.  Open the app in the app editor.

3.  Go to **Data**  and select the table you want to edit in the list.
    We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

     
    ## If you are using the legacy editor

    Go to **Data \> Columns** and expand the table you want to edit.

4.  Perform one of the following steps:
    - [Add a new table](https://support.google.com/appsheet/answer/10105821#add) using the spreadsheet updated in Step 1. 
    - For an existing table, [regenerate the table schema](https://support.google.com/appsheet/answer/10106675#regenerate-structure). The empty column now appears in the table.

5.  Select **Show** in the **Type** drop-down for the empty column.

6.  Click the **edit (pencil) icon** associated with the column.

7.  [Configure the column as a Show type](#configure) and click **Done**.
    If you want to display a heading on the new page, enter it in the **Content** field. Otherwise, to just create a page break, leave the **Content** field blank. 

     For example:

    Configure multi-page column as Show type

8.  Create the [detail](https://support.google.com/appsheet/answer/10106385) or [form](https://support.google.com/appsheet/answer/10107846) view.
    Include the `Show` column in your view. To reorder the columns, see [Control column order](https://support.google.com/appsheet/answer/10107315).

9.  If you are using the `Show` type column in a detail view, enable **Include Show columns in detail views** on the **UX \> Options** pane in the **Detail View** section.

10. Save your changes by selecting one of the following:
    - **Save** - Save the app.
    - **Save & verify data** - Save the app and verify that it is runnable based on external dependencies.

## Configure the column as a Show type

To configure the column as a `Show` type column..

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Property**                                                                  | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Column name                                                                   | Name of the column.                                                           |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| App formula                                                                   | **Note**: Displayed for virtual columns only; not displayed for empty table   |
|                                                                               | columns.                                                                      |
|                                                                               |                                                                               |
|                                                                               | Set to: "" (empty)                                                            |
|                                                                               |                                                                               |
|                                                                               | Since a `Show` type column is informational, this value has no impact and     |
|                                                                               | will be ignored.                                                              |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Show?                                                                         | Enable this toggle.                                                           |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Type                                                                          | Set to **Show**.                                                              |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Category                                                                      | Select one of the [categories](#categories) from the drop-down based on the   |
|                                                                               | information you want to display.                                              |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Content                                                                       | Enter the content to display for the `Show` type using the Expression         |
|                                                                               | Assistant. To just create a page break, leave this field blank. For example:  |
|                                                                               | `"Update Information"`                                                        |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

The **Data Validity**, **Display**, and **Other** property sections have no effect on `Show` type columns.
