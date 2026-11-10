---
fonte: https://support.google.com/docs/answer/3094095?hl=en
baixado: 2026-11-10
---

# PERCENTRANK

Returns the percentage rank (percentile) of a specified value in a dataset.

### Sample Usage

`PERCENTRANK(A2:A100,A2)`

`PERCENTRANK(A2:A100,1,7)`

### Syntax

`PERCENTRANK(data, value, [significant_digits])`

- `data` - The array or range containing the dataset to consider.
- `value` - The value whose percentage rank will be determined.
- `significant_digits` - **\[** OPTIONAL - `3` by default **\]** - The number of significant figures to use in the calculation.

### Notes

- If `data` does not contain `value` in any cell or element, `PERCENTRANK` will return the `#N/A` error.
- If a number less than or equal to 0 is used for `significant_digits` then this value will be ignored and the default number of significant digits will be used instead.

### See Also

[`PERCENTRANK.INC`](https://support.google.com/docs/answer/3267360): Returns the percentage rank (percentile) from 0 to 1 inclusive of a specified value in a dataset.

[`PERCENTRANK.EXC`](https://support.google.com/docs/answer/3267357): Returns the percentage rank (percentile) from 0 to 1 exclusive of a specified value in a dataset.

[`SMALL`](https://support.google.com/docs/answer/3094050): Returns the nth smallest element from a data set, where n is user-defined.

[`RANK`](https://support.google.com/docs/answer/3094098): Returns the rank of a specified value in a dataset.

[`QUARTILE`](https://support.google.com/docs/answer/3094041): Returns a value nearest to a specified quartile of a dataset.

[`PERCENTILE`](https://support.google.com/docs/answer/3094093): Returns the value at a given percentile of a dataset.

[`MINA`](https://support.google.com/docs/answer/3094018): Returns the minimum numeric value in a dataset.

[`MIN`](https://support.google.com/docs/answer/3094017): Returns the minimum value in a numeric dataset.

[`MEDIAN`](https://support.google.com/docs/answer/3094025): Returns the median value in a numeric dataset.

[`MAXA`](https://support.google.com/docs/answer/3094016): Returns the maximum numeric value in a dataset.

[`MAX`](https://support.google.com/docs/answer/3094013): Returns the maximum value in a numeric dataset.

[`LARGE`](https://support.google.com/docs/answer/3094008): Returns the nth largest element from a data set, where n is user-defined.

[`AVERAGEA`](https://support.google.com/docs/answer/3093617): Returns the numerical average value in a dataset.

[`AVERAGE`](https://support.google.com/docs/answer/3093615): The AVERAGE function returns the numerical average value in a dataset, ignoring text.

### Examples

Embedded content: https://docs.google.com/spreadsheet/pub?key=0As3tAuweYU9QdEZORElDbFU0aFphRXI4WGwydWNDVVE&output=html
