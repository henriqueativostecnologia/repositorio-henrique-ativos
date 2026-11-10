---
fonte: https://support.google.com/appsheet/answer/12008558?hl=en
baixado: 2026-11-10
---

# Use the AppSheet Apps Script Examples Project

## **Quick start**

 Copy the sample project as a starting point for your own Apps Script project.

1.  Open the sample project:

    [Open Sample Project](https://script.google.com/home/projects/17PLdwaMChT9-TSRUgZFAh28bd3ZYLyHsGRp59zDS_HzpRpaHFEztEPHl)
     
2.  Copy the project. 

## **What does this sample project do?**

This project has many different functions to help you get started, you can modify and mix-and-match these depending on your workflow.

|                         |                                                                             |
|-------------------------|-----------------------------------------------------------------------------|
| **Function Name**       | **Description**                                                             |
| `sayHello`              | Logs a message to the console                                               |
| `createCalendarEvent`   | Adds an event to the default calendar with the provided start and end times |
| `createDoc`             | Creates a Google Doc                                                        |
| `createSheet`           | Creates a Google Sheet                                                      |
| `createSlideDeck`       | Creates a Google Slide                                                      |
| `shareFile`             | Shares a Google Drive file with an email                                    |
| `sendAnEmail`           | Sends an email                                                              |
| `createAndSendDocument` | Creates a Google Doc and send an email with it as an attachment             |

### How to test from Apps Script

You can test executing the function from the Apps Script by clicking **Run** or **Debug** at the top of the editor:

Run and debug in Apps Script editor

Since it runs the function without setting arguments, you'll need to add default arguments. For example, instead of `function sayHello(msg)` change it to be `function sayHello(msg="Test message")`.

The first time you do this, you'll need to authorize scopes the script needs. 

## **Next steps**

After you have it set up, you can follow the instructions in [Call Apps Script from automation](https://support.google.com/appsheet/answer/11997142) to set up the task and bot inside AppSheet.

## **See also**

- [Call Apps Script from an automation](https://support.google.com/appsheet/answer/11997142)
- [Apps Script API Documentation](https://developers.google.com/apps-script/reference)
- [Use Apps Script to create a calendar event](https://support.google.com/appsheet/answer/12007551)
- [Use Apps Script to send an interactive chat message](https://support.google.com/appsheet/answer/12007046)
