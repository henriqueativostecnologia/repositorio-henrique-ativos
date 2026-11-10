---
fonte: https://support.google.com/appsheet/answer/10108288?hl=en
baixado: 2026-11-10
---

# TOTALMINUTES()

Count of minutes in Duration

Returns the number of minutes (`Decimal` value) represented by the given duration of time.

## Sample usage

`TOTALMINUTES("000:00:12")` returns `0.2` (number of minutes in 12 seconds)

`TOTALMINUTES("000:15:00")` returns `15`

`TOTALMINUTES("024:00:00")`returns `1440` (number of minutes in 24 hours)

`TOTALMINUTES("024:00:00" + "000:15:00" + "000:00:12")` returns `1455.2`; equivalent to `TOTALMINUTES(SUM(LIST("024:00:00", "000:15:00", "000:00:12")))`. See also: [`LIST()`](https://support.google.com/appsheet/answer/10107339), [`SUM()`](https://support.google.com/appsheet/answer/10107699)

`TOTALMINUTES(TIMENOW() - "00:00:00")` returns the number of minutes that have passed from midnight today to now. `TIMENOW()` returns the current `Time`; subtracting one `Time` value (`"00:00:00"` ) from another gives the needed `Duration` argument. See also: [`TIMENOW()`](https://support.google.com/appsheet/answer/10107985), [Date and time expressions](https://support.google.com/appsheet/answer/10107326)

## Syntax

`TOTALMINUTES(`*`duration`*`)`

- *`duration`* - A `Duration` value.

## See also

[Date and time expressions](https://support.google.com/appsheet/answer/10107326)

[`HOUR()`](https://support.google.com/appsheet/answer/10107679)

[`MINUTE()`](https://support.google.com/appsheet/answer/10107346)

[`SECOND()`](https://support.google.com/appsheet/answer/10108124)

[`TOTALHOURS()`](https://support.google.com/appsheet/answer/10108287)

[`TOTALSECONDS()`](https://support.google.com/appsheet/answer/10107422)
