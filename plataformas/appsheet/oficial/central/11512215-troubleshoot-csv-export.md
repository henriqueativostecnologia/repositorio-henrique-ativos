---
fonte: https://support.google.com/appsheet/answer/11512215?hl=en
baixado: 2026-11-10
---

# Troubleshoot CSV Export

Resolve problems with CSV Export

If the CSV Export data action fails, the following tips may help you resolve the problem.

Export only works for applications that [require sign-in](https://support.google.com/appsheet/answer/10104975), and only when the app is running in a browser. It is not supported for public applications.

## Export fails after about two minutes

There is a 2-minute elapsed time limit on how long CSV Export is allowed to run. Once that time is exceeded, the CSV Export will be cancelled and no CSV file will be produced. We do this to ensure that no single user monopolizes the resources of the system to the detriment of other users.

CSV Export time limit checking is enforced in various places in the code, but primarily when evaluating expressions. As a result, some CSV Exports may exceed the time limit and succeed, some may be cancelled after running more than the time limit, and some may be cancelled promptly when the time limit is reached.

The CSV time limit is more likely to be exceeded if one or more of the following conditions are true.

1.  The table you are exporting from contains a lot of rows be it a Google Sheet, Excel worksheet, or SQL database. This is typically not a problem unless there are a very large number of rows.
2.  There are expensive filters condition expressions being evaluated to decide which rows to export. Sometimes these filter condition expressions can be simplified while yielding the same result.
3.  There are expensive virtual column expressions being used in the table being exported. Expensive virtual column expression computations are one of the primary reasons that the time limit may be exceeded. Sometimes these virtual column expressions can be simplified while yielding the same result.

You can see performance information by opening the app in the Editor, going to **Manage \> Monitor \> Performance Profile**, and clicking **Launch Performance Analyzer**. Look for **`ExportView`** operations. Click the **binoculars** icon to see the performance information.

**Note**: We currently display very little detailed performance information for CSV Export. We hope to remedy this in the future.

When possible, consider partitioning a single CSV Export into two or more smaller CSV Exports.

## Unexpected rows appear in the Exported View when using Search Filter conditions

This can occur when rows in the exported view contain `Number`, `Decimal`, `Price`, `Percent`, or `Ref` field values that are blank. The server expression system may include rows in your view where the field value specified in the **Search Filter** is blank. This is the result of a bug in the way the server expression system compares blank field values. You can often fix this problem by changing the **Blank value comparison mode** setting from **Legacy** to **Consistent**.

For more information about configuring the **Blank value comparison mode** setting, see [Configure the behavior of comparison operators](https://support.google.com/appsheet/answer/11510515#configure-comparison-operators). 

**Note**: If you see bad side effects after changing from Legacy to Consistent mode, you can always revert to Legacy mode.

## The expression is valid but its result type '\<type\>' is not one of the expected types: Text

This error message displays when the expression specified in the **CSV file locale** property of the **Export** action does not yield a text value. Update the expression to return a valid locale identifier.

## Export CSV failed because CSV file locale is missing.

This error message displays when the expression specified in the **CSV file locale** property of the **Export** action yields an empty string rather than a valid locale identifier. Update the expression to return a valid locale identifier.

## Export CSV Failed. CSV file locale 'en-XX' is invalid.

This error message displays when the expression specified in the **CSV file locale** property of the **Export** action yields an invalid locale identifier. Update the expression to return a valid locale identifier.

## Export phone numbers with leading zeros to Excel

If you export `Phone` or `Text` type fields that contain leading zeros, the leading zeros may not be displayed when you open the CSV file in Microsoft Excel. The leading zeros are present in the CSV file. You can verify this by opening the CSV file in Microsoft Notepad. To get the leading zeros to be displayed in Microsoft Excel, use the **Second and more 'surgical' way** described in this [FAQ](https://provider.www.upenn.edu/computing/da/bo/webi/qna/iv_csvLeadingZeros.html).
