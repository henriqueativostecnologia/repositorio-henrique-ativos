---
fonte: https://support.google.com/docs/answer/9366497?hl=en
baixado: 2026-11-10
---

# IMLOG10 function

The IMLOG10 function returns the logarithm of a complex number with base 10.

## Parts of an IMLOG10 formula

`IMLOG10(value)`

+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Part**                                           | **Desription**                                     | **Notes**                                          |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `value`                                            | The input value of the logarithm function.         | -   The number can be written as plain numbers,    |
|                                                    |                                                    |     for example 1, to be interpreted as a real     |
|                                                    |                                                    |     number.                                        |
|                                                    |                                                    | -   The number can be written as quoted text in    |
|                                                    |                                                    |     order to specify both the real and complex     |
|                                                    |                                                    |     coefficients.                                  |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+

## Sample formulas 

`IMLOG10("1+i", 3.5)`

`IMLOG10(COMPLEX(25, 34), 2.3)`

`IMLOG10(100, 10)`

## Note

`IMLOG10` is equivalent to `IMLOG` given base of 10 for all numbers.

## Examples

|       |                             |                                     |
|-------|-----------------------------|-------------------------------------|
|       | **A**                       | **B**                               |
| **1** | **Formula**                 | **Result**                          |
| **2** | `=IMLOG10("1+i")`           | 0.150514997831991+0.34109408846046i |
| **3** | `=IMLOG10(COMPLEX(25, 34))` | 1.62533195973162+0.406835608369804i |
| **4** | `=IMLOG10(100)`             | 2                                   |

## Related functions

[IMLOG](https://support.google.com/docs/answer/9366486): The IMLOG function returns the logarithm of a complex number for a specified base.

[IMLOG2](https://support.google.com/docs/answer/9366426): The IMLOG2 function returns the logarithm of a complex number with base 2.

[COMPLEX](https://support.google.com/docs/answer/7407888): The COMPLEX function creates a complex number, given real and imaginary coefficients.

[IMAGINARY](https://support.google.com/docs/answer/7408639): Returns the imaginary coefficient of a complex number.

[IMREAL](https://support.google.com/docs/answer/7408138): Returns the real coefficient of a complex number.
