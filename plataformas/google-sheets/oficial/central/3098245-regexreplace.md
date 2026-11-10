---
fonte: https://support.google.com/docs/answer/3098245?hl=en
baixado: 2026-11-10
---

# REGEXREPLACE

Replaces part of a text string with a different text string using regular expressions.

### Sample Usage

`REGEXREPLACE("Spreadsheets", "S.*d", "Bed")`

### Syntax

`REGEXREPLACE(text, regular_expression, replacement)`

- `text` - The text, a part of which will be replaced.

- `regular_expression` - The regular expression. All matching instances in `text` will be replaced.

- `replacement` - The text which will be inserted into the original text.

### Notes

- Google products use RE2 for regular expressions. Google Sheets supports RE2 except Unicode character class matching.  Learn more on [how to use RE2 expressions](https://github.com/google/re2/blob/master/doc/syntax.txt).
- This function only works with text (not numbers) as input and returns text as output. If a number is desired as the output, try using the [`VALUE`](https://support.google.com/docs/answer/3094220) function in conjunction with this function. If numbers are used as input, convert them to text using the [`TEXT`](https://support.google.com/docs/answer/3094139) function.

### See Also

[`REGEXEXTRACT`](https://support.google.com/docs/answer/3098244): Extracts the first matching substrings according to a regular expression.

[`REGEXMATCH`](https://support.google.com/docs/answer/3098292): Whether a piece of text matches a regular expression.

[`SUBSTITUTE`](https://support.google.com/docs/answer/3094215): Replaces existing text with new text in a string.

[`REPLACE`](https://support.google.com/docs/answer/3098247): Replaces part of a text string with a different text string.

### Examples

Embedded content: https://docs.google.com/spreadsheet/pub?key=0As3tAuweYU9QdGFUTDhRTFVRUkpWZmp0emhOSm1yd0E&output=html
