---
fonte: https://support.google.com/docs/answer/9367691?hl=en
baixado: 2026-11-10
---

# MIDB function

The MIDB function returns a section of a string starting at a given character and up to a specified number of bytes.

## Parts of a MIDB function

`MIDB(string, starting_at, extract_length_bytes)`

|                        |                                                                |
|------------------------|----------------------------------------------------------------|
| **Part**               | **Description**                                                |
| `string`               | The string from which to extract a section.                    |
| `starting_at`          | The position in the input \`string\` to start extracting from. |
| `extract_length_bytes` | The number of bytes the extracted string should have.          |

## Notes

- `MIDB` returns the same value as `MID` if the input string has only single byte characters
- `Starting_at` must be greater than or equal to 1.
- `Extract_length_bytes` must be greater than or equal to 0.

## Examples

|       |             |                   |            |
|-------|-------------|-------------------|------------|
|       | **A**       | **B**             | **C**      |
| **1** | **Input**   | **Formula**       | **Output** |
| **2** | Aeñds       | `=MIDB(A2, 2, 2)` | eñ         |
| **3** | Aeñds       | `=MID(A3, 2, 2)`  | eñ         |
| **4** | `熊本=熊本` | `=MIDB(A4,2,4)`   | 本=熊      |
| **5** | `熊本=熊本` | `=MID(A5,2,4)`    | 本=熊本    |

## Related functions

- [LENB](https://support.google.com/docs/answer/9367584): The LENB function returns the length of a string in bytes.
- [LEFTB](https://support.google.com/docs/answer/9367470): The LEFTB function returns the left portion of a string up to a certain number of bytes.
- [RIGHTB](https://support.google.com/docs/answer/9367697): The RIGHTB function returns the right portion of a string up to a certain number of bytes.
