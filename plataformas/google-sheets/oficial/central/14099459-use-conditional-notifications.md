---
fonte: https://support.google.com/docs/answer/14099459?hl=en
baixado: 2026-11-10
---

# Use conditional notifications

You can create rules to send email notifications when a cell changes in Google Sheets.

- You can select which cell value changes trigger these notifications.
- You can select which email addresses will receive a notification.
- The notification will be sent on the behalf of the user who set up or last edited the rule.

## Set up conditional notifications

You can set up rules in Google Sheets that will send email notifications when cell values change in a custom range or column.

**Important:** Conditional notifications are only available to certain work or school accounts. Currently, this feature doesn't support group email addresses and non-Google recipients, like Outlook and Yahoo. If you can't find the option to use Conditional notifications, [contact your administrator](https://support.google.com/a/answer/6208960).

1.  On your computer, open a spreadsheet in [Google Sheets](http://sheets.google.com/).
2.  At the top, click **Tools** and then **Conditional notifications**.
    - **Tip:** Right-click in any cell to access the Conditional notifications directly from the cell.
3.  Click **Add rule**.
4.  \[Optional\] To name the rule, type in the name in the text editor.
5.  \[Optional\] Under “In this table,” select the table.
6.  Under “In this column,” select a column or a custom range.
7.  \[Optional\] To set additional criteria on your rule, click **Add condition**.
    - For example, to create a rule that sends a notification when a cell value changes to “Completed,” select **Text is exactly** and enter “Completed” in the text box.

      **Tip:** You can also select a different column or range for your condition. The notification is sent only when both the rule trigger and condition are met.
8.  To add the email addresses to send notifications to, under “Then take the following action,” select an option:
    - **Manually type each email**, then in the text box below, enter names or email addresses.

    - **Choose a column with emails**, then select the column that contains email addresses or people.

      **Tips:**

      - If you select a custom range for the rule, the size of the email range must be the same as the size of the custom range with cell value changes. For example, if you select a single cell for cell value changes, you must also select a single cell for the email range.
      - You can only add individual Gmail or workspace emails.

Example of rule set up and notification:

1.  You have a tracker for “Event planning,” and you set up a conditional notification to notify people in column “Assignee“ when the “Status” column value changes. Select the following under **Add rules:**
    - For when cell value changes, select the “Status” column.

    - For email recipients, select a column with emails.

    - To send an email notification, select the “Assignee” column.

      Event planning tracker
2.  The recipients (in the “Assignee” column, in this example) receive a notification. Based on the recipient's access level to the spreadsheet, the notification email may include:
    - First row value of the trigger column plus adjacent cells
    - Cell value that changed plus adjacent cells
    - Name of the user who made the change
    - Previous value and new value
    - Range that triggered the notifications and adjacent columns

**Tip:** Email notifications may not be immediate and multiple changes may be consolidated into one email.

## Find the trigger history

After triggering conditions are met, the trigger history will record its status. Trigger history will be available for 30 days.

- Successful runs: The rule was triggered but the notification may not be sent immediately or at all if changes were undone
- Failed and partial runs: Indicate issues with the notification process.

To find the last 30 days of your spreadsheet’s conditional notification history:

1.  On your spreadsheet, click **Tools** and then **Conditional notifications**.
2.  Click **View trigger history**.

To troubleshoot, you can filter by rule name or status.

#### Notifications may not trigger as expected when:

- **Value format changes:** This includes changes to decimal points (e.g., from 2.5 to 2.50).
- **External data changes:** If your data comes from outside sources, like [Connected Sheets or other documents](https://support.google.com/a/answer/9604541), changes there won't trigger notifications. For example, if you have a column that links to another file column (with the IMPORTRANGE formula).
- **Volatile functions are used:** These functions recalculate with any worksheet change, potentially causing notifications to miss updates that happen while the document is closed. For example, if you have a cell with a TODAY() formula (e.g. =TODAY()+1)), and the value changes while you have the document closed, the notification will not trigger.

## Unsubscribe from Conditional notifications

To unsubscribe from conditional notifications for a specific spreadsheet:

1.  You can go to:
    - The footer of the email notification: Click **Change what Google sends you**.
    - The spreadsheet: Click **Tools** and then **Notification settings** and then **Conditional notifications**.
2.  Under “Conditional notifications,” select **None**.

**Tip:** To report the spreadsheet as abusive in the notification email you receive, click **Report**.

## Related resource

- [Manage your notifications](https://support.google.com/docs/answer/91588)
