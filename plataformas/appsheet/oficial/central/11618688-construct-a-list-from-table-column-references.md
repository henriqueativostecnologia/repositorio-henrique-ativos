---
fonte: https://support.google.com/appsheet/answer/11618688?hl=en
baixado: 2026-11-10
---

# Construct a list from table-column references

Referencing a table and column together (a **table-column reference**) constructs a list of all values in that column of that table. Note that if the column itself contains duplicate values, so will the list.

- `Fruits[Name]` produces a list of all `Name` column values from the `Fruits` table. This is equivalent to `SELECT(Fruits[name], TRUE, FALSE)`. See also: [`SELECT()`](https://support.google.com/appsheet/answer/10108207)

&nbsp;

- `Orders[Customer]` produces a list of all `Customer` column values from the `Orders` table. Equivalent to `SELECT(Orders[Customer], TRUE, FALSE)`.

&nbsp;

- `Order Details[SKU]` produces a list of all `SKU` column values in the `Order Details` table. Equivalent to `SELECT(Order Details[SKU], TRUE, FALSE)`.

A table-column reference to a column of type `List` or `EnumList` will produce a list of lists. To "flatten" the list-of-lists into a single list composed of the values of the component lists, wrap the table-column reference with [`SPLIT()`](https://support.google.com/appsheet/answer/10107984).

- `SPLIT(Employees[Vacation Dates], ",")` produces a list of all employee vacation dates.

&nbsp;

- `SPLIT(Events[Notification Emails], ",")` produces a list of all notification email addresses.

## See also

[List expressions](https://support.google.com/appsheet/answer/10107669)

[Construct a list using the LIST() function](https://support.google.com/appsheet/answer/11617477)

[Construct a list of values](https://support.google.com/appsheet/answer/11617176)

[Subtract values from a list](https://support.google.com/appsheet/answer/11618788)

[`SELECT()`](https://support.google.com/appsheet/answer/10108207)

[`UNIQUE()`](https://support.google.com/appsheet/answer/10107368)
