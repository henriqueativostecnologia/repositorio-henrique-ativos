---
fonte: https://support.google.com/appsheet/answer/10108126?hl=en
baixado: 2026-11-10
---

# SUBSTITUTE()

Text with replacements

Returns the resulting text with the specified text replaced with new text.

## Sample usage

`SUBSTITUTE("abc", "a", "A")` returns `Abc`

`SUBSTITUTE("+1 212-555-1212", "-", ".")` returns `+1 212.555.1212`

`SUBSTITUTE("Hello, {}!", "{}", "Bob")` returns `Hello, Bob!`

## Syntax

`SUBSTITUTE(`*`text-to-search`*`, `*`search-for`*`, `*`replace-with`*`)`

- *`text-to-search`* - Any textual type that specifies the text containing occurrences of *`search-for`* to be replaced with *`replace-with`*.

&nbsp;

- *`search-for`* - Any textual type that specifies the text to be replaced where found in *`text-to-search`*.

&nbsp;

- *`replace-with`* - Any textual type that specifies the text to replace each occurrence of *`search-for`* found in *`text-to-search`*.

## See also

[`CONCATENATE()`](https://support.google.com/appsheet/answer/10107400)

[`CONTAINS()`](https://support.google.com/appsheet/answer/10107955)

[`FIND()`](https://support.google.com/appsheet/answer/10108197)

[`INITIALS()`](https://support.google.com/appsheet/answer/10108199)

[`LEFT()`](https://support.google.com/appsheet/answer/10106634)

[`MID()`](https://support.google.com/appsheet/answer/10107345)

[`RIGHT()`](https://support.google.com/appsheet/answer/10107983)

[`TRIM()`](https://support.google.com/appsheet/answer/10107932)
