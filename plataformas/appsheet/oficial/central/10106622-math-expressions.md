---
fonte: https://support.google.com/appsheet/answer/10106622?hl=en
baixado: 2026-11-10
---

# Math expressions

Calculate numeric values from other numeric values

The following sections describe the components for building Math expressions:

- [Math operators](#math-operators)
- [Math functions](#math-functions)
- [Numeric types](#numeric-types)

**New to expressions?** See also [Expressions: The Essentials](https://support.google.com/appsheet/answer/10104642).

## Math operators

The common numeric operators below may be used in math expressions.

### Add

The plus character (`+`) between two numeric values produces the result of adding them together. If both values are of the `Number` type, the result will be a `Number`; otherwise the result will be `Decimal`.

Examples:

- `2 + 2`
- `[Count] + 1`
- `[Price] + [Tax]` 

### Divide

The slash character (`/`) between two numeric values produces the result of dividing the left value by the right value. If both values are of the `Number` type, the result will be a `Number`; otherwise the result will be `Decimal`.

Examples:

- `4 / 2`
- `([Day Count] / 7.0)` 
- `[Total] / [Unit Count]` 

### Multiply

The asterisk character (`*`) between two numeric values produces the result of multiplying them together. If both values are of the `Number` type, the result will be a `Number`; otherwise the result will be `Decimal`.

Examples:

- `(10.0 * 10)`

- `[Week Count] * 7`

- `[Unit Cost] * [Unit Price]` 

### Negate

The minus character (`-`) preceding a single numeric value produces the arithmetic negation of the value: a positive value becomes negative, a negative value becomes positive. The type of the result will match that of the original value.

Examples:

- `-18.56`
- `-[Unit Count]`
- `-([Seat Count] * [Gift Value])`

### Subtract

The minus character (`-`) between two numeric values produces the result of subtracting the right value from the left value. If both values are of the `Number` type, the result will be a `Number`; otherwise the result will be `Decimal`.

Examples:

- `124.0 - 18.9`
- `(14.0 - [Vacation Days Used])`
- `[Price] - [Discount]`

 

## Math functions

The following Math functions can be used in math expressions within your app:

- [`ABS()`](https://support.google.com/appsheet/answer/10107329): Absolute value
- [`AVERAGE()`](https://support.google.com/appsheet/answer/10107675): Average of list of values
- [`CEILING()`](https://support.google.com/appsheet/answer/10104440): Nearest higher `Number`
- [`DECIMAL()`](https://support.google.com/appsheet/answer/10107887): `Decimal` from any value
- [`FLOOR()`](https://support.google.com/appsheet/answer/10106537): Nearest lower `Number`
- [`LN()`](https://support.google.com/appsheet/answer/10107406): Natural log
- [`LOG()`](https://support.google.com/appsheet/answer/10107407): Logarithm
- [`LOG2()`](https://support.google.com/appsheet/answer/10107968): Log base 2
- [`LOG10()`](https://support.google.com/appsheet/answer/10108107): Log base 10
- [`MOD()`](https://support.google.com/appsheet/answer/10108110): Remainder from `Number` division
- [`NUMBER()`](https://support.google.com/appsheet/answer/10108120): `Number` from any value
- [`POWER()`](https://support.google.com/appsheet/answer/10106551): Exponentiation
- [`RANDBETWEEN()`](https://support.google.com/appsheet/answer/10107982): Random `Number`
- [`ROUND()`](https://support.google.com/appsheet/answer/10108206): Nearest `Number`
- [`SQRT()`](https://support.google.com/appsheet/answer/10107366): Square root
- [`STDEVP()`](https://support.google.com/appsheet/answer/10107930): Standard deviation of list of values
- [`SUM()`](https://support.google.com/appsheet/answer/10107699): Sum of list of values

## Numeric types

AppSheet understands two basic numeric [data types](https://support.google.com/appsheet/answer/10106435):

`Decimal`: numbers that include a decimal point separating a whole number component from a fractional component. For example: `-0.03`, `0.0`, `3.14159`, `14.99`. Also known as a real number or floating-point number. The number of digits displayed after the decimal point (2 by default) can be changed in a `Decimal` column's configuration. The display format is also affected by the [app user's locale](https://support.google.com/appsheet/answer/10106783). See also: [`DECIMAL()`](https://support.google.com/appsheet/answer/10107887)

`Number`: numbers that do not include a decimal point. For example: `-29`, `-5`, `0`, `732`, `4096`. Also known as integers or whole numbers. See also: [`NUMBER()`](https://support.google.com/appsheet/answer/10108120)

Several other data types are based on the above:

`Percent` is a `Decimal` with special display characteristics. For example, a `Percent` value of `0.0` is displayed as 0%; `0.05` is displayed as 5%; `0.2` as 20%; and `1.0` as 100%.

`Price` is a `Decimal` with special display characteristics. For example, a `Price` value of `0.0` is displayed as \$0.00; `5.2` is displayed as \$5.20; `67.482` as \$67.48; and `100.0` as \$100.00. The currency symbol (`$` by default) can be changed in a `Price` column's configuration.
