---
fonte: https://support.google.com/appsheet/answer/11903794?hl=en
baixado: 2026-11-10
---

# Use data from Google BigQuery with Connected Sheets

The following sections describe how to use data from Google BigQuery with Connected Sheets:

- [Limits when using BigQuery with Connected Sheets](#limits)
- [Connect Google Sheets to Google BigQuery](#connect-sheets-bigquery)
- [Connect AppSheet to Google Sheets](#connect-appsheet-sheets)

See also the [Connected Sheets GA blog post](https://workspaceupdates.googleblog.com/2020/06/connected-sheets-google-sheets-bigquery.html?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+GoogleAppsUpdates+%28G+Suite+Updates+Blog%29).

You can use data from Google BigQuery with the [BigQuery data source](https://support.google.com/appsheet/answer/11905680) or with Connected Sheets (as described in this topic). To compare the two options, see [Use data from Google BigQuery with AppSheet](https://support.google.com/appsheet/answer/11905679).

If you have a lightweight use case and need to have production support right away, or have a lower license than the Enterprise Standard plan, use Connected Sheets as described in this topic.

## ****Limits when using BigQuery with Connected Sheets

AppSheet enforces the following limits when using BigQuery with Connected Sheets:

- For the current data extraction limits from BigQuery into Google Sheets using Connected Sheets, refer to [files you can store in Google Drive](https://support.google.com/drive/answer/37603).
- This procedure works for **read-only** use cases only from BigQuery into a Google Sheet and then to an AppSheet app. Any data that is written by the app to the specific tab in the Sheet that is connected to Big Query will be overwritten by the next BigQuery refresh, which would result in data loss for the app user.

## Connect Google Sheets to Google BigQuery

Connect Google Sheet to Google BigQuery as described in [Use Connected Sheets in your organization](https://support.google.com/a/answer/9604541). For additional information, see [Get started with BigQuery data in Google Sheets](https://support.google.com/docs/answer/9702507).

When you connect a Google Sheet to a BigQuery table in your Google account, you end up with a tab/sheet with a database icon. For example:

Connected sheet with database icon

However, this table can't be connected to from within AppSheet. If you attempt to do so, an error similar to the following will be displayed:

Error in AppSheet app when connecting directly to a connected sheet

To connect Google Sheets to Google BigQuery, you'll need to do the following:

1.  Set up a refresh schedule in your Google Sheet, as described in [Schedule a refresh](https://support.google.com/docs/answer/9703214#zippy=%2Cschedule-a-refresh)
2.  Pull data into an extract tab/sheet, as described in [Pull data into an extract](https://support.google.com/docs/answer/9703214#zippy=%2Cpull-data-into-an-extract)

## Connect AppSheet to Google Sheets

AppSheet can now use the **extract** tab/sheet as a Google Sheets data source. Remember, you should set the **Are updates allowed?** option to **Read-Only** in AppSheet as there is no ability to write back to BigQuery with this configuration. For more information, see [Tables: The Essentials](https://support.google.com/appsheet/answer/10105821#configure-table).

Set the Table as Read-Only.

If you configured a refresh schedule, the following shows an example of how the refresh options display:

Configured refresh options

Each time the schedule runs it will refresh both of the two tabs and BigQuery will overwrite any changes made to the `Extract` table. This is one of the reasons why this connection from AppSheet should be considered a **read-only** connection.
