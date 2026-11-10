---
fonte: https://support.google.com/appsheet/answer/11617679?hl=en
baixado: 2026-11-10
---

# Combine lists

The contents of two lists can be combined to construct a new list using the list-add operator (`+`). The items in the resulting list will be in the order they occurred in the original lists. Duplicate entries will be preserved.

- `({1, 2, 3} + LIST(2, 3, 4))` produces a list of `Number` values: `1`, `2`, `3`, `2`, `3`, `4`. See also [`LIST()`](https://support.google.com/appsheet/answer/10107339)*.*
- `(Employees[Office Phone] + Employees[Home Phone])` produces a list of all employee office and home phone numbers.

The list resulting from list addition will adopt the [data type](https://support.google.com/appsheet/answer/10106435) of the left-side list. If the right-side list is of a different data type, this may change how the values taken from it are interpreted.

- `({3} + {3.14})` produces a list of `Number` values from a list of one `Number` value (`3`) and a list of one `Decimal` value (`3.14`).
- `(LIST() + {3.14})` produces a list of one `Text` value from an empty list (`Text` by default) and a list of one `Decimal` value (`3.14`)

## See also

[Construct a list using the LIST() expression](https://support.google.com/appsheet/answer/11617477)

[Construct a list of values](https://support.google.com/appsheet/answer/11617176)

[Subtract values from a list](https://support.google.com/appsheet/answer/11618788)

[`INTERSECT()`](https://support.google.com/appsheet/answer/10107963)

[`LIST()`](https://support.google.com/appsheet/answer/10107339)

[`UNIQUE()`](https://support.google.com/appsheet/answer/10107368)
