---
fonte: https://support.google.com/appsheet/answer/10106757?hl=en
baixado: 2026-11-10
---

# App column type (deep link)

The App column type is used to navigate to a different view in the current app or to another app. The value in an App  column must be a **deep link**.

A deep link is a special text value that follows a particular format. There are two ways to create a deep link:

- [Use a deep link expression](#deep-link-expression) (easiest method)
- [Manually construct a deep link](#manual)

To learn more, [get started with a sample app](#get-started).

**Note**: In addition to being a normal column, App columns can be used with [app launchers](https://support.google.com/appsheet/answer/10105091) and [app actions.](https://support.google.com/appsheet/answer/10107706)

## Get started with a sample app

Learn how to deep link to a view in another app using `LINKTOVIEW()` by using the [Change view on row selection](https://www.appsheet.com/template/showdef?appId=ChangeViewonRowSelection-71626) sample app. This sample defines an action called **Change View** that uses the `LINKTOVIEW()` function to change the current view based on the `View Name` column in the Views table.

## Use a deep link function

AppSheet provides the following functions to create deep links.

+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Function**                                       | **Description**                                    | **Examples**                                       |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| [`LINKTOAPP()`](ht                                 | Deep link to an app                                | Navigate to app `MyApp-123` and displays its       |
| tps://support.google.com/appsheet/answer/10107914) |                                                    | default starting view:                             |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | `LINKTOAPP("MyApp-123")`                           |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| [`LINKTOFILTEREDVIEW()`](ht                        | Deep link to view with filtered row values         | **Note**: The second argument is a filter          |
| tps://support.google.com/appsheet/answer/10107338) |                                                    | expression over the rows in the view. This is      |
|                                                    |                                                    | similar to the filter in                           |
|                                                    |                                                    | [`SELECT()`](https://support                       |
|                                                    |                                                    | .google.com/appsheet/answer/10108207) expressions. |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | -   Navigate to the `Order View` and               |
|                                                    |                                                    |     display `Orders` whose `Order Status` is       |
|                                                    |                                                    |     `Open`:\                                       |
|                                                    |                                                    |     `LINKTOF                                       |
|                                                    |                                                    | ILTEREDVIEW("Order View", [Order Status] = Open)`  |
|                                                    |                                                    | -   Navigate to the `Customers Table View` and     |
|                                                    |                                                    |     display high-priority customers associated     |
|                                                    |                                                    |     with the current sales rep:\                   |
|                                                    |                                                    |     `LINKTOFIL                                     |
|                                                    |                                                    | TEREDVIEW("Customers Table View", AND([Sales Rep]  |
|                                                    |                                                    | = [_THISROW].[Sales Rep Id], [Priority] = High))`  |
|                                                    |                                                    | -   Navigate to the `Students Table View` and      |
|                                                    |                                                    |     display students having ages younger than the  |
|                                                    |                                                    |     current student:\                              |
|                                                    |                                                    |     `LINKTOFILTEREDVIEW                            |
|                                                    |                                                    | ("Students Table View", [Age] < [_THISROW].[Age])` |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| [`LINKTOFORM()`](ht                                | Deep link to a form with pre-filled                | **Note**: In the following examples, the           |
| tps://support.google.com/appsheet/answer/10106538) | values (current app, if not specified)             | function pre-fills the `[Store]` column with the   |
|                                                    |                                                    | value `Main Warehouse` and the `[Type]` column     |
|                                                    |                                                    | with the value `Wholesale`. You can include any    |
|                                                    |                                                    | number of column name-column value pairs in the    |
|                                                    |                                                    | function.                                          |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | -   Navigate to the `New Order` form in the        |
|                                                    |                                                    |     current app:\                                  |
|                                                    |                                                    |     `LINKTOFORM("New Order",                       |
|                                                    |                                                    |  "Store", "Main Warehouse", "Type", "Wholesale")`  |
|                                                    |                                                    | -   Navigate to app `MyOtherApp-123` and           |
|                                                    |                                                    |     display the `Other New Order` form:\           |
|                                                    |                                                    |                                                    |
|                                                    |                                                    |   `LINKTOFORM("Other New Order", "Store", "Main Wa |
|                                                    |                                                    | rehouse", "Type", "Wholesale", "MyOtherApp-123")`  |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| [`LINKTOPARENTVIEW()`](ht                          | Deep link to the parent view                       | Navigate to the parent view in the current app:    |
| tps://support.google.com/appsheet/answer/11621687) |                                                    |                                                    |
|                                                    |                                                    | `LINKTOPARENTVIEW()`                               |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| [`LINKTOROW()`](ht                                 | Deep link to a row (current app, if not specified) | -   Navigate to the `Order Details` view in the    |
| tps://support.google.com/appsheet/answer/10106539) |                                                    |     current app for the row having                 |
|                                                    |                                                    |     key `order456`: \                              |
|                                                    |                                                    |     `LINKTOROW("order456", "Order Details")`       |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | -   Navigate to the `Order Details` view in the    |
|                                                    |                                                    |     current app for the row with the key value     |
|                                                    |                                                    |     contained in `[Order Detail ID]`:\             |
|                                                    |                                                    |                                                    |
|                                                    |                                                    |    `LINKTOROW([Order Detail ID], "Order Details")` |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | -   Navigate to app `MyOtherApp-123` and display   |
|                                                    |                                                    |     the `Other Order Details` view for the row     |
|                                                    |                                                    |     with key `order456:`\                          |
|                                                    |                                                    |     `LINKTOROW("ord                                |
|                                                    |                                                    | er456", "Other Order Details", "MyOtherApp-123")`  |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | -   Navigate to app `MyOtherApp-123` and           |
|                                                    |                                                    |     display the `Other Order Details` view for the |
|                                                    |                                                    |     row with the key value contained in field      |
|                                                    |                                                    |     `[Order Detail ID]`:\                          |
|                                                    |                                                    |     `LINKTOROW([Order Det                          |
|                                                    |                                                    | ail ID], "Other Order Details", "MyOtherApp-123")` |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| [`LINKTOVIEW()`](ht                                | Link to a view (current app if not specified)      | -   Navigate to the `New Orders` view in the       |
| tps://support.google.com/appsheet/answer/10108105) |                                                    |     current app:\                                  |
|                                                    |                                                    |     `LINKTOVIEW("New Orders")`                     |
|                                                    |                                                    | -   Navigate to the app `MyOtherApp-123` and       |
|                                                    |                                                    |     display the `Other New Orders` view:\          |
|                                                    |                                                    |     `                                              |
|                                                    |                                                    | LINKTOVIEW("Other New Orders", "MyOtherApp-123")`  |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+

## Manually construct a deep link

You can manually construct deep links by specifying the [app name](#app-name) and [link parameters](#link-parameters), as described in the following sections and demonstrated in the [examples](#examples).

**Format tips**:

- Whitespace or other HTTP special characters in a deep link must be URL-encoded using the [`ENCODEURL()`](https://support.google.com/appsheet/answer/10106629) expression.
- A deep link is a text value, not an app expression. The link must be enclosed in quotes.

### App name

Your deep link can specify the app name. When no app name is specified, the current app name is assumed.

The app name is defined by the `appName` query parameter in the app URL when viewing the app in the editor or accessing the app in your desktop browser. (It is **not** equivalent to the Short Name of the app defined in Settings.) For example, in the following app URL the app name is `ShiftManagement-3518598`:
`https://www.appsheet.com/template/AppDef?appName=`**`ShiftManagement-3518598`**`&appId=58bb9fcc-b701-462a-87fd-34129fe8fcba&quickStart=False#Data.Columns.Admin%20Scheduled%20Shift`

### Link parameters

Your deep link can control which view and row is displayed by specifying optional link parameters following a `#` symbol. Link parameters are separated using the `&` symbol. The following link parameters are supported:

|                    |                                                                                                                                                                                                                                                                                                                         |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Link parameter** | **Description**                                                                                                                                                                                                                                                                                                         |
| `view`** **        | Name of the UX view to be displayed. If any link parameters are specified, this parameter is required.                                                                                                                                                                                                                  |
| `row`              | Key of the row to be displayed. This parameter is required for some views and is optional for others.                                                                                                                                                                                                                   |
| `mapcolumn`        | Name of the `Address` or `LatLong` column on which the Map view is based. This parameter is used for Map view controls.                                                                                                                                                                                                 |
| `at`               | Minimum timestamp required for the data. Setting the timestamp to a time in the future can force the app to sync to pick up data changes rather than work with stale data. The most common use for this parameter is in sending an email, SMS, or push notification with a link to a particular data entry in the app.  |

### Examples of manually constructed deep links

The following table provides example of manually constructed deep links.

|                                 |                                                                                              |                                                                                                                                                    |
|---------------------------------|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| **Deep link to**                | **Example**                                                                                  | **Description**                                                                                                                                    |
| App                             | `"MyApp-123"`                                                                                | Navigate to app `MyApp-123` and display its default starting view.                                                                                 |
| View in the current app         | `"#view=New Orders"`                                                                         | Navigate to the `New Orders` view in the current app.                                                                                              |
| View in another app             | `"MyOtherApp-123#view=Other New Orders"`                                                     | Navigate to app `MyOtherApp-123` and display the `Other New Orders` view.                                                                          |
| View and row in the current app | `"#view=Order Details&row=order456"`                                                         | Navigate to the `Order Details` view in the current app and display the row with key `order456`.                                                   |
|                                 | `CONCATENATE("#view=Order Details&row=", ENCODEURL([Order Detail ID]))`                      | Navigate to the `Order Details` view in the current app and display the row with the key value contained in `[Order Detail ID]`.                   |
|                                 | `CONCATENATE(LINKTOVIEW("Inspections"), "&at=", ENCODEURL(NOW()+1))`                         | Navigate to the Inspections view in the current app and force a sync.                                                                              |
| View and row in another app     | `"MyOtherApp-123#view=Other Order Details&row=order456"`                                     | Navigate to app `MyOtherApp-123` and display the `Other Order Details` view for the row with key `order456`.                                       |
|                                 | `CONCATENATE("MyOtherApp-123#view=Other Order Details&row=", ENCODEURL([Order Detail ID]))`  | Navigate to app `MyOtherApp-123` and display the `Other Order Details` view for the row with the key value contained in field `[Order Detail ID]`. |
| App and force a sync            | `CONCATENATE(LINKTOAPP("MyApp-123"), "#at=", ENCODEURL(NOW()+1))`                            | Navigate to app `MyApp-123`, force a sync, and display its default starting view.                                                                  |
