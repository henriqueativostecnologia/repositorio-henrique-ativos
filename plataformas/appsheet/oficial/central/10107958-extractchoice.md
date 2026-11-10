---
fonte: https://support.google.com/appsheet/answer/10107958?hl=en
baixado: 2026-11-10
---

# EXTRACTCHOICE()

Extract one Yes/No value within textual value

Returns one `Yes/No` expression based on whether `yes`, `true`, `no`, or `false` appears first in a string as follows:

- `TRUE` if first occurrence in the text is `yes` or `true`.
- `FALSE` if first occurrence in the text is `no` or `false`.

## Sample usage

`EXTRACTCHOICE("Based on the evidence, I must conclude that yes, he is guilty.")` returns `TRUE` 

`EXTRACTCHOICE("When I ask my son if he wants to eat broccoli, he screams NO!!!")` returns `FALSE` 

## Syntax

`EXTRACTCHOICE(`*`text-to-extract-from`*`)`

- *`text-to-extract-from`* - Any textual value.

## Notes

Returns a single value, unlike the other `EXTRACT()` functions which all return a list of values.

## See also

[`EXTRACT()`](https://support.google.com/appsheet/answer/10107889)

[`EXTRACTDATES()`](https://support.google.com/appsheet/answer/10107402)

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
