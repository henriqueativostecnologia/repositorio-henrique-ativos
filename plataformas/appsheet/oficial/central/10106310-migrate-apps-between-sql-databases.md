---
fonte: https://support.google.com/appsheet/answer/10106310?hl=en
baixado: 2026-11-10
---

# Migrate apps between SQL databases

If you need to migrate the data of your app from one SQL database to another, you can do so using AppSheet. The methods described in this article assume both the original and destination databases have already been created and added as data sources to your AppSheet account.

There are two possible scenarios: the destination tables do not yet exist, or they've already been created in the destination database.

## Scenario 1: Destination tables do not exist

If the destination tables do not exist, the easiest way to migrate your app from one database to another is to copy the app using the AppSheet editor and specify the new destination database. When the editor copies the app, it will automatically create the necessary tables in the destination database and write all of the app's data to these tables. To learn how to do this, see [Copy an existing app to an SQL database](https://support.google.com/appsheet/answer/10107300).

## Scenario 2: Destination tables already exist

If the destination tables already exist, you'll need to re-configure each table in your app to connect them to their corresponding SQL tables in the new database.

For each table, first click on the table's source path and select **browse for more data** in the drop-down menu.

Select brows fro more data in the Source Path drop-down

In the data source selection dialogue, choose the destination database, and then select the correct destination SQL table for your AppSheet table.

When setting-up and choosing SQL tables in the destination database, you must ensure the new SQL tables are compatible with the existing AppSheet tables in your app. Below is a checklist to help determine the compatibility of your tables:

1.  All columns in the AppSheet table must exist in the destination SQL table under the same names.
2.  The columns in the SQL table do not need to be in the same order as the columns in the AppSheet table.
3.  It's possible for the SQL table to have columns that do not exist in the AppSheet table. However, this is not recommended.
4.  For each column, the column's data type in AppSheet must be compatible with the SQL data type. For example, if your AppSheet column is of type `Number`, the corresponding SQL column must be a numeric type, such as `Integer` or `Decimal`.
5.  The AppSheet table and the SQL table do not need to have the same name.

Once you have reconfigured all of the app's tables to connect to the new tables in the destination database, your app will be completely migrated.

## Database types and file storage

The methods described in the scenarios above will still work even if you need to migrate your app from one database type to another. For instance, it's entirely possible to migrate your app from a MySQL database to a PostgreSQL database. Likewise, it's possible to migrate your app between different SQL hosting services, such as between Google MySQL and Amazon RDS.

**Note**: Even after your app has been migrated to the new database, all of the app's files and images will remain in their current locations in your account's main cloud storage provider, such as Google Drive or Dropbox.
