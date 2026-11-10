---
fonte: https://support.google.com/docs/answer/9116267?hl=en
baixado: 2026-11-10
---

# ERF function

The ERF function returns the integral of the Gauss error function over an interval of values.

## Parts of an ERF formula

`ERF(lower_bound, [upper_bound])`

|               |                                                                                                                                                               |                                |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|
| **Part**      | **Description**                                                                                                                                               | **Notes**                      |
| `lower_bound` | If this parameter is the only parameter, the integral is taken between 0 and this value. If z2 is provided, it refers to the lower boundary for the integral. |                                |
| `upper_bound` | The upper boundary of the integral.                                                                                                                           | Upper boundaries are optional. |

## Sample formulas

`ERF(-2.3, -0.7)`

`ERF(1)`

## Notes

If the lower or upper boundaries are non-numeric, ERF returns "#VALUE!."

## Examples

|       |                 |              |
|-------|-----------------|--------------|
|       | **A**           | **B**        |
| **1** | **Formula**     | **Result**   |
| **2** | ERF(-2.3, -0.7) | 0.3210556296 |
| **3** | ERF(1)          | 0.8427007929 |

## Related functions

- [ERFC](https://support.google.com/docs/answer/3093407): The ERFC function returns the complementary Gauss error function of a value.
- [NORMDIST](https://support.google.com/docs/answer/3094021): The NORMDIST function returns the value of the normal distribution function (or normal cumulative distribution function) for a specified value, mean, and standard deviation.
