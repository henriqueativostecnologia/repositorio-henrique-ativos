---
fonte: https://support.google.com/docs/answer/3098244?hl=en
baixado: 2026-11-10
---

# REGEXEXTRACT

Extracts the first matching substrings according to a regular expression.

### Sample Usage

`=REGEXEXTRACT("My favorite number is 241, but my friend's is 17", "\d+")`

**Tip: **REGEXEXTRACT will return "241" in this example because it returns the first matching case.

### Syntax

`REGEXEXTRACT(text, regular_expression)`

- `text` - The input text.

- `regular_expression` - The first part of `text` that matches this expression will be returned.

### Capture Groups

It is possible to return multiple results with capture groups. A capture group is a part of a pattern that can be enclosed in parentheses. If there are no capture groups, the function returns the whole match.

### Sample Usage

`=REGEXEXTRACT("You can also extract multiple values from text.”, “You can also (\w+) multiple (\w+) from text.”)`

**Tip:** The example above will return two columns of data, “extract” in the first and “values” in the second.

### Notes

- Google products use RE2 for [regular expressions](https://support.google.com/docs/answer/62754#regular_expression). Google Sheets supports RE2 except Unicode character class matching. Learn more on [how to use RE2 expressions](https://github.com/google/re2/blob/master/doc/syntax.txt).
- This function only works with text (not numbers) as input and returns text as output. If a number is desired as the output, try using the [`VALUE`](https://support.google.com/docs/answer/3094220) function in conjunction with this function. If numbers are used as input, convert them to text using the [`TEXT`](https://support.google.com/docs/answer/3094139) function.

### See Also

[`REGEXMATCH`](https://support.google.com/docs/answer/3098292): Whether a piece of text matches a regular expression.

[`REGEXREPLACE`](https://support.google.com/docs/answer/3098245): Replaces part of a text string with a different text string using regular expressions.

[`SUBSTITUTE`](https://support.google.com/docs/answer/3094215): Replaces existing text with new text in a string.

[`REPLACE`](https://support.google.com/docs/answer/3098247): Replaces part of a text string with a different text string.

### Examples

Embedded content: https://docs.google.com/spreadsheet/pub?key=0As3tAuweYU9QdFkxS1NreG5VSDVFOWlCTWVDU3dUWlE&output=html
