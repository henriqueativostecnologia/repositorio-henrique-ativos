---
fonte: https://support.google.com/docs/answer/7410791?hl=en
baixado: 2026-11-10
---

# IMCONJUGATE

Returns the complex conjugate of a number.

### Sample Usage

`IMCONJUGATE("3+4i")`

`IMCONJUGATE("-2i")`

### Syntax

`IMCONJUGATE(number)`

- `number` - The complex number to calculate the conjugate for.

### Notes

- The complex conjugate is defined as follows:
  - IMCONJUGATE Equation

### See also

- [`COMPLEX`](https://support.google.com/docs/answer/7407888): The COMPLEX function creates a complex number, given real and imaginary coefficients.
- [`IMREAL`](https://support.google.com/docs/answer/7408138): Returns the real coefficient of a complex number.
- [`IMAGINARY`](https://support.google.com/docs/answer/7408639): Returns the imaginary coefficient of a complex number.

### Examples

| **1** | A                                    | B          |
|-------|--------------------------------------|------------|
| 2     | **Formula**                          | **Result** |
| 3     | `=IMCONJUGATE("3+4i")`               | 3-4i       |
| 4     | `=IMCONJUGATE(COMPLEX(-2, -5, "j"))` | -2+5j      |
