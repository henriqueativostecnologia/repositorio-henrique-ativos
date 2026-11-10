---
fonte: https://support.google.com/docs/answer/9368240?hl=en
baixado: 2026-11-10
---

# QUARTILE.EXC function

The QUARTILE.EXC function returns value nearest to a given quartile of a dataset, exclusive of 0 and 4.

## Parts of a QUARTILE.EXC function

`QUARTILE.EXC(data, quartile_number)`

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Part**                                                                      | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `data`                                                                        | The array or range containing the dataset to consider.                        |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `quartile_number`                                                             | This is which quartile value to return                                        |
|                                                                               |                                                                               |
|                                                                               | -   1 returns the value in data closest to the first quartile (25% mark)      |
|                                                                               | -   2 returns the value in data closest to the median (50% mark)              |
|                                                                               | -   3 returns the value in data closest to the third quartile (75% mark)      |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

## Sample formulas

`QUARTILE.EXC(A2:A100, 3)`

`QUARTILE.EXC(A2:A100, B2)`

## Notes

- If the `quartile_number` is not an integer, the number is truncated. 
- The `quartile_number` must be between 0 and 4, exclusive.
- Different from `QUARTILE.INC`, `QUARTILE.EXC` calculates quartile based on a quartile range exclusive of 0th and 4th quartile.

## Examples

|        |          |
|--------|----------|
|        | **A**    |
| **1**  | **data** |
| **2**  | 6        |
| **3**  | 7        |
| **4**  | 15       |
| **5**  | 36       |
| **6**  | 39       |
| **7**  | 40       |
| **8**  | 41       |
| **9**  | 42       |
| **10** | 43       |
| **11** | 47       |
| **12** | 49       |

 

|       |              |            |                            |
|-------|--------------|------------|----------------------------|
|       | **A**        | **B**      | **C**                      |
| **1** | **Quartile** | **Result** | **Formula**                |
| **2** | 1            | 15         | `=QUARTILE.EXC(A2:A12, 1)` |
| **3** | 2            | 40         | `=QUARTILE.EXC(A2:A12, 2)` |
| **4** | 3            | 43         | `=QUARTILE.EXC(A2:A12, 3)` |

## Related functions

- [PERCENTILE](https://support.google.com/docs/answer/3094093): Returns the value at a given percentile of a dataset.
- [PERCENTILE.EXC](https://support.google.com/docs/answer/9368167): The PERCENTILE.EXC function returns the value at a given percentile of a dataset, exclusive of 0 and 1.
- [MEDIAN](https://support.google.com/docs/answer/3094025): Returns the median value in a numeric dataset.
- [QUARTILE](https://support.google.com/docs/answer/3094041): Returns a value nearest to a specified quartile of a dataset.
