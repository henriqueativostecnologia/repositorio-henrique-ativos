---
fonte: https://support.google.com/appsheet/answer/11513089?hl=en
baixado: 2026-11-10
---

# Send a notification from an automation

Push notifications are a direct mechanism to alert app users on Android and iOS devices. Send a notification from an automation bot as described in the following sections:

- [Add and configure the task](#add-configure)
- [How AppSheet processes notifications](#how-appsheet-processes-notifications)

## Add and configure the Send a notification task

Add and configure the **Send a notification** task by performing the following steps:

1.  Add the **Send a notification **task to a bot, as described in [Add a task to a bot](https://support.google.com/appsheet/answer/11445301#add-task).
2.  Configure the **Send a notification** task by setting the properties described in the following tables.
3.  When you are done, save the app by selecting one of the following:
    - **Save** - Save the app.
    - **Save & verify data** - Save the app and verify that it is runnable based on external dependencies.

After you save the app, you can reuse the task in other bots.

Configure the **Send a notification t**ask by using the settings described in the following tables.

See also [How AppSheet processes notifications](#how-appsheet-processes-notifications).

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Property**                                                                  | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Linking                                                                       | Enable or disable reuse of this component by expanding the **Linking** panel  |
|                                                                               | and toggling the **Linking** setting. See [Reuse automation                   |
|                                                                               | components](https://support.google.com/appsheet/answer/12193489).             |
|                                                                               |                                                                               |
|                                                                               | Expand the Linking panel and toggle the Linking setting to enable or disable  |
|                                                                               | component reuse                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Task name                                                                     | Name of the task. It must be unique within your app.                          |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Table name                                                                    | Table defined in the                                                          |
|                                                                               | [event](https://support.google.com/appsheet/answer/11445188) and used by the  |
|                                                                               | task.                                                                         |
|                                                                               |                                                                               |
|                                                                               | To view or edit the structure of the selected table, position your cursor in  |
|                                                                               | the field and click Edit icon  . See [Tables: The                             |
|                                                                               | Essentials](https://support.google.com/appsheet/answer/10105821) for more     |
|                                                                               | information.                                                                  |
|                                                                               |                                                                               |
|                                                                               | **Note**: To use a table that is different from the table defined in the      |
|                                                                               | event, add a [Call a                                                          |
|                                                                               | process](https://s                                                            |
|                                                                               | upport.google.com/appsheet/answer/11463007#step-type&zippy=%2Ccall-a-process) |
|                                                                               | step.                                                                         |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| To                                                                            | List of email recipients. Defaults to the app owner's email address.          |
|                                                                               |                                                                               |
|                                                                               | Click **Add** to add an email address or an expression using the Expression   |
|                                                                               | Assistant. Repeat to add additional email recipients.                         |
|                                                                               |                                                                               |
|                                                                               | See [Add email                                                                |
|                                                                               | recipien                                                                      |
|                                                                               | ts](https://support.google.com/appsheet/answer/11447614#add-email-recipients) |
|                                                                               | for more information.                                                         |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Use default content?                                                          | Toggle to indicate whether you want to use the default email content or       |
|                                                                               | provide customized content. If enabled, the task uses default content. If     |
|                                                                               | disabled, customize the content using the additional properties displayed, as |
|                                                                               | described below.                                                              |
|                                                                               |                                                                               |
|                                                                               | This property is enabled by default.                                          |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

If you disable the **Use default content?** property, customize the content using the additional properties displayed, as described below.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Property**                                                                  | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Title                                                                         | Title of the notification. Specify text and                                   |
|                                                                               | [variables](https://support.google.com/appsheet/answer/11539253).             |
|                                                                               |                                                                               |
|                                                                               | By default, a meaningful title is used.                                       |
|                                                                               |                                                                               |
|                                                                               | **Example**:                                                                  |
|                                                                               | `'<<EmployeeName>> please pickup package from <<CustomerName>>'.`             |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Body                                                                          | Body of the message. Specify text and                                         |
|                                                                               | [variables](https://support.google.com/appsheet/answer/11539253).             |
|                                                                               |                                                                               |
|                                                                               | By default, contains the following [built-in                                  |
|                                                                               | variab                                                                        |
|                                                                               | les](https://support.google.com/appsheet/answer/11539253#built-in-variables): |
|                                                                               |                                                                               |
|                                                                               | `<<_ROWKEY>>`                                                                 |
|                                                                               |                                                                               |
|                                                                               | `<<_UPDATEMODE>>`                                                             |
|                                                                               |                                                                               |
|                                                                               | `<<_USERNAME>>`                                                               |
|                                                                               |                                                                               |
|                                                                               | `<<_NOW>>`                                                                    |
|                                                                               |                                                                               |
|                                                                               | **Example**:                                                                  |
|                                                                               |                                                                               |
|                                                                               | `<<[FirstName]>> <<[LastName]>> your order for <<[Quan                        |
|                                                                               | tity] * [Price]>> shipped on <<TODAY()>> and will arrive on <<TODAY() + 3>>.` |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| DeepLink                                                                      | [DeepLink](https://support.google.com/appsheet/answer/10106757) to include in |
|                                                                               | the notification. You can use the DeepLink to link to specific application    |
|                                                                               | data, including:                                                              |
|                                                                               |                                                                               |
|                                                                               | -   Your AppSheet application                                                 |
|                                                                               | -   An entire View within your application                                    |
|                                                                               | -   A filtered View within your application                                   |
|                                                                               | -   A specific row within a View within your application                      |
|                                                                               | -   A form with pre-filled values                                             |
|                                                                               | -   A custom DeepLink you specify using an expression                         |
|                                                                               |                                                                               |
|                                                                               | Enter a link or an expression using the Expression Assistant.                 |
|                                                                               |                                                                               |
|                                                                               | Defaults to a DeepLink to the AppSheet application.                           |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

 Expand and customize the **Advanced** settings, as described below.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Inputs                                                                        | Add inputs to dynamically configure a task. For details, see [Set input       |
|                                                                               | values dynamically in                                                         |
|                                                                               | tasks](https:                                                                 |
|                                                                               | //support.google.com/appsheet/answer/11445301#set-input-values-dynamically).  |
|                                                                               |                                                                               |
|                                                                               | 1.  Expand the **Advanced** section.                                          |
|                                                                               | 2.  Click **Add** under Inputs.                                               |
|                                                                               | 3.  Enter the name of the input value in the **Name** field.                  |
|                                                                               | 4.  Select the data type from the **Type** drop-down.\                        |
|                                                                               |     Only a subset of data types are supported for inputs.                     |
|                                                                               | 5.  To add an initial value or edit any fields:                               |
|                                                                               |     1.  Click  to open the Input dialog.                                      |
|                                                                               |     2.  Add a value or expression in the **Initial value** field.\            |
|                                                                               |         If you don't specify an initial value, then the input value will be   |
|                                                                               |         required. If an initial value is specified, then the input value is   |
|                                                                               |         optional.                                                             |
|                                                                               |         Use of `[_THIS]` or `[_INPUT]` are not supported in the Initial value |
|                                                                               |         field.                                                                |
|                                                                               |     3.  Edit other fields, as required.                                       |
|                                                                               |     4.  Click **Done**.                                                       |
|                                                                               | 6.  Repeat to add additional input values.                                    |
|                                                                               |                                                                               |
|                                                                               | Then, use the following expressions to access the input values from the       |
|                                                                               | current step: `[_INPUT].[`*`inputname`*`]`                                    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

## How AppSheet processes notifications

You control who receives a notification by specifying the email address of the recipients in the **To** property when configuring the Send a notification task (above).

AppSheet uses *Notification Device Tokens* to convert each email address in the **To** property into the appropriate Device Tokens for the user's mobile devices. If the user has more than one device, the notification is sent to each device that the user has logged in from.

AppSheet handles Notification Device Tokens slightly differently for [branded](https://support.google.com/appsheet/answer/10105390) applications (which are rare) versus non-branded applications.

Typically, the notification recipient must be an authenticated user who has logged in to at least one AppSheet application using the email address specified in the **To** property. The application that the user signed in to need not be the application sending the notification.

[Branded](https://support.google.com/appsheet/answer/10105390)  applications work slightly differently. When a user logs in to a branded application, the Notification Device Token that is created by the login contains the AppId of the branded application. This enables AppSheet to track which branded applications each user has logged in to and to send notifications appropriately.

For example, assume you have two branded applications called `AppA` and `AppB`. Assume you have two users `User1@gmail.com` and `User2@gmail.com`. Assume that `User1` has only logged in to application `AppA` and that `User2` has only logged in to application `AppB`. A notification that originates from application `AppA` might specify both `User1` and `User2` in the **To** property, but the notification will only be sent to `User1` because only that user has logged in to the branded application. No notification will be sent to `User2` because that user has not logged in to the branded application.

AppSheet sends notifications by performing the following tasks:

1.  Translates the user email address you specify in the **To** property into an AppSheet User Id. That AppSheet User Id will only exist if the *user has logged in to at least one AppSheet application* that requires user authentication using the user email address you specify in the **To** property. The AppSheet application that the user logged in to need not be the AppSheet application sending the notification.

2.  Translates the AppSheet User Id into a list of one or more Google Firebase Cloud Messaging Device Tokens. If the user has a mobile device and has logged in to at least one AppSheet application from that device, then AppSheet will have a unique Device Token registered for the device. AppSheet will send the notification to all of the recipient's registered Device Tokens.

3.  If AppSheet cannot find an AppSheet User Id for the user email address you specify in the **To** property or cannot find at least one Device Token for the AppSheet User Id, then the bot entry in the [Audit History](https://support.google.com/appsheet/answer/10104794) will report the following warning:

    `"Warning: No notification sent to 'someuser@somesite.com' because no Notification Device Token is present for this user."`
