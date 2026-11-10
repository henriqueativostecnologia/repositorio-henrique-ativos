---
fonte: https://support.google.com/appsheet/answer/10105777?hl=en
baixado: 2026-11-10
---

# Errors and warnings during Sync

Sync has four stages:

1.  The client prepares the change data to be Synced to the server.
    This stage is usually quick. When this stage finishes, the Sync progress bar is about 1/4 complete.
2.  The client sends the change data to the server and the server processes the change data and any [app events](https://support.google.com/appsheet/answer/11445188#data-change-events) that are triggered.
    This stage may take a long time depending on the complexity of the changes being performed and the automation events, if any, that are triggered. When this stage finishes, the Sync progress bar is about 1/2 complete.
3.  The client fetches the latest application definition and application data from the server.
    This stage can take a while, but it normally takes less time than stage 2. When this stage finishes, the Sync progress bar is about 3/4 complete.
4.  The client processes the application definition and application data returned by the server.
    This stage is usually quick.

Most Sync errors occur in the second stage:

- If there are network errors between the client and the server, the Sync is retried a few times. If the failure persists, the Sync is halted. The solution is to retry later when connectivity is better.
- If you have poor connectivity or if large images have to be sent as part of the Sync, this step can take a long time and can potentially timeout. The solution is to retry later when connectivity is better.

You can always retry a failed Sync request.

## Error: A duplicate request is already in progress

When the AppSheet client submits a Sync request to the AppSheet server, the client includes a `RequestId` that uniquely identifies that client Sync request. When the AppSheet server receives the Sync request, it remembers the Sync request and its `RequestId`. The server then goes on to process the client Sync request.

If the client Sync request takes a long time to process, the client may resubmit the Sync request. The client may also resubmit the Sync request if it loses network communication with the server. In either event, when the client resubmits the Sync request, the server uses the `RequestId` in the Sync request to check the list of in flight client Sync requests. 

If the server has already completed the client Sync request, the server returns the same Sync response it returned for the original client Sync request. This ensure that the client Sync request is only performed once by the server, and that the client receives the same Sync response every time is submits the same Sync request. 

If the server detects that the client request is still being processed, it returns the warning:

`A duplicate request is already in progress`

This tells the client that the server is still  processing the original Sync request. The client will wait and later retry the Sync request. 

So long as the server is still processing the original client Sync request, each client Sync retry will get the warning response `A duplicate request is already in progress`. Once the server completes the original Sync request, the client will get the appropriate Sync response.

If you are seeing this warning repeatedly, check the [Performance Profile](https://support.google.com/appsheet/answer/10104997) to see why the client Sync requests is taking so long to complete. This warning may signify that the add, update, or delete is taking a long time to process. It may also signify that the add, update, or delete is triggering an automation that is taking a long time to process.

## Error: Unable to fetch data

If your users see errors like this during sync:

`The remote server returned an error: (403) Forbidden`

it means that our service is unable to fetch the data from your cloud service (such as, Google Sheets) because the cloud service has explicitly denied permissions. There are two possible reasons:

1.  You have enabled the **run as app user** security option in your app. Therefore, our service tries to access the data using the identity of the user of the app. And this app user does not have access to the data/spreadsheet. This option (run as app user) should be used only for extra security and in these situations, such a failure is appropriate.
2.  Your app creator account has been denied permission to access the data or spreadsheet in the cloud service. This can happen if you built the app from a shared spreadsheet and someone else removed your access to the sheet.  

## Error: Unable to update row

If you have made changes in the app and Sync, you may see an error of the form:

`Unable to update row in table 'Your-Table-Name'. Execution of request failed: https://spreadsheets.google.com/feeds/cells/....... Unable to complete sync`.

The error may say:

`Google sheets service seems to be unresponsive`

This error occurs when the AppSheet backend is unable to send your changes to the cloud storage provider (in this case, Google Sheets). Almost always, this is because the request times out. If this error occurs often, it is usually a clear sign that there are complex cross-sheet formulas in the Google Sheet. Making a simple update to the sheet takes a lot of time to complete because all the formulas are recomputed by Google Sheets. You will need to simplify your Google Sheet, in particular avoiding some cross-sheet formulas. 

## Error: This change cannot be applied

The following message is displayed if a client attempts to sync after the app definition has been changed on the server:

`This change cannot be applied because there is a newer version of your app`

For example, you will see this message if columns have been added or removed from a table and the client is not using the latest version of the application. You may also see an error message indicating that the number of columns is incorrect or that a column is missing. The local changes queued on the device cannot be applied by the server when this happens.

You can verify this by comparing the app and backend application version numbers. You can obtain the app version number by clicking the menu at the top left and selecting **About**. You can obtain the backend application version number by opening the application in the editor and going to the **Info \> Properties** pane.

There are two possible remedies when this occurs. With both the remedies, the changes queued up in the app will be copied to a recovery file and will need to be manually applied to the spreadsheet.

## Recovery mode

With this option, you will place the app in **Recovery Mode** to allow the sync to proceed. Follow the steps below:

1.  Open the app in the app editor.
2.  Go the **Manage \> Deploy** pane of the app editor.
3.  Click **Switch to recovery mode**.
4.  On the device where the sync fails, try the sync again. This time, it should go through successfully. 
5.  On the **Manage \> Deploy** pane, click **Return to normal mode**.
6.  You will find a special `_recoveryData` folder within the root folder for the app (in the app owner's cloud file system). The changes from the app will be saved to files in this recovery folder. Note that row images will still be saved in the app's usual image folder.
7.  Now examine the row values from the recovery folder and copy them to the spreadsheet as appropriate. The row values are saved in JSON format. You might want to copy these into an online service to convert them into a tabular format that is convenient to copy into a spreadsheet.

## Manual recovery

**Note**: Manual recovery is not supported for [desktop browsers](https://support.google.com/appsheet/answer/12407883). 

As an end-user of the app,  you can manually abandon the changes on a **mobile** device following the steps below:

1.  First capture the app's changes by clicking **Show Changes** in the  menu at the top left of the mobile app. This will allow you to send yourself or the app owner a copy of the changes via email, so that someone can manually process the changes and add them to the data source.
2.  This will also create a copy of the changes in a special `_recoveryData` folder in the root folder for the app (in the app owner's cloud file system). 
3.  In the app, click **Reset Changes** in the menu. This will permanently discard the queued up changes and synchronize the app with the backend.
