---
fonte: https://support.google.com/appsheet/answer/10107914?hl=en
baixado: 2026-11-10
---

# LINKTOAPP()

Constructed deep link to app

Returns a [deep link](https://support.google.com/appsheet/answer/10106757) (`App` value) to an app.

## Syntax

`LINKTOAPP(`*`app-name`*`)`

- *`app-name`* - An expression that returns the name of the target app. 

  The app name is defined by the `appName` query parameter in the app URL when viewing the app in the editor or accessing the app in your desktop browser. (It is **not** equivalent to the Short Name of the app defined in Settings.) For example, in the following app URL the app name is `ShiftManagement-3518598`:
  `https://www.appsheet.com/template/AppDef?appName=`**`ShiftManagement-3518598`**`&appId=58bb9fcc-b701-462a-87fd-34129fe8fcba&quickStart=False#Data.Columns.Admin%20Scheduled%20Shift`

## Notes

AppSheet does not validate *`app-name`*. If invalid (such as, misspelled or otherwise referring to a non-existent app), no error will be displayed.

*`app-name`* can be of any type, interpreted as `Text`, and will be encoded (as with [`ENCODEURL()`](https://support.google.com/appsheet/answer/10106629)) for use in the deep link.

## See also

[App column type (deep link)](https://support.google.com/appsheet/answer/10106757)

[`LINKTOFILTERDVIEW()`](https://support.google.com/appsheet/answer/10107338)

[`LINKTOFORM()`](https://support.google.com/appsheet/answer/10106538)

[`LINKTOPARENTVIEW()`](https://support.google.com/appsheet/answer/11621687)

[`LINKTOROW()`](https://support.google.com/appsheet/answer/10106539)

[`LINKTOVIEW()`](https://support.google.com/appsheet/answer/10108105)
