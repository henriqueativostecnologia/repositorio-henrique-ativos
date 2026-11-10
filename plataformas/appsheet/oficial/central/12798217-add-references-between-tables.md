---
fonte: https://support.google.com/appsheet/answer/12798217?hl=en
baixado: 2026-11-10
---

# Add references between tables

Once you have an app with multiple tables, it's often useful to create connections, known as **references**, between tables.

For example, an order capture app might contain the following tables:

1.  `Orders`, with one row per order.
2.  `Customers`, with one row per customer.

Each `Orders` row might reference the `Customers` table to include the customer name and location. In this case, you would add a `Reference` and a `Lookup` column.

Reference and lookup column in a database table

References serve three purposes:

1.  They allow you to represent relationships. For example, the reference between the `Orders` row and the `Customers` row allows you to capture the relationship between an order and the customer who placed that order.
2.  They allow you to easily retrieve information from a related row in another table. For example, you can add a `Lookup` column in the `Orders` table that references the location of the customer from the `Customers` table.
3.  They allow you to navigate from one row to another. For example, you might retrieve a particular `Order` row then navigate to the related `Customers` row.

Each row inside an AppSheet database has a unique Row ID automatically assigned to it. Row IDs act as a key for linking data from one table to another.  This makes it easier to manage data inside the database editor such as linking data across tables using `Reference` columns.   

You can select a different table key inside the app editor, but before doing so it is important to consider if the table is being referenced. If you change the table key, these references will break since the database will continue to use Row ID as the key. This means if the referenced table does not use Row ID as the key, the column type inside the database should not be a `Reference`. To learn more, see [Row ID](https://support.google.com/appsheet/answer/10106672#row-id).

Add references between tables as described in the following sections:

- [Add a Reference column](#add-reference)
- [Add a Lookup column](#add-lookup)
- [Manage table-to-table permissions](#manage-table-to-table-permissions)

## Add a Reference column

To add a reference between tables, [add a column](https://support.google.com/appsheet/answer/12726090) of type `Reference` to a table and select the table to reference from the drop-down list. For example, in the `Orders` table you can add a `Reference` to the `Customers` table.

 

To populate the column rows, double-click in the cell and select the desired row in the list. For example, in the `Orders` table you can associate a customer with each order.

When using `Reference` column data types, you can only reference tables within the same database.

 

The row values in the `Reference` column are populated from the column that is [set as the column label](https://support.google.com/appsheet/answer/12726090#set-column-as-label) in the referenced table.

Populate rows from referenced table

## Add a Lookup column

A `Lookup` column allows you to access content from a table that is referenced by an existing `Reference` column in the same table.

For example, you can add a `Lookup` column to add the **Location** information to the `Orders` table based on the customer selected in the **Customer** column.

The Location row values are populated automatically based on the row values in the Customer column.

`Lookup` column data types are converted to the type of the column that they reference when used in an AppSheet app.

## Manage table-to-table permissions

When you add a reference to a table, read permissions are added to the referenced table to allow access. You can view and manage the permission granted to the referenced tables using the **Table-to-Table permissions** setting when [editing the table settings](https://support.google.com/appsheet/answer/12725680#edit-table-settings).
