---
fonte: https://support.google.com/appsheet/answer/10106376?hl=en
baixado: 2026-11-10
---

# Add row labels

Row labels allow you to choose the most important columns in a table. Row labels determine which columns are prominently displayed for that table, similar to a title. One image column and one non-image column can be used as labels. All tables have a non-image label.

You designate the row label in the **Data \> Columns** pane by enabling the **Label?** setting for the particular column.

You can create a row label containing values from two or more columns as follows:

1.  Add a [virtual column](https://support.google.com/appsheet/answer/10106758) to the table.
2.  In the App formula field of the virtual column, enter a [`CONCATENATE()`](https://support.google.com/appsheet/answer/10107400) expression that combines appropriate column values to form the row label. For example: `CONCATENATE([First label column], ", ", [Second label column])`
3.  Disable the **Label?** property for any existing row label column.
4.  Enable the **Label?** property of the virtual column.
5.  Save your changes.

Row Labels are used throughout the app. Different views use them differently:

- **Deck view: **
  - Image label is used for the image on the left
  - Non-image label is used as the top text.
- **Table view: **
  - Non-image label is the first column shown. (Unless you have a custom [column order](https://support.google.com/appsheet/answer/10107315).)
- **Gallery view:**
  - Image label is used for the image
  - Non-image label is used as text below the image
- **Detail view**: 
  - Image label is shown as a large image on top
  - Non-image label is shown directly below the image.

The Ref popup, which is shown when choosing a `Ref` row from the form also uses the labels.

Ref popup labels
