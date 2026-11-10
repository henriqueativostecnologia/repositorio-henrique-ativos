---
fonte: https://support.google.com/appsheet/answer/11568421?hl=en
baixado: 2026-11-10
---

# Archive files created from a bot

The [Create a new file](https://support.google.com/appsheet/answer/11512511) task archives each file that it creates. The following sections provide more details:

- [How the file name is formed](#filename-formed)
- [How the folder name is formed](#foldername-formed)
- [How the complete folder and file path is formed](#complete-file-foldername-formed)
- [View the folder and file names in Audit History](#view-file-folder-names-audit-history)
- [Create an action to open a saved file](#create-action-open-saved-file)

For more information about the settings described, see [Create and save a file from an automation](https://support.google.com/appsheet/answer/11512511).

## How the filename is formed

The filename is formed by combining the **File Name Prefix** value, the timestamp (if **Disable Timestamp?** is disabled) formatted as *yyyyMMdd_HHmmss_fff*, and the file extension for the **HTTP Content Type**.

For example, if the **File Name Prefix** is set to **MyFileName** and the **HTTP Content Type** is **PDF**:

- If **Disable Timestamp?** is disabled, the archive attachment filename is: `MyFileName20190207_133355_804.pdf`
- If **Disable Timestamp?** is enabled, the archive attachment filename is: `MyFileName.pdf`

## How the folder name is formed

The folder name in which the file is stored is formed using the **default app folder** and the **File Folder Path** property.

To configure the default app folder, select **Settings ** Settings icon **\> Information**, and under **App properties** enter a value in the **Default app folder** setting. For example:

We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

## If you are using the legacy navigation

To configure the default app folder, select **Info \> Properties**, expand **App Properties**, and enter a value in the **Default app folder** property.

**Examples:**

If the **Default app folder** is `/1track/data/MyApp-24403/MyDefnFolder1`, and the **File Folder Path** is `MyFolderA/MyFolderZ`, then the folder name is:

    /1track/data/MyApp-24403/MyDefnFolder1/MyFolderA/MyFolderZ

If the default app folder is `/1track/data/MyApp-24403` and **File Folder Path** is not defined (defaults to `Files`), then the archive folder name is:

    /1track/data/MyApp-24403/Files

## How the complete folder and file path is formed

The complete folder and file path is formed by combining the **Folder Name** and **File Name** values.

**Examples:**

If the Folder Name is `/1track/data/MyApp-24403/Files` and the filename is `PurchaseOrder20190207_133355_804.pdf`, then the file and folder name is:

    /1track/data/MyApp-24403/Files/PurchaseOrder20190207_133355_804.pdf

 

If the Folder Name is `/1track/data/MyApp-24403/MyFiles/PurchaseOrdersByMonth_2019_02` and the filename is `PurchaseOrder20190207_133355_804.pdf`, then the archive file and folder name is:

    /1track/data/MyApp-24403/MyFiles/PurchaseOrdersByMonth_2019_02/PurchaseOrder20190207_133355_804.pdf

## View the folder and file names in the Audit History

View the file by [checking the audit history log](https://support.google.com/appsheet/answer/10104794). Customize the dashboard settings and look for an audit record related to the **Create a new file** task. The **FileName** value indicates the folder and file path where the file was archived.

**Note**: You may need to wait for up to five minutes for the audit record to appear. AppSheet groups audit records before writing them to the audit history log to reduce overhead. This can result in a delay before an audit record appears in the audit history. If you don't see an audit record, click **Search** periodically to refresh the audit history log.

## Create an action to open a saved file

You can create an action to open a saved file.

1.  Configure a [Create a new file](https://support.google.com/appsheet/answer/11512511) task.
    To create an action button that opens the file, the filename needs to be repeatable and unique. To ensure that the filename is unique, disable the timestamp and set the filename using a formula based on the [key](https://help.appsheet.com/en/articles/1023086-what-is-a-key) column. For example: `CONCATENATE(“PurchaseOrder_”, [ID])`
2.  Where `ID` is the name of the key column of the table.
3.  Add a column to your table to store the PDF filename. For example, call the column `FileName` and set its type to `File`.
4.  [Create a data change action](https://support.google.com/appsheet/answer/10107706#data-change) to set the file `FileName` column. The action must be of type: **Data: set the values of some columns in this row**. Use a formula to set the value to the relative file path of the file.

    For example, if the relative file path is: `/MyFolderA`

    And filename is: `CONCATENATE(“PurchaseOrder_”, [ID])`

    Then the formula should be: `CONCATENATE(“MyFolderA/”, “PurchaseOrder_”, [ID], “.pdf”)`
5.  Create an **Open File** action. The action must be of type: [External: open a file](https://support.google.com/appsheet/answer/10107706#external-open-file). Set `File` to point to the column that you created to store the filename. For this example, the formula would be: `[FileName]`
6.  Return to the bot that saves the file and add an action. Set the **Reaction** to **Change Data** and select the action you created in step 3.

When the bot is triggered, it will archive the file with the relative file path and filename you specified. It will save the file path and filename in the column you created. When you click the **Open File** action, it will retrieve the relative file path from that column and open that file.
