---
fonte: https://support.google.com/appsheet/answer/11511240?hl=en
baixado: 2026-11-10
---

# Send embedded app view email from an automation

Configure an automation bot to send an *embedded app view email* (or dynamic email) to one or more recipients based on an event, as described in the following sections:

- [What is an embedded app view email (dynamic email)?](#what-dynamic-email)
- [Get started with embedded app view email](#get-started)
- [Steps to send embedded app view email from a bot](#steps)
- [Create a view for the embedded app view email](#create)
- [Configure the embedded app view email](#configure)
- [Request a quota increase for cross-domain embedded app view emails](#quota-increase-cross-domain)
- [Current limitations with embedded app view email](#limitations)

See also [Troubleshoot embedded app view email](https://support.google.com/appsheet/answer/11541677).

## ****What is an embedded app view email (dynamic email)?

An embedded app view leverages [dynamic email in Gmail](https://developers.google.com/gmail/ampemail) (using [AMP](https://amp.dev/about/email/)) and enables users to interact directly with your app in the email rather than clicking out to view the AppSheet app in a separate window.

Here's a quick demo:

Video shows a dynamic email being sent to a user and the user interacting to approve the request.

For example, if an employee sends a request for a new chair (the event), you can configure the bot to send an email to their manager requesting approval before fulfilling the request.

With an embedded app view email, the manager can add notes and approve the request directly in the email, as shown in the following example:

Email showing an approval for a request being completed directly in the email

To view the embedded app view email content, email recipients must be app users. If there are multiple email recipients, emails are sent individually to each recipient from amp-noreply@appsheet.com.

Email recipients that interact with embedded app view email content are counted towards your app usage.

 

Embedded app view emails are interactive for 30 days. After 30 days, the embedded app view in the email will no longer render and users will have to navigate to the app to edit fields.

If the embedded app view content is out of date, recipients are notified and can click the **Refresh** button at any time to refresh the view, as shown below:

Warning message indicating the dynamic email is out of date with the Refresh button highlighted.

## Get started with embedded app views

Watch the following **introductory video** or read the **[blog](https://cloud.google.com/blog/products/no-code-development/using-appsheet-no-code-apps-in-gmail)** to learn more about embedded app view email (dynamic email) with AppSheet.

**Note**: The concepts in this video are still valid, though the AppSheet app editor UI has changed since it was recorded.

Video: https://www.youtube.com/watch?v=pVQlS0PliSQ

Get started with embedded app view email using the **sample app**:

- Try out the [Task Manager app](https://www.appsheet.com/start/f44209e4-cc1d-4abd-9718-22269c9db1de).
  Click **New Task** to add and save a task. You will receive an embedded app view email in your Gmail inbox where you can directly update the task status.
- To see how the embedded app view email task is created, check out the [sample app](https://www.appsheet.com/samples/Track-onetime-and-recurring-tasks-on-mobile-or-desktop?appGuidString=f6979af1-94b7-4f0d-920e-9f66f7edb196).

## ****Steps to send an embedded app view from a bot

**Before you begin**: Review [current limitations with embedded app view email](#limitations).

To send an embedded app view from a bot, perform the following steps:

1.  [Create a view for the embedded app view email](#create).
2.  [Configure the embedded app view email](#configure).

See also [Troubleshoot embedded app view email](https://support.google.com/appsheet/answer/11541677).

## ****Create a view for the embedded app view email

To enable users to interact directly with the content in the email message, you can add editable fields to the view that you use in the Send an email task.

The following views are supported for use with embedded app view email:

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **View**                                                                      | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Detail](https://support.google.com/appsheet/answer/10106385)                 | Displays and enables you to edit details for the current record.              |
|                                                                               |                                                                               |
|                                                                               | To add editable fields to your Detail view, add one or more **Quick edit      |
|                                                                               | columns**. For details, see [Quick                                            |
|                                                                               | Edit](https://support.google.com/appsheet/answer/10106609).                   |
|                                                                               |                                                                               |
|                                                                               | Each editable field is validated and saved as you move focus, and may trigger |
|                                                                               | another bot.                                                                  |
|                                                                               |                                                                               |
|                                                                               | **Supported data column types**                                               |
|                                                                               |                                                                               |
|                                                                               | A subset of data column types are not currently supported for use with        |
|                                                                               | embedded app view email, such as File or Image column types. For the complete |
|                                                                               | list of data column types that are **not supported** with embedded app view   |
|                                                                               | email, see [Current limitations with embedded app view email](#limitations).  |
|                                                                               |                                                                               |
|                                                                               | **Supported configuration properties**                                        |
|                                                                               |                                                                               |
|                                                                               | The following Detail view configuration properties are supported for use in   |
|                                                                               | embedded app view email:                                                      |
|                                                                               |                                                                               |
|                                                                               | -   Main image                                                                |
|                                                                               | -   Header columns                                                            |
|                                                                               | -   Quick edit columns                                                        |
|                                                                               | -   Column order                                                              |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Form](https://support.google.com/appsheet/answer/10107846)                   | Captures input from users. All fields provided in the Form view are editable  |
|                                                                               | in the embedded app view email and validated when the user submits the form.  |
|                                                                               |                                                                               |
|                                                                               | **Supported configuration property**                                          |
|                                                                               |                                                                               |
|                                                                               | The following Form view configuration property is supported for use in        |
|                                                                               | embedded app view email: **Column order**                                     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

## ****Configure the embedded app view email

Add and configure the **Send an email** task by performing the following steps:

1.  Add the **Send an email** task to a bot, as described in [Add a task to a bot](https://support.google.com/appsheet/answer/11445301#add-task).

2.  Configure the **Send an email** task by using the settings described in the tables below.

3.  When you are done, save the app by selecting one of the following:

    - **Save** - Save the app.
    - **Save & verify data** - Save the app and verify that it is runnable based on external dependencies.

4.  To preview the embedded app view email, click **Preview email body**.
    The first record in the table is displayed, by default.You need to save the app to preview the latest changes.

After you save the app, you can reuse the task in other bots.

Configure the **Send an email** task by using the settings described in the following tables.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Linking                                                                       |                                                                               |
|                                                                               |                                                                               |
|                                                                               |  Enable or disable reuse of this component by expanding the **Linking** panel |
|                                                                               | and toggling the **Linking** setting. See [Reuse automation                   |
|                                                                               | components](https://support.google.com/appsheet/answer/12193489).\            |
|                                                                               | \                                                                             |
|                                                                               | Expand the Linking panel and toggle the Linking setting to enable or disable  |
|                                                                               | component reuse                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Task name                                                                     | Name of the task. It must be unique within your app.                          |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Email Type                                                                    | [Email type](https://support.google.com/appsheet/answer/11447614#email-type). |
|                                                                               | Click **Embedded app view**.                                                  |
|                                                                               |                                                                               |
|                                                                               | **Note**: To configure a **Custom template** email, see [Send an email from   |
|                                                                               | an automation](https://support.google.com/appsheet/answer/11447614).          |
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
| To                                                                            | List of email recipients.                                                     |
|                                                                               |                                                                               |
|                                                                               | Enter an email address or an expression using the Expression Assistant. Click |
|                                                                               | **Add** to add additional email recipients.                                   |
|                                                                               |                                                                               |
|                                                                               | See [Add email                                                                |
|                                                                               | recipien                                                                      |
|                                                                               | ts](https://support.google.com/appsheet/answer/11447614#add-email-recipients) |
|                                                                               | for more information.                                                         |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Email Subject                                                                 | Subject of the email.                                                         |
|                                                                               |                                                                               |
|                                                                               | Specify text,                                                                 |
|                                                                               | [variables](https://support.google.com/appsheet/answer/11539253), and         |
|                                                                               | [expressions](https://support.google.com/appsheet/answer/10104642). For       |
|                                                                               | example:                                                                      |
|                                                                               |                                                                               |
|                                                                               | -   `Thank you for your order!`                                               |
|                                                                               | -   `Thanks <<[CustomerName]>> for your order!`                               |
|                                                                               | -   `Thanks <<[Custom                                                         |
|                                                                               | erName]>> for your order on <<TODAY()>> which will arrive on <<TODAY() + 7>>` |
|                                                                               |                                                                               |
|                                                                               | By default, a meaningful email subject is suggested.                          |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Email Body                                                                    | Body of the email.                                                            |
|                                                                               |                                                                               |
|                                                                               | Enter the email body, including text, images,                                 |
|                                                                               | [variables](https://support.google.com/appsheet/answer/11539253), and         |
|                                                                               | [expressions](https://support.google.com/appsheet/answer/10104642).           |
|                                                                               |                                                                               |
|                                                                               | By default, the Email Body includes data values from the added or updated     |
|                                                                               | row, excluding `Hidden` or `Show` type columns.                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| App view to embed in email body                                               | View to embed in the email body for Embedded app view emails. Select the      |
|                                                                               | Detail or Form view from the drop-down list. See [Create a view for the       |
|                                                                               | embedded app view email](#create-view).                                       |
|                                                                               |                                                                               |
|                                                                               | Only Detail and Form views will be displayed in the list. If you select a     |
|                                                                               | view that contains a configuration property or data column type for an        |
|                                                                               | editable field that is not supported for embedded app view email, a warning   |
|                                                                               | is displayed in the editor. For more information, see [Current limitations    |
|                                                                               | with embedded app view email](#limitations).                                  |
|                                                                               |                                                                               |
|                                                                               | **Note**: If you add a view to an embedded app view email and subsequently    |
|                                                                               | edit the view, the embedded app view email is refreshed in the recipients'    |
|                                                                               | Gmail inbox. However, if you include configuration properties or data column  |
|                                                                               | types that are not supported for embedded app view email, an error message is |
|                                                                               | displayed to current email recipients and in the AppSheet Admin UI to         |
|                                                                               | indicate that the embedded app view email task configuration is no longer     |
|                                                                               | valid.                                                                        |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

### Advanced settings

Expand and customize the **Advanced** settings for embedded app emails, as described below.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Customize "From" name                                                         | Customize the email address displayed in the `From` field of the email. By    |
|                                                                               | default, the app creator is used (for example, `appcreator@gmail.com`).       |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Email Footer                                                                  | Content that appears at the bottom of the email. For example:                 |
|                                                                               |                                                                               |
|                                                                               | `This email is from Simple Invento                                            |
|                                                                               | ry Manager. Our address is Company XYZ, 1354 Wallaby Way Cleveland, OH 46753` |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

## Request a quota increase for cross-domain embedded app view emails

Embedded app view emails that are sent to recipients that are not in the app creator's domain are called *cross-domain* embedded app view emails. This domain is based on the default email connected to your account.

Each app creator can send up to 50 cross-domain embedded app view emails per day. After this daily quota is met:

- Your Send an email task will no longer send embedded app view emails to recipients outside of your domain.
- If you have a public domain linked to your account (for example, `@gmail.com`), after the quota is met you will no longer be able to send embedded app view emails at all.
- If you are using a non-public domain (that is, not `@gmail.com`), embedded app view emails will continue to send for *in-domain* recipients.

The following table summarizes the behavior when using different types of email domains.

|                                           |                                                                                         |                                                                |
|-------------------------------------------|-----------------------------------------------------------------------------------------|----------------------------------------------------------------|
| **Type of email domain**                  | **In-domain emails**                                                                    | **Cross-domain emails**                                        |
| Non-public domain (custom domain)         | Embedded app view emails are sent regardless of quota                                   | Embedded app view emails are not sent after daily quota is met |
| Public domain (for example, `@gmail.com`) | N/A (all embedded app view emails sent from public domains are considered cross-domain) | Embedded app view emails are not sent after daily quota is met |

 

If you wish to request a quota increase for your daily cross-domain embedded app view emails, contact our support team through the [support form](https://www.appsheet.com/Support/Contact) and provide the following information:

- Short description of your use case.
- How many cross-domain embedded app view emails will you be sending per day? (An estimate is fine.)
- How many different domains will you be sending embedded app view emails to? (Provide a list.)

## ****Current limitations with embedded app view email

The following table summarizes the current limitations with embedded app view email.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Feature limitation**                                                        | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Mail client (Gmail only)                                                      | Embedded app view email is supported with **Google Gmail clients only**. If   |
|                                                                               | accessed using another client, the recipient will need to navigate to the app |
|                                                                               | to edit the contents.                                                         |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Maximum email size limit                                                      | Embedded app view email supports a maximum email size limit of 200 KB. If the |
|                                                                               | maximum size limit is exceeded, the embedded app view email will render as a  |
|                                                                               | static email.                                                                 |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| View types (Detail, Form)                                                     | The following views are supported in embedded app view email:                 |
|                                                                               |                                                                               |
|                                                                               | -   Detail view                                                               |
|                                                                               | -   Form view                                                                 |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Detail view limitations                                                       | The following Detail view configuration properties are supported for use in   |
|                                                                               | embedded app view email:                                                      |
|                                                                               |                                                                               |
|                                                                               | -   Main image                                                                |
|                                                                               | -   Header columns                                                            |
|                                                                               | -   Quick edit columns                                                        |
|                                                                               | -   Column order                                                              |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Form view configuration properties                                            | The following Form view configuration property is supported for use in        |
|                                                                               | embedded app view email: **Column order**                                     |
|                                                                               |                                                                               |
|                                                                               | In addition to setting the order of columns, **Column order** enables you to  |
|                                                                               | filter out unsupported column types for embedded app view email without       |
|                                                                               | having to create a slice.                                                     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Column type limitations                                                       | The following data column types are **not supported** as editable fields in   |
|                                                                               | an embedded app view email:                                                   |
|                                                                               |                                                                               |
|                                                                               | -   `ChangeCounter`                                                           |
|                                                                               | -   `ChangeLocation`                                                          |
|                                                                               | -   `ChangeTimestamp`                                                         |
|                                                                               | -   `Color`                                                                   |
|                                                                               | -   `Drawing`                                                                 |
|                                                                               | -   `File`                                                                    |
|                                                                               | -   `Image`                                                                   |
|                                                                               | -   `Price`                                                                   |
|                                                                               | -   `Progress`                                                                |
|                                                                               | -   `Show`                                                                    |
|                                                                               | -   `Signature`                                                               |
|                                                                               |                                                                               |
|                                                                               | In addition, `LongText` fields are rendered as `Text` fields in an embedded   |
|                                                                               | app view email.                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Show column types                                                             | Show column types are supported in embedded app view email. However, setting  |
|                                                                               | the `Video` category will display a **Play video** button, rather than        |
|                                                                               | embedding the video directly in the email.\                                   |
|                                                                               | \                                                                             |
|                                                                               | See [Customize input                                                          |
|                                                                               | forms](https://support.google.com/appsheet/answer/10106787) for more          |
|                                                                               | information about using Show column types.                                    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Action limitations                                                            | Currently only the following action types are supported:                      |
|                                                                               |                                                                               |
|                                                                               | -   Data: set the values of some columns in this row                          |
|                                                                               | -   Data: add a new row to another table using values from this row           |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Navigation to other views using actions (not supported)                       | Navigating to other views using actions from an embedded app view email is    |
|                                                                               | not yet supported.                                                            |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `CONTEXT("``View")` and `CONTEXT("``ViewType")` \                             | `CONTEXT("``View")` and `CONTEXT("``ViewType")` functions are not supported   |
| functions (not supported)                                                     | for embedded app view emails. The server is unaware of the view currently     |
|                                                                               | visible to the user, so cannot provide the view name or type.                 |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Sending embedded app view emails to Google Groups                             | Sending embedded app view email to Google Groups is not currently supported.  |
|                                                                               | If you include a Google Group as a recipient on an embedded app view email,   |
|                                                                               | the dynamic portion of the email will not render and users will have to click |
|                                                                               | a link to navigate to the app to view and edit fields.                        |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Forwarding embedded app view emails                                           | If you forward an embedded app view email, the dynamic portion of the email   |
|                                                                               | will no longer render and users will have to click a link to navigate to the  |
|                                                                               | app to view and edit fields.                                                  |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Time limitation (30 days)                                                     | Embedded app view email are interactive for 30 days. After 30 days, the       |
|                                                                               | embedded app view in the email will no longer render and users will have to   |
|                                                                               | click a link to navigate to the app to view and edit fields.                  |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
