---
fonte: https://support.google.com/docs/answer/9366258?hl=en
baixado: 2026-11-10
---

# IMCSCH function

The IMCSCH function returns the hyperbolic cosecant of the given complex number.  For example, a given complex number "x+yi" returns "csch(x+yi)."

## Parts of an IMCSCH function 

`IMCSCH(number) `

|          |                                                                |                                                                                                                                                                                                   |
|----------|----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Part** | **Description**                                                | **Notes**                                                                                                                                                                                         |
| `number` | The complex number for which you want the hyperbolic cosecant. | This can be either the result of the COMPLEX function, a real number interpreted as a complex number with imaginary parts equal to 0, or a string in the format “x+yi” where x and y are numeric. |

## Sample formulas 

`IMCSCH(COMPLEX(4,6))`

`IMCSCH(4)`

`IMCSCH("2+3i")`

## Notes

The `IMCSCH` function returns an error if the given number isn't a valid complex number.

## Examples 

|       |                         |                                         |
|-------|-------------------------|-----------------------------------------|
|       | **A**                   | **B**                                   |
| **1** | **Formula**             | **Result**                              |
| **2** | `=IMCSCH(COMPLEX(4,1))` | 0.0197797995721927-0.0308258875766998i  |
| **3** | `=IMCSCH(3.5)`          | 0.0604498900091561                      |
| **4** | `=IMCSCH("3+2i")`       | -0.0412009862885741-0.0904732097532074i |

## Related functions 

[IMCSC](https://support.google.com/docs/answer/9199155):  The IMCSC function returns the cosecant of the given complex number.

[IMSINH](https://support.google.com/docs/answer/9366445): The IMSINH function returns the hyperbolic sine of the given complex number.

[COMPLEX](https://support.google.com/docs/answer/7407888): The COMPLEX function creates a complex number, given real and imaginary coefficients.
