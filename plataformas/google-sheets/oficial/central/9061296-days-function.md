---
fonte: https://support.google.com/docs/answer/9061296?hl=en
baixado: 2026-11-10
---

# DAYS function

The DAYS function returns the number of days between two dates.

## Parts of a DAYS function

`DAYS(end_date,start_date)`

|              |                              |           |
|--------------|------------------------------|-----------|
| **Part**     | **Description**              | **Notes** |
| `end_date`   | The end of the date range.   |           |
| `start_date` | The start of the date range. |           |

## Sample formulas

`DAYS("7/24/1969", "7/16/1969")`
`DAYS(“2/28/2016”, “2/28/2017”)`

## Notes

The DAYS function factors in leap days. 

## Examples

The below example shows the difference between two days in the same month.  

|       |                                   |            |
|-------|-----------------------------------|------------|
|       | **A**                             | **B**      |
| **1** | **Formula**                       | **Result** |
| **2** | `=DAYS("7/24/1969", "7/16/1969")` | 8          |

The below example shows the difference between two dates factoring in a leap day:

|       |                                   |            |
|-------|-----------------------------------|------------|
|       | **A**                             | **B**      |
| **1** | **Formula**                       | **Result** |
| **2** | `=DAYS(“2/28/2016”, “2/28/2017”)` | 366        |

## Related functions

- [DAY](https://support.google.com/docs/answer/3093040): Returns the day of the month that a specific date falls on, in numeric format.
- [DAYS360](https://support.google.com/docs/answer/3093042): Returns the difference between two days based on the 360-day year used in some financial interest calculations.
- [NETWORKDAYS](https://support.google.com/docs/answer/3092979): Returns the number of net working days between two provided days.
