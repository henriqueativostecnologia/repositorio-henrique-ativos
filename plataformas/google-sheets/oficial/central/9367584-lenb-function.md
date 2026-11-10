---
fonte: https://support.google.com/docs/answer/9367584?hl=en
baixado: 2026-11-10
---

# LENB function

The LENB function returns the length of a string in bytes.

## Parts of a LENB function 

`LENB(string) `

|          |                                        |
|----------|----------------------------------------|
| **Part** | **Description**                        |
| `string` | The string to get the length in bytes  |

## Notes 

`LENB` returns the same value as `LEN` if the input string has only single byte characters.

## Examples

|       |           |             |            |
|-------|-----------|-------------|------------|
|       | **A**     | **B**       | **C**      |
| **1** | **Input** | **Formula** | **Output** |
| **2** | Aeñ       | `=LENB(A2)` | 3          |
| **3** | Aeñ       | `=LEN(A3)`  | 3          |
| **4** | `熊本`    | `=LENB(A4)` | 4          |
| **5** | `熊本`    | `=LEN(A5)`  | 2          |

## Related functions

- [MIDB](https://support.google.com/docs/answer/9367691): ​The MIDB function returns a section of a string starting at a given character and up to a specified number of bytes.
- [LEFTB](https://support.google.com/docs/answer/9367470): The LEFTB function returns the left portion of a string up to a certain number of bytes.
- [RIGHTB](https://support.google.com/docs/answer/9367697): The RIGHTB function returns the right portion of a string up to a certain number of bytes.
