---
fonte: https://support.google.com/appsheet/answer/11510515?hl=en
baixado: 2026-11-10
---

# Configure data processing

Control how AppSheet processes data by setting configuration options as described in the following sections:

- [Access configuration options](#access-options)
- [Configure the behavior of comparison operators](#configure-comparison-operators)

## ****Access the configuration options

To access the configuration option for data processing, select **Settings ** Settings icon **\> Data** in the app editor.

We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

## If you are using the legacy editor

To access the configuration options for data processing, select **Data \> Options** in the app editor

## ****Configure the behavior of comparison operators

Configure the **Blank value comparison mode** option in the **Expressions** category to control how AppSheet processes the comparison operators. Set this configuration option to one of the following modes:

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Mode**                                                                      | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Consistent                                                                    | Enables the following data processing enhancements:                           |
|                                                                               |                                                                               |
|                                                                               | -   **Consistent comparison of blank values**\                                |
|                                                                               |     Maintains consistent results for expressions comparing blank values that  |
|                                                                               |     are evaluated on the server and client (that is, app formulas in virtual  |
|                                                                               |     columns versus physical columns).                                         |
|                                                                               | -   **Performance**\                                                          |
|                                                                               |     Improves performance of comparison operators when they are evaluated on   |
|                                                                               |     the AppSheet server, such as in virtual columns. Since virtual columns    |
|                                                                               |     are recomputed on app sync, this mode might improve sync speed.           |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Legacy                                                                        | Maintains legacy behavior.                                                    |
|                                                                               |                                                                               |
|                                                                               | Since **Consistent** mode changes the behavior for how comparison operators   |
|                                                                               | handle blank values, it is not strictly backwards-compatible with existing    |
|                                                                               | expressions. The **Legacy** mode is provided to give app creators time to     |
|                                                                               | adapt to the new behavior. In the future, the AppSheet editor will explicitly |
|                                                                               | encourage the use of the **Consistent** mode. Eventually the **Legacy** mode  |
|                                                                               | will be removed.                                                              |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

When creating a new app, the mode defaults to Consistent. When copying an existing app, the mode set for the original app will be maintained. You can switch between Consistent and Legacy modes at any time.

If your app depends on the legacy behavior, switch back to **Legacy** mode. Then to achieve a stable version of the app using the new mode without impacting the behavior of the original app, make a copy of the original app as a test version, switch to **Consistent** mode, and make the necessary changes in the test app.

The following table compares the expression results on the server and client for the Legacy and Consistent modes when evaluating an expression with a blank value.

**Note**: The examples use column notation to represent a blank value (for example, `[Blank]`), but it can be any expression that evaluates to a blank value.

+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| **Expression example**                | **Server (Legacy)**                   | **Client (Legacy)**                   | **Server and Client (Consistent)**    |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| *`value`*` `*`operator`*` [Blank]`    | True                                  | True or False                         | True or False                         |
|                                       |                                       |                                       |                                       |
| For example:                          |                                       |                                       |                                       |
|                                       |                                       |                                       |                                       |
| `1 = [Blank]`                         |                                       |                                       |                                       |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| `[Blank] = [Blank]`                   | True                                  | True                                  | True                                  |
|                                       |                                       |                                       |                                       |
| `[Blank] <= [Blank]`                  |                                       |                                       |                                       |
|                                       |                                       |                                       |                                       |
| `[Blank] >= [Blank]`                  |                                       |                                       |                                       |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| `[Blank] = 0`                         | False                                 | True                                  | False                                 |
|                                       |                                       |                                       |                                       |
| `[BlankDuration] = “000:00:00”`       |                                       |                                       |                                       |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| `[Blan                                | False                                 | True                                  | False                                 |
| kDateTime] = “12/31/1969 6:00:00 PM”` |                                       |                                       |                                       |
|                                       |                                       |                                       |                                       |
| `[BlankDate] = “12/31/1969”`          |                                       |                                       |                                       |
|                                       |                                       |                                       |                                       |
| `[BlankTime] = “06:00:00 PM”`         |                                       |                                       |                                       |
|                                       |                                       |                                       |                                       |
| (The value on the right side is the   |                                       |                                       |                                       |
| user TZ offset from UTC UNIX epoch)   |                                       |                                       |                                       |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| `[Blank] <> 0`                        | True                                  | False                                 | True                                  |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| `[Blank] < 0`                         | False                                 | False                                 | False                                 |
|                                       |                                       |                                       |                                       |
| `[Blank] > 0`                         |                                       |                                       |                                       |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| `[Blank] <= 0`                        | False                                 | True                                  | False                                 |
|                                       |                                       |                                       |                                       |
| `[Blank] >= 0`                        |                                       |                                       |                                       |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| `[Blank] < 1`                         | False                                 | True                                  | True                                  |
|                                       |                                       |                                       |                                       |
| `[Blank] <= 1`                        |                                       |                                       |                                       |
|                                       |                                       |                                       |                                       |
| `[Blank] > -1`                        |                                       |                                       |                                       |
|                                       |                                       |                                       |                                       |
| `[Blank] >= -1`                       |                                       |                                       |                                       |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
