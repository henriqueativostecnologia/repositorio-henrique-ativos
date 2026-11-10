---
fonte: https://support.google.com/docs/answer/3267036?hl=en
baixado: 2026-11-10
---

# ARRAY_CONSTRAIN

Constrains an array result to a specified size.

### Sample Usage

`ARRAY_CONSTRAIN(A1:C10, 2, 3)`

`ARRAY_CONSTRAIN(SORT(A1:F100, 1, TRUE), 10, 6)`

### Syntax

`ARRAY_CONSTRAIN(input_range, num_rows, num_cols)`

- `input_range` - The range to constrain.
- `num_rows` - The number of rows the result should contain.
- `num_cols` - The number of columns the result should contain

### Notes

- Generally used in combination with other functions that return an array result when a fewer number of rows or columns are desired.

### See Also

[`ARRAYFORMULA`](https://support.google.com/docs/answer/3093275): Enables the display of values returned from an array formula into multiple rows and/or columns and the use of non-array functions with arrays.
