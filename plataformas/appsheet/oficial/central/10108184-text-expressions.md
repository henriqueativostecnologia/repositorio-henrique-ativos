---
fonte: https://support.google.com/appsheet/answer/10108184?hl=en
baixado: 2026-11-10
---

# Text expressions

Use and produce textual values

A **textual value** is a sequence of letters, numbers, punctuation, emoji, spaces, or other characters that is not recognized as some other [data type](https://support.google.com/appsheet/answer/10106435) or [expression](https://support.google.com/appsheet/answer/10104642) keyword or operator.

A text expression is an expression that produces a textual value, or that uses one or more textual values to produce a value of any type.

The basic textual data type is `Text`, which may contain only one line of text. The `LongText` data type allows multiple lines of text. Several other column types, including `Address`, `Email`, and `Name`, have additional characteristics but are fundamentally textual values, and may be used as such within expressions.

**New to expressions?** See also [Expressions: The Essentials](https://support.google.com/appsheet/answer/10104642).

## Constructing text

#### Constructing a raw textual value

Within an expression, in general, AppSheet will treat any sequence of letters, numbers, punctuation, emoji, or other non-space characters as `Text` if not recognizable as something else, such as a `Date`, `Decimal`, `Number`, or `Time` value, or an expression keyword or operator.

To ensure AppSheet recognizes a raw textual value in an expression, the raw textual value should be enclosed in double quotes:

- `"John Smith"`
- `"jsmith@email.work"`
- `"Please choose an option below:"`
- `"Company Name"`

Some words commonly used as column names may be confused with expression keywords. To avoid confusion entirely, best to always double-quote raw textual values:

- `"Date"`
- `"DateTime"`
- `"Decimal"`
- `"Number"`
- `"Text"`
- `"Time"`

To include spaces at the beginning or the end of a raw textual value, or multiple consecutive spaces within, the raw value must be double-quoted:

- `" space before"`
- "`space after "`

To spread text across multiple lines (as for a `LongText` value), the entire multi-line raw value must be double-quoted:

    "This value
    is spread
    across lines."

When in doubt, if you want a raw value treated as a textual value, put double-quotes around it.

#### Constructing a textual value with concatenation

Two or more textual values can be combined to produce a new textual value using **concatenation**. The [`CONCATENATE()`](https://support.google.com/appsheet/answer/10107400) function does this:

- `CONCATENATE("ABC", "123")` gives `ABC123`.
- `CONCATENATE("Hi, ", [First Name], " ", [Last Name], "!")` might give `Hi, John Smith!`

The `text-concatenate` operator (`&`) is a short way to concatenate two values:

- `("ABC" & "123")` gives `ABC123`.
- `("Hi, " & [First Name] & " " & [Last Name] & "!")` might give `Hi, John Smith!`

#### Constructing a textual value with a function

A number of functions produce textual results:

- [`CONCATENATE()`](https://support.google.com/appsheet/answer/10107400) - Text from textual fragments.
- [`ENCODEURL()`](https://support.google.com/appsheet/answer/10106629) - [Encoded](https://en.wikipedia.org/wiki/Percent-encoding) textual value for use in a URL.
- [`INITIALS()`](https://support.google.com/appsheet/answer/10108199) - First character of each word in a textual value.
- [`LEFT()`](https://support.google.com/appsheet/answer/10106634) - Left-most consecutive characters from a textual value.
- [`LINKTEXT()`](https://support.google.com/appsheet/answer/10107913)` `- Textual component of hyperlink.
- [`LOWER()`](https://support.google.com/appsheet/answer/10107342) - Textual value with all letters lowercase.
- [`MID()`](https://support.google.com/appsheet/answer/10107345) - Consecutive characters from a textual value.
- [`RIGHT()`](https://support.google.com/appsheet/answer/10107983) - Right-most consecutive characters from a textual value.
- [`SUBSTITUTE()`](https://support.google.com/appsheet/answer/10108126) - Textual value with one fragment replaced by another.
- [`TEXT()`](https://support.google.com/appsheet/answer/10107701) - Textual representation of any value.
- [`TRIM()`](https://support.google.com/appsheet/answer/10107932) - Textual value with excess whitespace removed.
- [`UNIQUEID()`](https://support.google.com/appsheet/answer/10108209) - Random text value suitable for ID.
- [`UPPER()`](https://support.google.com/appsheet/answer/10107369) - Textual value with all letters uppercase.

#### Constructing a textual value from a non-textual value

In certain places within expressions and in other AppSheet features, textual values may be required but the data you want to use is stored in a column of a non-textual type, such as `Decimal` or a `DateTime`. There are several ways to convert non-textual values to a `Text`:

- **`TEXT()` function:** Using a non-textual value with the [`TEXT()`](https://support.google.com/appsheet/answer/10107701) function (e.g. `TEXT([My Data])`) creates a new textual value from the original value, formatted in a suitable way. The result will be [localized](https://support.google.com/appsheet/answer/10106393), which may affect the appearance of dates, times, numbers, decimals, and currency. If the original value is a column value (e.g., not a raw value or the result of an expression), any column-specific display preferences, such as number of digits, decimal precision, time precision, and date verbosity, will also be applied.
- **`CONCATENATE()` function:** Using a non-textual value with the [`CONCATENATE()`](https://support.google.com/appsheet/answer/10107400) function (e.g. `CONCATENATE([My Data])`) or with the *text-concatenate* operator (e.g., `([My Data] & "")`) creates a new textual value using **the exact text of the original value** (the raw value, or the value as stored in the spreadsheet or other data store beneath the app table). Note that using this method **does not apply column-specific display preferences** (such as number of digits, decimal precision, time precision, and date verbosity), **nor is the result localized** (which may affect the appearance of dates, times, numbers, decimals, and currency).
- **Other functions:** A number of other functions designed to work with textual values may accept non-textual values and produce reasonable textual results. Using non-textual values directly with functions intended for textual values is not recommended. Instead, consider using `TEXT()` or `CONCATENATE()` as described above to convert the non-textual value first.

## Use text

#### Using text expressions to customize messages

The text of many of the messages AppSheet displays to the app user may be customized from the **[UX \> Localize](https://support.google.com/appsheet/answer/10106393)** page in the app editor.

By default, custom message text is provided as a raw value, but can be generated with an expression by toggling from the pencil (raw) to the flask (expression):

A common use is to **localize messages** to the user's preferred language. In an app designed to accommodate multiple languages, there might be a table specifically containing translation text (such as, `Translations`), where each row is for a specific language (specified by the `Language` column, for example) and each column is the translation of a specific message. The following expression might then be used to provide the localized text for the `Syncing the app` message according to the user's preferred language (from the `Language` user setting):

    LOOKUP(
      USERSETTINGS("Language"),
      "Translations",
      "Language",
      "Syncing the app"
    )

See also: [`LOOKUP()`](https://support.google.com/appsheet/answer/10107410), [`USERSETTINGS()`](https://support.google.com/appsheet/answer/10108291)

#### **Use textual values in functions**

A variety of functions accept textual input:

- `APP()` - App (deep-link) from a textual value.
- [`CONCATENATE()`](https://support.google.com/appsheet/answer/10107400) - `Text` from textual fragments.
- [`CONTAINS()`](https://support.google.com/appsheet/answer/10107955) - Does textual value contain fragment?
- [`DECIMAL()`](https://support.google.com/appsheet/answer/10107887) - `Decimal` from a textual value.
- [`ENCODEURL()`](https://support.google.com/appsheet/answer/10106629) - [Encoded](https://en.wikipedia.org/wiki/Percent-encoding) textual value for use in a URL.
- [`ENDSWITH()`](https://support.google.com/appsheet/answer/11582090) - Does text end with fragment?
- [`EXTRACT()`](https://support.google.com/appsheet/answer/10107889) - List of recognizable elements from a textual value.
- [`EXTRACTCHOICE()`](https://support.google.com/appsheet/answer/10107958)* *- Extract one `Yes/No` value from a textual value.
- [`EXTRACTDATES()`](https://support.google.com/appsheet/answer/10107402) - List of dates from a textual value.
- [`EXTRACTDATETIMES()`](https://support.google.com/appsheet/answer/10108193)` `- List of `DateTimes` from a textual value.
- `EXTRACTDOMAINS()` - List of email domains from a textual value.
- [`EXTRACTDURATIONS()`](https://support.google.com/appsheet/answer/10107333)` `- List of durations from a textual value.
- [`EXTRACTEMAILS()`](https://support.google.com/appsheet/answer/10107403) - List of email addresses from a textual value.
- [`EXTRACTHASHTAGS()`](https://support.google.com/appsheet/answer/10107890) - List of hashtags from a textual value.
- [`EXTRACTMENTIONS()`](https://support.google.com/appsheet/answer/10108195) - List of mentions from a textual value.
- [`EXTRACTNUMBERS()`](https://support.google.com/appsheet/answer/10107677) - List of numeric values from a textual value.
- [`EXTRACTPHONENUMBERS()`](https://support.google.com/appsheet/answer/10106631) - List of phone numbers from a textual value.
- [`EXTRACTPRICES()`](https://support.google.com/appsheet/answer/10107891) - List of prices from a textual value.
- [`EXTRACTTIMES()`](https://support.google.com/appsheet/answer/10107404) - List of times from a textual value.
- [`FIND()`](https://support.google.com/appsheet/answer/10108197) - Position of fragment in a textual value.
- [`INITIALS()`](https://support.google.com/appsheet/answer/10108199) - First character of each word in a textual value.
- [`ISBLANK()`](https://support.google.com/appsheet/answer/10107337) - Is value absent?
- [`ISNOTBLANK()`](https://support.google.com/appsheet/answer/10107964) - Is value present?
- [`LEFT()`](https://support.google.com/appsheet/answer/10106634) - Leftmost consecutive characters from a textual value.
- [`LEN()`](https://support.google.com/appsheet/answer/10107966) - Number of characters in a textual value.
- [`LOWER()`](https://support.google.com/appsheet/answer/10107342) - Textual value with all letters lowercase.
- [`MID()`](https://support.google.com/appsheet/answer/10107345) - Consecutive characters from a textual value.
- [`NUMBER()`](https://support.google.com/appsheet/answer/10108120) - Number from textual value.
- [`RIGHT()`](https://support.google.com/appsheet/answer/10107983) - Right-most consecutive characters from a textual value.
- [`SPLIT()`](https://support.google.com/appsheet/answer/10107984) - List from textual value.
- [`STARTSWITH()`](https://support.google.com/appsheet/answer/11581808) - Does text start with fragment?
- [`SUBSTITUTE()`](https://support.google.com/appsheet/answer/10108126) - Textual value with one fragment replaced by another.
- [`TEXT()`](https://support.google.com/appsheet/answer/10107701) - Textual representation of any value.
- [`TEXT_ICON()`](https://support.google.com/appsheet/answer/11622091) - `Icon` from text.
- [`TRIM()`](https://support.google.com/appsheet/answer/10107932) - Textual value with excess whitespace removed.
- [`UPPER()`](https://support.google.com/appsheet/answer/10107369) - Textual value with all letters uppercase.
