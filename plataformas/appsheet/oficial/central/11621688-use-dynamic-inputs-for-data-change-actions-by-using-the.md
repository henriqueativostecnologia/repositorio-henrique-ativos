---
fonte: https://support.google.com/appsheet/answer/11621688?hl=en
baixado: 2026-11-10
---

# Use dynamic inputs for data change actions by using the INPUT() function

**Note**: **The `INPUT()` function and the ability to bind the inputs to dynamic values, as described in this section, is no longer supported**.

 

Use the new INPUT syntax described in [Set input values dynamically in data-change actions](https://support.google.com/appsheet/answer/13779963). For information about the new syntax and recommended migration plan, see the [community announcement](https://www.googlecloudcommunity.com/gc/Announcements/General-Availability-fort-the-INPUT-functionality-with-updated/m-p/679261).

Data change actions are logical operations that modify data values. The desired new values are defined by expressions. In many cases, that value is constant (for example, an action to `ApproveOrder` sets the status of the `Order` to "Approved") or it has a well-defined expression (for example, an action to `EstimateDeliveryDate` sets the estimated delivery date of the `Order` to the maximum of the delivery dates of each of its sub-orders).

However, there are also situations that need a dynamic input specified either by the user in an app dialog, or specified by another invoking action. This is where the [`INPUT()`](https://support.google.com/appsheet/answer/11623804) function can be used.

Let’s consider an app with `Orders` and `Customers`. Let us say there is a `ChangeStatus` action on an `Order` that changes a status to "Complete" and also records a comment. This would be implemented in AppSheet as a `SetColumnValue` action with two columns that are set by expressions (`Status`: “Complete”, and `Notes`: “n/a”). For the app user, this action shows up as a “ChangeStatus” button in their app.

1.  Let’s assume we want to ask the app user to provide the notes that will be saved. To do so, the `ChangeStatus` action would set the value of `Notes` to `INPUT("NotesInput", "n/a")`. This means it is a special text input called "NotesInput" with a default value of "n/a". When the app user clicks the ChangeStatus button, they will be prompted with a dialog that asks them to provide the notes.

2.  Now let’s also assume we occasionally want to cancel a customer’s account. In that case, we want a single `CancelAccount` action on the `Customer` record that will go to all the orders of that customer and set their status to “Complete” with the notes saying “Account cancelled”. To do this, a Reference Action that can be defined on the `Customer`. This action can specify a set of `Orders` to be acted on (those that are created for this customer) and an action to invoke on them (ChangeStatus). Now in order to pass the desired values (“Account Cancelled”) for the notes column to the ChangeStatus action, the Reference Action definition has the ability to bind the NotesInput value to an expression (in this case, constant text "Account Cancelled", but in general, it can be any expression that is appropriate in the context of a `Customer`).

Here is an example of an action that sets the value of a column. It uses an `INPUT()` function.

Quantity is defined using an INPUT() function.

Here is an example of an action that references another action and binds its inputs to dynamic values.

Action references another action and binds its inputs to dynamic values.

The `INPUT()` function can be used in any expression but will always evaluate to its default value except for the specific usage scenarios below.

**Scenario**: In a Data Change Action that sets the value of a column, the `INPUT()` function must be used as the top-level expression (for example, `Notes` assigned to `INPUT("NotesInput", "n/a")`)

- When this action is invoked via a user button click in the app user interface, it will prompt a dialog that asks the user to provide the value.
- When this action is invoked from a Reference Action (whether in the running app or in an automation), the Reference Action can specify a binding expression.

Don't use nested expressions, such as `[Quantity] + INPUT("Quantity", 0)`. If you specify a nested expression, the user prompt won't be displayed.
