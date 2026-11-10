---
fonte: https://support.google.com/docs/answer/3098292?hl=en
baixado: 2026-11-10
---

# REGEXMATCH

Whether a piece of text matches a regular expression.

### Sample Usage

`REGEXMATCH("Spreadsheets", "S.r")`

### Syntax

`REGEXMATCH(text, regular_expression)`

- `text` - The text to be tested against the regular expression.

- `regular_expression` - The regular expression to test the text against.

### Notes

- Google products use RE2 for regular expressions. Google Sheets supports RE2 except Unicode character class matching. [Learn how to use RE2 expressions](https://github.com/google/re2/wiki/syntax).
- This function only works with text (not numbers) as input and returns a logical value, i.e. `TRUE` or `FALSE`, as output. If numbers are used as input, convert them to text using the [`TEXT`](https://support.google.com/docs/answer/3094139) function.

### See Also

[`REGEXEXTRACT`](https://support.google.com/docs/answer/3098244): Extracts the first matching substrings according to a regular expression.

[`REGEXREPLACE`](https://support.google.com/docs/answer/3098245): Replaces part of a text string with a different text string using regular expressions.

[`SUBSTITUTE`](https://support.google.com/docs/answer/3094215): Replaces existing text with new text in a string.

[`REPLACE`](https://support.google.com/docs/answer/3098247): Replaces part of a text string with a different text string.

### Examples

Embedded content: https://docs.google.com/spreadsheet/pub?key=0As3tAuweYU9QdF95dWZQSjVxT016cHZIbFE1WGFnN0E&output=html
