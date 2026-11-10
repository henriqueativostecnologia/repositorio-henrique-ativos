---
fonte: https://support.google.com/appsheet/answer/10107843?hl=en
baixado: 2026-11-10
---

# Use data from Smartsheet

AppSheet works well with Smartsheet. For example, AppSheet automatically handles Smartsheet-specific column types like Harvey Ball and Color.

Use your Smartsheet account to sign into AppSheet. You can then build AppSheet apps using your Smartsheet Sheets or Row Reports.

If you are a Smartsheet business customer, the solutions team at Smartsheet can help with your AppSheet integration.

### Create an AppSheet table based on a Smartsheet Sheet

You can add an AppSheet table which is based on a Smartsheet Sheet.

1.  In AppSheet, go to **Data ** and click **+** in the top header of the Data panel.

    We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

    ## If you are using the legacy navigation

    Go to **Data \> Tables **and click **+ New Table**.  

2.  Select **smartsheet**.

3.  In the **Choose a Sheet/Table** dialog box, navigate to and select your Smartsheet Sheet.

4.  AppSheet will create a new table based on your Smartsheet Sheet.

An AppSheet table that is based upon a Smartsheet Sheet supports add, update, and delete.

### Create an AppSheet table based on a Smartsheet Row Report

You can add an AppSheet table which is based on a Smartsheet Row Report.

1.  In AppSheet, go to **Data ** and click **+** in the top header of the Data panel.

    We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

    ## If you are using the legacy navigation

    Go to **Data \> Tables **and click **+ New Table**.  

2.  Select **smartsheet**.

3.  In the **Choose a Sheet/Table** dialog box, navigate to and select your Smartsheet Row Report.

4.  AppSheet will create a new table based on your Smartsheet Row Report.

An Appsheet table that is based upon a Smartsheet Row Report supports both update and delete. However, you cannot add new records to an Appsheet table that is based on a Smartsheet Row Report.

### Use Smartsheet Dropdown (Multi Select) Columns

Smartsheet Dropdown (Multi Select) columns are supported by AppSheet but they require work by the AppSheet application creator.

If your Smartsheet worksheet contains a Dropdown (Multi Select) column and you wish to add or update that column's value using AppSheet, please do the following:

1.  Open the worksheet In Smartsheet.
2.  Click the dropdown icon just to the right of the Dropdown (Multi Select) column name, select **Edit Column Properties ...**, and change the **Column Type** to **Text/Number**.
3.  Open the AppSheet application in the app editor.
4.  Go to the **Data \> Columns** tab and select the table containing the field corresponding to the Dropdown (Multi Select) column.
5.  Set the field's **Type** to **EnumList**. In **Type Details** set the list of allowed values **Values** appropriately. In the **Base type** dropdown select **Text**.

Doing this will ensure that AppSheet can add or update the column value in Smartsheet. This is necessary because when Smartsheet added the Dropdown (Multi Select) feature they did not update their API to fully support the new feature. When you update a Dropdown (Multi Select) field in AppSheet, we call the Smartsheet API to update the column in your Smartsheet worksheet. If the column in the Smartsheet worksheet is of type **Dropdown (Multi Select)** the Smartsheet API returns the error: **`Value is not supported for this column type. Use objectValue instead.`**

When you update the AppSheet `EnumList` field's value and save your changes, AppSheet writes those values as a comma separated list into the corresponding Smartsheet Text column. When AppSheet reads the Smartsheet worksheet. it copies the comma-separated list from the Smartsheet Text column into the appropriate dropdown values in the corresponding AppSheet `EnumList` field.

### Use Smartsheet Dropdown (Single Select) Columns

Smartsheet Dropdown (Single Select) columns are fully supported by AppSheet.

When you add an new table to AppSheet which is based on a Smartsheet worksheet having Dropdown (Single Select) columns, AppSheet automatically creates a corresponding `Enum` type field in the AppSheet table, and populates that `Enum` field's **Values** property with the values from your Smartsheet Dropdown (Single Select) column.

When you update the AppSheet `Enum` field's value and save your changes, AppSheet writes that value into the corresponding Smartsheet Dropdown (Single Select) column. When AppSheet reads the Smartsheet worksheet. it copies the Smartsheet Dropdown (Single Select) column's value into the corresponding AppSheet `Enum` field.
