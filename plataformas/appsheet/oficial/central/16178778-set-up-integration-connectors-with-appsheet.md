---
fonte: https://support.google.com/appsheet/answer/16178778?hl=en
baixado: 2026-11-10
---

# Set up Integration Connectors with AppSheet

This is a **preview release** of Integration Connectors with AppSheet. See [Track and manage feature releases](https://support.google.com/a/topic/1227580). Preview offerings are intended for use in test environments only. This feature is not recommended for use in production apps. For questions or assistance with this feature, contact [AppSheet Support](https://www.appsheet.com/Support/Contact).

Integration Connectors with AppSheet (preview) requires an **AppSheet Enterprise Plus** account.

To set up Integration Connectors with AppSheet, the Google Cloud and AppSheet team admins need to work together to complete the following steps:

+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Step**                                           | **Description**                                    | **Completed by**                                   |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| 1                                                  | [Set up Integration Connectors and create          | Google Cloud admin                                 |
|                                                    | connections](#set-up-create-connection)            |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| 2                                                  | [Set up the AppSheet team to use Integration       | AppSheet team admin & \                            |
|                                                    | Connectors](#set-up-team)                          | Google Cloud admin                                 |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+

 After you set up Integration Connectors with AppSheet, you can [add](https://support.google.com/appsheet/answer/15297394) and [use](https://support.google.com/appsheet/answer/16322183) connections as data sources.

Learn more [about the Google Cloud projects and service accounts used by AppSheet](https://support.google.com/appsheet/answer/15965965).

## Set up Integration Connectors and create connections

This step is completed by the Google Cloud admin.

Set up Integration Connectors and create connections as described in the following sections:

1.  [Create a Google Cloud project and service account](#project-service-account)
2.  [Set up Integration Connectors in the Google Cloud project](#set-up-integration-connectors)
3.  [Create connections](#create-connection)

### Create a Google Cloud project and service account

This step is completed by the **Google Cloud admin**.

As the Google Cloud admin, to create a Google Cloud project and a service account in the Google Cloud Console, do the following:

1.  [Create a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects). In the Google Cloud project, you'll create connections to use in AppSheet.  If you already have a project with the connections you want to use in AppSheet, you can skip this step.
2.  [*Grant permissions to create connections*](https://cloud.google.com/resource-manager/docs/access-control-proj). If you plan to allow your AppSheet team admins to create connections in the project, you’ll need to grant access control permissions to them.
3.  [Create a service account](https://cloud.google.com/iam/docs/service-accounts-create#creating) that will be used when creating connections using Integration Connectors. A service account is a special type of Google account intended to represent a non-human user that needs to authenticate and be authorized to access data in Google APIs.  

### Set up Integration Connectors in the Google Cloud project

This step is completed by the **Google Cloud admin**.

As the Google Cloud admin, you need to set up Integration Connectors for the Google Cloud project, as described in [Set up Integration Connectors](https://cloud.google.com/integration-connectors/docs/setup-integration-connectors).  If your project is already set up to use Integration Connectors, you can skip this step.

During the setup process, you'll enable the following APIs in your project:

- Secret Manager API
- Connectors API

After Integration Connectors is set up, you'll see the **Welcome to Integration Connectors Overview** page. 

### Create connections

This step is completed by the **Google Cloud admin**.

As the Google Cloud admin, you can create a connection based on one of the following data source types. You'll need the [roles/connectors.admin](https://cloud.google.com/integration-connectors/docs/connectors-access-permissions#iam-roles-for-integration-connectors) IAM role to create a connection. If you already have a connection to the data you want to use in AppSheet, you can skip this step.

Follow the links below for instructions on setting up each of the connectors you plan to enable. They will require granting certain roles to the service account created in [Create a Google Cloud project and service account](#project-service-account).

To minimize unnecessary exposure of your Google Cloud Platform resources, we recommend following the [*principle of least privilege*](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege) and not granting any other roles than the minimum required to use this feature. If your service account already has other roles, we recommend [*creating a new service account*](https://cloud.google.com/iam/docs/service-accounts-create#creating) for the connector.

- [Google BigQuery](https://cloud.google.com/integration-connectors/docs/connectors/bigquery/configure)
  To allow insert and update operations on BigQuery data, grant the following IAM roles to the service account used to create the connection: [`roles/bigquery.dataEditor`](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) and` `[`roles/bigquery.jobUser`](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.jobUser)

- [Jira Cloud](https://cloud.google.com/integration-connectors/docs/connectors/jiracloud/configure)

- [PostgreSQL](https://cloud.google.com/integration-connectors/docs/connectors/postgresql/configure)

- [Salesforce](https://cloud.google.com/integration-connectors/docs/connectors/salesforce/configure)

- [ServiceNow](https://cloud.google.com/integration-connectors/docs/connectors/servicenow/configure)
  When you configure the ServiceNow connection, we recommend that you specify the tables to include in the **Filter Tables** field. Otherwise, you might experience significant delays when loading your data.
   

  Filter tables field when configuring ServiceNow

  **Note**: To support multiple regions, you'll need to create a connection in *each* region. Make sure you select one of the following regions when creating your connection: **us-west1, us-central1, us-east4, europe-west4**

## Set up the AppSheet team to use Integration Connectors

This step is completed by both the **AppSheet team admin** and **Google Cloud admin** working together.

Before you can add a connection as a data source, the AppSheet team admin and Google Cloud admin need to work together to set up the AppSheet team to use Integration Connectors.

As the AppSheet admin, to set up your team to use Integration Connectors do the following:

1.  Go to the **My account \> Sources** and click **+ New Data Source**.
2.  Select the **Use Integration Connectors** tab.
3.  Click **Get started**.
    The Add data source using Integration Connectors dialog displays. Step through the wizard, as described in the following sections:
    - [Step 1: Create a service account](#create-service-account)
    - [Step 2: Grant access roles](#grant-access-roles)
    - [Step 3: View connections](#view-connections)
    - [Step 4: Add connection](#add-connection)

Click **Save for later** at anytime to save the current configuration settings and exit the wizard.

### Step 1: Create a service account

This step is completed by the **AppSheet team admin**.

Before you can add a connection as a data source, you'll need a [service account](https://cloud.google.com/iam/docs/service-account-overview) for your team that is used to manage the connection between AppSheet and Integration Connectors. This service account is different from the one created when the [Google Cloud project was set up](#project-service-account) by the Google Cloud admin.  This service account is created by AppSheet in the AppSheet-owned Google Cloud project and is only used for AppSheet. For more information, see [About the Google Cloud projects and service account used for Integration Connectors with AppSheet](https://support.google.com/appsheet/answer/15965965).

To create a service account in the AppSheet-owned Google Cloud project, do the following:

1.  If you have not already created a service account for your team, click **Create**.
    If you have already created a service account, its address will be displayed in the field.
2.  Click Copy icon to copy the service account address.
3.  Click **Next**.

Create service account, copy address, and click Next

### Step 2. Grant access roles

This step is completed by the **Google Cloud admin**.

To grant access roles, do the following:

1.  Request that your Google Cloud admin grant access roles to the service account to allow AppSheet to connect to Integration Connectors. Provide your Cloud admin with the service account address copied in [Step 1: Create a service account](#create-service-account).
2.  Your Cloud admin will need to follow the steps in [Allow AppSheet to connect to your connection](#allow-appsheet-to-connect).
3.  If you have connections in more than one project, repeat step 2 for each project for which you want to grant access.
4.  After access roles have been granted by your Cloud admin, click **Next**.

Request your Google Cloud admin grant access roles to the service account. Once done, click Next.

####  Allow AppSheet to connect to your connection

Request that your Google Cloud admin allow AppSheet to connect to Integration Connectors by using one of the following methods:

- [Use the Google Cloud console](#console) 
- [Use the gCloud CLI](#gcloud-cli)

See also: [Stop allowing AppSheet to connect to Integration Connectors](#stop-allowing-appsheet-connect)

Use the Google Cloud console

To use the Google Cloud console to update IAM permissions that allow AppSheet to connect to Integration Connectors, do the following:

1.  Open the [IAM permissions](https://console.cloud.google.com/iam-admin/iam) page in the Google Cloud console.
    Select the project where your connection was created. 
2.  Click **+Grant Access**.
    The Grant access form displays.
3.  In the **New principals** field, enter the **service account** *provided by AppSheet*. 
4.  Under Assign Roles in the **Role** drop-down, select [**Connector Invoker**](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.invoker).
5.  Click **+Add another role**.
6.  In the new **Role** drop-down, select [**Connectors Viewer**](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.viewer).
    The following shows an example of the form:

    Grant access to AppSheet service account
     
    To minimize unnecessary exposure of your Google Cloud Platform resources, we recommend following the [*principle of least privilege*](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege) and not granting any other roles than the minimum required to use this feature.
7.  Add IAM conditions to limit access to the specific connectors you want to use in AppSheet.
    By default, granting the above roles will allow AppSheet to perform the associated operations on all connectors in the project. If you only intend to use a subset of connectors with AppSheet, we recommend using IAM Conditions to limit access to those specific connectors. See [IAM conditions for fine-grained access](https://cloud.google.com/integration-connectors/docs/add-connector-iam-conditions).
8.  Click **Save**.

## Use the gCloud CLI

Your admin can use the [gCloud CLI](https://cloud.google.com/sdk/gcloud) to update IAM permissions that allow AppSheet to connect to your connection. To copy the script, expand the **Option 2: Use gCloud CLI** section and click **CLI access roles**   Copy icon  . Then, run the script from the command line.

Copy CLI access roles

### Step 3: View connections

This step is completed by the **AppSheet team admin**.

To view connections, do the following:

1.  Enter the **Google Cloud project ID** where the [connections were created](#create-connection) by the Google Cloud admin and click **Find**.
    The list of available connections is displayed.
2.  Select the connection that you'd like to add as a data source from the list.
3.  Click **Next**.

Enter the project ID, select the connection, and click Next

### Step 4: Add connection

This step is completed by the **AppSheet team admin**.

To add the connection, do the following:

1.  Optionally, select **Share connection for use within your team**.
    This step is optional; you can [share the data source with your team](https://support.google.com/appsheet/answer/10104795#share-data-sources) later.
2.  Select **Save and complete**.
    The connector is added as a data source.

Share with your team, if desired, and click Save and complete

## Next steps

- To add more connections, see [*Add connections as data sources*](https://support.google.com/appsheet/answer/15297394).
- To use connections as data sources in apps, see [Use connections as data sources](https://support.google.com/appsheet/answer/16322183).
