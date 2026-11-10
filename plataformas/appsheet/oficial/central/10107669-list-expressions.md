---
fonte: https://support.google.com/appsheet/answer/10107669?hl=en
baixado: 2026-11-10
---

# List expressions

Use and produce lists of values

A **list** is a collection of zero or more values, each of the same [data type](https://support.google.com/appsheet/answer/10106435), such as a list of numbers, a list of names, a list of email addresses, or a list of rows

A **list expression** is an [expression](https://support.google.com/appsheet/answer/10104642) that produces a list, or an expression that uses one or more lists to produce a result of any type.

Lists may be constructed in a variety of ways:

- From [raw values](https://support.google.com/appsheet/answer/11617176).
- From [expressions](https://support.google.com/appsheet/answer/11617477).
- From existing [values in the column of a table](https://support.google.com/appsheet/answer/11618688).
- From [expressions](https://support.google.com/appsheet/answer/11617175).
- By [dereferencing a list](https://support.google.com/appsheet/answer/11618586) of `Ref` values.
- By [list addition](https://support.google.com/appsheet/answer/11617679), to get all items in two lists.
- By [list subtraction](https://support.google.com/appsheet/answer/11618788), to get items unique to only one of two lists.

The value of a column of type `List` or `EnumList` is already a list, and may be used directly anywhere a list is allowed within an expression.

- `[Vacation Dates]` gives the list of vacation dates from with the current row, e.g. in an `Employees` table.
- `[Notification Emails]` gives the list of notification email addresses from the current row, e.g. in an `Events` table.
- `[Related Order Details]` gives the list of `Order Details` rows related to the current row, e.g in an `Orders` table.

**New to expressions?** See also [Expressions: The Essentials](https://support.google.com/appsheet/answer/10104642).

## Use lists in functions

A variety of functions accept lists as input:

- [`ANY()`](https://support.google.com/appsheet/answer/10107399) - One arbitrary item of a list.
- [`AVERAGE()`](https://support.google.com/appsheet/answer/10107675) - Arithmetic average of list of numeric values.
- [`COUNT()`](https://support.google.com/appsheet/answer/10107676) - Count of list items.
- [`IN()`](https://support.google.com/appsheet/answer/10107681) - Is item in a list?
- [`INDEX()`](https://support.google.com/appsheet/answer/10107336) - One specific item of a list.
- [`INTERSECT()`](https://support.google.com/appsheet/answer/10107963) - List of items common to two lists.
- [`ISBLANK()`](https://support.google.com/appsheet/answer/10107337) - Does the list have no items?
- [`ISNOTBLANK()`](https://support.google.com/appsheet/answer/10107964) - Does the list have any items?
- [`MAX()`](https://support.google.com/appsheet/answer/10107969) - Highest of a list of numeric or temporal values.
- [`MIN()`](https://support.google.com/appsheet/answer/10107972) - Lowest  of a list of numeric or temporal values.
- [`ORDERBY()`](https://support.google.com/appsheet/answer/10107362) - List of rows in custom order.
- [`SELECT()`](https://support.google.com/appsheet/answer/10108207)` `- List of column values from select rows.
- [`SORT()`](https://support.google.com/appsheet/answer/10107698) - List of items in order.
- [`STDEVP()`](https://support.google.com/appsheet/answer/10107930) - Arithmetic [standard deviation](https://en.wikipedia.org/wiki/Standard_deviation) of a list of numeric values.
- [`SUM()`](https://support.google.com/appsheet/answer/10107699) - Arithmetic sum of a list of numeric values.
- [`TOP()`](https://support.google.com/appsheet/answer/10107704) - List of initial items of list.
- [`UNIQUE()`](https://support.google.com/appsheet/answer/10107368) - List of items with duplicates removed.

## Use lists to show and hide columns

A column's [`Show?`](https://support.google.com/appsheet/answer/10108121) expression may be used to conditionally show or hide a column from the user. The `Show?` expression must produce a `Yes/No` result, not a list, but lists are commonly used within `Show?` expressions.

- `IN(USEREMAIL(), SELECT(Users[Email], ("Admin" = [Role])))`  shows the column only for users whose email (`USEREMAIL()`) is in the list of admin user emails (`SELECT(...)`). See also: [`IN()`](https://support.google.com/appsheet/answer/10107681), [`SELECT()`](https://support.google.com/appsheet/answer/10108207), [`USEREMAIL()`](https://support.google.com/appsheet/answer/10108210)

&nbsp;

- `IN(CONTEXT("ViewType"), { "deck", "table" })` shows the column only if the current view type (`CONTEXT(...)`) in the list of view types (`{...}`). See also: [`CONTEXT()`](https://support.google.com/appsheet/answer/10107885), [`IN()`](https://support.google.com/appsheet/answer/10107681)

## Use lists to show and hide views

A view's `Show if` expression may be used to conditionally show or hide a view in the main menu or navigation bar. The `Show if` expression must produce a `Yes/No` result, not a list, but lists are commonly used within `Show if `expressions.

- `IN(USEREMAIL(), SELECT(Users[Email], ("Admin" = [Role])))` shows the view only for users whose email (`USEREMAIL()`) is in the list of admin user emails (`SELECT(...)`). See also: [`IN()`](https://support.google.com/appsheet/answer/10107681), [`SELECT()`](https://support.google.com/appsheet/answer/10108207), [`USEREMAIL()`](https://support.google.com/appsheet/answer/10108210)

## Use lists to suggest column values

A column's [suggested values](https://support.google.com/appsheet/answer/10107397) expression may be used to suggest values when the user goes to make a change to the column. The suggested values expression must produce a list with elements of a compatible type, the values of which are then presented in a drop-down from which the user may choose.

- `Customers[Name]` produces a list of existing customer names, allowing the user to select from the list. Note that the list will be unsorted; to provide a sorted list, use `SORT(Customers[Name])`. See also: [`SORT()`](https://support.google.com/appsheet/answer/10108286)

&nbsp;

- `LIST(TODAY(), (TODAY() + 1), (TODAY() + 2)` produces a list of the dates for today, tomorrow, and the day after. See also: [`LIST()`](https://support.google.com/appsheet/answer/10107339), [`TODAY()`](https://support.google.com/appsheet/answer/10108286)

## Use lists to validate column values

The [`Valid If`](https://support.google.com/appsheet/answer/10107949)` `expression may be used to validate a column value. If the `Valid If` expression produces a list result, the values in the list are considered the only valid values for the column. When the user attempts to change the column's value, the values of the list are presented in a [drop-down menu](https://support.google.com/appsheet/answer/10107665) for the user to choose from.

- `Customers[Name]` produces a list of existing customer names, allowing the user to select from the list. Note that the list will be unsorted; to provide a sorted list, use `SORT(Customers[Name])`. See also: [`SORT()`](https://support.google.com/appsheet/answer/10107698)

&nbsp;

- `{ "Ordered", "Prepared", "Shipped", "Delivered" }` produces a fixed list of order status values from which the user may choose. Note that  the defined values of an *Enum* column could also be used to offer the same list of fixed options.

`Valid If` is commonly used to prevent duplicate values from occurring within a table. For instance, to ensure the current column value is the only occurrence in the entire `Customer Name` column of the `Customers` table:

    ISBLANK(
      FILTER(
        "Customers",
        ([_THIS] = [Customer Name])
      )
      - LIST([_THISROW])
    )
