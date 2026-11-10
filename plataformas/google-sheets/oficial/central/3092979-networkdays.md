---
fonte: https://support.google.com/docs/answer/3092979?hl=en
baixado: 2026-11-10
---

# NETWORKDAYS

Returns the number of net working days between two provided days.

### Sample Usage 

`NETWORKDAYS(DATE(1969,7,16),DATE(1969,7,24))`

`NETWORKDAYS(A2,B2)`

`NETWORKDAYS(40909,40924)`

`NETWORKDAYS(40900,40950,{40909,40924})`

### Syntax

`NETWORKDAYS(start_date, end_date, [holidays])`

- `start_date` - The start date of the period from which to calculate the number of net working days.

- `end_date` - The end date of the period from which to calculate the number of net working days.

- `holidays` - **\[** OPTIONAL **\]** - A range or array constant containing the date serial numbers to consider holidays.

  - The values provided within an array for `holidays` must be date serial number values, as returned by [`N`](https://support.google.com/docs/answer/3093357) or date values, as returned by [`DATE`](https://support.google.com/docs/answer/3092969), [`DATEVALUE`](https://support.google.com/docs/answer/3093039) or [`TO_DATE`](https://support.google.com/docs/answer/3094239). Values specified by a range should be standard date values or date serial numbers.

### Notes

- `NETWORKDAYS` does not autoconvert number formats in the same way that Google Sheets does upon direct entry into cells. Therefore, `NETWORKDAYS(10/10/2000,10/10/2001)` is interpreted as `NETWORKDAYS(0.005,0.00499750124938)`, the quotients of 10 divided by 10 divided by 2000 and 2001, respectively.

- `NETWORKDAYS` calculates the number of work days between two dates. To calculate the working day a specific number of days ahead of a date, use [`WORKDAY`](https://support.google.com/docs/answer/3093059).

- `NETWORKDAYS` works similarly to `NETWORKDAYS.INTL` but only treats Saturday and Sunday as the weekend. Use `NETWORKDAYS.INTL` to use other days of the week as the weekend.

### See Also

[`NETWORKDAYS.INTL`](https://support.google.com/docs/answer/3295902): Returns the number of net working days between two provided days excluding specified weekend days and holidays.

[`WORKDAY`](https://support.google.com/docs/answer/3093059): Calculates the end date after a specified number of working days.

[`TO_DATE`](https://support.google.com/docs/answer/3094239): Converts a provided number to a date.

[`N`](https://support.google.com/docs/answer/3093357): Returns the argument provided as a number.

[`DATEVALUE`](https://support.google.com/docs/answer/3093039): Converts a provided date string in a known format to a date value.

[`DATE`](https://support.google.com/docs/answer/3092969): Converts a year, month, and day into a date.

### Examples

Returns the number of workdays between the `start_date` and `end_date` (based on the given list of holidays).

Embedded content: https://docs.google.com/spreadsheet/pub?key=0As3tAuweYU9QdGtzaDluSEpYSFhvVVlseHdQOXczQlE&single=true&gid=0&output=html&widget=true
