---
fonte: https://support.google.com/appsheet/answer/14255794?hl=en
baixado: 2026-11-10
---

# Troubleshoot AppSheet databases

Troubleshoot and resolve issues with AppSheet databases.

## Error: An error occurred while creating a new row

If you receive the following error when using an AppSheet database:

`An error occurred while creating a new row in AppSheet databases`

Check to see if you are using a custom key in your app other than the Row ID. As described in [Row ID key](https://support.google.com/appsheet/answer/10106672?), for AppSheet databases the default key is the Row ID which is automatically generated for each row and stored in the `Row ID` column. This key allows users to create and manage references in the database editor, as described in [*Add references between tables*](https://support.google.com/appsheet/answer/12798217). 

To resolve this issue, do **one** of the following:

- Use Row ID as the key in the table.
- In the AppSheet database, copy existing references to a new column using the procedure described in [Row ID key](https://support.google.com/appsheet/answer/10106672?).

Contact [AppSheet Support](https://support.google.com/appsheet/gethelp) if the above recommendations do not resolve the issue.
