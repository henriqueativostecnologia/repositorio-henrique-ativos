---
fonte: https://support.google.com/appsheet/answer/13124857?hl=en
baixado: 2026-11-10
---

# EXTRACTDOMAINS()

Extract list of domain values within a textual value

Returns a list of domains within the textual value. 

## Sample usage

`EXTRACTDOMAINS("Contact AppSheet Support at support@appsheet.com.")` returns a list of one item: `appsheet.com` 

`EXTRACTDOMAINS("Mailing List: a@a.com, b@b.com, c.com")` returns a list of two items: `a.com, b.com`.

`EXTRACTDOMAINS([How can we contact you?])` returns a list of domains extracted from any email addresses the user entered in the `How can we contact you?` column of the form.

## Syntax

`EXTRACTDOMAINS(`*`text-to-extract-from`*`)`

- *`text-to-extract-from`* - Any textual value from which a list of domains are to be extracted.

## See also

[`DOMAINOF()`](https://support.google.com/appsheet/answer/13127104)

[`EXTRACT()`](https://support.google.com/appsheet/answer/10107889)

[`EXTRACTCHOICE()`](https://support.google.com/appsheet/answer/10107958)

[`EXTRACTDATES()`](https://support.google.com/appsheet/answer/10108193)

[`EXTRACTDATETIMES()`](https://support.google.com/appsheet/answer/10108193)

[`EXTRACTDURATIONS()`](https://support.google.com/appsheet/answer/10107333)

[`EXTRACTEMAILS()`](https://support.google.com/appsheet/answer/10107403)

[`EXTRACTHASHTAGS()`](https://support.google.com/appsheet/answer/10107890)

[`EXTRACTMENTIONS()`](https://support.google.com/appsheet/answer/10108195)

[`EXTRACTNUMBERS()`](https://support.google.com/appsheet/answer/10107677)

[`EXTRACTPHONENUMBERS()`](https://support.google.com/appsheet/answer/10106631)

[`EXTRACTPRICES()`](https://support.google.com/appsheet/answer/10107891)

[`EXTRACTTIMES()`](https://support.google.com/appsheet/answer/10107404)
