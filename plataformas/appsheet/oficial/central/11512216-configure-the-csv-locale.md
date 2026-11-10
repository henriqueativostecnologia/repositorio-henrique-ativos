---
fonte: https://support.google.com/appsheet/answer/11512216?hl=en
baixado: 2026-11-10
---

# Configure the CSV locale

How configure the CSV locale

When you configure either the [Import a CSV file for this view](https://support.google.com/appsheet/answer/11510988) or [Export this view to a CSV file](https://support.google.com/appsheet/answer/11579391) action, you must specify the locale of the CSV row data in one of two ways.

- You can select one of these [supported locales](https://support.google.com/appsheet/answer/11579290) from the **CSV file locale** dropdown. The locale defaults to `English (United States)`. The locale you choose applies to all users of the action.
- You can supply a locale expression that yields the locale identifier for one of these [supported locales](https://support.google.com/appsheet/answer/11579290) such as "en-US" for English (United States), "en-GB" for English (United Kingdom), or "de-DE" for German (Germany). This allows you to customize the locale for each user. For example, you might store the locale identifier in a field of UserSettings or retrieve it from a normal table using a LOOKUP expression. See topic "Storing the Locale in UserSettings" below for more details.

## Locale and data format

The locale must match the format of the data in the CSV file. This is important for data values who's format varies by locale. For example, when `Locale` is `English (United States)`, date values must be entered in `M/d/yyyy` format; when `Locale` is `English (United Kingdom)`, date values must be entered in `dd/MM/YYYY` format; when `Locale` is `German (Germany)`, date values must be entered in `dd.MM.yyyy` format.

See [Supported locales](https://support.google.com/appsheet/answer/11579290) for the date and time format patterns.

The following data types are locale dependent:

- `Date`
- `DateTime`
- `Decimal`
- `Percent`
- `Price`
- `Time`

## Locale and CSV delimiter

The locale also dictates the delimiter used between data values in the CSV file. The delimiter normally complements the decimal number separator.

- When the decimal number separator is period, the delimiter is comma.
- When the decimal number separator is comma, the delimiter is semicolon.

When the locale is `English (United States)`:

- Dates are in `M/d/yyyy` format.
- Times are in `h:mm:ss tt` format.
- `Decimal`, `Price`, and `Percent` values use period as the decimal separator.
- CSV data values are delimited by commas.
- `LatLong` values should be enclosed in quotes. For example: `"37.300000, -113.050000"`

When the locale is `English (United Kingdom)`:

- Dates are in `dd/MM/YYYY` format.
- Times are in `HH:mm:ss` format.
- `Decimal`, `Price`, and `Percent` values use period as the decimal separator.
- CSV data values are delimited by commas.
- `LatLong` values should be enclosed in quotes. For example: `"37.300000, -113.050000"`

When the locale is `German (Germany)`:

- Dates are in `dd.MM.yyyy` format.
- Times are in `HH:mm:ss` format.
- `Decimal`, `Price`, and `Percent` values use comma as the decimal separator.
- CSV data values are delimited by semicolons.

## Store the locale in User Settings

You can store the locale in `UserSettings` as follows:

1.  Open the app in the app editor.
2.  Go to **Data** ** \> User Settings**.
    We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

    ## If you are using the legacy editor

    Go to the **Data** ** \> User Settings** tab and expand **\_Per Users Settings**.
3.  Choose an available User Settings field and give it an appropriate name such as **CsvLocale**.
4.  Set the field's **Type **to **Text**.
5.  Set the field's **Initial value** to a [supported locale ID](https://support.google.com/appsheet/answer/11579290)  such as `de-DE`.
6.  Click the **Save** button.
7.  Go to **Actions ** Actions icon .
     We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

    ## If you are using the legacy navigation

    Go to **Behavior \> Actions**.  
8.  Open the Import or Export action.
9.  Click the expression (beaker) icon following the CSV file locale property and enter the following locale expression: `USERSETTINGS(CsvLocale)`
10. Click the **Save** button.
