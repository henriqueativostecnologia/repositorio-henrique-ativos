---
fonte: https://support.google.com/appsheet/answer/10106758?hl=en
baixado: 2026-11-10
---

# Use virtual columns

A *virtual column* is a column that doesn't correspond to an actual column in the underlying spreadsheet. Instead, it is automatically computed using an [app formula expression](https://support.google.com/appsheet/answer/10106437).  Virtual column values are not actually stored anywhere, so they won't show up in your spreadsheet once you create them. They do, however, impact your app, behaving much like an ordinary column.

The value of a virtual column is local to the user's device. The result of a virtual column's app formula calculated for one user is not available to other users, and the result may vary for different users.

Because virtual columns are computed for *each* column and row and the app formula expressions can be complex, there is usually a significant cost in performance if an app has a very high number of virtual columns. **In general, it's best to minimize the number of virtual columns as much as possible**.

Three common use cases for virtual columns are listed in the following table:

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Use case**                                                                  | **Example**                                                                   |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Combine other columns                                                         | If an app captures a `FirstName` and a `LastName`, define a virtual           |
|                                                                               | column `FullName` with the app                                                |
|                                                                               | formula: `CONCATENATE([LastName], ", ", [FirstName])`                         |
|                                                                               |                                                                               |
|                                                                               | See also:                                                                     |
|                                                                               | [`CONCATENATE()`](https://support.google.com/appsheet/answer/10107400)        |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Construct [conditional                                                        | If an app captures contact information, define a virtual column               |
| values](https://support.google.com/appsheet/answer/10107395)                  | `PreferredPhoneNumber` with the app                                           |
|                                                                               | formula: `IF([UseMobilePhone?], [MobilePhoneNumber], [PhoneNumber])`          |
|                                                                               |                                                                               |
|                                                                               | See also: [`IF()`](https://support.google.com/appsheet/answer/10108198)       |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Construct complex [Yes/No                                                     | If an app that captures orders, define a virtual column `Important?` with the |
| values](https://support.google.com/appsheet/answer/10107946)                  | app formula: `OR(([Amount] > 1000.0), ([Quantity] > 100))`                    |
|                                                                               |                                                                               |
|                                                                               | See also: [`OR()`](https://support.google.com/appsheet/answer/10108121)       |
|                                                                               |                                                                               |
|                                                                               | The ability to construct complex `Yes/No` values is important when they are   |
|                                                                               | used in other expressions like [column                                        |
|                                                                               | constraints](https://support.google.com/appsheet/answer/10107948) and [slice  |
|                                                                               | conditions](https://support.google.com/appsheet/answer/10106308). In short,   |
|                                                                               | any time there is a need for a complex condition in an app, it is often       |
|                                                                               | worthwhile to create a virtual column to represent the complex condition,     |
|                                                                               | then use the virtual column wherever needed.                                  |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

The following sections describe how to use virtual columns:

- [Add a virtual column](#add)
- [Control the order of virtual columns](#order)
- [Remove a virtual column](#remove)
- [Automatic virtual columns](#automatic)

 

## Add a virtual column

1.  Open the app in the editor.
2.  Go to **Data**  and select the table to which you want to add a virtual column.
3.  Click **+** in the table header.
    The new column is added and the configuration dialog is displayed.
4.  Configure the virtual column.
    You must specify an [app formula expression](https://support.google.com/appsheet/answer/10106437). Typically, the app formula uses values of other columns in the same row. The virtual column's [type](https://support.google.com/appsheet/answer/10108121) will be automatically detected by the app editor.
5.  Click **Done**.
6.   Save the app by selecting one of the following:
    - **Save** - Save the app.
    - **Save & verify data** - Save the app and verify that it is runnable based on external dependencies.

We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

## If you are using the legacy editor

1.  Open the app in the editor.
2.  Go to **Data \> Columns**,
3.  Expand the table to which you want to add a virtual column.
4.  Click **Add Virtual Column**.
5.  Configure the virtual column.
    You must specify an [app formula expression](https://support.google.com/appsheet/answer/10106437). Typically, the app formula uses values of other columns in the same row. The virtual column's [type](https://support.google.com/appsheet/answer/10108121) will be automatically detected by the app editor.
6.  Click **Done**.
7.   Save the app by selecting one of the following:
    - **Save** - Save the app.
    - **Save & verify data** - Save the app and verify that it is runnable based on external dependencies.

## Control the order of virtual columns

Virtual columns occur in the table's column order ***after*** all non-virtual columns, in the order they were created. In the app editor, the color of the edit icon preceding a virtual column is different than that for a non-virtual column:

Virtual columns displayed at the bottom with a different color edit icon

Control the order of virtual columns, as follows:

- To control the order of virtual columns globally, create a [slice with the desired column ordering](https://support.google.com/appsheet/answer/10106593).
- In detail, form, or table views, you have the option to set the column order, as described in [Control column order in a view](https://support.google.com/appsheet/answer/10107315). For example, in a table view the column order is controlled by the **Column order** option:

  Display columns in a different order

## Remove a virtual column

To remove a virtual column, go to the column's configuration screen and click the **Delete** button

Note that the app editor will ***not*** prevent you from deleting a virtual column in use elsewhere in your app. After saving the change, the app editor may display errors noting references to the now-deleted virtual column. These errors will likely render your app unusable until they are corrected.

## Automatic virtual columns

Sometimes, AppSheet will add virtual columns automatically. Typically, these automatic virtual columns are added when a table is first added to the app, or when the table's [structure is regenerated](https://support.google.com/appsheet/answer/10106675). These columns are typically added as a convenience based on common use. You may use, edit, or remove most system-added virtual columns as you see fit.

AppSheet also adds virtual columns to track [reverse references](https://support.google.com/appsheet/answer/10106510). These virtual columns can be recognized by the following properties:

1.  The column name will begin with "Related", like `Related Orders`.
2.  The app formula will use the [`REF_ROWS()`](https://support.google.com/appsheet/answer/10107364) function.
3.  Column type `List` and element type `Ref`.
4.  Description text like "... entries that reference this entry in the ... column".

While the app editor will allow you to delete these columns, they will be recreated automatically the next time the app configuration is saved; there is no way to delete them permanently. Some reconfiguration of these columns is possible, though.
