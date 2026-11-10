---
fonte: https://support.google.com/docs/answer/9369017?hl=en
baixado: 2026-11-10
---

# T.DIST.RT function

Returns the right tailed Student distribution for a value x. Along with `T.DIST.2T,` this function replaces `TDIST` and is equivalent to calling `TDIST` with the tails argument set to 1.

## Parts of a T.DIST.RT function

`T.DIST.2T(x, degrees_freedom)`

|                   |                                                        |
|-------------------|--------------------------------------------------------|
| **Part**          | **Description**                                        |
| `x`               | Required. The x value to evaluate the distribution at. |
| `degrees_freedom` | Required. The degrees of freedom.                      |

## Sample formulas

`Example 1: A1 has T.DIST.RT(1.96, 60)`
`Example 2: A1 has T.DIST.RT(-1.98, 2)`

## Notes

- If deg_freedom is less than 1, returns an \#NUM error.
- This formula along with `T.DIST.2T` replace the `TDIST` formula. `T.DIST.RT` is equivalent to calling the `TDIST` formula with tails = 1.

## Examples

Result for A1=`T.DIST.RT(1.96, 60)`

|       |                   |       |
|-------|-------------------|-------|
|       | **A**             | **B** |
| **1** | 0.027322464868265 |       |
| **2** |                   |       |

Result for A1=`T.DIST.RT(-1.98, 2)`

|       |                    |       |
|-------|--------------------|-------|
|       | **A**              | **B** |
| **1** | 0.9068737480782105 |       |
| **2** |                    |       |

## Related functions

- [T.DIST](https://support.google.com/docs/answer/9369014): The T.DIST function returns the right tailed Student distribution for a value x.
- [T.DIST.2T](https://support.google.com/docs/answer/9368252): The T.DIST.2T function returns the two tailed Student distribution for a value x.
- [TDIST](https://support.google.com/docs/answer/3295914): Calculates the probability for Student's t-distribution with a given input (x).
