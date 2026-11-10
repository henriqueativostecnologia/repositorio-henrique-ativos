---
fonte: https://support.google.com/appsheet/answer/10106434?hl=en
baixado: 2026-11-10
---

# Editable keys

We are sometimes asked if there is a way to make the key value editable. The short answer is **No**. Having a unique, static key is important to keeping your data consistent and accessible. However, you can make fields editable and have unique keys without risking your data.

The key value itself must remain constant because the key value is used to locate the record. Imagine two users attempting to update the same record at the same time, and one of the users attempting to change the key. The following events might occur:

1.  The first user retrieved the record and started updating it.
2.  The second user retrieved the record and started updating it. This user updated the key value.
3.  The second user saved their changes. This results in the record's key value changing.
4.  The first user saved their changes. This would result in the record not being found because the original key value is no longer present.

The record's key value must remain constant for the life of the record. However, you can ensure that a field's value is unique, while remaining editable. Normally, when someone asks to make the key editable, they're trying to do something like this.

1.  They have an `Employee` table and wish to use the `Name` value as the key.
2.  Each employee's `Name` is required to be unique but its value may change over time.
3.  They want the system to ensure that no two employees have the same name. The system should prevent a duplicate employee name from being added. If an existing employee name is edited, the system should prevent a duplicate employee name from being created.

Another common example is a `User` table where each user must have a unique email address. However, the user's email address must be editable.

You can achieve this by:

1.  Adding a new key column to your worksheet to serve as the key. The column will contain a [`UNIQUEID()`](https://support.google.com/appsheet/answer/10108209) value that uniquely identifies each record. For example, in the `Employee` table, you might call the new key column `EmployeeId`.
2.  In the AppSheet Editor, add the new key column, mark it as the Key, set its Initial Value to `UNIQUEID()`, and make it **Hidden**. This results in a key value that is auto generated, is not editable, and does not appear in views.
3.  In the editor, add a `Valid_If` expression to the `Name` field to ensure that every record has a unique `Name` value. The `Name` field is editable because it's not a key.

Here are the exact steps for doing this for the `Employee` table example:

1.  Add a new column as the first column in your worksheet. Give the new column a name ending in `Id`. For example, in the `Employee` table call the new column `EmployeeId`.

2.  Assign each existing row in the worksheet a unique key value as described in [Manually generate UNIQUEID() key values](https://support.google.com/appsheet/answer/10105828). Skip all empty rows.

3.  [Regenerate the structure](https://support.google.com/appsheet/answer/10106675). 

4.  Set the new field's initial value property to `UNIQUEID().`

5.  Mark the new field as the key for that table. Ensure that no other column in the table is marked as a key.

6.  If you wish, you can mark the new field as **Hidden**. This prevents the key field from being displayed in the app.

7.  Add a `Valid_If` expression to the non-key field you want to ensure has a unique value. In our example, do this for the **Name** field. See [Use lists to validate column values](https://support.google.com/appsheet/answer/10107669#list-validate-column-values).

8.  You may wish to set the non-key field’s Label property to `True`. This displays the Label field's value in lieu of the actual key value. In our example, this displays the employee's `Name`. See [Row labels](https://support.google.com/appsheet/answer/10106376) for more information.
