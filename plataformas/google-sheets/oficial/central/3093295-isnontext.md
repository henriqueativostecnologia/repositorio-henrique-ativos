---
fonte: https://support.google.com/docs/answer/3093295?hl=en
baixado: 2026-11-10
---

# ISNONTEXT

Checks whether a value is non-textual.

### Sample Usage

`ISNONTEXT(A2)`

`ISNONTEXT("cat")`

### Syntax

`ISNONTEXT(value)`

- `value` - The text to be checked.

  - `ISNONTEXT` returns `FALSE` if this is a text value or a reference to a cell containing a text value and `TRUE` otherwise.

  - When `value` is a reference to an empty cell, `ISNONTEXT` will return `TRUE`.

  - When `value` is an empty string, `ISNONTEXT` will return `FALSE`, as the empty string is considered text.

### Notes

- Nonprinting characters and whitespace count as text, so when `ISNONTEXT` is called on a cell containing such characters, the function will return `FALSE` even though the cell appears empty.

- Numbers input as text, e.g. `"1234"` count as text, and will cause `ISNONTEXT` to return `FALSE`.

- `ISNONTEXT(value)` is the logical equivalent of `NOT(ISTEXT(value))`

- This function is most often used in conjunction with `IF` in conditional statements.

### See Also

[`ISTEXT`](https://support.google.com/docs/answer/3093297): Checks whether a value is text.

[`ISREF`](https://support.google.com/docs/answer/3093354): Checks whether a value is a valid cell reference.

[`ISODD`](https://support.google.com/docs/answer/3093491): Checks whether the provided value is odd.

[`ISNUMBER`](https://support.google.com/docs/answer/3093296): Checks whether a value is a number.

[`ISNA`](https://support.google.com/docs/answer/3093293): Checks whether a value is the error \`#N/A\`.

[`ISLOGICAL`](https://support.google.com/docs/answer/3093351): Checks whether a value is \`TRUE\` or \`FALSE\`.

[`ISEVEN`](https://support.google.com/docs/answer/3093419): Checks whether the provided value is even.

[`ISERROR`](https://support.google.com/docs/answer/3093349): Checks whether a value is an error.

[`ISERR`](https://support.google.com/docs/answer/3093348): Checks whether a value is an error other than \`#N/A\`.

[`ISBLANK`](https://support.google.com/docs/answer/3093290): Checks whether the referenced cell is empty.

[`IF`](https://support.google.com/docs/answer/3093364): Returns one value if a logical expression is \`TRUE\` and another if it is \`FALSE\`.

### Examples

Embedded content: https://docs.google.com/spreadsheet/pub?key=0As3tAuweYU9QdHdxSmlNMklPYXhpbHdFSjNKTFNpNWc&output=html
