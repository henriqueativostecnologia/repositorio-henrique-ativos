---
fonte: https://support.google.com/docs/answer/3093296?hl=en
baixado: 2026-11-10
---

# ISNUMBER

Checks whether a value is a number.

### Sample Usage

`ISNUMBER(A2)`

`ISNUMBER(4)`

### Syntax

`ISNUMBER(value)`

- `value` - The value to be verified as a number.

  \*`ISNUMBER` returns `TRUE` if this is a number or a reference to a cell containing a numeric value and `FALSE` otherwise.

### Notes

- This function is most often used in conjunction with `IF` in conditional statements.

- Note that supplying a number enclosed in a string (e.g. `ISNUMBER("123")`) will cause this function to return `FALSE`.

### See Also

[`ISTEXT`](https://support.google.com/docs/answer/3093297): Checks whether a value is text.

[`ISREF`](https://support.google.com/docs/answer/3093354): Checks whether a value is a valid cell reference.

[`ISODD`](https://support.google.com/docs/answer/3093491): Checks whether the provided value is odd.

[`ISNONTEXT`](https://support.google.com/docs/answer/3093295): Checks whether a value is non-textual.

[`ISNA`](https://support.google.com/docs/answer/3093293): Checks whether a value is the error \`#N/A\`.

[`ISLOGICAL`](https://support.google.com/docs/answer/3093351): Checks whether a value is \`TRUE\` or \`FALSE\`.

[`ISEVEN`](https://support.google.com/docs/answer/3093419): Checks whether the provided value is even.

[`ISERROR`](https://support.google.com/docs/answer/3093349): Checks whether a value is an error.

[`ISERR`](https://support.google.com/docs/answer/3093348): Checks whether a value is an error other than \`#N/A\`.

[`ISBLANK`](https://support.google.com/docs/answer/3093290): Checks whether the referenced cell is empty.

[`IF`](https://support.google.com/docs/answer/3093364): Returns one value if a logical expression is \`TRUE\` and another if it is \`FALSE\`.

### Examples

Embedded content: https://docs.google.com/spreadsheet/pub?key=0As3tAuweYU9QdEFTQVJXTmRvTC0zVmhGM2dTNUpLNmc&output=html
