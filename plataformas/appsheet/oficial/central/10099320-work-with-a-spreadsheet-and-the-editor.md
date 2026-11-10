---
fonte: https://support.google.com/appsheet/answer/10099320?hl=en
baixado: 2026-11-10
---

# Work with a spreadsheet and the editor

A spreadsheet is a common, easy-to-use data source for AppSheet apps. Each spreadsheet consists of one or more worksheets, any of which may be used to store data for a corresponding [data table](https://support.google.com/appsheet/answer/10105821) within the app.

When creating a new app from a spreadsheet, AppSheet will automatically create a data table connected to the first worksheet in the spreadsheet. The app's data tables are described in the app editor in the **Data \> Tables** tab.

An app may use one worksheet, multiple worksheets within a single spreadsheet, multiple worksheets in multiple spreadsheets, or even mix worksheets with [other data sources](https://support.google.com/appsheet/topic/10102124), such as database tables. To add a new data table and connect it to a worksheet, in the app editor, go to the **Data \> Tables** tab.If the app editor is aware of any potential tables already in your data sources, it may offer a shortcut to add them, or you may add a new table manually by clicking **+ New Table**.

Each data table must be connected to a different worksheet or database table. Worksheets may be all in a single spreadsheet, or may be distributed across multiple spreadsheets, as you see fit.

AppSheet extracts tabular column structure from your spreadsheet, and works best when the spreadsheet has regular tabular data: the first row has [well-formatted column headers](https://support.google.com/appsheet/answer/10099523) and the remaining rows are data. Extraneous data, drawings, charts, etc. may cause problems.

In the **Data** section of the app editor, you see a few simple controls.

- Click **View Columns** to view the table columns. AppSheet navigates to **Data \> Columns** pane and expands the table.
- Click **View Source** to open the spreadsheet in a separate browser tab. If you are using Google Sheets, this allows you to edit the Google sheet in one tab while you see the effects on your app in the AppSheet tab.
- Click **View Data**, you see the first few rows of the spreadsheet conforming to the column structure that AppSheet has extracted. Each column has a header name and a data type. Also, one of the columns has been identified as the [unique key](https://support.google.com/appsheet/answer/10106672). The key choice is very important: the unique key helps AppSheet synchronize changes made in the app back to the spreadsheet.
- Click **Delete** to delete the table from the app.

Data \> Tables controls

Every time you refresh the app editor, AppSheet checks your app and shows error, warning, and info messages at the top of the page. Wherever possible, AppSheet tries to automatically inform you of any problems and automatically fix them

When you change the structure of the spreadsheet, AppSheet notices the difference between the spreadsheet and what it expects. So it gives you a warning that there are more columns or fewer columns than the app editor expects. If you are editing the app on our web page, it will try to automatically pick up the new structure. If the extracted column structure is not what you expect, or there are errors/warnings you want to act upon, you would typically make changes to your data in the spreadsheet and then click **Regenerate Structure** for the relevant table in the **Data \> Columns** tab.

You can also choose to **switch to another spreadsheet**. There are several reasons you might do this. For instance, if you start with an example data set for experimentation and now you want to switch to the real data, which might have a different structure, you'll need to regenerate. Another case would be when you want to switch to a different spreadsheet that has identical structure (for example, switching from test data to production data). Finally, you may realize that you need to add or take away a column in order to properly capture the data. In all cases where there's a change in the number of columns, AppSheet detects the new column structure and reacts appropriately to it.

## Use a specific worksheet

In the **Data \> Tables** tab, when you look at the details for the tables in the app, you can provide a specific worksheet name in the **Worksheet Name/Qualifier** field.

If a worksheet with this name is not found in the referenced spreadsheet, AppSheet will default to the first worksheet.

## Use multiple spreadsheets

On the **Data \> Tables** tab, click **+ New Table** to choose another spreadsheet. If you need to use a worksheet from the same workbook you are already using in your app, simply define the sheet name (case included) in the **Worksheet Name/Qualifier** field. The sheet automatically gets added to your app when you save your changes. You can now define control views over this data as well.

Note that you'll need to create a new UX view pointing to the new spreadsheet to get that sheet's data to display in the app.
