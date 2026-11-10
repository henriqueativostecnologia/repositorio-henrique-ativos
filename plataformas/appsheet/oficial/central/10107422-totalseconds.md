---
fonte: https://support.google.com/appsheet/answer/10107422?hl=en
baixado: 2026-11-10
---

# TOTALSECONDS()

Count of seconds in Duration

Returns the number of seconds (`Decimal` value) represented by the given duration of time.

## Sample usage

`TOTALSECONDS("000:00:12")` returns `12`

`TOTALSECONDS("000:15:00")` returns `900` (number of seconds in 15 minutes)

`TOTALSECONDS("024:00:00")` returns `86,400` (number of seconds in 24 hours)

`TOTALSECONDS("024:00:00" + "000:15:00" + "000:00:12")` returns `87,312`; equivalent to `TOTALSECONDS(SUM(LIST("024:00:00", "000:15:00", "000:00:12")))`. See also: [`LIST()`](https://support.google.com/appsheet/answer/10107339), [`SUM()`](https://support.google.com/appsheet/answer/10107699)

`TOTALSECONDS(TIMENOW() - "00:00:00")` returns the number of seconds that have passed from midnight today to now. `TIMENOW()` returns the current `Time`; subtracting one `Time` value (`"00:00:00"`) from another gives the needed `Duration` argument. See also: [`TIMENOW()`](https://support.google.com/appsheet/answer/10107985), [Date and time expressions](https://support.google.com/appsheet/answer/10107326)

## Syntax

`TOTALSECONDS(`*`duration`*`)`

- *`duration`* - A `Duration` value.

## See also

[Date and time expressions](https://support.google.com/appsheet/answer/10107326)

[`HOUR()`](https://support.google.com/appsheet/answer/10107679)

[`MINUTE()`](https://support.google.com/appsheet/answer/10107346)

[`SECOND()`](https://support.google.com/appsheet/answer/10108124)

[`TOTALHOURS()`](https://support.google.com/appsheet/answer/10108287)

[`TOTALMINUTES()`](https://support.google.com/appsheet/answer/10108288)
