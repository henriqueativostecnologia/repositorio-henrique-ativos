---
fonte: https://support.google.com/appsheet/answer/10106629?hl=en
baixado: 2026-11-10
---

# ENCODEURL()

Encode text for use in URL

Returns a [URL-encoded](https://en.wikipedia.org/wiki/Percent-encoding) text string.

## Sample usage

`ENCODEURL("Hello")` returns `Hello`

`ENCODEURL("Hello!")` returns `Hello%21`

`ENCODEURL("Hello there!")` returns `Hello%20there%21`

(`"https://www.google.com/search?q=" & ENCODEURL("AppSheet is fun!"))` returns `https://www.google.com/search?q=AppSheet%20is%20fun%21`

## Syntax

`ENCODEURL(`*`text`*`)`

- *`text`* - Text string to be URL encoded.

## Notes

- Encoding removes any special meaning the individual characters within the *`text`* string might have when used within a URL.

- Characters with special meanings in URLs include but are not limited to: space, ampersand (`&`), comma (`,`), hash (`#`), plus (`+`), question mark (`?`), semicolon (`;`), slash (`/`), and others.

- For safety, all characters that aren't letters or numbers are subject to encoding.

## See also

[`HYPERLINK()`](https://support.google.com/appsheet/answer/10107911)

[`SUBSTITUTE()`](https://support.google.com/appsheet/answer/10108126)
