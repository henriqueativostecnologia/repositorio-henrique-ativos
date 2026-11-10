---
fonte: https://support.google.com/docs/answer/3093226?hl=en
baixado: 2026-11-10
---

# FVSCHEDULE

The FVSCHEDULE function calculates the future value of some principal based on a specified series of potentially varying interest rates.

### Sample Usage

`FVSCHEDULE(10000,A2:A100)`

`FVSCHEDULE(10000,{0.1,0.95,0.9,0.85})`

`FVSCHEDULE(A2,B2:B20)`

### Syntax

`FVSCHEDULE(principal, rate_schedule)`

- `principal` - The amount of initial capital or value to compound against.

- `rate_schedule` - A series of interest rates to compound against the `principal`.

  - `rate_schedule` must be either a range or array containing the interest rates to compound, in sequence. These should be expressed either as decimals or as percentages using `UNARY_PERCENT`, i.e. `0.09` or `UNARY_PERCENT(9)` rather than `9`.

### See Also

[`PV`](https://support.google.com/docs/answer/3093243): Calculates the present value of an annuity investment based on constant-amount periodic payments and a constant interest rate.

[`PPMT`](https://support.google.com/docs/answer/3093187): The PPMT function calculates the payment on the principal of an investment based on constant-amount periodic payments and a constant interest rate.

[`PMT`](https://support.google.com/docs/answer/3093185): The PMT function calculates the periodic payment for an annuity investment based on constant-amount periodic payments and a constant interest rate.

[`NPER`](https://support.google.com/docs/answer/3093183): The NPER function calculates the number of payment periods for an investment based on constant-amount periodic payments and a constant interest rate.

[`IPMT`](https://support.google.com/docs/answer/3093175): The IPMT function calculates the payment on interest for an investment based on constant-amount periodic payments and a constant interest rate.

[`FV`](https://support.google.com/docs/answer/3093224): The FV function calculates the future value of an annuity investment based on constant-amount periodic payments and a constant interest rate.

### Examples

Embedded content: https://docs.google.com/spreadsheet/pub?key=0As3tAuweYU9QdGJqbTJKVnZ2Q3ZwT3NxM1dEajBqYnc&output=html
