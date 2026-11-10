---
fonte: https://support.google.com/appsheet/answer/12653576?hl=en
baixado: 2026-11-10
---

# Restrictions, limits, and known issues

The following sections capture the [restrictions](#restrictions), [limits](#limits), and [known issues](#known-issues) for AppSheet databases.

## Restrictions

The following restrictions apply to AppSheet databases:

- AppSheet databases are available by default, but can be [disabled](https://support.google.com/appsheet/answer/12629371) for your team by your administrator
- If your Workspace account is available for K12 audience, then AppSheet and AppSheet databases are automatically disabled as a security precaution

## Limits

The following limits are in effect based on your subscription plan. For example, if you have 5 AppSheet Core licenses, each of those 5 users are entitled to create 10 AppSheet databases with a maximum of 2500 rows per database.

When the limits summarized below are reached, existing data will be retained and you will continue to have read and edit access. However, you won't be able to add new data.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Subscription plan**                                                         | **Limits**                                                                    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Free                                                                          | -   1000 rows per AppSheet database                                           |
|                                                                               | -   5 AppSheet databases                                                      |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Starter                                                                       | -   2500 rows per AppSheet database                                           |
|                                                                               | -   5 AppSheet databases                                                      |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Core and\                                                                     | -   2500 rows per AppSheet database                                           |
| Publisher Pro                                                                 | -   10 AppSheet databases                                                     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Enterprise Plus                                                               | -   200,000 rows per AppSheet database                                        |
|                                                                               | -   Based on your data requirements, you can work with your AppSheet Sales    |
|                                                                               |     representative to increase the number of rows allowed per AppSheet        |
|                                                                               |     database                                                                  |
|                                                                               | -   Unlimited AppSheet databases (200 databases per user)                     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

In addition, the following technical limits apply across all plans:

- 20 tables per database

- 100 columns per table

- 2000 characters per cell

- 5000 characters per [`LongText`](https://support.google.com/appsheet/answer/10106435#text) column

See also: 

- [Automation limits](https://support.google.com/appsheet/answer/11828262)
- [Performance considerations for common data sources](https://support.google.com/appsheet/answer/10105761#data-sources)
- [AppSheet pricing](https://about.appsheet.com/pricing/)

## Known issues

The following list the known issues when using AppSheet databases:

- Copying and pasting text over a linked [Lookup](https://support.google.com/appsheet/answer/12798217#add-lookup) column is not supported yet
- Grouping and filtering is not supported for every column type yet
- Grouping on linked rows will pick the first linked [Lookup](https://support.google.com/appsheet/answer/12798217#add-lookup) column for the group headers
- [Chromebooks](https://support.google.com/chromebook/thread/1654780?hl=en) and [Apple Macs](https://www.nytimes.com/2017/02/02/technology/personaltech/solving-the-case-of-the-disappearing-scroll-bars.html) have system settings that can hide scrollbars so that scrollbars are missing
