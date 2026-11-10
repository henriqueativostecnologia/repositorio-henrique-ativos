---
fonte: https://support.google.com/docs/answer/6270316?hl=en
baixado: 2026-11-10
---

# ISFORMULA

Checks whether a formula is in the referenced cell.

### Sample Usage

`ISFORMULA(A2)`

### Syntax

`ISFORMULA(cell)`

- `cell` - The cell to check for a formula.

  - `ISFORMULA` returns `TRUE` if `cell` is a cell that contains a formula. If `cell` contains a range of cells then `TRUE` will be returned if the first cell in the range contains a formula. All other values will return `FALSE`.

### Notes

- `cell` can refer to a cell, a name associated with a cell, or a range (multiple cells).
- This function is most often used in conjunction with `IF` in conditional statements.

### See Also

[`ISERROR`](https://support.google.com/docs/answer/3093349): Checks whether a value is an error.

[`ISTEXT`](https://support.google.com/docs/answer/3093297): Checks whether a value is text.

[`ISREF`](https://support.google.com/docs/answer/3093354): Checks whether a value is a valid cell reference.

[`ISODD`](https://support.google.com/docs/answer/3093491): Checks whether the provided value is odd.

[`ISNUMBER`](https://support.google.com/docs/answer/3093296): Checks whether a value is a number.

[`ISNONTEXT`](https://support.google.com/docs/answer/3093295): Checks whether a value is non-textual.

[`ISNA`](https://support.google.com/docs/answer/3093293): Checks whether a value is the error \`#N/A\`.

[`ISLOGICAL`](https://support.google.com/docs/answer/3093351): Checks whether a value is \`TRUE\` or \`FALSE\`.

[`ISEVEN`](https://support.google.com/docs/answer/3093419): Checks whether the provided value is even.

[`ISERR`](https://support.google.com/docs/answer/3093348): Checks whether a value is an error other than \`#N/A\`.

[`ISBLANK`](https://support.google.com/docs/answer/3093290): Checks whether the referenced cell is empty.

[`IF`](https://support.google.com/docs/answer/3093364): Returns one value if a logical expression is \`TRUE\` and another if it is \`FALSE\`.

### Examples

Embedded content: https://docs.google.com/spreadsheets/d/1e6n66ld6CsLqAWmBC2NDiIzKlXfjPzusBxznDgxF5yM/pubhtml
