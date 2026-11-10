---
fonte: https://support.google.com/docs/answer/9084098?hl=en
baixado: 2026-11-10
---

# AVERAGE.WEIGHTED function

The AVERAGE.WEIGHTED function finds the weighted average of a set of values, given the values and the corresponding weights.

## Parts of an AVERAGE.WEIGHTED function

`AVERAGE.WEIGHTED(values, weights, [additional values], [additional weights])`

+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Part**                                           | **Description**                                    | **Notes**                                          |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `values`                                           | The values to be averaged.                         | -   May refer to a range of cells, or may contain  |
|                                                    |                                                    |     the values themselves.                         |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `weights`                                          | The corresponding list of weights to apply.        | -   May refer to a range of cells, or may contain  |
|                                                    |                                                    |     the weights themselves.                        |
|                                                    |                                                    | -   Weights cannot be negative, though they can be |
|                                                    |                                                    |     zero.                                          |
|                                                    |                                                    | -   At least one of the weights must be positive.  |
|                                                    |                                                    | -   If using a range of cells, that range must     |
|                                                    |                                                    |     have the same number of rows and columns as    |
|                                                    |                                                    |     the range of values.                           |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `[additional_values]`                              | Additional values to average.                      | -   Additional values are optional.                |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `[additional_weights]`                             | Additional weights to apply.                       | -   Additional weights are optional, but           |
|                                                    |                                                    |     each `additional_value` must be followed by    |
|                                                    |                                                    |     exactly one `additional_weight`.               |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+

 

## Sample formulas

`AVERAGE.WEIGHTED(10, 1, 20, 3)`

`AVERAGE.WEIGHTED(A1:A2, B1:B2)`

`AVERAGE.WEIGHTED(A1:A2, B1:B2, C1, C2)`

## Examples

This example shows the weighted averages of different numbers and weights:

|       |       |       |                                         |            |
|-------|-------|-------|-----------------------------------------|------------|
|       | **A** | **B** | **C**                                   | **D**      |
| **1** | 2     | 1     | **Formula**                             | **Result** |
| **2** | 4     | 3     | =AVERAGE.WEIGHTED(A1:A2, B1:B2)         | 3.5        |
| **3** | 8     | 6     | =AVERAGE.WEIGHTED(2, 10, 4, 15)         | 3.2        |
| **4** |       |       | =AVERAGE.WEIGHTED(A1:A2, B1:B2, C1, C2) | 6.2        |

 

This example of weighted average calculates someone's grade in a school course:

|       |               |                                 |                               |
|-------|---------------|---------------------------------|-------------------------------|
|       | **A**         | **B**                           | **C**                         |
| **1** | **Item**      | **Grade**                       | **Percentage of final grade** |
| **2** | Homework      | 95                              | 25%                           |
| **3** | Participation | 90                              | 10%                           |
| **4** | Midterm exam  | 85                              | 15%                           |
| **5** | Projects      | 88                              | 20%                           |
| **6** | Final exam    | 82                              | 30%                           |
| **7** |               | **Formula**                     | **Result**                    |
| **8** | Final grade   | =AVERAGE.WEIGHTED(B2:B6, C2:C6) | 87.7                          |

## Related functions

- [SUMPRODUCT](https://support.google.com/docs/answer/3094294): The SUMPRODUCT function calculates the sum of the products of corresponding entries in 2 equally sized arrays or ranges.
- [AVERAGE](https://support.google.com/docs/answer/3093615): The AVERAGE function returns the numerical average value in a dataset, ignoring text.
