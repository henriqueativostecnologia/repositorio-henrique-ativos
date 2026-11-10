---
fonte: https://support.google.com/appsheet/answer/10104991?hl=en
baixado: 2026-11-10
---

# Transfer an app between user accounts

You can transfer apps between AppSheet accounts. This is useful if you created an app under one account but wish to transfer it to another account. For example, you may have developed a new application under your own personal AppSheet account but want to deploy the application under another AppSheet account where all deployed applications reside. Having an AppSheet account where all deployed applications reside often makes administration easier.

You can transfer an app:

- From your cloud provider account to another of your cloud provider accounts
- From your cloud provider account to another user's cloud provider account

There are two use cases to consider based on the data sources (Google Drive, Smartsheet, Dropbox, OneDrive, SQL, and so on) used in the app:

- Recipient account has all of the same data sources as the original owner account
- Recipient account does not have all the same data sources as the original owner account

In addition, you can [transfer apps between team members](https://support.google.com/appsheet/answer/12007391).

After the app is transferred, the **original owner** remains a co-author and can edit the app.

## Data sources are available in the recipient account

**Note**: To transfer an app the recipient must have [edit app access](https://support.google.com/appsheet/answer/10104983#manage-roles-app-versions) and the recipient must request the transfer.

To transfer ownership, the **recipient** must do the following:

1.  Open the app in the editor.
2.  Go to **Manage  \> Collaborate & Publish**.
     We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

    ## If you are using the legacy editor

    Go to **Manage \> Author**.  
3.  Expand the **Transfer** section.
4.  Click **Request Transfer**. Transfer requests remain active for 48 hours.

Request transfer button in the Transfer section of the Author pane

To complete the app transfer the **original owner** must then do the following:

1.  Open the app in the editor.
2.  Go to **Manage  \> Collaborate & Publish**.
     We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

    ## If you are using the legacy editor

    Go to **Manage \> Author**.  
3.  Approve the transfer request by clicking **Transfer App**.

### Users of the app should not need to reinstall the app after a transfer

Ensure the recipient has access to the files (such as sheets, images, PDFs) and folders used by the app. Otherwise the app will stop working the moment ownership is transferred.

- If you are working with Google Sheets, share the sheets with the recipient as described [Share files from Google Drive](https://support.google.com/drive/answer/2494822?hl=en&ref_topic=7000947). The recipient must accept the shared sheet using **Add to my Drive**. Alternatively, you can transfer ownership of the sheets to the recipient as described in [Make someone else the owner of your file](https://support.google.com/drive/answer/2494892?co=GENIE.Platform%3DDesktop&hl=en).
- If you are working with spreadsheets from Dropbox, the process is different. Each table in your app references a spreadsheet in Dropbox based on its filepath (not an ID). So it is important that the recipient moves the spreadsheets to the same filepaths on their Dropbox account. For example, if the original app used a spreadsheet at `/appsheet/data/myapp/mysheet.xlsx`, then it is not enough to just share this file with the recipient. The recipient would actually need to move or copy the file to a file called `/appsheet/data/myapp/mysheet.xlsx` in their Dropbox account.

If your app uses image files referenced by name in spreadsheet cells, the image file names stored in the spreadsheet are relative to the location of the spreadsheet. The recipient's Images folder must be placed in the proper folder location so the relative paths are correct. Otherwise, images will not be rendered correctly in the app. Further, if the app captures images, the images will be stored in an Images subfolder. You must share/transfer the Images subfolder with the recipient as well. The process of sharing/transferring the Images subfolder is identical to the process of sharing/transferring the spreadsheet.

## Data sources are not available in the recipient account

You will need to share the app with the recipient with **View/copy app** or **Edit app** access, as described in [Share your app with individual users](https://support.google.com/appsheet/answer/10104983#share-individual-users). The recipient will see the app under the **Shared with me** section on the My Apps page.

The recipient can select **More**   **\> Copy** to copy the app on the My Apps page.
This copies the app, the app date, and everything associated with the app to the recipient.

This creates a completely new copy of the app. Users of the app must reinstall the new app after such a transfer.
