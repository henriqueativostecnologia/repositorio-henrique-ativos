---
fonte: https://support.google.com/docs/answer/3267357?hl=en
baixado: 2026-11-10
---

# PERCENTRANK.EXC

Returns the percentage rank (percentile) from 0 to 1 exclusive of a specified value in a dataset.

### Sample Usage

`PERCENTRANK.EXC(A1:A100, A2, 4)`

`PERCENTRANK.EXC(A1:A100, 10)`

### Syntax

`PERCENTRANK.EXC(data, value, [significant_digits])`

- `data` - The array or range containing the dataset to consider.
- `value` - The value whose percentage rank will be determined.
- `significant_digits` - **\[** OPTIONAL - `3` by default **\]** - The number of significant figures to use in the calculation.

### Notes

- If the `value` does not fall within the `data` given for the function, an estimation will be made to bring up a percentage rank for that value.

### See Also

[`PERCENTRANK`](https://support.google.com/docs/answer/3094095): Returns the percentage rank (percentile) of a specified value in a dataset.

[`PERCENTRANK.INC`](https://support.google.com/docs/answer/3267360): Returns the percentage rank (percentile) from 0 to 1 inclusive of a specified value in a dataset.

[`PERCENTILE`](https://support.google.com/docs/answer/3094093): Returns the value at a given percentile of a dataset.

[`LARGE`](https://support.google.com/docs/answer/3094008): Returns the nth largest element from a data set, where n is user-defined.

[`MIN`](https://support.google.com/docs/answer/3094017): Returns the minimum value in a numeric dataset.

[`MAX`](https://support.google.com/docs/answer/3094013): Returns the maximum value in a numeric dataset.

[`MEDIAN`](https://support.google.com/docs/answer/3094025): Returns the median value in a numeric dataset.
