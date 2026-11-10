---
fonte: https://support.google.com/docs/answer/15637642?hl=en
baixado: 2026-11-10
---

# Use table references in Google Sheets

To refer to a table or parts of it in a formula, you can use table references. You need to provide a table name and each column header when you convert your data to a table. You can use these names to reference cells in the table.

For example, instead of explicit cell references: `=Sum(C2:C7)`, you can use table references: `=SUM(DeptSales[Sales Amount])`.

When you use a name to reference table elements, the references update when you add or remove data from the table.

## Syntax & sample usage

[Make a copy](https://www.google.com/url?q=https://docs.google.com/spreadsheets/u/1/d/11b0Yjp85rorHSdSpmV7fDHHmeedTrWR6eoJEpe1vlkA/copy&sa=D&source=docs&ust=1731537277866355&usg=AOvVaw1ZdkSOAlU0bMsWU7xFwWYN)

**Tip:** Each example is in its own tab.

### Syntax

You can use table references to refer to:

- **A Table column:** `Table1[Column 1]`
  - Across single columns: `Table1[[#ALL],[Column 1]]`
  - Across multiple columns simultaneously: `Table1[[#ALL],[Column 1]:[Column 3]]`
- **Full table columns with column headers, data, and footers:** `Table1[#ALL]`
- **Table headers:** `Table1[#HEADERS]`
- **Table footers:** `Table1[#TOTALS]`
- **Table data and headers:** `Table1[[#HEADERS],[#DATA]]`
- **Table data and footers without headers:** `Table1[[#DATA],[#TOTALS]]`
- **Table data without headers and footers:** `Table1` or `Table1[#DATA]`

**Tip:** \#This Row currently is not supported

### Sample usage

Use table references in a formula:

- **SUM:** `SUM(Table1[Column1])`
- **IMPORTRANGE:** `IMPORTRANGE("https://docs.google.com/spreadsheets/d/abcd123abcd123", "DeptSales[Sales Amount]")`

Use table references with chip extraction syntax: `IF(Table1[Column 1]="","",Table1[Column 1].[file name])`
[Learn more about extracting data from smart chips in your Google Sheets](https://support.google.com/docs/answer/13524011).

#### Get to know more details & best practices

- **Always use tables:** If you have structured data, convert it into a table. This unlocks the power of table references and many other table features.
  - **To convert data into a table:** At the top, in the menu bar, click **Format** and then **Convert to table**.
- **Create meaningful table names:** To make your formulas clear, give descriptive names to your tables.
  - Table names must follow certain rules and format requirements. [Learn how to create table names in Google Sheets](https://support.google.com/docs/answer/14239833).
  - In formulas, spaces are replaced with underscores. For example, `Sales_Tracker[Sales Amount]`.
- **Turn on suggestions:** To help you complete formulas with the relevant functions, turn on autocomplete, formula corrections, and formula suggestions.
  1.  At the top of the sheet, in the menu bar, click **Tools** and then **Suggestion controls**.

  2.  Select all of the following:

      - **Enable autocomplete**
      - **Enable formula corrections**
      - **Enable formula suggestions**

      [Learn more about formula corrections or suggestions](https://support.google.com/docs/answer/46977).
- **Use ARRAYFORMULA when applicable:** To retrieve the values of an entire table or a range, use ARRAYFORMULA:
  - `ARRAYFORMULA(Table1)`
  - `ARRAYFORMULA(Table1[Column1])`
- **Follow table reference syntax:**
  - Use brackets around specifiers, such as table names and column names.
  - To improve readability, use space characters in formulas. For example, `=SUM( Table1[ [#ALL],[Column 1]:[Column 2] ] )`

#### Learn about limitations

These features don’t currently support the use of table references when you select a range:

- Conditional formatting
- Charts
- Pivot tables

## Related resources

- [Learn how to use tables in Google Sheets](https://support.google.com/docs/answer/14239833)
- [Learn about IMPORTRANGE](https://support.google.com/docs/answer/3093340)
- [Learn about ARRAYFORMULA](https://support.google.com/docs/answer/3093275)
