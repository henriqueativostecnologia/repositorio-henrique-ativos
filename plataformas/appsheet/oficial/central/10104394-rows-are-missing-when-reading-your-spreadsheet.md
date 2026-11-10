---
fonte: https://support.google.com/appsheet/answer/10104394?hl=en
baixado: 2026-11-10
---

# Rows are missing when reading your spreadsheet

When reading your spreadsheet, AppSheet must determine which rows contain valid data. For example, your spreadsheet may contain 1000 rows but most of those rows may be empty. AppSheet must ignore those empty rows.

AppSheet detects empty rows by examining each row in the spreadsheet. If a row contains at least one non-empty column value, AppSheet treats the row as a valid row. If every column value in the row is empty, AppSheet treats the row as an empty row and ignores it.

Columns containing Array formulas complicate empty row detection. A column with an array formula can have a non-empty field value even if the row is otherwise empty. That is the nature of array formulas. Consequently, AppSheet ignores any column having an array formula when deciding whether a row is empty.

You must ensure that at least one column in every row of your spreadsheet contains a non-empty value. Columns containing array formulas are ignored, so make sure the non-empty value is in some other column of the row.
