---
fonte: https://support.google.com/docs/answer/9116090?hl=en
baixado: 2026-11-10
---

# DECIMAL function

The DECIMAL function converts the text representation of a number in another base, to base 10 (decimal).

## Parts of a DECIMAL formula

`DECIMAL(value, base)`

|          |                                                                      |                                      |
|----------|----------------------------------------------------------------------|--------------------------------------|
| **Part** | **Description**                                                      | **Notes**                            |
| `value`  | The unsigned value to be converted to decimal, provided as a string. |                                      |
| `base`   | The base (or radix) to convert the number into.                      | The base is an integer from 2 to 36. |

## Sample formula

`DECIMAL(101,2)`

## Notes

- The string representation of the value is used, which should only contain numeric characters (i.e. scientific notation isn't permitted). The text of a string should be no longer than 255 characters.
- The DECIMAL function only converts to positive integers.

## Example

|       |                 |            |
|-------|-----------------|------------|
|       | **A**           | **B**      |
| **1** | **Formula**     | **Result** |
| **2** | =DECIMAL(101,2) | 5          |

## Related functions

- [BASE](https://support.google.com/docs/answer/9084167): The BASE function converts a decimal number into a text representation in another base.
- [BIN2DEC](https://support.google.com/docs/answer/3092991): The BIN2DEC function converts a signed binary number to decimal format.
- [BIN2HEX](https://support.google.com/docs/answer/3093133): The BIN2HEX function converts a signed binary number to signed hexadecimal format.
- [BIN2OCT](https://support.google.com/docs/answer/3092993): The BIN2OCT function converts a signed binary number to signed octal format.
- [OCT2BIN](https://support.google.com/docs/answer/3093144): The OCT2BIN function converts a signed octal number to signed binary format.
- [OCT2DEC](https://support.google.com/docs/answer/3093146): The OCT2DEC function converts a signed octal number to decimal format.
- [OCT2HEX](https://support.google.com/docs/answer/3093147): The OCT2HEX function converts a signed octal number to signed hexadecimal format.
- [DEC2BIN](https://support.google.com/docs/answer/3092997): The DEC2BIN function converts a decimal number to signed binary format.
- [DEC2OCT](https://support.google.com/docs/answer/3093138): The DEC2OCT function converts a decimal number to signed octal format.
- [DEC2HEX](https://support.google.com/docs/answer/3093137): The DEC2HEX function converts a decimal number to signed hexadecimal format.
- [HEX2DEC](https://support.google.com/docs/answer/3093192): The HEX2DEC function converts a signed hexadecimal number to decimal format.
- [HEX2BIN](https://support.google.com/docs/answer/3093139): The HEX2BIN function converts a signed hexadecimal number to signed binary format.
- [HEX2OCT](https://support.google.com/docs/answer/3093142): The HEX2OCT function converts a signed hexadecimal number to signed octal format.
