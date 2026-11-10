---
fonte: https://support.google.com/appsheet/answer/16322183?hl=en
baixado: 2026-11-10
---

# Use connections as data sources

This is a **preview release** of Integration Connectors with AppSheet. See [Track and manage feature releases](https://support.google.com/a/topic/1227580). Preview offerings are intended for use in test environments only. This feature is not recommended for use in production apps. For questions or assistance with this feature, contact [AppSheet Support](https://www.appsheet.com/Support/Contact).

Integration Connectors with AppSheet (preview) requires an **AppSheet Enterprise Plus** account.

Before you can use connections as data sources in your apps, the AppSheet team admin needs to [add connections as data sources](https://support.google.com/appsheet/answer/15297394) and then [share the data sources with your team](https://support.google.com/appsheet/answer/10104795#share-data-sources).

As a team admin or team member, use the data source in your app as you would any other data source when you [create an app](https://support.google.com/appsheet/answer/11980957) from existing data or [add a table](https://support.google.com/appsheet/answer/10105821#add) to an existing app.

For example, select the Google BigQuery data source and then the table to add. 

Select BigQuery connector as a data source

The following provides best practices for using connections as data sources in your app.

+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Data source**                                    | **Best practice**                                  | **Description**                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Google BigQuery                                    | Use [security                                      | Although security filters limit data access, they  |
|                                                    | filters](ht                                        | aren't a complete security solution. Users should  |
|                                                    | tps://support.google.com/appsheet/answer/10104488) | protect sensitive data operations at the data      |
|                                                    |                                                    | source level. For more information about securing  |
|                                                    |                                                    | your data, see [Security: The                      |
|                                                    |                                                    | Essentials](htt                                    |
|                                                    |                                                    | ps://support.google.com/appsheet/answer/10105078). |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | Include AppSheet                                   |
|                                                    |                                                    | [expressions](ht                                   |
|                                                    |                                                    | tps://support.google.com/appsheet/answer/10104642) |
|                                                    |                                                    | in the security filters, which will be translated  |
|                                                    |                                                    | to BigQuery SQL and executed on the server before  |
|                                                    |                                                    | the data is downloaded to the app.                 |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | **Note**: Security filters are pushed to the SQL   |
|                                                    |                                                    | Provider only for `AND()`, `IN()`, `NOT()`, and    |
|                                                    |                                                    | `OR()` expressions. Other expressions aren't       |
|                                                    |                                                    | supported for Provider-level querying before the   |
|                                                    |                                                    | row limit is applied. For BigQuery, the row limit  |
|                                                    |                                                    | of 100K is applied on that Provider query, so you  |
|                                                    |                                                    | can get too few rows if you use a security filter  |
|                                                    |                                                    | that isn't purely composed of these expression.    |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | **Examples**:                                      |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | -   Filter by                                      |
|                                                    |                                                    |     [`USEREMAIL()`](https:                         |
|                                                    |                                                    | //help.appsheet.com/en/articles/2357268-useremail) |
|                                                    |                                                    |     to get rows owned or viewable by the currently |
|                                                    |                                                    |     logged-in app user.                            |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | -   Filter by `DateTime` values in the last week   |
|                                                    |                                                    |     or month to get only the most recent data. For |
|                                                    |                                                    |     example, assuming there is a column in the     |
|                                                    |                                                    |     dataset called `DateCreated`, you could use    |
|                                                    |                                                    |     security filter expressions like:              |
|                                                    |                                                    |     -   For the last week:                         |
|                                                    |                                                    |         `[DateCreated] >= TODAY() - 7`             |
|                                                    |                                                    |     -   For the last month:                        |
|                                                    |                                                    |         `[DateCreated] >= TODAY() - 30`            |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | -   Use a combination of [user                     |
|                                                    |                                                    |     settings](ht                                   |
|                                                    |                                                    | tps://support.google.com/appsheet/answer/10106760) |
|                                                    |                                                    |     and security filters to allow your app user to |
|                                                    |                                                    |     limit the data. For example, using the user    |
|                                                    |                                                    |     setting column named `Year` and a column in    |
|                                                    |                                                    |     the dataset called `StartTime`, you can get    |
|                                                    |                                                    |     data from the year 2018 or later (assuming the |
|                                                    |                                                    |     user setting `Year` is set to `2018`), as      |
|                                                    |                                                    |     follows:                                       |
|                                                    |                                                    |     `[Star                                         |
|                                                    |                                                    | tTime] >= DATETIME("1/1/" & USERSETTINGS("YEAR"))` |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
|                                                    | Use BigQuery Views (read only)                     | You can create specific                            |
|                                                    |                                                    | [vi                                                |
|                                                    |                                                    | ews](https://cloud.google.com/bigquery/docs/views) |
|                                                    |                                                    | for AppSheet in BigQuery that have potentially     |
|                                                    |                                                    | complex SQL queries to create a limited number of  |
|                                                    |                                                    | rows from the dataset. When setting-up the         |
|                                                    |                                                    | BigQuery data source as a table in your app,       |
|                                                    |                                                    | select from the list of views in your project as   |
|                                                    |                                                    | well as from the base datasets.                    |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | **Note**: BigQuery views are read-only so changes  |
|                                                    |                                                    | made in AppSheet will not sync back to the         |
|                                                    |                                                    | BigQuery dataset.                                  |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
|                                                    | Create a new BigQuery Table                        | BigQuery allows you to set up a copy of a table    |
|                                                    |                                                    | that can be re-created periodically based on a     |
|                                                    |                                                    | scheduled query. This is similar to a view, but it |
|                                                    |                                                    | is a physical table that contains the subset of    |
|                                                    |                                                    | data. This can also be used to reduce the number   |
|                                                    |                                                    | of columns in order to simplify the table          |
|                                                    |                                                    | structure.                                         |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| ServiceNow                                         | Filter tables                                      | When you configure the ServiceNow connection, we   |
|                                                    |                                                    | recommend that you specify the tables to include   |
|                                                    |                                                    | in the **Filter Tables** field. Otherwise, you     |
|                                                    |                                                    | might experience significant delays when loading   |
|                                                    |                                                    | your data.\                                        |
|                                                    |                                                    |                                                    |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | Filter tables field when configuring ServiceNow    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
