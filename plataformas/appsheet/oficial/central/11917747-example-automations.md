---
fonte: https://support.google.com/appsheet/answer/11917747?hl=en
baixado: 2026-11-10
---

# Example automations

The following examples illustrate some of the ways you can define tasks that can be triggered by app events. See the [ClickToSendEmail](https://www.appsheet.com/Template/AppDef?appName=ClickToSendEmail-71626)sample app to see some of these examples.

## Send email when a row is added, updated, or deleted

You can create an event that sends a email when a row is added, updated, or deleted. For example, you might send an email each time an `Order` is added or updated. 

The `ServiceRequests` table and the `On Add in ServiceRequests_Action1` task illustrate how to send an email each time a new `Service Request` is created. For example:

1.  The `ServiceRequests` table contains the customer's name in column `Name`, the customer's email address in the `Email` column, and an `Enum` value that indicates whether the service request is `Pending`, `Active`, or `Completed`.

2.  The `On Add in ServiceRequests_Action1` task can be triggered on the AppSheet backend service each time a new row is added to the `ServiceRequests` table. It can then generate an email and send it to the email address contains in the `Email` column.

## Send email when a row is updated to have a specific column value

You can create an event that sends an email when a row is updated to have a specific column value. For example, you might send an email when the `Status` column in the `ServiceRequests` row is updated to contain the value `Active`.

    AND(
      ("Active" = [_THISROW_AFTER].[Status]),
      ([_THISROW_AFTER].[Status] <> [_THISROW_BEFORE].[Status])
    )

In this expression, note the use of [`[_THISROW_BEFORE]` and `[_THISROW_AFTER]`](https://support.google.com/appsheet/answer/11547057). These are system-provided [references](https://support.google.com/appsheet/answer/10106510) that refer to the state of the row before and after the change was made, respectively. This is really useful in order to check if the value of a field changed from one value to another.

Because `[_THISROW_BEFORE]` and `[_THISROW_AFTER]` are references, you use [a dereference expression](https://support.google.com/appsheet/answer/10107396) to access the value of a specific column in the referenced row.

## Send email when a row is updated to have two or more specific column values

The `ServiceRequests` table and the `On Change in ServiceRequests_Action1` task illustrate how to [send an email](https://support.google.com/appsheet/answer/11447614) when a new service request is in `Active` state and all needed parts are in hand. For example:

1.  The `ServiceRequests` table contains the customer's name in column `Name`, the customer's email address in column `Email`, an `Enum` column that indicates whether the service request is `Pending`, `Active`, or `Completed`, and a `Yes/No` column that indicates whether parts are on order.  

2.  The `On Change in ServiceRequests_Action1` task can be triggered on the AppSheet backend service each time a row in the `ServiceRequests` table is updated. For example, the following expression sends email to the email address in the `Email` column when either the `Status` or `PartsOnOrder` columns are changed, the `Status` is `Active`, and there are no `PartsOnOrder`. By checking whether `Status` or `PartsOnOrder` have just changed, we avoid sending email when some other column in the row has changed that is irrelevant to whether the service request is being worked on.

&nbsp;

    AND(
      ("Active" = [_THISROW_AFTER].[Status]),
      NOT([_THISROW_AFTER].[PartsOnOrder]),
      OR(
        ("Active" <> [_THISROW_BEFORE].[Status]),
        [_THISROW_BEFORE].[PartsOnOrder]
      )
    )

## Send email that includes file attachments

You can create an event that allows the user to control the file attachments appended to the email. For example, you might have a brochure for each product you offer. Each brochure might reside in its own PDF file. The customer could select which products they are interested in and you could attach the appropriate PDF file for each product to the email.

The `Customers` table and the `On Change in Customers_Action1` task illustrate how to send an email that includes one or more file attachments selected dynamically by the client. For example, the app user can select the images or PDF documents to include with the email by selecting values from an `EnumList`. For example:

1.  The `Customers` table contains the customer's name in column `Name`, the customer's email address in column `Email`, and an `EnumList` of potential email attachments in column `Attachments`.

2.  When the user edits a row in the `Customers` table they can select one or more values from the `Attachments` `EnumList`. In our case, the user can select `Apple`, `Banana`, or `Orange`, or any combination of the three. When `Apple` is selected, the file `Apple.pdf` is included as an email attachment. Likewise for `Banana` and `Orange`. The user selected values are stored in the `Attachments` field of the `Customers` row.

3.  The `On Change in Customers_Action1` task can be triggered on the AppSheet backend service each time the `Customers` table is updated. For example, the following expression determines if column `Attachments` has a value and if its value has changed. If so, it sends email to the email address contained in the `Email` column.

&nbsp;

    AND(
      ISNOTBLANK([_THISROW_AFTER].[Attachments]),
      ([_THISROW_AFTER].[Attachments] <> [_THISROW_BEFORE].[Attachments])
    )

 

The event can determine which PDF files to attach to the email using the following expression:

    <<IFS(IN("Apple", [Attachments]), {"Apple.pdf"}) + IFS(IN("Banana", [Attachments]), {"Banana.pdf"}) + IFS(IN("Orange", [Attachments]), {"Orange.pdf"})>>

 

The `Apple.pdf`, `Banana.pdf`, and `Orange.pdf` files must reside on the server in the application folder. 

## Send an email from an Action button

You can use an [action button](https://support.google.com/appsheet/answer/10107706) on the app to perform a data change. As a result, a single click of an action button in the app can trigger a customized email message that is sent to one or more recipients by the AppSheet backend service. You can label the action button to make it clear that an email will be sent when the action button is clicked.

The `Orders` table and the `On Change in Orders_Action1` task can be used to send email from an action button. For example:

1.  The `Orders` table includes the email column `Email` and the numeric column `EmailsSent`.

2.  When the user is viewing a row in the `Orders` table, they can click the **Email This Order** action button. That increments the value in column `EmailsSent`.

3.  The `On Change in Orders_Action1` task can be triggered on the AppSheet backend service each time the `Orders` table is updated. For example, the following expression determines if column `EmailsSent` has changed. If so, it generates an email and sends it to the email address contains in column `Email`.

&nbsp;

    AND(
      ISNOTBLANK([_THISROW_AFTER].[EmailsSent]),
      ([_THISROW_AFTER].[EmailsSent] <> [_THISROW_BEFORE].[EmailsSent])
    )

### Choose and send a report from a list of reports

The `Reports` table and the `ReportOpenOrders_Action1` and `ReportActiveServiceRequests_Action1` tasks can be used to choose and send a report from a list of reports. For example:

1.  The `Reports` table contains a list of reports each of which has a report name and description.
2.  A user can go to the menu, select the `Reports` view, choose a report from the list of Reports, and click the **Create** action to trigger the selected report.
3.  The **Create** action updates the value in the `LastRun` `DateTime` field of the chosen `Reports` record.
4.  The `Reports` record update triggers either the `ReportOpenOrders_Action1` and `ReportActiveServiceRequests_Action1` task depending on the `Name` contained in the `Reports` record.
5.  The event generates a report and sends it to the appropriate email recipients.

### Send an email only after adding a parent record and all of its children

When you add a parent record along with one or more child records, AppSheet first adds the parent record followed by each of the child records. This can make it difficult to trigger an automation only after all of the child records have been added. 

You can can use the following technique to ensure that all parent and child records are added before the automation runs.

This technique uses a `Form Saved` event to trigger a data-change action which triggers the task only after the child records have been added.

For example:

1.  The child table must contain a `Ref` field to the parent table. Set the **Is a part of **property of the `Ref` field to **On**. This makes it possible to add child records when the parent record is added.

2.  Add a `Text` field to the parent table. Call the field `Status` and set its **Initial value** property to **`""`** (blank). The `Status` column controls whether the event fires.

3.  Create a Data Change action for the parent table which sets the `Status` column's value to **`"Run"`**.

4.  Create a second Data Change action for the parent table which sets the `Status` column's value to **`""`** (blank).

5.  Create a Composite Action for the parent table that invokes the two Data Change actions above. This Composite Action invokes the first Data Change action to set the `Status` column's value to `"Run"`, and the second Data Change action to set the `Status` column's value to blank. These two Data Changes will be sent to the server as separate updates. The first update fires the event, while the second update prevents further updates from firing the event.

6.  Go to the **UX \> Views** tab. Click **Show system views**. Select the form for the parent table. Expand **Behavior**. Find **Event Actions** and set its **Form Saved** property to the Data Composite action created in the previous step.

7.  Set your event's **Event Type** property to **Updates only**. Set its **Condition** property to:

&nbsp;

    [Status] = "Run"

## Maintain per user settings

You can maintain "per user" settings. For example, you might want to allow each user to specify whether they prefer to receive an email or an SMS when a workflow is triggered.

You can store the settings as follows:

1.  Create a new table having one record per user. Each record will contain that user's settings. You might call the table `Automation Settings`.

2.  Create a slice on the  `Automation Settings` table so that each user "sees" only their own settings row. You might call the slice `Automation Settings Slice`. You cannot use a security filter because then one user's settings would not be visible to the other user's event.

3.  Create a view that allows each user to update the settings in their `Automation Settings Slice`.

You can use the preferences as follows:

1.  In your event, check the preferences contained in the `Automation Settings Slice` for the current user to control what action is taken.

For example, if you wish to allow each user to specify whether they prefer to receive an email or an SMS when a workflow is triggered, do the following:

1.  Define both an Email and an SMS event.

2.  In the Email event **Condition** property, check whether the current user wishes to receive an email. In the SMS event **Condition** property, check whether the current user wishes to receive an SMS.

## Invoke other actions

We have described how to send email, SMS, and notifications from the app. However, you can invoke any event-triggered task from the app using this approach. For example, you could invoke a task that uses a web hook to invoke an external web service.
