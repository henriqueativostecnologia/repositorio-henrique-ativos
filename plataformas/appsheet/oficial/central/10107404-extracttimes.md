---
fonte: https://support.google.com/appsheet/answer/10107404?hl=en
baixado: 2026-11-10
---

# EXTRACTTIMES()

Extract list of Time values within a textual value

Returns a list of `Time` values within the textual value. Includes specific times, times written in prose, and relative times, such as “tomorrow at 3pm”, “one hour from now”, and so on.

## Sample usage

`EXTRACTTIMES("Set a meeting for November 14th at 4pm.")` returns `4:00:00 PM` (list of one item).

`EXTRACTTIMES("Set a meeting for tomorrow at 4pm.")` `4:00:00 PM` (list of one item).

## Syntax

`EXTRACTTIMES(`*`text-to-extract-from`*`)`

- *`text-to-extract-from`* - Any textual value.

## See also

[Date and time expressions](https://support.google.com/appsheet/answer/10107326)

[`EXTRACT()`](https://support.google.com/appsheet/answer/10107889)

[`EXTRACTCHOICE()`](https://support.google.com/appsheet/answer/10107958)

[`EXTRACTDATES()`](https://support.google.com/appsheet/answer/10108193)

[`EXTRACTDATETIMES()`](https://support.google.com/appsheet/answer/10108193)

[`EXTRACTDOMAINS()`](https://support.google.com/appsheet/answer/13124857)

[`EXTRACTDURATIONS()`](https://support.google.com/appsheet/answer/10107333)

[`EXTRACTEMAILS()`](https://support.google.com/appsheet/answer/10107403)

[`EXTRACTHASHTAGS()`](https://support.google.com/appsheet/answer/10107890)

[`EXTRACTMENTIONS()`](https://support.google.com/appsheet/answer/10108195)

[`EXTRACTNUMBERS()`](https://support.google.com/appsheet/answer/10107677)

[`EXTRACTPHONENUMBERS()`](https://support.google.com/appsheet/answer/10106631)

[`EXTRACTPRICES()`](https://support.google.com/appsheet/answer/10107891)
