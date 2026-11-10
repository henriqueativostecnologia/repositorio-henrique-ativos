---
fonte: https://support.google.com/appsheet/answer/10107945?hl=en
baixado: 2026-11-10
---

# Column value expressions

Write an expression to get a value from a specific column and row

Column value expressions return the value of a specific column in a row. The row itself does not need to be specified; it's usually implicit in the context of the expression.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Expression**                                                                | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `[Column]`                                                                    | Value of a column in the current table.                                       |
|                                                                               |                                                                               |
|                                                                               | For example:                                                                  |
|                                                                               |                                                                               |
|                                                                               | -   In a [virtual                                                             |
|                                                                               |     column](https://support.google.com/appsheet/answer/10106758):             |
|                                                                               |     `CONCATENATE([FirstName], " ", [LastName])`                               |
|                                                                               | -   In a [slice filter                                                        |
|                                                                               |     condition](https://support.google.com/appsheet/answer/10106308):          |
|                                                                               |     `[Status] = "Complete"`                                                   |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `Table[Column]`                                                               | All values in a column of a table.                                            |
|                                                                               |                                                                               |
|                                                                               | For example: `IN("Complete", Order[Status])`                                  |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
|     [RefColumn].[Column]                                                      | Value of the column `Column` in the row referenced by `RefColumn`.            |
|                                                                               | `RefColumn` must be of type                                                   |
|                                                                               | [`Ref`](https://support.google.com/appsheet/answer/10106510). See             |
|                                                                               | [Dereference                                                                  |
|                                                                               | expressions](https://support.google.com/appsheet/answer/10107396).            |
|                                                                               |                                                                               |
|                                                                               | For example: `[Order ID].[Status] = "Complete"`                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `[ListRef][Column]`                                                           | All values of the column `Column` in the rows referenced by `ListRef`.        |
|                                                                               | `ListRef` must be of type `List`, with subtype `Ref`.                         |
|                                                                               |                                                                               |
|                                                                               | For example: `[Related Orders][Status]`                                       |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `[_THIS]`                                                                     | Value of the current column of the current row. Most often used in a [column  |
|                                                                               | constraint](https://support.google.com/appsheet/answer/10107948)              |
|                                                                               | ([`Editable if`](https://support.google.com/appsheet/answer/10107954),        |
|                                                                               |  [`Required if`](https://support.google.com/appsheet/answer/10106535),        |
|                                                                               | [`Show if`](https://support.google.com/appsheet/answer/10106628), or          |
|                                                                               | [`Valid if`](https://support.google.com/appsheet/answer/10107949)).           |
|                                                                               |                                                                               |
|                                                                               | For example:                                                                  |
|                                                                               |                                                                               |
|                                                                               | `AND((LEN([_THIS]) > 3), CONTAINS([_THIS], "@"))` returns `TRUE` if the       |
|                                                                               | current column value (such as with `Valid if`) is at least three characters   |
|                                                                               | long and contains at least one `@` symbol.                                    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `[_THISROW].[Column]`                                                         | Value of a column in the current table when the context is set to a different |
|                                                                               | table in the expression. If you just specify `[_THISROW]` (and omit the       |
|                                                                               | `[Column]`), the value of the                                                 |
|                                                                               | [key](https://support.google.com/appsheet/answer/10106672) column is          |
|                                                                               | returned.                                                                     |
|                                                                               |                                                                               |
|                                                                               | For example:                                                                  |
|                                                                               |                                                                               |
|                                                                               | `FILTER("Orders", ([Customer] = [_THISROW].[Customer]))` returns keys to rows |
|                                                                               | in the `Orders` data set in which the `Customers` column value is equal to    |
|                                                                               | the `Customers` column value of the current form (that is, orders for this    |
|                                                                               | customer).                                                                    |
|                                                                               |                                                                               |
|                                                                               | `SELECT(Orders[Order ID], ([Customer] = [_THISROW].[Customer]))` returns      |
|                                                                               | the `Order ID` column values (the row keys) for rows in the `Orders` data set |
|                                                                               | in which the `Customer` column value is equal to the `Customer` column value  |
|                                                                               | of the current form.                                                          |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `[_THISROW-`*`n`*`].[Column]`                                                 | Value of a column in a parent or grandparent record.                          |
|                                                                               |                                                                               |
|                                                                               | Can only be used with:                                                        |
|                                                                               |                                                                               |
|                                                                               | -   Embedded templates. See [Access columns in parent and grandparent         |
|                                                                               |     records](https://support.googl                                            |
|                                                                               | e.com/appsheet/answer/11541779#access-columns-in-parent-grandparent-records). |
|                                                                               |                                                                               |
|                                                                               | -   Nested `SELECT()` functions.\                                             |
|                                                                               |     \                                                                         |
|                                                                               |     For example, if you specify the following expression for a virtual column |
|                                                                               |     in the `TableRoot` table:\                                                |
|                                                                               |     \                                                                         |
|                                                                               |     `SEL                                                                      |
|                                                                               | ECT(Table1[Column], ANY(SELECT(Table2[Column], ANY(SELECT(Table3[Column])))`\ |
|                                                                               |     \                                                                         |
|                                                                               |     Then:                                                                     |
|                                                                               |                                                                               |
|                                                                               |     -   `[Column]` references `Table3` (innermost scope)                      |
|                                                                               |     -   `[_THISROW].[Column]` references `TableRoot` (outermost scope)        |
|                                                                               |     -   `[_THISROW - 1].[Column]` references `Table2` (*`n`* scopes from the  |
|                                                                               |         inner most scope)                                                     |
|                                                                               |     -   `[_THISROW - 2].[Column]` references `Table1`.                        |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `[_THISROW_AFTER].[COLUMN]`                                                   | Value of a column just after it is updated within the context of a data       |
|                                                                               | change.                                                                       |
|                                                                               |                                                                               |
|                                                                               | **Note**: Similar to `[_THIS].[COLUMN]`. Use `_THISROW_AFTER` if you want to  |
|                                                                               | use the value as it was after the change was made, but before any changes     |
|                                                                               | that were made during a bot execution.                                        |
|                                                                               |                                                                               |
|                                                                               | The After value contains all field values obtained from the sheet or database |
|                                                                               | record after it is applied, and includes:                                     |
|                                                                               |                                                                               |
|                                                                               | -   All virtual column values. The virtual column values are recomputed when  |
|                                                                               |     the After value is retrieved. This ensures that the virtual column values |
|                                                                               |     reflect the most current field values.                                    |
|                                                                               | -   Field values that are computed by Google Sheets, Microsoft Excel, or      |
|                                                                               |     SmartSheet worksheet formulas. This allows you to display or reference    |
|                                                                               |     the field values that were computed by these worksheet formulas.          |
|                                                                               |                                                                               |
|                                                                               | For full details, see [Access column values before and after an               |
|                                                                               | update](https://support.google.com/appsheet/answer/11547057).                 |
|                                                                               |                                                                               |
|                                                                               | For example, to display the after value of the `Priority` column in your      |
|                                                                               | template.                                                                     |
|                                                                               |                                                                               |
|                                                                               |     The new value of Priority is <<[_THISROW_AFTER].[Priority]>>              |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `[_THISROW_BEFORE].[COLUMN]`                                                  | Value of a column just before it is updated within the context of a data      |
|                                                                               | change.                                                                       |
|                                                                               |                                                                               |
|                                                                               | The Before value contains all field values obtained from the sheet or         |
|                                                                               | database record before it is applied, and includes all virtual column values. |
|                                                                               | The virtual column values are recomputed when the Before value is retrieved.  |
|                                                                               | This ensures that the virtual column values reflect the most current field    |
|                                                                               | values.                                                                       |
|                                                                               |                                                                               |
|                                                                               | For full details, see [Access column values before and after an               |
|                                                                               | update](https://support.google.com/appsheet/answer/11547057).                 |
|                                                                               |                                                                               |
|                                                                               | For example, to display the before value of the `Priority` column in your     |
|                                                                               | template:                                                                     |
|                                                                               |                                                                               |
|                                                                               |                                                                               |
|                                                                               |    The old value of the Priority columns was <<[_THISROW_BEFORE].[Priority]>> |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
