---
fonte: https://support.google.com/appsheet/answer/11918330?hl=en
baixado: 2026-11-10
---

# Edit multiple rows using CSV export and import

You can edit multiple rows in a table by:

1.  Exporting the rows of a view to a CSV file using the [Export this view to a CSV file](https://support.google.com/appsheet/answer/11579391) action.
2.  Updating the row data in the CSV file. When the key value in the CSV row matches the key of an existing table record, then that table record will be updated when the CSV file is Imported.
3.  You can also add new rows to the CSV file.
    1.  If the key value specified in the CSV row does not match the key of an existing table record, then a new record with the specified key will be added to the table.
    2.  If the key value is omitted from the CSV row and the table's key field contains an `Initial value` of [`UNIQUEID()`](https://support.google.com/appsheet/answer/10108209) or [`RANDBETWEEN()`](https://support.google.com/appsheet/answer/10107982), then the system will add the new row and initialize the row's key field to the `Initial value`.
4.  [Importing the rows](https://support.google.com/appsheet/answer/11510988) of the CSV file to the view.

Import and Export are symmetric. If you Export in a locale it is best to Import in that locale.

This action only works on desktop browsers and not on iOS or Android devices.
