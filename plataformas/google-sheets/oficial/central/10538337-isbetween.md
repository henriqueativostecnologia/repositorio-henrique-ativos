---
fonte: https://support.google.com/docs/answer/10538337?hl=en
baixado: 2026-11-10
---

# ISBETWEEN

Checks whether a provided number is between two other numbers either inclusively or exclusively.

### Parts of a ISBETWEEN function

`ISBETWEEN(value_to_compare, lower_value, upper_value, lower_value_is_inclusive, upper_value_is_inclusive)`

|                                       |                                                                                      |
|---------------------------------------|--------------------------------------------------------------------------------------|
| **Part**                              | **Description**                                                                      |
| value_to_compare                      | The value to test as being between \`lower_value\` and \`upper_value\`.              |
| lower_value                           | The lower boundary of the range of values that \`value_to_compare\` can fall within. |
| upper_value                           | The upper boundary of the range of values that \`value_to_compare\` can fall within. |
| lower_value_is_inclusive \[optional\] | Whether the range of values includes the \`lower_value\`. By default this is TRUE    |
| upper_value_is_inclusive \[optional\] | Whether the range of values includes the \`upper_value\`. By default this is TRUE    |

 

### Examples

Short description of the example being shown below. Feel free to add more rows and columns to the table below if needed.

 

|                                            |            |
|--------------------------------------------|------------|
| **FORMULA**                                | **OUTPUT** |
| =ISBETWEEN(7.9, 1.2, 12.45)                | TRUE       |
| =ISBETWEEN(1.2, 1.2, 12.45, TRUE)          | TRUE       |
| =ISBETWEEN(1.2, 1.2, 12.45, FALSE)         | FALSE      |
| =ISBETWEEN(12.45, 1.2, 12.45, TRUE, TRUE)  | TRUE       |
| =ISBETWEEN(12.45, 1.2, 12.45, TRUE, FALSE) | FALSE      |
| =ISBETWEEN(7.9, 1.2, 12.45, FALSE, FALSE)  | TRUE       |

 

### Related functions

- [GT](https://support.google.com/docs/answer/3098240)
- [GTE](https://support.google.com/docs/answer/3093975)
- [LT](https://support.google.com/docs/answer/3093596)
- [LTE](https://support.google.com/docs/answer/3093976)
