---
fonte: https://support.google.com/docs/answer/3094093?hl=en
baixado: 2026-11-10
---

# PERCENTILE function

Returns the value at a given percentile of a dataset.

### Sample Usage

`PERCENTILE(A2:A100,A2)`

`PERCENTILE(A2:A100,0.67)`

### Syntax

`PERCENTILE(data, percentile)`

- `data` - The array or range containing the dataset to consider.

- `percentile` - The percentile whose value within `data` will be calculated and returned.

### Notes

- The value returned by `PERCENTILE` is not necessarily a member of `data` as this function interpolates between values to calculate the alpha percentile.

- The 50th percentile, that is setting `percentile` to `0.5` is equivalent to using `MEDIAN` with the same dataset.

### See Also

[`SMALL`](https://support.google.com/docs/answer/3094050): Returns the nth smallest element from a data set, where n is user-defined.

[`RANK`](https://support.google.com/docs/answer/3094098): Returns the rank of a specified value in a dataset.

[`QUARTILE`](https://support.google.com/docs/answer/3094041): Returns a value nearest to a specified quartile of a dataset.

[`PERCENTRANK`](https://support.google.com/docs/answer/3094095): Returns the percentage rank (percentile) of a specified value in a dataset.

[`MINA`](https://support.google.com/docs/answer/3094018): Returns the minimum numeric value in a dataset.

[`MIN`](https://support.google.com/docs/answer/3094017): Returns the minimum value in a numeric dataset.

[`MEDIAN`](https://support.google.com/docs/answer/3094025): Returns the median value in a numeric dataset.

[`MAXA`](https://support.google.com/docs/answer/3094016): Returns the maximum numeric value in a dataset.

[`MAX`](https://support.google.com/docs/answer/3094013): Returns the maximum value in a numeric dataset.

[`LARGE`](https://support.google.com/docs/answer/3094008): Returns the nth largest element from a data set, where n is user-defined.

[`AVERAGEA`](https://support.google.com/docs/answer/3093617): Returns the numerical average value in a dataset.

[`AVERAGE`](https://support.google.com/docs/answer/3093615): The AVERAGE function returns the numerical average value in a dataset, ignoring text.

### Examples

Embedded content: https://docs.google.com/spreadsheet/pub?key=0As3tAuweYU9QdGJaNGYtSU1hLVhrZWp4R1pveVhGMmc&output=html
