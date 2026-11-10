---
fonte: https://support.google.com/appsheet/answer/10107677?hl=en
baixado: 2026-11-10
---

# EXTRACTNUMBERS()

Extract list of numeric values within a textual value

Returns a list of `Decimal` values within the textual value.

## Sample usage

`EXTRACTNUMBERS("My name is Theo and I’m three and a half years old!")` returns `3.5` (list of one `Decimal` value).

`EXTRACTNUMBERS("Tommy: I left a message. Richard: Really, what number did you call? Tommy: Two, four, niner, five, six, seven…”)` returns `2`, `4`, `5`, `6`, `7` (list of five `Number` values; note that `niner` is not recognized as a number). 

`EXTRACT("NUMBERS", "The address is 330 SW Main St, 97229”)` returns `330`, `97299` (list of two `Number` values).

## Syntax

`EXTRACTNUMBERS(`*`text-to-extract-from`*`)`

- *`text-to-extract-from`* - Any textual value.

## See also

[`EXTRACT()`](https://support.google.com/appsheet/answer/10107889)

[`EXTRACTCHOICE()`](https://support.google.com/appsheet/answer/10107958)

[`EXTRACTDATES()`](https://support.google.com/appsheet/answer/10108193)

[`EXTRACTDATETIMES()`](https://support.google.com/appsheet/answer/10108193)

[`EXTRACTDOMAINS()`](https://support.google.com/appsheet/answer/13124857)

[`EXTRACTDURATIONS()`](https://support.google.com/appsheet/answer/10107333)

[`EXTRACTEMAILS()`](https://support.google.com/appsheet/answer/10107403)

[`EXTRACTHASHTAGS()`](https://support.google.com/appsheet/answer/10107890)

[`EXTRACTMENTIONS()`](https://support.google.com/appsheet/answer/10108195)

[`EXTRACTPHONENUMBERS()`](https://support.google.com/appsheet/answer/10106631)

[`EXTRACTPRICES()`](https://support.google.com/appsheet/answer/10107891)

[`EXTRACTTIMES()`](https://support.google.com/appsheet/answer/10107404)
