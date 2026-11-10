---
fonte: https://support.google.com/appsheet/answer/11828262?hl=en
baixado: 2026-11-10
---

# Automation limits

Review the automation limits:

- [Process automation](#process-automation)
- [Email recipients](#email-recipients)
- [Data extraction for invoices, receipts, and so on (Intelligent Document Processing)](#data-extraction)

See also [Limitations with AI in automations](https://support.google.com/appsheet/answer/15999115).

## Process automation

The following process automation limits are in effect for AppSheet.

Daily limits are refreshed at 12:00 AM PST. 

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Item**                                                                      | **Limit**                                                                     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Maximum data size of a table record (image columns excluded) processed by a   | 10 MB                                                                         |
| bot                                                                           |                                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Maximum number of automation bots executing concurrently                      | 5000                                                                          |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Maximum number of days a process can be in a wait state                       | 30 days                                                                       |
| ([Wait]                                                                       |                                                                               |
| (https://support.google.com/appsheet/answer/11463007#step-type&zippy=%2Cwait) |                                                                               |
| step in the current process or waiting for a child process to execute)        |                                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Maximum number of [Wait for a                                                 | -   100,000 per day                                                           |
| condition](https://                                                           | -   2000 per 20 minutes                                                       |
| support.google.com/appsheet/answer/11463007#wait-for-condition&zippy=%2Cwait) |                                                                               |
| steps that are executed across all apps owned by a user                       |                                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Maximum number of [Wait for a period of                                       | -   30,000 per day                                                            |
| time](https://suppo                                                           | -   150 per 3 minutes                                                         |
| rt.google.com/appsheet/answer/11463007#wait-for-period-of-time&zippy=%2Cwait) |                                                                               |
| steps that are executed across all apps owned by a user                       |                                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Maximum number of process executions triggered by an app change event         | -   500,000 per day/per app owner account                                     |
|                                                                               | -   50,000 per 5 minutes/per app owner account                                |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Maximum number of process executions triggered by a scheduled event           | -   500,000 per day/per app owner account                                     |
|                                                                               | -   50,000 per 5 minutes/per app owner account                                |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Maximum number of event triggers that are external to the app (such           | -   100,000 per day                                                           |
| as [AppSheet                                                                  | -   500 per minute                                                            |
| database](https://support.go                                                  | -   20 events per table                                                       |
| ogle.com/appsheet/answer/11445188#configure-appsheet-database-event), [Google |                                                                               |
| Cha                                                                           |                                                                               |
| t](https://support.google.com/appsheet/answer/11445188#configure-chat-event), |                                                                               |
| and [Google                                                                   |                                                                               |
| Form                                                                          |                                                                               |
| s](https://support.google.com/appsheet/answer/11445188#configure-forms-event) |                                                                               |
| events)                                                                       |                                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Maximum number of [notifications sent from                                    | -   60,000 per day/per app owner account                                      |
| automations](https://support.google.com/appsheet/answer/11513089)             | -   1500 per minute                                                           |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Maximum number of days bot run data is available                              | 55 days                                                                       |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Maximum number of rows processed in                                           | 10,000                                                                        |
| [ForEachRowInTable](http                                                      |                                                                               |
| s://support.google.com/appsheet/answer/11445188#configure-scheduled-event) in |                                                                               |
| a deployed app                                                                |                                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Maximum number of rows processed in "For Each Row in Table" in a prototype    | 1000                                                                          |
| app                                                                           |                                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Maximum number of Chat Space IDs that can be listed when configuring a [Chat  | 3000                                                                          |
| message automation](https://support.google.com/appsheet/answer/12981549)      |                                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Maximum                                                                       | 5 minutes                                                                     |
| [schedul                                                                      |                                                                               |
| e event](https://support.google.com/appsheet/answer/11445188#schedule-events) |                                                                               |
| execution time                                                                |                                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Maximum                                                                       | 2 minutes                                                                     |
| [app](                                                                        |                                                                               |
| https://support.google.com/appsheet/answer/11445188#data-change-events) event |                                                                               |
| execution time                                                                |                                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Maximum PDF files                                                             | 2500 per day/per app owner account,\                                          |
|                                                                               | rate of 20 per second                                                         |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

## Email recipients

The following table summarizes the limits for email recipients when using [email automations](https://support.google.com/appsheet/answer/11447614).

+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| **Limit item**                        | **Free**                              | **Starter, Core,\                     | **Enterprise Plus**                   |
|                                       |                                       | & Publisher Pro**                     |                                       |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Email recipients per hour             | 5                                     | 200 - 400                             | 25,000                                |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Email recipients per day              | 30                                    | 1000 - 20,000                         | 50,000                                |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+

## Data extraction for invoices, receipts, and so on (Intelligent Document Processing)

The following data extraction limits are in effect for AppSheet automation.

|                                                                            |                           |
|----------------------------------------------------------------------------|---------------------------|
| **Item**                                                                   | **Limit**                 |
| Size of the document that can be processed                                 | 20 MB                     |
| Number of pages in a document that can be processed (for example, invoice) | 5                         |
| Processed document file formats supported                                  | PDF, GIF, TIFF, JPEG, PNG |
