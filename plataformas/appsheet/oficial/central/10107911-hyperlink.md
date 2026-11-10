---
fonte: https://support.google.com/appsheet/answer/10107911?hl=en
baixado: 2026-11-10
---

# HYPERLINK()

New hyperlink

Returns a hyperlink composed of the specified URL and clickable text.

**Note**: Don't use the `HYPERLINK()` function in [automation templates](https://support.google.com/appsheet/answer/11539957).

## Sample app

See an example of `HYPERLINK()` in the [Hyperlinks sample app](https://www.appsheet.com/Template/AppDef?appName=Hyperlinks-71626&appId=Hyperlinks-71626#Data.Tables).

## Sample usage

`HYPERLINK("https://www.google.com", "Google")` returns [Google](https://www.google.com/)

`HYPERLINK("https://www.appsheet.com", "AppSheet home page")` returns  [AppSheet home page](https://www.appsheet.com/)

`HYPERLINK("https://www.appsheet.com/samples/How-to-link-to-a-URL-with-custom-text?appGuidString=3f55edfc-aa53-47fc-a206-469720f10b13", "Hyperlinks sample app")` returns  [Hyperlinks sample app](https://www.appsheet.com/samples/How-to-link-to-a-URL-with-custom-text?appGuidString=3f55edfc-aa53-47fc-a206-469720f10b13)

`HYPERLINK([Vendor Site], [Vendor Name])` returns a hyperlink pointing to the URL in the `Vendor Site` column, with clickable text from the `Vendor Name` column.

### Encode text for URL

Certain characters, such as ampersand (`&`), colon (`:`), slash (`/`), and even a space, have special meanings within URLs. Text included in URLs that contains special characters should be "encoded" to remove the special meaning and avoid problems. The `ENCODEURL()` function is provided for this purpose.

    HYPERLINK(
      CONCATENATE(
        "https://www.google.com/search?q=",
        ENCODEURL([Product Name])
      ),
      ("Search for " & [Product Name] & " on Google")
    )

1.  `HYPERLINK(..., ...)` creates a hyperlink to the given target URL and with the given clickable text.
2.  `CONCATENATE(..., ...)` computes the target URL by combining the given values.
3.  `"https://www.google.com/search?q="`: the initial part of the target URL. This part is already properly encoded as a URL, so `ENCODEURL()` is not needed.
4.  `ENCODEURL([Product Name])` encodes the `Product Name` column value, ensuring the special meaning is removed from any special characters the value may contain.
5.  `("Search for " & [Product Name] & " on Google")` assembles the clickable text for the hyperlink from the given components. `ENCODEURL()` is not needed here because the clickable text is not part of the URL. Equivalent to `CONCATENATE("Search for ", [Product Name], " on Google")`.

See also: [`CONCATENATE()`](https://support.google.com/appsheet/answer/10107400), [`ENCODEURL()`](https://support.google.com/appsheet/answer/10106629)

## Syntax

`HYPERLINK(`*`url`*`, `*`text`*`)`

- `url` - Any textual type. Specifies the URL to which the user is to be sent upon clicking the link. No processing of the URL is done in constructing the hyperlink; the URL should be complete and valid.
- `text` -Any textual type. Specifies the text the user will see and click on.

## See also

[`ENCODEURL()`](https://support.google.com/appsheet/answer/10106629)

[`LINKTEXT()`](https://support.google.com/appsheet/answer/10107913)

[`LINKURL()`](https://support.google.com/appsheet/answer/10107967)
