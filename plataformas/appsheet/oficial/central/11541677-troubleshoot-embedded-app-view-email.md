---
fonte: https://support.google.com/appsheet/answer/11541677?hl=en
baixado: 2026-11-10
---

# Troubleshoot embedded app view email

Troubleshoot dynamic email as described in the following sections. See also:

- [Send embedded app view email from a bot](https://support.google.com/appsheet/answer/11511240)
- [Troubleshoot bots](https://support.google.com/appsheet/answer/11547467)
- [Troubleshoot email](https://support.google.com/appsheet/answer/11449723)

## Troubleshoot issues with interactive content

If an embedded app view email is sent successfully but the content is not interactive (that is, a static email is rendered), check the following:

- **Is the recipient using Gmail?**
  Embedded app view email is supported with Google Gmail clients only.
- **Is the embedded app view email being forwarded?**
  Embedded app view emails that are forwarded by either the recipient or by a mail server will render as static emails.
- **Does the embedded app view email exceed the maximum size limit of 200 KB?**
  If the maximum size limit is exceeded, the embedded app view email will render as a static email. 
- **Was the embedded app view email sent to a group?**
  Embedded app view emails sent to groups will render as static emails.
- **Is embedded app view email enabled in the Gmail client?**
  To verify and enable embedded app view email in Gmail, see [Complete tasks without leaving a message](https://support.google.com/mail/answer/9266768). You must also ensure the [Always display external images](https://support.google.com/mail/answer/145919?hl=en) setting is enabled in Gmail. If you do not see the embedded app view email setting or it is disabled, follow the instructions below for enabling embedded app view emails for your Workspace domain.
- **Is embedded app view email enabled for your Workspace domain?**
  To view embedded app view emails, they must be enabled for your Workspace domain. See [Turn dynamic email on or off for users](https://support.google.com/a/answer/9707629#) for instructions on how to enable embedded app view emails for your Workspace domain.
- **Is Gmail configured to prevent spoofing and spam?**
  Check the following Gmail configurations: [SPF](https://support.google.com/a/answer/33786), [DKIM](https://support.google.com/a/answer/174124), and [DMARC](https://support.google.com/a/answer/2466580) You may need to include `@appsheet.com` on the list of authorized servers.
- **Is Secure image access turned on?**
  Enabling **Secure image access** on the **Security \> Options** page prevents images from rendering outside of the app, such as in an email.

## Troubleshoot error messages in the AppSheet editor

The following summarize the error messages that may be displayed in the AppSheet editor and how to correct them.

|                              |                                                                                                                                                                              |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Error Message**            | **Description**                                                                                                                                                              |
| Unsupported view is selected | Only Detail and Form views are supported at this time. See [Create a view for the embedded app view email](https://support.google.com/appsheet/answer/11511240#create-view). |

## Troubleshoot error message in user emails

The following summarize the error messages that may be displayed directly in user emails and how to correct them.

|                                                                        |                                                                                                                                                                                      |
|------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Error Message**                                                      | **Description**                                                                                                                                                                      |
| You do not have access to this application                             | Email recipient must be granted access to the app.                                                                                                                                   |
| Row does not exist or is not accessible                                | Row does not exist or there is an error condition in the row or table that is preventing access.                                                                                     |
| View is out of date. Please open the application in AppSheet.          | Type of view has changed since the embedded app view email was sent (for example, from a Detail to Form view).                                                                       |
| This application associated with this email does not exist             | App associated with the embedded app view email no longer exists.                                                                                                                    |
| This table associated with this email does not exist                   | Table associated with the embedded app view email no longer exists.                                                                                                                  |
| The view associated with this email does not exist or has been renamed | View associated with the embedded app view email no longer exists or has been renamed.                                                                                               |
| This email has expired                                                 | Embedded app view emails expire after 30 days. After 30 days, the fields will no longer be editable directly in the email and users will have to navigate to the app to edit fields. |
