---
fonte: https://support.google.com/appsheet/answer/11544497?hl=en
baixado: 2026-11-10
---

# Sample email templates

The sample templates in this section are all based on the [Order Capture](https://www.appsheet.com/samples/An-app-for-managing-customers-products-and-orders?appGuidString=83be58ea-1901-4a6d-ac9c-38c7c555d8cd) sample app. This sample includes both an email body template and an attachment template. The variables in the templates refer to the column values in the `Order Capture` sample app.

Review the following sample email templates:

- [Template with column name variables](#column-name-variables)
- [Template with expression variables](#expression-variables)
- [Templates with embedded templates](#embedded-templates)
- [Order template in list format](#order-list-format)
- [Order template in table format](#order-table-format)
- [Customer template in list format](#customer-list-format)
- [Customer template in table format](#customer-table-format)

See also [Use templates in a bot](https://support.google.com/appsheet/answer/11539957).

## Template with column name variables

The [template with column name variables](https://docs.google.com/document/d/1HBWqSv4mfI79GZkPhcagXS-froR6FbnEPIYpn2NrdSU/edit?usp=sharing) sample displays the column values from a row in the `Customers` table. The template contains formatted text and column name variables. Each column name variable specifies the name of one column value from the `Customers` row.

The template produces the following output:

## Template with expression variables

The [template with expression variables](https://docs.google.com/document/d/1vrS8gS7X7tg26oIkegyz8YSWx0IBOVTSzZrpUji_H0M/edit?usp=sharing) sample contains both column name variables and expressions. It displays column values from the `Orders` table, column values from its parent `Customers` table, and computed values from its child `Order Details` table.

It displays the `Customer Name` column value using the following expression:

    Customer Name: <<[Customer Name].[Name]>>

`[Customer Name]` is the `Customer Name` reference column value in the `Orders` table. It refers to the parent `Customers` row. `[Customer Name].[Name]` displays the `Name` column value from the parent `Customers` row.

This template computes the total value of all child `Order Details` rows using the following expression:

    SUM(SELECT(Order Details[Total], [Order Id] = [_THISROW].[Order Id]))

The expression computes the sum of all `Order Details` rows having an `Order Id` column value that matches the `Order Id` in the current `Orders` row. That is, it computes the sum of all `Order Details` rows for this `Orders` row.

## Template with embedded templates

You can display a hierarchy of rows using embedded templates. For example, you can display a single `Customers` row. Beneath the `Customers` row, you can display all of its child `Orders` rows. Beneath each `Orders` row, you can display all of its child `Order Details` rows.

Each embedded template starts with `<<Start:StartExpression>>` and ends with `<<End>>`. The [Start expression](https://support.google.com/appsheet/answer/11541779) following the colon yields the list of rows to be formatted using the embedded template. The *`<>`* and *`<>`*elements must match, much like parentheses do within an arithmetic expression.

## Order template in list format

The [Order template in list format](https://docs.google.com/document/d/1iaJ4hjx-ezydd5evCCFDzgvXETWDpzYw1zLumpaudaI/edit?usp=sharing) sample is used when an `Orders` row is updated.

It contains templates that display the following:

- Single parent `Customers` row for the updated `Orders` row displayed in list format.
- Single updated `Orders` row displayed in list format.
- List of child `Order Details` rows for the updated `Orders` row displayed in list format.

## Order template in table format

The [Order template in table format](https://docs.google.com/document/d/1_eVU9RMkuNtG-SrZVd9SI5I5QNlOzj2PFWzUhXSHz68/edit?usp=sharing) sample is used when an `Orders` row is updated. It's like the previous template, but displays the `Order Details` rows in table format. It contains templates that display the following:

- Single parent `Customers` row for the updated `Orders` row displayed in list format.
- Single updated `Orders` row displayed in list format.
- List of child `Order Details` rows for the updated `Orders` row displayed in table format.

The `Order Details` rows are displayed in table format by the following portion of the template. It contains a header row template element, a data row template element, and a trailer row template element. It produces a table containing one header row, one or more data rows, and one trailer row.

 

The first cell in the data row template element contains a `<<Start:StartExpression>>` followed by an expression yielding the first data value to be displayed. The [Start expression](https://support.google.com/appsheet/answer/11541779) following the colon yields the list of child rows to be formatted using the data row template element. In this case, the Start Expression yields the list of child `Order Details` rows for the parent `Orders` row. The data row template element values between *`<>`* and *`<>`* are used to format each child `Order Details` row returned by the start expression.

Because the start expression refers to the `Order Details` table, the variables within the data row template element refer to column values in the `Order Details` table. For example, `<<Quantity>>` refers to the `Quantity` column value of that table. `<<[Product Id].[Product Name]>>` dereferences `Product Id` (a `Ref` column that points into the `Products` table) to retrieve the corresponding `Product Name` value (from the `Product` table).

The last cell in the data row template element contains the name of the last data column value to be displayed. It is followed by `<<End>>`.

A trailer row template element can be used to display summary information. Here we display the total value of all preceding `Order Details` rows. The outer enclosing template isn't shown here, but it displays `Orders` rows. Hence, `<<Order Total>>` refers to the `Order Total` column value in the `Orders` table.

## Customer template in list format

The [customer template in list format](https://docs.google.com/document/d/1tvECAXstS2TKw7qxV_HYYNQHQCn4AT8SRlVLc34DXuo/edit?usp=sharing) sample is used when a `Customers` row is updated.

It contains templates that display the following:

- Single updated `Customers` row displayed in list format.
- All child `Orders` row for the updated `Customers` row displayed in list format.
- All child `Order Details` rows for the parent `Orders` rows displayed in list format.

The part of the template that displays `Orders` rows starts with this expression:

    Start:ORDERBY([Related Orders By Customer Name], [Order Date])

`<<Start:StartExpression>>` signifies the start of an embedded template. The start expression following the colon yields a list of child rows to be formatted using the embedded template. The embedded template is terminated by `<<End>>`. Between` <>` and `<>`, include the formatted text, variables, and expressions to format each `Orders` row.

The start expression above includes an `ORDERBY()` to sort the child `Orders` rows in ascending (oldest-to-newest) order by the `Order Date` column value. If order wasn't important, you could omit `ORDERBY()` and simply specify:

    Start:[Related Orders By Customer Name]

You can limit the number of rows displayed by using a `TOP() `expression with an `ORDERBY()` expression. The first argument to the `TOP()` expression must be an `ORDERBY() `expression. The second argument to the `TOP()` expression specifies the maximum number of rows to be chosen. This second argument can be either a constant or an expression. For example:

    Start:TOP(ORDERBY([Related Orders By Customer Name], [Order Date]), 3)

You can select the child rows to display by specifying a `SELECT()` expression. For example, to display `Orders` having an `Order Status` value of `Open`, specify this `SELECT() `expression:

    SELECT([Related Orders By Customer Name][Order Id], [Order Status] = "Open")

This template produces the following output:

## Customer template in table format

The [customer template in table format](https://docs.google.com/document/d/1mWvDZI-GeLyhgHocbm4DN_AvpKxmJLPIw7fwA-pICDM/edit?usp=sharing) is used when a `Customers` row is updated.

It contains templates that display the following:

- Single updated `Customers` row displayed in list format.
- All child `Orders` row for the updated `Customers` row displayed in list format.
- All child `Order Details` rows for the `Orders` rows displayed in table format.

A Google Docs table is used to display the `Order Details` rows. The table may contain zero or more header rows, one data row, and zero or more trailer rows.

The `Order Details` rows are displayed in table format by the following portion of the template. It contains a header row template element, a data row template element, and a trailer row template element. It produces a table containing one header row, one or more data rows, and one trailer row.

The first cell in the data row template element contains a **`<<Start:`**`StartExpression`**`>>`** followed by an expression yielding the first data value to be displayed. The [Start expression](https://support.google.com/appsheet/answer/11541779) following the colon yields the list of child rows to be formatted using the data row template element. In this case, the start expression yields the list of child `Order Details` rows for the parent `Orders` row. The data row template element values between `<>` and `<>` are used to format each child `Order Details` row returned by the start expression.

Because the start expression refers to the `Order Details` table, the variables within the data row template element refer to column values in the `Order Details` table. For example, `<<Quantity>>` refers to the ***`Quantity`*** column value of that table. `<<[Product Id].[Product Name]>>` dereferences `Product Id` (a `Ref` column in the `Order Details` table that points into the `Products` table) to retrieve the corresponding `Product Name` value (from the `Product` table).

The last cell in the data row template element contains the name of the last data column value to be displayed. It is followed by `<<End>>`.

A trailer row template element can be used to display summary information. Here we display the total value of all preceding `Order Details` rows. The outer enclosing template isn't shown here, but it displays `Orders` rows. Hence, `<<Order Total>>` refers to the `Order Total `column value in the `Orders` table.

This template produces the following output:
