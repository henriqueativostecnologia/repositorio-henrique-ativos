---
fonte: https://support.google.com/appsheet/answer/10105383?hl=en
baixado: 2026-11-10
---

# Scale using data partitions

An AppSheet app defines a table as having one table source. The table source is usually a spreadsheet file with an optional worksheet name, but it could also be a database table or other table source.

When using the data partition, you:

1.  Partition (or divide) the rows of the table into many table sources
2.  Register these different table sources in the app's table definition using the app editor
3.  Provide a partition expression that lets the system determine which table source to use for which user

For example, if you have a table of timesheet entries for employees and there are 100,000 employees, you can partition this data into 10 separate sheets or partitions, each holding 10,000 employees. The partition expression will identify a specific partition for each user based on the [`USEREMAIL()`](https://support.google.com/appsheet/answer/10108210) or [`USERSETTINGS()`](https://support.google.com/appsheet/answer/10108291) values.

Data partitions are a powerful mechanism to scale your app while keeping your data in the format of familiar spreadsheet systems like Google Sheets, Excel, or Smartsheet. However, because you have divided your data set into several physical sheets, you may create extra management overhead for data maintenance and reporting.

**Important**: It is important that all the partitions have **identical column structure**. AppSheet cannot guarantee this behavior, so this becomes an additional responsibility for the app creator.

## Data partitioning: Multiple worksheets

Whatever the data source, you can partition the data into several worksheets in the same workbook/spreadsheet. See [Configure table settings](https://support.google.com/appsheet/answer/10105821).

Partition across many worksheets

## Data partitioning: Multiple files or sources

Whatever the data source, you can partition your table into files or sources. See [Configure table settings](https://support.google.com/appsheet/answer/10105821).

**Note**: All partitions must belong to the same data source at this time.

Partition using multiple spreadsheets

## Data partitioning: Maximal scale

The different data partitioning mechanisms can be combined. The data can be partitioned across several spreadsheet workbooks and each can be partitioned across several worksheets. It is important that each of the workbooks has identically named worksheets. A security filter may further reduce the data sent to the mobile device. This combination will maximize the scale of the app.

As long as each user of the app needs only a reasonably small subset of the overall table, the underlying data can scale almost infinitely in this fashion. Users on the Smartsheet platform can easily scale past the 20,000 row limit imposed by Smartsheet. Users on the Google Sheets platform can now scale up to [20 million cells](https://workspaceupdates.googleblog.com/2026/09/doubled-cell-limits-in-google-sheets-now-generally-available.html?m=1).

## Data partitioning: Other scenarios

While data partitioning is primarily a feature to improve performance at scale, it can also be a convenient mechanism to handle deployment scale in a relatively common scenario. It is sometimes the case that data sets needs to be maintained in separate physical containers (tables of a **single** database or spreadsheet files accessible by a **single** Google account source) for reasons other than performance. For example, if an app is used by five different clients, it might be important to keep each client's data in a separate sheet. However, if you want to build a single app that is used by all five clients, data partitions provide a convenient solution. You can build, maintain and distribute a single app, yet each client sees just their own data and the data sets for each client are all kept physically distinct.
