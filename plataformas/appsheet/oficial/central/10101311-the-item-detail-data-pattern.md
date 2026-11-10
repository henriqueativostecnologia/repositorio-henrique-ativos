---
fonte: https://support.google.com/appsheet/answer/10101311?hl=en
baixado: 2026-11-10
---

# The "item-detail" data pattern

A classic data model pattern to capture many Detail records that correspond to a single Item record

**Note**: This article assumes you are familiar with basic [AppSheet design concepts](https://support.google.com/appsheet/answer/10099795) and how the [AppSheet platform works](https://www.appsheet.com/how_to_make_an_app).

*Item-Detail* is one of the most common data design patterns in mobile apps. In fact, almost every meaningful AppSheet app utilizes this pattern in some form. It is a natural consequence of the "entity" approach to modeling data.

## Sample scenarios

**Scenario 1**: An app that captures sales orders. Each order is for one customer and has many line items. Each line item identifies a product and a quantity purchased. For an example of this scenario, see the [Order Capture How-to](https://www.appsheet.com/templates/An-app-for-managing-customers-products-and-orders?appGuidString=83be58ea-1901-4a6d-ac9c-38c7c555d8cd) template.

**Scenario 2**: A factory has several pieces of equipment and each has to be inspected several times over the course of the year. For an example, see the [Facility Inspections](https://www.appsheet.com/templates/Inspect-points-throughout-various-properties?appGuidString=d8389191-0217-42c0-bd50-406993b660f6) template.
 
**Scenario 3**: A school class assigns group projects for the students. Each student needs to add information about the project they worked on.

**Scenario 4**: A number of papers are submitted to a conference and the reviewers add their reviews to each paper.

In all of these scenarios, there are two entities involved in a nested relationship. Let us use the first scenario to explain. The entities are `Orders` and `LineItems`. The standard way to model the data is to have two tables:

1.  The `Order` table has an `Id`, `Customer Name`, and `Date`

2.  The `LineItem` table has an `Id`, `OrderId` (`Ref` to the `Order` table), `Product ID` (`Ref` to the `Product` table), `Quantity`, and `Cost`.

In order to add a new order, the user follows this sequence of steps: 

1.  Create an `Order` with the customer information.
2.  Add one or more `LineItems` to the order just created.

## Common variations

Here are some common variations that augment the basic Item-Detail pattern.

1.  Dereferenced values: each `LineItem` may need to include some information from the `Order`. For example, the `Order` may have a virtual `SalesTax` column and the `LineItem` may use this in a `SubTotal` column. This column would have an AppFormula: `[Cost] * [Quantity] * [OrderId].[SalesTax]`

    See  [Dereference expressions](https://support.google.com/appsheet/answer/10107396).

2.  Aggregate computation: the `Order` may have a virtual column that sums up the total value of the order across all the `LineItems`. This would be a virtual column `Total` with AppFormula: `SUM(SELECT(LineItem[SubTotal], [OrderId] = [_THISROW].[Id]))` 

    See [Use virtual columns](https://support.google.com/appsheet/answer/10106758).
