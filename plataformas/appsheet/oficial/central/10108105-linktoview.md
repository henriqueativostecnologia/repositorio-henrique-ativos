---
fonte: https://support.google.com/appsheet/answer/10108105?hl=en
baixado: 2026-11-10
---

# LINKTOVIEW()

Constructed deep link to view

Returns a [deep link](https://support.google.com/appsheet/answer/10106757) (`App` value) to a view for an app (the current app, if not specified).

## Syntax

`LINKTOVIEW(`*`view, `*`[`*`app-name`*`])`

- *`view`* - An expression that returns the name of the target view.
- *`app-name`* - An optional expression that returns the name of the app containing the target view. Defaults to the current app.

  The app name is defined by the `appName` query parameter in the app URL when viewing the app in the editor or accessing the app in your desktop browser. (It is **not** equivalent to the Short Name of the app defined in Settings.) For example, in the following app URL the app name is `ShiftManagement-3518598`:
  `https://www.appsheet.com/template/AppDef?appName=`**`ShiftManagement-3518598`**`&appId=58bb9fcc-b701-462a-87fd-34129fe8fcba&quickStart=False#Data.Columns.Admin%20Scheduled%20Shift`

  If the app is not deployed, users will be able to access the view until the user access limit (10) for testing purposes has been reached as long as there is no security policy in place to prevent access (for Enterprise plans).

## Notes

AppSheet does not validate *`view`* *or* *`app-name`*. If either of these are invalid (e.g., misspelled, or otherwise refer to something that doesn't exist), no error will be displayed

Both *`view`* and *`app-name`* may be of any type, are interpreted as `Text` values, and will be encoded (as with [`ENCODEURL()`](https://support.google.com/appsheet/answer/10106629)) for use in the deep link.

## See also

[App column type (deep link)](https://support.google.com/appsheet/answer/10106757)

[`LINKTOAPP()`](https://support.google.com/appsheet/answer/10107914)

[`LINKTOFILTEREDVIEW()`](https://support.google.com/appsheet/answer/10107338)

[`LINKTOFORM()`](https://support.google.com/appsheet/answer/10106538)

[`LINKTOPARENTVIEW()`](https://support.google.com/appsheet/answer/11621687)

[`LINKTOROW()`](https://support.google.com/appsheet/answer/10106539)
