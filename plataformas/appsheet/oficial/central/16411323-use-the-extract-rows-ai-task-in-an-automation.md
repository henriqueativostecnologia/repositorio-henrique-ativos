---
fonte: https://support.google.com/appsheet/answer/16411323?hl=en
baixado: 2026-11-10
---

# Use the Extract rows AI task in an automation

This feature is available to **AppSheet Enterprise Plus** accounts only.

Extract information from an uploaded image (such as a photo) or a file (PDF), and save it to rows in an existing table using AI by adding the **Extract rows **AI task in an automation.

Examples of extracting information using AI:

- Have technicians snap a photo of equipment and use AI to automatically extract the serial number, model number, or meter reading into your AppSheet table.
- Process uploaded purchase orders (as PDFs) or photos of shipping labels to extract PO numbers, company names, tracking numbers, or addresses.
- From incident reports, extract key details like location, date, or names.

Extract information and save to rows in an existing table using AI as described in the following sections:

- [Add and configure the Extract rows AI task](#extract)

See also:

- [Best practices for using AI in automations](https://support.google.com/appsheet/answer/16052759)
- [Limitations with AI in automations](https://support.google.com/appsheet/answer/15999115)

## Add and configure the Extract rows  AI task

To extract data from an uploaded image (such as a photo) or file (PDF), add and configure the **Extract rows **AI task by performing the following steps.

1.  Add the **Extract rows **AI task to a bot, as described in [Add a task to a bot](https://support.google.com/appsheet/answer/11445301#add-task).
2.  Configure the **Extract rows **AI task by using the settings described in the following table.  (Note: There is a **maximum 50 row import limit** per referenced table.)
3.  Save the app.

To extract data from an uploaded image (such as a photo) or a file (such as a PDF) and save it to rows in an existing table, configure the settings described in the following table.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Task type                                                                     | Select **AI task**.                                                           |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Table                                                                         | Table defined in the                                                          |
|                                                                               | [event](https://support.google.com/appsheet/answer/11445188) and used by the  |
|                                                                               | task.                                                                         |
|                                                                               |                                                                               |
|                                                                               | To view or edit the structure of the selected table, position your cursor in  |
|                                                                               | the field and click Edit icon . See [Tables: The                              |
|                                                                               | Essentials](https://support.google.com/appsheet/answer/10105821) for more     |
|                                                                               | information.                                                                  |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| AI task                                                                       | [Type of AI task](#types). Select **Extract rows**.                           |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Input column                                                                  | Column in the table that is used as input to the AI task.                     |
|                                                                               |                                                                               |
|                                                                               | For the Extract task, this must be one of the following types: `Drawing`,     |
|                                                                               | `File`, `Image`, or  `Thumbnail`                                              |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Add rows to                                                                   | Table to which you want to add the extracted rows. Select a [referenced       |
|                                                                               | table](https://support.google.com/appsheet/answer/10106510) from the          |
|                                                                               | drop-down. (**50 row import limit**)                                          |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Output                                                                        | Select one or more columns to define the information to extract, up to a      |
|                                                                               | **maximum of 12**. Select a column from the drop-down. Click **Add** to add   |
|                                                                               | more columns.                                                                 |
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
|                                                                               | **From the PDF file extract the items in the receipt that are above fifty     |
|                                                                               | dollars**                                                                     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
