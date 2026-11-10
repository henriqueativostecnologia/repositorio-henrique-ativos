---
fonte: https://support.google.com/appsheet/answer/11617176?hl=en
baixado: 2026-11-10
---

# Construct a list of values

A list can be constructed from raw values by enclosing the raw values in curly braces (`{`, `}`). The list must have at least one value. Multiple raw values should be separated by a comma (`,`). All raw values within the list must be of the same [data type](https://support.google.com/appsheet/answer/10106435).

- `{ "Apple", "Banana", "Cherry" }` constructs a list of `Text` values: `Apple`, `Banana`, `Cherry`.
- `{ 1, 2, 3 }` constructs a list of `Number` values: `1`, `2`, `3`.

Within curly braces, expressions are loosely recognized but may be evaluated in unexpected ways or not evaluated at all. Using expressions within curly braces is strongly discouraged! To use a raw value that might be interpreted as an expression, enclose the raw value in double quotes (`"`).

- `{ [Mobile Phone], [Office Phone], [Home Phone] }` produces a list of `Text` values: `[Mobile Phone]` , `[Office Phone]` , `[Home Phone]`. Because the raw values appear to be expressions, the expressions will be checked for validity and may produce errors (e.g., if a column doesn't exist), but these apparent expressions will not be evaluated!
- `{ 1, (1 + 1), (6 / 2), ROUND(POWER(2, 2)), ROUND(SQRT(25)) }`  produces a list of `Number` values: `1`, `1`, `1`, `6`, `2`, `4`, `5`. Note that these expressions are recognized but do not produce the expected results! See also: [`POWER()`](https://support.google.com/appsheet/answer/10106551), [`ROUND()`](https://support.google.com/appsheet/answer/10108206), [`SQRT()`](https://support.google.com/appsheet/answer/10107366)
- `{ "(1 + 1)", "(6 / 2)" }` produces a list of *Text* values: `(1 + 1)`, `(6 / 2)`. Note the apparent expressions are not recognized as expressions within the quotes.

## See also

[List expressions](https://support.google.com/appsheet/answer/10107669)

[Construct a list using the LIST() function](https://support.google.com/appsheet/answer/11617477)

[Construct a list from table-column references](https://support.google.com/appsheet/answer/11618688)

[`LIST()`](https://support.google.com/appsheet/answer/10107339)
