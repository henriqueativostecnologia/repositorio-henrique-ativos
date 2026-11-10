---
fonte: https://support.google.com/appsheet/answer/10107326?hl=en
baixado: 2026-11-10
---

# Date and time expressions

Incorporate dates and times into the behavior of your app

Date and time expressions use `Date` or `Duration` values to produce a `DateTime`, `Date`, `Time`, `Duration`, or `Number` value.

The following sections describe the components for building date and time expressions:

- [Current date and time functions](#date-time-expressions)
- [Time component functions](#time-expressions)
- [Date component functions](#date-expressions)
- [Legacy operators](#legacy)
- [Examples](#examples)

**New to expressions?** See also [Expressions: The Essentials](https://support.google.com/appsheet/answer/10104642).

## Current date and time functions

- [`NOW()`](https://support.google.com/appsheet/answer/10108119) for the current `DateTime` on the user's device.
- [`TIMENOW()`](https://support.google.com/appsheet/answer/10107985) for the current `Time` on the user's device. Equivalent to `TIME(NOW())`. See also [`TIME()`](https://support.google.com/appsheet/answer/10107367).
- [`TODAY()`](https://support.google.com/appsheet/answer/10108286) for the current `Date` on the user's device. Equivalent to `DATE(NOW())`. See also [`DATE()`](https://support.google.com/appsheet/answer/10107957).
- [`UTCNOW()`](https://support.google.com/appsheet/answer/10107371) for the current `DateTime`  in [Coordinated Universal Time (UTC)](https://en.wikipedia.org/wiki/Coordinated_Universal_Time). 

The values returned by `NOW()`, `TODAY()`,  and `TIMENOW()` reflect the timezone offset of the user's device. For example, if the timezone of the user's device is Pacific Standard Time (PST), the value returned is UTC-08:00; if the timezone of the user's device is Hong Kong, the value returned is UTC+8:00.

When the user's device contacts the server to read or update data, the device includes its timezone with the request. The server uses the timezone of the user's device when performing time and date calculations. For example, when the server evaluates security filters and workflow rules that include dates and times.

To understand how your mobile device's locale or browser's language setting can impact the format of the returned value, see [Considerations for apps using Date, Time, and DateTime formats](https://support.google.com/appsheet/answer/10106702).

## Time component functions

- [`EXTRACTDURATIONS()`](https://support.google.com/appsheet/answer/10107333) to extract a list of `Duration` values within a textual value.
- [`EXTRACTTIMES()`](https://support.google.com/appsheet/answer/10107404) to extract a list of `Time` values within a textual value.
- [`HOUR()`](https://support.google.com/appsheet/answer/10107679) for the hour component of a specific `Duration`.
- [`MINUTE()`](https://support.google.com/appsheet/answer/10107346) for the minute component of a specific `Duration`.
- [`SECOND()`](https://support.google.com/appsheet/answer/10108124) for the second component of a specific `Duration`.
- [`TIME()`](https://support.google.com/appsheet/answer/10107367) for the `Time` from `Date`, `DateTime`, or `Time`.
- [`TOTALHOURS()`](https://support.google.com/appsheet/answer/10108287) for count of hours in `Duration`.
- [`TOTALMINUTES()`](https://support.google.com/appsheet/answer/10108288) for count of minutes in `Duration`.
- [`TOTALSECONDS()`](https://support.google.com/appsheet/answer/10107422) for count of seconds in `Duration`.

Note that each of `HOUR()`, `MINUTE()`, and `SECOND()` accept as input a `Duration` value, not a `Time` value. To convert a `Time` value to a `Duration` value, subtract another `Time` value. For instance, to convert the current time-of-day to a `Duration`: `TIMENOW() - "00:00:00"`.

## Date component functions

- [`DATE()`](https://support.google.com/appsheet/answer/10107957)for the `Date` from `Date`, `DateTime`, or `Time`.
- [`DATETIME()`](https://support.google.com/appsheet/answer/10108190)for the `DateTime` from `Date`, `DateTime`, or `Time`.
- [`DAY()`](https://support.google.com/appsheet/answer/10107401)for the day of the month from a `Date`.
- [`EOMONTH()`](https://support.google.com/appsheet/answer/10107332) calculates the last day of a month some number of months away, factoring in different month lengths and leap years.
- [`EOWEEK()`](https://support.google.com/appsheet/answer/10108191) calculates the date of the last day of a week from `Date` or `DateTime`.
- [`EWOMONTH()`](https://support.google.com/appsheet/answer/10108192) calculates the date of the last weekday (Monday through Friday) of the month specified by the `Date` or `DateTime` value.
- [`EXTRACTDATES()`](https://support.google.com/appsheet/answer/10107402) to extract a list of `Date` values within a textual value.
- [`EXTRACTDATETIMES()`](https://support.google.com/appsheet/answer/10108193) to extract a list of `DateTime` values within a textual value.
- [`ISOWEEKNUM()`](https://support.google.com/appsheet/answer/11508685)for the ISO week number from `Date` or `DateTime`.
- [`MONTH()`](https://support.google.com/appsheet/answer/10107922) for the month number from a `Date`.
- [`WEEKDAY()`](https://support.google.com/appsheet/answer/10107424) for the day number from a `Date`. Sunday is `1`, Saturday is `7`.
- [`WEEKNUM()`](https://support.google.com/appsheet/answer/10107425) for the week number from a `Date`. A week begins on Sunday.
- [`WORKDAY()`](https://support.google.com/appsheet/answer/10107426) returns a date some number of days away, ignoring weekends and other designated days.
- [`YEAR()`](https://support.google.com/appsheet/answer/10107427) for the year from a `Date`.

Some constant values, such as `"MM/DD/YYYY"`, are evaluated as a `Date` value by AppSheet. Similarly, `"000:00:00"` is evaluated as a `Duration` value. This doesn't mean your spreadsheet data must use the same formats: the date and time formats in your spreadsheets are determined by the locale/language setting. Column will always be evaluated as the type of column. Additionally, you can convert data, both columns and string literals, to specific types using functions such as `DATE()`, `TIME()`, or `DATETIME()`. 

### **Formatting dates and times as text**

- [`TEXT()`](https://support.google.com/appsheet/answer/10107701) accepts a `DateTime`, `Date`, or `Time` and a format string, and returns a text representation.

## Legacy operators

For backwards compatibility, we also support the function syntax below for a set of functions that have been supported from the earliest AppSheet release.

- `@(_NOW)` is equivalent to [`NOW()`](https://support.google.com/appsheet/answer/10108119).
- `@(_TODAY)` is equivalent to [`TODAY()`](https://support.google.com/appsheet/answer/10108286).
- `@(_TIMENOW)` is equivalent to [`TIMENOW()`](https://support.google.com/appsheet/answer/10107985).

## Examples

### Examples that compute Dates

- `TODAY() + 1`: adds one day (a `Number`) to the current `Date`.
- `TODAY() - 3` : subtracts 3 days (a `Number`) from the current `Date`.
- `[StartDate] + 7` : adds 7 days (a `Number`) to the `StartDate` (a `Date`).
- `TODAY() - (WEEKDAY(TODAY()) - 1)`  : the date of the preceding Sunday.
- `TODAY() - (WEEKDAY(TODAY()) - 2)`  : the date of the preceding Monday.

### Examples that compute Times

- `TIMENOW() + 1` : adds one hour (a `Number`) to the current `Time`.
- `TIMENOW() + "003:03:00"` : adds 3 hours 3 minutes (a `Duration`) to the current `Time`.
- `TIMENOW() - "003:03:00"` : subtracts 3 hours 3 minutes (a `Duration`) from the current `Time`.

### Examples that compute DateTimes

- `NOW() + 1` : adds one day (a `Number`) to the current `DateTime`.
- `NOW() - 3` : subtracts three days (a `Number`) from the current `DateTime`.
- `[TargetDateTime] + "012:59:00"` : adds 12 hours 59 minutes (a `Duration`) to a `DateTime` value.
- `[TargetDate] + ([TargetTime] - "00:00:00")`  : Creates a `DateTime` value from a `Date` value and a `Time` value.

### Examples that compute Durations

- `TIMENOW() - "12:30:00"` : the `Duration` between the current `Time` and 12:30 PM (a `Time`).
- `NOW() - "03:15:30"` : the `Duration` between the current `Time` and 3:15:30 AM (a `Time`) on December 30, 1899 (the default `Date` if none is included).
- `TODAY() - "12/30/2001"` : the `Duration` between the current `Date` and December 30, 2001 (a `Date`).
- `[EndDate] - [StartDate]` : the `Duration` between `StartDate` (a `Date`) at midnight and `EndDate` (a `Date`) at midnight.
- `IF(([StopWhen] > [StartWhen]), ([StopWhen] - [StartWhen]), (([StopWhen] + 24) - [StartWhen]))` : the `Duration` between `StartWhen` and `StopWhen` (two `DateTime` values). See also [`IF()`](https://support.google.com/appsheet/answer/10108198).

### Examples that compute Durations in Days, Months, or Years

- `HOUR(TODAY() - [TargetDate]) / 24` : number of days between today's date and the `Date` value given in the `TargetDate` column.
- `((YEAR([EndDate]) - YEAR([StartDate])))`: the number of years between the start and end dates.
- `((((YEAR([EndDate]) - YEAR([StartDate])) * 12) + MONTH([EndDate])) - MONTH([StartDate]))` : the number of months between the start and end dates. 

### Examples that compare Dates, Times, and DateTimes

- `(TODAY() - [When]) = 7`: a `Yes/No` value indicating whether the `Date` or `DateTime` value of the `When` column value is exactly seven days before today's `Date`.

- `(EOMONTH([When], 0) = EOMONTH(TODAY(), 0))`: a `Yes/No` value indicating whether the `Date` or `DateTime` value of the `When` column value is in the same month as today's date. See also: [`EOMONTH()`](https://support.google.com/appsheet/answer/10107332), [`TODAY()`](https://support.google.com/appsheet/answer/10108286)

- `([When] - TODAY()) = 7` : a `Yes/No` value indicating whether the `Date` or `DateTime` value of the `When` column value is exactly seven days after today's `Date`.

- `AND([OrderDateTime] >= [StartDateTime], [OrderDateTime] <= [EndDateTime])` : a `Yes/No` value indicating whether the `DateTime` value of the `OrderDateTime` column is between the `StartDateTime` and `EndDateTime` column values. See also: [`AND()`](https://support.google.com/appsheet/answer/10107398)

- `AND([OrderDate] >= [StartDate], [OrderDate] <= [EndDate])` : a `Yes/No` value indicating whether the `Date` value of the `OrderDate` column is between the `StartDate` and `EndDate` column values. See also: [`AND()`](https://support.google.com/appsheet/answer/10107398)

- `AND(([When] >= (TODAY() - 7)), ([When] <= TODAY()))` : a `Yes/No` value indicating whether the `Date` or `DateTime` value of the `When` column is within the past seven days. See also: [`AND()`](https://support.google.com/appsheet/answer/10107398)

- `TODAY() > ([TargetWhen] + 1)`: a `Yes/No` value indicating whether the `Date` or `DateTime` value of the `TargetWhen` column is more than a day in the past.

- `[Timestamp] > (NOW() - 1)`: a `Yes/No` value indicating whether the `DateTime` value of the `Timestamp` column is within 24 hours of the current date and time.

- `[OrderDateTime] >= (NOW() - "001:30:00")`  a `Yes/No` value indicating whether the `DateTime` value of the `OrderDateTime`  column is within 1 hour 30 minutes of the current `DateTime`.

- `IN(MINUTE([_THIS] - "00:00:00"), LIST(0, 15, 30, 45))` : a `Yes/No` value indicating whether the minute component of the `DateTime` or `Time` value of the current column falls on the quarter hour (that is, is 0, 15, 30, or 45). See also: [`IN()`](https://support.google.com/appsheet/answer/10107681), [`LIST()`](https://support.google.com/appsheet/answer/10107339)

### Examples for scheduling

- `AND((TODAY() >= DATE("01/01/2021")),`
  `(TODAY() <= DATE("12/31/2021")),`
  `(MOD(HOUR(TODAY()- DATE("01/01/2021"))/24, 15) = 0))` : a `Yes/No` value for a scheduled periodic event. The `DATE` value in the first line specifies the starting date of the scheduled periodic event. The `DATE` value in the second line specifies the ending date of the scheduled periodic event. The `DATE` value in the third line specifies when the scheduled periodic event should first be triggered. Normally the `DATE` values in the first and third lines should be identical, but you could specify a slightly later `DATE` value in the third line to trigger the first scheduled periodic event at a slightly later date. The value 15 in the third line specifies that the scheduled periodic event should be triggered every 15 days after the `Date` specified in the third line.
