---
fonte: https://support.google.com/docs/answer/7004181?hl=en
baixado: 2026-11-10
---

# CHISQ.INV

Calculates the inverse of the left-tailed chi-squared distribution.

### Sample Usage

`CHISQ.INV(0.42, 2)`

`CHISQ.INV(A2, B2)`

### Syntax

`CHISQ.INV(probability, degrees_freedom)`

- `probability` - The probability associated with the left-tailed chi-squared distribution.

  - Must be greater than `0` and less than `1`.

- `degrees_freedom` - The number of degrees of freedom of the distribution.

### Notes

- `degrees_freedom` is truncated to an integer if a non-integer is provided.

- `degrees_freedom` must be at least `1`.

- All arguments must be numeric.

### See Also

[`CHIDIST`](https://support.google.com/docs/answer/7003346): Calculates the right-tailed chi-squared distribution, often used in hypothesis testing.

[`CHIINV`](https://support.google.com/docs/answer/7003198): Calculates the inverse of the right-tailed chi-squared distribution.

[`CHISQ.INV.RT`](https://support.google.com/docs/answer/7003348): Calculates the inverse of the right-tailed chi-squared distribution.

[`CHITEST`](https://support.google.com/docs/answer/7004263): Returns the probability associated with a Pearson’s chi-squared test on the two ranges of data. Determines the likelihood that the observed categorical data is drawn from an expected distribution.

[`F.INV`](https://support.google.com/docs/answer/7004265): Calculates the inverse of the left-tailed F probability distribution. Also called the Fisher-Snedecor distribution or Snedecor’s F distribution.

[`T.INV`](https://support.google.com/docs/answer/6055809): Calculates the negative inverse of the one-tailed TDIST function.

### Example

Suppose you want to find the cutoff for the chi-squared statistic associated with a left-tailed probability of `0.95`. With `4` degrees of freedom, you can consider any chi-squared statistic larger than `3.36` to be statistically significant.

|       | **A**           | **B**               | **C**               |
|-------|-----------------|---------------------|---------------------|
| **1** | **Probability** | **Degrees freedom** | **Solution**        |
| **2** | 0.95            | 4                   | 9.487729037         |
| **3** | 0.95            | 4                   | =CHISQ.INV(0.95, 4) |
| **4** | 0.95            | 4                   | =CHISQ.INV(A2, B2)  |
