---
fonte: https://support.google.com/appsheet/answer/10107891?hl=en
baixado: 2026-11-10
---

# EXTRACTPRICES()

Extract list of price values within a textual value

Returns a list of prices (`Decimal` values) within the textual value.

## Sample usage

`EXTRACTPRICES("So, we've got a frappuccino for $3.49, a chocolate muffin for $2.49, and a chocolate milk for 99 cents, for a total of $6.97. Will that be all?")` returns `$3.49, $2.49, $0.99, $6.97` (a list of four values)

## Syntax

`EXTRACTPRICES(text-to-extract-from)`

- `text-to-extract-from` - Any textual value.

## Notes

Note that prices in this case means only numeric values that are prefixed by a currency symbol (such as \$, £, ¥, and so on). If there's a demand for it, we may in the future offer an extract option that also gets all “currency-like-but-not-currency-symbol-prefixed” values as well. In the meantime, use [`EXTRACTNUMBERS()`](https://support.google.com/appsheet/answer/10107677) if you’d like to get all number-like entities from your text.

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

[`EXTRACTNUMBERS()`](https://support.google.com/appsheet/answer/10107677)

[`EXTRACTPHONENUMBERS()`](https://support.google.com/appsheet/answer/10106631)

[`EXTRACTTIMES()`](https://support.google.com/appsheet/answer/10107404)
