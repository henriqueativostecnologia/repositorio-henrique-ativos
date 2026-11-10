---
fonte: https://support.google.com/appsheet/answer/10107665?hl=en
baixado: 2026-11-10
---

# Drop-down from Valid_If

AppSheet displays a drop-down for fields having a [`Valid_If`](https://support.google.com/appsheet/answer/10107949) constraint that yields a list of values.

To check form input validity without creating a drop-down, see [Check form input validity (Valid_If)](https://support.google.com/appsheet/answer/10107949).

The `Valid_If` expression can be:

**1. A list of constant values**

For example: `{100, 200, 300}` 

Whenever a list of allowed values is provided, it is actually a syntactic shorthand for an expression that uses the `IN()` function. For example, `{100, 200, 300}` is the same as `IN([_THIS], {100, 200, 300})`.

**2. A list of values from a column in another table**

For example: `LookupTable[ColumnC]`

Where `LookupTable` is the name of the table containing the drop-down values, and `ColumnC` is the name of the column containing the drop-down values.

This is particularly useful if the list of allowed values can change while the app is being used.

**3. A list of values from a column in another table where the rows in that table are filtered**

For example: `SELECT(LookupTable[ColumnC], [ReportDate] > Today() - 7)`* *

Where `LookupTable` is the name of the table containing the dropdown values, and `ColumnC` is the name of the column containing the dropdown values. `[ReportDate] > Today() - 7` is an expression which filters the rows in the table to those where `ReportDate` is within the last week. The resulting values in `ColumnC` of `LookupTable` become the allowed list of valid values.

**4. A sorted list of values from a column in another table**

For example: `SORT(LookupTable[ColumnC])`

Where `LookupTable` is the name of the table containing the dropdown values, and `ColumnC` is the name of the column containing the dropdown values.

The list of values is sorted in ascending order. If it should be in descending order instead, use `SORT(LookupTable[ColumnC], true)`.

## Valid_If drop-downs on Ref columns

`Valid_If` can also be used to modify the drop-down of a `Ref` column (to filter the available options, for example), but there are some [additional considerations](https://support.google.com/appsheet/answer/10107321) to be aware of.
