---
fonte: https://support.google.com/docs/answer/9061440?hl=en
baixado: 2026-11-10
---

# BITAND function

The BITAND function returns the bitwise boolean AND of two numbers. [Learn more.](https://support.google.com/docs/answer/9061440) The truth table of BITAND is provided below:

|     |     |             |
|-----|-----|-------------|
| A   | B   | BITAND(A,B) |
| 0   | 0   | 0           |
| 0   | 1   | 0           |
| 1   | 0   | 0           |
| 1   | 1   | 1           |

## Parts of a BITAND function

`BITAND(value1,value2)`

|          |                    |                                                   |
|----------|--------------------|---------------------------------------------------|
| **Part** | **Description**    | **Notes**                                         |
| `value1` | The first number.  | Must be the decimal representation of the number. |
| `value2` | The second number. | Must be the decimal representation of the number. |

## Notes

It may make sense to use BITAND in conjunction with BIN2DEC as follows:

- BITAND(BIN2DEC(“1010”), BIN2DEC(“1001”)) which evaluates to “1000” in binary or 8 in decimal.

## Examples

10 in decimal is “1010” in binary. 9 in decimal is “1001” in binary. The result is “1000” in binary, which is 8 in decimal.

|       |                 |            |
|-------|-----------------|------------|
|       | **A**           | **B**      |
| **1** | **Formula**     | **Result** |
| **2** | `=BITAND(10,9)` | 8          |

 

The bitwise boolean AND of binary numbers “1110” and “0100” is the binary number “0100”, which is 4 in decimal.

|       |                                             |            |
|-------|---------------------------------------------|------------|
|       | **A**                                       | **B**      |
| **1** | **Formula**                                 | **Result** |
| **2** | `=BITAND(BIN2DEC("1110"), BIN2DEC("0100"))` | 4          |

## Related functions

- BITOR: The BITOR function returns the bitwise boolean OR of two numbers.
- BITXOR: The BITXOR function returns the bitwise boolean XOR (exclusive OR) of two numbers.
- BITLSHIFT: The BITLSHIFT function shifts the bits of the input a certain number of places to the left. Bits on the right are filled with zeroes (0s).
- BITRSHIFT: The BITRSHIFT function shifts the bits of the input a certain number of places to the right. Bits on the right are filled with zeroes (0s).
- [BIN2DEC](https://support.google.com/docs/answer/3092991): The BIN2DEC function converts a signed binary number to decimal format.
- [DEC2BIN](https://support.google.com/docs/answer/3092997): The DEC2BIN function converts a decimal number to signed binary format.
