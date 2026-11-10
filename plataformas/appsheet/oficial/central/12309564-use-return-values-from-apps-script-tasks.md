---
fonte: https://support.google.com/appsheet/answer/12309564?hl=en
baixado: 2026-11-10
---

# Use return values from Apps Script tasks

Configure and use return values in Apps Script automation tasks as described in the following sections:

- [What is an Apps Script task return value?](#about)
- [Configure the Apps Script return value in AppSheet](#configure)
- [Use the Apps Script return value in an automation](#use-return-value)
- [Use a nested field from the response](#nested-fields)
- [Type mapping between Apps Script and AppSheet](#type-mapping)
- [Type limitations](#type-limitations)
- [Automation limitation](#automation-limitation)
- [Tips for debugging return values](#debugging-tips)

## What is an Apps Script task return value?

Using [*Apps Script tasks*](https://goo.gle/appsheet-appsscript) you can pass the return value of a [*Google Apps Script*](https://developers.google.com/apps-script) function to another step within your AppSheet automation. This article will explain how to configure and reference the return value.

Example uses:

- Write the return value of a webhook call back to one of your Google Sheets
- Update or add a new table row based on the output of an Apps Script function
- Write a conditional flow based on the result on an Apps script function

## Configure the Apps Script return value in AppSheet

To configure the Apps Script return value in AppSheet, you’ll need to specify what is the expected return value from your Apps Script function and the AppSheet type to convert it to.

In Apps Script:

1.  Add a `return `statement to the Apps Script function you want to call in AppSheet. This can return any Apps Script type with some caveats listed in [*Type limitations*](#type-limitations). For example this function returns a boolean value:

    Example Apps Script function with a return value.

 

In AppSheet:

1.  Configure an Apps Script task, as described in [*Call Apps Script from an automation*](https://goo.gle/appsheet-appsscript).
2.  Enable the **Return Value** toggle to configure the return value.

    Return Value section of the Apps Script task
3.  Click the return type of your Apps Script function.
4.  Select the AppSheet type it should convert to in the drop-down.

## Use the Apps Script return value in an automation

Synchronous tasks ([**Run asynchronously?**](https://support.google.com/appsheet/answer/11997142#run-asynchronously) is disabled) will wait for a return value up to the limit specified in [Apps Script execution limitation](https://developers.google.com/apps-script/guides/services/quotas#current_limitations).

To reference the return value in an expression in a **subsequent** step in the process, you can refer to the output using the following syntax:

- `[StepName].[Output]` for strings, booleans, numbers, arrays, and dates

- `[StepName].[Key]` for objects where `Key `is the key of your returned object

**Note**: `StepName` must be unique relative to all step and column names within the context of the current automation.

For example this process has the step name `CreateFile `and is used in a data action step to set the row values:

Use the Apps Script return value in an automation

That’s it! You can write the return value back to a Sheet, modify the existing row, or run a conditional automation using the return value.

## Use a nested field from the response

AppSheet supports nested objects to any arbitrary level in the response. You use nested fields by using the `.` (dot) separator.

For example, if the return value in the Apps Script function is defined as follows:

`function myFunction() {`
`  return {`
`    a: {`
`      b: "Simple Example Text",`
`    },`
`    c: "More text",`
`  };`
`}`

You could reference the nested field using the following syntax:

`[StepName].[a.b] // this returns "Simple Example Text"`

## Type mapping between Apps Script and AppSheet

The table below summarizes the map between the Apps Script type and the equivalent AppSheet type it can convert to.

|                      |                           |                                      |
|----------------------|---------------------------|--------------------------------------|
| **Apps Script Type** | **Example**               | **AppSheet Type(s)**                 |
| String               | `“string”`                | Text, Url, Address, etc.             |
| Boolean              | `true`, `false`           | Yes/No                               |
| Number               | `42`                      | Number, Decimal, Price etc.          |
| Object               | `{a: “string”, b: false}` | Table Ref with columns for each type |
| Array                | `[1, 2, 3]`               | List or EnumList                     |
| Date                 | `new Date()`              | Date, Time, or DateTime              |

## Type limitations

Due to differences in the Apps Script and AppSheet type systems, the  advanced type defined in the following table is not supported.

|                            |                 |                                                                 |
|----------------------------|-----------------|-----------------------------------------------------------------|
| **Type**                   | **Example**     | **Explanation**                                                 |
| Arrays with multiple types | `[1, “string”]` | AppSheet type system expects a list to consist of the same type |

## Automation limitation

Return value can't currently be passed to another task directly, only to steps that are within the context of a process (such as actions and conditionals).

## Tips for debugging return values

If a type conversion fails, execution will still succeed but an error message will be reported in the [*Automation Monitor*](https://support.google.com/appsheet/answer/11447502). For example, `Failed Apps Script type translation: Type 'Number' failed to translate to 'Yes/No'` means a number was returned from Apps Script but the task was configured to expect a `Yes/No` type.
