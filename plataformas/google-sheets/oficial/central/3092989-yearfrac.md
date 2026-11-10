---
fonte: https://support.google.com/docs/answer/3092989?hl=en
baixado: 2026-11-10
---

# YEARFRAC

Returns the number of years, including fractional years, between two dates using a specified day count convention.

### Sample Usage

`YEARFRAC(DATE(1969,7,16),DATE(1969,7,24),1)`

`YEARFRAC(A2,A3)`

### Syntax

`YEARFRAC(start_date, end_date, [day_count_convention])`

- `start_date` - The start date to consider in the calculation. Must be a reference to a cell containing a date, a function returning a date type, or a number.

- `end_date` - The end date to consider in the calculation. Must be a reference to a cell containing a date, a function returning a date type, or a number.

- `day_count_convention` - **\[** OPTIONAL - `0` by default **\]** - An indicator of what day count method to use.

  - 0 indicates US (NASD) 30/360 - This assumes 30 day months and 360 day years as per the National Association of Securities Dealers standard, and performs specific adjustments to entered dates which fall at the end of months.

  - 1 indicates Actual/Actual - This calculates based upon the actual number of days between the specified dates, and the actual number of days in the intervening years. Used for US Treasury Bonds and Bills, but also the most relevant for non-financial use.

  - 2 indicates Actual/360 - This calculates based on the actual number of days between the specified dates, but assumes a 360 day year.

  - 3 indicates Actual/365 - This calculates based on the actual number of days between the specified dates, but assumes a 365 day year.

  - 4 indicates European 30/360 - Similar to `0`, this calculates based on a 30 day month and 360 day year, but adjusts end-of-month dates according to European financial conventions.

### Notes

- This function is mostly used in a financial setting, for calculation involving fixed-income securities. Because the most common calculations performed use the NASD standard calendar, this is the default behavior. However, for use in non-financial settings, option `1`, Actual/Actual, is most likely the correct choice.

- Ensure that the inputs to the function are either references to cells containing dates, functions which return date objects such as [`DATE`](https://support.google.com/docs/answer/3092969), [`DATEVALUE`](https://support.google.com/docs/answer/3093039) or [`TO_DATE`](https://support.google.com/docs/answer/3094239), or date serial numbers of the type returned by the [`N`](https://support.google.com/docs/answer/3093357) function.

- `YEARFRAC` does not autoconvert number formats in the same way that Google Sheets does upon direct entry into cells. Therefore, `YEARFRAC(10/10/2000,10/10/2001)` is interpreted as `YEARFRAC(0.005,0.00499750124938)`, the quotients of 10 divided by 10 divided by 2000 and 2001, respectively.

### See Also

[`TO_DATE`](https://support.google.com/docs/answer/3094239): Converts a provided number to a date.

[`N`](https://support.google.com/docs/answer/3093357): Returns the argument provided as a number.

[`DAYS360`](https://support.google.com/docs/answer/3093042): Returns the difference between two days based on the 360-day year used in some financial interest calculations.

[`DATEVALUE`](https://support.google.com/docs/answer/3093039): Converts a provided date string in a known format to a date value.

[`DATE`](https://support.google.com/docs/answer/3092969): Converts a year, month, and day into a date.

### Examples

Calculates the fraction of a year between `start_date` and `end_date` using different `day_count_convention`s.

Embedded content: https://docs.google.com/spreadsheet/pub?key=0As3tAuweYU9QdGNLSmEzQjQ4SC01QW5UOTNOWEhpUkE&single=true&gid=0&output=html&widget=true

Calculates a person's age by combining the `YEARFRAC` and `TODAY` functions, then applying `ROUNDDOWN` to the result to return the number of years.

Embedded content: https://docs.google.com/spreadsheet/pub?key=0As3tAuweYU9QdGNLSmEzQjQ4SC01QW5UOTNOWEhpUkE&single=true&gid=1&output=html&widget=true
