---
fonte: https://support.google.com/appsheet/answer/10107963?hl=en
baixado: 2026-11-10
---

# INTERSECT()

Items common to two lists

Returns a list of items common to two lists.

## Sample usage

`INTERSECT(LIST("Red", "Blue", "Green"), LIST("Orange", "Blue"))` returns a list with one item: `Blue`. See also: [`LIST()`](https://support.google.com/appsheet/answer/10107339)

`INTERSECT(Employees[Name], LIST("Bob"))` returns a list of one item, `Bob`, if that name occurs in the list of employee names. Equivalent to `IFS(IN("Bob", Employees[Name], LIST("Bob")))`. See also: [`IFS()`](https://support.google.com/appsheet/answer/10107912), [`IN()`](https://support.google.com/appsheet/answer/10107681)

`INTERSECT(Employees[Name], Employees[Name])` returns a list of unique names in the `Employees[Name]` column. Equivalent to `UNIQUE(Employees[Name])`. See also: [`UNIQUE()`](https://support.google.com/appsheet/answer/10107368)

## Syntax

`INTERSECT(`*`list1`*`, `*`list2`*`)`

- *`list1`*, *`list2`* - *T*wo lists of comparable types in which to find common elements.

## See also

[`ANY()`](https://support.google.com/appsheet/answer/10107399)

[`COUNT()`](https://support.google.com/appsheet/answer/10107676)

[`IN()`](https://support.google.com/appsheet/answer/10107681)

[`LIST()`](https://support.google.com/appsheet/answer/10107339)

[`MAX()`](https://support.google.com/appsheet/answer/10107969)

[`MIN()`](https://support.google.com/appsheet/answer/10107972)

[`SORT()`](https://support.google.com/appsheet/answer/10107698)

[`UNIQUE()`](https://support.google.com/appsheet/answer/10107368)
