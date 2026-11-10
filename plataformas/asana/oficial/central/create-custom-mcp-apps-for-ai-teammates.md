---
fonte: https://help.asana.com/s/article/create-custom-mcp-apps-for-ai-teammates?language=en_US
baixado: 2026-11-10
---

# Create custom MCP apps for AI Teammates

Custom MCP apps connect Asana AI Teammates to external MCP servers. Organization admins or developers can create an app in the Asana developer console, configure its external app connection method, distribute it to internal workspaces, and make it available for AI Teammate users.

> Find here how to set this up with [Salesforce](https://help.asana.com/s/article/connect-salesforce-to-ai-teammates-with-a-custom-mcp-app) and [Databricks](https://help.asana.com/s/article/connect-databricks-custom-apps-to-asana-ai-teammates) MCP servers. 

## Supported MCP servers

You can create a custom MCP app when the external MCP server meets all of these requirements:

1.  The external app permits MCP usage, typically through an admin setting.
2.  The external app supports OAuth 2.0. Custom MCP apps do not currently support bearer tokens, basic authentication, or custom headers.
3.  The external app lets you register a client app and provides a client ID, client secret, authorization URL, and token exchange URL. Dynamic client registration and client metadata documents are not currently supported.

## Create a custom MCP app

### Create the app in Asana

1.  Open the Asana developer console and go to **My apps**.
2.  Click **New app**.
3.  Enter an app name and select **External MCP** as the app type.
4.  Agree to the Asana API Terms, then click **Create**.

 

5.  On the configuration page, upload an app icon and enter a brief description. Explain what the app does and when AI Teammates should use its tools. The AI Teammate uses this description to help determine when to use the MCP server.

### Register Asana with the external service

1.  Sign in to the external service as an admin and register Asana as an app. 
2.  Enable OAuth 2.0, add the callback URL from the Asana developer console as an allowed redirect URL, and select the OAuth scopes the app needs. 
3.  Save the configuration and collect the client ID, client secret, authorization URL, and token exchange URL provided by the external service.

### Configure the external connection

In the app configuration, enter the connection and authentication details provided by the external service. The required fields are:

- **MCP server URL**: The URL of the MCP server provided by the external service. 
- **Authentication type**: We currently support OAuth 2.0. 
- **Client ID**: Enter the client ID received from the external app.
- **Client secret**: Enter the client secret received from the external app.
- **Authorization URL**: Paste your external app’s authorize URL. 
- **Token exchange URL**: Paste your external app’s token exchange URL.

You can also add a **Revocation URL** to revoke tokens when a user disconnects the app. Add **Scopes** as space-separated values when the external service requires them. Click **Save changes** when the configuration is complete.

> External MCP apps cannot be edited after saving, except for the app name and description. To change another parameter, create a separate app. This helps prevent an approved app from changing its scope after distribution.

 

###

### Distribute the app

Open **Distribution** and click + **Add workspace**. Select the workspaces where you want to publish the app. Some workspaces may require an admin to approve the app before it is distributed.

After distribution, the app appears in the AI Teammates app gallery for users in the selected workspaces. Users authenticate with their own credentials when they connect the app. Authentication tokens are not shared between users.

## Connect your custom MCP app to an AI Teammate

An AI Teammate admin or editor can connect the app from the teammate settings. Under **Customize**, click **Apps** and find the custom MCP app in the **Manage Apps** gallery. Add the app to the teammate.

Users of the AI Teammate can use the app after they authenticate with the external service. Each user authorizes the app with their own credentials, and the integration acts on behalf of the user who triggers the AI Teammate.
