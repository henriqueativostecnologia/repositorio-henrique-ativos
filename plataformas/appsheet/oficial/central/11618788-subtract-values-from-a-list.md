---
fonte: https://support.google.com/appsheet/answer/11618788?hl=en
baixado: 2026-11-10
---

# Subtract values from a list

The list-subtract operator (`-`) will produce a new list with the values of the left-side list that are not present in the right-side list. The values of the resulting list will be in the order they occurred in the original left-side list.

Duplicate result entries will be omitted.

- `({ 1, 2, 3 } - LIST(2, 3, 4))` produces a list of one `Number` value: `1`. See also: [`LIST()`](https://support.google.com/appsheet/answer/10107339)

&nbsp;

- `({ "Bob", "Mary", "Bob", "Alice" } - { "Alice" })` produces a list of `Text` values: `Bob`, `Mary`. In addition to the requested removal of `Alice`, note the duplicate occurrence of `Bob` was also omitted from the result.

&nbsp;

- `({ "Bob", "Mary", "Bob", "Alice" } - LIST())` produces a list of `Text` values: `Bob`, `Mary`, `Alice`. Note that the duplicate occurrence of `Bob` was omitted from the result. Equivalent to `UNIQUE({ "Bob", "Mary", "Bob", "Alice" })`. See also: [`UNIQUE()`](https://support.google.com/appsheet/answer/10107368)

&nbsp;

- `({ "Bob", "Mary", "Bob", "Alice" } - { "Bob" })` produces a list of *Text* values: `Mary`, `Alice`. Note that although `Bob` only occurs once in the right-side list, both (all) occurrences of `Bob` from the left-side list are removed in the result.

## See also

[Combine lists](https://support.google.com/appsheet/answer/11617679)

[List expressions](https://support.google.com/appsheet/answer/10107669)

[`INTERSECT()`](https://support.google.com/appsheet/answer/10107963)

[`UNIQUE()`](https://support.google.com/appsheet/answer/10107368)
