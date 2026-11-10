---
fonte: https://support.google.com/docs/answer/3093617?hl=en
baixado: 2026-11-10
---

# AVERAGEA

Returns the numerical average value in a dataset.

### Sample Usage

`AVERAGEA(A2:A100,B2:B100,4,26)`

`AVERAGEA(1,2,3,4,5,C6:C20)`

### Syntax

`AVERAGEA(value1, [value2, ...])`

- `value1` - The first value or range to consider when calculating the average value.

- `value2, ...` - **\[** OPTIONAL **\]** - Additional values or ranges to consider when calculating the average value.

### Notes

- Although `AVERAGEA` is specified as taking a maximum of 30 arguments, Google Sheets supports an arbitrary number of arguments for this function.

- Any text encountered in the `value` arguments will be set to `0` and included in calculation. To have text values ignored, use `AVERAGE`.

- `AVERAGEA` returns the mean of the combined `value` arguments; that is, the sum of the values in the `value` arguments divided by the number of such values. To calculate the median use `MEDIAN`.

### See Also

[`TRIMMEAN`](https://support.google.com/docs/answer/3094061): Calculates the mean of a dataset excluding some proportion of data from the high and low ends of the dataset.

[`SMALL`](https://support.google.com/docs/answer/3094050): Returns the nth smallest element from a data set, where n is user-defined.

[`RANK`](https://support.google.com/docs/answer/3094098): Returns the rank of a specified value in a dataset.

[`QUARTILE`](https://support.google.com/docs/answer/3094041): Returns a value nearest to a specified quartile of a dataset.

[`PERCENTRANK`](https://support.google.com/docs/answer/3094095): Returns the percentage rank (percentile) of a specified value in a dataset.

[`PERCENTILE`](https://support.google.com/docs/answer/3094093): Returns the value at a given percentile of a dataset.

[`MINA`](https://support.google.com/docs/answer/3094018): Returns the minimum numeric value in a dataset.

[`MIN`](https://support.google.com/docs/answer/3094017): Returns the minimum value in a numeric dataset.

[`MEDIAN`](https://support.google.com/docs/answer/3094025): Returns the median value in a numeric dataset.

[`MAXA`](https://support.google.com/docs/answer/3094016): Returns the maximum numeric value in a dataset.

[`LARGE`](https://support.google.com/docs/answer/3094008): Returns the nth largest element from a data set, where n is user-defined.

[`HARMEAN`](https://support.google.com/docs/answer/3094003): Calculates the harmonic mean of a dataset.

[`GEOMEAN`](https://support.google.com/docs/answer/3094001): Calculates the geometric mean of a dataset.

[`AVERAGE`](https://support.google.com/docs/answer/3093615): The AVERAGE function returns the numerical average value in a dataset, ignoring text.

### Examples

Embedded content: https://docs.google.com/spreadsheet/pub?key=0As3tAuweYU9QdFdrSlRKWUxodnN2b1VPeGRsZ2stWnc&output=html
