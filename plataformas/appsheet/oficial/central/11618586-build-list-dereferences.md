---
fonte: https://support.google.com/appsheet/answer/11618586?hl=en
baixado: 2026-11-10
---

# Build list dereferences

A column value of type `List` or `EnumList` with a base type of `Ref` can be dereferenced to produce a new list of the values from dereferencing each individual reference, an operation called a **list dereference**.

A list dereference is performed by enclosing the `Ref` list column name (such as `Related Orders`) and the column name of the desired column value (such as `Order Date`) each in square brackets (`[` `]`) and placing them adjacent to each other.

For example: 

`[Related Orders][Order Date]`

The result will be a list of `Order Date` column values from the rows identified by the list in the `Related Orders` column value.

**Note**: The result is similar to the following `SELECT()` expression (assuming the referenced table is `Orders` and its key column is `Order ID`):

`SELECT(`
` Orders[Order Date],`
` IN([Order ID], [_THISROW].[Related Orders])`
`)`

## Sort by another column

To gather a list of column values sorted by a different column value, use the [App formula](https://support.google.com/appsheet/answer/10106437) expression of a column to generate a list of [row references](https://support.google.com/appsheet/answer/10106510) in the desired order.

For example, for a column named `Next Two Weeks`, gather the list of rows from the `Events` table with a `Date` within the next 14 days, and order the rows by `Date` from earliest to latest:

    ORDERBY(
      FILTER(
        "Event",
        ([Date] < (TODAY() + 14))
      ),
      [Date]
    )

A list dereference can then be used to get the desired list of column values in that same order:

    [Next Two Weeks][Event Name]

The resulting list of dereferenced values will be in the same order as the original reference list.

See also: [Date and time expressions](https://support.google.com/appsheet/answer/10107326), [`FILTER()`](https://support.google.com/appsheet/answer/10108196), [`ORDERBY()`](https://support.google.com/appsheet/answer/10107362), [`TODAY()`](https://support.google.com/appsheet/answer/10108286)

## See also

[Dereference expressions](https://support.google.com/appsheet/answer/10107396)

[List expressions](https://support.google.com/appsheet/answer/10107669)

[`SELECT()`](https://support.google.com/appsheet/answer/10108207)
