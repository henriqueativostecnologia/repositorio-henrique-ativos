---
fonte: https://support.google.com/docs/answer/3094041?hl=en
baixado: 2026-11-10
---

# QUARTILE function

Returns a value nearest to a specified quartile of a dataset.

### Sample Usage

`QUARTILE(A2:A100,3)`

`QUARTILE(A2:A100,B2)`

### Syntax

`QUARTILE(data, quartile_number)`

- `data` - The array or range containing the dataset to consider.

- `quartile_number` - Which quartile value to return.

  - `0` returns the minimum value in `data` (0% mark).

  - `1` returns the value in `data` closest to the first quartile (25% mark).

  - `2` returns the value in `data` closest to the median (50% mark).

  - `3` returns the value in `data` closest to the third quartile (75% mark).

  - `4` returns the maximum value in `data` (100% mark).

### See Also

[`SMALL`](https://support.google.com/docs/answer/3094050): Returns the nth smallest element from a data set, where n is user-defined.

[`RANK`](https://support.google.com/docs/answer/3094098): Returns the rank of a specified value in a dataset.

[`PERCENTRANK`](https://support.google.com/docs/answer/3094095): Returns the percentage rank (percentile) of a specified value in a dataset.

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

Embedded content: https://docs.google.com/spreadsheet/pub?key=0As3tAuweYU9QdHotcmdRR0ZnYmtlekR6WUZGUDQzWGc&output=html
