---
fonte: https://support.google.com/appsheet/answer/15983005?hl=en
baixado: 2026-11-10
---

# Use the Categorize AI task in an automation

This feature is available to **AppSheet Enterprise Plus **accounts only. See [What features are supported with each subscription?](https://support.google.com/appsheet/answer/10105400#features)

Categorize information based on a predefined set of categories using AI by adding the **Categorize AI** task in an automation.

**Examples of categorizing information using AI:**

- Analyze the description in employee expense submissions and automatically categorize them by type (Travel, Meals, Software, or Training).
- Read incoming facility maintenance requests and categorize them by urgency (High, Medium, or Low) or equipment type (HVAC, Plumbing, or Electrical).
- Classify customer survey responses or feedback form submissions into types like Bug Report, Feature Request, Positive Feedback, or Billing Inquiry.

Categorize information using AI as described in the following sections.

- [Get started](#get-started)
- [Add and configure the Categorize AI task](#configure)

See also:

- [Best practices for using AI in automations](https://support.google.com/appsheet/answer/16052759)
- [Limitations with AI in automations](https://support.google.com/appsheet/answer/15999115)

## Get started

To get started using the Categorize AI task, [step through a quick start](https://support.google.com/appsheet/answer/16045284#quick-start) or [explore an app template](https://support.google.com/appsheet/answer/16045284#app-template).

## Add and configure the Categorize AI task

To categorize information based on a set of predefined categories, add and configure the **Categorize AI** task by performing the following steps.

1.  Add the **Categorize AI **task to a bot, as described in [Add a task to a bot](https://support.google.com/appsheet/answer/11445301#add-task).
2.  Configure the **Categorize AI** task by using the settings described in the following table. 
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
|                                                                               | Select **Categorize**.                                                        |
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
|                                                                               | **Note**: `List` columns are not supported at this time.                      |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Output                                                                        | Select one of the following:                                                  |
|                                                                               |                                                                               |
|                                                                               | -   **Save to table** to save the extracted information to the table in your  |
|                                                                               |     data source.                                                              |
|                                                                               | -   **Return value** to guide AI responses without storing the results in     |
|                                                                               |     your data source. Use the returned values in later steps, as              |
|                                                                               |     follows: `[`*`AI-step`*`].[`*`column`*`]`                                 |
|                                                                               |                                                                               |
|                                                                               | For best practices when saving content, see [Manage updates to row data by    |
|                                                                               | multiple                                                                      |
|                                                                               | bots](https:                                                                  |
|                                                                               | //support.google.com/appsheet/answer/16136023#update-row-data-multiple-bots). |
|                                                                               |                                                                               |
|                                                                               | Then, select the column that defines the allowed category values. Must be an  |
|                                                                               | `Enum` or `Ref` column.                                                       |
|                                                                               |                                                                               |
|                                                                               | **Note**: If you select a `Ref` column, it only works with existing values    |
|                                                                               | and there must be at least one row. AppSheet won't create a new entry in the  |
|                                                                               | referenced table.                                                             |
|                                                                               |                                                                               |
|                                                                               | For example, you might have a column called `How expensive?` that is an       |
|                                                                               | `Enum` column with the following values: `Inexpensive`,                       |
|                                                                               | `Moderately expensive`, `Expensive,Other`                                     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Additional instructions                                                       | Recommended. Do the following:                                                |
|                                                                               |                                                                               |
|                                                                               | -   Describe in more detail the requirements for each category value.         |
|                                                                               | -   Indicate what values to set if results are not known.                     |
|                                                                               | -   Ensure that any recommended values match the type and format of the       |
|                                                                               |     column, for best results.                                                 |
|                                                                               |                                                                               |
|                                                                               | Supports up to 1000 characters.                                               |
|                                                                               |                                                                               |
|                                                                               | For example:                                                                  |
|                                                                               |                                                                               |
|                                                                               | `Inexpensive: Less than 10 dollars`\                                          |
|                                                                               | `Moderately expensive: Between 10 and 50 dollars`\                            |
|                                                                               | `Expensive: Over 50 dollars`\                                                 |
|                                                                               | `Other: Not sure of value`                                                    |
|                                                                               |                                                                               |
|                                                                               | **Note**: Specifying a value that is not defined in the `Enum` or `Ref`       |
|                                                                               | column selected for the Output setting may cause unexpected behavior unless   |
|                                                                               | you [allow other                                                              |
|                                                                               | values]                                                                       |
|                                                                               | (https://support.google.com/appsheet/answer/10106509#allow-other-values) when |
|                                                                               | configuring the `Enum` column properties.                                     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
