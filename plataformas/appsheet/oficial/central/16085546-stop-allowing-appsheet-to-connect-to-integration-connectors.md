---
fonte: https://support.google.com/appsheet/answer/16085546?hl=en
baixado: 2026-11-10
---

# Stop allowing AppSheet to connect to Integration Connectors

This is a **preview release** of Integration Connectors with AppSheet. See [Track and manage feature releases](https://support.google.com/a/topic/1227580). Preview offerings are intended for use in test environments only. This feature is not recommended for use in production apps. For questions or assistance with this feature, contact [AppSheet Support](https://www.appsheet.com/Support/Contact).

Integration Connectors with AppSheet (preview) requires an **AppSheet Enterprise Plus** account.

If you no longer need to use your connections as data sources in AppSheet, you can stop allowing AppSheet to connect to Integration Connectors. Optionally, the AppSheet team admin can then [delete the data sources](https://support.google.com/appsheet/answer/10106309#delete).

This step is completed by both the AppSheet team admin and Google Cloud admin working together.

As the Google Cloud admin, to stop allowing AppSheet to connect to Integration Connectors, do the following:

1.  Locate the ID of the Google Cloud project where the connections were created. 
    If you aren't sure, request the AppSheet team admin to go to **My account \> Sources** and provide the ID in the **Google Cloud project ID** field for the relevant data sources.

    Google Cloud project ID on the Sources page
2.  Go to the Google Cloud console and in the project picker, select the project where the connections were created, the ID you identified in Step 1.
3.  Open the [IAM permissions](https://console.cloud.google.com/iam-admin/iam) page.
4.  Under **Principal**, locate the service account *provided by AppSheet*. 
    If you aren't sure, request the AppSheet team admin to follow the steps to set up the team to use Integration Connectors and copy the service account name displayed for step 1.
5.  Click to edit the principal.
6.  Under **Assign Roles**, click  adjacent to the following roles to delete them: 
    - Connector Invoker 
    - Connector Viewer
7.  If there are other roles assigned to this principal, these are not used by AppSheet. Check how they are being used before deleting them.
8.  Click **Save**.
9.  If you have connections in more than one Google Cloud project, repeat these steps for each project.
