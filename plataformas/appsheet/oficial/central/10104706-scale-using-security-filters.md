---
fonte: https://support.google.com/appsheet/answer/10104706?hl=en
baixado: 2026-11-10
---

# Scale using security filters

Although security filters limit data access, they aren't a complete security solution. Users should protect sensitive data operations at the data source level. For more information about securing your data, see [Security: The Essentials](https://support.google.com/appsheet/answer/10105078).

If you are loading large amounts of data your app will be less performant and is more likely to experience "out of memory" errors. A security filter can reduce the amount of data that AppSheet loads on your behalf.

A [security filter](https://support.google.com/appsheet/answer/10105821#security-filter) is an expression that is evaluated on each row in a table and returns true or false. If true, the row is included in the app and if false, the row is not included. While security filters are primarily meant to be a security feature, they can also be used as a scalability feature. 

Security filters usually compare data from the row with some user-specific data (such as, the user's email or some user setting value). For example, the app user's email address might be used to retrieve only the records that have that email value in a specific column.

Learn more about scaling using security filters in the following sections.

- [Security filters versus table slices](#security-filters-versus-slices)
- [Security filters with spreadsheet data](#security-filters-with-spreadsheet-data)
- [Security filters with database data](#security-filters-with-database-data)
- [Efficient security filter definitions for database data](#efficient-definitions-for-database-data)
- [Security filters with AppSheet databases](#security-filters-with-appsheet-databases)

## Security filters versus table slices

As covered in the following video, a security filter functions differently than a [table slice](https://support.google.com/appsheet/answer/10106592). Slices download all of the data to the client before filtering the data. Security filters retrieve only the records that meet the expression criteria, which restricts the content that gets downloaded to the client.

Video: https://www.youtube.com/watch?v=YvauqE63tGI

## Security filters with spreadsheet data

When reading data from a spreadsheet source, the entire spreadsheet or worksheet is retrieved from the cloud backend before the security filter is applied. Therefore, this does not reduce the time needed for this initial step of the sync process. However, it can significantly reduce the time needed for the second step (sending the data to the app) and can significantly reduce the time and space needed for the third step (saving the data locally with the app).

## Security filters with database data

When security filters are used with database sources, there is the potential for the system to convert the security filter into a database query. To explain, if the underlying database table has a million records but the security filter limits the table to those where the value of the Email column is `mary@mydomain.com`, there are two ways this can be executed:

- Fetch all of the million rows from the database to the AppSheet backend, evaluate the filter and retain just the ten records that match, or
- Send the database a query: `SELECT * from MyTable where Email =mary@mydomain.com`
  The database would return just the ten records that match. 

Obviously, the second approach is much more efficient. Database systems have techniques like indexing that can run such queries quickly. AppSheet can scale to handle millions of database records, provided the security filters can be mapped to efficient queries.

AppSheet attempts to send the security filter as an SQL query for the following database providers:

- [AppSheet databases](#security-filters-with-appsheet-databases)
- Google BigQuery
- MySql
- Microsoft SQL Server
- MariaDB
- Oracle
- Postgres
- Redshift
- Salesforce

## Efficient security filter definitions for database data

The best way to ensure that a security filter is efficient is if it reduces to a simple comparison of a column to a value, or if it involves an [`AND()`](https://support.google.com/appsheet/answer/10107398) with two or more such comparisons. More complex conditions are almost certain to lead to inefficiency as the data set scales.

Here is the list of simple conditions that AppSheet does recognize and push into the SQL query:

- `[Column] = `*`constant-value`*
- `[Column] < `*`constant-value`*
- `[Column] > `*`constant-value`*
- `[Column] <= `*`constant-value`*
- `[Column] >= `*`constant-value`*
- `IN([Column], {`*`constant-value1`*`, `*`constant-value2`*`, ... `*`constant-valueN`*`})`
- `AND(`*`simple-condition1`*`, `*`simple-condition2`*`, ... `*`simple-conditionN`*`)`

**Notes**:

- `AND()` and `IN() `conditions don't work when using [Salesforce](https://support.google.com/appsheet/answer/10106381) as a data provider.

- In general, for efficiency, avoid complex `NOT()` and `OR()` expressions in the security filter. However, these expressions are compatible with connected tables with [Google BigQuery](https://support.google.com/appsheet/answer/11905680) and [AppSheet databases](#security-filters-with-appsheet-databases).

**Almost all other conditions are not pushed into the SQL queries (such as `NOT()` or `OR()` expressions)**. The platform does make an effort to push partial conditions. For example:

- `AND([Column1] = 5, LEN(CONCATENATE([Column2], " file")) < 20)` - The second condition is not one of the simple conditions due to the `LEN(CONCATENATE([Column2], " file"))` part of the expression, but the first is, so the first alone will be pushed into the SQL query.

It is important to understand that often, the expression itself may be more complex, but what matters is that it can be *reduced* to a simple form just before execution. For example:

- `AND([Column] = 5, USERROLE() = "Admin")` - At runtime, AppSheet knows the user role. If the user is an admin and `[Column] = 5`, this expression evaluates to `TRUE` (which means "fetch all the rows").

- `IN([Column], SELECT(AnotherTable[SomeColumn], [EmailColumn] = USEREMAIL())) - `The entire [`SELECT()`](https://support.google.com/appsheet/answer/10108207) function evaluates to a constant list at runtime before this security filter has to be run. Therefore, the whole expression reduces to `IN([Column], `*`list-of-values`*`)` which can be pushed into the SQL query.

In general, for efficiency, avoid complex [`NOT()`](https://support.google.com/appsheet/answer/10107360) and [`OR()`](https://support.google.com/appsheet/answer/10108121) expressions in the security filter. If there are complex expressions, they should avoid using columns of the table that is being fetched.

## Security filters with AppSheet databases

AppSheet apps using AppSheet databases can significantly improve sync speed using security filters. The following sections describe the security filter formats that are optimized for performance with AppSheet databases:

- [Operators for column filters](#operators-column-filters)
- [Optimized column filters](#optimized-column-filters)
- [Optimized functions](#optimized-functions)
- [Column types that are not optimized](#column-types-not-optimized)
- [Important notes for security filter optimization](#important-notes)

### Operators for column filters

The following operators are supported for the [optimized column filters](#optimized-column-filters):

- Textual types: = (equals) and \<\> (not equals)
- Numeric and temporal types: = (equals), \<\> (not equals), \< (less than), \> (greater than), \<= (less than or equal to), \>= (greater than or equal to)

### Optimized column filters

The following column filters are optimized for performance with AppSheet databases:

- `Text`
- `LongText`
- `Name`
- `Number`
- `Decimal`
- `Date`
- `Datetime`
- `Duration`
- `Email`
- `Percent`
- `Phone`
- `Price`
- `Url`

### Optimized functions

Use the [optimized column filters](#optimized-column-filters) in multi-level expressions with `AND()`, `OR()`, `NOT()`, and `IN()` functions. 

The `IN()` function works with the `LIST()` function. For example: `IN([column_name],LIST(_,_,_))`

The following is an example of a security filter optimized using the functions `OR()`, `NOT()`, and `IN()` with temporal and textual column filters:

`OR([time_column]<>TIME("15:30"),NOT(IN([name_column],LIST("Jane Doe", "Adam"))))`

### Column types that are not optimized

The following column types are not optimized for security filters with AppSheet databases and won't improve sync speed. They will still filter correctly:

- `Address`  and `LatLong`
- `Enum` (such as Color, Progress)
- `Enumlist`
- `Reference`
- `RowId`
- `Time` (partially supported; can use all operators except “=” equality).
- `Yes/No` 

### Important notes for security filter optimization

The following table provides important notes for security filter optimization with AppSheet databases. A security filter in any other format will still evaluate correctly, but will not take advantage of the sync time performance optimization.

|            |                                                                                                                                                                                                              |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Type**   | **Required update**                                                                                                                                                                                          |
| `Duration` | Subtract `"00:00:00"` from a `TIME()` value: `[duration_column]=TIME("00:00:10") - "00:00:00"`                                                                                                               |
| `Number`   | When filtering by a column of `Number` type, don't use quotes around number literals. For example, don't use the filter `IN([number_column],LIST("1","2"))`. Use `IN([number_column],LIST(1,2))`.            |
| `Percent`  | Use a leading zero before the decimal: `[percent_column]=0.10`                                                                                                                                               |
| `Phone`    | Filter as a string with quotes: `[phone_column]="+1231231234"`                                                                                                                                               |
| `Text`     | When filtering by a column of `Text` type, don't use unquoted numbers in place of text literals. For example, don't use the filter `IN([text_column],LIST(10,20))`. Use `IN([text_column],LIST("10","20"))`. |
| `Time`     | Use the `TIME()` function: `[time_column]=TIME("03:30:00")`                                                                                                                                                  |
| `Url`      | In the AppSheet app editor, change the column type to `Text` and filter using quotes: `[url_column]="appsheet.com"`                                                                                          |
