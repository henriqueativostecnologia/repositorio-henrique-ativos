---
fonte: https://support.google.com/appsheet/answer/10106767?hl=en
baixado: 2026-11-10
---

# Use data from Airtable

You can create apps in AppSheet with data from Airtable. To do this, you need to first add an Airtable data source to your AppSheet account. 

- [Add an Airtable data source](#add-airtable-data-souce)
- [Supported Airtable data types](#data-types)
- [Airtable attachments](#airtable-attachments)

## Add an Airtable data source

To add an Airtable data source to your AppSheet account:

1.  Go to the **My Account \> Sources** tab.
2.  Click **+ New Data Source**.
3.  Enter a name for the data source and click **Airtable**.

To connect to Airtable, you need to provide the following information:

1.  Your Airtable Personal Access Token
2.  The ID of your Airtable base
3.  The names of tables in your Airtable base

To learn how to obtain your **Airtable Personal Access Token**, see [Understanding Personal Access Token basic actions](https://support.airtable.com/docs/creating-and-using-api-keys-and-access-tokens) on the Airtable site.

To obtain the ID of your Airtable base, open the [Airtable Standard API](https://airtable.com/api) page and click the Airtable base that you want to use. This will open the API page of the base.

Airtable Standard API page

The base ID can be found in the URL of the API page of the base. In the URL, the base ID is immediately after `https://airtable.com/` and starts with `app`.

Locating the base ID in the URL

Finally, type in the names of the tables in your Airtable base. The table names must be separated by commas. Test and save the connection.

Add Airtable connection information dialog

Once you have added your Airtable data source, click **+ Make a new app** on the **My Apps** page, select your Airtable data source, and you'll be able to create an app using one of the tables in Airtable that you have added.

Select a table and AppSheet will analyze the table and attempt to create a new app using the table's data. If the table is empty, that is, the table has no rows, AppSheet won't be able to analyze the table. If the table isn't empty but contains blank columns, all blank columns will be skipped by AppSheet. Therefore, to enable AppSheet to analyze and derive the column structure of the table you select, you must ensure that there is at least one row in the table that contains no blank column.

## Supported Airtable data types

When you add a new table from Airtable to your app, AppSheet will analyze the data types of the table's columns, and will map these data types to their corresponding AppSheet data types. Below is a list of Airtable data types that are currently supported by AppSheet and their default AppSheet counterparts. Note that for certain Airtable data types, such as `Currency`, you can override the default types selected by AppSheet and choose a more appropriate type, such as `Price`.

1.  Single line text: `Text`
2.  Long text: `Text`
3.  Attachment: `Image` or `File`
4.  Checkbox: `Yes/No`
5.  Single select: `Text`
6.  Multiple select: `Enum List`
7.  Collaborator: `Email`, `Name`
8.  Date or Created Time without time field: `Date`
9.  Date or Created Time with time field: `DateTime`
10. Phone number: `Phone`
11. Email: `Email`
12. URL: `URL`
13. Number: `Decimal`
14. Currency: `Decimal`
15. Percent: `Decimal`
16. Rating: `Decimal`
17. AutoNumber: `Number`
18. Barcode: `Text`
19. Formula: the AppSheet data type is determined by the output data type of the formula

Certain Airtable data types allow the user to store multiple values per cell. For instance, multiple images or files can be stored in a single cell of an `Attachment` column. Except for multi-select columns, this behavior is currently not supported by AppSheet.

The values of Airtable columns of type `Created Time`, `AutoNumber`, and `Formula` are automatically computed by Airtable. As such, these columns must be marked as read-only in AppSheet. Any attempt to edit these columns via an AppSheet app will result in an error.

## Airtable attachments

Airtable differs from other cloud storage providers, such as Google, in that it does not have a file system. In the case of Airtable, images and files are always stored in the main cloud file system associated with the app creator's primary AppSheet account, be it Google Drive, Dropbox, Office 365, or Box.

When your AppSheet app captures and saves an image or file, AppSheet creates a new file in the main cloud provider's file system for each image or file, and writes the image or file data to that file. It then places the URL of this file into the attachment column in Airtable. The files will be saved in a sub-folder of your account's default folder path (usually *`../appsheet/data`*). You can view and change the default folder path in your My Account page under the **Settings** tab.

Note that files or images that are added directly to Airtable will be saved in Airtable's server instead of your cloud storage provider's.
