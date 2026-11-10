---
fonte: https://support.google.com/appsheet/answer/11542175?hl=en
baixado: 2026-11-10
---

# Archive email attachments to Microsoft SharePoint

Archive your email attachments to Microsoft SharePoint by setting a SharePoint folders as your Default App Folder. This requires that you determine the SharePoint folder location.

To archive email attachments to Microsoft SharePoint:

1.  Determine the SharePoint folder location:

    1.  Go to Microsoft SharePoint.
    2.  Select a SharePoint site and optionally a folder within that site.
    3.  Create an Excel workbook in the SharePoint folder.
    4.  Open your existing AppSheet app in the app editor.
    5.  [Add a table](https://support.google.com/appsheet/answer/10105821).
    6.  In the **Get data from** dialog, select your Microsoft provider.
    7.  Select **SharePoint**.
    8.  Browse to your SharePoint site and folder.
    9.  Select the Excel workbook you added earlier.
    10. Select your newly added table in the Data panel.
    11. Click **Table settings**  Table settings icon  in the table header
    12. Under **Storage**, copy the first part of the **Source Id** property.
        This value starts with `SHAREPOINT_SITE_ID`. If you specified a folder, include the folder name, but omit the worksheet file name.
    13. Delete the newly added table, if desired.

2.  Go to **Settings \> Information**.

3.  Under **App Properties**,** **enter the `SHAREPOINT_SITE_ID` value (copied in **step 1l**) into the **Default app folder** property.

We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

## If you are using the legacy editor

To archive email attachments to Microsoft SharePoint:

1.  Determine the SharePoint folder location:

    1.  Go to Microsoft SharePoint.
    2.  Select a SharePoint site and optionally a folder within that site.
    3.  Create an Excel workbook in the SharePoint folder.
    4.  Open your existing AppSheet app in the app editor.
    5.  [Add a table](https://support.google.com/appsheet/answer/10105821).
    6.  In the **Get data from** dialog, select your Microsoft provider.
    7.  Select **SharePoint**.
    8.  Browse to your SharePoint site and folder.
    9.  Select the Excel workbook you added earlier.
    10. Go to the **Table \> Data** tab.
    11. Select your newly added table.
    12. Expand **Storage**.
    13. Copy the first part of the **Source Id** property.
        This value starts with `SHAREPOINT_SITE_ID`. If you specified a folder, include the folder name, but omit the worksheet file name.
    14. Delete the newly added table, if desired.

2.  Go to the **Info \> Properties** tab.

3.  Expand **App Properties**.

4.  Enter the `SHAREPOINT_SITE_ID` value (copied in **step 1m**) into the **Default app folder** property.
