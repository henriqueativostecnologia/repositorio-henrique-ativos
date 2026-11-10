---
fonte: https://support.google.com/appsheet/answer/15725655?hl=en
baixado: 2026-11-10
---

# Build an automation using Gmail

This is a **beta** release of building automations using Gmail events. See [Track and manage feature releases](https://support.google.com/a/topic/1227580). Preview offerings are intended for use in test environments only. This feature is not recommended for use in production apps. For questions or assistance with this feature, contact [AppSheet Support](https://www.appsheet.com/Support/Contact).

You must be a **Google Workspace user** to build AppSheet automations with Gmail. See [Add AppSheet to Google Workspace](https://support.google.com/a/answer/10447197).

If you are using your Google Workspace account, the [Google Workspace Terms of Service](https://workspace.google.com/terms/premier_terms/) govern your use of Gmail. Otherwise, refer to the [Google Terms of Service](https://policies.google.com/terms).

Build automations using Gmail events that can be triggered by on one or both of the following:

- Add label to an email
- Remove label from an email

The Gmail event will be triggered if the selected email label is manually added or removed in the Gmail UI, or if it is applied automatically using a Gmail filter, as described in [Create rules to filter your emails](https://support.google.com/mail/answer/6579).

Build an automation using Gmail as described in the following sections:

- [Get started](#get-started)
- [Steps to build automations using Gmail](#steps)
- [How to access content in the email messages](#access-email-content)
- [How to support group email](#support-group-email)
- [How to support delegated email](#support-delegated-email)
- [Limitations](#limitations)

## Get started

To get started building automations with Gmail, see [Quick start: Build your first automation using Gmail](https://support.google.com/appsheet/answer/15733195).

## Steps to build automations using Gmail

To build automations using Gmail, perform the following steps:

+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **\#**                                             | **Step**                                           | **Description**                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| 1                                                  | Create an email label in your Gmail account        | This step is optional. You can create a new label  |
|                                                    | (Optional)                                         | that will be used to trigger the Gmail event, as   |
|                                                    |                                                    | described in [Create labels to organize            |
|                                                    |                                                    | Gmai                                               |
|                                                    |                                                    | l](https://support.google.com/mail/answer/118708). |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | Alternatively, you can use one of the default      |
|                                                    |                                                    | Gmail labels (Inbox, Unread, Starred, and so on).  |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| 2                                                  | Use the email label interactions to trigger an     | Build an automation and [configure a Gmail         |
|                                                    | automation                                         | event](https://support.google.com                  |
|                                                    |                                                    | /appsheet/answer/11445188#configure-gmail-event).  |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | Gmail events are triggered by external sources.    |
|                                                    |                                                    | See [Externally triggered                          |
|                                                    |                                                    | events](https://support.google.com/apps            |
|                                                    |                                                    | heet/answer/11445188#externally-triggered-events). |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | When you connect a Gmail account to your AppSheet  |
|                                                    |                                                    | app when adding a Gmail event to an automation, it |
|                                                    |                                                    | is added as a data source but no table is added to |
|                                                    |                                                    | your app. To view or delete the Gmail data source, |
|                                                    |                                                    | see [Manage data                                   |
|                                                    |                                                    | sources](htt                                       |
|                                                    |                                                    | ps://support.google.com/appsheet/answer/10106309). |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | **Note: **When a Gmail event is triggered for a    |
|                                                    |                                                    | message on an email thread, the automation is also |
|                                                    |                                                    | triggered for each subsequent reply in the thread. |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| 3                                                  | Access content in the email messages (Optional)    | This step is optional. You can access content in   |
|                                                    |                                                    | the email message associated with a Gmail          |
|                                                    |                                                    | event using the available message column values.   |
|                                                    |                                                    | See [How to access content in the email            |
|                                                    |                                                    | messages](#access-content-email). **All email      |
|                                                    |                                                    | message content is read-only.**                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+

## How to access content in the email messages

To access content in the email messages, you can use the column values listed in the following table. **All email message content is read-only**. For more information about the email message content, see [Gmail API Overview](https://developers.google.com/gmail/api/guides).

+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Column**                                         | **Type**                                           | **Description**                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `[Body]`                                           | `LongText`                                         | Body of the email message                          |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `[CcAddresses]`                                    | `List`                                             | List of recipients' addresses (`Text` or `Email`)  |
|                                                    |                                                    | that are copied on the email                       |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | **Note**: To save the list values, use             |
|                                                    |                                                    | an `EnumList` column with **Allow other            |
|                                                    |                                                    | values** turned on.                                |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `[Date]`                                           | `DateTime`                                         | Date the email message was sent                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `[From]`                                           | `Text`                                             | From address                                       |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `[Internal Date]`                                  | `DateTime`                                         | Date the email was first received by Gmail         |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `[Labels]`                                         | `List`                                             | List of labels (`Text`) that are added to the      |
|                                                    |                                                    | email message                                      |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | **Notes**:                                         |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | -   To save the list values, use an `EnumList`     |
|                                                    |                                                    |     column with **Allow other values** turned on.  |
|                                                    |                                                    | -   Predefined labels aren't translated.           |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `[Message ID]`                                     | `Text`                                             | ID of the message                                  |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `[Related Gmail Event Attachments]`                | `List`                                             | **Note**: For beta, Gmail attachments are not yet  |
|                                                    |                                                    | supported. This column field is empty.             |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | Related attachments                                |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `[ReplyTo]`                                        | `Text`                                             | ReplyTo address                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `[Subject]`                                        | `Text`                                             | Subject line of the email message                  |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `[Thread ID]`                                      | `Text`                                             | ID of the email thread                             |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `[ToAddresses]`                                    | `List`                                             | List of recipients' addresses (`Text` or `Email`)  |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | **Note**: To save the list values, use             |
|                                                    |                                                    | an `EnumList` column with **Allow other            |
|                                                    |                                                    | values** turned on.                                |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+

To view the column values in the Expression Assistant, click the **Examples** tab and click the **Columns** sub tab of the **Examples** tab.

For example:

Insert \[Subject\] column in Expression Assistant by clicking Insert

You can also view the message content available in the **Gmail Event Email** section on the Data Explorer tab.

Gmail content in Data Explorer

## How to support group email

To support group email, like `my-group.googlegroups.com`, do the following:

1.  Automatically forward the group email to your personal email inbox by setting the subscription preferences to **Each email**. See [Manage your subscription and global settings](https://support.google.com/groups/answer/9792489).
2.  Use a Gmail filter to label messages coming from the group automatically.
    For more information, see [Create rules to filter your emails](https://support.google.com/mail/answer/6579).
    1.  Open the email in your inbox.
    2.  Select **More \>** **Filter messages like this**.

        Filter messages like this in the Gmail More menu
    3.  In the dialog, click **Create filter**.

        Create filter
    4.  Select **Apply the label** and select a label from the drop-down. Then, click **Create filter**.

##  How to support delegated email

To support delegated email, do the following:

1.  Automatically forward the delegated email to your personal email inbox, as descrbied in [Automatically forward Gmail messages to another account](https://support.google.com/mail/answer/10957).
2.  Use a Gmail filter to label messages coming from the forwarded email.
    For more information, see [Create rules to filter your emails](https://support.google.com/mail/answer/6579).
    1.  Open the email in your inbox.
    2.  Select **More ********\>** **Filter messages like this**.

        Filter messages like this in the Gmail More menu
    3.  In the dialog:
        1.  Delete the **From** field contents.
        2.  Populate the To field with the delegated user email.
        3.  Click **Create filter**.

            Create filter for delegated email
    4.  Select **Apply the label** and select a label from the drop-down. Then, click **Create filter**.

## Limitations

The following summarizes the list of known limitations of Gmail events for the beta release:

- For `[Body]`, if there is no text-based version of the email message body, a blank body is returned. 
- Gmail attachments, stored in `[Related Gmail Event Attachments]`, are not yet supported.  
- Use of webhooks are not yet supported with Gmail events.
