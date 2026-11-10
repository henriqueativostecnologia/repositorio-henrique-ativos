---
fonte: https://support.google.com/docs/answer/9366728?hl=en
baixado: 2026-11-10
---

# IMSEC function

The IMSEC function returns the secant of the given complex number. For example, a given complex number "x+yi" returns "sec(x+yi)."

## Parts of an IMSEC function

`IMSEC(number) `

|          |                                                   |                                                                                                                                                                                                   |
|----------|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Part** | **Description**                                   | **Notes**                                                                                                                                                                                         |
| `number` | The complex number for which you want the secant. | This can be either the result of the COMPLEX function, a real number interpreted as a complex number with imaginary parts equal to 0, or a string in the format “x+yi” where x and y are numeric. |

## Sample formulas

`IMSEC(COMPLEX(4,6))`

`IMSEC(4)`

`IMSEC("2+3i")`

## Notes

The `IMSEC` function returns an error if the given number isn't a valid complex number. 

## Examples

|       |                        |                                        |
|-------|------------------------|----------------------------------------|
|       | **A**                  | **B**                                  |
| **1** | **Formula**            | **Result**                             |
| **2** | `=IMSEC(COMPLEX(4,1))` | -0.557760402867351-0.491827502294509i  |
| **3** | `=IMSEC(3.5)`          | -1.06785504719181                      |
| **4** | `=IMSEC("3+2i")`       | -0.263512975158389+0.0362116365587685i |

## Related functions

[IMCOS](https://support.google.com/docs/answer/9116546):  The IMCOS function returns the cosine of the given complex number.

[IMSECH](https://support.google.com/docs/answer/9366440):  The IMSECH function returns the hyperbolic secant of the given complex number.

[COMPLEX](https://support.google.com/docs/answer/7407888): The COMPLEX function creates a complex number, given real and imaginary coefficients.
