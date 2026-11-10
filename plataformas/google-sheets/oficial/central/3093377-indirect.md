---
fonte: https://support.google.com/docs/answer/3093377?hl=en
baixado: 2026-11-10
---

# INDIRECT

Returns a cell reference specified by a string.

## Examples

[Make a copy](https://docs.google.com/spreadsheets/d/1cbh9wUeE0UtIMPSEv51GE7qYix-qwOm_er0wW4LhuK0/copy)

**Note**: Each example is in its own tab.

### Sample Usage

`INDIRECT("Sheet2!"&B10)`

`INDIRECT("A2")`

`INDIRECT("R2C3", FALSE)`

### Student info

Student Info data as a separate sheet in the spreadsheet.

Embedded content: https://docs.google.com/spreadsheet/pub?key=0As3tAuweYU9QdDNOSklLU1hCdGpaNHhlX3VFTlBBLVE&single=true&gid=1&output=html&widget=true

### Student grades

Returns the contents of the reference which can be a cell or an area.

Embedded content: https://docs.google.com/spreadsheet/pub?key=0As3tAuweYU9QdDNOSklLU1hCdGpaNHhlX3VFTlBBLVE&single=true&gid=0&output=html&widget=true

Embedded content: https://docs.google.com/spreadsheet/pub?key=0As3tAuweYU9QdDNOSklLU1hCdGpaNHhlX3VFTlBBLVE&single=true&gid=0&output=html&widget=true

### Syntax

`INDIRECT(cell_reference_as_string, [is_A1_notation])`

- `cell_reference_as_string` - A cell reference, written as a string with surrounding quotation marks.
- `use_a1_notation` - \[ OPTIONAL - `TRUE` by default \] - A boolean indicating whether to use `A1` style notation (TRUE) or `R1C1` style notation (FALSE).
