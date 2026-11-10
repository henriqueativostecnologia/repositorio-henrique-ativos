---
fonte: https://support.google.com/appsheet/answer/11432969?hl=en
baixado: 2026-11-10
---

# Bots: The Essentials

Understand and manage bots as described in the following sections:

- [What is a bot?](#what-is-bot)
- [Explore bot management](#explore-bot-management)
- [Add a bot](#add-bot)
- [Configure a bot](#configure-bot)
- [Set the icon for a bot](#set-icon)
- [Rename a bot](#rename-bot)
- [Add a comment to a bot](#document-bot)
- [Copy a bot](#copy-bot)
- [Monitor a bot](#monitor-bot)
- [Test a bot](#test-bot)
- [Run a bot with a scheduled event](#run-bot-with-scheduled-event)
- [Enable or disable a bot](#disable-bot)
- [Delete a bot](#delete-bot)

See also [Monitor automation](https://support.google.com/appsheet/answer/11447502).

## What is a bot?

A bot defines the automation you want AppSheet to run: 
**when something happens** (an [event](https://support.google.com/appsheet/answer/11445188)) **perform a set of activities** (each activity is a [task](https://support.google.com/appsheet/answer/11445301) and a set of tasks is a [process](https://support.google.com/appsheet/answer/11445386)).

bot that contains an event that calls a process, that consists of three tasks

Bots can perform a wide variety of functions. Here are some examples:

- [Use AI](https://support.google.com/appsheet/answer/16045284) to extract information from an image or file, categorize information, and more
- Create and [send an email](https://support.google.com/appsheet/answer/11447614), [SMS message](https://support.google.com/appsheet/answer/11509435), or [notification](https://support.google.com/appsheet/answer/11513089) regarding the modified record.
- Further update the modified record.
- Update the parent record of the modified record.
- Add, update, or delete child records belonging to the modified record.
- [Call a webhook](https://support.google.com/appsheet/answer/11511244) to invoke an external web service.

A subset of features, such as [sending emails](https://support.google.com/appsheet/answer/11447614) or [triggering bots with schedule events](https://support.google.com/appsheet/answer/11432969#schedule) using AppSheet automation, are not fully supported until you [purchase a subscription](https://support.google.com/appsheet/answer/15011908). That is, you can configure these features, but they won't execute as expected.

You can perform a wide variety of other functions because after the bot is triggered, it is capable of working on any table and doing almost anything. Once enabled, bots run in the background to listen for events or trigger processes on a schedule even when you are not directly using an app. To terminate the process automation, you can disable the bot.

For example, the **Confirmed appointment** bot is configured to trigger the **User notification of confirmed appointment** process anytime an **Appointments** record is updated to notify the user that their requested appointment has been confirmed. The bot continues to listen for the appointment update events and fire the associated process when the event occurs until it is disabled.

Learn more about how bots are [triggered](#how-bots-triggered) and [not triggered](#how-bots-not-triggered), and the relationship between the [app version and bots](#appversion-bots).

## How bots are triggered

Bots can be configured to trigger a process based on:

- An **[app event](#data-change).**
- A modification to one or more columns in an [**AppSheet database**](#appsheet-databases).
- A predetermined **[schedule](#schedule)**.
- A **[Google Workspace interaction](#workspace-interactions).**

**External data change events in Sheets or Salesforce data sources**: Using add-ons, you can trigger bots based on manual or direct updates to a connected Google Sheet or Salesforce data sources, external configuration is necessary. See [Sheets](https://support.google.com/appsheet/answer/11520310) and [Salesforce](https://support.google.com/appsheet/answer/10106381), respectively.

#### App events

Bots can be configured to trigger a process based on an app event, including the following:

- Data is added, updated, or deleted through the app. For example, you can trigger a bot when:

  - A new row is added through the app.

  - An existing row is updated through the app. For example, the update may occur as the result of editing a row in a [form view](https://support.google.com/appsheet/answer/10107846), or performing a [quick edit](https://support.google.com/appsheet/answer/10106609), or invoking a client [action](https://support.google.com/appsheet/answer/10107706) through a user button click.

  - An existing row is deleted through the app.

- A data change action is invoked on the AppSheet client.

- An add, update, or delete operation is performed using the [AppSheet API](https://support.google.com/appsheet/answer/10105768).

The app event that triggers a bot can be any type of data change made through the app that arrives at the server. For example, you can add an extra table column whose only purpose is to trigger a bot. Then, you can create a client [action](https://support.google.com/appsheet/answer/10107706) button that updates the extra column's value. Clicking the action button triggers your bot.

After the app changes are [synced](https://help.appsheet.com/en/articles/953859-sync-between-the-app-and-the-backend) to the server, AppSheet:

1.  Makes the appropriate changes to the spreadsheet or database.

2.  Ensures that any formulas in the spreadsheet are re-computed to use the latest data values.

3.  Determines whether your bot should be triggered.

To further restrict when a bot is triggered, you can specify the following:

- **Type of app changes** that trigger the bot when [configuring the event](https://support.google.com/appsheet/answer/11445188#configure-event). For example, you could trigger a bot for the following changes: 

  - All changes

  - Adds only

  - Adds and updates

  - Adds and deletes

  - Deletes only

  - Updates and deletes

  - Updates only

&nbsp;

- **Condition** that triggers the bot when [configuring the event](https://support.google.com/appsheet/answer/11445188#configure-event). For example, you could trigger a bot when:

  - A new row is added to the Inspections table though the app, and the value in the `InspectionPassed` column is `FALSE`.

  - A row is updated in the `Orders` table through the app, the value in the `OrderAmount` column is over \$500, and the value in the `DeliveryDate` column is within 10 days of the current date.

- Whether a **bot can trigger other bots** and, if so, **whether to sync data changes only after this bot and all bots that it triggers complete their execution** when [creating a bot](#create-bot).

**Note**: In some cases, user access to table data is limited as governed by [security filters](https://support.google.com/appsheet/answer/10104488) on the table. AppSheet provides the ability to enable a security bypass to allow access to the table data strictly for purposes of evaluating the condition to determine whether the bot should be run.

#### AppSheet database events

Bots can be configured to trigger a process based on modifications to one or more columns in a connected AppSheet database. 

#### Scheduled events

Bots can be configured to trigger a process based on a schedule. Just like an app event, a scheduled event is capable of working on any table and performing a wide variety of functions. See also [Events: The Essentials](https://support.google.com/appsheet/answer/11445188) and  [Understanding bot scheduling and retry](https://help.appsheet.com/en/articles/5353254-understanding-bot-scheduling-and-retry#h_f506e951d5).

#### Google Workspace interactions

Bots can be configured to trigger based on Google Workspace interactions, including:

- Google Chat app interaction**.**
- Form built with Google Forms is submitted.
- Label is added or removed from an email message in Gmail. 

See also [Events: The Essentials](https://support.google.com/appsheet/answer/11445188). 

## How bots are not triggered

Bots are **not** triggered by:

- Changes made directly to data sources (except AppSheet databases)
  With the exception of [AppSheet database events](#appsheet-databases), changes you make directly to the data source (spreadsheet or database) don't go through the AppSheet server, so they don't trigger AppSheet bots. For example, if you update a BigQuery database directly, it doesn't notify the AppSheet server about the change. Since the AppSheet server is unaware of this change, it doesn't trigger any AppSheet bots.

- Data change actions invoked by a bot unless the bot that makes the data changes has been explicitly configured to [trigger other bots](#trigger-other-bots)
  Data change actions that are invoked by bots don't trigger other AppSheet bots. For example, if a client device performs an add, update, or delete that triggers a bot, and that [bot invokes a data-change action](https://support.google.com/appsheet/answer/11463007#run-a-data-action), that data change action won't invoke any bots.

- Changes made through another AppSheet app, even if that app is using the same underlying spreadsheet or database table
  This is true even if the two AppSheet apps share the same underlying spreadsheet or database table. For example, you might have a Payroll app and a separate Personnel app that share an Employees table. Bots defined in the Payroll app will only be triggered by adds, updates, or deletes to the Employees table that are performed through the Payroll app. Adds, updates, or deletes to the Employees table that are performed through the Personnel app will not trigger bots defined in the Payroll app. In short, bots only work within a single AppSheet app; they do not work across two or more apps, even if those apps share common underlying spreadsheet or database tables.

## App version and bots

Each time you change your app, AppSheet creates a new version. These changes may include changes to your bots.

AppSheet includes the app version each time a user submits their adds, updates, or deletes to the server. This is essential because the user may be submitting changes based on an older version of your app.

When invoking bots, AppSheet invokes the version of the bots that match the user's version. This may result in invoking an older version of your bot. You can detect when this occurs by examining the [audit history](https://support.google.com/appsheet/answer/10104794). The audit history includes the app version number.

After the user has submitted their changes, the AppSheet client performs a sync that retrieves the latest data and app version. Any future changes will be submitted using that app version.

## Explore bot management

We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

**This section explores how to manage bots using the new editor (preview) only.** 

Go to **Automation ** Automation icon **  \> Bots**.

The Bots panel is displayed and the first bot in the list is opened in the editor.

Bot management

As highlighted in the previous figure, you manage bots by performing the following tasks:

- [Add a bot](#add-bot)
- Edit a bot by selecting it in the Bots panel
- Manage bot components, including [events](https://support.google.com/appsheet/answer/11445188), [processes](https://support.google.com/appsheet/answer/11445386), [steps](https://support.google.com/appsheet/answer/11463007), and [tasks](https://support.google.com/appsheet/answer/11445301)
- [Configure a bot](#configure-bot)
- [Enable or disable a bot](#disable-bot)
- [Monitor a bot](#monitor-bot)
- Manage a bot:
  - [Rename a bot](#rename-bot)
  - [Test a bot](#test-bot)
  - [Run a bot with a scheduled event](#run-bot-with-scheduled-event) (not shown)
  - [Copy a bot](#copy-bot)
  - [Delete a bot](#delete-bot)
- View error and warning messages that are related to bots by clicking the error or warning indicator in the bot header
- Search all bots 

## Add a bot

To add a bot:

1.  Open the app in the app editor.

2.  Go to **Automation** Automation icon ** \> Bots** and click **+** in the top header of the Bots panel.

     We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

    ## If you are using the legacy editor

    Go to **Automation \> Bots** and click **+ New Bot**.  

3.  Perform one of the following tasks:

    - **Choose from the list of suggestions.** AppSheet Automation is an intent-aware platform. The platform understands user intent and recommends configuration options that align with what you are trying to achieve. For example, selecting the following bot suggestion would create a fully configured bot:
      When **employees** record is updated, send an email

    - **Create a custom bot**. Click **Create a new bot**.

4.  [Add and configure an event](https://support.google.com/appsheet/answer/11445188).

5.  [Configure the process](https://support.google.com/appsheet/answer/11445386), including the [steps](https://support.google.com/appsheet/answer/11463007) and [tasks](https://support.google.com/appsheet/answer/11445301).

6.  Optionally, do one or more of the following:
    - [Configure the bot](#configure-bot)
    - [Set the icon for the bot](#set-icon)
    - [Rename the bot](#rename-bot)
    - [Add a comment to the bo](#document-bot)t

7.  Save the bot.

## Configure a bot

 To configure the bot to trigger other bots:

1.  Go to **Automation** Automation icon ** \> Bots **and select the bot you want to configure in the Bots panel.

    We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

     

    ## If you are using the legacy editor

    Go to **Automation \> Bots** and expand the bot for which you want to set an icon.

2.   Expand the **Options** section.

3.  Configure the following advanced settings to control the behavior of your bot:

    +-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Option**                                                                    | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Trigger other bots                                                            | Enable this option to allow data change steps in this bot to execute other    |
|                                                                               | bots that are listening for the same data change events. Disable this option  |
|                                                                               | to prevent data change events triggered by the current bot from triggering    |
|                                                                               | other bots.                                                                   |
|                                                                               |                                                                               |
|                                                                               |                                                                               |
|                                                                               |                                                                               |
|                                                                               | For **scheduled events**, this setting is valid in the following scenarios:   |
|                                                                               |                                                                               |
|                                                                               | -   If                                                                        |
|                                                                               |     **[ForEachRowIn                                                           |
|                                                                               | Table](https://support.google.com/appsheet/answer/11445188#configure-event)** |
|                                                                               |     is enabled and a data change step is included in the process.             |
|                                                                               | -   If **ForEachRowInTable** is disabled and a [Call a                        |
|                                                                               |                                                                               |
|                                                                               |  process](https://support.google.com/appsheet/answer/11463007#call-a-process) |
|                                                                               |     step that includes a data change event is included in the process.        |
|                                                                               |                                                                               |
|                                                                               | If enabled, the following policies are enforced to avoid infinite             |
|                                                                               | event-trigger loops:                                                          |
|                                                                               |                                                                               |
|                                                                               | -   An event that is a result of a data change made by the bot cannot         |
|                                                                               |     subsequently trigger the same bot.                                        |
|                                                                               |                                                                               |
|                                                                               | -   If two or more bots trigger one another continuously in succession, the   |
|                                                                               |     maximum number of triggers that can be initiated between them is 5. For   |
|                                                                               |     example:                                                                  |
|                                                                               |                                                                               |
|                                                                               |     -   Bot A triggers Bot B                                                  |
|                                                                               |                                                                               |
|                                                                               |     -   Bot B triggers Bot A                                                  |
|                                                                               |                                                                               |
|                                                                               |     -   Bot A triggers Bot B                                                  |
|                                                                               |                                                                               |
|                                                                               |     -   Bot B triggers Bot A                                                  |
|                                                                               |                                                                               |
|                                                                               |     -   Bot A triggers Bot B                                                  |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Wait for execution to complete                                                | **Note**: This option is available only if the **Trigger other bots** option  |
|                                                                               | is enabled.                                                                   |
|                                                                               |                                                                               |
|                                                                               | Enable this option to instruct the app to sync data changes only after this   |
|                                                                               | bot and all bots that it triggers complete their execution. Disable this      |
|                                                                               | option to instruct the app to sync data after this bot completes its          |
|                                                                               | execution, even if there are triggered bots still executing in the            |
|                                                                               | background.                                                                   |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

4.   Save the bot.

## Set the icon for a bot

The bot icon can provide easy identification.

To set the icon for a bot:

1.  Go to **Automation** Automation icon ** \> Bots **and select the bot you want to configure in the Bots panel.

    We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

     

    ## If you are using the legacy editor

    Go to **Automation \> Bots** and expand the bot for which you want to set an icon.

2.   Expand the **Options** section.

3.  Search for and select the desired icon in the **Bot icon** field.

4.   Save the bot.

  

## Rename a bot

To rename a bot:

1.  Go to **Automation** Automation icon ** \> Bots **and double-click the bot you want to rename in the Bots panel.

    We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

     

    ## If you are using the legacy editor

    Go to **Automation \> Bots** and expand the bot that you want to rename.

2.  Position your cursor over the bot you want to rename in the Bots navigation panel.

3.  Select **More**  Three-dot menu vertical   \> **Rename **in the bot header.

4.  Rename the bot.

Alternatively, you can double-click the name of the bot in the Bots panel and edit the name.

## Add a comment to a bot

To add a comment to a bot:

1.  Go to **Automation** Automation icon ** \> Bots **and select the bot you want to rename in the Bots panel.

    We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

     

    ## If you are using the legacy editor

    Go to **Automation \> Bots** and expand the bot for which you want to set an icon.

2.  Expand the **Documentation** section.

3.  Enter a descriptive comment for the bot that will enable collaborators to easily understand its purpose.

## Copy a bot

Copy the contents of a bot. A numeric value (such as 2) is appended to the bot and event names to ensure they are unique.

To copy a bot:

1.  Go to **Automation ** Automation icon ** \> Bots**.
2.  Select the bot you want to copy in the list.
3.  Select **More**  Three-dot menu vertical   \> **Duplicate **in the bot header.

 We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

## If you are using the legacy editor

To copy a bot:

1.  Go to **Automation \> Bots**.
2.  Expand the bot you want to copy.
3.  Click **Copy **in the bot heading.

 

##  Monitor a bot

Use the AppSheet [automation monitor](https://support.google.com/appsheet/answer/11447502) to monitor automation in your apps and keep a track of the bot executions that were successful, encountered errors, and are still pending

To monitor a bot:

To copy a bot:

1.  Go to **Automation ** Automation icon ** \> Bots**.
2.  Select the bot you want to monitor in the list.
3.  Click **Monitor **in the bot header.

 We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

## If you are using the legacy editor

To monitor a bot:

1.  Go to **Automation \> Bots**.
2.  Expand the bot you want to monitor.
3.  Click **Monitor **in the bot heading.

## Test a bot

Test a bot execution.

**Note**: For AppSheet free accounts, when testing a bot emails are sent only to the app owner.

To test a bot:

1.  Go to **Automation** Automation icon ** \> Bots **and select the bot you want to test in the Bots panel.

    We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

     

    ## If you are using the legacy editor

    Go to **Automation \> Bots** and expand the bot you want to test.

2.  Select **More**  Three-dot menu vertical   \> **Test **in the bot header.

##  Run a bot with a scheduled event

**Note**: For AppSheet free accounts, when running a bot with a scheduled event emails are sent only to the app owner.

To run a bot with a scheduled event on demand: 

1.  Go to **Automation** Automation icon ** \> Bots **and select the bot with the scheduled event that you want to test in the Bots panel.

    We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

     

    ## If you are using the legacy editor

    Go to **Automation \> Bots** and expand the bot you want to test.

2.  Click **Run **in the bot header.

## Enable or disable a bot

You can disable the bot to temporarily stop the automation. Then, re-enable it. 

To enable or disable a bot:

1.  Go to **Automation ** Automation icon ** \> Bots**.
2.  Select the bot you want to enable or disable in the list.
3.  Select **Enable** or **Disable **in the bot header.

 We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

## If you are using the legacy editor

To disable a bot:

1.  Go to **Automation \> Bots**.
2.  Expand the bot you want to delete.
3.  Click **Disable **in the bot heading.

## Delete a bot

Delete a bot to permanently remove it.

To delete a bot:

1.  Go to **Automation ** Automation icon ** \> Bots**.
2.  Select the bot you want to delete in the list.
3.  Select **More**  Three-dot menu vertical   \> **Delete **in the bot header.

 We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

## If you are using the legacy editor

To delete a bot:

1.  Go to **Automation \> Bots**.
2.  Expand the bot you want to delete.
3.  Click **Delete **in the bot heading.
