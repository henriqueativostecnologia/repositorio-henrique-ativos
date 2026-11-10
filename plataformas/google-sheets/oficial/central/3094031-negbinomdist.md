---
fonte: https://support.google.com/docs/answer/3094031?hl=en
baixado: 2026-11-10
---

# NEGBINOMDIST

Calculates the probability of drawing a certain number of failures before a certain number of successes given a probability of success in independent trials.

### Sample Usage

`NEGBINOMDIST(4,2,0.1, TRUE)`

`NEGBINOMDIST(A2,A3,A4, FALSE)`

### Syntax

`NEGBINOMDIST(num_failures, num_successes, prob_success, cumulative)`

- `num_failures` - The number of failures to model.

- `num_successes` - The number of successes to model.

- `prob_success` - The probability of success in any given trial.

- `cumulative` - Logical value that determines the form of the function.
  - If `TRUE: NEGBINOMDIST` returns the cumulative negative binomial distribution function.
  - If `FALSE: NEGBINOMDIST` returns the negative binomial probability mass function.

### Notes

- `NEGBINOMDIST` models the negative binomial distribution, which is related to the binomial distribution except that the number of trials is variable whereas the number of successes is fixed.

### See Also

[`WEIBULL`](https://support.google.com/docs/answer/3094116): Returns the value of the Weibull distribution function (or Weibull cumulative distribution function) for a specified shape and scale.

[`POISSON`](https://support.google.com/docs/answer/3094097): Returns the value of the Poisson distribution function (or Poisson cumulative distribution function) for a specified value and mean.

[`NORMSINV`](https://support.google.com/docs/answer/3094091): Returns the value of the inverse standard normal distribution function for a specified value.

[`NORMSDIST`](https://support.google.com/docs/answer/3094089): Returns the value of the standard normal cumulative distribution function for a specified value.

[`NORMINV`](https://support.google.com/docs/answer/3094022): Returns the value of the inverse normal distribution function for a specified value, mean, and standard deviation.

[`NORMDIST`](https://support.google.com/docs/answer/3094021): The NORMDIST function returns the value of the normal distribution function (or normal cumulative distribution function) for a specified value, mean, and standard deviation.

[`LOGNORMDIST`](https://support.google.com/docs/answer/3094011): Returns the value of the log-normal cumulative distribution with given mean and standard deviation at a specified value.

[`LOGINV`](https://support.google.com/docs/answer/3094010): Returns the value of the inverse log-normal cumulative distribution with given mean and standard deviation at a specified value.

[`HYPGEOMDIST`](https://support.google.com/docs/answer/3094004): Calculates the probability of drawing a certain number of successes in a certain number of tries given a population of a certain size containing a certain number of successes, without replacement of draws.

[`EXPONDIST`](https://support.google.com/docs/answer/3093995): Returns the value of the exponential distribution function with a specified lambda at a specified value.

[`BINOMDIST`](https://support.google.com/docs/answer/3093987): Calculates the probability of drawing a certain number of successes (or a maximum number of successes) in a certain number of tries given a population of a certain size containing a certain number of successes, with replacement of draws.

### Examples

Embedded content: https://docs.google.com/spreadsheet/pub?key=0As3tAuweYU9QdElJLWNJUkZ1MXh0Tnh2cXVoSjJZbVE&output=html
