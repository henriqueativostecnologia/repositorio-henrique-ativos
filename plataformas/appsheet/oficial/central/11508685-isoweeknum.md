---
fonte: https://support.google.com/appsheet/answer/11508685?hl=en
baixado: 2026-11-10
---

# ISOWEEKNUM()

Number of the ISO week of the year for the specified date

Returns the [number of the ISO week of the year](https://en.wikipedia.org/wiki/ISO_week_date) (1 to 53) for the specified date. If the date is not valid, `0` is returned.

## Sample usage

`ISOWEEKNUM("1/1/2021")` returns `53`

`ISOWEEKNUM("1/4/2021")` returns `1`

`ISOWEEKNUM(TODAY())` returns today's ISO week number. See also [`TODAY()`](https://help.appsheet.com/en/articles/2357327-today')

## Syntax

`ISOWEEKNUM(`*`date`*`)`

- *`date`* *-* Textual value (in quotes) or expression that resolves to a `Date` or `DateTime` value.

## Note

Some constant values, such as `"MM/DD/YYYY"`, are evaluated as a `Date` value by AppSheet. Similarly, `"000:00:00"` is evaluated as a `Duration` value. This doesn't mean your spreadsheet data must use the same formats: the date and time formats in your spreadsheets are determined by the locale/language setting. Column will always be evaluated as the type of column. Additionally, you can convert data, both columns and string literals, to specific types using functions such as `DATE()`, `TIME()`, or `DATETIME()`. 

## See also

[Date and time expressions](https://support.google.com/appsheet/answer/10107326)

[`EOMONTH()`](https://support.google.com/appsheet/answer/10107332)

[`WEEKDAY()`](https://support.google.com/appsheet/answer/10107424)

[`WEEKNUM()`](https://support.google.com/appsheet/answer/10107425)

[`WORKDAY()`](https://support.google.com/appsheet/answer/10107426)
