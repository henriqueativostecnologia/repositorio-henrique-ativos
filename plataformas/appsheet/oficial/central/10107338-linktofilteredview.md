---
fonte: https://support.google.com/appsheet/answer/10107338?hl=en
baixado: 2026-11-10
---

# LINKTOFILTEREDVIEW()

Constructed deep link to filtered view

Returns a [deep link](https://support.google.com/appsheet/answer/10106757) (`App` value) to a filtered view to display the rows matched by the filter expression.

## Sample usage

`LINKTOFILTEREDVIEW("Orders", ([Customer ID] = [_THISROW].[ID]))` returns a deep link to the `Orders` view that includes only those rows with a `Customer ID` column value that matches this row's `ID` column value.

`LINKTOFILTEREDVIEW("Customers", TRUE)` returns a deep link to the `Customers` view that includes all rows of the table.

## Syntax

`LINKTOFILTEREDVIEW(`*`view`*`, `*`filter`*`)`

- *`view`* - Any textual type. Must be the name of an existing view.
- *`filter`*  - A valid expression for filtering (as with [`FILTER()`](https://support.google.com/appsheet/answer/10108196)) the table attached to the view named by *`view`*.

## Notes

`LINKTOFILTEREDVIEW()` **cannot** be used to navigate to another app.

## See also

[App column type (deep link)](https://support.google.com/appsheet/answer/10106757)

[`LINKTOAPP()`](https://support.google.com/appsheet/answer/10107914)

[`LINKTOFORM()`](https://support.google.com/appsheet/answer/10106538)

[`LINKTOPARENTVIEW()`](https://support.google.com/appsheet/answer/11621687)

[`LINKTOROW()`](https://support.google.com/appsheet/answer/10106539)

[`LINKTOVIEW()`](https://support.google.com/appsheet/answer/10108105)
