---
fonte: https://support.google.com/appsheet/answer/11431791?hl=en
baixado: 2026-11-10
---

# AppSheet automation: The Components

AppSheet automation is a robust extension of AppSheet’s no-code platform that enables you to automate common business processes and document-based workflows.

- [Key components in AppSheet automation](#key-components)
- [About component reusability with AppSheet automation](#bot-component-reusability)

## ****Key components in AppSheet automation

The key components in AppSheet automation are illustrated in the following figure.

AppSheet Automation bot

The following table summarizes the key components in AppSheet automation.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Component**                                                                 | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Bot](https://support.google.com/appsheet/answer/11432969)                    | Defines the automation you want AppSheet to run.                              |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Event](https://support.google.com/appsheet/answer/11445188)                  | Identifies the app change, AppSheet database change, schedule, Chat app       |
|                                                                               | interaction, Google Forms form response, or Gmail label change that triggers  |
|                                                                               | the bot.                                                                      |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Process](https://support.google.com/appsheet/answer/11445386)                | Describes the set of                                                          |
|                                                                               | [steps](https://support.google.com/appsheet/answer/11463007) performed when   |
|                                                                               | the bot is triggered.                                                         |
|                                                                               |                                                                               |
|                                                                               | A step can:                                                                   |
|                                                                               |                                                                               |
|                                                                               | -   Run a **task** or **data** **action**                                     |
|                                                                               | -   Branch on a condition                                                     |
|                                                                               | -   Wait for a condition or period of time                                    |
|                                                                               | -   Call a process                                                            |
|                                                                               | -   Return values                                                             |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Task](https://support.google.com/appsheet/answer/11445301)                   | Defines a task-based step in a process, for example, send an email, extract   |
|                                                                               | information using AI (preview), and more.                                     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Action](https://support.google.com/appsheet/answer/10107706)                 | Defines an action-based step in a process, such as add an entry to a table.   |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Document processing](https://support.google.com/appsheet/answer/11447601)    | Allows you to automatically extract useful content from document files that   |
|                                                                               | are stored as PDF, GIF, PNG, JPEG or TIFF files.                              |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

## ****About component reusability with AppSheet automation

AppSheet automation encourages *reusability*, allowing you to build components once and reuse them in various automations to save time and accelerate development. You can create events, processes, tasks, and actions that can be reused in other components. For example, you can reuse actions and tasks within new processes, reuse events and processes within new bots, and so on. For more information, see [Reuse automation components](https://support.google.com/appsheet/answer/12193489).
