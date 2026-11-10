---
fonte: https://support.google.com/appsheet/answer/10106592?hl=en
baixado: 2026-11-10
---

# Slices: The Essentials

When you show the contents of a table in your app, you do not need to show every row, every column, and every action. Instead, you can *slice* the data, choosing to show only a subset of the rows, columns, and actions.

- [What is a slice?](#what-slice)
- [Add a slice](#add-slice)
- [Add a slice when configuring a view](#create-slice-configure-view)
- [Configure a slice](#configure-slice)
- [Copy a slice](#copy-slice)
- [Preview a sample of the data in a slice](#preview-slice)
- [Rename a slice](#rename-slice)
- [Delete a slice](#delete-slice)

## What is a slice?

A slice is a subset of the rows, columns, and actions of a table. A slice definition has five components:

- The table it's based on (required)
- Does the slice permit adds, deletes, and updates? (required)
- The subset of rows it retains from the table (optional)
- The subset of columns it retains from the table (optional)
- The subset of actions it retains from the table (optional)

It's important to note that a slice does not need to subset rows, columns, and actions. In fact, it's common to subset just the rows or just the columns or actions as appropriate.

Slices are most useful when you want to create a view of part of a table. For instance, if you have a table that's a list of people, you might have columns for their first name, last name, birthday, address, and phone number. However, if you only want to see their first name and phone number in a view, you can add a slice that filters out all the columns in the person table except for first name and phone number.

Another use for slices is to define a logical subset of a table that can then be used in other expressions (such as a Valid_If column constraint or in an automation workflow). For this usage scenario, slices usually use row filters but do not subset the columns or actions.

Remember, once you define the slice, you still need to use this slice in a UX view.

## Add a slice

See also: [Add a slice when configuring a view](#create-slice-configure-view)

To add a slice:

1.   Open the app in the editor.
2.  Go to **Data**  and click **+** associated with the table for which you want to add a slice. Add a slice
    We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

    ## If you are using the legacy editor

    Navigate to **Data \> Slices** and click **+ New Slice**.
3.  Choose from the list of suggestions or click **Create a new slice**.
    AppSheet understands user intent and recommends slice configurations that align with what you are trying to achieve.
4.  [Configure the slice](#configure-slice).
5.  To preview the rows and columns of data your slice contains, select the **Preview Data** button. 
6.  [Create a view](https://support.google.com/appsheet/answer/10106688#create-view) for the slice.
7.  Save your app.

Repeat these steps to add multiple slices.

## Add a slice when configuring a view

To add a slice when configuring a view:

1.  Open the app in the editor.
2.  [Create a view](https://support.google.com/appsheet/answer/10106688#create-view).
3.  When selecting a table for a view in the **For this Data** field, do one of the following:
    - Click **+** in the drop-down adjacent to the table for which you want to add a slice.

      Click the plus sign adjacent to the table for which you want to create a slice
    -  Click **Use slices to filter your data**. (You can dismiss this hint at any time.)

      Create slice by clicking Use slices to filter your data helper link
4.  Choose from the list of suggestions or click **Create a new slice for *tablename***.
    AppSheet understands user intent and recommends slice configurations that align with what you are trying to achieve.
5.  [Configure the slice](#configure-slice).
6.  Save your app.

## Configure a slice

Configure the slice by using the settings described in the following table.

|                      |                                                                                                                                                                                |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Setting**          | **Description**                                                                                                                                                                |
| Slice Name           | Unique name for the slice.                                                                                                                                                     |
| Source Table         | Table to use as the source.                                                                                                                                                    |
| Row filter condition | Expression that determines whether a row should be included in the slice. For details, see [Slice row filter conditions](https://support.google.com/appsheet/answer/10106308). |
| Slice Columns        | Columns to include in the slice. For details, see [Slice columns](https://support.google.com/appsheet/answer/10106593).                                                        |
| Slice Actions        | Actions to be included in the slice. For details, see [Slice actions](https://support.google.com/appsheet/answer/10106511).                                                    |
| Update mode          | Slice permissions. To enable changes, select one or more of the following: **Updates**, **Adds**, and **Deletes**. To provide read-only access, click **Read-only**.           |
| Descriptive comment  | Description of the slice.                                                                                                                                                      |

 

The following provides an example of a completed slice in the National Parks app that uses a [`Yes/No` expression](https://support.google.com/appsheet/answer/10107946) which in this example resolves to `TRUE` (Yes) or `FALSE` (No).

Slice columns

## Copy a slice

When you copy a slice, by default the slice is named *slicename n*, where *n* is incremented by 1 each time you copy the slice.

To copy a slice:

1.  Open the app in the editor.
2.  Go to **Data** .
3.  Select the slice you want to copy in the Data panel.
4.  Select **More ********************************************************\> Duplicate**.

We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

## If you are using the legacy editor

To copy a slice:

1.  Open the app in the editor.
2.  Go to **Data \> Slices**.
3.  Expand the slice that you want to copy.
4.  Click **Copy** in the slice header.

## Preview a sample of the data in a slice

Display a sample of the data in a slice in a separate tab.

To view a sample of the data in a slice:

1.  Open the app in the editor.
2.  Go to **Data** .
3.  Select the slice you want to view in the Data panel.
4.  Click **Preview data**.
5.  Select the number of rows that you want to evaluate for sample data in the slice. 

We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

## If you are using the legacy editor

To view a sample of the data in a slice:

1.  Open the app in the editor.
2.  Go to **Data \> Slices**.
3.  Expand the slice that you want to view.
4.  Click **View data** in the slice header.

##  Rename a slice

 To rename a slice:

1.   Open the app in the app editor.
2.  Go to **Data \> Slices**.
3.  Position your cursor over the slice in the Data pane and select **More ************************************************************************************************************************\> Rename**.
    Alternatively, you can double-click on the slice name in the Data pane.
4.   Edit the name and press **Enter**.
5.  Save the app.

## If you are using the legacy editor

 To rename data:

1.   Open the app in the app editor.
2.  Go to **Data \> Slices**.
3.  Expand the slice you want to rename.
4.  Edit the **Slice name** field.
5.  Save the app by selecting one of the following:
    - **Save** - Save the app.
    - **Save & verify data** - Save the app and verify that it is runnable based on external dependencies.

## Delete a slice

To delete a slice:

1.  Open the app in the editor.
2.  Go to **Data** .
3.  Select the slice you want to delete in the Data panel.
4.  Select **More ********************************************************\> Delete**.

We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

## If you are using the legacy editor

To delete a slice:

1.  Open the app in the editor.
2.  Go to **Data \> Slices**.
3.  Expand the slice that you want to delete.
4.  Click **Delete** in the slice header.
