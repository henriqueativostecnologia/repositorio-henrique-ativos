---
fonte: https://support.google.com/appsheet/answer/10106593?hl=en
baixado: 2026-11-10
---

# Slice columns

When [configuring a slice](https://support.google.com/appsheet/answer/10106592#configure-slice), you choose which columns to include using the **Slice Columns** field, shown below. 

Slice columns

By default, all columns are included in the slice.

To modify the columns included in the slice, do one or more of the following:

- To reorder a column, click  alongside the column and drag it to the desired position.
- To delete a column, position your cursor over a column and click .
  **Note**: AppSheet may automatically add back columns that are required for the slice to operate correctly. Usually, this occurs with key columns that have been inadvertently excluded from the slice.
- To add a column, click **+ Add**, select columns individually or click **Select All**, and click **Add**.
  **Note**: The **+ Add** button doesn't display if all columns are included in the slice.

When updating a row in a slice, all column values are updated regardless of the columns included in the slice, but **only the columns in the slice will have their updated values synced**. So the various expressions in your row can use values of all columns of the full table row, but only changes to the slice columns will be synced.

To see what is displayed in your slice, see [Preview a sample of the data in a slice](https://support.google.com/appsheet/answer/10106592#preview-data). For example:

Preview slice
