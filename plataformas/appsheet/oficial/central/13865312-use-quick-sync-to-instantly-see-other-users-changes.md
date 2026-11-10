---
fonte: https://support.google.com/appsheet/answer/13865312?hl=en
baixado: 2026-11-10
---

# Use Quick sync to instantly see other users' changes

The **Quick sync** setting allows you to instantly see other users' changes as they are saved. Users only see changes made by other users that are using the same [version of the app](https://support.google.com/appsheet/answer/10104708).

You **shouldn't use** this feature if your app uses [advanced security filters](https://support.google.com/appsheet/answer/13865312#security-filters), if your data sources compute values automatically (for example, if your Google Sheets data source uses formulas), or if your app has virtual columns that require a complete sync to be computed properly.

 

- [Configure Quick sync](#configure)
- [Security filter support](#security-filters)

If users change data directly in the data source (for example, editing directly in Google Sheets) or through another non-AppSheet system, the app will not reflect this updated data until the next sync.

Individual data updates will be cached on AppSheet servers. **If you have strict data residency requirements**, you may not want to use this feature.

## Configure Quick sync

To configure the Quick sync setting, see [Configure offline and sync](https://support.google.com/appsheet/answer/10107724#configure-offline-mode). Quick sync is turned on by default.

For best results, we recommend turning on **Sync on start** and **Automatic updates** when using Quick sync.

## Security filter support

Although security filters limit data access, they aren't a complete security solution. Users should protect sensitive data operations at the data source level. For more information about securing your data, see [Security: The Essentials](https://support.google.com/appsheet/answer/10105078).

Simple security filters that rely on row-scoped calculations (such as value comparisons) or user settings are supported for use with Quick sync. More complex security filters, for example those that rely on values from referenced tables, virtual columns, and other data outside the scope of the row, are not currently supported.

For example, the following simple security filters **are supported**:

- Constants, such as `=TRUE` and `=FALSE` 
- Value comparisons, such as`[Status]='Pending'`
- User settings and email checks, such as `[Assigned To]=USEREMAIL()`

The following complex security filters are **not supported** at this time:

- References in expressions like `[Order].[Assigned To]=USEREMAIL()`
- `SELECT()`, `FILTER()`, and other expressions that are table scoped, such as `SELECT(Table1[Col1], TRUE)`
