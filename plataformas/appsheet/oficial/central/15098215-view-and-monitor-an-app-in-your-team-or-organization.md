---
fonte: https://support.google.com/appsheet/answer/15098215?hl=en
baixado: 2026-11-10
---

# View and monitor an app in your team or organization

To view and monitor an app in your team or organization, [access the Apps page](https://support.google.com/appsheet/answer/14961200#explore-apps-page) and click an app name in the list of all apps. You can also click an app name anywhere it appears in the AppSheet Admin Console.

The Apps details page opens.

App details in the AppSheet Admin Console

The App details page allows you to do the following:

- [View app details](#app-detail-summary)
- [Generate an app summary using Gemini](#app-summary) (preview)
- [View users of the app](#app-users)
- [View sharing status of the app](#sharing-status)
- [View the app in the app editor](#view-in-editor)
- [Transfer the app to another account](#transfer-app)
- [Monitor the app](#view-manage-app)

## View app details

View more details about the selected app, including:

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **App detail**                                                                | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Owner                                                                         |  Owner of the app.                                                            |
|                                                                               |                                                                               |
|                                                                               | Click the owner name to [view details for the owner's                         |
|                                                                               | account](https://support.google.com/appsheet/answer/15100835).                |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| License required                                                              | Minimum license required to use the app based on                              |
|                                                                               | its [features](https://support.google.com/appsheet/answer/10105400#features). |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Users                                                                         | Number of users, both internal and external to your team or organization,     |
|                                                                               | that have accessed the app in the last 30 days.                               |
|                                                                               |                                                                               |
|                                                                               | **Note**: Due to delays with processing app usage details, at certain times   |
|                                                                               | the number of users on this page might not match the total number of users    |
|                                                                               | shown on the [Apps                                                            |
|                                                                               | page](https://support.google.com/appsheet/answer/14961200).                   |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Last modified                                                                 | Date the app was last modified by app owner (this account) or co-author.      |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Status                                                                        | Series of icons that indicate the status of the app, including one or more of |
|                                                                               | the following:\                                                               |
|                                                                               | green check mark  - App is runnable                                           |
|                                                                               |                                                                               |
|                                                                               |  - App is not runnable                                                        |
|                                                                               |                                                                               |
|                                                                               |  - App is prototype                                                           |
|                                                                               |                                                                               |
|                                                                               | Status icon indicating app is deployed  - App is deployed                     |
|                                                                               |                                                                               |
|                                                                               | Status icon indicating app is secure  - App is secure ([requires              |
|                                                                               | sign-in](https://support.google.com/appsheet/answer/10104975))                |
|                                                                               |                                                                               |
|                                                                               | Status icon indicating app is not secure  - App is not secure (doesn't        |
|                                                                               | require sign-in)                                                              |
|                                                                               |                                                                               |
|                                                                               |  - App is marked for personal use                                             |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

## Generate an app summary using Gemini

This is a **preview** release of generating app summaries using Gemini, and is intended for use in test environments only. This feature is not recommended for use in production apps. If you have any feedback on the app summary, select the **Send Feedback** button and include a screenshot of the app summary with your feedback.

As an admin with an AppSheet Enterprise Plus license, you can generate a summary of the apps owned by an enterprise creator in your organization.

Generating an app summary doesn't consume [credits for Gemini usage](https://support.google.com/appsheet/answer/16274771).

To generate an app summary using Gemini, expand the **App summary generated by Gemini** section, as shown. The app summary isn't generated until you expand the section. It will persist until a new version of the app is saved by the creator

The app summary is based on the details provided in the app definition including the app name, description, views, actions, automations, and so on. You can view all of the information included in the app definition by selecting **View in editor**. The app summary may reference aspects of the data schema (such as, column names) that are exposed in the app definition, but will not include data (such as, row-level information) from the tables connected to an app. 

## View users of the app

Select the **Users** tab to view more details about the users of the app, including:

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **User detail**                                                               | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| User name                                                                     | Email address of the AppSheet account.                                        |
|                                                                               |                                                                               |
|                                                                               | For accounts that are in your team or organization, click the user name to    |
|                                                                               | [view details for the                                                         |
|                                                                               | account](https://support.google.com/appsheet/answer/15100835).                |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Auth provider                                                                 | Provider used to authenticate AppSheet sign-ins. See [Require sign-in: The    |
|                                                                               | Essentials](https://support.google.com/appsheet/answer/10104975).             |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| User type                                                                     | Type of user. Can be one of the following:                                    |
|                                                                               |                                                                               |
|                                                                               | -   **Internal** when the user belongs to the same team or organization       |
|                                                                               | -   **External user** when the user doesn't belong to the team or             |
|                                                                               |     organization. See [About external user                                    |
|                                                                               |     licensing](https://support.google.com/appsheet/answer/15197435)           |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Team                                                                          | Team the AppSheet account belongs to. See [Define your team                   |
|                                                                               | membership](https://support.google.com/appsheet/answer/13964712).             |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Activity (by day)                                                             | Daily usage for the app.                                                      |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Last access                                                                   | Date that this account last accessed the app.                                 |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

## View sharing status of the app

Select the **Sharing status** tab to view the app sharing status and permissions, including:

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **User detail**                                                               | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| User/domain                                                                   | Name of the user or domain with which the app is shared.  See also [Share:    |
|                                                                               | The Essentials](https://support.google.com/appsheet/answer/10104983).         |
|                                                                               |                                                                               |
|                                                                               | For accounts that are in your team or organization, click the user name to    |
|                                                                               | [view details for the                                                         |
|                                                                               | account](https://support.google.com/appsheet/answer/15100835).                |
|                                                                               |                                                                               |
|                                                                               | If applicable, the following labels indicate whether the app is               |
|                                                                               | a [public](https://support.google.com/appsheet/answer/11938113) or [team](    |
|                                                                               | https://support.google.com/appsheet/answer/10104795#share-sample-app) sample: |
|                                                                               |                                                                               |
|                                                                               | Public or team sample label in Sharing status tab for app details in Admin    |
|                                                                               | Console                                                                       |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Type                                                                          | Type of user. Valid values are Creator or User.                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Access                                                                        | Access permission. Valid values include:\                                     |
|                                                                               |                                                                               |
|                                                                               | -   **Use app -** Users can use the app, but can't view or edit the app in    |
|                                                                               |     the app editor.                                                           |
|                                                                               | -   **View/copy app** - Users can view and copy the app in the app editor,    |
|                                                                               |     but can't edit the app. See also [Let another user copy your              |
|                                                                               |     app](https://support.google.com/appsheet/answer/10104387).                |
|                                                                               | -   **Edit app** - Users can edit the app in the app editor and add           |
|                                                                               |     additional tables from any of the data sources already connected to the   |
|                                                                               |     app.\                                                                     |
|                                                                               |     **Note**: Only one user should edit an app at a time. If two users        |
|                                                                               |     attempt to edit an app at the same time, conflicts may occur when the app |
|                                                                               |     is saved.                                                                 |
|                                                                               |                                                                               |
|                                                                               | See [Manage access for individual                                             |
|                                                                               | users](https://support.google.com/appsheet/answer/10104983).                  |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| In-app role                                                                   | App role for the account that is set when sharing the app. Valid values       |
|                                                                               | include User or Admin. See [Manage app access for individual                  |
|                                                                               | users](ht                                                                     |
|                                                                               | tps://support.google.com/appsheet/answer/10104983#manage-roles-app-versions). |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| App version                                                                   | Version of the app in use by the users, such as Default, Latest, or Stable.   |
|                                                                               | See [Manage app access for individual                                         |
|                                                                               | users](https://support.google.com/appsheet/answer/10104983).                  |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

## View the app in the app editor

To view the app in the app editor, click **View in editor**.

## Transfer the app to another account

To transfer the app to another account, see [Transfer an individual app to another account](https://support.google.com/appsheet/answer/15098213#transfer-app).

## Monitor the app

Monitor the app by doing one of the following tasks:

|                                           |                                                                                                           |
|-------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| **Task**                                  | **Description**                                                                                           |
| **More**  **\> View app**                 | Open app in a new browser tab.                                                                            |
| **More**  **\> Audit history**            | [Monitor app activity using Audit History](https://support.google.com/appsheet/answer/10104794).          |
| **More**  **\>** **Performance analyzer** | [Monitor app performance using Performance Profile](https://support.google.com/appsheet/answer/10104997). |
| **More**  **\>** **Version history**      | [View or restore a version of your app](https://support.google.com/appsheet/answer/10105387).             |
| **More**  **\> Usage stats**              | [Monitor app usage statistics](https://support.google.com/appsheet/answer/11449228).                      |
