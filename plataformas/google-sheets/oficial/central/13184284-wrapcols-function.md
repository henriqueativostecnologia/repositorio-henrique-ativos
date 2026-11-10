---
fonte: https://support.google.com/docs/answer/13184284?hl=en
baixado: 2026-11-10
---

# WRAPCOLS function

This function wraps the provided row or column of cells by columns after a specified number of elements to form a new array.

## Sample Usage

`WRAPCOLS(A1:E1, 2)`: A `WRAPCOLS` function that wraps the range with 2 values per column.

`WRAPCOLS(A1:E1, 2, “No value”)`: A `WRAPCOLS` function that wraps the range with 2 values per column and fills the extra cells with “No value.”

## Syntax

`WRAPCOLS(range, wrap_count, [pad_with])`

- `range`: The range to wrap.
- `wrap_count`: The maximum number of cells for each column. If the value isn’t a whole number, it’s rounded down to the nearest whole number.
- `[pad_with]`: The value with which to fill the extra cells in the range. By default, the WRAPCOLS function fills the extra cells with \#N/A.

## Examples

### Wrap simple data with WRAPCOLS

**Example data:**

|       | A   | B   | C   | D   | E   |
|-------|-----|-----|-----|-----|-----|
| **1** | A   | B   | C   | D   | E   |

**Example:** Input this formula in `G1: =WRAPCOLS(A1:E1, 2)`

**Result:**

|       | **G** | **H** | **I** |
|-------|-------|-------|-------|
| **1** | A     | C     | E     |
| **2** | B     | D     | \#N/A |

[Make a Copy](https://docs.google.com/spreadsheets/d/1ZSTYWGVXiCHkLAS-Kmh1J6V3QEXBeWwVBS2FDLJGK5w/copy)

### Wrap data with “No value” as pad with WRAPCOLS

**Example data:**

|       | A   | B   | C   | D   | E   |
|-------|-----|-----|-----|-----|-----|
| **1** | A   | B   | C   | D   | E   |

**Example:** Input this formula in `G1: =WRAPCOLS(A1:E1, 2, "No value")`

**Result:**

|       | **G** | **H** | **I**    |
|-------|-------|-------|----------|
| **1** | A     | C     | E        |
| **2** | B     | D     | No value |

[Make a Copy](https://docs.google.com/spreadsheets/d/1ZSTYWGVXiCHkLAS-Kmh1J6V3QEXBeWwVBS2FDLJGK5w/copy#gid=907400634)

## Related functions

- [WRAPROWS function](https://support.google.com/docs/answer/13184285): This function wraps the provided row or column of cells by rows after a specified number of elements to form a new array.
