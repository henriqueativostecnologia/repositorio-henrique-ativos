---
fonte: https://support.google.com/docs/answer/3094089?hl=en
baixado: 2026-11-10
---

# NORMSDIST

Returns the value of the standard normal cumulative distribution function for a specified value.

### Sample Usage

`NORMSDIST(2.4, TRUE)`

`NORMSDIST(A2, FALSE)`

### Syntax

`NORMSDIST(x, cumulative)`

- `x` - The input to the standard normal cumulative distribution function.
- `cumulative` - Logical value that determines the form of the function.
  - If `TRUE: NORMSDIST` returns the standard normal cumulative distribution function.
  - If `FALSE: NORMSDIST` returns the standard normal probability density function.

### Notes

- The "standard" normal distribution function is the normal distribution function with mean of `0` and variance (and therefore standard deviation) of `1`.

### See Also

[`ZTEST`](https://support.google.com/docs/answer/3094067): Returns the one-tailed P-value of a Z-test with standard distribution.

[`WEIBULL`](https://support.google.com/docs/answer/3094116): Returns the value of the Weibull distribution function (or Weibull cumulative distribution function) for a specified shape and scale.

[`POISSON`](https://support.google.com/docs/answer/3094097): Returns the value of the Poisson distribution function (or Poisson cumulative distribution function) for a specified value and mean.

[`NORMSINV`](https://support.google.com/docs/answer/3094091): Returns the value of the inverse standard normal distribution function for a specified value.

[`NORMINV`](https://support.google.com/docs/answer/3094022): Returns the value of the inverse normal distribution function for a specified value, mean, and standard deviation.

[`NORMDIST`](https://support.google.com/docs/answer/3094021): The NORMDIST function returns the value of the normal distribution function (or normal cumulative distribution function) for a specified value, mean, and standard deviation.

[`NEGBINOMDIST`](https://support.google.com/docs/answer/3094031): Calculates the probability of drawing a certain number of failures before a certain number of successes given a probability of success in independent trials.

[`LOGNORMDIST`](https://support.google.com/docs/answer/3094011): Returns the value of the log-normal cumulative distribution with given mean and standard deviation at a specified value.

[`LOGINV`](https://support.google.com/docs/answer/3094010): Returns the value of the inverse log-normal cumulative distribution with given mean and standard deviation at a specified value.

[`EXPONDIST`](https://support.google.com/docs/answer/3093995): Returns the value of the exponential distribution function with a specified lambda at a specified value.

[`BINOMDIST`](https://support.google.com/docs/answer/3093987): Calculates the probability of drawing a certain number of successes (or a maximum number of successes) in a certain number of tries given a population of a certain size containing a certain number of successes, with replacement of draws.

### Examples

Embedded content: https://docs.google.com/spreadsheet/pub?key=0As3tAuweYU9QdHFOYnBLRGhvNTZFUU01MUFodXZCUUE&output=html
