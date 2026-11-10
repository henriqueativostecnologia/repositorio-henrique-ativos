---
fonte: https://support.google.com/appsheet/answer/10107372?hl=en
baixado: 2026-11-10
---

# Use bulk actions

Bulk actions allow you to quickly execute an action on a set of rows. Bulk actions are supported in a table, deck, or gallery view that has one or more actions or that allows users to delete records.

There are two ways to perform bulk actions:

- App creators can add a **Data: execute an action on a set of rows** action to automatically select rows using an expression. See [Data: execute an action on a set of rows](https://support.google.com/appsheet/answer/10107706#data-change) for more information.
- App users can use bulk select to manually select the rows to execute an action on  (described below).

## Use bulk select

As an app user, if you work with applications that contain to-do lists, site management, or other daily reporting functions, using bulk select will enable you to work more efficiently. 

For example, to use bulk select in an expense tracking application that contains new expenses that require approval:

1.  Click   in the table, deck, or gallery view. Alternatively, you can long-press any row to enter selection mode.

2.  Once in bulk selection mode, tap on rows to select them. As you select rows, actions will appear in the top right corner of the screen. 
    **Note**: Only actions that are valid for all selected rows will appear.

    Select rows, notice valid actions appear in the top right corner
3.  Tap an action (such as approve) to update all the selected rows.
    If the app has delayed sync enabled, the changes will be queued; otherwise a sync will be triggered.

    Expenses are now all shown as approved
