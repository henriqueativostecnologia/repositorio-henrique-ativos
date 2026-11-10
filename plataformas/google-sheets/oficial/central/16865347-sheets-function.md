---
fonte: https://support.google.com/docs/answer/16865347?hl=en
baixado: 2026-11-10
---

# SHEETS function

This returns the total number of sheets in the spreadsheet.

## Sample usage

`SHEETS()`

## Syntax

`SHEETS(reference)`

- `reference` - **\[** OPTIONAL **\]** - Reference identifies the number of sheets.
  - If `reference` isn’t included, `SHEETS` returns the number of sheets in the workbook that contains the function.

## Notes

- The `SHEETS` function returns the number of sheets in the referenced document.
- If you don’t provide an argument, the function will return the total number of sheets in the spreadsheet where the formula is located.
- `SHEETS` takes a single argument.
- If `value` isn’t a valid sheet name or reference, `SHEETS` returns an error.

## See also

`SHEET`: Returns the current sheet number if you don’t provide a reference.

`ISNUMBER(value)`: Checks whether a value is a number.

`CELL(info_type, reference)`: Returns the requested information about the specified cell.
