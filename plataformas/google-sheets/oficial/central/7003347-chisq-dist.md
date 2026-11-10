---
fonte: https://support.google.com/docs/answer/7003347?hl=en
baixado: 2026-11-10
---

# CHISQ.DIST

Calculates the left-tailed chi-squared distribution, often used in hypothesis testing.

### Sample Usage

`CHISQ.DIST(3.45, 2, TRUE)`

`CHISQ.DIST(A2, B2, TRUE)`

### Syntax

`CHISQ.DIST(x, degrees_freedom, cumulative)`

- `x` - The input to the chi-squared probability distribution function. The value at which to evaluate the function.

  - Must be a positive number.

- `degrees_freedom` - The number of degrees of freedom of the distribution.

- `cumulative` - Logical value that determines the form of the function.

  - If `TRUE: CHI.DIST` returns the left-tailed cumulative distribution function.

  - If `FALSE: CHI.DIST` returns the probability density function.

### Notes

- `degrees_freedom` is truncated to an integer if a non-integer is provided.

- `degrees_freedom` must be at least `1` and may not exceed `10^10`.

- `x` and `degrees_freedom` must be numeric.

### See Also

[`CHIDIST`](https://support.google.com/docs/answer/7003346): Calculates the right-tailed chi-squared distribution, often used in hypothesis testing.

[`CHIINV`](https://support.google.com/docs/answer/7003198): Calculates the inverse of the right-tailed chi-squared distribution.

[`CHISQ.DIST.RT`](https://support.google.com/docs/answer/7003199): Calculates the right-tailed chi-squared distribution, which is commonly used in hypothesis testing.

[`CHITEST`](https://support.google.com/docs/answer/7004263): Returns the probability associated with a Pearson’s chi-squared test on the two ranges of data. Determines the likelihood that the observed categorical data is drawn from an expected distribution.

[`GAMMADIST`](https://support.google.com/docs/answer/7013989): Calculates the gamma distribution, a two-parameter continuous probability distribution.

### Example

Suppose you want to test the fairness of a 6-sided die:

- From several rolls, you obtain a chi-squared statistic of `12.3`.

- The number of degrees of freedom is `6 - 1 = 5`.

- We will evaluate the chi-squared distribution with `5` degrees of freedom when x equals `12.3`.

|       | **A** | **B**               | **C**                       |
|-------|-------|---------------------|-----------------------------|
| **1** | **x** | **Degrees freedom** | **Solution**                |
| **2** | 12.3  | 5                   | 0.01223870353               |
| **3** | 12.3  | 5                   | =CHISQ.DIST(12.3, 5, FALSE) |
| **4** | 12.3  | 5                   | =CHISQ.DIST(A2, B2, FALSE)  |
