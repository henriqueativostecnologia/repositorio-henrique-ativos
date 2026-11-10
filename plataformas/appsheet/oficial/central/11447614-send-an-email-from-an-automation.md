---
fonte: https://support.google.com/appsheet/answer/11447614?hl=en
baixado: 2026-11-10
---

# Send an email from an automation

Configure an automation bot to send an email to one or more recipients based on an event by using the **Send an email** task.

For example, if an employee sends a request for a new chair (the event), you can configure the bot to send an email to their manager requesting approval before fulfilling the request.

To send an email from a bot, add and configure the **Send an email** task based on the email type, as described in the following sections:

- [Email types](#email-type)
- [Add and configure the Send an email task](#add-configure-task)
- [Add email recipients](#add-email-recipients)
- [Examples of sending an email from an automation](#examples)
- [Prevent app creators from adding email attachments in automations](#prevent-email-attachments)

See also [Tasks: The Essentials](https://support.google.com/appsheet/answer/11445301).

## Email types

There are currently two types of emails that you can configure:

|                             |                                                                                                                                                                                                                                                                                                                                                          |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Email type**              | **Description**                                                                                                                                                                                                                                                                                                                                          |
| Embedded app view (dynamic) | Embedded app view emails enable you to embed supported app views within an email and allow Gmail recipients to interact directly with your app from within the email, without leaving their inbox. To configure an embedded app view email, see [Send embedded app view emails from an automation](https://support.google.com/appsheet/answer/11511240). |
| Custom template             | Custom template emails allow you to configure emails with text, HTML, or variables from app data. Configuration details are provided below.                                                                                                                                                                                                              |

## ****Add and configure the Send an email task

Add and configure the **Send an email** task by performing the following steps:

1.  Add the **Send an email** task to a bot, as described in [Add a task to a bot](https://support.google.com/appsheet/answer/11445301#add-task).

2.  Configure the **Send an email** task by using the settings described in the tables below.

3.  When you are done, save the app by selecting one of the following:

    - **Save** - Save the app.
    - **Save & verify data** - Save the app and verify that it is runnable based on external dependencies.

4.  To preview the email, click **Preview email**.
    The first record in the table is displayed, by default. You need to save the app to preview the latest changes.

After you save the app, you can reuse the task in other bots.

Configure the **Send an email** task by using the settings described in the following tables.

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
| Task name                                                                     | Name of the task. It must be unique within your app.                          |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Email Type                                                                    | [Email type](#email-type). Click **Custom template**.                         |
|                                                                               |                                                                               |
|                                                                               | **Note**: To configure an Embedded app view email,  see [Send embedded app    |
|                                                                               | view emails from an                                                           |
|                                                                               | automation](https://support.google.com/appsheet/answer/11511240).             |
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
| To                                                                            | List of email recipients. Defaults to the app owner's email address.          |
|                                                                               |                                                                               |
|                                                                               | Enter an email address or an expression using the Expression Assistant. Click |
|                                                                               | **Add** to add additional email recipients.                                   |
|                                                                               |                                                                               |
|                                                                               | See [Add email recipients](#add-email-recipients) for more information.       |
|                                                                               |                                                                               |
|                                                                               | **Note**: When using AppSheet with a free account, you can only send email to |
|                                                                               | the app owner's email address.                                                |
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
|                                                                               | To define the email body, do **one** of the following:                        |
|                                                                               |                                                                               |
|                                                                               | -   Enter the email body, including text, images,                             |
|                                                                               |     [variables](https://support.google.com/appsheet/answer/11539253), and     |
|                                                                               |     [expressions](https://support.google.com/appsheet/answer/10104642).       |
|                                                                               | -   Leave this setting blank and specify an **Email Body Template** (see      |
|                                                                               |     below).                                                                   |
|                                                                               | -   Leave this setting and **Email Body Template** blank to use the default   |
|                                                                               |     content.                                                                  |
|                                                                               |                                                                               |
|                                                                               | **Note**: The **Email** **Body Template** setting (if specified) takes        |
|                                                                               | precedence over this setting.                                                 |
|                                                                               |                                                                               |
|                                                                               | By default, the Email Body includes data values from the added or updated     |
|                                                                               | row, excluding `Hidden` or `Show` type columns.                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

### Other email parameters

Expand and customize the **Advanced** settings, as described below.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| CC                                                                            | List of email recipients to carbon copy (CC).                                 |
|                                                                               |                                                                               |
|                                                                               | Click **Add** to add an email address or an expression using the Expression   |
|                                                                               | Assistant. Repeat to add additional email recipients. See [Add email          |
|                                                                               | recipients](#add-email-recipients) for more information.                      |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| BCC                                                                           | List of email recipients to blind carbon copy (BCC).                          |
|                                                                               |                                                                               |
|                                                                               | Click **Add** to add an email address or an expression using the Expression   |
|                                                                               | Assistant. Repeat to add additional email recipients. See [Add email          |
|                                                                               | recipients](#add-email-recipients) for more information.                      |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Reply To                                                                      | Email address that will receive replies to the email.                         |
|                                                                               |                                                                               |
|                                                                               | Enter an email address or an expression using the Expression Assistant. See   |
|                                                                               | [Add email recipients](#add-email-recipients) for more information.           |
|                                                                               |                                                                               |
|                                                                               | Defaults to `noreply@appsheet.com`                                            |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Customize "From" name                                                         | Customize the email address displayed in the `From` field of the email. By    |
|                                                                               | default, the app creator is used (for example, `appcreator@gmail.com`).       |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| PreHeader                                                                     | Email preheader summary text that follows the subject line when viewed in an  |
|                                                                               | inbox.                                                                        |
|                                                                               |                                                                               |
|                                                                               | Specify text,                                                                 |
|                                                                               | [variables](https://support.google.com/appsheet/answer/11539253), and         |
|                                                                               | [expressions](https://support.google.com/appsheet/answer/10104642). For       |
|                                                                               | example:                                                                      |
|                                                                               |                                                                               |
|                                                                               | -   `Your Order`                                                              |
|                                                                               | -   `Order for <<[FirstName]>> <<[LastName]>>`                                |
|                                                                               | -   `Order for <<[FirstName]>> <<[LastName]>> on <<TODAY()>>`                 |
|                                                                               |                                                                               |
|                                                                               | To suppress the PreHeader, enter a **single space character**.                |
|                                                                               |                                                                               |
|                                                                               | Defaults to:                                                                  |
|                                                                               |                                                                               |
|                                                                               | `<<_UPDATEMODE>> to appli                                                     |
|                                                                               | cation '<<_APPNAME>>' table '<<_TABLENAME>>' by '<<_USEREMAIL>>' at <<_NOW>>` |
|                                                                               |                                                                               |
|                                                                               | For example:\                                                                 |
|                                                                               | `Update to application 'Workflow' by 'Julie Morgan' at 8/26/2021 6:12:28 PM`  |
|                                                                               |                                                                               |
|                                                                               | **Note**: `<<USEREMAIL>>` is omitted if your app does not require             |
|                                                                               | authentication.                                                               |
|                                                                               |                                                                               |
|                                                                               | See also [Built-in                                                            |
|                                                                               | variab                                                                        |
|                                                                               | les](https://support.google.com/appsheet/answer/11539253#built-in-variables). |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Email Body Template                                                           | Template to use for more precise control of the email body. See [Use          |
|                                                                               | templates in a bot](https://support.google.com/appsheet/answer/11539957) and  |
|                                                                               | the **Email Body** description (above).                                       |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

### Attachment settings

Expand and customize the **Attachment** **settings**, as described below.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Attachment Content Type                                                       | Content type of the email attachment file.                                    |
|                                                                               |                                                                               |
|                                                                               | Valid content type values include:                                            |
|                                                                               |                                                                               |
|                                                                               | -   CSV                                                                       |
|                                                                               | -   HTML                                                                      |
|                                                                               | -   ICS_Calendar                                                              |
|                                                                               | -   JSON                                                                      |
|                                                                               | -   PDF                                                                       |
|                                                                               | -   XLSX (Microsoft Excel)                                                    |
|                                                                               | -   XML                                                                       |
|                                                                               |                                                                               |
|                                                                               | Defaults to **PDF** which is the most often used content type for email       |
|                                                                               | attachments.                                                                  |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Attachment Template                                                           | Template to use for more precise control of the email attachment. See [Use    |
|                                                                               | templates in a bot](https://support.google.com/appsheet/answer/11539957) and  |
|                                                                               | [Archive email                                                                |
|                                                                               | attachments](https://support.google.com/appsheet/answer/11538747) for more    |
|                                                                               | information.                                                                  |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Attachment Name                                                               | Name of attachment.                                                           |
|                                                                               |                                                                               |
|                                                                               | Specify text,                                                                 |
|                                                                               | [variables](https://support.google.com/appsheet/answer/11539253), and         |
|                                                                               | [expressions](https://support.google.com/appsheet/answer/10104642). For       |
|                                                                               | example:                                                                      |
|                                                                               |                                                                               |
|                                                                               | -   `My Attachment`                                                           |
|                                                                               | -   `My Attachment for <<CustomerName>>`                                      |
|                                                                               | -   `My Attachment for <<CustomerName>> from <<_APPNAME>> on <<TODAY()>>`     |
|                                                                               |                                                                               |
|                                                                               | See [Archive email                                                            |
|                                                                               | attachments](https://support.google.com/appsheet/answer/11538747) and [How    |
|                                                                               | the archive attachment filename if                                            |
|                                                                               | for                                                                           |
|                                                                               | med](https://support.google.com/appsheet/answer/11538747#how-filename-formed) |
|                                                                               | for more information.                                                         |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Attachment Archive                                                            | Attachment file archive configuration.                                        |
|                                                                               |                                                                               |
|                                                                               | Valid values include:                                                         |
|                                                                               |                                                                               |
|                                                                               | -   **AttachAndDoNotArchive** - Attach file to email without archiving it.    |
|                                                                               | -   **AttachAndArchive** - Attach file to email and archive it.               |
|                                                                               | -   **ArchiveAndDoNotAttach** - Archive the file but do not attach it to the  |
|                                                                               |     email. This option is useful if the attachment file is too large to       |
|                                                                               |     include as an attachment. Instead, the email body can include the URL or  |
|                                                                               |     Weblink to the archived attachment file.                                  |
|                                                                               |                                                                               |
|                                                                               | See [Archive email                                                            |
|                                                                               | attachments](https://support.google.com/appsheet/answer/11538747) for more    |
|                                                                               | information.                                                                  |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Attachment File Store                                                         | File system where attachments are stored.                                     |
|                                                                               |                                                                               |
|                                                                               | When set to **Default** (the default setting), the attachment file is         |
|                                                                               | archived to the [authentication                                               |
|                                                                               | provider](https://support.google.com/appsheet/answer/10104975) file system.   |
|                                                                               | For example, if your authentication provider is Google, the attachment file   |
|                                                                               | is archived to Google Drive. If your authentication provider is Dropbox, the  |
|                                                                               | attachment file is archived to Dropbox.                                       |
|                                                                               |                                                                               |
|                                                                               | **Notes**:                                                                    |
|                                                                               |                                                                               |
|                                                                               | -   If Smartsheet is your authentication provider, AppSheet archives the      |
|                                                                               |     attachment file to Google Drive as Smartsheet does not have a file        |
|                                                                               |     system. If you use Smartsheet and wish to archive attachment files, you   |
|                                                                               |     must include Google as a data source, as described in [Use multiple data  |
|                                                                               |     sources](https://support.google.com/appsheet/answer/10106309).            |
|                                                                               | -   [Enterprise pricing                                                       |
|                                                                               |     plan](https://workspace.google.com/pricing.html?ga_lang=en) customers can |
|                                                                               |     archive attachment files to a [Cloud Object                               |
|                                                                               |     Store](https://support.google.com/appsheet/answer/10106769).              |
|                                                                               |                                                                               |
|                                                                               | See [Archive email                                                            |
|                                                                               | attachments](https://support.google.com/appsheet/answer/11538747) for more    |
|                                                                               | information.                                                                  |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Attachment Folder Path                                                        | Folder path where attachments are saved relative to the default app folder.   |
|                                                                               |                                                                               |
|                                                                               | Specify text and                                                              |
|                                                                               | [expressions](https://support.google.com/appsheet/answer/10104642). For       |
|                                                                               | example:                                                                      |
|                                                                               |                                                                               |
|                                                                               | -   `MyAttachments/MyPurchaseOrders`                                          |
|                                                                               |                                                                               |
|                                                                               | -   `<<CONCATENAT                                                             |
|                                                                               | E("MyAttachments/PurchaseOrdersByMonth_", YEAR(NOW()), "_", MONTH(NOW()))>>:` |
|                                                                               |                                                                               |
|                                                                               | In the second example, email attachment files would be stored in a separate   |
|                                                                               | folder, based on the month. For example:                                      |
|                                                                               | `MyAttachments/PurchaseOrdersByMonth_2019_02`                                 |
|                                                                               |                                                                               |
|                                                                               | Defaults to `Attachments`.                                                    |
|                                                                               |                                                                               |
|                                                                               | See [Archive email                                                            |
|                                                                               | attachments](https://support.google.com/appsheet/answer/11538747) and [How    |
|                                                                               | the archive attachment folder name if                                         |
|                                                                               | formed                                                                        |
|                                                                               | ](https://support.google.com/appsheet/answer/11538747#how-folder-name-formed) |
|                                                                               | for more information.                                                         |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Disable Timestamp?                                                            | Toggle to indicate whether to append a timestamp to attachment filenames.     |
|                                                                               | Appending the timestamp will ensure the filenames are unique.                 |
|                                                                               |                                                                               |
|                                                                               | The timestamp contains the date and time at which the attachment file was     |
|                                                                               | created, formatted as follows: *yyyyMMdd_HHmmss_fff* indicating year, month,  |
|                                                                               | day, hours, minutes, seconds, and milliseconds. For example:                  |
|                                                                               |                                                                               |
|                                                                               | `MyAttachmentName20190207_133355_804.pdf`                                     |
|                                                                               |                                                                               |
|                                                                               | If you disable the timestamp, you must ensure that every attachment filename  |
|                                                                               | is unique. Otherwise, the attachment files may be overwritten. For example,   |
|                                                                               | if you are archiving your attachment files to Google Drive and you disable    |
|                                                                               | the timestamp, only the most recent attachment file will be available. Older  |
|                                                                               | attachment files with the same name will have been overwritten.               |
|                                                                               |                                                                               |
|                                                                               | Disabled (timestamp is appended) by default.                                  |
|                                                                               |                                                                               |
|                                                                               | See [Archive email                                                            |
|                                                                               | attachments](https://support.google.com/appsheet/answer/11538747) for more    |
|                                                                               | information.                                                                  |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Attachment Page Orientation                                                   | Page orientation of the attachment. Valid values include: **Portrait** and    |
|                                                                               | **Landscape**                                                                 |
|                                                                               |                                                                               |
|                                                                               | **Note**: This setting is available only if you set **Attachment Content      |
|                                                                               | Type** to **PDF**.                                                            |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Attachment Page Size                                                          | Page size. Select a standard size or select **Custom** and enter the          |
|                                                                               | **Attachment Page Width** and **Attachment Page Height** in millimeters.      |
|                                                                               |                                                                               |
|                                                                               | **Note**: This setting is available only if you set **Attachment Content      |
|                                                                               | Type** to **PDF**.                                                            |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Use Custom Margins                                                            | Toggle to indicate whether you want to specify custom margins for the         |
|                                                                               | attachment.                                                                   |
|                                                                               |                                                                               |
|                                                                               | If disabled, the task uses default margins. If enabled, customize the margins |
|                                                                               | using the additional settings displayed, as described below.                  |
|                                                                               |                                                                               |
|                                                                               | **Note**: This setting is available only if you set **Attachment Content      |
|                                                                               | Type** to **PDF**.                                                            |
|                                                                               |                                                                               |
|                                                                               | Disabled by default.                                                          |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Other Attachments                                                             | Other attachment files such as drawings, images, signatures, thumbnails, or   |
|                                                                               | files.                                                                        |
|                                                                               |                                                                               |
|                                                                               | Click **Add** to add other attachments to the email. Specify text or          |
|                                                                               | [expressions](https://support.google.com/appsheet/answer/10104642). Repeat to |
|                                                                               | add additional attachment files.                                              |
|                                                                               |                                                                               |
|                                                                               | See [Add other attachments to an                                              |
|                                                                               | email](https://support.google.com/appsheet/answer/11538147) for more          |
|                                                                               | information.                                                                  |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

If you enable **Use Custom Margins**, customize the **attachment page margins** using the additional settings displayed, as described below.

|                               |                                             |                             |
|-------------------------------|---------------------------------------------|-----------------------------|
| **Setting**                   | **Description**                             | **Default (if applicable)** |
| Attachment Page Margin Top    | Top margin for the attachment in points.    | 0                           |
| Attachment Page Margin Right  | Right margin for the attachment in points.  | 0                           |
| Attachment Page Margin Bottom | Bottom margin for the attachment in points. | 0                           |
| Attachment Page Margin Left   | Left margin for the attachment in points.   | 0                           |

### Advanced

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

### ****Add email recipients

If you receive an `OutgoingEmailAllowListViolations` error in Audit History, then either your team admin has [restricted the recipient list for outgoing mail](https://support.google.com/appsheet/answer/11918568#outgoing-email-allowlist) or sending email to external recipients is not allowed by policy, as described in [Set the AppSheet Core security setting](https://support.google.com/a/answer/10447197#core-security). To address this issue, contact your team administrator to adjust the restricted recipient list or contact your Workspace administrator for assistance with turning off the AppSheet Core Security setting.

The following provides guidelines for adding the email recipients in **To**, **CC**, and **BCC** when configuring the email (described above):

- **Enter a specific email address**, such as **`JohnHughes@gmail.com`**.
  If an email address contains special characters such as hyphen or plus, you must enclose the email address in quotes. For example: **`"John-L-Hughes@gmail.com"`**

- **Use a field in a record that is being modified**.
  For example, when a new order is received, you can send an email to the customer who created the order. In this scenario, enter the name of the field that contains the customer's email address. For example, if the `CustomerEmail` field in the order record contains the customer's email address, enter the following expression: **`[CustomerEmail]`**

- **Use a field in a record that is referenced by the record being modified**.
  For example, when a new order is received, you can send an email to the customer who created the order. Each order record might contain a reference to a customer record that contains the customer's email address. In this scenario, enter the name of the order record field that references the customer record followed by the name of the customer record field that contains the customer's email address. For example, if the order record field that references the customer record is `CustRef` and the name of the customer record field containing the customer's email address is `CustEmail`, specify the customer's email address by entering the expression: **`[CustRef].[CustEmail]`**

- **Use an entire column in another table**.
  For example, each time a new order is added, you can send an email to all of the people defined in another table. In this scenario, enter the name of the table followed by the field that contains the email address. For example, if you create a table called `PeopleToInform` that contains two columns, `Name` and `EmailAddress`, each time a new order is added, you can send email to all of the people in the `PeopleToInform` table by entering the expression: **`PeopleToInform[EmailAddress]`**

- **Use selected rows in another table**.
  For example, each time a new order is added, you can send an email to all of the people in the sales department. In this scenario, enter the name of the table followed by the field that contains the email address, and set the department field to Sales. For example, if you create a table called `PeopleToInform` that contains three columns, `Name`, `EmailAddress`, and `Department`, each time a new order is added, you can send an email to all of the people in the `PeopleToInform` table who are in the `Sales` department by entering the expression: **`SELECT(PeopleToInform[EmailAddress], ([Department] = "Sales"), TRUE)`**

**Note**: While the app is in test mode (that is, you have not run a [deployment check](https://support.google.com/appsheet/answer/10104389) and deployed the app), any messages sent will be sent to the app creator only. To confirm the list of email recipients that will be included in **To**, **CC**, and **BCC**, check the Audit History, as described in [How do I determine whether an email was delivered](https://support.google.com/appsheet/answer/11449723#determine-email-delivered)[?](https://support.google.com/appsheet/answer/11449723#determine-email-delivered)

## Examples of sending an email from an automation

The following provide examples of sending an email from an automation.

### Send email when a row is updated to have a specific column value

You can create a workflow rule that sends an email when a row is updated to have a specific column value. For example, you might send an email when the `Status` column in the `ServiceRequests` row is updated to contain the value `Active`.

    AND(
      ("Active" = [_THISROW_AFTER].[Status]),
      ([_THISROW_AFTER].[Status] <> [_THISROW_BEFORE].[Status])
    )

In this expression, note the use of `[_THISROW_BEFORE]` and `[_THISROW_AFTER]`. These are system-provided [references](https://support.google.com/appsheet/answer/10106510) that refer to the state of the row [before and after](https://support.google.com/appsheet/answer/11547057) the change was made, respectively. This is really useful in order to check if the value of a field changed from one value to another.

Because `[_THISROW_BEFORE]` and `[_THISROW_AFTER]` are references, you use a [dereference expression](https://support.google.com/appsheet/answer/10107396) to access the value of a specific column in the referenced row.

### Send an email only after adding a parent record and all of its child records

When you add a parent record along with one or more child records, AppSheet first adds the parent record, then each of the child records. This can make it difficult to trigger an automation event only after all of the child records have been added. 

You can can use the following technique to ensure that all parent and child records are added before the event is triggered. This technique uses the `Form Saved` event to trigger a data-change action which triggers the event only after the child records have been added.

Do this as follows:

1.  The child table must contain a `Ref` field to the parent table. Enable the `Is a part of?` property of the `Ref` field. This makes it possible to add child records when the parent record is added.

2.  Add a `Text` field to the parent table. Call the field **Status** and set its `Initial value` property to **`""`** (blank). The `Status` column controls whether the data change event triggers.

3.  Create a data-change action for the parent table which sets the `Status` column's value to **`"Run"`**.

4.  Create a second data-change action for the parent table which sets the `Status` column's value to **`""`** (blank).

5.  Create a composite action for the parent table that invokes the two data-change actions above. This composite action invokes the first data-change action to set the `Status` column's value to `"Run"`, and the second data-change action to set the `Status` column's value to blank. These two data changes will be sent to the server as separate updates. The first update triggers the automation event, while the second update prevents further updates from triggering the automation event.

6.  Go to the **UX \> Views** tab. Click **Show system views**. Select the form for the parent table. Expand **Behavior**. Find **Event Actions** and set its `Form Saved` property to the compositive action created in the previous step.

7.  Set your data change event to **Updates only**. Set its `Condition` property to: **`[Status] = "Run"`**

## Prevent app creators from adding email attachments in automations

Prevent app creators from adding email attachments in automations by using the "Restrict Automation Email Attachments" policy, as described below. For more information, see [Define governance policies](https://support.google.com/appsheet/answer/11948767).

To app creators from adding attachments to emails sent from automations:

1.  Select **My account \> Policies**.
2.  Click **+ Account Policy** or **+ Team Policy** to add an account or team policy, respectively.
3.  Select **Restrict Automation Email Attachments** from the **Policy Template** drop-down.
4.  Click **Next**.
5.  The policy is preconfigured for you. You can modify any of the field values. See [Add a predefined policy](https://support.google.com/appsheet/answer/11948767#add-predefined-policy) for a description of each field. 
    **Important**: If you modify the **Condition** field, ensure that you retain the functionality defined below:
    `AND(ISBLANK([AttachmentTemplate]), ISBLANK([OtherAttachmentList]))`
6.  Click **Save**.
