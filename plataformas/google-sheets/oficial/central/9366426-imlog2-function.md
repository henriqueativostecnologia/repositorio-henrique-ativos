---
fonte: https://support.google.com/docs/answer/9366426?hl=en
baixado: 2026-11-10
---

# IMLOG2 function

The IMLOG2 function returns the logarithm of a complex number with base 2.

## Parts of an IMLOG2 formula 

`IMLOG2(value)`

+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Part**                                           | **Description**                                    | **Notes**                                          |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `value`                                            | The input value of the logarithm function.         | -   The number can be written as plain numbers,    |
|                                                    |                                                    |     for example 1, to be interpreted as a real     |
|                                                    |                                                    |     number.                                        |
|                                                    |                                                    | -   The number can be written as quoted text in    |
|                                                    |                                                    |     order to specify both the real and complex     |
|                                                    |                                                    |     coefficients.                                  |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+

## Sample formulas 

`IMLOG2("1+i", 3.5)`

`IMLOG2(COMPLEX(25, 34), 2.3)`

`IMLOG2(100, 10)`

## Notes

`IMLOG2` is equivalent to `IMLOG` given base of 2 for all numbers. 

## Examples 

|       |                            |                                    |
|-------|----------------------------|------------------------------------|
|       | **A**                      | **B**                              |
| **1** | **Formula**                | **Result**                         |
| **2** | `=IMLOG2("1+i")`           | 0.5+1.1330900354568i               |
| **3** | `=IMLOG2(COMPLEX(25, 34))` | 5.39923590055081+1.35147863744424i |
| **4** | `=IMLOG2(100)`             | 6.64385618977473                   |

## Related functions

[IMLOG](https://support.google.com/docs/answer/9366486): The IMLOG function returns the logarithm of a complex number for a specified base.

[IMLOG10](https://support.google.com/docs/answer/9366497): The IMLOG10 function returns the logarithm of a complex number with base 10.

[COMPLEX](https://support.google.com/docs/answer/7407888): The COMPLEX function creates a complex number, given real and imaginary coefficients.

[IMAGINARY](https://support.google.com/docs/answer/7408639): Returns the imaginary coefficient of a complex number.

[IMREAL](https://support.google.com/docs/answer/7408138): Returns the real coefficient of a complex number.
