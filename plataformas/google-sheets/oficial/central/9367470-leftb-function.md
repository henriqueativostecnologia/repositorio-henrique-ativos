---
fonte: https://support.google.com/docs/answer/9367470?hl=en
baixado: 2026-11-10
---

# LEFTB function

The LEFTB function returns the left portion of a string up to a certain number of bytes.

## Parts of a LEFTB function 

`LEFTB(string, num_of_bytes)`
 

|                |                                                                            |
|----------------|----------------------------------------------------------------------------|
| **Part**       | **Description**                                                            |
| `string`       | The string from which the left portion will be returned.                   |
| `num_of_bytes` | (Optional) The number of bytes to return from the left side of \`string\`. |

## Notes

- `LEFTB` returns the same value as `LEFT` if the input string has only single byte characters
- `num_of_bytes` must be greater than or equal to zero.
- If `num_of_bytes` is greater than the length of text in bytes, `LEFTB` returns all of text.
- If `num_of_bytes` is omitted, it is assumed to be 1.

## Examples

|       |           |                 |            |
|-------|-----------|-----------------|------------|
|       | **A**     | **B**           | **C**      |
| **1** | **Input** | **Formula**     | **Output** |
| **2** | Aeñ       | `=LEFTB(A2, 2)` | Ae         |
| **3** | Aeñ       | `=LEFT(A3,2)`   | Ae         |
| **4** | `熊本`    | `=LEFTB(A4, 2)` | 熊         |
| **5** | `熊本`    | `=LEFT(A5,2)`   | 熊本       |

## Related functions

- [MIDB](https://support.google.com/docs/answer/9367691): ​The MIDB function returns a section of a string starting at a given character and up to a specified number of bytes.
- [RIGHTB](https://support.google.com/docs/answer/9367697): The RIGHTB function returns the right portion of a string up to a certain number of bytes.
- [LENB](https://support.google.com/docs/answer/9367584): The LENB function returns the length of a string in bytes.
