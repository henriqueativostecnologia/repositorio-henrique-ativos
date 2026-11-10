---
fonte: https://support.google.com/appsheet/answer/16556501?hl=en
baixado: 2026-11-10
---

# Invoke an Application Integration connection from a webhook

Invoke an Application Integration connection from a webhook by doing the following:

1.  Create a secret with a randomly generated value to use as an API key for the webhook, and store it using the [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets). To generate the secret, you can use the `openssl` CLI command or another preferred method. For example: 

    `openssl rand -base64 32`
     

2.  Configure a webhook connection in Integration Connectors, as described in [Webhook](https://cloud.google.com/integration-connectors/docs/connectors/webhook/configure). This can be re-used for multiple AppSheet automations and Application Integration integrations.

    When configuring the **Webhook** (preview) connection, use the following recommended values:
     

    |                           |                                           |
|---------------------------|-------------------------------------------|
| **Setting**               | **Value**                                 |
| Listener Authentication   | **API Key Authentication**                |
| API key field location    | **Header**                                |
| API key field name        | **Api-Key**^(**\***)                      |
| API Key                   | Value of ***secret*** generated in step 1 |
| Event type field location | **Header**                                |
| Event type field name     | **Event-Type**^(**\***)                   |

    **^(\*)** This value is used in the AppSheet configuration, later

3.  Using Application Integration, create a new integration and add a webhook trigger, as described in [Webhook trigger](https://cloud.google.com/application-integration/docs/configure-webhook-trigger).

    When configuring the **Webhook** (preview) trigger, do the following recommended steps:
    1.  Set the **Custom Event Type ID** to the webhook trigger name, such as **AppSheetEvent**.
        This value identifies this specific integration. Different values can be used to use the same webhook connection for multiple integrations. 
    2.  Configure any desired tasks in the integration. For example, **Send Email** with the body of **ConnectorEventPayload_1** variable. See [Variables](https://docs.cloud.google.com/application-integration/docs/variables).
    3.  Publish the integration.

4.  Create or open an AppSheet app in the AppSheet editor.

5.  Create an automation and add the **Call a webhook **task, as described in [Add a task to a bot](https://support.google.com/appsheet/answer/11445301#add-task).

6.  Configure the **Call a webhook** task as described in the following table. For more information about the configuration settings, see [Call a webhook from a bot](https://support.google.com/appsheet/answer/11511244). 
     

    +-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Preset                                                                        | Select **Custom**.                                                            |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| URL                                                                           | Copy and paste the value of **Events listener endpoint** for the Integration  |
|                                                                               | Connectors connection created in step 2.                                      |
|                                                                               |                                                                               |
|                                                                               | For example:                                                                  |
|                                                                               |                                                                               |
|                                                                               |     https://service-abcd-efgh-1234.a.run.app/v1/projects/appshee              |
|                                                                               | t-appint/locations/us-central1/connections/appsheet-appint-apikey:listenEvent |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| HTTP Verb                                                                     | Select **Post**.                                                              |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| HTTP Content Type                                                             | Select **JSON**.                                                              |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Body                                                                          | Enter the command or data to send to the webhook. This is the JSON value that |
|                                                                               | will be set to the output variable from the trigger in the integration. You   |
|                                                                               | can use AppSheet                                                              |
|                                                                               | [expressions](https://support.google.com/appsheet/answer/10104642) here.      |
|                                                                               |                                                                               |
|                                                                               | For example:\                                                                 |
|                                                                               | `{`\                                                                          |
|                                                                               | `     "first_name":"<<[FirstName]>>",`\                                       |
|                                                                               | `     "email":"<<[Email]>>",`\                                                |
|                                                                               | `     "language":"<<[Preferred Language]>>"`\                                 |
|                                                                               | `}`                                                                           |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| HTTP Headers                                                                  | Click **Add** to add the following API headers:                               |
|                                                                               |                                                                               |
|                                                                               | -   `Api-Key: <api-key-value>`\                                               |
|                                                                               |     Where `Api-Key` is set to the **API key field name** value configured     |
|                                                                               |     in Step 2, and `<api-key-value>` is set to the secret value from step 1.\ |
|                                                                               |     **Note**: AppSheet currently can't retrieve the secret value              |
|                                                                               |     automatically.` `                                                         |
|                                                                               |                                                                               |
|                                                                               | -   `Event-Type: <webhook-trigger-name>`\                                     |
|                                                                               |     Where `Event-Type` matches the **Event type field name** value configured |
|                                                                               |     in Step 2, and `<webhook-trigger-name>` is set to the **Custom Event Type |
|                                                                               |     ID** value in step 3.                                                     |
|                                                                               |                                                                               |
|                                                                               | For example:\                                                                 |
|                                                                               | `Api-Key: 1234abcd5678`\                                                      |
|                                                                               | `Event-Type: AppSheetEvent`                                                   |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

7.  Save the app.
