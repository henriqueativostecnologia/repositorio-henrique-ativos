---
fonte: https://support.google.com/docs/answer/9203334?hl=en
baixado: 2026-11-10
---

# IMTAN function

The IMTAN function returns the tangent of the given complex number. For example, a given complex number "x+yi" returns "tan(x+yi)."

### Parts of an IMTAN formula

`IMTAN(number)`

|          |                                                    |                                                                                                                                                                                                                  |
|----------|----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Part** | **Description**                                    | **Notes**                                                                                                                                                                                                        |
| `number` | The complex number for which you want the tangent. | This can be either the result of the COMPLEX function, a real number (which will be interpreted as a complex number with imaginary part equal to 0), or a string in the format "x+yi" where x and y are numeric. |

### Sample formulas

`IMTAN(COMPLEX(4, 6))`

`IMTAN(4)`

`IMTAN("2+3i")`

### Notes

The IMTAN function returns an error if the given number isn’t a valid complex number or if the tangent function is undefined for the given number.

### Examples

|       |                       |                                       |
|-------|-----------------------|---------------------------------------|
|       | **A**                 | **B**                                 |
| **1** | **Formula**           | **Result**                            |
| **2** | =IMTAN(COMPLEX(4, 3)) | 0.00490825806749606+1.00070953606723i |
| **3** | =IMTAN(0.213)         | 0.216280749620508                     |
| **4** | =IMTAN("2-2i")        | -0.0283929528682323-1.02383559457047i |

### Related functions

- [COMPLEX](https://support.google.com/docs/answer/7407888): The COMPLEX function creates a complex number, given real and imaginary coefficients.
- [IMSIN](https://support.google.com/docs/answer/9198962): The IMSIN function returns the sine of the given complex number.
- [IMCOS](https://support.google.com/docs/answer/9116546): The IMCOS function returns the cosine of the given complex number.
