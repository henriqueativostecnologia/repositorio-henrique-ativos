---
fonte: https://support.google.com/appsheet/answer/10105756?hl=en
baixado: 2026-11-10
---

# Set access mode as app creator or app user

This feature is available to **AppSheet Core** accounts and above. See [AppSheet pricing](https://about.appsheet.com/pricing/).

The mobile app that you build communicates with the AppSheet backend, and it is the AppSheet backend that communicates with your cloud data provider (such as Google Drive) to read or update data.

For security reasons, cloud data providers only let AppSheet access your data after you grant AppSheet permission to do so. Whenever a user or app creator signs in, they grant AppSheet the permission to act on their behalf.

**Important:** Content in your connected data sources can be potentially viewed and updated by app users you invite to the application, even if they don't have permissions to view or edit that data source. For example, you may be the sole viewer or editor of a Google Sheet, but if connected to an app, that Sheet data may be exposed to any app users.

You can set **Access mode** for a table when you [configure table settings](https://support.google.com/appsheet/answer/10105821#configure-table) or on the **Security \> Security Filters** page. For example, in the image below, access mode can be customized for the `NationalParks` table on the Security Filters page. For information about setting the Security filter, see [Security filters: The Essentials](https://support.google.com/appsheet/answer/10104488).

Access mode in NationalParks table on Security \> Security Filters page

Although security filters limit data access, they aren't a complete security solution. Users should protect sensitive data operations at the data source level. For more information about securing your data, see [Security: The Essentials](https://support.google.com/appsheet/answer/10105078).

The following table describes the access mode types.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Access mode**                                                               | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| as app creator                                                                | In the default run mode (**as app creator)**, AppSheet accesses data using    |
|                                                                               | the identity of the app creator. If you as the app creator have access to the |
|                                                                               | spreadsheet, you can distribute your app to other people who do not have      |
|                                                                               | direct access to the spreadsheet.                                             |
|                                                                               |                                                                               |
|                                                                               | Most AppSheet app creators choose **as app creator** because it allows them   |
|                                                                               | to restrict direct access to the spreadsheet to solely the application        |
|                                                                               | creator.                                                                      |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| as app user                                                                   | You can set the run mode to **as app user**. In this mode, AppSheet will      |
|                                                                               | access data using the identity of the app user. The application must require  |
|                                                                               | sign-in, and all application users must have permission to directly access    |
|                                                                               | the source spreadsheet and folder.                                            |
|                                                                               |                                                                               |
|                                                                               | What are the benefits of **as app user **run mode?                            |
|                                                                               |                                                                               |
|                                                                               | 1.  Some users view it as a stricter security mechanism because it relies     |
|                                                                               |     entirely on the permissions model of the cloud data provider.             |
|                                                                               | 2.  It can be an auditing mechanism for cloud providers, like Google Drive    |
|                                                                               |     and Box, that maintain audit histories of all updates made to documents.  |
|                                                                               |     Each audit history record contains the identity of the user who made the  |
|                                                                               |     change.                                                                   |
|                                                                               |                                                                               |
|                                                                               | This option has no bearing on the identity of the user on the mobile device.  |
|                                                                               | The user who signs in is always the current user therefore expressions like   |
|                                                                               | [`USEREMAIL()`](https://support.google.com/appsheet/answer/10108210) always   |
|                                                                               | reflect the current signed-in user, never the app creator.                    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
