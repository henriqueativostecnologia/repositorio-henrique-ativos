---
fonte: https://support.google.com/appsheet/answer/10106538?hl=en
baixado: 2026-11-10
---

# LINKTOFORM()

Constructed deep link to form

Returns a [deep link](https://support.google.com/appsheet/answer/10106757) (`App` value) to a form to create a new record in an app (the current app, if not specified) with at least one column preset to a value.

To edit an existing record, see [`LINKTOROW()`](https://support.google.com/appsheet/answer/10106539)`.`

## Sample usage

`LINKTOFORM("Order Details_Form", "Order ID", [_THISROW])` creates a deep link to an `Order Details_Form` with the `Order ID` column preset with a [reference](https://support.google.com/appsheet/answer/10106510) back to the current row (making the new `Order Details` row a child of the current row).

`LINKTOFORM("Orders_Form", "Customer ID", [_THISROW], "Delivery Address", [Customer Address])` creates a deep link to an `Orders_Form`, with the `Customer ID` column preset with a [reference](https://support.google.com/appsheet/answer/10106510) back to the current row, and `Delivery Address` preset with a copy of the customer's address.

## Syntax

`LINKTOFORM(`*`view`*`, `*`column`*`, `*`value, `*`[`*`column`*`, `*`value`*`...], [`*`app-name`*`])`

- *`view`* - An expression that returns the name of the target view. The view named must be of type [`form`](https://support.google.com/appsheet/answer/10107846).
- *`column`* - An expression that returns the name of a column of the target table. 
- *value* - An expression that returns a value for the column named by the immediate-preceding *`column`* argument. 
- *`app-name`* - An optional expression that returns the name of the app containing the target form. Defaults to the current app.

  The app name is defined by the `appName` query parameter in the app URL when viewing the app in the editor or accessing the app in your desktop browser. (It is **not** equivalent to the Short Name of the app defined in Settings.) For example, in the following app URL the app name is `ShiftManagement-3518598`:
  `https://www.appsheet.com/template/AppDef?appName=`**`ShiftManagement-3518598`**`&appId=58bb9fcc-b701-462a-87fd-34129fe8fcba&quickStart=False#Data.Columns.Admin%20Scheduled%20Shift`

## Notes

AppSheet does not validate *`view`*, *`column`*, *or* *`app-name`*. If invalid (such as, misspelled or otherwise referring to a non-existent app), no error will be displayed.

Each of *`column`*,  *`value`*, and *`app-name`* may be of any type, are interpreted as `Text` values, and will be encoded (as with [`ENCODEURL()`](https://support.google.com/appsheet/answer/10106629)) for use in the deep link.

## See also

[App column type (deep link)](https://support.google.com/appsheet/answer/10106757)

[`LINKTOAPP()`](https://support.google.com/appsheet/answer/10107914)

[`LINKTOFILTEREDVIEW()`](https://support.google.com/appsheet/answer/10107338)

[`LINKTOPARENTVIEW()`](https://support.google.com/appsheet/answer/11621687)

[`LINKTOROW()`](https://support.google.com/appsheet/answer/10106539)

[`LINKTOVIEW()`](https://support.google.com/appsheet/answer/10108105)
