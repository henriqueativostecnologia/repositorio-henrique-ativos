---
fonte: https://support.google.com/appsheet/answer/10104801?hl=en
baixado: 2026-11-10
---

# Organize data for teams

**Note**: Teams are supported for Enterprise Plus plans only.

This section describes best practices for organizing application data across a team of app creators. It provides recommendations for two commonly used data sources: [Google Drive](#google-drive) and [Microsoft O365](#microsoft-0365). Both scenarios share the same common objectives:

- Ensure data is retained independently of individual accounts
- Control who can directly access data
- Minimize disruption when an app is transferred to a new owner
- Enable collaboration on applications between multiple app creators

There are two main factors to consider: 1) Where to store data; 2) Who can own applications. Using a shared data source ensures data will be available regardless of an individual’s account status.

Apps can be owned by individuals or by a central service account. In both cases, the app owner can add [co-authors](https://support.google.com/appsheet/answer/10104983). Co-authors access shared apps from their individual accounts and have full access to the shared app definitions. 

Maintaining ownership of apps in a central service account can be advantageous if the app contributors change frequently. However, it introduces additional steps when making new applications and requires an additional account to be created.

Applications owned by an individual can be [transferred](https://support.google.com/appsheet/answer/10104991) to a new owner when necessary. By using a shared data source, transferring applications between owners is easy and does not require migration of any data. This is generally more efficient, but the AppSheet admin must transfer apps before closing an app owner’s account.

### Example organization of applications and data

## Google Sheets

The following section describes how to configure an AppSheet account to use a Shared Drive as the default file storage location.

### Create a Shared Drive

Create a Shared Drive where you will store data used by AppSheet applications. Add members that will create and own applications. End users do **not** need to be added. Access for end users will be via the app and controlled by settings chosen by the app creator. 

### Set the default file storage location

The default file storage location can be set for an individual user’s account. When a user creates a new app, AppSheet creates a folder in this location to store files associated with the app (such as uploaded image or  email templates). After the app is created, the file storage location can be modified for the app independently of the account default.

To set the default file storage location for a user’s account, navigate to **My account \> Settings \> Default folder path**. 

To set the default file storage location for an individual app, open the app and navigate to **Info \> Properties \> App Properties \> Default app folder** .

[Working with Google Drive](https://support.google.com/appsheet/answer/10104795#team-drive) describes how to set a Shared Drive as the default file storage location for a user’s account. The same general process can be used to set the default location for an individual app.

### Update existing applications

Google does not currently support moving folders from an individual My Drive location to a Shared Drive location. A work-around if you already have apps based on data in My Drive is as follows:

1.  Follow the steps above to update the app owners default file storage location to the Shared Drive.
2.  Open the app to be moved and navigate to **Manage \> Author.**
3.  Click **Copy App** and set the **Save app to** dropdown to **Google**.

AppSheet will create a copy of the app definition and the associated data. The data will be saved to the default file storage location for the user’s account. 

The process can be combined with an [app upgrade](https://support.google.com/appsheet/answer/10105386) if it is important to maintain the same links for end-users to access the application.

## Microsoft O365

The following section describes how to configure an AppSheet account to use a SharePoint site as the default file storage location.

### Create a SharePoint location

Create a SharePoint location where you will store data used by AppSheet applications. Add members that will create and own applications. End users do **not** need to be added. Access for end users will be through the app and controlled by settings chosen by the app creator. 

### Get the SharePoint Site ID

To determine the SharePoint Site ID for the target folder, see [Archive email attachments to MicroSoft Powerpoint](https://support.google.com/appsheet/answer/11542175).

**Note**: the SharePoint Site ID will have double forward slashes `//`.

### Set the default file storage location

The default file storage location can be set for an individual user’s account. When a user creates a new app, AppSheet creates a folder in this location to store files associated with the app (e.g. uploaded images, email templates). After the app is created, the file storage location can be modified for the app independently of the account default.

To set the default file storage location for a user’s account, navigate to **My account \> Settings \> Default folder path**. 

To set the default file storage location for an individual app, open the app and navigate to **Info \> Properties \> App Properties \> Default app folder.**

Copy the SharePoint Site ID obtained above and paste into the desired location.

### Update existing applications

There are two methods to move an app’s data from OneDrive to SharePoint.

**Move the data and update each table with the new data location:**

1.  Navigate to the app’s folder in OneDrive.
2.  Right click the folder and select **Move to.**
3.  Specify the new folder in SharePoint and click **Move here**.
4.  After the data is moved, open the app and navigate to **Data \> Tables**.
5.  For each table
    a) Expand the **Storage** section.
    b) Click **Source Path** and locate the spreadsheet in its new SharePoint location.
    c) Click **Worksheet Name/Qualifier **and specify the correct worksheet for the table.

**Update the app owners default file storage location and copy the app:**

1.  Follow the steps in this section to update the app owner’s default file storage location to SharePoint
2.  Open the app to be moved and navigate to **Manage \> Author.**
3.  Click **Copy App** and set the **Save app to** drop-down to **office365**.

AppSheet will create a copy of the app definition and the associated data. The data will be saved to the default file storage location for the user’s account. 

The process can be combined with an [app upgrade](https://support.google.com/appsheet/answer/10105386) if it is important to maintain the same links for end users to access the application.
