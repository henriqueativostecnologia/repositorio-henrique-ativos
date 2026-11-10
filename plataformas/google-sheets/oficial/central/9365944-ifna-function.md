---
fonte: https://support.google.com/docs/answer/9365944?hl=en
baixado: 2026-11-10
---

# IFNA function

The IFNA function evaluates a value. If the value is an \#N/A error, return the specified value. 

## Parts of an IFNA function 

`IFNA(value, value_if_na) `

|               |                                                                        |
|---------------|------------------------------------------------------------------------|
| **Part**      | **Description**                                                        |
| `value`       | Required. The value to check if it is a \#N/A error.                   |
| `value_if_na` | Required. The value to return if the first argument is an \#N/A error. |

## Sample formulas 

`IFNA(205, “Na error”) `

`IFNA(#N/A, “Na error”) `

## Notes

- If value or value_if_na is an empty cell, IFNA treats the cell’s value as an empty string (“”).
- If value is a range reference, IFNA returns an array formula result with one entry for in-the-range reference.

## Examples 

|       |                          |            |
|-------|--------------------------|------------|
|       | **A**                    | **B**      |
| **1** | **Formula**              | **Result** |
| **2** | =`IFNA(205, "Na error")` | 205        |

 

|       |                           |            |
|-------|---------------------------|:-----------|
|       | **A**                     | **B**      |
| **1** | **Formula**               | **Result** |
| **2** | =`IFNA(#N/A, “Na error”)` | Na error   |

 

|     |                                |              |
|-----|--------------------------------|--------------|
|     | **A**                          | **B**        |
| 1   | **Formula**                    | **Result**   |
| 2   | =`IFNA(A3:A5, “Has na error”)` |              |
| 3   | \#N/A                          | Has na error |
| 4   | 100/0                          | \#ERROR      |
| 5   | 45                             | 45           |

## Related functions

- [IFERROR](https://support.google.com/docs/answer/3093304): Returns the first argument if it is not an error value, otherwise returns the second argument if present, or a blank if the second argument is absent.
