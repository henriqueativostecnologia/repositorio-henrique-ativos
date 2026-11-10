---
fonte: https://support.google.com/appsheet/answer/10107948?hl=en
baixado: 2026-11-10
---

# Use column constraints

Column constraints are UI features that affect the app's behavior and presentation. They aren't security controls and don't prevent users from accessing the data. For information about securing your data, see [Security: The Essentials](https://support.google.com/appsheet/answer/10105078).

Every column definition has a type that specifies what values are allowed in the column, as well as flags that specify if the column is hidden, if it's required for input, and so on. This is adequate for many apps, but sometimes a more dynamic or data-driven mechanism is needed. This is what column constraints provide. 

A column constraint is an expression that is dynamically computed to determine the behavior of a specific column when the user tries to enter or change its value.

Three column constraints govern the validity of input values for that column:

- [`Valid_If`](https://support.google.com/appsheet/answer/10107949)*:* What are acceptable values?
- [`Required_If`](https://support.google.com/appsheet/answer/10106535)*:* Is an empty value acceptable?
- [`Editable_If`](https://support.google.com/appsheet/answer/10107954)*:* Can it be modified at all?

Two further constraints are related to the presentation of the column:

- [`Show_If`](https://support.google.com/appsheet/answer/10106628)*:* Should the column be shown or hidden?

- [Suggested values](https://support.google.com/appsheet/answer/10107397)*:* A list of values to prompt the user with

An additional constraint can help influence how records are updated:

- [Reset on edit?](https://support.google.com/appsheet/answer/10106509#reset-on-edit)*:* Clear the value whenever that record is edited by a user

To add a column constraint, click the **Data \> Columns** tab and click the **Edit** icon at the left of the corresponding column definition.

**New to expressions?** See also [Expressions: The Essentials](https://support.google.com/appsheet/answer/10104642).

## Get started

Watch this video to learn more about using column constraints in your app.

Video: https://www.youtube.com/watch?v=wtJ-qaOWy5I

## Best practices

Column constraints give you the power to define very subtle or complex conditions, but users will only see the resulting behavior. As an app creator, it's important to provide adequate explanations for the columns affected by these expressions--particularly for `Valid_If` conditions--so users will know how to proceed if they provide an invalid column value. The best way to do so is by providing meaningful column descriptions.

When these expressions reference other fields in the row (not just `[_THIS]`), it's best to ensure they're always "backward" references to fields the user has already seen (meaning columns that come before the column being considered in the spreadsheet and appear above the column being considered in the `Columns` tab). Conditions containing "forward" references may be confusing to users and may cause problems with multi-page forms.
