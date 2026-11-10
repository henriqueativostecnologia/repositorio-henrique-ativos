---
fonte: https://support.google.com/appsheet/answer/14634161?hl=en
baixado: 2026-11-10
---

# Build an automation using Google Forms

You must be a **Google Workspace user** to build AppSheet automations with Google Forms. See [Add AppSheet to Google Workspace](https://support.google.com/a/answer/10447197).

If you are using your Google Workspace account, the [Google Workspace Terms of Service](https://workspace.google.com/terms/premier_terms/) govern your use of Google Forms. Otherwise, refer to the [Google Terms of Service](https://policies.google.com/terms).

Build an automation using Google Forms to trigger events based on a form response, as described in the following sections:

- [Get started](#get-started)
- [Steps to build automations using Google Forms](#steps)
- [How AppSheet stores responses from Forms](#forms-responses)

## Get started

To get started building automations with Google Forms, see [Quick start: Build your first app and automation using Google Forms](https://support.google.com/appsheet/answer/14714804).

## Steps to build automations using Google Forms

Build automations using Google Forms to trigger events based on a form submission by performing the following steps.

+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **\#**                                             | **Step**                                           | **Description**                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| 1                                                  | Create a form using Google Forms                   | Before you can build an automation, you must       |
|                                                    |                                                    | create a form using Google Forms. See [How to use  |
|                                                    |                                                    | Google                                             |
|                                                    |                                                    | Forms                                              |
|                                                    |                                                    | ](https://support.google.com/docs/answer/6281888). |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | **Notes**:                                         |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | -   By default, a form built using Google Forms    |
|                                                    |                                                    |     doesn't collect email addresses. This may be   |
|                                                    |                                                    |     suitable for surveys where anonymous feedback  |
|                                                    |                                                    |     is acceptable or preferred. For scenarios      |
|                                                    |                                                    |     where it is important to know the identity of  |
|                                                    |                                                    |     the user submitting the form, configure the    |
|                                                    |                                                    |     form to [collect respondents' email            |
|                                                    |                                                    |     addresses](htt                                 |
|                                                    |                                                    | ps://support.google.com/appsheet/answer/14915518). |
|                                                    |                                                    | -   For questions that allow file uploads, Google  |
|                                                    |                                                    |     Forms allows users to upload multiple files as |
|                                                    |                                                    |     the answer to a *single* question. AppSheet    |
|                                                    |                                                    |     doesn't support multiple uploaded files for a  |
|                                                    |                                                    |     single question and will save only the first   |
|                                                    |                                                    |     uploaded file (ignoring all other uploaded     |
|                                                    |                                                    |     files for that single question). To ensure     |
|                                                    |                                                    |     data consistency, we recommend                 |
|                                                    |                                                    |     allowing **one** file upload per question (the |
|                                                    |                                                    |     default) in a form being used with AppSheet.   |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| 2                                                  | Add the form to your app                           | Do one of the following:                           |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | -   [Add the                                       |
|                                                    |                                                    |     form](https://s                                |
|                                                    |                                                    | upport.google.com/appsheet/answer/10105821#add) to |
|                                                    |                                                    |     an existing app                                |
|                                                    |                                                    | -   Create an app from the form, as described      |
|                                                    |                                                    |     below.                                         |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | In each case, select **Google Forms** as the data  |
|                                                    |                                                    | source and then navigate to the form. See          |
|                                                    |                                                    | also [How AppSheet stores responses from Google    |
|                                                    |                                                    | Forms](#forms-responses).                          |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | To create an app from the form, do the following:  |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | 1.  Sign in                                        |
|                                                    |                                                    |     to [*AppSheet*](https://appsheet.com/)**.**\   |
|                                                    |                                                    |     The My Apps page is displayed.                 |
|                                                    |                                                    | 2.  Select **Create \> App \> Start with existing  |
|                                                    |                                                    |     data**.\                                       |
|                                                    |                                                    |     \                                              |
|                                                    |                                                    |     Create and app by starting with existing data\ |
|                                                    |                                                    |     \                                              |
|                                                    |                                                    |     The Create a new app dialog is displayed.      |
|                                                    |                                                    | 3.   Enter the name of the app and optionally      |
|                                                    |                                                    |     select a category.                             |
|                                                    |                                                    | 4.  Click **Choose your data**.\                   |
|                                                    |                                                    |     The Select data source dialog is displayed.    |
|                                                    |                                                    | 5.  Click **Google Forms**.\                       |
|                                                    |                                                    |     \                                              |
|                                                    |                                                    |     Select Google Forms as the data source\        |
|                                                    |                                                    |     \                                              |
|                                                    |                                                    |     The Select a file dialog is displayed.         |
|                                                    |                                                    | 6.  Navigate to the form and click **Select**.\    |
|                                                    |                                                    |     Your new app is created and opened in the      |
|                                                    |                                                    |     AppSheet app editor.                           |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| 3                                                  | Use the form responses to trigger an automation    | Build an automation and [add a Google Forms        |
|                                                    |                                                    | event](https://support.google.com                  |
|                                                    |                                                    | /appsheet/answer/11445188#configure-forms-event).  |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+

## How AppSheet stores responses from Google Forms

When you add a form from Google Forms to your app, AppSheet adds a **read-only** table to store the responses collected by the form. For example, the following shows the [Table settings](https://support.google.com/appsheet/answer/10105821#configure-table) for the read-only table that is used to store data collected by the Travel Request form.

Read-only table added by AppSheet to store Google Form responses

Because the read-only table is empty when you initially add the form, if you select to Send an email when you [configure a Google Forms event](https://support.google.com/appsheet/answer/11445188#forms-event), you won't be able to preview the email until at least one form response is submitted.
