---
fonte: https://support.google.com/appsheet/answer/11581808?hl=en
baixado: 2026-11-10
---

# STARTSWITH()

Does text begin with fragment?

Returns a `Yes/No` value as follows:

- `TRUE` if the text fragment is found at the beginning of the search value.
- `FALSE` if the text fragment is not found at the beginning of the search value.

**Note**: The search is case-insensitive: upper- and lower-case letters are equivalent.

## Sample usage

`STARTSWITH("aBc", "a")` returns `TRUE`

`STARTSWITH("aBc", "bc")` returns `FALSE` (`Bc` occurs, but not at the beginning)

`STARTSWITH("aBc", "D")` returns `FALSE` (`D` does not occur)

`STARTSWITH("I'm bored!", "Red")` returns `FALSE` (`red` occurs, but not at the beginning)

`STARTSWITH([Email], "noreply@")` answers the question: does the `Email` contain an address to which messages shouldn't be sent? Functionally equivalent to but more efficient than `("noreply" = ANY(SPLIT([Email], "@")))`. See also: [`ANY()`](https://support.google.com/appsheet/answer/10107399), [`SPLIT()`](https://support.google.com/appsheet/answer/10107984)

## Syntax

`STARTSWITH(`*`text-to-search`*`, `*`search-for`*`)`

- *`text-to-search`* - Text to be searched.

- *`search-for`* - Text string to search for in *`text-to-search`*.

## See also

[`ENDSWITH()`](https://support.google.com/appsheet/answer/11582090)

[`FIND()`](https://support.google.com/appsheet/answer/10108197)

[`IN()`](https://support.google.com/appsheet/answer/10107681)

[`LEFT()`](https://support.google.com/appsheet/answer/10106634)

[`RIGHT()`](https://support.google.com/appsheet/answer/10107983)
