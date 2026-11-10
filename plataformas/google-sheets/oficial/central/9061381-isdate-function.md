---
fonte: https://support.google.com/docs/answer/9061381?hl=en
baixado: 2026-11-10
---

# ISDATE function

The ISDATE function returns whether a value is a date. 

## Parts of an ISDATE function

`ISDATE(value)`

|          |                                     |
|----------|-------------------------------------|
| **Part** | **Description**                     |
| `value`  | The value to be verified as a date. |

## Sample formulas

`ISDATE("7/20/1969")`
`ISDATE(“July 20”)`
`ISDATE(A1)`

## Notes

Ensure your date has quotation marks around it, unless it’s a reference to a cell.

## Examples

|       |                           |            |
|-------|---------------------------|------------|
|       | **A**                     | **B**      |
| **1** | **Formula**               | **Result** |
| **2** | `=ISDATE(“July 20 1969”)` | TRUE       |
| **3** | `=ISDATE(“1969-20-07”)`   | TRUE       |
| **4** | `=ISDATE(“July”)`         | FALSE      |
| **5** | `=ISDATE(“Feb 30”)`       | FALSE      |
