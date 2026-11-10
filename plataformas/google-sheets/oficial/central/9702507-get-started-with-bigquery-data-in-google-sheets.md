---
fonte: https://support.google.com/docs/answer/9702507?hl=en
baixado: 2026-11-10
---

# Get started with BigQuery data in Google Sheets

You can access, analyze, visualize, and share billions of rows of data from your spreadsheet with Connected Sheets, the new BigQuery data connector. You can also use Connected Sheets to: 
 

- Collaborate with partners, analysts, or other stakeholders in a familiar spreadsheet interface. 
- Ensure a single source of truth for data analysis without additional .csv exports.
- Streamline your reporting and dashboard workflows.

Connected Sheets runs queries on BigQuery on your behalf either when manually requested or on a defined schedule. Results of those queries are saved in your spreadsheet for analysis and sharing.

[Watch a video tutorial to learn more about working with BigQuery data in Google Sheets](https://www.youtube.com/playlist?list=PLU8ezI8GYqs74i8hy_qln3FvkAuSpE-r1).

**Tip:** If you used the historical data connector, you can use extracts to [create the same table view you see in your previous workflow](https://support.google.com/docs/answer/9703214). You can also [set up scheduled refreshes to automatically update your data](https://support.google.com/docs/answer/9703214#refresh).

**Important:** When you access BigQuery data in Connected Sheets, entries are recorded in Cloud Audit Logs. The logs show who accessed the data and when. Only people with proper authorization can access log records. 

You can find the [spreadsheet ID in the audit log](https://support.google.com/a/answer/9604541). Every spreadsheet has a unique spreadsheet ID value containing letters, numbers, hyphens, or underscores. You can also find the spreadsheet ID in a Google Sheets URL.

[Learn more about Cloud Audit Logs](https://cloud.google.com/logging/docs/audit).

To restrict access to Google Cloud resources, you can use VPC Service Controls. Because VPC Service Controls does not support Sheets, you might not be able to access BigQuery data that VPC Service Controls protects. If you have the required permissions and meet the VPC Service Controls access restrictions, [you can use the VPC Service Controls to allow queries issued through Connected Sheets](https://cloud.google.com/bigquery/docs/connected-sheets).

## Work with sample BigQuery data in Google Sheets

To understand how Connected Sheets works, you can explore connected sheet examples with public data. 

1.  On your computer, [open the Google Sheets template gallery](https://docs.google.com/spreadsheets/u/0/?tgif=c&ftv=1).
2.  Choose one of the connected sheet Examples.

## What you need

To access BigQuery data in Google Sheets, you need to meet all of the following requirements:

- Access to the Google Cloud platform. If you're an admin, [learn how to turn on GCP for your organization.](https://support.google.com/a/answer/9197205)
- BigQuery access. [Learn how to get BigQuery](https://cloud.google.com/bigquery/).
- A project with billing setup in BigQuery. [Learn how to set up Google Cloud billing](https://cloud.google.com/bigquery/docs/sandbox).
  - If you don't have a project with billing setup, you can work with BigQuery data in a trial environment. [Learn how to try BigQuery](https://cloud.google.com/bigquery/docs/sandbox).
- [Learn more about the permissions and roles needed to access a BigQuery table or dataset.](https://support.google.com/a/answer/9604541)

## Add a BigQuery project

**Important:** You can’t change BigQuery data from within Google Sheets.

1.  On your computer, open a spreadsheet in [Google Sheets](https://docs.google.com/spreadsheets/u/0/).
2.  In the menu at the top, click **Data** and then  **Data connectors** and then  **Connect to BigQuery**.
3.  Choose a project.
    - If you don’t find any projects, [you need to add one](https://cloud.google.com/bigquery/quickstart-web-ui).
4.  Choose a table or view.
    - You can pick from any company table you have access to or from public data sets.
5.  Click **Connect ** and then  **Start analyzing**.

### Import datasets with Connected Sheets

If you have a large .csv file to import into Sheets or to upload from Drive, you can also choose to import the file to BigQuery directly from Sheets and continue your analysis using Connected Sheets. This allows users to open .csv files of any size and analyze them using familiar Sheets tools.

**Tip:** If you import into Sheets or upload from Drive and get the message “This file is too large to import directly into Google Sheets,” use Connected Sheets.

To import a file through Connected Sheets:

1.  Open the file.
2.  In the menu at the top, click **Data** and then **Data connectors** and then **Connect to BigQuery**.
3.  Under “Select Google Cloud project,” search for your project.
4.  Enter a name for your table.
5.  Click **Continue**.
    - A pop-up shows after the file is uploaded.
6.  To check your file, in the pop-up, click **Open file**.

## Add an alias to your columns for easy reference

Connected Sheets allows you to assign custom, user-friendly names (aliases) to your BigQuery column headers. This makes your data more customizable and easier to read within Google Sheets without changing the underlying BigQuery schema.

- There can only be one alias for a column, and it will use the same naming format as calculated columns in Connected Sheets.
- This alias only persists across a single BigQuery connection and its related database items within a single workbook.
- Multiple data sources in a single spreadsheet do not share aliases, even if the connection details are the same.
- Calculated columns cannot also have an alias assigned to them.

**Set up a column alias**

1.  On your computer, open a spreadsheet in Google Sheets that is connected to BigQuery data.
2.  At the top of the column you want to update, click the drop-down arrow.
3.  Click **Rename column with alias**.
4.  Enter a new name for the column and click **Save**.
5.  After you save the alias, refresh any linked objects to see the updated column names.

You can use either the alias you chose or the original column name when you refer to a column in a formula or range. If you update or remove an alias, refresh the database objects to see the updates.

## Use Connected Sheets on the Google Sheets app 

Using the Google Sheets app on your mobile device, you can:

- View Connected Sheets data.
- View calculated column formulas, filters and sorts, and connection settings.
- Copy and paste data from Connected Sheets.

To create, edit, or refresh data in Connected Sheets, open Google Sheets on a computer.

## [Next: Sort & filter your BigQuery data in Sheets](https://support.google.com/docs/answer/9702999%20)

## Related resources

[Sort & filter your BigQuery data in Sheets](https://support.google.com/docs/answer/9702999)
[Analyze & refresh your BigQuery data in Sheets](https://support.google.com/docs/answer/9703214)
[Write & edit a query with BigQuery data in Sheets](https://support.google.com/docs/answer/9703000)
[Fix problems with BigQuery data in Sheets](https://support.google.com/docs/answer/9703001)
[Share files from Google Drive](https://support.google.com/drive/answer/2494822?hl=en&co=GENIE.Platform%3DAndroid)
