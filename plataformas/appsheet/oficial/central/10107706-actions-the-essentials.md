---
fonte: https://support.google.com/appsheet/answer/10107706?hl=en
baixado: 2026-11-10
---

# Actions: The Essentials

Actions perform specific operations. Actions can be extremely helpful in accomplishing a variety of different tasks with your app, from email to copying a row. It's also possible to execute a sequence of actions.

There are four types of actions included in an app definition, as described in [Action types](#action-types).

- [**Navigation**](#navigate): Navigate to a different view within an app
- [**Data-change**](#data-change): Modify (add, delete, update) data in your app
- [**External**](#external-communication): Interact with an external service, such as opening the phone app on a device to start a call or sending information to an external service (such as a push notification or an SMS message
- **[Grouped](#composite):** Execute a sequence of actions in a specific order.

Besides the actions you can create in your app, other actions are automatically created. You can learn more about [system actions](https://support.google.com/appsheet/answer/10108131) and how to control them.

Not only can you create actions, you can also configure them to run when certain view navigation events happen using [view events](https://support.google.com/appsheet/answer/10108214).

The following sections provide more information about actions:

- [Where do actions appear?](#where-appear)
- [Where can an action run?](#where-run)
- [When does an action run?](#when-run)
- [How to show, hide, or reorder actions in a view](#show-hide-reorder)
- [Create an action](#create-action)
- [Configure an action](#configure-action)
- [Reorder actions in your app](#reorder-actions)
- [Add an action to your favorites](#favorites)
- [Action types](#action-types)

## Where do actions appear?

### Quick actions

In the detail view, a button is shown for each action in your app. When the button is tapped, the action is triggered.

Details view showing action buttons

### Bulk actions

In the table, deck, and gallery views, actions can be applied in bulk across many rows simultaneously. See [Use bulk actions](https://support.google.com/appsheet/answer/10107372).

## Where can an action run?

All AppSheet apps run on a device or in a browser. However, all apps are actually hosted from the AppSheet cloud service (also called the AppSheet *backend*) so some actions can also run in the cloud service, as follows:

- Navigation actions can only run in the app on the device or in a browser.
- Data- change actions can run in the app or in the cloud service. The app data is accessible and can be changed at either location.
- External actions only run in the client. For example, the External: Start an email action opens the email app on the device running the AppSheet app, it doesn't actually send the email. 

## When does an action run?

Every data action has to be *triggered* by some event that causes it to run. As the app creator, you control the trigger, as follows:

- **Explicit user invocation**: [Create an action](#create-action) to be shown as a visual icon or button. When the user taps or clicks on the icon or button, the app invokes the action.
- **Implicit user invocation**: Every view in the app has some standard behaviors when a user interacts with the data in the view. For example, when a user taps on a row in a tabular view, that specific row is shown in detail in a detail view. By default, the **Row selected** event triggers a system-defined UI Navigation action that takes the user to the new view. As the app creator, you can control a subset of the triggering events associated with each view. See [Run actions based on view events](https://support.google.com/appsheet/answer/10108214).
- **Automatic invocation in the cloud service**: Define automation bots that run in the cloud service and execute actions when specific changes occur or on a schedule. See [AppSheet automation: The Essentials](https://support.google.com/appsheet/answer/11998993).

## How to show, hide, and reorder actions in a view

To show, hide, and reorder actions in a view, do one or more of the following:

- [Create an action](#create-action) that will display for views that use the table.
- [Reorder actions in your app](#reorder-actions).
- Create a [group action](#composite) to run a set of actions, one-by-one, in order.
- [Configure](#configure-action) the **Only if this condition is true** setting in the [Behavior](#behavior) section for an action to control which rows show the actions and the order they are displayed.
  For example:
  - To show an action for detail views only, you can configure the setting as follows: `SHOW_IF = CONTEXT("VIEWTYPE")="Detail"`
  - To order actions as ABC for detail views and ACB for all other views, you can configure the setting for each action as follows:
    - Action A: Leave blank
    - Action B:  `SHOW_IF = CONTEXT("VIEWTYPE")="Detail"`
    - Action C:  Leave blank
    - Action B (duplicate): `SHOW_IF = NOT(CONTEXT("VIEWTYPE")="Detail")`
- Add a [slice](https://support.google.com/appsheet/answer/10106592) to filter specific actions in views. See [Slice actions](https://support.google.com/appsheet/answer/10106511).
- For deck views, [configure the action bar](https://support.google.com/appsheet/answer/10106514#configure-deck-view-options).
- [Hide system actions](https://support.google.com/appsheet/answer/10108131).

## Create an action

To create an action for a table:

1.  Open the app in the app editor.

2.  Go to **Actions**, click **+ **in the top header of the Actions panel, and select one of the suggestions or click **Create a new action**.
     We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

    ## If you are using the legacy navigation

    Go to **Behavior \> Actions **and click **+ New Action** or select one of the suggestions, if provided.

3.  [ Configure the action](#configure-action).

4.  Save the app.

## ****Configure an action

Configure an action by using the settings described in the following table, and optionally the following sections:

- [Display](#display)
- [Behavior](#behavior)
- [Documentation](#documentation)
- [Inputs](#advanced)

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Action name                                                                   | Displayed name of the action.                                                 |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| For a record of this table                                                    | Table to which the action applies.                                            |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Do this                                                                       | Action to be performed. Select an action from the drop-down list. See [Action |
|                                                                               | types](#action-types).                                                        |
|                                                                               |                                                                               |
|                                                                               | Based on the type selected, additional configuration options may be           |
|                                                                               | displayed, and are described with the action type descriptions.               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Position                                                                      | Control the position of the action or hide it from the display. Valid values  |
|                                                                               | are:                                                                          |
|                                                                               |                                                                               |
|                                                                               | -   **Primary** - Display independently of scrolling, such as floating        |
|                                                                               |     buttons on mobile devices and at the top of a view on desktop browsers.\  |
|                                                                               |     **Note**: On mobile devices using the [new mobile framework               |
|                                                                               |     (preview)](https://support.google.com/appsheet/answer/15831909), a        |
|                                                                               |     maximum of 6 primary actions are displayed. On mobile devices using the   |
|                                                                               |     legacy mobile design, a maximum of 4 primary actions are displayed.\      |
|                                                                               |     Primary position for action                                               |
|                                                                               | -   **Prominent** - Display in detail views as a button at the top of the     |
|                                                                               |     screen (most common).\                                                    |
|                                                                               |     Action prominent position                                                 |
|                                                                               | -   **Inline** - Display alongside the associated column.\                    |
|                                                                               |     Action inline position                                                    |
|                                                                               | -   **Hide** - Don't display in any view.\                                    |
|                                                                               |     Action hide position                                                      |
|                                                                               |                                                                               |
|                                                                               | The following illustration provides an example of the location of an          |
|                                                                               | action based on this setting.                                                 |
|                                                                               |                                                                               |
|                                                                               | Action prominence                                                             |
|                                                                               |                                                                               |
|                                                                               | **Note**: For table views, if an action is set to Display inline for a        |
|                                                                               | specific column, the action replaces the column content instead of displaying |
|                                                                               | alongside it. If you want to see both the action and the content, you should  |
|                                                                               | create another column to attach the action to. For example, attach the action |
|                                                                               | to the `Email` column so that both the  `Name` column contents and the action |
|                                                                               | item display in the table row, as shown in the following figure.              |
|                                                                               |                                                                               |
|                                                                               | Display inline actions in table views                                         |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

### ** **Display

All actions have configurable display options. The display options affect how the view is presented in the navigation bar along the bottom of the app display, and in the app's main menu.

Configure the action display by using the settings defined in the following table.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Display name                                                                  | Name displayed for the action. Enter a fixed value (**T**) or to a [text      |
|                                                                               | expression](https://support.google.com/appsheet/answer/10108184) (**flask**). |
|                                                                               |                                                                               |
|                                                                               | Display name using expression                                                 |
|                                                                               |                                                                               |
|                                                                               | **Notes**:                                                                    |
|                                                                               |                                                                               |
|                                                                               | -   If **Display name** is not specified or if set to an expression that      |
|                                                                               |     evaluates to a blank value, the action's name is used.                    |
|                                                                               | -   Text expressions aren't supported for inline actions in summary views     |
|                                                                               |     like deck, galleries, or tables.                                          |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Action Icon                                                                   | Icon to be displayed along with the action's **Display name** (see above).    |
|                                                                               | Choose an icon from the predefined list. Custom icons are not allowed. Every  |
|                                                                               | action must have an icon. If no icon is selected, a type-specific default     |
|                                                                               | will be used.                                                                 |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

### ****Behavior

All actions have configurable behavior options that control which rows to display the action and whether or not it requires confirmation before being applied.

Configure the action behavior by using the settings defined in the following table.

|                                |                                                                        |
|--------------------------------|------------------------------------------------------------------------|
| **Setting**                    | **Description**                                                        |
| Only if this condition is true | Expression that controls which rows display the action.                |
| Needs confirmation?            | Toggle that controls whether or not the action requires confirmation.  |
| Confirmation Message           | Confirmation message to display if **Needs confirmation?** is enabled. |

### ****Documentation

Expand the **Documentation** section and enter a descriptive comment for the action that will enable collaborators to easily understand its purpose.

### Inputs

This section is available to the [Data: set the value for some columns in this row](#data-set-the-value-of-some-columns-in-this-row) data-change action only. 

You can add *inputs* to dynamically configure an action, as follows:

- When the action is used in the app, a dialog displays to prompt the app user to enter values for the specified inputs.
- When this action is invoked from a [referenced action](https://support.google.com/appsheet/answer/10107706#data-execute-an-action-on-a-set-of-rows&zippy=%2Cdata-execute-an-action-on-a-set-of-rows) (whether in the running app or in an automation), the referenced action can specify a binding expression using the input values. 
- When the action is used in the [Run a data action](https://support.google.com/appsheet/answer/11463007#zippy=%2Crun-a-data-action) step type and **Set row values** is selected, the app creator can set input values when configuring the step.

In the action, use the following expression to access the input values: `[_INPUT].[`*`inputname`*`]`

Let’s assume we want to ask the app user to provide the notes that will be saved in the `Details` column. To do so, for the Change Status action, expand the **Advanced** section and add an input value, such as **Notes**, with an initial value of **n/a**. For example:

Input configuration showing Notes defined with an initial value of n/a

Then, you can use the input value to set the value of the `Details` column by using the expression: `[_INPUT].[Notes]`

Using an input value to set a column

When the app user clicks the Change Status button, they will be prompted with a dialog that asks them to provide the details. 

Don't use nested expressions, such as `[Amount]+[_INPUT].[Amount]`. If you specify a nested expression, the user prompt won't be displayed.

For more information and examples, see [Set input values dynamically in data-change actions.](https://support.google.com/appsheet/answer/13779963)

To add inputs that can be used to dynamically configure the action:

1.  Expand the **Advanced** section.
2.  Click **Add** adjacent to the Inputs setting.
3.  Enter the name of the input value in the **Name** field.
4.  Select the data type from the **Type** drop-down.
    Only a subset of data types are supported for inputs.
5.  To add an initial value or edit any fields:
    1.  Click  to open the Input dialog.
    2.  Add a value or expression in the **Initial value** field. 
        If you don't specify an initial value, then the input value will be *required*. If an initial value is specified, then the input value is *optional*.
        Use of `[_THIS]` or `[_INPUT]` are not supported in the Initial value field.
    3.  Edit other fields, as required.
    4.  Click **Done**.
6.  Repeat to add additional input values.

## Reorder actions in your app

Reorder actions in your app. 

**Notes**: 

- The order of actions in the app editor aren't impacted; only the order of actions in your app.
- [Position settings](https://support.google.com/appsheet/answer/10107706#prominence) and [format rules](https://support.google.com/appsheet/answer/10106703) might impact the visibility of actions.

 To reorder actions in your app:

1.  Open the app in the app editor.
2.  Go to **Actions ** Actions icon .
3.  Position your cursor over the table name associated with the actions you want to reorder and click** ** Reorder items .
    The Reorder actions for *table* dialog displays.
4.  Click  to drag an action to a different order.
5.  Repeat to reorder other actions.
6.  Close the dialog.

## Add an action to your favorites

To easily access frequently used actions, add them to your favorites. 

 To add an action to your favorites:

1.  Open the app in the app editor.
2.  Go to **Actions ** Actions icon .
3.  Position your cursor over the action in the Actions panel and select **More \> Add to favorites**.

Remove an action from your favorites by positioning your cursor over the action in your favorites and clicking **x**.

## Action types

The following summarize actions that can be performed for each type.

- [Navigation action types](#navigate)
- [Data-change action types](#data-change)
- [External communication action types](#external-communication)
- [Grouped action type](#composite)

### Navigation action types

The navigation action types are listed below.

#### App: copy this row and edit the copy

Copies the current row and opens it in a form view.

#### App: edit this row

Enables users to edit a row in the current table.

When editing content on **mobile**, **tablet**, or **[legacy desktop](https://support.google.com/appsheet/answer/12407883#legacy-desktop) **devices, the content is opened in a separate form. 

Edit in form

When editing content using the **[desktop design](https://support.google.com/appsheet/answer/12407883)**, you can customize the editing experience using the **Desktop behavior **option by selecting one of the following options:

- **Edit in place**: When editing content, make all fields editable in the currently displayed detail view. 

  **Note**: At this time, **Edit in place** isn't honored when the detail view is included in a dashboard view.

  Edit action in place

   

  Consider the following when using Edit in place for the desktop browser:

  - If there are [`Show_If` conditions](https://support.google.com/appsheet/answer/10106628) that take into account the [`CONTEXT()`](https://support.google.com/appsheet/answer/10107885), the conditions may apply to desktop, or mobile and tablet devices, or both.
  - If you specify a [different column order](https://support.google.com/appsheet/answer/10107315) (by using the Column Order setting) in the form and detail views, then the two views have different functional behaviors.

&nbsp;

- **Open a form**: When editing content, edit it in a separate form. This is the default setting.

  Edit in form

#### App: export this view to a CSV file

Downloads the rows in the current view to a CSV file. This action only works on desktop browsers and not in iOS or Android apps.

Options:

- **CSV file locale**: Locale of the exported CSV file.

See the following sample templates:

- [Export CSV](https://www.appsheet.com/samples/How-to-export-data-to-csv?appGuidString=866b3f95-8d83-47a2-b015-872f0a029089)
- [Export CSV of filtered rows](https://www.appsheet.com/samples/This-app-shows-how-to-filter-your-data-using-a-form-and-export-it-to-CSV?appGuidString=1561bf63-ff85-4158-87e4-d29f7cab2c67)

To send CSV files in an email, see [Use CSV templates](https://support.google.com/appsheet/answer/11575675).

#### App: go to another AppSheet app

Opens a different AppSheet app.

Options:

- **Target**: App deep link to navigate to when the action is triggered. This can be an expression to compute the value at the time the action is triggered. This uses the same structure as the [app column type](https://support.google.com/appsheet/answer/10106757).

#### App: go to another view within this app

Navigates to another view in the current app.

Options:

- **Target**: View deep link to navigate to when the action is triggered. This can be an expression to compute the value at the time the action is triggered. This uses the same structure as the [app column type](https://support.google.com/appsheet/answer/10106757).

#### App: import a CSV file for this view

Uploads the rows in a CSV file to the current view as described in [Import a CSV file for this view](https://support.google.com/appsheet/answer/11510988).

#### App: open a form to add a new row to this table

Opens a form that enables users to add a new row to the current table.

### Data-change action types

The data-change action types are described below.

#### Data: delete this row

Deletes the current row.

#### Data: execute an action on a set of rows

This bulk action option is an expression based version of bulk select. This automated version selects the rows using an expression rather than a user, such as yourself, selecting the bulk actions using your applications user interface. 

Options:

- **Referenced Table**: Table whose action will be executed.
- **Referenced Rows**: Rows to act on from the referenced table.
- **Referenced Action**: Action to apply to the referenced rows.

See also: [`SELECT()`](https://support.google.com/appsheet/answer/10108207)

See also [Manage updates to row data by multiple bots](https://support.google.com/appsheet/answer/16136023#update-row-data-multiple-bots) for best practices.

#### Data: set the value of some columns in this row

With this action type, you can set or update the value of a field on the current row.

Options:

- **Set these columns**: Columns and values to be updated when the action is triggered. You can specify an expression to compute the value that will be run at the time the action is triggered.
- **Inputs** (under Advanced): Input values that can be set by the action. See [Advanced](#advanced) configuration.

Common uses:

- Marking a task as complete
- Updating a ticket priority
- Assigning a record to someone
- Adding or subtracting a number
- Setting a date or time to the current time
- Setting a `Lat/Long` column to [`HERE()`](https://support.google.com/appsheet/answer/10107405)

You cannot set the value of a column that:

- is the [key column](https://support.google.com/appsheet/answer/10106672)
- Contains an [App formula](https://support.google.com/appsheet/answer/10106437)
- Is a `ChangeCounter`, `ChangeLocation`, or `ChangeTimeStamp` column

Check out the [Maintenance Overview](https://www.appsheet.com/Template/AppDef?appName=MaintenanceOverview-114348-71626) app for an example.

See also [Manage updates to row data by multiple bots](https://support.google.com/appsheet/answer/16136023#update-row-data-multiple-bots) for best practices.

#### Data: add a new row to another table by using values from this row

 By creating a new action and specifying which separate table data should be added to and defining each column added, rows of data can quickly be updated and moved across all tables in your application.

Options:

- **Table to add to**: Select the table you want to add the new row to.
- **Set these columns**: Values for the columns.

The action setup shown below produces the effect of copying the `Email` and `Course` values from the current row of the student table, and using the [`TODAY()`](https://support.google.com/appsheet/answer/10108286) and [`TIMENOW()`](https://support.google.com/appsheet/answer/10107985) expressions, to log the `Email`, `Course`, current date and time as a new row in the attendance table:

Add a new row to another table

**Note**: For [desktop browsers](https://support.google.com/appsheet/answer/12407883) and the [new mobile framework (preview)](https://support.google.com/appsheet/answer/15831909), if the Row ID is specified and exists in the table to which you are adding the row, the existing content is updated. 

### External action types

The external action types are described below.

#### External: go to a website

Navigate to a URL of your choosing.

Options:

- **Target**: URL to navigate to when the action is triggered. This can be an expression to compute the URL that will be run at the time the action is triggered.
- **Launch External**: Enable to launch the web site in the device's browser and not directly in the app.

Common use case:

- Google searching a value from the row: `CONCATENATE("`[`https://google.com/search?q=`](https://google.com/search?q=)`", [Search Column Name])`

#### External: open a file

Opens a viewer for a file on the device running the AppSheet app.

Options:

- **To**: File to open. This can be an expression to compute the value at the time the action is triggered.

#### External: start an email

Opens the email app on the device running the AppSheet app. For an example, see [Click to send email](https://www.appsheet.com/template/showdef?appId=ClickToSendEmail-71626).

Options**:**

- **To**: Recipient of the email. This can be an expression to compute the value at the time the action is triggered.
- **Subject**: Subject of the email. This can be an expression to compute the value at the time the action is triggered.
- **Body**: Body of the email.

#### External: start a phone call

Opens the phone app on the device running the AppSheet app. For an example, see [Click to send email](https://www.appsheet.com/template/showdef?appId=ClickToSendEmail-71626).

Options:

- **To**: Recipient of the phone call. This can be an expression to compute the value at the time the action is triggered.

#### External: start a text message

Opens the messaging app on the device running the AppSheet app. For an example, see [Click to send email](https://www.appsheet.com/template/showdef?appId=ClickToSendEmail-71626).

Options:

- **To**: Recipient of the message. This can be an expression to compute the value at the time the action is triggered.
- **Message**: Message to send. This can be an expression to compute the value at the time the action is triggered.

### Grouped action type

The grouped action type is described below.

#### Grouped: execute a sequence of actions

Run a set of actions, one-by-one, in order. This can be used to do multiple things when an action button is pressed. 

For [desktop browsers](https://support.google.com/appsheet/answer/12407883) and [new mobile framework (preview)](https://support.google.com/appsheet/answer/15831909):

- Only one [navigation action](#navigate) or [external action](#external-communication) is executed, even if you specify more than one. It also ends the execution of the grouped action.
- [Validations rules](https://support.google.com/appsheet/answer/10107949) are enforced in each step of the grouped action.

Options:

- **Actions**: Actions to run, in order of execution.

For an example,  see the **Go to Resource** action in the [Resource Portal](https://www.appsheet.com/templates/Share-marketing-resources-and-tracking-usage) sample template.
