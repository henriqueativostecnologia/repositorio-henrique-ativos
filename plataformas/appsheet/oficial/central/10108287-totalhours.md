---
fonte: https://support.google.com/appsheet/answer/10108287?hl=en
baixado: 2026-11-10
---

# TOTALHOURS()

Count of hours (Decimal) in Duration

Returns the number of hours (`Decimal` value) represented by the given duration of time.

## Sample usage

`TOTALHOURS("000:00:18")` returns `0.005` (number of hours in 18 seconds)

`TOTALHOURS("000:15:00")` returns `0.25` (number of hours in 15 minutes)

`TOTALHOURS("024:00:00")` returns `24`

`TOTALHOURS("024:00:00" + "000:15:00" + "000:00:18")` returns `24.255`; equivalent to `TOTALHOURS(SUM(LIST("024:00:00", "000:15:00", "000:00:18")))`. See also: [`LIST()`](https://support.google.com/appsheet/answer/10107339), [`SUM()`](https://support.google.com/appsheet/answer/10107699)

`TOTALHOURS(TIMENOW() - "00:00:00")` returns the number of hours that have passed from midnight today to now. `TIMENOW()` returns the current time; subtracting one `Time` value (`"00:00:00"`) from another gives the needed `Duration` value argument. See also: [`TIMENOW()`](https://support.google.com/appsheet/answer/10107985), [Date and time expressions](https://support.google.com/appsheet/answer/10107326)

### Hours worked this week

    TOTALHOURS(
      SUM(
        SELECT(
          Timesheets[Hours],
          AND(
            ([Employee] = USEREMAIL()),
            ([Date Worked] > (TODAY() - WEEKDAY(TODAY()))),
            ([Date Worked] <= (TODAY() - WEEKDAY(TODAY())) + 7)
          )
        )
      )
    )

1.  `SELECT(Timesheets[Hours], ...)` gathers the `Duration`-type values of the `Hours` column from rows in the `Timesheets` table that match the given criteria (`...` ; see (2)). See also: [`SELECT()`](https://support.google.com/appsheet/answer/10108207)

2.  `AND(..., ..., ...)` includes only rows that match all of the given criteria (see (3), (4), and (5)). See also: [`AND()`](https://support.google.com/appsheet/answer/10107398)

3.  `([Employee] = USEREMAIL())` includes only rows with an `Employee` column value that matches the current app user's email address. See also: [`USEREMAIL()`](https://support.google.com/appsheet/answer/10108210)

4.  `([Date Worked] > (TODAY() - WEEKDAY(TODAY())))` includes only rows for which the `Date Worked` is after the last day of the previous week. See also: [`TODAY()`](https://support.google.com/appsheet/answer/10108286), [`WEEKDAY()`](https://support.google.com/appsheet/answer/10107424)

5.  `([Date Worked] <= (TODAY() - WEEKDAY(TODAY())) + 7)` includes only rows for which the `Date Worked` is on or before the last day of the the current week.

6.  `SUM(...)` computes the total time as a `Duration` value from the gathered daily `Hours` values from (1). See also: [`SUM()`](https://support.google.com/appsheet/answer/10107699)

7.  `TOTALHOURS(...)` converts the `Duration` value from (6) to a `Decimal` value.

## Syntax

`TOTALHOURS(`*`duration`*`)`

- *`duration`* - A `Duration` value.

## See also

[Date and time expressions](https://support.google.com/appsheet/answer/10107326)

[`HOUR()`](https://support.google.com/appsheet/answer/10107679)

[`MINUTE()`](https://support.google.com/appsheet/answer/10107346)

[`SECOND()`](https://support.google.com/appsheet/answer/10108124)

[`TOTALMINUTES()`](https://support.google.com/appsheet/answer/10108288)

[`TOTALSECONDS()`](https://support.google.com/appsheet/answer/10107422)
