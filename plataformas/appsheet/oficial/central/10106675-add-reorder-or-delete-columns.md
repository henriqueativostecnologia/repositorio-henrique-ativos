---
fonte: https://support.google.com/appsheet/answer/10106675?hl=en
baixado: 2026-11-10
---

# Add, reorder, or delete columns

As you customize your app, you might need to modify the column structure in a table to add, reorder, or delete columns in a table. You'll need to regenerate the table if you modify the connected data directly.

- [How to add, reorder, or delete columns](#summary)
- [Modify the connected data directly](#modify-data)
- [Regenerate the table](#regenerate-structure)
- [Regenerate apps built from Google Forms ](#regenerate-google-forms)

## How to add, reorder, or delete columns

To add, reorder, or delete columns at the **global** level, do one or more of the following:

- [Modify the connected data directly](#modify-data) to add, reorder, or delete columns.
- Show or hide columns by using the [Show?](https://support.google.com/appsheet/answer/10106628) option.
- [Conditionally show or hide a column value (`Show_If`)](https://support.google.com/appsheet/answer/10106628).
- Add a [virtual column](https://support.google.com/appsheet/answer/10106758) to add a column that is automatically computed using an [app formula expression](https://support.google.com/appsheet/answer/10106437), but that doesn't correspond to an actual column in the connected data.
- Add a [slice](https://support.google.com/appsheet/answer/10106592) to reorder or filter specific columns in views. See [Slice columns](https://support.google.com/appsheet/answer/10106593).
- [Improve the presentation of detail and form views by using Show types](https://support.google.com/appsheet/answer/12463320).

To add, reorder, or delete columns for a **specific view**, for a subset of view types you can [control the column order in a view](https://support.google.com/appsheet/answer/10107315).

## Modify the connected data directly

You can modify the connected data directly to add, reorder, or delete columns. For example, if in your original spreadsheet you have three columns and decide to add another column, as shown in the following figure.

Spreadsheet showing the Added Column

After modifying the column structure in your connected data, you need to [regenerate the table](#regenerate-structure) in the app editor. If you don't regenerate the table, you might see an error similar to the following in the app preview:

`Unable to fetch app definition: Error: There is a mismatch in the number of columns between the spreadsheet for Class Descriptions and the table schema. The table has 5 columns but the schema has 4 columns. Please regenerate the table column structure. `

## Regenerate the table

Regenerate a table whenever you add, reorder, or delete columns directly in the connected data. 

The column structure will be regenerated and may impact the behavior of your app. Because all changes to your app will be saved, **this action cannot be undone**.

 

If you are using [Google Forms](https://support.google.com/appsheet/answer/10106596) as a data, review [Regenerating apps built form Google Forms](#regenerate-google-forms) before regenerating your table.

To regenerate the table:

1.  Open the app in the editor.
2.  Go to **Data**  and select the table you want to regenerate.
3.  Click **Regenerate schema**  in the table header.
4.  Click **Regenerate** to confirm the action.
5.  Save the app.

Alternatively, you can go to **Data**, position your cursor over the table that you want to regenerate in the Data panel, and select **More ** Three-dot menu vertical ** \>** **Regenerate schema**.

We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

## If you are using the legacy editor

1.  Open the app in the editor.
2.  Go to **Data \> Columns**. 
3.  Expand the table you want to view or edit.
4.  Click **Regenerate Structure**.
5.  Click **Regenerate** to confirm the action.
6.   Save the app.

 When you sync in the app preview, you'll now be able to see your additional column in whatever view(s) you have set up.

Added Column (from spreadsheet) displayed in the app

See also: [Improve performance when you add, remove, or rearrange columns](https://support.google.com/appsheet/answer/10106591)

## Regenerate apps built from a Google Forms

If the app was built from a [Google Form](https://support.google.com/appsheet/answer/10106596), the original form configuration will be stored in the response sheet in the form of notes attached to the header row. Regenerating will cause the columns to restore the settings contained within the notes, potentially overwriting changes you've made in the editor. To avoid this, remove the notes from the response sheet before regenerating. If you do accidentally regenerate with notes left in the sheet and lose your configuration, remember that you can restore an older version of the app using [version history](https://support.google.com/appsheet/answer/10105387).
