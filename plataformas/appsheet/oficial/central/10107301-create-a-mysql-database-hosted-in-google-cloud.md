---
fonte: https://support.google.com/appsheet/answer/10107301?hl=en
baixado: 2026-11-10
---

# Create a MySQL database hosted in Google Cloud

## Prerequisites

- An AppSheet plan that supports database connections.
- Access to a Google Cloud Platform account.

## Nomenclature

The following list defines a few terms with a focus on how they are used in relation to AppSheet.

- Database Instance: The database instance is the structure that manages a collection of database files. An instance can hold several databases. In the tutorial below, you will generate a public IP address to connect with the database instance.
- Database: A database is a collection of data. A database generally holds several tables. In AppSheet, each database will appear as an individual data source.
- Schema: In this context, schema and database are referring to the same thing. It is a collection of data made up of several tables. Schema is the term used in MySQL Workbench. Database is the term used in Google Cloud and AppSheet.
- Table: A table holds the actual data. A table generally has several columns, each with a specific type of data (such as, Name, email address, phone number, and so on). Each row contains a unique record. When viewing a form in AppSheet, each field in the form corresponds to a column in the table and saving the form creates a new row.

In summary, a database instance can have multiple databases and a database can have multiple tables.

## Create a Database Instance

1.  Open your Google Cloud account and click **SQL** in the left menu.

    Select SQL in the left menu of your Google Cloud account
     
2.  Click **Create Instance**.
3.  Choose your database engine. This tutorial uses MySQL.

    Choose MySQL

    Fill in the instance information.
4.  Choose an Instance ID. This is how your database will be identified in the Google Cloud account.
5.  Select a root password.
6.  Choose the region. For best performance, select the region based on where the majority of your users are located.
7.  Click **Show configuration options** to expand the configuration options.

    Fill in the instance information
8.  Under **Connectivity** ensure **Public IP** is checked. By checking this box, Google Cloud will create an IP address that you can use to connect your AppSheet account to the database instance.
9.  Click **Add network**. 

10. Enter the IP addresses listed in [Manage IP addresses and firewall information](https://support.google.com/appsheet/answer/10104492). This allows the AppSheet server to connect directly to your database. Google Cloud requires the IP addresses in CIDR notation. To write the IP address in CIDR notation, add `/32` to the end of each IP address. For example, `20.189.130.98` becomes `20.189.130.98/32`.
11. Select the machine type and storage. Select a machine type with enough memory to hold your largest table.
12. Update additional settings as needed. Generally, the default values for the remaining settings are correct.
13. Click to Create the database instance. This will take a few minutes to complete.

## Create a user account for the database instance

1.  After the database instance is created, click on the instance id to open the details page.

    Click the instanced ID to open the details page for the database instance
2.  Click **Users** and **Create user account**.

    Click Users then Create user account
3.  Create a user name and password for the account that will be used to connect with AppSheet.
    Record the username and password. After creating the account, you can *change* the password, but you cannot *retrieve* the password.

    Create a username and password for the account

## Create a Database - Method 1: Using Google Cloud Console

1.  Click **Databases** and **Create database**.

    Click Databases and Create database in the Google Cloud console
2.  Enter a database name and click **Create**.

    Enter a database name and click Create

## Create a Database - Method 2: Using database visualization tool

A data visualization tool is a common way to interact with the database. This tutorial uses MySQL Workbench to access and modify the database.

1.  To connect to the database with MySQL Workbench, you must add your workstation’s IP address to the firewall allow list. You can find this by searching “What’s my IP address” in your browser.
2.  Allow your IP address in Google Cloud by following the same steps used to allow the AppSheet IP addresses.
3.  **Open MySQL Workbench and create a new MySQL connection.**
    - The **hostname** is the public IP address for your database.
    - The **username** and **password** are from the user account you created above.
4.  Click **Test the Connection** then click **Ok**.
5.  Create a new schema.
    **Note**: The term *schema* in MySQL Workbench and the term *database* in Google Cloud (see Method 1 above) refer to the same thing.

## Connect AppSheet to the Database

1.  Go to the **My Account \> Sources** tab.
2.  Click **+ New Data Source**.
3.  Enter a name for the data source and click **Cloud Database** or **On-premises Database**.
    The Add database connection information dialog displays.
4.  Configure the database connection information. 
    - **Type**: Select MySQL.
    - **Server**: Enter the MySQL database server hostname or IP address.
    - **Database**: Enter the database name.
    - **Username**: Enter the username of the database user.
    - **Password**:Enter the password for the database user.
5.  Click **Test** to test the connection details.
6.  After a successful test, click **Authorize Access** to save the data source in your AppSheet account.

## Connect apps to the database

The database and schema are now connected to your AppSheet account. From within an AppSheet app, the process to add tables from a database is the same as adding tables from a spreadsheet. See [Add a table](https://support.google.com/appsheet/answer/10105821#add-table).

The database may appear in your AppSheet account as **database-1**. You can change the name for your database in AppSheet as follows: 

1.  Navigate to **My account \> Sources**.
2.  Click on the database you'd like to update.
3.  This opens a box where you can modify the name. Enter a new name (such as, AppSheet_Demo) and click **Cloud Database**.

4.  Fill in the same connection information and click **Authorize Access**. The database will now appear with the new name in AppSheet.

See also: [Use data from MySQL](https://support.google.com/appsheet/answer/10106676)
