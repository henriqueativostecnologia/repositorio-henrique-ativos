---
fonte: https://support.google.com/docs/answer/3238496?hl=en
baixado: 2026-11-10
---

# SUMIFS function

Returns the sum of a range depending on multiple criteria.

#### SUMIFS for BigQuery

Returns a conditional sum of a data column depending on multiple criteria.

## Sample Usage

`=SUMIFS(table_name!inventory, table_name!fruits, "Apple", table_name!price, ">5")`

## Syntax

**Important:** To calculate a sum, meet all criteria in a row.

`SUMIFS(sum_column, criteria_column1, criterion1, criteria_column2, criterion2)`

- `sum_column` - The data column to sum.
- `criteria_column1`: The data column to check against criterion1.
- `criterion1` - The pattern or test to apply to criteria_column1.
- `criteria_column2` - Additional data columns to check.
- `criterion2` - Additional criteria to check.

**Tip:** Returning sum across multiple columns is not supported.

### Sample Usage

`SUMIFS(A1:A10, B1:B10, ">20")`

`SUMIFS(A1:A10, B1:B10, ">20", C1:C10, "<30")`

`SUMIFS(C1:C100, E1:E100, "Yes")`

### Syntax

`SUMIFS(sum_range, criteria_range1, criterion1, [criteria_range2, criterion2, ...])`

- `sum_range` - The range to be summed.

- `criteria_range1` - The range to check against `criterion1`.

- `criterion1` - The pattern or test to apply to `criteria_range1`.

- `criteria_range2, criterion2, ...` - **\[** OPTIONAL **\]** - Additional ranges and criteria to check.

### See Also

[`SUM`](https://support.google.com/docs/answer/3093669): Returns the sum of a series of numbers and/or cells.

[`SUMIF`](https://support.google.com/docs/answer/3093583): Returns a conditional sum across a range.

[`SUMSQ`](https://support.google.com/docs/answer/3093714): Returns the sum of the squares of a series of numbers and/or cells.

[`SERIESSUM`](https://support.google.com/docs/answer/3093444): Given parameters `x`, `n`, `m`, and `a`, returns the power series sum a₁x^(n) + a₂x^((n+m)) + ... + a_(i)x^((n+(i-1)m)), where i is the number of entries in range \`a\`.

[`QUOTIENT`](https://support.google.com/docs/answer/3093436): Returns one number divided by another, without the remainder.

[`PRODUCT`](https://support.google.com/docs/answer/3093502): Returns the result of multiplying a series of numbers together.

[`MULTIPLY`](https://support.google.com/docs/answer/3093978): Returns the product of two numbers. Equivalent to the \`\*\` operator.

[`MINUS`](https://support.google.com/docs/answer/3093977): Returns the difference of two numbers. Equivalent to the \`-\` operator.

[`DSUM`](https://support.google.com/docs/answer/3094281): Returns the sum of values selected from a database table-like array or range using a SQL-like query.

[`DIVIDE`](https://support.google.com/docs/answer/3093973): Returns one number divided by another. Equivalent to the \`/\` operator.

[`COUNTIF`](https://support.google.com/docs/answer/3093480): Returns a conditional count across a range.

[`ADD`](https://support.google.com/docs/answer/3093590): Returns the sum of two numbers. Equivalent to the \`+\` operator.
