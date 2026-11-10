---
fonte: https://support.google.com/appsheet/answer/13380741?hl=en
baixado: 2026-11-10
---

# Customize Chat apps

When [configuring Chat apps with AppSheet](https://support.google.com/appsheet/answer/12849362), you can customize the following features in your Chat app:

- [First message](#default-menu) including the Chat app menu that displays when the Chat app is installed or mentioned in a Google Chat space
- [Search command](#search-command) that enables Chat app users to search your Chat app views using simple phrases
  (only available when you [use automatic configuration](https://support.google.com/appsheet/answer/12849362#automatic-configuration))
- [Chat app actions](#customize-chat-app-actions) that provide more ways to interact with your Chat app

## Customize the first message

When installed or @mentioned in a Google Chat space, the Chat app displays a menu that, by default, provides access to the primary menu views. You can customize the message and views that are displayed in the Chat card menu.

The following provides an example of the first message displayed for a Chat app:

Chat app menu

 

If a view is not supported for Chat apps with AppSheet, app users are prompted to open the web version in a new window, as shown for the My Team view in the above illustration.

To customize the first message:

1.  In the app editor, expand the **Customize** section on the Chat Setup page.
2.  Click **First message**.
3.  Edit the message text, as desired.
4.  Under **App views sent as a Chat card menu**, define the views to include, as follows:
    - Click **Add view** to add a view to the menu
    - Click  to delete a view
    - Press and hold the handle  and drag to reorder a view

At least one view is required. If you delete all views, AppSheet restores the default menu (all primary menu views).

## Customize the search command

**Note**: The search command is only available when you [use automatic configuration](https://support.google.com/appsheet/answer/12849362#automatic-configuration).

AppSheet provides a built-in `/search` command that enables users to search for Chat app views using simple terms or phrases, such as: `/search request`

By default, the search command is turned on. To turn off the search command, in the **Search** command section, select More ** \> Disable**.

## Customize Chat app actions

Optionally, you can customize Chat app actions to provide more ways to interact with your Chat app. A Chat app action can be:

- **An action in Google Chat**
  That can be triggered by one of the following:
  - **Slash command**
    A slash command allows users to access specific features of your Chat app. Any slash commands you’ve added will appear in Chat, so it’s easy for users to learn what they can do. Type **/** (slash) in the Chat conversation to display the slash commands that are available along with a short description.

    Slash commands in Approvals app

    For example, you can define slash commands that:

    - Open a Chat app view. For example, entering /form opens a form view in Chat.
    - Trigger an [automation](https://support.google.com/appsheet/answer/11445188#configure-chat-event) process. For example, entering /updaterequest sends a status update request to all project stakeholders.
       

    Slash commands are not required, but strongly encouraged. If not set, users will be able to access app views through the Chat app's initial message

  - **Chat app added to a space**
    For example, when a user adds your Chat app to a Space, send a welcome message with instructions about how to use the app. 

  - **Chat app removed from a space**
    For example, when a user removes your Chat app from a Space, send a message to the project stakeholders. 

&nbsp;

- **An action outside of Google Chat**
  For example, a change occurred to a connected data source or a date is reached. You can send a Chat message:
  - When something changes in a connected data source, for example a new item was added to a column name
  - On a particular schedule, for example once a week on Monday mornings
  - When a specific date is reached, for example when a project due date is reached
  - When a condition is met, for example when inventory data hasn't been updated for more than 7 days

[Create](#create-chat-app-actions) and [configure](#configure-chat-app-actions) Chat app actions as described in the following sections.

You can configure your Chat app with as many actions as you’d like – or not to use them at all. If you don’t configure any Chat app actions, your Chat app will still be able to send a welcome card when added to a Chat or space.

Simple inventory Chat app interface

### Create Chat app actions** **

Create Chat app actions from scratch or by starting with one of the *recipe* templates that are available for commonly used Chat actions. 

**Note:** Recipe templates for Chat app actions will require additional configuration to meet the requirements of your particular use case.

To create Chat app actions:

1.  In the app editor, expand the **Customize** section on the Chat Setup page.

2.  Click **+ Add an action **and select one of the following recipe templates or **[Build my own](#build-my-own-chat-app-action)...** in the drop-down to build a Chat app action from scratch. 
     

    |                                                                      |                                                                                                                           |
|----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| **Recipe template**                                                  | **Description**                                                                                                           |
| [Slash command: Open app view](#slash-command-open-app-in-view)      | Use a slash command to open an [existing app view](https://support.google.com/appsheet/answer/10106688) in  a Chat space. |
| [Slash command: Run an automation](#slash-command-run-an-automation) | Use a slash command to trigger a bot configured as a Chat event.                                                          |
| [Message when data changes](#message-when-data-changes)              | Send a message when data changes in your Chat app.                                                                        |
| [Message on a schedule](#message-on-a-schedule)                      | Send a message on a specific schedule.                                                                                    |
| [Message when added to space](#message-when-added-to-space)          | Send a message when your Chat app is added to a space                                                                     |
| [Message when removed from space](#message-when-removed-from-space)  | Send a message when your Chat app is removed from a space.                                                                |

3.  After selecting the recipe template or Build my own, [*configure the Chat app action*.](#configure-chat-app-actions) 

4.  Click one of the following:
    - **Next** to proceed to [*configure the Google Chat API*](#configure-chat-api)
    - **+ Add an action** to add another Chat app action

### Configure Chat app actions

Configure the Chat app action to meet the requirements of your particular use case, as described in the following sections.

#### Slash command: Open app in view

To configure a slash command to open an app view in the Chat space:

1.  When [*creating a Chat app action*](#create-chat-app-actions), select the **Slash command: Open app in view** recipe template. This recipe template provides quick access to Chat app views without the use of the clickable menu.
2.  Configure the following fields in the **New Slash command: Open app view** dialog. All fields are required. 
    1.  Select the Chat app view to return using the slash command in the **App View** drop-down.

    2.  Enter a name for the slash command in the **Name** field.
        Include the slash in the name. For example: /command
        **Note**: The name is case-insensitive.

    3.  Enter a description of the slash command in the **Description** field. This information is displayed to users when they type **/** in the Chat conversation.
3.  Click one of the following:
    - **Next** to proceed to the next configuration step
    - **+ New action** to add another Chat app action

#### Slash command: Run an automation

To configure a slash command to run an automation:

1.  When [*creating a Chat app action*](#create-chat-app-actions), select the **Slash command: Run an automation** recipe template in the drop-down.
    A bot is created and configured as a **Chat event** that is triggered by a slash command
2.  [*Configure the Chat event*](https://support.google.com/appsheet/answer/11445188#configure-chat-event).
3.  [*Configure the process*](https://support.google.com/appsheet/answer/11445386) to run when the event is triggered.
4.  Click to return to the Chat apps setup page.
5.  Click one of the following:
    - **Next** to proceed to the next configuration step
    - **+ New action** to add another Chat app action

#### Message when data changes

To send a Chat message when data changes:

1.  When [*creating a Chat app action*](#create-chat-app-actions), select the **Message when data changes** recipe template in the drop-down.
    A bot is created and configured as a **Data Change event** that is triggered by any data changes. 
2.  Configure the [*data change event*](https://support.google.com/appsheet/answer/11445188#configure-data-change-event) and [*Chat message*](https://support.google.com/appsheet/answer/12981549).
3.  Click to return to the Chat apps setup page.
4.  Click one of the following:
    - **Next** to proceed to the next configuration step
    - **+ New action** to add another Chat app action

#### Message on a schedule

To send a message on a schedule

1.  When [*creating a Chat app action*](#create-chat-app-actions), select the **Message on a schedule** recipe template in the drop-down.
    A bot is created and configured as a **Schedule event**. By default, it is scheduled to occur monthly on the first day of the month at noon.
2.  Configure the [*scheduled event*](https://support.google.com/appsheet/answer/11445188?hl=en&ref_topic=11998887#configure-scheduled-event) and [*Chat message*](https://support.google.com/appsheet/answer/12981549).
3.  Click to return to the Chat apps setup page.
4.  Click one of the following:
    - **Next** to proceed to the next configuration step
    - **+ New action** to add another Chat app action

#### Message when added to space

To send a Chat message when your Chat app is added to a space:

1.  When [*creating a Chat app action*](#create-chat-app-actions), select the **Message when added to a space** recipe template in the drop-down.
    A bot is created and configured as a **Chat event** that is triggered when the Chat app is added to the Chat space.
2.  Configure the [*Chat event*](https://support.google.com/appsheet/answer/11445188#configure-chat-event) and [*Chat message*](https://support.google.com/appsheet/answer/12981549).
3.  Click to return to the Chat apps setup page.
4.  Click one of the following:
    - **Next** to proceed to the next configuration step
    - **+ New action** to add another Chat app action

#### Message when removed from a space

To send a message when your Chat app is removed from a space:

1.  When [*creating a Chat app action*](#create-chat-app-actions), select the **Message when removed from a space** recipe template in the drop-down.
    A bot is created and configured as a **Chat event** that is triggered when the Chat app is removed from the Chat space, and opened in the bot editor.
2.  Configure the [*Chat event*](https://support.google.com/appsheet/answer/11445188#configure-chat-event) and [*Chat message*](https://support.google.com/appsheet/answer/12981549).
3.  Click to return to the Chat apps setup page.
4.  Click one of the following:
    - **Next** to proceed to the next configuration step
    - **+ New action** to add another Chat app action

#### Build your own Chat app action

To build your own Chat app action:

1.  When [*creating a Chat app action*](#create-chat-app-actions), select the **Build my own…**.
    The Bots page opens.
2.  [*Add and configure a bot*](https://support.google.com/appsheet/answer/11432969#add-bot).
3.  Return to the Chat apps setup page.
4.  Click one of the following:
    - **Next** to proceed to the next configuration step
    - **+ New action** to add another Chat app action
