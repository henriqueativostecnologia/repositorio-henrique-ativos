---
fonte: https://support.google.com/appsheet/answer/10106311?hl=en
baixado: 2026-11-10
---

# Use data from Excel spreadsheets in Office 365 and SharePoint

**Note**: AppSheet supports Excel `.xlsx` files. It does not support Excel `.xls` or `.xlsm` files.

You can add an Excel spreadsheet to your app by selecting it in the file picker in the app editor. First, select OneDrive or SharePoint depending on where your spreadsheet is located (select OneDrive if you're using data from Office 365).

Once you have made your selection, the files and folders in your OneDrive/SharePoint account will be listed. 

Choose a sheet or table dialog showing OneDrive

For SharePoint, the sites and sub-sites will also be listed.

Choose a sheet or table dialog showing SharePoint

 

While this process is mostly seamless, there are some specific behaviors of which you should be aware:

 

**Office 365**

 

With Office 365, if a user has the spreadsheet open for editing, other users and third-party apps like AppSheet can't make updates to the spreadsheet. Consequently, if you intend to build an app that updates the data (as most apps do), make sure to close the spreadsheet first. Otherwise, you'll see conflict (`409`) error messages and the app won't be able to save changes to the spreadsheet.

 

In order to connect an Office 365 data source to AppSheet, an admin managing your organization's Office 365 account may be required to approve AppSheet as an OAuth app. [Instructions on how to approve AppSheet in your Office 365 settings are available here](https://docs.microsoft.com/en-us/cloud-app-security/manage-app-permissions).

 

**SharePoint**

 

If using SharePoint, note that AppSheet can only access files and folders that are stored in the default drive, typically the "Documents" document library, of a SharePoint site or sub-site. Contents that are stored in user-created drives are currently not accessible.

 

In most cases, if you create a file or folder directly in a SharePoint site, the file/folder will automatically be created in the default drive of the site for you. Additionally, if a SharePoint site has been migrated to an on-premises server, it will no longer be accessible to AppSheet.

See also: [Use multiple data sources](https://support.google.com/appsheet/answer/10106309)
