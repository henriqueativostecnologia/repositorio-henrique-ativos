---
fonte: https://support.google.com/docs/answer/3094140?hl=en
baixado: 2026-11-10
---

# TRIM function

Removes leading, trailing, and repeated spaces in text.

### Sample Usage

`TRIM(" lorem ipsum")`

`TRIM(A2)`

### Syntax

`TRIM(text)`

- `text` - The string or reference to a cell containing a string to be trimmed.

### Notes

- Google Sheets trims text input into cells by default.

- It is important to use `TRIM` when text is used in formulas or data validation because spaces in front of or after the text are significant.

- `TRIM` removes all spaces in a text string, leaving just a single space between words.

- Whitespace or non-breaking space will not be trimmed.

### See Also

[`SUBSTITUTE`](https://support.google.com/docs/answer/3094215): Replaces existing text with new text in a string.

[`REPLACE`](https://support.google.com/docs/answer/3098247): Replaces part of a text string with a different text string.

### Examples

Embedded content: https://docs.google.com/spreadsheet/pub?key=0As3tAuweYU9QdG1xd21mTkRHbHYtVHgxTU5CTnNTMEE&output=html
