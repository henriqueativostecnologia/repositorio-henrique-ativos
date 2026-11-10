---
fonte: https://support.google.com/docs/answer/3267350?hl=en
baixado: 2026-11-10
---

# TIMEVALUE

Returns the fraction of a 24-hour day the time represents.

### Sample Usage

`TIMEVALUE("2:15 PM")`

`TIMEVALUE("14:15:30")`

`TIMEVALUE("11:59:59.50 PM")`

### Syntax

`TIMEVALUE(time_string)`

- `time_string` - The string that holds the time representation.

### Notes

- The string of text used in `time_string` should be within quotations and represent time using either the 12-hour or 24-hour time format, for example "2:15 PM" or "14:15".
- Returns a number between 0 (inclusive) and 1 (exclusive). Zero corresponds to 12:00:00 AM and 0.9999884259 corresponds to 11:59:59 PM. To get closer to 1.0, use fractions of seconds after 11:59:59 PM (e.g., 11:59:59.50 PM).
- Dates, for example the day of the week, are ignored in `time_string`.

### See Also

[`DATEVALUE`](https://support.google.com/docs/answer/3093039): Converts a provided date string in a known format to a date value.

[`MINUTE`](https://support.google.com/docs/answer/3093048): Returns the minute component of a specific time, in numeric format.

[`HOUR`](https://support.google.com/docs/answer/3093045): Returns the hour component of a specific time, in numeric format.

[`TIME`](https://support.google.com/docs/answer/3093056): Converts an hour, minute, and second into a time.

[`NOW`](https://support.google.com/docs/answer/3092981): Returns the current date and time as a date value.
