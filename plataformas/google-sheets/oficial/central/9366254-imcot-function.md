---
fonte: https://support.google.com/docs/answer/9366254?hl=en
baixado: 2026-11-10
---

# IMCOT function

The IMCOT function returns the cotangent of the given complex number. For example, a given complex number "x+yi" returns "cot(x+yi)."

## Parts of an IMCOT function 

`IMCOT(number) `

|          |                                                      |                                                                                                                                                                                                   |
|----------|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Part** | **Description**                                      | **Notes**                                                                                                                                                                                         |
| `number` | The complex number for which you want the cotangent. | This can be either the result of the COMPLEX function, a real number interpreted as a complex number with imaginary parts equal to 0, or a string in the format “x+yi” where x and y are numeric. |

## Sample formulas 

`IMCOT(COMPLEX(4,6))`

`IMCOT(4)`

`IMCOT("2+3i")`

## Notes

The `IMCOT` function returns an error if the given number isn't a valid complex number.

## Examples

|       |                        |                                      |
|-------|------------------------|--------------------------------------|
|       | **A**                  | **B**                                |
| **1** | **Formula**            | **Results**                          |
| **2** | `=IMCOT(COMPLEX(4,1))` | 0.253182007063936-0.928132757303418i |
| **3** | `=IMCOT(3.5)`          | 2.66961648496887                     |
| **4** | `=IMCOT("3+2i")`       | -0.0106047834703371-1.035746637765i  |

## Related functions 

[IMTAN](https://support.google.com/docs/answer/9203334): The IMTAN function returns the tangent of the given complex number.

[IMCOTH](https://support.google.com/docs/answer/9366256): The IMCOTH function returns the hyperbolic cotangent of the given complex number.

[COMPLEX](https://support.google.com/docs/answer/7407888): The COMPLEX function creates a complex number, given real and imaginary coefficients.
