---
fonte: https://support.google.com/appsheet/answer/15733195?hl=en
baixado: 2026-11-10
---

# Quick start: Build your automation using Gmail

This is a **beta** release of building automations using Gmail events. See [Track and manage feature releases](https://support.google.com/a/topic/1227580). Preview offerings are intended for use in test environments only. This feature is not recommended for use in production apps. For questions or assistance with this feature, contact [AppSheet Support](https://www.appsheet.com/Support/Contact).

You must be a **Google Workspace user** to build AppSheet automations with Gmail. See [Add AppSheet to Google Workspace](https://support.google.com/a/answer/10447197).

If you are using your Google Workspace account, the [Google Workspace Terms of Service](https://workspace.google.com/terms/premier_terms/) govern your use of Gmail. Otherwise, refer to the [Google Terms of Service](https://policies.google.com/terms).

In this Quick start, you'll build a new automation flow that is triggered when a label is manually added to an email. You'll then save content from the email message to a table in your app.

------------------------------------------------------------------------

To create your first automation using Gmail, perform the following steps:

1.  [Create an app from a template](#create-app-from-template).
2.  [Build an automation based on a Gmail event](#add-gmail-event).
3.  [Test your automation](#test-automation).

## Create an app from a template

To create an app from the IT Ticketing template, do the following:

1.  Open the [Project Tracker](https://www.appsheet.com/templates/Track-project-tasks-or-issues-in-a-kanban-dashboard?appGuidString=535cf3aa-c081-47f6-a027-a24d2602c26a) template.

2.  Click **Copy and Customize**.
    The Clone your app dialog opens.

3.  Click **Copy app**.
    Your app is created from the template and opened in the app editor. By default, the Learning Center is displayed.

4.  Go to **Data ** .
    The Data pane is displayed and the first table in the primary navigation is opened in the editor.

    Project Tracker data pane

    Notice that there are four tables, `Notes`, `People`, `Tracker`, and `Workstreams`. The `Tracker` table has table slices defined to access workstreams based on the status of the project.

5.  Click **View data source** in the top navigation to open the Google Sheet data source used by the app.

    Select View data source

The Tracker Sheet is opened in a separate tab. Leave the spreadsheet open -- you'll refer back to it later when testing your automation.

Tracker Google Sheet

Next you'll add a Gmail event automation that triggers an automation when a label is added to a project email message in your Gmail. You'll then capture the project information from the email message in the `Tracker` spreadsheet.

## Build an automation based on a Gmail event 

To build an automation based on a Gmail event:

1.  Return to the AppSheet editor tab.
2.  Go to **Automation** Automation icon ** \> Bots.**

    Select Automation \> Bots

    Currently, the app has an automation defined to send an email to task owners for incomplete tasks that are due today. The bot shows a warning because the app isn't deployed. This message can be ignored for now. 
3.  Click **+** in the top header of the Bots panel.

    Create a new bot

    The Add a new bot dialog is opened.
4.  In the Add a new bot dialog, click **Create a new bot**.

    Create a new bot

    A new empty bot is created and displayed in the center pane of the app editor.
5.  To edit the name of the bot, do the following:
    1.  Position your cursor over the New Bot in the left navigation pane.
    2.  Select **More ******** \> Rename**.

        Rename bot
    3.  Replace the text with **Urgent project** and press **Enter**.
6.  In the new bot flow in the center pane, click **Configure event**.

    Click Configure event
7.  For event name, enter **Urgent project received** and click **Create a new event**.

    Enter Urgent project received and click Create a new event

    The Settings pane opens in the right side of the app editor.
8.  In the Settings pane, configure the event as follows: 
    1.  In the Event source drop-down, select **Gmail (Beta)**.
    2.  To connect your Gmail account as a data source, click **Authorize.**
        The Add a new data source dialog displays.
    3.  Click **Gmail (beta)**.

        Add a new data source Gmail

        The Choose an account dialog displays.
    4.  Click your Gmail account and then respond to the remaining prompts to add your Gmail account as a data source and connect it to the app. 
    5.  In the **Gmail account** drop-down, select the account you just added.
    6.  In the **Label to watch** drop-down, select **Starred**.
        **Note**: For simplicity, you're using one of the default Gmail labels. Typically, you'll create a custom label for use with your automation. See [Create labels to organize Gmail](https://support.google.com/mail/answer/118708) and [Create rules to filter your emails](https://support.google.com/mail/answer/6579).
    7.  Select the following trigger actions:
        - **Added label to email**
        - **Removed label from email**
9.  In the bot flow in the center pane, click **+ Add a step**.

    Click Add a step
10. In the **Step name** field, enter **Save project details** and click **Create a new step**.

    Enter Save project details for step name and click Create a new step
11. Click the **Save project details** step in the center pane and select **Run a data action** in the drop-down.

    Run a data action

    The Settings pane is updated.
12. In the Settings pane, configure the step as follows:
    1.  Leave **Add new rows** selected as the data action.

    2.  In the **Add row to this table** drop-down, select **Tracker**.
        You'll add a new row to the Tracker spreadsheet using the values defined in the next step.

    3.  Under **With these values**, follow these steps to add the following values:

        +-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Value**                                                                     | **Steps**                                                                     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Workstream                                                                    | 1.  Select **Workstream** in the drop-down.                                   |
|                                                                               | 2.  Click in the value field to open the Expression Assistant.                |
|                                                                               | 3.  In the expression text box, enter: **"0.3399913417"**\                    |
|                                                                               |     Include the surrounding quotes. This ID corresponds to the ProjectA       |
|                                                                               |     workstream in the `Workstreams` spreadsheet. Let's assume that this       |
|                                                                               |     workstream tracks urgent projects.                                        |
|                                                                               | 4.  Click **Save**.\                                                          |
|                                                                               |     The Expression Assistant is closed.                                       |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Task                                                                          | 1.  Click **Add**.                                                            |
|                                                                               | 2.  Select **Task** in the drop-down.                                         |
|                                                                               | 3.  Click in the value field to open the Expression Assistant.                |
|                                                                               | 4.  Click the **Examples** tab and then click **Columns**.                    |
|                                                                               | 5.  Locate the row with **\[Subject\]** in the **Example** column and click   |
|                                                                               |     **Insert**.\                                                              |
|                                                                               |     \                                                                         |
|                                                                               |     Insert \[Subject\] column in Expression Assistant by clicking Insert      |
|                                                                               | 6.  Click **Save**.\                                                          |
|                                                                               |     The Expression Assistant is closed.                                       |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Description                                                                   | 1.  Click **Add**.                                                            |
|                                                                               | 2.  Select **Description** in the drop-down.                                  |
|                                                                               | 3.  Click in the value field to open the Expression Assistant.                |
|                                                                               | 4.  In the Examples tab, click **Columns**.                                   |
|                                                                               | 5.  Locate the row with **\[Body\]** in the **Example** column and click      |
|                                                                               |     **Insert**.                                                               |
|                                                                               | 6.  Click **Save**.                                                           |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Owner                                                                         | 1.  Click **Add**.                                                            |
|                                                                               | 2.  Select **Owner** in the drop-down.                                        |
|                                                                               | 3.  Click in the value field to open the Expression Assistant.                |
|                                                                               | 4.  In the text box, enter: **"IT@company.com"**\                             |
|                                                                               |     Include the surrounding quotes.                                           |
|                                                                               | 5.  Click **Save**.                                                           |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Due                                                                           | 1.  Click **Add**.                                                            |
|                                                                               | 2.  Select **Due** in the drop-down.                                          |
|                                                                               | 3.  Click in the value field to open the Expression Assistant.                |
|                                                                               | 4.  In the text box, enter: **TODAY()+1**\                                    |
|                                                                               |     Due to its urgent nature, you're indicating that the project needs to be  |
|                                                                               |     resolved in 24 hours.                                                     |
|                                                                               | 5.  Click **Save**.                                                           |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Status                                                                        | 1.  Click **Add**.                                                            |
|                                                                               | 2.  Select **Status** from the drop-down.                                     |
|                                                                               | 3.  Click in the value field to open the Expression Assistant.                |
|                                                                               | 4.  In the text box, enter: **"Not Started"**\                                |
|                                                                               |     Include the surrounding quotes and match the capitalization.              |
|                                                                               | 5.  Click **Save.**                                                           |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

      The Settings pane appears as follows:

    Settings pane for add new row
13. Click **Save** to save the app.

    ****Save the app****

Next, you'll test your automation.

## Test your automation

To test the automation:

1.  Go to your [Gmail](https://mail.google.com) account.
2.  Compose an email with the following content and send it to the yourself:
    - Email Subject: **Issue \#5555555**
    - Email body: **Monitor removal from conference room C**
3.  Check your inbox for the message.
4.  Click the **star** icon adjacent to the message to trigger the automation.

    Star email to trigger Gmail event
5.  Navigate back to the browser tab with the **Tracker** sheet.
6.  Make sure that the Tracker spreadsheet tab is selected and confirm that a new row has been added to track the project:

------------------------------------------------------------------------

**Congratulations!** You have built your first app and automation using Gmail. 

**What's next?** You can access more [quick starts](https://support.google.com/appsheet/answer/13474783) to learn about other AppSheet features.
