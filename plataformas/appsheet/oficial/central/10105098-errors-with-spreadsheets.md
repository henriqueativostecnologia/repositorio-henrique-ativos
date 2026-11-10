---
fonte: https://support.google.com/appsheet/answer/10105098?hl=en
baixado: 2026-11-10
---

# Errors with spreadsheets

The following sections provide guidance for resolving errors with spreadsheets:

- [Errors with spreadsheet structure](#spreadsheet-structure)
- [Errors accessing spreadsheet](#spreadsheet-access)

## Errors with spreadsheet structure

AppSheet automatically extracts structure from a spreadsheet so that your app can be generated. While most spreadsheets are simple tabular structures, there are also ways to use spreadsheets that are incompatible with AppSheet. So you may see errors, warnings, and information messages in the app editor when AppSheet reads your spreadsheet. 

- Errors with spreadsheet structure -- these errors typically occur when AppSheet is unable to properly identify the column headers. Often this is because the first worksheet in your spreadsheet has non-tabular data like charts or pictures.

- Errors when switching spreadsheets -- when you switch to a different spreadsheet, AppSheet tries to retain as much as possible of your existing app. However, the new spreadsheet may have a totally different column structure. In this case, you may see errors that ask you to change the other parts of the app definition appropriately.

- Warnings about column structure mismatch -- this is the most common warning seen during the app creation process. As users modify spreadsheets, they add, remove, or rename columns. Each time you do this and tell AppSheet to refresh the column structure, you are warned if the old column structure and new structure do not align. AppSheet always adjusts to the new structure, so this is a warning, not an error.

- Warnings about formulas -- there are only certain kinds of spreadsheet formulas that make sense to use in your data. See [Spreadsheet formulas](https://support.google.com/appsheet/answer/10099797).

- Information about the [key](https://support.google.com/appsheet/answer/10106672) column -- as described earlier, this information tells you which column is chosen as the key. The key also plays an important part in the presentation of data as described in the UX section. If AppSheet cannot find a good key column, it tries to combine pairs of columns to find a composite key. If that also fails, it settles for the row number (an implicit column). This is typically not a good choice unless you have an app that is purely showing information and prevents all edits. This is because the number of a row in a spreadsheet changes dynamically as rows are being added to or deleted from the spreadsheet either directly or through the app.

## Errors accessing a spreadsheet

AppSheet can experience errors reading or writing spreadsheet data from any cloud storage provider. 

- Error `401` -- this occurs when AppSheet does not have permission to work on behalf of the user.
- Error `403` (permission denied) -- this occurs when AppSheet tries to access your spreadsheet, but the storage provider responds that AppSheet does not have the permission to access it. 
- Error `404` (cannot access the spreadsheet) -- this occurs when AppSheet tries to access your spreadsheet but the storage provider responds that no such document exists. Perhaps you have deleted, renamed, or moved the document? Perhaps you never had access to it?
- Timeout -- occasionally, the remote storage provider has a timeout and fails to provide the spreadsheet data to AppSheet despite repeated retries. Although fewer than 1% of our requests encounter such issues, it is still significant enough that you may encounter such a problem. You may experience this problem as an unexpected delay during Sync, or even a sync failure. Typically a refresh or retry after a few seconds rectifies the problem.
- Error `500` (internal server error)  -- very infrequently the remote storage provider has an internal error and fails to provide the spreadsheet data to AppSheet. Typically this is a transient problem and often is hidden from our users because we automatically retry the request.
