---
fonte: https://support.google.com/docs/answer/3093987?hl=en
baixado: 2026-11-10
---

# BINOMDIST

Calculates the probability of drawing a certain number of successes (or a maximum number of successes) in a certain number of tries given a population of a certain size containing a certain number of successes, with replacement of draws.

### Sample Usage

`BINOMDIST(4,100,0.005,FALSE)`

`BINOMDIST(A2,A3,A4,TRUE)`

### Syntax

`BINOMDIST(num_successes, num_trials, prob_success, cumulative)`

- `num_successes` - The number of successes for which to calculate the probability in `num_trials` trials.

  - If `cumulative` is `TRUE` then `BINOMDIST` returns the probability of `num_successes` or fewer successes, otherwise the probability of exactly `num_successes` successes.

- `num_trials` - The number of independent trials.

- `prob_success` - The probability of success in any given trial.

- `cumulative` - **\[** `FALSE` by default **\]** - Whether to use the binomial cumulative distribution.

### Notes

- `HYPGEOMDIST` describes the probability of drawing a certain number of successes in a certain number of tries given a population of a certain size containing a certain number of successes, *without* replacement of draws.

### See Also

[`WEIBULL`](https://support.google.com/docs/answer/3094116): Returns the value of the Weibull distribution function (or Weibull cumulative distribution function) for a specified shape and scale.

[`PROB`](https://support.google.com/docs/answer/3094039): Given a set of values and corresponding probabilities, calculates the probability that a value chosen at random falls between two limits.

[`POISSON`](https://support.google.com/docs/answer/3094097): Returns the value of the Poisson distribution function (or Poisson cumulative distribution function) for a specified value and mean.

[`NORMSINV`](https://support.google.com/docs/answer/3094091): Returns the value of the inverse standard normal distribution function for a specified value.

[`NORMSDIST`](https://support.google.com/docs/answer/3094089): Returns the value of the standard normal cumulative distribution function for a specified value.

[`NORMINV`](https://support.google.com/docs/answer/3094022): Returns the value of the inverse normal distribution function for a specified value, mean, and standard deviation.

[`NORMDIST`](https://support.google.com/docs/answer/3094021): The NORMDIST function returns the value of the normal distribution function (or normal cumulative distribution function) for a specified value, mean, and standard deviation.

[`NEGBINOMDIST`](https://support.google.com/docs/answer/3094031): Calculates the probability of drawing a certain number of failures before a certain number of successes given a probability of success in independent trials.

[`LOGNORMDIST`](https://support.google.com/docs/answer/3094011): Returns the value of the log-normal cumulative distribution with given mean and standard deviation at a specified value.

[`LOGINV`](https://support.google.com/docs/answer/3094010): Returns the value of the inverse log-normal cumulative distribution with given mean and standard deviation at a specified value.

[`HYPGEOMDIST`](https://support.google.com/docs/answer/3094004): Calculates the probability of drawing a certain number of successes in a certain number of tries given a population of a certain size containing a certain number of successes, without replacement of draws.

[`EXPONDIST`](https://support.google.com/docs/answer/3093995): Returns the value of the exponential distribution function with a specified lambda at a specified value.

[`CRITBINOM`](https://support.google.com/docs/answer/3093623): Calculates the smallest value for which the cumulative binomial distribution is greater than or equal to a specified criteria.

### Examples

Embedded content: https://docs.google.com/spreadsheet/pub?key=0As3tAuweYU9QdGxhcG9Uem1xekpHcWhaUVlKZWlXeVE&output=html
