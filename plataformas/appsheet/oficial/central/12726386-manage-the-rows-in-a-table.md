---
fonte: https://support.google.com/appsheet/answer/12726386?hl=en
baixado: 2026-11-10
---

# Manage the rows in a table

Manage the rows in a table as described in the following sections:

- [Add a row](#add-row)
- [Edit a row](#edit-row)
- [Copy the contents of a cell in a row](#copy-contents)
- [Duplicate a row](#duplicate-row)
- [Add a comment to a row](#add-comment)
- [View row history and restore a row](#view-row-history)
- [Get a link to a row record](#get-link-to-row)
- [Clear row values](#clear-row-values)
- [Delete a row](#delete-row)

## Add a row

To add a row:

1.  [Open the database in the database editor](https://support.google.com/appsheet/answer/12632559).
2.  Select the table tab.
3.  Do one of the following:
    - To insert a row after the last row in the table:
      - Click **+ Add row** to add an empty row
      - Click  to open the Create row dialog, enter the row contents, and click **Save**.
    - To insert a row above a row, right-click the row and select **Insert row above**
    - To insert a row after the currently selected row, click **Shift-Enter**.

A blank row is added to the table.

## Edit a row

Edit a row directly in the table or by opening the row in the record view.

You can copy and paste directly from Google Sheets or Google Docs into a table in the [grid layout](https://support.google.com/appsheet/answer/12726685#grid-layout). You'll need to create identical column names and types in the AppSheet database table before copying the data. Any tab-separated content can be pasted across multiple columns within a table. Note the following:

- Pasting data over [`Lookup` column data types](https://support.google.com/appsheet/answer/12798217#add-lookup) is not supported
- Pasting values that do not match the options in a drop-down column results in the values being removed

To open the row in the record view:

1.  [Open the database in the database editor](https://support.google.com/appsheet/answer/12632559).
2.  Select the table tab.
3.  Right-click the row and select **Open in record view.**
    The **Edit Row from *tablename* **dialog opens.
4.  Edit the row details.
5.  Click **Save**.

## Copy the contents of a cell in a row

To copy the contents of a cell in a row:

1.  [Open the database in the database editor](https://support.google.com/appsheet/answer/12632559).
2.  Select the table tab.
3.  Right-click the cell that you want to copy and select **Copy**.
4.  Right-click the cell where you want to paste the content and select **Paste**.

## Duplicate a row

To duplicate a row:

1.  [Open the database in the database editor](https://support.google.com/appsheet/answer/12632559).
2.  Select the table tab.
3.  Right-click the row and select **Duplicate row.**

The row is added immediately after the copied row.

## Add a comment to a row

Tagging people in a comment is not yet supported. 

To add a comment to a row:

1.  [Open the database in the database editor](https://support.google.com/appsheet/answer/12632559).
2.  Select the table tab.
3.  Position your cursor in the numeric tracking column associated with the row and click one of the following: 
    - Add column to AppSheet database icon  if there are no comments
    -  if there are existing comments

    Add a comment to a AppSheet database row
4.  In the Comments dialog, do one of the following:
    - To start a new thread, click **New Comment Thread**, enter a comment, and click **Comment**.
    - To reply to an existing thread, click the thread, enter a comment, and click **Reply**.
    - To delete an entire comment thread, in the first comment select **More**  Three-dot menu vertical **\>** **Delete comment thread**, then click **OK** to confirm the delete operation.
    - To delete a reply, in any reply in the thread select **More**  Three-dot menu vertical **\>** **Delete reply**, then click **OK** to confirm the delete operation.
5.  Click anywhere outside of the dialog to close it.

## View row history and restore a row

See [View the change history and restore changes](https://support.google.com/appsheet/answer/12726292).

## Get the link to a row

Get the link to a row to share with collaborators.

To get the link to a row:

1.  [Open the database in the database editor](https://support.google.com/appsheet/answer/12632559).
2.  Select the table tab.
3.  Right-click the row and select **Get link to this row**.
4.  Share the link with collaborators.

## Clear row values

To clear the values within a row:

1.  [Open the database in the database editor](https://support.google.com/appsheet/answer/12632559).
2.  Select the table tab.
3.  Right-click in the row in the first (numeric) column of the row.
4.  Select **Clear row values**.

## Delete a row

To delete a row:

1.  [Open the database in the database editor](https://support.google.com/appsheet/answer/12632559).
2.  Select the table tab.
3.  Right-click the row and select **Delete**.
