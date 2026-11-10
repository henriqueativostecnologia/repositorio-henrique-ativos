---
fonte: https://support.google.com/appsheet/answer/10107333?hl=en
baixado: 2026-11-10
---

# EXTRACTDURATIONS()

Extract list of Duration values within textual value

Returns a list of `Duration` values within textual value.

## Sample usage

`EXTRACTDURATIONS("noon to 4p")` returns `04:00:00` (list of one item).

`EXTRACTDURATIONS("Monday to Friday")` returns `96:00:00` (list of one item).

`EXTRACTDURATIONS("From November 10th to November 12th")` returns `48:00:00` (list of one item).

`EXTRACTDURATIONS("Jan 1 to Feb 1")` returns `744:00:00` (list of one item).

`EXTRACTDURATIONS("Thursday at 10:27 to Sunday at 16:15")` returns `77:48:00` (list of one item).

## Syntax

`EXTRACTDURATIONS(`*`text-to-extract-from`*`)`

- *`text-to-extract-from`* - Any textual value. Includes spans of time between specific dates and times, spans of times written in prose, and relative dates and times, such as `tomorrow`, `yesterday`, `one hour from now`, and so on, as shown in samples above.

## See also

[Date and time expressions](https://support.google.com/appsheet/answer/10107326)

[`EXTRACT()`](https://support.google.com/appsheet/answer/10107889)

[`EXTRACTCHOICE()`](https://support.google.com/appsheet/answer/10107958)

[`EXTRACTDATES()`](https://support.google.com/appsheet/answer/10108193)

[`EXTRACTDATETIMES()`](https://support.google.com/appsheet/answer/10108193)

[`EXTRACTDOMAINS()`](https://support.google.com/appsheet/answer/13124857)

[`EXTRACTEMAILS()`](https://support.google.com/appsheet/answer/10107403)

[`EXTRACTHASHTAGS()`](https://support.google.com/appsheet/answer/10107890)

[`EXTRACTMENTIONS()`](https://support.google.com/appsheet/answer/10108195)

[`EXTRACTNUMBERS()`](https://support.google.com/appsheet/answer/10107677)

[`EXTRACTPHONENUMBERS()`](https://support.google.com/appsheet/answer/10106631)

[`EXTRACTPRICES()`](https://support.google.com/appsheet/answer/10107891)

[`EXTRACTTIMES()`](https://support.google.com/appsheet/answer/10107404)
