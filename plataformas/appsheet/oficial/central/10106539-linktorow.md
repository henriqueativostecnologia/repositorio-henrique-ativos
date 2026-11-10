---
fonte: https://support.google.com/appsheet/answer/10106539?hl=en
baixado: 2026-11-10
---

# LINKTOROW()

Constructed deep link to row

Returns a [deep link](https://support.google.com/appsheet/answer/10106757) to a row with the key column value for a target view in an app (the current app, if not specified).

To create a new record, see [`LINKTOFORM()`](https://support.google.com/appsheet/answer/10106538)`.`

## Syntax

`LINKTOROW(`*`key`*`, `*`view, `*`[`*`app-name`*`])`

- *`key`* - An expression that evaluates to the key column value of the row to which the link should point.
- *`view`* - An expression that evaluates to the name of the target view.
- *`app-name`* - An optional expression that evaluates to the name of the app containing the target view. Defaults to the current app.

  The app name is defined by the `appName` query parameter in the app URL when viewing the app in the editor or accessing the app in your desktop browser. (It is **not** equivalent to the Short Name of the app defined in Settings.) For example, in the following app URL the app name is `ShiftManagement-3518598`:
  `https://www.appsheet.com/template/AppDef?appName=`**`ShiftManagement-3518598`**`&appId=58bb9fcc-b701-462a-87fd-34129fe8fcba&quickStart=False#Data.Columns.Admin%20Scheduled%20Shift`

## **Notes**

AppSheet does not validate *`key`*, *`view`*, *or* *`app-name`*. If invalid (such as, misspelled or otherwise referring to a non-existent row, view, or app), no error will be displayed.

Each of *`key`*, *`view`*, and *`app-name` *may be of any type, are interpreted as `Text` values, and will be encoded (as with [`ENCODEURL()`](https://support.google.com/appsheet/answer/10106629)) for use in the deep link.

## See also

[App column type (deep link)](https://support.google.com/appsheet/answer/10106757)

[`LINKTOAPP()`](https://support.google.com/appsheet/answer/10107914)

[`LINKTOFILTEREDVIEW()`](https://support.google.com/appsheet/answer/10107338)

[`LINKTOFORM()`](https://support.google.com/appsheet/answer/10106538)

[`LINKTOPARENTVIEW()`](https://support.google.com/appsheet/answer/11621687)

[`LINKTOVIEW()`](https://support.google.com/appsheet/answer/10108105)
