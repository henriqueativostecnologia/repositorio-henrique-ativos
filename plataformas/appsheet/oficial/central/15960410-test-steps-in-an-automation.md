---
fonte: https://support.google.com/appsheet/answer/15960410?hl=en
baixado: 2026-11-10
---

# Test steps in an automation

Test a step in an automation to validate the expected results.

At this time, you can only test **AI task** steps in an automation (preview). See [Use AI in automations](https://support.google.com/appsheet/answer/16045284).

Testing a step:

- Won't impact any data in the data source. This is true even if **Save to table** is turned on for the output in the task.
- Counts towards the [automation limits](https://support.google.com/appsheet/answer/11828262).

Reusable (linkable) steps must be tested within the context of the automation.  

To test a step in an AI task automation, do the following:

1.  Open the app in the app editor.

2.  Go to **Automation ** Automation icon **  \> Bots**.

3.  Select the bot automation in the left pane.

4.  Select the AI task step that you want to test in the center pane.

5.  Make sure that you save all changes to the bot before testing steps.

6.  Click  Test step icon  in the top of the right pane or in the step in the center pane.

    Test icon in right pane of automation

    The Test step pane displays.

7.  By default, the extracted column values for the first row of the associated table are displayed. To select a different row of data to test:
    1.  Click **Select row**.
        The Select row for test input displays. Up to the last 500 rows in the data source are available for selection.
    2.  Select a different row of values to test.
    3.  Click **Refresh data** to ensure you are accessing the latest data.
    4.  Click **Apply**.

8.  Click **Run test** to run a test on the selected row.

9.  View and evaluate the results in the **Results** section.

    One of the following results will be returned:

    |            |                                                                |
|------------|----------------------------------------------------------------|
| **Result** | **Next steps**                                                 |
| Done       | Review the results returned to ensure they match expectations. |
| Error      | Follow the guidance provided to correct the error.             |

10. Optionally, modify the AI task configuration or update the data, save your app, and click **Run test again**.

11. Repeat steps to test other rows.
