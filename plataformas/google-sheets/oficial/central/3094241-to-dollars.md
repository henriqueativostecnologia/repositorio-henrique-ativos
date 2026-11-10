---
fonte: https://support.google.com/docs/answer/3094241?hl=en
baixado: 2026-11-10
---

# TO_DOLLARS

Converts a provided number to a dollar value.

### Sample Usage

`TO_DOLLARS(A2)`

`TO_DOLLARS(40826.43)`

### Syntax

`TO_DOLLARS(value)`

- `value` - The argument or reference to a cell to be converted to a dollar value.

  - If `value` is not a number or a reference to a cell containing a numeric value, `TO_DOLLARS` returns `value` without modification.

### Notes

- Because dates and percentages are backed by numbers, `TO_DOLLARS` will convert them successfully. However, these conversions are not typically meaningful.

- `TO_DOLLARS` is equivalent to applying Format -\> Number -\> Currency from the menu bar.

- `TO_DOLLARS` differs from the related function `DOLLAR` in that `DOLLAR` outputs text rather than applying a cell format to a number.

- `TO_DOLLARS` does not convert from other currencies into US Dollars. Please use the `GoogleFinance` function to convert currencies at current exchange rates.

### See Also

[`TO_TEXT`](https://support.google.com/docs/answer/3094285): Converts a provided numeric value to a text value.

[`TO_PURE_NUMBER`](https://support.google.com/docs/answer/3094243): Converts a provided date/time, percentage, currency or other formatted numeric value to a pure number without formatting.

[`TO_PERCENT`](https://support.google.com/docs/answer/3094284): Converts a provided number to a percentage.

[`TO_DATE`](https://support.google.com/docs/answer/3094239): Converts a provided number to a date.

[`N`](https://support.google.com/docs/answer/3093357): Returns the argument provided as a number.

[`GOOGLEFINANCE`](https://support.google.com/docs/answer/3093281): Fetches current or historical securities information from Google Finance.

[`DOLLAR`](https://support.google.com/docs/answer/3094071): Formats a number into the locale-specific currency format.

### Examples

Embedded content: https://docs.google.com/spreadsheet/pub?key=0As3tAuweYU9QdF9Sem5oRjBvelBUbG5YenpxVkIwVkE&output=html
