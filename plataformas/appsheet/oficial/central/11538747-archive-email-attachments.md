---
fonte: https://support.google.com/appsheet/answer/11538747?hl=en
baixado: 2026-11-10
---

# Archive email attachments

Archive email attachments as described in the following sections:

- [Configure the archive email attachment properties](#configure)
- [How the archive attachment filename is formed](#how-filename-formed)
- [How the archive attachment folder name is formed](#how-folder-name-formed)
- [How the complete archive folder and file path are formed](#how-complete-path-formed)
- [How the archive attachment file URL is formed](#how-url-formed)
- [Use archive attachment expression variables in templates](#use-expression-variables)
- [View the archive attachment in Audit History](#view-audit-history)

### Configure the archive email attachment properties

When sending an email, configure the following archive email attachment properties. For complete details, see [Send an email from an automation](https://support.google.com/appsheet/answer/11447614).

- **Attachment Archive** - Select whether to attach a file to an email without archiving, attach a file to an email and archive it, or archive a file without attaching it to an email (useful for large files).
- **Attachment Content Type** - Select the content type of the email attachment file.
- **Attachment File Store** - Specify the file system where attachments are stored.
- **Attachment Folder Path** - Specify the relative folder where attachments are saved within the file system.
- **Attachment Name** - Enter the name of the attachment.
- **Attachment Template** - Use a template for more precise control of the email attachment. See [Use templates in an automation](https://support.google.com/appsheet/answer/11539957).
- **Disable Timestamp** - Indicate whether to append a timestamp to the attachment file.

If enabled, email attachments are archived *before* the email is sent.

See also [Archive email attachments to Microsoft SharePoint](https://support.google.com/appsheet/answer/11542175).

### How the archive attachment filename is formed

The archive attachment filename is formed by combining the **Attachment Name** value with spaces removed, the timestamp (if **Disable Timestamp?** is disabled) formatted as *yyyyMMdd_HHmmss_fff*, and the file extension for the **Attachment Content Type**.

For example, if the **Attachment Name** is set to **MyAttachmentName** and the **Attachment Content Type** is **PDF**:

- If **Disable Timestamp?** is disabled, the archive attachment filename is: `MyAttachmentName20190207_133355_804.pdf`
- If **Disable Timestamp?** is enabled, the archive attachment filename is: `MyAttachmentName.pdf`

### How the archive attachment folder name is formed

The archive attachment folder name in which the archive attachment file is stored is formed using the **default app folder** and the **Attachment Folder Path** property.

To configure the default app folder, select **Info \> Properties**, expand **App Properties**, and enter a value in the **Default app folder** property.

**Examples**:

If if the **default app folder** is `/appsheet/data/MyApp-24403/MyDefnFolder1 `and **Attachment Folder Path** is set to `MyFolderA/MyFolderZ`, then the archive folder name is:

    /appsheet/data/MyApp-24403/MyDefnFolder1/MyFolderA/MyFolderZ

If the default app folder is `/1track/data/MyApp-24403` and **Attachment Folder Path** is not defined (defaults to `Attachments`), then the archive folder name is:

    /appsheet/data/MyApp-24403/Attachments

### How the complete archive attachment folder and file path are formed

The complete archive folder and file path is formed by combining the [archive attachment folder name](https://help.appsheet.com/en/articles/5307754-archiving-email-attachments#h_2f629f2b86) with the [archive attachment filename](https://help.appsheet.com/en/articles/5307754-archiving-email-attachments#h_36b3a7543d).

**Examples**:

If the archive folder name is `/appsheet/data/MyApp-24403/Attachments` and the archive file name is `ChangeReport20190207_133355_804.pdf`, then the archive file and folder name is:

    /appsheet/data/MyApp-24403/Attachments/ChangeReport20190207_133355_804.pdf

If the archive folder name is `/appsheet/data/MyApp-24403/MyAttachments/PurchaseOrdersByMonth_2019_02` and the archive file name is `PurchaseOrder20190207_133355_804.pdf`, then the archive file and folder name is:

    /appsheet/data/MyApp-24403/MyAttachments/PurchaseOrdersByMonth_2019_02/PurchaseOrder20190207_133355_804.pdf

### How the archive attachment file URL is formed

The archive attachment file URL is formed as follows:

    https://www.appsheet.com/template/getappfileurl?appName=$YOUR_APP_NAME&fileName=$YOUR_ATTACHMENT_FILENAME

Where:

- `$YOUR_APP_NAME` specifies the name of your app.

- `$YOUR_ATTACHMENT_FILENAME` specifies the **Attachment Folder Name** followed by the **Archive File Name**. You can omit the **Default app folder** name as calls to `www.appsheet.com/template/getappfileurl` automatically prepend the default app folder name.

**Note**: The `$YOUR_APP_NAME` and `$YOUR_ATTACHMENT_FILENAME` values must be URL encoded if they contain *reserved* or *unsafe* URL characters.

For example, if `$YOUR_APP_NAME` is `MyOrderApp-432567` and `$YOUR_ATTACHMENT_FILENAME` is `MyAttachments/MyPdfReport.pdf`, then the URL is:

    https://www.appsheet.com/template/getappfileurl?appName=MyOrderApp-432567&fileName=MyAttachments%2FMyPdfReport.pdf

In this example, the slash (`/`) in the `$YOUR_ATTACHMENT_FILENAME` is URL encoded as `%2F`.

### Use archive attachment expression variables in templates

The following expression variables for archive attachment files are available and can be used in your **Email Body** or [email attachment templates](https://support.google.com/appsheet/answer/11539957).

|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| **Expression variable**    | **Description**                                                                        |
| `_ATTACHMENTFILENAME`      | Archive attachment filename.                                                           |
| `_ATTACHMENTFILE_URL`      | Archive attachment file URL.                                                           |
| `_ATTACHMENTFILE_WEB_LINK` | Link to the archive attachment file. The **Attachment Name** is used as the link text. |

### View the archive attachment in Audit History

View the archive attachment file and folder names by [checking the audit history log](https://support.google.com/appsheet/answer/10104794).

Customize the dashboard settings and look for an audit record similar to the following:

    "EmailAttachment": "Name: 'ScheduledReport.pdf' Archive: AttachAndArchive FileName: 'MyOrderApp-432567/Attachments/ScheduledReport20190201_184450_854.pdf'",

The **FileName** value indicates the file and folder where the attachment was archived.

**Note**: You may need to wait for up to five minutes for the audit record to appear. AppSheet groups audit records before writing them to the audit history log to reduce overhead. This can result in a delay before an audit record appears in the audit history. If you don't see an audit record, click **Search** periodically to refresh the audit history log.
