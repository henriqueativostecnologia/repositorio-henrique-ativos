---
fonte: https://support.google.com/appsheet/answer/12738438?hl=en
baixado: 2026-11-10
---

# Use return values from webhooks

Use return values from webhooks as described in the following sections:

- [Configure the return value for a webhook](#configure)
- [Use the return value in an automation](#use)
- [Use nested fields from the response](#nested-fields)
- [Use a value in an array from the response](#array)
- [Tips for debugging return values](#tips)
- [Limitations with returned values](#limitations)

## Configure the return value for a webhook

When [configuring the task](https://support.google.com/appsheet/answer/11511244#configure), optionally use the following settings to capture the return values from a webhook:

- Enable the **Return value** toggle
- Use the **Specific types** field to map the return values in the JSON response to AppSheet [data types](https://support.google.com/appsheet/answer/10106435)

## Use the return value from a webhook in an automation

**Note**: Return values **cannot** be used to define:

- The Function Arguments field for an [Apps Script task](https://support.google.com/appsheet/answer/11997142)
- File Folder Path or File Name Prefix fields for a [create file task](https://support.google.com/appsheet/answer/11512511)

To use a return value from a webhook in an expression that is defined **after** this task in the automation, refer to the output using the following syntax:

- `[StepName].[FieldName]`

Return value field names are case-sensitive and can consist of letters, digits, and underscores only.

For example, if the Call a webhook task named **Call Address Service** captures the following return values:

To reference the return values, use the following format: `[Call Address Service].[`*`FieldName`*`]`

For example:

`CONCATENATE([Call Address Service].[ZipCode],[Call Address Service].[StreetName],"")`

## Use a nested field from the response

Nested arrays of complex types are not supported. See [Limitations with return values](#limitations).

AppSheet supports nested objects to any arbitrary level in the response. You use nested fields by using the `.` (dot) separator.

For example, if the response data for an employee contains the department information in the response as follows:

`"name": "John Doe",`
`"department": {`
`   "name": "Finance"`
`}`

You could reference the name of the department using the following syntax:

`[StepName].[department.name] // this returns "Finance"`

## Use a value in an array from the response

Use a value in an array from the response using the [`INDEX()`](https://support.google.com/appsheet/answer/10107336) function.

For example, if the response data for an employee contains the organization information as an array in the response, as follows:

`{`
`  "ID": 123,`
`  "company": "mycompany",`
`  "function": {`
`    "role": "project-manager",`
`    "organizations": ["Finance", "Engineering", "Cloud"]`
`  }`
`}`

You could reference the Engineering organization using the following syntax:

`INDEX([StepName].[function.organizations],2) // this returns "Engineering"`

## Tips for debugging return values

The following sections provides tips for debugging return values:

- [Error messages](#error-messages)
- [Timeout values](#timeout-values)

### Error messages

If a type conversion fails, bot execution will still succeed but an error message will be reported in the [*Automation Monitor*](https://support.google.com/appsheet/answer/11447502).

The following table lists the error messages returned based on the JSON mapping issue.

|                          |                                                                                                                                              |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| **JSON mapping issue**   | **Error message**                                                                                                                            |
| Different types in array | `Failed Webhook type translation: List type for key '{0}' must only have a single child type`                                                |
| Key not found            | `Failed Webhook type translation: Key '`*`key`*`' not found in returned object`                                                              |
| Incorrect type mapping   | `Failed Webhook type translation: Failed to translate ‘`*`type`*`’ to '`*`userDefinedType`*`' type`                                          |
| Nested object            | `Failed Webhook type translation: Failed to translate ‘`*`type`*`’ to ``'`*`userDefinedType`*`'`` type as the value is of object data type ` |
| Non-primitive array      | `Failed Webhook type translation: List type for key '{0}' cannot contain nested or repeated types`                                           |
| Null response            | `Failed Webhook type translation: Return value is NULL`                                                                                      |

## Timeout values

Timeouts are handled as follows:

- When comparing the following values, the minimum timeout value will be used:
  - Bot execution timeout
  - Webhook task timeout
- For automations with scheduled events, the maximum timeout is 5 minutes; for automations with data change events, the maximum timeout is 2 minutes.

## Limitations with returned values

Return values from webhooks **are only supported** for:

- HTTP `GET`, `PATCH`, `POST`, `PUT`, and `DELETE` methods

- JSON file formats

- Nested objects in the JSON responses, such as:

  `{`
  `  "ID": 123,`
  `  "company": "mycompany",`
  `  "employee": {`
  `    "lastname": "Doe",`
  `    "firstname": "Jane"`
  `  }`
  `}`

- Flat arrays of same types, such as:

  `{`
  `  "ID": 123,`
  `  "company": "mycompany",`
  `  "function": {`
  `    "role": "project-manager",`
  `    "organizations": ["Finance", "Engineering", "Cloud"]`
  `  }`
  `}`

At this time, return values from webhooks are **not supported** for:

- [Reusable automation components](https://support.google.com/appsheet/answer/12193489)
- Asynchronous HTTP calls (enable **Run Asynchronously**)
- Other file formats, such as XML
- Nested arrays of complex types, such as:

  `{"company": "mycompany",`` `
  `    "Employees":`
  `       [{`` `
  `          "lastname": "Doe",`
  ` ``          "firstname": "Jane"`
  ` ``       },{`
  ` ``          "lastname": "Doe",`
  ` ``          "firstname": "John"`
  ` ``       }]`
  `}`
