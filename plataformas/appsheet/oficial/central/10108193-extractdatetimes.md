---
fonte: https://support.google.com/appsheet/answer/10108193?hl=en
baixado: 2026-11-10
---

# EXTRACTDATETIMES()

Extract list of DateTime values within textual value

Returns a list of `DateTime` values within the textual value.

## Sample usage

`EXTRACTDATETIMES("Set a meeting for November 14th at 4pm.")` returns a list of one item: the date and time for November 14 of the current year at 4:00 PM.

`EXTRACTDATETIMES("Set a meeting for tomorrow at 4pm.")` returns a list of one item: the date and time for tomorrow at 4:00 PM.

## Syntax

`EXTRACTDATETIMES`**`(`***`text-to-extract-from`***`)`**

- *`text-to-extract-from`* - Any textual value. May include specific dates and times, dates and times written in prose, and relative dates and times, such as `tomorrow at 3pm`, `yesterday` `one hour from now`, etc. See samples above.

## Note

Some constant values, such as `"MM/DD/YYYY"`, are evaluated as a `Date` value by AppSheet. Similarly, `"000:00:00"` is evaluated as a `Duration` value. This doesn't mean your spreadsheet data must use the same formats: the date and time formats in your spreadsheets are determined by the locale/language setting. Column will always be evaluated as the type of column. Additionally, you can convert data, both columns and string literals, to specific types using functions such as `DATE()`, `TIME()`, or `DATETIME()`. 

## See also

[Date and time expressions](https://support.google.com/appsheet/answer/10107326)

[`EXTRACT()`](https://support.google.com/appsheet/answer/10107889)

[`EXTRACTCHOICE()`](https://support.google.com/appsheet/answer/10107958)

[`EXTRACTDATES()`](https://support.google.com/appsheet/answer/10108193)

[`EXTRACTDOMAINS()`](https://support.google.com/appsheet/answer/13124857)

[`EXTRACTDURATIONS()`](https://support.google.com/appsheet/answer/10107333)

[`EXTRACTEMAILS()`](https://support.google.com/appsheet/answer/10107403)

[`EXTRACTHASHTAGS()`](https://support.google.com/appsheet/answer/10107890)

[`EXTRACTMENTIONS()`](https://support.google.com/appsheet/answer/10108195)

[`EXTRACTNUMBERS()`](https://support.google.com/appsheet/answer/10107677)

[`EXTRACTPHONENUMBERS()`](https://support.google.com/appsheet/answer/10106631)

[`EXTRACTPRICES()`](https://support.google.com/appsheet/answer/10107891)

[`EXTRACTTIMES()`](https://support.google.com/appsheet/answer/10107404)
