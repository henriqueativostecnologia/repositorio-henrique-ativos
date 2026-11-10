---
fonte: https://support.google.com/docs/answer/3094215?hl=en
baixado: 2026-11-10
---

# SUBSTITUTE

Replaces existing text with new text in a string.

### Sample Usage

`SUBSTITUTE("search for it","search for","Google")`

`SUBSTITUTE(A2,"new york","New York")`

`SUBSTITUTE("January 2, 2012",2,3,1)`

### Syntax

`SUBSTITUTE(text_to_search, search_for, replace_with, [occurrence_number])`

- `text_to_search` - The text within which to search and replace.

- `search_for` - The string to search for within `text_to_search`.

  - `search_for` will match parts of words as well as whole words; therefore a search for `"vent"` will also replace text within `"eventual"`.

- `replace_with` - The string that will replace `search_for`.

- `occurrence_number` - **\[** OPTIONAL **\]** - The instance of `search_for` within `text_to_search` to replace with `replace_with`. By default, all occurrences of `search_for` are replaced; however, if `occurrence_number` is specified, only the indicated instance of `search_for` is replaced.

### Notes

- `SUBSTITUTE` can be used to replace one or all instances of a string within `text_to_search`. It cannot be used to replace multiple, but not all instances within a single call.
- This function returns text as the output. If a number is desired, try using the [`VALUE`](https://support.google.com/docs/answer/3094220) function in conjunction with this function.

### See Also

[`TEXT`](https://support.google.com/docs/answer/3094139): Converts a number into text according to a specified format.

[`REPLACE`](https://support.google.com/docs/answer/3098247): Replaces part of a text string with a different text string.

### Examples

Embedded content: https://docs.google.com/spreadsheet/pub?key=0As3tAuweYU9QdDhrejJicnZQWS1ud1lhREoxajRpdnc&output=html
