---
fonte: https://support.google.com/docs/answer/9368238?hl=en
baixado: 2026-11-10
---

# RRI function

The RRI function returns the interest rate needed for an investment to reach a specific value within a given number of periods.

## Parts of a RRI function

`RRI(number_of_periods, present_value, future_value)`

|                     |                                               |
|---------------------|-----------------------------------------------|
| **Part**            | **Description**                               |
| `number_of_periods` | Required. The number of periods.              |
| `present_value`     | Required. The present value of the investment |
| `future_value`      | Required. The future value of the investment. |

## Notes

- All values must be positive. `Number_of_periods` and `present_value` must be greater than 0.
- If `future_value` is 0, the rate returned is -1 (-100%).

## Examples

|               |                     |
|---------------|---------------------|
| **RRI**       | **Formula**         |
| -0.1083343751 | `=RRI(10.5, 10, 3)` |
| 0.2599210499  | `=RRI(3, 2, 4)`     |
| -1            | `=RRI(1, 10, 0)`    |

## Related functions

- [PDURATION](https://support.google.com/docs/answer/9368165): The PDURATION function returns the number of periods for an investment to reach a specific value at a given rate.
