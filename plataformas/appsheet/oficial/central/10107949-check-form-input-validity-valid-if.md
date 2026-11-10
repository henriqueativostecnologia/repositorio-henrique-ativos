---
fonte: https://support.google.com/appsheet/answer/10107949?hl=en
baixado: 2026-11-10
---

# Check form input validity (Valid_If)

Column constraints are UI features that affect the app's behavior and presentation. They aren't security controls and don't prevent users from accessing the data. For information about securing your data, see [Security: The Essentials](https://support.google.com/appsheet/answer/10105078).

Every input in a form is checked for validity based on its type. For example, a column of type `Number` won't accept `Hello` as an input. A `Valid_If` [column constraint](https://support.google.com/appsheet/answer/10107948) is a type of expression used in situations where the validity of the input requires richer data-dependent logic.

A `Valid_If` constraint is a condition expression that determines if the user input for the associated column is valid. 

Here are examples of commonly-used `Valid_If` constraints:

- Does the value of the column satisfy a simple condition? For example, comparing the value with a constant (such as, `[_THIS] > 5`), or comparing the value with another column (such as, `[_THIS] > [ColumnA]`).
- Is the value of the column in a list? You can accomplish this in one of the following ways:
  - Create a drop-down menu from the list, as described in [Drop-down from Valid_If](https://support.google.com/appsheet/answer/10107665) 
  - Validate the form input *without* creating a drop-down menu of values. For example:
    - `AND(TRUE, IN([_THIS], LookupTable[ColumnC]))`
    - `AND(TRUE, IN([_THIS], SELECT(LookupTable[ColumnC], ([ReportDate] > (TODAY() - 7))))`

Invalid inputs can prevent saving data or progressing to the next page in a form. For data changes made through forms or [Quick Edit](https://support.google.com/appsheet/answer/10106609) columns in detail views, `Valid_If` constraints are only enforced for visible inputs. This is because:

- There are many ways columns can be hidden or omitted from the view (for example, excluded from a slice, excluded from column order, or on a different page in a branching form), so it's often unclear whether blocking the user was intended or expected.
- If a user is blocked by a hidden column failing validation, the user generally has no way to fix it and doesn't understand why they're stuck. If the app creator didn't intend them to be blocked there, the user may not understand why either, leading to lost productivity.

`Valid_If` conditions can still reference values of hidden columns, so if you do want to block the form due to hidden values, just attach the expression to a visible column.

For updates made through actions, `Valid_If` conditions are enforced in two cases:

1.  If the column being updated becomes invalid, the update is blocked.
2.  If the update causes a different column to become invalid, the update is blocked.

This means an action won't be blocked due to preexisting invalid values that are unrelated to the action itself.

**New to expressions?** See also [Expressions: The Essentials](https://support.google.com/appsheet/answer/10104642).

## Valid_If and dependent drop-downs

Dependent drop-down menus are a common design pattern in apps that capture input. For example, consider an app like  the [Lead Tracking template](https://www.appsheet.com/samples/An-app-to-add-and-update-sales-leads?appGuidString=2f43eb0a-1dbf-417f-9e2d-ccb8b9600d02), that asks for a `Lead Region` (America, Asia, Europe), then for a `Country` within that region. This actually requires relatively complex logic, but AppSheet tries to make it simple. Dependent drop-down menus are driven by a separate lookup table.

In the sample, there is a separate `Regions` lookup table with two columns, `Region` and `Country`, which serves to describe the allowed combinations of regions and countries.

The `Lead Region` column has a regular `Valid_If` constraint: `Regions[Region]`. Therefore, when a new entry is being added, the input for this column shows three choices: `America`, `Asia`, and `Europe`.

Likewise, the `Country` column specifies a similar `Valid_If` constraint: `Regions[Country]`. However, because it follows the `Lead Region` column, and because both specify columns from the same lookup table, `Regions`, AppSheet recognizes the intent and implements a dependent drop-down menu.

Internally, AppSheet creates an expression to capture the allowed set of values for the `Country` column. The expression must say (in English!):

- Look at the `Regions` table.
- Filter the rows to make sure the `Region` column of the table matches the value in the `Lead Region` column of the row being edited in the form.
- Extract the `Country` column from those filtered rows.
- Eliminate any duplicates--these are the allowed countries!
- Recompute this list each time `Lead Region` is changed.

Strictly for the expression aficionado, the full underlying AppSheet expression would be: `IN( [_THIS], SELECT(Regions[Country], [_THISROW].[Lead Region] = [Region]))` 

While most app creators will never need to express something this complicated, you could in fact provide this expression as a `Valid_If` constraint. It's useful to know for advanced use cases. For example, instead of using an equality condition, an app creator could use inequality or richer expressions to build very expressive dynamic drop-down menus.

## Troubleshoot "failed Valid_If condition" for EnumList fields

The problem occurs when the `EnumList` field specifies a **`Valid_If`**` `expression containing a list of valid values. If you attempt to store a record containing two or more values in the `EnumList` field, the `Valid_If` condition will fail, and CSV Import will fail with the message:

`"Error: Row having key '<key value>' in table '<table Name>' containing value '<enumList field value>' failed Valid_If condition"`

For example, the `EnumList` field might specify the `Valid_If` expression:

`LIST("A", "B", "C", "D")`

The system automatically converts this `Valid_If` expression into the following equivalent `Valid_If` expression. Note that` [_THIS]` refers to the value of the current field. In this case, the `EnumList` field.

`IN([_THIS], LIST("A", "B", "C", "D"))`

When the server expression system evaluates the `IN` expression, it fails to detect that the `EnumList` field may contain a list of values. It mistakenly treats the value in the `EnumList` as a single value which it compares to each value in the `LIST`. For example, if the `EnumList` field contains "A , C", it compares "A , C" to the `LIST` values "A", then "B", then "C", and finally "D". The EnumList value "A , C" does not match any of these values, therefore the `Valid_If `condition fails.
