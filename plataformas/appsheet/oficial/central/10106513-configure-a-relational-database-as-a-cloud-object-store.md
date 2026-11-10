---
fonte: https://support.google.com/appsheet/answer/10106513?hl=en
baixado: 2026-11-10
---

# Configure a relational database as a cloud object store

This feature is available to **AppSheet Enterprise Plus **accounts only. See [What features are supported with each subscription?](https://support.google.com/appsheet/answer/10105400#features)

A relational database table can be used as a cloud object store. Customers who choose this option typically do so to capture images through the app and keep them along with the data in the same repository (convenient for backup and data management). The downside is that images stored within a relational database are not easy to access directly --- they can only be accessed through the app.

Each image or file is saved as a separate row in a database table. Instead of a table, you can use an updatable view. You need a `varchar(max)` column which can hold the content (in base-64 encoded text format). You also need a column (at least `nvarchar(256)`) to hold a unique text label that is used to identify and retrieve the image. AppSheet will only read and write these columns. Any other columns in the database table should therefore be nullable.

When you configure AppSheet, you will need to specify the database data source, the name of the table, and the names of the label column and the content column. If you expect this table to hold a large number of rows, it is a good idea to create a database index on the label column of this table.

Configure a relational database as a cloud object store as described in the following sections:

1.  [Add a relational database as a data source](#add-relational-db)
2.  [Add the cloud object store to your AppSheet account](#add-object-store)
3.  [Configure a table in an app to use the cloud object store](#configure-table)

## ****Add a relational database as a data source

To add a relational database as a datasource, see [Use multiple data sources](https://support.google.com/appsheet/answer/10106309).

## ****Add the cloud object store to your AppSheet account

After you have your relational database configured, you are ready to add it to your AppSheet account

1.   Sign in to [AppSheet](https://www.appsheet.com).
2.   Select your account from the account profile drop-down to go to the **My account** page.

    Access the My account page
3.  Go to **Integrations \> Stores**.
4.  Perform one of the following steps:
    - To add an object store for use by your own account, click **New Cloud Store** under **Object Stores**, then click **DB-Content**.
    - To add an object store for your team member accounts, click **New Cloud Store** under **Team** **Object Stores**, then click **DB-Content**. 
      **Note**: You must be a **Team Admin** to create a team object store.
5.  Complete the **Add DB-Content integration** dialog to create the new object store. Enter the database name, select the database data source, and enter the names of the database table, label column, and content column.
6.  Click **Save**.

## ****Configure a table in an app to use the cloud object store

After you have added a cloud object store to your account, you can configure a table in an app to use it.

1.  Sign in to [AppSheet](https://appsheet.com).
2.  Open the app in the app editor.
3.  Go to **Data**  and select the table you want to configure.
    We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

    ## If you are using the legacy editor

    Go to **Data \> Columns** and expand the table you want to configure.
4.  Click **Table settings** Table settings icon .
5.  In the **Store for image and file** drop-down, select the name of the object store that you set up for your account (such as, **DBStore**).
6.  Save the change.
