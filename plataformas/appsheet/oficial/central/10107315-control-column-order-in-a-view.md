---
fonte: https://support.google.com/appsheet/answer/10107315?hl=en
baixado: 2026-11-10
---

# Control column order in a view

AppSheet does its best to automatically order columns by their importance. If you’re using a detail, form, or table view, you can manually control the column order.

The following sections describe [how AppSheet automatically orders columns](#how) and how you can [manually control the column order](#manually-order).

## How AppSheet automatically orders columns

AppSheet automatically orders columns using the following rules:

- Rule 1. AppSheet always shows the key because by definition it uniquely identifies each row. Without the key, it is unclear which data entry is being shown. If the key is hidden (by disabling the **Show?** toggle in the editor), AppSheet does not show the key and instead shows the data left to right. See [What is a key?](https://support.google.com/appsheet/answer/10106672)
- Rule 2. Next AppSheet shows any fields that call for actionable icons (such as a phone number, email address, and so on). AppSheet assumes these items are things you'd want a quick click action on.
- Rule 3. Then AppSheet proceeds left to right in spreadsheet column order. Position the more important columns to the left in your spreadsheet.
- Rule 4. Many spreadsheets have a rightmost column that is computed by a formula-- such as, cost of items. If AppSheet recognizes this pattern, it makes sure to include this column.

## Manually control the column order in a view

To add, reorder, or delete columns at the **global** level, see [Add, reorder, or delete columns](https://support.google.com/appsheet/answer/10106675).

If you’re using a detail, form, or table view, you can manually control the column order when configuring the view.

From a table view, if you click on one of the rows, it will expand to show the whole row in a detail view. Currently, that detail view will not maintain the column order you specified for the table view. You can set that up separately by creating a detail view for the table, mark its position as `Ref` (to indicate that it isn't actually shown using a view button but only displayed when referenced), and define its column order as well.

To manually control the column order in a detail, form, or table view:

1.  Open the app in the editor.
2.   Go to **App ** App icon **\> Views** and click the view you want to edit in the View panel.
     We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

    ## If you are using the legacy editor

    Go to **UX \> Views** and expand the view you want to edit.  
3.  Select the view you want to edit.
4.  By default Column order is set to **Automatic** and the columns are ordered automatically, as described in [How AppSheet automatically orders columns](#how).

    To change the column order, in the Column order field click **Manual** and do any of the following:
    - To add columns, click + **Add**, select columns that you want to display, and click **Select**. Alternatively, position your cursor over a column name and click **+** and then **Add column before** or **Add column after**.
    - To delete one or more columns, select them in the list and click **Remove**. Alternatively, position your cursor over a column name and click **x**.
    - To rearrange columns, select them in the list, click **Move to**, and select an option in the drop-down. Alternatively, click  to drag a column to a different order.
    - If you want to control the order of a subset of columns, but still include all columns, you can add an **All other columns **at the desired location to include the remaining columns at the specified position..
    - To view or edit the column properties, position your cursor over a column name and click Edit icon . 
5.  Save your app.

**Note**: Make sure that you add the [Show type columns](https://support.google.com/appsheet/answer/12463320) that you want to be displayed.
