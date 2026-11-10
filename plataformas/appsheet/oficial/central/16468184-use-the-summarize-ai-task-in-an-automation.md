---
fonte: https://support.google.com/appsheet/answer/16468184?hl=en
baixado: 2026-11-10
---

# Use the Summarize AI task in an automation

This feature is available to **AppSheet Enterprise Plus** accounts only.

Summarize long textual data into a shorter summary using AI by adding the **Summarize **AI task in an automation. You can use multiple columns as input to the Summarize AI task.

Examples of summarizing information using AI:

- Summarize notes from a meeting to review the main highlights
- Summarize information for a specific customer, highlighting the main points of concern

Use the Summarize AI task in an automation as described in the following section.

- [Add and configure the Summarize AI task](#summarize)

See also:

- [Best practices for using AI in automations](https://support.google.com/appsheet/answer/16052759)
- [Limitations with AI in automations](https://support.google.com/appsheet/answer/15999115)

## Add and configure the Summarize AI task

To summarize information using AI, add and configure the **Summarize **AI task by performing the following steps.

1.  Add the **Summarize **AI task to a bot, as described in [Add a task to a bot](https://support.google.com/appsheet/answer/11445301#add-task).
2.  Configure the **Summarize **AI task by using the settings described in the following table. 
3.  Save the app.

To summarize information using AI, configure the settings described in the following table.

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
| AI task                                                                       | [Type of AI task](#types). Select **Summarize**.                              |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Input columns                                                                 | Add one or more columns to use as input to the AI task, up to a **maximum of  |
|                                                                               | 10**. Click **Add** and select a column from the drop-down.                   |
|                                                                               |                                                                               |
|                                                                               | Basic column data types and virtual columns are supported.                    |
|                                                                               |                                                                               |
|                                                                               | **The following data types** **are not supported**:                           |
|                                                                               |                                                                               |
|                                                                               | -   [Content                                                                  |
|                                                                               |     types](https://support.google.com/appsheet/answer/10106435#content):      |
|                                                                               |     `Drawing`, `File`, `Image`, `Signature`, `Thumbnail`, and `Video`         |
|                                                                               | -                                                                             |
|                                                                               |  [`Color`](https://support.google.com/appsheet/answer/10106435#enumerated)` ` |
|                                                                               | -   [Show types](https://support.google.com/appsheet/answer/10106435#show)    |
|                                                                               | -   [Other types](https://support.google.com/appsheet/answer/10106435#other): |
|                                                                               |     `URL`, `App`                                                              |
|                                                                               |                                                                               |
|                                                                               | **Note**:                                                                     |
|                                                                               |                                                                               |
|                                                                               | -   For `Ref` type columns, only the label is evaluated.                      |
|                                                                               | -   `List` columns are not supported at this time.                            |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Output                                                                        | Select one of the following:                                                  |
|                                                                               |                                                                               |
|                                                                               | -   **Save to table** to save the extracted information to the table in your  |
|                                                                               |     data source.                                                              |
|                                                                               | -   **Return value** to guide AI responses without storing the results in     |
|                                                                               |     your data source. Use the returned values in later steps, as              |
|                                                                               |     follows: `[`*`AI-step`*`].[`*`column`*`]`                                 |
|                                                                               |                                                                               |
|                                                                               | Then, select the column to capture the summary information from the           |
|                                                                               | drop-down. The column must be one of the following types: `LongText` or       |
|                                                                               | `Text`                                                                        |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Additional instructions                                                       | Recommended. Describe in more detail the information you want to include in   |
|                                                                               | the summary. Supports up to 1000 characters.                                  |
|                                                                               |                                                                               |
|                                                                               | For example:                                                                  |
|                                                                               |                                                                               |
|                                                                               | **Summarize the customer feedback, highlighting the main areas for            |
|                                                                               | improvement**                                                                 |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
