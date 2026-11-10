---
fonte: https://support.google.com/appsheet/answer/14771089?hl=en
baixado: 2026-11-10
---

# Build automations using AppSheet databases

Build an automation using AppSheet databases to trigger events when there are changes made to one or more columns, as described in the following sections:

- [Get started](#get-started)
- [Steps to build automations using AppSheet databases](#steps)
- [Copy apps with AppSheet database events](#copy-app)

See also [Automation limits](https://support.google.com/appsheet/answer/11828262).

## Get started

To get started building automations using AppSheet databases, see [Quick start: Build your first automation using an AppSheet database](https://support.google.com/appsheet/answer/14871588).

## Steps to build automations using AppSheet databases

Build automations using Google Forms to trigger events when there are changes made to one or more columns by performing the following steps.

+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **\#**                                             | **Step**                                           | **Description**                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| 1                                                  | Create an AppSheet database                        | Before you can build an automation, you must       |
|                                                    |                                                    | create an AppSheet database. See [Create and copy  |
|                                                    |                                                    | databases](htt                                     |
|                                                    |                                                    | ps://support.google.com/appsheet/answer/12635312). |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| 2                                                  | Add the AppSheet database to your app              | Do one of the following:                           |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | -   [Create an app from the AppSheet               |
|                                                    |                                                    |     database](https://support.google.com/          |
|                                                    |                                                    | appsheet/answer/12631543#create-app-from-database) |
|                                                    |                                                    | -   [Add the AppSheet database to an existing      |
|                                                    |                                                    |     app](https://support.google                    |
|                                                    |                                                    | .com/appsheet/answer/12631543#add-database-to-app) |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | In each case, select **AppSheet databases** as the |
|                                                    |                                                    | data source, then navigate to the database and     |
|                                                    |                                                    | click **Select**.                                  |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| 3                                                  | Use adds, updates, or deletes in the AppSheet      | Build an automation and [configure an AppSheet     |
|                                                    | database to trigger an event                       | database                                           |
|                                                    |                                                    | event](https://support.google.com/appsheet/an      |
|                                                    |                                                    | swer/11445188#configure-appsheet-database-event).  |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | App concepts or table settings defined in the app  |
|                                                    |                                                    | editor (such as making a column non-editable or    |
|                                                    |                                                    | required) won't affect how the bot gets triggered  |
|                                                    |                                                    | for event sources that are external to the app.    |
|                                                    |                                                    | For example, even if a column is marked as         |
|                                                    |                                                    | non-editable for apps, it can still be selected in |
|                                                    |                                                    | the Column to watch for setting in the event.      |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+

## Copy apps with AppSheet database events

To copy an app with AppSheet database events, follow the steps described in [Copy apps](https://support.google.com/appsheet/answer/12491039) and select AppSheet database in the **Save app to** field. Otherwise, the AppSheet database event will no longer work.
