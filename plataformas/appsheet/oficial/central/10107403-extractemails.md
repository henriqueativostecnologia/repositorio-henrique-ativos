---
fonte: https://support.google.com/appsheet/answer/10107403?hl=en
baixado: 2026-11-10
---

# EXTRACTEMAILS()

Extract list of Email values within a textual value

Returns a list of `Email` values within the textual value. 

## Sample usage

`EXTRACTEMAILS("Contact AppSheet Support at support@appsheet.com.")` returns a list of one item: `support@appsheet.com` 

`EXTRACTEMAILS("Mailing List: a@a.com, b@b.com, c@c.com")` returns a list of three items: `a@a.com, b@b.com, c@c.com`.

`EXTRACTEMAILS([How can we contact you?])` returns a list of any email addresses the user entered in the `How can we contact you?` column of the form.

## Syntax

`EXTRACTEMAILS(`*`text-to-extract-from`*`)`

- *`text-to-extract-from`* - Any textual value from which a list email addresses are to be extracted.

## See also

[`EXTRACT()`](https://support.google.com/appsheet/answer/10107889)

[`EXTRACTCHOICE()`](https://support.google.com/appsheet/answer/10107958)

[`EXTRACTDATES()`](https://support.google.com/appsheet/answer/10108193)

[`EXTRACTDATETIMES()`](https://support.google.com/appsheet/answer/10108193)

[`EXTRACTDOMAINS()`](https://support.google.com/appsheet/answer/13124857)

[`EXTRACTDURATIONS()`](https://support.google.com/appsheet/answer/10107333)

[`EXTRACTHASHTAGS()`](https://support.google.com/appsheet/answer/10107890)

[`EXTRACTMENTIONS()`](https://support.google.com/appsheet/answer/10108195)

[`EXTRACTNUMBERS()`](https://support.google.com/appsheet/answer/10107677)

[`EXTRACTPHONENUMBERS()`](https://support.google.com/appsheet/answer/10106631)

[`EXTRACTPRICES()`](https://support.google.com/appsheet/answer/10107891)

[`EXTRACTTIMES()`](https://support.google.com/appsheet/answer/10107404)
