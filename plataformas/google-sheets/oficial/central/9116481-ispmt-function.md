---
fonte: https://support.google.com/docs/answer/9116481?hl=en
baixado: 2026-11-10
---

# ISPMT function

The ISPMT function calculates the interest paid during a particular period of an investment.

## Parts of an ISPMT formula

`ISPMT(rate, period, number_of_periods, present_value)`

|                     |                                                                 |                                                   |
|---------------------|-----------------------------------------------------------------|---------------------------------------------------|
| **Part**            | **Description**                                                 | **Notes**                                         |
| `rate`              | The interest rate.                                              |                                                   |
| `period`            | The time frame for which you want to view the interest payment. | Should be number between 1 and number_of_periods. |
| `number_of_periods` | The number of payments to be made.                              |                                                   |
| `present_value`     | The current value of the annuity.                               |                                                   |

## Sample formula

`ISPMT(15%, 2, 5, 1000)`

## Notes

Make sure that consistent units are used for the rate, period, and number of periods. For example, a car loan for 36 months may be paid monthly, in which case the annual percentage rate (APR) should be divided by 12 and the number of payments is 36. A different type of loan of the same length might be paid quarterly, in which case the APR should be divided by 4 and the number of payments would be 12.

## Example

|       |                        |            |
|-------|------------------------|------------|
|       | **A**                  | **B**      |
| **1** | **Formula**            | **Result** |
| **2** | =ISPMT(B1, B2, B3, B4) | -2400      |

## Related functions

- [PPMT](https://support.google.com/docs/answer/3093187): The PPMT function calculates the payment on the principal of an investment based on constant-amount periodic payments and a constant interest rate.
- [PMT](https://support.google.com/docs/answer/3093185): The PMT function calculates the periodic payment for an annuity investment based on constant-amount periodic payments and a constant interest rate.
- [NPER](https://support.google.com/docs/answer/3093183): The NPER function calculates the number of payment periods for an investment based on constant-amount periodic payments and a constant interest rate.
- [IPMT](https://support.google.com/docs/answer/3093175): The IPMT function calculates the payment on interest for an investment based on constant-amount periodic payments and a constant interest rate.
- [FVSCHEDULE](https://support.google.com/docs/answer/3093226): The FVSCHEDULE function calculates the future value of some principal based on a specified series of potentially varying interest rates.
- [FV](https://support.google.com/docs/answer/3093224): The FV function calculates the future value of an annuity investment based on constant-amount periodic payments and a constant interest rate.
