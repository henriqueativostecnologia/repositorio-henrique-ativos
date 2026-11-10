---
fonte: https://support.google.com/docs/answer/3093988?hl=en
baixado: 2026-11-10
---

# CONFIDENCE.NORM

Calculates the width of half the confidence interval for a normal distribution.

### Sample Usage

`CONFIDENCE.NORM(0.05,1.6,250)`

`CONFIDENCE.NORM(A2,A3,A4)`

### Syntax

`CONFIDENCE.NORM(alpha, standard_deviation, pop_size)`

- `alpha` - One minus the desired confidence level. E.g. `0.1` for `0.9`, or 90%, confidence.

- `standard_deviation` - The standard deviation of the population.

- `pop_size` - The size of the population.

### Notes

- `CONFIDENCE.NORM` calculates the width of half the confidence interval such that a value picked at random from the data set has `1-alpha` probability of lying within the mean plus or minus the result of `CONFIDENCE.NORM`.
- You can use `CONFIDENCE` or `CONFIDENCE.NORM` to perform this function. 

### See Also

[`ZTEST`](https://support.google.com/docs/answer/3094067): Returns the one-tailed P-value of a Z-test with standard distribution.

### Examples

Embedded content: https://docs.google.com/spreadsheet/pub?key=0As3tAuweYU9QdHJMSEZmaGRhc3FENWZLWG5KLVRWS1E&output=html
