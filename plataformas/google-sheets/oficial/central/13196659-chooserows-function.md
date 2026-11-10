---
fonte: https://support.google.com/docs/answer/13196659?hl=en
baixado: 2026-11-10
---

# CHOOSEROWS function

This function creates a new array from the selected rows in the existing range.

## Sample Usage

`CHOOSEROWS(A2:B5, 1, 3, 1)`

`CHOOSEROWS(A2:B5, -1, -2, -3)`

## Syntax

`CHOOSEROWS(array, row_num1, [row_num2])`

- `array`: The array that contains the rows to be returned.
- `row_num1`: The row number of the first row to be returned.
- `row_num2…`: **\[** OPTIONAL **\]** The row number(s) of additional row(s) to be returned.

## Examples

### Simple data extraction operation with CHOOSEROWS

 

**Example data:**

 

|       | **A**       | **B**      |
|-------|-------------|------------|
| **1** | **Student** | **Grades** |
| **2** | Harry       | 95         |
| **3** | Jenny       | 85         |
| **4** | Lily        | 76         |
| **5** | Sunny       | 60         |

 

**Example:** Input this formula in D1: `=CHOOSEROWS(A1:B5, 1, 2, 4, 2)`

**Result:**

 

|       | **D**   | **E** |
|-------|---------|-------|
| **1** | Student | Grade |
| **2** | Harry   | 95    |
| **3** | Lily    | 76    |
| **4** | Harry   | 95    |

[Make a Copy](https://docs.google.com/spreadsheets/d/1r_WASEs19y3Ybu_YEjz5FA782esbxbdDApbspIlBqSM/copy)

 

### Simple data extraction with CHOOSEROWS selecting rows ranked from the bottom

 

**Example data:**

 

|       | **A**       | **B**     |
|-------|-------------|-----------|
| **1** | **Student** | **Grade** |
| **2** | Harry       | 95        |
| **3** | Jenny       | 85        |
| **4** | Lily        | 76        |
| **5** | Sunny       | 60        |

 

**Example:** Input this formula in D1: `=CHOOSEROWS(A1:B5, 1, -1, -2, -3)`

**Result:**

|       | **D**   | **E** |
|-------|---------|-------|
| **1** | Student | Grade |
| **2** | Sunny   | 60    |
| **3** | Lily    | 76    |
| **4** | Jenny   | 85    |

***[Make a Copy](https://docs.google.com/spreadsheets/d/1r_WASEs19y3Ybu_YEjz5FA782esbxbdDApbspIlBqSM/copy#gid=350337179)***

## Related functions

- [CHOOSECOLS](https://support.google.com/docs/answer/13197914)
