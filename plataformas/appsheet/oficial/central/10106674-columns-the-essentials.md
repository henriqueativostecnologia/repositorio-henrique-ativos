---
fonte: https://support.google.com/appsheet/answer/10106674?hl=en
baixado: 2026-11-10
---

# Columns: The Essentials

Once you have tables in the editor, you can categorize each column, and set properties to define their roles and behaviors.

- [About columns](#about-columns)
- [View and edit columns](#view-edit-columns)

## About columns

The following sections introduce you to columns and the :

- [Column structure](#column-structure)
- [Column basics: Name and data type](#name-datatype)
- [Keys](#keys)
- [Column properties: Roles and behaviors](#roles-behaviors)
- [Column order](#column-order)
- [Row labels](#row-label)
- [Virtual columns](#row-label)

### Column structure

As you determine all your tables, you'll review each column's [type](https://support.google.com/appsheet/answer/10106435) and [properties](https://support.google.com/appsheet/answer/10106509) and make changes to them within app the editor, relate different tables to one another, and more. See [View and edit columns](#view-edit-columns).

Edit columns in the app editor

### Column basics: Name and data type

You start defining your column when you give it a name in your spreadsheet and populate it with data of a particular type. The column type determines the role of the column in the app. 

Each column has a name. The editor determines the name of your column based on the top cell in the spreadsheet of each column. The editor deduces the [type of data](https://support.google.com/appsheet/answer/10106435) you have in your column based on the data in it.

For example, if you have a column named `Birthday` and all of your data points use the format `03-20-2000`, AppSheet will assume the column is of type `Date`.

The editor often correctly identifies the data type, but when it doesn't, you can change it using the **Type** drop-down.

This capability is useful for advanced scenarios where the data comes from non-spreadsheet sources. Another case where the column type might be different is that of the [App column type](https://support.google.com/appsheet/answer/10106757), which is used to navigate to different views or apps. However, if you're just getting started, using the default types should work pretty well.

If you edit the column name in the app, to avoid errors in your app:

- When prompted, update all places in the app where the column is used. Otherwise, you will encounter errors in the app where the old column name is used.
- Update any [column name variables](https://support.google.com/appsheet/answer/11539253#column-name) used in template expressions that include the old column name.
- Update the column name in the underlying data source to match the new column name (for example, the column header in the spreadsheet).

**Note**: There should rarely be a reason to change the column name. To change the user-visible name of the column, use the Display name property. See [Configure column properties](https://support.google.com/appsheet/answer/10106509).

### Keys

Keys uniquely identify each row from other rows using a particular column.

The [key](https://support.google.com/appsheet/answer/10106672) may be a single column (such as `Employee ID`) or two or more columns (such as `FirstName` and `LastName`). Each row in the table must have a key value that uniquely identifies it. In other words, no two rows in a table may have identical key values. This is critical, because it allows AppSheet to reliably find the right table row.

When a user changes data in the app, they're making changes to a local copy of the data cached on the device. When the user syncs these changes to the server, AppSheet sends the updated data to the server, finds the updated row using its unique key value, and applies those changes to that row. AppSheet can only find the right row because each row has a unique key value.

There are several ways keys can be determined. They can be natural or computed depending on the case.

### Column properties: Roles and behaviors

Column settings enable you to modify roles and behaviors. Roles determine what a column *is*, behaviors determine what a column *does*. There are several settings you can change for the role and the behavior of a column which enables you to customize your column so it functions exactly as you want. See [Configure column properties](https://support.google.com/appsheet/answer/10106509). 

Column settings showing roles and behaviors

To control other aspects of columns, such as their [order](https://support.google.com/appsheet/answer/10107315), see [UX: The Essentials](https://support.google.com/appsheet/answer/10107307).

### Column order

AppSheet does its best to automatically order columns in order of importance. If you’re using the Tabular or Grouped List views or the Table view, you can manually control column order.

To understand how AppSheet automatically orders columns and to manually control column order, see [Control column order](https://support.google.com/appsheet/answer/10107315).

You can decide which column is the key column. Sometimes, the editor will give you an automatically computed key if there's no obvious unique identifier. You can learn more about keys in [What is a Key?](https://support.google.com/appsheet/answer/10106672)

### Row labels

Row *labels* allow you to choose the most important columns in a table. One image column and one non-image column can be used as labels. All tables have a non-image label. The row labels are used to display [references to rows in other tables](https://support.google.com/appsheet/answer/10106510).

### Virtual columns

A virtual column is a column of a table in the app that doesn't have an actual column in the underlying spreadsheet. Instead, it's automatically computed via an [app formula expression](https://support.google.com/appsheet/answer/10106437).

Sometimes, virtual columns are system-generated and you'll see them show up in your column structure. For example, you can use virtual columns to create Row Labels, allowing you to identify columns that are the most important in a table.

For more information, see:

- [Use virtual columns](https://support.google.com/appsheet/answer/10106758)
- [Improve the presentation of detail and form views using Show types](https://support.google.com/appsheet/answer/12463320)

## View and edit columns

To view and edit the columns in a table:

1.  Open the app in the editor.
2.  Go to **Data**  and select the table you want to view or edit in the list.
    We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

     
    ## If you are using the legacy editor

    Go to **Data \> Columns** and expand the table you want to view or edit.
3.  Edit any of the column properties displayed.
4.  Click **Edit**  to view the full set of properties for a specific column. See [Configure column properties](https://support.google.com/appsheet/answer/10106509) for more information about the properties that you can configure.
5.   Save the app by selecting one of the following:
    - **Save** - Save the app.
    - **Save & verify data** - Save the app and verify that it is runnable based on external dependencies.

You also have the option to [add virtual columns](https://support.google.com/appsheet/answer/10107367) 

If you make changes to the structure of the columns in your spreadsheet, you need to [regenerate](https://support.google.com/appsheet/answer/10106675) the table. This ensures the editor will take in the new data you've added to your spreadsheet without running into errors.

###
