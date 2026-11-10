---
fonte: https://support.google.com/appsheet/answer/10107670?hl=en
baixado: 2026-11-10
---

# Backward compatibility expressions

Expressions supported for backward compatibility

Since the AppSheet platform is constantly being improved and updated, we've made some changes since we first got started: some expression components used to look a little different. We support the syntax below to accommodate apps that still use them.

- `@(_HERE)` returns the current location as a `LatLong` value; equivalent to [`HERE()`](https://support.google.com/appsheet/answer/10107405).
- `@(_NOW)` returns the current date and time as a `DateTime` value; equivalent to [`NOW()`](https://support.google.com/appsheet/answer/10108119).
- `@(_TIMENOW)` returns the current time as a `Time` value; equivalent to [`TIMENOW()`](https://support.google.com/appsheet/answer/10107985).
- `@(_TODAY)` returns the current date as a `Date` value; equivalent to [`TODAY()`](https://support.google.com/appsheet/answer/10108286).
- `@(_UNIQUE)` returns a new unique `Text` value suitable for use as a key; equivalent to [`UNIQUEID()`](https://support.google.com/appsheet/answer/10108209).
- `@(_USEREMAIL)` returns the user's email address as an `Email` value; equivalent to [`USEREMAIL()`](https://support.google.com/appsheet/answer/10108210).
- `@(_USERNAME)` returns the user's name as a `Name` value; equivalent to [`USERNAME()`](https://support.google.com/appsheet/answer/10108211). Note that the user's name may not be reliably available to AppSheet, so this value should not be considered a reliable identifier.

**New to expressions?** See also [Expressions: The Essentials](https://support.google.com/appsheet/answer/10104642).
