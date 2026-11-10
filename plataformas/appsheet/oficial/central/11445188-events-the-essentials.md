---
fonte: https://support.google.com/appsheet/answer/11445188?hl=en
baixado: 2026-11-10
---

# Events: The Essentials

Manage an event in a bot as described in the following sections:

- [What is an event?](#what-is-event)
- [Externally triggered events](#externally-triggered-events)
- [Add an event to a bot](#add-event)
- [Configure an app event](#configure-app-event)
- [Configure an AppSheet database event](#configure-appsheet-database-event)
- [Configure a scheduled event](#configure-scheduled-event)
- [Configure a Chat event](#configure-chat-event)
- [Configure a Forms event](#configure-forms-event)
- [Configure a Gmail event (beta)](#configure-gmail-event)
- [Copy an existing event](#copy-existing-event)
- [View events](#view-events)
- [Edit an event](#edit-event)
- [Delete an event](#delete-event)
- [Example: Trigger a schedule event on a specific date](#example-trigger-scheduled-event-on-specific-date)

## ****What is an event?

An event defines the activity or schedule that triggers a process. You can configure the types of events summarized in the following table.

|                   |                                                                                                                                                                                                                                                               |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Event type**    | **What triggers this event type?**                                                                                                                                                                                                                            |
| App               | Data is added, modified, or deleted through the app. For example, the status of a service ticket is changed through the app. See [Configure an app event](#configure-app-event).                                                                              |
| AppSheet database | Data is added, modified, or deleted in one or more columns in an AppSheet database. For example, the status of a service ticket is changed directly in the AppSheet database. See [Configure an AppSheet database event](#configure-appsheet-database-event). |
| Scheduled         | Set to occur periodically at a specific time. For example, every Monday morning at 9 AM. See [Configure a scheduled event](#configure-scheduled-event).                                                                                                       |
| Google Chat app   | Chat interactions, including interacting with a slash command in a Chat space, or adding or removing a Chat app in a Chat space. See [Configure a Chat event](#configure-chat-event).                                                                         |
| Google Forms      | Response for a form from Google Forms is received. For example, a travel request is sent for approval. See [Configure a Google Forms event](#configure-forms-event).                                                                                          |
| Gmail (beta)      | Label is added or removed from an email message in Gmail. See [Configure a Gmail event (beta)](#configure-gmail-event). Gmail events are triggered by external sources. See [Externally triggered events](#externally-triggered-events).                      |

App events generated due to an app action or as a result of an app data change from an [AppSheet API](https://support.google.com/appsheet/answer/10105768) call will fire without any external configuration.

 

## Externally triggered events

Most events are triggered by some change in the app data. For example, the `Status` column in an `Orders` table is changed to `Complete`.

Some events are triggered by an activity that occurs external to the app, and don't rely on an AppSheet table from a predefined data source to trigger a process. For example, a Gmail event (beta) that triggers a process when a label is added or removed from an email message. 

Externally triggered events:

- Only appear in the Automation tab of the editor
- Don't appear as tables in the Data tab
  **Note**: When you add an externally triggered event to an automation, a data source is added to your account which can be used in your automations, but no table is added to your app.
- Don't require system views, actions, and so on
- Don't support AI tasks or data actions (such as delete row, set row values, and so on) that require access to data in a table

For Gmail events, you can access and save email content to an existing table in your app, as described in [Build an automation using Gmail](https://support.google.com/appsheet/answer/15725655).

For data change events that are triggered externally in Sheets or Salesforce data sources, external configuration is necessary. See [Sheets](https://support.google.com/appsheet/answer/11520310) and [Salesforce](https://support.google.com/appsheet/answer/10106381), respectively.

## ****Add an event to a bot

To add an event to a bot:

1.  [Add a bot](https://support.google.com/appsheet/answer/11432969#create-bot).

2.  In the center panel, click **Configure event**.

    Click Configure event in the center panel

3.  In the **Event name** field, enter a name for the event.

4.  Do one of the following:

    - To **reuse an existing event**, select an event under **From this App**.
      For more information, see [Reuse automation components.](https://support.google.com/appsheet/answer/12193489)
    - To **create a new event**, do one of the following:
      - Click **Create a new event**.
      - Select an event from the list of **Suggestions.**
        AppSheet Automation is an intent-aware platform. The platform understands user intent and recommends configuration options that align with what you are trying to achieve. For example, selecting the following suggestion would configure a process and **Send an email** task for you:
        `When Available record is updated, send an email`

5.  Select and configure one of the following event sources:
    - [App event](#configure-app-event)
    - [AppSheet database event](#configure-appsheet-database-event)
    - [Scheduled event](#configure-scheduled-event)
    - [Google Chat event](#configure-chat-event)
    - [Google Forms event](#configure-forms-event) 
    - [Gmail event](#configure-gmail-event) (beta)

6.  Save the app.

## Configure an app event

To [add](#add-event) an app event, configure the following settings:

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Event name                                                                    | Name of the event.                                                            |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Event source                                                                  | Select **App**.                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Data change type                                                              | Select the data change types made through the app that trigger the            |
|                                                                               | event. Select one or more of the following options: Adds, Deletes, Updates.   |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Table                                                                         | Select the table whose data changes trigger the event.                        |
|                                                                               |                                                                               |
|                                                                               | To view or edit the structure of the selected table, position your cursor in  |
|                                                                               | the field and click Edit icon  . See [Tables: The                             |
|                                                                               | Essentials](https://support.google.com/appsheet/answer/10105821) for more     |
|                                                                               | information.                                                                  |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Condition                                                                     | Condition to check before triggering the event.                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Bypass Security Filters?                                                      | Toggle to indicates whether to execute as though there are no security        |
|                                                                               | filters on the data sources. This setting allows automated tasks (that run as |
|                                                                               | the app owner ID) to continue working. It is useful for generating reports or |
|                                                                               | performing other tasks that require more information.                         |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Event icon                                                                    | Expand the **Display** section and select an icon for the event.              |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Descriptive comment                                                           | Expand the **Documentation** section and enter a comment that describes the   |
|                                                                               | purpose of the event.                                                         |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Linking                                                                       | Enable or disable reuse of this component by expanding the **Linking** panel  |
|                                                                               | and toggling the **Linking** setting. See [Reuse automation                   |
|                                                                               | components](https://support.google.com/appsheet/answer/12193489).             |
|                                                                               |                                                                               |
|                                                                               | \                                                                             |
|                                                                               | Expand the Linking panel and toggle the Linking setting to enable or disable  |
|                                                                               | component reuse                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

 

The following shows an example of an App change event that is triggered by any change (add, delete, or update) to the Inventory table.

Data change event for adds only

##  Configure an AppSheet database event

Before you can add an AppSheet database event, you must:

1.  Create an AppSheet database. See [Create and copy databases](https://support.google.com/appsheet/answer/12635312).
2.  Add the AppSheet database to your app by [creating an app from the AppSheet database](https://support.google.com/appsheet/answer/12631543#create-app-from-database) or [adding the AppSheet database to an existing app](https://support.google.com/appsheet/answer/12631543#add-database-to-app). In each case, select **AppSheet databases** as the data source and then navigate to the database.

App concepts or table settings defined in the app editor (such as making a column non-editable or required) won't affect how the bot gets triggered for event sources that are external to the app. For example, even if a column is marked as non-editable for apps, it can still be selected in the Column to watch for updates setting in the event.

[Add an event to a bot](#add-event), and configure the settings for an AppSheet database event, as follows:

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Event name                                                                    | Name of the event.                                                            |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Event source                                                                  | Select **AppSheet database**.                                                 |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Table                                                                         | Select the table whose data changes trigger the event.                        |
|                                                                               |                                                                               |
|                                                                               | To view or edit the structure of the selected table, position your cursor in  |
|                                                                               | the field and click Edit icon  . See [Tables: The                             |
|                                                                               | Essentials](https://support.google.com/appsheet/answer/10105821) for more     |
|                                                                               | information.                                                                  |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Data change type                                                              | Select the data change types made to the AppSheet database that trigger the   |
|                                                                               | event. Select one or more of the following options: Adds, Deletes, Updates.   |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Columns to watch for updates                                                  | **Note**: This field is displayed only when **Updates** is selected for Data  |
|                                                                               | change type.                                                                  |
|                                                                               |                                                                               |
|                                                                               | Columns from the selected table whose data updates trigger the event. Open    |
|                                                                               | the drop-down and select one or more columns.                                 |
|                                                                               |                                                                               |
|                                                                               | For example:                                                                  |
|                                                                               |                                                                               |
|                                                                               | Continue to watch for updates                                                 |
|                                                                               |                                                                               |
|                                                                               | Make sure you select only those columns that you want to trigger the event.   |
|                                                                               | For example, you might want to be notified when the status or due date is     |
|                                                                               | changed, but not for other changes. In this example, you'd select only        |
|                                                                               | the Status and Due Date columns, but not the other column to avoid excessive  |
|                                                                               | or unnecessary notifications.                                                 |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Condition                                                                     | Condition that must be true to trigger the event.                             |
|                                                                               |                                                                               |
|                                                                               | **Note**: To trigger an event based on the time that *any* data is updated in |
|                                                                               | a row of the AppSheet database, do one of the following:                      |
|                                                                               |                                                                               |
|                                                                               | -   Select all columns in the Column to watch for updates field.              |
|                                                                               | -   Add a column of type `Update row timestamp` to track updates made to any  |
|                                                                               |     row. For more information, see [Track changes made through an AppSheet    |
|                                                                               |     database or the                                                           |
|                                                                               |     app](https:                                                               |
|                                                                               | //support.google.com/appsheet/answer/10106435#appsheet-database-change-type). |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Event icon                                                                    | Expand the **Display** section and select an icon for the event.              |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Descriptive comment                                                           | Expand the **Documentation** section and enter a comment that describes the   |
|                                                                               | purpose of the event.                                                         |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Linking                                                                       | Enable or disable reuse of this component by expanding the **Linking** panel  |
|                                                                               | and toggling the **Linking** setting. See [Reuse automation                   |
|                                                                               | components](https://support.google.com/appsheet/answer/12193489).             |
|                                                                               |                                                                               |
|                                                                               | \                                                                             |
|                                                                               | Expand the Linking panel and toggle the Linking setting to enable or disable  |
|                                                                               | component reuse                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

 

## Configure a scheduled event

A subset of features, such as [sending emails](https://support.google.com/appsheet/answer/11447614) or [triggering bots with schedule events](https://support.google.com/appsheet/answer/11432969#schedule) using AppSheet automation, are not fully supported until you [purchase a subscription](https://support.google.com/appsheet/answer/15011908). That is, you can configure these features, but they won't execute as expected.

[Add an event to a bot](#add-event), and configure the settings for a scheduled event, as follows

**Note**: To reference columns in a table, you must turn on the **For Each Row In Table** settings.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Event name                                                                    | Name of the event.                                                            |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Event source                                                                  | Select **Scheduled**.                                                         |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Schedule                                                                      | Set the schedule and time for the event.                                      |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Time zone                                                                     | Set the time zone for the schedule event.                                     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| For Each Row In Table                                                         | Flag that specifies whether to operate on each row in the specified table.    |
|                                                                               |                                                                               |
|                                                                               | Turn on **For Each Row In Table **if you want to run a process for each row   |
|                                                                               | of data in the table. When turned on, the option to specify a filter          |
|                                                                               | condition appears. If your task has return values, you must configure your    |
|                                                                               | automation as described in [Run a task with return values on multiple rows    |
|                                                                               | for a scheduled event](#run-task-with-return-values-multiple-rows).           |
|                                                                               |                                                                               |
|                                                                               |                                                                               |
|                                                                               |                                                                               |
|                                                                               | Turn off **For Each Row In Table** if your process doesn't rely on data in a  |
|                                                                               | table. When turned off, you can select any event except [Run a data           |
|                                                                               | a                                                                             |
|                                                                               | ction](https://support.google.com/appsheet/answer/11463007#run-a-data-action) |
|                                                                               | as a valid step type in the process.                                          |
|                                                                               |                                                                               |
|                                                                               | **Only turn off this setting if your process doesn’t rely on data in any      |
|                                                                               | table.**                                                                      |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Table                                                                         | **Notes**:                                                                    |
|                                                                               |                                                                               |
|                                                                               | -   This field only displays if **For Each Row In Table** is enabled.         |
|                                                                               | -   If you have [partitioned the                                              |
|                                                                               |     data](https://support.google.com/appsheet/answer/10105383), only one      |
|                                                                               |     partition will be evaluated, based on the Filter Condition.               |
|                                                                               |                                                                               |
|                                                                               | Table referenced by the event. Select an existing table in the list.          |
|                                                                               |                                                                               |
|                                                                               | Click **View definition** to view the structure of the selected table. See    |
|                                                                               | [Tables: The Essentials](https://support.google.com/appsheet/answer/10105821) |
|                                                                               | for more information about adding tables.                                     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Filter Condition                                                              | **Note**: This field only displays if **For Each Row In Table** is enabled.   |
|                                                                               |                                                                               |
|                                                                               | Filter condition to use to identify which rows in table are impacted.         |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Condition                                                                     | Condition that must be true to trigger the event.                             |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Bypass Security Filters?                                                      | Toggle to indicates whether to execute as though there are no security        |
|                                                                               | filters on the data sources.                                                  |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Event icon                                                                    | Expand the **Display** section and select an icon for the event.              |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Descriptive comment                                                           | Expand the **Documentation** section and enter a comment that describes the   |
|                                                                               | purpose of the event.                                                         |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Linking                                                                       | Enable or disable reuse of this component by expanding the **Linking** panel  |
|                                                                               | and toggling the **Linking** setting. See [Reuse automation                   |
|                                                                               | components](https://support.google.com/appsheet/answer/12193489).             |
|                                                                               |                                                                               |
|                                                                               | \                                                                             |
|                                                                               | Expand the Linking panel and toggle the Linking setting to enable or disable  |
|                                                                               | component reuse                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

 The following shows an example of a Scheduled event that is triggered every day at 12:00 PM UTC.

Settings for schedule events

### Run a task with return values on multiple rows for a scheduled event

The **For each row in table** configuration setting for scheduled events updates only the last row in the table for tasks with return values. 

Therefore, to run a task with return values on a multiple rows for a scheduled event (such as, the [Call a script](https://support.google.com/appsheet/answer/11997142) task), you need to create two bots in your automation, as follows:

1.  Create a bot that runs on a schedule and sets a column to [trigger another bot](https://support.google.com/appsheet/answer/11432969#ti). Turn on **For Each row in table** for the scheduled event.
2.  Create a bot that is triggered by the first bot to run the Apps Script task on a specific row. 

## Configure a Chat event

You must be a **Google Workspace user** to create Chat apps with AppSheet. See [Add AppSheet to Google Workspace](https://support.google.com/a/answer/10447197).

Before you can configure a Chat event, you must [configure your Chat app with AppSheet](https://support.google.com/appsheet/answer/12849362).

[Add an event to a bot](#add-event), and configure the settings for a Chat event, as follows

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Event name                                                                    | Name of the event.                                                            |
|                                                                               |                                                                               |
|                                                                               | **Note**: The name will be displayed in Chat.                                 |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Event source                                                                  | Select **Chat**.                                                              |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Chat interaction                                                              | Chat interaction that triggers the event:                                     |
|                                                                               |                                                                               |
|                                                                               | -   **Slash command** - Slash command is issued in the Chat space.            |
|                                                                               | -   **Added to space** - Chat app is added to a Chat space.                   |
|                                                                               | -   **Removed from space** - Chat app is removed from the Chat space.         |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Name                                                                          | **Note**: Valid only if **Slash command** is selected as the Chat             |
|                                                                               | interaction.                                                                  |
|                                                                               |                                                                               |
|                                                                               | Slash command that triggers the event.                                        |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Description                                                                   | **Note**: Valid only if **Slash command** is selected as the Chat             |
|                                                                               | interaction.                                                                  |
|                                                                               |                                                                               |
|                                                                               | Description of the slash command that triggers the event.                     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Event icon                                                                    | Expand the **Display** section and select an icon for the event.              |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Descriptive comment                                                           | Expand the **Documentation** section and enter a comment that describes the   |
|                                                                               | purpose of the event.                                                         |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

The following shows an example of a Chat event.

Chat event

## Configure a Google Forms event

You must be a **Google Workspace user** to build AppSheet automations with Google Forms. See [Add AppSheet to Google Workspace](https://support.google.com/a/answer/10447197).

If you are using your Google Workspace account, the [Google Workspace Terms of Service](https://workspace.google.com/terms/premier_terms/) govern your use of Google Forms. Otherwise, refer to the [Google Terms of Service](https://policies.google.com/terms).

Actions that are triggered by a Google Forms event can rely only on read-only data.

Timestamps in Google Forms events are in UTC time.

Before you can add a Google Forms event, you must:

1.  Create a form in Google Forms. See [How to use Google Forms](https://support.google.com/docs/answer/6281888). 

2.  Do one of the following:

    - [Create an app from the form](https://support.google.com/appsheet/answer/14824665)
    - [Add the form](https://support.google.com/appsheet/answer/10105821#add) to an existing app

    In each case, select **Google Forms** as the data source, navigate to the form, and click **Select**.

See also [Build an automation using Google Forms](https://support.google.com/appsheet/answer/14634161).

[Add an event to a bot](#add-event), and configure the settings for a Google Forms event, as follows

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Event name                                                                    | Name of the event.                                                            |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Event source                                                                  | Select **Forms**.                                                             |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Form                                                                          | Select the form from Google Forms that triggers the event.                    |
|                                                                               |                                                                               |
|                                                                               | **Note**: You need to ensure that the form is [added as a                     |
|                                                                               | table](https://support.google.com/appsheet/answer/10105821#add) to your app   |
|                                                                               | before you use it in a Google Forms event.                                    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Condition                                                                     | Condition that must be true to trigger the event.                             |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Bypass Security Filters?                                                      | **Not supported for Google Forms events.** Triggers from event sources that   |
|                                                                               | are external to the app can only be run as the app owner.                     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Event icon                                                                    | Expand the **Display** section and select an icon for the event.              |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Descriptive comment                                                           | Expand the **Documentation** section and enter a comment that describes the   |
|                                                                               | purpose of the event.                                                         |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

The following shows an example of a Forms event that is triggered when a Travel Request form is submitted.

Event configuration settings

##  Configure a Gmail event (beta)

This is a **beta** release of building automations using Gmail events. See [Track and manage feature releases](https://support.google.com/a/topic/1227580). Preview offerings are intended for use in test environments only. This feature is not recommended for use in production apps. For questions or assistance with this feature, contact [AppSheet Support](https://www.appsheet.com/Support/Contact).

You must be a **Google Workspace user** to build AppSheet automations with Gmail. See [Add AppSheet to Google Workspace](https://support.google.com/a/answer/10447197).

If you are using your Google Workspace account, the [Google Workspace Terms of Service](https://workspace.google.com/terms/premier_terms/) govern your use of Gmail. Otherwise, refer to the [Google Terms of Service](https://policies.google.com/terms).

Gmail events can be triggered when you add or remove a label from an email message in Gmail.

You can create a new label to trigger the Gmail event, as described in [Create labels to organize Gmail](https://support.google.com/mail/answer/118708). Alternatively, you can use one of the default Gmail labels (Inbox, Unread, Starred, and so on). You can apply a label automatically using a filter, as described in [Create rules to filter your emails](https://support.google.com/mail/answer/6579). See also [How to support collaborative or delegated email sources](https://support.google.com/appsheet/answer/15725655#collaborative-delegated-email).

After the Gmail event is triggered, you can access content in the email message associated with the event using the available message column values. See [How to access content in the email messages](https://support.google.com/appsheet/answer/15725655). **All email message content is read-only.**

**Note: **When a Gmail event is triggered for a message on an email thread, the automation is also triggered for each subsequent reply in the thread.

See also: [Build an automation using Gmail](https://support.google.com/appsheet/answer/15725655)

[Add an event to a bot](#add-event), and configure the settings for a Gmail event, as follows:

 

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Event name                                                                    | Name of the event.                                                            |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Event source                                                                  | Select **Gmail**.                                                             |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Authorize                                                                     | If no Gmail account has been authorized and connected as a data source, do    |
|                                                                               | the following:                                                                |
|                                                                               |                                                                               |
|                                                                               | 1.  Click **Authorize**.\                                                     |
|                                                                               |     The Add a new data source dialog displays.                                |
|                                                                               | 2.  Click **Gmail (beta)**.\                                                  |
|                                                                               |     The Choose an account dialog displays.                                    |
|                                                                               | 3.  Choose an account or click **Use another account** and respond to the     |
|                                                                               |     prompts to allow access to the Gmail account.                             |
|                                                                               |                                                                               |
|                                                                               | **Note**: Gmail events are *tableless*. When you connect a Gmail account to   |
|                                                                               | your AppSheet app when adding a Gmail event to an automation, it is added as  |
|                                                                               | a data source but no table is added to your app. For more information, see    |
|                                                                               | [What is a tableless                                                          |
|                                                                               | event?](https://support.google.com/appsheet/answer/11445188#tableless) To     |
|                                                                               | view or delete the Gmail data source, see [Use multiple data                  |
|                                                                               | sources](https://support.google.com/appsheet/answer/10106309).                |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Account                                                                       | Select the Gmail account in the drop-down that you want to use to trigger     |
|                                                                               | this event. To authorize a new Gmail account, select **Connect another        |
|                                                                               | account** and follow the prompts.                                             |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Label to watch                                                                | Define the email label and label interactions that trigger the event.         |
|                                                                               |                                                                               |
|                                                                               | 1.  Select a label from the list associated with the Gmail account in the     |
|                                                                               |     drop-down.                                                                |
|                                                                               | 2.  Select one or both of the following label interactions:                   |
|                                                                               |     -   Added label to email                                                  |
|                                                                               |     -   Removed label from email                                              |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Event icon                                                                    | Expand the **Display** section and select an icon for the event.              |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Descriptive comment                                                           | Expand the **Documentation** section and enter a comment that describes the   |
|                                                                               | purpose of the event.                                                         |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

The following shows an example of a Gmail event that is triggered when the **Urgent** label is added to or removed from an email message in the `user@altostrat.com` Gmail account.

Gmail event in an AppSheet automation

## ****Copy an existing event

When you copy an event, the name of the new event defaults to the name of the current event followed by a unique number (starting with 1 and incrementing), such as **My Event 1**.

To copy an existing reusable event:

1.  Open the app in the editor.
2.  Go to **Automation** Automation icon ** \> Events**.
3.  Select the event you want to copy in the Events panel.
4.  Select **More ************************************************************************************************************************\> Duplicate**.

We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

## If you are using the legacy editor

To copy an existing event:

1.  Select **Automation \> Events**.
2.  Select the event you want to copy.
3.  Click **Copy** in the event heading.

## ****View events

To view an event in a bot, select **Automation** Automation icon ** \> Bots**, select the bot in the Bots panel, and click the event in the main panel.

To view all events by table, select **Automation** Automation icon ** \> Events**. By default, only [reusable (linkable) events](https://support.google.com/appsheet/answer/12193489) are shown. To view all events, turn on **Show all automation components**, as described in [Configure app editor settings](https://support.google.com/appsheet/answer/13396480).

We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

 

## If you are using the legacy editor

To view all events, select **Automation** ** \> Events**. Events are organized based by table.

If an event is used by one or more bots, it displays a reusability indicator (number adjacent to the event name) to indicate the number of bots using the event. In the example below, the **Scheduled: Every day** event is a reusable component that is used in  **two**  bots.

View all events and see the number of shared components

Click the number to view the list of bots that are using the event. For more information, see [Reuse automation components](https://support.google.com/appsheet/answer/12193489).

## ****Edit an event

**Note**: If an event that is reused, consider the impact to all bots before editing the event.

To edit an event, [view the event](#view-event) in the app editor, edit the configuration, and save your changes.

## ****Delete an event

**Note**: If a [reusable event](https://support.google.com/appsheet/answer/12193489) is used in multiple bots, consider the impact to all bots before deleting the event. If you try to delete an event that is used by one or more bots, AppSheet will prompt you to confirm the operation, as shown:

Warning displayed for reusable component when attempting to delete

 To remove an event from a bot in the editor, select **Remove** in the drop-down menu. It is removed from the bot but retained on the **Events** tab.

Delete an event

To delete a reusable event:

1.  Select **Automation** Automation icon ** \> Events**.
2.  Select the event you want to delete in the Events panel.
3.  Select **More ********************************************************************************************************************************************************************************************************************************************************\> Delete**.

We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

##  If you are using the legacy editor

 To delete a reusable event:

1.  Select **Automation \> Events**.
2.  Expand the event you want to delete.
3.  Click **Delete** in the event heading.

## ****Example: Trigger a schedule event on a specific date

Trigger a schedule event automatically at predetermined dates obtained from the app's data. This can be done using the `Condition` setting of the scheduled report.

For example, suppose you have a table called **Tasks**. Each row in this table is a task that you have to perform, and each task has a `Date` column that stores the date when you have to perform the task. You can set up a scheduled report that will automatically send you an *alarm* message to remind you of the task at 7:00 am on the day the task is supposed to be carried out.

To do this, in the app editor, configure the schedule event as follows:

|                    |                                 |
|--------------------|---------------------------------|
| **Setting**        | **Setting**                     |
| Event name         | Any event name                  |
| Event source       | **Schedule**                    |
| Schedule           | **Daily**                       |
| Time               | **7:00 am**                     |
| Time zone          | Set according to your time zone |
| For EachRowInTable | **Enable**                      |
| Table              | **Tasks**                       |
| Filter Condition   | **`TODAY()=[Date]`**            |

Here's how the schedule works. Every day, at 7:00 am, the schedule will go through each task in the Tasks table and check the date of the task. If the date of the task is the current date, the schedule will be triggered, and an alert message will be sent.

**Note**: This design will not work if you want to trigger reports at specific times (hours and minutes) obtained from the app's data.
