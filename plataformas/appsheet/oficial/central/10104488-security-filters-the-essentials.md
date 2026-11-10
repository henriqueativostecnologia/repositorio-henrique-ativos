---
fonte: https://support.google.com/appsheet/answer/10104488?hl=en
baixado: 2026-11-10
---

# Security filters: The Essentials

This feature is available to **AppSheet Core** accounts and above. See [AppSheet pricing](https://about.appsheet.com/pricing/).

Although security filters limit data access, they aren't a complete security solution. Users should protect sensitive data operations at the data source level. For more information about securing your data, see [Security: The Essentials](https://support.google.com/appsheet/answer/10105078).

A security filter is an optional [Yes/No](https://support.google.com/appsheet/answer/10107946) expression that is evaluated for each row in a table. If true, the row is included in the app and if false, the row is not included.

To configure a security filter for a table, do the following:

1.  Open the app in the app editor.
2.  Go to **Security \> Security filters**.
3.  Expand the table for which you want to add a security filter.
4.  In the **Security filter** field, define an expression to restrict the rows displayed. 

You can also define security filters when [configuring table settings](https://support.google.com/appsheet/answer/10105821#configure-table).

To limit user access to a user's own data, [require user sign-in](https://support.google.com/appsheet/answer/10104975) and use the user's email address to filter the data shown to that user, as described in [Limit users to their own data](https://support.google.com/appsheet/answer/10104977). For example, to display only items assigned to the current user, set the security filter condition to: `[AssignedTo]=USEREMAIL()` 

While **security filters** are primarily meant to be a security feature, they can also be used as a *scalability feature*, as described in the following sections:

- [Security filters versus table slices](https://support.google.com/appsheet/answer/10104706#security-filters-versus-slices)
- [Security filters with spreadsheet data](https://support.google.com/appsheet/answer/10104706#security-filters-with-spreadsheet-data)
- [Security filters with database data](https://support.google.com/appsheet/answer/10104706#security-filters-with-database-data)
- [Efficient security filter definitions for database data](https://support.google.com/appsheet/answer/10104706#efficient-definitions-for-database-data)
- [Security filters with AppSheet databases](https://support.google.com/appsheet/answer/10104706#security-filters-with-appsheet-databases)
