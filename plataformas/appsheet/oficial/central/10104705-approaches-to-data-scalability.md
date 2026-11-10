---
fonte: https://support.google.com/appsheet/answer/10104705?hl=en
baixado: 2026-11-10
---

# Approaches to data scalability

When an app starts and fetches data, there are three steps involved:

1.  Cloud to AppSheet server: the data is fetched from the cloud source (a spreadsheet, database, or API) by the AppSheet server.

2.  AppSheet server to the app: the data is sent from the AppSheet server to the app running in a browser or device.

3.  Persist the data locally on the device/browser. AppSheet apps always download their entire working data set to the device or browser. This allows the apps to work seamlessly when offline, partially disconnected, or on a slow network.

App creators should consider how the app will scale when the data sets become large. The primary motivation is performance, of course. If you are loading large amounts of data your app will be less performant and is more likely to experience "out of memory" errors. A security filter, for example, can reduce the amount of data that AppSheet loads on your behalf.

However, there are other motivations as well. For example, Smartsheet does not allow more than 20,000 rows in a single spreadsheet. Google Sheets limits a spreadsheet to 20 million cells. Apps may need to scale to go past these limits.

There are two kinds of app patterns that can lead to large data sets:

- [**Partitionable**](#partitionable): Such apps may have a lot of data rows, but each app user only accesses a smaller subset of the rows. For example, an app that maintains timesheets for employees. Each employee only has one timesheet entry per day, but across a large organization, there may be several tens of thousands of employees.
- [**Non-partitionable**](#non-partitionable): Such apps require each user to have access to a large data set. For example, an app that keeps a catalog of a million products and wants this entire data set accessible in the mobile app.

## Scale partitionable apps

Partitionable apps can scale very effectively. This section identifies the following mechanisms that are used to achieve scale. With these techniques, a properly designed app can even work against data sets that have millions of records.

- [Scale using security filters](https://support.google.com/appsheet/answer/10104706): Reduce the amount of data that AppSheet loads on your behalf. The data is filtered after step 1 (Cloud to AppSheet server). For spreadsheet data sources, the entire sheet is fetched to AppSheet and the filtering only reduces the data in steps 2 and 3. For database data sources with simple security filters, the data is filtered during step 1 (Cloud to AppSheet server) at the database. This can lead to very significant performance improvements.
  Although security filters limit data access, they aren't a complete security solution. Users should protect sensitive data operations at the data source level. For more information about securing your data, see [Security: The Essentials](https://support.google.com/appsheet/answer/10105078).
- [Scale using data partitioning](https://support.google.com/appsheet/answer/10105383): the data is divided into many identical partitions, each with a different subset of the data. Each user gets data from just one specific partition. This technique can be used along with security filters and leads to almost infinite scalability.

Each of these techniques is described in a separate article in this section. The standard recommendations to scale an app are: 

- [Add security filters](https://support.google.com/appsheet/answer/10104488) (requires user sign in or user settings enabled in the app) 
- [Data partitioning](https://support.google.com/appsheet/answer/10105383) -- lets you scale your app while remaining on spreadsheets. 
- Move to a database data source -- see [Use multiple data sources](https://support.google.com/appsheet/answer/10106309) for information about databases (for example MySQL or SQL server).

## Scale non-partitionable apps

AppSheet apps do not work effectively for the second category (apps not suitable for per-user partitioning). If a lot of data must be available to every user of the app, all of it has to be fetched and moved through all three steps. This will certainly lead to an app that becomes unusably slow as the data set scales.
