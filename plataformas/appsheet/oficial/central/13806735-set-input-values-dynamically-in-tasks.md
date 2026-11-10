---
fonte: https://support.google.com/appsheet/answer/13806735?hl=en
baixado: 2026-11-10
---

# Set input values dynamically in tasks

When a task is reused in multiple steps in an automation, the app creator can dynamically configure the task for each step by setting input values.

Input values (`[_INPUT].[`*`inputname`*`]`) and `INPUT()` functions can't be used in the same action or task. They can be used in the same automation or app.

To add inputs when adding a task to a bot:

1.  Expand the **Advanced** section.
2.  Click **Add** under Inputs.
3.  Enter the name of the input value in the **Name** field.
4.  Select the data type from the **Type** drop-down.
    Only a subset of data types are supported for inputs.
5.  To add an initial value or edit any fields:
    1.  Click  to open the Input dialog.
    2.  Add a value or expression in the **Initial value** field.
        If you don't specify an initial value, then the input value will be required. If an initial value is specified, then the input value is optional.
        Use of `[_THIS]` or `[_INPUT]` are not supported in the Initial value field.
    3.  Edit other fields, as required.
    4.  Click **Done**.
6.  Repeat to add additional input values.

Then, use the following expressions to access the input values from the current step: `[_INPUT].[`*`inputname`*`]`

For example, the following Send an email task has defined a **Message** input that is used in the message body (`[_INPUT].[Message]`). When the task is used in a step, the app creator can customize the message that appears in the email (for example, `Thank you!`).

Set input values dynamically in tasks
