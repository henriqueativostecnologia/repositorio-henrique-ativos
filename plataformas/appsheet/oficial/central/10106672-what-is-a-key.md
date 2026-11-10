---
fonte: https://support.google.com/appsheet/answer/10106672?hl=en
baixado: 2026-11-10
---

# What is a key?

A key uniquely identifies each row in a table.

When you add a row to a table, that row must have a unique key value. The row's key value must remain constant for the life of the row.

When you update or delete a row through an AppSheet app, the key is used to find the row to update or delete.

If two or more rows are inadvertently assigned the same key value, we say the table contains "duplicate keys". This is a serious problem. If someone attempts to update or delete one of these rows, the wrong row may be updated or deleted.

Edit columns in the app editor

Above, we can see that the email address is selected as the key of the table. In this case, the key is the email address because the name uniquely identifies each user. Therefore, there is no risk of duplicate keys and the resulting issues.

The following sections provide more information about keys:

- [Types of keys](#types)
- [Select a key](#select)
- [Column types that can't be used as the key](#unsupported-column-types)

## Types of keys

AppSheet supports three types of keys. From best to worst, these key types are:

- [Natural keys](#natural-keys)
- [System-generated keys](#system-generated-key)
- [Row number keys](#row-number-key) (not recommended)

### Natural keys

Many tables have a Natural key, a single field or a combination of fields that uniquely identify each table row.

#### Natural single-column keys

Your table may often have a single field containing a value that uniquely identifies each row. For example, an `Employee` table may contain an `EmployeeID` field that contains a unique employee ID. When such a field is present, it makes an ideal key.

#### Natural multi-column keys

Your table may contain two or more fields that together contain values uniquely identifying each row. For example, a `Vehicle` table may contain a `State` field and a `LicensePlateNumber` field that together uniquely identify each row. A multi-column key is slightly more unwieldy than a single column key, but it makes an excellent key.

#### Natural computed keys

Your table may contain fields that can be combined to yield a unique computed key value. The row's computed key value must remain constant for the life of the row.

You specify the key computation expression in the key field's [app formula property](https://support.google.com/appsheet/answer/10106437).

The editor examines this expression to ensure that it yields the same result over time, and displays an error if it does not. For example, an app formula that includes the current date or time might yield different results over time, so it would be prohibited in a key field's app formula.

#### Why not worksheet formulas?

In a spreadsheet, it's sometimes convenient to have an ID column that is computed with a worksheet formula. For example, the worksheet formula might increment the value in the previous row. This does not work for AppSheet table keys for two reasons. First, keys must be unique and unchanging over time, but that is not possible to guarantee with worksheet formulas. Second, it must be possible to compute the formula when the app is working offline, but that is not possible with worksheet formulas.

### System-generated keys

Some tables do not have a natural key. Instead, you would like the system to generate a unique key for each new row.

#### Row ID key

In [AppSheet databases](https://support.google.com/appsheet/answer/12631542), the default key is the Row ID which is automatically generated for each row and stored in the “Row ID” column. This key allows users to create and manage references in the database editor, as described in [*Add references between tables*](https://support.google.com/appsheet/answer/12798217). 

The Row ID column is hidden by default in the database editor. If you want to show the Row ID in the database editor, [add](https://support.google.com/appsheet/answer/12726090#add-column) the Row ID column to the table.

In the app editor, you can select a different table key, but before doing so it is important to consider if the database table is being referenced. These references will break since the database will continue to use Row ID as the key. 

To ensure features such as references, formulas, or the CSV import action work properly, copy existing references to a new column. One way to do this is as follows:   

1.  In the AppSheet database editor, locate the [`Reference` column](https://support.google.com/appsheet/answer/12798217#add-reference) in the referencing table. 
2.  Create a new [`Lookup`](https://support.google.com/appsheet/answer/12798217#add-lookup) to the column that will be the new table key and delete the old `Reference` column.
3.  Convert the new `Lookup` column to a type that’s compatible with the data, such as `Text`.
4.  In the AppSheet app editor, [regenerate the table](https://support.google.com/appsheet/answer/10106675#regenerate-structure).
5.  Change the column that was just created to type `Ref` and choose the table to reference.
6.  Select a new key in the referenced table.

If you want to add a new reference column after selecting a key that’s not the Row ID, the process is the same for other data sources such as Google Sheets:

1.  In the AppSheet database editor, create a new column compatible with the data. This column should not be a `Reference` column.  
2.  In the AppSheet app editor, [regenerate the table](https://support.google.com/appsheet/answer/10106675#regenerate-structure) to see the new column.
3.  Change the new column to type `Ref` and choose the table to reference.

#### Sequential keys

We are often asked if there is a way for AppSheet to generate sequential, unique keys starting from a user specified initial value. *Sequential* means there must be no gaps in the key sequence. For example, the values `INV01000`, `INV01001`, and `INV01002`, are sequential. Ideally the sequential keys should be issued in order of record creation time.

Unfortunately in a distributed system, with multiple users, and offering offline data inserts, it's technically impossible to generate identifiers satisfying all of these requirements. That is true whether the generated value is used as a key value or as a normal field value.

You can use a [`MAX()`](https://support.google.com/appsheet/answer/10107969) expression to generate sequential unique key values; however, this only works when a single user adds records. For example, you might use the expression `MAX(Orders[OrderNumber])+1` to generate a sequential `OrderNumber` key value for the `Orders` table. It's very risky to use such an expression to generate a key value when more than one user can add records, because the computed key values may not be unique.

#### Random keys

One alternative to system-generated sequential keys, is system-generated random keys.

AppSheet currently supports two mechanisms for creating system-generated random keys.

- The [`UNIQUEID()`](https://support.google.com/appsheet/answer/10108209) function generates a 8-character long unique text value containing letters and numbers.
- The [`RANDBETWEEN(lower-bound, upper-bound)`](https://support.google.com/appsheet/answer/10107982) function generates a pseudo random numeric value between `lower-bound` and `upper-bound`.

Because these functions generate pseudo random values, they do not require coordination between the clients and the server. They work for multiple users doing offline inserts.

### Row number keys (not recommended)

If you do not specify a key, and AppSheet cannot automatically find a good key, AppSheet will default to using the worksheet row number as the key (for example `_RowNumber`). The row number is not a good key. If entries are moved or deleted, or if users add or delete entries simultaneously, the row number for each row will change and there is no way for AppSheet to uniquely identify the row. The Editor will give a warning if row number is chosen as the key.

## Select a key

Key selection can be automatic or manual.

### Automatic key selection

When you add a new table to your app, AppSheet attempts to find a suitable key for the table.

AppSheet first examines each worksheet column from left to right, looking for a column that contains unique data values. If your worksheet has a good key column, it's a good practice to make it the leftmost worksheet column. If AppSheet finds such a column, it makes that column the key.

Appsheet next examines pairs of worksheet columns from left to right, looking for a pair of columns that contain unique data values. The pair of columns need not be adjacent. If AppSheet finds such a pair of columns, it will combine the columns to create a *computed key*. The computed key will be added as a Virtual column at the end of the table.

If AppSheet cannot find a key column using any of these techniques, it will default to using row number as the key. The editor will give a warning if row number is chosen as the key.

### Manual key selection

You can manually override AppSheet's key selection as follows:

1.  Open the app in the app editor.
2.  [View the columns in the table that want to edit](https://support.google.com/appsheet/answer/10106674#view-edit-columns).
3.  Uncheck the **Key** property for the existing key column.
4.  Check the **Key** property for the column you want to make the key.
5.  If you don't want to see this column in your app, deselect the **Show?** property for this column.
6.  Click **Edit**  to change the column settings, and scroll down to the **Initial Value** setting. Change this to `UNIQUEID()` to generate a unique text code for each row.
    **Note**: You can also use `RANDBETWEEN()` if you want a numeric key.
7.   Save the app by selecting one of the following:
    - **Save** - Save the app.
    - **Save & verify data** - Save the app and verify that it is runnable based on external dependencies.

The key value for a record must be assigned once when the record is created and it must remain constant for the life of the record. That is why you must specify the key value in the Initial Value property and never in the App Formula property. The Initial Value property is computed once when the record is created. By contrast, the App Formula is computed once when the record is created and is recomputed each time the record is updated.

## Column types that can't be used as the key

The following column types can't be used as the key in your table:

- [Change column types](https://support.google.com/appsheet/answer/10106528), including:

  - `ChangeCounter`
  - `ChangeLocation`
  - `ChangeTimestamp`

- `Color`

- `List`

- `LongText`

- `Progress`

- `Show`

- `URL`
