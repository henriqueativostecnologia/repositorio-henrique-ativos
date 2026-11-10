---
fonte: https://support.google.com/docs/answer/3094061?hl=en
baixado: 2026-11-10
---

# TRIMMEAN

Calculates the mean of a dataset excluding some proportion of data from the high and low ends of the dataset.

### Sample Usage

`TRIMMEAN(A2:A100,0.1)`

`TRIMMEAN({1,1,2,3,5,8,13,21,34,55},0.05)`

### Syntax

`TRIMMEAN(data, exclude_proportion)`

- `data` - Array or range containing the dataset to consider.

- `exclude_proportion` - The proportion of the dataset to exclude, from the extremities of the set.

  - `exclude_proportion` must be greater than or equal to `0` and less than `1`.

### See Also

[`HARMEAN`](https://support.google.com/docs/answer/3094003): Calculates the harmonic mean of a dataset.

[`GEOMEAN`](https://support.google.com/docs/answer/3094001): Calculates the geometric mean of a dataset.

[`AVERAGEA`](https://support.google.com/docs/answer/3093617): Returns the numerical average value in a dataset.

[`AVERAGE`](https://support.google.com/docs/answer/3093615): The AVERAGE function returns the numerical average value in a dataset, ignoring text.

### Examples

Embedded content: https://docs.google.com/spreadsheet/pub?key=0As3tAuweYU9QdFhkTUctaVlCekg0ckl0R1lFZHpTdVE&output=html
