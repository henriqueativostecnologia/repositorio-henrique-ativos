---
fonte: https://support.google.com/docs/answer/9703000?hl=en
baixado: 2026-11-10
---

# Write & edit a query

If you want to do more complicated analysis, such as joining data from more than one BigQuery table, you can write a custom query.

**Important:**

- To access BigQuery data in Google Sheets, you need access to BigQuery. Learn how to [Get started with BigQuery](https://support.google.com/docs/answer/9702507).
- You can only use [Google Standard SQL](https://cloud.google.com/bigquery/docs/reference/standard-sql/introduction#bigquery-sql-dialects) with the BigQuery connector.

1.  On your computer, open a spreadsheet in [Google Sheets](https://docs.google.com/spreadsheets/u/0/).
2.  In the menu at the top, click **Data** and then **Data connectors** and then **Connect to BigQuery**.
3.  Select a project.
4.  Click **Saved queries and query editor**.
5.  Enter a query.
    - To preview how much data your query scans, at the bottom right of the editor, click **Preview results**.
6.  Click **Insert results**.

**Tips:**

- If you're a developer, learn how to [Use Apps Script with Connected Sheets](https://developers.google.com/apps-script/guides/sheets/connected-sheets).
- To find certain new saved queries, enable the Dataform API. [Learn more about Dataform API](https://cloud.google.com/dataform/reference/rest).
- Validate data types between BigQuery and Sheets data for analysis.

#### Use saved queries in Connected Sheets

To create queries in Connected Sheets, you can access saved queries from BigQuery projects. [Learn more about saved queries](https://cloud.google.com/bigquery/docs/saved-queries-introduction).

1.  On your computer, open a spreadsheet in [Google Sheets](https://docs.google.com/spreadsheets/u/0/).
2.  In the menu, at the top of the spreadsheet, click **Data** and then **Data connectors** and then **Connect to BigQuery**.
3.  Select a project.
4.  Click **Saved queries and query editor** and then **BigQuery saved queries**.
5.  Select a project and then a saved query.
6.  Click **Connect**.

To edit a saved query, update it directly within BigQuery. The updated query appears in Connected Sheets within 5 minutes.

To keep your saved queries up to date whenever you update saved queries in BigQuery:

1.  In the Connected Sheet, sync your saved queries through **Sync from BigQuery**.
2.  In the “BigQuery editor,” click **Connect**.

[Learn more about saved queries](https://cloud.google.com/bigquery/docs/saved-queries-introduction)

When an error occurs due to a modified or deleted saved query, you can update the connection from the error dialog or BigQuery editor.

1.  At the top right of the preview sheet, open **Connection settings**.
2.  To update the connection, click **Sync from BigQuery** and then **Connect**.
3.  To update the connection for the following cases:
    - **Modified query:** Click **View error** and then **Sync saved query**.
      - Or, you can open the query editor. Click **Edit** and then **Sync saved query** and then **Connect**.
    - **Deleted query:** Click **View error** and then **Use as custom query**.
      - Or, you can:
        1.  To open the query editor, click **Edit**.
        2.  Change to another query or unlink the existing query.
        3.  Click **Connect**.

#### Add parameters to your query

To use the value of one or more cells in a custom query, set up a parameter.

1.  In a Connected Sheet, open **Saved queries and query editor.**
2.  On the right, click **Parameters** and then **Add**.
3.  Enter a name for the parameter and click **Cell Reference.**
4.  Type or select a data range of one or more cells and click **OK**.
5.  In the BigQuery parameter window, click **Add**.
6.  In the query editor, type your query.
    - **Tip**: When using a list parameter, use the UNNEST() function.
7.  When the data is ready, click **Connect**.

#### Compare data in Sheets and BigQuery

To compare data from Sheets with data in BigQuery, you might need to change the data type. For example, if a column is a String type in BigQuery, then it must be plain text in Sheets to be compared correctly. If the data type in the spreadsheet and BigQuery are different, you can:

- [Change how the data is formatted in Sheets](https://support.google.com/docs/answer/56470). For example, data formatted as number could be changed to plain text.
- Cast the value in a query. For example: WHERE zip_code = CAST(@ZIP AS string).

## Example queries

### Simple query:

`SELECT word, SUM(word_count) AS word_count`

`` FROM `bigquery-public-data.samples.shakespeare` ``

`WHERE word IN ('me', 'I', 'you')`

`GROUP BY word;`

### Parameterized query:

- Parameter `@STATENAME` data range = `Sheet1!A1`

|     |            |
|-----|------------|
|     | **A**      |
| 1   | California |

`SELECT SUM(kw_total) as sum_kw_total`

`` FROM `bigquery-public-data.sunroof_solar.solar_potential_by_censustract` ``

`WHERE state_name = @STATENAME;`

### Parameterized query with IN():

- Parameter `@STATENAMES` data range = `Sheet1!A1`

|     |                                     |
|-----|-------------------------------------|
|     | **A**                               |
| 1   | Alaska, New York, Delaware, Florida |

 

`SELECT state_name, SUM(kw_total) AS sum_kw_total`

`` FROM `bigquery-public-data.sunroof_solar.solar_potential_by_censustract` ``

`WHERE state_name IN (SELECT TRIM(s) FROM UNNEST(SPLIT(@STATENAMES, ',')) s)`

`GROUP BY state_name;`

 

[Next: Fix problems with BigQuery data in Sheets](https://support.google.com/docs/answer/9703001)

## Related resources

- [Get started with BigQuery data in Sheets](https://support.google.com/docs/answer/9702507)
- [Sort & filter your BigQuery data in Sheets](https://support.google.com/docs/answer/9702999)
- [Analyze & refresh a query with BigQuery data in Sheets](https://support.google.com/docs/answer/9703214)
- [Fix problems with BigQuery data in Sheets](https://support.google.com/docs/answer/9703001)
