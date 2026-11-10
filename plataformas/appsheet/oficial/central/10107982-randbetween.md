---
fonte: https://support.google.com/appsheet/answer/10107982?hl=en
baixado: 2026-11-10
---

# RANDBETWEEN()

Random integer from range

Returns a randomly-chosen integer (`Number` value) that falls within the specified lower and upper bounds.

## Sample usage

`RANDBETWEEN(1, 10)` returns a random whole number between `1` and `10`.

`(RANDBETWEEN(0, 1) = 1)` returns a random `Yes/No` value.

`(RANDBETWEEN(0, 100) / 100.0)` returns a random `Decimal` value between `0.00` and `1.00` with two digits after the decimal point.

`INDEX({"Heads", "Tails"}, RANDBETWEEN(1, 2))` returns `Heads` or `Tails` as a `Text` value.  See also: [`INDEX()`](https://support.google.com/appsheet/answer/10107336)

`MID("ABCDE", RANDBETWEEN(1, 5), 1)` returns a random letter from *A* to *E* as a `Text` value. See also: [`MID()`](https://support.google.com/appsheet/answer/10107345)

`INDEX(Students[Name], RANDBETWEEN(1, COUNT(Students[Name])))` returns a randomly-chosen student's name. See also: [`COUNT()`](https://support.google.com/appsheet/answer/10107676)

`ORDERBY(Cards[Card ID], RANDBETWEEN(1, 52))` returns the list of `Card ID` column values in a random order. See also: [`ORDERBY()`](https://support.google.com/appsheet/answer/10107362)

## Syntax

`RANDBETWEEN(`*`lower-bound`*`, `*`upper-bound`*`)`

- *`lower-bound`* - Any numeric type that specifies the lowest random value that may be returned.
- *`upper-bound`* - Any numeric type that specifies the highest random value that may be returned.

## See also

[`UNIQUEID()`](https://support.google.com/appsheet/answer/10108209)
