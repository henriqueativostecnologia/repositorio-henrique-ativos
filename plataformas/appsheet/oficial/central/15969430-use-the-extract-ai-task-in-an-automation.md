---
fonte: https://support.google.com/appsheet/answer/15969430?hl=en
baixado: 2026-11-10
---

# Use the Extract AI task in an automation

This feature is available to **AppSheet Enterprise Plus **accounts only. See [What features are supported with each subscription?](https://support.google.com/appsheet/answer/10105400#features)

Extract information from an uploaded image (such as a photo), a file (PDF), or text (such as a description, as `Text` or `LongText`) using AI by adding the **Extract AI** task in an automation.

Examples of extracting information using AI:

- Have technicians snap a photo of equipment and use AI to automatically extract the serial number, model number, or meter reading into your AppSheet table.
- Process uploaded purchase orders (as PDFs) or photos of shipping labels to extract PO numbers, company names, tracking numbers, or addresses.
- From incident reports, extract key details like location, date, or names.

Extract information using AI as described in the following sections:

- [Get started](#get-started)
- [Add and configure the Extract AI task](#extract)

See also:

- [Best practices for using AI in automations](https://support.google.com/appsheet/answer/16052759)
- [Limitations with AI in automations](https://support.google.com/appsheet/answer/15999115)

## Get started

To get started using the Extract AI task:

- [Watch a quick tour video](https://support.google.com/appsheet/answer/16045284#video)
- [Step through a quick start](https://support.google.com/appsheet/answer/16045284#quick-start)
- [Explore an app template](https://support.google.com/appsheet/answer/16045284#app-template).

## Add and configure the Extract AI task

To extract data from an uploaded image (such as a photo), file (PDF), or text (description), add and configure the **Extract AI** task by performing the following steps.

1.  Add the **Extract AI **task to a bot, as described in [Add a task to a bot](https://support.google.com/appsheet/answer/11445301#add-task).
2.  Configure the **Extract AI** task by using the settings described in the following table. 
3.  Save the app.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Task type                                                                     | Select **AI task**.                                                           |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Table                                                                         | Table defined in the                                                          |
|                                                                               | [event](https://support.google.com/appsheet/answer/11445188) and used by the  |
|                                                                               | task. See [Tables: The                                                        |
|                                                                               | Essentials](https://support.google.com/appsheet/answer/10105821) for more     |
|                                                                               | information about tables.                                                     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| AI task                                                                       | Type of [AI                                                                   |
|                                                                               | t                                                                             |
|                                                                               | ask](https://support.google.com/appsheet/answer/16045284#supported-ai-tasks). |
|                                                                               | Select **Extract**.                                                           |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Input column                                                                  | Column in the table that is used as input to the AI task.                     |
|                                                                               |                                                                               |
|                                                                               | For the Extract task, this must be one of the following types: `Drawing`,     |
|                                                                               | `File`, `Image`, `LongText`, `Text`, or  `Thumbnail`                          |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Output                                                                        | Select one of the following:                                                  |
|                                                                               |                                                                               |
|                                                                               | -   **Save to table** to save the extracted information to the table in your  |
|                                                                               |     data source.                                                              |
|                                                                               | -   **Return value** to guide AI responses without storing the results in     |
|                                                                               |     your data source. Use the returned values in later steps, as              |
|                                                                               |     follows: `[`*`AI-step`*`].[`*`column`*`]`                                 |
|                                                                               |                                                                               |
|                                                                               | Then, select one or more columns to define the information to extract, up to  |
|                                                                               | a **maximum of 12**. Select a column from the drop-down. Click **Add** to add |
|                                                                               | more columns.                                                                 |
|                                                                               |                                                                               |
|                                                                               | **Notes**:                                                                    |
|                                                                               |                                                                               |
|                                                                               | -   [Boolean](https://support.google.com/appsheet/answer/10106435#enumerated) |
|                                                                               |     (Yes/No),                                                                 |
|                                                                               |     [numeric](https://support.google.com/appsheet/answer/10106435#numeric),   |
|                                                                               |     [date,                                                                    |
|                                                                               |     time](https://support.google.com/appsheet/answer/10106435#temporal), and  |
|                                                                               |     [text](https://support.google.com/appsheet/answer/10106435#text) types    |
|                                                                               |     are supported. This includes                                              |
|                                                                               |     [Enum](https://support.google.com/appsheet/answer/10106435#enumerated)    |
|                                                                               |     type with one of these subtypes.                                          |
|                                                                               | -   [Barcode and QR code                                                      |
|                                                                               |     scanning](https://support.google.com/appsheet/answer/10106618) isn't      |
|                                                                               |     supported at this time.                                                   |
|                                                                               |                                                                               |
|                                                                               | For best practices when saving content, see [Manage updates to row data by    |
|                                                                               | multiple                                                                      |
|                                                                               | bots](https:                                                                  |
|                                                                               | //support.google.com/appsheet/answer/16136023#update-row-data-multiple-bots). |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Additional instructions                                                       | Recommended. Do the following:                                                |
|                                                                               |                                                                               |
|                                                                               | -   Describe in more detail the information you want to extract.              |
|                                                                               | -   Indicate what values to set if results are unknown.                       |
|                                                                               | -   Ensure that any recommended values match the type and format of the       |
|                                                                               |     column, for best results.                                                 |
|                                                                               |                                                                               |
|                                                                               | Supports up to 2000 characters.                                               |
|                                                                               |                                                                               |
|                                                                               | For example:                                                                  |
|                                                                               |                                                                               |
|                                                                               | **If not sure of Make, Model, or Year, make best guess\                       |
|                                                                               | If not sure of Color, set to "Other"**\                                       |
|                                                                               | **For** **Description, add 2 to 3 sentences**                                 |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
