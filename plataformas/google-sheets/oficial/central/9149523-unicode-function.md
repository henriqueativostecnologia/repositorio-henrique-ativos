---
fonte: https://support.google.com/docs/answer/9149523?hl=en
baixado: 2026-11-10
---

# UNICODE function

The `UNICODE` function returns the decimal Unicode value of the first character of the text.

### Parts of a UNICODE function

`UNICODE(text)`

|      |                                                      |
|------|------------------------------------------------------|
| Part | Description                                          |
| text | The string containing the character to be evaluated. |

### Sample formulas

UNICODE("A")

UNICODE(123)

UNICODE(😀😀😄)

### Notes

- The UNICODE function will only work properly if the input string is not empty and the first character has a Unicode representation.

- Numbers may be passed directly into the UNICODE function and will be parsed as a string.

### Examples

UNICODE : General Usage

|     |        |                      |
|-----|--------|----------------------|
|     | A      | B                    |
| 1   | Result | Formula              |
| 2   | 65     | =UNICODE("Alphabet") |
| 3   | 49     | =UNICODE(123)        |
| 4   | 128512 | =UNICODE(😀😀😄)     |

### Related functions

[CHAR](https://support.google.com/docs/answer/3094120): Convert a number into a character according to the current Unicode table.

[CODE](https://support.google.com/docs/answer/3094122): Returns the numeric Unicode map value of the first character in the string provided.
