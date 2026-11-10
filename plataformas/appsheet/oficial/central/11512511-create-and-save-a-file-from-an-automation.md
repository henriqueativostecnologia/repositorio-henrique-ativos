---
fonte: https://support.google.com/appsheet/answer/11512511?hl=en
baixado: 2026-11-10
---

# Create and save a file from an automation

This feature is available to **AppSheet Core** accounts and above. See [AppSheet pricing](https://about.appsheet.com/pricing/).

Create and save a file by adding the **Create a new file** task to an automation bot.

Add and configure the **Create a new file** task by performing the following steps:

1.  Add the **Create a new file **task to a bot, as described in [Add a task to a bot](https://support.google.com/appsheet/answer/11445301#add-task).
2.  Configure the **Create a new file** task by setting the properties described in the following tables.
3.  Save the app.

After you save the app, you can reuse the task in other bots.

Configure the **Create a new file t**ask by using the settings described in the following tables.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Linking                                                                       | Enable or disable reuse of this component by expanding the **Linking** panel  |
|                                                                               | and toggling the **Linking** setting. See [Reuse automation                   |
|                                                                               | components](https://support.google.com/appsheet/answer/12193489).             |
|                                                                               |                                                                               |
|                                                                               | Expand the Linking panel and toggle the Linking setting to enable or disable  |
|                                                                               | component reuse                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Task name                                                                     | Name of the task. It must be unique within your app.                          |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Table name                                                                    | Table defined in the                                                          |
|                                                                               | [event](https://support.google.com/appsheet/answer/11445188) and used by the  |
|                                                                               | task.                                                                         |
|                                                                               |                                                                               |
|                                                                               | To view or edit the structure of the selected table, position your cursor in  |
|                                                                               | the field and click Edit icon  . See [Tables: The                             |
|                                                                               | Essentials](https://support.google.com/appsheet/answer/10105821) for more     |
|                                                                               | information.                                                                  |
|                                                                               |                                                                               |
|                                                                               | **Note**: To use a table that is different from the table defined in the      |
|                                                                               | event, add a [Call a                                                          |
|                                                                               | process](https://s                                                            |
|                                                                               | upport.google.com/appsheet/answer/11463007#step-type&zippy=%2Ccall-a-process) |
|                                                                               | step.                                                                         |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| HTTP Content Type                                                             | Content type of the file. Valid content type values include:                  |
|                                                                               |                                                                               |
|                                                                               | -   CSV                                                                       |
|                                                                               | -   HTML                                                                      |
|                                                                               | -   ICS_Calendar                                                              |
|                                                                               | -   JSON                                                                      |
|                                                                               | -   PDF                                                                       |
|                                                                               | -   XLSX (Microsoft Excel)                                                    |
|                                                                               | -   XML                                                                       |
|                                                                               |                                                                               |
|                                                                               | **Note**: A maximum of 2500 PDF files are allowed to be created per day per   |
|                                                                               | app owner account, at a rate of 20 per second. See [Automation                |
|                                                                               | limits](https://support.google.com/appsheet/answer/11828262).                 |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Template                                                                      | Template to use for more precise control of the file contents. See [Use       |
|                                                                               | templates in a bot](https://support.google.com/appsheet/answer/11539957).     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| File Store                                                                    | File system where files are saved.                                            |
|                                                                               |                                                                               |
|                                                                               | When set to **Default** (the default setting), the file is stored on the      |
|                                                                               | [authentication                                                               |
|                                                                               | provider](https://support.google.com/appsheet/answer/10104975) file system.   |
|                                                                               | For example, if your authentication provider is Google, the file is saved to  |
|                                                                               | Google Drive. If your authentication provider is Dropbox, the attachment file |
|                                                                               | is saved to Dropbox.                                                          |
|                                                                               |                                                                               |
|                                                                               | **Note**: If Smartsheet is your authentication provider, AppSheet saves the   |
|                                                                               | file to Google Drive as Smartsheet does not have a file system. If you use    |
|                                                                               | Smartsheet and wish to save files, you must include Google as a data source,  |
|                                                                               | as described in [Use multiple data                                            |
|                                                                               | sources](https://support.google.com/appsheet/answer/10106309).                |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| File Folder Path                                                              | Folder path where files are saved relative to the default app folder.         |
|                                                                               |                                                                               |
|                                                                               | Use the Expression Assistant to specify text,                                 |
|                                                                               | [variables](https://support.google.com/appsheet/answer/11539253), and         |
|                                                                               | [expressions](https://support.google.com/appsheet/answer/10104642). For       |
|                                                                               | example:                                                                      |
|                                                                               |                                                                               |
|                                                                               | -   `Files/MyPurchaseOrders`                                                  |
|                                                                               |                                                                               |
|                                                                               | -   `<<CONC                                                                   |
|                                                                               | ATENATE("MyFiles/PurchaseOrdersByMonth_", YEAR(NOW()), "_", MONTH(NOW()))>>:` |
|                                                                               |                                                                               |
|                                                                               | In the second example, email attachment files would be stored in a separate   |
|                                                                               | folder, based on the month. For example:                                      |
|                                                                               | `MyFiles/PurchaseOrdersByMonth_2019_02`                                       |
|                                                                               |                                                                               |
|                                                                               | By default, the folder path is `Files`.                                       |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| File Name Prefix                                                              | Prefix to prepend to the filename.                                            |
|                                                                               |                                                                               |
|                                                                               | Use the Expression Assistant to specify text,                                 |
|                                                                               | [variables](https://support.google.com/appsheet/answer/11539253), and         |
|                                                                               | [expressions](https://support.google.com/appsheet/answer/10104642).           |
|                                                                               |                                                                               |
|                                                                               | By default, the prefix is `AppSheetDoc`.                                      |
|                                                                               |                                                                               |
|                                                                               | **Note**: Forward slashes (/) are not supported in filenames. For example, if |
|                                                                               | you are using a date format that uses forward slashes, you will need to       |
|                                                                               | convert them to a different character such as a period (.).                   |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Attachment Page Orientation                                                   | Page orientation used for PDF files. Valid values include: **Portrait** (the  |
|                                                                               | default) and **Landscape**                                                    |
|                                                                               |                                                                               |
|                                                                               | **Note**: This setting is available only if you set **HTTP Content Type** to  |
|                                                                               | **PDF**.                                                                      |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Attachment Page Size                                                          | Page size for PDF files. Select a standard size or select **Custom** and      |
|                                                                               | enter the **Attachment Page Width** and **Attachment Page Height** in         |
|                                                                               | millimeters. Defaults to `A4`.                                                |
|                                                                               |                                                                               |
|                                                                               | **Note**: This setting is available only if you set **HTTP Content Type** to  |
|                                                                               | **PDF**.                                                                      |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Disable Timestamp?                                                            | Toggle to indicate whether to append a timestamp to filenames. Appending the  |
|                                                                               | timestamp will ensure the filenames are unique.                               |
|                                                                               |                                                                               |
|                                                                               | The timestamp contains the date and time at which the attachment file was     |
|                                                                               | created, formatted as follows: *yyyyMMdd_HHmmss_fff* indicating year, month,  |
|                                                                               | day, hours, minutes, seconds, and milliseconds. For example:                  |
|                                                                               |                                                                               |
|                                                                               | `MyFileName20190207_133355_804.pd`f                                           |
|                                                                               |                                                                               |
|                                                                               | If you disable the timestamp, you must ensure that every filename is unique.  |
|                                                                               | Otherwise, the files may be overwritten. For example, if you are saving files |
|                                                                               | to Google Drive and you disable the timestamp, only the most recent           |
|                                                                               | attachment file will be available. Older files with the same name will have   |
|                                                                               | been overwritten.                                                             |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

 Expand and customize the **Advanced** settings, as described below.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Inputs                                                                        | Add inputs to dynamically configure a task. For details, see [Set input       |
|                                                                               | values dynamically in                                                         |
|                                                                               | tasks](https:                                                                 |
|                                                                               | //support.google.com/appsheet/answer/11445301#set-input-values-dynamically).  |
|                                                                               |                                                                               |
|                                                                               | 1.  Expand the **Advanced** section.                                          |
|                                                                               | 2.  Click **Add** under Inputs.                                               |
|                                                                               | 3.  Enter the name of the input value in the **Name** field.                  |
|                                                                               | 4.  Select the data type from the **Type** drop-down.\                        |
|                                                                               |     Only a subset of data types are supported for inputs.                     |
|                                                                               | 5.  To add an initial value or edit any fields:                               |
|                                                                               |     1.  Click  to open the Input dialog.                                      |
|                                                                               |     2.  Add a value or expression in the **Initial value** field.\            |
|                                                                               |         If you don't specify an initial value, then the input value will be   |
|                                                                               |         required. If an initial value is specified, then the input value is   |
|                                                                               |         optional.                                                             |
|                                                                               |         Use of `[_THIS]` or `[_INPUT]` are not supported in the Initial value |
|                                                                               |         field.                                                                |
|                                                                               |     3.  Edit other fields, as required.                                       |
|                                                                               |     4.  Click **Done**.                                                       |
|                                                                               | 6.  Repeat to add additional input values.                                    |
|                                                                               |                                                                               |
|                                                                               | Then, use the following expressions to access the input values from the       |
|                                                                               | current step: `[_INPUT].[`*`inputname`*`]`                                    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
