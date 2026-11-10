---
fonte: https://support.google.com/docs/answer/9369014?hl=en
baixado: 2026-11-10
---

# T.DIST function

The T.DIST function returns the right tailed Student distribution for a value x. Along with `T.DIST.2T`, this function replaces `TDIST` and is equivalent to calling `TDIST` with the tails argument set to 1.

## Parts of a T.DIST function

`T.DIST(x, degrees_freedom, cumulative)`

|                   |                                                                                                                                                |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| **Part**          | **Description**                                                                                                                                |
| `x`               | Required. The x value to evaluate the distribution at.                                                                                         |
| `degrees_freedom` | Required. The degrees of freedom.                                                                                                              |
| `cumulative`      | Required. True/false value field. If true, returns the cumulative probability for x. If false, returns the probability density function for x. |

## Sample formulas

- `Example 1: A1 has T.DIST(1.96, 60, false)`
- `Example 2: A1 has T.DIST(-1.98, 2, false)`
- `Example 3: A1 has T.DIST(1.96, 60, true)`
- `Example 4: A1 has T.DIST(-1.98, 2, true)`

## Notes

If deg_freedom is less than 1, returns as \#NUM error. 

## Examples

Result for A1=`T.DIST(1.96, 60, false)`

|       |                   |       |
|-------|-------------------|-------|
|       | **A**             | **B** |
| **1** | 0.059847906211419 |       |
| **2** |                   |       |

Result for A1=`T.DIST(-1.98, 2, false)`

|       |                     |       |
|-------|---------------------|-------|
|       | **A**               | **B** |
| **1** | 0.06941821226899947 |       |
| **2** |                     |       |

Result for A1=`T.DIST(1.96, 60, true)`

|       |                   |       |
|-------|-------------------|-------|
|       | **A**             | **B** |
| **1** | 0.972677535131736 |       |
| **2** |                   |       |

Result for A1=`T.DIST(-1.98, 2, true)`

|       |                     |       |
|-------|---------------------|-------|
|       | **A**               | **B** |
| **1** | 0.09312625192178947 |       |
| **2** |                     |       |

## Related functions

- [TDIST](https://support.google.com/docs/answer/3295914): Calculates the probability for Student's t-distribution with a given input (x).
- [T.DIST.2T](https://support.google.com/docs/answer/9368252): The T.DIST.2T function returns the two tailed Student distribution for a value x.
- [T.DIST.RT](https://support.google.com/docs/answer/9369017): Returns the right tailed Student distribution for a value x.
