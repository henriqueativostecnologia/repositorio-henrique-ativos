---
fonte: https://support.google.com/appsheet/answer/12726090?hl=en
baixado: 2026-11-10
---

# Manage the columns in a table

In AppSheet database tables, every column describes a field that all rows in the table can have. For example, every row in a table of Team Members represents an individual who is part of your team, and every column in your table describes a field in a row. All fields are optional, so you can have an empty or blank value in a column.

Manage the columns in a table as described in the following sections:

- [Understand the column data types](#column-data-types)
- [Add a column](#add-column)
- [Edit the column name or data type](#edit-column-name-data-type)
- [Set column labels](#set-column-labels)
- [Duplicate column](#duplicate-column)
- [Rearrange columns](#rearrange-columns)
- [Freeze columns](#freeze-columns)
- [Lock columns](#lock-columns)
- [Delete a column](#delete-column)

If you change the column structure in a database that is in use by one or more apps, it is recommended that you regenerate the associated table in the app editor, as described in [Regenerate the table](https://support.google.com/appsheet/answer/10106675#regenerate-structure).

## Understand the column data types

The column data types supported by AppSheet databases map to the same data types in the AppSheet app editor with the exception of the following:

- [Row ID](https://support.google.com/appsheet/answer/10106672#row-id) column data types. 
  Each row inside an AppSheet database has a unique Row ID automatically assigned to it. Row IDs act as a key for linking data from one table to another. This makes it easier to manage data inside the database editor such as linking data across tables using `Reference` columns. The Row ID column is hidden by default in the database editor. If you want to show the Row ID in the database editor, [add](#add-column) the Row ID column to the table.
  You can select a different table key inside the app editor, but before doing so it is important to consider if the table is being referenced. If you change the table key, these references will break since the database will continue to use Row ID as the key. This means if the referenced table does not use Row ID as the key, the column type inside the database should not be a `Reference`. To learn more, see [Row ID](https://support.google.com/appsheet/answer/10106672#row-id).
- [Lookup column data types](https://support.google.com/appsheet/answer/12798217#add-lookup). `Lookup` column data types are converted to the type of the column that they reference.

For more information, see [Column data types](https://support.google.com/appsheet/answer/10106435). 

Also consider the following:

- When using `Reference` column data types, you can only reference tables within the same database. See [Add references between tables](https://support.google.com/appsheet/answer/12798217).
- If you have an `Enum` drop-down column that doesn't have options defined, a permanent warning is displayed in the AppSheet app editor prompting you to regenerate the schema. To avoid this error, make sure that the `Enum` drop-down column has at least one option defined. 
- When configuring drop-down columns in the app editor, turning on the **[Allow other values](https://support.google.com/appsheet/answer/10106509#allow-other-values) **property is not supported for AppSheet databases, If turned on, you will encounter errors in your app if values other than the predefined allowed values are specified.

## Add a column

To add a column to a table:

1.  [Open the database in the database editor](https://support.google.com/appsheet/answer/12632559).
2.  Select the table tab.
3.  Do one of the following:
    - To insert a column after the last column in the table:
      - Click **+ Add column** in the header bar
      - Click **Columns** in the toolbar to display the Edit table columns dialog and click **Add new column**
    - To insert a column to the left of a column:
      - Click **More**  Three-dot menu vertical **\> Insert column left** adjacent to the column name
      - Click **Columns** in the toolbar to display the Edit table columns dialog and click **More**  Three-dot menu vertical **\> Insert new column above** adjacent to the column name
4.  Enter the name of the column.
5.  Select a column data type.
6.  Click **Save**.

## Edit the column name or data type

**Note if editing the column data type**:

When converting between column data types that have incompatible values, for example a `Date` data type to a `Video` data type, a confirmation warning is displayed to indicate that row values that cannot be reasonably converted to the new type and will be left empty. You can **undo** the column data type change if you are not satisfied with the results of the conversion.

 

If you aren't sure about the compatibility of type conversion, you can make a copy of the column first so that you can compare the contents. 

To edit the column name or data type:

1.  [Open the database in the database editor](https://support.google.com/appsheet/answer/12632559).
2.  Select the table tab.
3.  Do one of the following:
    - Click **More**  Three-dot menu vertical **\> Edit column **adjacent to the column name
    - Click **Columns** in the toolbar to display the Edit table columns dialog and click **More**  Three-dot menu vertical **\> Edit column **adjacent to the column name
4.  Edit the column name. It must be unique within the table.
5.  Optionally, select a new [column data type](https://support.google.com/appsheet/answer/10106435) from the drop-down list. (See the **Note** above.)
6.  Configure the column data type, if required. 
    **Note**: You can configure options for `Color`, `Enum`, `EnumList`, `Lookup`, and `Progress` types only.
7.  Click **Save**.

## Set column labels

Labels allow you to choose the most important columns in a table. Labels determine which columns are prominently displayed for that table, similar to a title. One non-image column and one image column can be used as labels. All tables have a non-image label.

Set column labels as described in the following sections:

- [Set column as a label](#set-a-column-as-label)
- [Set column as an image label](#set-column-as-image-label)

When you [add references between tables](https://support.google.com/appsheet/answer/12798217) using the `Reference` column data type, the column label is used to identify the content that is used in the referenced table.

### Set column as a label

To set a column as a label:

1.  [Open the database in the database editor](https://support.google.com/appsheet/answer/12632559).
2.  Select the table tab.
3.  Select **More**  Three-dot menu vertical **\> Use column as label** adjacent to a column name. 
    **Note**: The Use column as label setting does not appear for the column that is currently selected as the label.

You can't unset a non-image column label; you can only set a different column as a column label.

### Set column as an image label

To set a column as an image label:

1.  [Open the database in the database editor](https://support.google.com/appsheet/answer/12632559).
2.  Select the table tab.
3.  Select **More**  Three-dot menu vertical **\> Use column as image label** (for Image data types only) adjacent to a column name. 
    **Note**: The Use column as image label setting does not appear for the column that is currently selected as the label.

To unset an image label, select **More**  Three-dot menu vertical **\> Unset column image label** adjacent to a column name.

## Duplicate a column

 To duplicate a column:

1.  [Open the database in the database editor](https://support.google.com/appsheet/answer/12632559).
2.  Select the table tab.
3.  Do one of the following:
    - Click **More**  Three-dot menu vertical **\> Duplicate column **adjacent to the column name
    - Click **Columns** in the toolbar to display the Edit table columns dialog and click **More**  Three-dot menu vertical **\> Duplicate column **adjacent to the column name

A column is added to the right of the duplicated column named as follows: *`columnname`*` - Copy` 
Edit the column name and configuration, as appropriate.

## Rearrange columns

To rearrange columns in a table:

1.  [Open the database in the database editor](https://support.google.com/appsheet/answer/12632559).
2.  Select the table tab.
3.  Do one of the following:
    - Press and hold the left mouse button over a column header and drag the column to its new location
    - Select **More**  Three-dot menu vertical **\> Move left** or **Move right** adjacent to a column name
    - Click **Columns** in the toolbar to display the Edit table columns dialog, press and hold the left mouse button over a column header, and drag the column to its new location

## Freeze columns

Freeze a column so that it stays in view on the screen while you scroll horizontally. This is useful when you have a lot of columns and want to keep specific data in view.

When you freeze a column, it affects the view configuration. To  persist the frozen columns, [save the view configuration](https://support.google.com/appsheet/answer/12726685#save-changes-view-configuration).

To freeze a column:

1.  [Open the database in the database editor](https://support.google.com/appsheet/answer/12632559).
2.  Select the table tab.
3.  Click **More**  Three-dot menu vertical **\> Freeze column** adjacent to the column name.

To unfreeze a column, click **More**  Three-dot menu vertical **\> Unfreeze columns **adjacent to the column name.

## Lock columns

Lock a column to prevent anyone with the appropriate [database permissions](https://support.google.com/appsheet/answer/12637319#database-permissions) from editing it. A locked column displays the lock symbol:

To lock a column:

1.  [Open the database in the database editor](https://support.google.com/appsheet/answer/12632559).
2.  Select the table tab.
3.  Click **More**  Three-dot menu vertical **\> Lock column** adjacent to the column name.

To unlock a column, click **More**  Three-dot menu vertical **\> Unlock column** adjacent to the column name.

## Delete a column

**Before you delete a column**, consider the impact the delete operation will have on any apps that are using it. See [Access the apps using a table](https://support.google.com/appsheet/answer/12728278). Deleting a column may also impact the filter or group by view configuration.

**Note**: You can't delete a column that is set as a label. You must first [set a different column as a label](#set-column-as-label).

To delete a column:

1.  [Open the database in the database editor](https://support.google.com/appsheet/answer/12632559).
2.  Select the table tab.
3.  Do one of the following:
    - Click **More**  Three-dot menu vertical **\> Delete column** adjacent to the column name
    - Click **Columns** in the toolbar to display the Edit table columns dialog and click **More**  Three-dot menu vertical **\> Delete column **adjacent to the column name
4.  Confirm the delete operation when prompted.
