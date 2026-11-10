---
fonte: https://support.google.com/docs/answer/9368267?hl=en
baixado: 2026-11-10
---

# MODE.MULT function

The MODE.MULT function returns the most commonly occurring values in a dataset.

## Parts of a MODE.MULT function

`MODE.MULT(value1, value2)`

|          |                                                                               |
|----------|-------------------------------------------------------------------------------|
| **Part** | **Description**                                                               |
| `value1` | The first value or range to consider when calculating mode.                   |
| `value2` | \[Repeatable\] Additional values or ranges to consider when calculating mode. |

## Notes

- `MODE.MULT` returns an error if all values occur only once.
- `MODE.MULT` returns an array formula result.

## Examples

|       |                                        |            |
|-------|----------------------------------------|------------|
|       | **A**                                  | **B**      |
| **1** | **Raw formula**                        | **Output** |
| **2** | `=MODE.MULT({10, 15, 20, 30, 10, 15})` | 10         |
| **3** |                                        | 15         |

## Related functions

- [MODE](https://support.google.com/docs/answer/3094029): Returns the most commonly occurring value in a dataset.
