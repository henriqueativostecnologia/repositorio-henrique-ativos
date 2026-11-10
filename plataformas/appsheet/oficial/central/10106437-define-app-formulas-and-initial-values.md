---
fonte: https://support.google.com/appsheet/answer/10106437?hl=en
baixado: 2026-11-10
---

# Define app formulas and initial values

Define app formulas and initial values as described in the following sections:

- [About app formulas and initial values](#about)
- [View and edit app formulas and initial values](#view-edit)

## About app formulas and initial values

Sometimes you might want column values to be computed automatically in the app while the user is interacting with the data in a form. You can make a column computed by configuring it with an *app formula* or an *initial value* expression.

Columns with **app formulas** are useful for values that should always be computed (they appear read-only to app users). When a form is opened (or when a row is modified through some other mechanism), all app formulas in the row are recomputed and their corresponding column values updated. As the user makes changes within the form, app formulas within the row that are affected by those changes will continue to update.

For example, if a record has a `Price` column and a `Tax` column, the `Tax` column might have an app formula `[Price]*0.05` to compute a 5% tax automatically. If the user changes the value of `Price`, the value of `Tax` will automatically update because it depends on `Price`.

Normal columns with app formulas that depend on other rows (for example using [`SELECT()`](https://support.google.com/appsheet/answer/10108207) or [`LOOKUP()`](https://support.google.com/appsheet/answer/10107410)) don't automatically update if the other rows change. For this sort of computed value, it might be better to use a [virtual column](https://support.google.com/appsheet/answer/10106758).  

Columns with **initial values** behave much like columns with app formulas, with two main differences: 

1.  They are not automatically read-only, so users have the option to override the computed value.
2.  They are only computed when adding new rows, not when updating existing rows.

The app formula and initial value can be any valid AppSheet expression that matches the type of the column. For more information about the different kinds of expressions supported by AppSheet, see [Expressions: The Essentials](https://support.google.com/appsheet/answer/10104642).

### App formulas for virtual columns

App formulas are also used to define [virtual columns](https://support.google.com/appsheet/answer/10106758). These columns do not actually exist in the spreadsheet but are only computed within the context of the app itself.

### App formulas versus spreadsheet formulas

App formulas are distinct from [spreadsheet formulas](https://support.google.com/appsheet/answer/10099797). The two mechanisms are complementary and both add value to your app. Your spreadsheet is a very powerful tool to run calculations. Those calculations run only when data syncs back to the spreadsheet.

App formulas are commonly used to calculate the value of a column when the user makes updates to the app. When the changes are synced back to the spreadsheet, the computed value is saved to the corresponding spreadsheet cell.

## View and edit app formulas and initial values

To view and edit an app formula and Initial value:

1.  Open the app in the editor.

2.  Go to **Data**  and select the table you want to view or edit in the list.
    We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

     
    ## If you are using the legacy editor

    Go to **Data \> Columns** and expand the table you want to view or edit.

3.  Edit any of the column properties displayed.

4.  Click **Edit**  to view the full set of properties for a specific column.

5.  Expand the **Auto Compute** section.

6.  Update the **App formula** and **Initial value **fields.

7.  Click **Done**.

8.  Save the app.
