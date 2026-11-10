---
fonte: https://support.google.com/appsheet/answer/10107396?hl=en
baixado: 2026-11-10
---

# Dereference expressions

Get a column value from the referenced row

A *dereference expression* gets the value of a column from a specific row of another table. A dereference expression makes use of [references between tables](https://support.google.com/appsheet/answer/10106510), using the value of a column of type `Ref` in this table to find a specific row in another table and get a value from one of its columns.

The following sections describe dereference expressions in more detail:

- [Get started](#get-started)
- [Dereference a column value](#dereference-column)
- [Dereference a list](#dereference-a-list)
- [Chained dereference expressions](#chained-dereference-expressions)

**New to expressions?** See also [Expressions: The Essentials](https://support.google.com/appsheet/answer/10104642).

## Get started

- [Watch a video](#video)
- [Explore a sample app](#sample-app)

### Watch a video

Watch this video to learn how to join data from multiple tables using dereference expressions and the [`LOOKUP()`](https://support.google.com/appsheet/answer/10107410) function.

**Note**: The concepts in this video are still valid, though the AppSheet app editor UI has changed since it was recorded.

 

Video: https://www.youtube.com/watch?v=CpWU6QwH1oE

### Explore a sample app

The [Order Deliveries](https://www.appsheet.com/templates/Track-order-delivery-status-and-send-customers-updates) sample app includes a typical dereference expression.

In the `Orders` table, the `Customer ID` column is a reference to the `Customers` table. The `Orders` table uses the dereference expression, `[Customer ID].[Email]`, to retrieve the customer email from the `Customers` table based on the customer ID.

Dereference expression \[Customer ID\].Email

This dereference expression does the following:

1.  In the `Customers` source table, find the row with a [key column value](https://support.google.com/appsheet/answer/10106672) that matches the `Customer ID` column of this row.
2.  From that row in the source table, get the value of the `Email` column. 

These steps are repeated to get the value of the `Phone` and `Address` columns.

## Dereference a column value

A dereference expression is of the form:

    [ref-column].[value-column]

Where `ref-column` is the name of the column of type `Ref` in the this table, and `value-column` is the name of a column of the other table.

The configuration of a column of type `Ref` identifies the table in which referenced rows are to be found:

Customer ID is a reference to Customers table

The value of a `Ref` column should be the [key column value](https://support.google.com/appsheet/answer/10106672) of a row in the `Ref` column's source table.

## Dereference a list

A column value of type `List` or `EnumList` with a base type of `Ref` can be dereferenced to produce a new list of the values from dereferencing each individual reference, an operation called a *list dereference*.

A list dereference is performed by enclosing the `Ref` list column name (such as, `Related Orders`) and the column name of the desired column value (such as, `Order Date`) each in square brackets (`[`, `]`) and placing them adjacent to each other: `[Related Orders][Order Date]`

The result will be a list of `Order Date` column values from the rows identified by the list in the `Related Orders` column value.

See also [Build list dereferences](https://support.google.com/appsheet/answer/11618586).

## Chained dereference expressions

You can dereference a dereference.

For example, you might have a three-level hierarchy consisting of a `Customer` row, a child `Order` row, and a grandchild `Order Detail` row. The `Order Detail` row contains a reference to the `Order` row. The `Order` row contains a reference to the `Customer` row.

From the `Order Detail` row, you can directly access the value of a column in the `Customer` row by chaining dereference expressions. That is, you can dereference from the `Order Detail` row to the `Order` row, and then dereference from the `Order` row to the `Customer` row in a single expression.

    [Order Id].[Customer Name].[Email]
