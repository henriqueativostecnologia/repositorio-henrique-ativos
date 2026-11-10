---
fonte: https://support.google.com/appsheet/answer/14871588?hl=en
baixado: 2026-11-10
---

# Quick start: Build your first automation using an AppSheet database

In this Quick Start, you'll build your first automation using an AppSheet database. The automation sends an email notification to the assignee when a new task is added directly in the AppSheet database.

**Before you begin**: Complete the [Quick start: Build your first app using an AppSheet database](https://support.google.com/appsheet/answer/14009539).

------------------------------------------------------------------------

To create your first automation using an AppSheet databases, perform the following steps:

1.  Sign in to [*AppSheet*](https://appsheet.com/)**.**

2.  Open the **Tasks App** app in the app editor.
    You created the Tasks App app when completing the [Quick start: Build your first app using an AppSheet database](https://support.google.com/appsheet/answer/14009539).

3.  In the navigation pane of the app editor, click **Automation ** Automation icon **.**

    Go to Bots page

    The Bots pane is displayed.

4.  Click **+** in the top header of the Bots pane.

    Click + in the top header of the Bots pane

5.  In the Add a new bot dialog, click **Create a new bot**.

    A new empty bot is created and displayed in the center pane of the app editor.

6.  Edit the name of the bot.
    1.  Position your cursor over the New Bot in the left navigation pane.
    2.  Select **More  \> Rename**.

        Rename bot
         
    3.  Rename the bot to **Task complete** and press **Enter**.

7.   In the new bot flow in the center pane, click **Configure event.**

    Click Configure event in the center pane

8.  For Event name, enter **Task complete** and click **Create a custom event**.

    Task completed event

    The Settings pane opens in the right side of the app editor.

    You could also select the **Tasks column Task is changed** suggestion to automatically configure a portion of the event. But for the purposes of this tutorial you'll learn how to configure the event manually. For more information, see [Suggestions in the app editor](https://support.google.com/appsheet/answer/12849262).

9.  In the right pane, configure the event settings as follows:

    +-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Field**                                                                     | **Setting**                                                                   |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Event source                                                                  | Select **AppSheet database** in the drop-down.                                |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Table                                                                         | Select **Tasks** in the drop-down.                                            |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Data change type                                                              | Do the following:                                                             |
|                                                                               |                                                                               |
|                                                                               | -   Select **Updates**.                                                       |
|                                                                               | -   Deselect **Adds** and **Deletes**.                                        |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Columns to watch for update                                                   | Open the drop-down menu and do the following:                                 |
|                                                                               |                                                                               |
|                                                                               | 1.  Select **Status**.                                                        |
|                                                                               | 2.  Deselect **Task**.                                                        |
|                                                                               | 3.  Click **Select 1 column(s)**.                                             |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Condition                                                                     | Enter a condition value using the Expression Assistant:                       |
|                                                                               |                                                                               |
|                                                                               | 1.  Click in the **Condition** field.\                                        |
|                                                                               |     The Expression Assistant is displayed.                                    |
|                                                                               | 2.  Enter **\[Status\] = "Complete"** in the expression text box. \           |
|                                                                               |     \                                                                         |
|                                                                               |     Enter \[Status\]="Complete" in the Expression Assistant                   |
|                                                                               | 3.  Click **Save**.                                                           |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

    The Settings pane appear as follows:

    Event settings for AppSheet database event

10. In the bot flow in the center pane, click **+ Add a step**.

    Add a step to the bot

11. For Step name, enter **Email approver** and click **Create a custom step**.

    Enter Send an email and click Send an email under Suggestions

    The Email approver step is added, it is set to **Run a task** by default, and the configuration settings are displayed in the right pane.

12. In the right pane, configure the task, as follows:

    1.  Leave the task type set to **Send an email**.
    2.  For Email Type, click **Custom template**.
        Additional fields are displayed.
    3.  In the **Table nam**e drop-down, select **Tasks** (if it is not already selected).
    4.  In the **To** field, click **Add** and in the field that is displayed enter your email address (for testing).
    5.  In the **Email Subject** field, enter: **Task complete**
    6.  Leave the **Email Body** set to the default.

    The Settings pane appears as follows:

    Send an email task settings

13. Click **Save** to save the app.

    ****Save the app****

14.  The following warning message is displayed:

    Bot deployment warning indicating email will be delivered to app owner only

    You can ignore this message for now. All test messages will be sent to you as the app owner, so you don't need to deploy the app in order to test the automation.

    Next, you'll test your automation.

15. To test your automation:

    1.  In the navigation pane of the app editor, click **Data **.

        Click Data in the navigation pane to open the Data pane

        The Data pane is displayed.

    2.  Click **Tasks** in the Data pane.

        Click Tasks in the Data pane to view the Tasks table

    3.  In the table navigation bar, click **View data source**.

        The **My Project Tracker** is opened in the AppSheet database editor in a new browser tab. The Tasks table is selected by default.

    4.  In the **Write script** row, set the **Status** column to **Complete**.

        In Write script row, set Status to Complete

    5.  Check your email for a message titled **Task complete. **

------------------------------------------------------------------------

**Congratulations!** You have created your first AppSheet automation by using an AppSheet database. 

**What's next?** You can access more [quick starts](https://support.google.com/appsheet/answer/13474783) to learn about other AppSheet features.
