---
fonte: https://support.google.com/appsheet/answer/10108289?hl=en
baixado: 2026-11-10
---

# USERLOCALE()

User's locale

Returns the locale designation (`Text` value) provided by the user's device.

## Syntax

`USERLOCALE()`

## Notes

A **locale** provides a standard way to convey a preferred set of communication norms and conventions covering a wide range of factors, including: address format, currency, language, numeral system, punctuation, sorting, units of measurement, and many others.

In the United States, the common locale designation is `en-US`, indicating a preference for US-style English and US-centric conventions.

Locale designations are controlled by the user's device; `USERLOCALE()` merely makes the device-supplied value available to the app.

Not supported for Chat apps at this time; set to the default table or app [locale](https://support.google.com/appsheet/answer/10106525).
