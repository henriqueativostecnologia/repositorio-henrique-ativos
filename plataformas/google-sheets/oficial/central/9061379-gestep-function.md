---
fonte: https://support.google.com/docs/answer/9061379?hl=en
baixado: 2026-11-10
---

# GESTEP function

The GESTEP function returns 1 if the rate is strictly greater than or equal to the provided step value, or 0 otherwise. If no step value is provided, then the default value of 0 is used. 

## Parts of a GESTEP function

`GESTEP(value,[step])`

|          |                                                                        |              |
|----------|------------------------------------------------------------------------|--------------|
| **Part** | **Description**                                                        | **Notes**    |
| `value`  | The value to test against the step number.                             |              |
| `step`   | The value to be tested against. It's 0 if the argument is left blank.  | \[OPTIONAL\] |

## Sample formulas

`GESTEP(5, 2)`
`GESTEP(2)`
`GESTEP(-0.00001)`
`GESTEP(-6, -1)`

## Notes

If either `value` or `step` is non-numeric, GESTEP returns \#VALUE!

## Examples

|       |                    |            |
|-------|--------------------|------------|
|       | **A**              | **B**      |
| **1** | **Formula**        | **Result** |
| **2** | `GESTEP(5, 2)`     | 1          |
| **3** | `GESTEP(2)`        | 1          |
| **4** | `GESTEP(-0.00001)` | 0          |
| **5** | `GESTEP(-6, -1)`   | 0          |

## Related function

[DELTA](https://support.google.com/docs/answer/3401147): Compare two numeric values, returning 1 if they're equal.
