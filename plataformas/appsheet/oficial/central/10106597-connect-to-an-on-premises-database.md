---
fonte: https://support.google.com/appsheet/answer/10106597?hl=en
baixado: 2026-11-10
---

# Connect to an on-premises database

Connect to an on-premises database as described in the following sections:

- [Manage IP address and firewall information](#ip-firewall)
- [Use Integration Connectors with AppSheet](#integration-connectors)
- [Use DreamFactory](#dreamfactory) (limited to existing customer configurations)

## Manage IP address and firewall information

To allow AppSheet to connect to an on-premises database, open up the database's firewall to AppSheet servers' IP addresses. See [Manage IP address and firewall information](https://support.google.com/appsheet/answer/10104492) for a list of AppSheet's IP addresses. 

## Use Integration Connectors with AppSheet

This is a **preview release** of Integration Connectors with AppSheet. See [Track and manage feature releases](https://support.google.com/a/topic/1227580). Preview offerings are intended for use in test environments only. This feature is not recommended for use in production apps. For questions or assistance with this feature, contact [AppSheet Support](https://www.appsheet.com/Support/Contact).

Integration Connectors with AppSheet (preview) requires an **AppSheet Enterprise Plus** account.

[Google Cloud Integration Connectors](https://cloud.google.com/integration-connectors/docs/overview) let you expose your enterprise data in different applications and integrations, including AppSheet. The connections you create in Google Cloud can be used as data sources in AppSheet. See [Overview of Integration Connectors with AppSheet](https://support.google.com/appsheet/answer/16178487).

## Use DreamFactory (limited)

**AVAILABILITY NOTICE**: Use of DreamFactory to connect securely to an on-premises database is not available to new customer configurations. It will continue to work for existing customer configurations.

### Install DreamFactory 

DreamFactory is a proxy server that exposes a REST API through which third-party applications can securely connect to your databases.

There are two ways to install DreamFactory. The first method is to create a DreamFactory instance hosted on a web server that is separate from your database's server. In this case, you will still need to open your database's firewall to allow the DreamFactory instance to connect to your database. The second approach is to download and install DreamFactory into your on-premise server alongside your database. See [DreamFactory](https://wiki.dreamfactory.com/DreamFactory/Installation) for more information on how to install and set up DreamFactory.

### Register AppSheet with DreamFactory

Once you have set up DreamFactory, log into your DreamFactory instance as an admin, and open the Apps tab, and register AppSheet by clicking **Create**. Name the new app **AppSheet**, check the **Active** check box, select **On a remote URL** as the app's location, and enter AppSheet's URL ([https://www.appsheet.com/](https://www.appsheet.com/)). 

Register AppSheet with DreamFactory

After you click save to register AppSheet, DreamFactory will automatically generate a new API key that AppSheet can use to connect to your DreamFactory instance.

New API key generated to connect to your DreamFactory instance from AppSheet

### Register your database as a new service

To allow DreamFactory to connect to your database, you need to register it as a new service in your DreamFactory instance.

In DreamFactory, open the **Services** tab, and click **Create** to add a new service. In the **Info** sub-tab, select the appropriate service type based on the type of your database. Currently, AppSheet only supports SQL databases (SQL Server, MySQL, MariaDB, and PostgreSQL). For MariaDB databases, you can select **MySQL**. After selecting the service type, give your service a name and a label.

Register the database as a new service

Next, open the **Config** sub-tab and fill out the address of your database server, the database's name, the username, and the password. If your database does not use the default port, you will need to specify the port number as well. If your DreamFactory instance is not hosted on the same server as your database, you will also need to note down the instance's IP address in the **Config** sub-tab and add it to your database's firewall. Most of the other settings can be ignored.

Configure the database for DreamFactory

Once you have saved your new service, open the **Schema** tab to verify that DreamFactory can now connect to your database. The newly created service should now be available in the service drop-down menu. Select the new service and then open the **Table** drop-down menu. If your service has been configured correctly, DreamFactory should be able to populate the drop-down menu with the names of tables and views in the database. Note that you may need to click **Refresh** for the tables and views to appear.

Verify DreamFactory was configured properly from the Schema tab

### Create roles and users

For security reasons, AppSheet can only connect to your DreamFactory instance using a user account instead of an admin account. As a result, you will need to create a new DreamFactory user account for AppSheet, and assign the appropriate role to this account.

First, open the **Roles** tab and click **Create** to create a new role. In the **Basic** sub-tab, name the new role and check the **Active** checkbox.

On the Roles tab, click Create to create a new role and check the Active box on the Basic sub-tab

Next, open the **Access** sub-tab and click on the plus button to add two new service access rules. 

For the first rule, select the database service that you have created, choose the component `_schema/*` , and enable the `GET` access mode. This access rule will allow AppSheet to access the table schemas in your database in order to obtain and analyze the column structure of your tables and views. Since AppSheet only needs to read the table schemas without making any modification, only the `GET` access mode needs to be enabled.

For the second rule, choose the component `_table/*` , and enable all available access modes. This rule will allow AppSheet to read and write data to tables and views in your database.

Configure rules for the database server

After you have saved the new role, open the **Users** tab and click **Create** to add a new user account. In the **Basic** sub-tab, fill out the email address of the account, check both the **Active** and **Set Password** checkboxes, and create a new password for the account.

Add a new user account

Next, open the **Roles** sub-tab. If AppSheet has been correctly registered in your DreamFactory instance, you should see AppSheet listed as one of the apps available to the new account. Select the role that you have just created for AppSheet, and the save the user account.

Verify that AppSheet has been correctly registered in your DreamFactory instance

### Add DreamFactory as a data source in AppSheet

Once you have set up and configured you DreamFactory instance, you can add the instance as a data source to your AppSheet account. To do this, open the **Sources** tab in the account page, click the add data source button, name your new data source, and then select **On-premises Database** as the data source type.

In the DreamFactory connection information page, fill out the following fields:

- **Database type**: the type of your database (MySQL, SQL Server, etc.)
- **Server**: the address of your DreamFactory instance. This must be a publicly accessible URL, IP address, or host name.
- **API key**: the API key assigned to AppSheet by DreamFactory
- **Service name**: the service name of your database in DreamFactory. Note that this is not the application name that you used to register AppSheet with DreamFactory.
- **User email:** the email of the DreamFactory user account that you have created
- **Password**: the password of the user account

Once the above fields have been filled out, test the connection, and finally authorize AppSheet to access your database through DreamFactory.
