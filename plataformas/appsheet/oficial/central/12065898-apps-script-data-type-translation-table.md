---
fonte: https://support.google.com/appsheet/answer/12065898?hl=en
baixado: 2026-11-10
---

# Apps Script data type translation table

When configuring the new [AppSheet Apps Script Task](https://support.google.com/appsheet/answer/11997142), you can pass data from the AppSheet app to the function arguments using [Expressions](https://support.google.com/appsheet/answer/10104642).

The table below summarizes the type translation of an argument that gets passed through an AppSheet task.

+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **AppSheet Data Type**                             | **Apps Script Data Type when passed**              | **Example**                                        |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| [Yes /                                             | Boolean                                            | AppSheet expression: `"YES"`                       |
| No](ht                                             |                                                    |                                                    |
| tps://support.google.com/appsheet/answer/10107946) |                                                    | Apps Script value: `true`                          |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| [Duration](ht                                      | Number (in milliseconds)                           | AppSheet expression: `"000:00:01"`                 |
| tps://support.google.com/appsheet/answer/10107326) |                                                    |                                                    |
|                                                    |                                                    | Apps Script value: `1000`                          |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| [Date &                                            | String (in [ISO                                    | AppSheet expression: `DATETIME("12/20/2020 7PM)"`  |
| Datetime](ht                                       | 8601](https                                        |                                                    |
| tps://support.google.com/appsheet/answer/10107326) | ://www.iso.org/iso-8601-date-and-time-format.html) | Apps Script value: `"2022-12-25T19:00:00"`         |
|                                                    | date format)                                       |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| [List &                                            | Array\<Value\>                                     | AppSheet expression:                               |
| EnumList](ht                                       |                                                    | `REF_ROWS("My Table", "TaskID")`                   |
| tps://support.google.com/appsheet/answer/10107669) |                                                    |                                                    |
|                                                    |                                                    | Apps Script value:                                 |
|                                                    |                                                    | `["taskId1", "taskId2", "taskId3"]`                |
|                                                    |                                                    |                                                    |
|                                                    |                                                    |                                                    |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | AppSheet expression: `LIST("a", "b", "c")`         |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | Apps Script value: `["a", "b", "c"]`               |
|                                                    |                                                    |                                                    |
|                                                    |                                                    |                                                    |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | AppSheet expression: `{"a", {"b", "c"}}`           |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | Apps Script value: `["a", ["b", "c"]]`             |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| [Number](htt                                       | Number                                             | AppSheet expression: 3.14                          |
| ps://support.google.com/appsheet/answer/10108120), |                                                    |                                                    |
| [Decimal](htt                                      |                                                    | Apps Script value: 3.14                            |
| ps://support.google.com/appsheet/answer/10107887), |                                                    |                                                    |
| and [ChangeCounter](ht                             |                                                    |                                                    |
| tps://support.google.com/appsheet/answer/10106528) |                                                    |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| All other types                                    | String                                             | AppSheet expression: `"Hello"`                     |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | Apps Script value: `"Hello"`                       |
|                                                    |                                                    |                                                    |
|                                                    |                                                    |                                                    |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | AppSheet expression: `TIME("15:14")`               |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | Apps Script value: `"3:14pm"`                      |
|                                                    |                                                    |                                                    |
|                                                    |                                                    |                                                    |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | AppSheet expression:                               |
|                                                    |                                                    | `HYPERLINK("https://www.google.com", "Google")`    |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | Apps Script value: `"https://www.google.com"`      |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+

 

### Tips

- For date types, you can go `new Date(dateString)` to convert the date string into a native Javascript Type object
- Most types are represented in their respective string format which will vary on the type. For example, a file type will return the path of the file in the provider and an email type will simply be the email as a string.

## See also

- [Call Apps Script from an Automation](https://support.google.com/appsheet/answer/11997142)
