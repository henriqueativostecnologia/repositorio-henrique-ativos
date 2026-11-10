---
fonte: https://support.google.com/appsheet/answer/10106510?hl=en
baixado: 2026-11-10
---

# References between tables

AppSheet references allow your apps to support relational data.

- [What is a reference?](#what-is-reference)
- [Get started with references](#get-started)
- [Create references](#create-reference)
- [Reverse references](#reverse-references)
- [References and reverse references contain key values](#key-values)
- [Express ownership between tables](#express-ownership)

## What is a reference?

Once you have an app with multiple tables, it's often useful to create connections, known as **references**, between the app's tables.

For example, an order capture app might contain the following **tables**:

1.  `Orders`, with one row per order.
2.  `Order Details`, with one row per line item.
3.  `Products`, with one row per product being sold.
4.  `Customers`, with one row per customer.

The order capture app might contain the following **references**:

1.  Each `Orders` row will reference the `Customers` row of the customer who placed that order.
2.  Each `Order Details` row will reference its parent `Orders` row.
3.  Each `Order Details` row will reference its corresponding `Products` row.

References serve three purposes:

1.  They allow you to represent relationships. For example, the reference between the `Orders` row and the `Customers` row allows you to capture the relationship between an order and the customer who placed that order.
2.  They allow you to easily retrieve information from a related row in another table. For example, the reference between the `Order Details` row and the `Products` table allows you to start from an individual `Order Details` row and retrieve the name, image, and price column values from the related `Products` row.
3.  They allow you to navigate from one row to another. For example, you might retrieve a particular `Order Detail` row then navigate to the related `Orders` rows, and then to the related `Customers` rows.

After you define a reference, to get a column value from a referenced table use [dereference expressions](https://support.google.com/appsheet/answer/10107396).

## Get started with references

Get started with references by watching a [video](#video) or using a [sample app](#sample-app), as described below.

### Video

Watch the following video to learn how to create references between tables with AppSheet.

Video: https://www.youtube.com/watch?v=tFFFKHlI-q0

### Sample app

Get started using references between tables in an app by using the [Order capture how-to](https://www.appsheet.com/template/showdef?appId=OrderCaptureHow-to-71626) feature sample. 

##  Create references

A reference can be added to a table in two ways.

- AppSheet automatically adds references when you generate or regenerate a table (system-added)
- You can manually add references (user-added)

### System-added references

When you initially create your app or when you regenerate a table's column structure, AppSheet will try to automatically infer references between tables. For example, if you have a `Customers` table with a `Name` column as its key, and if the `Orders` table has a column called `Customer Name`, the `Customer Name` column is assumed to be a `Ref` column.

### User-added references

You create a reference by adding a column of type `Ref` to a table and specifying the related table's name. For example, in the `Orders` table you would add a `Ref` to the `Customers` table. In the `Order Details` table you would add one `Ref` to the `Orders` table and another to the `Products` table.

You can add a reference as follows:

1.  Ensure your worksheet has a column to contain the reference.
2.  Open the app in the editor.
3.  Go to **Data**  and select the table you want to edit in the list.
    We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

     
    ## If you are using the legacy editor

    Go to **Data \> Columns** and expand the table you want to edit.
4.  If you needed to add a new worksheet column to contain the reference in step 1, [regenerate the table schema](https://support.google.com/appsheet/answer/10106675#regenerate-structure). This will include the newly added worksheet column in the table.
5.  In the **Type** drop-down, select **Ref**.
6.  In the **Source table** drop-down, select the referenced table.
7.  Click **Done**.
8.   Save the app.

## Reverse references

For each `Ref` you add, the system automatically adds a *reverse reference* in the opposite direction. This is true for both user-added and system-added references. The reverse reference virtual column is given a default name that you can change.

For example, when you add the `Ref` from the `Orders` table to the `Customers` table, the system automatically adds a reverse reference from the `Customers` table to the `Orders` table.

Reverse references serve three purposes:

1.  They allow you to navigate from one row to all of its related rows.
2.  They allow the user interface to easily display a row along with all of its related rows in another table.
3.  They allow aggregates to be computed like the count of a customer's orders or the total dollar value of a customer's orders.

The reverse reference virtual column is assigned an app formula that uses the special function [`REF_ROWS()`](https://support.google.com/appsheet/answer/10107364). Behind the scenes, `REF_ROWS()` performs a complex [`SELECT()`](https://support.google.com/appsheet/answer/10108207) operation.

For both references and reverse references, [reference icons are displayed](https://support.google.com/appsheet/answer/10106759).

## References and reverse references contain key values

A `Ref` column always stores the key column value of the referenced row. For example, if the key column value of a `Customers` row is `Ann Adams` then the `Ref` field in the related `Orders` row will contain the value `Ann Adams`. A table's key column value uniquely identifies each row in that table. The copy of the key column value in the `Ref` column allows the system to unambiguously retrieve the proper row in the referenced table. See [What is a key?](https://support.google.com/appsheet/answer/10106672)

The system-added reverse reference column is a list of the key column values of the related rows. For example, the reverse reference in `Customers` record `Ann Adams` would contain `1003`, `1005`, and `1010` if those were the key column values of Ann's related `Orders` records. When viewing an individual row, related reverse references appear as inline views that can be [customized](https://support.google.com/appsheet/answer/10106759).

## Express ownership between tables

References can indicate not only that two tables are related, but that rows of one table should be owned by (or considered a part of) rows from another table. This is done by activating the **IsAPartOf** option in the `Ref` column structure. Typically, this should only be done in cases where rows containing the `Ref` column only make sense when associated with a row from the referenced table. For example, you may have a separate `Order Details` table for line items that reference an `Order`, but conceptually each entry should be considered *part of* an `Order` and shouldn't exist independently (put another way, the `Order` record owns the `Order Details` that reference it).

There are several implications of enabling this ownership relationship:

1.  Form views should allow users to add or update related rows that are a part of that row without leaving the form.
2.  A form comprised of multiple rows should be treated as a single update.
3.  If a row is deleted, any related rows that are a part of it should also be deleted (and again treated as a single update).

The first of these to take effect will be \#1: System-generated reverse reference columns related to `Ref` columns marked `IsAPartOf` will appear in form views and allow users to view, add, and edit line items within the form view. The availability of these options is limited by the table or slice permissions (and until the final form is saved, pending adds can still be modified even if the table doesn't allow updates).

There are some limitations of which to be aware:

- A table can only have one `Ref` column marked `IsAPartOf` (a row can only be a part of one other row).
- Actions are not supported within forms. Inline views based on reverse references in forms will not display actions or trigger actions based on [view events](https://support.google.com/appsheet/answer/10108214).
- Canceling a form with pending line item adds/edits also cancels those adds/edits.
