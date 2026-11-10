---
fonte: https://support.google.com/appsheet/answer/10108195?hl=en
baixado: 2026-11-10
---

# EXTRACTMENTIONS()

Extract list of mentions within a textual value

Returns a list of `Text` values that represent the mentions within the textual value. Each mention will include its `@` sign at the front.

## Sample usage

`EXTRACTMENTIONS("Hey @channel, I have an urgent support issue that I need to address! @macguyver @RobertPaulson")`  returns `@channel, @macguyver, @RobertPaulson` (a list),

## Syntax

`EXTRACTMENTIONS(`*`text-to-extract-from`*`)`

- *`text-to-extract-from`* - Any textual value.

## See also

[`EXTRACT()`](https://support.google.com/appsheet/answer/10107889)

[`EXTRACTCHOICE()`](https://support.google.com/appsheet/answer/10107958)

[`EXTRACTDATES()`](https://support.google.com/appsheet/answer/10108193)

[`EXTRACTDATETIMES()`](https://support.google.com/appsheet/answer/10108193)

[`EXTRACTDOMAINS()`](https://support.google.com/appsheet/answer/13124857)

[`EXTRACTDURATIONS()`](https://support.google.com/appsheet/answer/10107333)

[`EXTRACTEMAILS()`](https://support.google.com/appsheet/answer/10107403)

[`EXTRACTHASHTAGS()`](https://support.google.com/appsheet/answer/10107890)

[`EXTRACTNUMBERS()`](https://support.google.com/appsheet/answer/10107677)

[`EXTRACTPHONENUMBERS()`](https://support.google.com/appsheet/answer/10106631)

[`EXTRACTPRICES()`](https://support.google.com/appsheet/answer/10107891)

[`EXTRACTTIMES()`](https://support.google.com/appsheet/answer/10107404)
