---
fonte: https://support.google.com/appsheet/answer/10106345?hl=en
baixado: 2026-11-10
---

# Control add, update, and delete operations

[Configure the table settings](https://support.google.com/appsheet/answer/10105821#configure-table) to control whether app users can add, delete, or edit rows in a table. You can specify combinations of these options for each table. 

Separate permissions can be chosen for [table slices](https://support.google.com/appsheet/answer/10106592), but they must be at least as strict as the permissions of the original table.

In advanced scenarios, you can use an expression to dynamically compute the update mode. Click on the flask icon to set up the expression. There are two common use cases for dynamic update modes:

1.  To allow some users to make updates but restrict this functionality for others
2.  To allow updates for some rows but restrict updates for other rows

The following are the allowed values when using expressions: `ALL_CHANGES`, `ADDS_ONLY`,  `ADDS_AND_UPDATES`, `ADDS_AND_DELETES`,  `UPDATES_ONLY`, `UPDATES_AND_DELETES`, `DELETES_ONLY`, and `READ_ONLY`

For example, allows `user1@mydomain.com` to update content and allows all other users read-only access.

`SWITCH(USEREMAIL(), `
`  "user1@mydomain.com", "UPDATES_ONLY", `
`  "READ_ONLY")`

## Allow adding rows, but do not show existing rows

In some apps (like public apps that are used to collect data from anonymous users), you may want to capture new data in forms (that is, allow adds) but not show any existing data. Turn on **Filter out all existing rows?** in the **Security** section when [configuring the table settings](https://support.google.com/appsheet/answer/10105821#configure-table). If you enable this setting for a table, none of the existing rows are read.
