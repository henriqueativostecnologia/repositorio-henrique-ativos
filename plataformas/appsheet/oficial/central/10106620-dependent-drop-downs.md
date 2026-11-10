---
fonte: https://support.google.com/appsheet/answer/10106620?hl=en
baixado: 2026-11-10
---

# Dependent drop-downs

Dependent drop-downs allow you to limit the values displayed in one drop-down based on the value selected in another drop-down. For example, this [Lead Tracking app template](https://www.appsheet.com/samples/An-app-to-add-and-update-sales-leads?appGuidString=2f43eb0a-1dbf-417f-9e2d-ccb8b9600d02) asks for the **Lead Region** (America, Asia, Europe) and then for a **Country** within that region.

This actually requires relatively complex logic, but AppSheet tries to make it simple. Dependent drop-downs are driven by a separate lookup table.

In the sample, there is a separate `Regions` lookup table with two columns: `Region` and `Country`. This acts as the lookup table for allowed combinations of regions and countries. 

The Lead Region column has a regular [`Valid_If`](https://support.google.com/appsheet/answer/10107949)` `constraint: `Regions[Region].` Therefore, when a new entry is being added, the input for this column shows three choices: `America`, `Asia`, and `Europe`.

Likewise, the `Country` column also specifies a similar `Valid_If` constraint: `Regions[Country].` However, because it follows the `Lead Region `column and because both specify columns from the same lookup table `Regions`, AppSheet recognizes the intent and implements a dependent drop-down. 

Internally, AppSheet creates an expression to capture the allowed set of values for the `Country` column. The expression must say (in English):

- Look at the `Regions` table
- Filter the rows to make sure that the `Region` column of the table matches the value in the `Lead Region` column of the row being edited in the form
- Now extract the `Country` column from those filtered rows
- Eliminate any duplicates --- these are the allowed countries
- Recompute this list each time the `Lead Region` is changed

Strictly for an expression expert, here is the full underlying AppSheet expression: `IN( [_THIS], SELECT(Regions[Country], [_THISROW].[Lead Region] = [Region]))`

While most app creators will never need to express something this complicated, you could in fact provide this expression as a `Valid_If` constraint. It is useful to know for advanced use cases. For example, instead of using an equality condition, an app creator could use inequality or richer expressions to build very expressive dynamic drop-downs.

## Disable dependent drop-downs

When the AppSheet platform finds several columns that have `Valid_If` constraints from the same lookup table, it assumes that the desired behavior is to have dependent drop-downs. Occasionally, this may not be what you wanted.

In these cases, provide an explicit [`SELECT()`](https://support.google.com/appsheet/answer/10108207) expression instead of just providing a column set expression. In other words, instead of `Regions[Region]`, use `SELECT(Regions[Region], true)`.
