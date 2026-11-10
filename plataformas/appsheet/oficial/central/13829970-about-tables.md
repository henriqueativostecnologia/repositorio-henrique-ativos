---
fonte: https://support.google.com/appsheet/answer/13829970?hl=en
baixado: 2026-11-10
---

# About tables

The following sections provide an overview of tables in AppSheet:

- [Tables are comprised of columns and rows](#columns-rows)
- [Each table must have a key](#key)
- [You can add multiple tables to your app](#can-add-multiple)
- [Tables can be private](#private)

## Tables are comprised of columns and rows

Tables are comprised of **columns**, which identify the different components of each row. For example, you might want to store the first name, last name, and phone number in your *data source*, such as a spreadsheet, as shown below.
Customers table with First Name, Last Name, and Phone \# columns

**Rows** contain the data for each individual record in your data source. Every time your app users add new data, a new row will be added to the data source. 

**Column headers** are essential to your app: you need column headers for each column in which you want to store data. AppSheet connects to your data source and reads each column header to define the column structure of the app. Normally your column headers should be the first row of your spreadsheet, but AppSheet is capable of finding your headers if they're anywhere near the top of your spreadsheet. See [Effective use of column headers](https://support.google.com/appsheet/answer/10099523).

- Before you add a new table to your app, it's a good idea to open the data source and make the column header row **bold**, which helps AppSheet locate it.
- Every time you change the columns in the data source, you need to regenerate the column structure within the app, or AppSheet won't know how to locate the columns to read and write data and your app will stop functioning. See [Add, rearrange, or delete columns](https://support.google.com/appsheet/answer/10106675).

## Each table must have a key

**[Keys](https://support.google.com/appsheet/answer/10106672)** uniquely distinguish each row from other rows by using a particular column.AppSheet uniquely identifies a row by the value in he key column.

The key may be a single column (such as Employee ID) or of two or more columns (such as FirstName and LastName). Each row in the table must have a key value that uniquely identifies it. In other words, no two rows in a table may have identical key values. This is critical, because keys allow AppSheet to reliably find the right table row.

When a user on a mobile device changes data through an AppSheet app, they're making changes to a local copy of the data temporarily stored on the device. When the user syncs these changes to the server, AppSheet sends the updated data to the server, finds the updated row using its unique key value, and applies those changes to that row. AppSheet can only find the right row because each row has a unique key value.

Using keys as a way to locate rows in the spreadsheet also allows for multiple users adding data at the same time. AppSheet will *serialize* the data going back to the spreadsheet from the app, letting the last person to write in a cell "win".

There are several ways keys can be determined: they can be natural, or calculated depending on the structure of the data and the access permissions to the table. See [Types of keys](https://support.google.com/appsheet/answer/10106672#types).

## You can add multiple tables to your app

Tables can be different worksheets from the same file, or from different data sources, such as other spreadsheets or databases. To learn more about the data sources supported, see [Use multiple data sources](https://support.google.com/appsheet/answer/10106309). To learn more about using multiple worksheets in [How to use multiple sheets in your app](https://support.google.com/appsheet/answer/10106507).

The app editor only recognizes **one** table per worksheet. If you have multiple tables in the same worksheet--a somewhat common pattern in Microsoft Excel and Google Sheets--you'll need to move tables to unique tabs.

## Tables can be private

One consideration to take into account when configuring your table's settings is whether it should be a [private table](https://support.google.com/appsheet/answer/10106508) - maybe you want certain tables to be accessed only by certain individuals in your organization. Disable the **Shared?** setting to make your table private. See [Private tables](https://support.google.com/appsheet/answer/10106508).

Security section of the National Parks table showing the Shared? field, currently enabled
