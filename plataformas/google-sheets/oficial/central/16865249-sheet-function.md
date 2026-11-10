---
fonte: https://support.google.com/docs/answer/16865249?hl=en
baixado: 2026-11-10
---

# SHEET function

This returns the sheet number of the specified sheet or other reference.

## Sample usage

`SHEET()`

`SHEET(Table1)`

`SHEET(Sheet1!A1)`

## Syntax

`SHEET(value)`

- `value` - **\[** OPTIONAL **\]** - The value to be verified as a sheet name or other reference.
  - If you don’t include an argument, the function will return the sheet number of the sheet where the formula is located.

## Notes

- The `SHEET` function returns the sheet number of the referenced sheet, table, or range.
- The first sheet is Sheet1, the second is Sheet2, and so on.
- `SHEET` takes a single argument.
- If `value` isn't a valid sheet name or reference, `SHEET` returns an error.

## See also

`SHEETS`: Returns the total number of sheets in the spreadsheet.

`ISNUMBER(value)`: Checks whether a value is a number.

`CELL(info_type, reference)`: Returns the requested information about the specified cell.
