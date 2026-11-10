---
fonte: https://support.google.com/appsheet/answer/10106514?hl=en
baixado: 2026-11-10
---

# Deck and table view types

The deck and the table view types have similar capabilities, but your unique use case will determine which view type is a better fit for your application. 

The table view shows information in a very compact way allowing you to quickly scroll to find a row. For a table view example, see the `Job_Inline` table view in the [Field Delivery sample template](https://www.appsheet.com/templates/Track-pending-in-progress-and-completed-deliveries).

The deck view shows information about each row in a "deck-of-cards" format including an image. If the data doesn't have an image, you should consider adding a virtual column with a thumbnail image constructed with the formula: `TEXT_ICON(INITIALS([Column_Of_Type_Name]))`

In addition to the image, the deck view will display two text columns as well as any action buttons for phone numbers or emails. The display columns are chosen in the following order: [Row Label](https://support.google.com/appsheet/answer/10106376), Virtual Columns of type Name, Name type columns, key columns, required columns, normal columns in sheet order.

The deck view also has an option to select a layer of data to display as a secondary view. This *nested* view provides a way to visualize lists of related data created by building [references between tables](https://support.google.com/appsheet/answer/10106510). 

The nested views can be other tables, decks, galleries or charts - for example, a quick snapshot of a product inventory bar chart for each company displayed in a deck view:

To enable a nested view, locate the **Nested Table Column** field within the deck view and choose a related list of items. Customize the view type of that related list by finding the corresponding **inline ref** view that was automatically created when the relationship was created. 

## Get started

Get started with:

- Deck views by using the:
  - `Leads` deck view in the [Lead Tracking sample app](https://www.appsheet.com/samples/An-app-to-manage-and-update-sales-leads?appGuidString=2f43eb0a-1dbf-417f-9e2d-ccb8b9600d02)
  - [Repair manual](https://www.appsheet.com/template/showdef?appId=ProjectTracker-71626) feature sample
- Table views by using the:
  - `Vendors` nested view in a deck view in the [Inventory Management sample app](https://www.appsheet.com/samples/An-app-for-streamlining-inventory-updates?appGuidString=225f95e5-27f6-49db-8c47-05cd309f4c2f)
  - [Interactive map dashboard](https://www.appsheet.com/template/showdef?appId=WorldHeritageSites-71626) feature sample

## Create a deck or table view

To create a deck or table view:

1.   Create a view, as described in [Create a view](https://support.google.com/appsheet/answer/10106688#create-view).
2.  To configure a deck view:
    - Select **deck** as the **View type** when configuring the deck view details, as described in [View details](https://support.google.com/appsheet/answer/10106688#view-details).
    - [Configure the deck view options](#configure-deck-view-options).
    - Configure the **Display**, **Behavior**, and **Documentation** settings, as described in [Configure the view](https://support.google.com/appsheet/answer/10106688#configure-view).
3.  To configure a table view: 
    - Select **table** as the **View type** when configuring the deck view details, as described in [View details](https://support.google.com/appsheet/answer/10106688#view-details).
    - [Configure the table view options](#configure-table-view-options).
    - Configure the **Display**, **Behavior**, and **Documentation** settings, as described in [Configure the view](https://support.google.com/appsheet/answer/10106688#configure-view).
4.  Save the app.

## ****Configure the deck view options

Configure the deck **View options** by using the settings described in the following tables.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Sort by                                                                       | Sort the rows by one or more columns.                                         |
|                                                                               |                                                                               |
|                                                                               | Click **Add** and select the column name and whether to sort in **Ascending** |
|                                                                               | or **Descending** order. Repeat to configure additional sort by rules.        |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Group by                                                                      | Group rows by the values in one or more columns.                              |
|                                                                               |                                                                               |
|                                                                               | Click **Add** and select the column name and whether to sort in **Ascending** |
|                                                                               | or **Descending** order. Repeat to configure additional sort by rules.        |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Group aggregate                                                               | Display a numeric summary of the rows in each group.                          |
|                                                                               |                                                                               |
|                                                                               | Select the format to use for the display from the drop-down list.             |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Main image                                                                    | Image column to display for each row.                                         |
|                                                                               |                                                                               |
|                                                                               | Select an image column from the drop-down or select one of the following      |
|                                                                               | values:                                                                       |
|                                                                               |                                                                               |
|                                                                               | -   Auto assign (*column*) - Let AppSheet automatically assign a value.       |
|                                                                               |     Column that is auto-assigned is shown in parentheses.                     |
|                                                                               | -   None - Don't set this option.                                             |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Primary header                                                                | Top text to use for each row.                                                 |
|                                                                               |                                                                               |
|                                                                               | Select a column from the drop-down or select one of the following values:     |
|                                                                               |                                                                               |
|                                                                               | -   Auto assign (*column*) - Let AppSheet automatically assign a value.       |
|                                                                               |     Column that is auto-assigned is shown in parentheses.                     |
|                                                                               |                                                                               |
|                                                                               | -   None - Don't set this option.                                             |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Secondary header                                                              | Bottom text to use for each row.                                              |
|                                                                               |                                                                               |
|                                                                               | Select a column from the drop-down or select one of the following values:     |
|                                                                               |                                                                               |
|                                                                               | -   Auto assign (*column*) - Let AppSheet automatically assign a value.       |
|                                                                               |     Column that is auto-assigned is shown in parentheses.                     |
|                                                                               |                                                                               |
|                                                                               | -   None - Don't set this option.                                             |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Summary column                                                                | Top-right text to use for each row.                                           |
|                                                                               |                                                                               |
|                                                                               | Select a column from the drop-down or select one of the following values:     |
|                                                                               |                                                                               |
|                                                                               | -   Auto assign (*column*) - Let AppSheet automatically assign a value.       |
|                                                                               |     Column that is auto-assigned is shown in parentheses.                     |
|                                                                               |                                                                               |
|                                                                               | -   None - Don't set this option.                                             |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Nested table column                                                           | Nested table containing a list of `Ref` values.                               |
|                                                                               |                                                                               |
|                                                                               | Select a table from the drop-down.                                            |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Image shape                                                                   | Shape used for the Main image. Select Square, Round, or Full.                 |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Show action bar                                                               | Enable to show action buttons at the bottom of each row.                      |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Actions                                                                       | Action buttons to display in the action bar. The actions are ordered          |
|                                                                               | automatically by AppSheet.                                                    |
|                                                                               |                                                                               |
|                                                                               | To manually control the action order, do any of the following:                |
|                                                                               |                                                                               |
|                                                                               | -   Click **Add** to add actions that you want to display in the order you    |
|                                                                               |     want them to appear.                                                      |
|                                                                               | -   Click  to drag an action to a different order.                            |
|                                                                               | -   Click  to delete an action.                                               |
|                                                                               |                                                                               |
|                                                                               | If you changed the action order, click **Reset** to switch back to the        |
|                                                                               | AppSheet automatic order.                                                     |
|                                                                               |                                                                               |
|                                                                               | Position your cursor over the action and click  Show icon  to open the action |
|                                                                               | configuration in a dialog. You can edit the action configuration and click    |
|                                                                               | **Done**, or click **Go to action** to open the action in the Actions panel.  |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

## ****Configure the table view options

Configure the table **View options** by using the settings described in the following tables.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Sort by                                                                       | Sort the rows by one or more columns.                                         |
|                                                                               |                                                                               |
|                                                                               | Click **Add** and select the column name and whether to sort in **Ascending** |
|                                                                               | or **Descending** order. Repeat to configure additional sort by rules.        |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Group by                                                                      | Group rows by the values in one or more columns.                              |
|                                                                               |                                                                               |
|                                                                               | Click **Add** and select the column name and whether to sort in **Ascending** |
|                                                                               | or **Descending** order. Repeat to configure additional sort by rules.        |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Group aggregate                                                               | Display a numeric summary of the rows in each group.                          |
|                                                                               |                                                                               |
|                                                                               | Select the format to use for the display from the drop-down list.             |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Column order                                                                  | Display columns in a different order than they appear.  See [Control column   |
|                                                                               | order](https://support.google.com/appsheet/answer/10107315).                  |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Column width                                                                  | Control the width of the columns. For example, select Narrow to fit more data |
|                                                                               | on the screen.                                                                |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Enable QuickEdit                                                              | Enable to allow edits to be made directly in the table view.                  |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

When [creating actions](https://support.google.com/appsheet/answer/10107706#create-action) for a table view, if the [Position](https://support.google.com/appsheet/answer/10107706#prominence) setting for an action is set to Inline for a specific column, the action replaces the column content instead of displaying alongside it. If you want to see both the action and the content, you should create another column to attach the action to. For example, attach the action to the `Email` column so that both the  `Name` column contents and the action item display in the table row, as shown in the following figure.

Display inline actions in table views
