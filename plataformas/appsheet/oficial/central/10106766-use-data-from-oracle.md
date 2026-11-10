---
fonte: https://support.google.com/appsheet/answer/10106766?hl=en
baixado: 2026-11-10
---

# Use data from Oracle

AppSheet can build apps from Oracle databases hosted in Oracle Cloud, Amazon RDS, or other cloud hosting provider that supports Oracle. To use data from Oracle in your app, you must first add an Oracle data source to your account.

## Add an Oracle data source

To add an Oracle data source to your AppSheet account:

1.  Go to the **My Account \> Sources** tab.
2.  Click **+ New Data Source**.
3.  Enter a name for the data source and click **Cloud Database** or **On-premises Database**.
    The Add database connection information dialog displays.
4.  Configure the database connection information. 
    - **Type**: Select **Oracle**.
    - **Server**: Enter the Oracle database server hostname or IP address.
    - **Database**: Enter the database name.
    - **Username**: Enter the username of the database user.
    - **Password**:Enter the password for the database user.
5.  Click **Test** to test the connection details.
6.  After a successful test, click **Authorize Access** to save the data source in your AppSheet account.

If you don't specify any port number with the server address, AppSheet will assume the database uses the default port `1521`; if a different port is used, it must be included in the server address. Below is an example of a server address with port number `8000`:

`myoracledb.cfq3vjtjkq6z.us-west-2.rds.amazonaws.com:8000`

In order for AppSheet to access the database, the Oracle instance must be hosted in the cloud (Oracle Cloud, Amazon RDS, or other cloud hosting provider), and both the network and the Oracle instance must accept inbound connections to the database from AppSheet servers. Please refer to [Manage IP address and firewall information](https://support.google.com/appsheet/answer/10104492) for further information.

Once an Oracle data source has been added to your account, you can add tables or views in the data source to any app. When you choose *Add Table* in the app editor, you can select the specific data source, and a table or view from that data source.

Once added to the app, AppSheet treats all data sources similarly. In fact, it's common and natural to combine data from an Oracle data source with data from other sources in the same app.

## Use Oracle on Amazon RDS

If your database is running on AWS, ensure that **Network Security** option **Publicly Accessible** is set to **Yes***.* Then create inbound rules to accept all traffic from AppSheet's IP addresses, which can be found in [Manage IP address and firewall information](https://support.google.com/appsheet/answer/10104492)*.*

AWS Create Security Group dialog

AWS Edit inbound rules dialog

## Work with identity columns

Starting with Oracle Database 12c release 1 (12.1), Oracle tables can use `IDENTITY` columns as key columns. The values of an `IDENTITY` column are auto-incrementing numbers that get automatically inserted by the database.

Oracle tables with `IDENTITY` columns can pose a problem when used in AppSheet. By default, SQL doesn't let an application define the `IDENTITY` column value. However, with AppSheet, new rows are created in the app when it's potentially offline and may only be synced later, so the app needs to be able to assign key/`IDENTITY` values.

The best solution is to avoid `IDENTITY` column keys altogether in your database schema. Instead, use a column that is an `NVARCHAR2(8)` (or in general an `NVARCHAR` of length greater than or equal to 8). In AppSheet's column definition for this key, give it an initial value of [`UNIQUEID()`](https://support.google.com/appsheet/answer/10107368). Now unique key values can be assigned by the app and inserted into the backend database.

If the database must use `IDENTITY` columns, it's preferable to create them with a large initial seed. For example, use `START WITH 100000` to set the initial value of the column to 100000. In AppSheet's column definition for this key, give it an initial value of `RANDBETWEEN(10000, 99999)`. Now any records created from your app will have five digit values that lie randomly in the range 10000 to 99999, while records created directly against the database will have higher values.

If the database schema cannot be changed and if there is already an `IDENTITY` column being used with the default initial seed (of 1), we recommend you follow the same approach as described earlier. However, you can first manually increment the `IDENTITY` seed as follows:

`ALTER TABLE `*`tablename`*` MODIFY (`*`columnName`*` GENERATED START WITH 100000)`

This should "re-seed" the `IDENTITY` column to the desired range. Your AppSheet app will insert values in the range specified by the [`RANDBETWEEN()`](https://support.google.com/appsheet/answer/10107982) function in the initial value of your AppSheet column definition.

## Save files created in the app

Database servers differ from the rest of our cloud storage providers in that they do not have a file system. This leads to a change in AppSheet behavior when saving files (like images and documents). If the app has to capture photographs, they're normally stored in a folder next to the source of data in cloud storage. However, in the case of an Oracle table, image and document files are stored in the main cloud file system associated with the app creator's primary AppSheet account (typically Google Drive/Dropbox/Office 365/Box). The files will be saved in a subfolder of your account's default folder path (usually `/appsheet/data`). You can view and change the default folder path in your **My Account** page under the **Settings** tab.
