---
fonte: https://support.google.com/docs/answer/9367752?hl=en
baixado: 2026-11-10
---

# REPLACEB function

The REPLACEB function replaces part of a text string, based on a number of bytes, with a different text string.

## Parts of a REPLACEB function

`REPLACEB(text, position, num_bytes, new_text)`

|             |                                                                  |
|-------------|------------------------------------------------------------------|
| **Part**    | **Description**                                                  |
| `text`      | The text, a part of which will be replaced.                      |
| `position`  | The position where the replacement will begin (starting from 1). |
| `num_bytes` | The number of bytes in the text to be replaced.                  |
| `new_text`  | The text which will be inserted into the original text.          |

## Notes

- `REPLACEB` returns the same value as `REPLACE` if the input \`text\` has only single byte characters
- This function returns text as the output. If a number is desired, try using the `VALUE` function in conjunction with this function.

## Examples

|       |             |                             |            |
|-------|-------------|-----------------------------|------------|
|       | **A**       | **B**                       | **C**      |
| **1** | **Input**   | **Formula**                 | **Output** |
| **2** | Aeñds       | `=REPLACEB(A2, 2, 3,"new")` | Anews      |
| **3** | Aeñds       | `=REPLACE(A3, 2, 3,"new")`  | Anews      |
| **4** | `熊本=熊本` | `=REPLACEB(A4, 2, 3,"new")` | 熊new熊本  |
| **5** | `熊本=熊本` | `=REPLACE(A5, 2, 3,"new") ` | 熊new本    |

## Related functions

- [LENB](https://support.google.com/docs/answer/9367584): The LENB function returns the length of a string in bytes.
- [LEFTB](https://support.google.com/docs/answer/9367470): The LEFTB function returns the left portion of a string up to a certain number of bytes.
- [RIGHTB](https://support.google.com/docs/answer/9367697): The RIGHTB function returns the right portion of a string up to a certain number of bytes.
- [MIDB](https://support.google.com/docs/answer/9367691):The MIDB function returns a section of a string starting at a given character and up to a specified number of bytes.
