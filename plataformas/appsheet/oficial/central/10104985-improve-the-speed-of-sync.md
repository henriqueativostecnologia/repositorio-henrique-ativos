---
fonte: https://support.google.com/appsheet/answer/10104985?hl=en
baixado: 2026-11-10
---

# Improve the speed of Sync

Make sure to read and understand the core concepts affecting app performance. If you can focus on improving Sync performance, it will have the greatest positive impact on the end-users of the app.

In this article, we'll focus on **read-only Syncs** as this affects all apps. There are additional approaches to improve the speed of Syncs that involve data updates, as described in [Improve the speed of Sync with data updates](https://support.google.com/appsheet/answer/10104494).

To improve the speed and performance of Sync, consider the following methods:

1.  [Choose an efficient data provider](#efficient-data-provider)
2.  [Reduce the amount of data transferred](#reduce-data-transferred) during Sync
3.  [Reduce the amount of computation](#reduce-computation) (for spreadsheet formulas and virtual columns) performed during Sync
4.  [Fetch or compute data in parallel](#parallel) (relevant if there are many tables in the app or many expensive virtual columns)
5.  [Use a faster network](#network) (this is relevant for the connection between the device and the AppSheet Server)
6.  [Run Sync in the background](#background) so that the user is not waiting for a Sync to occur

The AppSheet platform provides tools (like the [Performance Profile](https://support.google.com/appsheet/answer/10104997)) for you to understand, analyze, and improve app performance.

## 1. Choose an efficient data provider

AppSheet supports many different data providers. All the data providers vary in terms of the initial latency in responding to a request. Here are some general rules of thumb:

- Database providers are generally better than file system or spreadsheet providers. 
- Among spreadsheet file systems, Google Sheets is the most performant as it has been built from the ground-up to support web-based concurrent data access.
- If using Excel, it is more efficient to use Office365 than a pure file system like Dropbox or Box. With Office365, spreadsheet formulas can be run in the cloud by Office365, whereas with Dropbox and Box AppSheet has to download the entire Excel file and evaluate formulas locally.

In reality, this may not be a choice you have because your data set may already reside in a specific data provider.

## 2. Reduce the amount of data transferred 

Reduce the amount of data transferred by doing one or more of the following:

- [Remove unnecessary data](#remove-unecessary-data)
- [Use security filters](#security-filters)
- [Use data partitioning](#data-partioning)
- [Configure data caching settings](#configure-data-caching-settings)

### Remove unnecessary data

The first step is to remove unnecessary data in the table/worksheet itself. 

- Delete empty rows, including empty rows at the bottom of the sheet.
  If your worksheets contain hundreds or thousands of empty rows, you can greatly improve performance by deleting them.
- Delete empty columns, including empty columns to the right of the sheet.
  If your worksheets contain empty columns, you can greatly improve performance by deleting them.

A spreadsheet *workbook* (that is, file) contains one or more worksheets. The next step is to ensure that there isn't unnecessary data in the spreadsheet workbook. 

- Only include worksheets that the application requires and remove the rest.
  Extra worksheets will add overhead when the data provider is fetching the requested data. Any changes to those worksheets also interferes with caching optimizations.

- Place read-only tables in their own workbook.
  There are greater opportunities to cache read-only tables. When placed in their own workbook, the platform can more accurately track if they have been updated.

### Use security filters

Although security filters limit data access, they aren't a complete security solution. Users should protect sensitive data operations at the data source level. For more information about securing your data, see [Security: The Essentials](https://support.google.com/appsheet/answer/10105078).

While **security filters** are primarily meant to be a security feature, they can also be used as a *scalability feature*, as described in the following sections:

- [Security filters versus table slices](https://support.google.com/appsheet/answer/10104706#security-filters-versus-slices)
- [Security filters with spreadsheet data](https://support.google.com/appsheet/answer/10104706#security-filters-with-spreadsheet-data)
- [Security filters with database data](https://support.google.com/appsheet/answer/10104706#security-filters-with-database-data)
- [Efficient security filter definitions for database data](https://support.google.com/appsheet/answer/10104706#efficient-definitions-for-database-data)
- [Security filters with AppSheet databases](https://support.google.com/appsheet/answer/10104706#security-filters-with-appsheet-databases)

Use security filters to eliminate rows that do not satisfy the filter criteria. If the data comes from a spreadsheet source, the entire spreadsheet is read by the AppSheet Server, the security filter is applied, and the subset of rows that satisfy the condition are sent on to the app. If the data comes from a database source and the filter is simple (such as `[ColumnX] = USEREMAIL()`), then the filter can be "pushed" into the data retrieval from the data source. In other words, the data retrieval from the data source also becomes much more efficient and less data is transferred to the AppSheet provider.

### Use data partitioning

Manage very large data sets by dividing them into partitions. Each user only ever needs the data in one partition. Naturally, this significantly reduces the amount of data transferred. See [Scale using data partitions](https://support.google.com/appsheet/answer/10105383).

### Configure data caching settings

The app may also implicitly reduce the amount of data transferred by avoiding redundant data transfer. Data transfer is redundant if the app already has a cached copy of the latest data available (from a previous sync). In order for caching to be effective, the system needs to record when a cached copy was maintained and check if the data source has been updated since then.

 To configure the data caching settings: 

1.   Open the app in the app editor.
2.  Select **Settings \> Performance**.
3.  [Configure the settings](#configure-settings) under **Sync: Cloud to Data Source**.
4.  Save the app.

We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

 

## If you are using the legacy navigation

 To configure the data caching settings:

1.  Open the app in the app editor.
2.  Select **Behavior \> Offline/Sync**.
3.  [Configure the settings](#configure-settings) under **Sync: Cloud to Data Source**.
4.  Save the app.
     

Configure the data caching settings:

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Server caching                                                                | The AppSheet Server can maintain cached copies of read-only tables for up to  |
|                                                                               | five minutes. If your app depends on reference data that doesn't change       |
|                                                                               | often, be sure to mark the table as Read-Only and enable server caching.      |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Delta sync                                                                    | Enable this option to maintain timestamps for the last time each table was    |
|                                                                               | fetched. On each sync, the AppSheet server tries to determine if the table    |
|                                                                               | has been updated after that timestamp. Only then is the table data retrieved  |
|                                                                               | from the cloud data source.                                                   |
|                                                                               |                                                                               |
|                                                                               | The Delta sync setting is ignored for tables that use security filters.       |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

**Caution**: The Delta sync option has the potential to significantly speed up Sync, but it can cause computed fields to sometimes retain stale values.

- Delta sync is only applicable to tables based on Google Sheets and AppSheet Databases. It checks the `LastModifiedTime` property of the file to determine if it has been updated (updates could happen directly to the spreadsheet). In cloud file systems like Google Drive, this timestamp is not perfectly accurate.
- If the sheet involves formulas fetching data from external sources, the file itself may never reflect a modified timestamp although the computed data in it might change. [Virtual columns](https://support.google.com/appsheet/answer/10106758) relying solely on this data are not recomputed. 

## 3. Reduce the amount of computation 

Computations happen during sync at two places:

- In spreadsheet formulas
- In AppSheet virtual columns

Both can add significant overhead to Sync times.

Spreadsheets use formulas to compute data. Some formulas can be very expensive and long-running. Such formulas can cause significant delays and in extreme cases even timeouts when using AppSheet.

1.  Ensure that the spreadsheet only uses simple/cheap formulas.
2.  Cross-sheet formulas and those using external services (like Google Finance) are likely to severely impact sync [performance.](https://support.google.com/appsheet/answer/10104997)
3.  It is particularly important to minimize worksheet formulas when the data source is Excel on Dropbox or Box, because these formulas must be re-computed by the AppSheet Server each time the Excel worksheet is read. 

Virtual columns in a table are defined by App Formulas and are computed by the AppSheet Server on every sync. App Formulas are very powerful and expressive, but it is possible to write very inefficient App Formulas. For example, in an `Order Capture` app with three tables (`Products`, `Customers`, and `Orders`), let us assume there is a virtual column defined on the `Order` table to find the sum of all prior `Orders` made by the same `Customer` for the same `Product`. Depending on the amount of data in the app, this will probably be very expensive to compute against the entire data set. The [Performance Profile](https://support.google.com/appsheet/answer/10104997) will indicate if virtual columns are contributing significantly to sync time.

## 4. Fetch or compute data in parallel  

So far, we have ignored the fact that most apps have multiple tables. Let's say your app has five tables. Are they fetched from the data source one after the other or are they fetched in parallel? Ideally, this would be as fully parallel as possible, but doing this is resource-intensive for the AppSheet server (each parallel request requires a concurrent *thread* of computation in the server and there is a limit on the total number of threads that can run at the same time). Consequently, we control the degree of parallelism based on the subscription plan of the app owner --- the more expensive plans are given a greater degree of parallelism.

A similar approach is applied to the computation of virtual column values as well.

Increasing parallelism doesn't necessarily always result in faster sync. For example, if you have three tables, two of which take just a second to fetch and the third takes a whole minute to fetch, there will be no perceptible difference when increasing the degree of parallelism. The table that takes a whole minute to fetch dominates all other activities.
You can try out the effect of higher-degrees of parallelism in the app emulator hosted inside the app editor. Note that the effects vary depending on the amount of data in the tables as well. So while the effects may be minimal when developing your app with initial datasets, they may be more pronounced as the app is used and the data sets grow. 

## 5. Use a faster network

Most people intuitively believe that a *faster* network should lead to a faster Sync. The same intuition also leads people to believe that the biggest bottleneck in sync is the speed of the data network (2G vs LTE for example) used by the mobile devices. In most situations however, this is an oversimplification.

In our observation:

1.  Cloud provider **latency** is usually the biggest contributor to slow syncs. The actual data transfer between cloud provider and AppSheet server is pretty efficient (the internet has high throughput).
2.  Network **latency** between the device and the AppSheet server can also add significant delay. We observe this typically with customers who are geographically remote from the AppSheet server cloud.
3.  The actual data transfer from the AppSheet Server to the mobile device is usually very efficient (that is, even though mobile networks may not have great throughput, it is more than sufficient for the data volumes being transferred). The fact that AppSheet compresses the data before transmission helps with this.

This is a very important observation and it is because AppSheet apps typically have relatively small data volumes. Even if the underlying data set is very large, each app user typically only needs a small subset of the data and this is achieved via mechanisms like Security Filters and Data Partitioning.

## 6. Run Sync in the background  

All our discussion so far has been to reduce the actual latency of Sync. However, since all we really care about is latency *perceived* by the end-user, a very sensible additional step is to minimize the impact of Sync latency on the end-user by delaying the Sync or running it in the background.

There is a tradeoff in making this choice. The app is perceived to run faster. However, the data may be stale. You need to pick a suitable balance for your app, and utilize various Sync options to tell AppSheet how you want the system to behave.  When choosing Sync options, consider the following:

- With all Sync options disabled, the default behavior of the app is to sync immediately if a row is added/updated/deleted by the app.
- Enable **Sync on start** to force the app to sync every time it is restarted. This is a good mechanism to limit the staleness of the data.
- Enable **Delayed sync** to queue updates rather than sync them immediately. For apps that are used in remote regions (such as locations with poor internet service), this is a good option. When the user returns an area with good network access, such as the office, they can explicitly click **Sync** to sync all queued updates to the backend. Note that the longer the time between syncs, the greater the possibility for data conflicts because someone else may have updated the same data.
- Enable **Automatic updates** to hide latency without data staleness. This option is appropriate for environments where there is good network connectivity. Any updates made by the app immediately kick off a sync in the background, while the user can continue to use the app. If there are no updates made by the app, the system will still periodically run a sync to ensure that it has the latest data. This option will increase use of battery, network, and server resource and likely run more syncs than are necessary. This will need to be weighed against the benefit of having an app that is always close to up-to-date without users waiting for sync.
