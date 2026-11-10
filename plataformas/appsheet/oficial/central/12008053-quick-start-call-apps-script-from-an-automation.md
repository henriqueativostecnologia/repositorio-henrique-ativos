---
fonte: https://support.google.com/appsheet/answer/12008053?hl=en
baixado: 2026-11-10
---

# Quick start: Call Apps Script from an automation

In this Quick Start, you'll copy the AppSheet Apps Script Examples project that contains a simple "hello world" script to log a message to the Apps Script execution log. Then you'll call that script from an AppSheet automation and confirm its execution.

**To copy the AppSheet Apps Script Examples project:**

1.  Open the AppSheet Apps Script Examples project:

    [Open Project](https://script.google.com/home/projects/17PLdwaMChT9-TSRUgZFAh28bd3ZYLyHsGRp59zDS_HzpRpaHFEztEPHl)

2.  Click **Copy** to make a copy of the project.
    This copies the project to the root folder in My Drive by default.

3.  Rename the project to **AppSheet Apps Script Example** (or a name of your choosing).

    You'll call the `sayHello()` function that is defined in this project from your AppSheet app to log a message to the Apps Script execution log:

    `function sayHello(msg) {`
        `Logger.log('AppSheet says ' + msg);`
    `}`

For more information about this project, see [Use the AppSheet Apps Script Examples Project](https://support.google.com/appsheet/answer/12008558).

### To call the Apps Script from an automation:

1.  Make a copy of the [Shirt Orders Example](https://docs.google.com/spreadsheets/d/1dXt2AGJnfsty9mhfGws2JQ3IBQF0qifFvGpILjcTv3A/copy) spreadsheet.
    Click **Make a copy** to download and open a copy of the spreadsheet in Google Sheets.

2.  Rename the spreadsheet, if desired. For example, to: **Shirt Orders.**

3.  Sign in to [AppSheet](http://appsheet.com/).

4.  On the My apps page, click **Create \> App \> Start with existing data**.
    The Create a new app dialog displays.

5.  Optionally, edit the app name and select a category.

6.  Click **Choose your data**

7.  Click **Google Sheets** to access your Google Drive.

8.  Navigate to and select the **Shirt Orders** spreadsheet that you copied in Step 1.

9.  Click **Select**.
    AppSheet sets up your app.

10. Click **Customize your app** to open the app in the AppSheet editor.

11. Click **Automation ** Automation icon and click **+** in the Bots heading.
    We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

    ## If you are using the legacy editor

    Click **Automation \> Bots** and click **+ New Bot**

12. Select the following item in the list of suggestions: 
    **When a Shirt Orders record is created or updated, send a notification**

13. Click the **Send a notification** step to edit it.

14. Change the name to **Call a script**.

    Rename task to Call a script

15. Under **Task Settings** in the right pane, change the task type to **Call a script**.

16. In the **Apps Script Project** field:

    1.  Click **Browse** (File icon).

    2.  Navigate to and select the **AppSheet Apps Script Examples** project in your Drive.

    3.  Click **Select**.

    4.  If prompted to authorize, click **Authorize** and follow the prompts.
        **Note**: You'll only need to authorize the first time you access the project.

        If prompted, click Authorize and follow prompts to authorize access to the project

        The Apps Script Project is added and the **Function Name** field is populated with a drop-down list of available functions from the project

17. Select **sayHello(msg)** from the **Function Name** drop-down.

    Select sayHello(msg) from the Function Name drop-down

    The **Function Parameters** field is displayed.

18. For the **msg** argument, enter the following expression using Expression Assistant:
    **'Hello from AppSheet'**

    For the msg argument, enter 'Hello from AppSheet' using the Expression Assistant

19. Click **Save** to save the app.

20. In the right pane, click the **mobile** or **tablet** icon to display the app emulator.

    Click mobile app or tablet to preview app

21. Add a new shirt order and click **Save**.

22. Click **Sync** to sync your changes.

    Sync your changes

### **To confirm the execution of Apps Script:**

1.  Return to the Apps Script home page and view the **AppSheet Apps Script Examples** project.

2.  Click **Executions** in the left navigation bar to confirm that **sayHello()** function was successfully completed. You may have to click **Refresh** if the log has not appeared.

Validate successful execution of the sayHello() function on the Executions page
