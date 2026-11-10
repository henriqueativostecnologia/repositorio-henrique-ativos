---
fonte: https://help.asana.com/s/article/connect-salesforce-to-ai-teammates-with-a-custom-mcp-app?language=en_US
baixado: 2026-11-10
---

# Connect Salesforce to AI Teammates with a custom MCP app

Asana AI Teammates can connect to Salesforce through a [custom MCP app](https://help.asana.com/s/article/create-custom-mcp-apps-for-ai-teammates). After the connection is configured, an AI teammate can use Salesforce context to support sales and marketing workflows, create work in Asana, and update Salesforce without requiring users to leave Asana.

## What you can do with Salesforce and AI Teammates

Salesforce hosted MCP servers let AI teammates search CRM records and write updates back to Salesforce without requiring SOQL or a report request to operations.

For example, when a deal moves to Closed-Won, an AI teammate can gather the account name, contract value, scope, stakeholders, and target go-live date from Salesforce. It can then create an onboarding project from a template, populate custom fields such as deal size, renewal date, and account tier, add the project to the onboarding portfolio, and assign implementation milestones based on region or workload.

For renewals and QBRs, an AI teammate can find accounts with upcoming renewals and create a preparation project under the Q3 Renewals portfolio. Each task can include usage data, health score, open cases, and a link to the Salesforce record.

For pipeline hygiene, you can ask an AI teammate to find open opportunities over \$250,000 that have had no activity for 30 days. The teammate can create follow-up tasks in the appropriate sales project and update the opportunity in Salesforce when the work is complete.

## Set up Salesforce for AI Teammates

A Salesforce admin and an Asana admin must complete the setup. The process has three parts: create an external app in Salesforce, create the custom app in Asana, and authorize Salesforce for each AI teammate.

### **Create Asana as an external app in Salesforce**

In Salesforce, create an External Client App for Asana.

Set the redirect URL to:

[https://app.asana.com/-/integrations/oauth/callback](https://app.asana.com/-/integrations/oauth/callback)

Add these OAuth scopes:

1.  api
2.  refresh_token
3.  mcp_api

Save the configuration. Salesforce will generate a client ID, client secret, and other URLs. Keep these values available for the Asana setup.

For more information, refer to [Salesforce documentation](https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/create-external-client-app.html) about connecting external services.

### Create the Salesforce app in Asana

In Asana, the Salesforce admin creates a custom app named Salesforce. Follow the [Custom MCP Connection article](https://help.asana.com/s/article/create-custom-mcp-apps-for-ai-teammates) and provide the MCP server URL, client ID, and client secret from the Salesforce configuration.

### Add Salesforce to an AI teammate

After the Salesforce custom app is distributed to your organization, each user can add it to their AI teammate. Each user authorizes the app with their own OAuth grant.

OAuth tokens are not shared between users. Each user must have their own Salesforce access, which keeps queries scoped to that user's Salesforce permissions.
