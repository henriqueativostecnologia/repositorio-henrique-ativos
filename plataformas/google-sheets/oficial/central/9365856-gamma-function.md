---
fonte: https://support.google.com/docs/answer/9365856?hl=en
baixado: 2026-11-10
---

# GAMMA function

The GAMMA function returns the Gamma function evaluated at the specified value. 

## Parts of a GAMMA function 

`GAMMA(number) `

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Part**                                                                      | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `number`                                                                      | The input to the Gamma function. The natural logarithm of Gamma (number) will |
|                                                                               | be returned.\                                                                 |
|                                                                               | The number must be positive.                                                  |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

## Sample formulas 

`GAMMA(A1:A10)`

`GAMMA(1, 2, 3, 4)`

`GAMMA(B1:B5, 10)`

## Notes

`GAMMA` is used for certain types of analysis or as a component to other functions and is rarely used by itself.

## Examples 

|       |            |               |
|-------|------------|---------------|
|       | **A**      | **B**         |
| **1** | **Result** | **Formula**   |
| **2** | 11.6317284 | `=GAMMA(4.5)` |
| **3** | 2          | `=GAMMA(3)`   |

## Related functions 

- [GAMMALN](https://support.google.com/docs/answer/3093416): Returns the logarithm of a specified Gamma function, base e (Euler's number).
