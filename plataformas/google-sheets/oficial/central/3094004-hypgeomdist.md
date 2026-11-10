---
fonte: https://support.google.com/docs/answer/3094004?hl=en
baixado: 2026-11-10
---

# HYPGEOMDIST

Calculates the probability of drawing a certain number of successes in a certain number of tries given a population of a certain size containing a certain number of successes, without replacement of draws.

### Sample Usage

`HYPGEOMDIST(4,12,20,40, TRUE)`

`HYPGEOMDIST(A2,A3,A4,A5, FALSE)`

### Syntax

`HYPGEOMDIST(num_successes, num_draws, successes_in_pop, pop_size, cumulative)`

- `num_successes` - The desired number of successes.

- `num_draws` - The number of permitted draws.

- `successes_in_pop` - The total number of successes in the population.

- `pop_size` - The total size of the population

- `cumulative` - Logical value that determines the form of the function.
  - If `TRUE: HYPGEOMDIST` returns the cumulative hypergeometric distribution function.
  - If `FALSE: HYPGEOMDIST` returns the hypergeometric probability mass function.

### Notes

- `BINOMDIST` describes the probability of drawing a certain number of successes in a certain number of tries given a population of a certain size containing a certain number of successes, *with* replacement of draws.

### See Also

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

Embedded content: https://docs.google.com/spreadsheet/pub?key=0As3tAuweYU9QdFc4Zzcwb0VlelE4dDh4UUY5d3NzUFE&output=html
