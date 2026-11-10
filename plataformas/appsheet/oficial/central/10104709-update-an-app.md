---
fonte: https://support.google.com/appsheet/answer/10104709?hl=en
baixado: 2026-11-10
---

# Update an app

As an app creator or owner, you can make changes to the app definition at any time, For example, you might update an automation workflow. Your updates take effect the moment you save the change.

Most of your changes to the app definition involve changes to the actual mobile app. These changes are automatically picked up by your users the next time they **sync** **their app** from their mobile device.

When making updates to your app, you should be thoughtful about changes that might disrupt your app users, as described in the [Errors and warning during sync](https://support.google.com/appsheet/answer/10105777). For example, if your app user uses one version of your app to capture new data. Then, before the user syncs the data you make a change to the app definition (for example, you change some columns in the spreadsheet) and regenerate the app. When the user tries to sync the new data, AppSheet displays an error message indicating that there is a data mismatch.

At this point, the app is *stuck* -- it cannot fetch the latest definition of the app until it is able to send its changes to the backend; but the backend is not able to accept the changes because they cannot be applied.

In this scenario, there are two options:

- [App recovery mode](https://support.google.com/appsheet/answer/10105777#recovery-mode)
  App owners can place the app in **Recovery mode** to allow sync to proceed on the device and to auto-generate a recovery folder with the data updates that can be manually applied.

- [Manual recovery](https://support.google.com/appsheet/answer/10105777#manual-recovery)
  App users can discard the changes using the **Reset Changes** menu option and manually re-apply them. Before discarding them, users can select the **Show Changes** menu option and email the data changes to themselves or the app owner so that there is a record of the data changes to be manually applied.

  **Note**: If there is a large number of critical data changes, contact AppSheet Support to explore a custom approach to retrieve the data changes.
