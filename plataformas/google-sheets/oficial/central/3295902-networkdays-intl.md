---
fonte: https://support.google.com/docs/answer/3295902?hl=en
baixado: 2026-11-10
---

# NETWORKDAYS.INTL

Returns the number of net working days between two provided days excluding specified weekend days and holidays.

### Sample Usage

`NETWORKDAYS.INTL(DATE(1969, 7, 16), DATE(1969, 7, 24), 1, A1:A10)`

`NETWORKDAYS.INTL(DATE(1969, 7, 16), DATE(1969, 7, 24))`

`NETWORKDAYS.INTL("12/04/1995", "12/22/1995", 3)`

`NETWORKDAYS.INTL("12/04/1995", "12/22/1995", “0000011”)`

### Syntax

`NETWORKDAYS.INTL(start_date, end_date, [weekend], [holidays])`

- `start_date` - The start date of the period from which to calculate the number of net working days.
- `end_date` - The end date of the period from which to calculate the number of net working days.
- `weekend` - **\[** OPTIONAL - `1` by default **\]** - A number or string representing which days of the week are considered weekends.
  - **String method**: weekends can be specified using seven 0’s and 1’s, where the first number in the set represents Monday and the last number is for Sunday. A zero means that the day is a work day, a 1 means that the day is a weekend. For example, “0000011” would mean Saturday and Sunday are weekends.
  - **Number method**: instead of using the string method above, a single number can be used. 1 = Saturday/Sunday are weekends, 2 = Sunday/Monday, and this pattern repeats until 7 = Friday/Saturday. 11 = Sunday is the only weekend, 12 = Monday is the only weekend, and this pattern repeats until 17 = Saturday is the only weekend.
- `holidays` - **\[** OPTIONAL **\]** - A range or array constant containing the dates to consider as holidays.
  - The values provided within an array for `holidays` must be date serial number values, as returned by [`N`](https://support.google.com/docs/answer/3093357) or date values, as returned by [`DATE`](https://support.google.com/docs/answer/3092969), [`DATEVALUE`](https://support.google.com/docs/answer/3093039) or [`TO_DATE`](https://support.google.com/docs/answer/3094239). Values specified by a range should be standard date values or date serial numbers.

### Notes

- `NETWORKDAYS.INTL` does not autoconvert number formats in the same way that Google Sheets does upon direct entry into cells. Therefore, `NETWORKDAYS.INTL(10/10/2000,10/10/2001)` is interpreted as `NETWORKDAYS.INTL(0.005,0.00499750124938)`, the quotients of 10 divided by 10 divided by 2000 and 2001, respectively.

- `NETWORKDAYS.INTL` calculates the number of work days between two dates. To calculate the working days a specific number of days ahead of a date, use [`WORKDAY.INTL`](https://support.google.com/docs/answer/3294972).

- `NETWORKDAYS.INTL` works similarly to `NETWORKDAYS` but also allows weekend days to be specified (for areas where Saturday and Sunday are not considered the weekend).

### See Also

[`NETWORKDAYS`](https://support.google.com/docs/answer/3092979): Returns the number of net working days between two provided days.

[`WORKDAY.INTL`](https://support.google.com/docs/answer/3294972): Calculates the date after a specified number of workdays excluding specified weekend days and holidays.

[`EDATE`](https://support.google.com/docs/answer/3092974): Returns a date a specified number of months before or after another date.

[`EOMONTH`](https://support.google.com/docs/answer/3093044): Returns a date representing the last day of a month which falls a specified number of months before or after another date.

[`NOW`](https://support.google.com/docs/answer/3092981): Returns the current date and time as a date value.
