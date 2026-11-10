---
fonte: https://support.google.com/docs/answer/11468464?hl=en
baixado: 2026-11-10
---

# Learn how to improve Sheets performance

You can improve the performance of Google Sheets and speed up calculations.

## How Google Sheets performs calculations

You can use Google Sheets without an internet connection. Your changes are saved within your browser and then sent to Google, which means that even when you are offline, you can continue using Google Sheets.  

As you make edits, Google Sheets performs calculations in the background. A green loading bar may appear at the top right while you or other collaborators make edits. This progress bar shows that Google Sheets is working and you can continue to make edits. For example, you might see the green loading bar when you first load a sheet or when you perform formula calculations. 

The progress bar may also appear when a collaborator makes changes or an automated script is running in the background. The progress bar is only a visual representation that the application is working and updating, you don’t need to await its completion. 

Each time a cell is edited, Sheets evaluates the formula in that cell plus all dependent cells. For example, if B1 has `=A1+1` and A1 changes to `=2+2`, Sheets evaluates A1 and B1. Even a small value change in one cell can trigger many changes that can take a little while to fully calculate.

## Reference repeated subexpressions

If you repeat the same subexpression, you can move that subexpression into its own cell and reference the cell.

Instead of repeating the `SUM($A$2:$A$6)` formula in each cell, like the example below:

Consider moving that calculation to a new cell, and then reference that computed result. In the example below the `SUM($A$2:$A$6) `formula is moved into B8, and then the other formulas just reference `$B$8`. 

**Tip:** Some functions, like `TODAY,` `NOW`, and `RAND`, should be used sparingly because they’re volatile - they are constantly changing, and must be evaluated after every edit. Where appropriate, move them into their own cell.

## Use helper columns with VLOOKUP & MATCH

Avoid the use of functions on a range and nested inside the VLOOKUP and MATCH function’s range argument. These lookup functions are optimized to run over simple range arguments.

**Tips:**

- Instead of `VLOOKUP(“key”, SORT(A1:B10, 1), 2),` to organize data in `A1:B10,`click **Data** and then ** Sort range**.
- For `UNIQUE`, to remove duplicates, click **Data** and then ** Data cleanup** and then **Remove duplicates**.
- Instead of `MATCH(7, ARRAYFORMULA(WEEKDAY(G2:G4)), 0),` move the `ARRAYFORMULA` into a helper column and implement the match on that column.

## Remove conditional format rules

You can review and remove unnecessary conditional format rules, which can slow down calculations.

1.  In Google Sheets, open a spreadsheet.
2.  Select the entire sheet.
3.  At the top, click **Format** and then **Conditional Formatting**.
4.  On the right, find the rule you want to remove.
5.  Click Remove rule . 

This is an important optimization because conditional formatting can take a long time to calculate, and all the rules are applied to the entire data range As the data grows, there are more and more evaluations that need to happen. Conditional formatting rules can also become duplicative or overwrite each other and cleaning those cases up is the best way to make an easy improvement to the performance of your Sheet.
