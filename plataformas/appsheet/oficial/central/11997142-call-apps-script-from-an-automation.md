---
fonte: https://support.google.com/appsheet/answer/11997142?hl=en
baixado: 2026-11-10
---

# Call Apps Script from an automation

Call Apps Script from an automation as described in the following sections:

- [Overview](#overview)
- [Get started calling Apps Script from an automation](#get-started)
- [Create an Apps Script project](#create-apps-script-project)
- [Add and configure the "Call a script" task in a bot](#add-task)
- [Share an Apps Script project](#share)
- [Manage Apps Script projects in your account](#manage)
- [Quotas and limitations](#quotas-limitations)

## ****Overview

Apps Script is a cloud-based JavaScript platform that lets you integrate with and automate tasks across Google products. With Apps Script, you write code in modern JavaScript and have access to built-in libraries for Google Workspace applications.

You can use custom logic from within your AppSheet app by calling [Apps Script](https://developers.google.com/apps-script) from an AppSheet automation bot.

Examples of custom logic that you can implement include:

- Create a calendar appointment when a button is clicked
- Add a slide to a presentation when a new row is added
- Save photos to Drive and share with specific individuals when uploaded using a form
- Create an audit log by generating a Google Docs file with data from a table
- Call an external service for machine learning prediction using data from a newly added row and write back model prediction

**Notes**:

- The Apps Script service must be enabled in your organization to call Apps Script from an automation. See [Turn Apps Script on or off for users](https://support.google.com/a?p=apps_script_on_off). Otherwise, you'll receive a message similar to the following:

  `We are sorry, but you do not have access to Google Apps Script. Please contact your Organization Administrator for access`

- Apps Script always executes the [head deployment](https://developers.google.com/apps-script/concepts/deployments#head_deployments) regardless of the deployed versions. You can't designate a different version to be called by the task.

- AppSheet supports only [standalone scripts](https://developers.google.com/apps-script/guides/standalone). It does not support [container-bound scripts](https://developers.google.com/apps-script/guides/bound) at this time.

**New to Apps Script?** See [Google Apps Script overview](https://developers.google.com/apps-script/overview).
**New to AppSheet Automation?** See [AppSheet Automation: The Essentials](https://support.google.com/appsheet/answer/11431791).

## ****Get started calling Apps Script from an automation

Get started calling Apps Script from an automation.

- Watch an introductory video on calling Apps Script from an automation.

  **Note**: The concepts in this video are still valid, though the AppSheet app editor UI has changed since it was recorded.

  Video: https://www.youtube.com/watch?v=-0ETflTeIO0

- Walk through the [quick start](https://support.google.com/appsheet/answer/12008053) to call a simple "hello world" script from an AppSheet automation and confirm its execution.

- Use Apps Script samples
  - [Use the AppSheet Apps Script Examples Project ](https://support.google.com/appsheet/answer/12008558)
  - [Use Apps Script to create a calendar event](https://support.google.com/appsheet/answer/12007551)
  - [Use Apps Script to send an interactive chat message](https://support.google.com/appsheet/answer/12007046)

## ****Create an Apps Script project

First, you must create an Apps Script project for your script files and related resources. An Apps Script project includes:

- One or more script files (`.gs`) to define your custom integrations
- Optionally, HTML files, that might include JavaScript and CSS, to create custom templates and layouts

Create an Apps Script

To create an Apps Script project:

1.  From the [Apps Script home page](https://script.google.com/) you can:

    - Create a new Apps Script project, as described in [Create and delete projects](https://developers.google.com/apps-script/guides/projects#create_and_delete_projects).

    - Copy an existing Apps Script project:

      1.  Open the Apps Script project editor.

      2.  Click **Overview** in the left sidebar and click **Make a copy** (copy icon) in the right side of the page.

2.  Add one or more scripts to the project or modify the existing scripts. For examples, see [Use the AppSheet Apps Script Examples project](https://support.google.com/appsheet/answer/12008558).

## ****Add and configure the "Call a script" task in a bot

Add and configure the **Call a script** task in a bot by performing the following steps.

For more information about adding and configuring tasks in an automation bot, see [Tasks: The Essentials](https://support.google.com/appsheet/answer/11445301).

1.  Add the **Call a script** task to a bot, as described in [Add a task to a bot](https://support.google.com/appsheet/answer/11445301#add-task).
2.  [Configure the "Call a script" task](#configure-task).
3.  Click **Authorize** to authorize the Apps Script project to run.
    **Note**: You'll need to authorize the first time you access the project and anytime authentication scopes are added. As indicated, the script will always run as the app owner regardless of the account used to authorize the project.
4.  Select the Apps Script function that you want to call in the **Function Name** drop-down.

    The list is populated using the functions defined by the Apps Script project selected in the previous step. After you select the function, the list of associated arguments is displayed. 
5.  Enter an expression that defines each argument that will be passed to the function in the **Function Parameters** field. For example:
    For the msg argument, enter 'Hello from AppSheet' using the Expression Assistant
6.  Optionally, enable the **Return Value** option to use the return value from the Apps Script function. See [Use return values from Apps Script tasks](https://support.google.com/appsheet/answer/12309564) for more information.
7.  Optionally, enable the **Run asynchronously?** option to run the Apps Script task asynchronously as a background task. Enabling this option can improve client response time.

    Before setting this option, consider whether your application requires the Apps Script to complete synchronously to execute correctly. For example, if your Apps Script is changing data and your application relies on that data being updated before the sync completes, then using an asynchronous call may yield incorrect results.
8.  When you are done, save the task by selecting one of the following:
    - **Save** - Save the app.
    - **Save & verify data** - Save the app and verify that it is runnable based on external dependencies.

### Configure the "Call a script" task

Configure the Call a script task by using the settings in the following table.

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
| Task name                                                                     | Name of the task that appears in the automation process flow. It must be      |
|                                                                               | unique within your app.                                                       |
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
| Apps Script Project                                                           | Apps Script project that contains the function you want to call. To populate  |
|                                                                               | the field:                                                                    |
|                                                                               |                                                                               |
|                                                                               | 1.  Click **Browse** (File icon).                                             |
|                                                                               | 2.  Click **Files on Google Drive**.                                          |
|                                                                               | 3.  Navigate to the Apps Script project in your Drive. See [Create an Apps    |
|                                                                               |     Script project](#create-apps-script-project).                             |
|                                                                               | 4.  Click **Select**.                                                         |
|                                                                               |                                                                               |
|                                                                               | Click **Open Project** to open the project, if desired.                       |
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

## ****Share an Apps Script project

Share your Apps Script project by sharing it directly or using a [shared drive](https://developers.google.com/drive/api/v3/about-shareddrives). For details, see [Collaborating with other developers](https://developers.google.com/apps-script/guides/collaborating).

## ****Manage Apps Script projects in your AppSheet account

The following sections describe how to manage Apps Script projects in your AppSheet account:

- [View Apps Script projects in your AppSheet account](#view-projects)
- [Add an Apps Script project to your AppSheet account](#add-project)
- [Remove an Apps Script project from your AppSheet account](#remove-project)

### View Apps Script projects in your AppSheet account

To view Apps Script projects in your AppSheet account:

1.  Sign in to [AppSheet](http://www.appsheet.com/).
2.  Go to the **My account** page.
3.  **Select Integrations \> Apps Scripts**.

The Apps Script projects are displayed, as follows:

View Apps Script projects in your account on the Integrations \> Apps Script pane

### Add an Apps Script project to your AppSheet account

When you [add and configure a Call a script task](#add-task), the Apps Script project is added to your account automatically.

### Remove an Apps Script project from your AppSheet account

Remove access to an Apps Script project from your AppSheet user or team account so that it is no longer available for use by other apps.

**Note**: Before removing an Apps Script project from your AppSheet account, you should delete all references to the Apps Script project in your apps to avoid errors. If you removed a project from the **My Account** page, and want to add the project back to your account, select the script again from within the [“Call a script” flow](#configure-task).

To remove an App Script to your user or team account:

1.  Sign in to [AppSheet](http://www.appsheet.com/).
2.  Go to the **My account** page.
3.  Select **Integrations \> Apps Scripts**.
4.  Click **Delete** (Trash icon) to delete access to a particular script.

## ****Quotas and limitations

- Apps Script executions are subject to standard Google Workspace quotas and limitations as stated in [Quotas for Google Services](https://developers.google.com/apps-script/guides/services/quotas).
- Apps Script tasks will be available for users in the AppSheet Core plan and above. See [AppSheet pricing plans](https://solutions.appsheet.com/pricing).
