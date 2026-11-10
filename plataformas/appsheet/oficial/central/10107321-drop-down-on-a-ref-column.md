---
fonte: https://support.google.com/appsheet/answer/10107321?hl=en
baixado: 2026-11-10
---

# Drop-down on a Ref column

You can limit which values appear when updating a [**Ref**](https://support.google.com/appsheet/answer/10106510) column by specifying a [Valid_If](https://support.google.com/appsheet/answer/10107665) expression on the [column](https://support.google.com/appsheet/answer/10106674). For example, in an order capture application you might limit the allowed values to open orders or to orders totaling over \$1000.

Your expression must yield a [list of values](https://support.google.com/appsheet/answer/10107669) from the [key column](https://help.appsheet.com/data/keys/what-is-a-key) of the referenced table. For example, if the referenced table is `Orders` and that table's key column is `OrderId`, then the expression must yield values that can be found in the `OrderId` column. For example: 

`SELECT(Orders[`**`OrderId`**`], OR([Status] = "open", [Total] > 1000))`

A common mistake is to use an expression like: 

`SELECT(Orders[`**`Not the key column`**`], ...) `

With the intent of showing a different column than the key. The drop-down will still function and show the intended column, but selected values will not match the referenced key column and will result in broken references (indicated by an **!** icon). Instead, you should use [row labels](https://support.google.com/appsheet/answer/10106376) to control which columns are shown.
