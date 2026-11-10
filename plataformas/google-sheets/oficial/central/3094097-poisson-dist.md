---
fonte: https://support.google.com/docs/answer/3094097?hl=en
baixado: 2026-11-10
---

# POISSON.DIST

Returns the value of the Poisson distribution function (or Poisson cumulative distribution function) for a specified value and mean.

### Sample Usage

`POISSON.DIST(2.4,1,FALSE)`

`POISSON.DIST(A2,A3,TRUE)`

### Syntax

`POISSON.DIST(x, mean, cumulative)`

- `x` - The input to the Poisson distribution function.

- `mean` - The mean (mu) of the Poisson distribution function.

- `cumulative` - Whether to use the Poisson cumulative distribution function rather than the distribution function..

### Notes

- The Poisson distribution function is typically used to calculate the number of 'arrivals' or 'events' over a period of time, such as the number of network packets or login attempts given some mean.

- If `cumulative` is `TRUE` then `POISSON.DIST` returns the probability of `x` or fewer events, otherwise the probability of exactly `x` events.

- You can use `POISSON` or `POISSON.DIST` to perform this function. 

### See Also

[`WEIBULL`](https://support.google.com/docs/answer/3094116): Returns the value of the Weibull distribution function (or Weibull cumulative distribution function) for a specified shape and scale.

[`NORMSINV`](https://support.google.com/docs/answer/3094091): Returns the value of the inverse standard normal distribution function for a specified value.

[`NORMSDIST`](https://support.google.com/docs/answer/3094089): Returns the value of the standard normal cumulative distribution function for a specified value.

[`NORMINV`](https://support.google.com/docs/answer/3094022): Returns the value of the inverse normal distribution function for a specified value, mean, and standard deviation.

[`NORMDIST`](https://support.google.com/docs/answer/3094021): The NORMDIST function returns the value of the normal distribution function (or normal cumulative distribution function) for a specified value, mean, and standard deviation.

[`NEGBINOMDIST`](https://support.google.com/docs/answer/3094031): Calculates the probability of drawing a certain number of failures before a certain number of successes given a probability of success in independent trials.

[`LOGNORMDIST`](https://support.google.com/docs/answer/3094011): Returns the value of the log-normal cumulative distribution with given mean and standard deviation at a specified value.

[`LOGINV`](https://support.google.com/docs/answer/3094010): Returns the value of the inverse log-normal cumulative distribution with given mean and standard deviation at a specified value.

[`EXPONDIST`](https://support.google.com/docs/answer/3093995): Returns the value of the exponential distribution function with a specified lambda at a specified value.

[`BINOMDIST`](https://support.google.com/docs/answer/3093987): Calculates the probability of drawing a certain number of successes (or a maximum number of successes) in a certain number of tries given a population of a certain size containing a certain number of successes, with replacement of draws.

### Examples

Embedded content: https://docs.google.com/spreadsheet/pub?key=0As3tAuweYU9QdHRSaDhrWGxkbVA2cUZWblNLcmczR3c&output=html
