---
fonte: https://support.google.com/docs/answer/9368252?hl=en
baixado: 2026-11-10
---

# T.DIST.2T function

The T.DIST.2T function returns the two tailed Student distribution for a value x. Along with `T.DIST.RT`, this function replaces `TDIST` and is equivalent to calling `TDIST` with the tails argument set to 2.

## Parts of a T.DIST.2T function

`T.DIST.2T(x, degrees_freedom)`

|                   |                                                        |
|-------------------|--------------------------------------------------------|
| **Part**          | **Description**                                        |
| `x`               | Required. The x value to evaluate the distribution at. |
| `degrees_freedom` | Required. The degrees of freedom.                      |

## Sample formulas

`Example 1: T.DIST.2T(1.96, 60)`

`Example 2: T.DIST.2T(1, 2)`

## Notes

- If deg_freedom is less than 1, returns an \#NUM error.
- If x is negative, returns an \#NUM error.
- Along with `T.DIST.RT`, this formula replaces the `TDIST` formula. This is equivalent to calling the `TDIST` formula with tails = 2.

## Examples

Result for A1=`T.DIST.2T(1.96, 60)`
 

|       |                   |       |
|-------|-------------------|-------|
|       | **A**             | **B** |
| **1** | 0.054644929736529 |       |
| **2** |                   |       |

Result for A1=`T.DIST.2T(1, 2)`

|       |                  |       |
|-------|------------------|-------|
|       | **A**            | **B** |
| **1** | 0.42264973081037 |       |
| **2** |                  |       |

## Related functions

- [T.DIST](https://support.google.com/docs/answer/9369014): The T.DIST function returns the right tailed Student distribution for a value x.
- [T.DIST.RT](https://support.google.com/docs/answer/9369017): Returns the right tailed Student distribution for a value x.
- [TDIST](https://support.google.com/docs/answer/3295914): Calculates the probability for Student's t-distribution with a given input (x).
