---
fonte: https://support.google.com/docs/answer/9703001?hl=en
baixado: 2026-11-10
---

# Fix problems with BigQuery data in Google Sheets

## Fix access or sharing problems

For access to BigQuery data in Google Sheets, you need:

- Access to BigQuery. [Learn how to get BigQuery](https://cloud.google.com/bigquery/).
- A project with billing setup in BigQuery. [Learn how to set up Google Cloud billing](https://cloud.google.com/billing/docs/how-to/manage-billing-account).
- A BigQuery Job Creator role on the selected billing project.
- A BigQuery Data Viewer role on the datasets containing the selected table.

If you share a sheet with someone who doesn't meet the criteria above, they'll be able to see analysis created with Connected Sheets and perform regular Sheets operations, but they won't be able to refresh it or create their own connected sheet.

If you share a sheet with someone who doesn't have access to the correct data tables, they won't be able to create or refresh Connected Sheets analysis, and will need to contact the BigQuery admin.

#### Fix problems with scheduled data refresh

**Important: **Scheduled refreshes of Connected Sheets don't propagate any end-user context such as IP address or device information. Virtual Private Cloud Service Controls (VPC-SC) perimeters that use end-user context to restrict access will cause scheduled refreshes to fail.

If you have problems with a scheduled data refresh:

- The schedule owner might have revoked OAuth authorization. Talk to the schedule owner.  
- The schedule owner might not have edit access to the Google Sheet. Talk to the Google Sheet owner to request edit access. [Learn more about Google sharing permissions](https://support.google.com/drive/answer/7166529).
- The schedule owner's account might not be eligible to use BigQuery in Sheets anymore. [Learn what you need to use BigQuery in Google Sheets](https://support.google.com/docs/answer/9703715).
- The BigQuery table might be deleted. Talk to the table owner. 
- The schedule owner's account might be deleted. [Learn how to take over the schedule](https://support.google.com/docs/answer/9703214#takeover). 
- The schedule might be paused because the data source has changed. To unpause the data source, talk to the schedule owner. 

#### Fix problems with query failing

If you have problems with a query failing:

- The BigQuery table might have been deleted. Contact the table owner. To connect to a new table, at the bottom next to "Refresh," click More options More and then **Connection settings**. Click the new table and then **Connect**.
- The columns in the BigQuery table might have changed. Contact the table owner to ask if columns have changed. If they have, reference the correct column in the query.
- You might not have permission to view the tables in BigQuery. Contact the table owner to request access.
- You might not have permission to run jobs on the selected billing project. Go to connection settings and change the billing project or contact the billing project owner to request access.
- Your query results might be too large. Your query will fail if:
  - Pivot tables have over 100K results. To reduce your query results, you can:
    - Use filters to limit results
    - Limit the number of rows per breakout
    - Turn off “show totals” when adding rows, columns, values, and filters
  - Results size is more than 10MB. To reduce size, return fewer rows or columns.
- You're using BigQuery sandbox and might have run into sandbox limits. [Learn more about the limits of the BigQuery sandbox](https://support.google.com/docs/answer/9703715#datalimit). If you've met your data limit, [learn how to upgrade your account](https://support.google.com/docs/answer/9702507#whatyouneed).
