---
fonte: https://support.google.com/appsheet/answer/10106599?hl=en
baixado: 2026-11-10
---

# Use data from SQL Server

AppSheet can build apps from Microsoft SQL Server databases that are hosted in Amazon AWS, Microsoft Azure, or another cloud-hosting provider.

## Add an SQL Server data source

To add an SQL Server data source to your AppSheet account:

1.  Go to the **My Account \> Sources** tab.
2.  Click **+ New Data Source**.
3.  Enter a name for the data source and click **Cloud Database** or **On-premises Database**.
    The Add database connection information dialog displays.
4.  Select **SQL Server** from the **Type** drop-down menu.

To add an SQL Server data source, you'll be prompted to provide a server name, database name, username, password, and whether Secure Socket Layer (SSL) communication is required. The system stores these values securely, and concatenates them to construct a connection string to the database

In order for AppSheet servers to access your data, both your network and SQL Server must accept inbound connections to the database from AppSheet servers. See [Manage IP address and firewall information](https://support.google.com/appsheet/answer/10104492).

If your database is running on AWS, ensure that **Network Security** option **Publicly Accessible** is set to **Yes** and add a **Security Group** rule for the server that allows the AppSheet server IP addresses.

- SQL Server has a default port of `1433`. If a non-default port number is being used, it should be provided as part of the server name. For example, if the instance is running on port `2000`, use **mycomputer.test.xxx.com,2000** as the server name.

- If a non-default instance name is being used for the SQL Server, provide that as part of the server name. So for example, if the instance is called **myInstance**, use **mycomputer.test.xxx.com\myInstance** as the server name.

Once an SQL Server data source has been added to your account, you can add SQL Server tables or views to any app. When you add a new table in your app, you can select the specific data source, and a table or view from that data source.

Once added to the app, AppSheet treats all data sources similarly. In fact, it's common and natural to combine data from an SQL Server data source with data from other sources in the same app.

## Database identity columns

It's common for a database table to use an `IDENTITY` column as a key. The values of the `IDENTITY` column are auto-incrementing numbers that get automatically inserted by the database. When you use such a table with AppSheet, there can be a problem. By default, SQL doesn't let an application define the `IDENTITY` column value. However, with AppSheet, new rows are created in the app when it's potentially offline and may only be synced later. So the app needs to be able to assign key/`IDENTITY` values. This problem isn't new and every app framework that enables offline access data entry has to deal with it.

The best solution is to avoid `IDENTITY` column keys altogether in your database schema. Instead, use a column that is an `NVARCHAR(8)` (or in general an `NVARCHAR` of length greater than or equal to 8). In AppSheet's column definition for this key, give it an initial value of [`UNIQUEID()`](https://support.google.com/appsheet/answer/10108209). Now unique key values can be assigned by the app and inserted into the backend database.

If the database must use `IDENTITY` columns, it's preferable to create them with a large initial seed. For example, `IDENTITY(100000, 1)`. In AppSheet's column definition for this key, give it an initial value of `RANDBETWEEN(10000, 99999)`. Now any records created from your app will have five digit values that lie randomly in the range `10000` to `99999`, while records created directly against the database will have higher values. Note that when your app is being synced, AppSheet will turn on the `IDENTITY_INSERT` property for the table, insert a new row and then turn it off again. There are restrictions on how many of these operations can occur concurrently, so if this is a high-traffic app, errors could occur. In these situations, we again advise that an `NVARCHAR(8)` column should be used as the key instead.

If the database schema cannot be changed and if there is already an `IDENTITY` column being used with the default initial seed (of 1), we recommend that you follow the same approach as described earlier. However, you can first manually increment the identity seed as follows:

`SET IDENTITY_INSERT `*`tablename`*` ON; INSERT INTO `*`tablename`*` (`*`col1Name`*`, `*`col2Name`*` ...) VALUES(100000, ....); SET IDENTITY_INSERT `*`tablename`*` OFF;`

Delete the row just inserted

This should "re-seed" the identity column to the desired range. Your AppSheet app will insert values in the range specified by the [`RANDBETWEEN()`](https://support.google.com/appsheet/answer/10107982) function in the initial value of your AppSheet column definition.

## Date-time columns

There are 2 main data types to store date-time values in SQL Server: `DATETIME` and `DATETIME2`. The `DATETIME` type only accepts date-time values between `01/01/1753 00:00:00` and `12/31/9999 23:59:59`. On the other hand, the `DATETIME2` type allows a much larger range, from` 01/01/0001 00:00:00` to `12/31/9999 23:59:59`. In general, we recommend that you use `DATETIME2` instead of `DATETIME` in your database, especially if you expect your app to work with dates before `01/01/1753`. Another common pitfall using date-time in SQL Server is how date-time inputs are typed into the app. Some browsers, such as Firefox, do not provide a date-time picker. Instead, the user will have to manually type in date-time values. This might lead to typos or formatting errors, which would cause SQL Server to reject the input date-time values.

For instance, a common typo is to type `0217` instead of `2017`. In this case, if `DATETIME` is used in the database, the year value will be rejected. If `DATETIME2` is used in the database, the value will be accepted even though it's incorrect.

Another common formatting error is to type in 2-digit year values, such as `04/17/17` instead of `04/17/2017`. In this case, the server will interpret the year to be `0017` instead of `2017`. If `DATETIME` is used in the database, the year value will be rejected. If `DATETIME2` is used in the database, the value will be accepted even though it's incorrect.

## Image and file columns

AppSheet treats image and file columns in a special way. When your AppSheet app captures and saves an image or file, AppSheet creates a new file on the provider's file system for each image or file, and writes the image or file data to that file. It then places the name of this file into the image or file column in your SQL table. Finally, it writes the image or file column value to your SQL database. The files will be saved in a subfolder of your account's default folder path (usually `/appsheet/data`). You can view and change the default folder path in your account page under the **Settings** tab.

Database providers differ from other cloud storage providers in that they do not have a file system. In the case of an SQL Server provider, images and files are always stored in the main cloud file system associated with the app creator's primary AppSheet account, be it Google Drive, Dropbox, Office 365, or Box.

If your AppSheet app captures images or files, your database table must include a `VARCHAR` or `NVARCHAR` column to store the file name of the saved image or file.
