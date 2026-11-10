---
fonte: https://support.google.com/appsheet/answer/16701354?hl=en
baixado: 2026-11-10
---

# Work with a shared drive

Many AppSheet users use a Google Drive as their cloud file system. 

Google Drive has a feature called a **shared drive** that allows a team of users to share a common cloud folder hierarchy. When appropriately configured, each user sees not only My Drive, but also one or more shared drives. AppSheet apps can also utilize data from a shared drive.

### Use a spreadsheet from a shared drive

When choosing to add a spreadsheet as a table in your app, the Google file picker will automatically show you any available shared drives in addition to My Drive. Simply browse into a shared drive and select a spreadsheet. AppSheet will work seamlessly with that data.

### Use a shared drive as the root folder of an account

Every AppSheet account has a **Default folder path**, which is defined on the **My account \> Settings** page. The root folder path defaults to `/appsheet/data`. Every app created by your account results in a subfolder created within that root folder. For example, an application called MySales for user 123456 will result in a folder of the form `/appsheet/data/MySales-123456`.

This root folder path can be configured to use a shared drive. This is useful for managing many apps in a team. By ensuring that the application folders live in a shared drive, the organization can ensure that apps can be easily transferred and will continue to run, even if the original app creator leaves the organization.

To use a shared drive as the root folder of an account, set the **Default folder path** using the following format:

`/[TeamDrive]`*`shared-drive-name`*`/appsheetdata`

Where *`shared-drive-name`* is the name of the shared drive.

For example, if you have a shared drive called `MyTeamDrive` associated with the Google Drive of the AppSheet account, set the **Default folder path** as follows: 

`/[TeamDrive]MyTeamDrive/appsheetdata`

When a new app is created in this account, it will have a folder called `/appsheetdata/MySales-123456` created within the `MyTeamDrive` shared drive.
