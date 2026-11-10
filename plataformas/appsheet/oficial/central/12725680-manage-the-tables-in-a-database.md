---
fonte: https://support.google.com/appsheet/answer/12725680?hl=en
baixado: 2026-11-10
---

# Manage the tables in a database

Manage the tables in an AppSheet database as described in the following sections:

- [Add a table](#add-table)
- [Copy a table](#copy-table)
- [Edit table settings](#edit-table-settings)
- [Close and reopen a table](#close-reopen-table)
- [Delete a table](#delete-table)

## Add a table

When you [create a database](https://support.google.com/appsheet/answer/12635312), it contains at least one table. 

To add a table to a database:

1.  [Open the database in the database editor](https://support.google.com/appsheet/answer/12632559).
2.  Click  **+ Add Table \> Create new table**.

A new blank table is added to the database and named Table\_*n*, by default, where *n* is incremented by 1 each time you add a new table. You can change the table name and other properties, as described in [*Edit table settings*](#edit-table-settings). 

You can copy and paste directly from Google Sheets or Google Docs into a table in the [grid layout](https://support.google.com/appsheet/answer/12726685#grid-layout). You'll need to create identical column names and types in the AppSheet database table before copying the data. Any tab-separated content can be pasted across multiple columns within a table. Note the following:

- Pasting data over [`Lookup` column data types](https://support.google.com/appsheet/answer/12798217#add-lookup) is not supported
- Pasting values that do not match the options in a drop-down column results in the values being removed

## Copy a table

To copy a table:

1.  [Open the database in the database editor](https://support.google.com/appsheet/answer/12632559).
2.  Position your cursor over the table tab.
3.  Select **More ** Three-dot menu vertical ** \> Copy table**.
    The Copy this table dialog displays.
4.  Select **Copy table rows** to copy the rows in the existing table to the new table.
5.  Click **OK**.

A new table is added to the database and named **Copy of *tablename***.

## Edit table settings

To edit table settings:

1.  [Open the database in the database editor](https://support.google.com/appsheet/answer/12632559).
2.  Position your cursor over the table tab.
3.  Select **More ** Three-dot menu vertical ** \> Table settings**.
4.  Modify one or more of the following settings:
    +-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Table name                                                                    | Edit the name of the table. Must be unique within the database.               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Table description.                                                            | Add a description of the table.                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Table time zone                                                               | Select a timezone from the drop-down list.                                    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Table locale                                                                  | Select the locale used for `Date` and `Time` columns formats (for example:    |
|                                                                               | 9/22/22, 1:38 PM)                                                             |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Table-to-table permissions                                                    | Manage read access permissions by other tables in the database.               |
|                                                                               |                                                                               |
|                                                                               | Table-to-table permissions are added automatically when you [add a            |
|                                                                               | `Reference` column in a                                                       |
|                                                                               | table](https://support.google.com/appsheet/answer/12798217#add-reference).    |
|                                                                               |                                                                               |
|                                                                               | **Note**: If you remove a table-to-table permission, it will cause any linked |
|                                                                               | columns that rely on the permission to break and fail.                        |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
5.  Click **Save**.

## Close and reopen a table

When you open an AppSheet database in the database editor for the first time, AppSheet shows the 10 most recent tables only. On subsequent loads, AppSheet may only display a subset of tables based on the current session history (can be greater than 10). If the desired table is not in view (closed), use the steps described below to reopen the table.

To close a table in the database editor:

1.  [Open the database in the database editor](https://support.google.com/appsheet/answer/12632559).
2.  Position your cursor over the table tab.
3.  Select **More ** Three-dot menu vertical ** \> Close**.

To reopen a table in the database editor:

1.  [Open the database in the database editor](https://support.google.com/appsheet/answer/12632559).
2.  Click  **+ Add Table \> Load existing table**.
3.  Select the table you want to reopen.

## Delete a table

**Before you delete a table**, consider the impact the delete operation will have on any apps that are using it. See [Access the apps using a table](https://support.google.com/appsheet/answer/12728278).

To delete a table:

1.  [Open the database in the database editor](https://support.google.com/appsheet/answer/12632559).
2.  Position your cursor over the table tab.
3.  Select **More ** Three-dot menu vertical ** \> Delete table**.
4.  Click **OK** to confirm the delete operation.
