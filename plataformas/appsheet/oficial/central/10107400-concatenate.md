---
fonte: https://support.google.com/appsheet/answer/10107400?hl=en
baixado: 2026-11-10
---

# CONCATENATE()

Merged text from parts

Returns a new text value consisting of each part merged together in the order specified.

## Sample usage

`CONCATENATE("Good", "morning", "!")` returns `Goodmorning!`

`CONCATENATE("Good", " ", "morning", "!")`  returns `Good morning!`

`CONCATENATE("Good morning, ", [First Name], "!")` returns `Good morning, Martin!`

`CONCATENATE([Last Name], ", ", [First Name])` returns `Sandwich, Martin`

`CONCATENATE("Today is ", MONTH("4/1/2010"), "/", DAY("4/1/2010"), ".")` returns `Today is 4/1`.

### Include the weekday name

Include the computed weekday name into a constructed statement:

    CONCATENATE(
      "Today is ",
      INDEX(
        {"Sunday", "Monday", "Tuesday", "Wednesday",
          "Thursday", Friday", "Saturday", "Sunday"},
        WEEKDAY("4/1/2010")
      ),
      "."
    )

1.  `WEEKDAY(...)` returns the weekday number for the given `Date` or `DateTime` value: `5`
2.  `INDEX({...}, ...)` uses the weekday number to retrieve the weekday name from a list of weekday names: `Thursday`
3.  `CONCATENATE("Today is ", ..., ".")` assembles all of the parts into the final text: `Today is Thursday`*.*

See also: [`INDEX()`](https://support.google.com/appsheet/answer/10107336), [`WEEKDAY()`](https://support.google.com/appsheet/answer/10107424)

## Syntax

**`CONCATENATE(`***`part, `*`[`*`part`*` ...]`**`)`**

- *`part`* - A value of any type to be included in the merged text. You can specify multiple parts enclosed in quotes and separated by a comma.

## See also

[`INITIALS()`](https://support.google.com/appsheet/answer/10108199)

[`LEFT()`](https://support.google.com/appsheet/answer/10106634)

[`MID()`](https://support.google.com/appsheet/answer/10107345)

[`RIGHT()`](https://support.google.com/appsheet/answer/10107983)

[`SPLIT()`](https://support.google.com/appsheet/answer/10107984)

[`SUBSTITUTE()`](https://support.google.com/appsheet/answer/10108126)
