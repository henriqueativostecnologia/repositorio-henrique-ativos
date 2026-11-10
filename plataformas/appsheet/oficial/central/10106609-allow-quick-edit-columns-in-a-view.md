---
fonte: https://support.google.com/appsheet/answer/10106609?hl=en
baixado: 2026-11-10
---

# Allow quick edit columns in a view

Quick edit columns allows you to mark specific columns to be editable directly from the detail view. For example, quick edit is ideal for updating the **Status** field of a record without editing the full record.

The following columns **cannot** be set as quick edit columns:

- Key columns
- Read-only columns
- Columns computed by an AppFormula or sheet formula
- System columns like row number
- `Change` type columns
- Columns with [`Editable_If`](https://support.google.com/appsheet/answer/10107954) expressions that disallow edits.

Other notes about quick edit columns:

- Changes to quick edit columns can cause other column values to change through formula dependencies.

- [`Valid_If`](https://support.google.com/appsheet/answer/10107949) and [`Required_If`](https://support.google.com/appsheet/answer/10106535) conditions will be applied. Changes that violate either the `Valid_If` or `Required_If` conditions will be rejected.

- Each edit is a separate row update, so quick edit is best used together with the **Delayed Sync** option. You can set **Delayed Sync** when [configuring offline and sync](https://support.google.com/appsheet/answer/10107724).

Add quick edit columns as described in the following sections:

- [Get started with an app template](#get-started)
- [Add a quick edit column](#add-quick-edit-columns)

## Get started with an app template

The [Quote Generator](https://www.appsheet.com/templates/Produce-job-quotes-and-proposals-Workflows-email-quotes-and-proposals-to-customers?appGuidString=6f8708d5-689e-4b90-bb98-feeafa470d7b) app template demonstrates a quick edit column. 

When configuring the **Customer Quotes_Detail** view, the **10%Deposit Paid** column is added to the **Quick edit columns** list.

Quick edit columns with 10%Deposit Paid column

When using the app, the value is editable in the detail view.

Quick edit column in detail view in app

## Add quick edit columns

To add quick edit columns:

1.   Open the app in the editor.
2.  Go to **App ** App icon **\> Views**.
     We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

    ## If you are using the legacy editor

    Go to **UX \> Views**.  
3.  [Create a detail view](https://support.google.com/appsheet/answer/10106385) for the table or slice you wish to configure as quick edit. The table or slice must allow edits.
4.  Expand the newly added view.
5.  Add one or more **Quick edit columns**.
6.  Set the view [position](https://support.google.com/appsheet/answer/10106688#position) to **ref** if you do not want to add a button for this new detail view.
