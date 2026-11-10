---
fonte: https://support.google.com/docs/answer/3094286?hl=en
baixado: 2026-11-10
---

# FREQUENCY

Calculates the frequency distribution of a one-column array into specified classes.

### Sample Usage

`FREQUENCY(A2:A40,B2:B5)`

### Syntax

`FREQUENCY(data, classes)`

- `data` - The array or range containing the values to be counted.

- `classes` - The array or range containing the set of classes.

  - `FREQUENCY` returns results in the exact order of the provided bins in this range.

### Notes

- `FREQUENCY` outputs a vertical range one size larger than `classes`. The final value is the number of elements in `data` greater than any of the class boundaries.
- The results are shown based on the order of classes in the formula.

### Examples

Embedded content: https://docs.google.com/spreadsheet/pub?key=0As3tAuweYU9QdDVnRXNXOTFRS016X01mdEV1cFhLWkE&output=html
