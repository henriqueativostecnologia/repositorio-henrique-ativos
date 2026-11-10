---
fonte: https://support.google.com/appsheet/answer/10106591?hl=en
baixado: 2026-11-10
---

# Improve performance when you add, remove, or rearrange columns

When you regenerate a table that resides in a Google Sheets or Microsoft Excel worksheet, AppSheet reads and analyzes the contents of that worksheet. 

Specifically, AppSheet analyzes the following:

- Worksheet header cell contents
- Worksheet cell data values 
- Format of each cell
- Worksheet formula of each cell
- Data validation rules defined for the worksheet

AppSheet uses this information to determine the name and data type of each column in the worksheet. It combines this new information with any existing information that may exist for the column. AppSheet's goal is to detect newly added columns and accurately determine their name and type. At the same time, AppSheet tries to maintain the name and type information for existing columns.

Before AppSheet can analyze the data value in each cell, it must first calculate the value of all worksheet formula contained in the worksheet being regenerated. The time required to calculate these worksheet formula depends on the number and complexity to the worksheet formulas contained in the worksheet being regenerated. It also depends on the whether these worksheet formulas refer to cells in other worksheets that contain worksheet formulas. 

Consider the following example, in which cell `A2` of the regenerated worksheet contains a worksheet formula that refers to a sequence of cells in other worksheets that contain worksheet formulas. Assume the worksheet formula in cell `A2` of the regenerated worksheet refers to cell `B2` of the OtherSheet1 worksheet. Assume the worksheet formula in cell `B2` of OtherSheet1 worksheet refers to cell `C2` of OtherSheet2 worksheet which also contains a worksheet formula. In this case, to compute the value of cell `A2` in the regenerated worksheet, AppSheet must first compute the value of cell `C2` in the OtherSheet2 worksheet, and then cell `B2` in the OtherSheet1 worksheet, and then cell A2 in the regenerated worksheet.

AppSheet uses a **Calc Chain** to keep track of the cells containing worksheet formulas that need to be evaluated. The Calc Chain is ordered to reflect the precise order that the worksheet formulas need to be evaluated to yield the correct result. For example, the Calc Chain for our previous example would contain `cell C2 of sheet Othersheet2`, followed by `cell B2 of sheet Othersheet1`, followed by `cell A2 of the regenerated sheet`.

The Calc Chain length depend in large part on the number of cells in the regenerated worksheet that contain worksheet formulas. The Calc Chain contains a discrete entry for each cell of the regenerated worksheet that contains a worksheet formula, followed by the worksheet formulas on which the regenerated formula depends. If you double the number of rows in the regenerated worksheet, the Calc Chain length can double. If you quadruple the number of rows in the regenerated worksheet, the Calc Chain length can quadruple, and so on.

The time required to compute the Calc Chain depends on both the number and complexity of the worksheet formulas it contains. The time required to compute the Calc Chain can significantly increase the time required to regenerate a worksheet. The Calc Chain computation time can vary from seconds to many minutes. If you are regenerating a worksheet having many rows with many complex formulas, the regenerate can take a very long time.

You can greatly reduce the time required to do a regenerate by temporarily reducing the number of rows contained in the regenerated worksheet. For example, your worksheet probably contain thousands of nearly identical rows that only differ in their specific cell values. In this case, you can speed up regenerate as follows:

1.  Make a copy of the data values in regenerated worksheet.
2.  Delete all but the first three to five rows of the regenerated worksheet. 
3.  Perform the regenerate using the truncated worksheet.
4.  Verify that the regenerate was successful. For example, confirm that the column names and types are correct. Confirm that the worksheet formulas contained in the table's **Spreadsheet formula** property are correct. 
5.  Restore all of the original data values in the regenerated worksheet.
6.  Sync the updated table using your AppSheet application and confirm that you can see all of the rows of the regenerated table.
