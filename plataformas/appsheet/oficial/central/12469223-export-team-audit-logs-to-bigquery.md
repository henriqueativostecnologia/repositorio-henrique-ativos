---
fonte: https://support.google.com/appsheet/answer/12469223?hl=en
baixado: 2026-11-10
---

# Export team audit logs to BigQuery

**Notes**:

- Teams are supported for Enterprise plans only.
- Only team **root** or **admin** can export team audit logs to BigQuery

To monitor recent activity for a team app, you can use AppSheet's Audit History, as described in [Monitor team app activity using Audit History](https://support.google.com/appsheet/answer/11918345#audit-history).

Alternatively, you can export the Audit History logs for your team to BigQuery to manage and analyze the data.

Benefits of using BigQuery include:

- Monitor recent activity across multiple team apps 
- Use your existing monitoring tools to analyze the data
- Query the Audit History logs for specific data across team apps
- Extend the retention period for your AppSheet audit logs

Export your team audit logs to BigQuery as described in the following sections:

- [Configure the export of team audit logs to BigQuery](#configure)
- [Run a query on the exported data](#run-query)
- [View and edit a team connection](#view-edit-team-connection)
- [Delete a team connection](#delete-team-connection)

## Configure the export of team audit logs to BigQuery

To configure the export of team audit logs to BigQuery, perform the following steps:

- [Step 1: Create a BigQuery dataset in your Google Cloud project](#create-dataset)
- [Step 2: Connect to the BigQuery dataset from your AppSheet team](#connect-to-bigquery-dataset)
- [Step 3: Update the BigQuery dataset permissions in the Google Cloud console](#update-dataset-permissions)
- [Step 4: Test the connection to the BiqQuery dataset](#test-bigquery-connection)

### Step 1: Create a BigQuery dataset in your Google Cloud project

To create a BigQuery dataset in your Google Cloud project:

1.  In the Google Cloud console, on the project selector page, select or [create a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

    [Go to Google Cloud console](https://pantheon.corp.google.com/projectselector2/home/dashboard)
     
2.  Open the BigQuery page in the console.

    [Go to the BigQuery page](https://console.cloud.google.com/bigquery)
     
3.  Create a new dataset for your AppSheet data, as described in [*Creating datasets*](https://cloud.google.com/bigquery/docs/datasets).
    For example:

### Step 2: Connect to the BigQuery dataset from your AppSheet team

To connect to the BigQuery dataset from your AppSheet team:

1.  Sign in to [AppSheet](http://www.appsheet.com/).
2.  Select **My team** in the account profile drop-down.
3.  Click the **Settings** tab.
4.  Under **Configure Audit Log Export**, click **Add a new export**.
5.  Enter values for the following fields:
     
    |                       |                                                                                                                                     |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| **Field**             | **Description**                                                                                                                     |
| GCP Project ID        | ID of your Google Cloud project.                                                                                                    |
| BigQuery Dataset Name | Name of the [BigQuery dataset](https://cloud.google.com/bigquery/docs/datasets-intro) to connect to. For example: **appsheet_logs** |
| Table Name            | Name of the table. Defaults to **audit_log_export**.                                                                                |
6.  Click **Save**.
    AppSheet generates a new service account in an AppSheet-owned Google Cloud project. This service account is associated with your AppSheet team account. 
7.  Click **Copy**  Copy icon to copy the service account name. It is needed in the next step.

### Step 3: Update the BigQuery dataset permissions in the Google Cloud console

To update the BigQuery dataset permission in the Google Cloud console:

1.  Open the BigQuery page in the console.
     
    [Go to the BigQuery page](https://console.cloud.google.com/bigquery)
     
2.  Select the new **BigQuery dataset** in the Explorer panel.
3.  Select **Sharing \> Permissions**.
4.  Click +**Add principal**.
5.  In the **New Principals** field, paste the service account name that you copied in the last step.
6.  In the **Role** drop-down, select [**BigQuery Data Editor**](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor).
    Type the role name in the **Filter Type to filter** field to easily locate it in the list of roles.
    To minimize unnecessary exposure of your Google Cloud Platform resources, we recommend following the [*principle of least privilege*](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege) and not granting any other roles than the minimum required to use this feature.
7.  Click **Save**.

After the BigQuery dataset permissions are updated, a new table, **audit_log_export**, is created for your dataset.
 

audit_log_exports table displaying the schema tab

### Step 4: Test the connection to the BiqQuery dataset

To test the connection to the BigQuery dataset:

1.  Sign in to [AppSheet](http://www.appsheet.com/).
2.  Select **My team** in the account profile drop-down.
3.  Click the **Settings** tab.
4.  Under **Configure Audit Log Export**, click **Test** associated with the configured export that you want to test.

The following message displays if the connection is successful: `Connection successful`

If an error is returned, ensure that the [BigQuery dataset has been created](#create-dataset) and the appropriate [permissions](#update-dataset-permissions) have been set.

## Run a query on the exported data

AppSheet exports to BigQuery the Audit History logs for your team approximately every **hour** starting from the time the connection is configured between AppSheet and BigQuery.

After you have configured the export of team audit logs to BigQuery, you can [run an interactive or batch query](https://cloud.google.com/bigquery/docs/running-queries) on the dataset. 

Rows added to BigQuery initially have a `_PARTITIONTIME` of null. If you use the *default* query set by BigQuery, you will not get results. 

To run an interactive query:

1.   Open the BigQuery page in the console.
     
    [Go to the BigQuery page](https://console.cloud.google.com/bigquery)
     
2.  Select the **audit_log_export** table for the BiqQuery dataset in the Explorer panel.
3.  Click **Query \> In new tab** or **Query \> In split tab**.
4.  Update the query details. (See the [sample query](#sample-query) below.)
5.  Click **Run**.

### Sample query

The following sample query:

- Selects all columns from the **audit_log_export** table in the ***`dataset-id`*** dataset in the ***`project-id`*** project that have no `_PARTIONTIME` (new logs) or that were logged before the current date.
  To populate *`project-id.dataset_id`*, you can copy the string by selecting **More ** Three-dot menu vertical **\> Copy ID** for the dataset in the BigQuery Explorer panel. The result will include both values in the proper format.
- Orders the events so that the most recent are first.
- Limits the results to 1000 events. 

`SELECT`
` *`
`FROM`
``  ` ``*`project-id`*`.`*`dataset-id`*`` .audit_log_export` ``
`WHERE`
` _PARTITIONTIME IS NULL OR DATE(_PARTITIONTIME) <= CURRENT_DATE()`
`ORDER BY OperationTimestamp DESC `
`LIMIT 1000;`

### Sample query results 

The following shows the Query results: 

Sample query and results in Google Cloud console

## View and edit the audit log export configuration for a team

To view and edit the audit log export configuration for a team:

1.  Sign in to [AppSheet](http://www.appsheet.com/).
2.  Select **My team** in the account profile drop-down.
3.  Click the **Settings** tab.
4.  Under **Configure Audit Log Export**, click the configured export that you want to edit.
    The Edit audit log export dialog displays. 
5.  Edit the configured export details.
6.  Click **Save**.

## Delete an audit log export configuration for a team

To delete an audit log export configuration for a team:

1.  Sign in to [AppSheet](http://www.appsheet.com/).
2.  Select **My team** in the account profile drop-down.
3.  Click the **Settings** tab.
4.  Under **Configure Audit Log Export**, click **Delete**  associated with the configured export that you want to delete.
5.  When prompted, confirm the action.
