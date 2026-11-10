---
fonte: https://support.google.com/docs/answer/9198277?hl=en
baixado: 2026-11-10
---

# IMEXP function

The IMEXP function returns Euler's number, e (~2.718) raised to a complex power.

## Parts of a IMEXP function

`IMEXP`(exponent)

|            |                             |
|------------|-----------------------------|
| Part       | Description                 |
| `exponent` | The exponent to raise e to. |

##  Sample formulas

`IMEXP("2+3i")`

`IMEXP("2-4j")`

`IMEXP(COMPLEX(2, 3))`

## Notes

- The exponential of a complex number is defined as follows:

IMEXP(x+yi) = e^(x)cos(y) + ie^(x)sin(y)

## Examples

|       |                |                                     |
|-------|----------------|-------------------------------------|
|       | A              | B                                   |
| **1** | **Formula**    | **Result**                          |
| **2** | =IMEXP("1+i")  | 1.46869393991589+2.28735528717884i  |
| **3** | =IMEXP("2-2j") | -3.07493232063936-6.71884969742825j |

## Related functions

- [EXP](https://support.google.com/docs/answer/3093411): Returns Euler's number, e (~2.718) raised to a power.
- [IMLN](https://support.google.com/docs/answer/9000651): The `IMLN` function returns the logarithm of a complex number, base e (Euler's number).
- [COMPLEX](https://support.google.com/docs/answer/7407888): The COMPLEX function creates a complex number, given real and imaginary coefficients.
- [IMAGINARY](https://support.google.com/docs/answer/7408639): Returns the imaginary coefficient of a complex number.
