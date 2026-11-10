---
fonte: https://support.google.com/appsheet/answer/12981549?hl=en
baixado: 2026-11-10
---

# Send a Chat message from an automation

Configure an automation bot to send a Chat message to one or more Chat spaces based on an event by using the **Send a Chat message** task.

For example, if an employee sends a request for a new chair (the event), you can configure the bot to send a Chat message to their manager requesting approval before fulfilling the request.

Before you can build automations for your Chat apps, you must [Configure your Chat app with AppSheet](https://support.google.com/appsheet/answer/12849362), including [granting IAM access to run automations](https://support.google.com/appsheet/answer/12849362#set-iam-policy-for-async-messages) if you selected [manual configuration](https://support.google.com/appsheet/answer/12849362#manual-configuration) to configure you Chat app.

Add and configure the **Send a Chat message** task by performing the following steps: 

1.  Add the **Send a Chat message **task to a bot, as described in [Add a task to a bot](https://support.google.com/appsheet/answer/11445301#add-task).
2.  Configure the **Send a Chat message **task by using the settings described in the table below.
3.  When you are done, save the app by selecting one of the following:
    - **Save** - Save the app.
    - **Save & verify data** - Save the app and verify that it is runnable based on external dependencies.

Configure the **Send a Chat message** task by using the settings described in the following table.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Linking                                                                       | Enable or disable reuse of this component by expanding the **Linking** panel  |
|                                                                               | and toggling the **Linking** setting. See [Reuse automation                   |
|                                                                               | components](https://support.google.com/appsheet/answer/12193489).\            |
|                                                                               | \                                                                             |
|                                                                               | Expand the Linking panel and toggle the Linking setting to enable or disable  |
|                                                                               | component reuse                                                               |
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
| Message content                                                               | Select one of the following in the drop-down:                                 |
|                                                                               |                                                                               |
|                                                                               | -   **Select chat spaces** to explicitly select the Chat spaces, group Chats, |
|                                                                               |     or direct messages (using the Space IDs field) to which you want to send  |
|                                                                               |     the Chat message.                                                         |
|                                                                               | -   **Respond to same thread** to respond to the originating Chat space       |
|                                                                               |     thread.                                                                   |
|                                                                               |                                                                               |
|                                                                               | **Note**: If you select **Respond to same thread**:                           |
|                                                                               |                                                                               |
|                                                                               | -   For the parent process, don't set linking on. The originating Chat space  |
|                                                                               |     thread can't be identified when the process is used by multiple bots.     |
|                                                                               |     See [Reuse automation                                                     |
|                                                                               |     components](https://support.google.com/appsheet/answer/12193489).         |
|                                                                               | -   The parent event must be a Chat event. See [Configure Chat                |
|                                                                               |     event                                                                     |
|                                                                               | s](https://support.google.com/appsheet/answer/11445188#configure-chat-event). |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Space IDs                                                                     | **Note**: This setting is available if you choose **Select chat spaces** in   |
|                                                                               | the Message content drop-down.                                                |
|                                                                               |                                                                               |
|                                                                               | Specify the IDs for the Chat spaces, group Chats, or direct messages to which |
|                                                                               | you want to send the Chat message. Click **Add** and select an item from the  |
|                                                                               | drop-down list. Repeat to add additional IDs.                                 |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Message text                                                                  | Chat message text. Specify text,                                              |
|                                                                               | [variables](https://support.google.com/appsheet/answer/11539253), and         |
|                                                                               | [expressions](https://support.google.com/appsheet/answer/10104642).           |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Send an app view (optional)                                                   | Optionally, you can send an app view to the Chat space as a [Chat             |
|                                                                               | card](https://developers.google.com/chat/api/guides/message-formats/cards).   |
|                                                                               |                                                                               |
|                                                                               | **Note**: For preview, only deck and detail views are supported from Send a   |
|                                                                               | Chat message tasks. For more information, see [Supported view types and       |
|                                                                               | settings                                                                      |
|                                                                               | ](https://support.google.com/appsheet/answer/14102086#supported-view-types).  |
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
