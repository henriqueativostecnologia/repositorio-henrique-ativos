---
fonte: https://support.google.com/appsheet/answer/13779963?hl=en
baixado: 2026-11-10
---

# Set input values dynamically in data-change actions

Data change actions are logical operations that modify data values. The desired new values are defined by expressions. In many cases, that value is constant (for example, an action to Approve Order sets the status of the Order to "Approved") or it has a well-defined expression (for example, an action to Estimate Delivery Date action sets the estimated delivery date of the Order to the maximum of the delivery dates of each of its sub-orders). However, there are also situations that need to set an input value dynamically either by the user in an app dialog, or specified by another invoking action. 

Set input values dynamically in a data-change action, as follows:

- When the action is used in the app, display a dialog to prompt the app user to enter values for the specified inputs. See [Set input values dynamically for columns in a row by prompting user](#set-values-rows-dynamic-input).
- When the action is used in an automation, the app creator sets custom input values when configuring the step. See [Set input values dynamically when running an action on a set of rows in an automation](#set-row-values-automation-dynamic-input).
- When the action is invoked from a Referenced Action (whether in the running app or in an automation), the Referenced Action can specify a binding expression using the input values. See [Set input values dynamically when running an action on a set of rows (referenced actions)](#set-row-values-automation-dynamic-input).

In the action, use the following expression to access the input values: `[_INPUT].[`*`inputname`*`]`

To learn how to add input values when configuring an action, see [Inputs](https://support.google.com/appsheet/answer/10107706#advanced).

Input values (`[_INPUT].[`*`inputname`*`]`) and `INPUT()` functions can't be used in the same action or task. They can be used in the same automation or app.

## Set input values dynamically for columns in a row by prompting user

When an action is used in the app, you can display a dialog to prompt the app user to enter values for the specified inputs.

For example, consider an app with `Orders` and `Customers`. Let's say there is a Change Status action on an `Order` that changes the status to "Shipped" and also records a comment. In AppSheet, this would be implemented as a **Data: set the values of some columns in this row** action with two columns that are set by expressions: 

- `Status`: “Shipped”
- `Details`: “Some notes*"* ("n/a" by default)

For the app user, this action shows up as a “Change Status” button in their app.

Let’s assume we want to ask the app user to provide the notes that will be saved in the `Details` column. To do so, for the Change Status action, expand the **Advanced** section and add an input value, such as **Notes**, with an initial value of **n/a**. For example:

Input configuration showing Notes defined with an initial value of n/a

Then, you can use the input value to set the value of the `Details` column by using the expression: `[_INPUT].[Notes]`

Using an input value to set a column

When the app user clicks the Change Status button, they will be prompted with a dialog that asks them to provide the details. 

Don't use nested expressions, such as `[Amount]+[_INPUT].[Amount]`. If you specify a nested expression, the user prompt won't be displayed.

To learn how to add input values when configuring an action, see [Inputs](https://support.google.com/appsheet/answer/10107706#advanced).

## Set input values dynamically when running an action on a set of rows in an automation

You can set input values dynamically when running an acton on a set of rows in an automation by adding a [Run a data action](https://support.google.com/appsheet/answer/11463007#zippy=%2Crun-a-data-action) step and selecting **Set row values**. When an action is used in an automation, you (the app creator) can set custom input values when configuring the step.

For example, the following Run a data action step executes the Change Status action (defined in the previous section). For each step that runs the action, you can add custom details by setting the input value, Notes.

Run an action with dynamic input in an automation

## Set input values dynamically when running an action on a set of rows by using referenced actions

When the action is invoked from a Referenced Action (whether in the running app or in an automation), the Referenced Action can specify a binding expression using the input values.

Let's assume we occasionally want to cancel a customer’s account. In that case, we want a single Cancel Account action on the `Customer` record that will go to all the orders of that customer and set their status to “Complete” with the notes saying “Account cancelled”. To do this, a Referenced Action that can be defined on the `Customer` by adding a "Data: execute an action on a set of rows" action. This action can specify a set of `Orders` to be acted on (those that are created for this customer) and an action to invoke on them (Change Status). Now in order to pass the desired values (“Account Cancelled”) for the notes column to the Change Status action, set the Notes value to an expression in the the Referenced Action field (in this case, constant text "Account Cancelled", but in general, it can be any expression that is appropriate in the context of a `Customer`).

For example:

Using input values for a referenced action
