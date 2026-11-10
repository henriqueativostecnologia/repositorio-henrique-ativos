---
fonte: https://support.google.com/appsheet/answer/13659499?hl=en
baixado: 2026-11-10
---

# Migrate to an AppSheet database

If you have an existing app and prefer to use AppSheet’s native data source for app building, then follow the steps below to migrate to AppSheet databases. AppSheet databases have quick sync enabled by default and support a higher number of concurrent edits compared to Sheets. Before migrating, review the [*restrictions, limits, and known issues for AppSheet databases.*](https://support.google.com/appsheet/answer/12653576)

## Migrating an app to use AppSheet databases as its data source

Apps with large data sets may not copy properly using this procedure, or may require some reconfiguration after the migration.

To migrate an app to use AppSheet databases as its data source:

1.  Perform one of the following steps for the app you want to copy:
    - On the **My Apps** page, locate the app and select **More** More ** \> Copy**.
    - Open the app in the editor, select **Manage \> Author**, and click **Copy App**.

2.  Enter the following information in the Copy app dialog:

    |             |                                                                        |
|-------------|------------------------------------------------------------------------|
| **Field**   | **Description**                                                        |
| App name    | Edit the name of the app. Defaults to the current name.                |
| Category    | Select a category from the drop-down. Defaults to the current category |
| Save app to | Select **AppSheet database.**                                          |

3.  Enable the options to copy the app data or file data (such as images).

4.  Click **Copy app**.

A new database will be created with a new app in the prototype state. Before deploying the new app, make sure it works as expected by checking these common areas:

- If any images are not being displayed properly, do the following:
  - Ensure the file path for attachments is correct.
  - Upload the images to a data source that is connected to AppSheet (most likely Google Drive if you sign in by using your Google account) and then re-add the images.
- By default the new app will use the same keys as previously defined. AppSheet databases come with a predefined key column called Row ID for each table. Learn more about the tradeoffs between using Row ID and your own defined key column in [System-generated keys](https://support.google.com/appsheet/answer/10106672#system-generated-key). 
- If the new app is still connected to the original data source, go to the My Apps page to confirm that the new AppSheet database was created and then connect it to the new app. 

## Migrating a data source to AppSheet databases 

If you have a Google Sheets data source, you can [import it to create an AppSheet database](https://support.google.com/appsheet/answer/12635312#import-google-sheet).
