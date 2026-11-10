---
fonte: https://support.google.com/chat/answer/14179758?hl=en
baixado: 2026-11-10
---

# Use search operators in Google Chat

To filter your Google Chat search results, you can use words or symbols called search operators. To filter your results in detail, you can combine operators.

## Search operators you can use

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **What you can search for**                                                   | **Search operator & example**                                                 |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Search for messages from a specific sender.                                   | `from:`                                                                       |
|                                                                               |                                                                               |
|                                                                               | Examples:                                                                     |
|                                                                               |                                                                               |
|                                                                               | `from:me`                                                                     |
|                                                                               |                                                                               |
|                                                                               | `from:john@xyz.com`                                                           |
|                                                                               |                                                                               |
|                                                                               | **Tip:** When you use the `from:` operator, suggested contacts may            |
|                                                                               | autocomplete. To accept a suggestion, click the contact’s name.               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Search for messages that have a Google Docs, Sheets, or Slides attachment.    | `has:doc`                                                                     |
|                                                                               |                                                                               |
|                                                                               | `has:sheet`                                                                   |
|                                                                               |                                                                               |
|                                                                               | `has:slide`                                                                   |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Search for messages that have a file, link, video, or another attachment      | `has:file`                                                                    |
| type.                                                                         |                                                                               |
|                                                                               | `has:url`                                                                     |
|                                                                               |                                                                               |
|                                                                               | `has:video`                                                                   |
|                                                                               |                                                                               |
|                                                                               | `has:pdf`                                                                     |
|                                                                               |                                                                               |
|                                                                               | `has:image`                                                                   |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Search for messages that mention a specific person.                           | `at:`                                                                         |
|                                                                               |                                                                               |
|                                                                               | Examples:                                                                     |
|                                                                               |                                                                               |
|                                                                               | `at:me`                                                                       |
|                                                                               |                                                                               |
|                                                                               | `at:rashad`                                                                   |
|                                                                               |                                                                               |
|                                                                               | `at:fatima@xyz.com`                                                           |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Search for an exact word or phrase.                                           | `" "`                                                                         |
|                                                                               |                                                                               |
|                                                                               | Examples:                                                                     |
|                                                                               |                                                                               |
|                                                                               | `"happy birthday"`                                                            |
|                                                                               |                                                                               |
|                                                                               | `"anniversary"`                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Exclude specific messages from search results.                                | `-`                                                                           |
|                                                                               |                                                                               |
|                                                                               | Examples:                                                                     |
|                                                                               |                                                                               |
|                                                                               | `from:issac -from:jenny`                                                      |
|                                                                               |                                                                               |
|                                                                               | `-birthday from:jenny`                                                        |
|                                                                               |                                                                               |
|                                                                               | `-has:file from:issac`                                                        |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Search for messages sent within a certain time period.                        | `after:`                                                                      |
|                                                                               |                                                                               |
|                                                                               | `before:`                                                                     |
|                                                                               |                                                                               |
|                                                                               | Examples:                                                                     |
|                                                                               |                                                                               |
|                                                                               | `after:2023/04/16`                                                            |
|                                                                               |                                                                               |
|                                                                               | `before:04/18/2023`                                                           |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| With “d” (day), “m” (month), and “y” (year), you can search for messages      | `older_than:`                                                                 |
| older or newer than a particular time period.                                 |                                                                               |
|                                                                               | `newer_than:`                                                                 |
|                                                                               |                                                                               |
|                                                                               | Examples:                                                                     |
|                                                                               |                                                                               |
|                                                                               | `newer_than:2d`                                                               |
|                                                                               |                                                                               |
|                                                                               | `older_than:1y`                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Specify a timezone for messages sent within a time period.                    | `tz:GMT+hh:mm`                                                                |
|                                                                               |                                                                               |
|                                                                               | `tz:GMT-hh:mm`                                                                |
|                                                                               |                                                                               |
|                                                                               | Examples:                                                                     |
|                                                                               |                                                                               |
|                                                                               | `after:2023/01/02 before:2023/12/20 tz:GMT-05:30`                             |
|                                                                               |                                                                               |
|                                                                               | `newer_than:3d older_than:2d tz:GMT+05:00`                                    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Narrow results to a direct message or a space.                                | Narrow results to a direct message                                            |
|                                                                               |                                                                               |
|                                                                               | `is:dm`                                                                       |
|                                                                               |                                                                               |
|                                                                               | `is:chat`                                                                     |
|                                                                               |                                                                               |
|                                                                               | Narrow results to unread messages                                             |
|                                                                               |                                                                               |
|                                                                               | `is:unread`                                                                   |
|                                                                               |                                                                               |
|                                                                               | **Tips:**                                                                     |
|                                                                               |                                                                               |
|                                                                               | -   This search operator only shows unread main messages from conversations   |
|                                                                               |     or spaces.                                                                |
|                                                                               | -   For replies within an inline thread, is:unread only returns unread        |
|                                                                               |     replies from followed threads.                                            |
|                                                                               |                                                                               |
|                                                                               | Narrow results to a space                                                     |
|                                                                               |                                                                               |
|                                                                               | `is:room`                                                                     |
|                                                                               |                                                                               |
|                                                                               | Examples:                                                                     |
|                                                                               |                                                                               |
|                                                                               | `happy birthday is:dm`                                                        |
|                                                                               |                                                                               |
|                                                                               | `anniversary is:room`                                                         |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Search for messages in a specific space.                                      | `in:<space>`                                                                  |
|                                                                               |                                                                               |
|                                                                               | Examples:                                                                     |
|                                                                               |                                                                               |
|                                                                               | `apple in:recipes`                                                            |
|                                                                               |                                                                               |
|                                                                               | `apple in:(mobile phones)`                                                    |
|                                                                               |                                                                               |
|                                                                               | `apple in:”mobile phones”`                                                    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

## Related resources

- [Search for Google Chat messages](https://support.google.com/chat/answer/7655805)
- [Add formatting to your Google Chat messages](https://support.google.com/chat/answer/7649118)
