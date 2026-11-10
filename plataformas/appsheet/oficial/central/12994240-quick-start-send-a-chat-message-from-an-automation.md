---
fonte: https://support.google.com/appsheet/answer/12994240?hl=en
baixado: 2026-11-10
---

# Quick start: Send a Chat message from an automation

In this Quick Start, you'll send a Chat message that alerts you when inventory for an item falls below a threshold, as shown:

Simple inventory sample app inventory alert as a Chat message

This quick start builds on [Quick start: Create your first Chat app with AppSheet](https://support.google.com/appsheet/answer/12923581). 

------------------------------------------------------------------------

To send a Chat message from an automation:

1.  First, you need to create a Chat app. Follow the steps in [Quick start: Create your first Chat app with AppSheet](https://support.google.com/appsheet/answer/12923581) to create a Chat app using Simple inventory sample app.

2.  If you selected [manual configuration](https://support.google.com/appsheet/answer/12849362#manual-configuration) to configure you Chat app, to support asynchronous interactions with your Chat app when sending Chat messages from an automation:
    If you selected [automatic configuration](https://support.google.com/appsheet/answer/12849362#automatic-configuration) to configure you Chat app, you can skip this step.

    1.  In the app editor, expand the **Grant IAM access to run automations** section on the Chat Setup page.
    2.  Click **[Google Cloud Console \> IAM & Admin \> IAM](https://pantheon.corp.google.com/iam-admin/iam)** to open the IAM & Admin page in the Google Cloud Console.
    3.  Click **Grant access**.
        The Grant access panel displays.
    4.  In the app editor, copy the **New principal**.
    5.  In the console, paste it in the** New principals** field in the **Add principals** section.
    6.  In the console, select **Service Usage Consumer** in the **Role** drop-down in the **Assign roles** section.
    7.  Click **Save**.

3.  Return to the app editor and go to **Automation \> Bots**.
    The bot named **When stock available of an item is below threshold, send an email** is selected and displayed by default. You'll modify this bot to also send a Chat message.

4.  In the process flow, click **+ Add a step**.

    Click Add a step in the process flow
     

5.  Select **Run a task** in the drop-down.

6.  Change the Step name to **Send a Chat message**.

7.  Under **Task Settings**, select **Send a chat message**.

8.  Configure the Chat message as follows:

    |                             |                                                                                                                                                                                              |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Setting**                 | ** Description**                                                                                                                                                                             |
| Table name                  | Leave set to **Inventory.**                                                                                                                                                                  |
| Message Content             | Select **Select chat spaces** in the drop-down.                                                                                                                                              |
| Space ID(s)                 | Click **Add** and select the Chat space you to which you added the Chat app in [Quick start: Create your first Chat app with AppSheet](https://support.google.com/appsheet/answer/12923581). |
| Message Text                | Set to: **\<\<\_APPNAME\>\> ALERT - \<\<\[Item ID\].\[Name\]\>\> inventory is below threshold**                                                                                              |
| Send an app view (optional) | Select **Inventory_Detail**.                                                                                                                                                                 |

9.   Save the app by selecting one of the following options:
    - **Save** - Save the app.
    - **Save & verify data** - Save the app and verify that it is runnable based on external dependencies.

10. Go to the Chat space and enter **/**,** **select **/inventory-form** in the list, and press **Enter**.

11. Click **Open in app**. 

12. Select **Saw** and set the **Amount** to any value, such as **-83**.
    You can leave the DateTime field set to the default.

    Enter inventory log
     

13. Click **Save**.

14. Return to the Chat space and notice that the inventory alert message is displayed with the **Inventory_Detail** chat card showing the details for the item.

    Simple inventory sample app inventory alert as a Chat message

**Congratulations!** You have successfully created your first Chat message from an automation with AppSheet!
