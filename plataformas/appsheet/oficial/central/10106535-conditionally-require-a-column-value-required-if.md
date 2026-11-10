---
fonte: https://support.google.com/appsheet/answer/10106535?hl=en
baixado: 2026-11-10
---

# Conditionally require a column value (Required_If)

Column constraints are UI features that affect the app's behavior and presentation. They aren't security controls and don't prevent users from accessing the data. For information about securing your data, see [Security: The Essentials](https://support.google.com/appsheet/answer/10105078).

The `Required_If` [column constraint](https://support.google.com/appsheet/answer/10107948) may be used to require a column value of a row be present before the row may be saved. If a required column value is blank, the row cannot be saved.

`Required_If` is commonly used to enforce conditional input requirements, such as:

- Requiring a signature if the balance is above a threshold.
- Requiring a card number if paying with credit or debit.
- Requiring completion of prerequisites first.

**New to expressions?** See also [Expressions: The Essentials](https://support.google.com/appsheet/answer/10104642).

## The Required_If expression

The `Required_If `column constraint is [a Yes/No expression](https://support.google.com/appsheet/answer/10107946). If the expression evaluates as `TRUE`, the column value may not be blank; if `FALSE`, the column value may be blank.

As in all column constraint expressions, the `Required_If` expression may refer to the current column value using the column value expression, `[_THIS]`. For instance, if the current column is `Employee `` Name`, `[Employee Name]` and `[_THIS]` both refer to the same value.

#### Examples

`([Subtotal] >= 20.0)` - Require a signature if the subtotal is over \$20.

`IN([Payment Type], {"Credit Card", "Debit Card"})` - Require a card number if the chosen payment type is a credit or debit card. See also: [`IN()`](https://support.google.com/appsheet/answer//10107681)

`ISNOTBLANK([Address Line 2])` - Require address line 1 if line 2 has been provided already. No address is fine, but if you provide line 2, you must provide line 1.  See also: [`ISNOTBLANK()`](https://support.google.com/appsheet/answer/10107964)

`AND(ISBLANK([Home]), ISBLANK([Mobile]), ISBLANK([Work]))` - Require at least one of the three phone numbers. See also: [`AND()`](https://support.google.com/appsheet/answer/10107398), [`ISBLANK()`](https://support.google.com/appsheet/answer/10107337)

`TRUE` - Require always. Equivalent to setting **Require?** to **ON**.

`FALSE` - Never require. Equivalent to setting **Require?** to **OFF**.

## Setting Required_If

To set a column's `Required_If` column constraint, go to the **Data \> Columns** tab in the app editor and click on the edit icon next to the desired column:

Edit icon in the Columns page of the Data section.

Scroll down to locate (and, if necessary, expand) the **Data Validity** section, which contains the **Require?** setting. Clicking the flask icon to the right will replace the ON/OFF switch with an expression box.

Require? appears in Data Validity section. Click flask to toggle expression box.

 

Click in the expression box to enter your `Required_If` expression. To remove the `Required_If` column constraint, click the **X** to the right of the expression box.

Require? set to an expression in the Data Validity section.

 

## Scope of Required_If

The `Required_If` column constraint is applied any time a row update is attempted, such as when the user interacts with a [Form view](https://support.google.com/appsheet/answer/10107846) or with a [Quick Edit](https://support.google.com/appsheet/answer/10106609) column (such as, in a [Detail](https://support.google.com/appsheet/answer/10106385) or [Table](https://support.google.com/appsheet/answer/10106514) view), when [app formulas and initial values](https://support.google.com/appsheet/answer/10106437) are applied, and when [actions](https://support.google.com/appsheet/answer/10107706) attempt a data-change operation.
