---
fonte: https://support.google.com/appsheet/answer/12635312?hl=en
baixado: 2026-11-10
---

# Create, import, and copy databases

Create and copy AppSheet databases as described in the following sections:

- [Create a new database](#create-new-database)
- [Create a database by importing a Google Sheet](#import-google-sheet)
- [Create a database by importing a Microsoft Excel workbook](#import-microsoft-excel)
- [Copy an existing database](#copy-existing-database)
- [Create an AppSheet database when copying an existing app](#copy-existing-app)

### Create a new database

To create a new database:

1.  [*Access the My Apps page*](https://support.google.com/appsheet/answer/12392972).
2.  Select **Create \> Database \> New database**.
    A new database is created and opened in the database editor. It is named **Untitled database**, by default, and contains some basic example data.
3.  Rename the database by clicking the name and editing the contents.
4.  [Manage the database using the database editor](https://support.google.com/appsheet/topic/12631941).

### Create a database by importing a Google Sheet

To create a database by importing a Google Sheet:

1.  [*Access the My Apps page*](https://support.google.com/appsheet/answer/12392972).
2.  Select **Create \> Database \> Import from Sheets**.
3.  Navigate to and select the Google Sheet that you want to import.
4.  Click **Select**.
    The new AppSheet database is created from the Google Sheet and opened in the database editor. Its name defaults to the name of the Google Sheet from which it was copied.
    Up to five worksheets from the Google Sheet will be imported into the AppSheet database.

     

    The pop-up blocker in your browser may prevent AppSheet from automatically opening the database in the database editor. If it doesn't open automatically, navigate to the **Databases** tab and click the database in the list to open it in the database editor.
5.  [Manage the database using the database editor](https://support.google.com/appsheet/topic/12631941).

### Create a database by importing a Microsoft Excel workbook

This is a** preview** release of creating a database by importing Microsoft Excel workbook. See [product launch stages](https://cloud.google.com/products#section-23). Preview offerings are intended for use in test environments only. This feature is not recommended for use in production apps. 

To create a database by importing a Microsoft Excel workbook (`.xls` or `.xlsx`):

1.  [*Access the My Apps page*](https://support.google.com/appsheet/answer/12392972).
2.  Select **Create \> Database \> Import from Excel**.
3.  Navigate to and select the Microsoft Excel workbook that you want to import.
4.  Click **Select**.
    The new AppSheet database is created from the Microsoft Excel workbook and opened in the database editor. The name of the table in the AppSheet database matches the name of the first worksheet in the Microsoft Excel workbook from which it was imported.
    **Notes**:

    - For the preview release, you can only import a single worksheet from a Microsoft Excel workbook. 
    - `Date` and data validation columns are converted to `Enum` columns.

    The pop-up blocker in your browser may prevent AppSheet from automatically opening the database in the database editor. If it doesn't open automatically, navigate to the **Databases** tab and click the database in the list to open it in the database editor.
5.  [Manage the database using the database editor](https://support.google.com/appsheet/topic/12631941).

**Limitations with importing a Microsoft Excel workbook**

The following are **not supported** at this time when importing a Microsoft Excel workbook, and will result in the `Failed to import` error message:

- Multiple columns with the same name
- Unstructured worksheets
- More than 100,000 rows, 1000 columns, or 5000 characters per cell in a worksheet
- Multiple types within a column
- Charts
- Conversion of drop-downs to `EnumLists`

### Copy an existing database

To copy an existing database:

1.  [*Access the My Apps page*](https://support.google.com/appsheet/answer/12392972).
2.  Click **Databases** to view the list of existing databases.
3.  Click the database that you want to copy to open it in the database editor.
4.  Select **Settings  ** Settings icon  \> **Copy database**.
5.  [Manage the database using the database editor](https://support.google.com/appsheet/topic/12631941).

###  Create an AppSheet database when copying an existing app 

[Copy an existing app](https://support.google.com/appsheet/answer/12491039) and select **AppSheet database** in the **Save app to** field to create a copy of the app using an AppSheet database as the data source.
