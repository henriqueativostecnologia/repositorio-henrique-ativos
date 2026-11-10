---
fonte: https://support.google.com/appsheet/answer/10105403?hl=en
baixado: 2026-11-10
---

# App changes are not captured in the spreadsheet or the app

## If changes are not captured in a spreadsheet

If changes made in the app do not appear to be recorded in the backend spreadsheet, here are some troubleshooting steps:

1.  Is the app being synced after the updates are made? In some cases, your app users may not know they should click **Sync**.
2.  Were there any errors reported during Sync?
3.  Check the app's [Audit History](https://support.google.com/appsheet/answer/10104794) to see if it shows that the changes were actually received and successfully applied.
4.  Do you have a lot of empty rows in your sheet? If you have a hundred empty rows followed by a row with some text in it, AppSheet will insert new entries after that very last row. You may not see these rows because you may not be scrolling down your spreadsheet to find them. Remove all empty rows in your sheet to avoid this situation. 
5.  Do you use the `RowNumber` column as the key of your table? This is a bad idea and can lead to data being overwritten or the wrong row being updated.

If you are using Google Sheets:

1.  Do you have filters set on the sheet? There is a bug in Google Sheets that causes updates to appear to succeed (but never actually get applied). Do not use spreadsheet filters -- instead use filter views if you are using Google Sheets.
2.  Using the **File** menu in Google Sheets, you can access the Revision History of the sheet. This shows all changes made to the sheet, so you can go back in time to see earlier states and the changes made. It is useful to correlate these changes with the audit log to find the effect of a specific change. Note that these times may be local to your computer while the audit log times are in UTC.

If you are using Smartsheet:

1.  Does the column order in Smartsheet still match the column order in your AppSheet app definition? If there is a mismatch, AppSheet may not correctly find the row to make an update.
2.  Do you have a column called `Row ID` in your Smartsheet? Remove this column. AppSheet utilizes a *fake column* called `Row ID` in order to match to specific rows in Smartsheet. If you have such an explicit column, it messes up this comparison and causes updates to be skipped.

## If some rows from the sheet are not visible in the app

If changes made in the app are correctly captured in the spreadsheet but are not shown in the app, the most common reason is the presence of a number of empty rows in the middle of the sheet.

If you are using Google sheets, the presence of custom formatting might prevent AppSheet from reading the entire spreadsheet. One common type of sheet formatting that can cause problems is alternating colors. If you have an **alternating colors** formatting rule in your sheet, you need to ensure that the range of the rule applies to the entire sheet. For instance, if the range of the rule is `A1:F7`, AppSheet will only recognize rows `1` to `7` and columns `A` to `F` as being part of the table. Any row beyond row `7` and any column beyond `F` will be ignored when AppSheet reads the sheet. To fix this problem, you can change the range of the rule to `A:F`, which includes all the rows in the sheet. If new columns are added to the sheet, you will need to modify the rule accordingly to include the new column in the formatting rule.

If you are using Excel and the worksheet has nested tables, only the first nested table is read by AppSheet.

If your app contains tables that are not used directly in any view (for example, if all views are based on a slice of the table), the server may determine the full table is not needed and only send the rows that are part of the slice. This can affect expressions that lookup data from the full table. If your app uses expressions that require the full table data, you can make sure the full data set is sent to the app by including at least one view based on the full table.
