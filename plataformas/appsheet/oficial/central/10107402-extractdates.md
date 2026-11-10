---
fonte: https://support.google.com/appsheet/answer/10107402?hl=en
baixado: 2026-11-10
---

# EXTRACTDATES()

Extract list of dates within textual value

Returns list of `Date` values within a textual value.

## Sample usage

`EXTRACTDATES("Set a meeting for November 14th at 4pm.")` returns a list of one item: the date of November 14 of the current year.

`EXTRACTDATES("Set a meeting for tomorrow.")` returns a list with one item: tomorrow's date.

`EXTRACTDATES("Yesterday, today, and tomorrow.")` returns a list with thee items: the dates equivalent to `(TODAY() - 1)`, `TODAY()`, and `(TODAY() + 1)`.

`EXTRACTDATES("1 month 3 days ago; 7 years 2 months 4 days ago; 2 weeks from tomorrow; in 4 days")` returns a list with the corresponding relative dates.

`EXTRACTDATES("first of last month; first of this month; first of next month; 15th of this month; first day of next year")` returns a list with the corresponding relative dates.

`EXTRACTDATES("Monday; last Monday; this Monday; next Monday; Monday 2 weeks from now")` returns a list with the corresponding relative dates.

`EXTRACTDATES("March")` returns a list with two dates, the first day of the given month of the current year and the first day of the following month: `3/1/2021`, `4/1/2021`.

`EXTRACTDATES("2020")` returns a list with two dates, the first day of the given year and the first day of the following year: `1/1/2020`, `1/1/2021`. Any four-digit value between 1900 and 2050 (inclusive) are handled as such.

## Syntax

`EXTRACTDATES`**`(`***`text-to-extract-from`***`)`**

- *`text-to-extract-from`* - Any textual value. May include specific dates, dates written in prose, relative dates (such as `tomorrow` or `yesterday`), day and month names, and bare 4-digit year numbers. See samples above.

## Note

Some constant values, such as `"MM/DD/YYYY"`, are evaluated as a `Date` value by AppSheet. Similarly, `"000:00:00"` is evaluated as a `Duration` value. This doesn't mean your spreadsheet data must use the same formats: the date and time formats in your spreadsheets are determined by the locale/language setting. Column will always be evaluated as the type of column. Additionally, you can convert data, both columns and string literals, to specific types using functions such as `DATE()`, `TIME()`, or `DATETIME()`. 

## See also

[Date and time expressions](https://support.google.com/appsheet/answer/10107326)

[`EXTRACT()`](https://support.google.com/appsheet/answer/10107889)

[`EXTRACTCHOICE()`](https://support.google.com/appsheet/answer/10107958)

[`EXTRACTDATETIMES()`](https://support.google.com/appsheet/answer/10108193)

[`EXTRACTDOMAINS()`](https://support.google.com/appsheet/answer/13124857)

[`EXTRACTDURATIONS()`](https://support.google.com/appsheet/answer/10107333)

[`EXTRACTEMAILS()`](https://support.google.com/appsheet/answer/10107403)

[`EXTRACTHASHTAGS()`](https://support.google.com/appsheet/answer/10107890)

[`EXTRACTMENTIONS()`](https://support.google.com/appsheet/answer/10108195)

[`EXTRACTNUMBERS()`](https://support.google.com/appsheet/answer/10107677)

[`EXTRACTPHONENUMBERS()`](https://support.google.com/appsheet/answer/10106631)

[`EXTRACTPRICES()`](https://support.google.com/appsheet/answer/10107891)

[`EXTRACTTIMES()`](https://support.google.com/appsheet/answer/10107404)
