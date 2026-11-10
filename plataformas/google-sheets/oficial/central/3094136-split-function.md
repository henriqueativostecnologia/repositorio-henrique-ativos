---
fonte: https://support.google.com/docs/answer/3094136?hl=en
baixado: 2026-11-10
---

# SPLIT function

Divides text around a specified character or string, and puts each fragment into a separate cell in the row.

### Examples

[Make a copy](https://docs.google.com/spreadsheets/d/1fnJNavi4NHw1sa9huCwg8UMzz3ztRwQfKb-Je5XFCNo/copy)

Embedded content: https://docs.google.com/spreadsheet/pub?key=0As3tAuweYU9QdElfUHBJeXFPZlctRGxpc3N3Z2M2T0E&output=html

### Sample Usage

`SPLIT("1,2,3", ",")`

`SPLIT("Alas, poor Yorick"," ")`

`SPLIT(A1, ",")`

### Syntax

`SPLIT(text, delimiter, [split_by_each], [remove_empty_text])`

- `text` - The text to divide.

- `delimiter` - The character or characters to use to split `text`.

  - By default, each character in `delimiter` is considered individually, e.g. if `delimiter` is `"the"`, then `text` is divided around the characters `"t"`, `"h"`, and `"e"`. Set `split_by_each` to `FALSE` to turn off this behavior.

- `split_by_each` - **\[** OPTIONAL - `TRUE` by default **\]** - Whether or not to divide `text` around each character contained in `delimiter`.

- `remove_empty_text ` - \[ OPTIONAL - `TRUE` by default \] - Whether or not to remove empty text messages from the split results. The default behavior is to treat consecutive delimiters as one (if `TRUE`). If `FALSE`, empty cells values are added between consecutive delimiters.

### Notes

- Note that the character or characters to split the string around will not be contained in the result themselves.

### See Also

[`CONCATENATE`](https://support.google.com/docs/answer/3094123): Appends strings to one another.
