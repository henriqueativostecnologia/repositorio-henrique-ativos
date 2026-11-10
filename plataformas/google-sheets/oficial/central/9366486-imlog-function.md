---
fonte: https://support.google.com/docs/answer/9366486?hl=en
baixado: 2026-11-10
---

# IMLOG function

The IMLOG function returns the logarithm of a complex number for a specified base.

## Parts of an IMLOG formula 

The `IMLOG` formula is formatted as `=IMLOG(value, base)`.

+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Part**                                           | **Description**                                    | **Notes**                                          |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `value`                                            | The input value of the logarithm function.         | -   The number can be written as plain numbers,    |
|                                                    |                                                    |     e.g. 1, to be interpreted as a real number.    |
|                                                    |                                                    | -   The number can be written as quoted text in    |
|                                                    |                                                    |     order to specify both the real and complex     |
|                                                    |                                                    |     coefficients.                                  |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `base`                                             | The base to use when calculating the logarithm.    | Must be a positive real number.                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+

## Sample formulas 

`IMLOG("1+i", 3.5)`

`IMLOG(COMPLEX(25, 34), 2.3)`

`IMLOG(100, 10)`

## Notes

- `IMLOG` is equivalent to `LOG` for all non-complex values that are greater than zero.
- `IMLOG` is equivalent to `IMLN` given base of `e`, or `EXP(1)`.
- `IMLOG` is equivalent to `IMLOG10` given base of `10`.
- `IMLOG` is equivalent to `IMLOG2`  given base of `2`.

## Examples

|       |                                |                                      |
|-------|--------------------------------|--------------------------------------|
|       | **A**                          | **B**                                |
| **1** | **Formula**                    | **Result**                           |
| **2** | `=IMLOG("1+i", 3.5)`           | 0.276647377832556+0.626932774314643i |
| **3** | `=IMLOG(COMPLEX(25, 34), 2.3)` | 4.49324546771284+1.12470086031758i   |
| **4** | `=IMLOG(100, 10)`              | 2                                    |

## Related function 

[IMLN](https://support.google.com/docs/answer/9000651): The `IMLN` function returns the logarithm of a complex number, base e (Euler's number).

[IMLOG10](https://support.google.com/docs/answer/9366497): The IMLOG10 function returns the logarithm of a complex number with base 10.

[IMLOG2](https://support.google.com/docs/answer/9366426): The IMLOG2 function returns the logarithm of a complex number with base 2.

[COMPLEX](https://support.google.com/docs/answer/7407888): The COMPLEX function creates a complex number, given real and imaginary coefficients.

[IMAGINARY](https://support.google.com/docs/answer/7408639): Returns the imaginary coefficient of a complex number.

[IMREAL](https://support.google.com/docs/answer/7408138): Returns the real coefficient of a complex number.

[LOG](https://support.google.com/docs/answer/3093495): Returns the logarithm of a number given a base.
