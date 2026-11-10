---
fonte: https://support.google.com/appsheet/answer/10105001?hl=en
baixado: 2026-11-10
---

# Connect a Zapier "ZAP" to Your App

[Zapier](https://www.zapier.com/) is a service that allows non-technical users to connect a triggering event from one service with one or more actions in other services. There are hundreds of services connected to Zapier and each connection between services is called a *Zap*.

You can use Zapier with your AppSheet applications.

- Use a webhook in an AppSheet automation to trigger Zapier Zaps as described in [Integrate with Zapier](https://support.google.com/appsheet/answer/11557001).
- Write Zapier Zaps that add, delete, find (read), or update records in AppSheet tables and invoke AppSheet [actions](https://support.google.com/appsheet/answer/10107706).

## Enable the API

To use Zapier you must enable the API for each AppSheet application you wish to access from Zapier and ensure that at least one Application Access Key has been created and is enabled for each application, as described in [Enable the API](https://support.google.com/appsheet/answer/10105769).

## Accept the AppSheet Zapier invitation

To use AppSheet from Zapier, go to the [Zapier](https://zapier.com/platform/public-invite/4368/597ae61fde8ebae08b865d92d46817be/) site and click **Accept Invite & Build a Zap**.

## Creating a Zapier "Zap"

To create a Zapier Zap, you must complete the following steps:

1.  Create a new Zapier account and sign in.
2.  Click **Make a Zap!** to create a new Zap.
3.  Give the Zap a name. On the top left, replace **Name your zap** with a Zap name of your choice.
4.  Add a trigger to the Zap.
    Your trigger can come from AppSheet or from any other trigger source that Zapier supports. [Integrate with Zapier](https://support.google.com/appsheet/answer/11557001). Alternatively, you can use a trigger from another trigger source. 
5.  Add an action to the Zap.
    Click **Add a Step** and then click **Action/Search**.
6.  Choose AppSheet as your Action App.
    In the **Choose an Action App** dialog enter **AppSheet** in the search box and press **Enter**. Select **AppSheet (2.0.3)** from the search results.
7.  Select an AppSheet action.
    Select an AppSheet action from the list of choices. For example, select **Update Record**. Then click **Save + Continue.**
8.  Select an AppSheet Account.
    - If you have already created an AppSheet account in Zapier, select it and click "Save + Continue".
    - If you do not yet created an AppSheet Account in Zapier:
      1.  Click **Connect an Account**. 
      2.  In the **Account ID** field enter your AppSheet Account Id from the AppSheet editor My Account page. 
      3.  In the **Account Access Key** field enter the **Access Key** displayed in the **My account \> Integrations \> Channels In** page.
      4.  Click **Yes, Continue** to create an AppSheet Account in Zapier.
      5.  Click **Save + Continue**.
9.  Choose the application.
    Click the down arrow in the **Application** field. This will retrieve the list of application that you enabled in step [Enable the API](#enable-api) above. Select one of the applications.
10. Choose the table.
    Click the down arrow in the **Table** field. This will retrieve the list of tables in the application you just selected. Select one of the listed tables.
11. Choose the locale.
    AppSheet will automatically select the appropriate Locale based on the table you selected.
12. Enter the location.
    If you wish, you can enter a location **Latitude** and **Longitude**.
13. Choose the timezone.
    Click the down arrow in the **Timezone** field. This will retrieve the list of all timezones. Select one of the timezones. Alternatively, you can accept the default timezone.
14. Enter key and data field values and click **Continue**.
    - If you choose **Add Record**, enter data values in all of the **required** fields. You must normally enter a data value for each of the key fields. However, if the key field contains an **Initial value**, you can omit the key field value. The system will initialize the key field to the **Initial value**. For example, you should omit the key field value when the key field has an InitialValue of [`UNIQUEID()`](https://support.google.com/appsheet/answer/10108209) or [`RANDBETWEEN()`](https://support.google.com/appsheet/answer/10107982). You can enter data values in the non-required fields if you wish.
    - If you choose **Delete Record**, enter data values in all of the key fields. Only the key fields are displayed.
    - If you choose **Find Record**, enter data values in all of the key fields. Only the key fields are displayed.
    - If you choose **Update Record**, enter data values in all of the key fields. The key fields will appear first and they will all be required. Enter data values in any fields you wish to update. Fields that you leave empty are not updated.
    - If you choose **Invoke Action**, enter data values in all of the key fields. Only the key fields are displayed. Click the down arrow in the **Action** field. This will retrieve the list of actions for the table. Select one of the actions.
15. Test the Zap.
    To test your action, click **Send Test to AppSheet**. The resulting table row will be displayed. You can use the data values from the returned row can be used in subsequent Actions.  
16. If the test is successful, click **Finish**.
17. Turn on Your Zap.
    Click **Your Zap is** to turn on your Zap.

## Troubleshoot Zapier API calls

If your Zapier API calls are failing start by checking Audit History.

1.  Go to the **Manage \> Monitor \> Audit History** pane and click **Launch log analyzer**.
2.  You will see a series of checkboxes that allow you to select which types of Audit History records are displayed. Select only **REST API**. Zapier calls the REST API when adding and updating records.
3.  You may wish to specify **Start at** and **End at** (in UTC time). and **Only Display Failures** to narrow the search.
