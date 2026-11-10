---
fonte: https://support.google.com/appsheet/answer/10107964?hl=en
baixado: 2026-11-10
---

# ISNOTBLANK()

Is value present?

Returns a `Yes/No` expression, as follows:

- `TRUE` if the specified item has a value.

- `FALSE` if the specified item has no value. (An empty list has no value.)

## Sample usage

`ISNOTBLANK("")` returns `FALSE`. Equivalent to `NOT(ISBLANK(""))`. See also: [`ISBLANK()`](https://support.google.com/appsheet/answer/10107337), [`NOT()`](https://support.google.com/appsheet/answer/10107360)

`NOT(ISNOTBLANK(""))` returns `TRUE`. Equivalent to `ISBLANK("")`.

`ISNOTBLANK("Hi!")` returns `TRUE`

`ISNOTBLANK(0)` returns `TRUE`

`ISNOTBLANK(LIST())` returns `FALSE`. See also: [`LIST()`](https://support.google.com/appsheet/answer/10107339)

`ISNOTBLANK(LIST("Red", "Yellow", "Green"))` returns `TRUE`

`ISNOTBLANK([Address])` returns `TRUE` if the `Address` column has a value, `FALSE` otherwise.

`ISNOTBLANK(FILTER("Customers", ([City] = "London")))` returns `TRUE` if any customers are in London. Equivalent to `(COUNT(FILTER("Customers", ([City] = "London"))) <> 0)`. See also: [`COUNT()`](https://support.google.com/appsheet/answer/10107676), [`FILTER()`](https://support.google.com/appsheet/answer/10108196)

## Syntax

`ISNOTBLANK(`*`value`*`)`

- *`value` *- Any singular value of any type, or a list of any type.

## See also

[`ISBLANK()`](https://support.google.com/appsheet/answer/10107337)
