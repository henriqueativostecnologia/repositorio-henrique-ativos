---
fonte: https://support.google.com/appsheet/answer/10101313?hl=en
baixado: 2026-11-10
---

# Mismatched spreadsheet formulas

When you add or regenerate a table you may see the warning:

`Column '<column name>' of sheet '<sheet name>' contains mismatched formulas. `

This article explains what this message means, how to find the mismatched formulas, and how to fix the mismatched formulas.

## Understand mismatched formulas

When you add or regenerate a table, AppSheet checks the spreadsheet formulas in each column of your sheets. If a column contains a consistent spreadsheet formula, AppSheet recognizes the formula and stores it in the **Spreadsheet formula** property of that field. 

To view the Spreadsheet formula property:

1.  Open your app in the editor.
2.  Go to the **Data \> Columns** tab.
3.  Expand the table.
4.  Click the **Edit** (pencil) icon associated with the column.
5.  Expand **Auto Compute**.
6.  Check the **Spreadsheet formula** property.

When a field contains a **Spreadsheet formula**, AppSheet inserts that formula in that field for every newly added row.

### Check spreadsheet formulas

AppSheet checks the sheet formula in every cell of a column. It does this by translating the sheet formula from the customary **A1** format to [**R1C1**  format](https://bettersolutions.com/excel/formulas/cell-references-a1-r1c1-notation.htm). **A1** format is the default sheet formula format used by both Google Sheets and Excel. **R1C1**  format is used less frequently, but it it is very useful when comparing one sheet formula to another. It is the easiest way to determine if two sheet formulas are exactly equivalent.

AppSheet computes the percentage of cells in the column that contain each type of **R1C1** formula. AppSheet treats an empty cell with no formula as yet another type of formula (the "Empty Formula"). Every cell in the column contributes to the percentage of one type of formula or another. 

If one type of **R1C1** formula appears in a high percentage of column cells, AppSheet assigns that formula to the entire column. This approach allows AppSheet to detect the formula that appears most frequently while ignoring the occasional distinct formula type that might appear somewhere in the column.

### Mismatched formulas

If a column contains mismatched formula, AppSheet reports the warning `Column '<column name>' of sheet '<sheet name>' contains mismatched formulas`. The warning goes on to report what mismatched formulas it has found and what rows contain each version of the mismatched formula. This can help you find the mismatched formulas. Often only one or two cells contain mismatched formulas.

You can resolve the mismatch by making the formulas in those cells consistent and regenerating the table. Every time you regenerate your table, AppSheet reexamines the formulas in each column of the table.

## Find mismatched formulas

When the AppSheet app editor detects formula mismatches it displays a warning message containing:

1.  The number of mismatches found.
2.  The first five mismatched formulas in both **A1** and **R1C1** format along with the row numbers containing those formulas.

Use the warning information to find the mismatched formulas.

1.  Compare the formulas in **R1C1** format. Matching formulas will have exactly the same formula value in **R1C1** format. Mismatched formulas will have different formula values in **R1C1** format. Even a single character difference in the **R1C1** formats will result in a mismatch.
2.  Use the row numbers to find the rows having the mismatched formulas.

## Fix mismatched formulas

One common cause of mismatching formulas is using a constant row number without specifying the row number in [Absolute](https://support.office.com/en-us/article/switch-between-relative-absolute-and-mixed-references-dfec08cd-ae65-4f56-839e-5f0d8d0baca9) form. For example, a mismatched formula warning will occur if the formula `$A10` appears in **A1** format in every cell of a column. `$A` makes the column reference Absolute; however, the row number `10` is [Relative](https://support.office.com/en-us/article/switch-between-relative-absolute-and-mixed-references-dfec08cd-ae65-4f56-839e-5f0d8d0baca9) because it is not preceded by a `$`. It will results in a different **R1C1** formula value in each row of the sheet. If you intend to specify a constant row number, specify the **A1** formula `$A$10`. In this **A1** formula both the column and row are in Absolute form.
