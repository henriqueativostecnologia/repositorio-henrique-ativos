---
fonte: https://support.google.com/appsheet/answer/14714804?hl=en
baixado: 2026-11-10
---

# Quick start: Build your first app and automation using Google Forms

You must be a **Google Workspace user** to build AppSheet automations with Google Forms. See [Add AppSheet to Google Workspace](https://support.google.com/a/answer/10447197).

If you are using your Google Workspace account, the [Google Workspace Terms of Service](https://workspace.google.com/terms/premier_terms/) govern your use of Google Forms. Otherwise, refer to the [Google Terms of Service](https://policies.google.com/terms).

 In this Quick start, you'll build your first app using [Google Forms](https://support.google.com/docs/topic/9055404) that is based on a travel request approval workflow. You'll create an app using a form from Google Forms and build a new automation flow that sends an email notification when a form response is received requesting approval for business travel.

------------------------------------------------------------------------

To create your first automation using Google Forms, perform the following steps:

1.  [Create a form using Google Forms](#create-form).
2.  [Create an app using the form](#create-app).
3.  [Build an automation using the form](#build-automation).
4.  [Test the automation](#test).

## Create a form using Google Forms

Create a simple form using Google Forms. See [How to use Google Forms](https://support.google.com/docs/answer/6281888). 

For example, in this quick start we use the following **Travel Request** form. But you don't have to match this exactly.

Travel request form

In the next step, you'll create an app using the form you just created.

## Create an app using the form

To create an app using the Travel Request form:

1.  Sign in to [*AppSheet*](https://appsheet.com/)**.**
    The My Apps page is displayed.
2.  Select **Create \> App \> Start with existing data**.

    Create and app by starting with existing data

    The Create a new app dialog is displayed.
3.  For App name, enter **Travel Approval** and click **Choose your data**.

    In the Create new app dialog, enter Travel Approval click Choose your data

    The Select data source dialog is displayed.
4.  Click **Google Forms**.

    Select Google Forms as the data source

    The Select a file dialog is displayed.
5.  Navigate to the **Travel Request** form and click **Select**.
    Your new Travel Approval app is created and opened in the AppSheet app editor. The Learning Center is displayed, by default.
     
    If the Try it out! dialog is displayed, click **Customize with AppSheet** to close it.
6.  In the app editor, click **Data ** in the left navigation bar.

    Go to Data in the app editor

    When you create an app using a form from Google Forms, AppSheet adds a **read-only** table, in this case Travel Request, to store the responses collected by the form, as shown:
     
    Your table content might vary; the table columns are based on your form's fields.
7.  Travel request table

In the next step, you'll build an automation using the Travel Request form from Google Forms.

## Build an automation using the form

In this step, you'll build an automation using the form that triggers the travel request approval flow. Specifically, you'll learn how to create a bot that sends an email to the approver. 

To build an automation using the Travel Request form:

1.   In the app editor, go to **Automation** Automation icon **.**

    Select Automation \> Bots in the left navigation

2.  Click **+** in the top header of the Bots pane.

    Click + to add a bot

3.  In the Add a new bot dialog, click **Create a new bot**.

    Add a new bot

    A new empty bot is created and displayed in the center pane of the app editor.

4.  Edit the name of the bot.
    1.  Position your cursor over the New Bot in the left navigation pane.
    2.  Select **More  \> Rename**.

        Rename bot
         
    3.  Rename the bot to **Travel request approval** and press **Enter**.

5.  In the new bot flow in the center pane, click **Configure event.**

    Configure event in new bot

6.  For Event name, enter **Travel request form submitted** and click **Create a custom event**.

    Create a custom event

    The Settings pane opens in the right side of the app editor.

    You could also select **A new form resonse is submitted to Travel Request** in the list of suggestions to automatically configure a portion of the event. But for the purposes of this tutorial you'll learn how to configure the event manually. For more information, see [Suggestions in the app editor](https://support.google.com/appsheet/answer/12849262).

7.  Configure the event as follows:
    - In the Event source drop-down, select **Forms**.
      New response is selected automatically.
    - For **Form**, select **Travel Request** in the drop-down (it should already be selected).

    The Settings appear as follows:

    Event configuration settings

8.  In the bot flow in the center pane, click **+ Add a step**.

    Add a step to the bot

9.  For Step name, enter **Email approver** and click **Create a custom step**.

    Enter Send an email and click Send an email under Suggestions

    The Email approver task is added and the configuration settings are displayed in the right pane.

10. Edit the task configuration settings in the right pane, as follows:
    1.  Leave the task type set to **Send an email**.
    2.  For Email Type, click **Custom template.**
    3.  Note, the Table is set to **Travel Request**.
    4.  In the **To** field, click **Add** and enter your email address (for testing).
    5.  In the **Email Subject** field, enter: **Travel request to \<\<\[Destination\]\>\> by \<\<\[Name\]\>\>**
        The `<<[Destination]>>` and `<<[Name]>>` are variables that refer to column data stored in the table from the requester's response.
    6.  Leave the Email Body field set to the default content. 
        By default, the Email Body includes data values from the requester's response (the added row).

    The Settings appear as follows:

11. Click **Save** to save the app.

    **Save the app**

 The following warning message is displayed:

Bot deployment warning indicating email will be delivered to app owner only

You can ignore this message for now. All test messages will be sent to you as the app owner, so you don't need to deploy the app in order to test the automation.

Next, you'll test your automation.

## Test the automation

To test the automation:

1.  Send the Travel Request form to yourself and submit a response. 
2.  Check your email for a message titled **Travel request to *destination* by *name***, where *destination* matches the destination and *name* matches the name specified in the submitted form.

------------------------------------------------------------------------

**Congratulations!** You have built your first app and automation using Google Forms. 

**What's next?** You can access more [quick starts](https://support.google.com/appsheet/answer/13474783) to learn about other AppSheet features.
