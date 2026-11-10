---
fonte: https://support.google.com/appsheet/answer/10106688?hl=en
baixado: 2026-11-10
---

# Views: The Essentials

**Views** allow you to control how, when, and where data is presented to the app user, and how the user interacts with the data.

The following provides an example of the **Nearby** card view from the [Facility Inspections](https://www.appsheet.com/templates/Inspect-points-throughout-various-properties?appGuidString=d8389191-0217-42c0-bd50-406993b660f6) template. You have full control over the view name (**Nearby**), its position in the app (**navigation bar**), its layout and contents, and conditions for when it is displayed.

Nearby card view from Facility Inspections sample.

See also [View types](https://support.google.com/appsheet/answer/10106772).

## Explore the Views pane

We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

**The Views pane is available in the new editor only. **The Views pane does not appear in the legacy editor.

Go to **App ** App icon **\> Views**.

The Views pane is displayed and the first view in the primary navigation is opened in the editor.

Views secondary panel

As highlighted in the previous figure, you can use the View pane to:

- [Create a view](#create-view)
  You can create views that appear in the **primary navigation**, **menu navigation**, or that are referenced from **other views** but that do not appear in navigation
- [Configure a view](#configure-view) (select in the list)
- Manage views, including:
  - [Preview a view](#preview)
  - [Rename a view](#rename-view)
  - [Move a view to a different position](#move-view) (primary, menu, other)
  - [Copy a view](#copy-view)
  - [Add a view to favorites](#favorites)
  - [Delete a view](#delete-view)
- Manage system-generated views for your data
  **Notes**:

  - You can [configure](#configure-view), [preview](#preview), [copy](#copy-view), and [delete](#delete-view) system-generated views. 
  - If you are using the legacy app editor, you can show or hide system-generated views by default. See [Configure app editor settings](https://support.google.com/appsheet/answer/13396480).
- Go to view settings, as described in [View settings: The Essentials](https://support.google.com/appsheet/answer/10107387)
- Search the list of views
- Expand or collapse all sections in the navigation

See also [View types](https://support.google.com/appsheet/answer/10106772).

## ****Create a view

 To create a view:

1.   Open the app in the app editor.
2.  Go to **App ** App icon **\> Views**.
3.  [Depending on where you want to launch the view in your app](#position), click **+** adjacent to Primary navigation, Menu navigation, or Other views. 
4.  You can change the view position, as described in [Move a view to a different position](#move-view),
5.  The Add a new view dialog displays.
6.  Do one of the following:
    - To add a suggested view, click the suggested view.
    - Click **Create a new view**.
7.  [Configure the view](#configure-view).
8.  Save the app.
     

We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

## If you are using the legacy editor

 To create a view:

1.   Open the app in the app editor.
2.  Go to **UX \> Views**.
3.  Perform one of the following tasks:
    - To create a new view, click **New View**.
    - To add a suggested view, click the suggested view.
    - To copy an existing view, expand it and click **Copy**.

      Create a new view, add a suggested view, or copy an existing view.
4.  [Configure the view](#configure-view).
5.  Save the app.

## ****Configure the view

Configure the view by using the settings described in the following sections.

- [View details](#view-details)
- [View options](#view-options)
- [Display](#display)
- [Behavior](#behavior)
- [Documentation](#documentation)

### ****View details

Configure the view details defined in the following table.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| View name                                                                     | Name of the view. It must be unique within your app.                          |
|                                                                               |                                                                               |
|                                                                               | If you enter a name that is the same as an existing view, the app editor will |
|                                                                               | automatically append a number to the view name to differentiate between them. |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| For this data                                                                 | Data referenced by this view. Select a                                        |
|                                                                               | [table](https://support.google.com/appsheet/answer/10105821) or               |
|                                                                               | [slice](https://support.google.com/appsheet/answer/10106592) from the list.   |
|                                                                               | Only data from the table or slice can be displayed within the view.           |
|                                                                               |                                                                               |
|                                                                               | To create a new slice, see [Create a slice when configuring a                 |
|                                                                               | view](http                                                                    |
|                                                                               | s://support.google.com/appsheet/answer/10106592#create-slice-configure-view). |
|                                                                               |                                                                               |
|                                                                               | **Note**: This option is not available for [dashboard                         |
|                                                                               | views](https://support.google.com/appsheet/answer/10106384).                  |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| View type                                                                     | [View type](https://support.google.com/appsheet/answer/10106772) that         |
|                                                                               | determines how the data is presented to the app user.                         |
|                                                                               |                                                                               |
|                                                                               | Select from a variety of view types, such as chart, form, detail, map, table, |
|                                                                               | and more. Each view type has its own characteristics and type-specific [view  |
|                                                                               | options](#view-options).                                                      |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Position                                                                      | Where you want to launch the view in your app.  Select one of the following   |
|                                                                               | positions:                                                                    |
|                                                                               |                                                                               |
|                                                                               | -   **Primary navigation**: Accessed in the **primary navigation bar** at the |
|                                                                               |     bottom of the screen for mobile and tablet apps and in the left           |
|                                                                               |     navigation bar on desktop apps Set **Position** to **first**, **next**,   |
|                                                                               |     **middle**, **later**, or **last** based on the preferred order of        |
|                                                                               |     appearance.\                                                              |
|                                                                               |     **Note**: If you select the same Position setting for multiple views,     |
|                                                                               |     they are ordered chronologically based on the view creation time.         |
|                                                                               | -   **Menu navigation**: Accessed in the app's main menu. Set **Position**    |
|                                                                               |     to **menu**.                                                              |
|                                                                               | -   **Other view**: Accessed only when [referenced implicitly while           |
|                                                                               |     navigating through                                                        |
|                                                                               |     data](https://support.google.com/appsheet/answer/10106516). Set           |
|                                                                               |     **Position** to **ref**.                                                  |
|                                                                               |                                                                               |
|                                                                               | For example, the following shows the position of primary and menu navigation  |
|                                                                               | views in mobile apps:                                                         |
|                                                                               |                                                                               |
|                                                                               | Mobile app showing primary views in the bottom navigation bar and menu views  |
|                                                                               | in the dropdown menu                                                          |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

### ****View options

Each [view type](https://support.google.com/appsheet/answer/10106772) has type-specific view options that allow you to tailor the appearance of the view. For example, the view options for a [table view](https://support.google.com/appsheet/answer/10106514) are shown in the following figure.

View options example

For more information about the view options shown, see:

- [Control row sort order in a view](https://support.google.com/appsheet/answer/10106522)
- [Control grouping in a view](https://support.google.com/appsheet/answer/10106698)
- [Control column order in a view](https://support.google.com/appsheet/answer/10107315)
- [Control column width in a view](https://support.google.com/appsheet/answer/10107316)
- [Allow quick edit columns in a view](https://support.google.com/appsheet/answer/10106609)

### ****Display

All view types have configurable display options. Display options affect how the view is presented in the navigation bar along the bottom of the app display, and in the app's main menu.

Display options for a view

Configure the view display by using the settings defined in the following table.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Icon                                                                          | Icon to be displayed along with the view's **Display name** (see below).      |
|                                                                               | Choose an icon from the predefined list. Custom icons are not allowed. Every  |
|                                                                               | view must have an icon. If no icon is selected, a type-specific default will  |
|                                                                               | be used.                                                                      |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Display name                                                                  | Name displayed for the view. Enter a fixed value (**T**) or to a [text        |
|                                                                               | expression](https://support.google.com/appsheet/answer/10108184) (**flask**). |
|                                                                               |                                                                               |
|                                                                               | Display name using expression                                                 |
|                                                                               |                                                                               |
|                                                                               | If **Display name** is not specified or if set to an expression that          |
|                                                                               | evaluates to a blank value, the view's name is used.                          |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Show if                                                                       | [Yes/No expression](https://support.google.com/appsheet/answer/10107946) that |
|                                                                               | determines whether the view is included as a navigation element in its        |
|                                                                               | designated **Position** (for example, in the navigation bar or the main       |
|                                                                               | menu).                                                                        |
|                                                                               |                                                                               |
|                                                                               | If the expression evaluates to `TRUE`, the view will be included.             |
|                                                                               |                                                                               |
|                                                                               | Show if using expression                                                      |
|                                                                               |                                                                               |
|                                                                               | No **Show if** expression is equivalent to the expression, `TRUE` .           |
|                                                                               |                                                                               |
|                                                                               | **Warning**: **Show if is not a security measure**. **Show if** merely hides  |
|                                                                               | the view from navigation; there are other legitimate ways for a user to       |
|                                                                               | access the view.                                                              |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

### ****Behavior

Each [view type](https://help.appsheet.com/en/articles/961510-view-types) has type-specific behavior options that may allow you to tailor the behavior of the view when the user interacts with it. For example, the behavior options for a [table view](https://help.appsheet.com/en/articles/3509909-ux-view-type-deck-and-table) are shown here:

Behavior options in a view

Configure the behavior for the view by using the settings defined in the following table, if available.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Event Actions                                                                 | Some view types provide the opportunity to customize the app's response to    |
|                                                                               | certain events triggered by user activity. When a recognized [view            |
|                                                                               | event](https://support.google.com/appsheet/answer/10108214) occurs, the       |
|                                                                               | configured [action](https://support.google.com/appsheet/answer/10107706) is   |
|                                                                               | performed.                                                                    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| App link                                                                      | Not configurable. Provides two ways to target the view from a navigation      |
|                                                                               | element:                                                                      |
|                                                                               |                                                                               |
|                                                                               | -   [Deep link](https://support.google.com/appsheet/answer/10106757) to the   |
|                                                                               |     view to be used as the target of an                                       |
|                                                                               |     [action](https://support.google.com/appsheet/answer/10107706) of type     |
|                                                                               |     `App: go to another view within this app`. For example:                   |
|                                                                               |     (`LINKTOVIEW("By House")`                                                 |
|                                                                               |                                                                               |
|                                                                               | -   Full URL for the view to be used as the target of an action of type       |
|                                                                               |     `External: go to a web site` or from a web browser.                       |
|                                                                               |                                                                               |
|                                                                               | **Note**: The use of app links is not affected by a view's **Show if**        |
|                                                                               | setting; a **Show if** expression that evaluates to `FALSE` does not prevent  |
|                                                                               | the use of an app link to the view.                                           |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

### ****Documentation

Expand the **Documentation** section and enter a descriptive comment for the card view that will enable collaborators to easily understand its purpose.

## Preview a view

 To preview a view:

1.   Open the app in the app editor.
2.  Go to **App ** App icon **\> View**.
3.  Position your cursor over the view in the Views pane and select **More \> Show in preview**.

We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

## If you are using the legacy editor

1.  Open the app in the app editor.
2.  Go to **UX \> Views**
3.  Expand the view you want to preview.
4.  Click **Show in Preview**.

## Rename a view

To rename a view:

1.  Open the app in the app editor.
2.  Go to **App ** App icon **\> View**.
3.  Position your cursor over the view in the Views pane and select **More ************************\> Rename**.
4.  Edit the name end press **Enter**.
5.  Save the app.

You can also rename a view by editing the **View name** field when configuring the [view details](#view-details).

We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

## If you are using the legacy editor

1.  Open the app in the app editor.
2.  Go to **UX \> Views**
3.  Expand the view you want to rename.
4.  Edit the **View name** field under [View details](#view-details).
5.   Save the app.

## Move a view to a different position

To move a view to a different position:

1.  Open the app in the app editor.
2.  Go to **App ** App icon **\> View**.
3.  Position your cursor over the view in the Views pane and select **More ********\> Move to **and select **Primary navigation**, **Menu navigation**, or **Other view**. 
    The currently selected position is checked.
4.   Save the app.
     

You can also move a view to a different position by editing the [**Position**](#position) field when configuring the [view details](#view-details).

We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

## If you are using the legacy editor

1.  Open the app in the app editor.
2.  Go to **UX \> Views**
3.   Edit the **Position** field under [View details](#view-details).
4.   Save the app.

## Copy a view

To copy a view:

1.  Open the app in the app editor.
2.  Go to **App ** App icon **\> View**.
3.  Position your cursor over the view in the Views pane and select **More ************************\> Duplicate**.
4.   Save the app.

The view is copied *viewname_n*, by default, where *viewname* is the name of the existing view and *n* is incremented by 1 each time you copy the view. You can edit the name of the view, see rename the view.

We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

## If you are using the legacy editor

 To copy a view:

1.   Open the app in the app editor.
2.  Go to **UX \> Views**.
3.  Expand the view you want to copy.
4.  Click **Copy**.
5.   Save the app.

## Add a view to your favorites

To easily access frequently used views, add them to your favorites. 

Favorites list

 To add a view to your favorites:

1.  Open the app in the app editor.
2.  Go to **App ** App icon **\> View**.
3.  Position your cursor over the view in the Views pane and select **More ********************************************************\> Add to favorites**.

Remove a view from your favorites by positioning your cursor over the view in the Favorites list and clicking **x**.

## ****Delete a view

 To delete a view:

1.   Open the app in the app editor.
2.  Go to **App ** App icon **\> View**.
3.  Position your cursor over the view in the Views pane and select **More \> Delete**.
4.  Save the app.

We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

## If you are using the legacy editor

 To delete a view:

1.   Open the app in the app editor.
2.  Go to **UX \> Views**.
3.  Expand the view you want to delete.
4.  Click **Delete**.
5.  Save the app.
