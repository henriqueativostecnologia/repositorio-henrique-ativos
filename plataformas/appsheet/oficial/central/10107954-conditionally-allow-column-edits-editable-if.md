---
fonte: https://support.google.com/appsheet/answer/10107954?hl=en
baixado: 2026-11-10
---

# Conditionally allow column edits (Editable_If)

Column constraints are UI features that affect the app's behavior and presentation. They aren't security controls and don't prevent users from accessing the data. For information about securing your data, see [Security: The Essentials](https://support.google.com/appsheet/answer/10105078).

The `Editable_If` [column constraint](https://support.google.com/appsheet/answer/10107948) may be used to limit the user's ability to edit a column value for a row.

`Editable_If` is commonly used to only allow column value changes:

- By administrators or specific users, but not others.
- When another column has a specific value.
- When adding a new row, but not when editing an existing one.
- When no value has yet been provided.

**New to expressions?** See also [Expressions: The Essentials](https://support.google.com/appsheet/answer/10104642).

## The Editable_If Expression

The `Editable_If` column constraint is [a Yes/No expression](https://support.google.com/appsheet/answer/10107946): if the expression evaluates as `TRUE`, the user is allowed to edit the column value; if `FALSE`, the user is not allowed.

As in all column constraint expressions, the `Editable_If` expression may refer to the current column value using the column value expression, `[_THIS]`. For instance, if the current column is `Employee Name`, `[Employee Name]` and `[_THIS]` both refer to the same value.

#### Examples

`("Admin" = USERROLE())` - Allow only designated app admins. See also: [`USERROLE()`](https://support.google.com/appsheet/answer/10108128)

`IN(USEREMAIL(), LIST("joe@example.biz", "mary@example.biz"))` - Allow only specific users. See also: [`LIST()`](https://support.google.com/appsheet/answer/10107339), [`USEREMAIL()`](https://support.google.com/appsheet/answer/10108210)

`(USEREMAIL() = [Email])` - Allow only if the *Email* column value matches the current user. See also: [`USEREMAIL()`](https://support.google.com/appsheet/answer/10108210)

`NOT(IN([Employee ID], Employees[Employee ID]))` - Allow only for a new row, but not an existing row. See also: [`IN()`](https://support.google.com/appsheet/answer/10107681), [`NOT()`](https://support.google.com/appsheet/answer/10107360)

`ISBLANK(LOOKUP([_THISROW].[Employee ID], "Employees", "Employee ID", "Name"))` - Allow only if the *`Name`* has not been previously set for this `Employee ID`. See also: [`ISBLANK()`](https://support.google.com/appsheet/answer/10107337), [`LOOKUP()`](https://support.google.com/appsheet/answer/10107410)

`(NOW() < ([Timestamp] + "024:00:00"))` - Allow only if the row is less than a day old. See also: [`NOW()`](https://support.google.com/appsheet/answer/10108119)

`AND((TIMENOW() >= "08:00:00"), (TIMENOW() < "18:00:00"))` - Allow only during business hours. See also: [`AND()`](https://support.google.com/appsheet/answer/10107398), [`TIMENOW()`](https://support.google.com/appsheet/answer/10107985)

`(WEEKDAY(TODAY()) = 2)` - Allow only on Mondays. See also: [`TODAY()`](https://support.google.com/appsheet/answer/10108286), [`WEEKDAY()`](https://support.google.com/appsheet/answer/10107424)

`FALSE` : Prohibit all user changes while allowing changes by [app formulas and initial values](https://support.google.com/appsheet/answer/10106437), and [actions](https://support.google.com/appsheet/answer/10107706).

## Setting Editable_If

To set a column's `Editable_If` column constraint, go to the **Data \> Columns** tab in the app editor and click on the edit icon next to the desired column:

Edit icon in the Columns page of the Data section.

Scroll down to locate (and, if necessary, expand) the **Update Behavior** section, which contains the **Editable?** setting. Clicking the flask icon to the right will replace the ON/OFF switch with an expression box.

Click in the expression box to enter your `Editable_If` expression. To remove the `Editable_If` column constraint, click the X to the right of the expression box.

Editable field with an expression defined.

## Scope of Editable_If

The `Editable_If `column constraint **only affects the user's access** to the column value, such as when the user interacts with [a](https://support.google.com/appsheet/answer/10108121) [Form view](https://support.google.com/appsheet/answer/10107846) containing the column. The constraint is also checked before allowing access to [Quick Edit](https://support.google.com/appsheet/answer/10106609) columns (such as, in a [Detail](https://support.google.com/appsheet/answer/10106385) or [Table](https://support.google.com/appsheet/answer/10106514) view).

`Editable_If` **does not affect** the application of [app formulas and initial values](https://support.google.com/appsheet/answer/10106437), the performance of [actions](https://support.google.com/appsheet/answer/10107706), or any other app behaviors.

`Editable_If` is consulted only if all of the following are true:

- The table containing the column [allows adds or updates](https://support.google.com/appsheet/answer/10106345).
- The slice containing the column (if applicable) [allows adds or updates](https://support.google.com/appsheet/answer/10106592).
- The column has an `Editable_If` expression set.

`Editable_If` can only be used to reduce access; it cannot be used to expand access beyond that allowed by the underlying slice or table.
