---
fonte: https://support.google.com/appsheet/answer/10105761?hl=en
baixado: 2026-11-10
---

# App performance: Core concepts

In order to make apps run faster, you need to first understand some core concepts.

Ideally, the users of an app should never need to wait for the app to sync data or react to inputs. A well-tuned AppSheet app can come close to achieving this ideal.

AppSheet apps run on a mobile device or browser. All the table data used in the app is maintained in a local copy on the device or browser. This local copy allows the app to be interactive, responsive, and run offline. The platform needs to ensure that this local data copy stays in Sync with the true source of the data which is in a cloud data provider (like Google Drive or Office365 or SQLServer). 

The following sections provide considerations for improving app performance:

- [Latency versus throughput](#latency-throughput)
- [Improve the speed of sync](#how-sync-works)
- [Improve app performance](#other-considerations)
- [Performance considerations for common data sources](#data-sources)

## Latency versus throughput

When we refer to the **performance** of the app, we typically mean the responsiveness of the app as perceived by the end users of the app. The term **latency** means time spent waiting. App responsiveness is directly related to perceived latency. Our goal is to minimize latency perceived by end-users.

As you understand how AppSheet apps work, you'll see that there are different systems communicating with each other. Each communication involves the transfer of data between the systems. In this context, **latency** refers to the time a system takes to initially respond to a request. The term **throughput** refers to the amount of data that can be transferred per second. So for example, to fetch a spreadsheet from Google Drive, the overall latency is the sum of the initial latency to respond to the request and then the time taken to make the actual data transfer. 

## Improve the speed of sync

The AppSheet app cannot directly connect to the cloud data provider. Instead, it communicates to the AppSheet backend service (the **AppSheet server** in the figure below) which then acts as an intermediary to communicate with the cloud provider. This tiering is necessary for the sake of security but also has performance benefits. 

Initially, let's consider the case of Sync in a read-only app. This behavior also occurs during initial launch of any app and in any app that has the Sync-On-Start option enabled.

- Read Step 1: When the app on the mobile device starts a sync, it requests data from the AppSheet Server. The AppSheet Server in turn requests data from the Cloud Provider. 
- Read Step 2: Once the AppSheet Server receives the data from the Cloud Provider, it computes any virtual columns defined and then returns the data to the app on the mobile device. The app stores the data on the mobile device. 

Note that in step 1, the AppSheet Server may have to fetch many tables from the same or different Cloud Providers. In step 2, all the data is sent together to the app. Later, we will discuss various optimizations that can reduce the data transferred and the time taken in these steps.

Now let's consider the case of an app that has made some data changes (to its local data copy) and is then invoking Sync. The app first sends each of the data updates in order to the AppSheet Server (steps 3 and 4 in the figure) and after that, it performs a read-only sync. 

- Write Step 3: the app sends each of the added, updated, and deleted data rows to the AppSheet Server. If you captured photos, drawings, or signatures, they are sent along with the data rows.
- Write Step 4: When the AppSheet Server receives this information, it writes the data back to the Cloud Provider. If there are any automations defined, they are also run (these will typically require that the updated rows be re-read from the Cloud Provider before executing the action).

As an app creator, you can improve the speed  and performance of Sync. See:

- [Improve the speed of Sync](https://support.google.com/appsheet/answer/10104985)
- [Improve the speed of Sync with data updates](https://support.google.com/appsheet/answer/10104494)

It might also be useful to review this community article: [Obstacles with AppSheet for business due to large data](https://www.googlecloudcommunity.com/gc/AppSheet-Q-A/Obstacles-with-Appsheet-for-Business-Due-to-Large-Data/td-p/526327)

## Improve app performance

In addition to optimizing sync performance, there are other key concepts and technical features to be familiar with when designing a performant app that can scale to many concurrent users:

- [Format rules](https://support.google.com/appsheet/answer/10106703) - Define rules to customize icons, text, and more. Format rules may require a lot of computation each time a screen is scrolled which directly affects interactivity. 
- [Virtual columns](https://support.google.com/appsheet/answer/10106758) - Automatically compute columns using an app [expression](https://support.google.com/appsheet/answer/10106437). Since these are computed for each column and row and the expressions can be complex, there is usually a significant cost in performance if an app has a very high number of virtual columns. In general, it's best to minimize the number of virtual columns if possible.
- [References](https://support.google.com/appsheet/answer/10106510) - Data references are very useful for most applications for usability and to avoid data replication. However they can have a negative impact on performance if they are used excessively because each reference requires a virtual column and additional reads of the referenced data. Consider whether a reference is truly needed in the application before adding them.
- [Data partitioning](https://support.google.com/appsheet/answer/10105383) - Partitioning (dividing) your app’s data into multiple tables can have a positive effect on overall performance, regardless of backend data source type.

&nbsp;

- [Security filters](https://support.google.com/appsheet/answer/10104488) - Provide a way to limit either user access or in general the amount of data being fetched from the back end data source. This can usually have positive effects on overall performance, but special considerations must be taken depending on the back end technology used:
  - Google Sheets - Apps with Sheets fetch the entire Sheet data and apply a filter on the server. If dealing with large amounts of data the performance impact could be negative because the security filter executes on a row-by-row basis.
  - Cloud SQL - Security filters will be converted into a SQL statement and sent to the database. This can usually improve the performance, but if the expression is very complex the performance gains could be negligible because AppSheet converts whatever it can on the database and then the filter is (re)applied at the server.
  - AppSheet databases - Security filters on AppSheet databases should typically improve the performance.

  Although security filters limit data access, they aren't a complete security solution. Users should protect sensitive data operations at the data source level. For more information about securing your data, see [Security: The Essentials](https://support.google.com/appsheet/answer/10105078).
- [Offline data and image caching](https://support.google.com/appsheet/answer/10107724) - When dealing with large datasets, it’s also helpful to consider that offline [caching](https://support.google.com/appsheet/answer/10108551) can be affected, and even cause, the client device to crash if the device is limited on storage and memory.

## Performance considerations for common data sources

In general the AppSheet platform dynamically scales horizontally to serve any size audience. Although the Google infrastructure on which AppSheet runs is equipped to handle extremely high levels of concurrent requests, including millions, the number of concurrent users that AppSheet can support **is strictly governed by the scalability of the data source used in the app**. 

As an analogy, imagine a restaurant that could hypothetically allow unlimited patrons into the waiting area (AppSheet platform), but the kitchen and server staff and other resources, such as dining tables, and how much food available to cook (data source), is what dictates the overall restaurant capacity (that is, how many concurrent customers can be served at one time).

The following table provides performance considerations for the most common AppSheet data sources.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Data source**                                                               | **App performance considerations**                                            |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [AppSheet databases](https://support.google.com/appsheet/answer/12631542)     | AppSheet apps with an AppSheet database data source are:                      |
|                                                                               |                                                                               |
|                                                                               | -   Easy to provision. It's as easy as creating a spreadsheet.                |
|                                                                               | -   Can potentially scale to higher capacities than Google Sheets.            |
|                                                                               | -   High concurrency with 200 requests per 10 seconds.                        |
|                                                                               | -   [Quick                                                                    |
|                                                                               |     sync]                                                                     |
|                                                                               | (https://support.google.com/appsheet?p=offline-sync#sync-cloud-to-datasource) |
|                                                                               |     is enabled by default for all apps that use AppSheet databases.           |
|                                                                               |                                                                               |
|                                                                               | **Summary**                                                                   |
|                                                                               |                                                                               |
|                                                                               | AppSheet databases combine the familiarity of editing data in a table-like    |
|                                                                               | structure with the performance and scale of a cloud database.                 |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Google Sheets](https://support.google.com/appsheet/answer/10106594)          | AppSheet applications using Google Sheets as a data source is very common and |
|                                                                               | practical, especially for small to medium size applications. App creators     |
|                                                                               | performing large scale app deployments with Sheets data sources, however,     |
|                                                                               | should be mindful of how AppSheet uses the Sheets API so as not run into      |
|                                                                               | quota exhaustion issues. Here are some key details to note regarding quota    |
|                                                                               | usage:                                                                        |
|                                                                               |                                                                               |
|                                                                               | -   The [Sheets API                                                           |
|                                                                               |     quota](https://developers.google.com/sheets/api/limits) calculation is    |
|                                                                               |     based on a per minute, per project, per user request basis.               |
|                                                                               | -   All AppSheet apps access the API from a single Cloud project running the  |
|                                                                               |     entire AppSheet environment.                                              |
|                                                                               |     -   This AppSheet project has an unpublished, increased quota that is     |
|                                                                               |         occasionally updated as demand increases.                             |
|                                                                               |     -   Since individual AppSheet apps do not have their own Cloud projects,  |
|                                                                               |         it is not possible to request a quota increase.                       |
|                                                                               | -   The per user quota calculation is typically based on the individual app   |
|                                                                               |     creator’s credentials as the default [access                              |
|                                                                               |     mode](https://support.google.com/appsheet/answer/10105756) is to run as   |
|                                                                               |     the app creator.                                                          |
|                                                                               |                                                                               |
|                                                                               | Again, quota overruns are typically not seen with small to medium             |
|                                                                               | size Sheets-based applications, but application creators should take note of  |
|                                                                               | these API quota considerations when planning large scale deployments to serve |
|                                                                               | many users simultaneously at peak times.                                      |
|                                                                               |                                                                               |
|                                                                               | **Example apps and expected Sheets API quotas**                               |
|                                                                               |                                                                               |
|                                                                               | A **Travel Approval** app - A basic app for submitting travel approval        |
|                                                                               | requests.                                                                     |
|                                                                               |                                                                               |
|                                                                               | -   Runs continuously 24/7 for employees to submit their travel plans for     |
|                                                                               |     approval. There are *no significant usage peaks* as the load is spread    |
|                                                                               |     out over the entire day.                                                  |
|                                                                               | -   The application’s data needs are also comparatively small. Typically just |
|                                                                               |     enough information cover travel details (travel dates, reason for travel, |
|                                                                               |     flight and hotel expenses, and so on).                                    |
|                                                                               | -   Since the data needs are small, and the traffic is spread out over time,  |
|                                                                               |     running as app creator or app user access modes is not a large factor.    |
|                                                                               | -   Summary: Light risk. This app would likely not experience concurrency or  |
|                                                                               |     quota issues with the Sheets API.                                         |
|                                                                               |                                                                               |
|                                                                               | A **Daily Tasks** app - An app to track multiple daily tasks for employees    |
|                                                                               | every morning.                                                                |
|                                                                               |                                                                               |
|                                                                               | -   A large scale app with multiple users and large data amounts accessed     |
|                                                                               |     during a specific time of the day.                                        |
|                                                                               | -   This app could experience issues with API quota limits, especially  if    |
|                                                                               |     the app has peak usage spikes, such as in the morning in a specific       |
|                                                                               |     region.                                                                   |
|                                                                               | -   Large data amounts could further compound the problem especially if each  |
|                                                                               |     user is generating multiple tasks per usage, and if each task has         |
|                                                                               |     multiple data fields.                                                     |
|                                                                               | -   Due to high peak usage times and high data volume, this app could be      |
|                                                                               |     impacted with API quota issues if a large number of people access the app |
|                                                                               |     within a minute.                                                          |
|                                                                               | -   Additionally, if running with creator access mode, this will further      |
|                                                                               |     compound the risk for quota overruns.                                     |
|                                                                               | -   Summary - High risk. This app would likely experience concurrency/quota   |
|                                                                               |     issues with the Sheets API since it has peak usage times and processes    |
|                                                                               |     large data amounts. This could still potentially be moderated if the app  |
|                                                                               |     is running in user access mode, with limited data amounts and if app      |
|                                                                               |     access was spread out over time.                                          |
|                                                                               |                                                                               |
|                                                                               | **Summary**                                                                   |
|                                                                               |                                                                               |
|                                                                               | AppSheet apps with Google Sheets data sources can experience concurrency or   |
|                                                                               | quota issues with the Sheets API if app access time (avoidance of peak usage  |
|                                                                               | spikes), app access mode, and overall data volume are not considered when     |
|                                                                               | designing AppSheet with Sheets architectures.                                 |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Cloud SQL ([MySQL](https://support.google.com/appsheet/answer/10106676),      | AppSheet apps with Cloud SQL data sources will not experience the same quota  |
| [PostgreSQL](https://support.google.com/appsheet/answer/10106598), and [SQL   | limit issues as the Sheets API since Cloud SQL does not even impose any       |
| Server](https://support.google.com/appsheet/answer/10106599))                 | [queries per second (QPS) limits](https://cloud.google.com/sql/faq#sizeqps).  |
|                                                                               |                                                                               |
|                                                                               | If a Cloud SQL instance is receiving excessively high amounts of requests for |
|                                                                               | what it is configured for, the database will experience slowness and timeouts |
|                                                                               | due to resource exhaustion (which will appear in the audit logs). Again, this |
|                                                                               | can be remedied by properly configuring the SQL instance for the additional   |
|                                                                               | traffic.                                                                      |
|                                                                               |                                                                               |
|                                                                               | Additionally, the types of queries that the app is making against the         |
|                                                                               | database and overall data profile (that is, the number of tables, rows        |
|                                                                               | columns and whether database views are used) can also impact performance and  |
|                                                                               | scalability.                                                                  |
|                                                                               |                                                                               |
|                                                                               | The primary factor however that governs scalability is the Cloud SQL instance |
|                                                                               | configuration, including the following:                                       |
|                                                                               |                                                                               |
|                                                                               | -   Number of vCPUs                                                           |
|                                                                               | -   Memory                                                                    |
|                                                                               | -   Storage type and capacity                                                 |
|                                                                               |                                                                               |
|                                                                               | The default production and development configurations for the three database  |
|                                                                               | types (MySQL, PostgreSQL, and SQL Server) are shown below.                    |
|                                                                               |                                                                               |
|                                                                               | +--------------+------------------+-----------------+                         |
|                                                                               | |              | **Production**   | **Development** |                         |
|                                                                               | +--------------+------------------+-----------------+                         |
|                                                                               | | Availability | Highly Available | Single Zone     |                         |
|                                                                               | +--------------+------------------+-----------------+                         |
|                                                                               | | vCPU         | 8                | 4               |                         |
|                                                                               | +--------------+------------------+-----------------+                         |
|                                                                               | | Memory       | 32 GiB           | 16 GiB          |                         |
|                                                                               | +--------------+------------------+-----------------+                         |
|                                                                               | | Storage      | 250 GiB          | 100 GiB         |                         |
|                                                                               | +--------------+------------------+-----------------+                         |
|                                                                               |                                                                               |
|                                                                               | **Summary**                                                                   |
|                                                                               |                                                                               |
|                                                                               | AppSheet apps with Google Cloud SQL data sources will not experience          |
|                                                                               | concurrency issues due to quota overruns. Instead, maximum database           |
|                                                                               | performance is 100% governed by how your instances are configured. In a       |
|                                                                               | production environment with changing needs over time, it’s recommended that   |
|                                                                               | you continuously adjust your SQL instance configurations to best suit your    |
|                                                                               | performance and concurrency goals.                                            |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
