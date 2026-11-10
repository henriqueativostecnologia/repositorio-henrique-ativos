---
fonte: https://support.google.com/appsheet/answer/10106676?hl=en
baixado: 2026-11-10
---

# Use data from MySQL

AppSheet can build apps from [MySQL databases](https://www.mysql.com/) that are hosted in the cloud, including [Google Cloud SQL](https://cloud.google.com/sql), [Amazon RDS](https://aws.amazon.com/rds/), [Oracle MySQL Cloud Service](https://www.oracle.com/mysql/), or other cloud-hosting provider that supports MySQL.

Use data from MySQL as described in the following sections:

- [Add a MySQL data source](#add-mysql-datasource)
- [Configure SSL](#configure-ssl)
- [Use a MySQL data source in your app](#use-in-app)
- [Use MySQL on Amazon RDS](#use-on-amazon-rds)
- [Supported MySQL versions](#supported-mysql-versions)
- [How files created in the app are saved](#how-files-in-app-saved)
- [How required columns are set](#how-required-columns-set)
- [Work with IDENTITY columns](#work-with-identity-columns)
- [Work with special characters](#work-with-special-chars)

## ****Add a MySQL data source

Before adding a MySQL data source, see [Supported MySQL versions](#supported-mysql-versions).

**Note:** In order for AppSheet servers to access your data, both the MySQL database's network and the MySQL database itself must accept inbound connections from AppSheet servers to the database. For more information, see [Manage IP address and firewall information](https://support.google.com/appsheet/answer/10104492).

To add a MySQL data source:

1.  Go to the **My Account \> Sources**.
    You can view all of the data sources that are currently available for your use.
2.  Click **+ New Data Source**.

3.  Enter a data source name and click **Cloud Database** in the list of data sources.

    Select Cloud Database on the Add a new data source dialog
4.  Configure the database connection information. 
    - **Type**: Select **MySQL**.
    - **Server**: Enter the MySQL database server hostname or IP address.
    - **Database**: Enter the database name.
    - **Username**: Enter the username of the database user.
    - **Password**:Enter the password for the database user.
    - **SSL**: Select the SSL mode required for the connection. For more information, see [Configure SSL](#configure-ssl).
5.  Click **Test** to test the connection details.
6.  After a successful test, click **Authorize Access** to save the data source in your AppSheet account.

## ****Configure SSL

AppSheet can connect to MySQL instances using [Secure Socket Layer (SSL)](https://en.wikipedia.org/wiki/SSL). When adding a MySQL data source, select one of the following options:

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **SSL mode**                                                                  | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| None                                                                          | SSL connection is not required, although some cloud providers will still      |
|                                                                               | attempt to establish SSL, if possible.                                        |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Required                                                                      | Data to and from the MySQL instance must be encrypted using the SSL protocol. |
|                                                                               |                                                                               |
|                                                                               | Only the [server                                                              |
|                                                                               | certificate](htt                                                              |
|                                                                               | ps://en.wikipedia.org/wiki/Public_key_certificate#TLS/SSL_server_certificate) |
|                                                                               | (owned by the MySQL instance) is required to establish the connection. The    |
|                                                                               | [client                                                                       |
|                                                                               | certificate](htt                                                              |
|                                                                               | ps://en.wikipedia.org/wiki/Public_key_certificate#TLS/SSL_client_certificate) |
|                                                                               | (normally stored in the application client) is optional.                      |
|                                                                               |                                                                               |
|                                                                               | **Note**: If your MySQL instance is configured to use                         |
|                                                                               | [X.509](https://en.wikipedia.org/wiki/X.509) mode, you'll need to change the  |
|                                                                               | connection mode to SSL in order for the connection to work. For instances     |
|                                                                               | hosted on Google Cloud, X.509 mode can be turned off by going to the **SSL**  |
|                                                                               | tab and clicking **Allow unsecured connections**. This will relax the client  |
|                                                                               | certificate requirement.                                                      |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| VerifyCa                                                                      | Data to and from the MySQL instance must be encrypted using the SSL protocol. |
|                                                                               |                                                                               |
|                                                                               | Uses a client certificate to authenticate with the server. Additionally,      |
|                                                                               | verifies the server's CA with the provided CA certificate. This mode          |
|                                                                               | tolerates hostname mismatch.                                                  |
|                                                                               |                                                                               |
|                                                                               | You are prompted to upload the following content:                             |
|                                                                               |                                                                               |
|                                                                               | -   Client certificate                                                        |
|                                                                               | -   Client certificate private key                                            |
|                                                                               | -   Server CA certificate                                                     |
|                                                                               |                                                                               |
|                                                                               | **Note**: This mode is useful for the database servers that do not have a     |
|                                                                               | hostname but expose IP addresses for connections, such as Google CloudSQL.    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| VerifyFull                                                                    | Data to and from the MySQL instance must be encrypted using the SSL protocol. |
|                                                                               |                                                                               |
|                                                                               | This mode is the same as VerifyCa, but also matches the server hostname with  |
|                                                                               | the CA certificate.                                                           |
|                                                                               |                                                                               |
|                                                                               | You are prompted to upload the following content:                             |
|                                                                               |                                                                               |
|                                                                               | -   Client certificate                                                        |
|                                                                               | -   Client certificate private key                                            |
|                                                                               | -   Server CA certificate                                                     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

When using an SSL connection, it's highly recommended that the MySQL instance uses a server certificate generated by a widely recognized [certificate authority](https://en.wikipedia.org/wiki/Certificate_authority) such as [VeriSign](http://www.verisign.com/) or [GeoTrust](http://www.geotrust.com/). This will ensure that the certificate meets all of the relevant encryption and formatting standards. Some cloud storage providers, such as Google Cloud and Amazon RDS, also generate server certificates for the MySQL instances that they host. Currently, server certificates generated by TinyCA and self-signed certificates are not supported.

Additionally, it's a good practice to sign the server certificate using [SHA-2](https://en.wikipedia.org/wiki/SHA-2) hashing algorithms. This is because [SHA-1](https://en.wikipedia.org/wiki/SHA-1) algorithms are no longer considered fully secure, and many cloud providers, including Microsoft, Amazon, and Google, are increasingly moving to SHA-2 and [SHA-3](https://en.wikipedia.org/wiki/SHA-3).

## ****Use a MySQL data source in your app

After you add a MySQL data source to your account, you can add MySQL tables or views to any app. When you choose **Add Table** in your app, you can select the specific data source, and a table or view from that data source.

Once added to the app, AppSheet treats all data sources similarly. In fact, it's common to combine data from a MySQL data source with data from other sources in the same app.

## ****Use MySQL on Amazon RDS

If your MySQL instance is hosted on [Amazon RDS](https://aws.amazon.com/rds/), you may need to set the **Publicly Accessible** setting to **Yes**. To ensure the server accepts traffic from AppSheet, go to security groups settings in Amazon RDS, enter the EC2 Management Console, choose **Edit inbound rules**, and create rules to accept all traffic from AppSheet's IP addresses, as described in [Manage IP address and firewall information](https://support.google.com/appsheet/answer/10104492)*.*

## ****Supported MySQL versions

For your MySQL instance to work with AppSheet, we recommend that you use MySQL version 5.7.6 or above.

In addition, because MySQL is open source, there are many variants of MySQL, such as [MariaDB](https://mariadb.com/) or [Percona](https://www.percona.com/). If you use a variant of MySQL, AppSheet cannot guarantee that your database will work.

**Note**: When working with a MySQL data source, if you encounter an `Unknown column error`, the issue is most likely version related.

## ****How files created in the app are saved

Typically, if an app has to capture photographs, for example, they are typically stored in a folder adjacent to the source of data in cloud storage. Unlike our other cloud-storage providers, database servers do not have a file system and require a change in AppSheet behavior when saving files (like images and documents).

In a MySQL table, image and document files are stored in the main cloud file system associated with the app creator's primary AppSheet account (typically Google Drive, Dropbox, Office 365, or Box). The files will be saved in a subfolder of your account's default folder path (usually `/appsheet/data`).

You can view and change the default folder path in your account page under the **Settings** tab.

## ****How required columns are set

Each database column that specifies `NOT NULL` (for example, `NN`) in the MySQL schema will have **Required?** set to **ON** in the AppSheet table. By specifying `NOT NULL` for the MySQL column, you ensure the column has a value in both the MySQL database and the AppSheet app.

Each time you regenerate the table's columns in the app editor, AppSheet sets the **Required?** property for the AppSheet field based on the current `NOT NULL` setting of the MySQL column.

## ****Work with IDENTITY columns

It's common for a database table to use an `IDENTITY` column as a key. The values of the `IDENTITY` column are auto-incrementing numbers that get automatically inserted by the database.

Using `IDENTITY` columns in this way with AppSheet may cause problems. By default, MySQL doesn't let an application define the `IDENTITY` column value. Because with AppSheet new rows can be created in an app when it's offline and synced later, the app needs to be able to assign `IDENTITY` key values.

We recommend that you avoid using `IDENTITY` column keys in your database schema. Instead, use a column that is an `NVARCHAR` value of length greater than or equal to 8, such as `NVARCHAR(8)`. In AppSheet's column definition for this key, enter an initial value using [`UNIQUEID()`](https://help.appsheet.com/en/articles/2357317-uniqueid). Using this method, unique key values can be assigned by the app and inserted into the backend database.

If the database must use `IDENTITY` columns, we recommend that you create them with a large initial seed. For example, set `AUTO_INCREMENT = 100000`. In AppSheet's column definition for this key, give it an initial value of [`RANDBETWEEN`](https://help.appsheet.com/en/articles/2357303-randbetween)`(10000, 99999)`. This way, any records created from your app will have five-digit values that fall randomly in the range 10000 to 99999, while records created directly against the database will have higher values.

If the database schema cannot be changed and if there is already an `IDENTITY` column being used with the default initial seed (of `1`), we recommend that you follow the same approach as described earlier. However, you can first manually increment the `IDENTITY` seed as follows:

    ALTER TABLE tablename AUTO_INCREMENT = 100000;

This should "re-seed" the `IDENTITY` column to the desired range. Your AppSheet app will insert values in the range specified by the `RANDBETWEEN()` function in the initial value of your AppSheet column definition.

## ****Work with special characters

A MySQL character set defines the characters that can be read and processed by a particular MySQL database or table. The default character set of a MySQL database should work with most Latin characters. However, many languages, such as Spanish or Chinese, have special characters that aren't included in the default character set. In order to work with these special characters, you'll need to configure your MySQL database or table to use the appropriate character set.

For example, to configure an entire database to work with special characters in Spanish, such as ñ, use the following command:

    ALTER DATABASE db_name DEFAULT CHARACTER SET utf8 COLLATE utf8_spanish_ci;

Alternatively, to configure only a single table, use the following command:

`ALTER TABLE db_table CONVERT TO CHARACTER SET utf8 COLLATE utf8_spanish_ci;`
 

More information about available character sets in MySQL can be found in the MySQL developer documentation:

[https://dev.mysql.com/doc/refman/5.7/en/charset.html](https://dev.mysql.com/doc/refman/5.7/en/charset.html)
