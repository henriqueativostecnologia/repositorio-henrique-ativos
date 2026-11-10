---
fonte: https://support.google.com/appsheet/answer/11513071?hl=en
baixado: 2026-11-10
---

# Troubleshoot CSV Import

Resolve problems with CSV Import

If the CSV Import data action fails, the following tips may help you resolve the problem.

Import only works for applications that [require sign-in](https://support.google.com/appsheet/answer/10104975), and only when the app is running in a browser. It is not supported for public applications.

## EnumList field import fails with "failed Valid_If condition"

You may see the `failed Valid_If condition` error if you import a CSV file containing an `EnumList` field. Though, this issue can occur regardless of whether the `EnumList` field was imported. For details, see [Troubleshoot "failed Valid_If condition" for EnumList fields](https://support.google.com/appsheet/answer/10107949#failed-valid-if-condition).

## The expression is valid but its result type '\<type\>' is not one of the expected types: Text

This error message displays when the expression specified in the **CSV file locale** property of the **Import** action does not yield a text value. Update the expression to return a valid locale identifier.

## Importing records to table: TestCsvImport failed because CSV file locale is missing.

This error message displays when the expression specified in the **CSV file locale** property of the **Import** action yields an empty string rather than a valid locale identifier. Update the expression to return a valid locale identifier.

## Import CSV Failed. CSV file locale 'en-XX' is invalid.

This error message displays when the expression specified in the **CSV file locale** property of the **Import** action yields an invalid locale identifier. Update the expression to return a valid locale identifier.

## Row key field '\<field Name\>' value is missing.

If the CSV file header does not contain the table's key column name, or if the CSV file header does not exactly match the table's key column name, you may see an error such as the following:

`Row key field 'Name' value is missing.`

This happens when the table's key column name cannot be found in the CSV file header.

In the example above, the table's key column name was `Name` but the CSV file header contained `name `which was not capitalized.

## Field '\<field Name\>' cannot be converted to type '\<type\>' using locale '\<locale name\>'.

If the wrong locale is specified for the CSV Import data action, you may see an error such as the following:

`Error: Row having key 'Bob' in table 'TestCsvImport' containing value '25/12/2021' in field 'OrderDate' cannot be converted to type 'Date' using locale 'English (United States)'.`

This happens because the **CSV file locale** you specify for the Import data action determines how field values in the CSV file which are locale sensitive are parsed. For a list of locale sensitive data types see [Locale and Data Format](https://support.google.com/appsheet/answer/11512216#locale-and-data-format).

In the example above, the date field `OrderDate` in the CSV file contained a date value in `English (United Kingdom)` `dd/MM/YYYY` format. The Import data action specified a **CSV file locale** of `English (United States)` so all dates are expected to be in `M/d/yyyy` format. The error occurred because `25` is not a valid month value.

## Only one CSV header column was found

If the wrong locale is specified for the CSV Import data action, you may see the error:

`Failed to get rows due to: Only one CSV header column was found. It has the value 'Name,Date,DateTime,Decimal,Price,Count'. It is possible that the wrong Locale was specified and hence the wrong column delimiter ';' was used. If you are attempting to Import CSV data, please verify that the proper 'CSV file locale' is being specified in the Import data action.`

This happens because the locale you specify for the Import data action determines which CSV delimiter is used to parse the CSV header row. For example, if you specify locale `de-DE` then the expected CSV delimiter is semicolon. If the CSV header row delimiter is actually comma, then the CSV header row will not be parsed correctly and this error will result.

## Timeout occurred or import is taking too long

If your CSV file contains a large number of rows or columns, CSV Import may exceed the 4-minute time limit. The complexity of your app formulas and the number and complexity of your automation processes can also have a large effect on the CSV Import time. See [Choose a CSV file size](https://support.google.com/appsheet/answer/11510988#choose-csv-file-size) for more details.

You can use the Performance Analyzer to better understand CSV Import performance. In the Editor go to **Manage** \> **Monitor** \> **Performance Profile** and click **Launch performance analyzer** to launch the performance analyzer.

Find and expand the ImportCSV record to see where the time is going.

- If your table includes Virtual Fields, check the time required to compute the app formulas for those fields.
- If you have automation processes that are triggered by the CSV Import, check the time required to process them.
