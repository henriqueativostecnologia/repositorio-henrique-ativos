---
fonte: https://support.google.com/appsheet/answer/11575067?hl=en
baixado: 2026-11-10
---

# Use Microsoft Excel templates

Customize content using Microsoft Excel templates as described in the following sections:

- [Customize content using a Microsoft Excel template](#customize-content)
- [View the template](#view-template)
- [Edit the template](#edit-template)
- [Build the Microsoft Excel template](#build-template)

See also [Use templates in a bot](https://support.google.com/appsheet/answer/11539957).

## Customize content using a Microsoft Excel template

When configuring a [Send an email](https://support.google.com/appsheet/answer/11447614), [Call a webhook](https://support.google.com/appsheet/answer/11511244), or [Create a new file](https://support.google.com/appsheet/answer/11512511) task, customize content using a Microsoft Excel template by performing one of the following tasks:

- Create a **XLSX** template, as described in [Create a template](https://support.google.com/appsheet/answer/11539957#create-template).

- [Manually create a Microsoft Excel template](#build-template) in your cloud file system and use it, as described in [Use an existing template](https://support.google.com/appsheet/answer/11539957#use-existing-template).

For information about customizing the template, see [Customize content using templates](https://support.google.com/appsheet/answer/11539957#customize-content) and the tips provided below.

## View the template

After creating or selecting the template, click **View** adjacent to the template property to view the template.

**Note**: We do not recommend that you edit the template in this view due to the built-in limitations in the way Microsoft Excel files can be opened and edited from the web.

## Edit the template

To edit the template, open the Microsoft Excel template from your data source.

## Build the Microsoft Excel template

AppSheet supports only simple Microsoft Excel templates.

The **first row** in the Excel template can contain only column header values.

The **second row** in the Excel template can contain only a Start expression, one or more cell data values, and an End expression, as follows:

- The left-most cell contains a **Start** expression immediately followed by a data value or Microsoft Excel worksheet formula.
- Intermediate cells contain data values or Microsoft Excel worksheet formulas.
- The rightmost cell contains a data value or Microsoft Excel worksheet formula immediately followed by an **End** expression.

The Start expression retrieves a set of rows from a table you specify. Each retrieved table row populates a row in the resulting Excel file.

In the following example, the Start expression retrieves rows from the Customer table. The resulting Excel file contains one row for each customer who is 21 years of age or older.

Row in spreadsheet with Start expression that retrieves rows from the Customer table.

### Use Excel worksheet formulas

Your template can include Excel worksheet formulas. In the following template, the `Total` column contains a worksheet formula which multiplies `Price` and `Qty`.

    =B2*C2

### Format cells

You can apply Excel formatting to the cells of the template. For example, the `Price` cell could be formatted as a `Currency` value.

### Use multi-worksheet workbooks

Your Excel workbook template can contain one or more worksheets each of which is a template. The resulting `.xlsx` file contains each of these worksheets.

### Limitations

1.  Excel tables are not supported. Templates must be simple worksheets.
2.  Excel pivot tables are not supported.
3.  Nested tables cannot be displayed in the same Excel worksheet. For example, you cannot display each `Order` record followed its child `Order Detail` records.

### Troubleshoot

You may see the following Excel error message when you attempt to open the resulting Excel `.xlsx` file.

    Excel cannot open the file <filename>.xlsx because the file format or file extension is not valid. Verify that the file has not been corrupted and that the file extension matches the format of the file.

This error can occur if you use a Google Docs template file rather than a Microsoft Excel template file. If you inadvertently use a Google Docs template file, the output is an HTML file that may look like an Excel worksheet but it will not be a valid Excel `.xlsx `file.
