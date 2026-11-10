---
fonte: https://support.google.com/appsheet/answer/10104997?hl=en
baixado: 2026-11-10
---

# Monitor app performance using the performance analyzer

AppSheet maintains a performance analyzer for every app. The performance analyzer is similar to the Audit History log, recording each sync, add, update, or delete recorded by the AppSheet backend. Along with each entry, there is detailed performance information captured during the execution of the operation. 

- [Access the performance analyzer](#access)
- [Tips for analyzing performance information](#tips)

## Access the performance analyzer

To monitor app performance using the performance analyzer, do one of the following:

- Open your app in the editor, go to the **Manage \> Monitor** tab, expand **Performance Profile**, and click **Launch performance analyzer**.
- (AppSheet admins only) Use the AppSheet Admin Console (preview) to [view details for an app](https://support.google.com/appsheet/answer/15098215) in your team or organization and select **More**  **\> Performance analyzer**.

The performance analyzer opens and displays the following information:

- A list of recommendations for improving performance, if applicable
- Summary graphs showing:
  - Average duration (seconds) per operation type
  - Average virtual column computation time (seconds) by app version

For example:

- Audit History log results based on filters selected (listed below)

Do any of the following tasks:

- Filter the log by:
  - Syncs, Adds, Updates, Deletes, API calls, or Documents
  - Start or end date
  - Failures only
  - Table name, user ID, or rule name
- Within a record, click the **Performance** icon to view performance details.
- Optionally, click **Download Search results** to download a copy of the search results as a JSON payload.

By default, the performance analyzer is shown for a limited recent period of time. Richer filtering and analysis capabilities are available as part of an AppSheet Enterprise Plus subscription. See [How to choose a subscription](https://support.google.com/appsheet/answer/10105400).

## Tips for analyzing performance data

When analyzing the performance data, look for:

- Tables that take a long time to read. Perhaps they have too much data?
- Virtual column expressions that take a long time to read. Perhaps they can be written more optimally?

Most often, a long sync time is due to the number and size of tables. Consider the following:

- If you 10 tables in your app, AppSheet's server has to read them all from the cloud backend. AppSheet will only read a few of them at a time in parallel. For example, accounts with self-service plans will only have 2 or 3 threads loading tables in parallel. Business subscriptions will have 4 or 5 threads loading tables in parallel.
- If a table is very large or takes a long time to load, then it slows down the overall sync time.
- Often there are references between tables and, therefore, automatically added [`REF_ROWS()`](https://support.google.com/appsheet/answer/10107364) virtual columns that compute the relationships between the tables. It may appear that one of the virtual column computations is taking a long time to complete. However, this is rarely the case. The time required by this computation is typically used to fetch the table itself before computing the relationship. In other words, fetching tables is almost always the source of delay.

  **Note**: If you write your own virtual column expressions with inefficient [`SELECT()`](https://support.google.com/appsheet/answer/10108207) expressions, this may cause delays in sync time.
