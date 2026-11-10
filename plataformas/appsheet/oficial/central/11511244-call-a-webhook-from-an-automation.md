---
fonte: https://support.google.com/appsheet/answer/11511244?hl=en
baixado: 2026-11-10
---

# Call a webhook from an automation

Call a webhook from an automation bot as described in the following sections:

- [Add and configure the task](#add-configure)
- [Specify the HTTP Basic Authentication header](#specify-http-basic-auth-header)

 

**For AppSheet Core accounts**: If you receive a `Workspace AppSheet Core security violation` error, then the use of this feature is not allowed by policy, as described in [Control access to AppSheet](https://support.google.com/a/answer/16018438). Contact your Workspace administrator for assistance.

## Add and configure the Call a webhook task

Add and configure the **Call a webhook** task by performing the following steps:

1.  Add the **Call a webhook **task to a bot, as described in [Add a task to a bot](https://support.google.com/appsheet/answer/11445301#add-task).
2.  Configure the **Call a webhook** task by setting the properties described in the following tables.
3.  When you are done, save the app by selecting one of the following:
    - **Save** - Save the app.
    - **Save & verify data** - Save the app and verify that it is runnable based on external dependencies.

After you save the app, you can reuse task in other bots.

Configure the **Call a webhook** task by using the settings described in the following tables.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Linking                                                                       |                                                                               |
|                                                                               |                                                                               |
|                                                                               | Enable or disable the reuse of this component by expanding the **Linking**    |
|                                                                               | panel and toggling the **Linking** setting. See [Reuse automation             |
|                                                                               | components](https://support.google.com/appsheet/answer/12193489).\            |
|                                                                               | \                                                                             |
|                                                                               | Expand the Linking panel and toggle the Linking setting to enable or disable  |
|                                                                               | component reuse                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Task name                                                                     | Name of the task. It must be unique within your app.                          |
|                                                                               |                                                                               |
|                                                                               | **Note**: This setting is available only if **Linking** is turned on.         |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Table name                                                                    | Table defined in the                                                          |
|                                                                               | [event](https://support.google.com/appsheet/answer/11445188) and used by the  |
|                                                                               | task.                                                                         |
|                                                                               |                                                                               |
|                                                                               | To view or edit the structure of the selected table, position your cursor in  |
|                                                                               | the field and click Edit icon  . See [Tables: The                             |
|                                                                               | Essentials](https://support.google.com/appsheet/answer/10105821) for more     |
|                                                                               | information.                                                                  |
|                                                                               |                                                                               |
|                                                                               | **Note**: To use a table that is different from the table defined in the      |
|                                                                               | event, add a [Call a                                                          |
|                                                                               | process](https://s                                                            |
|                                                                               | upport.google.com/appsheet/answer/11463007#step-type&zippy=%2Ccall-a-process) |
|                                                                               | step.                                                                         |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Preset                                                                        | Customize all settings or select a preset to pre-populate a subset of values. |
|                                                                               |                                                                               |
|                                                                               | Valid values include:                                                         |
|                                                                               |                                                                               |
|                                                                               | -   **Custom** - Set all configuration values manually. This is the default.  |
|                                                                               | -   **Slack Hook** - Pre-populate values for a Slack webhook.                 |
|                                                                               | -   **AppSheet API** - Pre-populate values for the AppSheet API.              |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Url                                                                           | URL of the web service for the HTTP request. The URL must be absolute and may |
|                                                                               | include text,                                                                 |
|                                                                               | [variables](https://support.google.com/appsheet/answer/11539253), and         |
|                                                                               | [expressions](https://support.google.com/appsheet/answer/10104642).           |
|                                                                               |                                                                               |
|                                                                               | **Note**: Redirects are not supported for webhooks.                           |
|                                                                               |                                                                               |
|                                                                               | For example:                                                                  |
|                                                                               |                                                                               |
|                                                                               |                                                                               |
|                                                                               |  https://api.webservice.com/add/table/<<[Table Name]>>/id/<<[Record Id] + 1>> |
|                                                                               |                                                                               |
|                                                                               | \                                                                             |
|                                                                               | If you are using the webhook to invoke the AppSheet API, enter the webhook    |
|                                                                               | URL value in the following form:\                                             |
|                                                                               | `https://api.appsheet.com/api/v2/apps/{appId}/...`\                           |
|                                                                               | `    tables/{tableName}/Action`                                               |
|                                                                               |                                                                               |
|                                                                               | Where:                                                                        |
|                                                                               |                                                                               |
|                                                                               | -   `{appId}` specifies the GUID of the AppSheet application. You can obtain  |
|                                                                               |     the `{appId}` from the **Manage \> Integrations \> IN** pane.             |
|                                                                               | -   `{tableName}` specifies the name of the table.                            |
|                                                                               |                                                                               |
|                                                                               | While the app is in test mode (that is, it has not passed a [deployment       |
|                                                                               | check](https://support.google.com/appsheet/answer/10104389)), the webhook can |
|                                                                               | be invoked. This allows you to test your webhook before your application is   |
|                                                                               | deployed.                                                                     |
|                                                                               |                                                                               |
|                                                                               | **Note**: This setting is available only when **Preset** is set to            |
|                                                                               | **Custom** or **Slack Hook**.                                                 |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| HTTP Verb                                                                     | HTTP verb used to call the web service. Select a value from the list. Valid   |
|                                                                               | values include Delete, Get Patch, Post (most common), and Put.                |
|                                                                               |                                                                               |
|                                                                               | **Note**: This setting is available only when **Preset** is set to            |
|                                                                               | **Custom**.                                                                   |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| HTTP Content Type                                                             | Content type of the body. Valid content type values include:                  |
|                                                                               |                                                                               |
|                                                                               | -   CSV                                                                       |
|                                                                               | -   FORM_URL_ENCODED                                                          |
|                                                                               | -   HTML                                                                      |
|                                                                               | -   ICS_Calendar                                                              |
|                                                                               | -   JSON                                                                      |
|                                                                               | -   PDF                                                                       |
|                                                                               | -   XLSX (Microsoft Excel)                                                    |
|                                                                               | -   XML                                                                       |
|                                                                               |                                                                               |
|                                                                               | Defaults to JSON.                                                             |
|                                                                               |                                                                               |
|                                                                               | **Note**: This setting is available only when **Preset** is set to            |
|                                                                               | **Custom**.                                                                   |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| App Id                                                                        | ID of app to send the request to. Defaults to the ID of the current app.      |
|                                                                               |                                                                               |
|                                                                               | **Note**: This setting is available only when **Preset** is set to **AppSheet |
|                                                                               | API**.                                                                        |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Target Table Name                                                             | Name of the target table in the app to send the request to.                   |
|                                                                               |                                                                               |
|                                                                               | See [Tables: The                                                              |
|                                                                               | Essentials](https://support.google.com/appsheet/answer/10105821) for more     |
|                                                                               | information about adding tables.                                              |
|                                                                               |                                                                               |
|                                                                               | **Note**: This setting is available only when **Preset** is set to **AppSheet |
|                                                                               | API**.                                                                        |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Body                                                                          | Body containing the command or data to send to the webhook.                   |
|                                                                               |                                                                               |
|                                                                               | To define the body, do **one** of the following:                              |
|                                                                               |                                                                               |
|                                                                               | -   Enter the webhook body in this setting, including text, images,           |
|                                                                               |     [variables](https://support.google.com/appsheet/answer/11539253), and     |
|                                                                               |     [expressions](https://support.google.com/appsheet/answer/10104642).       |
|                                                                               | -   Leave this setting blank and specify an **Body Template** (see below).    |
|                                                                               | -   Leave this setting and **Body Template** setting blank to use the default |
|                                                                               |     content.                                                                  |
|                                                                               |                                                                               |
|                                                                               | **Note**:                                                                     |
|                                                                               |                                                                               |
|                                                                               | -   To access a user setting, use `ANY(_Per user Settings[Column])` in the    |
|                                                                               |     JSON body of the webhook task. Don't                                      |
|                                                                               |     speci                                                                     |
|                                                                               | fy [`USERSETTINGS()`](https://support.google.com/appsheet/answer/10108291) in |
|                                                                               |     the JSON body of a webhook task; it is not supported at this time.        |
|                                                                               |                                                                               |
|                                                                               | -   The **Body Template** setting (if specified) takes precedence over this   |
|                                                                               |     setting.                                                                  |
|                                                                               |                                                                               |
|                                                                               | Defaults to data values from the added or updated row, excluding `Hidden` or  |
|                                                                               | `Show` type columns.                                                          |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| HTTP Headers                                                                  | List of HTTP headers that are included in the HTTP request.                   |
|                                                                               |                                                                               |
|                                                                               | It is common to include an `Authentication` header that contains              |
|                                                                               | authentication information such as authentication token or a username and     |
|                                                                               | password. See [Specify the HTTP Basic Authentication                          |
|                                                                               | header](#specify-http-basic-auth-header).                                     |
|                                                                               |                                                                               |
|                                                                               | Click **Add** to add an HTTP header using the following format:               |
|                                                                               |                                                                               |
|                                                                               | `<header>: <value>` Repeat to add additional HTTP headers.                    |
|                                                                               |                                                                               |
|                                                                               | The header name and header value may include constants or AppSheet            |
|                                                                               | [expressions](https://support.google.com/appsheet/answer/10104642). The       |
|                                                                               | expression result will replace the expression in the HTTP header.             |
|                                                                               |                                                                               |
|                                                                               | If the header value contains quote characters, you must enclose the entire    |
|                                                                               | header value within quotes, and escape each embedded quote with two quotes.   |
|                                                                               | For example, if the header name is `Authorization` and the header value is    |
|                                                                               | `Token token="537d7d"`, you should enter                                      |
|                                                                               | `Authorization: "Token token=""537d7d"""` in the header line.                 |
|                                                                               |                                                                               |
|                                                                               | By default, AppSheet sets the `Content-Type` header as follows:               |
|                                                                               | `Content-Type: "application/json"`                                            |
|                                                                               |                                                                               |
|                                                                               | **Example**:                                                                  |
|                                                                               |                                                                               |
|                                                                               | When invoking Pushpad from a webhook, you might need to include the following |
|                                                                               | header values:                                                                |
|                                                                               |                                                                               |
|                                                                               | -   `Authorization: "Token token=""9474e7df4ba7c96a06"""`                     |
|                                                                               | -   `Accept: "application/json"`                                              |
|                                                                               |                                                                               |
|                                                                               | **Note**: This setting is only available when **Preset** is set to **Custom** |
|                                                                               | or **AppSheet API**.                                                          |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Body Template                                                                 | Template to use for more precise control of the webhook body. See [Use        |
|                                                                               | templates in a bot](https://support.google.com/appsheet/answer/11539957) and  |
|                                                                               | the **Body** setting description (above).                                     |
|                                                                               |                                                                               |
|                                                                               | **Note**: This setting is only available when **Preset** is set to **Custom** |
|                                                                               | or **AppSheet API**.                                                          |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Body Template Data Source                                                     | Data source used for the body template.                                       |
|                                                                               |                                                                               |
|                                                                               | **Note**: This setting is only available when **Preset** is set to **Custom** |
|                                                                               | or **AppSheet API**.                                                          |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Return value                                                                  | Enable this toggle to capture the return values from web service              |
|                                                                               | call. See[ Use return values from                                             |
|                                                                               | webhooks](https://support.google.com/appsheet/answer/12738438).               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Specific types                                                                | Enable this toggle to capture the return values from web service              |
|                                                                               | call. See[ Use return values from                                             |
|                                                                               | webhooks](https://support.google.com/appsheet/answer/12738438).               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Timeout                                                                       | Number of seconds AppSheet should wait for the webhook to complete before     |
|                                                                               | timing out. Defaults to 180.                                                  |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Max number of retries on failure                                              | Maximum number of times to retry the webhook in the event of failure.         |
|                                                                               | Defaults to 3.                                                                |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Run asynchronously                                                            | Toggle that specifies whether AppSheet runs asynchronously as a background    |
|                                                                               | task. Invoking the webhook asynchronously can improve client response time.   |
|                                                                               |                                                                               |
|                                                                               | Before setting this setting, consider whether your application requires the   |
|                                                                               | webhook to complete synchronously to execute correctly. For example, if your  |
|                                                                               | webhook is changing data and your application relies on that data being       |
|                                                                               | updated before the sync completes, then using an asynchronous call may yield  |
|                                                                               | incorrect results.                                                            |
|                                                                               |                                                                               |
|                                                                               | By default, the setting is disabled.                                          |
|                                                                               |                                                                               |
|                                                                               | **Note**: This setting is available only when **Return value** is turned off. |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

 Expand and customize the **Advanced** settings, as described below.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Inputs                                                                        | Add inputs to dynamically configure a task. For details, see [Set input       |
|                                                                               | values dynamically in                                                         |
|                                                                               | tasks](https:                                                                 |
|                                                                               | //support.google.com/appsheet/answer/11445301#set-input-values-dynamically).  |
|                                                                               |                                                                               |
|                                                                               | 1.  Expand the **Advanced** section.                                          |
|                                                                               | 2.  Click **Add** under Inputs.                                               |
|                                                                               | 3.  Enter the name of the input value in the **Name** field.                  |
|                                                                               | 4.  Select the data type from the **Type** drop-down.\                        |
|                                                                               |     Only a subset of data types are supported for inputs.                     |
|                                                                               | 5.  To add an initial value or edit any fields:                               |
|                                                                               |     1.  Click  to open the Input dialog.                                      |
|                                                                               |     2.  Add a value or expression in the **Initial value** field.\            |
|                                                                               |         If you don't specify an initial value, then the input value will be   |
|                                                                               |         required. If an initial value is specified, then the input value is   |
|                                                                               |         optional.                                                             |
|                                                                               |         Use of `[_THIS]` or `[_INPUT]` are not supported in the Initial value |
|                                                                               |         field.                                                                |
|                                                                               |     3.  Edit other fields, as required.                                       |
|                                                                               |     4.  Click **Done**.                                                       |
|                                                                               | 6.  Repeat to add additional input values.                                    |
|                                                                               |                                                                               |
|                                                                               | Then, use the following expressions to access the input values from the       |
|                                                                               | current step: `[_INPUT].[`*`inputname`*`]`                                    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

## Specify the HTTP Basic Authentication header

You can specify an HTTP Basic Authentication header as follows.

- Header name: `Authorization` 
- Header value: `Basic <base64-encoded authentication value>`

When invoking Twilio, you must specify your Twilio Account SID, followed by a colon, followed by your Twilio Auth Token in the form:
`<TwilioAccountSID>:<TwilioAuthToken>`

**Example**:

If your Twilio Account SID is `BDe8de733fd2363d6d0d86719f6ad324db` and your Twilio Auth Token is `5c3a028974b570eebc48fc4de2a5f567`, the resulting **authentication value** is:
`BDe8de733fd2363d6d0d86719f6ad324db:5c3a028974b570eebc48fc4de2a5f567`

When this value is **Base64 UTF-8** encoded using a web service like [Base64Encode.org](https://www.base64encode.org/) it yields the value:

    QkRlOGRlNzMzZmQyMzYzZDZkMGQ4NjcxOWY2YWQzMjRkYjo1YzNhMDI4OTc0YjU3MGVlYmM0OGZjNGRlMmE1ZjU2Nw==

The resulting header value is:

    Basic QkRlOGRlNzMzZmQyMzYzZDZkMGQ4NjcxOWY2YWQzMjRkYjo1YzNhMDI4OTc0YjU3MGVlYm
    M0OGZjNGRlMmE1ZjU2Nw==
