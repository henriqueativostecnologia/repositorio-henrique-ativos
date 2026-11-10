---
fonte: https://support.google.com/appsheet/answer/10106628?hl=en
baixado: 2026-11-10
---

# Conditionally show or hide a column value (Show_If)

Column constraints are UI features that affect the app's behavior and presentation. They aren't security controls and don't prevent users from accessing the data. For information about securing your data, see [Security: The Essentials](https://support.google.com/appsheet/answer/10105078).

A `Show_If` [column constraint](https://support.google.com/appsheet/answer/10107948) may be used to show or hide a column *value* according to a condition. This column constraint doesn't control whether or not the column is displayed, just the value for a particular row.

`Show_If` is commonly used to:

- Hide columns that aren't intended for [forms](https://support.google.com/appsheet/answer/10107846).
- Show only non-zero values in a column of numeric values.
- Show [action buttons](https://support.google.com/appsheet/answer/10107706) in only select views.

**New to expressions?** See also [Expressions: The Essentials](https://support.google.com/appsheet/answer/10104642).

## The Show_If expression

The `Show_If` column constraint is [Yes/No expression](https://support.google.com/appsheet/answer/10107946): if the expression evaluates as `TRUE`, the column value will be shown; if `FALSE`, the column value will be hidden.

As in all column constraint expressions, the `Show_If` expression may refer to the current column value using the column value expression, `[_THIS]`. For instance, if the current column is `Employee Name`, `[Employee Name]` and `[_THIS]` both refer to the same value.

## Scope of Show_If

The `Show_If` column constraint is applied any time the column itself is displayed. The column constraint is not applied to the column value when used in an expression.

`Show_If` conditions can enabled for only form views or for the entire app. To control this behavior, set the **Apply show-if constraints universally** when [configuring form view type settings](https://support.google.com/appsheet/answer/10107387).
