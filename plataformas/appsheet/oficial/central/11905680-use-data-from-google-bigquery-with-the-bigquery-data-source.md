---
fonte: https://support.google.com/appsheet/answer/11905680?hl=en
baixado: 2026-11-10
---

# Use data from Google BigQuery with the BigQuery data source

The following sections describe how to use data from Google BigQuery with the BigQuery data source:

- [Overview](#overview)
  - [Licensing requirements for a BigQuery data source](#licensing-requirements)
  - [Limits when using a BigQuery data source](#limits)
  - [Best practices for setting up your app to use a BigQuery data source](#best-practices)
- [Configure BigQuery in Google Cloud](#configure)
  - [Create a service account](#create-service-account)
  - [Create a JSON key for the service account](#create-json-key-target-service)
- [Add the BigQuery data source to your AppSheet app](#add-bigquery-data-source)
- [Add a BigQuery table to your AppSheet app](#add-bigquery-table)

**Note**: You can use data from Google BigQuery with the BigQuery data source (as described in this topic) or with [Connected Sheets](https://support.google.com/appsheet/answer/11903794). To compare the two options, see [Use data from Google BigQuery with AppSheet](https://support.google.com/appsheet/answer/11905679). You can also use Integration Connectors to connect with BigQuery. See [What is the difference between using the existing BigQuery connection method and the new BigQuery connector?](https://support.google.com/appsheet/answer/15405481#zippy=%2Cwhat-is-the-difference-between-using-the-existing-bigquery-connection-method-and-the-new-bigquery-connector)

## ****Overview

The BigQuery data source provides app creators with read-write access to BigQuery datasets.

 Watch the following video for an introduction to using data from BigQuery with the BigQuery data source.
**(Note**: Since the date this video was created, the BigQuery data source now provides app creators with **read-write** access to BiqQuery datasets. The video incorrectly states access is read-only.)

Video: https://www.youtube.com/watch?v=pL8mugW24ic

### Licensing requirements for a BigQuery data source

BigQuery is a [Google Cloud](https://cloud.google.com/) service that many enterprise customers use for data reporting. Because the volume of data that must be processed can be significant, BigQuery is classified as an Advanced Data Connector and requires an AppSheet Enterprise Plus plan.

### Limits when using a BigQuery data source

Because BigQuery has the potential to have massive amounts of data (potentially tens of millions of rows or more and up to 10,000 columns), we have put some product limits in place to ensure your apps will be able to load data and perform well.

AppSheet enforces the following limits for a BigQuery data source:

- **Maximum of 100,000 rows** - BigQuery datasets exceeding the maximum number of rows will be truncated.
- **Partitioned tables are not supported** - Any BigQuery tables that have partitioned columns will report an error during configuration in AppSheet. Use a BigQuery View that omits the partitioned column to work around this limitation.
- **Google Cloud access required** - Service accounts are the **only access method** AppSheet supports. You will need to have access to create service accounts and keys in your Google Cloud project, or you will need to request assistance from an IT administrator with the appropriate level of access. The IT administrator can create the data source as a [team data source](https://support.google.com/appsheet/answer/10104801) and share it with you.

In addition, there are complex types that are not supported for writing to BiqQuery. These types are `Array`, `Bytes`, `Geography`, and `Struct`.

The next section provides best practices for setting up your app to work within the product limits.

### Best practices for setting up your app to use a BigQuery data source

**1. Use [security filters](https://support.google.com/appsheet/answer/10104488).**

Include AppSheet [expressions](https://support.google.com/appsheet/answer/10104642) in the security filters, which will be translated to BigQuery SQL and executed on the server before the data is downloaded to the app.

Security filters are pushed to the SQL Provider only for `AND()`, `IN()`, `NOT()`, and `OR()` expressions. Other expressions aren't supported for Provider-level querying before the row limit is applied. For BigQuery, the row limit of 100K is applied on that Provider query, so you can get too few rows if you use a security filter that isn't purely composed of these expression. 

Although security filters limit data access, they aren't a complete security solution. Users should protect sensitive data operations at the data source level. For more information about securing your data, see [Security: The Essentials](https://support.google.com/appsheet/answer/10105078).

**Examples**:

- Filter by [`USEREMAIL()`](https://help.appsheet.com/en/articles/2357268-useremail) to get rows owned or viewable by the currently logged-in app user.

- Filter by `DateTime` values in the last week or month to get only the most recent data. For example, assuming there is a column in the dataset called `DateCreated`, you could use security filter expressions like:
  - For the last week: `[DateCreated] >= TODAY() - 7`
  - For the last month: `[DateCreated] >= TODAY() - 30`

- Use a combination of [user settings](https://support.google.com/appsheet/answer/10106760) and security filters to allow your app user to limit the data. For example, using the user setting column named `Year` and a column in the dataset called `StartTime`, you can get data from the year 2018 or later (assuming the user setting `Year` is set to `2018`), as follows: `[StartTime] >= DATETIME("1/1/" & USERSETTINGS("YEAR"))`

**2. Use BigQuery Views **(read only)

You can create specific [views](https://cloud.google.com/bigquery/docs/views) for AppSheet in BigQuery that have potentially complex SQL queries to create a limited number of rows from the dataset. When setting-up the BigQuery data source as a table in your app, select from the list of views in your project as well as from the base datasets.

**Note**: BigQuery views are read-only so changes made in AppSheet will not sync back to the BigQuery dataset.

**3. Create a new BigQuery Table**

BigQuery allows you to set up a copy of a table that can be re-created periodically based on a scheduled query. This is similar to a view, but it is a physical table that contains the subset of data. This can also be used to reduce the number of columns in order to simplify the table structure.

## Configure BigQuery in Google Cloud

In order to connect AppSheet to BigQuery, a service account must be created in Google Cloud with the correct role to access BigQuery data. A service account is a special kind of account that is used to grant *system-to-system* level access, rather than grant access to individual users. AppSheet (a system) will use the service account user to access BigQuery (a system) which will establish the system-to-system communications. Additional user-level access can be configured in AppSheet through [security filters](https://support.google.com/appsheet/answer/10104488) on the data source.

### Required roles

Accessing a **public dataset** only requires the **BigQuery Job User** role.

Accessing a **private dataset** requires the **BigQuery Job User** and **BigQuery Data Editor** roles. These roles encompass all required permissions.

Granting BigQuery Job User and BigQuery Data Editor roles will result in some unused permissions. If your organization requires it, you can follow the steps to [*create a custom role*](https://cloud.google.com/iam/docs/creating-custom-roles#creating) with only the required permissions listed below:

- `bigquery.datasets.get`
- `bigquery.jobs.create`
- `bigquery.routines.get`
- `bigquery.routines.list`
- `bigquery.tables.get`
- `bigquery.tables.getData`
- `bigquery.tables.list`
- `resourcemanager.projects.get`

### Create a service account

The following steps describe how to create a service account using the Google Cloud console.

1.  Go to the [Google Cloud console](https://console.cloud.google.com/).

2.  In the navigation menu, select **IAM & Admin \> Service Accounts** to access the **Service accounts** page.

3.  Click **+ Create Service Account**.

    Create a service account in the Google Cloud Console

4.  Create service account with the **BigQuery Job User** role

    1.  Enter the a **Service account name** and **Service account description** and click **Create**.

        Add service account details

    2.  Type in **BigQuery Job** in the text box to filter to the list of roles and select **BigQuery Job User**.

        Grant BigQuery Job User role to service account

    3.  If connecting to a private dataset, repeat this step to add the **BigQuery Data Editor** role. Alternatively, if you created a custom role, add that role instead of the BigQuery Data Editor role. 
         
        To minimize unnecessary exposure of your Google Cloud Platform resources, we recommend following the [*principle of least privilege*](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege) and not granting any other roles than the minimum required to use this feature.

    4.  Click **Done**.

        Click Done to create your service account

**Notes**:

- Alternatively, see the [*Create a service account*](https://cloud.google.com/iam/docs/creating-managing-service-accounts#creating) in the IAM documentation for instructions on how to create service accounts using the gcloud command-line interface.
- See the BigQuery documentation for additional details about the [*BigQuery Job User*](https://cloud.google.com/bigquery/docs/access-control#bigquery.jobUser) and [*BigQuery Data Editor*](https://cloud.google.com/bigquery/docs/access-control#bigquery.dataEditor) roles

Setting the BigQuery Data Editor role as described above gives the service account access to all datasets in the project. If more restrictive permissions are required, the BigQuery Data Editor role can be set at the dataset or table level instead. See [Grant access to a resource](https://cloud.google.com/bigquery/docs/control-access-to-resources-iam#grant_access_to_a_resource) in the BigQuery documentation.

Create a JSON key for the service account

The following steps involve downloading a [*service account key*](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys) to the local file system. A service account key is like a password that grants the bearer full access to the service account. These steps should only be performed on a trusted device, and the downloaded file must be handled carefully to avoid accidentally exposing your Google Cloud Platform resources. The file should be deleted after setup is complete (or if setup is abandoned before completion), and you should take care not to leave it in a “recycle bin”. Please also ensure that your service account has only been granted the [*minimum roles and data access*](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege) required to use this feature. If you are hesitant to accept the risks of an exported key, consider using an [*alternative data source*](https://support.google.com/appsheet/answer/10106309) or connecting to BigQuery using [*Integration Connectors*](https://support.google.com/appsheet/answer/16178487).

1.  Click the **More** menu (three dots) in the Actions column of the new service account you created, and select **Manage keys**.

    Manage keys in your service account

2.  Click **Add Key** and select **Create new key**.

    Add key \> Create new key in your service account

3.  Accept the default selection of **JSON** and click **Create**.

    Create private key for the service account in JSON format (default)

4.  Note the file name. You will find this in your browser’s download folder. Depending on your browser type, you may see the downloaded file in the bottom bar of your browser window. Click **Close**.

    View and copy the private key that is saved to your computer

5.  Open the file with a text editor you trust so you can copy and paste the contents in the [*next step*](#add-bigquery-data-source).

## Add the BigQuery data source to an AppSheet app

1.  Sign in to [AppSheet](https://www.appsheet.com).

2.  Go to the **My Account \> Sources**.

3.  Click **+ New Data Source**.

4.  Enter the data source name to use for your new data source in the text box, such as **BigQuery-NYC-Citibikes.**

5.  Select **Cloud Database.**

    Enter data source name as BigQuery-NYC-Citibikes and click Cloud Database

6.  Choose **BigQuery** from the drop-down list of available database types.

    Select BigQuery from available database types

7.  Next, you need to obtain the following three values from the Google Cloud Console and the key file you downloaded previously: the **BigQuery DataSet ID**, the **Google Cloud Project ID**, and the **Service Account key**

8.  To obtain the **BigQueryDataSet ID**, go to the [Google Cloud Console](https://console.cloud.google.com/) and select **BigQuery** under the **Big Data** section in the navigation menu. You may need to scroll down to find it.

    Select BigQuery under the Big Data section in the navigation menu of the Cloud Console

9.  Find the BigQuery dataset that you’d like to use. We’ll use a **public dataset** called **bigquery-public-data:new_york_citibike** in our demo, but you should select the dataset that you would like to use in your app. If you don’t see the dataset you want, click **+ Add Data** and add it.

10. Open the dataset by clicking on the **More** menu (three vertical dots) to the right of the dataset name. Make sure you are at the top level. That is, the dataset level, indicated by this icon:

    Not on a table level, indicated by this icon:

    Click More \> Open to open the dataset

11. Copy the **Dataset ID** so that you can paste it into AppSheet.

    Copy the contents of the Dataset ID field

12. Paste the **Dataset ID** into the **DataSet ID** field in AppSheet's Add database connection information window.

    **Notes**:

    - The Dataset ID has the following format: `<project_id>`**`.`**`<dataset_id>`. You must **replace the . (period) with a : (colon)**. The resulting format will be this: `<project_id>`**`:`**`<dataset_id>`
    - The `<project_id>` component is optional if the dataset is in the same project as the service account. You must always include the `<project_id>` component when connecting to a public dataset. This is because public datasets are stored in the `bigquery-public-data` project, which is different from the project where you created your service account

    For example:

    Past value in Dataset ID field in Add database connection information dialog

13. To obtain the **Google Cloud Project ID**, go back to the Google Cloud Console. Click on the **project name** in the top navigation bar, and then copy the **Project ID** in the Select a project dialog so that you can paste it into AppSheet.

    Obtain the Google Cloud Project ID

14. Paste the **Project Id** into the **Google Cloud Project ID** field in AppSheet's Add database connection information window.

    Paste project ID in Add database connection information dialog

15. To obtain the **Service Account key**, go to the JSON file that was downloaded when you created the key on the Service Account in Google Cloud Console (IAM & Admin). Find the file that was downloaded (it will be in your browser’s download directory) and open it with any text editor (if it is not already open). Copy the entire contents of the file.

16. Paste the contents of the file into the **Service Account key** field in AppSheet's Add database connection information window.

17. Click **Test** and then **Authorize Access.**

    Click Test, then Authorize in the Add database connection information dialog

At this point you no longer need the downloaded JSON file, and we recommend [*deleting it from the filesystem*](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys#file-system) (and be careful not to leave it in a “recycle bin”). If for some reason you want to retain it, be sure to [*move it out of the Downloads folder*](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys#temp-locations) to a secure location.

## Add a BigQuery table to your AppSheet app

1.  In AppSheet, go to **Data ** and click **+** in the top header of the Data panel.

    We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

    ## If you are using the legacy navigation

    Go to **Data \> Tables **and click **+ New Table**.  

2.  Select the data store you created (like **big query NYC citibikes**).

3.  Select Tables or Views. (In this demo, we select **Tables**.) Then, select the table that you want for your App. (In this demo, we select **citibike_stations**.)

    Select tables and then select the citibike_stations table

4.  Mark the table as **Read-Only** to improve performance as the app will not try to recache as often. Click **Add This Table**.

5.  Now, your app will have access to this data as if it were any other table.

6.  **Important**: Don’t forget to add [security filters](https://support.google.com/appsheet/answer/10104488) to limit the number of rows that will be used with AppSheet.
