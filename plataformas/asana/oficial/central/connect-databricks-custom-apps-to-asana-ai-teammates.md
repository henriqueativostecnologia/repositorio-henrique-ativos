---
fonte: https://help.asana.com/s/article/connect-databricks-custom-apps-to-asana-ai-teammates?language=en_US
baixado: 2026-11-10
---

# Connect Databricks custom apps to Asana AI Teammates

Asana AI Teammates can connect to Databricks through [custom MCP apps](https://help.asana.com/s/article/create-custom-mcp-apps-for-ai-teammates). After an admin configures the connection, you can ask an AI teammate questions about your Databricks data without leaving Asana.

## Configure Asana as an external app in Databricks

A Databricks admin must first create an OAuth app connection for Asana.

In Databricks, go to **Settings** and select **App connections**. Select **Add connection**, name the app, and enter this redirect URL:

[https://app.asana.com/-/integrations/oauth/callback](https://app.asana.com/-/integrations/oauth/callback)

Grant the Genie scope, generate a client secret, and copy the client ID and client secret. Store the client secret securely because it cannot be retrieved later. For more information, refer to [Databricks documentation](https://docs.databricks.com/aws/en/agents/mcp-tools/connect-clients) about connecting external services.

## Create the Databricks app in Asana

An Asana admin needs to create a custom app named **Databricks** in Asana by following the [Custom MCP Connection article](https://help.asana.com/s/article/create-custom-mcp-apps-for-ai-teammates).

When prompted, provide the MCP server URL, client ID, and client secret from the Databricks setup. Confirm the server URL and required OAuth details with your Databricks admin before saving the app.

## Add Databricks to an AI teammate

After the **Databricks** custom app is distributed to your organization, users can add it to their AI teammate.

Each user authorizes the app with their own OAuth grant. OAuth tokens are not shared between users, and each user must have access to Databricks. This keeps queries scoped to the permissions of the person who authorized the connection.

## Use Databricks with an AI teammate

After the connection is authorized, you can ask an AI teammate questions using data available through the connected Databricks MCP server. The full list of Databricks-managed MCP servers is available in Databricks documentation.

For example, Databricks Genie One lets you ask complex data questions in plain English and receive tables, charts, or drafts without writing SQL.

You can use an AI teammate with Genie One to discover dashboards for tracking new user adoption, answer revenue questions for a quarterly business review, or retrieve marketing results such as MQLs by region for a campaign retrospective. The results can remain in the Asana project with the related briefs, decisions, and next steps.
