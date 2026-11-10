---
fonte: https://support.google.com/appsheet/answer/11617477?hl=en
baixado: 2026-11-10
---

# Construct a list using the LIST() function

The [`LIST()`](https://support.google.com/appsheet/answer/10107339) expression constructs a list from any combination of raw values, column values, and expressions. The values in the resulting list will be in the order they were given to the `LIST()` expression.

- `LIST("Apple", "Banana", "Cherry")` produces a list of `Text` values: `Apple`, `Banana`, `Cherry`.

&nbsp;

- `LIST([Mobile Phone], [Office Phone], [Home Phone])` produces a list of phone numbers from three column values of the current row.

&nbsp;

- `LIST(1, (1 + 1), (6 / 2), ROUND(POWER(2, 2)), ROUND(SQRT(25)))` produces a list of `Number` values: `1`, `2`, `3`, `4`, `5`. See also: [`POWER()`](https://support.google.com/appsheet/answer/10106551), [`ROUND()`](https://support.google.com/appsheet/answer/10108206), [`SQRT()`](https://support.google.com/appsheet/answer/10107366)

&nbsp;

- `LIST()` produces an empty list.

## See also

[Expressions: The Essentials](https://support.google.com/appsheet/answer/10104642)

[List expressions](https://support.google.com/appsheet/answer/10107669)

[Construct a list from table-column references](https://support.google.com/appsheet/answer/11618688)

[Construct a list of values](https://support.google.com/appsheet/answer/11617176)

[`LIST()`](https://support.google.com/appsheet/answer/10107339)
