---
fonte: https://support.google.com/appsheet/answer/10104716?hl=en
baixado: 2026-11-10
---

# Example: Copy newly added records

You can use a webhook and the API to copy newly added records from one table to another.

This example uses two identical tables called `People` and `PeopleEcho`.  Both tables contains four identical fields named `Name`, `Age`, `DropDown`, and `Count`. Admittedly this example is simple and contrived, but it illustrates how you can use the same approach in more complex cases.

Every time a new record is added to the `People` table, the webhook is triggered. The webhook uses the API to add an identical record into the `PeopleEcho` table.

To copy newly added records:

1.  [Enable the API.](https://support.google.com/appsheet/answer/10105769)

2.  Go to Automation section and create an automation bot with a webhook task and configure the following properties:

    - **Target data** property choose the **People** table.

    - **Update event **property choose **ADDS_ONLY**.

    - **Url** property enter: 
      **https://www.appsheet.com/api/v2/apps/ad178014-1282-4055-bf14-505e31c90c73/tables/PeopleEcho/Action**

      Where the app ID following `apps/` is the app ID from the **Manage \> Integrations \> IN** pane and the value following `tables/` is the name of the target table. In this case, `PeopleEcho`.

    - **HTTP Verb** property enter **Post**.

    - **HTTP Headers** property enter: **applicationAccessKey: "C2iXO-RjfVq-PmcLy-d7nil-YiLvt-BCAYy-C04LY-Ynt0q"**

      Where the access key value is the **Access Key** from the **Manage \> Integrations \> IN** pane. The **Access Key** must be enclosed in quotes. For more informations, see [Specify application access key when invoking from a webhook](https://support.google.com/appsheet/answer/10105398#application-access-key-webhook).

3.  Create a JSON Body Template that looks like the one below.

    This JSON Body Template copies the value of the `Name` field of table `People` to the `Name` field of table `PeopleEcho`. Ditto for the other three fields.

    This example, is simply copying the entire record from `People` to `PeopleEcho` but you could do other things. You could copy a subset of the fields. You could initialize the fields of the new record using constants or expressions. 

&nbsp;

    {
      "Action": "Add",
      "Properties": {
       "Locale": "en-US",
       "Location": "47.623098, -122.330184",
       "Timezone": "Pacific Standard Time",
       "UserSettings": {
          "Option 1": "value1",
          "Option 2": "value2"
       }
      },
      "Rows": [
        {
          "Name": "<<[Name]>>",
          "Age": "<<[Age]>>",
          "DropDown": "<<[DropDown]>>",
          "Count": "<<[Count]>>"
        }
      ]
    }

### Create the JSON body template

If you click the **Create** button following the **JSON Body Template** property, AppSheet will create an initial JSON Body Template which you can then modify. The template is based on the fields of the table you specify in the **Target data** property.

The following technique can simplify template creation.

1.  Temporarily change the **Target data** property to the table you want to use for the template.
2.  Click **Save** to save the temporary change.
3.  Click **Create** to create the template.
4.  Restore the **Target data** property to its original value.
5.  Click **Save** to save all changes.

### Troubleshoot your webhook and API

- To troubleshoot your webhook, see [Troubleshoot webhooks](https://support.google.com/appsheet/answer/11562141).
- To troubleshoot your API, see [Troubleshoot API calls](https://support.google.com/appsheet/answer/10104718).
