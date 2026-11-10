---
fonte: https://support.google.com/docs/answer/3256534?hl=en
baixado: 2026-11-10
---

# AVERAGEIFS

Returns the average of a range depending on multiple criteria.

#### AVERAGEIFS for BigQuery

## Sample Usage

Returns the average of a data column depending on multiple criteria.

### Sample Usage

`AVERAGEIFS(table_name!price, table_name!fruits, “Apple”, table_name!inventory, “<30”)`

### Syntax

`AVERAGEIFS(average_column, criteria_column1, criterion1, criteria_column2, criterion 2)`

- `average_column` - The data column to average.
- `criteria_column1` - The data column to check against \`criterion1\`.
- `criterion1` - The pattern or test to apply to \`criteria_column1\`.
- `criteria_column2 `- Additional data column to check.
- `criterion 2 `- Additional criteria to check.

### Sample Usage

`AVERAGEIFS(A1:A10, B1:B10, ">20")`

`AVERAGEIFS(A1:A10, B1:B10, ">20", C1:C10, "<30")`

`AVERAGEIFS(C1:C100, E1:E100, "Yes")`

### Syntax

`AVERAGEIFS(average_range, criteria_range1, criterion1, [criteria_range2, criterion2, ...])`

- `average_range` - The range to average.

- `criteria_range1` - The range to check against `criterion1`.

- `criterion1` - The pattern or test to apply to `criteria_range1`.

- `criteria_range2, criterion2, ...` - **\[** OPTIONAL **\]** - Additional ranges and criteria to check.

### See Also

[`AVERAGE`](https://support.google.com/docs/answer/3093615): The AVERAGE function returns the numerical average value in a dataset, ignoring text.

[`AVERAGEA`](https://support.google.com/docs/answer/3093617): Returns the numerical average value in a dataset.

[`AVERAGEIF`](https://support.google.com/docs/answer/3256529): Returns the average of a range depending on criteria.

[`SUMIFS`](https://support.google.com/docs/answer/3238496): Returns the sum of a range depending on multiple criteria.

[`COUNTIFS`](https://support.google.com/docs/answer/3256550): Returns the count of a range depending on multiple criteria.

[`IF`](https://support.google.com/docs/answer/3093364): Returns one value if a logical expression is \`TRUE\` and another if it is \`FALSE\`.

[`MEDIAN`](https://support.google.com/docs/answer/3094025): Returns the median value in a numeric dataset.
