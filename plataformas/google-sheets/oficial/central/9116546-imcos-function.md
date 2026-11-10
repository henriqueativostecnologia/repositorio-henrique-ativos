---
fonte: https://support.google.com/docs/answer/9116546?hl=en
baixado: 2026-11-10
---

# IMCOS function

The IMCOS function returns the cosine of the given complex number. For example, a given complex number "x+yi" returns "cos(x+yi)."

## Parts of an IMCOS formula

`IMCOS(number)`

|          |                                                   |                                                                                                                                                                                                                  |
|----------|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Part** | **Description**                                   | **Notes**                                                                                                                                                                                                        |
| `number` | The complex number for which you want the cosine. | This can be either the result of the COMPLEX function, a real number (which will be interpreted as a complex number with imaginary part equal to 0), or a string in the format “x+yi” where x and y are numeric. |

## Sample formulas

`IMCOS(COMPLEX(4, 6))`

`IMCOS(4)`

`IMCOS("2+3i")`

## Notes

The IMCOS function returns an error if the given number isn't a valid complex number.

## Examples

|       |                       |                                      |
|-------|-----------------------|--------------------------------------|
|       | **A**                 | **B**                                |
| **1** | **Formula**           | **Result**                           |
| **2** | =IMCOS(COMPLEX(4, 1)) | -1.00862481342516+0.889395195838485i |
| **3** | =IMCOS(3.5)           | -0.936456687290796                   |
| **4** | =IMCOS("3+2i")        | -3.72454550491532-0.511822569987385i |

## Related function

[COMPLEX](https://support.google.com/docs/answer/7407888): The COMPLEX function creates a complex number, given real and imaginary coefficients.
