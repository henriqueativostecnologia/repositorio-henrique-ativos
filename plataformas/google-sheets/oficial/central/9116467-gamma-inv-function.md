---
fonte: https://support.google.com/docs/answer/9116467?hl=en
baixado: 2026-11-10
---

# GAMMA.INV function

The GAMMA.INV function returns the value of the inverse gamma cumulative distribution function for the specified probability, alpha, and beta parameters.

## Parts of a GAMMA.INV formula

`GAMMA.INV(probability, alpha, beta)`

+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Part**                                           | **Description**                                    | **Notes**                                          |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `probability`                                      | The input to the inverse gamma distribution        | -   Must be between 0 and 1.                       |
|                                                    | function.                                          |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `alpha`                                            | The shape of the gamma distribution.               | -   Must be positive.                              |
|                                                    |                                                    | -   The sign of significance is ignored.           |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `beta`                                             | The scale of the gamma distribution.               | -   Must be positive.                              |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+

## Sample formulas

`GAMMA.INV(0.65, 4, 2)`

`GAMMA.INV(C3, 3, 2)`

## Note

- You can use `GAMMAINV` or `GAMMA.INV` to perform this function. 

## Example

|       |                       |             |
|-------|-----------------------|-------------|
|       | **A**                 | **B**       |
| **1** | **Formula**           | **Result**  |
| **2** | =GAMMA.INV(0.3, 5, 1) | 3.633609083 |

## Related function

- [GAMMA.DIST](https://support.google.com/docs/answer/7013990): The GAMMA.DIST function calculates the gamma distribution, a 2-parameter continuous probability distribution.
