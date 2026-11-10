---
fonte: https://support.google.com/appsheet/answer/11541779?hl=en
baixado: 2026-11-10
---

# Use Start expressions in templates

Use `Start` expressions as described in the following sections:

- [Display a list of records using Start expressions in templates](#display-a%20list-of-records)
- [Access columns in parent and grandparent records](#access-columns-in-parent-grandparent-records)
- [Common Start expressions](#common)
- [Control the record order](#control-record-order)
- [Control the number of records displayed](#control-number-records)
- [Troubleshoot Start and End expressions](#troubleshoot)

See also:

- [Examples of using Start expressions in templates](https://support.google.com/appsheet/answer/16279304)
- [Example of using \[\_THISROW-n\] in templates](https://support.google.com/appsheet/answer/16302828)

When used in an HTML template, `Start` expressions must appear within a `<p>` or heading element.

## Display a list of records using Start expressions in templates

`Start` expressions are used in templates to display a list of records. The `Start` expression appearing at the beginning of the template controls which records are displayed. Then, the template is used to format each record.

Each template starts with **`<<Start:`*`StartExpression`*`>>`** and ends with **`<<End>>`**. The `Start` expression following the colon yields a list of records to be formatted using the template. To be more specific, the `Start` expression yields the list of *key values* of the table rows to be formatted using the template.

A template may contain one or more embedded templates. You can display a hierarchy of records by embedding one template within another. For example, you can display `Customers`, `Orders`, and `Order Details` records in a three-level hierarchy by:

1.  Creating a template for `Customers`.
2.  Creating an embedded template for `Orders` within the `Customers` template.
3.  Creating an embedded template for `Order Details` within the `Orders` template.

An Embedded template with a `Start` expression is used in the following use cases.

- **Embedded expression in a data change bot**
  A data change bot is fired when a specific record in a table is modified. For example, a data change bot associated with the `Orders` table is triggered when an `Order` is changed. The template is evaluated in the context of the changed record. Your template can display both the specifics of the `Orders` record and the `Order Details` records associated with that `Orders` record. Your template must include an embedded template with a `Start` expression to display the `Order Details` records.
- **Top-level expression in a scheduled bot**
  In a scheduled bot, you can display a set of records. For example, you can display all `Orders` or all *open* `Orders`. Your template must include an embedded template with a `Start` expression to display the `Orders` records.
- **Embedded expression in a scheduled bot**
  In a scheduled bot, you can display a hierarchy of records. For example, you can display all *open* `Orders` records along with their related `Order Details` records. Your template must include an embedded template with a `Start` expression to display the `Orders` records. Then create an embedded template for `Order Details` within the `Orders` template.

**Example**

Consider this [template](https://docs.google.com/document/d/1_eVU9RMkuNtG-SrZVd9SI5I5QNlOzj2PFWzUhXSHz68/edit?usp=sharing) which is used in a data change bot when an `Orders` record is updated. It contains an embedded template to display all of the `Order Details` records for the updated `Orders` record.

The embedded template contains the following `Start` expression:
`<<Start:[Related Order Details]>>`

It is important to remember that the `Start` expression is evaluated in the context of the template that contains it. In this case, the outer template is used to format the `Orders` record, so the `Start` expression is evaluated in the context of that `Orders` record. Therefore, the `Start` expression can make use of the columns in the current `Orders` record.

By contrast, the expressions between `<<Start>>` and `<<End>>`, other than the `Start` expression, are evaluated in the context of each *child record*. In our example, since the `Start` expression refers to the `Order Details` records, the expressions between `<<Start>>` and `<<End>>` are evaluated in the context of a child `Order Details` record. The expressions between `<<Start>>` and `<<End>>` normally refer to the columns of the `Order Details` record.

The embedded template is evaluated once for each child record returned by the `Start` expression. For example, if there are five child **Order Details** records, the embedded template is evaluated five times.

## Access columns in parent and grandparent records

Within an embedded template, you can refer to the columns of tables of your outer-level templates. For example, you might have a three-level hierarchy of templates consisting of a Customer record, an embedded child Order record, and a further embedded grandchild Order Detail record.

### Access a column in a parent record

In the embedded Order Detail template, you refer to columns of the *parent* `Order` record by specifying a dereference expression of the form:
`[_THISROW-1].[ParentRecordColumnName]`

For example, **`[_THISROW-1].[Order Date]`** retrieves the value of the `Order Date` column of the parent `Order` record

**Note**: There cannot be any embedded white spaces in the `[_THISROW-`*`n`*`] `string. The value *n* is a constant number value; it cannot be an expression.

### Access a column in a grandparent record

In the embedded `Order Detail` template, you refer to columns of the *grandparent* `Customer` record by specifying a dereference expression of the form:
`[_THISROW-2].[GrandparentRecordColumnName]`

For example, **`[_THISROW-2].[Phone]`** retrieves the value of the `Phone` column of the grandparent `Customer` record.

`[_THISROW]` =\> Top level
`[_THISROW-1] `=\> One level up to the parent
`[_THISROW-2]` =\> Two levels up to the grandparent
`[_THISROW-3]` =\> Three levels up to the great grandparent
`[_THISROW-`*`n`*`]` =\> *n* levels up

## Common Start expressions

A `Start` expression may take several forms. The following provide some common examples.

### An entire table

The simplest `Start` expression is the name of a table and its key column:

    <<Start:Orders[Order Id]>>

This form of `Start` expressions is typically only meaningful as the top-level `Start` expression in a scheduled bot.

### Reverse reference

A common `Start` expression is the name of a reverse reference virtual column. For example:
`<<Start:[Related Order Details]>>`

The `Orders` record contains the reverse reference virtual column `Related Order Details`. This virtual column was automatically added by AppSheet to contain the reverse references from the `Orders` table to the child `Order Details` table. It contains the list of key values of the related child `Order Details` records. In the example above, the column name `Related Order Details` must be enclosed in square brackets.

### Reverse reference with a condition

Another common `Start` expression is the name of a reverse reference virtual column that selects a subset of the referenced records. You can achieve this by enclosing the reverse reference in a `SELECT` expression. For example:
`<<Start:SELECT([Related Order Details][OrderDetail Id], [Order Status] = "Open")>>`

The `Orders` record contains the reverse reference virtual column `Related Order` `Details`. In the example above, the column name `Related Order Details` must be enclosed in square brackets.

This virtual column was automatically added by AppSheet to contain the reverse references from the `Orders` table to the child `Order Details` table. It contains the list of key values of the related child `Order Details` records. AppSheet originally named this column `Related Order Details [Order Id]`. In the example, we needed to rename the column to `Related Order Details` to use it in the `SELECT` expression because the square brackets around `[Order Id]` in the original AppSheet generated name prevent the expression from working.

A `SELECT` expression in a `Start` expression must always return a list of key values, so the first argument of the `SELECT` expression is `[Related Order Details][OrderDetail Id]`. The value `[Related Order Details] `is the name of the reverse reference column. The value `[OrderDetail Id`**`]`** is the name of the key column of the `Order Details` table. Taken together, the first argument returns the keys of all referenced `Order Details` records.

The second argument of the `SELECT` expression includes only those referenced `Order Details` records where the `Order Status` is `Open`.

### SELECT expression

You can display a subset of the child records by specifying a `SELECT` expression that yields the key values of the child records you wish to display.
`<<Start: SELECT(Orders[Order Id], AND(IN([Order Id],[_THISROW].[Related Orders]), [Order Status] = "Open"))>>`

The `SELECT` expression must yield a list of key values. In this example, the `Order Id` column is the key of the `Orders` table.

## Control  the record order

You can use `OrderBy` to control the order in which records are displayed.

The parameters to the `OrderBy()` function are `OrderBy(`*`keys`*`, `*`sort-key`*`, `*`descending-order?`*`)`.

You can display the `Order Details` records in order from most expensive to least expensive using the following `Start` expression. The `Total` column contains the total value of each `Order Details` record:
`<<Start:OrderBy([Related Order Details], [Total], FALSE)>>`

You can display "Open" `Orders` records by `Order Date` using the following `Start` expression:
`<<Start:OrderBy(SELECT(Orders[Order Id], [Order Status]="Open"),[Order Date],FALSE)>>`

You can display "Open" `Orders` records by inverse `Order Date` using the following `Start` expression:
`<<Start:OrderBy(SELECT(Orders[Order Id], [Order Status]="Open"),[Order Date],TRUE)>>`

## Control the number of records displayed

You can limit the maximum number of records displayed by using the `Top` function.

The parameters of the `Top` function are `Top(OrderedListOfRecords, MaxNumberOfRecords)`.

**Note**: `Top` only works with `OrderBy` and cannot be used in isolation.

Display at most 3 records as follows:
`<<Start:Top(OrderBy([Related Orders], [Order Date]), 3)>>`

Display the most recent "Open" `Orders` record using this `Start` expression:`<<Start:Top(OrderBy(SELECT(Orders[Order Id], [Order Status]="Open"),[Order Date],TRUE),1)>>`

Display the oldest "Open" `Orders` record using this `Start` expression:`<<Start:Top(OrderBy(SELECT(Orders[Order Id], [Order Status]="Open"),[Order Date],FALSE),1)>>`

## Troubleshoot Start and End expressions

The following list common error messages and how to address them.

### Incomplete Start expression

If your `Start` expression contains an error and the displayed **error message only contains part of your `Start` expression**, ensure that your `Start` expression does not contain an embedded carriage return. Embedded carriage returns confuse the expression parser. This is especially common when the `Start` expression is contained in a table cell. In this case it is easy to inadvertently enter a carriage return within the `Start` expression.

### Found 1 unmatched 'End'

The error message `Found 1 unmatched 'End'` indicates that the expression parser found an `End` expression but could not find its matching `Start` expression.

Ensure that your `Start` expression does not contain an embedded carriage return. Embedded carriage returns confuse the expression parser. This is especially common when the `Start` Expression is contained in a table cell. In this case it is easy to inadvertently enter a carriage return somewhere within the `Start` expression. For example, you may find a carriage return in the middle of the `Start` expression, between `<<` and `Start`, following `Start:`, or before the closing `>>`.

### Found 1 unmatched 'Start'

The error message `Found 1 unmatched 'Start'` indicates that the expression parser found a `Start` expression but could not find its matching End expression.

Ensure that your `End` expression does not contain an embedded carriage return. Embedded carriage returns will confuse the expression parser. This is especially common when the `End` expression is contained in a table cell. In this case it is easy to inadvertently enter a carriage return within the `End` expression. For example, you may find a carriage return between `<<` and `End` or between `End` and `>>`.

### Found n '\<\<' values but m '\>\>' values

Ensure that all of your `Start` and `End` expressions begin with `<<` and end with `>>`.
