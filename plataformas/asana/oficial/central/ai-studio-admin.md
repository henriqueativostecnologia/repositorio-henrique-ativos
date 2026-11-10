---
fonte: https://help.asana.com/s/article/ai-studio-admin?language=en_US
baixado: 2026-11-10
---

# An admin's guide to AI Studio

AI Studio helps your teams automate routine work with smart workflows and allows admins to keep guardrails in place. This guide shows you how to enable the feature, set sensible defaults, manage cost, and troubleshoot common issues, with links to deeper Help Center articles where you need them.

This article is for organization and division admins who manage access, data scope, and usage for AI Studio. Builders can also use it as a quick reference when they want safe defaults and lightweight review steps.

## Before you begin

Confirm that both Asana AI and AI Studio are enabled for your organization or division. Check this in your admin console under Billing \> AI Studio. AI Studio cannot be used if Asana AI is not enabled.

Only super admins can enable or disable Asana AI for your domain. Division admins can disable AI features but cannot enable them unless they complete super admin verification. Learn more in [Asana AI features and admin controls](https://help.asana.com/s/article/asana-ai-features-and-admin-controls).

For more detailed information on availability and billing details, see the overview and pricing pages [Introduction to AI Studio](https://help.asana.com/s/article/ai-studio), [AI Studio add‑on and pricing](https://help.asana.com/s/article/ai-studio-pricing).

## Understanding builder eligibility

Let's go over the differences between AI Studio Basic, AI Studio Plus, and AI Studio Pro.

AI Studio Basic is now part of the core Asana AI experience for all paid plans. All users in the domain can see and use AI Studio, and consume Basic credits. Basic credits are provided free of charge, but there’s a limit on how many can be used per month.

AI Studio Plus offers customers the opportunity to purchase a monthly or annual AI Studio Plus subscription directly in-product which includes 100,000 credits that reset each month, as well as the ability to purchase more credits where required.

If you use AI Studio Pro, you’ll maintain an approved builder list so only those members consume Pro credits. You can review usage regularly and adjust the list as your needs evolve. See detailed information in our article on managing access to AI Studio Pro credits.

Note that guests cannot be builders.

## Managing the AI Studio Pro builder list

If you are using AI Studio Pro, admins can manage who uses Pro credits through the builder list. Members added to the list gain access to Pro credits, while those not on the list continue using AI Studio Basic. There are three ways that admins can grant access to Pro credits:

### Via the AI Studio card in the admin console

1.  In the admin console, click **Billing** on the left navigation bar.
2.  Click the **AI Studio** card.
3.  Ensure you are viewing the **Access** tab.
4.  Click **Add members** to grant access to Pro credits by adding people to the builder list.
5.  Click **Remove** beside any name in the builder list to revoke access to Pro credits.

### Via the Add-ons column in the Members table

1.  In the admin console, click the **Members** tab.
2.  Find the **Add-ons** column in the table. See image below.
3.  Click the **Add-ons** dropdown next to the user you wish to grant access to.
4.  Select **AI Studio Pro** to add them to the Pro builder list.

### Bulk assign via CSV import

1.  Export a CSV of the members via the **CSV export** on the **Members** tab.
2.  Add the term **AI Studio Pro** in the Add-ons column next to anyone you wish to grant access to. Note that the term **AI Studio Pro** is case sensitive. See image below.
3.  Import the CSV via the **CSV import** button in the top-right of the **Members** tab.

### Via SCIM provisioning

Admins can use SCIM to manage the AI Studio Pro builder list at scale. By assigning the “AI Studio” license type through your identity provider's SCIM configuration, members are automatically added to the Pro builder list.

> The “AI Studio” license type only controls which users can build AI Studio automations that draw from the AI Studio Pro credit pool. This license type does not limit which users can use AI Studio basic credits.

For details on accepted license type attributes, see the [SCIM developer documentation](https://developers.asana.com/docs/scim).

For detailed instructions on setting up SCIM provisioning, see [Provisioning and deprovisioning users with SCIM](https://help.asana.com/s/article/provisioning-and-deprovisioning-users-with-scim).

AI Studio is available to all members by default; any users who have not been designated with an AI Studio Pro license will draw from a limited AI Studio Basic credit pool included in your organization's product tier. This Basic credit pool refreshes monthly (see link for more information about AI Studio Basic credits included in each [product tier](https://help.asana.com/s/article/ai-studio-pricing#ai-studio-basic)). If you need to restrict access to AI Studio for specific members, you can create a custom role and turn off the **AI Automations** permission for that role. Members assigned to this custom role will not be able to use AI Studio.

For more information on creating and managing custom roles, see the article on [role-based access control](https://help.asana.com/s/article/role-based-access-control-with-custom-roles).

## Data, privacy, and web access

By default, a workflow can read the task that triggers the rule and the project that houses the rule. Nothing else is visible unless the builder intentionally expands access. Even then, a builder can only provide access to work that they can access themselves. Visit the article [Connect your smart workflow with the right data sources](https://help.asana.com/s/article/ai-studio-connect-your-smart-workflow) for detailed information on managing data scope for smart workflows.

Admins can set their web access policy to match their company’s security posture. They can enable web access in the admin console, and builders can opt to use it on a per workflow basis; note that [web access](https://help.asana.com/s/article/ai-studio-faq#ai-studio-and-web-access) is not available in HIPAA‑compliant workspaces.

Asana and its AI partners do not use your data to train models. Partners delete input and output data after each response. See the [Asana AI FAQ](https://help.asana.com/s/article/asana-ai-faq) and [Trust Center](https://asana.com/trust) for details.

## What drives credit consumption

Each time a smart workflow runs, it consumes credits based on the total content processed and the model’s multiplier. In simple terms, larger inputs/outputs and higher‑cost models use more credits. It makes sense to use lower‑cost models for straightforward tasks. See [model pricing](https://help.asana.com/s/article/ai-studio-pricing#model-pricing) for detailed information on multipliers.

There are four main drivers of credit use: **the model** you choose, the **volume of input data** sent to the model, the **volume of output** the rule generates, and **how often** the rule runs. If the workflow uses web access, each execution also consumes additional credits.

Choose lighter models for classification or short summaries, trim large attachments, cap output length in your instructions, and add conditions so rules run only when inputs are ready. You may also opt to use web access sparingly. Searching and reading URLs adds credit usage per execution, so it makes sense to enable it only in rules where its use changes the outcome.

## Monitor credit spend

If credit usage spikes, open the **Usage** view in the admin console to find the workflow causing the issue, and check the model and/or execution frequency. Data updates every few hours.

You can review AI Studio usage in the admin console under **Billing \> AI Studio \> Usage**. The view shows usage by builder and by workflow, including the model used and [total credits consumed](https://help.asana.com/s/article/ai-studio-pricing#view-ai-studio-usage-data-in-the-admin-console).

Make sure your credits match your demand. Basic and Plus credits reset monthly, while Pro credits are reset quarterly; consult the pricing pages for current details on [AI Studio Plus](https://help.asana.com/s/article/ai-studio-pricing#ai-studio-plus) and [AI Studio Pro](https://help.asana.com/s/article/ai-studio-pricing#ai-studio-pro). Admins receive warnings at 80% and 100% of the credit limit. When credits are exhausted, AI Studio rules stop running and builders receive an email notification.

### Divisions

AI Studio offers division-level credit allocations, enabling Enterprise and Enterprise+ admins to monitor and manage AI Studio credit usage across divisions within their organization. This provides visibility into how credits are being consumed by different divisions and allows admins to set soft limits with notification alerts.

**Credit visibility**

Admins can view AI Studio credit usage broken down by division in the AI Studio usage page within the admin console. This visibility helps track which divisions are consuming credits and at what rate.

Once users are assigned to a division and begin executing AI Studio rules, their usage will appear under that division. Note that usage data does not backfill from before divisions were created.

**Soft limits and notifications**

Admins can set a soft limit for AI Studio Pro credits for each division in their organization. When a division approaches or exceeds its allocated limit, division admins receive email notifications about usage.

Soft limits provide early warning signals without interrupting active workflows. Rules will continue to execute even when limits are exceeded, ensuring critical work is not disrupted unexpectedly.

**How to access division-level credit allocations**

To use division-level credit allocations:

1.  Your organization must be enrolled in the Divisions in Paid Orgs. Set up divisions in your organization either manually or through SCIM integration.
2.  Assign users to divisions.
3.  Navigate to the AI Studio usage page in your admin console to view credit usage by division.
4.  Set soft limits for divisions as needed.

 

#### To set credit allocations for divisions

1.  Navigate to the **admin console**.
2.  Click **Billing** in the left sidebar.
3.  Select **AI Studio**, then click the **Limits** tab.
4.  Click **Set up limits**

In the **Division** drop-down you will see a list of divisions in your organization. From here, you can enter a credit limit for each division. This sets a soft limit. Click **Save** to apply the allocation.

 

## Get your team started quickly

Once you’re comfortable with your setup, we recommend that beginners start with [Words to workflows](https://help.asana.com/s/article/ai-studio-words-to-workflows) and [Pre-built AI rules](https://help.asana.com/s/article/ai-studio-pre-built-ai-rules). Both of these features offer a low barrier to entry while still allowing you to customize your workflows once you are confident with the basics.
